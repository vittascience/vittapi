import time

from seeed_dht import DHT as GroveDHT

class DHT():
    def __init__(self, pin, sensor):
        self.pin = pin
        self.sensor = sensor
        self.dht = GroveDHT(self.pin, self.sensor)

    def read(self):
        humi, temp = self.dht.read()
        return humi, temp

    def read_humidity(self):
        humi = self.dht.read()[0]
        return humi

    def read_temperature(self):
        temp = self.dht.read()[1]
        return temp

