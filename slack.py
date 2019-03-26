from talon.voice import Context, Key

ctx = Context("slack", bundle="com.tinyspeck.slackmacgap")

keymap = {
    "channel": Key("cmd-k"),
    "channel last": Key("alt-up"),
    "channel next": Key("alt-down"),
    "tools command": ["``", Key("left")],
    "tools code": ["``````", Key("left left left return return up")],
}

ctx.keymap(keymap)
