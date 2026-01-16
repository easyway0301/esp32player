# ESP32-S3 MicroPython 入門｜LCD1602A I2C 顯示教學

本章示範如何使用 **LCD1602A I2C 顯示模組** 搭配 **Seeed XIAO ESP32-S3**  
以 **MicroPython** 顯示文字。

👉 此頁完整 SOP 教學可參考 → GitHub Pages  
https://easyway0301.github.io/Seeed%20Xiao%20Esp32S3%20With%20MicroPython/B03-LCD1602A%20I2C/sop.html

---

## 📌 第一步：認識 LCD1602A I2C 模組

LCD1602A 是一個 16×2 文字顯示器（LCD），使用 I2C 通訊只需兩條線（SDA / SCL）即可顯示文字。

📌 特點：

- 顯示尺寸：16 字 × 2 行  
- 通訊方式：I2C（SDA / SCL）  
- 常見 I2C 位址：`0x27`（部分模組為 `0x3F`）

📷 Pin List 圖片來源：  
Seeed Studio 官方文件 

---

## 🧑‍💻 第二步：MicroPython 控制範例

以下是一個可直接在 ESP32-S3 上執行的範例程式，  
可顯示兩行文字：

```python
from time import sleep_ms
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

# I2C LCD 預設位址
DEFAULT_I2C_ADDR = 0x27

# 建立 I2C & LCD 物件
i2c = I2C(scl=Pin(6), sda=Pin(5), freq=100000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

# 清除螢幕
lcd.clear()

# 顯示第一行文字
lcd.move_to(0, 0)
lcd.putstr("Hello ESP32-S3")

# 顯示第二行文字
lcd.move_to(0, 1)
lcd.putstr("LCD1602A I2C OK")

# 保持顯示
while True:
    sleep_ms(1000)
