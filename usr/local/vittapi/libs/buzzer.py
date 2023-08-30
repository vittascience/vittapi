import time
import RPi.GPIO as GPIO


class GroveBuzzer(object):
    def __init__(self, pin):
        self.pin = pin
        self.tone = 0
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = None
    
    def cleanup(self):
        GPIO.cleanup()

    def pitch(self, tone, duration=0.5):
        self.tone = tone
        if self.pwm:
            self.pwm.stop()
            self.pwm = None
        self.pwm = GPIO.PWM(self.pin, self.tone)
        self.pwm.ChangeFrequency(self.tone)
        self.pwm.start(50)
        time.sleep(duration)
        self.pwm.stop()
        # self.cleanup()

