# from talon.voice import Context, ContextGroup
# from talon.voice import talon
# from talon import app
#
# sleepy_mode = ContextGroup('wakeup')
# wakeup = Context('wakeup', group=sleepy_mode)
#
# def disengage(m):
#   sleepy_mode.disable()
#   talon.enable()
#   app.notify('sleepy mode disengaged')
#
#
# wakeup.keymap({
#   'sleepy': disengage
# })
#
# sleepy_mode.load()
#
# context = Context('sleepy')
#
# def engage_sleepy_mode(m):
#   talon.disable()
#   sleepy_mode.enable()
#   app.notify('in sleepy mode')
#
# context.keymap({
#   'sleepy': engage_sleepy_mode,
# })
