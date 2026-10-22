---
name: metrics
description: >-
  Auditor universal de proyectos tecnológicos basado en evidencia física estricta (Ground Truth) y la
  metodología de 10 módulos canónicos adaptados al dominio (MetricsThinking™ v4.0 Holistic Governance).
  Soporta 14 arquetipos de ingeniería, motor espectral de eficiencia contextual FPIA (S_spectral / S_linear),
  vector de seguridad Zero-Tolerance (Shannon H <= 4.5, PII, Prompt Injection), vector de resiliencia AST (Ca/Ce, SPOFs),
  servidor MCP (6 herramientas) y materialización de cuatro artefactos sincronizados (MetricsThinking.json,
  MetricsThinking.md, INFERRED_ROADMAP.md y CONTEXT_PRUNING_PLAN.json). Se activa con /metrics.
---

# MetricsThinking™: Auditor Forense Universal de Proyectos e Ingeniería Inversa (/metrics)

Esta habilidad permite al agente actuar como **Lead Systems & AI Architect y Auditor de Gobernanza de Proyectos** en Google Antigravity y entornos multi-asistente, ejecutando auditorías profundas por **ingeniería inversa** basadas en evidencia física estricta (**Ground Truth First**) y generando roadmaps de ejecución interactivos, vectores espectrales de eficiencia de contexto y planes de poda reversibles.

---

## 1. Misión y Cuándo Activar

- Al invocar `/metrics`, `/metrics <ruta-del-proyecto>` o expresiones naturales como `/metrics (evalua este proyecto como una skill para IA)`.
- Al solicitar auditar la madurez, avance real, deuda técnica o calidad de cualquier repositorio de software, datos, IA, plataformas, skills de agentes o infraestructura.
- Para diagnosticar el cuello de botella inmediato, optimizar el presupuesto contextual de tokens y derivar el roadmap de ejecución operacional desacoplado en 10 etapas adaptadas al arquetipo de ingeniería.

### Protocolo de Entrada y Aceptación de Contexto (Natural Language Hints)

El usuario puede invocar `/metrics` de diversas formas:
1. **Invocación Simple / Auto-detección**: `/metrics` (audita el directorio activo detectando automáticamente el arquetipo a partir de la evidencia física y el seed).
2. **Invocación con Ruta**: `/metrics "./otro_proyecto"` (audita una ruta específica con auto-detección).
3. **Invocación con Contexto o Pista en Lenguaje Natural**:
   - `/metrics (evalua este proyecto como una skill para IA)`
   - `/metrics evalua como data-platform`
   - `/metrics para un proyecto de web-app`
4. **Invocación Explícita por CLI**:
   ```bash
   python -m metricsthinking.cli audit --target . --profile agent-skill --prune --medallion
   ```

> 💡 **Acuse de Recibo Inicial**: Al comenzar la respuesta de auditoría, emite un breve bloque introductorio confirmando el proyecto analizado y el perfil resuelto:
> ```markdown
> > 🔍 **MetricsThinking™ v4.0 | Auditoría Forense Holística**
> > - **Proyecto Auditado:** `<NOMBRE_PROYECTO>` (`<RUTA>`)
> > - **Perfil / Arquetipo:** `<PERFIL>` (*<DESCRIPCIÓN_CORTA>*)
> > - **Modo de Inspección:** `<INSPECTION_MODE>`
> > - **Backend Activo:** `<RUST_NATIVE | PYTHON_FALLBACK>`
> ```

---

## 2. Los Arquetipos de Ingeniería Soportados (v4.0)

| Arquetipo | Perfil YAML | Modo de Inspección | Foco Principal |
|:---|:---|:---|:---|
| **AI Agent Skill / Context Eng** | `agent-skill` | `governance_spec` | `SKILL.md`, frontmatter YAML, plantillas maestras, multi-agent rules, installers |
| **Data Platform & Lakehouse** | `data-platform` | `pipeline_orchestration` | Medallion (Bronze/Silver/Gold), Kimball, Delta/Iceberg/BigQuery, dbt, SLAs |
| **Web Application & Frontend** | `web-app` | `source_code` | Componentes UI, state management, API client, routing, testing visual/E2E |
| **Software Engineering** | `default` | `source_code` | AST, modelos canónicos, suites de tests unitarios/integración, empaquetado |
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

## 3. Los Cuatro Artefactos Sincronizados

Toda auditoría de MetricsThinking™ v4.0 materializa físicamente cuatro entregables:
1. **`artifacts/MetricsThinking.json`**: Telemetría completa, metadatos del repositorio, arquetipo de dominio, primitivas de evidencia universal, vector espectral FPAI, informe de seguridad, resiliencia y criterios evaluados con rutas de archivo.
2. **`artifacts/MetricsThinking.md`**: Reporte ejecutivo formal con resumen de primitivas, tabla de módulos canónicos, roadmap visual Mermaid LR optimizado, radar espectral FPAI, vector de seguridad y plan de remediación priorizado (P1 a P4).
3. **`artifacts/plans/active/INFERRED_ROADMAP.md`**: Roadmap operacional desacoplado en 10 fases con checklists interactivos (`[x]` confirmados en código/manifiestos, `[ ]` pendientes inferidos) y entregables tangibles.
4. **`artifacts/plans/active/CONTEXT_PRUNING_PLAN.json`**: Plan reversible de poda contextual FPIA y compensación de tokens inertes/redundantes sincronizado con `.agentignore`.

---

## 4. Vectores Avanzados de Evaluación Holística (v4.0)

### 4.1. Vector de Eficiencia Contextual Espectral (FPAI Economy)
- **Potencia Aparente Espectral:** $S_{\text{spectral}} = \sqrt{P^2 + (Q_{\text{dead}} + Q_{\text{dup}})^2 + D^2}$
- **Potencia Aparente Lineal:** $S_{\text{linear}} = P + Q_{\text{dead}} + Q_{\text{dup}} + D$
- **Factor de Potencia Espectral:** $PF_{\text{spectral}} = \min\left(1.0, \frac{P}{S_{\text{spectral}}} \times G\right)$ *(Meta $\ge 0.70$)*
- **Compensación Reversible:** Poda de tokens inertes mediante delimitadores seguros `# >>> FPAI-PRUNE-START` y `# <<< FPAI-PRUNE-END` en `.agentignore`.

### 4.2. Vector de Seguridad y Superficie de Ataque
- **Zero-Tolerance Gate ($G$):** Si se detecta cualquier clave API, token de acceso o credencial activa, $G = 0.0$.
- **Entropía de Shannon:** Alerta si $H > 4.50$ bits/símbolo en tokens alfanuméricos sospechosos.
- **Inmunidad ante Inyecciones de Prompt:** Escaneo de ataques directos/indirectos y jailbreaks.
- **Índice de Superficie de Ataque ($0.0 - 100.0$):** Umbral óptimo $\le 15.0$.

### 4.3. Vector de Resiliencia y Acoplamiento AST
- **Acoplamiento Modular:** Cálculo de $C_a$ (Aferente) y $C_e$ (Eferente).
- **Inestabilidad Modular:** $I = \frac{C_e}{C_a + C_e} \in [0.0, 1.0]$.
- **Puntos Únicos de Fallo (SPOFs):** Detección de módulos sobrecargados con $C_a \ge 3$ y $C_e \le 1$.
- **Patrones de Tolerancia a Fallos:** Conteo de timeouts, retries, circuit breakers y degradación con fallback.

---

## 5. Protocolo de Ejecución CLI y Servidor MCP

### Comandos CLI
```bash
# Auditoría forense estándar:
python -m metricsthinking.cli audit --target . --profile default

# Auditoría con poda contextual reversible y pipeline Medallion local:
python -m metricsthinking.cli audit --target . --profile default --prune --medallion

# Poda contextual independiente:
python -m metricsthinking.cli prune --target . --apply

# Pipeline Medallion local (Bronze -> Silver -> Gold):
python -m metricsthinking.cli medallion --raw-dir data/raw/telemetry --processed-dir data/processed/telemetry

# Servidor MCP stdio:
python -m metricsthinking.cli mcp
```

### Herramientas Expuestas en MCP (`metricsthinking-mcp`)
1. **`audit_project`**: Auditoría completa con cálculo de score, FPAI y artefactos.
2. **`get_project_score`**: Puntuación numérica, banda de madurez y cuello de botella activo.
3. **`get_module_evaluation`**: Inspección en detalle de un módulo canónico (M01 a M10).
4. **`get_spectral_efficiency`**: Vector espectral FPAI ($P, Q, D, S, PF$).
5. **`generate_pruning_plan`**: Plan de poda contextual y tokens recuperables.
6. **`apply_pruning_plan`**: Aplicación segura a `.agentignore`.
