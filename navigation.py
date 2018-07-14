from talon.voice import Context, Key

ctx = Context('navigation')

keymap = {
    # Requires activation of System Preferences -> Shortcuts -> Input Sources
    # -> "Select the previous input source"
    # 'change language': Key('ctrl-space'),

    # Application navigation
    'launcher': Key('alt-space'),
    'spotty': Key('cmd-space'),
    'switch': Key('cmd-tab'),
    'tab close': Key('cmd-w'),
    'window new': Key('cmd-n'),
    'window next': Key('cmd-`'),
    'window last': Key('cmd-shift-`'),

    # Following three commands should be application specific
    'tab last': Key('cmd-alt-left'),
    'tab next': Key('cmd-alt-right'),
    'tab new': Key('cmd-t'),
    'tab reset': Key('cmd-r'),
    'tab (and | end)': Key('cmd-9'),

    # deleting
    'kite': Key('alt-delete'),
    'snip left': Key('cmd-shift-left delete'),
    'snip right': Key('cmd-shift-right delete'),
    'slurp': Key('backspace delete'),
    'trough': Key('alt-backspace'),

    # 'shocker': [Key('cmd-left enter up')],
    # 'wonkrim': Key('alt-ctrl-left'),
    # 'wonkrish': Key('alt-ctrl-right'),
    'locky': Key('alt-left'),
    'rocky': Key('alt-right'),
    'ricky': Key('cmd-right'),
    'lefty': Key('cmd-left'),
    # '(left | crimp)': Key('left'),
    # '(right | chris)': Key('right'),
    # 'jeep': Key('up'),
    # '(down | dune | doom)':  Key('down'),

    # selecting
    'snatch': Key('cmd-x'),
    'stoosh': Key('cmd-c'),
    'spark': Key('cmd-v'),
    'shreepway': Key('cmd-shift-up'),
    'shroomway': Key('cmd-shift-down'),
    'shreep': Key('shift-up'),
    'shroom': Key('shift-down'),
    'lecksy': Key('cmd-shift-left'),
    'ricksy': Key('cmd-shift-right'),
    'shlocky': Key('alt-shift-left'),
    'shrocky': Key('alt-shift-right'),
    'shlicky': Key('shift-left'),
    'shricky': Key('shift-right'),
}

ctx.keymap(keymap)
