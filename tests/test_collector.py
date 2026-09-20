"""Unit tests for ProjectCollector and ProjectEvidence."""
from pathlib import Path

from metricsthinking.collector import ProjectCollector


def test_collector_basic_scan(tmp_path: Path):
    # Setup dummy project
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    py_file = src_dir / "main.py"
    py_file.write_text("def hello():\n    return 'world'\n", encoding="utf-8")

    doc_file = tmp_path / "README.md"
    doc_file.write_text("# Test Project\n\nProblem statement and architecture.\n", encoding="utf-8")

    collector = ProjectCollector(str(tmp_path))
    evidence = collector.collect()

    assert evidence.total_files >= 2
    assert ".py" in evidence.file_extensions
    assert len(evidence.docs) >= 1
    assert "README.md" in evidence.docs
    assert "problem statement" in evidence.file_cache.get("README.md", "").lower()


def test_collector_anti_fraud_seed_filtering(tmp_path: Path):
    # Valid seed
    seed_dir = tmp_path / "01_seed"
    seed_dir.mkdir()
    real_seed = seed_dir / "seed-test-master.md"
    real_seed.write_text("# Seed Test\nProject DNA\n", encoding="utf-8")

    # Fraudulent test seed in tests directory
    tests_seed_dir = tmp_path / "tests" / "fixtures"
    tests_seed_dir.mkdir(parents=True)
    fake_seed = tests_seed_dir / "seed-fake.md"
    fake_seed.write_text("# Fake Seed\n", encoding="utf-8")

    collector = ProjectCollector(str(tmp_path))
    evidence = collector.collect()

    assert len(evidence.seeds) == 1
    assert "01_seed/seed-test-master.md" in evidence.seeds


def test_collector_detects_ci_and_tests(tmp_path: Path):
    tests_dir = tmp_path / "tests"
    tests_dir.mkdir()
    test_file = tests_dir / "test_app.py"
    test_file.write_text("def test_one(): assert True\n", encoding="utf-8")

    ci_dir = tmp_path / ".github" / "workflows"
    ci_dir.mkdir(parents=True)
    ci_file = ci_dir / "ci.yml"
    ci_file.write_text("name: CI\non: [push]\n", encoding="utf-8")

    collector = ProjectCollector(str(tmp_path))
    evidence = collector.collect()

    assert len(evidence.tests) >= 1
    assert len(evidence.ci_workflows) >= 1
