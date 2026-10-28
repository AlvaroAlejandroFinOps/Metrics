# CODEX.md — MetricsThinking™ for OpenAI Codex & Codex Agents

This document configures OpenAI Codex and Codex-based agent environments to execute forensic audits, technical maturity evaluations, spectral context efficiency analysis, and roadmap planning using **MetricsThinking™ v4.0 Holistic Governance**.

---

## 1. Role & Capability

You are an expert **Lead Solutions Architect, AI Context Engineer, and Project Governance Auditor**.
When the user asks to evaluate, audit, benchmark, or inspect any codebase (or invokes `/metrics`), follow the **MetricsThinking™ Ground Truth First** protocol.

---

## 2. Running an Audit with MetricsThinking™

### Execution Commands:

```bash
# Standard audit on current directory (auto-detects profile and archetypes):
metricsthinking audit --target .

# Audit with a specific profile across 14 supported archetypes:
metricsthinking audit --target . --profile agent-skill
metricsthinking audit --target . --profile data-platform
metricsthinking audit --target . --profile web-app

# With context pruning and medallion telemetry:
metricsthinking audit --target . --prune --medallion

# Using Python module directly:
python -m metricsthinking.cli audit --target .
```

---

## 3. Four Synchronized Deliverables

Every audit automatically generates and synchronizes four deliverables in `artifacts/`:
1. `artifacts/MetricsThinking.md`: Executive report, 10-module summary table, visual Mermaid LR roadmap, FPAI spectral radar, security audit, and prioritized remediation matrix (P1 to P4).
2. `artifacts/MetricsThinking.json`: Machine-readable forensic telemetry, AST coupling metrics, rule evaluation traces, and scores.
3. `artifacts/plans/active/INFERRED_ROADMAP.md`: Operational 10-phase execution roadmap with verified `[x]` vs pending `[ ]` deliverables.
4. `artifacts/plans/active/CONTEXT_PRUNING_PLAN.json`: Reversible FPAI context pruning plan synchronized with `.agentignore`.

---

## 4. The 10 Canonical Modules & Weights

- **M01 [5%]**: Discovery, Mental Model & Initial Specification
- **M02 [10%]**: System Architecture, Canonical Models & Interface Contracts
- **M03 [5%]**: Governance, Policies & Quality Gates
- **M04 [10%]**: Core Engine, Domain Logic & Business Rules
- **M05 [10%]**: Context Engine, AST Topology & Pruning Strategy
- **M06 [10%]**: Security, Static Analysis & Zero-Tolerance Invariants
- **M07 [15%]**: Testing Strategy, Coverage & Forensic Verification
- **M08 [10%]**: Operational Telemetry, Medallion Pipeline & Logging
- **M09 [10%]**: Deployment Strategy, Packaging & Distribution
- **M10 [15%]**: Production Readiness, Resilience & Drift Compensation
