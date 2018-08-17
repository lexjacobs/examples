from talon.voice import Context, Key

ctx = Context('symbol')

keymap = {
    'clamor': '!',
    'coal gap': ': ',
    'coal shock': [':', Key('enter')],
    'crunder': '_',
    'dollar [sign]': '$',
    'dot js': '.js',
    'open fat': ' =>',
    'glitch': ['``', Key('left')],
    'minus twice': '--',
    'plus twice': '++',
    'questo': '?',
    'sunk': ';',
    'sinker': [Key('cmd-right ;')],
    'slurp': [Key('delete'), Key('backspace')],
    'spunk': Key('delete'),
}

ctx.keymap(keymap)
