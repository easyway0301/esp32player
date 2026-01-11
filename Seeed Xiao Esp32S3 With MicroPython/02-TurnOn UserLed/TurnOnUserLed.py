from machine import Pin
import time

# 本範例適用Seeed XIAO Esp32S3開發板
# TYPEC插頭朝上，UserLed燈在右邊，打開是黃燈。

# 設定 LED 腳位
# 貼片式LED燈焊在GPIO 21 
UserLed = Pin(21, Pin.OUT)

def 打開UserLed():
    print("打開UserLed")
    # LED 亮燈
    UserLed.value(0)
    #UserLed.off() # 注意如果要用off，它會亮燈

def 關掉UserLed():
    print("關掉UserLed")
    # LED 熄燈
    UserLed.value(1)
    #UserLed.on() # 注意如果要用on，它會關燈

打開UserLed()

print("暫停2秒")
time.sleep(2)

關掉UserLed()
