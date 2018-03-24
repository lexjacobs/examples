from talon.engine import engine
from talon.voice import Context, Key
from talon.voice import Rep, RepPhrase

ctx = Context('repetition')

mapping = {
    'one': 1,
    'one\\number': 1,
    'won': 1,
    'two': 2,
    'to': 2,
    'too': 2,
    'three': 3,
    'for': 4,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'ate': 8,
    'nine': 9
}

def repeat(m):
    words = list(map(lambda x:  x.word, m.dgndictation[0]._words))
    times = int(mapping[words[0]])
    rest = words[1:]
    print('final: ', words, times, rest)

    for x in range(0, times):
        print(rest)
        engine.mimic(rest)


keymap = {
    # 'repeat <dgndictation>': repeat,
    'wink': Rep(1),
    'creek': RepPhrase(1),
    'soup': Rep(2),
    'trace': Rep(3),
    'quarr': Rep(4),
    'fypes': Rep(5),
}

ctx.keymap(keymap)
