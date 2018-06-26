import eye_mouse
import time
from talon import ctrl, tap
from talon.voice import Context
from talon import ui

ctx = Context('mouse')

x, y = ctrl.mouse_pos()
mouse_history = [(x, y, time.time())]
force_move = None

def on_move(typ, e):
    mouse_history.append((e.x, e.y, time.time()))
    if force_move:
        e.x, e.y = force_move
        return True
tap.register(tap.MMOVE, on_move)

def click_pos(m):
    word = m._words[0]
    start = (word.start + min((word.end - word.start) / 2, 0.100)) / 1000.0
    diff, pos = min([(abs(start - pos[2]), pos) for pos in mouse_history])
    return pos[:2]

def delayed_click(m, button=0, times=1):
    old = eye_mouse.config.control_mouse
    eye_mouse.config.control_mouse = False
    x, y = click_pos(m)
    ctrl.mouse(x, y)
    ctrl.mouse_click(x, y, button=button, times=times, wait=16000)
    time.sleep(0.032)
    eye_mouse.config.control_mouse = old

def delayed_right_click(m):
    delayed_click(m, button=1)

def delayed_dubclick(m):
    delayed_click(m, button=0, times=2)

def delayed_tripclick(m):
    delayed_click(m, button=0, times=3)

def mouse_drag(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, down=True)

def mouse_release(m):
    x, y = click_pos(m)
    ctrl.mouse_click(x, y, up=True)

def adv_click(button, *mods, **kwargs):
    def click(e):
        for key in mods:
            ctrl.key_press(key, down=True)
        ctrl.mouse_click(button=button, **kwargs)
        for key in reversed(mods):
            ctrl.key_press(key, up=True)
    return click

def mouse_grid(m):
    positions = {1: (0, 0), 2: (2, 0), 3: (4, 0), 4: (0, 2), 5: (
        2, 2), 6: (4, 2), 7: (0, 4), 8: (2, 4), 9: (4, 4)}
    position = int(str(m._words[2]))
    screen_size = ui.main_screen()
    width = screen_size.width
    height = screen_size.height
    segmentx = width / 6
    segmenty = height / 6
    spokenx = positions.get(position)[0]
    spokeny = positions.get(position)[1]
    ctrl.mouse((segmentx * spokenx + segmentx),(segmenty * spokeny + segmenty))

keymap = {
    'click right': delayed_right_click,
    'click left': delayed_click,
    'click double': delayed_dubclick,
    'click triple': delayed_tripclick,
    'click drag': mouse_drag,
    'click release': mouse_release,
    'click control': adv_click(0, 'ctrl'),
    'click command': adv_click(0, 'cmd'),
    'click option': adv_click(0, 'alt'),
    'click shift': adv_click(0, 'shift'),
    'click shift alt': adv_click(0, 'alt', 'shift'),
    'click shift double': adv_click(0, 'shift', times=2),
    'mouse corner': lambda m: ctrl.mouse(0, 0),
    'mouse grid (1|2|3|4|5|6|7|8|9)': mouse_grid,
    'move up': lambda m: ctrl.mouse(0, 0, dx=0, dy=-10),
    'move right': lambda m: ctrl.mouse(0, 0, dx=10, dy=0),
    'move left': lambda m: ctrl.mouse(0, 0, dx=-10, dy=0),
    'move down': lambda m: ctrl.mouse(0, 0, dx=0, dy=10),
}
ctx.keymap(keymap)
