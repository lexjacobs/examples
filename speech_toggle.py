from talon_plugins import eye_mouse
from talon.voice import Context, ContextGroup, talon, ctrl
from talon.engine import engine
from talon_plugins import speech

sleep_group = ContextGroup("sleepy")
sleepy = Context("sleepy", group=sleep_group)

sleepy.keymap(
    {
        "talon sleep": lambda m: speech.set_enabled(False),
        "talon wake": speech.set_enabled(True),
        "dragon wake": [
            lambda m: speech.set_enabled(False),
            lambda m: engine.mimic("wake up".split()),
        ],
        "talon wake": [
            lambda m: speech.set_enabled(True),
            lambda m: engine.mimic("go to sleep".split()),
        ],
    }
)
sleep_group.load()
