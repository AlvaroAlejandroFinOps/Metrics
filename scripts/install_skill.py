#!/usr/bin/env python3
"""
MetricsThinking™ Multi-Provider AI Skill Installer.
Deploys skill definitions, prompt rules, and MCP configurations across AI environments:
- Google Antigravity (Local & Global) 
- Anthropic Claude Code & Claude Desktop
- Cursor IDE & Windsurf
- GitHub Copilot & OpenAI
- Model Context Protocol (MCP) Clients
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

# Resolve repository root
REPO_ROOT = Path(__file__).resolve().parent.parent


def get_user_home() -> Path:
    return Path.home()


def install_antigravity(dest_root: Path, is_global: bool = False, dry_run: bool = False) -> list[Path]:
    created = []
    if is_global:
        target_skill_dir = get_user_home() / ".gemini" / "config" / "skills" / "metrics"
    else:
        target_skill_dir = dest_root / ".agents" / "skills" / "metrics"

    print(f"[*] Installing Google Antigravity Skill -> {target_skill_dir}")

    src_skill_md = REPO_ROOT / ".agents" / "skills" / "metrics" / "SKILL.md"
    if not src_skill_md.exists():
        # Fallback to local copy if needed
        src_skill_md = REPO_ROOT / "config" / "SKILL.md"

    if not dry_run:
        target_skill_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_skill_dir / "SKILL.md"
        if src_skill_md.exists():
            if src_skill_md.resolve() != target_file.resolve():
                shutil.copy2(src_skill_md, target_file)
            created.append(target_file)

        # Copy scripts and packages if global install
        if is_global:
            scripts_dest = target_skill_dir / "scripts"
            # Purge stale pycache if present
            for pycache_dir in scripts_dest.rglob("__pycache__"):
                if pycache_dir.is_dir():
                    shutil.rmtree(pycache_dir, ignore_errors=True)
            scripts_dest.mkdir(parents=True, exist_ok=True)
            src_pkg = REPO_ROOT / "src" / "metricsthinking"
            if src_pkg.exists():
                pkg_dest = scripts_dest / "metricsthinking"
                shutil.copytree(src_pkg, pkg_dest, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                created.append(pkg_dest)
                for py_file in src_pkg.glob("*.py"):
                    shutil.copy2(py_file, scripts_dest / py_file.name)
                    created.append(scripts_dest / py_file.name)
            
            profiles_dest = target_skill_dir / "profiles"
            profiles_dest.mkdir(parents=True, exist_ok=True)
            for yaml_file in (REPO_ROOT / "config" / "profiles").glob("*.yaml"):
                shutil.copy2(yaml_file, profiles_dest / yaml_file.name)
                created.append(profiles_dest / yaml_file.name)

            gov_yaml = REPO_ROOT / "config" / "fpai_governance.yaml"
            if gov_yaml.exists():
                gov_dest = target_skill_dir / "fpai_governance.yaml"
                shutil.copy2(gov_yaml, gov_dest)
                created.append(gov_dest)
    else:
        created.append(target_skill_dir / "SKILL.md")

    return created


def install_codex(dest_root: Path, is_global: bool = False, dry_run: bool = False) -> list[Path]:
    created = []
    if is_global:
        target_skill_dir = get_user_home() / ".codex" / "skills" / "metrics"
    else:
        target_skill_dir = dest_root / ".codex" / "skills" / "metrics"

    print(f"[*] Installing OpenAI Codex Skill -> {target_skill_dir}")

    src_skill_md = REPO_ROOT / ".agents" / "skills" / "metrics" / "SKILL.md"
    if not src_skill_md.exists():
        src_skill_md = REPO_ROOT / "config" / "SKILL.md"

    if not dry_run:
        target_skill_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_skill_dir / "SKILL.md"
        if src_skill_md.exists():
            if src_skill_md.resolve() != target_file.resolve():
                shutil.copy2(src_skill_md, target_file)
            created.append(target_file)

        # Copy scripts, profiles and packages if global install
        if is_global:
            scripts_dest = target_skill_dir / "scripts"
            # Purge stale pycache if present
            for pycache_dir in scripts_dest.rglob("__pycache__"):
                if pycache_dir.is_dir():
                    shutil.rmtree(pycache_dir, ignore_errors=True)
            scripts_dest.mkdir(parents=True, exist_ok=True)
            src_pkg = REPO_ROOT / "src" / "metricsthinking"
            if src_pkg.exists():
                pkg_dest = scripts_dest / "metricsthinking"
                shutil.copytree(src_pkg, pkg_dest, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
                created.append(pkg_dest)
                for py_file in src_pkg.glob("*.py"):
                    shutil.copy2(py_file, scripts_dest / py_file.name)
                    created.append(scripts_dest / py_file.name)
            
            profiles_dest = target_skill_dir / "profiles"
            profiles_dest.mkdir(parents=True, exist_ok=True)
            for yaml_file in (REPO_ROOT / "config" / "profiles").glob("*.yaml"):
                shutil.copy2(yaml_file, profiles_dest / yaml_file.name)
                created.append(profiles_dest / yaml_file.name)

            gov_yaml = REPO_ROOT / "config" / "fpai_governance.yaml"
            if gov_yaml.exists():
                gov_dest = target_skill_dir / "fpai_governance.yaml"
                shutil.copy2(gov_yaml, gov_dest)
                created.append(gov_dest)
    else:
        created.append(target_skill_dir / "SKILL.md")

    return created


def _upsert_segmented_rule(src_file: Path, dest_file: Path, tool_key: str = "METRICSTHINKING") -> None:
    """Inserts or updates a segmented rule block non-destructively (Protocol v5.0)."""
    content = src_file.read_text(encoding="utf-8", errors="replace").strip()
    start_marker = f"<!-- >>> ICONTEXT-V5:{tool_key}:START >>> -->"
    end_marker = f"<!-- <<< ICONTEXT-V5:{tool_key}:END >>> -->"
    wrapped = f"{start_marker}\n{content}\n{end_marker}"
    if not dest_file.exists():
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        dest_file.write_text(wrapped + "\n", encoding="utf-8")
        return
    existing = dest_file.read_text(encoding="utf-8", errors="replace")
    if start_marker in existing and end_marker in existing:
        import re
        pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL)
        updated = pattern.sub(lambda _m: wrapped, existing)
    elif existing.strip() and existing.strip() != content:
        updated = existing.rstrip() + "\n\n" + wrapped + "\n"
    else:
        updated = wrapped + "\n"
    dest_file.write_text(updated, encoding="utf-8")


def install_claude(dest_root: Path, dry_run: bool = False) -> list[Path]:
    created = []
    print(f"[*] Installing Anthropic Claude Code Integration -> {dest_root}")
    src_claude_md = REPO_ROOT / "integrations" / "claude" / "CLAUDE.md"
    target_claude_md = dest_root / "CLAUDE.md"

    if src_claude_md.exists():
        if not dry_run:
            _upsert_segmented_rule(src_claude_md, target_claude_md, "METRICSTHINKING")
        created.append(target_claude_md)

    return created


def install_cursor(dest_root: Path, dry_run: bool = False) -> list[Path]:
    created = []
    target_dir = dest_root / ".cursor" / "rules"
    print(f"[*] Installing Cursor IDE Rule -> {target_dir}")
    src_mdc = REPO_ROOT / "integrations" / "cursor" / "metrics.mdc"
    target_mdc = target_dir / "metrics.mdc"

    if src_mdc.exists():
        if not dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_mdc, target_mdc)
        created.append(target_mdc)

    return created


def install_copilot(dest_root: Path, dry_run: bool = False) -> list[Path]:
    created = []
    target_dir = dest_root / ".github"
    print(f"[*] Installing GitHub Copilot Instructions -> {target_dir}")
    src_copilot = REPO_ROOT / "integrations" / "copilot" / "copilot-instructions.md"
    target_copilot = target_dir / "copilot-instructions.md"

    if src_copilot.exists():
        if not dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_copilot, target_copilot)
        created.append(target_copilot)

    return created


def install_mcp_config(dest_root: Path, dry_run: bool = False) -> list[Path]:
    print("[*] Generating Model Context Protocol (MCP) Configuration...")
    mcp_snippet = {
        "mcpServers": {
            "metricsthinking": {
                "command": "python",
                "args": ["-m", "metricsthinking.mcp_server"]
            }
        }
    }
    config_path = dest_root / "mcp_metricsthinking.json"
    if not dry_run:
        config_path.write_text(json.dumps(mcp_snippet, indent=2), encoding="utf-8")
    
    print(f"    [+] MCP configuration snippet saved to: {config_path}")
    print("    [+] You can copy this server block to Claude Desktop or Cursor MCP settings:")
    print(json.dumps(mcp_snippet, indent=2))
    return [config_path]


def run_installer(target: str = "all", dest: str = ".", is_global: bool = False, dry_run: bool = False):
    dest_path = Path(dest).resolve()
    print("=" * 70)
    print("  METRICSTHINKING™ MULTI-PROVIDER AI SKILL INSTALLER")
    print("=" * 70)
    print(f"  Target Provider: {target}")
    print(f"  Destination:     {dest_path}")
    print(f"  Global Mode:     {is_global}")
    print(f"  Dry Run:         {dry_run}")
    print("-" * 70)

    installed = []

    if target in ("all", "antigravity"):
        installed.extend(install_antigravity(dest_path, is_global=is_global, dry_run=dry_run))

    if target in ("all", "codex"):
        installed.extend(install_codex(dest_path, is_global=is_global, dry_run=dry_run))

    if target in ("all", "claude"):
        installed.extend(install_claude(dest_path, dry_run=dry_run))

    if target in ("all", "cursor"):
        installed.extend(install_cursor(dest_path, dry_run=dry_run))

    if target in ("all", "copilot"):
        installed.extend(install_copilot(dest_path, dry_run=dry_run))

    if target in ("all", "mcp"):
        installed.extend(install_mcp_config(dest_path, dry_run=dry_run))

    print("=" * 70)
    print(f"[+] Skill installation completed successfully ({len(installed)} artifacts deployed).")
    for item in installed:
        print(f"    - {item}")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="MetricsThinking™ Multi-Provider AI Skill Installer"
    )
    parser.add_argument(
        "--target", "-t",
        choices=["all", "antigravity", "codex", "claude", "cursor", "copilot", "mcp"],
        default="all",
        help="Target AI provider to install skill for (default: all)"
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Install skill for all supported AI providers (alias for --target all)"
    )
    parser.add_argument(
        "--dest", "-d",
        default=".",
        help="Target destination directory (default: current workspace)"
    )
    parser.add_argument(
        "--global", "-g",
        dest="is_global",
        action="store_true",
        help="Install globally into user profile (Google Antigravity global config)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate installation without writing files"
    )

    args = parser.parse_args()
    target_provider = "all" if args.all else args.target
    run_installer(
        target=target_provider,
        dest=args.dest,
        is_global=args.is_global,
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()
