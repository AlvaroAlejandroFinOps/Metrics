"""
Model Context Protocol (MCP) Server for MetricsThinking™.
Enables any MCP-compliant AI client (Claude Desktop, Cursor, Zed, Continue, Antigravity)
to execute forensic repository audits and retrieve maturity metrics via stdio JSON-RPC.
"""

import json
import sys
from pathlib import Path
from typing import Any

from .engine import run_audit


TOOLS = [
    {
        "name": "audit_repository",
        "description": "Execute a full MetricsThinking™ Ground Truth forensic audit on a repository, calculating maturity score (0-100%), identifying active bottlenecks, and generating Markdown, JSON, and Roadmap artifacts.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Absolute or relative path to the repository to audit.",
                    "default": "."
                },
                "profile": {
                    "type": "string",
                    "description": "Domain profile to use (default, data-platform, web-app).",
                    "default": "default"
                },
                "out_dir": {
                    "type": "string",
                    "description": "Optional custom output directory for artifacts (defaults to <target>/artifacts).",
                }
            },
            "required": []
        }
    },
    {
        "name": "list_profiles",
        "description": "List all available MetricsThinking™ evaluation profiles.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "get_audit_report",
        "description": "Retrieve the latest MetricsThinking™ JSON report or Markdown summary for a project.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "target": {
                    "type": "string",
                    "description": "Target repository path.",
                    "default": "."
                },
                "format": {
                    "type": "string",
                    "enum": ["markdown", "json", "roadmap"],
                    "default": "markdown",
                    "description": "Report format to retrieve."
                }
            }
        }
    }
]


def handle_list_tools() -> list[dict[str, Any]]:
    return TOOLS


def handle_call_tool(name: str, arguments: dict[str, Any]) -> list[dict[str, Any]]:
    if name == "audit_repository":
        target = arguments.get("target", ".")
        profile = arguments.get("profile", "default")
        out_dir = arguments.get("out_dir")
        
        report, artifacts = run_audit(
            target_path=target,
            profile_name=profile,
            out_dir=out_dir,
            quiet=True
        )
        
        summary = (
            f"Audit completed successfully for {report.project_name}.\n"
            f"- Consolidated Score: {report.consolidated_score:.2f}%\n"
            f"- Maturity Band: {report.maturity_band.value}\n"
            f"- Active Bottleneck: {report.active_bottleneck}\n"
            f"- Artifacts generated:\n"
            f"  * Markdown Report: {artifacts['markdown']}\n"
            f"  * JSON Telemetry:  {artifacts['json']}\n"
            f"  * Inferred Roadmap: {artifacts['roadmap']}"
        )
        return [{"type": "text", "text": summary}]

    elif name == "list_profiles":
        # Look for profiles in target or package config
        pkg_dir = Path(__file__).resolve().parent
        repo_root = pkg_dir.parent.parent
        profiles_dir = repo_root / "config" / "profiles"
        profiles = ["default", "data-platform", "web-app"]
        if profiles_dir.exists():
            profiles = [p.stem for p in profiles_dir.glob("*.yaml")]
        return [{"type": "text", "text": json.dumps({"profiles": profiles}, indent=2)}]

    elif name == "get_audit_report":
        target = Path(arguments.get("target", ".")).resolve()
        fmt = arguments.get("format", "markdown")
        
        if fmt == "json":
            file_path = target / "artifacts" / "MetricsThinking.json"
        elif fmt == "roadmap":
            file_path = target / "artifacts" / "plans" / "active" / "INFERRED_ROADMAP.md"
        else:
            file_path = target / "artifacts" / "MetricsThinking.md"

        if not file_path.exists():
            return [{"type": "text", "text": f"Error: Report file '{file_path}' not found. Run audit_repository first."}]

        return [{"type": "text", "text": file_path.read_text(encoding="utf-8")}]

    else:
        raise ValueError(f"Unknown tool: {name}")


def run_mcp_server():
    """Runs the stdio JSON-RPC server loop."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
            req_id = request.get("id")
            method = request.get("method")
            params = request.get("params", {})

            if method == "initialize":
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "serverInfo": {
                            "name": "metricsthinking-mcp",
                            "version": "2.0.0"
                        },
                        "capabilities": {
                            "tools": {}
                        }
                    }
                }
            elif method == "tools/list":
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": handle_list_tools()
                    }
                }
            elif method == "tools/call":
                name = params.get("name")
                arguments = params.get("arguments", {})
                content = handle_call_tool(name, arguments)
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": content
                    }
                }
            elif method == "notifications/initialized":
                continue
            else:
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {
                        "code": -32601,
                        "message": f"Method '{method}' not found"
                    }
                }

            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0",
                "id": request.get("id") if 'request' in locals() and isinstance(request, dict) else None,
                "error": {
                    "code": -32603,
                    "message": str(e)
                }
            }
            sys.stdout.write(json.dumps(error_response) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    run_mcp_server()
