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
    'application doctor': open_application('docker'),
    'application firefox': open_application('firefox.app'),
    'application I term': open_application('iterm'),
    'application messages': open_application('messages'),
    'application music': open_application('itunes'),
    'application skype': open_application('skype'),
    'application slacker': open_application('slack'),
    'application sublime': open_application('sublime text'),
    'application terminal': open_application('terminal'),
    'application tree': open_application('sourcetree'),
    'application zoom': open_application('zoom'),
    'preffies': Key('cmd-,'),
    'marco': Key('cmd-f'),
    'marco project': Key('cmd-shift-f'),
    'marco select': Key('cmd-e cmd-f enter'),
    'marco next': Key('cmd-g'),
    'marco last': Key('cmd-shift-g'),
    'run stacks': Key('ctrl-alt-d'),
}

ctx.keymap(keymap)
