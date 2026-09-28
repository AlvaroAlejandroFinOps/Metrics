# METRICSTHINKING: Universal Technology Project Reverse Engineering & Ground Truth Audit Engine

**Language:** [English](README.md) | [Español](README_ES.md)

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-1a1a1a?style=flat-square&logo=python)](https://python.org)
[![Version](https://img.shields.io/badge/Version-3.0.0%20Universal-2b2b2b?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Architecture](https://img.shields.io/badge/Architecture-Polymorphic%20Multi--Archetype-2b2b2b?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Verification](https://img.shields.io/badge/Verification-Pytest%20100%25-34495e?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Engine](https://img.shields.io/badge/Engine-Ground%20Truth%20AST%20Auditing-1a1a1a?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![License](https://img.shields.io/badge/License-Apache%202.0-4b5563?style=flat-square)](LICENSE)

---

## 1. Executive Abstract

MetricsThinking™ v3.0 Universal is an enterprise-grade static analysis, reverse engineering, and project governance engine designed to compute the formal mathematical maturity of technology repositories across **10 Engineering Archetypes**. In modern AI-assisted and multidisciplinary engineering, assessing actual repository progress frequently suffers from cognitive bias, deceptive placeholder artifacts, and unverified architectural claims. MetricsThinking resolves this tension by executing exhaustive physical Ground Truth inspection across file systems, abstract syntax trees (ASTs), test suites, container manifests, data contracts, and CI/CD pipelines.

The engine partitions any technology project into a domain-adapted matrix of 10 Canonical Modules ($M_1, \dots, M_{10}$). Every module evaluates a parameterized set of criteria against physical file presence, syntactic token density, and semantic invariants across **5 Universal Evidence Primitives** (`config`, `spec`, `pipeline`, `verification`, `implementation`). The scoring pipeline produces a deterministic, weighted completion percentage ($0.0\% - 100.0\%$), maps the codebase into five standardized maturity bands, and generates synchronized deliverables: structured JSON data contracts, an executive Markdown report containing a zero-nesting Mermaid LR flowchart, and an actionable inferred implementation roadmap.

---

## 2. Supported Engineering Archetypes (v3.0)

MetricsThinking™ v3.0 natively supports 10 distinct engineering disciplines via decoupled evaluation profiles:

| # | Archetype | ID | Inspection Mode | Key Evidence Inspected |
|:--|:----------|:---|:----------------|:-----------------------|
| 1 | **MLOps** | `mlops` | `pipeline_orchestration` | Model cards, datasets, MLflow/DVC pipelines, drift monitors, training scripts |
| 2 | **LLMOps / GenAIOps** | `llmops` | `pipeline_orchestration` | Context engineering, prompt registries, RAG pipelines, evals/guardrails |
| 3 | **DataOps / Data Platform** | `dataops` | `pipeline_orchestration` | Medallion architecture, Data Contracts, dbt/Dataform models, Great Expectations |
| 4 | **GitOps / Declarative Infra** | `gitops` | `declarative_config` | Kubernetes manifests, Helm/Kustomize, ArgoCD/Flux applications, drift policies |
| 5 | **Platform Engineering / IDP** | `platform-eng` | `declarative_config` | Developer portals (Backstage), Golden Paths, service catalogs, Score/IaC templates |
| 6 | **DevSecOps** | `devsecops` | `governance_spec` | Threat models, SAST/DAST rules, SBOM (CycloneDX/SPDX), Policy-as-Code (OPA/Kyverno) |
| 7 | **Dual-Track Agile** | `dual-track` | `polyglot_hybrid` | Opportunity solution trees, PRDs, discovery spikes, A/B experiments, telemetry |
| 8 | **Team Topologies** | `team-topologies` | `governance_spec` | Team contracts, interaction modes, bounded context maps, cognitive load telemetry |
| 9 | **Chaos Engineering** | `chaos-eng` | `declarative_config` | Steady-state hypotheses, fault injection experiments (Chaos Mesh/Litmus), Game Days |
| 10 | **Spec-Driven Dev (SDD)** | `sdd` | `governance_spec` | OpenAPI/AsyncAPI/Proto specs, contract tests (Pact), generated SDK stubs, mocks |

---

## 3. System Architecture & Topology

```text
+----------------------------------------------------------------------------------------------------+
|                                METRICSTHINKING v3.0 UNIVERSAL CORE                                 |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  +---------------------------+       +----------------------------+       +---------------------+  |
|  |    01. EvidenceCollector  | ----> |    02. ModuleEvaluator     | ----> |   03. AuditScorer   |  |
|  |  - 5 Evidence Primitives  |       |  - Polymorphic Dispatch    |       |  - Dynamic Weights  |  |
|  |  - Deep filesystem scan   |       |  - 10 Archetype Profiles   |       |  - Maturity Bands   |  |
|  |  - AST & Token inspection |       |  - 25+ Domain Rules        |       |  - Remediation Plan |  |
|  |  - ThinkingSeed Metadata  |       |  - Anti-Fraud Filtering    |       |  - Bottleneck Trap  |  |
|  +---------------------------+       +----------------------------+       +---------------------+  |
|               |                                                                      |             |
|               v                                                                      v             |
|  +---------------------------+                                            +---------------------+  |
|  |   ProjectEvidence (DTO)   |                                            |  ProjectAuditReport |  |
|  +---------------------------+                                            +---------------------+  |
|                                                                                      |             |
|                                                                                      v             |
|                                      +----------------------------+       +---------------------+  |
|                                      |   05. Multi-Channel Sync   | <---- | 04. ArtifactRenderer|  |
|                                      |  - Local artifacts/ dir    |       |  - MetricsThinking. |  |
|                                      |  - Multi-AI Skill deploy   |       |    json / .md       |  |
|                                      |  - CI/CD & MCP JSON-RPC    |       |  - Mermaid LR flow  |  |
|                                      |                            |       |  - INFERRED_ROADMAP |  |
|                                      +----------------------------+       +---------------------+  |
+----------------------------------------------------------------------------------------------------+
```

---

## 4. Mathematical Formulation & Analytical Engines

### 4.1. Criterion-Level Score Computation
Let $\mathcal{C}_{i,j}$ denote the $j$-th criterion within module $M_i$. Its raw verification score $s(\mathcal{C}_{i,j}) \in [0, 100]$ is determined by the presence of physical evidence matching file patterns $\mathcal{P}_{i,j}$ and containing required semantic keywords $\mathcal{K}_{i,j}$:

$$s(\mathcal{C}_{i,j}) = \min\left(100.0, \; 100 \cdot \frac{|\mathcal{E}_{i,j}^{valid}|}{\max(1, |\mathcal{P}_{i,j}|)} \cdot \mathbb{I}(\text{keywords\_satisfied})\right)$$

where $\mathcal{E}_{i,j}^{valid}$ represents the subset of discovered files strictly excluding anti-fraud paths (e.g. test fixtures, stubs, and auto-generated logs), and $\mathbb{I}(\cdot)$ is the indicator function.

### 4.2. Module Score and Global Weighted Progress
Let $w_i \in (0, 1]$ be the architectural weight assigned to module $M_i$ such that $\sum_{i=1}^{10} w_i = 1.0$. The module score $S(M_i)$ and overall repository maturity score $\Phi(\mathcal{R})$ are computed as:

$$S(M_i) = \sum_{j=1}^{K_i} \omega_{i,j} \cdot s(\mathcal{C}_{i,j}), \quad \text{where } \sum_{j=1}^{K_i} \omega_{i,j} = 1.0$$

$$\Phi(\mathcal{R}) = \sum_{i=1}^{10} w_i \cdot S(M_i) \quad \in [0.0\%, 100.0\%]$$

### 4.3. Maturity Band Mapping
The global score $\Phi(\mathcal{R})$ maps deterministically to a discrete maturity band $\mathcal{B}$:

$$\mathcal{B}(\Phi) = \begin{cases}
\text{Inception / Prototyping} & 0.0 \le \Phi < 25.0 \\
\text{Foundational Development} & 25.0 \le \Phi < 50.0 \\
\text{Functional Maturation} & 50.0 \le \Phi < 75.0 \\
\text{Operational Excellence / Production Ready} & 75.0 \le \Phi < 90.0 \\
\text{Enterprise Certified / Battle-Tested} & 90.0 \le \Phi \le 100.0
\end{cases}$$

---

## 5. Repository Structure & Multi-Provider Ecosystem

```text
MetricsThinking/
├── .agents/skills/metrics/                   # Google Antigravity local workspace skill
│   └── SKILL.md
├── integrations/                             # Native AI provider adapters
│   ├── claude/CLAUDE.md                      # Anthropic Claude Code & Desktop
│   ├── cursor/metrics.mdc                    # Cursor IDE / Windsurf rules
│   └── copilot/copilot-instructions.md       # GitHub Copilot & OpenAI instructions
├── AGENTS.md                                 # Universal open agent standard
├── artifacts/
│   ├── MetricsThinking.json                  # Canonical machine-readable audit report
│   ├── MetricsThinking.md                    # Executive human-readable audit report
│   └── plans/active/
│       └── INFERRED_ROADMAP.md               # Reverse-engineered execution roadmap
├── config/profiles/                          # 10 Universal Archetype Evaluation Profiles
│   ├── default.yaml                          # Software engineering canonical profile
│   ├── mlops.yaml                            # MLOps & Machine Learning lifecycle
│   ├── llmops.yaml                           # LLMOps, GenAI, Context Engineering
│   ├── dataops.yaml                          # DataOps & Modern Data Stack
│   ├── gitops.yaml                           # GitOps & Declarative Infrastructure
│   ├── platform-eng.yaml                     # Platform Engineering & IDP
│   ├── devsecops.yaml                        # DevSecOps, Policy-as-Code, SBOM
│   ├── dual-track.yaml                       # Dual-Track Agile & Product Engineering
│   ├── team-topologies.yaml                  # Socio-technical architecture & boundaries
│   ├── chaos-eng.yaml                        # Chaos Engineering & Steady State
│   ├── sdd.yaml                              # Spec-Driven Development (SDD)
│   ├── data-platform.yaml                    # Data platform & AI pipeline profile
│   └── web-app.yaml                          # Modern frontend/fullstack web app profile
├── schemas/                                  # JSON Schema validation suite (Draft 2020-12)
│   ├── audit_criterion.schema.json           # JSON Schema for criteria contracts
│   ├── canonical_module.schema.json          # JSON Schema for module contracts
│   ├── project_audit_report.schema.json      # JSON Schema for full audit reports
│   ├── thinking_seed_v3.schema.json          # JSON Schema for ThinkingSeed v3.0
│   └── evidence_primitives.schema.json       # JSON Schema for 5 evidence primitives
├── scripts/
│   └── install_skill.py                      # Multi-provider skill installer
├── src/
│   └── metricsthinking/
│       ├── __init__.py                       # Package exports
│       ├── cli.py                            # Multi-command CLI interface
│       ├── collector.py                      # 5 Universal Evidence Primitives & Seed parser
│       ├── engine.py                         # 5-phase orchestrator & auto-detection
│       ├── evaluator.py                      # Polymorphic matrix evaluator & 25+ domain rules
│       ├── mcp_server.py                     # Model Context Protocol (MCP) JSON-RPC server
│       ├── models.py                         # Immutable Pydantic v2 data models
│       ├── renderer.py                       # Mermaid LR and Markdown generator
│       └── scorer.py                         # Archetype-aware scoring & action planner
├── tests/                                    # Exhaustive pytest verification suite (50+ tests)
├── pyproject.toml                            # Standard Python build configuration (v3.0.0)
├── README.md                                 # International English documentation
└── README_ES.md                              # Rigorous Spanish documentation
```

---

## 6. Multi-Provider AI Skill Installation

MetricsThinking can be deployed as an active skill/tool across all major AI assistant platforms:

### 6.1. Quick Installation via CLI
```bash
# Clone the repository
git clone https://github.com/AlvaroAlejandroFinOps/Metrics.git
cd Metrics
pip install -e ".[dev]"

# Install skill for ALL detected AI providers in current workspace:
metricsthinking install-skill --target all

# Or install for a specific provider:
metricsthinking install-skill --target antigravity   # Google Antigravity
metricsthinking install-skill --target claude        # Anthropic Claude Code
metricsthinking install-skill --target cursor        # Cursor IDE
metricsthinking install-skill --target copilot       # GitHub Copilot
metricsthinking install-skill --target mcp           # Model Context Protocol snippet
```

### 6.2. Global Google Antigravity Skill Installation
To make the `/metrics` skill available globally across any workspace in Antigravity:
```bash
metricsthinking install-skill --target antigravity --global
```

### 6.3. Model Context Protocol (MCP) Integration
Launch the standard JSON-RPC stdio server:
```bash
metricsthinking mcp
```
Add to your Claude Desktop or Cursor `mcp_config.json`:
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

## 7. Execution & Verification Protocol

### 7.1. Running Forensic Audits Directly

```bash
# List all available profiles and archetypes
metricsthinking list-profiles

# Run full audit on current directory using default profile (or auto-detected from ThinkingSeed)
metricsthinking audit --target . --out-dir artifacts

# Run audit with a specialized archetype profile
metricsthinking audit --target . --profile mlops --out-dir artifacts
metricsthinking audit --target . --profile llmops --out-dir artifacts
metricsthinking audit --target . --profile dataops --out-dir artifacts
metricsthinking audit --target . --profile gitops --out-dir artifacts
metricsthinking audit --target . --profile devsecops --out-dir artifacts
metricsthinking audit --target . --profile sdd --out-dir artifacts
```

### 7.2. Verification Suite & Invariant Tests

```bash
# Run unit test suite with coverage (50 tests)
python -m pytest tests/ -v

# Execute static linting
ruff check src/ tests/ scripts/
```

---

## 8. Domain Glossary

* **Ground Truth:** Verifiable, physical evidence within the repository (source code, compiled assets, configuration manifests, test suites, contracts) as opposed to aspirational documentation.
* **Canonical Module:** One of the 10 domain-adapted lifecycle stages evaluated to calculate overall project completeness.
* **Universal Evidence Primitives:** Standardized 5-type evidence classification (`config`, `spec`, `pipeline`, `verification`, `implementation`) preventing false negatives on non-traditional repositories.
* **Domain Archetype:** Specialized engineering discipline (MLOps, LLMOps, GitOps, etc.) with custom evaluation rules and remediation paths.
* **Anti-Fraud Guardrail:** Filtering logic that discards mock files, test fixtures, and auto-generated outputs to prevent false positive maturity inflation.
* **Mermaid LR Roadmap:** A horizontal flowchart visualization of project stages styled with semantic state classes (`done`, `active`, `backlog`, `blocked`).

---

## 9. Academic & Engineering References

1. IEEE Computer Society. *IEEE Standard for Software and System Test Documentation*. IEEE Std 829-2008.
2. Fowler, M. *Continuous Integration*. Addison-Wesley, 2006.
3. Bass, L., Clements, P., & Kazman, R. *Software Architecture in Practice (4th Edition)*. Addison-Wesley Professional, 2021.
4. Skelton, M., & Pais, M. *Team Topologies: Organizing Business and Technology Teams for Fast Flow*. IT Revolution Press, 2019.
5. Forsgren, N., Humble, J., & Kim, G. *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press, 2018.

### BibTeX Citation
```bibtex
@software{metricsthinking_2026,
  author = {HyperScale Thinking Systems},
  title = {MetricsThinking: Universal Technology Project Reverse Engineering and Ground Truth Audit Engine},
  year = {2026},
  version = {3.0.0},
  url = {https://github.com/AlvaroAlejandroFinOps/Metrics}
}
```
