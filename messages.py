from talon.voice import Context, Key

ctx = Context('messages', bundle='com.apple.iChat')

keymap = {
    'tab next': [Key('cmd-shift-]')],
    'tab last': [Key('cmd-shift-[')],
    'tab new': [Key('cmd-n')],
    'tab close': [Key('cmd-backspace')],
}

ctx.keymap(keymap)
