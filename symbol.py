from talon.voice import Context, Key

ctx = Context('symbol')

keymap = {
    'clamor': '!',
    'coalgap': ': ',
    'coalshock': [':', Key('enter')],
    'crunder': '_',
    'dollar [sign]': '$',
    'dot js': '.js',
    'opera fat': ' => ',
    'glitch': ['`', '`', Key('left')],
    'junk': Key('backspace'),
    'minus twice': '--',
    'plus twice': '++',
    'questo': '?',
    'randall': Key('esc'),
    '(semi | semicolon | sunk)': ';',
    'sinker': [Key('cmd-right ;')],
    'slurp': [Key('delete'), Key('backspace')],
    'spunk': Key('delete'),
    'swipe super': ', ',
}

ctx.keymap(keymap)
