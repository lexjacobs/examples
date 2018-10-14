from talon.voice import Context, Rep, RepPhrase, talon
from user.utils import parse_words_as_integer

ctx = Context('repeater')

def repeat(m):
    repeat_count = parse_words_as_integer(m._words[1:])
    if repeat_count != None and repeat_count >= 2:
        repeater = Rep(repeat_count - 1)
        repeater.ctx = talon
        return repeater(None)

ctx.keymap({
    'creek': RepPhrase(1),
    '(rep | repeat) (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)++': repeat,
})
