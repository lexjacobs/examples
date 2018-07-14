# import math
# import time
#
# from talon import ctrl, cron, tap
#
# speed = 2.0
#
# class SmoothScroll:
#     def __init__(self, speed=1.1):
#         self.speed = speed
#         tap.register(tap.SCROLL | tap.HOOK, self.on_scroll)
#         self.velocity = 0
#         self.job = None
#         self.ts = time.time()
#
#     def on_scroll(self, typ, e):
#         if e.by_line:
#             now = time.time()
#             dt = min(now - self.ts, 1)
#             self.ts = now
#             self.velocity += e.dy * dt * self.speed
#             e.block()
#             if not self.job:
#                 self.job = cron.interval('10ms', self.tick)
#
#     def tick(self):
#         self.velocity *= 0.95
#         if -0.1 < self.velocity < 0.1:
#             self.velocity = 0
#             self.job = None
#             return True
#         ctrl.mouse_scroll(by_lines=False, y=self.velocity)
#
# smooth_scroll = SmoothScroll(speed=speed)
