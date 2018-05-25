from talon.voice import Context, Key
from talon import macos

ctx = Context('mission_control')

ctx.keymap({
    "(mission control | switch all)": lambda m: macos.dock_notify('com.apple.expose.awake'),
    "expose": lambda m: macos.dock_notify('com.apple.expose.front.awake'),
    "space last": Key('ctrl-alt-cmd-left'),
    "space next": Key('ctrl-alt-cmd-right'),
    "launchpad": lambda m: macos.dock_notify('com.apple.launchpad.toggle'),
    "desktop show": lambda m: macos.dock_notify('com.apple.showdesktop.awake'),
})
