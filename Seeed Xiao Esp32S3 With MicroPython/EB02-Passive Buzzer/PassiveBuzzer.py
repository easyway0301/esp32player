from machine import Pin, PWM
import time

# =====================
# 設定無源蜂鳴器腳位
# =====================
# Expansion Board 上的無源蜂鳴器
buzzer = PWM(Pin(4))

# =====================
# 定義音符頻率
# =====================
Do  = 262
Re  = 294
Mi  = 330
Fa  = 349
So  = 392
La  = 440
Si  = 494
Do2 = 523
REST = 0   # 休止符

# =====================
# 播放單一音符的函式
# =====================
def play(note, duration):
    if note == REST:
        buzzer.duty(0)          # 休止（不發聲）
    else:
        buzzer.freq(note)       # 設定頻率
        buzzer.duty(512)        # 50% 占空比（音量適中）
    time.sleep(duration)
    buzzer.duty(0)              # 音符結束關閉
    time.sleep(0.02)            # 音符間小間隔

# =====================
# 《少女的祈禱》簡化旋律
# =====================
song = [
    Mi, So, La, So, Mi, Re,
    Mi, So, La, So, Mi, Re,
    Mi, So, La, Do2, La, So,
    Mi, Re, Do, REST,

    Mi, So, La, So, Mi, Re,
    Mi, So, La, So, Mi, Re,
    Mi, So, La, Do2, La, So,
    Mi, Re, Do
]

# =====================
# 播放旋律
# =====================
for note in song:
    play(note, 0.35)

# 播放完關閉 PWM
buzzer.deinit()

