import math
import time
from grove.adc import ADC as GroveADC

class ADC():
    def __init__(self, channel):
        self.channel = channel
        self.adc = GroveADC()

    def read(self):
        value = self.adc.read(self.channel)
        return value
    
    def read_analog(self):
        value = self.adc.read_voltage(self.channel)
        return value

