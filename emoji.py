from talon import clip
from talon.voice import press, Context

ctx = Context('emoji')

def Paste(s):
    def func(m):
        clip.set(s)
        press('cmd-v')
    return func

ctx.keymap({
    'snippet shrug': Paste("¯\_(ツ)_/¯"),
})
