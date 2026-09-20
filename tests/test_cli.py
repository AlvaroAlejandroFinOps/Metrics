"""Unit tests for MetricsThinking CLI."""
import sys
from pathlib import Path

from metricsthinking.cli import main
from metricsthinking.engine import run_audit


def test_engine_run_audit(tmp_path: Path):
    # Setup dummy project
    src = tmp_path / "src"
    src.mkdir()
    (src / "main.py").write_text("print('hello')", encoding="utf-8")
    (tmp_path / "README.md").write_text("# Project\nProblem statement: core architecture.\n", encoding="utf-8")

    out_dir = tmp_path / "artifacts"

    report, written = run_audit(
        target_path=str(tmp_path),
        profile_name="default",
        out_dir=str(out_dir),
        quiet=True,
    )

    assert report is not None
    assert report.consolidated_score > 0
    assert written["markdown"].exists()
    assert written["json"].exists()
    assert written["roadmap"].exists()


def test_cli_main_invocation(tmp_path: Path, monkeypatch):
    # Setup dummy project
    (tmp_path / "README.md").write_text("# Project\nProblem statement: core architecture.\n", encoding="utf-8")
    out_dir = tmp_path / "custom_artifacts"

    test_args = [
        "metricsthinking",
        "audit",
        "--target", str(tmp_path),
        "--out-dir", str(out_dir),
        "--quiet"
    ]
    monkeypatch.setattr(sys, "argv", test_args)

    # Calling main() should run without exceptions
    main()

    assert (out_dir / "MetricsThinking.md").exists()
    assert (out_dir / "MetricsThinking.json").exists()
