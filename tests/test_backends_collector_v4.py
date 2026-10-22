"""
Automated validation of FEP-007 & FEP-008: Dual Backend, Caching, and Single-Pass Collector.
"""
from pathlib import Path
from metricsthinking.backends import (
    get_active_backend,
    scan_directory,
    fast_shannon_entropy,
    calculate_shingling_jaccard,
    compute_ast_coupling,
)
from metricsthinking.collector import ProjectCollector


def test_active_backend_availability():
    backend = get_active_backend()
    assert backend in ["RUST_NATIVE", "PYTHON_FALLBACK"]


def test_rust_crate_structure():
    crate_dir = Path("crates/metricsthinking_rs")
    assert crate_dir.exists()
    assert (crate_dir / "Cargo.toml").exists()
    assert (crate_dir / "src/lib.rs").exists()
    assert (crate_dir / "src/walker.rs").exists()
    assert (crate_dir / "src/entropy_sec.rs").exists()
    assert (crate_dir / "src/ast_graph.rs").exists()
    assert (crate_dir / "src/ballast_tokens.rs").exists()


def test_scan_directory_and_incremental_cache(tmp_path):
    f1 = tmp_path / "mod_a.py"
    f1.write_text("import os\nprint('hello')\n", encoding="utf-8")
    f2 = tmp_path / "mod_b.py"
    f2.write_text("import mod_a\n", encoding="utf-8")

    cache_file = tmp_path / "cache.json"

    # First pass: cold start
    records1 = scan_directory(str(tmp_path), cache_path=str(cache_file))
    assert len(records1) == 2
    assert cache_file.exists()

    # Second pass: cache hit
    records2 = scan_directory(str(tmp_path), cache_path=str(cache_file))
    assert len(records2) == 2
    assert records1[0]["sha256"] == records2[0]["sha256"]


def test_shingling_jaccard_backend():
    t1 = "the quick brown fox jumps over the lazy dog"
    t2 = "the quick brown fox jumps over another dog"
    sim = calculate_shingling_jaccard(t1, t2, k=3)
    assert 0.40 <= sim <= 0.85


def test_ast_coupling_calculation():
    files = {
        "core/base.py": "class Base:\n    pass\n",
        "services/service_a.py": "from core.base import Base\n",
        "services/service_b.py": "from core.base import Base\n",
        "services/service_c.py": "from core.base import Base\n",
    }
    metrics = compute_ast_coupling(files)
    assert "afferent_coupling_ca" in metrics
    assert "efferent_coupling_ce" in metrics
    assert "instability_i" in metrics
    # core.base has afferent coupling >= 3
    ca = metrics["afferent_coupling_ca"]
    assert ca.get("core.base", 0) >= 3


def test_single_pass_collector_integration():
    collector = ProjectCollector(target_path=".")
    evidence = collector.collect()
    assert evidence.total_files > 0
    assert len(evidence.file_hashes) > 0
    assert len(evidence.python_files) > 0
    assert "src/metricsthinking/models.py" in evidence.rel_files
    assert evidence.lockfile_pinned is True
    assert len(evidence.evidence_primitives) == 5
    assert evidence.ast_metrics != {}
