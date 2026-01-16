from machine import Pin, I2C
import sh1106

# https://github.com/robert-hh/SH1106/tree/master
# 3.3V可用
# 不能直接顯示中文，要用其他方式

# 初始化 I2C
i2c = I2C(scl=Pin(6), sda=Pin(5), freq=400000)

# 不使用 RES 腳
display = sh1106.SH1106_I2C(128, 64, i2c, res=None, addr=0x3c)

# 顯示內容
display.sleep(False)
display.fill(0)
display.text('hello! World', 0, 0)
display.text('Micropython', 0, 8)
display.text('Line 3', 0, 16)
display.text('Line 4', 0, 24)
display.text('Line 5', 0, 32)
display.text('Line 6', 0, 40)
display.text('Line 7', 0, 48)
display.text('Line 8', 0, 56)

display.show()

