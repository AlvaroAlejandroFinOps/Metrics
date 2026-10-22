"""Unit tests for MetricsThinking installer and MCP server."""
import json
from pathlib import Path

from scripts.install_skill import install_antigravity, install_claude, install_cursor, install_copilot, install_mcp_config, run_installer
from metricsthinking.mcp_server import handle_list_tools, handle_call_tool


def test_install_antigravity_local(tmp_path: Path):
    created = install_antigravity(dest_root=tmp_path, is_global=False, dry_run=False)
    assert len(created) > 0
    assert (tmp_path / ".agents" / "skills" / "metrics" / "SKILL.md").exists()


def test_install_claude(tmp_path: Path):
    created = install_claude(dest_root=tmp_path, dry_run=False)
    assert len(created) > 0
    assert (tmp_path / "CLAUDE.md").exists()


def test_install_cursor(tmp_path: Path):
    created = install_cursor(dest_root=tmp_path, dry_run=False)
    assert len(created) > 0
    assert (tmp_path / ".cursor" / "rules" / "metrics.mdc").exists()


def test_install_copilot(tmp_path: Path):
    created = install_copilot(dest_root=tmp_path, dry_run=False)
    assert len(created) > 0
    assert (tmp_path / ".github" / "copilot-instructions.md").exists()


def test_install_mcp_config(tmp_path: Path):
    created = install_mcp_config(dest_root=tmp_path, dry_run=False)
    assert len(created) > 0
    mcp_file = tmp_path / "mcp_metricsthinking.json"
    assert mcp_file.exists()
    content = json.loads(mcp_file.read_text(encoding="utf-8"))
    assert "metricsthinking" in content["mcpServers"]


def test_run_installer_all(tmp_path: Path):
    run_installer(target="all", dest=str(tmp_path), dry_run=False)
    assert (tmp_path / ".agents" / "skills" / "metrics" / "SKILL.md").exists()
    assert (tmp_path / "CLAUDE.md").exists()
    assert (tmp_path / ".cursor" / "rules" / "metrics.mdc").exists()
    assert (tmp_path / ".github" / "copilot-instructions.md").exists()
    assert (tmp_path / "mcp_metricsthinking.json").exists()


def test_mcp_server_tools(tmp_path: Path):
    tools = handle_list_tools()
    assert len(tools) >= 3
    tool_names = [t["name"] for t in tools]
    assert "audit_repository" in tool_names
    assert "list_profiles" in tool_names
    assert "get_audit_report" in tool_names

    # Test list_profiles
    profiles_res = handle_call_tool("list_profiles", {})
    assert len(profiles_res) > 0
    profiles_data = json.loads(profiles_res[0]["text"])
    assert "profiles" in profiles_data
