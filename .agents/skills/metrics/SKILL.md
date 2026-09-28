---
name: metrics
description: >-
  Auditor universal de proyectos tecnológicos basado en evidencia física estricta (Ground Truth) y la
  metodología de 10 módulos canónicos adaptados al dominio (MetricsThinking™ v3.0). Soporta 10 arquetipos
  de ingeniería (MLOps, LLMOps, DataOps, GitOps, Platform Engineering, DevSecOps, Dual-Track Agile,
  Team Topologies, Chaos Engineering y SDD). Evalúa objetivamente el grado de madurez matemática (0-100%),
  genera el roadmap visual en Mermaid LR y materializa tres artefactos sincronizados (MetricsThinking.json,
  MetricsThinking.md e INFERRED_ROADMAP.md). Se activa con /metrics.
---

# MetricsThinking™: Auditor Forense Universal de Proyectos e Ingeniería Inversa (/metrics)

Esta habilidad permite al agente actuar como **Lead Systems & AI Architect y Auditor de Gobernanza de Proyectos** en Google Antigravity, ejecutando auditorías profundas por **ingeniería inversa** basadas en evidencia física estricta (**Ground Truth First**) y generando roadmaps de ejecución interactivos.

---

## 1. Misión y Cuándo Activar

- Al invocar `/metrics` o `/metrics <ruta-del-proyecto>`.
- Al solicitar auditar la madurez, avance real, deuda técnica o calidad de cualquier repositorio de software, datos, IA, plataformas o infraestructura.
- Para diagnosticar el cuello de botella inmediato y derivar el roadmap de ejecución operacional desacoplado en 10 etapas adaptadas al arquetipo de ingeniería.

---

## 2. Los 10 Arquetipos de Ingeniería Soportados (v3.0)

| Arquetipo | Perfil YAML | Modo de Inspección | Foco Principal |
|:---|:---|:---|:---|
| **Software Engineering** | `default` | `source_code` | AST, modelos canónicos, suites de tests, empaquetado |
| **MLOps** | `mlops` | `pipeline_orchestration` | Model registries, data drift, pipelines de entrenamiento, model cards |
| **LLMOps / GenAIOps** | `llmops` | `pipeline_orchestration` | Context engineering, prompt registry, eval suites, guardrails |
| **DataOps / MDS** | `dataops` | `pipeline_orchestration` | Data contracts, linaje dbt, reconciliación, SLAs de datos |
| **GitOps / K8s** | `gitops` | `declarative_config` | Manifiestos K8s/Helm, ArgoCD/Flux, drift detection, immutable releases |
| **Platform Engineering** | `platform-eng` | `declarative_config` | Service catalog (Backstage), Golden Paths, módulos IaC, portal DevEx |
| **DevSecOps** | `devsecops` | `governance_spec` | Policy-as-Code (OPA/Rego), escaneo de secretos, SBOM, SAST/DAST |
| **Dual-Track Agile** | `dual-track` | `polyglot_hybrid` | Opportunity trees, tarjetas de hipótesis, feature flags, discovery |
| **Team Topologies** | `team-topologies` | `governance_spec` | Team APIs, límites de dominio (DDD), carga cognitiva, modos de interacción |
| **Chaos Engineering** | `chaos-eng` | `declarative_config` | Steady-state hypothesis, inyección de fallos, blast radius, Game Days |
| **Spec-Driven Dev** | `sdd` | `governance_spec` | OpenAPI/AsyncAPI, CodeGen automático, Spectral linting, mock servers |

---

## 3. Los Tres Artefactos Sincronizados

Toda auditoría de MetricsThinking™ materializa físicamente tres entregables:
1. **`artifacts/MetricsThinking.json`**: Telemetría completa, metadatos del repositorio, arquetipo de dominio, primitivas de evidencia universal y criterios evaluados con rutas de archivo.
2. **`artifacts/MetricsThinking.md`**: Reporte ejecutivo formal con resumen de primitivas, tabla de módulos canónicos, roadmap visual Mermaid LR optimizado y plan de remediación priorizado (P1 a P4).
3. **`artifacts/plans/active/INFERRED_ROADMAP.md`**: Roadmap operacional desacoplado en 10 fases con checklists interactivos (`[x]` confirmados en código/manifiestos, `[ ]` pendientes inferidos) y entregables tangibles.

---

## 4. Protocolo de Ejecución en 5 Fases

### FASE 1: Ingeniería Inversa y Reconciliación de Verdad (Ground Truth)
- Inspecciona la memoria técnica (`01_seed/` o `README.md`) y detecta `domain_archetype` e `inspection_mode`.
- Clasifica las **Primitivas Universales de Evidencia**: `config`, `spec`, `pipeline`, `verification`, `implementation`.
- **Regla Antifraude**: Detección estricta de stubs, clases base sin implementación, comentarios `TODO`/`FIXME` o promesas no materializadas. Prohibido inferir cumplimiento de archivos vacíos.

### FASE 2: Taxonomía Canónica Instanciada al Dominio (10 Módulos)
Mapea la evidencia del repositorio a los 10 módulos canónicos (M01 a M10), adaptando los criterios y rutas al arquetipo:
- **M01 [Peso: 5%]**: Descubrimiento, Modelo Mental y Especificación Inicial.
- **M02 [Peso: 10%]**: Arquitectura del Sistema, Contratos y Modelos de Dominio.
- **M03 [Peso: 5%]**: Gobernanza, Políticas y Reglas de Calidad / Seguridad.
- **M04 [Peso: 5%]**: Aprovisionamiento, Entorno Reproducible y Fixtures.
- **M05 [Peso: 25%]**: Construcción del Núcleo / Motor Central del Dominio.
- **M06 [Peso: 15%]**: Integración, Serialización, Emitters e Interoperabilidad.
- **M07 [Peso: 10%]**: Aseguramiento de Calidad, Robustez y Pruebas de Estrés.
- **M08 [Peso: 10%]**: Validación Organizacional, Proyecciones y Cockpits de Liderazgo.
- **M09 [Peso: 10%]**: Automatización, CI/CD y Puertas de Calidad.
- **M10 [Peso: 5%]**: Memoria Técnica (Seed), Guías de Operación y Roadmap Futuro.

### FASE 3: Cálculo Matemático Ponderado (0 a 100%)
- **Avance de Fase ($P_i$):** $P_i = \left( \frac{\text{Criterios Cumplidos}_i}{\text{Criterios Totales}_i} \right) \times 100$
- **Contribución Ponderada ($S_i$):** $S_i = W_i \times \left( \frac{P_i}{100} \right)$
- **Score Total Consolidado:** $Score_{Total} = \sum_{i=1}^{10} S_i$
- **Bandas de Madurez:**
  - 🔴 **0.0% – 49.9%**: `Fase Inicial / Riesgo Crítico`
  - 🟡 **50.0% – 74.9%**: `Construcción Activa / Madurez Media`
  - 🔵 **75.0% – 89.9%**: `Madurez Avanzada / Pre-producción`
  - 🟢 **90.0% – 100.0%**: `Excelencia Operativa / Producción`

### FASE 4: Diseño Visual Mermaid (Roadmap Horizontal en IDE)
- Utiliza estrictamente `flowchart LR` continuo sin anidar subgrafos verticales (`direction TB`).
- Formato de tarjetas concisas: `MXX["<b>MXX: Nombre Real</b><br/>XX.X% | Estado"]`.
- Enlaces secuenciales: `-->` si el siguiente módulo está en curso o completo; `-.->` si está en backlog/pendiente.
- Estilos semánticos exactos con `classDef`.
- Tarjeta de resumen final destacando Score Global, Banda de Madurez y Cuello de Botella Activo (`M10 ==> SUMMARY`).

### FASE 5: Generación y Verificación de Artefactos
Invoca el motor automatizado mediante el CLI de Python:

```bash
# Auditoría con perfil específico
metricsthinking audit --target "<RUTA_PROYECTO>" --profile <PERFIL> --out-dir "<RUTA_PROYECTO>/artifacts"

# O mediante Python module:
python -m metricsthinking.cli audit --target "<RUTA_PROYECTO>" --profile <PERFIL>

# Listar todos los perfiles disponibles:
python -m metricsthinking.cli list-profiles
```

---

## 5. Confirmación de Resultados

Al concluir la auditoría, presenta al usuario:
1. **Nota Global Consolidada ($Score_{Total}$)**, **Arquetipo** y **Banda de Madurez**.
2. **Cuello de Botella Inmediato**: Primer módulo secuencial incompleto.
3. **Dashboard de los 10 Módulos** adaptados al dominio.
4. **Rutas directas con markdown links** a los 3 artefactos generados.

