---
name: metrics
description: >-
  Auditor universal de proyectos tecnológicos basado en evidencia física estricta (Ground Truth) y la
  metodología de 10 módulos canónicos adaptados al dominio (MetricsThinking™). Evalúa objetivamente el grado
  de madurez matemática (0-100%), genera el roadmap visual en Mermaid LR y materializa tres artefactos
  sincronizados (MetricsThinking.json, MetricsThinking.md e INFERRED_ROADMAP.md). Se activa con /metrics.
---

# MetricsThinking™: Auditor Forense de Proyectos e Ingeniería Inversa (/metrics)

Esta habilidad permite al agente actuar como **Lead Solutions Architect y Auditor de Gobernanza de Proyectos** en Google Antigravity, ejecutando auditorías profundas por **ingeniería inversa** basadas en evidencia física estricta (**Ground Truth First**) y generando roadmaps de ejecución interactivos.

---

## 1. Misión y Cuándo Activar

- Al invocar `/metrics` o `/metrics <ruta-del-proyecto>`.
- Al solicitar auditar la madurez, avance real, deuda técnica o calidad de cualquier repositorio de software, datos, IA o infraestructura.
- Para diagnosticar el cuello de botella inmediato y derivar el roadmap de ejecución operacional desacoplado en 10 etapas.

---

## 2. Los Tres Artefactos Sincronizados

Toda auditoría de MetricsThinking™ materializa físicamente tres entregables:
1. **`artifacts/MetricsThinking.json`**: Telemetría completa, metadatos del repositorio, criterios evaluados con rutas de archivo y datos estructurados para ingestión analítica.
2. **`artifacts/MetricsThinking.md`**: Reporte ejecutivo formal con tabla resumen de módulos, roadmap visual Mermaid LR optimizado y plan de remediación priorizado (P1 a P4).
3. **`artifacts/plans/active/INFERRED_ROADMAP.md`**: Roadmap operacional desacoplado en 10 fases con checklists interactivos (`[x]` confirmados en código, `[ ]` pendientes inferidos) y entregables tangibles.

---

## 3. Protocolo de Ejecución en 5 Fases

### FASE 1: Ingeniería Inversa y Reconciliación de Verdad (Ground Truth)
- Inspecciona la memoria técnica (`01_seed/` o `README.md`) y planes activos (`artifacts/plans/active/`).
- Examina el código fuente real (`src/`, `lib/`, `app/`), suites de pruebas (`tests/`) y manifiestos (`pyproject.toml`, `package.json`).
- **Regla Antifraude**: Detección estricta de stubs, clases base sin implementación, comentarios `TODO`/`FIXME` o promesas arquitectónicas no materializadas. Prohibido aprobar fases completas usando archivos dummy.

### FASE 2: Taxonomía Canónica Instanciada al Dominio (10 Módulos)
Mapea la evidencia del repositorio a los 10 arquetipos universales de entrega, adaptando los nombres al dominio del proyecto:
- **M01 [Peso: 5%]**: Descubrimiento, Modelo Mental y Especificación Inicial (Seed/README/Problem Statement).
- **M02 [Peso: 10%]**: Arquitectura del Sistema, Modelos Canónicos y Contratos de Interfaz (ADRs, Schemas, Modelos Pydantic/AST).
- **M03 [Peso: 5%]**: Gobernanza, Políticas y Reglas de Calidad (Clasificación sensible/PII, reglas de scoring, linting contextual).
- **M04 [Peso: 5%]**: Aprovisionamiento, Entorno y Datos de Prueba (Tooling, dependencias fijadas, fixtures enterprise/mock data).
- **M05 [Peso: 25%]**: Construcción del Núcleo / Motor Central (Lógica algorítmica nuclear, transformadores, lógica de negocio principal).
- **M06 [Peso: 15%]**: Integración, Serialización e Interoperabilidad (Backend emitters, serializadores atómicos, compatibilidad de salida).
- **M07 [Peso: 10%]**: Aseguramiento de Calidad y Pruebas de Estrés (Tests unitarios, integración, regresión determinista, benchmarks de volumen).
- **M08 [Peso: 10%]**: Validación Organizacional y Proyecciones de Negocio (Interfaces ejecutivas, vistas por perfil/persona, CLI de diagnóstico).
- **M09 [Peso: 10%]**: Automatización, Despliegue y CI/CD (Pipelines automatizados, empaquetado buildable, pre-commits, distribución).
- **M10 [Peso: 5%]**: Extensibilidad, Adaptadores Futuros y Documentación Final (Extensión multicanal declarada, manuales operativos, roadmap de cierre).

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
- Estilos semánticos exactos:
  ```mermaid
  classDef done fill:#1E4620,stroke:#2ECC71,stroke-width:2px,color:#FFFFFF;
  classDef active fill:#0D47A1,stroke:#2196F3,stroke-width:3px,color:#FFFFFF;
  classDef backlog fill:#2C3E50,stroke:#7F8C8D,stroke-width:1px,stroke-dasharray: 4 4,color:#BDC3C7;
  classDef blocked fill:#641E16,stroke:#E74C3C,stroke-width:2px,color:#FFFFFF;
  classDef summary fill:#1A252F,stroke:#F39C12,stroke-width:2px,color:#F1C40F;
  ```
- Tarjeta de resumen final destacando Score Global, Banda de Madurez y Cuello de Botella Activo (`M10 ==> SUMMARY`).

### FASE 5: Generación y Verificación de Artefactos
Invoca el motor automatizado mediante el CLI de Python:

```bash
metricsthinking audit --target "<RUTA_PROYECTO>" --profile <PERFIL> --out-dir "<RUTA_PROYECTO>/artifacts"
```
O directamente con Python:
```bash
python -m metricsthinking.cli audit --target "<RUTA_PROYECTO>" --profile <PERFIL> --out-dir "<RUTA_PROYECTO>/artifacts"
```

---

## 4. Confirmación de Resultados

Al concluir la auditoría, presenta al usuario:
1. **Nota Global Consolidada ($Score_{Total}$)** y **Banda de Madurez**.
2. **Cuello de Botella Inmediato**: Primer módulo secuencial incompleto.
3. **Dashboard de los 10 Módulos** adaptados al dominio.
4. **Rutas directas con markdown links** a los 3 artefactos generados.
