# METRICSTHINKING - iDirectory Architecture v3.0

Framework modular gobernado por **Gravity HyperScale Thinking** con Context Engineering nativo.

> **Protocolo de Ingesta para Agentes (Bootloader):**
> 1. Lee `AGENTS.md` (o `GEMINI.md` / `CLAUDE.md`).
> 2. Lee `.context/tree.json` (Mapa Topológico Satelital de ~250 tokens).
> 3. Lee `01_seed/seed-metricsthinking-master.md` (ADN y Ground Truth del proyecto).
> 4. Lee el `.context.yaml` del directorio objetivo antes de modificar archivos.

## Manifiesto de Directorios y Roles

- **`01_seed/`**: Semilla de proyecto y memoria técnica (ThinkingSeed Master). ADN arquitectónico del sistema. `[Priority: p0]`
- **`02_foundation/engine/`**: Núcleo del framework de automatización, lógica de ruteo, indexación y governance engine. `[Priority: p1]`
- **`03_research/notebooks/`**: Notebooks de desarrollo interactivo (Jupyter/Colab/Fabric/Databricks) para análisis exploratorio (EDA). `[Priority: p2]`
- **`03_research/prompts/`**: Estructuras de prompts para LLMs, system prompts, árboles de contexto y plantillas de inferencia. `[Priority: p1]`
- **`03_research/experiments/`**: Pruebas de concepto (PoCs), prototipos de modelos algorítmicos, benchmarks e I+D. `[Priority: p2]`
- **`src/metricsthinking/`**: Motor principal de auditoría forense, evaluación canónica M01-M10, FPIA Context Engine y CLI/MCP. `[Priority: p0]`
- **`crates/metricsthinking_rs/`**: Motor nativo acelerado en Rust para escaneo de alto rendimiento (PyO3). `[Priority: p1]`
- **`packages/fpai_core/`**: Motor espectral de contexto (migrado a `src/metricsthinking/fpai/`). `[Priority: p2]`
- **`integrations/`**: Integraciones con IDEs y agentes (Claude, Cursor, Copilot, Antigravity). `[Priority: p2]`
- **`artifacts/plans/active/`**: Planes de capacidad activos (F-SKUs), presupuestos cloud vigentes e hitos operativos en curso. `[Priority: p1]`
- **`artifacts/plans/archive/`**: Histórico de planes evaluados, arquitecturas descartadas y documentación obsoleta preservada por trazabilidad. `[Priority: p3]`
- **`docs/architecture/`**: Diagramas de arquitectura multi-cloud, topologías C4 y flujos de datos de las capas Medallion. `[Priority: p1]`
- **`docs/specs/`**: Especificaciones técnicas detalladas, linaje de datos, contratos de esquemas y requerimientos no funcionales. `[Priority: p1]`
- **`docs/notes/`**: Bitácoras de ingeniería, registro de deuda técnica, decisiones rápidas (ADRs) y análisis de causa raíz (RCA). `[Priority: p2]`
- **`config/`**: Parámetros de entorno (dev, staging, prod) y variables de configuración desacopladas. `[Priority: p1]`
- **`data/raw/`**: Zona de aterrizaje local (Bronze) para fuentes puras e inmutables. Ignorado en Git y AI. `[Priority: p3]`
- **`data/processed/`**: Datos transformados localmente (Silver/Gold) en formatos estructurados (Parquet/Delta). `[Priority: p3]`
- **`data/sandbox/`**: Entorno aislado para experimentación de científicos de datos y arquitectos. `[Priority: p3]`
- **`schemas/`**: Definiciones estrictas de esquemas (Avro, JSON Schema, DDL de SQL) para control de deriva de datos. `[Priority: p1]`
- **`scripts/`**: Scripts operativos del sistema operativo (bash, powershell, make) para tareas de mantenimiento. `[Priority: p2]`
- **`tests/`**: Suites de pruebas unitarias, integración y calidad de datos (Great Expectations / pytest). `[Priority: p1]`
- **`.agents/`**: Skills y configuraciones para agentes autónomos. `[Priority: p1]`
- **`logs/`**: Trazas locales de ejecución, auditorías y dumps de errores. `[Priority: p3]`
- **`.context/`**: Directorio de telemetría, esquemas y mapas satelitales de Context Engineering de iDirectory. `[Priority: p0]`
