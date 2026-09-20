"""Unit tests for ReportRenderer."""
from pathlib import Path

from metricsthinking.models import (
    AuditCriterion,
    CanonicalModuleEvaluation,
    ProjectAuditReport,
)
from metricsthinking.renderer import ReportRenderer


def test_renderer_mermaid_syntax(tmp_path: Path):
    crit = AuditCriterion(
        criterion_id="M01-C01",
        name="Specs",
        fulfilled=True,
        evidence_path="README.md",
        evidence_detail="Found",
        remediation_hint="None",
    )

    modules = [
        CanonicalModuleEvaluation(
            module_id=f"M{i:02d}",
            name=f"Module {i}",
            weight=0.10,
            stage_group="Core",
            criteria=[crit],
        )
        for i in range(1, 11)
    ]

    report = ProjectAuditReport(
        project_name="TestProject",
        project_path=str(tmp_path),
        audit_date="2026-09-20 00:00:00",
        auditor="MetricsThinking™ Universal Auditor",
        profile_used="default",
        modules=modules,
        remediation_plan=[],
        stats={"total_files_scanned": 5},
    )

    renderer = ReportRenderer(report)
    md_content = renderer.render_markdown()

    assert "flowchart LR" in md_content
    assert "classDef done" in md_content
    assert "classDef backlog" in md_content
    assert "SUMMARY" in md_content


def test_renderer_generates_markdown_and_roadmap(tmp_path: Path):
    crit = AuditCriterion(
        criterion_id="M01-C01",
        name="Specs",
        fulfilled=True,
        evidence_path="README.md",
        evidence_detail="Found",
        remediation_hint="None",
    )

    modules = [
        CanonicalModuleEvaluation(
            module_id=f"M{i:02d}",
            name=f"Module {i}",
            weight=0.10,
            stage_group="Core",
            criteria=[crit],
        )
        for i in range(1, 11)
    ]

    report = ProjectAuditReport(
        project_name="CompleteProject",
        project_path=str(tmp_path),
        audit_date="2026-09-20 00:00:00",
        auditor="MetricsThinking™ Universal Auditor",
        profile_used="default",
        modules=modules,
        remediation_plan=[],
        stats={"total_files_scanned": 20},
    )

    renderer = ReportRenderer(report)
    md_content = renderer.render_markdown()
    roadmap_content = renderer.render_inferred_roadmap()

    assert "# METRICSTHINKING™: Auditoría Forense y Madurez del Proyecto" in md_content
    assert "100.0%" in md_content

    assert "# INFERRED OPERATIONAL ROADMAP: COMPLETEPROJECT" in roadmap_content
    assert "M01: Module 1" in roadmap_content

    # Test writing artifacts
    out_dir = tmp_path / "artifacts"
    written = renderer.write_artifacts(out_dir)
    assert written["markdown"].exists()
    assert written["json"].exists()
    assert written["roadmap"].exists()


def test_golden_snapshot_regression():
    golden_file = Path(__file__).parent / "fixtures" / "sample_golden_audit.json"
    assert golden_file.exists()
    content = golden_file.read_text(encoding="utf-8")
    assert "GoldenProject" in content
    assert "Excelencia Operativa" in content

