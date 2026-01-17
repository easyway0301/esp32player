import machine
import time
import dht

# 假設 DHT22 資料線接在 GPIO4
d = dht.DHT22(machine.Pin(4))

try:
    d.measure()  # 開始量測
    temp = d.temperature()  # 攝氏溫度
    hum = d.humidity()      # 濕度 (%)

    print("🌡 溫度: {:.1f}°C, 💧 濕度: {:.1f}%".format(temp, hum))

except OSError as e:
    print("讀取失敗:", e)

'''
📌 注意事項

接線方式 (AM2302 / DHT22 模組常見 3Pin 版)

VCC → 3.3V  接在DHT22的+

DATA → ESP32 的 GPIO (例子用 GPIO4) 擴充板上GPIO4的S接在DHT22的OUT

GND → GND

有些模組板已經內建 10kΩ 上拉電阻，若是裸晶片就要在 DATA 與 VCC 之間加一顆 10kΩ 上拉。

dht.DHT22() 與 dht.DHT11() 都可以用，但要對應正確的感測器型號。

量測不要太頻繁，官方建議 2 秒以上 才讀一次。
'''
