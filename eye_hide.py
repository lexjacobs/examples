# import time
#
# from talon import ctrl, tap, ui, cron
# from eye_mouse import tracker, mouse, Point2d
#
# class EyeHide:
#     def __init__(self):
#         self.job = None
#         self.show = False
#         tracker.register('post:gaze', self.on_gaze)
#         ui.register('win_focus', self.on_focus)
#         ui.register('app_activate', self.on_focus)
#
#     def on_focus(self, win):
#         ctrl.cursor_visible(self.show)
#
#     def on_gaze(self, b):
#         if mouse.last_ctrl and mouse.break_force > 6:
#             self.cursor(True)
#         else:
#             try:
#                 # hides after every eye jump until a head movement
#                 origin = mouse.origin
#                 frames = [xy for xy in mouse.xy_hist if xy.ts >= origin.ts]
#                 m = max([(origin - xy).len() for xy in frames])
#                 self.cursor(m > 5)
#
#                 return
#                 # this variant hides the cursor on every eye jump until it settles (can tweak radius up to 200)
#                 p, origin, radius = mouse.zone1
#                 self.cursor(radius > 20)
#             except Exception:
#                 self.cursor(True)
#
#     def cursor(self, show):
#         now = time.time()
#         if show:
#             self.last_show = now
#         elif self.show and now - self.last_show < 0.5:
#             return
#
#         if show != self.show:
#             self.job = None
#             ctrl.cursor_visible(show)
#             self.show = show
#
# hide = EyeHide()
