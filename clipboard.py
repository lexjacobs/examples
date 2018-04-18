from talon.voice import Context, Key, Str, press
from talon import clip

ctx = Context('clipboard')

def get_selection():
    old = clip.get()
    serial = clip.serial()
    press('cmd-c', wait=0)
    sel = clip.await_change(after=serial)
    clip.set(old)
    return sel

def bigPrevious(everything):
    def select_and_change(m):
        press('shift-alt-left')
        value = get_selection()
        if everything == True:
            Str(value.upper())(None)
        else:
            Str(value.capitalize())(None)
    return select_and_change

keymap = {
    'run caps': bigPrevious(False),
    'run yeller': bigPrevious(True)
}

ctx.keymap(keymap)
