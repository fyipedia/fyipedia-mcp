---
name: fyipedia-mcp
description: Unified MCP server exposing 53 developer tools from 10 FYI packages to AI assistants. Use when you need to add color conversion, emoji lookup, symbol encoding, Unicode search, Google Fonts, distance calculation, timezone operations, unit conversion, Korean romanization, or holiday date tools to an MCP-compatible AI client.
license: MIT
metadata:
  author: fyipedia
  version: "0.1.1"
  homepage: "https://fyipedia.com/"
---

# FYIPedia MCP -- Developer Tools for AI Assistants

One MCP server gives AI assistants access to 53 tools from 10 packages -- color conversion, emoji metadata, symbol encoding, Unicode lookup, Google Fonts, distance calculation, timezone operations, unit conversion, Korean romanization, and holiday dates.

**Install**: `pip install "fyipedia-mcp[all]"` · **PyPI**: [fyipedia-mcp](https://pypi.org/project/fyipedia-mcp/) · **CLI**: [fyipedia](https://pypi.org/project/fyipedia/)

## When to Use

- You need to add developer reference tools to Claude Desktop, Cursor, Windsurf, or Claude Code
- You want one MCP server config instead of 10 separate server entries
- You need color, emoji, Unicode, font, distance, time, unit, name, or holiday tools available to AI assistants
- You want lazy-loading -- only installed packages register their tools

## Install

```bash
pip install "fyipedia-mcp[all]"              # All 53 tools from 10 packages
pip install "fyipedia-mcp[color,distance]"   # Just color + distance (14 tools)
pip install "fyipedia-mcp[color,emoji,font]" # Pick any combination
pip install fyipedia-mcp                     # Core only (no tools)
```

Requires Python 3.10+.

## Integration

Add to your MCP client config:

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

| Client | Config File |
|--------|-------------|
| Claude Desktop (macOS) | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Claude Desktop (Windows) | `%APPDATA%/Claude/claude_desktop_config.json` |
| Cursor | `.cursor/mcp.json` (project root) |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` |
| Claude Code | `~/.claude/settings.json` |

## Tools (53 total)

### Color Tools (9 tools) -- colorfyi

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

### Emoji Tools (7 tools) -- emojifyi

| Tool | Parameters | Description |
|------|-----------|-------------|
| `emojifyi_emoji_lookup` | `slug` | Full emoji metadata (character, codepoint, category, version, skin tones) |
| `emojifyi_emoji_by_char` | `character` | Reverse lookup -- find emoji info from character |
| `emojifyi_emoji_search` | `query`, `limit?` | Search 3,953 emojis by keyword |
| `emojifyi_emoji_encode` | `character` | 8 encodings (UTF-8, UTF-16, HTML, CSS, Python, JS, Java) |
| `emojifyi_emoji_categories` | -- | All 10 emoji categories with icons and counts |
| `emojifyi_emoji_by_category` | `category_slug`, `limit?` | Browse emojis within a category |
| `emojifyi_emoji_stats` | -- | Dataset statistics (total emojis, ZWJ sequences, skin tone variants) |

### Symbol Tools (3 tools) -- symbolfyi

| Tool | Parameters | Description |
|------|-----------|-------------|
| `symbolfyi_symbol_info` | `character` | Full Unicode properties + 11 encodings |
| `symbolfyi_symbol_encode` | `character` | 11 formats (Unicode, HTML, CSS, JS, Python, Java, UTF-8/16, URL) |
| `symbolfyi_html_entity_lookup` | `entity` | Reverse HTML entity lookup (e.g., `&hearts;` to character) |

### Unicode Tools (4 tools) -- unicodefyi

| Tool | Parameters | Description |
|------|-----------|-------------|
| `unicodefyi_char_info` | `codepoint_or_char` | Full Unicode info (accepts U+hex, character, or hex codepoint) |
| `unicodefyi_char_encode` | `codepoint_or_char` | 17 encodings (HTML, CSS, JS, Python, Go, Rust, C/C++, URL, UTF-8/16/32) |
| `unicodefyi_unicode_search` | `query`, `limit?` | Search characters by name substring |
| `unicodefyi_html_entity_lookup` | `entity` | HTML entity lookup (e.g., `&amp;` to ampersand) |

### Font Tools (6 tools) -- fontfyi

| Tool | Parameters | Description |
|------|-----------|-------------|
| `fontfyi_font_info` | `slug` | Google Font metadata (family, weights, subsets, designer, rank) |
| `fontfyi_font_search` | `query`, `limit?` | Search Google Fonts by name |
| `fontfyi_font_css` | `slug` | CSS import snippet + font-family declaration |
| `fontfyi_font_pairings` | `slug` | Font pairing recommendations with mood and use cases |
| `fontfyi_font_stacks` | -- | 10 CSS font stack presets for common use cases |
| `fontfyi_popular_fonts` | `limit?` | Most popular Google Fonts by rank |

### Distance Tools (5 tools) -- distancefyi

| Tool | Parameters | Description |
|------|-----------|-------------|
| `distancefyi_calculate_distance` | `lat1`, `lon1`, `lat2`, `lon2`, `same_continent?` | Full distance report (km/miles/NM), bearing, midpoint, travel times |
| `distancefyi_get_bearing` | `lat1`, `lon1`, `lat2`, `lon2` | Bearing degrees + compass direction |
| `distancefyi_get_midpoint` | `lat1`, `lon1`, `lat2`, `lon2` | Geographic midpoint coordinates |
| `distancefyi_get_flight_time` | `distance_km` | Estimated flight time (variable speed 600-850 km/h) |
| `distancefyi_convert_distance` | `value`, `from_unit`, `to_unit` | Distance conversion between km, miles, nautical miles |

### Time Tools (5 tools) -- timefyi

| Tool | Parameters | Description |
|------|-----------|-------------|
| `timefyi_current_time` | `timezone_id` | Current time in IANA timezone (with UTC offset, DST status) |
| `timefyi_time_difference` | `from_tz`, `to_tz` | Time difference between two timezones |
| `timefyi_convert_time` | `time_str`, `from_tz`, `to_tz` | Convert specific time across timezones |
| `timefyi_business_hours_overlap` | `timezones`, `start_hour?`, `end_hour?` | Find overlapping business hours across timezones |
| `timefyi_sun_info` | `latitude`, `longitude`, `timezone_id` | Sunrise, sunset, day length, current daylight status |

### Unit Tools (4 tools) -- unitfyi

| Tool | Parameters | Description |
|------|-----------|-------------|
| `unitfyi_convert_unit` | `value`, `from_unit`, `to_unit` | Convert between 220 units in 20 categories with Decimal precision |
| `unitfyi_conversion_table` | `from_unit`, `to_unit` | Markdown table with common conversion values |
| `unitfyi_list_categories` | -- | All 20 measurement categories |
| `unitfyi_list_units` | `category` | All units in a category with slug, name, and symbol |

### Name Tools (4 tools) -- namefyi

| Tool | Parameters | Description |
|------|-----------|-------------|
| `namefyi_romanize_korean` | `hangul` | Revised Romanization of Korean text |
| `namefyi_five_elements` | `stroke_count` | Five Elements category for CJK stroke count |
| `namefyi_element_compatibility` | `element_a`, `element_b` | Compatibility between two Five Elements |
| `namefyi_format_population` | `population` | Format large numbers with M/K suffixes |

### Holiday Tools (5 tools) -- holidayfyi

| Tool | Parameters | Description |
|------|-----------|-------------|
| `holidayfyi_upcoming_holidays` | `country_iso`, `n?` | Next N public holidays for ISO country code |
| `holidayfyi_check_holidays_on_date` | `date_str`, `countries` | Check holidays on a specific date across countries |
| `holidayfyi_easter_date` | `year`, `orthodox?` | Western or Orthodox Easter date for any year |
| `holidayfyi_nth_weekday` | `year`, `month`, `weekday`, `n` | Find nth occurrence of weekday in a month |
| `holidayfyi_count_days_until` | `target_date_str`, `from_date_str?` | Days countdown to a target date |

## Architecture

Hub aggregation pattern -- each package has its own standalone MCP server, and the hub collects all tools into a single server with `{package}_` prefixed tool names.

```
fyipedia-mcp (hub server)
├── colorfyi.mcp_server     →  9 tools
├── emojifyi.mcp_server     →  7 tools
├── symbolfyi.mcp_server    →  3 tools
├── unicodefyi.mcp_server   →  4 tools
├── fontfyi.mcp_server      →  6 tools
├── distancefyi.mcp_server  →  5 tools
├── timefyi.mcp_server      →  5 tools
├── namefyi.mcp_server      →  4 tools
├── unitfyi.mcp_server      →  4 tools
└── holidayfyi.mcp_server   →  5 tools
                               ──
                               52 tools total
```

Missing packages are silently skipped. Each package's MCP server also works standalone.

## Available FYI Packages

| Plugin | Package | Description |
|--------|---------|-------------|
| Color | [colorfyi](https://pypi.org/project/colorfyi/) | Color conversion (7 spaces), WCAG contrast, harmonies, shades, color blindness |
| Emoji | [emojifyi](https://pypi.org/project/emojifyi/) | 3,953 emoji metadata, search, 8 encoding formats |
| Symbol | [symbolfyi](https://pypi.org/project/symbolfyi/) | Symbol encoding (11 formats), Unicode properties |
| Unicode | [unicodefyi](https://pypi.org/project/unicodefyi/) | Unicode character info, 17 encodings, 90 HTML entities |
| Font | [fontfyi](https://pypi.org/project/fontfyi/) | 50 Google Fonts metadata, CSS snippets, font pairings |
| Distance | [distancefyi](https://pypi.org/project/distancefyi/) | Haversine distance, bearing, midpoint, travel times |
| Time | [timefyi](https://pypi.org/project/timefyi/) | Timezone operations, time differences, sunrise/sunset |
| Name | [namefyi](https://pypi.org/project/namefyi/) | Korean romanization, Five Elements, CJK stroke count |
| Unit | [unitfyi](https://pypi.org/project/unitfyi/) | 220 units across 20 categories, Decimal precision |
| Holiday | [holidayfyi](https://pypi.org/project/holidayfyi/) | Holiday dates for 100+ countries, Easter calculation |

## Demo

![FYIPedia MCP demo](https://raw.githubusercontent.com/fyipedia/fyipedia-mcp/main/demo.gif)

## FYIPedia Ecosystem

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem. Also available as a [unified CLI](https://pypi.org/project/fyipedia/) (`fyi` command) for terminal use.
