"""
Pure Python High-Efficiency Fallback Backend for MetricsThinking™ v4.0.

Provides single-pass directory scanning with incremental SHA-256 caching,
AST dependency coupling (Ca, Ce, Instability, SPOFs), Shannon entropy,
and k-shingle Jaccard overlap when native Rust extension is not available.
"""

from collections import Counter
import hashlib
import json
import math
import os
from pathlib import Path
import re
from typing import Any

DEFAULT_EXCLUDED_DIRS = {
    ".git", ".venv", "venv", "node_modules", "__pycache__",
    ".pytest_cache", ".ruff_cache", ".mypy_cache", "dist", "build",
    ".egg-info", "data/raw", "data/processed", "data/sandbox", ".system_generated"
}

_MEMORY_CONTENT_CACHE: dict[tuple[str, float, int], str] = {}


def fast_shannon_entropy(data: str) -> float:
    """Computes Shannon entropy in bits per symbol."""
    if not data:
        return 0.0
    length = len(data)
    counts = Counter(data)
    return -sum((count / length) * math.log2(count / length) for count in counts.values())


def calculate_shingling_jaccard(a: str, b: str, k: int = 3) -> float:
    """Computes k-shingle Jaccard similarity between two texts."""
    words_a = re.findall(r"\w+", a.lower())
    words_b = re.findall(r"\w+", b.lower())

    if len(words_a) < k:
        shingles_a = set(words_a)
    else:
        shingles_a = {" ".join(words_a[i:i+k]) for i in range(len(words_a) - k + 1)}

    if len(words_b) < k:
        shingles_b = set(words_b)
    else:
        shingles_b = {" ".join(words_b[i:i+k]) for i in range(len(words_b) - k + 1)}

    union = len(shingles_a.union(shingles_b))
    if union == 0:
        return 0.0
    intersection = len(shingles_a.intersection(shingles_b))
    return round(intersection / union, 4)


def scan_directory(
    path: str,
    ignore_patterns: list[str] | None = None,
    include_content: bool = True,
    cache_path: str | None = None,
) -> list[dict[str, Any]]:
    """
    Performs a single-pass file system crawl with incremental SHA-256 caching.
    """
    root = Path(path).resolve()
    if not root.exists():
        return []

    pats = ignore_patterns or []
    cache_file = Path(cache_path) if cache_path else root / ".context" / "cache" / "scan_cache.json"
    cache: dict[str, dict[str, Any]] = {}

    if cache_file.exists():
        try:
            cache = json.loads(cache_file.read_text(encoding="utf-8"))
        except Exception:
            cache = {}

    records: list[dict[str, Any]] = []
    new_cache: dict[str, dict[str, Any]] = {}

    for dirpath, dirnames, filenames in os.walk(root):
        # Exclude directories
        dirnames[:] = [
            d for d in dirnames
            if d not in DEFAULT_EXCLUDED_DIRS and d not in pats and not (d.startswith(".venv") or d == ".git")
        ]

        curr_dir = Path(dirpath)
        for f in filenames:
            file_path = curr_dir / f
            try:
                rel_path = file_path.relative_to(root).as_posix()
            except ValueError:
                rel_path = file_path.as_posix()

            if file_path.resolve() == cache_file.resolve():
                continue
            if any(rel_path.startswith(f"{p}/") or f"/{p}/" in rel_path or rel_path == p or rel_path.endswith(f"/{p}") for p in pats):
                continue
            if rel_path == ".git" or rel_path.startswith(".git/") or "/.git/" in rel_path or "__pycache__" in rel_path:
                continue

            try:
                stat = file_path.stat()
                size_bytes = stat.st_size
                mtime = stat.st_mtime
            except OSError:
                continue

            # Check cache
            cached = cache.get(rel_path)
            content_str = None
            if cached and cached.get("mtime") == mtime and cached.get("size") == size_bytes:
                sha256 = cached["sha256"]
                line_count = cached["line_count"]
                token_estimate = cached["token_estimate"]
                if include_content and size_bytes < 2 * 1024 * 1024:
                    mem_key = (file_path.as_posix(), mtime, size_bytes)
                    if mem_key in _MEMORY_CONTENT_CACHE:
                        content_str = _MEMORY_CONTENT_CACHE[mem_key]
                    else:
                        try:
                            content_str = file_path.read_text(encoding="utf-8", errors="replace")
                            if len(_MEMORY_CONTENT_CACHE) > 50000:
                                _MEMORY_CONTENT_CACHE.clear()
                            _MEMORY_CONTENT_CACHE[mem_key] = content_str
                        except Exception:
                            content_str = None
            else:
                # Fresh compute
                sha256 = ""
                line_count = 0
                if size_bytes < 2 * 1024 * 1024:
                    try:
                        content_str = file_path.read_text(encoding="utf-8", errors="replace")
                        line_count = content_str.count("\n") + (1 if content_str and not content_str.endswith("\n") else 0)
                        sha256 = hashlib.sha256(content_str.encode("utf-8")).hexdigest()
                        mem_key = (file_path.as_posix(), mtime, size_bytes)
                        if len(_MEMORY_CONTENT_CACHE) > 50000:
                            _MEMORY_CONTENT_CACHE.clear()
                        _MEMORY_CONTENT_CACHE[mem_key] = content_str
                    except Exception:
                        content_str = None
                if not sha256:
                    try:
                        sha256 = hashlib.sha256(file_path.read_bytes()).hexdigest()
                    except Exception:
                        sha256 = "error"

                token_estimate = max(1, size_bytes // 4)

            new_cache[rel_path] = {
                "mtime": mtime,
                "size": size_bytes,
                "sha256": sha256,
                "line_count": line_count,
                "token_estimate": token_estimate,
            }

            records.append({
                "path": rel_path,
                "size_bytes": size_bytes,
                "line_count": line_count,
                "sha256": sha256,
                "token_estimate": token_estimate,
                "content": content_str if include_content else None,
            })

    # Save cache safely
    try:
        cache_file.parent.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(json.dumps(new_cache, indent=2), encoding="utf-8")
    except Exception:
        pass

    records.sort(key=lambda r: r["path"])
    return records


def compute_ast_coupling(python_files: dict[str, str]) -> dict[str, Any]:
    """
    Computes Afferent Coupling (Ca), Efferent Coupling (Ce), Instability (I),
    SPOF identification, and resilience pattern detection across Python source files.
    """
    all_modules: set[str] = set()
    import_graph: dict[str, set[str]] = {}

    for path in python_files.keys():
        norm = path.replace("\\", "/").rstrip(".py")
        mod_name = norm.replace("/", ".")
        all_modules.add(mod_name)
        import_graph[mod_name] = set()

    resilience_patterns: dict[str, int] = {
        "timeout": 0,
        "retry": 0,
        "circuit_breaker": 0,
        "fallback": 0,
    }

    for path, content in python_files.items():
        norm = path.replace("\\", "/").rstrip(".py")
        mod_name = norm.replace("/", ".")
        deps: set[str] = set()

        for line in content.splitlines():
            stripped = line.strip()

            # Scan resilience patterns
            if "timeout" in stripped.lower() or "timeout=" in stripped:
                resilience_patterns["timeout"] += 1
            if "retry" in stripped.lower() or "backoff" in stripped.lower():
                resilience_patterns["retry"] += 1
            if "circuit_breaker" in stripped.lower() or "circuitbreaker" in stripped.lower():
                resilience_patterns["circuit_breaker"] += 1
            if "fallback" in stripped.lower():
                resilience_patterns["fallback"] += 1

            # Imports
            if stripped.startswith("import ") or stripped.startswith("from "):
                for other in all_modules:
                    if other != mod_name and (other in stripped or other.split(".")[-1] in stripped):
                        deps.add(other)

        import_graph[mod_name] = deps

    ca: dict[str, int] = {m: 0 for m in all_modules}
    ce: dict[str, int] = {m: len(deps) for m, deps in import_graph.items()}
    instability: dict[str, float] = {}

    for src, targets in import_graph.items():
        for target in targets:
            if target in ca:
                ca[target] += 1

    spof_nodes: list[str] = []
    for m in sorted(list(all_modules)):
        aff = ca[m]
        eff = ce[m]
        tot = aff + eff
        inst = round(eff / tot, 3) if tot > 0 else 0.0
        instability[m] = inst

        # Single Point of Failure (SPOF): High afferent coupling (>= 3) and low efferent coupling (<= 1)
        if aff >= 3 and eff <= 1:
            spof_nodes.append(m)

    # Coverage ratio of critical modules having resilience patterns
    total_patterns = sum(resilience_patterns.values())
    resilience_coverage_ratio = round(min(1.0, total_patterns / max(1, len(all_modules))), 3)

    return {
        "afferent_coupling_ca": ca,
        "efferent_coupling_ce": ce,
        "instability_i": instability,
        "spof_nodes": spof_nodes,
        "resilience_patterns_count": resilience_patterns,
        "resilience_coverage_ratio": resilience_coverage_ratio,
    }
