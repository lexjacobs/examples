from talon.voice import Context, Key, Str
import time

ctx = Context('application_launcher')

def open_application(application):
    def open_new(m):
        Key('alt-space')(None)
        time.sleep(0.2)
        Str(application)(None)
        time.sleep(0.2)
        Key('return')(None)
    return open_new

keymap = {
    'application adam': open_application('atom'),
    'application code': open_application('code.app'),
    'application developer': open_application('developer'),
    'application firefox': open_application('firefox.app'),
    'application I term': open_application('iterm'),
    'application messages': open_application('messages'),
    'application music': open_application('itunes'),
    'application slacker': open_application('slack'),
    'application terminal': open_application('terminal'),
    'application tree': open_application('sourcetree'),
    'application zoom': open_application('zoom'),
    'preffies': Key('cmd-,'),
    'marco': Key('cmd-f'),
    'marco super': Key('cmd-shift-f'),
    'run stacks': Key('ctrl-alt-d'),
}

ctx.keymap(keymap)
