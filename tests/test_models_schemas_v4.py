"""
Automated validation of FEP-002: Unified Models and JSON Schemas v4.0.
"""
import json
from pathlib import Path
import jsonschema
from metricsthinking import (
    AuditCriterion,
    CanonicalModuleEvaluation,
    ContextPruningPlan,
    DomainArchetype,
    FPAISpectralVector,
    InspectionMode,
    ProjectAuditReport,
    PruningActionItem,
    RemediationItem,
    SecurityVulnerabilityReport,
    SystemsResilienceReport,
)


def test_models_instantiation():
    fpai = FPAISpectralVector(
        p_active=1000.0,
        q_dead=200.0,
        q_dup=100.0,
        d_structural=50.0,
        s_spectral=1025.91,
        s_linear=1350.0,
        divergence_ratio=0.24,
        power_factor_spectral=0.974,
        power_factor_linear=0.74,
        active_ratio=0.74,
        dead_ratio=0.148,
        redundant_ratio=0.074,
        distortion_ratio=0.037,
        calibration_state="DETERMINISTIC",
        gain_coefficient=1.0,
    )
    assert fpai.p_active == 1000.0
    assert fpai.power_factor_spectral > 0.9

    sec = SecurityVulnerabilityReport(
        shannon_entropy_max=3.8,
        entropy_findings=[],
        pii_matches_count=0,
        pii_findings=[],
        prompt_injection_surface_count=0,
        prompt_injection_findings=[],
        supply_chain_lockfile_pinned=True,
        attack_surface_index=5.0,
    )
    assert sec.shannon_entropy_max == 3.8

    res = SystemsResilienceReport(
        afferent_coupling_ca={"pkg.a": 2},
        efferent_coupling_ce={"pkg.a": 1},
        instability_i={"pkg.a": 0.33},
        spof_nodes=["pkg.critical"],
        resilience_patterns_count={"timeout": 5, "retry": 3},
        resilience_coverage_ratio=0.85,
    )
    assert res.resilience_coverage_ratio == 0.85

    prune_item = PruningActionItem(
        file_path="src/unused.py",
        line_count=45,
        token_estimate=350,
        pruning_type="Q_DEAD",
        sha256_before="abc12345",
        justification="Zero afferent imports and not declared in seed",
        reversible=True,
    )
    prune_plan = ContextPruningPlan(
        target_path=".",
        items=[prune_item],
        total_tokens_recovered=350,
        active_tokens_remaining=1000,
        power_factor_target=0.85,
        generated_at="2026-10-21T18:00:00Z",
    )
    assert prune_plan.total_tokens_recovered == 350

    crit = AuditCriterion(
        criterion_id="M01-C01",
        name="Architecture DNA Seed Present",
        fulfilled=True,
        evidence_path="01_seed/seed-metricsthinking-master.md",
        evidence_detail="Seed verified",
    )
    mod = CanonicalModuleEvaluation(
        module_id="M01",
        name="Architecture & Governance DNA",
        weight=0.10,
        criteria=[crit],
    )
    # 10 canonical modules
    modules = [mod] + [
        CanonicalModuleEvaluation(
            module_id=f"M0{i}" if i < 10 else f"M{i}",
            name=f"Module {i}",
            weight=0.10,
            criteria=[crit],
        )
        for i in range(2, 11)
    ]

    report = ProjectAuditReport(
        project_name="TestProject",
        project_path=".",
        audit_date="2026-10-21",
        profile_used="default",
        domain_archetype=DomainArchetype.SOFTWARE_ENGINEERING,
        inspection_mode=InspectionMode.SOURCE_CODE,
        modules=modules,
        fpai=fpai,
        security=sec,
        resilience=res,
        pruning_plan=prune_plan,
    )

    assert report.fpai is not None
    assert report.security is not None
    assert report.resilience is not None
    assert report.pruning_plan is not None

    # Validate against JSON schema
    schema_path = Path("schemas/project_audit_report.schema.json")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    report_dict = json.loads(report.model_dump_json())
    # Add computed properties for schema validation
    report_dict["consolidated_score"] = report.consolidated_score
    report_dict["maturity_band"] = report.maturity_band.value
    report_dict["active_bottleneck"] = report.active_bottleneck
    jsonschema.validate(instance=report_dict, schema=schema)


def test_fpai_manifest_and_telemetry_schemas_valid():
    manifest_schema_path = Path("schemas/repo_fpai_manifest.v2.json")
    telemetry_schema_path = Path("schemas/telemetry_event.v2.json")

    assert manifest_schema_path.exists()
    assert telemetry_schema_path.exists()

    manifest_schema = json.loads(manifest_schema_path.read_text(encoding="utf-8"))
    telemetry_schema = json.loads(telemetry_schema_path.read_text(encoding="utf-8"))

    # Validate that both schemas themselves are valid Draft 2020-12 / Draft 7 schemas
    jsonschema.Draft202012Validator.check_schema(manifest_schema)
    jsonschema.Draft7Validator.check_schema(telemetry_schema)
