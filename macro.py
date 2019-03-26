# https://github.com/dwiel/talon_user/blob/master/macro.py
from talon.voice import Context, talon
from talon.engine import engine

macro = []
last_actions = None
macro_recording = False


def macro_record(j):
    global macro
    global last_actions
    global macro_recording

    if macro_recording:
        if j["cmd"] == "p.end" and j["path"]:
            new = talon.last_actions
            if new != last_actions:
                macro.extend(new)
                last_actions = new


def macro_start(m):
    global macro
    global macro_recording

    macro_recording = True
    macro = []


def macro_stop(m):
    global macro
    global macro_recording

    if macro_recording:
        macro = macro[1:]
        macro_recording = False


def macro_play(m):
    global macro

    macro_stop(None)

    for item in macro:
        for action, rule in item:
            act = action(rule) or (action, rule)


engine.register("post:phrase", macro_record)

ctx = Context("macro")
ctx.keymap(
    {"macro start": macro_start, "macro stop": macro_stop, "macro play": macro_play}
)
