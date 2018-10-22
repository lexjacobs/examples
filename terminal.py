from talon.voice import Word, Key, Context, Str
import string

terminals = ('com.apple.Terminal', 'com.googlecode.iterm2')
ctx = Context('terminal', func=lambda app, win: any(
    t in app.bundle for t in terminals))

keymap = {
    'cd last': 'cd -; ls -a;\n',
    'cd desktop': 'cd ~/Desktop; ls -a;\n',
    'cd develop': 'cd ~/develop; ls -a;\n',
    'cd (download|downloads)': 'cd ~/Downloads; ls -a;\n',
    'cd home': 'cd ~; ls -a;\n',
    'cd parent': 'cd ..; ls -a;\n',

    'shell snip': [Key('ctrl-a'), Key('ctrl-k')],
    'kite': [Key('esc'), Key('d')],
    'trough': [Key('ctrl-w')],
    'tools oedipus': [Key('ctrl-x'), Key('ctrl-e')],
    'open code': Str('code .\n'),
    'open sublime': Str('subl .\n'),
    'open adam': Str('atom .\n'),

    'window clear': Key('cmd-k'),
    'tools full-screen': Key('cmd-enter'),
    'tools exit': [Key('ctrl-c'), 'exit\n'],
    'tools (reset|refresh)': Key('ctrl-c up enter'),
    'tools wi-fi off': 'networksetup -setairportpower en0 off\n',
    'tools wi-fi on': 'networksetup -setairportpower en0 on\n'
}

ctx.keymap(keymap)
