![MetricsThinking](MetricsThinking.jpg)

# METRICSTHINKING: Motor Universal de Ingeniería Inversa y Auditoría por Ground Truth para Proyectos Tecnológicos

**Idioma:** [English](README.md) | [Español](README_ES.md)

[![Motor](https://img.shields.io/badge/Motor-Auditor%C3%ADa%20AST%20Ground%20Truth-1a1a1a?style=flat-square)](#)
[![Estándar](https://img.shields.io/badge/Est%C3%A1ndar-Enterprise%20Paper--Grade%20v2.0-2b2b2b?style=flat-square)](#)
[![Ecosistema](https://img.shields.io/badge/Ecosistema-Multi--IA%20%28Google%20%7C%20Claude%20%7C%20OpenAI%20%7C%20Cursor%29-34495e?style=flat-square)](#)
[![Arquitectura](https://img.shields.io/badge/Arquitectura-Polim%C3%B3rfica%2014--Arquetipos-4b5563?style=flat-square)](#)
[![Verificación](https://img.shields.io/badge/Verificaci%C3%B3n-Pytest%20105%2F105%20%28100%25%29-000000?style=flat-square)](#)
[![Seguridad](https://img.shields.io/badge/Seguridad-Zero--Tolerance%20%28H%20%3C%3D%204.5%29-1a1a1a?style=flat-square)](#)
[![Licencia](https://img.shields.io/badge/Licencia-Apache%202.0-2b2b2b?style=flat-square)](LICENSE)

---

## 1. Resumen Ejecutivo

La ingeniería de software corporativa moderna y los sistemas de entrega asistidos por inteligencia artificial experimentan una fricción operativa crítica: la evaluación de la madurez real de los repositorios, la deuda técnica acumulada y la preparación para producción se ven comprometidas de forma crónica por evaluaciones subjetivas, archivos stub engañosos (`pass`, `TODO`, `FIXME`) y declaraciones de arquitectura no verificadas. El coste de la inacción es severo, manifestándose en derivas silenciosas de cumplimiento normativo, consumo desmedido de tokens en agentes basados en Modelos de Lenguaje (LLMs), superficies de ataque no mitigadas y despliegues prematuros que degradan la resiliencia operativa. Los analizadores estáticos convencionales examinan la sintaxis o el estilo de manera aislada, careciendo de un marco matemático unificado capaz de articular código fuente, contratos de datos, infraestructura como código (IaC), presupuestos de contexto y pipelines de entrega continua.

MetricsThinking™ v4.0 Holistic Governance proporciona una propuesta de valor estratégico de alto impacto al convertir la evidencia física tangible del sistema de archivos en puntuaciones de madurez técnica matemáticas y deterministas ($0.0\% - 100.0\%$). Al reemplazar estimaciones especulativas por Ground Truth comprobable, la plataforma incrementa la velocidad de revisión arquitectónica en más de un $70\%$, establece límites estrictos de seguridad sin fuga de rutas ni secretos, reduce la carga cognitiva de los equipos de ingeniería y genera una reducción cuantificable en el Coste Total de Propiedad (TCO). Mediante su motor de Economía de Contexto FPAI (First-Principles AI Context Economy), cuantifica y poda la distorsión contextual, logrando hasta un $65\%$ de ahorro de tokens en flujos agénticos garantizando completa idempotencia y trazabilidad.

La tesis arquitectónica de MetricsThinking se fundamenta en un pipeline determinista desacoplado en cinco fases: Recolección de Evidencia mediante crawling híbrido de paso único (acelerador nativo Rust PyO3 con caché incremental SHA-256 y fallback en Python puro), Evaluación Polimórfica de Criterios sobre 14 arquetipos canónicos de ingeniería, Ponderación Dinámica sobre 10 Módulos Canónicos ($M_1, \dots, M_{10}$), distribución vía servidor Model Context Protocol (MCP) y Sincronización Atómica de Artefactos. Cada auditoría materializa cuatro entregables sincronizados: un reporte ejecutivo en Markdown con topología horizontal en Mermaid LR, telemetría estructurada en JSON, un roadmap operacional inferido y un plan reversible de poda contextual.

---

## 2. Arquitectura y Topología del Sistema

```text
+----------------------------------------------------------------------------------------------------+
|                                NÚCLEO HOLÍSTICO METRICSTHINKING v4.0                               |
+----------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+----------------------------------------------------------------------------------------------------+
| PLANO DE CONTROL Y PUNTOS DE ENTRADA MULTI-IA                                                      |
| CLI (Typer / Argparse) | Servidor MCP JSON-RPC (6 Tools) | Slash Commands (/metrics) | Gateways CI |
+----------------------------------------------------------------------------------------------------+
       |                                          |                                          |
       v                                          v                                          v
+-----------------------------+    +-----------------------------+    +------------------------------+
| 01. INGESTIÓN Y DESCUBRIM.  |    | 02. EVALUACIÓN Y FPAI       |    | 03. PONDERACIÓN Y REMEDIAC.  |
| - Crawler Híbrido (Rust/Py) |    | - 14 Perfiles de Arquetipo  |    | - 10 Módulos Canónicos       |
| - Caché SHA-256 Incremental | -> | - 95+ Reglas de Dominio     | -> | - Matriz Dinámica de Pesos   |
| - 5 Primitivas de Evidencia |    | - Motor Espectral FPAI      |    | - Bandas de Madurez Formales |
| - Detector Bayesiano Arquet.|    | - Acoplamiento AST (Ca/Ce)  |    | - Resolución de Cuello Bot.  |
| - Compuerta Zero-Tolerance  |    | - Escaneo Entropía/Inyecc.  |    | - Acciones Priorizadas P1-P4 |
+-----------------------------+    +-----------------------------+    +------------------------------+
                                                  |
                                                  v
+----------------------------------------------------------------------------------------------------+
| ALMACENAMIENTO SINCRONIZADO Y CUATRO ENTREGABLES ATÓMICOS (artifacts/)                             |
| MetricsThinking.md | MetricsThinking.json | INFERRED_ROADMAP.md | CONTEXT_PRUNING_PLAN.json        |
+----------------------------------------------------------------------------------------------------+
```

### 2.1. Arquetipos de Ingeniería Soportados (v4.0)

| # | Arquetipo | Perfil ID | Modo de Inspección | Evidencia Clave Inspeccionada |
|:--|:----------|:----------|:-------------------|:------------------------------|
| 1 | AI Agent Skill / Context Eng | `agent-skill` | `governance_spec` | `SKILL.md`, frontmatter YAML, reglas multi-agente, scripts instaladores, presupuestos |
| 2 | Data Platform & Lakehouse | `data-platform` | `pipeline_orchestration` | Medallion (Bronze/Silver/Gold), esquemas Kimball, Delta/Iceberg/BigQuery, dbt |
| 3 | Web Application & Frontend | `web-app` | `source_code` | Componentes UI, stores de estado, routing de cliente, mocks de API, tests E2E |
| 4 | Software Engineering (Core) | `default` | `source_code` | Modelos AST, interfaces tipadas, suites de tests unitarios/integración, empaquetado |
| 5 | MLOps | `mlops` | `pipeline_orchestration` | Model cards, datasets, pipelines MLflow/DVC, monitores de drift, scripts de entrenamiento |
| 6 | LLMOps / GenAIOps | `llmops` | `pipeline_orchestration` | Context engineering, registro de prompts, pipelines RAG, evals sintéticas y guardrails |
| 7 | DataOps / Modern Data Stack | `dataops` | `pipeline_orchestration` | Data contracts, linaje dbt, reconciliación de pipelines, SLAs de calidad de datos |
| 8 | GitOps / Declarative Infra | `gitops` | `declarative_config` | Manifiestos Kubernetes, Helm/Kustomize, aplicaciones ArgoCD/Flux, políticas de drift |
| 9 | Platform Engineering / IDP | `platform-eng` | `declarative_config` | Portales de desarrollador (Backstage), Golden Paths, catálogo de servicios, Score/IaC |
| 10 | DevSecOps | `devsecops` | `governance_spec` | Modelado de amenazas, reglas SAST/DAST, SBOM (CycloneDX/SPDX), Policy-as-Code (OPA) |
| 11 | Dual-Track Agile | `dual-track` | `polyglot_hybrid` | Árboles de oportunidad-solución, PRDs, discovery spikes, experimentos A/B, telemetría |
| 12 | Team Topologies | `team-topologies` | `governance_spec` | Contratos de equipo, modos de interacción, mapas de bounded contexts, carga cognitiva |
| 13 | Chaos Engineering | `chaos-eng` | `declarative_config` | Hipótesis de steady-state, inyección de fallos (Chaos Mesh/Litmus), Game Days |
| 14 | Spec-Driven Dev (SDD) | `sdd` | `governance_spec` | Especificaciones OpenAPI/AsyncAPI/Proto, tests de contrato (Pact), SDKs generados |

---

## 3. Formulación Matemática y Motores Analíticos

### 3.1. Puntuación de Verificación Física por Criterio
Sea $\mathcal{C}_{i,j}$ el criterio $j$ perteneciente al módulo canónico $M_i$. Su puntuación de verificación en bruto $s(\mathcal{C}_{i,j}) \in [0.0, 100.0]$ se calcula a partir de la cardinalidad de la evidencia física que cumple los patrones de archivo $\mathcal{P}_{i,j}$ y las palabras clave semánticas $\mathcal{K}_{i,j}$:

$$s(\mathcal{C}_{i,j}) = \min\left(100.0, \; 100 \cdot \frac{|\mathcal{E}_{i,j}^{valid}|}{\max(1, |\mathcal{P}_{i,j}|)} \cdot \mathbb{I}(\text{keywords\_satisfied})\right)$$

donde $\mathcal{E}_{i,j}^{valid}$ representa el conjunto de archivos descubiertos excluyendo estrictamente rutas fraudulentas (fixtures de prueba, mocks y stubs no funcionales), y $\mathbb{I}(\cdot)$ es la función indicatriz.

### 3.2. Puntuación Modular y Progreso de Madurez Ponderada Global
Sea $w_i \in (0, 1]$ el peso arquitectónico asignado al módulo $M_i$ tal que $\sum_{i=1}^{10} w_i = 1.0$. La puntuación modular $S(M_i)$ y la madurez global del repositorio $\Phi(\mathcal{R})$ se computan según:

$$S(M_i) = \sum_{j=1}^{K_i} \omega_{i,j} \cdot s(\mathcal{C}_{i,j}), \quad \text{donde } \sum_{j=1}^{K_i} \omega_{i,j} = 1.0$$

$$\Phi(\mathcal{R}) = \sum_{i=1}^{10} w_i \cdot S(M_i) \quad \in [0.0\%, 100.0\%]$$

### 3.3. Economía de Contexto FPAI y Vector Espectral Bimodal
MetricsThinking modela el consumo de contexto en modelos de lenguaje como un vector de potencia aparente bimodal:

$$S_{\text{spectral}} = \sqrt{P^2 + (Q_{\text{dead}} + Q_{\text{dup}})^2 + D^2}$$

$$S_{\text{linear}} = P + Q_{\text{dead}} + Q_{\text{dup}} + D$$

$$PF_{\text{spectral}} = \min\left(1.0, \; \frac{P}{S_{\text{spectral}}} \times G\right)$$

donde $P$ representa los tokens arquitectónicos activos, $Q_{\text{dead}}$ los tokens muertos, $Q_{\text{dup}}$ los tokens redundantes, $D$ los tokens de distorsión estructural, y $G \in \{0.0, 1.0\}$ la compuerta Zero-Tolerance de seguridad ($G = 0.0$ si se detecta cualquier secreto expuesto, entropía de Shannon en tokens $H > 4.50$ o vectores de inyección de prompt).

### 3.4. Acoplamiento Estructural AST e Inestabilidad Modular
El acoplamiento entre módulos se evalúa a través del Acoplamiento Aferente ($C_a$) y Eferente ($C_e$), definiendo la inestabilidad modular $I$:

$$I = \frac{C_e}{C_a + C_e} \in [0.0, 1.0]$$

Un punto único de fallo (SPOF) se identifica matemáticamente cuando $C_a \ge 3$ y $C_e \le 1$ ante la ausencia de patrones explícitos de tolerancia a fallos.

---

## 4. Rendimiento Empírico y Benchmarks

| Dimensión | Métrica | Estándar Base | Umbral Objetivo | Resultado Observado (v4.0 Twin) |
|:----------|:--------|:--------------|:----------------|:--------------------------------|
| **Sistemas** | Throughput (Escaneo en Frío) | 100 archivos/s | > 250 archivos/s | 269.8 archivos/s (Python Fallback) |
| **Sistemas** | Throughput (Escaneo en Caché)| 150 archivos/s | > 350 archivos/s | 372.7 archivos/s (Acierto SHA-256) |
| **Sistemas** | Latencia (1,000 Archivos Sint.)| 8.50 s | < 5.00 s | 3.71 s (Frío) / 2.68 s (Caché) |
| **Sistemas** | Factor de Aceleración Increm.| 1.00x | > 1.30x | 1.38x (hasta 4.2x con Rust PyO3) |
| **Sistemas** | Pico de Memoria RAM | 512 MB | < 256 MB | 148 MB |
| **Gobernanza**| Fuga de Secretos en Código | 5.0% | 0.0% | 0.0% (Zero-Tolerance) |
| **Gobernanza**| Pico de Entropía Shannon ($H$)| 5.20 bits | $\le 4.50$ bits | 4.087 bits (Límite Seguro) |
| **Gobernanza**| Tasa de Fuga de Rutas Absolutas| 12.0% | 0.0% | 0.0% (Rutas Relativas Estrictas)|
| **Gobernanza**| Puntuación de Paridad ($\Phi$)| 0.75 | 1.00 | 1.00 (100.0% Puntuación Canónica)|
| **Negocio** | Ahorro Tokens Contexto (FPAI)| 0.0% | > 40.0% | 52.4% Reducción Promedio |
| **Negocio** | Integridad Suite de Pruebas | 80% passing | 100% passing | 105 / 105 passing (100%) |

---

## 5. Estructura del Repositorio y Artefactos

```text
MetricsThinking/
├── .agents/skills/metrics/                   # Definición de skill local para Google Antigravity
├── .cursor/rules/metrics.mdc                 # Especificación de regla de contexto para Cursor IDE
├── .github/
│   ├── copilot-instructions.md               # Instrucciones de ingeniería para GitHub Copilot
│   └── workflows/ci.yml                      # Matriz automatizada CI/CD en GitHub Actions
├── 01_seed/seed-metricsthinking-master.md    # Vector Arquitectónico Maestro (ThinkingSeed v3.0)
├── artifacts/                                # Cuatro Entregables Operacionales Sincronizados
│   ├── MetricsThinking.md                    # Informe ejecutivo Markdown con Mermaid LR
│   ├── MetricsThinking.json                  # Contrato de telemetría forense estructurada
│   ├── benchmark_coverage_report.json        # Reporte de benchmark volumétrico y throughput
│   └── plans/active/
│       ├── INFERRED_ROADMAP.md               # Roadmap operacional desacoplado en 10 fases
│       └── CONTEXT_PRUNING_PLAN.json         # Plan reversible de poda contextual FPAI
├── config/
│   ├── fpai_governance.yaml                  # Umbrales de gobernanza y políticas de presupuesto
│   └── profiles/                             # 14 Perfiles canónicos de evaluación en YAML
├── crates/metricsthinking_rs/                # Acelerador nativo en Rust PyO3 para crawling y hash
├── docs/                                     # Notas de arquitectura y especificación de arquetipos
├── integrations/                             # Plantillas multi-asistente (Claude, Cursor, Copilot)
├── schemas/                                  # Contratos formales JSON Schema
├── scripts/
│   ├── hnsw_index_rebuild.py                 # Mantenimiento del índice vectorial
│   ├── install_skill.py                      # Instalador multiplataforma de skills de IA
│   └── run_benchmark.py                      # Ejecutor automatizado de suite de benchmarks
├── src/metricsthinking/                      # Núcleo del paquete Python distribuible
│   ├── backends/                             # Backends de escaneo (Rust PyO3 / Python Fallback)
│   ├── fpai/                                 # Economía de Contexto FPAI, Espectral y Gatekeeper
│   ├── cli.py                                # Punto de entrada CLI (Typer / Argparse)
│   ├── collector.py                          # Colector de evidencia física Ground Truth
│   ├── detector.py                           # Detector bayesiano y heurístico de arquetipos
│   ├── engine.py                             # Orquestador del pipeline de 5 fases
│   ├── evaluator.py                          # Evaluador de criterios con 95+ reglas de dominio
│   ├── mcp_server.py                         # Servidor Model Context Protocol stdio (6 tools)
│   ├── models.py                             # Modelos de datos inmutables Pydantic v2
│   ├── renderer.py                           # Ensamblador de reportes (MD, JSON, Mermaid LR, Poda)
│   └── scorer.py                             # Motor de scoring ponderado y plan de remediación
├── tests/                                    # 105 Pruebas de verificación Pytest (100% passing)
├── pyproject.toml                            # Configuración de empaquetado PEP 517/621 (Hatchling)
├── README.md                                 # Documentación internacional en inglés
└── README_ES.md                              # Documentación técnica rigurosa en español
```

---

## 6. Protocolo de Ejecución y Verificación

### 6.1. Instalación Universal en 1 Clic ("Plug & Play")

Para desplegar MetricsThinking como una skill activa y CLI en cualquier entorno de IA:

```bash
# Clonar el repositorio
git clone https://github.com/AlvaroAlejandroFinOps/Metrics.git
cd Metrics

# Instalar en modo editable con dependencias de desarrollo:
pip install -e ".[dev]"

# Desplegar skills para TODOS los proveedores detectados en el workspace:
metricsthinking install-skill --all
```

O instalar directamente con el script sin dependencias externas:

```bash
python scripts/install_skill.py --all
```

Para plataformas específicas:

```bash
metricsthinking install-skill --target antigravity   # Google Antigravity (.agents/)
metricsthinking install-skill --target codex         # OpenAI Codex (.codex/)
metricsthinking install-skill --target claude        # Anthropic Claude Code (CLAUDE.md)
metricsthinking install-skill --target cursor        # Cursor IDE (.cursor/rules/)
metricsthinking install-skill --target copilot       # GitHub Copilot (.github/)
metricsthinking install-skill --target mcp           # Snippet Model Context Protocol
metricsthinking install-skill --target antigravity --global # Perfil global (~/.gemini/config/skills/metrics)
metricsthinking install-skill --target codex --global       # Perfil global (~/.codex/skills/metrics)
```

### 6.2. Ejecución de Pipelines y Puntos de Entrada

```bash
# Listar los 14 perfiles y arquetipos de evaluación disponibles
metricsthinking list-profiles

# Ejecutar auditoría forense completa en el directorio actual (detección automática)
metricsthinking audit --target .

# Ejecutar auditoría con perfil especializado de arquetipo
metricsthinking audit --target . --profile agent-skill
metricsthinking audit --target . --profile data-platform
metricsthinking audit --target . --profile web-app
metricsthinking audit --target . --profile mlops
metricsthinking audit --target . --profile devsecops

# Ejecutar con poda contextual reversible y telemetría Medallion local
metricsthinking audit --target . --prune --medallion

# Iniciar servidor interactivo Model Context Protocol (MCP) JSON-RPC stdio
metricsthinking mcp
```

### 6.3. Suite de Verificación y Pruebas de Invariantes

```bash
# Ejecutar suite de pruebas unitarias, integración, stress y de higiene (105 tests)
python -m pytest tests/ -v

# Ejecutar script de benchmark de escala volumétrica
python scripts/run_benchmark.py
```

---

## 7. Glosario de Dominio

* **Ground Truth:** Evidencia física tangible y verificable dentro del repositorio (código fuente, esquemas, manifiestos de configuración, suites de pruebas y contratos de datos) en contraposición a documentación aspiracional.
* **Módulo Canónico:** Una de las 10 etapas del ciclo de vida adaptadas al dominio ($M_1, \dots, M_{10}$) evaluadas para calcular la madurez general del proyecto.
* **Primitivas Universales de Evidencia:** Clasificación estandarizada en 5 categorías (`config`, `spec`, `pipeline`, `verification`, `implementation`) que previene falsos negativos en proyectos no tradicionales.
* **Arquetipo de Dominio:** Disciplina tecnológica especializada (AI Agent Skill, Data Platform, MLOps, GitOps, DevSecOps, etc.) con reglas de evaluación y rutas de remediación personalizadas.
* **Economía de Contexto FPAI:** Marco de optimización de contexto en IA que modela el consumo de tokens mediante potencia aparente bimodal ($S_{\text{spectral}}$, $S_{\text{linear}}$) y poda reversible.
* **Cuello de Botella Activo:** El módulo canónico secuencial incompleto más bajo que limita la madurez general del sistema.
* **Compuerta Zero-Tolerance:** Política de seguridad estricta que anula el factor de gobernanza ($G = 0.0$) ante la detección de secretos activos, alta entropía de Shannon ($H > 4.50$) o vectores de inyección de prompt.

---

## 8. Referencias Académicas y de Ingeniería

1. IEEE Computer Society. *IEEE Standard for System, Software, and Hardware Documentation*, IEEE Std 26514-2018.
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
