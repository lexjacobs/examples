from talon.voice import Context
from talon.voice import Rep, RepPhrase

ctx = Context('repetition')

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
