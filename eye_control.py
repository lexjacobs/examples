import eye
from talon.voice import Word, Context, Key, Rep, Str, press

ctx = Context('eye_control')
ctx.keymap({
    'camera debug': lambda m: eye.on_menu('Eye Tracking >> Show Debug Overlay'),
    '(sluggish | camera mouse | camera pause)': lambda m: eye.on_menu('Eye Tracking >> Control Mouse'),
    'camera overlay': lambda m: eye.on_menu('Eye Tracking >> Show Camera Overlay'),
    'camera calibration': lambda m: eye.on_menu('Eye Tracking >> Calibrate'),
})
