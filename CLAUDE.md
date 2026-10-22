# CLAUDE.md — MetricsThinking™ for Claude Code & Anthropic

This document configures Anthropic Claude Code to execute forensic audits, technical maturity evaluations, spectral context efficiency analysis, and roadmap planning using **MetricsThinking™ v4.0 Holistic Governance**.

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
- **M04 [5%]**: Provisioning, Tooling & Synthetic Test Data
- **M05 [25%]**: Core Engine / Business Logic Construction
- **M06 [15%]**: Integration, Serialization & Interoperability
- **M07 [10%]**: Quality Assurance, Stress Testing & Invariants
- **M08 [10%]**: Organizational Validation, Multi-persona Views & CLI
- **M09 [10%]**: CI/CD, Packaging, Build Automation & Distribution
- **M10 [5%]**: Extensibility, Future Adapters & Final Documentation

---

## 5. Ground Truth & Security Anti-Fraud Rules

- **Do NOT** accept stubs, empty functions (`pass`), or placeholder `TODO`/`FIXME` as complete implementations.
- Base all scoring strictly on verifiable code, unit tests, and concrete configuration artifacts.
- Enforce Zero-Tolerance security: verify Shannon entropy $H \le 4.5$ on non-URL tokens, zero hardcoded secrets/API keys, and zero prompt injection attack surface.
