from talon.voice import Context, Key

ctx = Context("messages", bundle="com.apple.iChat")

keymap = {
    "chat next": [Key("cmd-shift-]")],
    "chat last": [Key("cmd-shift-[")],
    "chat new": [Key("cmd-n")],
    "chat close": [Key("cmd-backspace")],
}

ctx.keymap(keymap)
