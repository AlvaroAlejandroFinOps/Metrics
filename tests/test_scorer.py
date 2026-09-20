"""Unit tests for AuditScorer."""
from pathlib import Path

from metricsthinking.collector import ProjectEvidence
from metricsthinking.models import (
    AuditCriterion,
    CanonicalModuleEvaluation,
    MaturityBand,
    ModuleStatus,
)
from metricsthinking.scorer import AuditScorer


def test_scorer_overall_score_calculation(tmp_path: Path):
    crit_done = AuditCriterion(
        criterion_id="M01-C01",
        name="Test Crit",
        fulfilled=True,
        evidence_path="README.md",
        evidence_detail="Found",
        remediation_hint="None",
    )

    crit_backlog = AuditCriterion(
        criterion_id="M02-C01",
        name="Test Crit 2",
        fulfilled=False,
        evidence_path=None,
        evidence_detail="Missing",
        remediation_hint="Implement",
    )

    modules = [
        CanonicalModuleEvaluation(
            module_id=f"M{i:02d}",
            name=f"Module {i}",
            weight=0.10,
            stage_group="Core",
            criteria=[crit_done if i <= 5 else crit_backlog],
        )
        for i in range(1, 11)
    ]

    evidence = ProjectEvidence(str(tmp_path))
    evidence.total_files = 10
    evidence.is_git = False

    scorer = AuditScorer(modules, evidence, profile_name="default")
    report = scorer.score()

    assert report.consolidated_score == 50.0
    assert sum(1 for m in report.modules if m.status == ModuleStatus.DONE) == 5
    assert sum(1 for m in report.modules if m.status == ModuleStatus.BACKLOG) == 5
    assert report.maturity_band == MaturityBand.CONSTRUCTION
    assert len(report.remediation_plan) > 0
