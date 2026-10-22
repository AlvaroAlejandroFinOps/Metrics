# METRICSTHINKING™: Enterprise Project Evaluation Engine & Universal SDD Framework

**Documento:** Marco Metodológico y Motor Evaluador Corporativo  
**Versión:** `1.0.0-ENTERPRISE`  
**Autor:** Google Antigravity Agent (Lead Solutions Architect & Quality Auditor)  
**Ubicación:** `artifacts/plans/metricsthinking/00_METRICSTHINKING_FRAMEWORK.md`  
**Ámbito de Aplicación:** Universal (Software, Data Platforms, AI/ML Systems, Cloud Infrastructure, Compilers)

---

## 1. MISIÓN Y PROPÓSITO ESTRATÉGICO

**MetricsThinking™** es un motor analítico, didáctico y corporativo diseñado para evaluar de manera objetiva, cuantitativa y reproducible el grado de madurez, avance técnico y calidad de ejecución de proyectos tecnológicos.

A diferencia de las estimaciones cualitativas subjetivas (e.g. *"el proyecto va al 70%"*), MetricsThinking opera bajo una estricta **disciplina de auditoría basada en evidencia (Ground Truth)**. Cada punto porcentual de avance debe estar respaldado por un artefacto verificable, un contrato validado, una prueba automatizada o un manifiesto formal en el repositorio.

### Principios Rectores:
1. **Evidencia sobre Supuestos (Ground Truth First)**: Ningún criterio se considera cumplido sin una ruta física, símbolo o prueba automatizada que lo certifique.
2. **Universalidad y Adaptabilidad**: Diseñado para evaluar compiladores, plataformas de datos, servicios cloud, aplicaciones web o modelos de machine learning mediante un catálogo adaptable de criterios.
3. **Didáctico y Accionable**: No solo emite una calificación cuantitativa; diagnostica cuellos de botella específicos y prescribe el camino crítico de remediación inmediata.
4. **Determinismo Matemático**: Mismas evidencias físicas producen exactamente la misma calificación global y distribución ponderada.

---

## 2. METODOLOGÍA: LOS 10 MÓDULOS CANÓNICOS DEL CICLO DE VIDA UNIVERSAL (SDD / STAGE-GATE)

El ciclo de vida de todo proyecto de ingeniería de software y datos se descompone en **10 módulos canónicos estandarizados**, cada uno con un peso relativo ponderado ($W_i$) que totaliza el 100%:

```mermaid
flowchart LR
    M01["M01: Alcance (5%)"] --> M02["M02: Arquitectura (10%)"]
    M02 --> M03["M03: Gobernanza (5%)"]
    M03 --> M04["M04: Readiness (5%)"]
    M04 --> M05["M05: Core Engine (25%)"]
    M05 --> M06["M06: Interoperabilidad (15%)"]
    M06 --> M07["M07: QA & Testing (10%)"]
    M07 --> M08["M08: Validación (10%)"]
    M08 --> M09["M09: CI/CD (10%)"]
    M09 --> M10["M10: Extensibilidad (5%)"]

    classDef default fill:#1e293b,stroke:#475569,stroke-width:1px,color:#f8fafc;
```

### Tabla de Distribución de Pesos Canónicos

| ID | Módulo de Ciclo de Vida | Peso ($W_i$) | Enfoque de Evaluación |
|:---|:---|:---:|:---|
| **M01** | **Descubrimiento y Alcance** | **5%** | Declaración de problema, fronteras del sistema, actores y casos de uso formales. |
| **M02** | **Arquitectura y Diseño Técnico** | **10%** | Desacoplamiento estructural, ADRs, contratos de interfaces (JSON Schemas) y topología. |
| **M03** | **Gobernanza y Cumplimiento** | **5%** | Seguridad por diseño, PII, reglas de calidad de datos, trazabilidad y cumplimiento legal. |
| **M04** | **Aprovisionamiento y Readiness** | **5%** | Entorno reproducible, dependencias versionadas, linters, types y fixtures enterprise. |
| **M05** | **Construcción Núcleo (Core Engine)** | **25%** | Lógica de negocio fundamental, parsers, motores de inferencia, generadores y compiladores. |
| **M06** | **Integración e Interoperabilidad** | **15%** | Emitters físicos, serializadores de formato estándar, compatibilidad con ecosistemas externos. |
| **M07** | **Aseguramiento de Calidad (QA & Stress)** | **10%** | Cobertura de pruebas unitarias/integración, regresión determinista (Golden files) y estrés. |
| **M08** | **Validación y Aceptación Organizacional** | **10%** | Proyecciones por perfil (Persona Lenses), cockpits de liderazgo, herramientas CLI de diagnóstico. |
| **M09** | **Despliegue y Automatización (CI/CD)** | **10%** | Pipelines automatizados multi-OS/multi-versión, puertas de enlace de calidad y empaquetado. |
| **M10** | **Cierre, Extensibilidad y Documentación** | **5%** | ADN técnico portable (ThinkingSeed), manuales de usuario, CLI help y roadmap de adaptadores. |
| **TOTAL** | **Ciclo de Vida Completo** | **100%** | **Evaluación Integral de Madurez Organizacional** |

---

## 3. FORMULACIÓN MATEMÁTICA Y BANDA DE MADUREZ

### 3.1 Fórmula del Score Total Ponderado

Para cada módulo $i \in \{1, \dots, 10\}$:
- $W_i$: Peso porcentual del módulo, con $\sum_{i=1}^{10} W_i = 100\%$.
- $C_i$: Criterios cumplidos objetivamente en el módulo ($C_i \in \mathbb{N}_0$).
- $T_i$: Criterios totales evaluados en el módulo ($T_i \in \mathbb{N}^+$).
- $P_i = \frac{C_i}{T_i} \times 100\%$: Porcentaje de cumplimiento intrínseco del módulo.
- $S_i = W_i \times \frac{C_i}{T_i}$: Contribución ponderada del módulo a la nota global.

La **Nota Global Consolidada ($Score_{Total}$)** se define como:

$$Score_{Total} = \sum_{i=1}^{10} \left( W_i \times \frac{C_i}{T_i} \right)$$

### 3.2 Clasificación por Bandas de Madurez

| Rango de Score | Banda Cualitativa | Descripción Operativa y Estado de Riesgo |
|:---:|:---|:---|
| **0.0% – 49.9%** | 🔴 **En Fase Inicial / Riesgo Alto** | Proyecto en ideación o prototipado temprano. Componentes nucleares incompletos; riesgo crítico de viabilidad. |
| **50.0% – 74.9%** | 🟡 **Construcción / Fase Media** | Core engine operativo pero con brechas severas en integración, calidad, gobernanza o automatización. |
| **75.0% – 89.9%** | 🔵 **Madurez Avanzada / Pre-producción** | Sistema robusto con core e integraciones funcionales; pendiente de cierre de CI/CD formal, estrés masivo o endurecimiento de documentación. |
| **90.0% – 100.0%** | 🟢 **Producción / Excelencia Operativa** | Sistema enterprise verificado con pruebas exhaustivas, cero deuda bloqueante, CI/CD automatizado y documentación paper-grade. |

---

## 4. CONVENCIONES DE ESTADO Y VISUALIZACIÓN MERMAID

MetricsThinking prescribe una sintaxis semántica unificada para graficar el avance del proyecto mediante diagramas Mermaid:

- `complete`: Módulo al **100%** de cumplimiento de criterios. Color verde (`#2ECC71`).
- `inprogress`: Módulo con avance parcial (**1% a 99%**). Color azul (`#3498DB`).
- `pending`: Módulo sin iniciar (**0%**). Color gris (`#7F8C8D`) con borde discontinuo.
- `blocked`: Módulo detenido por dependencias previas no satisfechas o deuda técnica crítica. Color rojo (`#E74C3C`).

---

## 5. CATÁLOGO DIDÁCTICO PARA AUDITORES Y LEAD ARCHITECTS

El motor MetricsThinking debe responder cuatro preguntas fundamentales en cada informe:
1. **¿Dónde estamos hoy?** (Evidencia forense del repositorio en el commit actual).
2. **¿Cuál es la nota matemática real?** (Ponderación libre de sesgos).
3. **¿Cuál es el cuello de botella inmediato?** (El primer módulo secuencial que no alcanza el 100%).
4. **¿Qué acciones exactas se requieren para alcanzar el 100%?** (Plan de remediación priorizado por retorno de inversión técnica).
