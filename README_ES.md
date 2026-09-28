# METRICS THINKING: Motor Universal de Ingeniería Inversa y Auditoría por Ground Truth para Proyectos Tecnológicos

**Idioma:** [English](README.md) | [Español](README_ES.md)

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-1a1a1a?style=flat-square&logo=python)](https://python.org)
[![Version](https://img.shields.io/badge/Versi%C3%B3n-3.0.0%20Universal-2b2b2b?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Arquitectura](https://img.shields.io/badge/Arquitectura-Polim%C3%B3rfica%20Multi--Arquetipo-2b2b2b?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Verificación](https://img.shields.io/badge/Verificaci%C3%B3n-Pytest%20100%25-34495e?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Motor](https://img.shields.io/badge/Motor-Auditor%C3%ADa%20AST%20Ground%20Truth-1a1a1a?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Licencia](https://img.shields.io/badge/Licencia-Apache%202.0-4b5563?style=flat-square)](LICENSE)

---

## 1. Resumen Ejecutivo

MetricsThinking™ v3.0 Universal es un motor empresarial de análisis estático, ingeniería inversa y gobernanza de proyectos diseñado para computar la madurez matemática formal de repositorios tecnológicos a través de **10 Arquetipos de Ingeniería**. En la ingeniería de software moderna asistida por IA y desarrollada por equipos multidisciplinarios, la evaluación del avance real frecuentemente se ve distorsionada por sesgos cognitivos, archivos stub engañosos y declaraciones arquitectónicas no verificadas. MetricsThinking resuelve esta tensión ejecutando una inspección exhaustiva de evidencia física tangible (Ground Truth) en el sistema de archivos, árboles de sintaxis abstracta (AST), suites de pruebas, manifiestos de contenedores, contratos de datos y pipelines de automatización CI/CD.

El motor desacopla cualquier proyecto tecnológico en una matriz adaptada al dominio compuesta por 10 Módulos Canónicos ($M_1, \dots, M_{10}$). Cada módulo evalúa un conjunto parametrizado de criterios frente a la presencia de archivos físicos, densidad de tokens sintácticos e invariantes semánticos clasificados en **5 Primitivas Universales de Evidencia** (`config`, `spec`, `pipeline`, `verification`, `implementation`). El pipeline de scoring calcula un porcentaje ponderado y determinista de completitud ($0.0\% - 100.0\%$), clasifica el código en cinco bandas estandarizadas de madurez y genera artefactos sincronizados: contratos de datos en JSON, un informe ejecutivo en Markdown con un diagrama de flujo horizontal Mermaid LR sin anidamientos conflictivos y un roadmap de implementación inferido.

---

## 2. Arquetipos de Ingeniería Soportados (v3.0)

MetricsThinking™ v3.0 soporta nativamente 10 disciplinas tecnológicas mediante perfiles desacoplados:

| # | Arquetipo | ID | Modo de Inspección | Evidencia Clave Inspeccionada |
|:--|:----------|:---|:-------------------|:------------------------------|
| 1 | **MLOps** | `mlops` | `pipeline_orchestration` | Model cards, datasets, pipelines MLflow/DVC, monitores de drift, scripts de entrenamiento |
| 2 | **LLMOps / GenAIOps** | `llmops` | `pipeline_orchestration` | Context engineering, registro de prompts, pipelines RAG, evals sintéticas y guardrails |
| 3 | **DataOps / Data Platform** | `dataops` | `pipeline_orchestration` | Arquitectura Medallion, Data Contracts, modelos dbt/Dataform, suites Great Expectations |
| 4 | **GitOps / Declarative Infra** | `gitops` | `declarative_config` | Manifiestos Kubernetes, Helm/Kustomize, aplicaciones ArgoCD/Flux, políticas de drift |
| 5 | **Platform Engineering / IDP** | `platform-eng` | `declarative_config` | Portales de desarrollador (Backstage), Golden Paths, catálogo de servicios, Score/IaC |
| 6 | **DevSecOps** | `devsecops` | `governance_spec` | Modelado de amenazas, reglas SAST/DAST, SBOM (CycloneDX/SPDX), Policy-as-Code (OPA/Kyverno) |
| 7 | **Dual-Track Agile** | `dual-track` | `polyglot_hybrid` | Árboles de oportunidad-solución, PRDs, discovery spikes, experimentos A/B, telemetría |
| 8 | **Team Topologies** | `team-topologies` | `governance_spec` | Contratos de equipo, modos de interacción, mapas de bounded contexts, carga cognitiva |
| 9 | **Chaos Engineering** | `chaos-eng` | `declarative_config` | Hipótesis de steady-state, experimentos de inyección de fallos (Chaos Mesh/Litmus), Game Days |
| 10 | **Spec-Driven Dev (SDD)** | `sdd` | `governance_spec` | Especificaciones OpenAPI/AsyncAPI/Proto, tests de contrato (Pact), SDKs generados, mocks |

---

## 3. Arquitectura y Topología del Sistema

```text
+----------------------------------------------------------------------------------------------------+
|                                NÚCLEO UNIVERSAL METRICSTHINKING v3.0                               |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  +---------------------------+       +----------------------------+       +---------------------+  |
|  |    01. EvidenceCollector  | ----> |    02. ModuleEvaluator     | ----> |   03. AuditScorer   |  |
|  |  - 5 Primitivas Evidencia |       |  - Despacho Polimórfico    |       |  - Pesos Dinámicos  |  |
|  |  - Escaneo de archivos    |       |  - 10 Perfiles Arquetipo   |       |  - Bandas Madurez   |  |
|  |  - Inspección AST/tokens  |       |  - 25+ Reglas de Dominio   |       |  - Plan de Acción   |  |
|  |  - Metadatos ThinkingSeed |       |  - Filtros Antifraude      |       |  - Cuello Botella   |  |
|  +---------------------------+       +----------------------------+       +---------------------+  |
|               |                                                                      |             |
|               v                                                                      v             |
|  +---------------------------+                                            +---------------------+  |
|  |   ProjectEvidence (DTO)   |                                            |  ProjectAuditReport |  |
|  +---------------------------+                                            +---------------------+  |
|                                                                                      |             |
|                                                                                      v             |
|                                      +----------------------------+       +---------------------+  |
|                                      |  05. Sincronización Multi  | <---- | 04. ArtifactRenderer|  |
|                                      |  - Carpeta artifacts/      |       |  - MetricsThinking. |  |
|                                      |  - Despliegue Multi-Skill  |       |    json / .md       |  |
|                                      |  - Servidor MCP JSON-RPC   |       |  - Flujo Mermaid LR |  |
|                                      |                            |       |  - INFERRED_ROADMAP |  |
|                                      +----------------------------+       +---------------------+  |
+----------------------------------------------------------------------------------------------------+
```

---

## 4. Formulación Matemática y Motores Analíticos

### 4.1. Cálculo de Puntuación a Nivel de Criterio
Sea $\mathcal{C}_{i,j}$ el $j$-ésimo criterio perteneciente al módulo $M_i$. Su puntuación de verificación bruta $s(\mathcal{C}_{i,j}) \in [0, 100]$ se calcula a partir de la presencia de evidencia física que cumpla con los patrones de archivo $\mathcal{P}_{i,j}$ y contenga las palabras clave semánticas requeridas $\mathcal{K}_{i,j}$:

$$s(\mathcal{C}_{i,j}) = \min\left(100.0, \; 100 \cdot \frac{|\mathcal{E}_{i,j}^{valid}|}{\max(1, |\mathcal{P}_{i,j}|)} \cdot \mathbb{I}(\text{keywords\_satisfied})\right)$$

donde $\mathcal{E}_{i,j}^{valid}$ representa el subconjunto de archivos descubiertos excluyendo estrictamente rutas detectadas por los filtros antifraude (ej. fixtures de prueba, stubs y logs generados automáticamente), y $\mathbb{I}(\cdot)$ es la función indicadora.

### 4.2. Puntuación de Módulo y Avance Ponderado Global
Sea $w_i \in (0, 1]$ el peso arquitectónico asignado al módulo $M_i$ tal que $\sum_{i=1}^{10} w_i = 1.0$. La puntuación del módulo $S(M_i)$ y el grado de madurez global del repositorio $\Phi(\mathcal{R})$ se computan como:

$$S(M_i) = \sum_{j=1}^{K_i} \omega_{i,j} \cdot s(\mathcal{C}_{i,j}), \quad \text{donde } \sum_{j=1}^{K_i} \omega_{i,j} = 1.0$$

$$\Phi(\mathcal{R}) = \sum_{i=1}^{10} w_i \cdot S(M_i) \quad \in [0.0\%, 100.0\%]$$

### 4.3. Asignación a Bandas de Madurez
La puntuación global $\Phi(\mathcal{R})$ se clasifica deterministamente en una banda de madurez discreta $\mathcal{B}$:

$$\mathcal{B}(\Phi) = \begin{cases}
\text{Inception / Prototyping} & 0.0 \le \Phi < 25.0 \\
\text{Foundational Development} & 25.0 \le \Phi < 50.0 \\
\text{Functional Maturation} & 50.0 \le \Phi < 75.0 \\
\text{Operational Excellence / Production Ready} & 75.0 \le \Phi < 90.0 \\
\text{Enterprise Certified / Battle-Tested} & 90.0 \le \Phi \le 100.0
\end{cases}$$

---

## 5. Estructura del Repositorio y Ecosistema Multi-Proveedor

```text
MetricsThinking/
├── .agents/skills/metrics/                   # Skill local para Google Antigravity
│   └── SKILL.md
├── integrations/                             # Adaptadores nativos para proveedores de IA
│   ├── claude/CLAUDE.md                      # Anthropic Claude Code y Desktop
│   ├── cursor/metrics.mdc                    # Reglas para Cursor IDE y Windsurf
│   └── copilot/copilot-instructions.md       # Instrucciones GitHub Copilot y OpenAI
├── AGENTS.md                                 # Estándar abierto universal para agentes
├── artifacts/
│   ├── MetricsThinking.json                  # Reporte canónico machine-readable
│   ├── MetricsThinking.md                    # Reporte ejecutivo human-readable
│   └── plans/active/
│       └── INFERRED_ROADMAP.md               # Roadmap inferido de implementación
├── config/profiles/                          # 10 Perfiles Universales de Evaluación
│   ├── default.yaml                          # Perfil canónico de ingeniería de software
│   ├── mlops.yaml                            # Perfil de ciclo de vida MLOps
│   ├── llmops.yaml                           # Perfil LLMOps, GenAI y Context Engineering
│   ├── dataops.yaml                          # Perfil DataOps y Modern Data Stack
│   ├── gitops.yaml                           # Perfil GitOps e Infraestructura Declarativa
│   ├── platform-eng.yaml                     # Perfil Platform Engineering e IDP
│   ├── devsecops.yaml                        # Perfil DevSecOps, Policy-as-Code y SBOM
│   ├── dual-track.yaml                       # Perfil Dual-Track Agile y Product Engineering
│   ├── team-topologies.yaml                  # Perfil Team Topologies y límites de dominio
│   ├── chaos-eng.yaml                        # Perfil Chaos Engineering y Steady State
│   ├── sdd.yaml                              # Perfil Spec-Driven Development (SDD)
│   ├── data-platform.yaml                    # Perfil para plataformas de datos e IA
│   └── web-app.yaml                          # Perfil para aplicaciones web fullstack
├── schemas/                                  # Suite de esquemas JSON Schema (Draft 2020-12)
│   ├── audit_criterion.schema.json           # Contrato JSON Schema para criterios
│   ├── canonical_module.schema.json          # Contrato JSON Schema para módulos
│   ├── project_audit_report.schema.json      # Contrato JSON Schema para reportes
│   ├── thinking_seed_v3.schema.json          # Contrato JSON Schema para ThinkingSeed v3.0
│   └── evidence_primitives.schema.json       # Contrato JSON Schema para 5 primitivas
├── scripts/
│   └── install_skill.py                      # Instalador automatizado multi-proveedor
├── src/
│   └── metricsthinking/
│       ├── __init__.py                       # Exportaciones del paquete
│       ├── cli.py                            # Interfaz CLI multi-comando
│       ├── collector.py                      # 5 Primitivas universales e ingestión Seed
│       ├── engine.py                         # Orquestador del pipeline y autodescubrimiento
│       ├── evaluator.py                      # Evaluador matricial y 25+ reglas de dominio
│       ├── mcp_server.py                     # Servidor Model Context Protocol (MCP)
│       ├── models.py                         # Modelos Pydantic v2 inmutables
│       ├── renderer.py                       # Generador Mermaid LR y Markdown
│       └── scorer.py                         # Motor de scoring y priorización
├── tests/                                    # Suite exhaustiva de pruebas unitarias (50+ tests)
├── pyproject.toml                            # Especificación de build estándar (v3.0.0)
├── README.md                                 # Documentación maestra en inglés
└── README_ES.md                              # Documentación técnica en español
```

---

## 6. Instalación de la Skill en Proveedores de IA

MetricsThinking puede desplegarse como herramienta o skill activa en todos los principales asistentes de IA:

### 6.1. Instalación Rápida vía CLI
```bash
# Clonar el repositorio
git clone https://github.com/AlvaroAlejandroFinOps/Metrics.git
cd Metrics
pip install -e ".[dev]"

# Instalar skill para TODOS los proveedores en el workspace actual:
metricsthinking install-skill --target all

# O instalar para un proveedor específico:
metricsthinking install-skill --target antigravity   # Google Antigravity
metricsthinking install-skill --target claude        # Anthropic Claude Code
metricsthinking install-skill --target cursor        # Cursor IDE
metricsthinking install-skill --target copilot       # GitHub Copilot
metricsthinking install-skill --target mcp           # Generar snippet MCP
```

### 6.2. Instalación Global en Google Antigravity
Para disponibilizar `/metrics` de forma global en cualquier workspace de Antigravity:
```bash
metricsthinking install-skill --target antigravity --global
```

### 6.3. Integración Universal vía Model Context Protocol (MCP)
Iniciar el servidor JSON-RPC por stdio:
```bash
metricsthinking mcp
```
Snippet para añadir a `mcp_config.json` en Claude Desktop o Cursor:
```json
{
  "mcpServers": {
    "metricsthinking": {
      "command": "metricsthinking",
      "args": ["mcp"]
    }
  }
}
```

---

## 7. Protocolo de Ejecución y Verificación

### 7.1. Auditorías Directas

```bash
# Listar todos los perfiles y arquetipos disponibles
metricsthinking list-profiles

# Ejecutar auditoría completa sobre el directorio actual (o autodetectar vía ThinkingSeed)
metricsthinking audit --target . --out-dir artifacts

# Ejecutar auditoría con perfil especializado en un arquetipo
metricsthinking audit --target . --profile mlops --out-dir artifacts
metricsthinking audit --target . --profile llmops --out-dir artifacts
metricsthinking audit --target . --profile dataops --out-dir artifacts
metricsthinking audit --target . --profile gitops --out-dir artifacts
metricsthinking audit --target . --profile devsecops --out-dir artifacts
metricsthinking audit --target . --profile sdd --out-dir artifacts
```

### 7.2. Suite de Verificación y Pruebas de Invariantes

```bash
# Ejecutar suite de pruebas unitarias (50 tests)
python -m pytest tests/ -v

# Ejecutar linter estático
ruff check src/ tests/ scripts/
```

---

## 8. Glosario de Dominio

* **Ground Truth:** Evidencia física tangible y contrastable en el repositorio (código fuente real, esquemas compilados, contratos, configuraciones y pruebas) en contraposición a documentación aspiracional.
* **Módulo Canónico:** Una de las 10 etapas del ciclo de vida tecnológico evaluadas para cuantificar el avance real del proyecto.
* **Primitivas Universales de Evidencia:** Clasificación estandarizada en 5 tipos (`config`, `spec`, `pipeline`, `verification`, `implementation`) que previene falsos negativos en proyectos no convencionales.
* **Arquetipo de Dominio:** Disciplina de ingeniería especializada (MLOps, LLMOps, GitOps, etc.) con reglas de evaluación y remediación ad-hoc.
* **Filtro Antifraude:** Lógica de inspección que descarta archivos mock, fixtures de prueba y salidas autogeneradas para impedir inflado de métricas.
* **Roadmap Mermaid LR:** Diagrama horizontal de flujo de ejecución estilizado con clases semánticas de estado (`done`, `active`, `backlog`, `blocked`).

---

## 9. Referencias Académicas y de Ingeniería

1. IEEE Computer Society. *IEEE Standard for Software and System Test Documentation*. IEEE Std 829-2008.
2. Fowler, M. *Continuous Integration*. Addison-Wesley, 2006.
3. Bass, L., Clements, P., & Kazman, R. *Software Architecture in Practice (4th Edition)*. Addison-Wesley Professional, 2021.
4. Skelton, M., & Pais, M. *Team Topologies: Organizing Business and Technology Teams for Fast Flow*. IT Revolution Press, 2019.
5. Forsgren, N., Humble, J., & Kim, G. *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press, 2018.

### Citación BibTeX
```bibtex
@software{metricsthinking_2026,
  author = {HyperScale Thinking Systems},
  title = {MetricsThinking: Universal Technology Project Reverse Engineering and Ground Truth Audit Engine},
  year = {2026},
  version = {3.0.0},
  url = {https://github.com/AlvaroAlejandroFinOps/Metrics}
}
```
