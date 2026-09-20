"""Unit tests for CriteriaEvaluator."""
from pathlib import Path

from metricsthinking.collector import ProjectCollector
from metricsthinking.evaluator import CriteriaEvaluator


def test_evaluator_default_profile(tmp_path: Path):
    # Create sample project structure
    (tmp_path / "01_seed").mkdir()
    (tmp_path / "01_seed" / "seed-project-master.md").write_text("# Project Architecture\nProblem Statement: Core scope.", encoding="utf-8")

    (tmp_path / "pyproject.toml").write_text("[build-system]\nrequires = ['setuptools']\n[project]\nname = 'test'\nversion = '1.0.0'\ndependencies = ['pydantic>=2.0.0']", encoding="utf-8")

    (tmp_path / "src" / "pkg").mkdir(parents=True)
    (tmp_path / "src" / "pkg" / "__init__.py").write_text("", encoding="utf-8")
    (tmp_path / "src" / "pkg" / "engine.py").write_text(
        "class ProcessingEngine:\n    def process(self, data: str) -> str:\n        return data.strip()\n",
        encoding="utf-8"
    )

    collector = ProjectCollector(str(tmp_path))
    evidence = collector.collect()

    profiles_dir = Path(__file__).parent.parent / "config" / "profiles"
    evaluator = CriteriaEvaluator.load_profile("default", profiles_dir=profiles_dir)
    modules = evaluator.evaluate(evidence)

    assert len(modules) == 10
    # M01 should have criteria passed
    m01 = next(m for m in modules if m.module_id == "M01")
    assert m01.criteria_passed > 0
    assert m01.phase_completion_pct > 0.0


def test_evaluator_detects_empty_repository(tmp_path: Path):
    collector = ProjectCollector(str(tmp_path))
    evidence = collector.collect()

    profiles_dir = Path(__file__).parent.parent / "config" / "profiles"
    evaluator = CriteriaEvaluator.load_profile("default", profiles_dir=profiles_dir)
    modules = evaluator.evaluate(evidence)

    assert len(modules) == 10
    for mod in modules:
        assert mod.phase_completion_pct == 0.0
        assert mod.status.value in ["backlog", "blocked"]
