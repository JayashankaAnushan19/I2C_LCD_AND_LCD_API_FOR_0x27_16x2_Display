# 🔧 I2C LCD API for ESP32-S3

A lightweight MicroPython library for interfacing with 16x2 I2C LCD displays (0x27) using the ESP32-S3. This module provides a simple and structured API for displaying text and controlling the LCD in embedded and robotics projects.

---

## 🚀 Overview

This project simplifies communication between the ESP32-S3 and a 16x2 I2C LCD module by abstracting low-level I2C operations into an easy-to-use Python interface.

It is designed for rapid prototyping and integration into embedded systems where visual feedback is required.

---

## ✨ Features

* Simple I2C-based communication (minimal wiring)
* High-level API for LCD control
* Supports:

  * Text display
  * Screen clearing
  * Cursor positioning
* Compatible with standard 16x2 LCD modules (I2C address `0x27`)
* Lightweight and optimized for MicroPython

---

## 🧠 Use Cases

* Embedded system debugging output
* Robotics status display (sensor data, states, alerts)
* User interface for microcontroller projects
* Educational and prototyping applications

---

## ⚙️ Requirements

* ESP32-S3 development board
* MicroPython firmware
* 16x2 I2C LCD module (0x27)
* Built-in MicroPython modules:

  * `machine`
  * `time`

---

## 🔌 Wiring

| ESP32-S3 Pin | LCD Pin |
| ------------ | ------- |
| 3.3V / 5V    | VCC     |
| GND          | GND     |
| GPIO21 (SDA) | SDA     |
| GPIO22 (SCL) | SCL     |

**Note:** SDA and SCL pins can be reassigned in the code if needed.

---

## ▶️ Usage

1. Upload the module to your ESP32-S3 using tools like Thonny, `ampy`, or `mpremote`.

2. Import and initialize:

```python id="j2k9ls"
from i2c_lcd import I2C_LCD

lcd = I2C_LCD(sda=21, scl=22, i2c_addr=0x27)
```

3. Display text:

```python id="8w3p1x"
lcd.clear()
lcd.print("Hello, ESP32-S3!")
lcd.set_cursor(0, 1)
lcd.print("16x2 I2C LCD")
```

---

## ⚠️ Troubleshooting

* Ensure the correct I2C address (`0x27` by default)
* Verify wiring connections (SDA/SCL)
* Use I2C scanner to confirm device address
* Add pull-up resistors if communication is unstable

---

## 🔮 Future Improvements

* Support for multiple LCD sizes
* Custom character generation
* Scrolling text support
* Integration with sensor dashboards
* ROS 2 / robotics system display integration

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests for improvements or new features.

---

## 👨‍💻 Author

Developed by **Jayashanka Anushan**
