from talon.voice import Context
import os

ctx = Context('websites')

def openSite(s):
    def func(m):
        os.system('open ' + s)
    return func

ctx.keymap({
    'website doc': openSite('https://duckduckgo.com/'),
    'website get hub': openSite('https://github.com/lexjacobs/'),
    'website gmail': openSite('https://gmail.com'),
    'website google': openSite('https://google.com'),
    'website stack': openSite('https://stackoverflow.com/'),
    'website youtube': openSite('https://youtube.com'),
})
