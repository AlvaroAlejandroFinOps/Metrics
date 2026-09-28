"""
Tests for MetricsThinking™ v3.0 Universal Archetypes, Profiles, and Primitives.
"""

from pathlib import Path
import pytest
import yaml

from metricsthinking.collector import ProjectCollector, ProjectEvidence
from metricsthinking.evaluator import CriteriaEvaluator
from metricsthinking.models import DomainArchetype, InspectionMode, MaturityBand
from metricsthinking.scorer import AuditScorer
from metricsthinking.engine import run_audit


PROFILES_DIR = Path(__file__).resolve().parent.parent / "config" / "profiles"

ALL_PROFILES = [
    "default",
    "mlops",
    "llmops",
    "dataops",
    "gitops",
    "platform-eng",
    "devsecops",
    "dual-track",
    "team-topologies",
    "chaos-eng",
    "sdd",
    "data-platform",
    "web-app"
]


@pytest.mark.parametrize("profile_name", ALL_PROFILES)
def test_profile_structure_and_weights(profile_name):
    """Verifies that every profile has 10 canonical modules summing to 1.0."""
    profile_file = PROFILES_DIR / f"{profile_name}.yaml"
    assert profile_file.exists(), f"Profile {profile_name}.yaml not found"

    with open(profile_file, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    assert "name" in data
    assert "modules" in data
    modules = data["modules"]
    assert len(modules) == 10, f"Profile {profile_name} does not have exactly 10 modules"

    total_weight = sum(m["weight"] for m in modules)
    assert pytest.approx(total_weight, 0.001) == 1.0, f"Profile {profile_name} weights sum to {total_weight}, expected 1.0"

    # Verify canonical module IDs
    expected_ids = [f"M{i:02d}" for i in range(1, 11)]
    actual_ids = [m["id"] for m in modules]
    assert actual_ids == expected_ids


@pytest.mark.parametrize("profile_name", ALL_PROFILES)
def test_profile_rule_dispatch(profile_name):
    """Verifies that all criteria rules in the profile map to real methods in CriteriaEvaluator."""
    evaluator = CriteriaEvaluator.load_profile(profile_name, PROFILES_DIR)
    evidence = ProjectEvidence(str(Path(__file__).parent))

    for mod in evaluator.profile.get("modules", []):
        for crit in mod.get("criteria", []):
            rule_name = crit.get("rule", "")
            assert hasattr(evaluator, rule_name), f"Rule '{rule_name}' in profile '{profile_name}' is not implemented in CriteriaEvaluator"
            # Execute rule method to verify signature
            method = getattr(evaluator, rule_name)
            res = method(crit, evidence)
            assert res.criterion_id == crit["id"]
            assert res.name == crit["name"]
            assert isinstance(res.fulfilled, bool)


def test_thinking_seed_v3_detection(tmp_path):
    """Verifies that ThinkingSeed v3.0 frontmatter is correctly parsed by ProjectCollector."""
    seed_dir = tmp_path / "01_seed"
    seed_dir.mkdir(parents=True)
    seed_file = seed_dir / "seed-mlops-master.md"
    seed_file.write_text(
        """---
project_name: "TestMLOps"
seed_version: "3.0"
domain_archetype: "mlops"
inspection_mode: "pipeline_orchestration"
version: "1.0.0"
---
# MLOps Architecture
Problem Statement: Predicción de demanda en tiempo real.
Scope: In-Scope: modelos de regresión y clasificación.
""",
        encoding="utf-8"
    )

    collector = ProjectCollector(str(tmp_path))
    evidence = collector.collect()

    assert evidence.seed_detected is True
    assert evidence.detected_archetype == "mlops"
    assert evidence.detected_mode == "pipeline_orchestration"
    assert evidence.seed_version == "3.0"


def test_universal_evidence_primitives(tmp_path):
    """Verifies that files are classified into universal primitives."""
    # Create config primitive
    (tmp_path / "config").mkdir()
    (tmp_path / "config" / "settings.yaml").write_text("env: prod", encoding="utf-8")

    # Create spec primitive
    (tmp_path / "schemas").mkdir()
    (tmp_path / "schemas" / "model.schema.json").write_text("{}", encoding="utf-8")

    # Create pipeline primitive
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    (tmp_path / ".github" / "workflows" / "ci.yml").write_text("name: CI", encoding="utf-8")

    # Create verification primitive
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_app.py").write_text("def test_ok(): pass", encoding="utf-8")

    # Create implementation primitive
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "core.py").write_text("def run(): pass", encoding="utf-8")

    collector = ProjectCollector(str(tmp_path))
    evidence = collector.collect()

    assert "config" in evidence.evidence_primitives
    assert evidence.evidence_primitives["config"].file_count >= 1
    assert "spec" in evidence.evidence_primitives
    assert evidence.evidence_primitives["spec"].file_count >= 1
    assert "pipeline" in evidence.evidence_primitives
    assert evidence.evidence_primitives["pipeline"].file_count >= 1
    assert "verification" in evidence.evidence_primitives
    assert evidence.evidence_primitives["verification"].file_count >= 1
    assert "implementation" in evidence.evidence_primitives
    assert evidence.evidence_primitives["implementation"].file_count >= 1
