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
    'word cycling': 'cyclom',
    'word define': 'def ',
    'word doctor': 'docker',
    'word for each': 'forEach',
    'word import': 'import ',
    'word get': 'git',
    'word get hub': 'github',
    'word gist': 'gist',
    'word hero': 'heroku',
    'word jason': 'JSON',
    'word no': 'null',
    'word no super': 'NULL',
    'word printf': 'printf',
    'word slack': 'slack',
    'word string': 'JSON.stringify',
    'word pseudo-\\\\pseudo': 'sudo ',
    'word them': 'vim',
    'word will': 'twilio',
    'word with': 'width',
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
    'image': 'img',
    'jason': 'json',
    'message': 'msg',
    'package': 'pkg',
    'parameter': 'param',
    'source': 'src',
    'standard': 'std',
    'temporary': 'tmp',
    'text': 'txt',
    'user': 'usr',
    'user id': 'uid',
    'utilities': 'utils',
}

ctx.keymap(keymap)
