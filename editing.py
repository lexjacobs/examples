from talon.voice import Context, Key
from talon import clip
import time

ctx = Context('editing')

keymap = {
    'commander': Key('cmd-a'),
    'sage': Key('cmd-s'),
    'dizzle': Key('cmd-z'),
    'jolt': Key('shift-cmd-right right shift-cmd-left cmd-c right return cmd-v'),
    'rizzle': Key('cmd-shift-z'),
    'shackle': Key('shift-cmd-right right shift-cmd-left'),
    'snipple': Key('shift-cmd-left delete'),
    'snipper': Key('shift-cmd-right delete'),
    'snip line': [Key('cmd-right'), lambda m: time.sleep(0.05), Key('shift-cmd-left shift-cmd-left delete delete')],
    'trundle': Key('cmd-/'),
    'trundle super': [Key('/'), Key('*'), Key('*'), Key('/'), Key('left'), Key('left'), Key('return'), Key('return'), Key('up')],
}

ctx.keymap(keymap)
