from talon.voice import Context, Key, Str

ctx = Context('words')


def shrink_word(m):
    word = str(m.dgndictation[0]._words[0]).lower()
    if not word in shrink_map:
        raise Exception('%s not in shrink map' % word)
    Str(shrink_map[word])(None)


keymap = {
    'dot company': '.com',
    'word parse integer': ['parseInt()', Key('left')],

    'word and': 'end',
    'word a sink': 'async',
    'word acxiom': 'axios',
    'word adam': 'atom',
    'word cape': 'kapyra',
    'word cycling': 'cyclom',
    'word define': 'def ',
    'word doctor': 'docker',
    'word for each': 'forEach',
    'word import': 'import ',
    'word display in line': 'display: inline-block;',
    'word display block': 'display: block;',
    'word get': 'git',
    'word get hub': 'github',
    'word glitch': 'glitch',
    'word just': 'gist',
    'word hand': 'hand',
    'word hero': 'heroku',
    'word jason': 'JSON',
    'word mongo': 'mongo',
    'word no': 'null',
    'word no super': 'NULL',
    'word nodemon': 'nodemon',
    'word postgres': 'postgres',
    'word printf': 'printf',
    'word ramda': 'ramda',
    'word (sql|sequel)': 'sequelize',
    'word slack': 'slack',
    'word string': 'JSON.stringify',
    'word ping': 'ping ',
    'word pseudo': 'sudo ',
    'word them': 'vim',
    'word two strings': 'toString',
    'word will': 'twilio',
    'word with': 'width',
    'word while': 'wow',
    'word zeppelin': 'zeplin',
    'shrink <dgndictation>': shrink_word,
}

shrink_map = {

    'administrator': 'admin',
    'alternate': 'alt',
    'apartment': 'apt',
    'applications': 'apps',
    'arguments': 'args',
    'attributes': 'attrs',
    'button': 'btn',
    'command': 'cmd',
    'compute': 'cmp',
    'context': 'ctx',
    'concatenate': 'concat',
    'configure': 'config',
    'control': 'ctrl',
    'format': 'fmt',
    'function': 'func',
    'image': 'img',
    'jason': 'json',
    'message': 'msg',
    'package': 'pkg',
    'parameter': 'param',
    'parameters': 'params',
    'source': 'src',
    'standard': 'std',
    'temporary': 'tmp',
    'text': 'txt',
    'user': 'usr',
    'user id': 'uid',
    'utilities': 'utils',
}

ctx.keymap(keymap)
