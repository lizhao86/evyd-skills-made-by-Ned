"""
EVYD PPT Generator — Style Presets
====================================
Add a new style by copying an existing entry and changing the values.
Select a style via content.json meta.style or --style CLI flag.
"""
from pptx.dml.color import RGBColor

def rgb(hex_str):
    """Parse '#RRGGBB' or 'RRGGBB' to RGBColor."""
    h = hex_str.lstrip('#')
    return RGBColor(int(h[0:2],16), int(h[2:4],16), int(h[4:6],16))


STYLES = {

    # ── EVYD Blue (default) ─────────────────────────────────────────────────
    # Navy header strip + blue content backgrounds.
    # Cards: dark navy. Accent: teal.
    "evyd_blue": {
        "font":          "Aptos",
        "accent":        rgb("2CD5C3"),   # teal
        "accent2":       rgb("0076B3"),   # medium blue
        "navy":          rgb("172E41"),
        "white":         rgb("FFFFFF"),

        # Card backgrounds on blue slides
        "card":          rgb("003B6B"),   # dark card
        "card_side":     rgb("004F7D"),   # card left strip
        "card_num":      rgb("3388BB"),   # large number
        "text_dim":      rgb("BBCCDD"),   # dim body text
        "text_num":      rgb("CCE8F5"),   # slide-number colour

        # Card backgrounds on white slides
        "card_white":    rgb("EFF7FD"),   # very light blue
        "text_gray":     rgb("446688"),   # mid-gray body text
        "text_dark":     rgb("172E41"),   # navy body text
        "line_gray":     rgb("225588"),   # rule on blue slides
    },

    # ── EVYD White ──────────────────────────────────────────────────────────
    # White content backgrounds throughout.
    # Useful for printed handouts.
    "evyd_white": {
        "font":          "Aptos",
        "accent":        rgb("0076B3"),   # blue accent
        "accent2":       rgb("2CD5C3"),   # teal secondary
        "navy":          rgb("172E41"),
        "white":         rgb("FFFFFF"),

        "card":          rgb("EFF7FD"),
        "card_side":     rgb("0076B3"),
        "card_num":      rgb("0076B3"),
        "text_dim":      rgb("446688"),
        "text_num":      rgb("AAAAAA"),

        "card_white":    rgb("EFF7FD"),
        "text_gray":     rgb("446688"),
        "text_dark":     rgb("172E41"),
        "line_gray":     rgb("BCD6E8"),
    },

    # ── EVYD Teal ───────────────────────────────────────────────────────────
    # High-contrast teal accent with navy backgrounds.
    # Good for external presentations.
    "evyd_teal": {
        "font":          "Aptos",
        "accent":        rgb("2CD5C3"),
        "accent2":       rgb("06B6AA"),
        "navy":          rgb("0A1E30"),
        "white":         rgb("FFFFFF"),

        "card":          rgb("072834"),
        "card_side":     rgb("076C60"),
        "card_num":      rgb("2CD5C3"),
        "text_dim":      rgb("88BBBB"),
        "text_num":      rgb("99DDDD"),

        "card_white":    rgb("E8F9F7"),
        "text_gray":     rgb("2A6666"),
        "text_dark":     rgb("0A1E30"),
        "line_gray":     rgb("076C60"),
    },
}
