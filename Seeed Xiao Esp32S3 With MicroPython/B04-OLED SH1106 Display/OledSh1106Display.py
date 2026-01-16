
from machine import Pin, I2C        # 匯入 Pin 與 I2C 類別
import sh1106                      # 匯入 SH1106 OLED 驅動
import time                        # 匯入時間模組

# === 建立 I2C 物件 ===
# scl 使用 GPIO6
# sda 使用 GPIO5
i2c = I2C(
    scl=Pin(6),                    # 設定 I2C SCL 腳位
    sda=Pin(5),                    # 設定 I2C SDA 腳位
    freq=400000                    # 設定 I2C 速度
)

# === 建立 OLED 顯示物件 ===
oled = sh1106.SH1106_I2C(
    128,                           # 螢幕寬度 128
    64,                            # 螢幕高度 64
    i2c,                           # 使用 I2C
    addr=0x3C                      # OLED I2C 位址
)

# === 清除畫面 ===
oled.fill(0)                       # 填滿黑色（清畫面）

# === 顯示文字 ===
oled.text("ESP32-S3", 0, 0)        # 在 (0,0) 顯示文字
oled.text("MicroPython", 0, 16)    # 在 (0,16) 顯示文字
oled.text("SH1106 OLED", 0, 32)    # 在 (0,32) 顯示文字

# === 更新顯示 ===
oled.show()                        # 將畫面送到 OLED

