"""
Evidence Collector for MetricsThinking™.
Performs comprehensive, strictly READ-ONLY inspection of the target repository.
"""

import os
import subprocess
from pathlib import Path


class ProjectEvidence:
    """Encapsulates all raw physical evidence collected from the repository."""

    def __init__(self, target_path: str):
        self.root_path = Path(target_path).resolve()
        self.project_name = self.root_path.name
        self.exists = self.root_path.exists()

        # Raw findings
        self.files: list[Path] = []
        self.rel_files: list[str] = []
        self.dirs: list[Path] = []
        self.rel_dirs: list[str] = []

        # Metadata
        self.git_commit: str | None = None
        self.git_branch: str | None = None
        self.is_git: bool = False

        # Specific collections
        self.seeds: list[str] = []
        self.manifests: dict[str, str] = {}
        self.context_files: list[str] = []
        self.schemas: list[str] = []
        self.tests: list[str] = []
        self.ci_workflows: list[str] = []
        self.docs: list[str] = []
        self.source_files: list[str] = []
        self.adrs: list[str] = []
        self.dashboards: list[str] = []
        self.tools_and_scripts: list[str] = []

        # Code stats
        self.total_files: int = 0
        self.total_lines_of_code: int = 0
        self.file_extensions: dict[str, int] = {}
        self.file_cache: dict[str, str] = {}  # RelPath -> Content snippet or full text for key files


class ProjectCollector:
    """Reads repository metadata and builds ProjectEvidence with anti-fraud filtering."""

    EXCLUDED_DIRS = {
        ".git", ".venv", "venv", "node_modules", "__pycache__",
        ".pytest_cache", ".ruff_cache", ".mypy_cache", "dist", "build",
        ".egg-info", "data/raw", "data/processed", "data/sandbox", ".system_generated"
    }

    KEY_FILE_EXTENSIONS = {
        ".py", ".ts", ".js", ".json", ".yaml", ".yml", ".md",
        ".toml", ".sh", ".ps1", ".sql", ".rs", ".go"
    }

    def __init__(self, target_path: str):
        self.evidence = ProjectEvidence(target_path)

    def collect(self) -> ProjectEvidence:
        """Executes full read-only scan of the project."""
        if not self.evidence.exists:
            return self.evidence

        self._collect_git_metadata()
        self._scan_filesystem()
        self._classify_files()
        self._read_key_content()
        return self.evidence

    def _collect_git_metadata(self):
        """Reads git commit and branch if repo has .git directory."""
        git_dir = self.evidence.root_path / ".git"
        if git_dir.exists():
            self.evidence.is_git = True
            try:
                commit = subprocess.check_output(
                    ["git", "rev-parse", "--short", "HEAD"],
                    cwd=str(self.evidence.root_path),
                    stderr=subprocess.DEVNULL,
                    text=True
                ).strip()
                self.evidence.git_commit = commit
            except Exception:
                self.evidence.git_commit = "untracked"

            try:
                branch = subprocess.check_output(
                    ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                    cwd=str(self.evidence.root_path),
                    stderr=subprocess.DEVNULL,
                    text=True
                ).strip()
                self.evidence.git_branch = branch
            except Exception:
                self.evidence.git_branch = "unknown"

    def _scan_filesystem(self):
        """Walks tree ignoring noisy / artifact folders."""
        for root, dirs, files in os.walk(self.evidence.root_path):
            # Prune excluded directories
            dirs[:] = [d for d in dirs if d not in self.EXCLUDED_DIRS and not d.startswith(".venv")]

            curr_dir = Path(root)
            rel_dir = curr_dir.relative_to(self.evidence.root_path).as_posix()
            if rel_dir != ".":
                self.evidence.dirs.append(curr_dir)
                self.evidence.rel_dirs.append(rel_dir)

            for f in files:
                file_path = curr_dir / f
                rel_path = file_path.relative_to(self.evidence.root_path).as_posix()
                self.evidence.files.append(file_path)
                self.evidence.rel_files.append(rel_path)

                # Extension count
                ext = file_path.suffix.lower() or "no_ext"
                self.evidence.file_extensions[ext] = self.evidence.file_extensions.get(ext, 0) + 1

        self.evidence.total_files = len(self.evidence.files)

    def _classify_files(self):
        """Categorizes files into evidence buckets with strict anti-fraud filtering."""
        for rel in self.evidence.rel_files:
            lower = rel.lower()

            # Seeds & Core DNA (Only authoritative markdown seeds, excluding test fixtures or previous reports)
            if (("01_seed" in lower or lower.startswith("seed-") or lower.startswith("seed_") or lower.endswith("seed.md")) and lower.endswith(".md")) and not lower.startswith("tests/") and "artifacts/plans/metricsthinking" not in lower:
                self.evidence.seeds.append(rel)

            # Packaging & Manifests
            if lower in ["pyproject.toml", "package.json", "cargo.toml", "requirements.txt", "setup.py", "go.mod"] and not lower.startswith("tests/"):
                self.evidence.manifests[rel] = lower

            # Governance / iDirectory context
            if lower.endswith(".context.yaml") or lower == ".context/tree.json":
                self.evidence.context_files.append(rel)

            # Schemas & Contracts (ignoring pure governance context files)
            if (("schemas/" in lower and not lower.endswith(".context.yaml")) or lower.endswith(".schema.json") or lower.endswith(".proto")) and not lower.startswith("tests/"):
                self.evidence.schemas.append(rel)

            # Tests (valid test code files, not docs or json outputs in tests)
            if (("tests/" in lower or "test_" in lower or lower.endswith("_test.py") or ".spec." in lower) and any(lower.endswith(ext) for ext in [".py", ".ts", ".js", ".rs", ".go"])) and not lower.endswith(".context.yaml") and "tests/other" not in lower:
                self.evidence.tests.append(rel)

            # CI/CD
            if (".github/workflows" in lower or lower in [".gitlab-ci.yml", "jenkinsfile", "dockerfile", "docker-compose.yml", ".pre-commit-config.yaml"]) and not lower.startswith("tests/"):
                self.evidence.ci_workflows.append(rel)

            # Documentation & ADRs
            if (lower.endswith(".md") or "docs/" in lower) and not lower.startswith("tests/") and "artifacts/plans/metricsthinking" not in lower and not lower.endswith(".context.yaml"):
                self.evidence.docs.append(rel)
                if ("adr-" in lower or "docs/notes" in lower or "adr" in lower) and lower.endswith(".md"):
                    self.evidence.adrs.append(rel)

            # Dashboards & BI
            if ("dashboards" in lower or "streamlit" in lower) and any(lower.endswith(ext) for ext in [".py", ".ts", ".js", ".tsx"]) and not lower.endswith(".context.yaml"):
                self.evidence.dashboards.append(rel)

            # Tools & scripts
            if ("tools/" in lower or "scripts/" in lower) and any(lower.endswith(ext) for ext in [".py", ".sh", ".ps1", ".bash", ".ts", ".js"]) and not lower.endswith(".context.yaml"):
                self.evidence.tools_and_scripts.append(rel)

            # Source files
            if (lower.startswith("src/") or lower.startswith("app/") or lower.startswith("lib/")) and any(lower.endswith(ext) for ext in [".py", ".ts", ".js", ".rs", ".go", ".sql"]) and not lower.endswith(".context.yaml"):
                self.evidence.source_files.append(rel)

    def _read_key_content(self):
        """Reads content of high-value metadata files with safety limits."""
        files_to_read = []

        # Read seeds
        files_to_read.extend(self.evidence.seeds)
        # Read manifests
        files_to_read.extend(list(self.evidence.manifests.keys()))
        # Read CI workflows
        files_to_read.extend(self.evidence.ci_workflows)
        # Read docs and active plans
        for rel in self.evidence.docs:
            if "active" in rel.lower() or "foundation" in rel.lower() or rel.lower() in ["readme.md", "readme_es.md", "agents.md"]:
                files_to_read.append(rel)
        if ".context/tree.json" in self.evidence.rel_files:
            files_to_read.append(".context/tree.json")

        for rel in set(files_to_read):
            abs_path = self.evidence.root_path / rel
            if abs_path.exists() and abs_path.is_file():
                try:
                    # Limit reading to 200KB per file for safety
                    content = abs_path.read_text(encoding="utf-8", errors="replace")[:200000]
                    self.evidence.file_cache[rel] = content
                except Exception:
                    pass
