# # Copyright (c) Ryan Hileman, 2018
# # This file is for personal use only with the Talon project and is not licensed for redistribution in part or in whole.
#
# import time
# import math
#
# from talon import canvas, ctrl, tap, ui
# from talon.voice import Context
# from talon.track.geom import Point2d, EyeFrame
# from talon.track.filter import DwellFilter, LowPassFilter, MultiFilter
# from eye_mouse import tracker
#
# screen = ui.main_screen()
#
# rad_ratio = math.pi / 180
# def deg2rad(deg): return deg * rad_ratio
#
# class MouseJump:
#     def __init__(self):
#         self.radius = 35
#         self.dwell_filt = DwellFilter(self.radius)
#         self.drift_filt = MultiFilter(LowPassFilter, 2)
#         self.last = 0
#         self.cooldown = 0.25
#         self.last_gaze = None
#         self.gaze = None
#         self.running = False
#
#     def registerHandlers(self):
#         tap.register(tap.MMOVE, self.on_move)
#         tracker.register('gaze', self.on_gaze)
#         canvas.register('overlay', self.draw)
#         self.running = True
#
#     def unregisterHandlers(self):
#         tap.unregister(tap.MMOVE, self.on_move)
#         tracker.unregister('gaze', self.on_gaze)
#         canvas.unregister('overlay', self.draw)
#         self.running = False
#
#     def draw(self, canvas):
#         if not self.gaze or not canvas.rect.contains(self.gaze.x, self.gaze.y):
#             return False
#
#         paint = canvas.paint
#         paint.style = paint.Style.STROKE
#         paint.color = '00000022'
#         mid = canvas.x + canvas.width / 2
#
#         if self.gaze:
#             canvas.draw_circle(self.gaze.x, self.gaze.y, self.radius * 1.5)
#             paint.style = paint.Style.FILL
#             paint.color = 'cccccc22'
#             canvas.draw_circle(self.gaze.x, self.gaze.y, self.radius * 1.5)
#
#     def on_gaze(self, b):
#         now = time.time()
#         dt = 1 if self.last_gaze is None else now - self.last_gaze
#         self.last_gaze = now
#
#         # FIXME: weights duplicated from eye_mouse
#         l, r = EyeFrame(b, 'Left'), EyeFrame(b, 'Right')
#         if not l and not r:
#             self.gaze = None
#             return
#
#         weight = lambda x: max(0.25, min((0.25 + (max(x, 0) ** 1.8) / 2), 0.75))
#         lw = weight(l.gaze.x)
#         rw = 1 - weight(r.gaze.x)
#         gaze = (l.gaze * lw + r.gaze * rw) / (lw + rw)
#         gaze *= Point2d(screen.width, screen.height)
#
#         self.gaze = Point2d(*self.dwell_filt(gaze.x, gaze.y, dt)).apply(self.drift_filt, 15 * dt)
#         # ctrl.mouse(self.gaze.x, self.gaze.y)
#
#     def on_move(self, typ, e):
#         now = time.time()
#         diff = now - self.last
#         self.last = now
#         if diff < self.cooldown or not self.gaze:
#             return
#
#         old = Point2d(*ctrl.mouse_pos())
#         move = Point2d(e.dx, e.dy)
#
#         # TODO: only arm for movement if you look at a new place
#         if (self.gaze - old).len() > 250:
#             e.block()
#             jump = self.gaze + move
#             ctrl.mouse(jump.x, jump.y)
#             return
#
#             angle = move.angle()
#             off = Point2d(math.cos(deg2rad(angle)), math.sin(deg2rad(angle))) * self.radius
#             jump = self.gaze + off
#             ctrl.mouse(jump.x, jump.y)
#
#         # draw a line from cursor to gaze, intersect on circle radius
#         # if (gaze - old).len() > 250:
#         #     e.block()
#         #     ctrl.mouse(gaze.x, gaze.y)
#
# # TODO:
# # 1. track dwell locations
# # 2. if you look away from your recent dwell location, and move the mouse within a time window after, jump it to the gaze circle
# # 3. if you were already moving the mouse and you look to a new location, do nothing unless you stop and resume moving the mouse?
# # 4. if you shake the mouse or move it in roughly a circle, jump it to center gaze
#
# mouse_jump = MouseJump()
#
# def toggle(m):
#     if mouse_jump.running:
#         mouse_jump.unregisterHandlers()
#     else:
#         mouse_jump.registerHandlers()
#
# ctx = Context('mouse_jump')
#
# ctx.keymap({
#     'mouse guide': toggle
# })
