from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ctrl
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

alpha_alt = 'air bat cap die each fail gone harm sit jury crash look mad near odd pit quest red sun trap urge vest whale box yes zip'.split()
# alpha_alt = 'arch brov char dell etch fomp goof hark ice jinks koop lug mowsh nerb ork pooch quash rosh souk teek unks verge womp trex yang zooch'.split()

alnum = list(zip(alpha_alt, string.ascii_lowercase)) + [(str(i), str(i)) for i in range(0, 10)]

alpha = {}
alpha.update(dict(alnum))
# alpha.update({'sky %s' % word: letter for word, letter in zip(alpha_alt, string.ascii_uppercase)})

extra_modifier_key_targets = [{'left':'left','right':'right','up':'up','down':'down','minus':'-','plus':'+','(return|enter)':'enter','slash':'/','delete':'backspace','space':'space','index right':']','index left':'['}]
for (k, v) in extra_modifier_key_targets[0].items():
    alnum.append((k, v))

alpha.update({'control %s' % k: Key('ctrl-%s' % v) for k, v in alnum})
alpha.update({'shift %s' % k: Key('shift-%s' % v) for k, v in alnum})
alpha.update({'command %s' % k: Key('cmd-%s' % v) for k, v in alnum})
alpha.update({'command shift %s' % k: Key('cmd-shift-%s' % v) for k, v in alnum})
alpha.update({'control shift %s' % k: Key('ctrl-shift-%s' % v) for k, v in alnum})
alpha.update({'control option %s' % k: Key('ctrl-alt-%s' % v) for k, v in alnum})
alpha.update({'command control %s' % k: Key('cmd-ctrl-%s' % v) for k, v in alnum})
alpha.update({'command option %s' % k: Key('cmd-alt-%s' % v) for k, v in alnum})
alpha.update({'option %s' % k: Key('alt-%s' % v) for k, v in alnum})
alpha.update({'option shift %s' % k: Key('alt-shift-%s' % v) for k, v in alnum})
# print(alpha)

mapping = {
    'semicolon': ';',
    'new-line': '\n',
    'new-paragraph': '\n\n',
}

token_replace =  {
    'et cetera': 'etc',
    'e-mail': 'email',
    'i\\pronoun': 'I',
    'i\'m': 'I\'m',
    'i\'ve': 'I\'ve',
    'i\'d': 'I\'d',
}

def parse_word(word):
    word = token_replace.get(word, word)
    word = word.lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

def text(m):
    tmp = [str(s).lower() for s in m.dgndictation[0]._words]
    words = [parse_word(word) for word in tmp]
    Str(' '.join(words))(None)

def word(m):
    tmp = [str(s).lower() for s in m.dgnwords[0]._words]
    words = [parse_word(word) for word in tmp]
    Str(' '.join(words))(None)

def surround(by):
    def func(i, word, last):
        if i == 0: word = by + word
        if last: word += by
        return word
    return func

def rot13(i, word, _):
    out = ''
    for c in word.lower():
        if c in string.ascii_lowercase:
            c = chr((((ord(c) - ord('a')) + 13) % 26) + ord('a'))
        out += c
    return out

formatters = {
    'dunder': (True,  lambda i, word, _: '__%s__' % word if i == 0 else word),
    'camel':  (True,  lambda i, word, _: word if i == 0 else word.capitalize()),
    'snake':  (True,  lambda i, word, _: word if i == 0 else '_'+word),
    'smash':  (True,  lambda i, word, _: word),
    # 'sentence':  (False, lambda i, word, _: (' ' + word.capitalize()) if i == 0 else word),
    'swipe':  (False, lambda i, word, _: (', ' + word) if i == 0 else word),
    # 'trench':  (False, lambda i, word, _: (' ' + word) if i == 0 else word),
    'title':  (False, lambda i, word, _: word.capitalize()),
    # 'allcaps': (False, lambda i, word, _: word.upper()),
    'string': (False, surround("'")),
    'padded': (False, surround(" ")),
    # 'rotthirteen':  (False, rot13),

    'cram':  (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    'pathway':  (True, lambda i, word, _: word if i == 0 else '/'+word),
    'dotsway':  (True, lambda i, word, _: word if i == 0 else '.'+word),
    'snake':  (True, lambda i, word, _: word if i == 0 else '_'+word),
    'yellsnik':  (True, lambda i, word, _: word.capitalize() if i == 0 else '_'+word.capitalize()),
    'dollcram': (True, lambda i, word, _: '$'+word if i == 0 else word.capitalize()),
    'champ': (True, lambda i, word, _: word.capitalize() if i == 0 else " "+word),
    'lowcram': (True, lambda i, word, _: '@'+word if i == 0 else word.capitalize()),
    'criff': (True, lambda i, word, _: word.capitalize()),

    'spine':  (True, lambda i, word, _: word if i == 0 else '-'+word),
    'yeller': (False, lambda i, word, _: word.upper()),
    'thrack': (False, lambda i, word, _: word[0:3]),
    'quattro': (False, lambda i, word, _: word[0:4]),

}

def FormatText(m):
    fmt = []
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    words = [str(s).lower() for s in m.dgndictation[0]._words]

    # added modification to split tokens
    tmp = []
    for word in words:
        tmp.extend(word.split())
    words = tmp
    # end added modification

    tmp = []
    spaces = True
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words)-1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = ' '
    if not spaces:
        sep = ''
    Str(sep.join(words))(None)


def sentence_text(m):
    tmp = [str(s).lower() for s in m.dgndictation[0]._words]
    words = [parse_word(word) for word in tmp]
    words[0] = words[0].title()
    Str(' '.join(words))(None)

ctx = Context('input')

keymap = {}
keymap.update(alpha)
keymap.update({
    'say <dgndictation> [over]': text,
    # 'phrase <dgndictation> [over]': text,
    # 'word <dgnwords>': word,
    '(%s)+ <dgndictation>' % (' | '.join(formatters)): FormatText,

    'tab':   Key('tab'),
    'left':  Key('left'),
    'right': Key('right'),
    'up':    Key('up'),
    'down':  Key('down'),

    # added modifications for dictation
    'sentence <dgndictation> [over]': sentence_text,
    'comma <dgndictation> [over]': [', ', text],
    'period <dgndictation> [over]': ['. ', sentence_text],
    'more <dgndictation> [over]': [' ', text],
    # end added modifications for dictation

    # 'run commit <dgndictation>': ['git commit -m "', text, '"', Key('left')],


    'delete': Key('backspace'),

    'slap': [Key('cmd-right enter')],
    'enter': Key('enter'),
    'escape': Key('esc'),
    'question [mark]': '?',
    'tilde': '~',
    '(bang | exclamation point)': '!',
    'dollar [sign]': '$',
    'downscore': '_',
    '(semi | semicolon)': ';',
    'colon': ':',
    # '(square | left square [bracket])': '[',
    # '(rsquare | are square | right square [bracket])': ']',
    # '(paren | left paren)': '(', '(rparen | are paren | right paren)': ')',
    # '(brace | left brace)': '{', '(rbrace | are brace | right brace)': '}',
    # '(angle | left angle | less than)': '<', '(rangle | are angle | right angle | greater than)': '>',
    'angle': '<', 'rangle': '>',

    '(star | asterisk)': '*',
    # '(pound | hash [sign] | octo | thorpe | number sign)': '#',
    'pound': '#',
    'percent [sign]': '%',
    'caret': '^',
    'at sign': '@',
    '(ampersand | amper)': '&',
    'pipe': '|',

    'dubquote': '"',
    'quote': "'",
    'triple quote': "'''",
    '(dot | period)': '.',
    'comma': ',',
    'space': ' ',
    '[forward] slash': '/',
    'backslash': '\\',

    '(dot dot | dotdot)': '..',
    'elipses': '...',
    'cd': 'cd ',
    'cd talon home': 'cd {}'.format(TALON_HOME),
    'cd talon user': 'cd {}'.format(TALON_USER),
    'cd talon plugins': 'cd {}'.format(TALON_PLUGINS),

    # 'run make (durr | dear)': 'mkdir ',
    # 'run git': 'git ',
    # 'run git clone': 'git clone ',
    # 'run git diff': 'git diff ',
    # 'run git commit': 'git commit ',
    # 'run git push': 'git push ',
    # 'run git pull': 'git pull ',
    # 'run git status': 'git status ',
    # 'run git add': 'git add ',
    # 'run (them | vim)': 'vim ',
    # 'run ellis': 'ls\n',
    # 'run make': 'make\n',
    # 'run jobs': 'jobs\n',
    'dot pie': '.py',
    'teapot': 'this.',

    'state const': 'const ',
    'state static': 'static ',
    'tip pent': 'int ',
    'tip char': 'char ',
    'tip byte': 'byte ',
    # 'tip pent 64': 'int64_t ',
    # 'tip you went 64': 'uint64_t ',
    # 'tip pent 32': 'int32_t ',
    # 'tip you went 32': 'uint32_t ',
    # 'tip pent 16': 'int16_t ',
    # 'tip you went 16': 'uint16_t ',
    # 'tip pent 8': 'int8_t ',
    # 'tip you went 8': 'uint8_t ',
    # 'tip size': 'size_t',

    'args': ['()', Key('left')],
    'args left': '(',
    'args right': ')',
    'index': ['[]', Key('left')],
    'index left': '[',
    'index right': ']',
    'block': [' {}', Key('left enter')],
    'block super': [' {}', Key('left enter enter up tab')],
    # 'block': [' {}', Key('left enter')],
    'block left': '{',
    'block right': '}',
    'empty array': ['[]', Key('left')],
    'empty object': ['{}', Key('left')],

    'state (def | deaf | deft)': 'def ',
    # 'state else if': 'elif ',
    'state if': ['if ()', Key('left')],
    'state else': [' else {}', Key('left'), Key('enter')],
    'state else if': [' else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': 'for`',
    # 'state for': 'for ',
    'state switch': ['switch ()', Key('left')],
    'state case': ['case \nbreak;', Key('up')],
    # 'state goto': 'goto ',
    'state import': 'import ',
    # 'state class': 'class ',
    'state let': 'let ',
    'state return': 'return ',
    'state variable': 'var ',

    'comment see': '// ',
    'comment py': '# ',

    'state queue': 'queue',
    'state eye': 'eye',
    # 'word bson': 'bson',
    # 'word iter': 'iter',
    # 'word no': 'NULL',
    # 'word cmd': 'cmd',
    # 'word dup': 'dup',
    # 'word streak': ['streq()', Key('left')],
    # 'word printf': 'printf',
    # 'word (dickt | dictionary)': 'dict',

    # 'word lunixbochs': 'lunixbochs',

    'dunder in it': '__init__',
    'self pot': 'self.',
    # 'dickt in it': ['{}', Key('left')],
    # 'list in it': ['[]', Key('left')],
    'tinker': '`',
    # 'string utf8': "'utf8'",
    # 'state past': 'pass',

    'equals': '=',
    'minus': '-',
    'plus': '+',
    # 'arrow': '->',
    'opera arrow': ' -> ',
    'call': '()',
    # 'indirect': '&',
    # 'dereference': '*',
    'assign': ' = ',
    'opera (minus | subtract)': ' - ',
    'opera (plus | add)': ' + ',
    'opera (times | multiply)': ' * ',
    'opera divide': ' / ',
    'opera mod': ' % ',
    '[opera] (minus | subtract) equals': ' -= ',
    '[opera] (plus | add) equals': ' += ',
    '[opera] (times | multiply) equals': ' *= ',
    '[opera] divide equals': ' /= ',
    # '[opera] mod equals': ' %= ',

    '(opera | is) greater [than]': ' > ',
    '(opera | is) less [than]': ' < ',
    # '(opera | is) equal to': ' == ',
    '(opera | is) equal to': ' === ',
    '(opera | is) not equal to': ' !== ',
    # '(opera | is) greater or equal to': ' >= ',
    '(opera | is) greater equal': ' >= ',
    '(opera | is) less equal': ' <= ',
    # '(opera | is) less or equal to': ' <= ',
    # '(opera (power | exponent) | to the power [of])': ' ** ',
    'opera and': ' && ',
    'opera or': ' || ',
    # '[opera] (logical | bitwise) and': ' & ',
    '[opera] (logical | bitwise) or': ' | ',
    # '(opera | logical | bitwise) (ex | exclusive) or': ' ^ ',
    # '[(opera | logical | bitwise)] (left shift | shift left)': ' << ',
    # '[(opera | logical | bitwise)] (right shift | shift right)': ' >> ',
    # '(opera | logical | bitwise) and equals': ' &= ',
    # '(opera | logical | bitwise) or equals': ' |= ',
    # '(opera | logical | bitwise) (ex | exclusive) or equals': ' ^= ',
    # '[(opera | logical | bitwise)] (left shift | shift left) equals': ' <<= ',
    # '[(opera | logical | bitwise)] (right shift | shift right) equals': ' >>= ',

    # 'new window': Key('cmd-n'),
    # 'next window': Key('cmd-`'),
    # 'last window': Key('cmd-shift-`'),
    # 'next app': Key('cmd-tab'),
    # 'last app': Key('cmd-shift-tab'),
    # 'next tab': Key('ctrl-tab'),
    # 'new tab': Key('cmd-t'),
    # 'last tab': Key('ctrl-shift-tab'),

    # 'next space': Key('cmd-alt-ctrl-right'),
    # 'last space': Key('cmd-alt-ctrl-left'),

    'scroll up': [Key('pageup')],
    'scroll down': [Key('pagedown')],
    'scroll top': [Key('cmd-up')],
    'scroll bottom': [Key('cmd-down')],
})
ctx.keymap(keymap)
