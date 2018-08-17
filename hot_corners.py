# from talon.dispatch import Dispatch
# from talon import ui, tap, voice
# from user import speech_toggle
#
# class EdgeFilter:
#     def __init__(self):
#         self.value = None
#
#     def __call__(self, value):
#         if value != self.value:
#             self.value = value
#             return value
#         return None
#
# class HotCorners(Dispatch):
#     def __init__(self):
#         super().__init__()
#         tap.register(tap.MMOVE, self.on_move)
#         self.top_left  = EdgeFilter()
#         self.top_right = EdgeFilter()
#         self.bot_left  = EdgeFilter()
#         self.bot_right = EdgeFilter()
#
#     def on_move(self, typ, e):
#         for screen in ui.screens():
#             right = screen.rect.right - e.x < 2
#             left = e.x - screen.rect.left < 2
#             top = e.y - screen.rect.top < 2
#             bot = screen.rect.bot - e.y < 2
#             corners = [
#                 (top and left,  'top_left',  self.top_left),
#                 (top and right, 'top_right', self.top_right),
#                 (bot and left,  'bot_left',  self.bot_left),
#                 (bot and right, 'bot_right', self.bot_right),
#             ]
#             for val, sig, filt in corners:
#                 val = filt(val)
#                 if val is True: self.dispatch(sig, 'enter')
#                 if val is False: self.dispatch(sig, 'exit')
#
# hot_corners = HotCorners()
#
# def toggle_speech(e):
#     speech_toggle.set_enabled(e == 'exit')
#
# hot_corners.register('top_left', toggle_speech)
