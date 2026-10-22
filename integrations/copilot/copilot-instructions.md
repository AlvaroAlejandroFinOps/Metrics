# GitHub Copilot Instructions for MetricsThinking™ (v4.0 Holistic Governance)

When evaluating, auditing, or planning work in this repository or any target repository:

1. **Adhere to MetricsThinking™**:
   - Assess projects across 10 canonical modules: M01 (Discovery), M02 (Architecture), M03 (Governance), M04 (Tooling), M05 (Core Engine), M06 (Integration), M07 (QA & Stress), M08 (Org Validation & CLI), M09 (CI/CD & Packaging), M10 (Extensibility & Docs).
   - Base all evaluations on verified physical evidence (Ground Truth First) in code, configuration, schemas, and tests.
   - Enforce Zero-Tolerance security: verify Shannon entropy $H \le 4.5$, zero credentials/API keys, and zero prompt injection attack surface.

2. **Run the Forensic Engine**:
   ```bash
   # Run audit on current repository
   metricsthinking audit --target .

   # Run with specialized profile (14 archetypes supported)
   metricsthinking audit --target . --profile agent-skill
   metricsthinking audit --target . --profile data-platform
   metricsthinking audit --target . --profile web-app

   # Install skill for current environment
   metricsthinking install-skill --all
   ```

3. **Four Synchronized Artifacts**:
   - Keep `artifacts/MetricsThinking.md`, `artifacts/MetricsThinking.json`, `artifacts/plans/active/INFERRED_ROADMAP.md`, and `artifacts/plans/active/CONTEXT_PRUNING_PLAN.json` synchronized.
