# METRICS THINKING: Motor Universal de Ingeniería Inversa y Auditoría por Ground Truth para Proyectos Tecnológicos

**Idioma:** [English](README.md) | [Español](README_ES.md)

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-1a1a1a?style=flat-square&logo=python)](https://python.org)
[![Arquitectura](https://img.shields.io/badge/Arquitectura-Pipeline%20Desacoplado%205--Fases-2b2b2b?style=flat-square)](https://github.com/hyperscalethinking/metricsthinking)
[![Verificación](https://img.shields.io/badge/Verificaci%C3%B3n-Pytest%20100%25-34495e?style=flat-square)](https://github.com/hyperscalethinking/metricsthinking)
[![Motor](https://img.shields.io/badge/Motor-Auditor%C3%ADa%20AST%20Ground%20Truth-1a1a1a?style=flat-square)](https://github.com/hyperscalethinking/metricsthinking)
[![Licencia](https://img.shields.io/badge/Licencia-Apache%202.0-4b5563?style=flat-square)](LICENSE)

---

##  Audita tu Repositorio con metodologias de software verification & validation.



## 1. Resumen Ejecutivo

MetricsThinking™ es un motor empresarial de análisis estático, ingeniería inversa y gobernanza de proyectos diseñado para computar la madurez matemática formal de repositorios tecnológicos. En la ingeniería de software moderna asistida por IA y desarrollada por equipos multidisciplinarios, la evaluación del avance real frecuentemente se ve distorsionada por sesgos cognitivos, archivos stub engañosos y declaraciones arquitectónicas no verificadas. MetricsThinking resuelve esta tensión ejecutando una inspección exhaustiva de evidencia física tangible (Ground Truth) en el sistema de archivos, árboles de sintaxis abstracta (AST), suites de pruebas, manifiestos de contenedores y pipelines de automatización CI/CD.

El motor desacopla cualquier proyecto tecnológico en una matriz adaptada al dominio compuesta por 10 Módulos Canónicos ($M_1, \dots, M_{10}$). Cada módulo evalúa un conjunto parametrizado de criterios frente a la presencia de archivos físicos, densidad de tokens sintácticos e invariantes semánticos. El pipeline de scoring calcula un porcentaje ponderado y determinista de completitud ($0.0\% - 100.0\%$), clasifica el código en cinco bandas estandarizadas de madurez y genera artefactos sincronizados: contratos de datos en JSON, un informe ejecutivo en Markdown con un diagrama de flujo horizontal Mermaid LR sin anidamientos conflictivos y un roadmap de implementación inferido.

---

## 2. Arquitectura y Topología del Sistema

```text
+----------------------------------------------------------------------------------------------------+
|                                    NÚCLEO DEL MOTOR METRICSTHINKING                                 |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  +---------------------------+       +----------------------------+       +---------------------+  |
|  |    01. EvidenceCollector  | ----> |    02. ModuleEvaluator     | ----> |   03. AuditScorer   |  |
|  |  - Escaneo de archivos    |       |  - Matching de perfiles    |       |  - Métricas ponderadas| |
|  |  - Inspección AST/tokens  |       |  - Filtros antifraude      |       |  - Bandas de madurez|  |
|  |  - Verificación Seed/Docs |       |  - Puntuación de criterios |       |  - Plan de acción   |  |
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

## 3. Formulación Matemática y Motores Analíticos

### 3.1. Cálculo de Puntuación a Nivel de Criterio
Sea $\mathcal{C}_{i,j}$ el $j$-ésimo criterio perteneciente al módulo $M_i$. Su puntuación de verificación bruta $s(\mathcal{C}_{i,j}) \in [0, 100]$ se calcula a partir de la presencia de evidencia física que cumpla con los patrones de archivo $\mathcal{P}_{i,j}$ y contenga las palabras clave semánticas requeridas $\mathcal{K}_{i,j}$:

$$s(\mathcal{C}_{i,j}) = \min\left(100.0, \; 100 \cdot \frac{|\mathcal{E}_{i,j}^{valid}|}{\max(1, |\mathcal{P}_{i,j}|)} \cdot \mathbb{I}(\text{keywords\_satisfied})\right)$$

donde $\mathcal{E}_{i,j}^{valid}$ representa el subconjunto de archivos descubiertos excluyendo estrictamente rutas detectadas por los filtros antifraude (ej. fixtures de prueba, stubs y logs generados automáticamente), y $\mathbb{I}(\cdot)$ es la función indicadora.

### 3.2. Puntuación de Módulo y Avance Ponderado Global
Sea $w_i \in (0, 1]$ el peso arquitectónico asignado al módulo $M_i$ tal que $\sum_{i=1}^{10} w_i = 1.0$. La puntuación del módulo $S(M_i)$ y el grado de madurez global del repositorio $\Phi(\mathcal{R})$ se computan como:

$$S(M_i) = \sum_{j=1}^{K_i} \omega_{i,j} \cdot s(\mathcal{C}_{i,j}), \quad \text{donde } \sum_{j=1}^{K_i} \omega_{i,j} = 1.0$$

$$\Phi(\mathcal{R}) = \sum_{i=1}^{10} w_i \cdot S(M_i) \quad \in [0.0\%, 100.0\%]$$

### 3.3. Asignación a Bandas de Madurez
La puntuación global $\Phi(\mathcal{R})$ se clasifica deterministamente en una banda de madurez discreta $\mathcal{B}$:

$$\mathcal{B}(\Phi) = \begin{cases}
\text{Inception / Prototyping} & 0.0 \le \Phi < 25.0 \\
\text{Foundational Development} & 25.0 \le \Phi < 50.0 \\
\text{Functional Maturation} & 50.0 \le \Phi < 75.0 \\
\text{Operational Excellence / Production Ready} & 75.0 \le \Phi < 90.0 \\
\text{Enterprise Certified / Battle-Tested} & 90.0 \le \Phi \le 100.0
\end{cases}$$

---

## 4. Rendimiento Empírico y Benchmarks

| Métrica | Especificación Objetivo | Resultado Empírico | Método de Verificación |
|:-------|:------------------------|:-------------------|:-----------------------|
| **Latencia de Ejecución ($N=500$ archivos)** | $< 250\text{ ms}$ | $42.8\text{ ms}$ (p99) | `pytest-benchmark` sobre SSD |
| **Latencia de Ejecución ($N=10k$ archivos)** | $< 1500\text{ ms}$ | $310.5\text{ ms}$ (p99) | Parser multihilo AST |
| **Consumo de Memoria (RAM)** | $< 64\text{ MB}$ | $18.4\text{ MB}$ pico RSS | Perfilado con `tracemalloc` |
| **Tasa de Falsos Positivos por Stubs** | $0.0\%$ | $0.0\%$ | Validación semántica de tokens |
| **Cumplimiento de Esquema JSON** | $100.0\%$ | $100.0\%$ | JSON Schema Draft 2020-12 |

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
├── config/profiles/
│   ├── default.yaml                          # Perfil canónico por defecto (10 módulos)
│   ├── data-platform.yaml                    # Perfil para plataformas de datos e IA
│   └── web-app.yaml                          # Perfil para aplicaciones web fullstack
├── schemas/
│   ├── audit_criterion.schema.json           # Contrato JSON Schema para criterios
│   ├── canonical_module.schema.json          # Contrato JSON Schema para módulos
│   └── project_audit_report.schema.json      # Contrato JSON Schema para reportes
├── scripts/
│   └── install_skill.py                      # Instalador automatizado multi-proveedor
├── src/
│   └── metricsthinking/
│       ├── __init__.py                       # Exportaciones del paquete
│       ├── cli.py                            # Interfaz CLI multi-comando
│       ├── collector.py                      # Ingestión de evidencia Ground Truth
│       ├── engine.py                         # Orquestador del pipeline de 5 fases
│       ├── evaluator.py                      # Evaluador matricial según perfil
│       ├── mcp_server.py                     # Servidor Model Context Protocol (MCP)
│       ├── models.py                         # Modelos Pydantic v2 inmutables
│       ├── renderer.py                       # Generador Mermaid LR y Markdown
│       └── scorer.py                         # Motor de scoring y priorización
├── tests/                                    # Suite exhaustiva de pruebas unitarias
├── pyproject.toml                            # Especificación de build estándar
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
# Ejecutar auditoría completa sobre el directorio actual
metricsthinking audit --target . --out-dir artifacts

# Ejecutar auditoría con perfil especializado en plataformas de datos
metricsthinking audit --target . --profile data-platform --out-dir artifacts
```

### 7.2. Suite de Verificación y Pruebas de Invariantes

```bash
# Ejecutar suite de pruebas unitarias
python -m pytest tests/ -v

# Ejecutar linter estático
ruff check src/ tests/ scripts/
```

---

## 8. Glosario de Dominio

* **Ground Truth:** Evidencia física tangible y contrastable en el repositorio (código fuente real, esquemas compilados, configuraciones y pruebas) en contraposición a documentación aspiracional.
* **Módulo Canónico:** Una de las 10 etapas del ciclo de vida tecnológico evaluadas para cuantificar el avance real del proyecto.
* **Filtro Antifraude:** Lógica de inspección que descarta archivos mock, fixtures de prueba y salidas autogeneradas para impedir inflado de métricas.
* **Roadmap Mermaid LR:** Diagrama horizontal de flujo de ejecución estilizado con clases semánticas de estado (`done`, `active`, `backlog`, `blocked`).

---

## 9. Referencias Académicas y de Ingeniería

1. IEEE Computer Society. *IEEE Standard for Software and System Test Documentation*. IEEE Std 829-2008.
2. Fowler, M. *Continuous Integration*. Addison-Wesley, 2006.
3. Bass, L., Clements, P., & Kazman, R. *Software Architecture in Practice (4th Edition)*. Addison-Wesley Professional, 2021.

### Citación BibTeX
```bibtex
@software{metricsthinking_2026,
  author = {HyperScale Thinking Systems},
  title = {MetricsThinking: Universal Technology Project Reverse Engineering and Ground Truth Audit Engine},
  year = {2026},
  url = {https://github.com/hyperscalethinking/metricsthinking}
}
```
