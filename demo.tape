# fyipedia-mcp — Unified MCP Server Demo
Output demo.gif

Set FontSize 20
Set Width 1000
Set Height 580
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 30ms
Set Padding 24

Type "uv run --with fyipedia-mcp python3"
Enter
Sleep 2.5s

Type "import fyipedia_mcp; print('fyipedia-mcp', fyipedia_mcp.__version__)"
Enter
Sleep 1.5s

Type "from fyipedia_mcp.server import mcp, _collect_tools"
Enter
Sleep 1s

Type "tools = _collect_tools(); print(len(tools), 'MCP tools available')"
Enter
Sleep 2s

Type "exit()"
Enter
Sleep 1s
