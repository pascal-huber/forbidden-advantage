import re

KEY_WIDTH = 48
KEY_HEIGHT = 48
KEY_PADDING = 2
KEY_SPACING=10
LINE_SPACING = 18
BOARD_SPACING = 2
KEY_RADIUS = 2


STYLE = """
    svg {
        font-family: "Iosevka Term Slab", monospace;
        font-size: 22px;
        font-kerning: normal;
        font-weight: bold;
        text-rendering: optimizeLegibility;
        fill: #24292e;
    }

    rect {
        fill: #f6f8fa;
        stroke: #333;
    }

    .combo {
        font-size: 20px;
    }

    .key {
        stroke: #333;
    }

    .pressed {
        fill: #555;
    }

    .pressed-text {
        fill: #faa;
    }

    .disabled {
        fill: #f6f8fa;
        stroke: #ccc;
        border-color: red;
    }

    .deactivated {
        fill: #f000;
        stroke: #f000;
    }

    .sticky {
        fill: #ccc;
    }
"""


# inexistent key
___ = {"key": "", "class": "deactivated", "rowspan": False}

# disabled/unused
_u_ = {"key": "", "class": "disabled", "rowspan": False}
_u2_ = {"key": "", "class": "disabled", "rowspan": True}

# disabled
def d(key, rowspan=False):
    return {"key": key, "class": "disabled", "rowspan": bool(rowspan)}

# normal key
def n(key, rowspan=False):
    return {"key": key, "class": "key", "rowspan": bool(rowspan)}

# pressed
def p(key, rowspan=False):
    return {"key": key, "class": "pressed", "rowspan": bool(rowspan)}

# sticky key
def sk(key, rowspan=False):
    return {"key": key, "class": "sticky", "rowspan": bool(rowspan)}


KEYMAP = [
    {
        "name": "base",
        "rows": [
            [___,  "w", "f", "p", "b", ___, "j", "l", "u",      "y",      ___ ],
            ["a",  "r", "s", "t", "g", ___, "m", "n", "e",      "i",      "o" ],
            ["z",  "x", "c", "d", "v", ___, "k", "h", "&lt; ,", "&gt; .", "? /" ],

            [___,  ___, ___,  _u_, sk("CTRL"), ___,                 "F5", _u_,  ___, ___, ___,  ],
            [___,  ___, n("NAV", 1), n("SHFT", 1),  sk("CTRL SHFT"), ___, "F10", n("SPC", 1), n("SYM", 1), ___, ___, ],
            [___,  ___, ___, ___, _u_, ___,                 "F11", ___, ___, ___, ___, ]
        ],
        "combos": [
            (0,1,"q")
        ],
    },
    {
        "name": "sym",
        "rows": [
            [___,  "[", "{", "(", "~", ___, "^", ")", "}", "]", ___           ],
            ["-",  "*", "=", "_", "$", ___, "#", sk("MOD"), sk("ALT"), sk("CTRL"), sk("SHFT")             ],
            ["+",  "|", "@", "\\", "%", ___, "`", "&amp;", "'", "\"", "!" ],
            [___,  ___, ___,  _u_, _u_, ___,                 _u_, _u_,  ___, ___, ___,  ],
            [___,  ___, n("NAV", True), n("BSPC", True), _u_, ___, _u_, _u2_, p("SYM", True), ___, ___, ],
            [___,  ___, ___, ___, _u_, ___,                 _u_, ___, ___, ___, ___, ]
        ],
        "combos": [],
    },
    {
        "name": "nav",
        "rows": [
            [___,  ";", ":", "q", "ö", ___, "page up", "home", "↑", "end", ___           ],
            [sk("SHFT"),  sk("CTRL"), sk("ALT"), sk("MOD"), "ä", ___, "page down", "←", "↓", "→", _u_ ],
            [sk("ALT GR"),  _u_, _u_, "ESC", "ü", ___, "DEL", "INS", "TAB", "C-g", _u_ ],
            [___,  ___, ___,  _u_, _u_, ___,                 "vol up", _u_,  ___, ___, ___,  ],
            [___,  ___, p("NAV", True), _u2_,  _u_, ___, "vol down", n("RET", True), n("SYM", True), ___, ___, ],
            [___,  ___, ___, ___, _u_, ___,                 _u_, ___, ___, ___, ___, ]
        ],
        "combos": [],
    },
    {
        "name": "nav_sym",
        "rows": [
            [___,  "5", "3", "1", "9", ___, "8", "0", "2", "4", ___           ],
            [sk("SHFT"),  sk("CTRL"), sk("ALT"), sk("MOD"), "7", ___, "6", sk("MOD"), sk("ALT"), sk("CTRL"), sk("SHFT")             ],
            ["F7",  "F5", "F3", "F1", "F9", ___, "F8", "F10", "F2", "F4", "F6" ],
            [___,  ___, ___,  _u_, _u_, ___,                 _u_, _u_,  ___, ___, ___,  ],
            [___,  ___, p("NAV", True), _u2_,  _u_, ___, _u_, _u2_, p("SYM", True), ___, ___, ],
            [___,  ___, ___, ___, _u_, ___,                 _u_, ___, ___, ___, ___, ]
        ],
        "combos": [
            (2, 2, "F11"),
            (2, 7, "F12"),
        ],
    },
    {
        "name": "soldering",
        "rows": [
            [___,  "0/1", "0/2", "0/3", "0/4", ___, "0/7", "0/8", "0/9", "0/10", ___           ],
            ["1/0",  "1/1", "1/2", "1/3", "1/4", ___, "1/7", "1/8", "1/9", "1/10", "1/11"           ],
            ["2/0",  "2/1", "2/2", "2/3", "2/4", ___, "2/7", "2/8", "2/9", "2/10", "2/11"           ],
            [d("3/0"),  d("3/1"), d("3/2"), d("3/3"), ___,  ___, ___, d("3/8"), d("3/9"), d("3/10"), d("3/11") ],
            [___,  ___, ___,  "4/2", "4/3", ___,                 "4/8", "4/9",  ___, ___, ___,  ],
            [___,  ___, n("4/4", True), n("4/5", True),  "4/1", ___, "4/10", n("4/6", True), n("4/7", True), ___, ___, ],
            [___,  ___, ___, ___, "4/0", ___,                 "4/11", ___, ___, ___, ___, ]
        ],
        "combos": []
    }
]

def print_key(x, y, key):
    content = ''
    key_class = ""
    rowspan = False
    if type(key) is dict:
        key_class = key["class"]
        rowspan= key["rowspan"]
        key = key["key"]
    key_height = KEY_HEIGHT
    if rowspan:
        key_height = KEY_HEIGHT * 2 + KEY_SPACING
    content += f'<rect rx="{KEY_RADIUS}" ry="{KEY_RADIUS}" x="{x}" y="{y}" width="{KEY_WIDTH}" height="{key_height}" class="{key_class} key" />'
    words = key.split()
    x +=  (KEY_WIDTH) / 2
    y +=  (key_height + KEY_SPACING - (len(words) - 1) * LINE_SPACING) / 2.2
    key_class += "-text"
    for word in key.split():
        content += f'<text text-anchor="middle" dominant-baseline="middle" x="{x}" y="{y}" class="{key_class}">'
        content += word
        content += '</text>'
        y += LINE_SPACING
    return content


def print_combo(row, col, key):
    x = BOARD_SPACING
    y = BOARD_SPACING
    content = ""
    key_fract_x = 0.7
    key_fract_y = 0.4
    # jump to key "x", jump to center to nect key, jump back half of the key length
    x += col * (KEY_WIDTH + KEY_SPACING) +  (KEY_WIDTH + KEY_SPACING/2) - key_fract_x*KEY_WIDTH/2
    # jump to key "y" go back 2/3 of the small key height
    y += row * (KEY_HEIGHT + KEY_SPACING) + KEY_HEIGHT - key_fract_y*KEY_HEIGHT*2/3
    key_h = KEY_HEIGHT * key_fract_y
    key_w = KEY_WIDTH * key_fract_x
    key_class = "combo"
    content += f'<rect rx="{4}" ry="{4}" x="{x}" y="{y}" width="{key_w}" height="{key_h}" class="{key_class} key" />'
    x +=  (KEY_WIDTH*key_fract_x/2)
    y +=  KEY_PADDING + (1.0-key_fract_y)*KEY_HEIGHT / 3
    for word in key.split():
        content += f'<text text-anchor="middle" dominant-baseline="middle" x="{x}" y="{y}" class="combo">'
        content += word
        content += '</text>'
        y += LINE_SPACING
    return content


def print_combos(combos):
    content = ""
    for combo in combos:
        content += print_combo(combo[0], combo[1], combo[2])
    return content


def print_row(x, y, row):
    content = ''
    for key in row:
        content += print_key(x, y, key)
        x += KEY_WIDTH
        x += KEY_SPACING
    return content


def print_layer(x, y, layer):
    content = ''
    for i, row in enumerate(layer["rows"]):
        content += print_row(x, y, row)
        y += KEY_HEIGHT
        y += KEY_SPACING
    content += print_combos(layer["combos"])
    return content


def layer_dimensions(layer):
    ncol = 0
    nrow = 0
    for row in layer["rows"]:
        ncol = max(ncol, len(row))
        nrow += 1
    return nrow, ncol


for i, layer in enumerate(KEYMAP):
    nrow, ncol = layer_dimensions(layer)
    layer_width = ncol * KEY_WIDTH + (ncol - 1) * KEY_SPACING
    layer_height = nrow * KEY_HEIGHT + (nrow - 1) * KEY_SPACING
    svg_width = layer_width + 2 * BOARD_SPACING
    svg_height = layer_height + 2 * BOARD_SPACING
    content = f'<svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">'
    content += f'<style>{STYLE}</style>'
    content += print_layer(BOARD_SPACING, BOARD_SPACING, layer)
    content += '</svg>'
    with open('dist/layer_' + layer["name"] + '.svg', 'w') as f:
        f.write(content)
