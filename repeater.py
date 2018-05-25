from talon.voice import Context, Rep, talon
# from user.utils import parse_words_as_integer

import itertools

number_conversions = {
    'oh': '0', # 'oh' => zero
}
for i, w in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',]):
    number_conversions[str(i)] = str(i)
    number_conversions[w] = str(i)
    number_conversions['%s\\number'%(w)] = str(i)

def parse_words_as_integer(words):

    # Ignore any potential trailing non-number words
    number_words = list(itertools.takewhile(lambda w: w not in number_conversions, words))

    # Somehow, no numbers were detected
    if len(number_words) == 0:
        return None

    # Map number words to simple number values
    number_values = list(map(lambda w: number_conversions[w.word], number_words))

    # Filter out initial zero values
    normalized_number_values = []
    non_zero_found = False
    for n in number_values:
        if not non_zero_found and n == '0':
            continue
        non_zero_found = True
        normalized_number_values.append(n)

    # If the entire sequence was zeros, return single zero
    if len(normalized_number_values) == 0:
        normalized_number_values = ['0']

    # Create merged number string and convert to int
    return int(''.join(normalized_number_values))


ctx = Context('repeater')

def repeat(m):
    repeat_count = parse_words_as_integer(m._words[1:])

    if repeat_count != None and repeat_count >= 2:
        repeater = Rep(repeat_count - 1)
        repeater.ctx = talon
        return repeater(None)

ctx.keymap({
    'repeat (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)+': repeat,
})
