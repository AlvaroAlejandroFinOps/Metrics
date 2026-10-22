"""
Automated validation of FEP-005: Drift Auditor and Reversible Compensation/Pruning.
"""
from pathlib import Path
from metricsthinking.fpai.drift_auditor import audit_seed_to_code_drift
from metricsthinking.fpai.compensation import (
    generate_pruning_plan,
    apply_pruning_plan,
    PRUNE_START_MARKER,
    PRUNE_END_MARKER,
)


def test_seed_to_code_drift_detection(tmp_path):
    seed_file = tmp_path / "seed-test.md"
    seed_file.write_text(
        "# Seed\n"
        "Key files:\n"
        "- `src/metricsthinking/engine.py`\n"
        "- `src/metricsthinking/models.py`\n"
        "- `src/metricsthinking/missing_file.py`\n",
        encoding="utf-8",
    )

    repo_files = {
        "src/metricsthinking/engine.py": "code",
        "src/metricsthinking/models.py": "code",
        "src/metricsthinking/undocumented.py": "code",
    }

    result = audit_seed_to_code_drift(str(seed_file), repo_files)
    assert result["drift_detected"] is True
    assert "src/metricsthinking/missing_file.py" in result["missing_files"]
    assert "src/metricsthinking/undocumented.py" in result["undocumented_files"]
    assert 0.0 < result["drift_score"] <= 1.0


def test_pruning_plan_generation():
    dead = ["src/unused.py"]
    redundant = ["src/dup.py"]
    structural = ["config/conflict.yaml"]
    sizes = {"src/unused.py": 800, "src/dup.py": 400, "config/conflict.yaml": 200}

    plan = generate_pruning_plan(
        target_path=".",
        dead_files=dead,
        redundant_files=redundant,
        structural_files=structural,
        file_sizes=sizes,
    )

    assert len(plan.items) == 3
    assert plan.total_tokens_recovered == (800 // 4) + (400 // 4) + (200 // 4)
    assert all(item.reversible for item in plan.items)


def test_apply_pruning_plan_reversibility(tmp_path):
    agentignore = tmp_path / ".agentignore"
    agentignore.write_text("existing_rule_1\nexisting_rule_2\n", encoding="utf-8")

    plan = generate_pruning_plan(
        target_path=str(tmp_path),
        dead_files=["dead.py"],
        redundant_files=[],
        structural_files=[],
        file_sizes={"dead.py": 400},
    )

    res = apply_pruning_plan(plan, repo_root=str(tmp_path), update_agentignore=True)
    assert res["status"] == "APPLIED"

    updated = agentignore.read_text(encoding="utf-8")
    assert "existing_rule_1" in updated
    assert "existing_rule_2" in updated
    assert PRUNE_START_MARKER in updated
    assert "dead.py" in updated
    assert PRUNE_END_MARKER in updated

    # Idempotent re-run with new item
    plan2 = generate_pruning_plan(
        target_path=str(tmp_path),
        dead_files=["other.py"],
        redundant_files=[],
        structural_files=[],
        file_sizes={"other.py": 200},
    )
    apply_pruning_plan(plan2, repo_root=str(tmp_path), update_agentignore=True)

    updated2 = agentignore.read_text(encoding="utf-8")
    assert "existing_rule_1" in updated2
    assert "other.py" in updated2
    assert "dead.py" not in updated2  # Replaced cleanly inside marker block
    assert updated2.count(PRUNE_START_MARKER) == 1
