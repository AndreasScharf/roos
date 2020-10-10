import time
class timer(object):
    """docstring for timer."""

    def __init__(self, id):
        self.id = id
        self.timer = 0
        self.current_time = lambda: int(round(time.time() * 1000))

    def cleartimer(self):
        self.timer = 0
    def elapsed(self):
        return self.timer and self.current_time() >= self.timer
