from machine import TouchPad, Pin
import time

# 使用 GPIO1 的 Touch 功能
touch = TouchPad(Pin(1))

# 根據實測數值設定門檻
# 未觸碰：約 17331
# 觸  碰：約 147034
THRESHOLD = 50000

# 進入無限迴圈
# ⚠️ 若要停止程式，需在 Thonny 按兩次 Ctrl + C
while True:
    # 讀取觸控感測值
    # ⚠️ ESP32S3 的 Touch：
    #   - 沒碰時：數值通常較小
    #   - 觸碰時：數值會變得很大
    val = touch.read()
    
    # 將原始數值印出來，方便觀察與校正門檻
    print(val)

    # 判斷是否「被觸碰」
    # 門檻值需依實際環境調整（電線長度、濕度、人體）
    if val > THRESHOLD:
        print("⚡ GPIO1 被觸碰")
        
    # 稍作延遲，避免刷太快
    time.sleep(0.1)

