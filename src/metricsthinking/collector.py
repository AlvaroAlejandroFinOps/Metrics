"""
Evidence Collector for MetricsThinking™.
Performs comprehensive, strictly READ-ONLY inspection of the target repository.
"""

import os
import subprocess
from pathlib import Path
from typing import Any

import yaml

from metricsthinking.models import EvidencePrimitiveSummary


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

        # Specific collections (canonical & legacy compatibility)
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

        # v3.0 Universal Evidence Primitives
        self.evidence_primitives: dict[str, EvidencePrimitiveSummary] = {}
        self.detected_archetype: str | None = None
        self.detected_mode: str | None = None
        self.seed_detected: bool = False
        self.seed_version: str | None = None
        self.seed_data: dict[str, Any] = {}

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
        ".toml", ".sh", ".ps1", ".sql", ".rs", ".go", ".tf", ".hcl",
        ".proto", ".graphql", ".gql", ".cue", ".rego"
    }

    def __init__(self, target_path: str, evidence_hints: dict[str, Any] | None = None):
        self.evidence = ProjectEvidence(target_path)
        self.evidence_hints = evidence_hints or {}

    def collect(self) -> ProjectEvidence:
        """Executes full read-only scan of the project."""
        if not self.evidence.exists:
            return self.evidence

        self._collect_git_metadata()
        self._scan_filesystem()
        self._classify_files()
        self._read_key_content()
        self._parse_seed_metadata()
        self._classify_universal_primitives()
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
        custom_source_prefixes = self.evidence_hints.get("source_patterns", [])
        custom_test_prefixes = self.evidence_hints.get("test_patterns", [])

        for rel in self.evidence.rel_files:
            lower = rel.lower()

            # Seeds & Core DNA (Only authoritative markdown seeds, excluding test fixtures or previous reports)
            if (("01_seed" in lower or lower.startswith("seed-") or lower.startswith("seed_") or lower.endswith("seed.md")) and lower.endswith(".md")) and not lower.startswith("tests/") and "artifacts/plans/metricsthinking" not in lower:
                self.evidence.seeds.append(rel)

            # Packaging & Manifests
            if lower in ["pyproject.toml", "package.json", "cargo.toml", "requirements.txt", "setup.py", "go.mod", "kustomization.yaml", "chart.yaml", "terraform.tf", "dbt_project.yml"] and not lower.startswith("tests/"):
                self.evidence.manifests[rel] = lower

            # Governance / iDirectory context
            if lower.endswith(".context.yaml") or lower == ".context/tree.json":
                self.evidence.context_files.append(rel)

            # Schemas & Contracts (ignoring pure governance context files)
            if (("schemas/" in lower and not lower.endswith(".context.yaml")) or lower.endswith(".schema.json") or lower.endswith(".proto") or lower.endswith(".graphql") or lower.endswith(".gql") or "openapi" in lower) and not lower.startswith("tests/"):
                self.evidence.schemas.append(rel)

            # Tests (valid test code files, not docs or json outputs in tests)
            is_test = False
            if (("tests/" in lower or "test_" in lower or lower.endswith("_test.py") or ".spec." in lower) and any(lower.endswith(ext) for ext in [".py", ".ts", ".js", ".rs", ".go"])) and not lower.endswith(".context.yaml") and "tests/other" not in lower:
                is_test = True
            elif custom_test_prefixes and any(lower.startswith(p.lower()) or p.lower() in lower for p in custom_test_prefixes):
                is_test = True

            if is_test:
                self.evidence.tests.append(rel)

            # CI/CD
            if (".github/workflows" in lower or lower in [".gitlab-ci.yml", "jenkinsfile", "dockerfile", "docker-compose.yml", ".pre-commit-config.yaml", "skaffold.yaml"]) and not lower.startswith("tests/"):
                self.evidence.ci_workflows.append(rel)

            # Documentation & ADRs
            if (lower.endswith(".md") or "docs/" in lower) and not lower.startswith("tests/") and "artifacts/plans/metricsthinking" not in lower and not lower.endswith(".context.yaml"):
                self.evidence.docs.append(rel)
                if ("adr-" in lower or "docs/notes" in lower or "adr" in lower or "/decisions/" in lower) and lower.endswith(".md"):
                    self.evidence.adrs.append(rel)

            # Dashboards & BI
            if ("dashboards" in lower or "streamlit" in lower or "grafana" in lower) and any(lower.endswith(ext) for ext in [".py", ".ts", ".js", ".tsx", ".json"]) and not lower.endswith(".context.yaml"):
                self.evidence.dashboards.append(rel)

            # Tools & scripts
            if ("tools/" in lower or "scripts/" in lower) and any(lower.endswith(ext) for ext in [".py", ".sh", ".ps1", ".bash", ".ts", ".js"]) and not lower.endswith(".context.yaml"):
                self.evidence.tools_and_scripts.append(rel)

            # Source files
            is_source = False
            if (lower.startswith("src/") or lower.startswith("app/") or lower.startswith("lib/") or lower.startswith("pkg/")) and any(lower.endswith(ext) for ext in [".py", ".ts", ".js", ".rs", ".go", ".sql", ".tf", ".rego"]) and not lower.endswith(".context.yaml"):
                is_source = True
            elif custom_source_prefixes and any(lower.startswith(p.lower()) or p.lower() in lower for p in custom_source_prefixes):
                is_source = True

            if is_source:
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

    def _parse_seed_metadata(self):
        """Parses ThinkingSeed metadata if present in repo."""
        for seed_rel in self.evidence.seeds:
            content = self.evidence.file_cache.get(seed_rel, "")
            if not content:
                abs_path = self.evidence.root_path / seed_rel
                if abs_path.exists() and abs_path.is_file():
                    try:
                        content = abs_path.read_text(encoding="utf-8", errors="replace")[:100000]
                    except Exception:
                        continue

            if content:
                self.evidence.seed_detected = True
                # Check for YAML frontmatter
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        try:
                            data = yaml.safe_load(parts[1])
                            if isinstance(data, dict):
                                self.evidence.seed_data = data
                                self.evidence.detected_archetype = data.get("domain_archetype") or data.get("archetype")
                                self.evidence.detected_mode = data.get("inspection_mode")
                                self.evidence.seed_version = str(data.get("seed_version", "3.0"))
                        except Exception:
                            pass
                break

    def _classify_universal_primitives(self):
        """Builds universal evidence primitives for polymorphic evaluation."""
        primitives: dict[str, list[str]] = {
            "config": [],
            "spec": [],
            "pipeline": [],
            "verification": [],
            "implementation": []
        }

        for rel in self.evidence.rel_files:
            lower = rel.lower()

            # Config
            if any(lower.endswith(ext) for ext in [".yaml", ".yml", ".toml", ".ini", ".env", ".tfvars"]) or "config/" in lower or lower in ["dockerfile", "docker-compose.yml", "kustomization.yaml"]:
                primitives["config"].append(rel)

            # Spec
            if lower.endswith(".schema.json") or lower.endswith(".proto") or lower.endswith(".graphql") or "openapi" in lower or "swagger" in lower or lower.startswith("specs/") or lower.startswith("contracts/") or rel in self.evidence.adrs or rel in self.evidence.seeds:
                primitives["spec"].append(rel)

            # Pipeline
            if ".github/workflows" in lower or "pipelines/" in lower or "dags/" in lower or "flows/" in lower or lower.startswith(".gitlab") or "jenkins" in lower or "argo/" in lower:
                primitives["pipeline"].append(rel)

            # Verification
            if rel in self.evidence.tests or "evals/" in lower or "benchmarks/" in lower or "experiments/" in lower or "chaos/" in lower or "policies/" in lower or "rego/" in lower:
                primitives["verification"].append(rel)

            # Implementation
            if rel in self.evidence.source_files or "models/" in lower or "dbt/" in lower or "prompts/" in lower or "modules/" in lower or "charts/" in lower:
                primitives["implementation"].append(rel)

        for p_type, p_files in primitives.items():
            self.evidence.evidence_primitives[p_type] = EvidencePrimitiveSummary(
                primitive_type=p_type,
                file_count=len(p_files),
                total_lines=0,  # Computed lazily if needed
                sample_paths=p_files[:5],
                verified_valid=len(p_files) > 0
            )
