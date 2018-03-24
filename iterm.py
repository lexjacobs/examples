from talon.voice import Key, Context

ctx = Context('iterm', bundle='com.googlecode.iterm2')

keymap = {
    '[toggle] full-screen': Key('cmd-enter'),
    'exit session': [Key('ctrl-c'), 'exit\n'],
    # 'broadcaster': Key('cmd-alt-i'),
    'window clear': Key('cmd-k'),
    'window split': Key('cmd-shift-d'),
    # 'split vertical': Key('cmd-d'),
}

ctx.keymap(keymap)
