"""
Calibration and Archetype Precision Tests for MetricsThinking™ v3.0.
"""

from pathlib import Path
import pytest

from metricsthinking.collector import ProjectCollector
from metricsthinking.evaluator import CriteriaEvaluator
from metricsthinking.models import DomainArchetype, InspectionMode, MaturityBand
from metricsthinking.scorer import AuditScorer
from metricsthinking.engine import run_audit

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES_DIR = REPO_ROOT / "config" / "profiles"


def test_self_audit_with_sdd_profile():
    """Verifies that MetricsThinking auditing itself under SDD profile scores in pre-prod/excellence."""
    report, artifacts = run_audit(
        target_path=str(REPO_ROOT),
        profile_name="sdd",
        quiet=True
    )

    assert report.domain_archetype == DomainArchetype.SDD
    assert report.inspection_mode == InspectionMode.GOVERNANCE_SPEC
    # Self audit score should be high given schemas, tests, ci, seed, CLI
    assert report.consolidated_score >= 80.0, f"Expected self audit score >= 80.0%, got {report.consolidated_score}%"
    assert report.maturity_band in [MaturityBand.ADVANCED_MATURITY, MaturityBand.OPERATIONAL_EXCELLENCE]
    assert artifacts["markdown"].exists()
    assert artifacts["json"].exists()
    assert artifacts["roadmap"].exists()


def test_gitops_synthetic_repo_calibration(tmp_path):
    """Calibrates GitOps evaluation on a declarative infrastructure repository."""
    # Create GitOps repository layout
    (tmp_path / "manifests" / "apps").mkdir(parents=True)
    (tmp_path / "manifests" / "apps" / "deployment.yaml").write_text("image: myapp:1.2.3\nsha256:abc123456", encoding="utf-8")
    (tmp_path / "charts" / "myapp").mkdir(parents=True)
    (tmp_path / "charts" / "myapp" / "Chart.yaml").write_text("name: myapp\nversion: 1.0.0", encoding="utf-8")
    (tmp_path / "policies").mkdir()
    (tmp_path / "policies" / "admission.rego").write_text("package admission\ndefault allow = false", encoding="utf-8")
    (tmp_path / "README.md").write_text("# GitOps Platform\nProblem statement: Declarative cluster infra.\nScope: In-Scope: staging & prod clusters.", encoding="utf-8")
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    (tmp_path / ".github" / "workflows" / "ci.yml").write_text("name: CI\non: push", encoding="utf-8")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_manifests.py").write_text("def test_manifests(): pass", encoding="utf-8")

    report, artifacts = run_audit(
        target_path=str(tmp_path),
        profile_name="gitops",
        quiet=True
    )

    assert report.domain_archetype == DomainArchetype.GITOPS
    assert report.inspection_mode == InspectionMode.DECLARATIVE_CONFIG
    # Check that M02 (declarative k8s, policies) evaluated positively
    m02 = next(m for m in report.modules if m.module_id == "M02")
    assert m02.phase_completion_pct > 0.0


def test_mlops_synthetic_repo_calibration(tmp_path):
    """Calibrates MLOps evaluation on an ML project repository."""
    (tmp_path / "01_seed").mkdir()
    (tmp_path / "01_seed" / "seed-mlops.md").write_text(
        "---\ndomain_archetype: mlops\n---\n# MLOps Project\nProblem statement: Churn prediction.\nScope: In-Scope: feature pipeline.",
        encoding="utf-8"
    )
    (tmp_path / "src" / "training").mkdir(parents=True)
    (tmp_path / "src" / "training" / "train.py").write_text("def train_model(): pass", encoding="utf-8")
    (tmp_path / "models").mkdir()
    (tmp_path / "models" / "model_card.md").write_text("# Model Card\nFairness and bias analysis.", encoding="utf-8")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_pipeline.py").write_text("def test_train(): pass", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'mlops'\ndependencies = ['torch>=2.0.0']", encoding="utf-8")

    report, artifacts = run_audit(
        target_path=str(tmp_path),
        profile_name="mlops",
        quiet=True
    )

    assert report.domain_archetype == DomainArchetype.MLOPS
    assert report.inspection_mode == InspectionMode.PIPELINE_ORCHESTRATION
    m01 = next(m for m in report.modules if m.module_id == "M01")
    assert m01.phase_completion_pct == 100.0


def test_llmops_synthetic_repo_calibration(tmp_path):
    """Calibrates LLMOps evaluation on a GenAI / RAG project repository."""
    (tmp_path / "01_seed").mkdir()
    (tmp_path / "01_seed" / "seed-llmops.md").write_text(
        "---\ndomain_archetype: llmops\n---\n# LLMOps RAG Agent\nProblem statement: Customer Support RAG.\nScope: In-Scope: vector retrieval.",
        encoding="utf-8"
    )
    (tmp_path / "prompts").mkdir()
    (tmp_path / "prompts" / "system_prompt.yaml").write_text("system: You are a helpful assistant.", encoding="utf-8")
    (tmp_path / "src" / "rag").mkdir(parents=True)
    (tmp_path / "src" / "rag" / "vector_store.py").write_text("class ChromaVectorStore: pass", encoding="utf-8")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_ragas_evals.py").write_text("def test_faithfulness(): pass", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text("[project]\nname = 'llmops'\ndependencies = ['google-genai>=0.1.0']", encoding="utf-8")

    report, artifacts = run_audit(
        target_path=str(tmp_path),
        profile_name="llmops",
        quiet=True
    )

    assert report.domain_archetype == DomainArchetype.LLMOPS
    assert report.inspection_mode == InspectionMode.PIPELINE_ORCHESTRATION
    # Verify prompt registry and context engineering rules passed
    m02 = next(m for m in report.modules if m.module_id == "M02")
    m04 = next(m for m in report.modules if m.module_id == "M04")
    assert any(c.fulfilled for c in m02.criteria)
    assert any(c.fulfilled for c in m04.criteria)
