# BMP180 氣壓感測模組  
ESP32-S3 × MicroPython 教學

---

## 模組介紹

BMP180 是一款常見的 **氣壓與溫度感測模組**，  
可透過氣壓變化推算高度，常用於氣象、戶外與高度量測應用。

**模組特性：**
- 通訊介面：I2C  
- 氣壓範圍：300 ~ 1100 hPa  
- 內建溫度補償  
- 常見 I2C 位址：`0x77`

---

## 接線方式（Seeed XIAO ESP32-S3）

| BMP180 | ESP32-S3 |
|------|----------|
| VCC  | 3V3      |
| GND  | GND      |
| SDA  | GPIO 5   |
| SCL  | GPIO 6   |

📌 BMP180 為 I2C 裝置，不需要外接上拉電阻。

---

## MicroPython 範例程式（單次測量）

以下程式碼 **不使用 `while` 迴圈**，  
上電後只會測量一次溫度、氣壓與高度。

```python
from machine import I2C, Pin
import time
import ustruct

# 初始化 I2C
i2c = I2C(1, scl=Pin(6), sda=Pin(5), freq=100000)

# BMP180 I2C 位址
BMP180_ADDR = 0x77

# 讀取校正資料
def read_calibration():
    data = i2c.readfrom_mem(BMP180_ADDR, 0xAA, 22)
    return ustruct.unpack(">hhhHHhhhhhh", data)

AC1, AC2, AC3, AC4, AC5, AC6, B1, B2, MB, MC, MD = read_calibration()

# 讀取原始溫度
def read_raw_temp():
    i2c.writeto_mem(BMP180_ADDR, 0xF4, b'\x2E')
    time.sleep_ms(5)
    raw = i2c.readfrom_mem(BMP180_ADDR, 0xF6, 2)
    return ustruct.unpack(">H", raw)[0]

# 讀取原始氣壓
def read_raw_pressure():
    i2c.writeto_mem(BMP180_ADDR, 0xF4, b'\x34')
    time.sleep_ms(8)
    msb = i2c.readfrom_mem(BMP180_ADDR, 0xF6, 1)[0]
    lsb = i2c.readfrom_mem(BMP180_ADDR, 0xF7, 1)[0]
    xlsb = i2c.readfrom_mem(BMP180_ADDR, 0xF8, 1)[0]
    return ((msb << 16) + (lsb << 8) + xlsb) >> 8

# 計算溫度
UT = read_raw_temp()
X1 = ((UT - AC6) * AC5) >> 15
X2 = (MC << 11) // (X1 + MD)
B5 = X1 + X2
temperature = ((B5 + 8) >> 4) / 10

# 計算氣壓
UP = read_raw_pressure()
B6 = B5 - 4000
X1 = (B2 * (B6 * B6 >> 12)) >> 11
X2 = (AC2 * B6) >> 11
X3 = X1 + X2
B3 = ((AC1 * 4 + X3) + 2) >> 2
X1 = (AC3 * B6) >> 13
X2 = (B1 * ((B6 * B6) >> 12)) >> 16
X3 = (X1 + X2 + 2) >> 2
B4 = (AC4 * (X3 + 32768)) >> 15
B7 = (UP - B3) * 50000

if B7 < 0x80000000:
    pressure = (B7 * 2) // B4
else:
    pressure = (B7 // B4) * 2

# 計算高度
altitude = 44330 * (1 - (pressure / 101325) ** (1 / 5.255))

print("溫度:", temperature, "°C")
print("氣壓:", pressure, "Pa")
print("高度:", altitude, "m")
