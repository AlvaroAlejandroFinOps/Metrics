"""
Automated validation of FEP-001: Technical Debt Sanitization and Repository Hygiene.
"""
from pathlib import Path
import json
import tomllib
import metricsthinking


def test_requirements_hygiene():
    req_path = Path("requirements.txt")
    assert req_path.exists(), "requirements.txt must exist"
    raw = req_path.read_bytes()
    assert not raw.startswith(b"\xff\xfe"), "requirements.txt must not have UTF-16LE BOM"
    assert not raw.startswith(b"\xef\xbb\xbf"), "requirements.txt must not have UTF-8 BOM"
    content = raw.decode("utf-8")
    assert "-e" not in content, "requirements.txt must not contain editable local install path"
    assert "PROYECTOS" not in content, "requirements.txt must not contain absolute Windows path"
    assert "pydantic>=2.0.0" in content
    assert "jsonschema>=4.19.0" in content


def test_pyproject_version_and_deps():
    pyproject_path = Path("pyproject.toml")
    assert pyproject_path.exists()
    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)
    assert data["project"]["version"] == "4.0.0"
    deps = data["project"]["dependencies"]
    assert any("jsonschema" in d for d in deps)


def test_package_and_mcp_version_sync():
    assert metricsthinking.__version__ == "4.0.0"
    mcp_code = Path("src/metricsthinking/mcp_server.py").read_text(encoding="utf-8")
    assert '"version": "4.0.0"' in mcp_code


def test_skeleton_directories_removed():
    deleted_dirs = [
        Path("src/cloud_jobs"),
        Path("src/core"),
        Path("src/dashboards"),
        Path("src/data_generation"),
        Path("tools"),
    ]
    for d in deleted_dirs:
        assert not d.exists(), f"Skeleton dir {d} must be deleted"


def test_engine_readme_seed_link():
    engine_readme = Path("02_foundation/engine/engine_readme.md").read_text(encoding="utf-8")
    assert "seed-metricsthinking-master.md" in engine_readme
    assert "seed-idirectory-master.md" not in engine_readme


def test_tree_json_hygiene():
    tree_path = Path(".context/tree.json")
    assert tree_path.exists()
    tree = json.loads(tree_path.read_text(encoding="utf-8"))
    nodes = list(tree.get("nodes", {}).keys())
    assert "src/metricsthinking" in nodes
    assert "src/cloud_jobs" not in nodes
    assert "src/core" not in nodes
    assert "src/dashboards" not in nodes
    assert "src/data_generation" not in nodes
    assert "tools" not in nodes
