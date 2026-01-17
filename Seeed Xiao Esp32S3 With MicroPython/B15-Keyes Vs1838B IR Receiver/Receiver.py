from machine import Pin
import time

# ========= VS1838B 紅外線接收 =========
ir = Pin(9, Pin.IN)

# 接收狀態旗標
收到紅外線 = False

def ir_callback(pin):
    global 收到紅外線
    收到紅外線 = True
    print("📡 偵測到紅外線")

# 設定中斷（紅外線來時 OUT 會變 LOW）
ir.irq(trigger=Pin.IRQ_FALLING, handler=ir_callback)

print("開始接收紅外線（10 秒）")
time.sleep(10)

# 10 秒到，關閉中斷
ir.irq(handler=None)

print("接收結束")

if 收到紅外線:
    print("✅ 10 秒內有收到紅外線")
else:
    print("❌ 10 秒內沒有收到紅外線")


