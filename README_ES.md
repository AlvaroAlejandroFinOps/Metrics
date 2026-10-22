![alt text](MetricsThinking.jpg)
# METRICSTHINKING: Motor Universal de Ingeniería Inversa y Auditoría por Ground Truth para Proyectos Tecnológicos 

**Idioma:** [English](README.md) | [Español](README_ES.md)

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-1a1a1a?style=flat-square&logo=python)](https://python.org)
[![Versión](https://img.shields.io/badge/Versi%C3%B3n-4.0.0%20Gobernanza%20Hol%C3%ADstica-2b2b2b?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Arquitectura](https://img.shields.io/badge/Arquitectura-Polim%C3%B3rfica%2014--Arquetipos-2b2b2b?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Verificación](https://img.shields.io/badge/Verificaci%C3%B3n-Pytest%2094%2F94%20(100%25)-34495e?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Motor](https://img.shields.io/badge/Motor-Auditor%C3%ADa%20AST%20Ground%20Truth-1a1a1a?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Seguridad](https://img.shields.io/badge/Seguridad-Zero--Tolerance%20(H%20%3C%3D%204.5)-27ae60?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Licencia](https://img.shields.io/badge/Licencia-Apache%202.0-4b5563?style=flat-square)](LICENSE)

---

## 1. Resumen Ejecutivo

**MetricsThinking™ v4.0 Holistic Governance** es un motor empresarial de análisis estático, ingeniería inversa y gobernanza de proyectos diseñado para computar la madurez matemática formal de repositorios tecnológicos a través de **14 Arquetipos de Ingeniería**. En la ingeniería de software moderna asistida por IA y desarrollada por equipos multidisciplinarios o agentes autónomos, la evaluación del avance real frecuentemente se ve distorsionada por sesgos cognitivos, archivos stub engañosos y declaraciones arquitectónicas no verificadas. MetricsThinking resuelve esta tensión ejecutando una inspección exhaustiva de evidencia física tangible (Ground Truth) en el sistema de archivos, árboles de sintaxis abstracta (AST), suites de pruebas, manifiestos de contenedores, contratos de datos y pipelines de automatización CI/CD.

El motor desacopla cualquier proyecto tecnológico en una matriz adaptada al dominio compuesta por 10 Módulos Canónicos ($M_1, \dots, M_{10}$). Cada módulo evalúa un conjunto parametrizado de criterios frente a la presencia de archivos físicos, densidad de tokens sintácticos e invariantes semánticos clasificados en **5 Primitivas Universales de Evidencia** (`config`, `spec`, `pipeline`, `verification`, `implementation`). El pipeline de scoring calcula un porcentaje ponderado y determinista de completitud ($0.0\% - 100.0\%$), clasifica el código en bandas estandarizadas de madurez y genera **cuatro entregables sincronizados**: telemetría en JSON, un informe ejecutivo en Markdown con un diagrama de flujo horizontal Mermaid LR sin anidamientos conflictivos, un roadmap de implementación operacional inferido y un plan reversible de poda contextual (Economía de Contexto FPAI).

---

## 2. Arquetipos de Ingeniería Soportados (v4.0)

MetricsThinking™ v4.0 soporta nativamente 14 disciplinas tecnológicas mediante perfiles YAML desacoplados:

| # | Arquetipo | Perfil ID | Modo de Inspección | Evidencia Clave Inspeccionada |
|:--|:----------|:----------|:-------------------|:------------------------------|
| 1 | **AI Agent Skill / Context Eng** | `agent-skill` | `governance_spec` | `SKILL.md`, frontmatter YAML, multi-agent rules, scripts instaladores, presupuestos de tokens |
| 2 | **Data Platform & Lakehouse** | `data-platform` | `pipeline_orchestration` | Medallion (Bronze/Silver/Gold), Kimball, Delta/Iceberg/BigQuery, dbt, SLAs |
| 3 | **Web Application & Frontend** | `web-app` | `source_code` | Componentes UI, stores de estado, routing de cliente, mocks de API, tests visuales/E2E |
| 4 | **Software Engineering (Core)** | `default` | `source_code` | Modelos AST, interfaces tipadas, suites de tests unitarios/integración, manifiestos |
| 5 | **MLOps** | `mlops` | `pipeline_orchestration` | Model cards, datasets, pipelines MLflow/DVC, monitores de drift, scripts de entrenamiento |
| 6 | **LLMOps / GenAIOps** | `llmops` | `pipeline_orchestration` | Context engineering, registro de prompts, pipelines RAG, evals sintéticas y guardrails |
| 7 | **DataOps / MDS** | `dataops` | `pipeline_orchestration` | Data contracts, linaje dbt, reconciliación, SLAs de datos |
| 8 | **GitOps / Declarative Infra** | `gitops` | `declarative_config` | Manifiestos Kubernetes, Helm/Kustomize, aplicaciones ArgoCD/Flux, políticas de drift |
| 9 | **Platform Engineering / IDP** | `platform-eng` | `declarative_config` | Portales de desarrollador (Backstage), Golden Paths, catálogo de servicios, Score/IaC |
| 10 | **DevSecOps** | `devsecops` | `governance_spec` | Modelado de amenazas, reglas SAST/DAST, SBOM (CycloneDX/SPDX), Policy-as-Code (OPA/Kyverno) |
| 11 | **Dual-Track Agile** | `dual-track` | `polyglot_hybrid` | Árboles de oportunidad-solución, PRDs, discovery spikes, experimentos A/B, telemetría |
| 12 | **Team Topologies** | `team-topologies` | `governance_spec` | Contratos de equipo, modos de interacción, mapas de bounded contexts, carga cognitiva |
| 13 | **Chaos Engineering** | `chaos-eng` | `declarative_config` | Hipótesis de steady-state, experimentos de inyección de fallos (Chaos Mesh/Litmus), Game Days |
| 14 | **Spec-Driven Dev (SDD)** | `sdd` | `governance_spec` | Especificaciones OpenAPI/AsyncAPI/Proto, tests de contrato (Pact), SDKs generados, mocks |

---

## 3. Arquitectura y Topología del Sistema

```text
+----------------------------------------------------------------------------------------------------+
|                                NÚCLEO HOLÍSTICO METRICSTHINKING v4.0                               |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  +---------------------------+       +----------------------------+       +---------------------+  |
|  |    01. EvidenceCollector  | ----> |    02. CriteriaEvaluator   | ----> |   03. AuditScorer   |  |
|  |  - Rust PyO3 / Python Fall|       |  - Despacho Polimórfico    |       |  - Pesos Dinámicos  |  |
|  |  - 5 Primitivas Evidencia |       |  - 14 Perfiles de Dominio  |       |  - Bandas de Madurez|  |
|  |  - Caché SHA-256 Increm.  |       |  - Motor Espectral FPAI    |       |  - Plan Remediación |  |
|  |  - Zero-Tolerance Gate    |       |  - Acoplamiento AST (Ca/Ce)|       |  - Cuello de Botella|  |
|  +---------------------------+       +----------------------------+       +---------------------+  |
|               |                                                                      |             |
|               v                                                                      v             |
|  +---------------------------+                                            +---------------------+  |
|  |   ProjectEvidence (DTO)   |                                            |  ProjectAuditReport |  |
|  +---------------------------+                                            +---------------------+  |
|                                                                                      |             |
|                                                                                      v             |
|                                      +----------------------------+       +---------------------+  |
|                                      |   05. Sincronización Multi | <---- | 04. ReportRenderer  |  |
|                                      |  - Carpeta artifacts/      |       |  - MetricsThinking. |  |
|                                      |  - Despliegue Multi-AI     |       |    md / .json       |  |
|                                      |  - Servidor MCP JSON-RPC   |       |  - Mermaid LR flow  |  |
|                                      |  - Gateways de CI/CD       |       |  - INFERRED_ROADMAP |  |
|                                      |  - Plan de Poda Reversible |       |  - PRUNING_PLAN.json|  |
|                                      +----------------------------+       +---------------------+  |
+----------------------------------------------------------------------------------------------------+
```

---

## 4. Formulación Matemática y Motores Analíticos

### 4.1. Cálculo de Puntuación por Criterio
Sea $\mathcal{C}_{i,j}$ el criterio $j$ dentro del módulo $M_i$. Su puntuación $s(\mathcal{C}_{i,j}) \in [0, 100]$ se computa por la presencia de evidencia física que satisfaga los patrones $\mathcal{P}_{i,j}$ y las palabras clave semánticas $\mathcal{K}_{i,j}$:

$$s(\mathcal{C}_{i,j}) = \min\left(100.0, \; 100 \cdot \frac{|\mathcal{E}_{i,j}^{valid}|}{\max(1, |\mathcal{P}_{i,j}|)} \cdot \mathbb{I}(\text{keywords\_satisfied})\right)$$

donde $\mathcal{E}_{i,j}^{valid}$ representa el conjunto de archivos descubiertos excluyendo rutas antifraude (stubs, fixtures y logs automáticos).

### 4.2. Puntuación Modular y Madurez Global Ponderada
Sea $w_i \in (0, 1]$ el peso asignado al módulo $M_i$ con $\sum_{i=1}^{10} w_i = 1.0$. La puntuación $S(M_i)$ y la madurez global $\Phi(\mathcal{R})$ se calculan como:

$$S(M_i) = \sum_{j=1}^{K_i} \omega_{i,j} \cdot s(\mathcal{C}_{i,j}), \quad \text{donde } \sum_{j=1}^{K_i} \omega_{i,j} = 1.0$$

$$\Phi(\mathcal{R}) = \sum_{i=1}^{10} w_i \cdot S(M_i) \quad \in [0.0\%, 100.0\%]$$

### 4.3. Economía de Contexto FPAI y Potencia Espectral
MetricsThinking v4.0 modela el consumo de contexto en LLMs como un vector de potencia aparente bimodal:

$$S_{\text{spectral}} = \sqrt{P^2 + (Q_{\text{dead}} + Q_{\text{dup}})^2 + D^2}$$

$$S_{\text{linear}} = P + Q_{\text{dead}} + Q_{\text{dup}} + D$$

$$PF_{\text{spectral}} = \min\left(1.0, \frac{P}{S_{\text{spectral}}} \times G\right)$$

donde $P$ son tokens arquitectónicos activos, $Q$ tokens muertos o duplicados, $D$ distorsión estructural y $G \in \{0, 1\}$ la compuerta Zero-Tolerance de seguridad ($G=0$ si se detecta cualquier secreto expuesto, entropía $H > 4.5$ o vector de inyección de prompt).

---

## 5. Estructura del Repositorio

```text
./
├── .agents/skills/metrics/                   # Definición de skill para Google Antigravity
├── .cursor/rules/metrics.mdc                 # Regla forense para Cursor IDE
├── .github/
│   ├── copilot-instructions.md               # Instrucciones para GitHub Copilot
│   └── workflows/ci.yml                      # Matriz automatizada CI/CD en GitHub Actions
├── 01_seed/seed-metricsthinking-master.md    # Vector Arquitectónico Maestro (ThinkingSeed v3.0)
├── artifacts/                                # Cuatro Entregables Sincronizados
│   ├── MetricsThinking.md                    # Reporte ejecutivo Markdown con Mermaid LR
│   ├── MetricsThinking.json                  # Telemetría forense completa en JSON
│   └── plans/active/
│       ├── INFERRED_ROADMAP.md               # Roadmap operacional desacoplado en 10 fases
│       └── CONTEXT_PRUNING_PLAN.json         # Plan reversible de poda de contexto FPAI
├── config/
│   ├── fpai_governance.yaml                  # Umbrales de gobernanza y presupuestos de tokens
│   └── profiles/                             # 14 Perfiles canónicos de evaluación en YAML
├── crates/metricsthinking_rs/                # Acelerador nativo en Rust PyO3 (opcional)
├── integrations/                             # Plantillas para asistentes (Claude, Cursor, Copilot)
├── schemas/                                  # Contratos formales JSON Schema
├── scripts/
│   └── install_skill.py                      # Instalador multiplataforma de skills de IA
├── src/metricsthinking/                      # Paquete Python distribuible
│   ├── backends/                             # Crawling con backend Rust PyO3 / Python Fallback
│   ├── fpai/                                 # Economía de Contexto FPAI y Security Gatekeeper
│   ├── cli.py                                # Punto de entrada CLI (Typer / Argparse)
│   ├── collector.py                          # Colector de evidencia física Ground Truth
│   ├── engine.py                             # Orquestador del pipeline de 5 fases
│   ├── evaluator.py                          # Evaluador de criterios con 95+ reglas
│   ├── mcp_server.py                         # Servidor Model Context Protocol stdio (6 tools)
│   ├── models.py                             # Modelos Pydantic v2 inmutables
│   ├── renderer.py                           # Ensamblador de reportes (MD, JSON, Mermaid LR, Poda)
│   └── scorer.py                             # Motor de cálculo ponderado y plan de remediación
├── tests/                                    # 94 Pruebas de verificación Pytest (100% passing)
├── pyproject.toml                            # Empaquetado PEP 517/621 (Hatchling)
├── README.md                                 # Documentación internacional en inglés
└── README_ES.md                              # Documentación técnica rigurosa en español
```

---

## 6. Instalación de la Skill en Proveedores de IA

MetricsThinking se instala de manera inmediata como una herramienta activa en los principales asistentes de IA:

### 6.1. Instalación Rápida por CLI
```bash
# Clonar el repositorio
git clone https://github.com/AlvaroAlejandroFinOps/Metrics.git
cd Metrics

# Instalar en modo editable con dependencias de desarrollo:
pip install -e ".[dev]"

# Instalar la skill en TODOS los proveedores detectados en el workspace:
metricsthinking install-skill --all
```

O instalar directamente con el script sin necesidad de instalación pip previa:
```bash
python scripts/install_skill.py --all
```

### 6.2. Instalación por Proveedor Específico
```bash
metricsthinking install-skill --target antigravity   # Google Antigravity (.agents/)
metricsthinking install-skill --target claude        # Anthropic Claude Code (CLAUDE.md)
metricsthinking install-skill --target cursor        # Cursor IDE (.cursor/rules/)
metricsthinking install-skill --target copilot       # GitHub Copilot (.github/)
metricsthinking install-skill --target mcp           # Snippet Model Context Protocol
```

### 6.3. Instalación Global en Google Antigravity
Para disponibilizar la skill `/metrics` globalmente en cualquier proyecto de Antigravity:
```bash
metricsthinking install-skill --target antigravity --global
```

### 6.4. Integración con Model Context Protocol (MCP)
Inicia el servidor interactivo estándar JSON-RPC stdio:
```bash
metricsthinking mcp
```
Agrégalo en la configuración `mcp_config.json` de Claude Desktop o Cursor:
```json
{
  "mcpServers": {
    "metricsthinking": {
      "command": "python",
      "args": ["-m", "metricsthinking.mcp_server"]
    }
  }
}
```

---

## 7. Protocolo de Ejecución y Verificación

### 7.1. Ejecución de Auditorías Forenses
```bash
# Listar los 14 perfiles y arquetipos disponibles
metricsthinking list-profiles

# Ejecutar auditoría completa en el directorio actual
metricsthinking audit --target .

# Ejecutar con un perfil especializado de arquetipo
metricsthinking audit --target . --profile agent-skill
metricsthinking audit --target . --profile data-platform
metricsthinking audit --target . --profile web-app
metricsthinking audit --target . --profile mlops
metricsthinking audit --target . --profile devsecops

# Ejecutar con poda contextual reversible y telemetría Medallion local
metricsthinking audit --target . --prune --medallion
```

### 7.2. Suite de Pruebas y Verificación de Invariantes
```bash
# Ejecutar suite de pruebas unitarias, integración, stress y de higiene (94 tests)
python -m pytest tests/ -v

# Verificación de sintaxis y tipado estático
ruff check .
```

---

## 8. Referencias Académicas y de Ingeniería

1. IEEE Computer Society. *IEEE Standard for Software and System Test Documentation*. IEEE Std 829-2008.
2. Shannon, C. E. *A Mathematical Theory of Communication*. Bell System Technical Journal, 1948.
3. Fowler, M. *Continuous Integration*. Addison-Wesley, 2006.
4. Bass, L., Clements, P., & Kazman, R. *Software Architecture in Practice (4th Edition)*. Addison-Wesley Professional, 2021.
5. Skelton, M., & Pais, M. *Team Topologies: Organizing Business and Technology Teams for Fast Flow*. IT Revolution Press, 2019.
6. Forsgren, N., Humble, J., & Kim, G. *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press, 2018.

### Citación BibTeX
```bibtex
@software{metricsthinking_2026,
  author = {HyperScale Thinking Systems},
  title = {MetricsThinking: Universal Technology Project Reverse Engineering and Ground Truth Audit Engine},
  year = {2026},
  version = {4.0.0},
  url = {https://github.com/AlvaroAlejandroFinOps/Metrics}
}
```
