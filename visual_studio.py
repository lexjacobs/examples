from talon.voice import Word, Key, Context, Str, press
import string
from user.utils import parse_words_as_integer

ctx = Context('visual_studio', bundle='com.microsoft.VSCode');

def move_to_line(m):
    line_number = parse_words_as_integer(m._words[1:])
    print('line number', line_number)
    press('ctrl-g')
    Str(str(line_number))(None)
    press('enter')

keymap = {
    '(spring) (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)++': move_to_line,
    'bracken': Key('cmd-ctrl-shift-right'),
    'tools beautify': Key('alt-shift-f'),
    'tools terminal': Key('ctrl-shift-`'),
    'window terminal next': Key('cmd-alt-right'),
    'tools tree': Key('cmd-shift-e'),
    'tools run code': Key('ctrl-alt-n'),
}

ctx.keymap(keymap)