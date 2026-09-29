"""
MetricsThinking™ Engine & Orchestrator.
Universal Project Auditor executing Ground Truth forensic inspection.
"""

import sys
from pathlib import Path

# Ensure local directory is in sys.path for standalone script execution
_PKG_DIR = Path(__file__).resolve().parent
if str(_PKG_DIR) not in sys.path:
    sys.path.insert(0, str(_PKG_DIR))

try:
    from metricsthinking.collector import ProjectCollector
    from metricsthinking.evaluator import CriteriaEvaluator
    from metricsthinking.models import ProjectAuditReport
    from metricsthinking.renderer import ReportRenderer
    from metricsthinking.scorer import AuditScorer
except (ImportError, ValueError):
    try:
        from .collector import ProjectCollector
        from .evaluator import CriteriaEvaluator
        from .models import ProjectAuditReport
        from .renderer import ReportRenderer
        from .scorer import AuditScorer
    except (ImportError, ValueError):
        from collector import ProjectCollector
        from evaluator import CriteriaEvaluator
        from models import ProjectAuditReport
        from renderer import ReportRenderer
        from scorer import AuditScorer


PROFILE_ALIASES: dict[str, str] = {
    # Agent skills & AI Context Engineering
    "agent-skill": "agent-skill",
    "agent_skill": "agent-skill",
    "agentskill": "agent-skill",
    "skill": "agent-skill",
    "skills": "agent-skill",
    "ai-skill": "agent-skill",
    "ai_skill": "agent-skill",
    "context-skill": "agent-skill",
    "context-engineering": "agent-skill",
    "context_engineering": "agent-skill",
    "prompt-engineering": "agent-skill",
    "prompt_engineering": "agent-skill",
    "agent": "agent-skill",
    "agents": "agent-skill",
    # Data platform & DataOps
    "data-platform": "data-platform",
    "data_platform": "data-platform",
    "data": "data-platform",
    "lakehouse": "data-platform",
    "medallion": "data-platform",
    "dataops": "dataops",
    # Web app
    "web-app": "web-app",
    "web_app": "web-app",
    "webapp": "web-app",
    "web": "web-app",
    "frontend": "web-app",
    # LLMOps & GenAI
    "llmops": "llmops",
    "llm": "llmops",
    "genai": "llmops",
    "rag": "llmops",
    # MLOps
    "mlops": "mlops",
    "ml": "mlops",
    # GitOps
    "gitops": "gitops",
    "k8s": "gitops",
    "kubernetes": "gitops",
    # Platform engineering
    "platform-eng": "platform-eng",
    "platform": "platform-eng",
    "platform_eng": "platform-eng",
    # DevSecOps
    "devsecops": "devsecops",
    "security": "devsecops",
    "sec": "devsecops",
    # Chaos engineering
    "chaos-eng": "chaos-eng",
    "chaos": "chaos-eng",
    # SDD / Spec-driven
    "sdd": "sdd",
    "api": "sdd",
    "spec": "sdd",
    "spec-driven": "sdd",
    # Dual-track & Team topologies
    "dual-track": "dual-track",
    "agile": "dual-track",
    "team-topologies": "team-topologies",
    "team": "team-topologies",
    # Default
    "software-engineering": "default",
    "software": "default",
    "default": "default",
    "auto": "auto"
}


def resolve_profile_name(hint_or_name: str | None) -> str:
    """Resolves profile names, aliases, or natural language prompts into canonical profile name."""
    if not hint_or_name:
        return "default"

    clean = hint_or_name.strip().lower()

    # Direct match in aliases
    if clean in PROFILE_ALIASES:
        return PROFILE_ALIASES[clean]

    # Natural language pattern matching (e.g. "evalua este proyecto como una skill para IA")
    if any(k in clean for k in ["skill", "habilidad", "agente", "agent", "prompt", "context engineering", "thinkingseed"]):
        return "agent-skill"
    if any(k in clean for k in ["lakehouse", "data platform", "plataforma de datos", "dbt", "bigquery", "medallion"]):
        return "data-platform"
    if any(k in clean for k in ["dataops", "calidad de datos", "contratos de datos"]):
        return "dataops"
    if any(k in clean for k in ["web app", "web", "frontend", "react", "nextjs", "vite", "ui"]):
        return "web-app"
    if any(k in clean for k in ["llmops", "genai", "rag", "langchain", "llamaindex", "guardrails"]):
        return "llmops"
    if any(k in clean for k in ["mlops", "machine learning", "modelo ml", "model registry"]):
        return "mlops"
    if any(k in clean for k in ["gitops", "kubernetes", "k8s", "helm", "argo"]):
        return "gitops"
    if any(k in clean for k in ["platform eng", "plataforma", "backstage", "developer portal", "iac"]):
        return "platform-eng"
    if any(k in clean for k in ["devsecops", "seguridad", "security", "sast", "sbom"]):
        return "devsecops"
    if any(k in clean for k in ["chaos eng", "caos", "resiliencia", "fault injection"]):
        return "chaos-eng"
    if any(k in clean for k in ["sdd", "spec-driven", "openapi", "swagger", "api first"]):
        return "sdd"
    if any(k in clean for k in ["dual-track", "discovery", "hipotesis"]):
        return "dual-track"
    if any(k in clean for k in ["team topologies", "topologias de equipo"]):
        return "team-topologies"

    return clean


def run_audit(
    target_path: str = ".",
    profile_name: str = "default",
    archetype: str | None = None,
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

    # If archetype is explicitly passed, use it as profile name, resolving aliases and natural language hints
    raw_profile = archetype if archetype else profile_name
    effective_profile = resolve_profile_name(raw_profile)

    out_path = target / "artifacts" if not out_dir else Path(out_dir).resolve()

    if not quiet:
        print("[*] Starting MetricsThinking™ Audit v3.0...")
        print(f"    - Target:    {target}")
        print(f"    - Profile:   {effective_profile}")
        print(f"    - Output:    {out_path}")
        print(f"    - Prefix:    {prefix}")

    # Phase 1: Collect
    collector = ProjectCollector(str(target))
    evidence = collector.collect()
    if not quiet:
        print(f"    - Scanned:   {evidence.total_files} files in repository")

    # Auto-detect archetype from seed/evidence if profile is default/auto
    if (effective_profile in ["default", "auto"]) and evidence.detected_archetype:
        detected = resolve_profile_name(evidence.detected_archetype)
        # Verify if profile exists
        if profiles_dir and (profiles_dir / f"{detected}.yaml").exists():
            effective_profile = detected
            if not quiet:
                print(f"    - Auto-detected Profile from Repository/Seed: {effective_profile}")

    # Phase 2: Evaluate
    evaluator = CriteriaEvaluator.load_profile(effective_profile, profiles_dir)
    modules = evaluator.evaluate(evidence)

    # Phase 3: Score
    scorer = AuditScorer(
        modules,
        evidence,
        profile_name=effective_profile,
        profile_data=evaluator.profile
    )
    report = scorer.score()

    # Phase 4: Render & Write
    renderer = ReportRenderer(report)
    artifacts = renderer.write_artifacts(out_path, filename_prefix=prefix)

    if not quiet:
        print("\n" + "=" * 75)
        print(f"  METRICSTHINKING™ AUDIT RESULTS: {report.project_name.upper()}")
        print(f"  Archetype: {report.domain_archetype.value} | Mode: {report.inspection_mode.value}")
        print("=" * 75)
        print(f"  Consolidated Score: {report.consolidated_score:.2f}% / 100.0%")
        print(f"  Maturity Band:      {report.maturity_band.value}")
        print(f"  Active Bottleneck:  {report.active_bottleneck}")
        print("-" * 75)
        print(f"  {'ID':<5} {'Módulo':<40} {'Peso':<8} {'% Fase':<10} {'Estado':<10}")
        print("-" * 75)
        for m in report.modules:
            pct_str = f"{m.phase_completion_pct:.1f}%"
            weight_str = f"{m.weight*100:.0f}%"
            print(f"  {m.module_id:<5} {m.name[:38]:<40} {weight_str:<8} {pct_str:<10} {m.status.value:<10}")
        print("=" * 75)
        print("[+] Artifacts written successfully:")
        print(f"    - Executive Report: {artifacts['markdown']}")
        print(f"    - Audit Telemetry:  {artifacts['json']}")
        print(f"    - Inferred Roadmap: {artifacts['roadmap']}")

    return report, artifacts

