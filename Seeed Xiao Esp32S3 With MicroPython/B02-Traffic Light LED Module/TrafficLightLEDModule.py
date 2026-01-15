from machine import Pin, Timer
# 從 machine 模組匯入 Pin（控制腳位）與 Timer（定時器）

# === LED 腳位設定（共陰極：GPIO=1 亮） ===
red = Pin(9, Pin.OUT)      
# 將 GPIO9 設定為輸出，用來控制紅燈

yellow = Pin(8, Pin.OUT)   
# 將 GPIO8 設定為輸出，用來控制黃燈

green = Pin(7, Pin.OUT)    
# 將 GPIO7 設定為輸出，用來控制綠燈

# === 燈號狀態表 ===
# 每一組代表 (紅燈, 綠燈, 黃燈)
# 1 = 亮，0 = 滅（共陰極）
states = [
    (1, 0, 0),  # 紅燈亮
    (0, 1, 0),  # 綠燈亮
    (0, 0, 1),  # 黃燈亮
]

state_index = 0
# 用來記錄目前是哪一個燈號狀態（從第 0 個開始）

def update_led(timer):
    # Timer 觸發時會自動呼叫這個函式

    global state_index
    # 使用全域變數 state_index，記錄目前狀態

    r, g, y = states[state_index]
    # 從狀態表中取出目前的紅、綠、黃燈狀態

    red.value(r)
    # 設定紅燈亮或滅

    green.value(g)
    # 設定綠燈亮或滅

    yellow.value(y)
    # 設定黃燈亮或滅

    state_index = (state_index + 1) % len(states)
    # 狀態往下一個移動，超過就從 0 開始

# === 設定定時器 ===
tim = Timer(0)
# 建立一個硬體定時器（編號 0）

tim.init(
    period=1000,              # 每 1000 毫秒（1 秒）觸發一次
    mode=Timer.PERIODIC,      # 週期性定時器（會一直重複）
    callback=update_led       # 每次觸發就執行 update_led()
)

