# Air Quality 获取Wi-Fi信息

Air Quality Wi-Fi相关API与案例程序。

## 案例程序


```cpp line-num

#include <M5Unified.h>
#include <WiFi.h>

void setup() {
  // 初始化 M5Unified
  M5.begin();
  //  一次性清屏——黑底
  M5.Lcd.fillScreen(TFT_BLACK);
  // 设置文字属性
  M5.Lcd.setTextSize(1);
  M5.Lcd.setTextColor(TFT_WHITE, TFT_BLACK);
  //  扫描 Wi-Fi
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);
  int n = WiFi.scanNetworks();
  //  把结果打印到屏幕上
  M5.Lcd.setCursor(0, 0);
  M5.Lcd.printf("Found %d networks\n\n", n);
  for (int i = 0; i < n; i++) {
    // SSID 太长会自动换行
    M5.Lcd.printf("%2d: %s\n    (%d dBm)\n\n",
                  i + 1,
                  WiFi.SSID(i).c_str(),
                  WiFi.RSSI(i));
    delay(50);
  }
}

void loop() {

  M5.update();
  // 如果要定时重刷可以放在这里
}
```

上传完成，按下复位按键就可以看到下面的效果了

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/m5air_quality_arduino_quickstart_wifi.jpg" width="30%">

