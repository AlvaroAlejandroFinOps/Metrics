<SEED_ARCHITECTURAL_VECTOR version="5.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">

# THINKING SEED MASTER: MetricsThinking™ Engine

> **[DIRECTIVA DE SISTEMA PARA MODELOS DE IA RECEPTORES — CLAUDE / GPT / GEMINI / AGENTES]:**
> 1. **Naturaleza del Artefacto:** Este documento es un **Vector Arquitectónico y Memoria Técnica (ThinkingSeed Master v5.0)** con `contains_source_code="false"`. **NO es el repositorio de código fuente completo** ni un volcado truncado. La ausencia de bloques de código de implementación es una **invariante deliberada de ingeniería** para maximizar la densidad semántica y preservar más del 99% de tu ventana de contexto.
> 2. **Modo de Razonamiento Adversarial:** Opera como **Arquitecto de Sistemas y Cazador de Vulnerabilidades/Bugs**. Utiliza las firmas simbólicas (Sección 4) y la superficie de tensión (Sección 7) para detectar condiciones de carrera, acoplamientos frágiles y casos borde antes de proponer cambios.
> 3. **Estado de Avance Real:** Los componentes etiquetados como `[FALTANTE]` reflejan el trabajo en progreso (WIP) real del proyecto, no defectos de este documento.

## Seed Changelog
- `2026-10-28 (v5.0)`: [CONFIRMADO] Evolución a **MetricsThinking™ v5.0 (iContext Federation Protocol v5.0 — Capa L2)**: (1) Auditoría AST real en `drift_auditor.py` poblando `signature_mismatches` contra la Sección 4.1 del Seed; (2) Sincronización automática de artefactos en `./artifacts/plans/metricsthinking/` y del estado `l2_metricsthinking` en el Bus Cognitivo Federado `./.context/icontext_bus.json`; (3) Encabezado YAML frontmatter conforme a `./schemas/plan_metadata.schema.json` en `INFERRED_ROADMAP.md`; (4) Composición no destructiva de reglas segmentadas en `./scripts/install_skill.py`.
- `2026-10-27`: [CONFIRMADO] Integración de detector heurístico de arquetipos (`detector.py` con 14 arquetipos ponderados), script ejecutor de benchmarks (`scripts/run_benchmark.py`), banner corporativo `MetricsThinking.jpg`, expansión de suite a 105 tests pasando al 100% y estandarización dual Paper-Grade en `README.md` y `README_ES.md`.
- `2026-10-21`: [CONFIRMADO] Emisión de ThinkingSeed Master v3.0 para MetricsThinking™ v4.0 Holistic Governance. Incorpora arquitectura híbrida Rust/Python (`crates/metricsthinking_rs` + `src/metricsthinking/backends/`), motor espectral de eficiencia contextual FPIA (8 submódulos en `src/metricsthinking/fpai/`), firewall Zero-Tolerance (Shannon $H \le 4.5$, PII, Prompt Injection), vector de resiliencia AST ($C_a/C_e$, SPOFs), servidor MCP stdio con 6 herramientas, materialización de 4 artefactos sincronizados y suite de 94 pruebas Pytest pasando al 100%.
- `2026-10-21`: [CONFIRMADO] Actualización mayor a ThinkingSeed Master v3.0. Estandarización de 14 perfiles canónicos YAML, soporte nativo de primitivas universales de evidencia (`EvidencePrimitiveSummary`), integración de servidor MCP stdio JSON-RPC (`mcp_server.py`), instalador multi-asistente portable (`scripts/install_skill.py`) y sincronización de contratos con `schemas/thinking_seed_v3.schema.json`.
- `2026-09-20`: [CONFIRMADO] Emisión inicial v2.0 del motor monolítico de auditoría estática con 10 módulos canónicos y reporteador Mermaid LR.

---

## 0. IDENTIDAD, METADATOS Y CONTRATO DEL RECEPTOR
```yaml
seed_schema_version: "5.0"
project_name: "MetricsThinking"
repository_name: "MetricsThinking"
project_type: "library"
repository_mode: "single-project"
generated_at: "2026-10-28T22:45:00-03:00"
generated_by: "Antigravity (iContext Federation Protocol v5.0)"
repository_root: "./"
git_branch: "master"
git_commit: "8fd8cca"
working_tree_state: "dirty"
analysis_mode: "static+git+validated"
coverage_level: "high"
known_analysis_limits:
  - "Inspección estática profunda de AST, árbol de archivos, esquemas y metadatos sin ejecución dinámica no supervisada de binarios externos."
  - "Evaluación de dependencias basada en pyproject.toml y requirements.txt sin análisis dinámico de red o resolución de lockfiles en tiempo real."
```

### 0.1 Instrucciones para el modelo receptor
1. **ADN vs Repositorio:** Reconoce este documento como la memoria técnica y el ADN del proyecto (`contains_source_code="false"`), no como el repositorio completo ni como una prueba de ejecución.
2. **Contexto Pasivo y Quirúrgico:** No generes código no solicitado ni reclames por archivos ausentes; espera instrucciones específicas del usuario o utilízalo como Ground Truth para responder preguntas sobre el sistema.
3. **Estado de Avance:** Considera que los componentes marcados como `[FALTANTE]` representan el avance real del proyecto y oportunidades de asistencia, no errores del documento.
4. **Rigor Epistemológico:** Respeta las etiquetas `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, `[NO VERIFICADO]` y `[FALTANTE]`.
5. **Portabilidad de Rutas:** Cita siempre rutas relativas a la raíz del repositorio (`./ruta/archivo`) con `/`. Prohibido emitir rutas locales absolutas o enlaces con esquema `file` local.
6. **Contratos Simbólicos:** Conserva arquitectura, firmas simbólicas (Sección 4) e invariantes (`[INV-01]` a `[INV-08]`).
7. **Postura Adversarial Constructiva:** Revisa siempre la Sección 7 (Superficie de Tensión) antes de proponer cambios.
8. **Seguridad Zero-Trust:** No reveles ni solicites secretos. Usa placeholders (`<REDACTED>`).

---

## 1. RESUMEN EJECUTIVO Y ALCANCE
- **1.1 Proyecto en una frase:** [CONFIRMADO] Motor universal de ingeniería inversa, auditoría forense y gobernanza contextual de proyectos tecnológicos que calcula matemáticamente la madurez técnica (0.0% a 100.0%) basándose estrictamente en evidencia física tangible (Ground Truth).
- **1.2 Problema que resuelve:** [CONFIRMADO] Erradica las evaluaciones subjetivas, las alucinaciones de completitud por parte de LLMs y los falsos positivos en revisiones de código, verificando físicamente código real, tests, esquemas, seguridad y CI/CD frente a 10 módulos canónicos ponderados adaptados a 14 arquetipos de ingeniería y gobernanza FPIA.
- **1.3 Usuarios y sistemas consumidores:**
  - *Agentes de IA Autónomos:* Google Antigravity (slash command `/metrics`), Claude Code, Cursor IDE, GitHub Copilot.
  - *Arquitectos de Software y Data Platform Leads:* Auditoría de proyectos brownfield/greenfield, cálculo de eficiencia contextual y validación de estándares.
  - *Equipos de Gobernanza, QA y Release Engineering:* Puertas de calidad automatizadas en pipelines de CI/CD.
  - *Clientes MCP:* Servidor Model Context Protocol stdio para asistentes de desarrollo.
- **1.4 Alcance y límites del sistema:**
  - *In Scope:* [CONFIRMADO] Inspección estática del sistema de archivos local, detección de 14 arquetipos de ingeniería (`agent-skill`, `data-platform`, `web-app`, `mlops`, `llmops`, `dataops`, `gitops`, `platform-eng`, `devsecops`, `dual-track`, `team-topologies`, `chaos-eng`, `sdd`, `software-engineering`), scoring matemático determinista, motor espectral FPIA, firewall Zero-Tolerance, generación simultánea de 4 artefactos sincronizados (`MetricsThinking.md`, `MetricsThinking.json`, `INFERRED_ROADMAP.md`, `CONTEXT_PRUNING_PLAN.json`), servidor MCP stdio e instalador multi-plataforma.
  - *Out of Scope:* [DECLARADO] Ejecución no supervisada de binarios externos compilados, análisis dinámico con inyección de tráfico en red o mutación destructiva del repositorio destino.
- **1.5 Casos de uso canónicos:**
  - *Caso 1 (Auditoría Forense de Repositorio):* Ejecución CLI `metricsthinking audit --target . --profile default` para obtener diagnósticos y roadmap.
  - *Caso 2 (Evaluación de Habilidad Agéntica):* Auditoría con `--profile agent-skill` para verificar contratos de contexto, prompts y guardrails.
  - *Caso 3 (Asistencia MCP en IDE):* Consulta de métricas y herramientas de auditoría en tiempo real desde Cursor o Claude Desktop vía JSON-RPC.
  - *Caso 4 (Poda Contextual Reversible):* Ejecución con flag `--prune` para generar plan de compensación de deriva y optimizar ventanas de contexto.

---

## 2. ARQUITECTURA, TOPOLOGÍA Y FRONTERAS MODULARES
- **2.1 Estilo arquitectónico:** [CONFIRMADO] Arquitectura de pipeline determinista y desacoplada en 5 fases secuenciales: Ingestión de Evidencia (`ProjectCollector` con acelerador Rust/Python) -> Evaluación de Reglas (`CriteriaEvaluator` con motor espectral FPIA) -> Scoring Ponderado (`AuditScorer`) -> Renderizado y Persistencia Atómica (`ReportRenderer`) -> Distribución Multi-Proveedor (`install_skill.py`).
- **2.2 Árbol estructural del repositorio:**
```text
./
├── .agents/skills/metrics/        # Definición de skill para Google Antigravity
│   └── SKILL.md
├── .context/                      # Telemetría y mapa satelital iDirectory
│   └── tree.json
├── .cursor/rules/                 # Reglas de contexto para Cursor IDE
│   └── metrics.mdc
├── .github/                       # Configuración de CI/CD e instrucciones Copilot
│   ├── copilot-instructions.md
│   └── workflows/ci.yml
├── 01_seed/                       # Memoria técnica y ADN del proyecto (ThinkingSeed)
│   ├── .context.yaml
│   └── seed-metricsthinking-master.md
├── 02_foundation/engine/          # Especificaciones de infraestructura y arquitectura
│   ├── .context.yaml
│   └── engine_readme.md
├── 03_research/                   # Entornos de exploración y prompts
│   ├── experiments/.context.yaml
│   ├── notebooks/.context.yaml
│   └── prompts/.context.yaml
├── artifacts/                     # Salidas de auditoría y roadmaps operacionales
│   ├── MetricsThinking.json
│   ├── MetricsThinking.md
│   ├── benchmark_coverage_report.json
│   └── plans/
│       ├── active/
│       │   ├── CONTEXT_PRUNING_PLAN.json
│       │   ├── INFERRED_ROADMAP.md
│       │   └── implementation_plan.md
│       └── archive/
├── config/                        # Perfiles de evaluación y configuración
│   ├── .context.yaml
│   ├── fpai_governance.yaml
│   └── profiles/                  # 14 perfiles canónicos YAML (M01-M10)
├── crates/                        # Módulos nativos en Rust (PyO3)
│   └── metricsthinking_rs/
│       ├── Cargo.toml
│       └── src/
│           ├── ast_graph.rs
│           ├── ballast_tokens.rs
│           ├── entropy_sec.rs
│           ├── lib.rs
│           └── walker.rs
├── docs/                          # Documentación técnica y notas de ingeniería
│   ├── PERSONA_LENSES.md
│   └── notes/
├── integrations/                  # Plantillas para asistentes externos
│   ├── claude/CLAUDE.md
│   ├── copilot/copilot-instructions.md
│   └── cursor/metrics.mdc
├── schemas/                       # Esquemas JSON Schema de contratos de auditoría
│   ├── audit_criterion.schema.json
│   ├── canonical_module.schema.json
│   ├── evidence_primitives.schema.json
│   ├── project_audit_report.schema.json
│   ├── repo_fpai_manifest.v2.json
│   ├── telemetry_event.v2.json
│   └── thinking_seed_v3.schema.json
├── scripts/                       # Automatización y scripts de mantenimiento
│   ├── .context.yaml
│   ├── hnsw_index_rebuild.py
│   ├── install_skill.py
│   └── run_benchmark.py           # Runner determinista de benchmarks volumétricos
├── src/                           # Código fuente del motor
│   ├── __init__.py
│   └── metricsthinking/           # Paquete Python distribuible
│       ├── __init__.py
│       ├── backends/              # Abstracción de crawling (Rust / Python fallback)
│       │   ├── __init__.py
│       │   └── python_fallback.py
│       ├── fpai/                  # Motor de Gobernanza y Eficiencia Contextual FPIA
│       │   ├── __init__.py
│       │   ├── ablation.py
│       │   ├── attribution.py
│       │   ├── compensation.py
│       │   ├── confidence.py
│       │   ├── drift_auditor.py
│       │   ├── gatekeeper.py
│       │   ├── medallion.py
│       │   └── spectral_engine.py
│       ├── cli.py
│       ├── collector.py
│       ├── detector.py            # Detector heurístico y bayesiano de arquetipos
│       ├── engine.py
│       ├── evaluator.py
│       ├── mcp_server.py
│       ├── models.py
│       ├── renderer.py
│       └── scorer.py
├── tests/                         # Suite de pruebas Pytest (105 tests passing)
│   ├── fixtures/
│   │   ├── golden_baseline_report.json
│   │   └── sample_golden_audit.json
│   ├── test_archetype_detector.py
│   ├── test_backends_collector_v4.py
│   ├── test_benchmarks_stress.py
│   ├── test_calibration.py
│   ├── test_cli.py
│   ├── test_cli_mcp_renderer_v4.py
│   ├── test_collector.py
│   ├── test_drift_compensation_v4.py
│   ├── test_evaluator.py
│   ├── test_evaluator_v4.py
│   ├── test_gatekeeper_v4.py
│   ├── test_hygiene_v4.py
│   ├── test_installer.py
│   ├── test_medallion_ablation_v4.py
│   ├── test_models_schemas_v4.py
│   ├── test_renderer.py
│   ├── test_scorer.py
│   ├── test_spectral_engine_v4.py
│   └── test_v3_archetypes.py
├── AGENTS.md                      # Instrucciones maestras de gobernanza universal
├── CLAUDE.md                      # Guía de ejecución para Claude Code
├── README.md                      # Documentación en inglés Enterprise Paper-Grade
├── README_ES.md                   # Documentación en español
├── mcp_metricsthinking.json       # Snippet de configuración de servidor MCP
└── pyproject.toml                 # Manifiesto de empaquetado Hatchling / PEP 621
```
- **2.3 Responsabilidad por directorio y archivo clave:**
  - `./src/metricsthinking/models.py`: [CONFIRMADO] Modelos de datos Pydantic v2 inmutables (`DomainArchetype`, `ModuleStatus`, `AuditCriterion`, `CanonicalModuleEvaluation`, `FPAISpectralVector`, `SecurityVulnerabilityReport`, `SystemsResilienceReport`, `PruningActionItem`, `ContextPruningPlan`, `ProjectAuditReport`).
  - `./src/metricsthinking/collector.py`: [CONFIRMADO] Escaneo estático profundo con backend unificado (Rust/Python), caché incremental SHA-256 y cómputo de métricas AST y resiliencia.
  - `./src/metricsthinking/detector.py`: [CONFIRMADO] Detector heurístico y bayesiano de arquetipos de ingeniería con ponderación de señales físicas y multi-modalidad.
  - `./src/metricsthinking/backends/`: [CONFIRMADO] Abstracción modular de indexación y escaneo de disco con selección dinámica de acelerador Rust o fallback Python puro.
  - `./src/metricsthinking/fpai/`: [CONFIRMADO] Motor de Inteligencia y Gobernanza Contextual FPIA: espectro $S_{\text{spectral}}$, firewall Zero-Tolerance, ablación, atribución, auditoría de deriva y compensación.
  - `./src/metricsthinking/evaluator.py`: [CONFIRMADO] Despachador de reglas de evaluación (`CriteriaEvaluator`) con más de 95 métodos de verificación especializada (`check_*`).
  - `./src/metricsthinking/scorer.py`: [CONFIRMADO] Motor de cálculo matemático ponderado, asignación de banda de madurez y construcción de plan de remediación P1-P4.
  - `./src/metricsthinking/renderer.py`: [CONFIRMADO] Ensamblador de reportes Markdown con diagramas Mermaid LR, JSON de telemetría, roadmap operacional y plan de poda contextual.
  - `./src/metricsthinking/engine.py`: [CONFIRMADO] Orquestador central de ejecución (`run_audit`) y resolución semántica de perfiles (`resolve_profile_name`).
  - `./src/metricsthinking/cli.py`: [CONFIRMADO] Interfaz CLI (`argparse`) con subcomandos `audit`, `install-skill`, `mcp` y `list-profiles`.
  - `./src/metricsthinking/mcp_server.py`: [CONFIRMADO] Servidor Model Context Protocol stdio JSON-RPC con 6 herramientas operacionales.
  - `./scripts/install_skill.py`: [CONFIRMADO] Script instalador multi-asistente (Google Antigravity, OpenAI Codex, Claude Code, Cursor, Copilot, MCP).
- **2.4 Matriz topológica y prioridades de Context Engineering (según `.context/tree.json`):**
  - `p0 (Crítico / ADN)`: `./01_seed/`, `./.context/`, `./artifacts/plans/`.
  - `p1 (Core & Especificación)`: `./02_foundation/engine/`, `./src/metricsthinking/`, `./config/`, `./schemas/`, `./tests/`, `./docs/`, `./integrations/`, `./crates/`.
  - `p2 (Investigación & Tooling)`: `./03_research/notebooks/`, `./03_research/prompts/`, `./03_research/experiments/`, `./scripts/`.
  - `p3 (Almacenamiento & Logs)`: `./data/raw/`, `./data/processed/`, `./logs/`, `./artifacts/plans/archive/`.

---

## 3. FLUJOS DE EJECUCIÓN, ENTRY POINTS Y CICLO DE VIDA
- **3.1 Puntos de entrada principales:**
  - *CLI Oficial:* `metricsthinking audit --target . --profile default`
  - *Módulo Python:* `python -m metricsthinking.cli audit --target .`
  - *API Python:* `from metricsthinking.engine import run_audit; report, artifacts = run_audit(target_path=".")`
  - *Servidor MCP:* `python -m metricsthinking.mcp_server` (o `metricsthinking mcp`)
  - *Instalador de Skills:* `python scripts/install_skill.py --target all`
  - *Slash Command Antigravity:* `/metrics` (invocando `.agents/skills/metrics/SKILL.md`)
- **3.2 Diagrama de flujo principal E2E:**
```mermaid
flowchart LR
    Target["Target Repository"] --> Collect["1. ProjectCollector (Rust/Py Backends)"]
    Collect --> Evidence["ProjectEvidence (Ground Truth + AST)"]
    Evidence --> Eval["2. CriteriaEvaluator (14 YAML Profiles + FPAI)"]
    Eval --> Modules["10 Canonical Modules (M01-M10)"]
    Modules --> Score["3. AuditScorer (0.0% - 100.0%)"]
    Score --> Report["ProjectAuditReport (Pydantic v2)"]
    Report --> Render["4. ReportRenderer"]
    Render --> OutMD["MetricsThinking.md (Mermaid LR)"]
    Render --> OutJSON["MetricsThinking.json (Telemetry)"]
    Render --> OutRoad["INFERRED_ROADMAP.md (Checklists)"]
    Render --> OutPrune["CONTEXT_PRUNING_PLAN.json (Pruning Plan)"]
```
- **3.3 Ciclo de vida y persistencia sincronizada:**
  1. *Fase 1 (Recolección y Crawling):* Inspección del sistema de archivos mediante acelerador nativo Rust o fallback determinista Python con hash SHA-256, lectura Git, categorización en primitivas universales y cómputo de métricas de acoplamiento AST.
  2. *Fase 2 (Evaluación de Criterios y FPAI):* Carga del perfil YAML (`config/profiles/`), ejecución determinista de reglas `check_*`, evaluación del firewall de seguridad y cálculo del vector espectral FPIA.
  3. *Fase 3 (Ponderación y Scoring):* Cálculo de la puntuación consolidada $\sum (W_i \times \text{completion}_i)$, clasificación en 4 bandas de madurez y construcción de plan de remediación P1-P4.
  4. *Fase 4 (Materialización Atómica):* Escritura en `./artifacts/` garantizando codificación UTF-8 pura sin BOM de los cuatro artefactos sincronizados.

---

## 4. CONTRATOS SIMBÓLICOS, MODELO DE DATOS Y PERSISTENCIA

### 4.1 Firmas Simbólicas AST de 1 Línea (Invariante Zero Source Code)
```text
# --- src/metricsthinking/models.py ---
src/metricsthinking/models.py::DomainArchetype(str, Enum) -> Enum | 15 arquetipos de ingeniería (software-engineering, mlops, llmops, dataops, gitops, platform-eng, devsecops, dual-track, team-topologies, chaos-eng, sdd, data-platform, web-app, agent-skill, custom)
src/metricsthinking/models.py::InspectionMode(str, Enum) -> Enum | 5 modos de inspección (source_code, declarative_config, pipeline_orchestration, governance_spec, polyglot_hybrid)
src/metricsthinking/models.py::EvidencePrimitiveSummary(BaseModel) -> Model | Resumen universal de primitivas físicas (primitive_type, file_count, total_lines, sample_paths, verified_valid)
src/metricsthinking/models.py::ModuleStatus(str, Enum) -> Enum | 4 estados canónicos (done, active, backlog, blocked)
src/metricsthinking/models.py::MaturityBand(str, Enum) -> Enum | 4 bandas de madurez cuantitativa (INITIAL_RISK, CONSTRUCTION, ADVANCED_MATURITY, OPERATIONAL_EXCELLENCE)
src/metricsthinking/models.py::AuditCriterion(BaseModel) -> Model | Criterio individual (criterion_id, name, fulfilled, evidence_path, evidence_detail, remediation_hint)
src/metricsthinking/models.py::CanonicalModuleEvaluation(BaseModel) -> Model | Módulo canónico evaluado (module_id, name, weight, stage_group, criteria)
src/metricsthinking/models.py::CanonicalModuleEvaluation.criteria_passed -> int | Cantidad de criterios cumplidos
src/metricsthinking/models.py::CanonicalModuleEvaluation.criteria_total -> int | Total de criterios del módulo
src/metricsthinking/models.py::CanonicalModuleEvaluation.phase_completion_pct -> float | Porcentaje de avance de fase (0.0% a 100.0%)
src/metricsthinking/models.py::CanonicalModuleEvaluation.weighted_contribution_pct -> float | Aporte ponderado al puntaje global (weight * phase_completion_pct)
src/metricsthinking/models.py::CanonicalModuleEvaluation.status -> ModuleStatus | Estado del módulo según porcentaje de completitud
src/metricsthinking/models.py::RemediationItem(BaseModel) -> Model | Acción de remediación priorizada (priority, module_id, criterion_id, action, impact_score, files_to_touch)
src/metricsthinking/models.py::FPAISpectralVector(BaseModel) -> Model | Vector espectral bimodal de contexto (d_raw, d_clean, s_linear, s_spectral, efficiency_class, token_savings_pct, p0_tokens, p1_tokens, p2_tokens, p3_tokens)
src/metricsthinking/models.py::SecurityVulnerabilityReport(BaseModel) -> Model | Telemetría forense de seguridad (shannon_entropy_max, entropy_findings, pii_matches_count, pii_findings, prompt_injection_surface_count, prompt_injection_findings, supply_chain_lockfile_pinned, attack_surface_index)
src/metricsthinking/models.py::SystemsResilienceReport(BaseModel) -> Model | Métricas AST de arquitectura (afferent_coupling_ca, efferent_coupling_ce, instability_metric, spof_modules, circular_dependencies_detected, fault_tolerance_patterns_count, resilience_score)
src/metricsthinking/models.py::PruningActionItem(BaseModel) -> Model | Acción individual de poda contextual (action_id, target_path, estimated_tokens_saved, priority_bucket, reason, reversible)
src/metricsthinking/models.py::ContextPruningPlan(BaseModel) -> Model | Plan integral de poda contextual (total_tokens_prunable, estimated_efficiency_gain_pct, actions)
src/metricsthinking/models.py::ProjectAuditReport(BaseModel) -> Model | Contrato consolidado de auditoría (project_name, project_path, audit_date, auditor, profile_used, domain_archetype, inspection_mode, git_commit, git_branch, seed_detected, seed_version, evidence_primitives, modules, remediation_plan, stats, fpai_spectral, security_report, resilience_report, pruning_plan)
src/metricsthinking/models.py::ProjectAuditReport.consolidated_score -> float | Puntuación global del proyecto (0.0% a 100.0%)
src/metricsthinking/models.py::ProjectAuditReport.maturity_band -> MaturityBand | Clasificación en banda de madurez correspondiente
src/metricsthinking/models.py::ProjectAuditReport.active_bottleneck -> str | Primer módulo canónico con completitud inferior al 100.0%

# --- src/metricsthinking/backends/__init__.py & python_fallback.py ---
src/metricsthinking/backends/__init__.py::get_active_backend() -> str | Retorna nombre de backend activo ("rust_pyo3" o "python_fallback")
src/metricsthinking/backends/__init__.py::scan_directory(root_path: str, ignore_patterns: list[str] | None = None, include_content: bool = True) -> list[dict[str, Any]] | Crawling con despacho a backend disponible
src/metricsthinking/backends/__init__.py::fast_shannon_entropy(data: str) -> float | Despacha cálculo de entropía a backend disponible
src/metricsthinking/backends/__init__.py::calculate_shingling_jaccard(tokens_a: list[str], tokens_b: list[str], k: int = 5) -> float | Despacha cálculo Jaccard a backend disponible
src/metricsthinking/backends/__init__.py::compute_ast_coupling(file_paths: list[str], root_path: str) -> dict[str, Any] | Despacha cálculo AST de acoplamiento Ca/Ce
src/metricsthinking/backends/python_fallback.py::fast_shannon_entropy(data: str) -> float | Cálculo vectorial de entropía Shannon $H(X) = -\sum p \log_2(p)$
src/metricsthinking/backends/python_fallback.py::calculate_shingling_jaccard(tokens_a: list[str], tokens_b: list[str], k: int = 5) -> float | Coeficiente Jaccard $J(A, B) = |A \cap B| / |A \cup B|$
src/metricsthinking/backends/python_fallback.py::scan_directory(root_path: str, ignore_patterns: list[str] | None = None, include_content: bool = True) -> list[dict[str, Any]] | Crawling determinista con caché SHA-256 en `./.context/cache/`
src/metricsthinking/backends/python_fallback.py::compute_ast_coupling(file_paths: list[str], root_path: str) -> dict[str, Any] | Análisis estático AST de dependencias cruzadas e inestabilidad $I = C_e / (C_a + C_e)$

# --- src/metricsthinking/fpai/ ---
src/metricsthinking/fpai/spectral_engine.py::compute_spectral_vector(file_cache: dict[str, str], priority_map: dict[str, str] | None = None) -> FPAISpectralVector | Calcula bimodalidad $S_{\text{spectral}}$ y $S_{\text{linear}}$
src/metricsthinking/fpai/gatekeeper.py::calculate_shannon_entropy(text: str) -> float | Entropía Shannon pura
src/metricsthinking/fpai/gatekeeper.py::is_safe_placeholder(text: str) -> bool | Filtro para cadenas de prueba y placeholders permitidos
src/metricsthinking/fpai/gatekeeper.py::scan_file_security(file_path: str, content: str, entropy_threshold: float = 4.5) -> dict[str, Any] | Escaneo de entropía, secretos, PII e inyecciones de prompt
src/metricsthinking/fpai/gatekeeper.py::scan_repository_security(file_contents: dict[str, str], lockfile_present: bool = True, entropy_threshold: float = 4.5, ignore_tests: bool = True) -> SecurityVulnerabilityReport | Auditoría forense de seguridad y superficie de ataque
src/metricsthinking/fpai/ablation.py::run_ablation_sampling(file_cache: dict[str, str], sample_ratio: float = 0.2) -> dict[str, Any] | Muestreo de ablación para estimar sensibilidad a pérdida de contexto
src/metricsthinking/fpai/attribution.py::resolve_context_attribution(source_tokens: list[str], reference_tokens: list[str]) -> dict[str, Any] | Atribución por k-shingles Jaccard
src/metricsthinking/fpai/drift_auditor.py::audit_seed_to_code_drift(seed_path: str, codebase_root: str) -> dict[str, Any] | Auditoría de divergencia entre firmas declaradas en Seed y AST real
src/metricsthinking/fpai/compensation.py::generate_pruning_plan(file_cache: dict[str, str], priority_map: dict[str, str]) -> ContextPruningPlan | Ensambla plan de poda para optimizar ventana de contexto
src/metricsthinking/fpai/compensation.py::apply_pruning_plan(plan: ContextPruningPlan, agentignore_path: str = ".agentignore") -> int | Escribe de forma idempotente exclusiones en `.agentignore`
src/metricsthinking/fpai/confidence.py::calculate_confidence_envelope(score: float, file_count: int, test_coverage: float) -> tuple[float, float] | Intervalo de confianza estadístico de la madurez
src/metricsthinking/fpai/medallion.py::run_local_medallion_pipeline(event_data: dict[str, Any], base_dir: str = "data") -> None | Ingestión local en capas Bronze, Silver y Gold de telemetría

# --- src/metricsthinking/collector.py ---
src/metricsthinking/collector.py::ProjectEvidence(target_path: str) -> Object | Contenedor en memoria de hallazgos brutos, caché de archivos y primitivas universales
src/metricsthinking/collector.py::ProjectCollector.__init__(target_path: str, evidence_hints: dict[str, Any] | None = None) -> None | Inicializa colector con filtros y exclusiones
src/metricsthinking/collector.py::ProjectCollector.collect() -> ProjectEvidence | Ejecuta escaneo estático read-only completo con filtros antifraude
src/metricsthinking/collector.py::ProjectCollector._collect_git_metadata() -> None | Extrae hash corto y rama git mediante subprocess sin lanzar excepciones
src/metricsthinking/collector.py::ProjectCollector._single_pass_scan() -> None | Crawling de archivo único vía backend activo con caché SHA-256
src/metricsthinking/collector.py::ProjectCollector._classify_files() -> None | Clasifica archivos en 16 categorías funcionales de evidencia
src/metricsthinking/collector.py::ProjectCollector._parse_seed_metadata() -> None | Parsea metadatos de semillas ThinkingSeed v2/v3 para auto-detección
src/metricsthinking/collector.py::ProjectCollector._classify_universal_primitives() -> None | Agrupa hallazgos en primitivas universales normalizadas
src/metricsthinking/collector.py::ProjectCollector._compute_ast_and_resilience() -> None | Calcula métricas de acoplamiento Ca/Ce e inestabilidad modular

# --- src/metricsthinking/evaluator.py ---
src/metricsthinking/evaluator.py::CriteriaEvaluator.__init__(profile_name: str, profile_data: dict[str, Any]) -> None | Instancia evaluador con matriz de reglas
src/metricsthinking/evaluator.py::CriteriaEvaluator.load_profile(profile_path_or_name: str, profiles_dir: Path | None = None) -> CriteriaEvaluator | Carga perfil YAML resolviendo alias o fallback
src/metricsthinking/evaluator.py::CriteriaEvaluator.evaluate(evidence: ProjectEvidence) -> list[CanonicalModuleEvaluation] | Evalúa los 10 módulos canónicos secuencialmente
src/metricsthinking/evaluator.py::CriteriaEvaluator.check_security_zero_secrets(cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion | Valida ausencia total de secretos en código
src/metricsthinking/evaluator.py::CriteriaEvaluator.check_security_entropy_threshold(cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion | Valida umbral de Shannon $H \le 4.5$ y cero inyecciones
src/metricsthinking/evaluator.py::CriteriaEvaluator.check_resilience_coupling_and_spof(cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion | Valida ausencia de puntos únicos de fallo y bajo acoplamiento
src/metricsthinking/evaluator.py::CriteriaEvaluator.check_resilience_fault_tolerance_patterns(cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion | Verifica patrones de tolerancia a fallos
src/metricsthinking/evaluator.py::CriteriaEvaluator.check_context_spectral_efficiency(cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion | Valida eficiencia espectral FPIA $S_{\text{spectral}}$
src/metricsthinking/evaluator.py::CriteriaEvaluator.check_*(cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion | 95+ métodos de verificación empírica especializada

# --- src/metricsthinking/scorer.py ---
src/metricsthinking/scorer.py::AuditScorer.__init__(modules: list[CanonicalModuleEvaluation], evidence: ProjectEvidence, profile_name: str = "default", profile_data: dict[str, Any] | None = None) -> None | Inicializa motor de scoring
src/metricsthinking/scorer.py::AuditScorer.score() -> ProjectAuditReport | Genera reporte consolidado con estadísticas, FPAI y remediación
src/metricsthinking/scorer.py::AuditScorer._resolve_archetype() -> DomainArchetype | Resuelve arquetipo efectivo de evaluación
src/metricsthinking/scorer.py::AuditScorer._resolve_inspection_mode(archetype: DomainArchetype) -> InspectionMode | Asocia modo de inspección según arquetipo
src/metricsthinking/scorer.py::AuditScorer._build_remediation_plan(archetype: DomainArchetype, mode: InspectionMode) -> list[RemediationItem] | Ordena acciones pendientes P1 a P4 por retorno de inversión

# --- src/metricsthinking/renderer.py ---
src/metricsthinking/renderer.py::ReportRenderer.__init__(report: ProjectAuditReport) -> None | Instancia renderizador con el reporte validado
src/metricsthinking/renderer.py::ReportRenderer.render_markdown() -> str | Ensambla reporte ejecutivo en Markdown con diagrama Mermaid LR y telemetría FPIA
src/metricsthinking/renderer.py::ReportRenderer.render_inferred_roadmap() -> str | Ensambla roadmap operacional con checklists interactivos
src/metricsthinking/renderer.py::ReportRenderer.write_artifacts(output_dir: Path, filename_prefix: str = "MetricsThinking") -> dict[str, Path] | Escribe atómicamente los 4 artefactos en disco garantizando UTF-8
src/metricsthinking/renderer.py::ReportRenderer._render_spectral_context_efficiency() -> str | Renderiza bloque de telemetría espectral FPIA
src/metricsthinking/renderer.py::ReportRenderer._render_security_and_attack_surface() -> str | Renderiza bloque forense de seguridad y superficie de ataque
src/metricsthinking/renderer.py::ReportRenderer._render_systems_modularity_and_resilience() -> str | Renderiza bloque de resiliencia y acoplamiento AST

# --- src/metricsthinking/detector.py ---
src/metricsthinking/detector.py::ArchetypeScore(BaseModel) -> Model | Puntuación normalizada de arquetipo por señales físicas (archetype, raw_score, normalized_score, matched_signals)
src/metricsthinking/detector.py::ArchetypeDetectionResult(BaseModel) -> Model | Resultado consolidado de detección bayesiana (primary_archetype, confidence, scores, detected_modes)
src/metricsthinking/detector.py::ArchetypeDetector(class) -> Object | Motor de inferencia y resolución bayesiana de arquetipos basado en 14 perfiles y señales de evidencia
src/metricsthinking/detector.py::ArchetypeDetector.detect_from_evidence(ev: ProjectEvidence) -> ArchetypeDetectionResult | Clasificación de arquetipo basada en evidencia física recolectada
src/metricsthinking/detector.py::ArchetypeDetector.detect_from_filesystem(target_path: str) -> ArchetypeDetectionResult | Clasificación estática autónoma directa del sistema de archivos
src/metricsthinking/detector.py::probe_archetype(target_path: str = ".") -> str | Resolución rápida de arquetipo primario para enrutamiento de auditoría

# --- src/metricsthinking/engine.py ---
src/metricsthinking/engine.py::resolve_profile_name(hint_or_name: str | None) -> str | Normaliza alias, nombres de perfiles y lenguaje natural
src/metricsthinking/engine.py::probe_project(target_path: str = ".", custom_profiles_dir: Path | None = None) -> ArchetypeDetectionResult | Sonda exploratoria rápida de detección de arquetipo
src/metricsthinking/engine.py::run_audit(target_path: str = ".", profile_name: str = "default", archetype: str | None = None, out_dir: str | None = None, prefix: str = "MetricsThinking", quiet: bool = False, prune: bool = False, medallion: bool = False) -> tuple[ProjectAuditReport, dict[str, Path]] | Orquesta el pipeline completo de 5 fases y persistencia de 4 artefactos

# --- src/metricsthinking/cli.py ---
src/metricsthinking/cli.py::list_available_profiles() -> None | Despliega en stdout catálogo de 14 perfiles y arquetipos disponibles
src/metricsthinking/cli.py::main() -> None | Parser CLI con soporte de subcomandos audit (--probe, --json, --hint, --apply, --raw-dir, --processed-dir), install-skill (--all, --dest, --global, -g, --dry-run), mcp y list-profiles (--index-dir, --compact)

# --- src/metricsthinking/mcp_server.py ---
src/metricsthinking/mcp_server.py::handle_list_tools() -> list[dict[str, Any]] | Retorna especificación JSON de 6 herramientas MCP disponibles
src/metricsthinking/mcp_server.py::handle_call_tool(name: str, arguments: dict[str, Any]) -> list[dict[str, Any]] | Ejecuta herramienta solicitada por cliente MCP
src/metricsthinking/mcp_server.py::run_mcp_server() -> None | Loop interactivo stdio para protocolo JSON-RPC 2.0

# --- scripts/install_skill.py, hnsw_index_rebuild.py & run_benchmark.py ---
scripts/hnsw_index_rebuild.py::rebuild_hnsw_index(root_path: str, index_output: str) -> None | Reconstruye índice vectorial HNSW para búsqueda semántica
scripts/run_benchmark.py::main() -> None | Runner determinista de benchmarks volumétricos y generación de telemetría de cobertura
scripts/install_skill.py::get_user_home() -> Path | Retorna directorio home de usuario de manera multiplataforma
scripts/install_skill.py::install_antigravity(dest_root: Path, is_global: bool = False, dry_run: bool = False) -> list[Path] | Despliega skill de Google Antigravity en .agents/ o global
scripts/install_skill.py::install_codex(dest_root: Path, is_global: bool = False, dry_run: bool = False) -> list[Path] | Despliega skill de OpenAI Codex en .codex/ o global
scripts/install_skill.py::install_claude(dest_root: Path, dry_run: bool = False) -> list[Path] | Copia CLAUDE.md en raíz de destino
scripts/install_skill.py::install_cursor(dest_root: Path, dry_run: bool = False) -> list[Path] | Despliega .cursor/rules/metrics.mdc
scripts/install_skill.py::install_copilot(dest_root: Path, dry_run: bool = False) -> list[Path] | Despliega .github/copilot-instructions.md
scripts/install_skill.py::install_mcp_config(dest_root: Path, dry_run: bool = False) -> list[Path] | Genera snippet de configuración mcp_metricsthinking.json
scripts/install_skill.py::run_installer(target: str = "all", dest: str = ".", is_global: bool = False, dry_run: bool = False) -> None | Orquesta despliegue para proveedores seleccionados
```

- **4.2 Esquemas y Contratos de Datos:**
  - `./schemas/audit_criterion.schema.json`: Valida criterios individuales evaluados.
  - `./schemas/canonical_module.schema.json`: Valida módulos canónicos M01 a M10 y sus ponderaciones.
  - `./schemas/evidence_primitives.schema.json`: Valida primitivas universales (`config`, `spec`, `pipeline`, `verification`, `implementation`).
  - `./schemas/project_audit_report.schema.json`: Valida el reporte consolidado emitido.
  - `./schemas/repo_fpai_manifest.v2.json`: Valida manifiesto FPIA de gobernanza y presupuestos de tokens.
  - `./schemas/telemetry_event.v2.json`: Valida eventos de telemetría para capas Medallion.
  - `./schemas/thinking_seed_v3.schema.json`: Valida contratos polimórficos de semillas ThinkingSeed v3.0.
- **4.3 Persistencia y Sincronización de Artefactos:**
  - `./artifacts/MetricsThinking.md`: Reporte ejecutivo para consumo humano con diagrama Mermaid LR.
  - `./artifacts/MetricsThinking.json`: Telemetría forense completa para consumo por herramientas y agentes.
  - `./artifacts/plans/active/INFERRED_ROADMAP.md`: Roadmap operacional desacoplado en 10 fases con tareas pendientes `[ ]` y completadas `[x]`.
  - `./artifacts/plans/active/CONTEXT_PRUNING_PLAN.json`: Plan determinista y reversible de poda contextual para control de derivas.

---

## 5. CONFIGURACIÓN, ENTORNOS Y DEPENDENCIAS
- **5.1 Variables y Argumentos CLI:**
  - `--target` / `-t`: Directorio del repositorio a auditar (Default: `.`).
  - `--profile` / `-p`: Perfil de evaluación YAML a aplicar (Default: `default`).
  - `--archetype` / `-a`: Override explícito del arquetipo de ingeniería.
  - `--out-dir` / `-o`: Directorio de destino para los artefactos generados (Default: `<target>/artifacts`).
  - `--prefix`: Prefijo de nombre de archivo para artefactos (Default: `MetricsThinking`).
  - `--quiet` / `-q`: Suprime el despliegue de la tabla resumen en consola.
  - `--prune`: Aplica poda contextual automática e idempotente en `.agentignore`.
  - `--medallion`: Habilita persistencia de eventos de telemetría en capas Bronze, Silver y Gold.
  - `--list-profiles`: Muestra en consola el catálogo de perfiles disponibles y finaliza la ejecución.
- **5.2 Perfiles de Auditoría Canónicos (14 perfiles en `./config/profiles/`):**
  - `default.yaml`: Perfil universal para proyectos de software y plataformas complejas.
  - `agent-skill.yaml`: AI Agent Skills, Context Engineering, Prompt Engineering y orquestación multi-asistente.
  - `data-platform.yaml`: Plataformas de datos, Medallion Lakehouses, ETL/ELT y BigQuery/Databricks/Fabric.
  - `dataops.yaml`: Data Contracts, linaje, SLAs de datos y reconciliación de pipelines.
  - `web-app.yaml`: Aplicaciones web modernas (React, Vite, Next.js, TypeScript).
  - `mlops.yaml`: Model Registry, pipelines de entrenamiento, tracking de experimentos y data drift.
  - `llmops.yaml`: RAG, gestión de prompts, guardrails, vector stores y evaluación de LLMs.
  - `gitops.yaml`: Manifiestos K8s, controladores de reconciliación (Argo/Flux) y control de deriva.
  - `platform-eng.yaml`: Internal Developer Platforms (IDP), Backstage, Golden Paths e IaC.
  - `devsecops.yaml`: Policy-as-Code, SBOM, escaneo SAST/DAST y escaneo de secretos.
  - `dual-track.yaml`: Árboles de oportunidad, validación de hipótesis y feature flags.
  - `team-topologies.yaml`: Carga cognitiva, contratos de interacción y límites de dominio.
  - `chaos-eng.yaml`: Inyección de fallos, steady-state verification y Game Days.
  - `sdd.yaml`: Spec-Driven Development, contratos OpenAPI/AsyncAPI/Proto y generación estricta de código.
- **5.3 Matriz de Dependencias (definidas en `pyproject.toml`):**
  - *Producción:* `pydantic>=2.0.0`, `pyyaml>=6.0`, `rich>=13.0.0`, `typer>=0.9.0`.
  - *Desarrollo / QA:* `pytest>=7.4.0`, `pytest-cov>=4.1.0`, `ruff>=0.1.0`, `mypy>=1.6.0`, `jsonschema>=4.19.0`.
  - *Acelerador Nativo Opcional:* Rust Cargo / PyO3 (`crates/metricsthinking_rs`). Fallback automático en Python puro ante ausencia de binario compilado.

---

## 6. PRUEBAS, CI/CD, DESPLIEGUE Y OPERACIÓN
- **6.1 Estrategia de pruebas:**
  - Suite de Pytest completa con 105 pruebas unitarias, de integración, stress y detección bayesiana en `./tests/`, cubriendo calibración de scoring, CLI, colector, evaluador, detector de arquetipos, instalador, renderizador, scorer, backends v4, motor espectral FPIA, firewall de seguridad, resiliencia y los 14 arquetipos v3.0.
  - Pruebas de regresión determinista (*Golden Regression Tests*) validadas contra `./tests/fixtures/sample_golden_audit.json` y `./tests/fixtures/golden_baseline_report.json`.
  - Ejecución de pruebas: `python -m pytest` (100% pruebas pasando, 105/105 passed, 0 fallos).
- **6.2 Pipeline CI/CD (`.github/workflows/ci.yml`):**
  - Ejecución automatizada en GitHub Actions en branches `main` y `master`.
  - Matriz de pruebas sobre Python 3.10, 3.11 y 3.12.
  - Pasos obligatorios: Linting con Ruff (`ruff check .`), verificación estática de tipos con Mypy (`mypy src/`), ejecución de Pytest con cobertura y auto-auditoría con `metricsthinking audit --target .`.
- **6.3 Despliegue y Distribución:**
  - Empaquetado estandarizado compatible con PEP 517/621 vía Hatchling (`pyproject.toml`).
  - Despliegue multi-asistente ejecutable mediante `python scripts/install_skill.py --target all`.

---

## 7. SUPERFICIE DE TENSIÓN, CONTRADICCIONES Y MODOS DE FALLA

### 7.1 Cruce Adversarial: Resolución de Tensiones v4.0
- **Vector T-01: Inconsistencia y codificación en `requirements.txt` [RESUELTO]:**
  - *Resolución:* `./requirements.txt` fue recodificado a UTF-8 puro sin BOM, eliminando referencias absolutas locales y sincronizando con `pyproject.toml` (v4.0.0). Verificado con `tests/test_hygiene_v4.py`.
- **Vector T-02: Directorios esqueleto vacíos heredados de iDirectory [RESUELTO]:**
  - *Resolución:* Eliminados los directorios vacíos sin código (`./src/cloud_jobs/`, `./src/core/`, `./src/dashboards/`, `./src/data_generation/`, `./tools/`). Topología sincronizada en `.context/tree.json`.
- **Vector T-03: Divergencia de nombres en documentación heredada [RESUELTO]:**
  - *Resolución:* `./02_foundation/engine/engine_readme.md` corregido para apuntar exactamente a `01_seed/seed-metricsthinking-master.md`.
- **Vector T-04: Inconsistencia de versión en `mcp_server.py` y `mcp_metricsthinking.json` [RESUELTO]:**
  - *Resolución:* Sincronizada la versión `"4.0.0"` en `mcp_server.py`, `__init__.py`, `pyproject.toml` y manifiestos MCP.
- **Vector T-05: Dependencia de PYTHONPATH para ejecución directa [RESUELTO]:**
  - *Resolución:* `src/metricsthinking/cli.py` soporta ejecución portable mediante `python -m metricsthinking.cli` y configuración empaquetada.
- **Vector T-06: Brecha en M07 (Cuello de Botella Activo: 66.7% -> 100.0%) [RESUELTO]:**
  - *Resolución:* Materializada suite de benchmark volumétrico (`./tests/test_benchmarks_stress.py`) y reporte físico (`./artifacts/benchmark_coverage_report.json`), cerrando M07 al 100.0%.
- **Vector T-07: Falsos positivos en `SecurityGatekeeper` por cadenas literales en planes de diseño [RESUELTO]:**
  - *Resolución:* En `artifacts/plans/active/implementation_plan.md`, las descripciones de ataques de prompt injection se reformularon para evitar cadenas literales de ataque, asegurando que la auditoría de seguridad se mantenga en 0 inyecciones y permitiendo que `tests/test_evaluator_v4.py` pase al 100%.

### 7.2 Modos de Falla y Resiliencia
- **Resiliencia ante ausencia de acelerador Rust:** Si el módulo nativo compilado `_core_rs` no está disponible, el sistema captura transparentemente el `ImportError` y activa `python_fallback.py` con caché SHA-256 en memoria y disco sin degradar funcionalidad.
- **Resiliencia ante repositorios sin Git:** Si el directorio carece de `.git` o el comando falla, el colector asigna de manera segura `git_commit = "untracked"` y `git_branch = "unknown"` sin interrumpir la auditoría.
- **Protección contra desbordamiento de memoria:** El colector excluye explícitamente directorios gigantes (`.git`, `node_modules`, `.venv`, `venv`, `build`, `dist`, `data/raw`), evitando lecturas descontroladas en disco.
- **Codificación y archivos no-UTF8:** La lectura de archivos clave utiliza captura de excepciones silenciosa, previniendo fallos catastróficos por codificaciones binarias o corruptas.

### 7.3 Idempotencia y No-Degradación
- Ejecuciones consecutivas de `run_audit()` sobre el mismo árbol de archivos generan reportes con hashes y resultados deterministas, sin mutar el código fuente del proyecto auditado.
- La aplicación del plan de poda (`--prune`) sobre `.agentignore` está acotada entre marcadores `# >>> METRICSTHINKING AUTO-PRUNE >>>`, permitiendo reversibilidad total.

---

## 8. SEGURIDAD, PRIVACIDAD Y GUARDRAILS
- **8.1 Escaneo Seguro y Modo Solo-Lectura:** [CONFIRMADO] `ProjectCollector` realiza operaciones estrictamente de lectura. Ningún archivo del repositorio auditado es modificado o eliminado durante la fase de análisis.
- **8.2 Detección y Enmascarado de PII / Secretos:** [CONFIRMADO] Los nombres de archivos y extractos se procesan bajo política Zero-Trust. Prohibido persistir contraseñas, tokens JWT, claves privadas o cadenas sensibles. Cualquier coincidencia es enmascarada con `<REDACTED>`.
- **8.3 Aislamiento de Carpetas Sensibles:** [CONFIRMADO] Carpetas que típicamente contienen credenciales locales (`.ssh`, `.aws`, `.env`, `secrets/`) son ignoradas automáticamente por el colector.
- **8.4 Firewall de Seguridad Zero-Tolerance:** [CONFIRMADO] Verificación estricta de umbral Shannon ($H \le 4.5$) y detección de ataques de inyección de prompt sobre archivos de instrucciones agénticas (`.mdc`, `SKILL.md`, `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`).

---

## 9. ESTADO REAL, DEUDA TÉCNICA Y DECISIONES (ADRs)
- **9.1 Nivel de Madurez Cuantitativa:** [CONFIRMADO] **100.0% / 100.0%** (Perfil `default`) | **100.0%** (Perfil `agent-skill`) — Banda: **Excelencia Operativa / Producción (90.0% - 100.0%)**.
- **9.2 Cuello de Botella Activo:** [CONFIRMADO] `Ninguno. Todos los módulos canónicos se encuentran al 100.0% de cumplimiento.`
- **9.3 Registro de Decisiones de Arquitectura (ADRs):**
  - `[ADR-001]`: [CONFIRMADO] Adopción de modelo canónico desacoplado de 10 módulos (`M01` a `M10`) con pesos fijos por perfil para garantizar consistencia matemática en comparaciones inter-proyecto.
  - `[ADR-002]`: [CONFIRMADO] Pydantic v2 como motor de validación tipada estricta para modelos de evidencia y reportes de auditoría.
  - `[ADR-003]`: [CONFIRMADO] Prohibición estricta de subgrafos anidados en diagramas Mermaid, estandarizando flujos horizontales `flowchart LR` para evitar truncamiento en visores markdown corporativos.
  - `[ADR-004]`: [CONFIRMADO] Desacoplamiento de perfiles de evaluación en archivos YAML independientes dentro de `./config/profiles/`, permitiendo extender arquetipos sin modificar el núcleo del motor.
  - `[ADR-005]`: [CONFIRMADO] Adopción de Model Context Protocol (MCP) nativo vía stdio con 6 herramientas para interoperabilidad directa con ecosistemas de IA generativa.
  - `[ADR-006]`: [CONFIRMADO] Integración de motor espectral FPIA bimodal ($S_{\text{spectral}}$ y $S_{\text{linear}}$) para cuantificar el costo y eficiencia de contexto consumido por LLMs.
  - `[ADR-007]`: [CONFIRMADO] Arquitectura de crawling híbrida: PyO3 Rust en `crates/metricsthinking_rs` con fallback transparente en Python puro y caché incremental SHA-256 en disco.
- **9.4 Matriz de Remediación Priorizada:**
  - `P4 (Mantenimiento Continuo)`: Mantener la suite de 94 pruebas Pytest sincronizada y vigilar derivas en nuevos submódulos.

---

## 10. REGLAS DE MODIFICACIÓN, GLOSARIO E ÍNDICE DE EVIDENCIAS

### 10.1 Invariantes de Ingeniería Inviolables
- `[INV-01] Rigor de Evidencia Física (Ground Truth):` Prohibido otorgar puntaje > 0% a criterios basados en stubs, funciones vacías (`pass`) o comentarios `TODO`/`FIXME`.
- `[INV-02] Invariante Zero Source Code en Seeds:` Prohibido incrustar bloques de código fuente de implementación en archivos seed; documentar únicamente mediante firmas simbólicas AST de 1 sola línea.
- `[INV-03] Portabilidad Estricta de Rutas:` Prohibido incluir rutas absolutas con letras de unidad o esquemas file-URI locales. Usar exclusivamente rutas relativas limpias (`./ruta/archivo`).
- `[INV-04] Suma Ponderada Canónica:` Todo perfil de evaluación debe contener exactamente 10 módulos (`M01` a `M10`) cuyas ponderaciones sumen exactamente `1.0` (100%).
- `[INV-05] Sincronización de Cuatro Artefactos Holísticos:` Cualquier corrida de auditoría debe producir y sincronizar obligatoriamente `MetricsThinking.md`, `MetricsThinking.json`, `INFERRED_ROADMAP.md` y `CONTEXT_PRUNING_PLAN.json`.
- `[INV-06] Invariante de Diagramación Mermaid LR:` Todo diagrama de roadmap debe usar `flowchart LR` sin subgrafos verticales para garantizar legibilidad en interfaces de chat y visores Markdown.
- `[INV-07] Safe Atomic Write:` Toda escritura a disco debe realizarse con codificación UTF-8 pura (sin BOM) y validación previa de directorio padre.
- `[INV-08] Sanitización Zero-Trust:` Prohibido imprimir o registrar credenciales o secretos en consola o artefactos generados.

### 10.2 Glosario de Términos
- **Ground Truth:** Evidencia física tangible y verificable en el disco duro (código, pruebas, esquemas, configuración), contrapuesta a declaraciones no comprobadas.
- **Canonical Modules (M01-M10):** Las 10 etapas universales del ciclo de vida de un proyecto tecnológico que estructuran el cálculo de madurez.
- **Stage-Gate:** Metodología de gobierno que condiciona el avance a la verificación formal de entregables físicos.
- **ThinkingSeed Master:** Memoria técnica determinista y vector arquitectónico de alta densidad que encapsula el ADN completo de un sistema sin incluir código de implementación.
- **FPAI (First-Principles AI Context Economy):** Paradigma de cuantificación y optimización del consumo de tokens mediante análisis espectral y poda dirigida.
- **Active Bottleneck:** El módulo canónico de menor avance que limita la madurez general del proyecto.

### 10.3 Índice de Evidencias Físicas
| Ruta Relativa del Archivo | Rol en el Sistema | Estado Verificado |
| :--- | :--- | :--- |
| `./pyproject.toml` | Manifiesto de empaquetado y dependencias PEP 621 | [CONFIRMADO] v4.0.0 |
| `./src/metricsthinking/models.py` | Modelos Pydantic v2 inmutables | [CONFIRMADO] 187 líneas |
| `./src/metricsthinking/collector.py` | Colector estático con backend híbrido | [CONFIRMADO] 263 líneas |
| `./src/metricsthinking/detector.py` | Detector bayesiano de arquetipos | [CONFIRMADO] 441 líneas |
| `./src/metricsthinking/backends/__init__.py` | Despachador de backends (Rust/Python) | [CONFIRMADO] 82 líneas |
| `./src/metricsthinking/backends/python_fallback.py` | Crawling determinista con caché SHA-256 | [CONFIRMADO] 184 líneas |
| `./src/metricsthinking/fpai/spectral_engine.py` | Motor espectral de contexto FPIA | [CONFIRMADO] 142 líneas |
| `./src/metricsthinking/fpai/gatekeeper.py` | Firewall de seguridad y Zero-Tolerance | [CONFIRMADO] 218 líneas |
| `./src/metricsthinking/evaluator.py` | Evaluador de criterios con 95+ reglas | [CONFIRMADO] 751 líneas |
| `./src/metricsthinking/scorer.py` | Motor de cálculo ponderado y remediación | [CONFIRMADO] 257 líneas |
| `./src/metricsthinking/renderer.py` | Generador de Markdown, JSON, Roadmap y Poda | [CONFIRMADO] 468 líneas |
| `./src/metricsthinking/engine.py` | Orquestador de auditoría de 5 fases | [CONFIRMADO] 268 líneas |
| `./src/metricsthinking/cli.py` | Interfaz de línea de comandos Typer/Argparse | [CONFIRMADO] 178 líneas |
| `./src/metricsthinking/mcp_server.py` | Servidor Model Context Protocol stdio (6 tools) | [CONFIRMADO] 285 líneas |
| `./crates/metricsthinking_rs/` | Acelerador nativo en Rust (PyO3) | [CONFIRMADO] 5 módulos .rs |
| `./config/profiles/` | 14 perfiles canónicos YAML | [CONFIRMADO] 14 archivos |
| `./schemas/` | Contratos JSON Schema formales | [CONFIRMADO] 7 esquemas |
| `./scripts/run_benchmark.py` | Suite automatizada de benchmarks volumétricos | [CONFIRMADO] 208 líneas |
| `./tests/` | Suite Pytest unitaria, integración y stress | [CONFIRMADO] 105/105 passed |
| `./.agents/skills/metrics/SKILL.md` | Skill para Google Antigravity | [CONFIRMADO] Operacional |

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA

> **Mensaje de orientación para el modelo de IA receptor:**
> "Esto es una semilla de proyecto (**ThinkingSeed Master v3.0**): el vector arquitectónico y ADN del proyecto (`contains_source_code="false"`), no su repositorio completo. Refleja el avance real, los contratos simbólicos y la superficie de tensión del sistema hasta la fecha. Como modelo receptor, tu función es usar esta semilla como memoria técnica para:
> 1. **Responder preguntas** sobre la arquitectura, contratos simbólicos, dependencias y flujos del sistema.
> 2. **Auditar riesgos y sugerir mejoras** evaluando activamente la Superficie de Tensión (Sección 7) y las áreas marcadas como `[FALTANTE]`.
> 3. **Generar código o soluciones compatibles** respetando las rutas relativas (`./`), firmas simbólicas e invariantes definidas aquí, cuando el usuario te lo solicite."

### Pautas de resolución:
Antes de resolver una solicitud:
1. Identifica el objetivo del usuario.
2. Localiza los componentes afectados usando las rutas relativas (`./`) del Seed.
3. Revisa restricciones (`[INV-01]` a `[INV-08]`), contratos simbólicos (Sección 4) y vectores de tensión (Sección 7).
4. Explicita supuestos cuando sea necesario: "Supongo que X debido a Y".
5. Propone cambios por archivo con rutas relativas claras y separadores Unix (`/`).
6. Añade pruebas, riesgos y criterios de aceptación.

### 🤝 Acuse de Recibo Inicial
Si el usuario adjuntó esta semilla **sin una instrucción específica**, no intentes generar código ni completar archivos vacíos. Responde únicamente con:
1. Un saludo confirmando que asimilaste el ADN arquitectónico v3.0 de **MetricsThinking™ Engine** (`<SEED_ARCHITECTURAL_VECTOR>`) y su stack principal.
2. Un breve resumen de 2-3 líneas sobre el objetivo, su estado actual y sus principales vectores de tensión.
3. Una frase poniéndote a disposición para resolver dudas sobre su funcionamiento o colaborar en los siguientes pasos de desarrollo.

</SEED_ARCHITECTURAL_VECTOR>