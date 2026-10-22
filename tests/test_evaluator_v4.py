"""
Automated validation of FEP-009: Evaluator Expansion (Security, Resilience, Context) and Scorer.
"""
from pathlib import Path
from metricsthinking.collector import ProjectCollector
from metricsthinking.evaluator import CriteriaEvaluator
from metricsthinking.scorer import AuditScorer


def test_v4_evaluation_rules_on_current_repo():
    collector = ProjectCollector(target_path=".")
    evidence = collector.collect()

    evaluator = CriteriaEvaluator.load_profile("default", profiles_dir=Path("config/profiles"))

    # Test 1: Zero Secrets
    c_sec = evaluator.check_security_zero_secrets({"id": "TEST-SEC-1", "name": "Zero Secrets"}, evidence)
    assert c_sec.fulfilled is True
    assert "Zero-Tolerance" in c_sec.evidence_detail

    # Test 2: Entropy Threshold
    c_ent = evaluator.check_security_entropy_threshold({"id": "TEST-SEC-2", "name": "Entropy Threshold"}, evidence)
    assert c_ent.fulfilled is True

    # Test 3: Resilience & SPOF
    c_res1 = evaluator.check_resilience_coupling_and_spof({"id": "TEST-RES-1", "name": "Resilience Coupling"}, evidence)
    assert c_res1.fulfilled is True

    # Test 4: Fault Tolerance Patterns
    c_res2 = evaluator.check_resilience_fault_tolerance_patterns({"id": "TEST-RES-2", "name": "Fault Tolerance"}, evidence)
    assert c_res2.fulfilled is True

    # Test 5: Context Spectral Efficiency
    c_ctx = evaluator.check_context_spectral_efficiency({"id": "TEST-CTX-1", "name": "Spectral Efficiency"}, evidence)
    assert c_ctx.fulfilled is True


def test_scorer_populates_v4_vectors():
    collector = ProjectCollector(target_path=".")
    evidence = collector.collect()
    evaluator = CriteriaEvaluator.load_profile("default", profiles_dir=Path("config/profiles"))
    modules = evaluator.evaluate(evidence)

    scorer = AuditScorer(modules=modules, evidence=evidence, profile_name="default")
    report = scorer.score()

    assert report.fpai is not None
    assert report.fpai.power_factor_spectral > 0.70
    assert report.security is not None
    assert report.security.supply_chain_lockfile_pinned is True
    assert report.resilience is not None
    assert report.pruning_plan is not None
