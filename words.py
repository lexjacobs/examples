from talon.voice import Context, Key

ctx = Context('words')

keymap = {
    'shrink command': 'cmd',
    'shrink control': 'ctrl',
    'shrink option': 'opt',

    'state git': 'git',
    'state gist': 'gist',
    'state with': 'width',
    'state static': 'static ',
    'state no': 'null',
    'state no super': 'NULL',
    'state printf': 'printf',
    'state define': 'def ',
    'state import': 'import ',
    'dot company': '.com',
}

ctx.keymap(keymap)
