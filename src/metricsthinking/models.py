"""
Models and Pydantic v2 data contracts for MetricsThinking™ Universal Project Auditor.
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class DomainArchetype(str, Enum):
    SOFTWARE_ENGINEERING = "software-engineering"
    MLOPS = "mlops"
    LLMOPS = "llmops"
    DATAOPS = "dataops"
    GITOPS = "gitops"
    PLATFORM_ENG = "platform-eng"
    DEVSECOPS = "devsecops"
    DUAL_TRACK = "dual-track"
    TEAM_TOPOLOGIES = "team-topologies"
    CHAOS_ENG = "chaos-eng"
    SDD = "sdd"
    DATA_PLATFORM = "data-platform"
    WEB_APP = "web-app"
    AGENT_SKILL = "agent-skill"
    CUSTOM = "custom"


class InspectionMode(str, Enum):
    SOURCE_CODE = "source_code"
    DECLARATIVE_CONFIG = "declarative_config"
    PIPELINE_ORCHESTRATION = "pipeline_orchestration"
    GOVERNANCE_SPEC = "governance_spec"
    POLYGLOT_HYBRID = "polyglot_hybrid"


class EvidencePrimitiveSummary(BaseModel):
    primitive_type: str = Field(..., description="Tipo canónico de evidencia universal (config, spec, pipeline, verification, implementation)")
    file_count: int = Field(0, description="Cantidad de archivos clasificados")
    total_lines: int = Field(0, description="Líneas de código/especificación acumuladas")
    sample_paths: list[str] = Field(default_factory=list, description="Rutas de muestra")
    verified_valid: bool = Field(True, description="Verificación sintáctica o de no-vacío")


class ModuleStatus(str, Enum):
    DONE = "done"          # 100% cumplido (#2ECC71)
    ACTIVE = "active"      # 1% - 99% cumplido (#2196F3)
    BACKLOG = "backlog"    # 0% cumplido (#7F8C8D)
    BLOCKED = "blocked"    # Bloqueado por dependencias (#E74C3C)


class MaturityBand(str, Enum):
    INITIAL_RISK = "Fase Inicial / Riesgo Crítico (0.0% - 49.9%)"
    CONSTRUCTION = "Construcción Activa / Madurez Media (50.0% - 74.9%)"
    ADVANCED_MATURITY = "Madurez Avanzada / Pre-producción (75.0% - 89.9%)"
    OPERATIONAL_EXCELLENCE = "Excelencia Operativa / Producción (90.0% - 100.0%)"


class AuditCriterion(BaseModel):
    criterion_id: str = Field(..., description="Identificador único (e.g. M01-C01)")
    name: str = Field(..., description="Nombre descriptivo del criterio")
    fulfilled: bool = Field(False, description="Estado binario de cumplimiento")
    evidence_path: str | None = Field(None, description="Ruta relativa o identificador de archivo de evidencia")
    evidence_detail: str = Field("Pendiente de evaluación", description="Detalle empírico comprobado en la inspección")
    remediation_hint: str | None = Field(None, description="Acción recomendada en caso de incumplimiento")


class CanonicalModuleEvaluation(BaseModel):
    module_id: str = Field(..., description="Identificador canónico (M01 a M10)")
    name: str = Field(..., description="Nombre del módulo canónico")
    weight: float = Field(..., description="Peso relativo W_i (e.g. 0.25 para 25%)")
    stage_group: str = Field("Core", description="Grupo de etapa en el roadmap (Fundamentos, Construcción, etc.)")
    criteria: list[AuditCriterion] = Field(default_factory=list)

    @property
    def criteria_passed(self) -> int:
        return sum(1 for c in self.criteria if c.fulfilled)

    @property
    def criteria_total(self) -> int:
        return len(self.criteria)

    @property
    def phase_completion_pct(self) -> float:
        if not self.criteria:
            return 0.0
        return (self.criteria_passed / self.criteria_total) * 100.0

    @property
    def weighted_contribution_pct(self) -> float:
        return self.weight * self.phase_completion_pct

    @property
    def status(self) -> ModuleStatus:
        if self.phase_completion_pct >= 100.0:
            return ModuleStatus.DONE
        if self.phase_completion_pct > 0.0:
            return ModuleStatus.ACTIVE
        return ModuleStatus.BACKLOG


class RemediationItem(BaseModel):
    priority: str = Field(..., description="P1 (Crítico/Bloqueante), P2 (Alto ROI), P3 (Maduración), P4 (Pulido)")
    module_id: str
    criterion_id: str
    action: str
    impact_score: float
    files_to_touch: list[str] = Field(default_factory=list)


class ProjectAuditReport(BaseModel):
    project_name: str
    project_path: str
    audit_date: str
    auditor: str = "MetricsThinking™ Universal Auditor"
    profile_used: str = "default"
    domain_archetype: DomainArchetype = DomainArchetype.SOFTWARE_ENGINEERING
    inspection_mode: InspectionMode = InspectionMode.SOURCE_CODE
    git_commit: str | None = None
    git_branch: str | None = None
    seed_detected: bool = False
    seed_version: str | None = None
    evidence_primitives: dict[str, EvidencePrimitiveSummary] = Field(default_factory=dict)
    modules: list[CanonicalModuleEvaluation]
    remediation_plan: list[RemediationItem] = Field(default_factory=list)
    stats: dict[str, Any] = Field(default_factory=dict)

    @property
    def consolidated_score(self) -> float:
        return sum(m.weighted_contribution_pct for m in self.modules)

    @property
    def maturity_band(self) -> MaturityBand:
        score = self.consolidated_score
        if score >= 90.0:
            return MaturityBand.OPERATIONAL_EXCELLENCE
        if score >= 75.0:
            return MaturityBand.ADVANCED_MATURITY
        if score >= 50.0:
            return MaturityBand.CONSTRUCTION
        return MaturityBand.INITIAL_RISK

    @property
    def active_bottleneck(self) -> str:
        for m in self.modules:
            if m.phase_completion_pct < 100.0:
                return f"{m.module_id}: {m.name} ({m.phase_completion_pct:.1f}% completado)"
        return "Ninguno. Todos los módulos canónicos se encuentran al 100%."
