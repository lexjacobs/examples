from talon.voice import Word, Key, Context, Str
import string

terminals = ('com.apple.Terminal', 'com.googlecode.iterm2')
ctx = Context('terminal', func=lambda app, win: any(
    t in app.bundle for t in terminals))

keymap = {
    'cd back': 'cd -; ls -a;\n',
    'cd develop': 'cd ~/develop; ls -a;\n',
    'cd home': 'cd ~; ls -a;\n',
    'cd parent': 'cd ..; ls -a;\n',

    'snip line': [Key('ctrl-a'), Key('ctrl-k')],
    'kite': [Key('esc'), Key('d')],
    'trough': [Key('ctrl-w')],
    'tools oedipus': [Key('ctrl-x'), Key('ctrl-e')],
    'open sublime': Str('subl .\n'),
    'open adam': Str('atom .\n'),

    'tools full-screen': Key('cmd-enter'),
    'tools exit': [Key('ctrl-c'), 'exit\n'],
    'window clear': Key('cmd-k'),
}

ctx.keymap(keymap)
