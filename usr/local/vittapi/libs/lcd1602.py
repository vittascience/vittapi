import smbus
import time

bus = smbus.SMBus(1)  # Utilisez le bus I2C 1
LCD_ADDRESS = 0x3E

class LCD1602():
    def __init__(self):
        self.__lcd_init()

    def __lcd_init(self):
        self.write_command(0x38)  # Mode 8 bits, 2 lignes, caractères 5x8
        self.write_command(0x0C)  # Écran allumé, curseur éteint
        self.write_command(0x01)  # Efface l'écran

    def write_command(self, cmd):
        bus.write_byte_data(LCD_ADDRESS, 0x80, cmd)
        time.sleep(0.05)

    def write_data(self, data):
        bus.write_byte_data(LCD_ADDRESS, 0x40, data)
        time.sleep(0.05)

    def setCursor(self, row, column):
        # Pour un LCD 16x2 :
        # La première ligne commence à l'adresse 0x80
        # La seconde ligne commence à l'adresse 0xC0
        if row == 0:
            address = 0x80 + column
        elif row == 1:
            address = 0xC0 + column
        else:
            raise ValueError("Invalid row number (0 or 1 allowed)")
        self.write_command(address)

    def writeTxt(self, s):
        # Tronquer le texte à 16 caractères s'il est trop long
        truncated_text = s[:16]
        
        byte_list = [ord(char) for char in truncated_text]
        bus.write_i2c_block_data(LCD_ADDRESS, 0x40, byte_list)

    def clear(self):
        self.write_command(0x01)
        
