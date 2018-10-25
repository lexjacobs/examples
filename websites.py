from talon import clip
from talon.voice import press, Context
import os

ctx = Context('websites')

def Paste(s):
    def func(m):
        clip.set(s)
        press('cmd-v')
    return func

ctx.keymap({
    'website gmail': lambda m: os.system('open https://gmail.com'),
    'website get hub': lambda m: os.system('open https://github.com/lexjacobs/')
})
