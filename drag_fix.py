from talon import ctrl, tap

def on_move(typ, e):
    buttons = ctrl.mouse_buttons_down()
    if not e.flags & tap.DRAG and buttons:
        e.flags |= tap.DRAG
        e.button = buttons[0]
        e.modify()

tap.register(tap.MMOVE | tap.HOOK, on_move)