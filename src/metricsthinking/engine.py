"""
MetricsThinking™ Engine & Orchestrator.
Universal Project Auditor executing Ground Truth forensic inspection.
"""

from pathlib import Path

from .collector import ProjectCollector
from .evaluator import CriteriaEvaluator
from .models import ProjectAuditReport
from .renderer import ReportRenderer
from .scorer import AuditScorer


def run_audit(
    target_path: str = ".",
    profile_name: str = "default",
    out_dir: str | None = None,
    prefix: str = "MetricsThinking",
    quiet: bool = False
) -> tuple[ProjectAuditReport, dict[str, Path]]:
    """Executes full 4-phase MetricsThinking™ audit."""
    target = Path(target_path).resolve()
    if not target.exists():
        raise FileNotFoundError(f"Target path '{target}' does not exist.")

    # Find profiles directory: check config/profiles in target or package root
    pkg_dir = Path(__file__).resolve().parent
    repo_root = pkg_dir.parent.parent
    profiles_candidates = [
        target / "config" / "profiles",
        repo_root / "config" / "profiles",
        pkg_dir / "profiles"
    ]
    profiles_dir = None
    for cand in profiles_candidates:
        if cand.exists():
            profiles_dir = cand
            break

    out_path = target / "artifacts" if not out_dir else Path(out_dir).resolve()

    if not quiet:
        print("[*] Starting MetricsThinking™ Audit...")
        print(f"    - Target:  {target}")
        print(f"    - Profile: {profile_name}")
        print(f"    - Output:  {out_path}")
        print(f"    - Prefix:  {prefix}")

    # Phase 1: Collect
    collector = ProjectCollector(str(target))
    evidence = collector.collect()
    if not quiet:
        print(f"    - Scanned: {evidence.total_files} files in repository")

    # Phase 2: Evaluate
    evaluator = CriteriaEvaluator.load_profile(profile_name, profiles_dir)
    modules = evaluator.evaluate(evidence)

    # Phase 3: Score
    scorer = AuditScorer(modules, evidence, profile_name=profile_name)
    report = scorer.score()

    # Phase 4: Render & Write
    renderer = ReportRenderer(report)
    artifacts = renderer.write_artifacts(out_path, filename_prefix=prefix)

    if not quiet:
        print("\n" + "=" * 70)
        print(f"  METRICSTHINKING™ AUDIT RESULTS: {report.project_name.upper()}")
        print("=" * 70)
        print(f"  Consolidated Score: {report.consolidated_score:.2f}% / 100.0%")
        print(f"  Maturity Band:      {report.maturity_band.value}")
        print(f"  Active Bottleneck:  {report.active_bottleneck}")
        print("-" * 70)
        print(f"  {'ID':<5} {'Módulo':<38} {'Peso':<8} {'% Fase':<10} {'Estado':<10}")
        print("-" * 70)
        for m in report.modules:
            pct_str = f"{m.phase_completion_pct:.1f}%"
            weight_str = f"{m.weight*100:.0f}%"
            print(f"  {m.module_id:<5} {m.name[:36]:<38} {weight_str:<8} {pct_str:<10} {m.status.value:<10}")
        print("=" * 70)
        print("[+] Artifacts written successfully:")
        print(f"    - Executive Report: {artifacts['markdown']}")
        print(f"    - Audit Telemetry:  {artifacts['json']}")
        print(f"    - Inferred Roadmap: {artifacts['roadmap']}")

    return report, artifacts
