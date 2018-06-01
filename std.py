from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import ctrl, clip
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

alpha_alt = 'air bat cap die each fail gone harm sit jury crash look mad near odd pit quest red sun trap urge vest whale box yes zip'.split()
alnum = list(zip(alpha_alt, string.ascii_lowercase)) + [(str(i), str(i)) for i in range(0, 10)]

alpha = {}
alpha.update(dict(alnum))
# alpha.update({'ship %s' % word: letter for word, letter in zip(alpha_alt, string.ascii_uppercase)})

extra_modifier_key_targets = {'left':'left','right':'right','up':'up','down':'down','minus':'-','plus':'+','(return|enter)':'enter','slash':'/','delete':'backspace','space':'space','index right':']','index left':'[','escape':'esc'}
for (k, v) in extra_modifier_key_targets.items():
    alnum.append((k, v))

alpha.update({'control %s' % k: Key('ctrl-%s' % v) for k, v in alnum})
alpha.update({'command %s' % k: Key('cmd-%s' % v) for k, v in alnum})
alpha.update({'command shift %s' % k: Key('cmd-shift-%s' % v) for k, v in alnum})
alpha.update({'alt %s' % k: Key('alt-%s' % v) for k, v in alnum})

alpha.update({'shift %s' % k: Key('shift-%s' % v) for k, v in alnum})
alpha.update({'control shift %s' % k: Key('ctrl-shift-%s' % v) for k, v in alnum})
alpha.update({'control option %s' % k: Key('ctrl-alt-%s' % v) for k, v in alnum})
alpha.update({'command control %s' % k: Key('cmd-ctrl-%s' % v) for k, v in alnum})
alpha.update({'command option %s' % k: Key('cmd-alt-%s' % v) for k, v in alnum})
alpha.update({'option %s' % k: Key('alt-%s' % v) for k, v in alnum})
alpha.update({'option shift %s' % k: Key('alt-shift-%s' % v) for k, v in alnum})

mapping = {
    'semicolon': ';',
    'new-line': '\n',
    'new-paragraph': '\n\n',
}
punctuation = set('.,–!?')

token_replace = {
    'et cetera': 'etc',
    'e-mail': 'email',
    'I\\pronoun': 'I',
    'I\'m': 'I\'m',
    'I\'ve': 'I\'ve',
    'I\'d': 'I\'d',
}

def parse_word(word):
    word = str(word)
    if word in token_replace:
        word = token_replace.get(word)
    else:
        word = word.lower()
    word = word.lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

def join_words(words, sep=' '):
    out = ''
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += word
    return out

def parse_words(m):
    return list(map(parse_word, m.dgndictation[0]._words))

def insert(s):
    Str(s)(None)

def text(m):
    insert(join_words(parse_words(m)))

def sentence_text(m):
    insert(join_words(capitalize(parse_words(m))))

def capitalize(words):
    return [words[0].capitalize()] + words[1:]

def word(m):
    text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
    insert(text.lower())

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
    'squash':  (False,  lambda i, word, _: word),
    # spinal or kebab?
    'spine':  (True,  lambda i, word, _: word if i == 0 else '-'+word),
    'title':  (False, lambda i, word, _: word.capitalize()),
    # 'allcaps': (False, lambda i, word, _: word.upper()),
    'dubstring': (False, surround('"')),
    'string': (False, surround("'")),
    'padded': (False, surround(" ")),
    'pickle': (True,  lambda i, word, _: word if i == 0 else ''),
    'rockthirteen':  (False, rot13),
    'pathway':  (True, lambda i, word, _: word if i == 0 else '/'+word),
    'dotsway':  (True, lambda i, word, _: word if i == 0 else '.'+word),
    'yellsnik':  (True, lambda i, word, _: word.capitalize() if i == 0 else '_'+word.capitalize()),
    'champion': (True, lambda i, word, _: word.capitalize() if i == 0 else " "+word),
    'criff': (True, lambda i, word, _: word.capitalize()),
    'yeller': (False, lambda i, word, _: word.upper()),
    'thrack': (True, lambda i, word, _: word[0:3]),
    'quattro': (True, lambda i, word, _: word[0:4]),
}

def FormatText(m):
    fmt = []
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    try:
        words = parse_words(m)
    except AttributeError:
        with clip.capture() as s:
            press('cmd-c')
        words = s.get().split(' ')
        if not words:
            return

    # Ensure multi-word phrases are single words
    tmp = []
    for word in words:
        tmp.extend(word.split())
    words = tmp

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

ctx = Context('input')

keymap = {}
keymap.update(alpha)
keymap.update({
    'oh <dgndictation> [over]': text,
    'word <dgnwords>': word,

    'sentence <dgndictation> [over]': [' ', sentence_text],
    'champ <dgndictation> [over]': sentence_text,
    'comma <dgndictation> [over]': [', ', text],
    'more <dgndictation> [over]': [' ', text],
    'period <dgndictation> [over]': ['. ', sentence_text],

    '(%s)+ [<dgndictation>]' % (' | '.join(formatters)): FormatText,

    'tab':   Key('tab'),
    'tarp':   Key('shift-tab'),
    'left':  Key('left'),
    'right': Key('right'),
    'up':    Key('up'),
    'down':  Key('down'),

    'delete': Key('backspace'),

    'slap': [Key('cmd-right enter')],
    'enter': Key('enter'),
    'shock': Key('cmd-shift-enter'),
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
    # '(and sign | ampersand | amper)': '&',
    '(ampersand | amper)': '&',
    'pipe': '|',

    # '(dubquote | double quote)': '"',
    'dubquote': '"',
    'quote': "'",
    'triple quote': "'''",
    # '(dot | period)': '.',
    'dot': '.',
    '(comma | pebble)': ',',
    'space': ' ',
    '[forward] slash': '/',
    'backslash': '\\',

    '(dot dot | dotdot)': '..',
    'elipses': '...',
    'cd': 'cd ',
    'cd talon home': 'cd {}'.format(TALON_HOME),
    'cd talon user': 'cd {}'.format(TALON_USER),
    'cd talon plugins': 'cd {}'.format(TALON_PLUGINS),

    'run make (durr | dear)': 'mkdir ',
    'run get': 'git ',
    'run get (R M | remove)': 'git rm ',
    'run get add': 'git add ',
    'run get add dot': 'git add .\n',
    'run get amend': 'git add .; git commit --amend --no-edit\n',

    'run get bisect': 'git bisect ',
    'run get branch': 'git branch ',
    'run get checkout': 'git checkout ',
    'run get clone': 'git clone ',
    'run get commit': 'git commit ',
    # 'run get diff': 'git diff ',
    'run get diff': 'git diff \n',
    'run get fetch': 'git fetch ',
    'run get grep': 'git grep ',
    # 'run get in it': 'git init ',
    'run get in it': 'git init \n',
    'run get log': 'git log ',
    'run get merge': 'git merge ',
    'run get move': 'git mv ',
    'run get pull': 'git pull ',
    'run get push': 'git push ',
    'run get push origin': 'git push origin ',
    'run get push origin master': 'git push origin master ',
    'run get rebase': 'git rebase ',
    'run get reset': 'git reset ',
    'run get show': 'git show ',
    # 'run get status': 'git status ',
    'run get status': 'git status \n',
    'run get tag': 'git tag ',
    'run (them | vim)': 'vim ',
    # 'run L S': 'ls\n',
    'run (L S|ellis)': 'ls -a \n',
    'dot pie': '.py',
    'run make': 'make\n',
    'run jobs': 'jobs\n',

    # 'const': 'const ',
    'state const': 'const ',
    # 'static': 'static ',
    # 'tip pent': 'int ',
    # 'tip char': 'char ',
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
    # 'tip float': 'float ',
    # 'tip double': 'double ',

    'args': ['()', Key('left')],
    'args left': '(',
    'args right': ')',
    'index': ['[]', Key('left')],
    'index left': '[',
    'index right': ']',
    'block left': '{',
    'block right': '}',
    'block': [' {}', Key('left enter')],
    'block super': [' {}', Key('left enter enter up tab')],
    'empty array': '[]',
    'empty object': '{}',

    'state (def | deaf | deft)': 'def ',
    # 'state else if': 'elif ',
    # 'state if': 'if ',
    'state if': ['if ()', Key('left')],
    'state else': [' else {}', Key('left'), Key('enter')],
    'state else if': [' else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    # 'state for': 'for ',
    'state for': 'for`',
    'state switch': ['switch ()', Key('left')],
    'state case': ['case \nbreak;', Key('up')],
    # 'state goto': 'goto ',
    'state import': 'import ',
    'state class': 'class ',
    'state let': 'let ',
    'state function': 'function ',
    'state return': 'return ',
    'state var': 'var ',
    'state variable': 'var ',

    # 'state include': '#include ',
    # 'state include system': ['#include <>', Key('left')],
    # 'state include local': ['#include ""', Key('left')],
    # 'state type deaf': 'typedef ',
    # 'state type deaf struct': ['typedef struct {\n\n};', Key('up'), '\t'],

    'comment see': '// ',
    'comment py': '# ',

    'word queue': 'queue',
    'word eye': 'eye',
    # 'word bson': 'bson',
    # 'word iter': 'iter',
    # 'word no': 'NULL',
    'word no': 'null',
    'word cmd': 'cmd',
    # 'word dup': 'dup',
    # 'word streak': ['streq()', Key('left')],
    # 'word printf': 'printf',
    # 'word (dickt | dictionary)': 'dict',
    'word shell': 'shell',

    'snippet console': 'cl`',
    'snippet shrug': 'shrug`',
    'snippet spooky': 'spooky`',

    # 'word lunixbochs': 'lunixbochs',
    'word talon': 'talon',
    # 'word Point2d': 'Point2d',
    # 'word Point3d': 'Point3d',
    # 'title Point': 'Point',
    'word angle': 'angle',

    'dunder in it': '__init__',
    'self taught': 'self.',
    'teapot': 'this.',
    'dickt in it': ['{}', Key('left')],
    'list in it': ['[]', Key('left')],
    'string utf8': "'utf8'",
    # 'state past': 'pass',

    'tinker': '`',
    'tinker triple': '```',
    'equals': '=',
    # '(minus | dash)': '-',
    'minus': '-',
    'plus': '+',
    # 'arrow': '->',
    'opera arrow': ' -> ',
    'call': '()',
    # 'indirect': '&',
    # 'dereference': '*',
    # '(op equals | assign)': ' = ',
    'assign': ' = ',
    # 'op (minus | subtract)': ' - ',
    'opera minus': ' - ',
    # 'op (plus | add)': ' + ',
    'opera plus': ' + ',
    # 'op (times | multiply)': ' * ',
    'opera (times | multiply)': ' * ',
    # 'op divide': ' / ',
    'opera divide': ' / ',
    # 'op mod': ' % ',
    'opera mod': ' % ',
    # '[op] (minus | subtract) equals': ' -= ',
    'opera minus equals': ' -= ',
    # '[op] (plus | add) equals': ' += ',
    'opera plus equals': ' += ',
    # '[op] (times | multiply) equals': ' *= ',
    'opera times equals': ' *= ',
    # '[op] divide equals': ' /= ',
    'opera divide equals': ' /= ',
    # '[op] mod equals': ' %= ',

    # '(op | is) greater [than]': ' > ',
    'opera greater': ' > ',
    # '(op | is) less [than]': ' < ',
    'opera less]': ' < ',
    # '(op | is) equal': ' == ',
    'opera equal': ' === ',
    # '(op | is) not equal': ' != ',
    'opera not equal': ' !== ',
    # '(op | is) greater [than] or equal': ' >= ',
    'opera greater equal': ' >= ',
    # '(op | is) less [than] or equal': ' <= ',
    'opera less equal': ' <= ',
    # '(op (power | exponent) | to the power [of])': ' ** ',
    'opera power': ' ** ',
    # 'op and': ' && ',
    'opera and': ' && ',
    # 'op or': ' || ',
    'opera or': ' || ',
    'opera question': ' ? ',
    'opera colon': ' : ',
    '[op] (logical | bitwise) and': ' & ',
    # '[op] (logical | bitwise) or': ' | ',
    'opera pipe': ' | ',
    # '(op | logical | bitwise) (ex | exclusive) or': ' ^ ',
    # '[(op | logical | bitwise)] (left shift | shift left)': ' << ',
    # '[(op | logical | bitwise)] (right shift | shift right)': ' >> ',
    # '(op | logical | bitwise) and equals': ' &= ',
    # '(op | logical | bitwise) or equals': ' |= ',
    # '(op | logical | bitwise) (ex | exclusive) or equals': ' ^= ',
    # '[(op | logical | bitwise)] (left shift | shift left) equals': ' <<= ',
    # '[(op | logical | bitwise)] (right shift | shift right) equals': ' >>= ',

    # 'shebang bash': '#!/bin/bash -u\n',

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

    # 'scroll down': [Key('down')] * 30,
    'scroll up': [Key('pageup')],
    # 'scroll up': [Key('up')] * 30,
    'scroll down': [Key('pagedown')],
    'scroll top': [Key('cmd-up')],
    'scroll bottom': [Key('cmd-down')],
})
ctx.keymap(keymap)
