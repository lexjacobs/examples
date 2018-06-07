import time
from talon.voice import Context, Key, ctrl
from talon import ui

ctx = Context('mouse')


def adv_click(button, *mods, **kwargs):
    def click(e):
        for key in mods:
            ctrl.key_press(key, down=True)
        ctrl.mouse_click(button=button, **kwargs)
        for key in reversed(mods):
            ctrl.key_press(key, up=True)
    return click


def mouse_drag(m):
    ctrl.mouse_click(0, down=True)


def mouse_release(m):
    ctrl.mouse_click(0, up=True)


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
    ctrl.mouse((segmentx * spokenx + segmentx),
               (segmenty * spokeny + segmenty))


keymap = {
    'click drag': mouse_drag,
    'click release': mouse_release,
    'click left': adv_click(0),
    'click right': adv_click(1),
    'click control': adv_click(0, 'ctrl'),
    'click command': adv_click(0, 'cmd'),
    'click option': adv_click(0, 'alt'),
    'click shift': adv_click(0, 'shift'),
    'click shift alt': adv_click(0, 'alt', 'shift'),
    'click double': adv_click(0, times=2),
    'click triple': adv_click(0, times=3),
    'click shift double': adv_click(0, 'shift', times=2),
    'mouse corner': lambda m: ctrl.mouse(0, 0),
    'mouse grid (1|2|3|4|5|6|7|8|9)': mouse_grid,
}

ctx.keymap(keymap)
