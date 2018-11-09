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
    'website doc': lambda m: os.system('open https://duckduckgo.com/'),
    'website get hub': lambda m: os.system('open https://github.com/lexjacobs/'),
    'website gmail': lambda m: os.system('open https://gmail.com'),
    'website google': lambda m: os.system('open https://google.com'),
    'website stack': lambda m: os.system('open https://stackoverflow.com/'),
})
