"""
CLI Interface for MetricsThinking™.
Command-line auditor and forensic reporter.
"""

import argparse
import sys

from .engine import run_audit


def main():
    parser = argparse.ArgumentParser(
        prog="metricsthinking",
        description="MetricsThinking™: Universal Project Evaluation Engine & Forensic Auditor"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # audit subcommand
    audit_parser = subparsers.add_parser("audit", help="Run forensic audit on a repository")
    audit_parser.add_argument("--target", "-t", default=".", help="Path to project repository to audit")
    audit_parser.add_argument("--profile", "-p", default="default", help="Profile name (default, data-platform, web-app)")
    audit_parser.add_argument("--out-dir", "-o", default=None, help="Output directory for generated artifacts")
    audit_parser.add_argument("--prefix", default="MetricsThinking", help="Filename prefix for generated artifacts")
    audit_parser.add_argument("--quiet", "-q", action="store_true", help="Suppress console summary table")

    # Global options on root
    parser.add_argument("--target", "-t", default=".", help="Path to project repository to audit")
    parser.add_argument("--profile", "-p", default="default", help="Profile name (default, data-platform, web-app)")
    parser.add_argument("--out-dir", "-o", default=None, help="Output directory for generated artifacts")
    parser.add_argument("--prefix", default="MetricsThinking", help="Filename prefix for generated artifacts")
    parser.add_argument("--quiet", "-q", action="store_true", help="Suppress console summary table")

    args = parser.parse_args()

    try:
        run_audit(
            target_path=args.target,
            profile_name=args.profile,
            out_dir=args.out_dir,
            prefix=args.prefix,
            quiet=args.quiet
        )
    except Exception as e:
        print(f"[ERROR] MetricsThinking audit failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
