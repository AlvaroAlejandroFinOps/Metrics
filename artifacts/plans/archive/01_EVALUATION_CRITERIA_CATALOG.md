# METRICSTHINKING™: Catálogo Universal de Criterios de Evaluación

**Documento:** Matriz de Criterios y Protocolo de Auditoría Forense  
**Versión:** `1.0.0-ENTERPRISE`  
**Autor:** Google Antigravity Agent  
**Ubicación:** `artifacts/plans/metricsthinking/01_EVALUATION_CRITERIA_CATALOG.md`  

---

## 1. INTRODUCCIÓN A LA TAXONOMÍA DE CRITERIOS

En MetricsThinking, un **criterio** es una afirmación técnica atómica, objetiva y binaria ($C \in \{0, 1\}$) que puede ser comprobada mediante la inspección del sistema de archivos, ejecución de comandos, validación de esquemas o análisis de código estático.

Un criterio **NO** puede ser una opinión subjetiva (e.g. *"el código está bien estructurado"*). Debe referenciar:
- La existencia y validez sintáctica de un archivo o directorio.
- La presencia de símbolos o clases específicas.
- La aprobación exitosa de una suite de pruebas automatizadas.
- El cumplimiento de un contrato o esquema formal.

---

## 2. MATRIZ DE CRITERIOS POR MÓDULO CANÓNICO

A continuación se detalla la matriz de referencia aplicada a plataformas de datos y compiladores semánticos (con generalización para proyectos de software empresarial):

### M01: Descubrimiento y Alcance (Peso: 5%)
| ID Criterio | Nombre del Criterio | Evidencia Esperada | Verificación Binaria |
|:---|:---|:---|:---:|
| `M01-C01` | **Problem Statement Formalizado** | Documento de definición o ThinkingSeed con declaración explícita de problemas empresariales y técnicos a resolver. | `[0, 1]` |
| `M01-C02` | **Límites y Scope Declarados** | Sección formal de "In Scope" y "Out of Scope" delimitando responsabilidades del sistema. | `[0, 1]` |
| `M01-C03` | **Casos de Uso Formales** | Definición de al menos 3 perfiles de usuario o sistemas consumidores (e.g., Analytics Engineers, Governance Officers, C-Level). | `[0, 1]` |

### M02: Arquitectura y Diseño Técnico (Peso: 10%)
| ID Criterio | Nombre del Criterio | Evidencia Esperada | Verificación Binaria |
|:---|:---|:---|:---:|
| `M02-C01` | **AST Canónico Desacoplado** | Modelos de datos centrales neutrales frente a tecnologías externas o motores destino. | `[0, 1]` |
| `M02-C02` | **ADRs Documentados** | Decisiones arquitectónicas registradas formalmente (`ADR-###`) con contexto, decisión y consecuencias. | `[0, 1]` |
| `M02-C03` | **Contratos JSON Schema Validados** | Esquemas formales (`.schema.json`) para validar estructuras de entrada/salida y pruebas de conformidad. | `[0, 1]` |
| `M02-C04` | **Topología y Grafos Formales** | Representación estructural explícita de dependencias relacionales mediante grafos computacionales (e.g. NetworkX). | `[0, 1]` |

### M03: Gobernanza y Cumplimiento (Peso: 5%)
| ID Criterio | Nombre del Criterio | Evidencia Esperada | Verificación Binaria |
|:---|:---|:---|:---:|
| `M03-C01` | **Detección y Marcado de PII** | Atributos y clasificadores de privacidad por diseño en los modelos de entidades. | `[0, 1]` |
| `M03-C02` | **Reglas de Calidad Formales (cQS)** | Motor o algoritmo de penalización cuantitativo que califique la completitud y corrección semántica. | `[0, 1]` |
| `M03-C03` | **Validación Estricta de Esquemas** | Intercepción y rechazo de esquemas inválidos antes de compilación o ejecución física. | `[0, 1]` |

### M04: Aprovisionamiento y Readiness (Peso: 5%)
| ID Criterio | Nombre del Criterio | Evidencia Esperada | Verificación Binaria |
|:---|:---|:---|:---:|
| `M04-C01` | **Entorno Reproducible** | Manifiestos de empaquetado y configuración de herramientas estandarizados (`pyproject.toml`, ruff, mypy, pytest). | `[0, 1]` |
| `M04-C02` | **Dependencias Versionadas** | Especificación estricta de versiones mínimas para todas las librerías directas de producción y desarrollo. | `[0, 1]` |
| `M04-C03` | **Fixture Enterprise Disponible** | Datos o esquemas de prueba de nivel corporativo para pruebas deterministas integradas. | `[0, 1]` |

### M05: Construcción Núcleo (Core Engine) (Peso: 25%)
| ID Criterio | Nombre del Criterio | Evidencia Esperada | Verificación Binaria |
|:---|:---|:---|:---:|
| `M05-C01` | **Parsers Funcionales** | Módulos de ingesta declarativa capaces de procesar formatos estándar de entrada (e.g., Markdown, YAML, JSON). | `[0, 1]` |
| `M05-C02` | **Inferencia de Roles Operativa** | Motor algorítmico capaz de deducir roles funcionales (Hechos, Dimensiones, Puentes) a partir de la topología. | `[0, 1]` |
| `M05-C03` | **Resolución de Relaciones y Ciclos** | Resolver algorítmico con detección de aciclicidad y cálculo de cardinalidades 1:N unidireccionales. | `[0, 1]` |
| `M05-C04` | **Generador de Métricas Canónico** | Síntesis automática de cálculos y medidas de negocio (e.g., DAX canónico) a partir del modelo. | `[0, 1]` |

### M06: Integración e Interoperabilidad (Backend & Emitters) (Peso: 15%)
| ID Criterio | Nombre del Criterio | Evidencia Esperada | Verificación Binaria |
|:---|:---|:---|:---:|
| `M06-C01` | **Emisores de Dialecto Nativo** | Módulos generadores de código de plataforma de destino (e.g. TMDL nativo para Power BI). | `[0, 1]` |
| `M06-C02` | **Escritura Atómica y Safe-Encoding** | Escritor a disco que previene corrupción con staging temporal y codificación UTF-8 pura (sin BOM). | `[0, 1]` |
| `M06-C03` | **Exportación Multi-Formato** | Soporte de serialización a múltiples representaciones de consumo (Markdown, JSON, Mermaid ERD). | `[0, 1]` |

### M07: Aseguramiento de Calidad (QA & Stress Testing) (Peso: 10%)
| ID Criterio | Nombre del Criterio | Evidencia Esperada | Verificación Binaria |
|:---|:---|:---|:---:|
| `M07-C01` | **Cobertura y Tasa de Éxito al 100%** | 100% de pruebas unitarias/integración en estado PASS y cobertura superior al umbral corporativo (>=80%). | `[0, 1]` |
| `M07-C02` | **Golden Regression Tests Validados** | Pruebas de regresión deterministas contra salidas maestras conocidas para garantizar cero deriva. | `[0, 1]` |
| `M07-C03` | **Suites de Estrés Masivo por Tiers** | Pruebas de carga, estrés sintético y benchmarking segmentadas por escalas operativas (e.g. PYME, Mediana, Enterprise). | `[0, 1]` |

### M08: Validación y Aceptación Organizacional (Peso: 10%)
| ID Criterio | Nombre del Criterio | Evidencia Esperada | Verificación Binaria |
|:---|:---|:---|:---:|
| `M08-C01` | **Proyecciones por Rol (Persona Lenses)** | Lentes especializadas que proyectan vistas adaptadas a cada rol de la organización cumpliendo contratos JSON Schema. | `[0, 1]` |
| `M08-C02` | **Data Leadership Cockpit Operativo** | Cuadro de mando ejecutivo sintetizado con radar de madurez por dominio, KPIs y recomendaciones priorizadas. | `[0, 1]` |
| `M08-C03` | **CLI de Diagnóstico y Exploración** | Interfaz de línea de comandos completa con capacidades de inspección, validación, explicación y exportación. | `[0, 1]` |

### M09: Despliegue y Automatización (CI/CD) (Peso: 10%)
| ID Criterio | Nombre del Criterio | Evidencia Esperada | Verificación Binaria |
|:---|:---|:---|:---:|
| `M09-C01` | **Pipeline CI/CD Automatizado** | Flujo de trabajo en la nube (`.github/workflows`) con matrices multi-plataforma y puertas de calidad automáticas. | `[0, 1]` |
| `M09-C02` | **Empaquetado y Distribución Estandarizada** | Manifiesto de empaquetado (Wheel/Sdist), entry points de consola o hooks de pre-commit integrados. | `[0, 1]` |

### M10: Cierre, Extensibilidad y Documentación (Peso: 5%)
| ID Criterio | Nombre del Criterio | Evidencia Esperada | Verificación Binaria |
|:---|:---|:---|:---:|
| `M10-C01` | **Documentación Técnica Exhaustiva (Seed)** | Memoria técnica completa y ADN del proyecto (ThinkingSeed Master) documentando arquitectura y contratos. | `[0, 1]` |
| `M10-C02` | **CLI Help Documentado** | Documentación exhaustiva en línea de comandos para cada comando, argumento y opción. | `[0, 1]` |
| `M10-C03` | **Adaptadores Multicanal / Roadmap** | Interfaces base (`BaseTargetAdapter`), planificador de capacidades y roadmap de extensión formal para destinos futuros. | `[0, 1]` |
