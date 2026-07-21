# Air Quality 实时时钟

Air Quality RTC时钟相关API与案例程序。

## 案例程序


```cpp line-num

#include <WiFi.h>
#include "time.h"
#include <M5Unified.h>

const char* ssid       = "YOUR WIFI SSID NAME"; 
const char* password   = "YOUR WIFI PASSWORD";

const char* ntpServer  = "pool.ntp.org";
const long  gmtOffset_sec    = 0;
const int   daylightOffset_sec = 8 * 3600;

void setup(){
  // —— 初始化 M5Unified
  auto cfg = M5.config();          
  cfg.serial_baudrate = 115200;     // 保留串口输出
  M5.begin(cfg);                    // 初始化显示、RTC、按键等 

  // —— 初次屏幕布局 ——  
  M5.Display.fillScreen(TFT_WHITE);
  M5.Display.setTextSize(2);
  M5.Display.setTextColor(TFT_BLACK);

  // —— 连接 Wi-Fi ——  
  Serial.printf("Connecting to %s\n", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected.");

  // —— NTP 时间同步 ——  
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
  Serial.print("Syncing time");
  #if SNTP_ENABLED
    while (sntp_get_sync_status() != SNTP_SYNC_STATUS_COMPLETED) {
      delay(500);
      Serial.print(".");
    }
  #else
    delay(1500);
  #endif
  Serial.println(" done.");

  // —— 断开 Wi-Fi，节省功耗 ——  
  WiFi.disconnect(true);
  WiFi.mode(WIFI_OFF);
}

void loop(){
  M5.update();  // 刷新按键/触摸/RTC 等状态 

  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Failed to obtain time");
    return;
  }

  Serial.println(&timeinfo, "%Y/%m/%d %H:%M:%S");
  M5.Display.fillRect(0, 0, 240, 48, TFT_WHITE);

  M5.Display.setCursor(0, 0);
  M5.Display.printf("%04d/%02d/%02d",
                    timeinfo.tm_year + 1900,
                    timeinfo.tm_mon + 1,
                    timeinfo.tm_mday);

  M5.Display.setCursor(0, 24);
  M5.Display.printf("%02d:%02d:%02d",
                    timeinfo.tm_hour,
                    timeinfo.tm_min,
                    timeinfo.tm_sec);

  delay(1000);
}

```

上传完成就可以看到下面的效果了

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/m5air_quality_arduino_quickstart_rtc.jpg" width="30%">

## API

Air Quality RTC时钟部分使用了M5Unified库中的`RTC8563_Class`，更多相关的API可以参考下方文档：

- [M5Unified - RTC8563 Class](/zh_CN/arduino/m5unified/rtc8563_class)

