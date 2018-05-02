from talon.voice import Context, Key

ctx = Context('words')

keymap = {
    'state command': 'cmd',
    'state control': 'ctrl',
    'state option': 'opt',

    'state cycling': 'cyclom',
    'state doctor': 'docker',
    'state for each': 'forEach',
    'state jason': 'JSON',
    'state git': 'git',
    'state gist': 'gist',
    'state hero': 'heroku',
    'state will': 'twilio',
    'state with': 'width',
    'state them': 'vim',
    'state static': 'static ',
    'state string': 'JSON.stringify',
    'state no': 'null',
    'state no super': 'NULL',
    'state printf': 'printf',
    'state define': 'def ',
    'state import': 'import ',
    'dot company': '.com',
}

ctx.keymap(keymap)
