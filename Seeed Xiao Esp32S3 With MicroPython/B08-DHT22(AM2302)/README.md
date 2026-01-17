# DHT22 溫溼度感測模組  
ESP32-S3 × MicroPython 教學

---

## 模組介紹

DHT22（AM2302）是一款常見的 **數位溫溼度感測模組**，  
MicroPython 內建 `dht` 模組即可直接使用。

**模組特性：**
- 溫度範圍：-40 ~ 80°C  
- 濕度範圍：0 ~ 100% RH  
- 通訊方式：單線數位  
- 建議讀取間隔：≥ 2 秒  

---

## 接線方式（Seeed XIAO ESP32-S3）

| DHT22 | ESP32-S3 |
|-----|---------|
| VCC | 3V3 |
| GND | GND |
| DATA | GPIO 9 |

📌 DATA 腳位通常需要上拉電阻（多數模組已內建）。

---

## MicroPython 範例程式（單次測量）

```python
import machine              # 匯入 machine 模組，用來控制硬體
import time                 # 匯入 time 模組（此範例未使用延遲）
import dht                  # 匯入 DHT 感測器驅動

# 建立 DHT22 物件，資料腳位接在 GPIO9
dht22 = dht.DHT22(machine.Pin(9))

try:
    dht22.measure()         # 觸發感測器量測一次

    temp = dht22.temperature()  # 取得溫度（攝氏）
    hum = dht22.humidity()      # 取得濕度（百分比）

    # 輸出格式化結果
    print("🌡 溫度: {:.1f}°C, 💧 濕度: {:.1f}%".format(temp, hum))

except OSError as e:
    # 感測失敗時會拋出例外
    print("讀取失敗:", e)
