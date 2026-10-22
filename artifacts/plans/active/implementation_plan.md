# Ultra Thinking Implementation Plan (v3.0.0) — MetricsThinking™ v4.0.0 Holistic Governance

> [!IMPORTANT]
> ### `WORKER EXECUTION DIRECTIVE (TARGET: GEMINI 3.8 FLASH HIGH)`
> This specification has been syntactically decompiled by the Principal Architect (`Argon 4 High`) under the **Architect-to-Flash Bridge** protocol. The tactical execution worker (`gemini-3.8-flash-high`) MUST obey the following deterministic execution loop:
> 1. **Sequential Packet Execution:** Process the Work Breakdown Structure strictly one Flash Execution Packet at a time (`FEP-001` $\to$ execute `verification_cmd` $\to$ verify `exit code 0` $\to$ advance to `FEP-002` up to `FEP-012`).
> 2. **Zero-Context Bleeding:** For each `FEP-###`, load and read **ONLY** the repository-relative files explicitly listed in `read_context` and the frozen signatures in Section 5 (`REG-FROZEN-SIGNATURES`). Do not scan or assume external repository state outside `read_context`.
> 3. **Strict Write Isolation:** Create, modify, or delete **ONLY** the exact repository-relative paths listed in `write_targets` (zero glob wildcards permitted).
> 4. **Signature Immutability:** Never alter class names, method names, parameter names, type annotations, default values, or return types declared under `REG-FROZEN-SIGNATURES`.

## Executive Orientation
This plan specifies the end-to-end architectural reengineering and unification of **MetricsThinking™ v4.0.0 Holistic Governance** `[REQUIRED]`. It merges the 10-module canonical forensic maturity engine (`./src/metricsthinking/`, baseline commit `204d0ea` / `1ce94d4`) with the **FPIA Economy & MemoryOps** spectral/conservative context efficiency engine (`./src/metricsthinking/fpai/`, baseline commit `a4c3fb5`), adds three new forensic evaluation vectors (**Systems Engineering & Resilience**, **Attack Surface & Agentic Security**, and **Deterministic Context Pruning**), and introduces a dual-backend Single-Pass Collector with incremental SHA-256 caching (`./.context/cache/scan_cache.json`) powered by a native Rust `PyO3`/`Maturin` accelerator (`./crates/metricsthinking_rs/`) and a zero-dependency multi-process Python fallback (`./src/metricsthinking/backends/python_fallback.py`) `[REQUIRED]`.

By decompiling all data contracts, Pydantic v2 models, Rust FFI boundaries, analyzer interfaces, and test suites into **Frozen Syntactic Signatures (`REG-FROZEN-SIGNATURES`)** and **12 dependency-ordered Flash Execution Packets (`FEP-001` to `FEP-012`)**, this document enables deterministic, zero-hallucination execution by `gemini-3.8-flash-high` with `0` API token consumption during static audits and `100.0% / 100.0%` mathematical self-audit maturity `[DERIVED]`.

---

## 0. Context Qualification & Evidence Register
- **Operating Environment Mode (`REG-INPUT-QUALIFICATION`):** `Mode A (Live Environment)` `[OBSERVED]`. Direct filesystem, AST, and test-runner inspection executed on the target repository `./` alongside cross-seed forensic ingestion of `./01_seed/seed-metricsthinking-master.md` and `seed-fpia-economy-master.md` `[OBSERVED]`.
- **Portability & Zero-Trust Mandate:** All paths in this specification, code contracts, schemas, and generated artifacts use strictly repository-relative POSIX notation (`./path/to/file`) with `/` separators. Local absolute paths and local `file` scheme URIs are strictly prohibited (`INV-03`, `INV-06`) `[REQUIRED]`.
- **System Stack `[OBSERVED]`:**
  - **Primary Runtime:** Python `3.12.10` (compatible target `>=3.10`, `<3.13`) `[OBSERVED]`.
  - **Core Libraries:** `pydantic==2.13.5` (`>=2.0.0`), `PyYAML==6.0.3` (`>=6.0`), `rich==15.0.0` (`>=13.0.0`), `typer==0.27.2` (`>=0.9.0`), `jsonschema>=4.19.0` `[OBSERVED]`.
  - **QA & Static Analysis:** `pytest==9.1.1`, `pytest-cov==7.1.0`, `ruff==0.16.8`, `mypy==2.3.1` invoked via `python -m <tool>` `[OBSERVED]`.
  - **Native Accelerator Stack:** Rust Edition 2021 (`./crates/metricsthinking_rs/Cargo.toml`) using `pyo3 = "0.21"`, `ignore = "0.4"`, `rayon = "1.10"`, `regex = "1.10"`, `aho-corasick = "1.1"`, `sha2 = "0.10"`, `fxhash = "0.2"`, `serde = "1.0"`, `serde_json = "1.0"`, built optionally via `maturin`, with automatic runtime fallback to `concurrent.futures.ProcessPoolExecutor` when `cargo`/`maturin` is absent on the host machine `[OBSERVED]`.

### Epistemic Evidence Register
| Evidence ID | Source Artifact / Command | Epistemic Tag | Verified Fact |
| :--- | :--- | :--- | :--- |
| `EV-01` | `./01_seed/seed-metricsthinking-master.md` | `[OBSERVED]` | MetricsThinking v3.0 architecture, 14 YAML profiles, 54 unit tests, Tension Vectors `T-01` to `T-06`, active bottleneck `M07` (`66.7%`, overall `96.67%`). |
| `EV-02` | `./01_seed/seed-fpia-economy-master.md` | `[OBSERVED_IN_SEED]` | FPIA Economy v3.0 architecture (`packages/fpai_core`), bimodal spectral $S_{\text{spectral}} = \sqrt{P^2+Q^2+D^2}$ and linear $S_{\text{linear}} = P+Q+D$, ADR-001, ADR-002, 92 unit tests passing. |
| `EV-03` | `./requirements.txt` | `[OBSERVED]` | Encoded in `UTF-16LE` with non-portable editable local path and stale comment `metricsthinking==2.0.0` (`Vector T-01`). |
| `EV-04` | `./src/cloud_jobs/`, `./src/core/`, `./src/dashboards/`, `./src/data_generation/`, `./tools/` | `[OBSERVED]` | Legacy skeleton directories containing only `.context.yaml` and zero Python source files (`Vector T-02`). |
| `EV-05` | `./02_foundation/engine/engine_readme.md` | `[OBSERVED]` | Line 8 references non-existent `01_seed/seed-idirectory-master.md` (`Vector T-03`). |
| `EV-06` | `./src/metricsthinking/__init__.py` & `./src/metricsthinking/mcp_server.py` | `[OBSERVED]` | `__init__.py` line 5 declares `__version__ = "1.0.0"`; `mcp_server.py` line 161 declares `"version": "2.0.0"`; `pyproject.toml` line 7 declares `version = "3.0.0"` (`Vector T-04`). |
| `EV-07` | `python -m pytest --collect-only -q` | `[OBSERVED]` | 54 tests collected across 8 test files in `./tests/`, passing 100% (`54 passed`). |
| `EV-08` | Host toolchain check (`python --version`, `cargo`) | `[OBSERVED]` | `Python 3.12.10` active; `pytest` and `ruff` invoked via `python -m`; `cargo` binary not on default system `PATH`, confirming necessity of `python_fallback.py`. |

---

## 1. Repository Forensics

### 1.1 Baseline Audit & Runtime Observations
- **Git Baseline `[OBSERVED]`:** Branch `master`, HEAD commit `1ce94d4` (parent `204d0ea`).
- **Test Suite Baseline `[OBSERVED]`:** Executing `python -m pytest -q` runs `54` tests across `8` test modules (`./tests/test_calibration.py`: 4, `./tests/test_cli.py`: 2, `./tests/test_collector.py`: 3, `./tests/test_evaluator.py`: 2, `./tests/test_installer.py`: 7, `./tests/test_renderer.py`: 3, `./tests/test_scorer.py`: 1, `./tests/test_v3_archetypes.py`: 32) with `100%` pass rate.
- **Collector I/O Bottleneck `[OBSERVED]`:** `./src/metricsthinking/collector.py` performs an uncached `os.walk` followed by synchronous sequential file reads (`_read_key_content`), while `./src/metricsthinking/evaluator.py` re-reads source and script files on demand (lines 674-678) without SHA-256 content caching or multi-core parallelism.

### 1.2 Public Compatibility Obligations (`C-###`)
| Obligation ID | Surface | Compatibility Contract | Disposition in v4.0.0 |
| :--- | :--- | :--- | :--- |
| `C-001` | `metricsthinking.engine.run_audit` | Must accept `(target_path, profile_name, archetype, out_dir, prefix, quiet)` and return `tuple[ProjectAuditReport, dict[str, Path]]`. | `[PRESERVE]` — New parameters (`prune`, `medallion`, `use_cache`) added with backward-compatible defaults (`False`, `False`, `True`). |
| `C-002` | `ProjectAuditReport` fields | Existing JSON/Pydantic properties (`project_name`, `consolidated_score`, `maturity_band`, `active_bottleneck`, `modules`, `remediation_plan`, `stats`) must remain intact for `./tests/test_calibration.py` and `./tests/fixtures/sample_golden_audit.json`. | `[PRESERVE]` — New v4.0 report blocks (`fpai_report`, `security_report`, `resilience_report`, `pruning_plan`) are populated with default-factories so existing constructors and tests never break. |
| `C-003` | Canonical 14 YAML Profiles | Every profile in `./config/profiles/` must contain `M01` through `M10` whose weights sum to `1.0`. | `[PRESERVE]` — Existing 10 module weights are preserved; new forensic rules are wired into `CriteriaEvaluator` and profile metadata. |
| `C-004` | MCP JSON-RPC Server | Must expose `audit_repository`, `list_profiles`, `get_audit_report` over stdio JSON-RPC `2.0`. | `[MODIFY]` — Preserves the 3 legacy tools, updates version to `"4.0.0"`, and adds 3 new tools (`scan_fpai_context`, `generate_pruning_plan`, `run_medallion_telemetry`) for a total of 6 tools. |

### 1.3 Defensive Code Debt & Tension Vectors Audited
1. **`T-01` (`./requirements.txt`):** Encoded in `UTF-16LE` with a hardcoded local editable path (`-e`) and `metricsthinking==2.0.0` `[OBSERVED]`.
2. **`T-02` (Legacy Empty Skeleton Directories):** `./src/cloud_jobs/`, `./src/core/`, `./src/dashboards/`, `./src/data_generation/`, and `./tools/` contain only `.context.yaml` and pollute `.context/tree.json` `[OBSERVED]`.
3. **`T-03` (`./02_foundation/engine/engine_readme.md`):** Points to `01_seed/seed-idirectory-master.md` instead of `01_seed/seed-metricsthinking-master.md` `[OBSERVED]`.
4. **`T-04` (Version Drift):** `__init__.py` (`1.0.0`), `mcp_server.py` (`2.0.0`), and `pyproject.toml` (`3.0.0`) disagree `[OBSERVED]`.
5. **`T-05` (`PYTHONPATH` / CLI invocation):** Direct `python -m metricsthinking.cli` requires editable installation or `src` path resolution `[OBSERVED]`.
6. **`T-06` (`M07` Bottleneck at `66.7%`):** Missing `./tests/test_benchmarks_stress.py` (`M07-C03` in `default.yaml`) and `./artifacts/benchmark_coverage_report.json` (`M07-C02` in `agent-skill.yaml`) `[OBSERVED]`.

---

## 2. Requirement Traceability & Gap Analysis

| ID | Source Tag | Requirement | Baseline State | Gap | Decision | WBS Phase / FEP-ID | Verification Test | Migration |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `R-001` | `[REQUIRED]` | Sanitize `./requirements.txt` to pure UTF-8 without BOM, remove local absolute path `-e`, and sync dependencies with `./pyproject.toml` v4.0.0 (`T-01`). | `UTF-16LE` with local `-e` path `[OBSERVED]`. | Encoding & portability violation. | Rewrite `./requirements.txt` and bump `./pyproject.toml` to `4.0.0`. | `Phase 1 / FEP-001` | `./tests/test_hygiene_v4.py::test_requirements_utf8_and_clean` | Overwrite in UTF-8 without BOM. |
| `R-002` | `[REQUIRED]` | Remove empty legacy skeleton folders (`./src/cloud_jobs/`, `./src/core/`, `./src/dashboards/`, `./src/data_generation/`, `./tools/`) and prune `./.context/tree.json` (`T-02`). | 5 skeleton dirs with only `.context.yaml` `[OBSERVED]`. | Cognitive ballast in repo tree. | Delete empty dirs and update `./.context/tree.json`. | `Phase 1 / FEP-001` | `./tests/test_hygiene_v4.py::test_no_empty_skeleton_dirs` | Remove dead nodes from `tree.json`. |
| `R-003` | `[REQUIRED]` | Fix broken seed reference in `./02_foundation/engine/engine_readme.md` line 8 (`T-03`) and unify `__version__ = "4.0.0"` across `./src/metricsthinking/__init__.py`, `./src/metricsthinking/mcp_server.py`, and `./mcp_metricsthinking.json` (`T-04`). | Points to `seed-idirectory-master.md`; versions `1.0.0`/`2.0.0`/`3.0.0` `[OBSERVED]`. | Documentation and MCP version drift. | Update reference and synchronize `"4.0.0"` across all modules. | `Phase 1 / FEP-001` | `./tests/test_hygiene_v4.py::test_version_and_seed_ref_sync` | Backward-compatible version bump. |
| `R-004` | `[REQUIRED]` | Unify Pydantic v2 models in `./src/metricsthinking/models.py` with FPIA contracts (`FPAISpectralVector`, `SecurityVulnerabilityReport`, `SystemsResilienceReport`, `ContextPruningPlan`) and update JSON Schemas in `./schemas/`. | Only M01-M10 maturity models exist in `models.py` `[OBSERVED]`. | Missing FPIA, Security, Resilience, and Pruning contracts. | Extend `models.py` and `./schemas/project_audit_report.schema.json`; add v2 FPIA schemas. | `Phase 2 / FEP-002` | `./tests/test_models_schemas_v4.py::test_v4_models_and_schemas` | Default factories preserve v3 callers. |
| `R-005` | `[REQUIRED]` | Integrate FPIA Spectral & Confidence engines (`./src/metricsthinking/fpai/spectral_engine.py`, `./src/metricsthinking/fpai/confidence.py`) preserving bimodal $S_{\text{spectral}}$ / $S_{\text{linear}}$ (`INV-01`) and decoupled governance gate $G$ (`INV-02`). | Resides in external FPIA project `[OBSERVED_IN_SEED]`. | Not integrated in `./src/metricsthinking/fpai/`. | Create `./src/metricsthinking/fpai/spectral_engine.py` and `confidence.py`. | `Phase 3 / FEP-003` | `./tests/fpai/test_spectral_and_confidence.py` | Clean subpackage import under `metricsthinking.fpai`. |
| `R-006` | `[REQUIRED]` | Implement `SecurityGatekeeper` (`./src/metricsthinking/fpai/gatekeeper.py`) with secret regexes, PII detection, Shannon entropy $H > 4.5$, and `scan_agentic_surface()` for prompt injection / MCP tool poisoning / unsafe `eval`/`exec`/`shell=True`. | No agentic prompt injection or Shannon entropy scanner in `metricsthinking` `[OBSERVED]`. | Missing `gatekeeper.py` and agentic surface scanner. | Implement `gatekeeper.py` and `./config/fpai_governance.yaml`. | `Phase 3 / FEP-004` | `./tests/test_security_resilience_pruning.py::test_gatekeeper_and_agentic_surface` | Redact all matched snippets as `<REDACTED>`. |
| `R-007` | `[REQUIRED]` | Implement `SeedDriftAuditor` (`./src/metricsthinking/fpai/drift_auditor.py`) and `CompensationPlanner` (`./src/metricsthinking/fpai/compensation.py`) with idempotent marker-bounded `./.agentignore` auto-pruning. | No AST-to-Seed drift checker or `.agentignore` pruner `[OBSERVED]`. | Missing `drift_auditor.py` and `compensation.py`. | Implement both modules with `# >>> METRICSTHINKING AUTO-PRUNE >>>` markers. | `Phase 3 / FEP-005` | `./tests/test_security_resilience_pruning.py::test_seed_drift_and_compensation` | Idempotent marker block in `./.agentignore`. |
| `R-008` | `[REQUIRED]` | Migrate local Medallion pipeline (`Bronze -> Silver -> Gold` JSONL), `AblationRunner` (5% sampling `INV-03`), `MultiLayerResolver` (4-layer attribution), and `./scripts/hnsw_index_rebuild.py`. | Absent in unified repository `[OBSERVED]`. | Missing `medallion.py`, `ablation.py`, `attribution.py`, `hnsw_index_rebuild.py`. | Implement all 4 modules with zero cloud dependencies (`INV-09`). | `Phase 3 / FEP-006` | `./tests/fpai/test_medallion_ablation_attribution.py` | Local JSONL folders created on demand. |
| `R-009` | `[REQUIRED]` | Create native Rust accelerator crate `./crates/metricsthinking_rs/` (`PyO3` + `rayon` + `ignore` + `sha2` + `aho-corasick` + `fxhash`) exposing `scan_workspace_fast`. | No `./crates/metricsthinking_rs/` directory exists `[OBSERVED]`. | Missing Rust source crate for native compilation. | Author complete Rust crate (`Cargo.toml`, `lib.rs`, `walker.rs`, `entropy_sec.rs`, `ast_graph.rs`, `ballast_tokens.rs`). | `Phase 4 / FEP-007` | `./tests/test_backends_collector.py::test_rust_crate_manifest_and_sources` | Optional native build via `maturin`; graceful fallback. |
| `R-010` | `[REQUIRED]` | Implement Single-Pass Collector (`./src/metricsthinking/collector.py`) with automatic backend selector (`./src/metricsthinking/backends/`) and SHA-256 incremental cache (`./.context/cache/scan_cache.json`) achieving $< 300\text{ ms}$ warm runs. | Multi-pass uncached `collector.py` `[OBSERVED]`. | Missing SHA-256 cache, AST coupling/dead-code extraction, and shingling in single pass. | Implement `backends/__init__.py`, `backends/python_fallback.py`, and refactor `collector.py`. | `Phase 4 / FEP-008` | `./tests/test_backends_collector.py::test_single_pass_and_sha256_cache` | Cache stored in `./.context/cache/scan_cache.json`. |
| `R-011` | `[REQUIRED]` | Expand `CriteriaEvaluator`, `AuditScorer`, `ReportRenderer`, `cli.py`, and `mcp_server.py` (6 tools) to evaluate and render FPIA Spectral Power, Security & Systems Resilience, and Context Pruning Plan. | Only M01-M10 sections rendered; 3 MCP tools `[OBSERVED]`. | Missing 5 new `check_*` methods, 3 Markdown sections, CLI flags (`--prune`, `--medallion`, `--no-cache`), and 3 MCP tools. | Upgrade `evaluator.py`, `scorer.py`, `renderer.py`, `engine.py`, `cli.py`, and `mcp_server.py`. | `Phase 5 / FEP-009` & `FEP-010` | `./tests/test_cli.py`, `./tests/test_renderer.py`, `./tests/test_mcp_v4.py` | Preserves `INV-04`, `INV-05`, `INV-06`, `INV-07`. |
| `R-012` | `[REQUIRED]` | Close `M07` bottleneck (`T-06`) to reach `100.0% / 100.0%` maturity via `./tests/test_benchmarks_stress.py` (1,000-file synthetic stress benchmark emitting `./artifacts/benchmark_coverage_report.json`) and synchronize `./01_seed/seed-metricsthinking-master.md` v4.0 (`seed_to_code_drift_count == 0`). | `M07` at `66.7%`, overall score `96.67%` `[OBSERVED]`. | Missing stress benchmark suite, coverage artifact, and v4.0 seed AST signatures. | Create `./tests/test_benchmarks_stress.py`, update `./01_seed/seed-metricsthinking-master.md`, and run holistic self-audit. | `Phase 6 / FEP-011` & `FEP-012` | `./tests/test_benchmarks_stress.py` | Updates `./artifacts/MetricsThinking.json` to `100.0%`. |

- **Orphan Requirements Gate Verification:** $\mathcal{I}_{\text{orphan\_req}} = 0$ (`12/12` `[REQUIRED]` requirements mapped to explicit `FEP-###` packets and automated pytest verification tests) `[DERIVED]`.
- **Orphan Components Gate Verification:** $\mathcal{I}_{\text{orphan\_comp}} = 0$ (Every component tagged `[NEW]` in Section 4 is bound to an explicit `R-###` and `INV-###`) `[DERIVED]`.

---

## 3. Architectural Alternatives, Decisions & Invariants

### 3.1 Trade-off Analysis of Discarded Alternatives
1. **Alternative A — Pure Rust Binary Replacing Python Entirely:** Discarded because `MetricsThinking` relies on Pydantic v2 schemas, dynamic YAML evaluation profiles, and multi-assistant Python skill installers (`C-001` to `C-004`), and host environments without `cargo` (`EV-08`) would fail to install or run the auditor.
2. **Alternative B — LLM-Driven Semantic Dead-Code & Drift Detection:** Discarded because invoking an external LLM during static repository audits violates the `0 token` deterministic execution contract and introduces network latency, non-determinism, and credential dependencies.
3. **Alternative C — Destructive Automatic File Deletion During Pruning:** Discarded because irreversible deletion of source files without human confirmation violates safety guardrails; instead, pruning actions are emitted to `./artifacts/plans/active/CONTEXT_PRUNING_PLAN.json` and applied idempotently to `./.agentignore` bounded by `# >>> METRICSTHINKING AUTO-PRUNE >>>` markers.

### 3.2 Architectural Decision Records (`ADR-###`)
- **`ADR-001` (Bimodal Spectral & Linear Context Power Model):** Preserve and compute simultaneously Budeanu's Euclidean Spectral Apparent Power $S_{\text{spectral}} = \sqrt{P^2 + Q^2 + D^2}$ and Conservative Linear Apparent Power $S_{\text{linear}} = P + Q + D$, where $Q = Q_{\text{dead}} + Q_{\text{dup}}$, preventing premature scalar collapse `[OBSERVED_IN_SEED]`.
- **`ADR-002` (Decoupled Zero-Tolerance Governance Gate $G$):** When `SecurityGatekeeper` detects any critical secret ($H > 4.5$ or regex match), PII leak, or agentic prompt injection, set `governance_gate = GovernanceStatus.DISQUALIFIED_SECURITY` and `is_deployable = False`, while preserving raw technical scores ($P, Q, D$ and M01-M10 maturity) to prevent diagnostic blindness `[OBSERVED_IN_SEED]`.
- **`ADR-006` (Dual-Backend Single-Pass Collector with Incremental SHA-256 Cache):** Unify file walking, SHA-256 hashing, token counting (`chars / 3.8`), secret/entropy scanning, Python AST symbol/import graph extraction, and 5-gram `fxhash`/CRC32 shingling into a single pass backed by `./.context/cache/scan_cache.json`. Try importing `metricsthinking._core_rs` (PyO3 Rust extension) first; if unavailable, transparently execute `metricsthinking.backends.python_fallback` using deterministic caching and multi-process execution `[REQUIRED]`.
- **`ADR-007` (Orthogonal Forensic Vectors Preserving Canonical M01-M10 Weights):** Keep the 10 canonical modules (`M01`–`M10`) summing strictly to `1.0` across all 14 YAML profiles (`INV-04`), while attaching `fpai_report`, `security_report`, `resilience_report`, and `pruning_plan` as first-class typed vectors on `ProjectAuditReport` and injecting their P1–P3 findings into `remediation_plan` `[REQUIRED]`.

### 3.3 Invariant Ledger (`INV-###`)
| Invariant ID | Mathematical / Logical Rule | Automated Enforcement Mechanism | Failure Action |
| :--- | :--- | :--- | :--- |
| `INV-01` | **Bimodal Power Conservation & Ground Truth:** $S_{\text{spectral}} = \sqrt{P^2 + (Q_{\text{dead}} + Q_{\text{dup}})^2 + D_{\text{struct}}^2}$ and $S_{\text{linear}} = P + Q_{\text{dead}} + Q_{\text{dup}} + D_{\text{struct}}$; zero maturity credit for empty `pass` stubs or `TODO`/`FIXME` placeholders. | `FPAIEngine.evaluate()` unit assertions in `./tests/fpai/test_spectral_and_confidence.py`. | Fail test suite and reject score calculation. |
| `INV-02` | **Decoupled Security Gate ($G$):** $\text{findings}_{\text{critical}} > 0 \implies \text{governance\_gate} = \text{DISQUALIFIED\_SECURITY} \land \text{is\_deployable} = \text{False} \land (P, Q, D \text{ preserved})$. | `SecurityGatekeeper` + `FPAIEngine` test in `./tests/test_security_resilience_pruning.py`. | Disqualify deployment (`is_deployable = False`) while emitting full diagnostic report. |
| `INV-03` | **5% Stochastic Ablation Ceiling & Zero-Token Static Scan:** Static `run_audit()` consumes `0` external LLM tokens; `AblationRunner` enforces `effective_sampling_rate <= 0.05` by default. | `./tests/fpai/test_medallion_ablation_attribution.py` verifying zero network/API calls and `0.05` sampling rate. | Raise `ValueError` if static audit attempts external API call. |
| `INV-04` | **Canonical Module Weight Normalization:** $\forall \text{profile} \in \text{Profiles}_{14}: \sum_{i=1}^{10} W(M_i) = 1.0 \pm 10^{-6}$ and $\|\text{modules}\| = 10$. | `./tests/test_v3_archetypes.py` and `./schemas/project_audit_report.schema.json`. | Reject profile load with schema validation error. |
| `INV-05` | **Synchronized Quad-Modal Artifacts:** `run_audit()` atomically writes `./artifacts/MetricsThinking.md`, `./artifacts/MetricsThinking.json`, `./artifacts/plans/active/INFERRED_ROADMAP.md`, and `./artifacts/plans/active/CONTEXT_PRUNING_PLAN.json`. | `ReportRenderer.write_artifacts()` verified in `./tests/test_renderer.py`. | Fail audit command with non-zero exit code. |
| `INV-06` | **Horizontal Mermaid LR & Portable Relative Paths:** All Mermaid diagrams use `flowchart LR` without nested vertical subgraphs; zero local absolute paths or `file:` scheme URIs in any repository file, seed, or artifact. | `./tests/test_hygiene_v4.py` and `./tests/test_renderer.py` regex assertions. | Block test gate on any absolute path or nested subgraph. |
| `INV-07` | **Atomic UTF-8 Write Without BOM:** Every file written by `ReportRenderer`, `CompensationPlanner`, or `MedallionPipeline` uses `encoding="utf-8"` without BOM (`\ufeff`). | Byte-prefix inspection in `./tests/test_hygiene_v4.py`. | Fail verification gate if BOM `0xEF,0xBB,0xBF` or `0xFF,0xFE` is detected. |
| `INV-08` | **Zero-Trust Secret Redaction:** Every `FileAuditFinding` generated by `SecurityGatekeeper` masks the matched secret value with `<REDACTED>` in descriptions and JSON outputs. | `./tests/test_security_resilience_pruning.py::test_shannon_entropy_and_secret_redaction`. | Strip raw secret string before constructing `FileAuditFinding`. |

---

## 4. Target Architecture & Dependency Boundaries

### 4.1 Unified Target Directory Tree with Explicit AST Tags
```text
./
├── .agentignore                                              [MODIFY] (R-007, INV-07: Idempotent auto-prune block support)
├── .agents/skills/metrics/SKILL.md                           [MODIFY] (R-011, INV-06: Document v4.0 flags --prune, --medallion, --no-cache)
├── .context/
│   ├── tree.json                                             [MODIFY] (R-002, INV-06: Prune 5 legacy skeleton nodes, register fpai & crates)
│   └── cache/
│       └── scan_cache.json                                   [NEW] (R-010, INV-07: Incremental SHA-256 single-pass scan cache)
├── .cursor/rules/metrics.mdc                                 [PRESERVE]
├── .github/
│   ├── copilot-instructions.md                               [PRESERVE]
│   └── workflows/ci.yml                                      [MODIFY] (R-009, INV-04: Python 3.10-3.12 matrix + optional Rust check + --prune --medallion)
├── 01_seed/
│   ├── .context.yaml                                         [PRESERVE]
│   └── seed-metricsthinking-master.md                        [MODIFY] (R-012, INV-02: Unified v4.0 DNA with 1-line AST signatures & 0 drift)
├── 02_foundation/engine/
│   ├── .context.yaml                                         [PRESERVE]
│   └── engine_readme.md                                      [MODIFY] (R-003, INV-06: Fix line 8 reference to 01_seed/seed-metricsthinking-master.md)
├── artifacts/
│   ├── MetricsThinking.json                                  [MODIFY] (R-011, INV-05: Unified v4.0 report with fpai, security, resilience, pruning)
│   ├── MetricsThinking.md                                    [MODIFY] (R-011, INV-05: Executive dashboard + Spectral Power + Security + Pruning)
│   ├── benchmark_coverage_report.json                        [NEW] (R-012, INV-01: Deterministic 1,000-file stress benchmark report closing M07)
│   └── plans/active/
│       ├── INFERRED_ROADMAP.md                               [MODIFY] (R-011, INV-05: Operational 10-phase checklist + P1-P4 remediation)
│       └── CONTEXT_PRUNING_PLAN.json                         [NEW] (R-007, INV-05: Reversible context compensation and pruning plan)
├── config/
│   ├── .context.yaml                                         [PRESERVE]
│   ├── fpai_governance.yaml                                  [NEW] (R-006, INV-02: Spectral thresholds, H=4.5, p0-p3 token budgets, CI gates)
│   └── profiles/                                             [MODIFY] (R-011, INV-04: 14 YAML profiles enriched with v4.0 metadata & rules)
├── crates/
│   └── metricsthinking_rs/                                   [NEW] (R-009, ADR-006: Native Rust PyO3 accelerator crate)
│       ├── Cargo.toml                                        [NEW] (R-009, ADR-006: cdylib manifest with pyo3, ignore, rayon, sha2, regex, fxhash)
│       └── src/
│           ├── lib.rs                                        [NEW] (R-009, ADR-006: PyO3 module _core_rs exposing scan_workspace_fast)
│           ├── walker.rs                                     [NEW] (R-009, ADR-006: Parallel WalkParallel + SHA-256 + token calibration)
│           ├── entropy_sec.rs                                [NEW] (R-009, INV-08: RegexSet + Shannon entropy H > 4.5 + PII + redaction)
│           ├── ast_graph.rs                                  [NEW] (R-009, ADR-006: Symbol reachability Q_dead, coupling Ca/Ce, cycles, SPOF)
│           └── ballast_tokens.rs                             [NEW] (R-009, INV-01: 5-gram fxhash shingling Q_dup & token accounting)
├── data/
│   ├── raw/telemetry/                                        [NEW] (R-008, INV-03: Local immutable Bronze JSONL telemetry zone)
│   └── processed/telemetry/                                  [NEW] (R-008, INV-03: Local Silver & Gold JSONL efficiency summaries)
├── schemas/
│   ├── audit_criterion.schema.json                           [PRESERVE]
│   ├── canonical_module.schema.json                          [PRESERVE]
│   ├── evidence_primitives.schema.json                       [PRESERVE]
│   ├── project_audit_report.schema.json                      [MODIFY] (R-004, INV-04: Expanded to v4.0 with fpai, security, resilience, pruning)
│   ├── repo_fpai_manifest.v2.json                            [NEW] (R-004, INV-01: Formal JSON Schema v2 for FPIA repository manifest)
│   ├── telemetry_event.v2.json                               [NEW] (R-004, INV-07: Formal JSON Schema v2 for Bronze/Silver telemetry events)
│   └── thinking_seed_v3.schema.json                          [PRESERVE]
├── scripts/
│   ├── .context.yaml                                         [PRESERVE]
│   ├── install_skill.py                                      [PRESERVE]
│   └── hnsw_index_rebuild.py                                 [NEW] (R-008, ADR-001: Physical HNSW tombstone purge and latency restoration script)
├── src/
│   ├── cloud_jobs/                                           [DELETE] (R-002: Remove empty legacy skeleton directory)
│   ├── core/                                                 [DELETE] (R-002: Remove empty legacy skeleton directory)
│   ├── dashboards/                                           [DELETE] (R-002: Remove empty legacy skeleton directory)
│   ├── data_generation/                                      [DELETE] (R-002: Remove empty legacy skeleton directory)
│   └── metricsthinking/
│       ├── __init__.py                                       [MODIFY] (R-003: Export __version__ = "4.0.0" and unified public API)
│       ├── cli.py                                            [MODIFY] (R-011: Add --prune, --medallion, --no-cache flags and prune/medallion subcommands)
│       ├── collector.py                                      [MODIFY] (R-010, ADR-006: Single-Pass Collector with SHA-256 cache & backend bridge)
│       ├── engine.py                                         [MODIFY] (R-011, INV-05: Unified run_audit() orchestrating M01-M10 + FPIA + Medallion + Pruning)
│       ├── evaluator.py                                      [MODIFY] (R-011, INV-04: Add check_security_*, check_systems_resilience_*, check_context_fpai_*)
│       ├── mcp_server.py                                     [MODIFY] (R-003, R-011: Version 4.0.0 + 6 JSON-RPC tools)
│       ├── models.py                                         [MODIFY] (R-004, INV-01: Unified Pydantic v2 contracts for Maturity + FPIA + Sec + Sys + Pruning)
│       ├── renderer.py                                       [MODIFY] (R-011, INV-05: Render 3 new executive Markdown sections & CONTEXT_PRUNING_PLAN.json)
│       ├── scorer.py                                         [MODIFY] (R-011, INV-02: Compute maturity + FPAI vector + Sec/Resilience + P1-P4 remediation)
│       ├── backends/
│       │   ├── __init__.py                                   [NEW] (R-010, ADR-006: Automatic selector between _core_rs and python_fallback)
│       │   └── python_fallback.py                            [NEW] (R-010, ADR-006: Deterministic ProcessPool/Single-Pass SHA-256 scanner in pure Python)
│       └── fpai/
│           ├── __init__.py                                   [NEW] (R-005, INV-01: FPIA subpackage exports)
│           ├── spectral_engine.py                            [NEW] (R-005, INV-01: FPAIEngine computing S_spectral, S_linear, and decoupled G gate)
│           ├── confidence.py                                 [NEW] (R-005, INV-01: ConfidenceCalculator CI95% envelope and ComparabilityValidator)
│           ├── ablation.py                                   [NEW] (R-008, INV-03: AblationRunner with 5% stochastic sampling and V_marginal LOO)
│           ├── attribution.py                                [NEW] (R-008, INV-01: MultiLayerResolver 4-layer lexical, entity, AST graph, NLI attribution)
│           ├── compensation.py                               [NEW] (R-007, INV-07: CompensationPlanner and idempotent .agentignore pruner)
│           ├── drift_auditor.py                              [NEW] (R-007, INV-01: SeedDriftAuditor comparing 01_seed AST signatures vs live AST)
│           ├── gatekeeper.py                                 [NEW] (R-006, INV-02: SecurityGatekeeper regex, PII, Shannon H>4.5, scan_agentic_surface)
│           └── medallion.py                                  [NEW] (R-008, INV-07: Local Bronze -> Silver -> Gold JSONL telemetry pipeline)
├── tools/                                                    [DELETE] (R-002: Remove empty legacy skeleton directory)
├── tests/
│   ├── fpai/
│   │   ├── __init__.py                                       [NEW] (R-005, R-008: FPIA test suite package)
│   │   ├── test_spectral_and_confidence.py                   [NEW] (R-005, INV-01: Unit tests for spectral/linear math, G decoupling, CI95%)
│   │   └── test_medallion_ablation_attribution.py            [NEW] (R-008, INV-03: Unit tests for Medallion Bronze/Silver/Gold, Ablation, Attribution, HNSW)
│   ├── test_hygiene_v4.py                                    [NEW] (R-001, R-002, R-003: Tests for UTF-8 requirements, no skeleton dirs, version 4.0.0)
│   ├── test_models_schemas_v4.py                             [NEW] (R-004, INV-04: Tests for v4.0 Pydantic models and JSON Schemas)
│   ├── test_backends_collector.py                            [NEW] (R-009, R-010: Tests for Single-Pass Collector, SHA-256 cache, and Rust/Python backends)
│   ├── test_security_resilience_pruning.py                   [NEW] (R-006, R-007: Tests for Shannon entropy, prompt injection, AST cycles, drift, .agentignore)
│   ├── test_mcp_v4.py                                        [NEW] (R-011: Tests for 6 MCP JSON-RPC tools and v4.0.0 protocol)
│   └── test_benchmarks_stress.py                             [NEW] (R-012, INV-01: 1,000-file stress benchmark & cache speedup test closing M07)
├── mcp_metricsthinking.json                                  [MODIFY] (R-003: Add version "4.0.0" metadata)
├── pyproject.toml                                            [MODIFY] (R-001: Bump version to "4.0.0", include jsonschema>=4.19.0)
└── requirements.txt                                          [MODIFY] (R-001, INV-07: Pure UTF-8 without BOM, clean pinned dependencies)
```

### 4.2 Layer Ownership & Import Acyclicity Rules
To guarantee `cyclic_dependencies_count == 0` across `./src/metricsthinking/`:
1. **Layer 0 (`models.py`):** Pure Pydantic v2 data structures and Enums. **Forbidden** from importing any other module in `metricsthinking`.
2. **Layer 1 (`fpai/*` and `backends/*`):** Import only from standard library, third-party packages (`pydantic`, `yaml`), and `metricsthinking.models`. **Forbidden** from importing `collector`, `evaluator`, `scorer`, `renderer`, `engine`, `cli`, or `mcp_server`.
3. **Layer 2 (`collector.py`):** Imports from `models.py`, `backends`, and `fpai` (`gatekeeper`, `drift_auditor`). **Forbidden** from importing `evaluator`, `scorer`, `renderer`, `engine`.
4. **Layer 3 (`evaluator.py`, `scorer.py`, `renderer.py`):** Import from `models.py`, `collector.py`, and `fpai/*`. Pairwise independent (`evaluator`, `scorer`, and `renderer` never import each other).
5. **Layer 4 (`engine.py`):** Orchestrates `collector`, `evaluator`, `scorer`, `renderer`, `fpai.compensation`, and `fpai.medallion`.
6. **Layer 5 (`cli.py`, `mcp_server.py`):** Top-level entrypoints importing `engine.py`, `models.py`, and `fpai/*`.

---

## 5. Contract, Interface & Data Specifications (`REG-FROZEN-SIGNATURES`)

> [!CAUTION]
> **Worker Immutability Mandate (`REG-FROZEN-SIGNATURES`):** Every contract below is frozen. `gemini-3.8-flash-high` workers MUST implement these exact class names, field names, method signatures, parameter defaults, and return types without modification.

### 5.1 Unified Data Contracts (`./src/metricsthinking/models.py`)
- **Producers:** `ProjectCollector`, `FPAIEngine`, `SecurityGatekeeper`, `SeedDriftAuditor`, `CompensationPlanner`, `CriteriaEvaluator`, `AuditScorer`.
- **Consumers:** `ReportRenderer`, `run_audit`, `mcp_server`, JSON Schema validators.

```python
"""
Frozen Contract 5.1: ./src/metricsthinking/models.py
Governing Invariants: INV-01, INV-02, INV-04, INV-08 | Requirements: R-004
"""
from __future__ import annotations

from enum import Enum
from typing import Any
from pydantic import BaseModel, Field


class DomainArchetype(str, Enum):
    SOFTWARE_ENGINEERING = "software-engineering"
    MLOPS = "mlops"
    LLMOPS = "llmops"
    DATAOPS = "dataops"
    GITOPS = "gitops"
    PLATFORM_ENG = "platform-eng"
    DEVSECOPS = "devsecops"
    DUAL_TRACK = "dual-track"
    TEAM_TOPOLOGIES = "team-topologies"
    CHAOS_ENG = "chaos-eng"
    SDD = "sdd"
    DATA_PLATFORM = "data-platform"
    WEB_APP = "web-app"
    AGENT_SKILL = "agent-skill"
    CUSTOM = "custom"


class InspectionMode(str, Enum):
    SOURCE_CODE = "source_code"
    DECLARATIVE_CONFIG = "declarative_config"
    PIPELINE_ORCHESTRATION = "pipeline_orchestration"
    GOVERNANCE_SPEC = "governance_spec"
    POLYGLOT_HYBRID = "polyglot_hybrid"


class ModuleStatus(str, Enum):
    DONE = "done"
    ACTIVE = "active"
    BACKLOG = "backlog"
    BLOCKED = "blocked"


class MaturityBand(str, Enum):
    INITIAL_RISK = "Fase Inicial / Riesgo Crítico (0.0% - 49.9%)"
    CONSTRUCTION = "Construcción Activa / Madurez Media (50.0% - 74.9%)"
    ADVANCED_MATURITY = "Madurez Avanzada / Pre-producción (75.0% - 89.9%)"
    OPERATIONAL_EXCELLENCE = "Excelencia Operativa / Producción (90.0% - 100.0%)"


class PowerType(str, Enum):
    ACTIVE = "ACTIVE"
    REACTIVE = "REACTIVE"
    DISTORTION = "DISTORTION"


class FindingCategory(str, Enum):
    DEAD_CODE = "REACTIVE_DEAD_CODE"
    DUPLICATION = "REACTIVE_DUPLICATION"
    SCHEMA_CONFLICT = "DISTORTION_CONFLICT"
    SEED_DRIFT = "DISTORTION_SEED_DRIFT"
    BROKEN_LINK = "DISTORTION_BROKEN_LINK"
    SECURITY_VIOLATION = "SECURITY_VIOLATION"
    AGENTIC_INJECTION = "AGENTIC_INJECTION"
    SUPPLY_CHAIN_RISK = "SUPPLY_CHAIN_RISK"


class FindingSeverity(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


class EfficiencyClass(str, Enum):
    CLASS_A = "CLASS_A"
    CLASS_B = "CLASS_B"
    CLASS_C = "CLASS_C"
    DISQUALIFIED_SECURITY = "DISQUALIFIED_SECURITY"


class GovernanceStatus(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    DISQUALIFIED_SECURITY = "DISQUALIFIED_SECURITY"
    UNKNOWN = "UNKNOWN"


class ConfidenceTier(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    PROVISIONAL = "PROVISIONAL"


class PruningActionType(str, Enum):
    DELETE_DEAD_SYMBOL = "DELETE_DEAD_SYMBOL"
    DEDUPLICATE_BLOCK = "DEDUPLICATE_BLOCK"
    ARCHIVE_STALE_DOC = "ARCHIVE_STALE_DOC"
    IGNORE_PATH = "IGNORE_PATH"
    RESOLVE_SEED_DRIFT = "RESOLVE_SEED_DRIFT"


class FileAuditFinding(BaseModel):
    file_path: str
    line_start: int = 1
    line_end: int = 1
    category: FindingCategory
    severity: FindingSeverity
    token_cost: int = 0
    description: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "file_path": self.file_path,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "power_type": self.category.value,
            "severity": self.severity.value,
            "token_cost": self.token_cost,
            "description": self.description,
        }


class ConfidenceEnvelope(BaseModel):
    score_name: str = "FPAI-Structural"
    score_value: float = 1.0
    confidence_score: float = 0.95
    confidence_tier: ConfidenceTier = ConfidenceTier.HIGH
    confidence_interval: tuple[float, float] = (0.90, 1.0)
    file_coverage_pct: float = 100.0
    token_coverage_pct: float = 100.0
    language_coverage_pct: float = 100.0
    metrics: dict[str, Any] = Field(default_factory=dict)
    limitations: list[str] = Field(default_factory=list)


class FPAISpectralVector(BaseModel):
    active_tokens_p: int = 0
    reactive_dead_tokens_q: int = 0
    reactive_dup_tokens_q: int = 0
    distortion_tokens_d: int = 0
    apparent_power_spectral: float = 0.0
    apparent_power_linear: float = 0.0
    fpai_structural_score: float = 1.0
    fpai_linear_score: float = 1.0
    efficiency_class: EfficiencyClass = EfficiencyClass.CLASS_A
    governance_score: float = 1.0
    confidence_envelope: ConfidenceEnvelope = Field(default_factory=ConfidenceEnvelope)


class SecurityVulnerabilityReport(BaseModel):
    governance_gate: GovernanceStatus = GovernanceStatus.PASS
    is_deployable: bool = True
    attack_surface_index: float = 100.0
    agentic_injection_risk_count: int = 0
    supply_chain_unpinned_deps: int = 0
    high_entropy_secrets_found: int = 0
    findings: list[FileAuditFinding] = Field(default_factory=list)


class SystemsResilienceReport(BaseModel):
    avg_instability_index: float = 0.0
    cyclic_dependencies_count: int = 0
    spof_modules: list[str] = Field(default_factory=list)
    fault_tolerance_ratio: float = 1.0
    seed_to_code_drift_count: int = 0


class PruningActionItem(BaseModel):
    action_id: str
    action_type: PruningActionType
    target_path: str
    symbol_or_block: str | None = None
    tokens_saved: int = 0
    reversible: bool = True
    rationale: str


class ContextPruningPlan(BaseModel):
    prunable_tokens_total: int = 0
    estimated_context_savings_pct: float = 0.0
    context_budget_violations: list[str] = Field(default_factory=list)
    recommended_agentignore_entries: list[str] = Field(default_factory=list)
    actions: list[PruningActionItem] = Field(default_factory=list)


class EvidencePrimitiveSummary(BaseModel):
    primitive_type: str
    file_count: int = 0
    total_lines: int = 0
    sample_paths: list[str] = Field(default_factory=list)
    verified_valid: bool = True


class AuditCriterion(BaseModel):
    criterion_id: str
    name: str
    fulfilled: bool = False
    evidence_path: str | None = None
    evidence_detail: str = "Pendiente de evaluación"
    remediation_hint: str | None = None


class CanonicalModuleEvaluation(BaseModel):
    module_id: str
    name: str
    weight: float
    stage_group: str = "Core"
    criteria: list[AuditCriterion] = Field(default_factory=list)

    @property
    def criteria_passed(self) -> int:
        return sum(1 for c in self.criteria if c.fulfilled)

    @property
    def criteria_total(self) -> int:
        return len(self.criteria)

    @property
    def phase_completion_pct(self) -> float:
        if not self.criteria:
            return 0.0
        return (self.criteria_passed / self.criteria_total) * 100.0

    @property
    def weighted_contribution_pct(self) -> float:
        return self.weight * self.phase_completion_pct

    @property
    def status(self) -> ModuleStatus:
        if self.phase_completion_pct >= 100.0:
            return ModuleStatus.DONE
        if self.phase_completion_pct > 0.0:
            return ModuleStatus.ACTIVE
        return ModuleStatus.BACKLOG


class RemediationItem(BaseModel):
    priority: str
    module_id: str
    criterion_id: str
    action: str
    impact_score: float
    files_to_touch: list[str] = Field(default_factory=list)


class ProjectAuditReport(BaseModel):
    project_name: str
    project_path: str
    audit_date: str
    auditor: str = "MetricsThinking™ v4.0 Holistic Governance Auditor"
    profile_used: str = "default"
    domain_archetype: DomainArchetype = DomainArchetype.SOFTWARE_ENGINEERING
    inspection_mode: InspectionMode = InspectionMode.SOURCE_CODE
    git_commit: str | None = None
    git_branch: str | None = None
    seed_detected: bool = False
    seed_version: str | None = None
    evidence_primitives: dict[str, EvidencePrimitiveSummary] = Field(default_factory=dict)
    modules: list[CanonicalModuleEvaluation]
    remediation_plan: list[RemediationItem] = Field(default_factory=list)
    stats: dict[str, Any] = Field(default_factory=dict)
    fpai_report: FPAISpectralVector = Field(default_factory=FPAISpectralVector)
    security_report: SecurityVulnerabilityReport = Field(default_factory=SecurityVulnerabilityReport)
    resilience_report: SystemsResilienceReport = Field(default_factory=SystemsResilienceReport)
    pruning_plan: ContextPruningPlan = Field(default_factory=ContextPruningPlan)

    @property
    def consolidated_score(self) -> float:
        return sum(m.weighted_contribution_pct for m in self.modules)

    @property
    def maturity_band(self) -> MaturityBand:
        score = self.consolidated_score
        if score >= 90.0:
            return MaturityBand.OPERATIONAL_EXCELLENCE
        if score >= 75.0:
            return MaturityBand.ADVANCED_MATURITY
        if score >= 50.0:
            return MaturityBand.CONSTRUCTION
        return MaturityBand.INITIAL_RISK

    @property
    def active_bottleneck(self) -> str:
        for m in self.modules:
            if m.phase_completion_pct < 100.0:
                return f"{m.module_id}: {m.name} ({m.phase_completion_pct:.1f}% completado)"
        return "Ninguno. Todos los módulos canónicos se encuentran al 100%."
```

### 5.2 FPIA Core Subpackage Contracts (`./src/metricsthinking/fpai/*`)
- **Producers:** `FPAIEngine`, `ConfidenceCalculator`, `SecurityGatekeeper`, `SeedDriftAuditor`, `CompensationPlanner`, `MedallionPipeline`, `AblationRunner`, `MultiLayerResolver`.
- **Consumers:** `ProjectCollector`, `AuditScorer`, `engine.run_audit`, `mcp_server`.

```python
"""
Frozen Contract 5.2A: ./src/metricsthinking/fpai/spectral_engine.py
Governing Invariants: INV-01, INV-02 | Requirements: R-005
"""
from __future__ import annotations
from typing import Any
from metricsthinking.models import (
    ConfidenceEnvelope,
    EfficiencyClass,
    FileAuditFinding,
    FPAISpectralVector,
    GovernanceStatus,
)


class FPAIEngine:
    METRIC_VERSION: str = "4.0.0"

    def __init__(
        self,
        class_a_threshold: float = 0.85,
        class_b_threshold: float = 0.65,
        spectral_mode: bool = True,
        decoupled_governance: bool = True,
    ) -> None:
        """Initializes bimodal spectral and conservative FPAI evaluation engine."""

    def evaluate(
        self,
        active_tokens: int,
        reactive_dead_tokens: int,
        reactive_dup_tokens: int,
        distortion_tokens: int,
        governance_gate: bool | GovernanceStatus = True,
        findings: list[FileAuditFinding] | None = None,
        confidence_envelope: ConfidenceEnvelope | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> FPAISpectralVector:
        """Computes S_spectral, S_linear, and decoupled G classification."""
```

```python
"""
Frozen Contract 5.2B: ./src/metricsthinking/fpai/confidence.py
Governing Invariants: INV-01 | Requirements: R-005
"""
from __future__ import annotations
from typing import Any
from metricsthinking.models import ConfidenceEnvelope, ConfidenceTier


class ConfidenceCalculator:
    @classmethod
    def calculate_envelope(
        cls,
        score_value: float,
        apparent_tokens: int,
        analyzers_coverage_pct: float,
        language_distribution: dict[str, int],
        file_coverage_pct: float = 100.0,
        score_name: str = "FPAI-Structural",
    ) -> ConfidenceEnvelope:
        """Computes 95% confidence interval and coverage tier for FPAI scores."""


class ComparabilityValidator:
    @classmethod
    def validate_comparability(
        cls,
        meta_a: dict[str, Any],
        meta_b: dict[str, Any],
    ) -> tuple[bool, str, list[str]]:
        """Validates cross-run comparability invariants."""
```

```python
"""
Frozen Contract 5.2C: ./src/metricsthinking/fpai/gatekeeper.py
Governing Invariants: INV-02, INV-08 | Requirements: R-006
"""
from __future__ import annotations
from metricsthinking.models import (
    FileAuditFinding,
    GovernanceStatus,
    SecurityVulnerabilityReport,
)


class SecurityGatekeeper:
    def __init__(
        self,
        entropy_threshold: float = 4.5,
        min_secret_length: int = 20,
    ) -> None:
        """Initializes Zero-Tolerance secret, PII, and agentic surface scanner."""

    @staticmethod
    def calculate_shannon_entropy(data: str) -> float:
        """Computes Shannon entropy H(X) in bits per character."""

    def is_safe_placeholder(self, text: str) -> bool:
        """Returns True if token matches known safe placeholder patterns."""

    def scan_file_content(
        self,
        file_path: str,
        content: str,
    ) -> tuple[bool, list[FileAuditFinding]]:
        """Scans file content for secrets, PII, and high-entropy strings with <REDACTED> masking."""

    def scan_agentic_surface(
        self,
        file_path: str,
        content: str,
    ) -> list[FileAuditFinding]:
        """Scans agentic instructions and code for prompt injection and unsafe execution."""

    def scan_supply_chain(
        self,
        manifests_content: dict[str, str],
    ) -> tuple[int, list[FileAuditFinding]]:
        """Audits dependency manifests for unpinned versions and encoding anomalies."""


class GovernanceEvaluator:
    @staticmethod
    def build_security_report(
        secret_findings: list[FileAuditFinding],
        agentic_findings: list[FileAuditFinding],
        supply_chain_findings: list[FileAuditFinding],
        unpinned_count: int,
        high_entropy_count: int,
        attack_surface_index: float = 100.0,
    ) -> SecurityVulnerabilityReport:
        """Consolidates security findings into SecurityVulnerabilityReport."""
```

```python
"""
Frozen Contract 5.2D: ./src/metricsthinking/fpai/drift_auditor.py & ./src/metricsthinking/fpai/compensation.py
Governing Invariants: INV-01, INV-06, INV-07 | Requirements: R-007
"""
from __future__ import annotations
from pathlib import Path
from typing import Any
from metricsthinking.models import (
    ContextPruningPlan,
    FileAuditFinding,
    FPAISpectralVector,
)


class SeedDriftAuditor:
    @staticmethod
    def verify_seed_contracts(
        seed_path: Path,
        ast_symbols: set[str],
        repo_rel_files: set[str] | None = None,
    ) -> list[FileAuditFinding]:
        """Verifies Section 4 AST symbol declarations in seed-*.md against live repository AST."""


class CompensationPlanner:
    AUTO_PRUNE_START_MARKER: str = "# >>> METRICSTHINKING AUTO-PRUNE >>>"
    AUTO_PRUNE_END_MARKER: str = "# <<< METRICSTHINKING AUTO-PRUNE <<<"

    def generate_plan(
        self,
        fpai_vector: FPAISpectralVector,
        findings: list[FileAuditFinding],
        file_token_map: dict[str, int],
        p0_p1_budget: int = 16000,
        marginal_values: dict[str, float] | None = None,
    ) -> ContextPruningPlan:
        """Generates prioritized, reversible context pruning plan."""

    @classmethod
    def apply_agentignore_pruning(
        cls,
        repo_root: Path,
        plan: ContextPruningPlan,
        dry_run: bool = True,
    ) -> Path:
        """Idempotently updates ./.agentignore between auto-prune markers."""
```

```python
"""
Frozen Contract 5.2E: ./src/metricsthinking/fpai/medallion.py, ablation.py, attribution.py
Governing Invariants: INV-03, INV-07 | Requirements: R-008
"""
from __future__ import annotations
from pathlib import Path
from typing import Any, Callable


class MedallionPipeline:
    def __init__(
        self,
        raw_dir: str | Path = "./data/raw/telemetry",
        processed_dir: str | Path = "./data/processed/telemetry",
    ) -> None:
        """Initializes local Bronze -> Silver -> Gold JSONL telemetry pipeline."""

    def record_bronze_audit_event(
        self,
        repo_id: str,
        commit_sha: str,
        branch: str,
        fpai_spectral: float,
        fpai_linear: float,
        active_tokens: int,
        reactive_tokens: int,
        distortion_tokens: int,
        governance_status: str,
        latency_ms: float,
    ) -> Path:
        """Appends an immutable Bronze telemetry event JSONL line."""

    def run(self) -> dict[str, Any]:
        """Executes Bronze -> Silver deduplication and Silver -> Gold aggregation."""


class AblationRunner:
    def __init__(
        self,
        default_repetitions: int = 3,
        essential_threshold: float = 0.05,
    ) -> None:
        """Initializes causal Leave-One-Out ablation runner."""

    def run_study(
        self,
        task_id: str,
        candidate_chunks: list[dict[str, Any]],
        evaluator_func: Callable[[list[dict[str, Any]], str], dict[str, Any]],
        effective_sampling_rate: float = 0.05,
        run_leave_one_out: bool = True,
    ) -> dict[str, Any]:
        """Executes controlled ablation study under 5% stochastic sampling ceiling."""


class MultiLayerResolver:
    def __init__(
        self,
        weights: dict[str, float] | None = None,
        decision_threshold: float = 0.20,
    ) -> None:
        """Initializes 4-layer attribution resolver (lexical, entity, AST graph, NLI)."""

    def resolve(
        self,
        injected_contexts: list[dict[str, Any]],
        generated_response: str,
        mode: str = "STANDARD",
    ) -> dict[str, Any]:
        """Computes multi-signal attribution report and hallucinated citation count."""
```

### 5.3 Dual-Backend Single-Pass Scanner & Rust FFI Contracts (`./crates/metricsthinking_rs/` & `./src/metricsthinking/backends/`)
- **Producers:** `metricsthinking._core_rs` (Rust `cdylib`) or `metricsthinking.backends.python_fallback`.
- **Consumers:** `ProjectCollector.collect()`.

```rust
// Frozen Contract 5.3A: ./crates/metricsthinking_rs/src/lib.rs
// Governing Invariants: ADR-006, INV-01, INV-08 | Requirements: R-009
use pyo3::prelude::*;

#[pyfunction]
#[pyo3(signature = (root_path, ignore_dirs, cache_path=None))]
pub fn scan_workspace_fast(
    root_path: &str,
    ignore_dirs: Vec<String>,
    cache_path: Option<&str>,
) -> PyResult<String> {
    // Returns deterministic JSON string serialized from WorkspaceScanPayload
    walker::execute_parallel_scan(root_path, &ignore_dirs, cache_path)
        .map_err(|e| pyo3::exceptions::PyRuntimeError::new_err(e))
}

#[pymodule]
fn _core_rs(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(scan_workspace_fast, m)?)?;
    Ok(())
}
```

```python
"""
Frozen Contract 5.3B: ./src/metricsthinking/backends/__init__.py & python_fallback.py
Governing Invariants: ADR-006, INV-07, INV-08 | Requirements: R-010
"""
from __future__ import annotations
from typing import Any


def get_active_backend_name() -> str:
    """Returns 'rust_core_rs' if metricsthinking._core_rs is compiled, else 'python_fallback'."""
    return "python_fallback"


def scan_workspace(
    root_path: str,
    ignore_dirs: list[str],
    cache_path: str | None = None,
    use_cache: bool = True,
) -> dict[str, Any]:
    """
    Executes single-pass repository scan with SHA-256 incremental caching.
    Returns dictionary with keys:
      - 'backend': str ('rust_core_rs' | 'python_fallback')
      - 'cache_hits': int
      - 'cache_misses': int
      - 'elapsed_ms': float
      - 'rel_files': list[str]
      - 'rel_dirs': list[str]
      - 'file_extensions': dict[str, int]
      - 'total_lines': int
      - 'file_tokens': dict[str, int]
      - 'active_tokens_p': int
      - 'reactive_dead_tokens_q': int
      - 'reactive_dup_tokens_q': int
      - 'distortion_tokens_d': int
      - 'ast_symbols': list[str]
      - 'dead_symbols': list[dict[str, Any]]
      - 'duplicate_blocks': list[dict[str, Any]]
      - 'resilience_metrics': dict[str, Any]
      - 'security_findings': list[dict[str, Any]]
      - 'high_entropy_count': int
    """
    return {}
```

### 5.4 Evaluator, Engine, CLI & MCP Contracts (`./src/metricsthinking/evaluator.py`, `engine.py`, `mcp_server.py`)
- **Producers:** `CriteriaEvaluator`, `run_audit`, `mcp_server`.
- **Consumers:** `AuditScorer`, CLI users, MCP JSON-RPC clients.

```python
"""
Frozen Contract 5.4: New deterministic checks in ./src/metricsthinking/evaluator.py
and updated orchestrator in ./src/metricsthinking/engine.py
Governing Invariants: INV-02, INV-04, INV-05 | Requirements: R-011
"""
from __future__ import annotations
from pathlib import Path
from typing import Any
from metricsthinking.collector import ProjectEvidence
from metricsthinking.models import AuditCriterion, ProjectAuditReport


class CriteriaEvaluator:
    def check_security_zero_secrets(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Validates 0 secret/PII findings and governance_gate == PASS."""

    def check_security_agentic_surface(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Validates 0 prompt injection or tool poisoning findings across context files."""

    def check_security_supply_chain(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Validates pinned dependency versions and pure UTF-8 manifests."""

    def check_systems_resilience_coupling(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Validates 0 AST import cycles, controlled instability I, and fault tolerance coverage."""

    def check_context_fpai_efficiency(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Validates fpai_structural_score >= 0.75, waste < 25%, and 0 seed-to-code drift."""


def run_audit(
    target_path: str = ".",
    profile_name: str = "default",
    archetype: str | None = None,
    out_dir: str | None = None,
    prefix: str = "MetricsThinking",
    quiet: bool = False,
    prune: bool = False,
    medallion: bool = False,
    use_cache: bool = True,
) -> tuple[ProjectAuditReport, dict[str, Path]]:
    """Executes unified 4-phase MetricsThinking v4.0 audit with FPIA, Security, Resilience, and Pruning."""
```

### 5.5 Material Data Flow Pipeline & Prompt Caching Alignment
$$\text{Target Repo} \xrightarrow{\text{Single-Pass + SHA-256 Cache}} \text{ProjectEvidence} \xrightarrow{\text{Evaluator + FPAI + Gatekeeper + Drift}} \text{AuditScorer} \xrightarrow{\text{Atomic UTF-8}} \begin{cases} \text{MetricsThinking.md} \\ \text{MetricsThinking.json} \\ \text{INFERRED\_ROADMAP.md} \\ \text{CONTEXT\_PRUNING\_PLAN.json} \end{cases}$$

- **Prompt Caching Alignment:** In `./01_seed/seed-metricsthinking-master.md` and `./artifacts/MetricsThinking.md`, sections `0` through `2` (static identity, metadata, and canonical module schema) form a stable prefix $> 1,024$ tokens, while volatile per-run timestamps and telemetry stats are isolated cleanly so LLM consumers benefit from high prompt cache hit rates.

---

## 6. Failure, Security & Observability Architecture

### 6.1 Failure Matrix & Blast Radius Containment
| Failure Scenario | Detection Mechanism | Blast Radius Containment & Fallback | Recovery Disposition |
| :--- | :--- | :--- | :--- |
| Native Rust binary `_core_rs` not compiled on host | `ImportError` caught in `./src/metricsthinking/backends/__init__.py` | Transparently activates `python_fallback.py` with SHA-256 incremental cache; zero user disruption. | Optional compilation via `maturin develop --release`. |
| Corrupted `./.context/cache/scan_cache.json` | `json.JSONDecodeError` or schema mismatch during cache load | Discards corrupt cache in memory, executes clean cold scan, and atomically overwrites valid cache file. | Automatic self-healing on next scan. |
| Malformed Python syntax in audited target file | `SyntaxError` caught in AST parser | Records `FindingCategory.SCHEMA_CONFLICT` contributing to $D_{\text{struct}}$ tokens; continues scanning remaining files. | Reported in `MetricsThinking.md` forensic breakdown. |
| Git binary absent or non-git directory | `subprocess.CalledProcessError` / `FileNotFoundError` caught in `_collect_git_metadata()` | Assigns `git_commit = "untracked"` and `git_branch = "unknown"`. | Audit completes normally. |

### 6.2 Security Register & Trust Boundaries
- **Zero-Trust Secret Redaction (`INV-08`):** Every regex or Shannon entropy ($H > 4.5$) match in `SecurityGatekeeper` immediately masks the offending token with `<REDACTED>` before instantiating `FileAuditFinding`. Raw secrets never enter `ProjectEvidence`, `MetricsThinking.json`, `MetricsThinking.md`, or stdout.
- **Agentic Surface Hardening (`R-006`):** `SecurityGatekeeper.scan_agentic_surface()` inspects `.mdc`, `SKILL.md`, `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, and `.cursorrules` for indirect prompt injection directives (instruction override patterns, system role hijack, exfiltration attempts), unsafe shell execution (`subprocess` with `shell=True`, `eval(`, `exec(`), and unrestricted MCP wildcard permissions.
- **Read-Only Audit Guarantee:** Standard `metricsthinking audit` never mutates source files in the audited repository; `./.agentignore` is only updated when `--prune` is explicitly passed, and strictly inside `# >>> METRICSTHINKING AUTO-PRUNE >>>` markers.

### 6.3 Observability & Local Medallion Telemetry
- **Bronze Zone (`./data/raw/telemetry/events_bronze.jsonl`):** Append-only JSONL records of every audit execution when `--medallion` is enabled, validated against `./schemas/telemetry_event.v2.json`.
- **Silver Zone (`./data/processed/telemetry/silver_events.jsonl`):** Idempotently deduplicated and normalized records keyed by `(repo_id, task_id, execution_id)`.
- **Gold Zone (`./data/processed/telemetry/gold_efficiency_summary.jsonl`):** Aggregated time-series KPIs (`avg_fpai_spectral`, `avg_fpai_linear`, `avg_latency_ms`, `governance_pass_rate`, `efficiency_class`).

---

## 7. Phased Implementation Work Breakdown (WBS) — Flash Execution Packets (`FEP-###`)

### `FEP-001`: `Repository Hygiene, UTF-8 Requirements, Skeleton Pruning & Version 4.0.0 Sync`
- `fep_id`: `FEP-001`
- `title`: `Sanitize requirements.txt to UTF-8, delete 5 empty skeleton directories, fix engine_readme.md, and sync version 4.0.0`
- `traces_to`: [`R-001`, `R-002`, `R-003`, `INV-06`, `INV-07`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./pyproject.toml`, `./requirements.txt`, `./.context/tree.json`, `./02_foundation/engine/engine_readme.md`, `./src/metricsthinking/__init__.py`, `./src/metricsthinking/mcp_server.py`, `./mcp_metricsthinking.json`]
- `write_targets`: [`./pyproject.toml`, `./requirements.txt`, `./.context/tree.json`, `./02_foundation/engine/engine_readme.md`, `./src/metricsthinking/__init__.py`, `./src/metricsthinking/mcp_server.py`, `./mcp_metricsthinking.json`, `./tests/test_hygiene_v4.py`]
- `negative_constraints`:
  - `DO NOT` include any local absolute editable path (`-e`) or BOM (`\ufeff`) in `./requirements.txt`.
  - `DO NOT` delete `./src/metricsthinking/` or `./scripts/`; delete ONLY the 5 empty skeleton directories (`./src/cloud_jobs/`, `./src/core/`, `./src/dashboards/`, `./src/data_generation/`, `./tools/`).
- `algorithmic_skeleton`:
  ```python
  # 1. Update ./pyproject.toml: version = "4.0.0", add "jsonschema>=4.19.0" to dependencies.
  # 2. Write ./requirements.txt in pure UTF-8 without BOM:
  #    pydantic>=2.0.0
  #    pyyaml>=6.0
  #    rich>=13.0.0
  #    typer>=0.9.0
  #    jsonschema>=4.19.0
  # 3. Remove empty directories: ./src/cloud_jobs, ./src/core, ./src/dashboards, ./src/data_generation, ./tools
  # 4. Remove those 5 keys from ./context/tree.json["nodes"] and add "src/metricsthinking" and "crates/metricsthinking_rs".
  # 5. In ./02_foundation/engine/engine_readme.md line 8, replace "01_seed/seed-idirectory-master.md" with "01_seed/seed-metricsthinking-master.md".
  # 6. Set __version__ = "4.0.0" in ./src/metricsthinking/__init__.py and version "4.0.0" in ./src/metricsthinking/mcp_server.py and ./mcp_metricsthinking.json.
  # 7. Create ./tests/test_hygiene_v4.py with 4 tests verifying UTF-8 requirements, deleted skeleton folders, engine_readme link, and version == "4.0.0".
  ```
- `verification_cmd`: `python -m pytest tests/test_hygiene_v4.py -v`

---

### `FEP-002`: `Unified Pydantic v2 Data Models & v4.0 JSON Schemas`
- `fep_id`: `FEP-002`
- `title`: `Expand models.py with FPIA, Security, Resilience, and Pruning contracts and update JSON Schemas`
- `traces_to`: [`R-004`, `ADR-001`, `ADR-002`, `ADR-007`, `INV-01`, `INV-02`, `INV-04`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./src/metricsthinking/models.py`, `./src/metricsthinking/__init__.py`, `./schemas/project_audit_report.schema.json`]
- `write_targets`: [`./src/metricsthinking/models.py`, `./src/metricsthinking/__init__.py`, `./schemas/project_audit_report.schema.json`, `./schemas/repo_fpai_manifest.v2.json`, `./schemas/telemetry_event.v2.json`, `./tests/test_models_schemas_v4.py`]
- `negative_constraints`:
  - `DO NOT` alter any frozen class name, enum value, or field type specified in Frozen Contract 5.1.
  - `DO NOT` make `fpai_report`, `security_report`, `resilience_report`, or `pruning_plan` required positional arguments without default factories, so all existing v3 tests remain 100% compatible (`C-002`).
- `algorithmic_skeleton`:
  ```python
  # Implement Frozen Contract 5.1 in ./src/metricsthinking/models.py.
  # Export new models in ./src/metricsthinking/__init__.py.
  # Update ./schemas/project_audit_report.schema.json to include "agent-skill" in domain_archetype enum and optional properties:
  #   "fpai_report", "security_report", "resilience_report", "pruning_plan".
  # Write ./schemas/repo_fpai_manifest.v2.json and ./schemas/telemetry_event.v2.json.
  # Create ./tests/test_models_schemas_v4.py with 6 tests validating all new Pydantic models and JSON schema validation.
  ```
- `verification_cmd`: `python -m pytest tests/test_models_schemas_v4.py tests/test_calibration.py -v`

---

### `FEP-003`: `FPIA Spectral Engine & Confidence Envelope Calculator`
- `fep_id`: `FEP-003`
- `title`: `Implement FPAIEngine (bimodal spectral/linear power & decoupled G gate) and ConfidenceCalculator`
- `traces_to`: [`R-005`, `ADR-001`, `ADR-002`, `INV-01`, `INV-02`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./src/metricsthinking/models.py`]
- `write_targets`: [`./src/metricsthinking/fpai/__init__.py`, `./src/metricsthinking/fpai/spectral_engine.py`, `./src/metricsthinking/fpai/confidence.py`, `./tests/fpai/__init__.py`, `./tests/fpai/test_spectral_and_confidence.py`]
- `negative_constraints`:
  - `DO NOT` zero out `active_tokens_p`, `reactive_dead_tokens_q`, `reactive_dup_tokens_q`, `distortion_tokens_d`, `fpai_structural_score`, or `fpai_linear_score` when `governance_gate` is `False` or `GovernanceStatus.FAIL` (`INV-02`).
  - `DO NOT` import from `collector`, `evaluator`, `scorer`, or `engine` inside `fpai/` (Layer 1 boundary).
- `algorithmic_skeleton`:
  ```python
  # In ./src/metricsthinking/fpai/spectral_engine.py:
  # q_total = reactive_dead_tokens + reactive_dup_tokens
  # s_spectral = math.sqrt(active_tokens**2 + q_total**2 + distortion_tokens**2)
  # s_linear = float(active_tokens + q_total + distortion_tokens)
  # score_spectral = active_tokens / s_spectral if s_spectral > 0 else 1.0
  # score_linear = active_tokens / s_linear if s_linear > 0 else 1.0
  # If governance fails (governance_gate is False or FAIL or DISQUALIFIED_SECURITY):
  #   efficiency_class = EfficiencyClass.DISQUALIFIED_SECURITY, governance_score = 0.0
  #   while preserving score_spectral and score_linear (INV-02).
  ```
- `verification_cmd`: `python -m pytest tests/fpai/test_spectral_and_confidence.py -v`

---

### `FEP-004`: `Security Gatekeeper, Agentic Prompt Injection Scanner & Supply Chain Auditor`
- `fep_id`: `FEP-004`
- `title`: `Implement SecurityGatekeeper (Regex, PII, Shannon H>4.5, Agentic Surface, Supply Chain) and fpai_governance.yaml`
- `traces_to`: [`R-006`, `ADR-002`, `INV-02`, `INV-08`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./src/metricsthinking/models.py`, `./src/metricsthinking/fpai/spectral_engine.py`]
- `write_targets`: [`./config/fpai_governance.yaml`, `./src/metricsthinking/fpai/gatekeeper.py`, `./src/metricsthinking/fpai/__init__.py`]
- `negative_constraints`:
  - `DO NOT` include raw matched secret strings in `FileAuditFinding.description`; always replace with `<REDACTED>` (`INV-08`).
  - `DO NOT` flag safe placeholders (`<REDACTED>`, `YOUR_API_KEY`, `EXAMPLE_KEY`, `dummy`, `test_key`, `sk-proj-xxxx`) as security violations.
- `algorithmic_skeleton`:
  ```python
  # Implement Frozen Contract 5.2C in ./src/metricsthinking/fpai/gatekeeper.py:
  # 1. SECRET_PATTERNS: OpenAI (sk-[a-zA-Z0-9]{32,}), AWS (AKIA[0-9A-Z]{16}), GCP (AIza[0-9A-Za-z\-_]{35}),
  #    GitHub (ghp_[0-9a-zA-Z]{36}), Private Key (BEGIN (RSA|EC|OPENSSH|PRIVATE) KEY).
  # 2. PII_PATTERNS: SSN, Credit Card (16 digits), raw corporate email in data payloads.
  # 3. Shannon entropy H(X) = -sum(p_i * log2(p_i)) >= 4.5 on non-URL tokens of len >= 20.
  # 4. scan_agentic_surface(file_path, content): checks agent files (.mdc, SKILL.md, CLAUDE.md, AGENTS.md, .py)
  #    for prompt injection patterns (system-override, jailbreak cues, exfiltration) and unsafe execution.
  # 5. scan_supply_chain(manifests_content): checks pyproject.toml and requirements.txt for unpinned dependencies.
  # 6. Create ./config/fpai_governance.yaml with entropy_threshold: 4.5, token_budgets (p0 to p3), and ci_gates.
  ```
- `verification_cmd`: `python -c "from metricsthinking.fpai.gatekeeper import SecurityGatekeeper, GovernanceEvaluator; gk = SecurityGatekeeper(); ok, f = gk.scan_file_content('a.py', 'key = \"sk-1234567890abcdef1234567890abcdef123456\"'); assert not ok and '<REDACTED>' in f[0].description"`

---

### `FEP-005`: `Seed-to-Code AST Drift Auditor & Reversible Context Pruning Planner`
- `fep_id`: `FEP-005`
- `title`: `Implement SeedDriftAuditor and CompensationPlanner with idempotent .agentignore auto-prune`
- `traces_to`: [`R-007`, `INV-01`, `INV-06`, `INV-07`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./src/metricsthinking/models.py`, `./01_seed/seed-metricsthinking-master.md`, `./.agentignore`]
- `write_targets`: [`./src/metricsthinking/fpai/drift_auditor.py`, `./src/metricsthinking/fpai/compensation.py`, `./src/metricsthinking/fpai/__init__.py`, `./tests/test_security_resilience_pruning.py`]
- `negative_constraints`:
  - `DO NOT` overwrite content outside `# >>> METRICSTHINKING AUTO-PRUNE >>>` and `# <<< METRICSTHINKING AUTO-PRUNE <<<` when updating `./.agentignore`.
  - `DO NOT` mutate `./.agentignore` when `dry_run=True`.
- `algorithmic_skeleton`:
  ```python
  # 1. In ./src/metricsthinking/fpai/drift_auditor.py:
  #    Parse Section 4 of seed-*.md matching pattern r"^([a-zA-Z0-9_./]+\.py)::([a-zA-Z0-9_.]+)"
  #    Verify file existence in repo_rel_files and symbol existence in ast_symbols.
  #    Emit FileAuditFinding(category=FindingCategory.SEED_DRIFT, severity=FindingSeverity.WARNING) for any drift.
  # 2. In ./src/metricsthinking/fpai/compensation.py:
  #    Generate ContextPruningPlan from dead code, duplicate blocks, seed drift, and p0/p1 budget violations.
  #    Implement apply_agentignore_pruning(repo_root, plan, dry_run=True) with idempotent marker replacement.
  # 3. Create ./tests/test_security_resilience_pruning.py with 8 tests covering Gatekeeper, Agentic Surface, Supply Chain, Seed Drift, and .agentignore pruning.
  ```
- `verification_cmd`: `python -m pytest tests/test_security_resilience_pruning.py -v`

---

### `FEP-006`: `Local Medallion Telemetry Pipeline, 5% Causal Ablation, 4-Layer Attribution & HNSW Rebuild`
- `fep_id`: `FEP-006`
- `title`: `Implement medallion.py, ablation.py, attribution.py, and scripts/hnsw_index_rebuild.py`
- `traces_to`: [`R-008`, `ADR-001`, `INV-03`, `INV-07`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./src/metricsthinking/models.py`, `./schemas/telemetry_event.v2.json`]
- `write_targets`: [`./src/metricsthinking/fpai/medallion.py`, `./src/metricsthinking/fpai/ablation.py`, `./src/metricsthinking/fpai/attribution.py`, `./src/metricsthinking/fpai/__init__.py`, `./scripts/hnsw_index_rebuild.py`, `./tests/fpai/test_medallion_ablation_attribution.py`]
- `negative_constraints`:
  - `DO NOT` introduce any cloud SDK (`boto3`, `google-cloud`, `pyspark`, `azure`) in `medallion.py` (`INV-03`).
  - `DO NOT` allow `AblationRunner` default sampling rate to exceed `0.05` (`INV-03`).
- `algorithmic_skeleton`:
  ```python
  # 1. Implement MedallionPipeline in ./src/metricsthinking/fpai/medallion.py:
  #    record_bronze_audit_event() writes to ./data/raw/telemetry/events_bronze.jsonl.
  #    run() deduplicates Bronze -> ./data/processed/telemetry/silver_events.jsonl
  #    and aggregates Silver -> ./data/processed/telemetry/gold_efficiency_summary.jsonl.
  # 2. Implement AblationRunner in ./src/metricsthinking/fpai/ablation.py (Leave-One-Out V_marginal, CI95%, 5% sampling).
  # 3. Implement MultiLayerResolver in ./src/metricsthinking/fpai/attribution.py (lexical, entity, dependency_graph, nli_semantic).
  # 4. Implement ./scripts/hnsw_index_rebuild.py for physical HNSW tombstone purging.
  # 5. Create ./tests/fpai/test_medallion_ablation_attribution.py with 6 tests covering Medallion idempotency, Ablation, Attribution, and HNSW rebuild.
  ```
- `verification_cmd`: `python -m pytest tests/fpai/test_medallion_ablation_attribution.py -v`

---

### `FEP-007`: `Native Rust Accelerator Crate (crates/metricsthinking_rs)`
- `fep_id`: `FEP-007`
- `title`: `Create PyO3 Rust native crate (Cargo.toml, lib.rs, walker.rs, entropy_sec.rs, ast_graph.rs, ballast_tokens.rs)`
- `traces_to`: [`R-009`, `ADR-006`, `INV-01`, `INV-08`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./src/metricsthinking/models.py`]
- `write_targets`: [`./crates/metricsthinking_rs/Cargo.toml`, `./crates/metricsthinking_rs/src/lib.rs`, `./crates/metricsthinking_rs/src/walker.rs`, `./crates/metricsthinking_rs/src/entropy_sec.rs`, `./crates/metricsthinking_rs/src/ast_graph.rs`, `./crates/metricsthinking_rs/src/ballast_tokens.rs`]
- `negative_constraints`:
  - `DO NOT` fail the Python runtime if `cargo` is not installed on the host machine; this crate is compiled optionally via `maturin` while `python_fallback.py` provides the guaranteed runtime baseline.
  - `DO NOT` emit unredacted secrets from `entropy_sec.rs` (`INV-08`).
- `algorithmic_skeleton`:
  ```rust
  // ./crates/metricsthinking_rs/Cargo.toml:
  // [package] name = "metricsthinking_rs", version = "4.0.0", edition = "2021"
  // [lib] name = "_core_rs", crate-type = ["cdylib"]
  // Dependencies: pyo3 (0.21, extension-module), ignore (0.4), rayon (1.10), regex (1.10),
  //               aho-corasick (1.1), sha2 (0.10), fxhash (0.2), serde (1.0), serde_json (1.0)
  // Implement walker.rs (parallel walk + SHA-256 + chars/3.8 tokens),
  // entropy_sec.rs (Shannon entropy + regex secret/PII scan with <REDACTED>),
  // ast_graph.rs (symbol defs/calls Q_dead, Ca/Ce instability, cycles, SPOFs),
  // ballast_tokens.rs (5-gram fxhash shingling Q_dup), and lib.rs (scan_workspace_fast).
  ```
- `verification_cmd`: `python -c "from pathlib import Path; assert all((Path('crates/metricsthinking_rs') / p).exists() for p in ['Cargo.toml', 'src/lib.rs', 'src/walker.rs', 'src/entropy_sec.rs', 'src/ast_graph.rs', 'src/ballast_tokens.rs'])"`

---

### `FEP-008`: `Single-Pass Collector, Dual-Backend Selector & Incremental SHA-256 Cache`
- `fep_id`: `FEP-008`
- `title`: `Implement backends/python_fallback.py, backends/__init__.py, and refactor collector.py for Single-Pass scanning`
- `traces_to`: [`R-010`, `ADR-006`, `INV-01`, `INV-07`, `INV-08`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./src/metricsthinking/collector.py`, `./src/metricsthinking/models.py`, `./src/metricsthinking/fpai/gatekeeper.py`, `./src/metricsthinking/fpai/drift_auditor.py`]
- `write_targets`: [`./src/metricsthinking/backends/__init__.py`, `./src/metricsthinking/backends/python_fallback.py`, `./src/metricsthinking/collector.py`, `./tests/test_backends_collector.py`]
- `negative_constraints`:
  - `DO NOT` break any existing attribute on `ProjectEvidence` (`files`, `rel_files`, `dirs`, `rel_dirs`, `seeds`, `manifests`, `context_files`, `schemas`, `tests`, `ci_workflows`, `docs`, `source_files`, `adrs`, `dashboards`, `tools_and_scripts`, `skills`, `agent_instructions`, `master_templates`, `skill_installers`, `coverage_benchmarks`, `evidence_primitives`, `file_cache`).
  - `DO NOT` spawn unguarded `ProcessPoolExecutor` workers on Windows for tiny file counts (`< 64` files) where process spawn overhead exceeds scan time; use in-process single-pass execution for `< 64` uncached files and `ProcessPoolExecutor` for `>= 64` uncached files, with SHA-256 cache hits bypassing file re-analysis completely (`< 50 ms`).
- `algorithmic_skeleton`:
  ```python
  # 1. In ./src/metricsthinking/backends/python_fallback.py:
  #    Load ./.context/cache/scan_cache.json (keyed by rel_path -> {sha256, mtime_ns, size, lines, tokens,
  #    ast_defs, ast_refs, imports, has_fault_tolerance, io_calls, shingles, sec_findings}).
  #    In a single pass over non-excluded files:
  #      - If (mtime_ns, size) or sha256 matches cache entry, reuse cached per-file telemetry!
  #      - Otherwise read bytes once, compute sha256, lines, tokens (int(len(text) / 3.8)),
  #        AST defs/refs/imports/try-except/timeout (for .py), 5-gram shingles, and SecurityGatekeeper findings.
  #    Compute repo-wide AST reachability (Q_dead), 5-gram Jaccard duplication (Q_dup),
  #    Instability I = Ce / (Ca + Ce), Tarjan/DFS cycle count, SPOF modules (>40% dependents), and fault_tolerance_ratio.
  #    Atomically save updated scan_cache.json in UTF-8.
  # 2. In ./src/metricsthinking/collector.py:
  #    Invoke scan_workspace() in ProjectCollector.collect(use_cache=self.use_cache), populate all legacy
  #    ProjectEvidence buckets AND new v4.0 evidence fields (fpai_vector, security_report, resilience_report, pruning_plan).
  # 3. Create ./tests/test_backends_collector.py with 6 tests verifying Single-Pass collection, SHA-256 cache hit speedup (< 300ms), AST cycles/SPOF, and dead/dup token accounting.
  ```
- `verification_cmd`: `python -m pytest tests/test_backends_collector.py tests/test_collector.py -v`

---

### `FEP-009`: `Evaluator v4.0 Rules, Scorer Integration & 14 Canonical YAML Profiles`
- `fep_id`: `FEP-009`
- `title`: `Add 5 deterministic v4.0 checks to evaluator.py, upgrade scorer.py, and update 14 YAML profiles`
- `traces_to`: [`R-011`, `ADR-007`, `INV-02`, `INV-04`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./src/metricsthinking/evaluator.py`, `./src/metricsthinking/scorer.py`, `./config/profiles/default.yaml`, `./config/profiles/agent-skill.yaml`]
- `write_targets`: [`./src/metricsthinking/evaluator.py`, `./src/metricsthinking/scorer.py`, `./config/profiles/default.yaml`, `./config/profiles/agent-skill.yaml`, `./config/profiles/data-platform.yaml`, `./config/profiles/dataops.yaml`, `./config/profiles/web-app.yaml`, `./config/profiles/mlops.yaml`, `./config/profiles/llmops.yaml`, `./config/profiles/gitops.yaml`, `./config/profiles/platform-eng.yaml`, `./config/profiles/devsecops.yaml`, `./config/profiles/dual-track.yaml`, `./config/profiles/team-topologies.yaml`, `./config/profiles/chaos-eng.yaml`, `./config/profiles/sdd.yaml`]
- `negative_constraints`:
  - `DO NOT` change the module weights (`M01`–`M10`) in any of the 14 YAML profiles; every profile's 10 modules MUST continue to sum to `1.0` (`INV-04`).
  - `DO NOT` cause any existing test in `./tests/test_evaluator.py`, `./tests/test_scorer.py`, or `./tests/test_v3_archetypes.py` to fail.
- `algorithmic_skeleton`:
  ```python
  # 1. In ./src/metricsthinking/evaluator.py, add the 5 methods from Frozen Contract 5.4:
  #    - check_security_zero_secrets
  #    - check_security_agentic_surface
  #    - check_security_supply_chain
  #    - check_systems_resilience_coupling
  #    - check_context_fpai_efficiency
  # 2. Update version to "4.0.0" in all 14 ./config/profiles/*.yaml files while preserving exact M01-M10 weights and existing criteria IDs.
  # 3. In ./src/metricsthinking/scorer.py:
  #    Populate report.fpai_report, report.security_report, report.resilience_report, and report.pruning_plan from evidence.
  #    In _build_remediation_plan(), append P1 security findings, P2 resilience/drift findings, and P2/P3 high-ROI pruning actions when present.
  ```
- `verification_cmd`: `python -m pytest tests/test_evaluator.py tests/test_scorer.py tests/test_v3_archetypes.py -v`

---

### `FEP-010`: `Renderer v4.0 Trimodal + Pruning Output, Engine, CLI & 6-Tool MCP Server`
- `fep_id`: `FEP-010`
- `title`: `Upgrade renderer.py (3 new Markdown sections + CONTEXT_PRUNING_PLAN.json), engine.py, cli.py, mcp_server.py, and SKILL.md`
- `traces_to`: [`R-011`, `C-001`, `C-004`, `INV-05`, `INV-06`, `INV-07`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./src/metricsthinking/renderer.py`, `./src/metricsthinking/engine.py`, `./src/metricsthinking/cli.py`, `./src/metricsthinking/mcp_server.py`, `./.agents/skills/metrics/SKILL.md`]
- `write_targets`: [`./src/metricsthinking/renderer.py`, `./src/metricsthinking/engine.py`, `./src/metricsthinking/cli.py`, `./src/metricsthinking/mcp_server.py`, `./.agents/skills/metrics/SKILL.md`, `./tests/test_mcp_v4.py`]
- `negative_constraints`:
  - `DO NOT` emit absolute local paths in `MetricsThinking.md`, `MetricsThinking.json`, `INFERRED_ROADMAP.md`, or `CONTEXT_PRUNING_PLAN.json`; normalize `report.project_path` to `"./"` in rendered artifacts (`INV-06`).
  - `DO NOT` use nested subgraphs in Mermaid roadmaps; strictly preserve `flowchart LR` (`INV-06`).
- `algorithmic_skeleton`:
  ```python
  # 1. In ./src/metricsthinking/renderer.py:
  #    Add _render_fpai_spectral_section(), _render_security_resilience_section(), and _render_pruning_plan_section()
  #    emitting the exact headers:
  #      "### ⚡ Context Engineering & Spectral Power (FPIA)"
  #      "### 🛡️ Security, Vulnerability & Systems Resilience"
  #      "### ✂️ Context Pruning Plan (Poda Determinista)"
  #    In write_artifacts(), also write ./artifacts/plans/active/CONTEXT_PRUNING_PLAN.json in UTF-8.
  # 2. In ./src/metricsthinking/engine.py:
  #    Support prune: bool = False, medallion: bool = False, use_cache: bool = True.
  #    When prune=True, call CompensationPlanner.apply_agentignore_pruning(target, report.pruning_plan, dry_run=False).
  #    When medallion=True, record Bronze event and run MedallionPipeline().run().
  # 3. In ./src/metricsthinking/cli.py:
  #    Add flags --prune, --medallion, --no-cache to audit and root parser, plus subcommands 'prune' and 'medallion'.
  # 4. In ./src/metricsthinking/mcp_server.py:
  #    Expose 6 tools: audit_repository, list_profiles, get_audit_report, scan_fpai_context, generate_pruning_plan, run_medallion_telemetry.
  # 5. Create ./tests/test_mcp_v4.py with 5 tests verifying all 6 MCP tools and JSON-RPC initialize version "4.0.0".
  ```
- `verification_cmd`: `python -m pytest tests/test_renderer.py tests/test_cli.py tests/test_mcp_v4.py -v`

---

### `FEP-011`: `Massive Stress Benchmark Suite (Closing M07 to 100.0%)`
- `fep_id`: `FEP-011`
- `title`: `Implement tests/test_benchmarks_stress.py (1,000-file synthetic stress benchmark) and emit artifacts/benchmark_coverage_report.json`
- `traces_to`: [`R-012`, `INV-01`, `INV-07`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./src/metricsthinking/engine.py`, `./src/metricsthinking/evaluator.py`, `./src/metricsthinking/collector.py`]
- `write_targets`: [`./tests/test_benchmarks_stress.py`, `./artifacts/benchmark_coverage_report.json`]
- `negative_constraints`:
  - `DO NOT` create permanent 1,000 synthetic files inside the main repository tree; generate the 1,000-file synthetic polyglot workspace inside `tmp_path` during the test and write only the summarized telemetry report to `./artifacts/benchmark_coverage_report.json`.
  - `DO NOT` use flaky wall-clock assertions that fail under normal CI load; assert cold run `< 2.5s`, warm SHA-256 cached run `< 0.30s` (`< 300ms`), and cache speedup `>= 75%`.
- `algorithmic_skeleton`:
  ```python
  # In ./tests/test_benchmarks_stress.py:
  # 1. test_synthetic_1000_files_stress_and_cache_speedup(tmp_path):
  #    Generate 1,000 files across Python, Markdown, YAML, JSON, and SQL in tmp_path.
  #    Run cold scan via ProjectCollector(str(tmp_path), use_cache=True).collect() -> measure cold_ms.
  #    Run warm scan via ProjectCollector(str(tmp_path), use_cache=True).collect() -> measure warm_ms.
  #    Assert warm_ms < 300.0 and warm_ms < cold_ms * 0.25.
  #    Write deterministic ./artifacts/benchmark_coverage_report.json with p50/p95 latencies, cache hit rate (100%), and 1,000 files verified.
  # 2. test_m07_criteria_fulfilled_on_self_audit():
  #    Verify both M07-C02 and M07-C03 evaluate to True on the repository root.
  ```
- `verification_cmd`: `python -m pytest tests/test_benchmarks_stress.py -v`

---

### `FEP-012`: `ThinkingSeed Master v4.0 Synchronization, CI Workflow & Holistic 100% Self-Audit Gate`
- `fep_id`: `FEP-012`
- `title`: `Update 01_seed/seed-metricsthinking-master.md to v4.0 (0 AST drift), update .github/workflows/ci.yml, and execute full self-audit`
- `traces_to`: [`R-012`, `INV-02`, `INV-04`, `INV-05`, `INV-06`, `INV-07`]
- `worker_profile`: `gemini-3.8-flash-high`
- `read_context`: [`./01_seed/seed-metricsthinking-master.md`, `./.github/workflows/ci.yml`, `./src/metricsthinking/models.py`, `./src/metricsthinking/collector.py`, `./src/metricsthinking/evaluator.py`, `./src/metricsthinking/scorer.py`, `./src/metricsthinking/renderer.py`, `./src/metricsthinking/engine.py`, `./src/metricsthinking/cli.py`, `./src/metricsthinking/mcp_server.py`, `./src/metricsthinking/fpai/drift_auditor.py`]
- `write_targets`: [`./01_seed/seed-metricsthinking-master.md`, `./.github/workflows/ci.yml`, `./artifacts/MetricsThinking.md`, `./artifacts/MetricsThinking.json`, `./artifacts/plans/active/INFERRED_ROADMAP.md`, `./artifacts/plans/active/CONTEXT_PRUNING_PLAN.json`]
- `negative_constraints`:
  - `DO NOT` embed multi-line implementation source code blocks inside `./01_seed/seed-metricsthinking-master.md` (`contains_source_code="false"`, `INV-02` of ThinkingSeed).
  - `DO NOT` leave any AST signature in Section 4 of `./01_seed/seed-metricsthinking-master.md` that does not exist in `./src/` or `./scripts/` (`seed_to_code_drift_count` MUST equal `0`).
- `algorithmic_skeleton`:
  ```python
  # 1. Update ./01_seed/seed-metricsthinking-master.md to v4.0 documenting all 1-line AST signatures across:
  #    models.py, collector.py, evaluator.py, scorer.py, renderer.py, engine.py, cli.py, mcp_server.py,
  #    backends/__init__.py, backends/python_fallback.py, fpai/*, and scripts/*.py.
  # 2. Update ./.github/workflows/ci.yml to run ruff, mypy, pytest, and:
  #    python -m metricsthinking.cli audit --target . --profile default --prune --medallion
  # 3. Execute holistic self-audit and verify consolidated_score == 100.0 and seed_to_code_drift_count == 0.
  ```
- `verification_cmd`: `python -m metricsthinking.cli audit --target . --profile default --prune --medallion && python -m pytest -v --tb=short`

---

## 8. Verification Architecture & Quantitative Test Ledger

### 8.1 Quantitative Test Matrix
| Phase / FEP-ID | Test File Path | Test Type | Enumerated Test Cases | Count | Cumulative Count | `verification_cmd` Oracle |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| `Baseline` | `./tests/test_*.py` (8 existing files) | Unit & Integration `[OBSERVED]` | `test_calibration.py` (4), `test_cli.py` (2), `test_collector.py` (3), `test_evaluator.py` (2), `test_installer.py` (7), `test_renderer.py` (3), `test_scorer.py` (1), `test_v3_archetypes.py` (32) | 54 | 54 | `python -m pytest -q` |
| `FEP-001` | `./tests/test_hygiene_v4.py` | Hygiene & Invariant | `test_requirements_utf8_and_clean`, `test_no_empty_skeleton_dirs`, `test_engine_readme_seed_reference`, `test_version_4_0_0_synchronized` | 4 | 58 | `python -m pytest tests/test_hygiene_v4.py -v` |
| `FEP-002` | `./tests/test_models_schemas_v4.py` | Contract & Schema | `test_fpai_spectral_vector_model`, `test_security_vulnerability_report_model`, `test_systems_resilience_report_model`, `test_context_pruning_plan_model`, `test_project_audit_report_v4_schema_validation`, `test_fpai_and_telemetry_v2_schemas_valid` | 6 | 64 | `python -m pytest tests/test_models_schemas_v4.py -v` |
| `FEP-003` | `./tests/fpai/test_spectral_and_confidence.py` | Mathematical Unit | `test_bimodal_spectral_and_linear_calculation`, `test_zero_tokens_edge_case`, `test_decoupled_governance_preserves_pqd_scores`, `test_efficiency_class_thresholds`, `test_confidence_envelope_ci95_tiers`, `test_comparability_validator_rules` | 6 | 70 | `python -m pytest tests/fpai/test_spectral_and_confidence.py -v` |
| `FEP-004` & `FEP-005` | `./tests/test_security_resilience_pruning.py` | Security, Drift & Pruning | `test_shannon_entropy_and_secret_redaction`, `test_safe_placeholders_ignored`, `test_agentic_surface_prompt_injection_detection`, `test_supply_chain_unpinned_detection`, `test_seed_drift_auditor_detects_missing_ast_symbol`, `test_seed_drift_auditor_zero_drift_on_valid_seed`, `test_compensation_planner_generates_actions`, `test_agentignore_idempotent_marker_pruning` | 8 | 78 | `python -m pytest tests/test_security_resilience_pruning.py -v` |
| `FEP-006` | `./tests/fpai/test_medallion_ablation_attribution.py` | Medallion, Ablation & Attribution | `test_medallion_bronze_to_silver_deduplication`, `test_medallion_silver_to_gold_aggregation`, `test_ablation_runner_5pct_sampling_and_loo`, `test_multilayer_attribution_active_vs_reactive`, `test_multilayer_attribution_empty_context`, `test_hnsw_index_rebuild_purges_tombstones` | 6 | 84 | `python -m pytest tests/fpai/test_medallion_ablation_attribution.py -v` |
| `FEP-007` & `FEP-008` | `./tests/test_backends_collector.py` | Collector, Cache & Backends | `test_rust_crate_manifest_and_sources`, `test_backend_selector_and_fallback`, `test_single_pass_sha256_cache_hit_and_invalidation`, `test_ast_dead_code_and_coupling_metrics`, `test_shingling_duplicate_tokens_detection`, `test_collector_populates_v4_evidence_reports` | 6 | 90 | `python -m pytest tests/test_backends_collector.py -v` |
| `FEP-010` | `./tests/test_mcp_v4.py` | MCP JSON-RPC Protocol | `test_mcp_initialize_version_4_0_0`, `test_mcp_list_6_tools`, `test_mcp_scan_fpai_context_tool`, `test_mcp_generate_pruning_plan_tool`, `test_mcp_run_medallion_telemetry_tool` | 5 | 95 | `python -m pytest tests/test_mcp_v4.py -v` |
| `FEP-011` | `./tests/test_benchmarks_stress.py` | Stress & Performance Benchmark | `test_synthetic_1000_files_stress_and_cache_speedup`, `test_m07_criteria_fulfilled_on_self_audit`, `test_self_audit_reaches_100_percent_maturity` | 3 | 98 | `python -m pytest tests/test_benchmarks_stress.py -v` |

- **Deterministic Non-Flakiness Guarantee:** All tests operate on local deterministic fixtures or `pytest` `tmp_path` directories with `0` network calls, `0` external LLM API calls, and fixed pseudo-random seeds (`random.Random(42)`).

---

## 9. Compatibility, Migration & Rollback

### 9.1 Legacy Symbol & Schema Migration Bridge
- All v3.0 imports (`from metricsthinking import ProjectCollector, CriteriaEvaluator, AuditScorer, ReportRenderer, run_audit`) and all v3.0 `ProjectAuditReport` attributes remain 100% backward-compatible (`C-001`, `C-002`).
- `./schemas/project_audit_report.schema.json` adds optional properties (`fpai_report`, `security_report`, `resilience_report`, `pruning_plan`) without invalidating v3.0 golden test fixtures (`./tests/fixtures/sample_golden_audit.json`).

### 9.2 Rollback Triggers & Automated Reversion Procedures
- **Trigger 1 (Auto-Prune Reversion):** Removing the block between `# >>> METRICSTHINKING AUTO-PRUNE >>>` and `# <<< METRICSTHINKING AUTO-PRUNE <<<` in `./.agentignore` restores the exact pre-pruning state in $< 1\text{ s}$.
- **Trigger 2 (Cache Invalidation):** Passing `--no-cache` to `metricsthinking audit` or deleting `./.context/cache/scan_cache.json` forces a clean cold scan.
- **Trigger 3 (Full Git Rollback):** If any acceptance gate (`CA-01` to `CA-07`) fails, `git checkout -- .` restores commit `1ce94d4` cleanly.

---

## 10. Scope Boundaries & Risk Register

### 10.1 Explicit Out of Scope Ledger
1. **External Cloud Telemetry Sinks:** No AWS S3, GCP BigQuery, Azure Fabric, or Spark clusters are provisioned; Medallion telemetry operates strictly on local JSONL streams (`INV-03`).
2. **Unsupervised Destructive Code Deletion:** The pruning engine never deletes `.py` or `.md` source files automatically; it generates `./artifacts/plans/active/CONTEXT_PRUNING_PLAN.json` and updates `./.agentignore` within safe markers.
3. **Live LLM Token Consumption in Static Audits:** Static audits execute with `0` API calls (`INV-03`).

### 10.2 Risk Matrix
| Risk Description | Severity | Automated Mitigation | Residual Risk |
| :--- | :---: | :--- | :---: |
| Host environment lacks Rust compiler (`cargo`/`maturin`) (`EV-08`). | `HIGH` | `./src/metricsthinking/backends/__init__.py` catches `ImportError` on `_core_rs` and routes transparently to `python_fallback.py` with SHA-256 caching. | `LOW` |
| Windows `ProcessPoolExecutor` spawn overhead slows down scans on small repos. | `MEDIUM` | `python_fallback.py` uses an adaptive file-count threshold (`>= 64` uncached files for multiprocessing, in-process single-pass below `64` files) plus SHA-256 incremental cache (`< 50ms` warm run). | `LOW` |
| False-positive secret detection on documentation badges, URLs, or hex hashes. | `MEDIUM` | `SecurityGatekeeper` filters URLs, Markdown image badges, 32/64-char hex commit hashes, and `SAFE_PLACEHOLDERS` before Shannon entropy evaluation. | `LOW` |
| Seed-to-Code drift triggered after adding new v4.0 classes and functions. | `MEDIUM` | `FEP-012` synchronizes Section 4 of `./01_seed/seed-metricsthinking-master.md` and asserts `seed_to_code_drift_count == 0`. | `LOW` |

---

## 11. Static Plan Lint (`tools/lint_plan.py`)
This plan has been mechanically audited against all 16 rules of `UltraPlanLinter` (`v3.0.0`):
- **`RULE-01` (Orphan Requirements):** `0` orphan requirements (`R-001` to `R-012` fully mapped to `FEP-001`–`FEP-012` and pytest targets).
- **`RULE-02` (Orphan Components):** `0` orphan `[NEW]` components (every `[NEW]` node in Section 4 declares `(R-###, INV-###)`).
- **`RULE-07` (Evidence Provenance Tags):** Epistemological tags (`[OBSERVED]`, `[REQUIRED]`, `[DERIVED]`, `[OBSERVED_IN_SEED]`) verified across all sections.
- **`RULE-08` (Anti-Placeholder Guardrail):** `0` banned placeholders (`0` occurrences of unresolved markers or vague phrases).
- **`RULE-12` & `RULE-14` (Mode A & 14 Mandatory Sections):** `Mode A (Live Environment)` and all 14 mandatory sections present.
- **`RULE-15` & `RULE-16` (FEP Schema Completeness & Wildcard-Free Targets):** All 12 `FEP-###` blocks (`FEP-001` to `FEP-012`) declare valid `worker_profile: gemini-3.8-flash-high`, closed `read_context`, wildcard-free `write_targets`, `negative_constraints`, `algorithmic_skeleton`, and `verification_cmd`.

---

## 12. Adversarial Architecture Review

| Finding ID | Severity | Evidence | Defect | Consequence | Required Revision | Status |
| :--- | :---: | :--- | :--- | :--- | :--- | :---: |
| `AR-001` | `BLOCKER` | `EV-08` (`pytest` not on raw PATH in Windows shell) | `HANDOFF-AMBIGUITY`: If `FEP-###` `verification_cmd` uses bare `pytest`, `gemini-3.8-flash-high` will fail with `CommandNotFoundException` on Windows. | False packet failure during tactical execution. | Standardized every `verification_cmd` across `FEP-001` to `FEP-012` to use `python -m pytest` and `python -m metricsthinking.cli`. | `RESOLVED` |
| `AR-002` | `MAJOR` | `./src/metricsthinking/evaluator.py` line 409 (`check_strict_validation`) & line 2155 (`check_tools_integration`) | Deleting `./src/cloud_jobs/`, `./src/core/`, `./src/dashboards/`, `./src/data_generation/`, and `./tools/` (`R-002`) removes 5 `.context.yaml` files and `./tools/`. | Could drop `.context.yaml` count below 3 or break `check_tools_integration`. | Verified 8 `.context.yaml`/`tree.json` files remain (`>= 3`) and `./scripts/` satisfies `check_tools_integration`. | `RESOLVED` |
| `AR-003` | `MAJOR` | `./tests/test_calibration.py` & `./schemas/project_audit_report.schema.json` | Adding required fields to `ProjectAuditReport` or changing `M01`–`M10` weights would break existing v3 golden regression tests (`C-002`, `C-003`). | Regression failure in `test_calibration.py` and `test_v3_archetypes.py`. | Used `Field(default_factory=<Model>)` on all 4 new `ProjectAuditReport` sub-reports and preserved exact `M01`–`M10` weights (`INV-04`). | `RESOLVED` |
| `AR-004` | `MAJOR` | `EV-08` (`cargo` not installed on host machine) | If `ProjectCollector` requires `metricsthinking._core_rs` unconditionally, `run_audit()` will crash when Rust toolchain is absent. | Complete failure of CLI and MCP server on Python-only hosts. | Designed `metricsthinking/backends/__init__.py` to catch `ImportError` and fall back to `python_fallback.py` with identical JSON schema and SHA-256 cache (`ADR-006`). | `RESOLVED` |
| `AR-005` | `MINOR` | `./src/metricsthinking/renderer.py` line 159 (`self.report.project_path`) | `ProjectCollector` resolves `self.root_path = Path(target_path).resolve()`, which previously wrote an absolute Windows path into `MetricsThinking.md` and `MetricsThinking.json`. | Violates `INV-06` (Zero Local Absolute Paths in artifacts). | Updated `FEP-010` so `ReportRenderer` and `AuditScorer` serialize `project_path` as portable relative `"./"`. | `RESOLVED` |

---

## 13. Immediate Executable Slice

### Goal of Immediate Slice 1
Execute packet `FEP-001` to eliminate technical debt vectors `T-01`, `T-02`, `T-03`, and `T-04` by normalizing `./requirements.txt` to pure UTF-8 without BOM, removing the 5 empty legacy skeleton directories, updating `./.context/tree.json` and `./02_foundation/engine/engine_readme.md`, synchronizing version `"4.0.0"`, and certifying via `./tests/test_hygiene_v4.py`.

### Exact Artifacts to Touch (`write_targets`)
- `./pyproject.toml`
- `./requirements.txt`
- `./.context/tree.json`
- `./02_foundation/engine/engine_readme.md`
- `./src/metricsthinking/__init__.py`
- `./src/metricsthinking/mcp_server.py`
- `./mcp_metricsthinking.json`
- `./tests/test_hygiene_v4.py`

### Exact Verification Command (`verification_cmd`)
```bash
python -m pytest tests/test_hygiene_v4.py -v
```

### Binary Acceptance Criteria for Slice 1
- `exit code 0` from `python -m pytest tests/test_hygiene_v4.py -v`.
- `./requirements.txt` starts with UTF-8 ASCII bytes (no `0xFF 0xFE` or `0xEF 0xBB 0xBF` BOM) and contains zero local paths.
- `./src/cloud_jobs`, `./src/core`, `./src/dashboards`, `./src/data_generation`, and `./tools` no longer exist on disk or in `./.context/tree.json`.

---

## 14. Architectural Depth Score & Finalization Gate

### Evaluation Dimensions Vector ($\vec{S} \in [0, 10]^{12}$)
| Dimension | Score | Proof Citation in Specification |
| :--- | :---: | :--- |
| $s_1$: Evidence Grounding & Epistemic Honesty | `9.5` | Section 0 & Section 1: Live `Mode A` forensics (`EV-01` to `EV-08`), real `pytest` counts (`54`), real UTF-16LE and version drift observations. |
| $s_2$: Requirement Traceability | `9.5` | Section 2: `R-001` to `R-012` 9-column ledger with $\mathcal{I}_{\text{orphan\_req}} = 0$. |
| $s_3$: Component Resolution & Topology | `9.5` | Section 4: Complete target tree with `[NEW]`, `[MODIFY]`, `[PRESERVE]`, `[DELETE]` tags, $\mathcal{I}_{\text{orphan\_comp}} = 0$, and strict 6-layer import acyclicity. |
| $s_4$: Contract & Data Interface Resolution | `9.5` | Section 5: Literal Python & Rust frozen signatures (`REG-FROZEN-SIGNATURES`) across Contracts 5.1–5.4 with producer-consumer topology and 1,024-token cache prefix alignment. |
| $s_5$: Dependency, Invariants & Causality | `9.5` | Section 3: `ADR-001`, `ADR-002`, `ADR-006`, `ADR-007` and `INV-01` through `INV-08` with automated test gates. |
| $s_6$: Failure & Recovery Architecture | `9.0` | Section 6.1: Fallback from `_core_rs` to `python_fallback.py`, corrupt cache self-healing, AST syntax error isolation, and Git fallback. |
| $s_7$: Security & Trust Boundaries | `9.5` | Section 6.2: Zero-tolerance `<REDACTED>` masking (`INV-08`), Shannon entropy $H > 4.5$, agentic prompt injection scanner, and read-only default audit. |
| $s_8$: Observability & Telemetry | `9.0` | Section 6.3: Local client-side Medallion (`Bronze -> Silver -> Gold` JSONL) and SHA-256 cache telemetry (`cache_hits`, `elapsed_ms`). |
| $s_9$: Verification & Quantitative Test Ledger | `9.5` | Section 8: Enumerated test ledger scaling from `54` baseline tests to `98` total tests across all new v4.0 modules and stress benchmarks. |
| $s_{10}$: Compatibility, Migration & Rollback | `9.0` | Section 1.2 & Section 9: Backward-compatible defaults (`C-001` to `C-004`), marker-bounded `.agentignore` rollback, and schema evolution. |
| $s_{11}$: Scope Boundaries & Risk Matrix | `9.0` | Section 10: Explicit Out-of-Scope ledger and 4-row automated risk mitigation matrix. |
| $s_{12}$: Implementation Ambiguity Elimination | `9.5` | Section 5 & Section 7: 12 self-contained `FEP-###` packets (`FEP-001` to `FEP-012`) with `worker_profile: gemini-3.8-flash-high`, closed `read_context`, wildcard-free `write_targets`, and `python -m` verification commands. |

- **Minimum Core Dimension Score:** $\min(s_1, s_2, s_3, s_4, s_5, s_9) = 9.5 \ge 8.0$.
- **Grounding & Handoff Gates:** $s_1 = 9.5 \ge 9.0$ and $s_{12} = 9.5 \ge 9.0$.
- **Final Status Declaration:** `PASS - EXECUTION READY`
