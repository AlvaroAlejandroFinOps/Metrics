# METRICSTHINKING™: Reusable Engine Technical Blueprint

**Documento:** Especificación de Arquitectura de Software para el Motor Evaluador  
**Versión:** `1.0.0-ENTERPRISE`  
**Autor:** Google Antigravity Agent  
**Ubicación:** `artifacts/plans/metricsthinking/02_REUSABLE_ENGINE_BLUEPRINT.md`  

---

## 1. VISIÓN DE LA HERRAMIENTA AUTOMATIZADA

Para escalar MetricsThinking a cualquier repositorio de software, ciencia de datos o infraestructura, el marco se implementará como un paquete CLI y módulo de Python extensible:

```bash
# Ejemplo de invocación universal
metricsthinking audit --target ./my-project --seed ./01_seed/seed.md --format markdown --out artifacts/MetricsThinking.md
```

El motor realiza inspección estática del repositorio, ejecuta suites de prueba no destructivas, valida esquemas JSON y sintetiza el reporte de auditoría completo con diagramas Mermaid integrados.

---

## 2. MODELO DE DATOS Y CONTRATOS (PYDANTIC V2)

```python
from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class ModuleStatus(str, Enum):
    COMPLETE = "complete"      # 100% cumplido (#2ECC71)
    IN_PROGRESS = "inprogress"  # 1% - 99% cumplido (#3498DB)
    PENDING = "pending"        # 0% cumplido (#7F8C8D)
    BLOCKED = "blocked"        # Bloqueado por dependencias (#E74C3C)

class MaturityBand(str, Enum):
    INITIAL_RISK = "Fase Inicial / Riesgo Alto (0.0% - 49.9%)"
    CONSTRUCTION = "Construcción / Fase Media (50.0% - 74.9%)"
    ADVANCED_MATURITY = "Madurez Avanzada / Pre-producción (75.0% - 89.9%)"
    OPERATIONAL_EXCELLENCE = "Producción / Excelencia Operativa (90.0% - 100.0%)"

class AuditCriterion(BaseModel):
    criterion_id: str = Field(..., description="Identificador único (e.g. M01-C01)")
    name: str = Field(..., description="Nombre del criterio")
    fulfilled: bool = Field(..., description="Estado binario de cumplimiento")
    evidence_path: Optional[str] = Field(None, description="Ruta relativa de archivo de evidencia")
    evidence_detail: str = Field(..., description="Detalle comprobado en la inspección")

class CanonicalModuleEvaluation(BaseModel):
    module_id: str = Field(..., description="M01 a M10")
    name: str = Field(..., description="Nombre canónico del módulo")
    weight: float = Field(..., description="Peso relativo W_i (ej: 0.25 para 25%)")
    criteria: List[AuditCriterion]
    
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
            return ModuleStatus.COMPLETE
        elif self.phase_completion_pct > 0.0:
            return ModuleStatus.IN_PROGRESS
        return ModuleStatus.PENDING

class ProjectAuditReport(BaseModel):
    project_name: str
    project_version: str
    audit_date: str
    auditor: str
    git_commit: str
    git_branch: str
    modules: List[CanonicalModuleEvaluation]
    
    @property
    def consolidated_score(self) -> float:
        return sum(m.weighted_contribution_pct for m in self.modules)
    
    @property
    def maturity_band(self) -> MaturityBand:
        score = self.consolidated_score
        if score >= 90.0:
            return MaturityBand.OPERATIONAL_EXCELLENCE
        elif score >= 75.0:
            return MaturityBand.ADVANCED_MATURITY
        elif score >= 50.0:
            return MaturityBand.CONSTRUCTION
        return MaturityBand.INITIAL_RISK
    
    @property
    def active_bottleneck(self) -> Optional[str]:
        for m in self.modules:
            if m.phase_completion_pct < 100.0:
                return f"{m.module_id}: {m.name} ({m.phase_completion_pct:.1f}% completado)"
        return "Ninguno. Todos los módulos canónicos se encuentran al 100%."
```

---

## 3. ARQUITECTURA DE INSPECCIÓN FORENSE (PLUGINS)

El motor automatizado opera en 4 fases desacopladas:
1. **Collector**: Recolecta árbol de archivos, lee `pyproject.toml`, parsea ThinkingSeeds y ejecuta `pytest --json-report`.
2. **Evaluator**: Aplica la matriz de criterios binarios según el perfil del proyecto (Data/Compiler, Web, Cloud).
3. **Scorer**: Calcula matemáticamente las contribuciones ponderadas y determina el cuello de botella.
4. **Renderer**: Genera:
   - Reporte Markdown interactivo (`MetricsThinking.md`).
   - Diagrama de flujo Mermaid con codificación de colores estandarizada.
   - Resumen JSON para integración con dashboards corporativos de FinOps / Data Governance.
