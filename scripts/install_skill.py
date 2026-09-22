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
        if src_skill_md.exists():
            shutil.copy2(src_skill_md, target_skill_dir / "SKILL.md")
            created.append(target_skill_dir / "SKILL.md")

        # Copy scripts if global install
        if is_global:
            scripts_dest = target_skill_dir / "scripts"
            scripts_dest.mkdir(parents=True, exist_ok=True)
            for py_file in (REPO_ROOT / "src" / "metricsthinking").glob("*.py"):
                shutil.copy2(py_file, scripts_dest / py_file.name)
                created.append(scripts_dest / py_file.name)
            
            profiles_dest = target_skill_dir / "profiles"
            profiles_dest.mkdir(parents=True, exist_ok=True)
            for yaml_file in (REPO_ROOT / "config" / "profiles").glob("*.yaml"):
                shutil.copy2(yaml_file, profiles_dest / yaml_file.name)
                created.append(profiles_dest / yaml_file.name)
    else:
        created.append(target_skill_dir / "SKILL.md")

    return created


def install_claude(dest_root: Path, dry_run: bool = False) -> list[Path]:
    created = []
    print(f"[*] Installing Anthropic Claude Code Integration -> {dest_root}")
    src_claude_md = REPO_ROOT / "integrations" / "claude" / "CLAUDE.md"
    target_claude_md = dest_root / "CLAUDE.md"

    if src_claude_md.exists():
        if not dry_run:
            shutil.copy2(src_claude_md, target_claude_md)
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
        choices=["all", "antigravity", "claude", "cursor", "copilot", "mcp"],
        default="all",
        help="Target AI provider to install skill for (default: all)"
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
    run_installer(
        target=args.target,
        dest=args.dest,
        is_global=args.is_global,
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()
