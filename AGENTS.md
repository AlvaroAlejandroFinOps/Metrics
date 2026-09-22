# AGENTS.md — Universal Agent Instructions for MetricsThinking™

This repository hosts **MetricsThinking™**, the Universal Technology Project Reverse Engineering & Ground Truth Audit Engine.

---

## Agent Role & Principles

When interacting with this codebase or auditing other repositories:
- **Ground Truth First**: Never infer completion from stubs, missing implementations, or placeholders (`pass`, `TODO`, `FIXME`).
- **Mathematical Rigor**: Project maturity is calculated strictly using weighted canonical modules (M01 to M10).
- **Synchronized Artifacts**: Any audit must produce `MetricsThinking.md`, `MetricsThinking.json`, and `INFERRED_ROADMAP.md`.

---

## Executable CLI Reference

```bash
# Run forensic audit on current directory
metricsthinking audit --target .

# Run audit with specialized domain profile
metricsthinking audit --target . --profile data-platform
metricsthinking audit --target . --profile web-app

# Install skill for current environment
metricsthinking install-skill --all
```

---

## Architecture Layout

- `src/metricsthinking/`: Python package containing collector, evaluator, models, renderer, scorer, CLI, and MCP server.
- `config/profiles/`: YAML evaluation profiles (`default.yaml`, `data-platform.yaml`, `web-app.yaml`).
- `schemas/`: JSON schemas validating audit output and telemetry.
- `integrations/`: AI provider integrations (Google Antigravity, Claude Code, Cursor, Copilot, MCP).
- `scripts/`: Standalone scripts (`install_skill.py`).
- `tests/`: Pytest suite with 100% coverage target.
