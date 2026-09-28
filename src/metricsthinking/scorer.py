"""
Scorer and Remediation Planner for MetricsThinking™.
Computes canonical weighted scores, maturity bands, and prioritized technical remediation.
"""

from datetime import datetime
from typing import Any

from .collector import ProjectEvidence
from .models import (
    CanonicalModuleEvaluation,
    DomainArchetype,
    InspectionMode,
    ProjectAuditReport,
    RemediationItem,
)


class AuditScorer:
    """Calculates quantitative metrics and prioritizes remediation actions."""

    def __init__(
        self,
        modules: list[CanonicalModuleEvaluation],
        evidence: ProjectEvidence,
        profile_name: str = "default",
        profile_data: dict[str, Any] | None = None
    ):
        self.modules = modules
        self.evidence = evidence
        self.profile_name = profile_name
        self.profile_data = profile_data or {}

    def score(self) -> ProjectAuditReport:
        """Generates the consolidated ProjectAuditReport."""
        archetype = self._resolve_archetype()
        mode = self._resolve_inspection_mode(archetype)
        remediation_items = self._build_remediation_plan(archetype, mode)

        stats = {
            "total_files_scanned": self.evidence.total_files,
            "seeds_detected": len(self.evidence.seeds),
            "manifests_detected": len(self.evidence.manifests),
            "context_files_detected": len(self.evidence.context_files),
            "schemas_detected": len(self.evidence.schemas),
            "tests_detected": len(self.evidence.tests),
            "source_files_detected": len(self.evidence.source_files),
            "is_git": self.evidence.is_git,
            "domain_archetype": archetype.value,
            "inspection_mode": mode.value,
        }

        report = ProjectAuditReport(
            project_name=self.evidence.project_name,
            project_path=str(self.evidence.root_path),
            audit_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            auditor="MetricsThinking™ Universal Auditor",
            profile_used=self.profile_name,
            domain_archetype=archetype,
            inspection_mode=mode,
            git_commit=self.evidence.git_commit,
            git_branch=self.evidence.git_branch,
            seed_detected=self.evidence.seed_detected,
            seed_version=self.evidence.seed_version,
            evidence_primitives=self.evidence.evidence_primitives,
            modules=self.modules,
            remediation_plan=remediation_items,
            stats=stats
        )

        return report

    def _resolve_archetype(self) -> DomainArchetype:
        """Determines the active DomainArchetype from profile data, seed, or fallback."""
        raw = self.profile_data.get("domain_archetype") or self.evidence.detected_archetype or self.profile_name
        for arch in DomainArchetype:
            if arch.value.lower() == str(raw).lower():
                return arch
        return DomainArchetype.SOFTWARE_ENGINEERING

    def _resolve_inspection_mode(self, archetype: DomainArchetype) -> InspectionMode:
        """Determines the active InspectionMode."""
        raw = self.profile_data.get("inspection_mode") or self.evidence.detected_mode
        if raw:
            for m in InspectionMode:
                if m.value.lower() == str(raw).lower():
                    return m

        # Default mapping based on archetype
        if archetype in [DomainArchetype.GITOPS, DomainArchetype.PLATFORM_ENG, DomainArchetype.CHAOS_ENG]:
            return InspectionMode.DECLARATIVE_CONFIG
        if archetype in [DomainArchetype.MLOPS, DomainArchetype.LLMOPS, DomainArchetype.DATAOPS, DomainArchetype.DATA_PLATFORM]:
            return InspectionMode.PIPELINE_ORCHESTRATION
        if archetype in [DomainArchetype.DEVSECOPS, DomainArchetype.TEAM_TOPOLOGIES, DomainArchetype.SDD]:
            return InspectionMode.GOVERNANCE_SPEC
        if archetype in [DomainArchetype.DUAL_TRACK, DomainArchetype.CUSTOM]:
            return InspectionMode.POLYGLOT_HYBRID
        return InspectionMode.SOURCE_CODE

    def _build_remediation_plan(self, archetype: DomainArchetype, mode: InspectionMode) -> list[RemediationItem]:
        """Prioritizes unfulfilled criteria based on module weight and critical path."""
        remediation_items: list[RemediationItem] = []

        # Find first incomplete module (the bottleneck)
        bottleneck_id = None
        for m in self.modules:
            if m.phase_completion_pct < 100.0:
                bottleneck_id = m.module_id
                break

        for m in self.modules:
            for crit in m.criteria:
                if not crit.fulfilled:
                    # Calculate priority
                    if m.module_id == bottleneck_id or m.weight >= 0.20:
                        priority = "P1"
                    elif m.weight >= 0.10:
                        priority = "P2"
                    else:
                        priority = "P3"

                    action = crit.remediation_hint or f"Implementar y verificar cumplimiento de '{crit.name}'."
                    impact = (m.weight / len(m.criteria)) * 100.0 if m.criteria else 0.0
                    files_to_touch = self._infer_remediation_paths(m.module_id, crit.criterion_id, archetype, mode)

                    remediation_items.append(
                        RemediationItem(
                            priority=priority,
                            module_id=m.module_id,
                            criterion_id=crit.criterion_id,
                            action=action,
                            impact_score=round(impact, 2),
                            files_to_touch=files_to_touch
                        )
                    )

        # Sort by Priority (P1, P2, P3, P4) and descending impact score
        priority_order = {"P1": 1, "P2": 2, "P3": 3, "P4": 4}
        remediation_items.sort(key=lambda item: (priority_order.get(item.priority, 5), -item.impact_score))
        return remediation_items

    def _infer_remediation_paths(
        self,
        module_id: str,
        criterion_id: str,
        archetype: DomainArchetype,
        mode: InspectionMode
    ) -> list[str]:
        """Infers dynamic file paths tailored to the domain archetype."""
        if "M01" in module_id:
            return ["01_seed/seed-ThinkingSeed-master.md", "README.md", "README_ES.md"]

        if "M02" in module_id:
            if archetype == DomainArchetype.GITOPS:
                return ["manifests/", "charts/", "k8s/"]
            if archetype == DomainArchetype.PLATFORM_ENG:
                return ["catalog-info.yaml", "modules/", "templates/"]
            if archetype == DomainArchetype.SDD:
                return ["specs/", "contracts/", "schemas/"]
            if archetype == DomainArchetype.MLOPS:
                return ["models/", "schemas/", "docs/architecture/"]
            if archetype == DomainArchetype.LLMOPS:
                return ["prompts/", "schemas/", "src/"]
            if archetype == DomainArchetype.DEVSECOPS:
                return ["policies/", "security/", "schemas/"]
            return ["schemas/", "docs/notes/ADR-001.md"]

        if "M03" in module_id:
            if archetype in [DomainArchetype.DEVSECOPS, DomainArchetype.GITOPS]:
                return ["policies/", ".pre-commit-config.yaml"]
            if archetype == DomainArchetype.DATAOPS:
                return ["contracts/", "models/"]
            return [".context.yaml", "schemas/"]

        if "M04" in module_id:
            if archetype == DomainArchetype.GITOPS:
                return ["manifests/", "kustomization.yaml", "tests/fixtures/"]
            if archetype == DomainArchetype.LLMOPS:
                return ["prompts/", "configs/", "tests/fixtures/"]
            return ["pyproject.toml", "tests/fixtures/"]

        if "M05" in module_id:
            if archetype == DomainArchetype.GITOPS:
                return ["manifests/", "apps/"]
            if archetype == DomainArchetype.DATAOPS:
                return ["models/", "dbt_project.yml"]
            if archetype == DomainArchetype.MLOPS:
                return ["src/training/", "pipelines/"]
            if archetype == DomainArchetype.SDD:
                return ["specs/", "src/"]
            if archetype == DomainArchetype.CHAOS_ENG:
                return ["chaos/", "experiments/"]
            return ["src/"]

        if "M06" in module_id:
            if archetype == DomainArchetype.GITOPS:
                return ["manifests/overlays/", "charts/"]
            if archetype == DomainArchetype.DEVSECOPS:
                return ["reports/", ".github/workflows/"]
            return ["src/"]

        if "M07" in module_id:
            return ["tests/"]

        if "M08" in module_id:
            if archetype == DomainArchetype.GITOPS:
                return ["dashboards/", "scripts/"]
            return ["src/", "dashboards/"]

        if "M09" in module_id:
            return [".github/workflows/ci.yml"]

        if "M10" in module_id:
            return ["01_seed/", "docs/"]

        return ["src/"]

