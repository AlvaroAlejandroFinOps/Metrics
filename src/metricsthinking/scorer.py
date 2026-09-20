"""
Scorer and Remediation Planner for MetricsThinking™.
Computes canonical weighted scores, maturity bands, and prioritized technical remediation.
"""

from datetime import datetime

from .collector import ProjectEvidence
from .models import (
    CanonicalModuleEvaluation,
    ProjectAuditReport,
    RemediationItem,
)


class AuditScorer:
    """Calculates quantitative metrics and prioritizes remediation actions."""

    def __init__(self, modules: list[CanonicalModuleEvaluation], evidence: ProjectEvidence, profile_name: str = "default"):
        self.modules = modules
        self.evidence = evidence
        self.profile_name = profile_name

    def score(self) -> ProjectAuditReport:
        """Generates the consolidated ProjectAuditReport."""
        remediation_items = self._build_remediation_plan()

        stats = {
            "total_files_scanned": self.evidence.total_files,
            "seeds_detected": len(self.evidence.seeds),
            "manifests_detected": len(self.evidence.manifests),
            "context_files_detected": len(self.evidence.context_files),
            "schemas_detected": len(self.evidence.schemas),
            "tests_detected": len(self.evidence.tests),
            "source_files_detected": len(self.evidence.source_files),
            "is_git": self.evidence.is_git,
        }

        report = ProjectAuditReport(
            project_name=self.evidence.project_name,
            project_path=str(self.evidence.root_path),
            audit_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            auditor="MetricsThinking™ Universal Auditor",
            profile_used=self.profile_name,
            git_commit=self.evidence.git_commit,
            git_branch=self.evidence.git_branch,
            modules=self.modules,
            remediation_plan=remediation_items,
            stats=stats
        )

        return report

    def _build_remediation_plan(self) -> list[RemediationItem]:
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

                    files_to_touch = []
                    if "M01" in m.module_id:
                        files_to_touch = ["01_seed/seed-ThinkingSeed-master.md", "README.md"]
                    elif "M02" in m.module_id:
                        files_to_touch = ["docs/notes/ADR-001.md", "schemas/"]
                    elif "M03" in m.module_id:
                        files_to_touch = [".context.yaml", "schemas/"]
                    elif "M04" in m.module_id:
                        files_to_touch = ["pyproject.toml", "tests/fixtures/"]
                    elif "M05" in m.module_id:
                        files_to_touch = ["src/metricsthinking/"]
                    elif "M06" in m.module_id:
                        files_to_touch = ["src/metricsthinking/renderer.py"]
                    elif "M07" in m.module_id:
                        files_to_touch = ["tests/"]
                    elif "M08" in m.module_id:
                        files_to_touch = ["src/metricsthinking/cli.py"]
                    elif "M09" in m.module_id:
                        files_to_touch = [".github/workflows/ci.yml"]
                    elif "M10" in m.module_id:
                        files_to_touch = ["01_seed/", "docs/"]

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
