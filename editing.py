from talon.voice import Context, Key
from talon import clip

def set_this(m):
    result = clip.get()
    print('result', result)

ctx = Context('edit')

keymap = {
    'sage': Key('cmd-s'),
    'dizzle': Key('cmd-z'),
    'rizzle': Key('cmd-shift-z'),
    'snipple': Key('shift-cmd-left delete'),
    'snipper': Key('shift-cmd-right delete'),
    'trundle': Key('cmd-/'),
}

ctx.keymap(keymap)
