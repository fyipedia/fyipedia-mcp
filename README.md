# fyipedia-mcp

Unified [MCP](https://modelcontextprotocol.io/) server for [FYIPedia](https://fyipedia.com) developer tools.

One server, 30+ tools from 10 packages.

## Install

```bash
pip install "fyipedia-mcp[all]"     # All tools
pip install "fyipedia-mcp[color,distance]"  # Specific packages
```

## Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "fyipedia": {
            "command": "python",
            "args": ["-m", "fyipedia_mcp.server"]
        }
    }
}
```

## Available Tool Packages

| Package | Tools | Description |
|---------|-------|-------------|
| colorfyi | 5+ | Color conversions, WCAG contrast, harmonies |
| emojifyi | 3+ | Emoji lookup, search, encoding |
| symbolfyi | 3+ | Symbol encoding, Unicode properties |
| unicodefyi | 3+ | Unicode character info, encoding |
| fontfyi | 3+ | Google Fonts metadata, CSS, pairing |
| distancefyi | 5 | Distance, bearing, midpoint, flight time |
| timefyi | 5 | Timezone ops, time diff, business hours |
| namefyi | 4 | Korean romanization, Five Elements |
| unitfyi | 4 | Unit conversion (220 units, 20 categories) |
| holidayfyi | 5 | Holiday dates, Easter, upcoming holidays |

## License

MIT
