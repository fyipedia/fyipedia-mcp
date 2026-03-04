"""Unified MCP server that aggregates tools from all FYIPedia packages.

Only tools from installed packages are registered. Install individual packages
to enable their tools::

    pip install "fyipedia-mcp[all]"       # All tools
    pip install "fyipedia-mcp[color]"     # Just color tools

Configure in claude_desktop_config.json::

    {
        "mcpServers": {
            "fyipedia": {
                "command": "python",
                "args": ["-m", "fyipedia_mcp.server"]
            }
        }
    }
"""

from __future__ import annotations

import logging
from importlib import import_module
from typing import Any

from mcp.server.fastmcp import FastMCP

logger = logging.getLogger(__name__)

mcp = FastMCP("fyipedia")

# Each package's MCP server module path.
# Tools are imported from these modules and re-registered on the hub server.
_MCP_MODULES: list[tuple[str, str]] = [
    ("colorfyi", "colorfyi.mcp_server"),
    ("emojifyi", "emojifyi.mcp_server"),
    ("symbolfyi", "symbolfyi.mcp_server"),
    ("unicodefyi", "unicodefyi.mcp_server"),
    ("fontfyi", "fontfyi.mcp_server"),
    ("distancefyi", "distancefyi.mcp_server"),
    ("timefyi", "timefyi.mcp_server"),
    ("namefyi", "namefyi.mcp_server"),
    ("unitfyi", "unitfyi.mcp_server"),
    ("holidayfyi", "holidayfyi.mcp_server"),
]


def _collect_tools() -> list[str]:
    """Import MCP modules and re-register their tools on the hub server.

    Each package defines a FastMCP instance with @mcp.tool() decorated functions.
    We import the module, find callable tool functions, and register them on our hub.
    """
    registered: list[str] = []

    for pkg_name, module_path in _MCP_MODULES:
        try:
            mod = import_module(module_path)
        except ImportError:
            logger.debug("Skipping %s (not installed)", pkg_name)
            continue

        # Find the package's FastMCP instance to get its registered tools
        pkg_mcp: FastMCP | None = getattr(mod, "mcp", None)
        if pkg_mcp is None:
            logger.debug("No mcp instance found in %s", module_path)
            continue

        # Re-register each tool function on the hub
        for tool_name, tool_obj in _get_tools(pkg_mcp):
            fn = tool_obj.fn
            # Prefix tool name with package name to avoid collisions
            prefixed_name = f"{pkg_name}_{tool_name}"
            mcp.tool(name=prefixed_name)(fn)
            registered.append(prefixed_name)

    return registered


def _get_tools(server: FastMCP) -> list[tuple[str, Any]]:
    """Extract registered tools from a FastMCP server instance."""
    tools: list[tuple[str, Any]] = []
    # FastMCP stores tools in _tool_manager._tools dict
    tool_manager = getattr(server, "_tool_manager", None)
    if tool_manager is None:
        return tools
    tool_dict: dict[str, Any] = getattr(tool_manager, "_tools", {})
    for name, tool in tool_dict.items():
        tools.append((name, tool))
    return tools


# Register all discovered tools at import time
_registered = _collect_tools()


def main() -> None:
    """Run the unified MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
