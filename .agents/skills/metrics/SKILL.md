---
name: metrics
description: >-
  Auditor universal de proyectos tecnológicos basado en evidencia física estricta (Ground Truth) y la
  metodología de 10 módulos canónicos adaptados al dominio (MetricsThinking™ v5.0 Holistic Governance / iContext Federation Protocol v5.0).
  Soporta 14 arquetipos de ingeniería, motor espectral de eficiencia contextual FPIA (S_spectral / S_linear),
  auditor de deriva semántica AST contra ThinkingSeed v5.0, vector de seguridad Zero-Tolerance (Shannon H <= 4.5, PII, Prompt Injection),
  vector de resiliencia AST (Ca/Ce, SPOFs), servidor MCP (6 herramientas) y materialización de cuatro artefactos sincronizados
  (MetricsThinking.json, MetricsThinking.md, INFERRED_ROADMAP.md compatible con plan_metadata.schema.json y CONTEXT_PRUNING_PLAN.json). Se activa con /metrics.
---

# MetricsThinking™ v5.0: Auditor Forense Universal de Proyectos e Ingeniería Inversa (/metrics)

Esta habilidad permite al agente actuar como **Lead Systems & AI Architect y Auditor de Gobernanza de Proyectos** en Google Antigravity y entornos multi-asistente, ejecutando auditorías profundas por **ingeniería inversa** basadas en evidencia física estricta (**Ground Truth First**), integradas en el **iContext Federation Protocol v5.0** (Capa L2).

---

## 1. Misión y Cuándo Activar

- Al invocar `/metrics`, `/metrics <ruta-del-proyecto>` o expresiones naturales como `/metrics (evalua este proyecto como una skill para IA)`.
- Al solicitar auditar la madurez, avance real, deuda técnica, deriva semántica AST o calidad de cualquier repositorio de software, datos, IA, plataformas, skills de agentes o infraestructura.
- Para diagnosticar el cuello de botella inmediato, optimizar el presupuesto contextual de tokens y derivar el roadmap de ejecución operacional desacoplado en 10 etapas adaptadas al arquetipo de ingeniería.

### Protocolo de Entrada y Aceptación de Contexto (Natural Language Hints)

El usuario puede invocar `/metrics` de diversas formas:
1. **Invocación Simple / Auto-detección**: `/metrics` (activa la **Fase 0: Sonda Exploratoria Ligera** para diagnosticar el arquetipo antes de auditar).
2. **Invocación con Ruta**: `/metrics "./otro_proyecto"` (ejecuta sonda exploratoria sobre la ruta destino).
3. **Invocación con Contexto o Pista en Lenguaje Natural**:
   - `/metrics (evalua este proyecto como una skill para IA)`
   - `/metrics evalua como data-platform`
   - `/metrics para un proyecto de web-app`
   - `/metrics como sdd / spec-driven`
4. **Invocación Explícita por CLI**:
   ```bash
   python -m metricsthinking.cli audit --target . --profile sdd --prune --medallion
   ```

---

### Fase 0: Sonda Exploratoria Ligera y Diagnóstico de Arquetipos (SDD & Token Economy)

Antes de ejecutar la auditoría forense pesada (a menos que el usuario haya fijado explícitamente el perfil):
1. **Ejecutar la Sonda Ligera**:
   ```bash
   python -m metricsthinking.cli probe --target . --json
   ```
   *(O invocar la herramienta MCP `probe_archetype`)*.
2. **Interpretación y Rigor SDD**:
   - La sonda inspecciona en < 100 ms los contratos, manifiestos y estructura troncal sin volcar archivos en el contexto del LLM.
   - Si la confianza es alta ($\ge 65\%$), se selecciona automáticamente el perfil recomendado (`recommended_profile`).
   - Si se detecta un **Dominio Emergente** (confianza $< 65\%$ en todos los perfiles de catálogo), se evalúa con el metamodelo universal (`default`) o se sintetiza un perfil ad-hoc en `.metricsthinking/profiles/custom.yaml`.
3. **Ejecución Determinística**:
   Disparar la auditoría con el perfil resuelto:
   ```bash
   python -m metricsthinking.cli audit --target . --profile <PERFIL_RESUELTO>
   ```

> 💡 **Acuse de Recibo Inicial**: Al comenzar la respuesta de auditoría, emite un breve bloque introductorio confirmando el proyecto analizado y el perfil resuelto:
> ```markdown
> > 🔍 **MetricsThinking™ v5.0 | Auditoría Forense Holística (iContext L2)**
> > - **Proyecto Auditado:** `<NOMBRE_PROYECTO>` (`<RUTA>`)
> > - **Perfil / Arquetipo:** `<PERFIL>` (*<DESCRIPCIÓN_CORTA>*)
> > - **Confianza Sonda (Fase 0):** `<CONFIANZA_PCT>` (*<JUSTIFICACIÓN_EVIDENCIA>*)
> > - **Modo de Inspección:** `<INSPECTION_MODE>`
> > - **Backend Activo:** `<RUST_NATIVE | PYTHON_FALLBACK>`
> ```

---

## 2. Los Arquetipos de Ingeniería Soportados (v5.0)

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

## 3. Los Cuatro Artefactos Sincronizados y Federación iContext v5.0

Toda auditoría de MetricsThinking™ v5.0 materializa físicamente los entregables y sincroniza el bus de federación:
1. **`artifacts/MetricsThinking.json`** (y espejo canónico en `artifacts/plans/metricsthinking/MetricsThinking.json`): Telemetría completa, metadatos del repositorio, arquetipo de dominio, primitivas de evidencia universal, vector espectral FPAI, deriva semántica AST (`signature_mismatches`), seguridad y resiliencia.
2. **`artifacts/MetricsThinking.md`** (y espejo en `artifacts/plans/metricsthinking/MetricsThinking.md`): Reporte ejecutivo formal con resumen de primitivas, tabla de módulos canónicos, roadmap visual Mermaid LR optimizado, radar espectral FPAI, vector de seguridad y plan de remediación priorizado (P1 a P4).
3. **`artifacts/plans/active/INFERRED_ROADMAP.md`**: Roadmap operacional con frontmatter YAML compatible con `schemas/plan_metadata.schema.json` (`plan_id`, `status: active`, `target_nodes`, `expires_at`) para integración nativa con el Garbage Collector de `iDirectory v5.0`.
4. **`artifacts/plans/active/CONTEXT_PRUNING_PLAN.json`**: Plan reversible de poda contextual FPIA sincronizado con `.agentignore`.
5. **`.context/icontext_bus.json` (`l2_metricsthinking`)**: Publicación automática de `global_score`, `band`, `fpai_pf_spectral`, `drift_tokens` y `security_gate` para consumo por `iDirectory` y `iReadme`.

---

## 4. Vectores Avanzados de Evaluación Holística (v5.0)

### 4.1. Vector de Eficiencia Contextual Espectral (FPAI Economy) & AST Drift Auditor
- **Potencia Aparente Espectral:** $S_{\text{spectral}} = \sqrt{P^2 + (Q_{\text{dead}} + Q_{\text{dup}})^2 + D^2}$
- **Potencia Aparente Lineal:** $S_{\text{linear}} = P + Q_{\text{dead}} + Q_{\text{dup}} + D$
- **Factor de Potencia Espectral:** $PF_{\text{spectral}} = \min\left(1.0, \frac{P}{S_{\text{spectral}}} \times G\right)$ *(Meta $\ge 0.70$)*
- **Auditoría de Deriva AST vs Seed (Sección 4.1):** Cruza los símbolos AST reales (`.context/contracts_ast.json` o AST en vivo) contra los contratos declarados en `01_seed/seed-*-master.md`, cuantificando `signature_mismatches` en $D$ (tokens de distorsión).
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
