# fyipedia-mcp

[![PyPI](https://img.shields.io/pypi/v/fyipedia-mcp)](https://pypi.org/project/fyipedia-mcp/)
[![Python](https://img.shields.io/pypi/pyversions/fyipedia-mcp)](https://pypi.org/project/fyipedia-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Unified [MCP](https://modelcontextprotocol.io/) server for the [FYIPedia](https://github.com/fyipedia) developer tools ecosystem. One server gives AI assistants access to 53 tools from 10 packages -- [color conversion](https://colorfyi.com/), [emoji metadata](https://emojifyi.com/), [symbol encoding](https://symbolfyi.com/), [Unicode lookup](https://unicodefyi.com/), [Google Fonts](https://fontfyi.com/), [distance calculation](https://distancefyi.com/), [timezone operations](https://timefyi.com/), [Korean romanization](https://namefyi.com/), [unit conversion](https://unitfyi.com/), and [holiday dates](https://holidayfyi.com/).

> **One config, 53 tools.** Works with [Claude Desktop](https://claude.ai/download), [Cursor](https://cursor.com/), [Windsurf](https://codeium.com/windsurf), [Continue](https://continue.dev/), and any [MCP-compatible](https://modelcontextprotocol.io/) client. Each package is loaded lazily -- only installed packages register their tools.

## Install

```bash
pip install "fyipedia-mcp[all]"              # All 53 tools from 10 packages
pip install "fyipedia-mcp[color,distance]"   # Just color + distance (14 tools)
pip install "fyipedia-mcp[color,emoji,font]" # Pick any combination
pip install fyipedia-mcp                     # Core only (no tools)
```

Requires Python 3.10+. Each package is an optional dependency.

## Integration Guides

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%/Claude/claude_desktop_config.json` (Windows):

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

Restart Claude Desktop. You should see 53 tools available under "fyipedia".

### Cursor

Add to `.cursor/mcp.json` in your project root:

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

### Windsurf

Add to `~/.codeium/windsurf/mcp_config.json`:

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

### Claude Code

Add to `~/.claude/settings.json`:

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

### Standalone

Run the server directly for testing:

```bash
python -m fyipedia_mcp.server
```

## Available Tools (53 total)

### Color Tools (9 tools) -- `colorfyi`

| Tool | Parameters | Description |
|------|-----------|-------------|
| `colorfyi_color_info` | `hex_code` | Convert hex to 7 color spaces (RGB, HSL, HSV, CMYK, Lab, OKLCH) |
| `colorfyi_contrast_check` | `fg`, `bg` | WCAG 2.1 contrast ratio with AA/AAA compliance checks |
| `colorfyi_color_harmonies` | `hex_code` | 5 harmony types (complementary, analogous, triadic, split-comp, tetradic) |
| `colorfyi_color_shades` | `hex_code` | Tailwind-style shade palette (50-950 scale) |
| `colorfyi_simulate_color_blindness` | `hex_code` | Protanopia, deuteranopia, tritanopia, achromatopsia simulation |
| `colorfyi_mix_colors` | `hex1`, `hex2`, `ratio?` | Mix two colors in perceptual Lab space |
| `colorfyi_compare_colors` | `hex1`, `hex2` | Delta E comparison, contrast ratio, gradient |
| `colorfyi_gradient` | `hex1`, `hex2`, `steps?` | Smooth perceptual gradient steps |
| `colorfyi_text_color_for_background` | `hex_code` | Best text color (black or white) for any background |

### Emoji Tools (7 tools) -- `emojifyi`

| Tool | Parameters | Description |
|------|-----------|-------------|
| `emojifyi_emoji_lookup` | `slug` | Full emoji metadata (character, codepoint, category, Unicode version, skin tones) |
| `emojifyi_emoji_by_char` | `character` | Reverse lookup -- find emoji info from character |
| `emojifyi_emoji_search` | `query`, `limit?` | Search 3,953 emojis by keyword |
| `emojifyi_emoji_encode` | `character` | 8 encodings (UTF-8, UTF-16, HTML decimal/hex, CSS, Python, JS, Java) |
| `emojifyi_emoji_categories` | -- | All 10 emoji categories with icons and counts |
| `emojifyi_emoji_by_category` | `category_slug`, `limit?` | Browse emojis within a category |
| `emojifyi_emoji_stats` | -- | Dataset statistics (total emojis, ZWJ sequences, skin tone variants) |

### Symbol Tools (3 tools) -- `symbolfyi`

| Tool | Parameters | Description |
|------|-----------|-------------|
| `symbolfyi_symbol_info` | `character` | Full Unicode properties (name, block, script, bidi, combining) + 11 encodings |
| `symbolfyi_symbol_encode` | `character` | 11 formats (Unicode, HTML decimal/hex/entity, CSS, JS, Python, Java, UTF-8/16, URL) |
| `symbolfyi_html_entity_lookup` | `entity` | Reverse HTML entity lookup (e.g., `&hearts;` to character) |

### Unicode Tools (4 tools) -- `unicodefyi`

| Tool | Parameters | Description |
|------|-----------|-------------|
| `unicodefyi_char_info` | `codepoint_or_char` | Full Unicode info (accepts U+hex, character, or hex codepoint) |
| `unicodefyi_char_encode` | `codepoint_or_char` | 17 encodings (HTML, CSS, JS, Python, Go, Ruby, Rust, C/C++, URL, UTF-8/16/32) |
| `unicodefyi_unicode_search` | `query`, `limit?` | Search characters by name substring |
| `unicodefyi_html_entity_lookup` | `entity` | HTML entity lookup (e.g., `&amp;` to ampersand) |

### Font Tools (6 tools) -- `fontfyi`

| Tool | Parameters | Description |
|------|-----------|-------------|
| `fontfyi_font_info` | `slug` | Google Font metadata (family, category, weights, subsets, designer, rank) |
| `fontfyi_font_search` | `query`, `limit?` | Search Google Fonts by name |
| `fontfyi_font_css` | `slug` | CSS import snippet + font-family declaration |
| `fontfyi_font_pairings` | `slug` | Font pairing recommendations with mood and use cases |
| `fontfyi_font_stacks` | -- | 10 CSS font stack presets for common use cases |
| `fontfyi_popular_fonts` | `limit?` | Most popular Google Fonts by rank |

### Distance Tools (5 tools) -- `distancefyi`

| Tool | Parameters | Description |
|------|-----------|-------------|
| `distancefyi_calculate_distance` | `lat1`, `lon1`, `lat2`, `lon2`, `same_continent?` | Full distance report (km/miles/NM), bearing, midpoint, travel times |
| `distancefyi_get_bearing` | `lat1`, `lon1`, `lat2`, `lon2` | Bearing degrees + compass direction (N, NE, E, etc.) |
| `distancefyi_get_midpoint` | `lat1`, `lon1`, `lat2`, `lon2` | Geographic midpoint coordinates |
| `distancefyi_get_flight_time` | `distance_km` | Estimated flight time (variable speed 600-850 km/h) |
| `distancefyi_convert_distance` | `value`, `from_unit`, `to_unit` | Distance conversion between km, miles, nautical miles |

### Time Tools (5 tools) -- `timefyi`

| Tool | Parameters | Description |
|------|-----------|-------------|
| `timefyi_current_time` | `timezone_id` | Current time in IANA timezone (with UTC offset, DST status) |
| `timefyi_time_difference` | `from_tz`, `to_tz` | Time difference between two timezones |
| `timefyi_convert_time` | `time_str`, `from_tz`, `to_tz` | Convert specific time across timezones |
| `timefyi_business_hours_overlap` | `timezones`, `start_hour?`, `end_hour?` | Find overlapping business hours across timezones |
| `timefyi_sun_info` | `latitude`, `longitude`, `timezone_id` | Sunrise, sunset, day length, current daylight status |

### Unit Tools (4 tools) -- `unitfyi`

| Tool | Parameters | Description |
|------|-----------|-------------|
| `unitfyi_convert_unit` | `value`, `from_unit`, `to_unit` | Convert between 220 units in 20 categories with Decimal precision |
| `unitfyi_conversion_table` | `from_unit`, `to_unit` | Markdown table with common conversion values |
| `unitfyi_list_categories` | -- | All 20 measurement categories (length, weight, temperature, volume, etc.) |
| `unitfyi_list_units` | `category` | All units in a category with slug, name, and symbol |

### Name Tools (4 tools) -- `namefyi`

| Tool | Parameters | Description |
|------|-----------|-------------|
| `namefyi_romanize_korean` | `hangul` | Revised Romanization of Korean text |
| `namefyi_five_elements` | `stroke_count` | Five Elements category (Wood/Fire/Earth/Metal/Water) for CJK stroke count |
| `namefyi_element_compatibility` | `element_a`, `element_b` | Compatibility between two Five Elements (compatible/neutral/incompatible) |
| `namefyi_format_population` | `population` | Format large numbers with M/K suffixes |

### Holiday Tools (5 tools) -- `holidayfyi`

| Tool | Parameters | Description |
|------|-----------|-------------|
| `holidayfyi_upcoming_holidays` | `country_iso`, `n?` | Next N public holidays for ISO country code |
| `holidayfyi_check_holidays_on_date` | `date_str`, `countries` | Check holidays on a specific date across multiple countries |
| `holidayfyi_easter_date` | `year`, `orthodox?` | Western or Orthodox Easter date for any year |
| `holidayfyi_nth_weekday` | `year`, `month`, `weekday`, `n` | Find nth occurrence of weekday in a month (e.g., 4th Thursday) |
| `holidayfyi_count_days_until` | `target_date_str`, `from_date_str?` | Days countdown to a target date |

## Architecture

FYIPedia MCP uses a **hub aggregation pattern**. Each package has its own standalone MCP server. The hub collects all tools into a single server:

```
fyipedia-mcp (hub server)
│
├── colorfyi.mcp_server     →  9 tools prefixed with colorfyi_
├── emojifyi.mcp_server     →  7 tools prefixed with emojifyi_
├── symbolfyi.mcp_server    →  3 tools prefixed with symbolfyi_
├── unicodefyi.mcp_server   →  4 tools prefixed with unicodefyi_
├── fontfyi.mcp_server      →  6 tools prefixed with fontfyi_
├── distancefyi.mcp_server  →  5 tools prefixed with distancefyi_
├── timefyi.mcp_server      →  5 tools prefixed with timefyi_
├── namefyi.mcp_server      →  4 tools prefixed with namefyi_
├── unitfyi.mcp_server      →  4 tools prefixed with unitfyi_
└── holidayfyi.mcp_server   →  5 tools prefixed with holidayfyi_
                               ──
                               52 tools total
```

**How it works:**

1. Hub defines a catalog of 10 `(package_name, module_path)` entries
2. At startup, `importlib.import_module()` loads each package's MCP module
3. Tools are extracted from each package's `FastMCP._tool_manager._tools`
4. Each tool is re-registered on the hub with a `{package}_` prefix to avoid collisions
5. Missing packages are silently skipped -- partial installation works fine

**Why a hub?** Instead of configuring 10 separate MCP servers, you configure one. AI assistants see all tools in a single namespace. Install only the packages you need, and only those tools appear.

**Standalone mode** -- each package can also run its own MCP server independently:

```json
{
    "mcpServers": {
        "colorfyi": {
            "command": "python",
            "args": ["-m", "colorfyi.mcp_server"]
        }
    }
}
```

## Features

- **53 tools from 10 packages**: Color, emoji, symbol, Unicode, font, distance, time, name, unit, holiday
- **One config**: Single MCP server entry instead of 10 separate configurations
- **Lazy loading**: Only installed packages register their tools -- no bloat
- **Flexible installation**: Install all tools or pick specific packages
- **Tool name prefixing**: Automatic `{package}_` prefix prevents collisions
- **Graceful degradation**: Missing packages are silently skipped
- **MCP v1.0 compatible**: Works with any MCP client (Claude, Cursor, Windsurf, Continue, etc.)
- **Markdown responses**: All tools return formatted markdown for readable AI output
- **Type-safe**: Full type annotations, strict mypy, PEP 561 compliant
- **Zero lock-in**: Each package's MCP server also works standalone

## Also Available as CLI

Use all 10 tools from the terminal via the [unified CLI](https://github.com/fyipedia/fyipedia):

```bash
pip install "fyipedia[all]"
fyi color info FF6B35
fyi distance calc --lat1 37.57 --lon1 126.98 --lat2 35.68 --lon2 139.65
```

See the [fyipedia README](https://github.com/fyipedia/fyipedia) for the full command reference.

## FYIPedia Developer Tools

Part of the [FYIPedia](https://github.com/fyipedia) open-source developer tools ecosystem:

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| [colorfyi](https://colorfyi.com/) | [`colorfyi`](https://pypi.org/project/colorfyi/) | [`@fyipedia/colorfyi`](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies, 809 named colors |
| [emojifyi](https://emojifyi.com/) | [`emojifyi`](https://pypi.org/project/emojifyi/) | [`emojifyi`](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 Unicode emojis |
| [symbolfyi](https://symbolfyi.com/) | [`symbolfyi`](https://pypi.org/project/symbolfyi/) | [`symbolfyi`](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats + Unicode properties |
| [unicodefyi](https://unicodefyi.com/) | [`unicodefyi`](https://pypi.org/project/unicodefyi/) | [`unicodefyi`](https://www.npmjs.com/package/unicodefyi) | Unicode character lookup, 17 encodings + search |
| [fontfyi](https://fontfyi.com/) | [`fontfyi`](https://pypi.org/project/fontfyi/) | [`fontfyi`](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata, CSS helpers, font pairings |
| [distancefyi](https://distancefyi.com/) | [`distancefyi`](https://pypi.org/project/distancefyi/) | [`distancefyi`](https://www.npmjs.com/package/distancefyi) | Haversine distance, bearing, travel times |
| [timefyi](https://timefyi.com/) | [`timefyi`](https://pypi.org/project/timefyi/) | [`timefyi`](https://www.npmjs.com/package/timefyi) | Timezone operations, time differences, sunrise/sunset |
| [namefyi](https://namefyi.com/) | [`namefyi`](https://pypi.org/project/namefyi/) | [`namefyi`](https://www.npmjs.com/package/namefyi) | Korean romanization, Five Elements, CJK stroke count |
| [unitfyi](https://unitfyi.com/) | [`unitfyi`](https://pypi.org/project/unitfyi/) | [`unitfyi`](https://www.npmjs.com/package/unitfyi) | Unit conversion, 220 units, 20 categories |
| [holidayfyi](https://holidayfyi.com/) | [`holidayfyi`](https://pypi.org/project/holidayfyi/) | [`holidayfyi`](https://www.npmjs.com/package/holidayfyi) | Holiday dates, Easter calculation, 100+ countries |
| [fyipedia](https://github.com/fyipedia/fyipedia) | [`fyipedia`](https://pypi.org/project/fyipedia/) | -- | Unified CLI (`fyi` command) for all 10 tools |
| **fyipedia-mcp** | [`fyipedia-mcp`](https://pypi.org/project/fyipedia-mcp/) | -- | Unified MCP server for AI assistants |

## Links

- [Model Context Protocol](https://modelcontextprotocol.io/) -- MCP specification
- [FYIPedia GitHub Organization](https://github.com/fyipedia) -- All repositories
- [fyipedia CLI](https://github.com/fyipedia/fyipedia) -- Terminal interface for all 10 tools
- [awesome-fyi](https://github.com/fyipedia/awesome-fyi) -- Curated list of FYIPedia resources
- [Source Code](https://github.com/fyipedia/fyipedia-mcp) -- MIT licensed

## License

MIT
