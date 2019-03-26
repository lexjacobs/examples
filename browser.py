from talon.voice import Context, Key

ctx = Context("browser")

keymap = {
    "history last": Key("cmd-["),
    "history next": Key("cmd-]"),
    "tools (inspect | inspector)": Key("cmd-shift-c"),
    "tools console": Key("cmd-alt-j"),
    "tools (develop | developer)": Key("cmd-alt-i"),
    "tools screen capture": Key("cmd-shift-4"),
    "tools screen copy": Key("cmd-ctrl-shift-4"),
    "tools source": Key("cmd-alt-u"),
}

ctx.keymap(keymap)
