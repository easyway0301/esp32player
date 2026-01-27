import network   # Wi-Fi 控制模組
import time      # 延遲用

# ===== Wi-Fi 設定 =====
SSID = "你的WiFi名稱"
PASSWORD = "你的WiFi密碼"

# 建立 STA（Client）模式物件
sta = network.WLAN(network.STA_IF)

# 啟用 STA 模式
sta.active(True)

# 如果之前有連線，先中斷（避免卡住）
if sta.isconnected():
    sta.disconnect()

print("📡 開始連線 Wi-Fi...")
sta.connect(SSID, PASSWORD)

# 等待最多 10 秒嘗試連線
timeout = 10
while not sta.isconnected() and timeout > 0:
    print("⏳ 連線中...")
    time.sleep(1)
    timeout -= 1

# 檢查結果
if sta.isconnected():
    print("✅ Wi-Fi 連線成功")
    print("IP 位址:", sta.ifconfig()[0])
else:
    print("❌ Wi-Fi 連線失敗")

