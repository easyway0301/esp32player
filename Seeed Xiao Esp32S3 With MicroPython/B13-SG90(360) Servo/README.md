# ESP32-S3 MicroPython SG90 360° 伺服教學
控制旋轉方向與停止

---

## 第一部分：認識 SG90 360° 模組
SG90 360° 是連續旋轉伺服馬達，透過 PWM 脈衝控制轉速與方向。

📌 注意事項：
- 旋轉時不要超載，避免馬達燒毀  
- 避免手動強行轉動齒輪  

**接線方式：**
- 黃色線 → GPIO 9（PWM 控制訊號）  
- 紅色線 → 3V3  
- 褐色線 → GND  

---

## 第二部分：MicroPython 程式碼

以下程式碼示範正轉、停止、反轉，單次執行即可：

```python
from machine import Pin, PWM      # 匯入 Pin 與 PWM 類別
import time                        # 匯入時間模組

# === 初始化 PWM ===
pwm_pin = PWM(Pin(9))             # 將 GPIO9 設為 PWM 輸出
pwm_pin.freq(50)                   # 設定頻率 50Hz（SG90 標準）

# === 定義旋轉函式 ===
def rotate(speed_ms):
    """
    speed_ms: PWM 脈衝寬度對應 (ms)
        1.0 ~ 2.0 ms
        1.5ms 停止
    """
    duty = int(speed_ms / 20 * 1023)  # 將 20ms 週期轉成 ESP32 10bit duty
    pwm_pin.duty(duty)                 # 設定 PWM 輸出

# === 順時針慢速 ===
rotate(1.7)                          # PWM 1.7ms → 順時針轉
time.sleep(2)                         # 旋轉 2 秒

# === 停止 ===
rotate(1.5)                          # PWM 1.5ms → 停止旋轉
time.sleep(1)                         # 等待 1 秒

# === 逆時針慢速 ===
rotate(1.3)                          # PWM 1.3ms → 逆時針轉
time.sleep(2)                         # 旋轉 2 秒

# === 停止 ===
rotate(1.5)                          # 停止
time.sleep(1)                         # 等待 1 秒
