from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ui
import time
import os

running = {}
launch = {}


def switch_app(m):
    name = str(m["switcher.running"][0])
    full = running.get(name)
    if not full:
        return
    for app in ui.apps():
        if app.name == full:
            app.focus()
            # TODO: replace sleep with a check to see when it is in foreground
            time.sleep(0.25)
            break


def launch_app(m):
    name = str(m["switcher.launch"][0])
    path = launch.get(name)
    if path:
        ui.launch(path=path)


ctx = Context("switcher")
ctx.keymap(
    {"focus {switcher.running}": switch_app, "launch {switcher.launch}": launch_app}
)


def update_lists():
    global running
    global launch
    new = {}
    for app in ui.apps():
        if app.background and not app.windows():
            continue
        words = app.name.split(" ")
        for word in words:
            if word and not word in new:
                new[word] = app.name
        new[app.name] = app.name
    running = new
    ctx.set_list("running", running.keys())

    new = {}
    for base in "/Applications", "/Applications/Utilities":
        for name in os.listdir(base):
            path = os.path.join(base, name)
            name = name.rsplit(".", 1)[0]
            new[name.lower()] = path.lower()
            words = name.split(" ")
            for word in words:
                if word and word not in new:
                    if len(name) > 6 and len(word) < 3:
                        continue
                    new[word.lower()] = path.lower()
    launch = new
    ctx.set_list("launch", launch.keys())


def ui_event(event, arg):
    if event in ("app_activate", "app_launch", "app_close", "win_open", "win_close"):
        update_lists()


ui.register("", ui_event)
update_lists()
