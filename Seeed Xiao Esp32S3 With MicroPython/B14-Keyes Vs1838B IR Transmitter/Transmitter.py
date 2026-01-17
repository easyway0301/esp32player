from machine import Pin, PWM
import time

# ========= 紅外線發射設定 =========
ir = PWM(Pin(9), freq=38000, duty=0)  # GPIO 9 為紅外線發射腳位

def 發射紅外線(duration_ms):
    打開UserLed()        # 發射時 LED 亮
    ir.duty(512)        # 開啟 38kHz 紅外線
    time.sleep_ms(duration_ms)
    ir.duty(0)          # 關閉紅外線
    關掉UserLed()        # 發射結束 LED 滅


print("開始發射紅外線")
發射紅外線(500)   # 發射 0.5 秒
print("發射完成")

