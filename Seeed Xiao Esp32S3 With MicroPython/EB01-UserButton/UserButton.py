from machine import Pin
import time

# 本範例適用 XIAO ESP32S3 開發板搭配 Expansion Board Base for XIAO擴充板
# User LED 為低電位點亮（Active LOW）

# =====================
# 設定 Esp32 User LED（GPIO21）
# =====================
UserLed = Pin(21, Pin.OUT)

# =====================
# 設定 Expansion Board Base for XIAO擴充板 D1 按鈕（腳位是 GPIO2）
# =====================
Button_D1 = Pin(2, Pin.IN, Pin.PULL_UP)

def 打開UserLed():
    UserLed.value(0)   # 低電位 → 亮

def 關掉UserLed():
    UserLed.value(1)   # 高電位 → 滅

# 開機先關燈
關掉UserLed()

while True:
    if Button_D1.value() == 0:   # 按下
        打開UserLed()
    else:                        # 放開
        關掉UserLed()

    time.sleep(0.01)

