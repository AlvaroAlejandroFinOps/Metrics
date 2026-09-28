"""
CLI Interface for MetricsThinking™.
Command-line auditor, forensic reporter, MCP server, and AI skill installer.
"""

import argparse
import sys
from pathlib import Path

import yaml

# Ensure local directory is in sys.path for standalone script execution
_PKG_DIR = Path(__file__).resolve().parent
if str(_PKG_DIR) not in sys.path:
    sys.path.insert(0, str(_PKG_DIR))

try:
    from metricsthinking.engine import run_audit
except (ImportError, ValueError):
    try:
        from .engine import run_audit
    except (ImportError, ValueError):
        from engine import run_audit


def list_available_profiles() -> None:
    """Lists all available evaluation profiles with descriptions."""
    pkg_dir = Path(__file__).resolve().parent
    repo_root = pkg_dir.parent.parent
    profiles_dir = None
    for cand in [repo_root / "config" / "profiles", Path.cwd() / "config" / "profiles", pkg_dir / "profiles"]:
        if cand.exists():
            profiles_dir = cand
            break

    print("\n" + "=" * 75)
    print("  METRICSTHINKING™ v3.0 UNIVERSAL PROFILES & ARCHETYPES")
    print("=" * 75)

    if not profiles_dir or not profiles_dir.exists():
        print("  No profiles directory found.")
        return

    for p_file in sorted(profiles_dir.glob("*.yaml")):
        try:
            with open(p_file, encoding="utf-8") as f:
                data = yaml.safe_load(f)
            p_name = data.get("name", p_file.stem)
            p_desc = data.get("description", "No description provided.")
            p_arch = data.get("domain_archetype", "generic")
            p_mode = data.get("inspection_mode", "source_code")
            print(f"  • {p_name:<18} [{p_arch}] ({p_mode})")
            print(f"    {p_desc}")
            print()
        except Exception:
            pass
    print("=" * 75)


def main():
    parser = argparse.ArgumentParser(
        prog="metricsthinking",
        description="MetricsThinking™ v3.0: Universal Project Evaluation Engine & Multi-Provider AI Skill"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # 1. audit subcommand
    audit_parser = subparsers.add_parser("audit", help="Run forensic audit on a repository")
    audit_parser.add_argument("--target", "-t", default=".", help="Path to project repository to audit")
    audit_parser.add_argument("--profile", "-p", default="default", help="Profile name (e.g. default, mlops, llmops, dataops, gitops, platform-eng, devsecops, dual-track, team-topologies, chaos-eng, sdd)")
    audit_parser.add_argument("--archetype", "-a", default=None, help="Engineering archetype override")
    audit_parser.add_argument("--out-dir", "-o", default=None, help="Output directory for generated artifacts")
    audit_parser.add_argument("--prefix", default="MetricsThinking", help="Filename prefix for generated artifacts")
    audit_parser.add_argument("--quiet", "-q", action="store_true", help="Suppress console summary table")
    audit_parser.add_argument("--list-profiles", action="store_true", help="List all available profiles and exit")

    # 2. install-skill subcommand
    install_parser = subparsers.add_parser("install-skill", help="Install MetricsThinking™ skill for AI assistants")
    install_parser.add_argument(
        "--target", "-t",
        choices=["all", "antigravity", "claude", "cursor", "copilot", "mcp"],
        default="all",
        help="Target AI assistant / platform (default: all)"
    )
    install_parser.add_argument(
        "--dest", "-d",
        default=".",
        help="Destination directory (default: current directory)"
    )
    install_parser.add_argument(
        "--global", "-g",
        dest="is_global",
        action="store_true",
        help="Install globally into user profile (Google Antigravity global config)"
    )
    install_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files"
    )

    # 3. mcp subcommand
    mcp_parser = subparsers.add_parser("mcp", help="Start Model Context Protocol (MCP) JSON-RPC stdio server")

    # 4. list-profiles subcommand
    subparsers.add_parser("list-profiles", help="List all available evaluation profiles and archetypes")

    # Default fallback options on root parser for backwards compatibility
    parser.add_argument("--target", "-t", default=".", help="Path to project repository to audit")
    parser.add_argument("--profile", "-p", default="default", help="Profile name")
    parser.add_argument("--archetype", "-a", default=None, help="Engineering archetype override")
    parser.add_argument("--out-dir", "-o", default=None, help="Output directory for generated artifacts")
    parser.add_argument("--prefix", default="MetricsThinking", help="Filename prefix for generated artifacts")
    parser.add_argument("--quiet", "-q", action="store_true", help="Suppress console summary table")
    parser.add_argument("--list-profiles", action="store_true", help="List all available profiles and exit")

    args = parser.parse_args()

    try:
        if getattr(args, "list_profiles", False) or args.command == "list-profiles":
            list_available_profiles()
            return

        if args.command == "install-skill":
            # Import installer logic
            script_installer = Path(__file__).resolve().parent.parent.parent / "scripts" / "install_skill.py"
            if script_installer.exists():
                import importlib.util
                spec = importlib.util.spec_from_file_location("installer", script_installer)
                installer_mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(installer_mod)
                installer_mod.run_installer(
                    target=args.target,
                    dest=args.dest,
                    is_global=args.is_global,
                    dry_run=args.dry_run
                )
            else:
                print("[ERROR] Installer script not found.", file=sys.stderr)
                sys.exit(1)

        elif args.command == "mcp":
            from .mcp_server import run_mcp_server
            run_mcp_server()

        else:
            # Default to audit
            run_audit(
                target_path=args.target,
                profile_name=args.profile,
                archetype=getattr(args, "archetype", None),
                out_dir=args.out_dir,
                prefix=args.prefix,
                quiet=args.quiet
            )
    except Exception as e:
        print(f"[ERROR] MetricsThinking command failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

