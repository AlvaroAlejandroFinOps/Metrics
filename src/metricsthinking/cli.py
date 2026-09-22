"""
CLI Interface for MetricsThinking™.
Command-line auditor, forensic reporter, MCP server, and AI skill installer.
"""

import argparse
import sys
from pathlib import Path

from .engine import run_audit


def main():
    parser = argparse.ArgumentParser(
        prog="metricsthinking",
        description="MetricsThinking™: Universal Project Evaluation Engine & Multi-Provider AI Skill"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # 1. audit subcommand
    audit_parser = subparsers.add_parser("audit", help="Run forensic audit on a repository")
    audit_parser.add_argument("--target", "-t", default=".", help="Path to project repository to audit")
    audit_parser.add_argument("--profile", "-p", default="default", help="Profile name (default, data-platform, web-app)")
    audit_parser.add_argument("--out-dir", "-o", default=None, help="Output directory for generated artifacts")
    audit_parser.add_argument("--prefix", default="MetricsThinking", help="Filename prefix for generated artifacts")
    audit_parser.add_argument("--quiet", "-q", action="store_true", help="Suppress console summary table")

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

    # Default fallback options on root parser for backwards compatibility
    parser.add_argument("--target", "-t", default=".", help="Path to project repository to audit")
    parser.add_argument("--profile", "-p", default="default", help="Profile name (default, data-platform, web-app)")
    parser.add_argument("--out-dir", "-o", default=None, help="Output directory for generated artifacts")
    parser.add_argument("--prefix", default="MetricsThinking", help="Filename prefix for generated artifacts")
    parser.add_argument("--quiet", "-q", action="store_true", help="Suppress console summary table")

    args = parser.parse_args()

    try:
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
                out_dir=args.out_dir,
                prefix=args.prefix,
                quiet=args.quiet
            )
    except Exception as e:
        print(f"[ERROR] MetricsThinking command failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
