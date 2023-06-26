#set document(
    title: "Forbidden Advantage Keymap",
    author: "Pascal Huber",
)
#set page(
    margin: (x: 0.2cm, y: 0.6cm),
    // flipped: true,
    // paper: "a5",
    width: 14cm,
    height: 9cm,
)
#set text(
    font: "Iosevka Term Slab",
)

#grid(
    columns: (auto, auto),
    rows: (auto, auto),
    gutter: 15pt,
    image("dist/layer_base.svg"),
    image("dist/layer_nav.svg"),
    image("dist/layer_sym.svg"),
    image("dist/layer_nav_sym.svg"),
)
