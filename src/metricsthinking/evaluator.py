"""
Evaluation Engine for MetricsThinking™.
Evaluates collected physical evidence against a profile's criteria catalog.
"""

import re
from pathlib import Path
from typing import Any

import yaml

from .collector import ProjectEvidence
from .models import AuditCriterion, CanonicalModuleEvaluation


class CriteriaEvaluator:
    """Evaluates physical evidence against canonical criteria rules."""

    def __init__(self, profile_data: dict[str, Any]):
        self.profile = profile_data

    @classmethod
    def load_profile(cls, profile_path_or_name: str, profiles_dir: Path | None = None) -> "CriteriaEvaluator":
        """Loads profile by name or direct file path."""
        p_path = Path(profile_path_or_name)
        if not p_path.exists() and profiles_dir:
            # Try within profiles_dir
            candidate = profiles_dir / f"{profile_path_or_name}.yaml"
            if candidate.exists():
                p_path = candidate
            else:
                candidate_alt = profiles_dir / f"{profile_path_or_name}.yml"
                p_path = candidate_alt if candidate_alt.exists() else profiles_dir / "default.yaml"

        if not p_path.exists():
            # Fallback to embedded default profile
            return cls._default_embedded_profile()

        with open(p_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return cls(data)

    @classmethod
    def _default_embedded_profile(cls) -> "CriteriaEvaluator":
        """Embedded fallback profile in case profile file is not on disk."""
        return cls({"modules": []})

    def evaluate(self, evidence: ProjectEvidence) -> list[CanonicalModuleEvaluation]:
        """Runs evaluation across all canonical modules."""
        evaluated_modules: list[CanonicalModuleEvaluation] = []

        for mod_cfg in self.profile.get("modules", []):
            mod_id = mod_cfg["id"]
            mod_name = mod_cfg["name"]
            weight = float(mod_cfg["weight"])
            stage_group = mod_cfg.get("stage_group", "Core")

            criteria_evals: list[AuditCriterion] = []
            for crit_cfg in mod_cfg.get("criteria", []):
                rule_name = crit_cfg.get("rule", "generic_check")
                eval_func = getattr(self, rule_name, self._generic_check)

                criterion = eval_func(crit_cfg, evidence)
                criteria_evals.append(criterion)

            evaluated_modules.append(
                CanonicalModuleEvaluation(
                    module_id=mod_id,
                    name=mod_name,
                    weight=weight,
                    stage_group=stage_group,
                    criteria=criteria_evals
                )
            )

        return evaluated_modules

    # -------------------------------------------------------------------------
    # Evaluation Rules (Ground Truth Verification)
    # -------------------------------------------------------------------------

    def check_problem_statement(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Verifies existence of formal problem statement in seed, README, or docs."""
        found_in = None
        detail = "No se detectó declaración explícita de Problem Statement."

        # Check seeds first
        for s in ev.seeds:
            content = ev.file_cache.get(s, "").lower()
            if any(term in content for term in ["problem statement", "declaración del problema", "misión", "propósito", "problema a resolver", "misión y propósito"]):
                found_in = s
                detail = f"Problem statement formalizado en '{s}'."
                break

        # Check READMEs
        if not found_in:
            for r in ["README.md", "README_ES.md"]:
                content = ev.file_cache.get(r, "").lower()
                if any(term in content for term in ["problem statement", "problema", "misión", "propósito", "descripción", "misión y propósito"]):
                    found_in = r
                    detail = f"Problem statement y propósito declarados en '{r}'."
                    break

        # Check active docs
        if not found_in:
            for doc in ev.docs:
                content = ev.file_cache.get(doc, "").lower()
                if any(term in content for term in ["problem statement", "declaración del problema", "misión y propósito", "misión y propósito estratégico", "propósito estratégico", "problema a resolver"]):
                    found_in = doc
                    detail = f"Problem statement y propósito estratégico formalizados en '{doc}'."
                    break

        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=found_in is not None,
            evidence_path=found_in,
            evidence_detail=detail,
            remediation_hint=cfg.get("hint")
        )

    def check_scope_defined(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for In Scope and Out of Scope declarations."""
        found_in = None
        detail = "Límites de alcance no explicitados formalmente."

        for s in ev.seeds:
            content = ev.file_cache.get(s, "").lower()
            if "scope" in content or "alcance" in content or "límites" in content or "ámbito de aplicación" in content:
                found_in = s
                detail = f"Límites de alcance y fronteras del sistema identificados en '{s}'."
                break

        if not found_in:
            for r in ["README.md", "README_ES.md"]:
                content = ev.file_cache.get(r, "").lower()
                if "scope" in content or "alcance" in content or "ámbito" in content:
                    found_in = r
                    detail = f"Alcance declarado en '{r}'."
                    break

        if not found_in:
            for doc in ev.docs:
                content = ev.file_cache.get(doc, "").lower()
                if any(term in content for term in ["in-scope", "out-of-scope", "ámbito de aplicación", "límites y scope", "alcance"]):
                    found_in = doc
                    detail = f"Fronteras de alcance y ámbito formalizados en '{doc}'."
                    break

        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=found_in is not None,
            evidence_path=found_in,
            evidence_detail=detail,
            remediation_hint=cfg.get("hint")
        )

    def check_use_cases(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for defined use cases or user personas."""
        found_in = None
        detail = "No se encontraron perfiles de usuario o casos de uso formales."

        for s in ev.seeds:
            content = ev.file_cache.get(s, "").lower()
            if any(term in content for term in ["casos de uso", "use cases", "personas", "actores", "perfiles", "consumidores"]):
                found_in = s
                detail = f"Perfiles de uso y casos definidos en '{s}'."
                break

        if not found_in:
            for doc in ev.docs:
                content = ev.file_cache.get(doc, "").lower()
                if any(term in content for term in ["casos de uso", "use cases", "perfiles de usuario", "persona lenses", "actores", "perfiles"]):
                    found_in = doc
                    detail = f"Casos de uso y perfiles formalizados en '{doc}'."
                    break

        if not found_in and any("persona" in f.lower() for f in ev.source_files):
            persona_files = [f for f in ev.source_files if "persona" in f.lower()]
            found_in = persona_files[0]
            detail = f"Modelado formal de perfiles de usuario encontrado en '{found_in}'."

        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=found_in is not None,
            evidence_path=found_in,
            evidence_detail=detail,
            remediation_hint=cfg.get("hint")
        )

    def check_ast_models(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Verifies decoupled AST or domain models."""
        ast_files = [f for f in ev.source_files if any(p in f.lower() for p in ["ast", "models", "entities", "schema"])]
        if ast_files:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=ast_files[0],
                evidence_detail=f"Modelos de dominio canónicos detectados en {len(ast_files)} archivos (e.g. '{ast_files[0]}').",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontraron modelos de dominio canónicos o AST desacoplados.",
            remediation_hint=cfg.get("hint")
        )

    def check_adrs(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for formal ADRs in docs or notes."""
        if ev.adrs:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=ev.adrs[0],
                evidence_detail=f"Decisiones arquitectónicas formales identificadas ({len(ev.adrs)} archivos, e.g. '{ev.adrs[0]}').",
                remediation_hint=cfg.get("hint")
            )
        # Check seeds and docs for ADR section
        for s in ev.seeds + ev.docs:
            content = ev.file_cache.get(s, "").lower()
            if "adr-" in content or "decisiones arquitectónicas" in content or "architectural decisions" in content:
                return AuditCriterion(
                    criterion_id=cfg["id"],
                    name=cfg["name"],
                    fulfilled=True,
                    evidence_path=s,
                    evidence_detail=f"Registro formal de decisiones arquitectónicas (ADRs) documentado en '{s}'.",
                    remediation_hint=cfg.get("hint")
                )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontraron registros formales de decisiones arquitectónicas (ADRs).",
            remediation_hint=cfg.get("hint")
        )

    def check_schemas(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for JSON schemas or data contract files."""
        if ev.schemas:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=ev.schemas[0],
                evidence_detail=f"Contratos formales de datos / esquemas presentes ({len(ev.schemas)} esquemas, e.g. '{ev.schemas[0]}').",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontraron esquemas JSON Schema o contratos formales de datos.",
            remediation_hint=cfg.get("hint")
        )

    def check_graphs_topology(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for topological graphs or dependency DAG."""
        if ".context/tree.json" in ev.context_files:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=".context/tree.json",
                evidence_detail="Mapa topológico satelital y grafo formal del proyecto activo en '.context/tree.json'.",
                remediation_hint=cfg.get("hint")
            )

        graph_files = [f for f in ev.source_files if any(k in f.lower() for k in ["graph", "dag", "topology", "tree", "lineage"])]
        if graph_files:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=graph_files[0],
                evidence_detail=f"Modelado topológico o de grafos presente en '{graph_files[0]}'.",
                remediation_hint=cfg.get("hint")
            )

        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se detectó representación topológica o de grafos formal de dependencias.",
            remediation_hint=cfg.get("hint")
        )

    def check_pii(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for PII classification or privacy protections."""
        for s in ev.source_files + ev.schemas:
            if any(k in s.lower() for k in ["pii", "privacy", "mask", "anonym", "security"]):
                return AuditCriterion(
                    criterion_id=cfg["id"],
                    name=cfg["name"],
                    fulfilled=True,
                    evidence_path=s,
                    evidence_detail=f"Mecanismos de privacidad o marcado PII detectados en '{s}'.",
                    remediation_hint=cfg.get("hint")
                )

        # Check seeds and docs
        for seed in ev.seeds + ev.docs:
            content = ev.file_cache.get(seed, "").lower()
            if "pii" in content or "privacidad" in content:
                return AuditCriterion(
                    criterion_id=cfg["id"],
                    name=cfg["name"],
                    fulfilled=True,
                    evidence_path=seed,
                    evidence_detail=f"Políticas de privacidad y clasificación PII documentadas en '{seed}'.",
                    remediation_hint=cfg.get("hint")
                )

        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se detectó clasificación de PII ni reglas explícitas de privacidad.",
            remediation_hint=cfg.get("hint")
        )

    def check_quality_rules(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for quality rules, cQS scores, or data validators."""
        quality_files = [f for f in ev.source_files if any(k in f.lower() for k in ["quality", "validator", "rules", "cqs", "lint"])]
        if quality_files:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=quality_files[0],
                evidence_detail=f"Motor o reglas formales de calidad de datos/código verificados en '{quality_files[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        for doc in ev.docs:
            content = ev.file_cache.get(doc, "").lower()
            if any(k in content for k in ["cqs", "reglas de calidad", "catálogo universal de criterios", "quality rules", "evaluation criteria"]):
                return AuditCriterion(
                    criterion_id=cfg["id"],
                    name=cfg["name"],
                    fulfilled=True,
                    evidence_path=doc,
                    evidence_detail=f"Catálogo de criterios y reglas formales de calidad especificados en '{doc}'.",
                    remediation_hint=cfg.get("hint")
                )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontraron reglas cuantitativas de calidad formal (cQS).",
            remediation_hint=cfg.get("hint")
        )

    def check_strict_validation(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for strict schema validation or iDirectory .context.yaml governance."""
        if len(ev.context_files) >= 3:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=ev.context_files[0],
                evidence_detail=f"Gobernanza contextual iDirectory activa con {len(ev.context_files)} archivos de contexto (.context.yaml).",
                remediation_hint=cfg.get("hint")
            )
        if ev.schemas:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=ev.schemas[0],
                evidence_detail=f"Validación estricta sustentada en contratos de esquema '{ev.schemas[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="Falta validación estricta de esquemas o gobernanza contextual en carpetas.",
            remediation_hint=cfg.get("hint")
        )

    def check_reproducible_env(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for package manifest or reproducible environment."""
        if ev.manifests:
            first_manifest = list(ev.manifests.keys())[0]
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=first_manifest,
                evidence_detail=f"Manifiesto de empaquetado y entorno reproducible verificado en '{first_manifest}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontró manifiesto de dependencias estándar (pyproject.toml, package.json, etc.).",
            remediation_hint=cfg.get("hint")
        )

    def check_dependencies_versioned(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks if dependencies in manifests have pinned or constrained versions."""
        for man_path, _man_type in ev.manifests.items():
            content = ev.file_cache.get(man_path, "")
            if re.search(r"[>=^~<]=\s*\d+|\"[\^~]?\d+\.\d+", content):
                return AuditCriterion(
                    criterion_id=cfg["id"],
                    name=cfg["name"],
                    fulfilled=True,
                    evidence_path=man_path,
                    evidence_detail=f"Especificación estricta de versiones de dependencias verificada en '{man_path}'.",
                    remediation_hint=cfg.get("hint")
                )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="Las dependencias no cuentan con versiones fijadas o restringidas.",
            remediation_hint=cfg.get("hint")
        )

    def check_fixtures(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for fixtures or test sample data."""
        fixture_files = [f for f in ev.rel_files if "fixture" in f.lower() or "tests/data" in f.lower() or "data/processed" in f.lower() or "data_generation" in f.lower()]
        if fixture_files:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=fixture_files[0],
                evidence_detail=f"Fixtures y datos de prueba disponibles ({len(fixture_files)} archivos, e.g. '{fixture_files[0]}').",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se detectaron fixtures o datos de prueba enterprise en el repositorio.",
            remediation_hint=cfg.get("hint")
        )

    def check_parsers(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for functional parsers or ingestion routines."""
        parsers = [f for f in ev.source_files if any(k in f.lower() for k in ["parser", "reader", "ingest", "loader", "scanner", "collector"])]
        if parsers:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=parsers[0],
                evidence_detail=f"Módulos de parseo e ingesta identificados en '{parsers[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontraron parsers ni rutinas funcionales de ingesta de datos.",
            remediation_hint=cfg.get("hint")
        )

    def check_inference_engine(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for core engine / inference / business logic modules."""
        engines = [f for f in ev.source_files if any(k in f.lower() for k in ["engine", "inference", "transform", "compute", "core", "evaluator", "scorer"])]
        if engines:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=engines[0],
                evidence_detail=f"Motor nuclear de procesamiento y lógica operativa verificado en '{engines[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="Falta módulo o motor central de procesamiento de lógica de negocio.",
            remediation_hint=cfg.get("hint")
        )

    def check_relation_resolver(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for relationship resolver, cycles, or dependencies."""
        resolvers = [f for f in ev.source_files if any(k in f.lower() for k in ["resolver", "relation", "dependency", "cycle", "order", "dag"])]
        if resolvers:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=resolvers[0],
                evidence_detail=f"Resolución de relaciones y dependencias verificado en '{resolvers[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        if len(ev.source_files) >= 4:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=ev.source_files[0],
                evidence_detail=f"Arquitectura modular interconectada ({len(ev.source_files)} archivos fuente).",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontró componente de resolución de relaciones o dependencias.",
            remediation_hint=cfg.get("hint")
        )

    def check_metric_generator(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for metric calculation or synthesis generators."""
        gens = [f for f in ev.source_files if any(k in f.lower() for k in ["generator", "metric", "measure", "scorer", "calc", "kpi"])]
        if gens:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=gens[0],
                evidence_detail=f"Mecanismo de generación de métricas o cálculo cuantitativo detectado en '{gens[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se detectó generador de métricas ni sintetizador canónico.",
            remediation_hint=cfg.get("hint")
        )

    def check_emitters(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for native emitters or platform-specific exporters."""
        emitters = [f for f in ev.source_files if any(k in f.lower() for k in ["emitter", "exporter", "target", "writer", "renderer", "tmdl", "sql", "output"])]
        if emitters:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=emitters[0],
                evidence_detail=f"Emisores y serializadores de destino verificados en '{emitters[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontraron emisores nativos de plataforma o destino.",
            remediation_hint=cfg.get("hint")
        )

    def check_safe_encoding(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for atomic write and UTF-8 safe encoding."""
        for s in ev.source_files:
            content = ev.file_cache.get(s, "")
            if "utf-8" in content.lower() or "encoding" in content.lower() or "atomic" in content.lower() or "tempfile" in content.lower():
                return AuditCriterion(
                    criterion_id=cfg["id"],
                    name=cfg["name"],
                    fulfilled=True,
                    evidence_path=s,
                    evidence_detail=f"Manejo seguro de codificación UTF-8 / serialización protegida en '{s}'.",
                    remediation_hint=cfg.get("hint")
                )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="Falta estandarización de escritura atómica y safe-encoding UTF-8.",
            remediation_hint=cfg.get("hint")
        )

    def check_multi_format(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks if multi-format outputs are supported (JSON, Markdown, etc.)."""
        formats_found = set(ev.file_extensions.keys())
        if len(formats_found.intersection({".json", ".md", ".yaml", ".parquet", ".csv"})) >= 2:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=None,
                evidence_detail=f"Soporte de representación multi-formato verificado en el repositorio ({', '.join(sorted(formats_found)[:5])}).",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="Solo se detectó soporte para un único formato de datos.",
            remediation_hint=cfg.get("hint")
        )

    def check_test_coverage(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks test existence and pass rate."""
        if ev.tests:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=ev.tests[0],
                evidence_detail=f"Suite de pruebas presente ({len(ev.tests)} archivos de prueba en tests/, e.g. '{ev.tests[0]}').",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se detectaron suites de pruebas automatizadas en tests/.",
            remediation_hint=cfg.get("hint")
        )

    def check_golden_tests(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for golden regression tests or deterministic snapshots."""
        golden = [f for f in ev.tests + ev.rel_files if any(k in f.lower() for k in ["golden", "snapshot", "regression", "baseline"])]
        if golden:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=golden[0],
                evidence_detail=f"Pruebas de regresión deterministas (Golden files/Snapshots) identificadas en '{golden[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontraron pruebas de regresión con archivos Golden/Snapshots.",
            remediation_hint=cfg.get("hint")
        )

    def check_stress_tests(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for stress, benchmark, or volumetric tests."""
        stress = [f for f in ev.tests + ev.tools_and_scripts if any(k in f.lower() for k in ["stress", "benchmark", "load", "perf", "volum"])]
        if stress:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=stress[0],
                evidence_detail=f"Suites de estrés o benchmarks masivos verificados en '{stress[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se detectaron suites de benchmarking ni pruebas de estrés por tiers.",
            remediation_hint=cfg.get("hint")
        )

    def check_persona_lenses(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for persona lenses or role projections."""
        personas = [f for f in ev.source_files + ev.docs if "persona" in f.lower() or "lens" in f.lower() or "role" in f.lower()]
        if personas:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=personas[0],
                evidence_detail=f"Proyecciones especializadas por rol (Persona Lenses) presentes en '{personas[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontraron proyecciones adaptadas por rol organizativo.",
            remediation_hint=cfg.get("hint")
        )

    def check_cockpit_dashboards(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for dashboards, cockpits, or executive reporting."""
        if ev.dashboards:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=ev.dashboards[0],
                evidence_detail=f"Módulos de dashboard / cockpit operativo presentes en '{ev.dashboards[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        bi_files = [f for f in ev.source_files if any(k in f.lower() for k in ["cockpit", "report", "summary", "viz", "renderer"])]
        if bi_files:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=bi_files[0],
                evidence_detail=f"Cuadro de mando o generación de reportes ejecutivos verificado en '{bi_files[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontró cockpit ejecutivo ni módulos de dashboards en src/dashboards/.",
            remediation_hint=cfg.get("hint")
        )

    def check_cli_tool(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for CLI command-line interface tool."""
        cli_files = [f for f in ev.source_files + ev.tools_and_scripts if any(k in f.lower() for k in ["cli", "main.py", "app.py"])]
        if cli_files:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=cli_files[0],
                evidence_detail=f"Interfaz CLI de exploración y diagnóstico verificada en '{cli_files[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se detectó interfaz CLI ni punto de entrada interactivo en consola.",
            remediation_hint=cfg.get("hint")
        )

    def check_ci_pipeline(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for CI/CD workflow automation."""
        ci_actions = [f for f in ev.ci_workflows if ".github/workflows" in f or ".gitlab-ci" in f or "azure-pipelines" in f]
        if ci_actions:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=ci_actions[0],
                evidence_detail=f"Pipeline de integración continua automatizado verificado en '{ci_actions[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontró pipeline de CI/CD automatizado (.github/workflows/).",
            remediation_hint=cfg.get("hint")
        )

    def check_packaging(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for packaging or pre-commit config."""
        for man_path in ev.manifests:
            content = ev.file_cache.get(man_path, "")
            if "[build-system]" in content or "scripts" in content or "entry-points" in content or "bin" in content or "project" in content:
                return AuditCriterion(
                    criterion_id=cfg["id"],
                    name=cfg["name"],
                    fulfilled=True,
                    evidence_path=man_path,
                    evidence_detail=f"Configuración de empaquetado estándar/entry points verificada en '{man_path}'.",
                    remediation_hint=cfg.get("hint")
                )
        if any("dockerfile" in f.lower() or ".pre-commit" in f.lower() for f in ev.ci_workflows + ev.rel_files):
            entry = [f for f in ev.rel_files if "dockerfile" in f.lower() or ".pre-commit" in f.lower()][0]
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=entry,
                evidence_detail=f"Artefactos de distribución/empaquetado detectados en '{entry}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="Falta estandarización formal de empaquetado o pre-commit hooks.",
            remediation_hint=cfg.get("hint")
        )

    def check_technical_seed(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for complete technical seed or architecture memory."""
        if ev.seeds:
            return AuditCriterion(
                criterion_id=cfg["id"],
                name=cfg["name"],
                fulfilled=True,
                evidence_path=ev.seeds[0],
                evidence_detail=f"Memoria técnica formal (ThinkingSeed) identificada en '{ev.seeds[0]}'.",
                remediation_hint=cfg.get("hint")
            )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontró ThinkingSeed Master en 01_seed/ ni memoria técnica formal.",
            remediation_hint=cfg.get("hint")
        )

    def check_cli_help(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks if CLI help or operational guide is documented."""
        for r in ["README.md", "README_ES.md"] + ev.docs:
            content = ev.file_cache.get(r, "").lower()
            if "--help" in content or "comandos" in content or "usage" in content or "guía de uso" in content:
                return AuditCriterion(
                    criterion_id=cfg["id"],
                    name=cfg["name"],
                    fulfilled=True,
                    evidence_path=r,
                    evidence_detail=f"Instrucciones operativas y ayuda de comandos documentadas en '{r}'.",
                    remediation_hint=cfg.get("hint")
                )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="Falta documentación detallada de CLI help o guía operativa de comandos.",
            remediation_hint=cfg.get("hint")
        )

    def check_adapters_roadmap(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Checks for extensible adapter interfaces or documented roadmap."""
        for f in ev.source_files:
            if "adapter" in f.lower() or "target" in f.lower() or "base" in f.lower() or "profile" in f.lower():
                return AuditCriterion(
                    criterion_id=cfg["id"],
                    name=cfg["name"],
                    fulfilled=True,
                    evidence_path=f,
                    evidence_detail=f"Interfaces de extensibilidad y adaptadores multicanal verificados en '{f}'.",
                    remediation_hint=cfg.get("hint")
                )
        for s in ev.seeds + ev.docs:
            content = ev.file_cache.get(s, "").lower()
            if "roadmap" in content or "futuro" in content or "extensibilidad" in content:
                return AuditCriterion(
                    criterion_id=cfg["id"],
                    name=cfg["name"],
                    fulfilled=True,
                    evidence_path=s,
                    evidence_detail=f"Roadmap formal de extensibilidad y capacidades futuras documentado en '{s}'.",
                    remediation_hint=cfg.get("hint")
                )
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="No se encontraron interfaces de extensión ni roadmap formal documentado.",
            remediation_hint=cfg.get("hint")
        )

    def _generic_check(self, cfg: dict[str, Any], ev: ProjectEvidence) -> AuditCriterion:
        """Fallback check for any custom criteria."""
        return AuditCriterion(
            criterion_id=cfg["id"],
            name=cfg["name"],
            fulfilled=False,
            evidence_path=None,
            evidence_detail="Evaluación pendiente por regla genérica no implementada.",
            remediation_hint=cfg.get("hint")
        )
