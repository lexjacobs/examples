from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import app, ctrl, clip, ui
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

# cleans up some Dragon output from <dgndictation>
mapping = {"semicolon": ";", "new-line": "\n", "new-paragraph": "\n\n"}

# used for auto-spacing
punctuation = set(".,–!?")

token_replace = {
    "Café": "cafe",
    "crème brûlée": "creme brulee",
    "et cetera": "etc",
    "e-mail": "email",
    "I\\pronoun": "I",
    "I'll": "I'll",
    "I'm": "I'm",
    "I've": "I've",
    "I'd": "I'd",
    "JavaScript": "JavaScript",
    "meta-\\\\meta": "meta",
}


def parse_word(word):
    word = str(word)
    if word in token_replace:
        word = token_replace.get(word)
    else:
        word = word.lower()
    word = word.lstrip("\\").split("\\", 1)[0]
    word = mapping.get(word, word)
    return word


def join_words(words, sep=" "):
    out = ""
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
        if i == 0:
            word = by + word
        if last:
            word += by
        return word

    return func


def rot13(i, word, _):
    out = ""
    for c in word.lower():
        if c in string.ascii_lowercase:
            c = chr((((ord(c) - ord("a")) + 13) % 26) + ord("a"))
        out += c
    return out


formatters = {
    # 'dunder': (True,  lambda i, word, _: '__%s__' % word if i == 0 else word),
    "camel": (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    "snake": (True, lambda i, word, _: word if i == 0 else "_" + word),
    "smash": (True, lambda i, word, _: word),
    "squash": (False, lambda i, word, _: word),
    "spine": (True, lambda i, word, _: word if i == 0 else "-" + word),
    "title": (False, lambda i, word, _: word.capitalize()),
    "dubstring": (False, surround('"')),
    "string": (False, surround("'")),
    "padded": (False, surround(" ")),
    "pickle": (True, lambda i, word, _: word if i == 0 else ""),
    "rockthirteen": (False, rot13),
    "pathway": (True, lambda i, word, _: word if i == 0 else "/" + word),
    "dotsway": (True, lambda i, word, _: word if i == 0 else "." + word),
    "yellsnik": (
        True,
        lambda i, word, _: word.capitalize() if i == 0 else "_" + word.capitalize(),
    ),
    "champion": (True, lambda i, word, _: word.capitalize() if i == 0 else " " + word),
    "criff": (True, lambda i, word, _: word.capitalize()),
    "yeller": (False, lambda i, word, _: word.upper()),
    "thrack": (True, lambda i, word, _: word[0:3]),
    "quattro": (True, lambda i, word, _: word[0:4]),
}


def FormatText(m):
    fmt = []
    for w in m._words:
        # if isinstance(w, Word):
        if isinstance(w, Word) and w.word in formatters:
            fmt.append(w.word)
    try:
        words = parse_words(m)
    except AttributeError:
        with clip.capture() as s:
            press("cmd-c")
        words = s.get().split(" ")
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
            word = func(i, word, i == len(words) - 1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = " "
    if not spaces:
        sep = ""
    Str(sep.join(words))(None)


def copy_bundle(m):
    bundle = ui.active_app().bundle
    clip.set(bundle)
    app.notify("Copied app bundle", body="{}".format(bundle))


ctx = Context("input")


def CursorText(s):
    left, right = s.split("{.}", 1)
    return [left + right, Key(" ".join(["left"] * len(right)))]


keymap = {}
keymap.update(
    {
        "oh <dgndictation> [over]": text,
        "word <dgnwords>": word,
        "sentence <dgndictation> [over]": [" ", sentence_text],
        "champ <dgndictation> [over]": sentence_text,
        "coal gap <dgndictation> [over]": [": ", text],
        "swipe <dgndictation> [over]": [", ", text],
        "dot <dgndictation> [over]": [".", text],
        "glitchy <dgndictation> [over]": ["`", text, "`"],
        "more <dgndictation> [over]": [" ", text],
        "period <dgndictation> [over]": [". ", sentence_text],
        "marco <dgndictation> [over]": [Key("cmd-f"), text, Key("enter")],
        "marco project <dgndictation> [over]": [Key("cmd-shift-f"), text, Key("enter")],
        "assign <dgndictation> [over]": [" = ", text],
        "state import <dgndictation> [over]": ["import ", text],
        "state class <dgndictation> [over]": ["class ", text],
        "state constant <dgndictation> [over]": ["const ", text],
        "state let <dgndictation> [over]": ["let ", text],
        "state function <dgndictation> [over]": ["function ", text],
        "state return <dgndictation> [over]": ["return ", text],
        "state while <dgndictation> [over]": CursorText("while ({.})") + [text],
        "state (var|variable) <dgndictation> [over]": ["var ", text],
        "state (def|define) <dgndictation> [over]": ["def ", text],
        "args <dgndictation>": ["()", Key("left"), text],
        "click replace <dgndictation>": [
            lambda m: ctrl.mouse_click(button=0, times=2),
            text,
        ],
        "replace last <dgndictation>": [Key("alt-backspace"), text],
        "replace next <dgndictation>": [Key("alt-shift-right"), text],
        "tools emoji": Key("cmd-ctrl-space"),
        "pixel": "px",
        "word pixel": "pixel",
        "tools tag <dgndictation>": ["<", text, ">", "</", text, ">"],
        "tools tag": CursorText("<{.}>"),
        "(%s)+ [<dgndictation>]" % (" | ".join(formatters)): FormatText,
        "tarp": Key("shift-tab"),
        # 'left': Key('left'),
        # 'right': Key('right'),
        # 'up': Key('up'),
        # 'down': Key('down'),
        "slap": [Key("cmd-right enter")],
        "shock": Key("cmd-shift-enter"),
        "question [mark]": "?",
        "tilde": "~",
        "(bang | exclamation point)": "!",
        "dollar [sign]": "$",
        "downscore": "_",
        "(semi | semicolon)": ";",
        "colon": ":",
        "angle": "<",
        "rangle": ">",
        "(star | asterisk)": "*",
        "pound": "#",
        "percent [sign]": "%",
        "caret": "^",
        "at sign": "@",
        "(ampersand | amper)": "&",
        "pipe": "|",
        "dubquote": '"',
        "quote": "'",
        "triple quote": "'''",
        "(dot | point)": ".",
        "comma": ",",
        "pebble": ", ",
        "space": " ",
        "[forward] slash": "/",
        "backslash": "\\",
        "(dot dot | dotdot)": "..",
        "elipses": "...",
        "cd": "cd ",
        "cd talon home": "cd {}".format(TALON_HOME),
        "cd talon user": "cd {}".format(TALON_USER),
        "cd talon plugins": "cd {}".format(TALON_PLUGINS),
        "run make (durr | dear)": "mkdir ",
        "run get": "git ",
        "run get (R M | remove)": "git rm ",
        "run get add": "git add ",
        "run get add dot": "git add .\n",
        "run get amend": "git add .; git commit --amend --no-edit\n",
        "run get bisect": "git bisect ",
        "run get branch": "git branch ",
        "run get checkout": "git checkout ",
        "run get clone": "git clone ",
        "run get commit": "git commit ",
        "run get diff": "git diff \n",
        "run get fetch": "git fetch ",
        "run get grep": "git grep ",
        "run get history": "git hist \n",
        "run get in it": "git init \n",
        "run get log": "git log ",
        "run get merge": "git merge ",
        "run get move": "git mv ",
        "run get pull": "git pull ",
        "run get push": "git push ",
        "run get push origin": "git push origin ",
        "run get push origin master": "git push origin master ",
        "run get rebase": "git rebase ",
        "run get remote": "git remote -v \n",
        "run get reset": "git reset ",
        "run get show": "git show ",
        "run get stash": "git stash ",
        "run get stash pop": "git stash pop\n",
        "run get status": "git status \n",
        "run get tag": "git tag ",
        "run rim raft": "rm -rf ",
        "run (them | vim)": "vim ",
        "run (L S |ellis)": "ls -a \n",
        "dot pie": ".py",
        "run make": "make\n",
        "run jobs": "jobs\n",
        "state const": "const ",
        "tip byte": "byte ",
        "args": CursorText("({.})"),
        "args left": "(",
        "args right": ")",
        "index": CursorText("[{.}]"),
        "block left": "{",
        "block right": "}",
        "block": [" {}", Key("left enter")],
        "block super": [" {}", Key("left enter enter up tab")],
        "empty array": "[]",
        "empty object": "{}",
        "state (def | deaf | deft)": "def ",
        "state if": CursorText("if ({.})"),
        "state if not": CursorText("if (!{.})"),
        "state else": [" else {}", Key("left"), Key("enter")],
        "state else super": [" else {}", Key("left"), Key("enter enter up tab")],
        "state else if": CursorText(" else if ({.})"),
        "state while": CursorText("while ({.})"),
        # 'state for': ['for ()', Key('left')],
        "state for": "for`",
        "state switch": CursorText("switch ({.})"),
        "state case": ["case \nbreak;", Key("up")],
        "state import": "import ",
        "state class": "class ",
        "state let": "let ",
        "state function": "function ",
        "state return": "return ",
        "state var": "var ",
        "state variable": "var ",
        "comment see": "// ",
        "comment py": "# ",
        "word queue": "queue",
        "word eye": "eye",
        "word no": "null",
        "word cmd": "cmd",
        "word shell": "shell",
        "snippet console": "cl`",
        "snippet spooky": "spooky`",
        "word talon": "talon",
        "word angle": "angle",
        "dunder in it": "__init__",
        "self taught": "self.",
        "teapot": "this.",
        "dickt in it": CursorText("{{.}}"),
        "string utf8": "'utf8'",
        "tanker": "`",
        "tanker triple": "```",
        "equals": "=",
        "open arrow": " -> ",
        "call": "()",
        "assign": " = ",
        "open minus": " - ",
        "open plus": " + ",
        "open (times | multiply)": " * ",
        "open divide": " / ",
        "open mod": " % ",
        "open minus equals": " -= ",
        "open plus equals": " += ",
        "open times equals": " *= ",
        "open divide equals": " /= ",
        "open greater": " > ",
        "open less": " < ",
        "open equal": " === ",
        "open not equal": " !== ",
        "open greater equal": " >= ",
        "open less equal": " <= ",
        "open power": " ** ",
        "open and": " && ",
        "open or": " || ",
        "open question": " ? ",
        "open colon": " : ",
        "open pipe": " | ",
        "look up": [Key("pageup")],
        "look down": [Key("pagedown")],
        "look top": [Key("cmd-up")],
        "look bottom": [Key("cmd-down")],
        "ten": "10",
        "twenty": "20",
        "thirty": "30",
        "forty": "40",
        "fifty": "50",
        "sixty": "60",
        "seventy": "70",
        "eighty": "80",
        "ninety": "90",
        "chain catch": CursorText(".catch({.})"),
        "chain then": CursorText(".then({.})"),
        "tools copy bundle": copy_bundle,
    }
)


def select_text_to_left_of_cursor(m):
    words = parse_words(m)
    if not words:
        return
    old = clip.get()
    key = join_words(words).lower()
    press("shift-home", wait=2000)
    press("cmd-c", wait=2000)
    press("right", wait=2000)
    text_left = clip.get()
    clip.set(old)
    result = text_left.find(key)
    if result == -1:
        return
    # cursor over to the found key text
    for i in range(0, len(text_left) - result):
        press("left", wait=0)
    # now select the matching key text
    for i in range(0, len(key)):
        press("shift-right")


def select_text_to_right_of_cursor(m, mod):
    key = join_words(parse_words(m)).lower()
    with clip.capture() as clipboardText:
        press("cmd-shift-right")
        press("cmd-c")
        press("left")
    textRight = clipboardText.get()
    result = textRight.find(key)
    if result == -1:
        return
    # cursor over to the found key text
    for i in range(0, result):
        press(mod, wait=0)
    # now select the matching key text
    for i in range(0, len(key)):
        press("shift-right", wait=0)


keymap.update(
    {
        "crew <dgndictation> [over]": lambda m: select_text_to_right_of_cursor(
            m, mod="right"
        ),
        "trail <dgndictation> [over]": lambda m: select_text_to_left_of_cursor(m),
        "crew select <dgndictation> [over]": lambda m: select_text_to_right_of_cursor(
            m, mod="shift-right"
        ),
    }
)

ctx.keymap(keymap)
