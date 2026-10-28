"""
Comprehensive unit and integration tests for ArchetypeDetector & Pre-Flight Probing (Fase 0).
Validates detection accuracy across major engineering archetypes, prevention of AGENTS.md false positives,
and extensible custom profile support.
"""

import json
from pathlib import Path
import pytest

from metricsthinking.detector import ArchetypeDetector, probe_archetype
from metricsthinking.collector import ProjectCollector
from metricsthinking.engine import probe_project, run_audit


def test_sdd_archetype_detection(tmp_path):
    """Verifies that an OpenAPI / Spec-First repository is detected as 'sdd'."""
    (tmp_path / "specs").mkdir(parents=True)
    (tmp_path / "specs" / "openapi.yaml").write_text("openapi: 3.1.0\ninfo:\n  title: Core API\n", encoding="utf-8")
    (tmp_path / "specs" / "contracts").mkdir(parents=True)
    (tmp_path / "specs" / "contracts" / "events.proto").write_text('syntax = "proto3";\n', encoding="utf-8")
    (tmp_path / ".spectral.yaml").write_text("extends: spectral:oas\n", encoding="utf-8")

    res = probe_archetype(str(tmp_path))
    assert res.primary_archetype == "sdd"
    assert res.recommended_profile == "sdd"
    assert res.inspection_mode == "governance_spec"
    assert res.confidence >= 0.70
    assert any("openapi" in s.lower() for s in res.detected_signals)


def test_data_platform_archetype_detection(tmp_path):
    """Verifies that a Lakehouse / dbt repository is detected as 'data-platform'."""
    (tmp_path / "dbt_project.yml").write_text("name: 'analytics_warehouse'\nversion: '1.0.0'\n", encoding="utf-8")
    (tmp_path / "models" / "bronze").mkdir(parents=True)
    (tmp_path / "models" / "bronze" / "raw_events.sql").write_text("SELECT * FROM raw", encoding="utf-8")
    (tmp_path / "models" / "silver").mkdir(parents=True)
    (tmp_path / "models" / "gold").mkdir(parents=True)

    res = probe_archetype(str(tmp_path))
    assert res.primary_archetype == "data-platform"
    assert res.recommended_profile == "data-platform"
    assert res.inspection_mode == "pipeline_orchestration"
    assert res.confidence >= 0.70


def test_web_app_archetype_detection(tmp_path):
    """Verifies that a frontend / web application is detected as 'web-app'."""
    (tmp_path / "package.json").write_text(
        json.dumps({
            "name": "my-dashboard",
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "next": "^14.0.0"
            }
        }),
        encoding="utf-8"
    )
    (tmp_path / "src" / "components").mkdir(parents=True)
    (tmp_path / "src" / "components" / "Header.tsx").write_text("export const Header = () => <nav />;", encoding="utf-8")
    (tmp_path / "src" / "components" / "Chart.tsx").write_text("export const Chart = () => <div />;", encoding="utf-8")
    (tmp_path / "tailwind.config.js").write_text("module.exports = {};", encoding="utf-8")

    res = probe_archetype(str(tmp_path))
    assert res.primary_archetype == "web-app"
    assert res.recommended_profile == "web-app"
    assert res.inspection_mode == "source_code"
    assert res.confidence >= 0.70


def test_mlops_archetype_detection(tmp_path):
    """Verifies that an ML pipeline / DVC project is detected as 'mlops'."""
    (tmp_path / "dvc.yaml").write_text("stages:\n  train:\n    cmd: python train.py\n", encoding="utf-8")
    (tmp_path / "MLproject").write_text("name: churn_predictor\n", encoding="utf-8")
    (tmp_path / "model_cards").mkdir(parents=True)
    (tmp_path / "model_cards" / "v1.md").write_text("# Model Card v1\n", encoding="utf-8")

    res = probe_archetype(str(tmp_path))
    assert res.primary_archetype == "mlops"
    assert res.recommended_profile == "mlops"
    assert res.inspection_mode == "pipeline_orchestration"


def test_llmops_archetype_detection(tmp_path):
    """Verifies that an LLM application with prompt registries & evals is detected as 'llmops'."""
    (tmp_path / "prompts").mkdir(parents=True)
    (tmp_path / "prompts" / "system_prompt.txt").write_text("You are an assistant.", encoding="utf-8")
    (tmp_path / "evals").mkdir(parents=True)
    (tmp_path / "evals" / "test_ragas.py").write_text("from ragas import evaluate\n", encoding="utf-8")
    (tmp_path / "guardrails.py").write_text("# Guardrails config\n", encoding="utf-8")

    res = probe_archetype(str(tmp_path))
    assert res.primary_archetype == "llmops"
    assert res.recommended_profile == "llmops"


def test_gitops_archetype_detection(tmp_path):
    """Verifies that a Kubernetes / Helm repository is detected as 'gitops'."""
    (tmp_path / "Chart.yaml").write_text("apiVersion: v2\nname: microservice\nversion: 0.1.0\n", encoding="utf-8")
    (tmp_path / "templates").mkdir(parents=True)
    (tmp_path / "templates" / "deployment.yaml").write_text("kind: Deployment\n", encoding="utf-8")
    (tmp_path / "kustomization.yaml").write_text("resources:\n  - templates/deployment.yaml\n", encoding="utf-8")

    res = probe_archetype(str(tmp_path))
    assert res.primary_archetype == "gitops"
    assert res.recommended_profile == "gitops"
    assert res.inspection_mode == "declarative_config"


def test_devsecops_archetype_detection(tmp_path):
    """Verifies that a Policy-as-Code / Security repository is detected as 'devsecops'."""
    (tmp_path / "policies").mkdir(parents=True)
    (tmp_path / "policies" / "deny.rego").write_text("package authz\ndefault allow = false\n", encoding="utf-8")
    (tmp_path / "policies" / "ingress.rego").write_text("package kubernetes\n", encoding="utf-8")
    (tmp_path / "trivy.yaml").write_text("severity: HIGH,CRITICAL\n", encoding="utf-8")

    res = probe_archetype(str(tmp_path))
    assert res.primary_archetype == "devsecops"
    assert res.recommended_profile == "devsecops"
    assert res.inspection_mode == "governance_spec"


def test_agent_skill_pure_detection(tmp_path):
    """Verifies that a genuine AI Skill repository is detected as 'agent-skill'."""
    skill_dir = tmp_path / ".agents" / "skills" / "my_custom_skill"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        "---\nname: my_custom_skill\ndescription: AI agent skill\n---\n# My Skill\n",
        encoding="utf-8"
    )
    (tmp_path / "scripts").mkdir(parents=True)
    (tmp_path / "scripts" / "install_skill.py").write_text("# installer\n", encoding="utf-8")

    res = probe_archetype(str(tmp_path))
    assert res.primary_archetype == "agent-skill"
    assert res.recommended_profile == "agent-skill"
    assert res.inspection_mode == "governance_spec"


def test_prevent_agents_md_false_positive(tmp_path):
    """CRITICAL TEST: Verifies that having an AGENTS.md in a software repo does NOT falsely classify it as agent-skill."""
    # Create standard Python software project
    src_dir = tmp_path / "src" / "mypackage"
    src_dir.mkdir(parents=True)
    (src_dir / "__init__.py").write_text("", encoding="utf-8")
    for i in range(12):
        (src_dir / f"mod_{i}.py").write_text(f"def fn_{i}(): return {i}\n", encoding="utf-8")

    (tmp_path / "pyproject.toml").write_text("[project]\nname='mypackage'\nversion='0.1.0'\n", encoding="utf-8")
    tests_dir = tmp_path / "tests"
    tests_dir.mkdir(parents=True)
    (tests_dir / "test_core.py").write_text("def test_ok(): assert True\n", encoding="utf-8")

    # Add standard AI governance files (common in modern software)
    (tmp_path / "AGENTS.md").write_text("# Agent instructions for coding assistant\n", encoding="utf-8")
    (tmp_path / ".cursorrules").write_text("Always write clean code.\n", encoding="utf-8")

    res = probe_archetype(str(tmp_path))

    # MUST be classified as software-engineering, NOT agent-skill!
    assert res.primary_archetype == "software-engineering"
    assert res.recommended_profile == "default"
    assert res.primary_archetype != "agent-skill"


def test_custom_profile_extensibility(tmp_path):
    """Verifies that user-defined custom YAML profiles in .metricsthinking/profiles/ are discovered and supported."""
    custom_dir = tmp_path / ".metricsthinking" / "profiles"
    custom_dir.mkdir(parents=True)
    (custom_dir / "iot-embedded.yaml").write_text(
        """name: iot-embedded
description: Custom profile for IoT and Embedded Systems
domain_archetype: iot-embedded
inspection_mode: source_code
modules: []
""",
        encoding="utf-8"
    )

    detector = ArchetypeDetector(tmp_path)
    discovered = detector._discover_custom_profiles()
    assert "iot-embedded" in discovered
    assert discovered["iot-embedded"].name == "iot-embedded.yaml"


def test_emerging_domain_fallback(tmp_path):
    """Verifies that an uncataloged bare project falls back to adaptive software-engineering metamodel."""
    (tmp_path / "README.md").write_text("# Bare Experimental Project\n", encoding="utf-8")

    res = probe_archetype(str(tmp_path))
    assert res.primary_archetype == "software-engineering"
    assert res.recommended_profile == "default"
    assert res.is_emerging_domain is True
