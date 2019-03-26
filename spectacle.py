from talon.voice import Key, press, Str, Context

# Move and resize windows with Spectacle.app

ctx = Context("spectacle")


keymap = {
    # 'wendy center': Key('cmd-alt-f4'),
    "wendy max": Key("cmd-ctrl-alt-f10"),
    "wendy left": Key("cmd-ctrl-alt-f11"),
    "wendy right": Key("cmd-ctrl-alt-f12"),
    # 'wendy top': Key('cmd-alt-top'),
    # 'wendy bottom': Key('cmd-alt-bottom'),
    # 'wendy upper left': Key('cmd-ctrl-alt-f3'),
    # 'wendy lower left': Key('cmd-ctrl-shift-left'),
    # 'wendy upper right': Key('cmd-ctrl-right'),
    # 'wendy lower right': Key('cmd-ctrl-shift-right'),
    "wendy next": Key("cmd-ctrl-alt-f6"),
    "wendy last": Key("cmd-ctrl-alt-f5"),
    "wendy middle": [
        Key("cmd-ctrl-alt-f3"),
        Key("cmd-ctrl-alt-f4"),
        Key("cmd-ctrl-alt-f8"),
        Key("cmd-ctrl-alt-f8"),
        Key("cmd-ctrl-alt-f8"),
        Key("cmd-ctrl-alt-f8"),
        Key("cmd-ctrl-alt-f8"),
        Key("cmd-ctrl-alt-f8"),
        Key("cmd-ctrl-alt-f8"),
        Key("cmd-ctrl-alt-f8"),
        Key("cmd-ctrl-alt-f8"),
        Key("cmd-ctrl-alt-f8"),
        Key("cmd-ctrl-alt-f8"),
    ],
    # 'wendy next third': Key('ctrl-alt-right'),
    # 'wendy previous third': Key('ctrl-alt-left'),
    "wendy larger": Key("cmd-ctrl-alt-f8"),
    "wendy smaller": Key("cmd-ctrl-alt-f9"),
    "wendy undo": Key("cmd-ctrl-alt-f7"),
    # 'wendy redo': Key('cmd-alt-shift-z'),
    "wendy restore": Key("cmd-ctrl-r"),  # from Display Maid
}

ctx.keymap(keymap)
