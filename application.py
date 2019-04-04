from talon.voice import Context, Key, Str, ui
import time

ctx = Context("application_launcher")

# will launch if not already open
def open_application(application):
    def open_or_switch(m):
        ui.launch(bundle=application)

    return open_or_switch


# get bundle: osascript -e 'id of app "app-name"'
keymap = {
    # '(stratum|application adam)': open_application('com.github.atom'),
    "application activity": open_application("com.apple.ActivityMonitor"),
    "(chromie|application chrome)": open_application("com.google.Chrome"),
    "application code": open_application("com.microsoft.VSCode"),
    # 'application developer': open_application('org.mozilla.firefoxdeveloperedition'),
    # 'application doctor': open_application('com.docker.docker'),
    # 'application firefox': open_application('org.mozilla.firefox'),
    # '(termite|application I term)': open_application('com.googlecode.iterm2'),
    "(termite|application I term)": open_application("com.apple.Terminal"),
    "(chatter|application (message|messages))": open_application("com.apple.iChat"),
    "application music": open_application("com.apple.iTunes"),
    "application reminder": open_application("com.apple.reminders"),
    "application skype": open_application("com.skype.skype"),
    "(slacker|application slacker)": open_application("com.tinyspeck.slackmacgap"),
    # 'application sublime': open_application('com.sublimetext.3'),
    "application terminal": open_application("com.apple.Terminal"),
    "application text": open_application("com.apple.TextEdit"),
    # 'application video': open_application('org.videolan.vlc'),
    "application tree": open_application("com.torusknot.SourceTreeNotMAS"),
    # '(zeppelin|application zeppelin)': open_application('io.zeplin.osx'),
    "application zoom": open_application("us.zoom.xos"),
    "system preferences": open_application("com.apple.systempreferences"),
    # 'preffies': Key('cmd-,'),
    # 'marco': Key('cmd-f'),
    # 'marco project': Key('cmd-shift-f'),
    # 'marco select': Key('cmd-e cmd-f enter'),
    # 'marco next': Key('cmd-g'),
    # 'marco last': Key('cmd-shift-g'),
    "run stacks": Key("ctrl-alt-d"),
}

ctx.keymap(keymap)
