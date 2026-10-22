"""
Automated validation of FEP-010: Renderer Expansion, Engine Orchestrator, CLI and MCP Server.
"""
import json
from pathlib import Path
from metricsthinking.collector import ProjectCollector
from metricsthinking.evaluator import CriteriaEvaluator
from metricsthinking.scorer import AuditScorer
from metricsthinking.renderer import ReportRenderer
from metricsthinking.engine import run_audit
from metricsthinking.mcp_server import handle_list_tools, handle_call_tool


def test_renderer_materializes_four_artifacts(tmp_path):
    collector = ProjectCollector(target_path=".")
    evidence = collector.collect()
    evaluator = CriteriaEvaluator.load_profile("default", profiles_dir=Path("config/profiles"))
    modules = evaluator.evaluate(evidence)
    scorer = AuditScorer(modules=modules, evidence=evidence, profile_name="default")
    report = scorer.score()

    renderer = ReportRenderer(report)
    md_text = renderer.render_markdown()

    # Check 3 new sections in Markdown
    assert "## 6. EFICIENCIA CONTEXTUAL Y VECTOR ESPECTRAL" in md_text
    assert "## 7. VECTOR DE SEGURIDAD Y SUPERFICIE DE ATAQUE AGÉNTICA" in md_text
    assert "## 8. VECTOR DE RESILIENCIA Y ACOPLAMIENTO DE SISTEMAS" in md_text

    # Write artifacts to tmp_path
    artifacts = renderer.write_artifacts(tmp_path)
    assert Path(artifacts["markdown"]).exists()
    assert Path(artifacts["json"]).exists()
    assert Path(artifacts["roadmap"]).exists()
    assert (Path(report.project_path) / "artifacts" / "plans" / "active" / "CONTEXT_PRUNING_PLAN.json").exists()


def test_engine_run_audit_with_prune_and_medallion(tmp_path):
    report, artifacts = run_audit(
        target_path=".",
        profile_name="default",
        out_dir=str(tmp_path),
        quiet=True,
        prune=True,
        medallion=True,
    )
    assert report.consolidated_score > 0.0
    assert report.fpai is not None
    assert report.security is not None
    assert report.resilience is not None
    assert Path(artifacts["markdown"]).exists()


def test_mcp_server_six_tools():
    tools = handle_list_tools()
    tool_names = [t["name"] for t in tools]

    expected_tools = [
        "audit_project",
        "get_project_score",
        "get_module_evaluation",
        "get_spectral_efficiency",
        "generate_pruning_plan",
        "apply_pruning_plan",
    ]
    for exp in expected_tools:
        assert exp in tool_names, f"Tool {exp} must be exposed in MCP server"


def test_mcp_server_tool_calls():
    # 1. get_project_score
    resp_score = handle_call_tool("get_project_score", {"target": "."})
    assert len(resp_score) == 1
    data_score = json.loads(resp_score[0]["text"])
    assert "consolidated_score" in data_score

    # 2. get_module_evaluation
    resp_mod = handle_call_tool("get_module_evaluation", {"module_id": "M01", "target": "."})
    assert len(resp_mod) == 1
    data_mod = json.loads(resp_mod[0]["text"])
    assert data_mod["module_id"] == "M01"

    # 3. get_spectral_efficiency
    resp_spec = handle_call_tool("get_spectral_efficiency", {"target": "."})
    assert len(resp_spec) == 1
    data_spec = json.loads(resp_spec[0]["text"])
    assert "power_factor_spectral" in data_spec

    # 4. generate_pruning_plan
    resp_prune = handle_call_tool("generate_pruning_plan", {"target": "."})
    assert len(resp_prune) == 1
    data_prune = json.loads(resp_prune[0]["text"])
    assert "total_tokens_recovered" in data_prune
