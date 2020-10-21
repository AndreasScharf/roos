import RPi.GPIO as GPIO

relai = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relai, GPIO.OUT)
GPIO.output(relai, GPIO.HIGH)

GPIO.output(relai, GPIO.LOW)
