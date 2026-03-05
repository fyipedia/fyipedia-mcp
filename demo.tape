# fyipedia-mcp — Unified MCP Server Demo
Output demo.gif

Set FontSize 14
Set Width 920
Set Height 620
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 35ms
Set Padding 20

Type `python -c "import fyipedia_mcp; print('fyipedia-mcp', fyipedia_mcp.__version__)"`
Enter
Sleep 2s

Type `echo '{"mcpServers":{"fyipedia":{"command":"uvx","args":["fyipedia-mcp"]}}}' | jq .`
Enter
Sleep 2s

Type `python -c "from fyipedia_mcp.server import mcp, _collect_tools; tools=_collect_tools(); print(len(tools),'MCP tools:'); [print(f'  {t}') for t in sorted(tools)[:12]]; print('  ...')"`
Enter
Sleep 3s

Sleep 2s
