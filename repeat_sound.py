import threading, logging
from talon.voice import Context, Rep, talon
from talon.audio import noise
from talon import cron

context = Context('repeat_sound')


class Repeater:
    def __init__(self, initial_delay = '500ms', repeat_delay = '100ms'):
        self.initial_delay = initial_delay
        self.repeat_delay = repeat_delay
        self.job = None
        self.lock = threading.RLock()
        self.enable()

    def disable(self):
        noise.unregister('noise', self.on_noise)
        self.cancel()

    def enable(self):
        noise.register('noise', self.on_noise)

    def cancel(self):
        with self.lock:
            if self.job:
                cron.cancel(self.job)
                self.job = None

    def on_noise(self, noise):
        if noise == 'hiss_start' and talon.enabled:
            with self.lock:
                self.cancel()
                self.job = cron.after(self.initial_delay, self.initial)
            logging.debug('HISS START')
        elif noise == 'hiss_end' and self.job:
            logging.debug('HISS STOP')
            self.cancel()

    def initial(self):
        with self.lock:
            self.job = cron.interval(self.repeat_delay, self.repeat)
        self.repeat()

    def repeat(self):
        logging.debug('REPEAT')
        repeater = Rep(1)
        repeater.ctx = talon
        repeater(None)

repeater = Repeater()
context.keymap({
    'enable repeat': lambda m: repeater.enable(),
    'disable repeat': lambda m: repeater.disable(),
})
