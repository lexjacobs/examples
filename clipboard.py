from talon.voice import Context, Key, Str, press
from talon import clip

ctx = Context('clipboard')

def get_selection():
    with clip.capture() as s:
        press('cmd-c', wait=0)
    return s.get()

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
