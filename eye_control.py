import eye_mouse
import eye_zoom_mouse
from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('eye_control')
ctx.keymap({
    'camera debug':   lambda m: eye_mouse.on_menu('Eye Tracking >> Show Debug Overlay'),
    'camera pause':   lambda m: eye_mouse.on_menu('Eye Tracking >> Control Mouse'),
    'camera overlay':  lambda m: eye_mouse.on_menu('Eye Tracking >> Show Camera Overlay'),
    'camera pop':  lambda m: eye_zoom_mouse.on_menu('Eye Tracking >> Control Mouse (Zoom)'),
    'camera calibrate': lambda m: eye_mouse.on_menu('Eye Tracking >> Calibrate'),
})
