# METRICSTHINKING: Universal Technology Project Reverse Engineering & Ground Truth Audit Engine

**Language:** [English](README.md) | [Español](README_ES.md)

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-1a1a1a?style=flat-square&logo=python)](https://python.org)
[![Version](https://img.shields.io/badge/Version-4.0.0%20Holistic%20Governance-2b2b2b?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Architecture](https://img.shields.io/badge/Architecture-Polymorphic%2014--Archetype-2b2b2b?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Verification](https://img.shields.io/badge/Verification-Pytest%2094%2F94%20(100%25)-34495e?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Engine](https://img.shields.io/badge/Engine-Ground%20Truth%20AST%20Auditing-1a1a1a?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![Security](https://img.shields.io/badge/Security-Zero--Tolerance%20(H%20%3C%3D%204.5)-27ae60?style=flat-square)](https://github.com/AlvaroAlejandroFinOps/Metrics)
[![License](https://img.shields.io/badge/License-Apache%202.0-4b5563?style=flat-square)](LICENSE)

---

## 1. Executive Abstract

**MetricsThinking™ v4.0 Holistic Governance** is an enterprise-grade static analysis, reverse engineering, and project governance engine designed to compute the formal mathematical maturity of technology repositories across **14 Engineering Archetypes**. In modern AI-assisted, multi-agent, and multidisciplinary software engineering, assessing actual repository progress frequently suffers from cognitive bias, deceptive placeholder artifacts, and unverified architectural claims. MetricsThinking resolves this tension by executing exhaustive physical Ground Truth inspection across file systems, abstract syntax trees (ASTs), test suites, container manifests, data contracts, and CI/CD pipelines.

The engine partitions any technology project into a domain-adapted matrix of 10 Canonical Modules ($M_1, \dots, M_{10}$). Every module evaluates a parameterized set of criteria against physical file presence, syntactic token density, and semantic invariants across **5 Universal Evidence Primitives** (`config`, `spec`, `pipeline`, `verification`, `implementation`). The scoring pipeline produces a deterministic, weighted completion percentage ($0.0\% - 100.0\%$), maps the codebase into standardized maturity bands, and generates **four synchronized deliverables**: structured JSON telemetry, an executive Markdown report containing a zero-nesting Mermaid LR flowchart, an actionable inferred implementation roadmap, and a reversible context pruning plan (FPAI Economy).

---

## 2. Supported Engineering Archetypes (v4.0)

MetricsThinking™ v4.0 natively supports 14 distinct engineering disciplines via decoupled YAML evaluation profiles:

| # | Archetype | Profile ID | Inspection Mode | Key Evidence Inspected |
|:--|:----------|:-----------|:----------------|:-----------------------|
| 1 | **AI Agent Skill / Context Eng** | `agent-skill` | `governance_spec` | `SKILL.md`, frontmatter YAML, multi-agent rules, installers, context budgets |
| 2 | **Data Platform & Lakehouse** | `data-platform` | `pipeline_orchestration` | Medallion (Bronze/Silver/Gold), Kimball schemas, Delta/Iceberg/BigQuery, dbt |
| 3 | **Web Application & Frontend** | `web-app` | `source_code` | UI components, state stores, client routing, mock handlers, visual/E2E tests |
| 4 | **Software Engineering (Core)** | `default` | `source_code` | AST models, typed interfaces, unit/integration test suites, package manifests |
| 5 | **MLOps** | `mlops` | `pipeline_orchestration` | Model cards, datasets, MLflow/DVC pipelines, drift monitors, training scripts |
| 6 | **LLMOps / GenAIOps** | `llmops` | `pipeline_orchestration` | Context engineering, prompt registries, RAG pipelines, evals/guardrails |
| 7 | **DataOps / Modern Data Stack**| `dataops` | `pipeline_orchestration` | Data contracts, dbt lineage, reconciliation pipelines, data quality SLAs |
| 8 | **GitOps / Declarative Infra** | `gitops` | `declarative_config` | Kubernetes manifests, Helm/Kustomize, ArgoCD/Flux applications, drift policies |
| 9 | **Platform Engineering / IDP** | `platform-eng` | `declarative_config` | Developer portals (Backstage), Golden Paths, service catalogs, Score/IaC templates |
| 10 | **DevSecOps** | `devsecops` | `governance_spec` | Threat models, SAST/DAST rules, SBOM (CycloneDX/SPDX), Policy-as-Code (OPA/Kyverno) |
| 11 | **Dual-Track Agile** | `dual-track` | `polyglot_hybrid` | Opportunity solution trees, PRDs, discovery spikes, A/B experiments, telemetry |
| 12 | **Team Topologies** | `team-topologies` | `governance_spec` | Team contracts, interaction modes, bounded context maps, cognitive load telemetry |
| 13 | **Chaos Engineering** | `chaos-eng` | `declarative_config` | Steady-state hypotheses, fault injection experiments (Chaos Mesh/Litmus), Game Days |
| 14 | **Spec-Driven Dev (SDD)** | `sdd` | `governance_spec` | OpenAPI/AsyncAPI/Proto specs, contract tests (Pact), generated SDK stubs, mocks |

---

## 3. System Architecture & Topology

```text
+----------------------------------------------------------------------------------------------------+
|                                METRICSTHINKING v4.0 HOLISTIC CORE                                  |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  +---------------------------+       +----------------------------+       +---------------------+  |
|  |    01. EvidenceCollector  | ----> |    02. CriteriaEvaluator   | ----> |   03. AuditScorer   |  |
|  |  - Rust PyO3 / Python Fall|       |  - Polymorphic Dispatch    |       |  - Dynamic Weights  |  |
|  |  - 5 Evidence Primitives  |       |  - 14 Archetype Profiles   |       |  - Maturity Bands   |  |
|  |  - SHA-256 Incremental    |       |  - FPAI Spectral Engine    |       |  - Remediation Plan |  |
|  |  - Zero-Tolerance Gate    |       |  - AST Coupling (Ca/Ce)    |       |  - Bottleneck Trap  |  |
|  +---------------------------+       +----------------------------+       +---------------------+  |
|               |                                                                      |             |
|               v                                                                      v             |
|  +---------------------------+                                            +---------------------+  |
|  |   ProjectEvidence (DTO)   |                                            |  ProjectAuditReport |  |
|  +---------------------------+                                            +---------------------+  |
|                                                                                      |             |
|                                                                                      v             |
|                                      +----------------------------+       +---------------------+  |
|                                      |   05. Multi-Channel Sync   | <---- | 04. ReportRenderer  |  |
|                                      |  - Local artifacts/ dir    |       |  - MetricsThinking. |  |
|                                      |  - Multi-AI Skill deploy   |       |    md / .json       |  |
|                                      |  - MCP Server JSON-RPC     |       |  - Mermaid LR flow  |  |
|                                      |  - CI/CD Gateways          |       |  - INFERRED_ROADMAP |  |
|                                      |  - Reversible Pruning Plan |       |  - PRUNING_PLAN.json|  |
|                                      +----------------------------+       +---------------------+  |
+----------------------------------------------------------------------------------------------------+
```

---

## 4. Mathematical Formulation & Analytical Engines

### 4.1. Criterion-Level Score Computation
Let $\mathcal{C}_{i,j}$ denote the $j$-th criterion within module $M_i$. Its raw verification score $s(\mathcal{C}_{i,j}) \in [0, 100]$ is determined by the presence of physical evidence matching file patterns $\mathcal{P}_{i,j}$ and containing required semantic keywords $\mathcal{K}_{i,j}$:

$$s(\mathcal{C}_{i,j}) = \min\left(100.0, \; 100 \cdot \frac{|\mathcal{E}_{i,j}^{valid}|}{\max(1, |\mathcal{P}_{i,j}|)} \cdot \mathbb{I}(\text{keywords\_satisfied})\right)$$

where $\mathcal{E}_{i,j}^{valid}$ represents discovered files strictly excluding anti-fraud paths (e.g. fixtures, stubs, and auto-generated logs), and $\mathbb{I}(\cdot)$ is the indicator function.

### 4.2. Module Score and Global Weighted Progress
Let $w_i \in (0, 1]$ be the architectural weight assigned to module $M_i$ such that $\sum_{i=1}^{10} w_i = 1.0$. The module score $S(M_i)$ and overall repository maturity score $\Phi(\mathcal{R})$ are computed as:

$$S(M_i) = \sum_{j=1}^{K_i} \omega_{i,j} \cdot s(\mathcal{C}_{i,j}), \quad \text{where } \sum_{j=1}^{K_i} \omega_{i,j} = 1.0$$

$$\Phi(\mathcal{R}) = \sum_{i=1}^{10} w_i \cdot S(M_i) \quad \in [0.0\%, 100.0\%]$$

### 4.3. FPAI Context Economy & Spectral Power Vector
MetricsThinking v4.0 models context consumption as a bimodal apparent power vector:

$$S_{\text{spectral}} = \sqrt{P^2 + (Q_{\text{dead}} + Q_{\text{dup}})^2 + D^2}$$

$$S_{\text{linear}} = P + Q_{\text{dead}} + Q_{\text{dup}} + D$$

$$PF_{\text{spectral}} = \min\left(1.0, \frac{P}{S_{\text{spectral}}} \times G\right)$$

where $P$ is active architectural tokens, $Q$ is dead/duplicate tokens, $D$ is structural distortion, and $G \in \{0, 1\}$ is the Zero-Tolerance Security Gate ($G=0$ if any unmasked secret, $H > 4.5$, or prompt injection is present).

---

## 5. Repository Layout

```text
./
├── .agents/skills/metrics/                   # Google Antigravity local skill definition
├── .cursor/rules/metrics.mdc                 # Cursor IDE forensic rule
├── .github/
│   ├── copilot-instructions.md               # GitHub Copilot instructions
│   └── workflows/ci.yml                      # GitHub Actions automated test & audit matrix
├── 01_seed/seed-metricsthinking-master.md    # Master Architecture Vector (ThinkingSeed v3.0)
├── artifacts/                                # Four Synchronized Audit Outputs
│   ├── MetricsThinking.md                    # Executive Markdown with Mermaid LR flowchart
│   ├── MetricsThinking.json                  # Complete machine-readable forensic telemetry
│   └── plans/active/
│       ├── INFERRED_ROADMAP.md               # 10-phase operational execution roadmap
│       └── CONTEXT_PRUNING_PLAN.json         # Reversible FPAI context pruning plan
├── config/
│   ├── fpai_governance.yaml                  # Governance thresholds & token budgets
│   └── profiles/                             # 14 Canonical YAML evaluation profiles
├── crates/metricsthinking_rs/                # Optional native Rust PyO3 acceleration module
├── integrations/                             # Multi-provider skill templates (Claude, Cursor, Copilot)
├── schemas/                                  # Formal JSON Schema contracts
├── scripts/
│   └── install_skill.py                      # Multi-provider AI skill installer
├── src/metricsthinking/                      # Distributable Python package
│   ├── backends/                             # Rust PyO3 / Python Fallback crawling
│   ├── fpai/                                 # FPAI Context Economy & Security Gatekeeper
│   ├── cli.py                                # Typer / Argparse CLI entry point
│   ├── collector.py                          # Ground Truth physical evidence collector
│   ├── engine.py                             # 5-phase audit orchestrator
│   ├── evaluator.py                          # Criteria evaluator with 95+ verification rules
│   ├── mcp_server.py                         # Model Context Protocol stdio server (6 tools)
│   ├── models.py                             # Immutable Pydantic v2 data models
│   ├── renderer.py                           # Report assembler (MD, JSON, Mermaid LR, Pruning)
│   └── scorer.py                             # Archetype-aware scoring & action planner
├── tests/                                    # 94 Pytest verification tests (100% passing)
├── pyproject.toml                            # PEP 517/621 packaging (Hatchling)
├── README.md                                 # International English documentation
└── README_ES.md                              # Rigorous Spanish documentation
```

---

## 6. Multi-Provider AI Skill Installation

MetricsThinking installs seamlessly as an active skill/tool across all major AI assistant platforms:

### 6.1. Quick Installation via CLI
```bash
# Clone the repository
git clone https://github.com/AlvaroAlejandroFinOps/Metrics.git
cd Metrics

# Install editable package with dev dependencies:
pip install -e ".[dev]"

# Install skill for ALL detected AI providers in current workspace:
metricsthinking install-skill --all
```

Or install directly using the standalone script without pip installation:
```bash
python scripts/install_skill.py --all
```

### 6.2. Targeted Provider Installation
```bash
metricsthinking install-skill --target antigravity   # Google Antigravity (.agents/)
metricsthinking install-skill --target claude        # Anthropic Claude Code (CLAUDE.md)
metricsthinking install-skill --target cursor        # Cursor IDE (.cursor/rules/)
metricsthinking install-skill --target copilot       # GitHub Copilot (.github/)
metricsthinking install-skill --target mcp           # Model Context Protocol snippet
```

### 6.3. Global Google Antigravity Skill Installation
To make the `/metrics` skill available globally across any workspace in Antigravity:
```bash
metricsthinking install-skill --target antigravity --global
```

### 6.4. Model Context Protocol (MCP) Integration
Launch the standard JSON-RPC stdio server:
```bash
metricsthinking mcp
```
Add to your Claude Desktop or Cursor `mcp_config.json`:
```json
{
  "mcpServers": {
    "metricsthinking": {
      "command": "python",
      "args": ["-m", "metricsthinking.mcp_server"]
    }
  }
}
```

---

## 7. Execution & Verification Protocol

### 7.1. Running Forensic Audits
```bash
# List all 14 available profiles and archetypes
metricsthinking list-profiles

# Run full audit on current directory using default profile
metricsthinking audit --target .

# Run audit with specialized archetype profile
metricsthinking audit --target . --profile agent-skill
metricsthinking audit --target . --profile data-platform
metricsthinking audit --target . --profile web-app
metricsthinking audit --target . --profile mlops
metricsthinking audit --target . --profile devsecops

# Run with reversible context pruning and local medallion telemetry
metricsthinking audit --target . --prune --medallion
```

### 7.2. Test Suite & Invariant Verification
```bash
# Run unit, integration, benchmark stress, and hygiene tests (94 tests)
python -m pytest tests/ -v

# Static linting with Ruff
ruff check .
```

---

## 8. Academic & Engineering References

1. IEEE Computer Society. *IEEE Standard for Software and System Test Documentation*. IEEE Std 829-2008.
2. Shannon, C. E. *A Mathematical Theory of Communication*. Bell System Technical Journal, 1948.
3. Fowler, M. *Continuous Integration*. Addison-Wesley, 2006.
4. Bass, L., Clements, P., & Kazman, R. *Software Architecture in Practice (4th Edition)*. Addison-Wesley Professional, 2021.
5. Skelton, M., & Pais, M. *Team Topologies: Organizing Business and Technology Teams for Fast Flow*. IT Revolution Press, 2019.
6. Forsgren, N., Humble, J., & Kim, G. *Accelerate: The Science of Lean Software and DevOps*. IT Revolution Press, 2018.

### BibTeX Citation
```bibtex
@software{metricsthinking_2026,
  author = {HyperScale Thinking Systems},
  title = {MetricsThinking: Universal Technology Project Reverse Engineering and Ground Truth Audit Engine},
  year = {2026},
  version = {4.0.0},
  url = {https://github.com/AlvaroAlejandroFinOps/Metrics}
}
```
