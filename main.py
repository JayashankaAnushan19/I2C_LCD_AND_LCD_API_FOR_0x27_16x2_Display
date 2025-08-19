from machine import Pin, SoftI2C
from lcd_api import LcdApi  # Fixed: Import the class LcdApi from lcd_api module
from i2c_lcd import I2cLcd  # Fixed: Import the class I2cLcd from i2c_lcd module
from time import sleep

I2C_ADDR = 0x27  # Replace with your scanned address
NUM_ROWS = 2
NUM_COLS = 16

i2c = SoftI2C(sda=Pin(8), scl=Pin(9), freq=400000)  # Updated pins
lcd = I2cLcd(i2c, I2C_ADDR, NUM_ROWS, NUM_COLS)

try:
    lcd.putstr("Hello, ESP32-S3!")
    sleep(2)
    lcd.clear()
    lcd.move_to(0, 1)  # Move to second row
    lcd.putstr("I2C LCD Works")
    while True:
        sleep(1)
except KeyboardInterrupt:
    lcd.clear()
    print("Stopped")
