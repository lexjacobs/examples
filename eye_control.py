from talon_plugins import eye_mouse, eye_zoom_mouse
from talon_plugins.eye_mouse import tracker
from talon.voice import Context, ui
from talon import ui, eye

ctx = Context('eye_control')
ctx.keymap({
    'camera debug':   lambda m: eye_mouse.debug_overlay.toggle(),
    'camera pause':   lambda m: eye_mouse.control_mouse.toggle(),
    'camera overlay':  lambda m: eye_mouse.camera_overlay.toggle(),
    'camera pop':  lambda m: eye_zoom_mouse.toggle_zoom_mouse(not eye_zoom_mouse.zoom_mouse.enabled),
    'camera calibrate': lambda m: eye_mouse.calib_start(),
})
