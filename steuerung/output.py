import RPi.GPIO as GPIO

class pump(object):
    """docstring for pumpe."""

    def __init__(self, actor_id, run_pin, ready_pin, feedback_pin):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.actor_id = actor_id
        self.run_pin = run_pin
        self.ready_pin = ready_pin
        self.feedback_pin = feedback_pin

        GPIO.setup(run_pin, GPIO.OUT)
        GPIO.setup(ready_pin, GPIO.IN)
        GPIO.setup(feedback_pin, GPIO.IN)
        GPIO.output(self.run_pin, GPIO.HIGH)


    def set_run(self, bit):
        if bit and self.get_ready():
            GPIO.output(self.run_pin, GPIO.LOW)
        else:
            GPIO.output(self.run_pin, GPIO.HIGH)

    def get_ready(self):
        return GPIO.input(self.ready_pin)
    def get_feedback(self):
        return GPIO.input(self.feedback_pin)

class ventil(object):
    """docstring for ventil."""

    def __init__(self, actor_id, pin):
      self.actor_id = actor_id
      self.pin = pin
      GPIO.setwarnings(False)
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.pin, GPIO.OUT)
      GPIO.output(self.pin, GPIO.HIGH)

    def close(self):
      GPIO.output(self.pin, GPIO.HIGH)
    def open(self):
      GPIO.output(self.pin, GPIO.LOW)
