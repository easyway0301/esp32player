# B05 – HC-SR04 超音波測距教學（ESP32-S3 + MicroPython）

本章示範如何使用常見的 **超音波測距模組 HC-SR04** 搭配 **Seeed XIAO ESP32-S3**  
透過 MicroPython 量測距離，自動測 10 秒後結束。

👉 線上 SOP 教學頁：  
https://easyway0301.github.io/Seeed%20Xiao%20Esp32S3%20With%20MicroPython/B05-HC-SR04/sop.html

---

## 📌 一、模組介紹

HC-SR04 是常見的超音波測距感測器，可非接觸式測量距離。  
利用超音波發射與接收時間差計算物體距離。

### 📍 模組特性

- 測距範圍：約 2 cm ～ 400 cm  
- 通訊方式：TRIG / ECHO  
- 距離計算公式：聲速 × 時間 ÷ 2 :contentReference[oaicite:1]{index=1}

---

## 🔌 二、接線方式（Seeed XIAO ESP32-S3）

將超音波模組與 ESP32-S3 接線如下：

| HC-SR04 腳位 | XIAO ESP32-S3 |
|--------------|---------------|
| VCC          | 5V（或依模組需求） |
| GND          | GND |
| TRIG         | GPIO 9 |
| ECHO         | GPIO 8 |

⚠️ 若 ECHO 腳位為 5 V 輸出，請透過分壓或邏輯電平轉換器保護 ESP32 腳位。 :contentReference[oaicite:2]{index=2}

---
### 引腳示意圖（參考）
![HC-SR04 示意圖](HC-SR04.jpeg)
![Pin List](Pin-List.png)

圖片來源：Seeed Studio 官方文件
[https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/](https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/)

---

## 🧑‍💻 三、MicroPython 程式範例（10 秒測試）

以下程式碼可在 Thonny 等 MicroPython IDE 上執行，  
每秒測量一次距離，總共執行 10 秒後結束。

```python
from machine import Pin, time_pulse_us   # 匯入 Pin 與脈衝測量
import time                               # 匯入時間模組

# === 腳位設定 ===
TRIG = Pin(9, Pin.OUT)                    # TRIG 為輸出腳位
ECHO = Pin(8, Pin.IN)                     # ECHO 為輸入腳位

def get_distance_mm():
    # 觸發超音波（發送 10 微秒脈衝）
    TRIG.value(0)
    time.sleep_us(2)
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)

    # 測量 ECHO 迴波高電位時間（微秒）
    duration = time_pulse_us(ECHO, 1, 30000)

    # 若回傳 <0，代表測量失敗
    if duration < 0:
        return None

    # 計算距離（毫米）
    distance_mm = (duration * 343) / (2 * 1000)
    return distance_mm

# === 開始測量並計時 ===
start_time = time.time()

while time.time() - start_time < 10:
    dist_mm = get_distance_mm()
    if dist_mm is not None:
        dist_cm = dist_mm / 10
        print("距離: {:.2f} cm ({:.2f} mm)".format(dist_cm, dist_mm))
    else:
        print("測量失敗")
    time.sleep(1)   # 每秒量測一次
