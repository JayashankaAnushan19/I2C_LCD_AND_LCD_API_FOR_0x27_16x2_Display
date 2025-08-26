# I2C_LCD and LCD_API

A simple Python script to connect and control a 16x2 I2C LCD (0x27) display using an ESP32-S3. Perfect for displaying text from your ESP32S3 projects with minimal hassle.

## Features
- Easy connection via I2C (no need for tons of wires)
- Supports basic commands like:
  - Displaying text
  - Clearing the screen
  - Cursor control
- Works with 0x27 I2C 16x2 LCD modules

## Requirements
- ESP32-S3 board
- MicroPython installed on ESP32-S3
- 16x2 I2C LCD (address 0x27)
- ```machine``` and ```time``` modules (built-in in MicroPython)

## Wiring
| ESP32-S3 Pin | LCD Pin |
| ------------ | ------- |
| 3.3V / 5V    | VCC     |
| GND          | GND     |
| GPIO21 (SDA) | SDA     |
| GPIO22 (SCL) | SCL     |

```Note: You can use different GPIOs for SDA and SCL. Just update your code accordingly.```

## Usage
1. Copy your ```.py``` file to the ESP32-S3 using Thonny, ampy, or mpremote.
2. Import your module in ```main.py``` or the REPL:
```
from i2c_lcd import I2C_LCD

# Initialize LCD
lcd = I2C_LCD(sda=21, scl=22, i2c_addr=0x27)

# Display text
lcd.clear()
lcd.print("Hello, ESP32-S3!")
lcd.set_cursor(0, 1)
lcd.print("16x2 I2C LCD Rocks!")
```
3. Enjoy seeing your ESP32-S3 flex on the LCD! 😎

## Troubleshooting
- Make sure your LCD address is correct (```0x27``` by default).
- Double-check your wiring. SDA/SCL swapped? LCD stays blank.
- Pull-up resistors may be needed if display flickers.

  ## Contributing
  Feel free to fork, modify, and PR improvements. Let’s make ESP32S3 + I2C LCD projects epic. 🚀
