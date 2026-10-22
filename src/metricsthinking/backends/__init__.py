"""
Backend Selector for MetricsThinking™ v4.0.

Provides automatic runtime selection between native Rust accelerator (_core_rs)
and pure Python fallback with SHA-256 caching.
"""

import logging
from typing import Any
from . import python_fallback as py_backend

logger = logging.getLogger("metricsthinking.backends")

_RUST_AVAILABLE = False
try:
    import _core_rs  # type: ignore
    _RUST_AVAILABLE = True
except ImportError:
    _RUST_AVAILABLE = False


def get_active_backend() -> str:
    """Returns 'RUST_NATIVE' if compiled extension is loaded, else 'PYTHON_FALLBACK'."""
    return "RUST_NATIVE" if _RUST_AVAILABLE else "PYTHON_FALLBACK"


def scan_directory(
    path: str,
    ignore_patterns: list[str] | None = None,
    include_content: bool = True,
    cache_path: str | None = None,
) -> list[dict[str, Any]]:
    """Scans directory via active backend."""
    if _RUST_AVAILABLE:
        try:
            return _core_rs.scan_directory(path, ignore_patterns, include_content)
        except Exception as e:
            logger.warning(f"Native scanner error: {e}. Falling back to Python.")
            return py_backend.scan_directory(path, ignore_patterns, include_content, cache_path)
    return py_backend.scan_directory(path, ignore_patterns, include_content, cache_path)


def fast_shannon_entropy(data: str) -> float:
    """Computes fast Shannon entropy via active backend."""
    if _RUST_AVAILABLE:
        try:
            return float(_core_rs.fast_shannon_entropy(data))
        except Exception:
            return py_backend.fast_shannon_entropy(data)
    return py_backend.fast_shannon_entropy(data)


def calculate_shingling_jaccard(a: str, b: str, k: int = 3) -> float:
    """Computes k-shingle Jaccard overlap via active backend."""
    if _RUST_AVAILABLE:
        try:
            return float(_core_rs.calculate_shingling_jaccard(a, b, k))
        except Exception:
            return py_backend.calculate_shingling_jaccard(a, b, k)
    return py_backend.calculate_shingling_jaccard(a, b, k)


def compute_ast_coupling(python_files: dict[str, str]) -> dict[str, Any]:
    """Computes AST coupling metrics via active backend."""
    if _RUST_AVAILABLE:
        try:
            return _core_rs.compute_ast_coupling(python_files)
        except Exception:
            return py_backend.compute_ast_coupling(python_files)
    return py_backend.compute_ast_coupling(python_files)
