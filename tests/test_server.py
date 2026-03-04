"""Tests for the fyipedia MCP hub server."""

from fyipedia_mcp.server import _MCP_MODULES, _registered, mcp


def test_mcp_instance_exists() -> None:
    """Hub MCP server is created."""
    assert mcp is not None
    assert mcp.name == "fyipedia"


def test_mcp_modules_list() -> None:
    """Should have 10 package modules registered."""
    assert len(_MCP_MODULES) == 10


def test_registered_tools_is_list() -> None:
    """Registered tools should be a list (may be empty if no packages installed)."""
    assert isinstance(_registered, list)


def test_no_duplicate_tool_names() -> None:
    """All registered tool names should be unique."""
    assert len(_registered) == len(set(_registered))
