# Paper RTC 实时时钟

Paper RTC 实时时钟相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 2.1.4
- 开发板选项 = M5Paper
- M5Unified 库版本 >= 0.2.5
- M5GFX 库版本 >= 0.2.7

```cpp line-num
#define WIFI_SSID     "********"
#define WIFI_PASSWORD "********"

#define NTP_TIMEZONE "UTC-8"  // POSIX standard, in which "UTC+0" is UTC London, "UTC-8" is UTC+8 Beijing, "UTC+5" is UTC-5 New York
#define NTP_SERVER1  "0.pool.ntp.org"
#define NTP_SERVER2  "1.pool.ntp.org"
#define NTP_SERVER3  "2.pool.ntp.org"
#include <WiFi.h>

// Different versions of the framework have different SNTP header file names and availability.
#if __has_include(<esp_sntp.h>)
#include <esp_sntp.h>
#define SNTP_ENABLED 1
#elif __has_include(<sntp.h>)
#include <sntp.h>
#define SNTP_ENABLED 1
#endif

#ifndef SNTP_ENABLED
#define SNTP_ENABLED 0
#endif

#include <M5Unified.h>

static constexpr const char* const wd[7] = { "Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat" };

void setup() {
  M5.begin();
  M5.Display.setRotation(1);
  M5.Display.setFont(&fonts::FreeMono24pt7b);
  M5.Display.setEpdMode(epd_fast);  // epd_quality, epd_text, epd_fast, epd_fastest
  M5.Display.println("RTC Test");

  if (!M5.Rtc.isEnabled()) {
    M5.Display.println("RTC not found");
    while (true) {
      delay(500);
    }
  }
  M5.Display.println("RTC found");

  M5.Display.print("WiFi: ");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    M5.Display.print(".");
    delay(500);
  }
  M5.Display.println("\nWiFi connected");

  configTzTime(NTP_TIMEZONE, NTP_SERVER1, NTP_SERVER2, NTP_SERVER3);

  M5.Display.print("NTP: ");
#if SNTP_ENABLED
  while (sntp_get_sync_status() != SNTP_SYNC_STATUS_COMPLETED) {
    M5.Display.print(".");
    delay(500);
  }
#else
  struct tm timeInfo;
  while (!getLocalTime(&timeInfo, 1000)) {
    M5.Display.print(".");
    delay(500);
  }
#endif
  M5.Display.println("\nNTP connected");

  time_t t = time(nullptr) + 1;  // Advance one second
  while (t > time(nullptr))
    ;  // Synchronization in seconds
  M5.Rtc.setDateTime(gmtime(&t));

  delay(1000);
  M5.Display.clear();
  M5.Display.setCursor(0, 0);
  M5.Display.println("RTC Test");
}

void loop() {
  auto dt = M5.Rtc.getDateTime();
  M5.Display.setCursor(0, 100);
  M5.Display.printf("RTC   UTC  : \n%04d/%02d/%02d(%s)  %02d:%02d:%02d", dt.date.year, dt.date.month, dt.date.date, wd[dt.date.weekDay], dt.time.hours, dt.time.minutes, dt.time.seconds);

  // ESP32 internal timer
  auto t = time(nullptr);

  {
    auto tm = gmtime(&t);  // for UTC
    M5.Display.setCursor(0, 220);
    M5.Display.printf("ESP32 UTC  : \n%04d/%02d/%02d(%s)  %02d:%02d:%02d", tm->tm_year + 1900, tm->tm_mon + 1, tm->tm_mday, wd[tm->tm_wday], tm->tm_hour, tm->tm_min, tm->tm_sec);
  }

  {
    auto tm = localtime(&t);  // for local timezone
    M5.Display.setCursor(0, 340);
    M5.Display.printf("ESP32 %s: \n%04d/%02d/%02d(%s)  %02d:%02d:%02d", NTP_TIMEZONE, tm->tm_year + 1900, tm->tm_mon + 1, tm->tm_mday, wd[tm->tm_wday], tm->tm_hour, tm->tm_min, tm->tm_sec);
  }

  delay(200);

  // refresh the whole display every 60 seconds
  int refreshTimer = millis() % 60000;
  if (refreshTimer >= 59000 && refreshTimer < 60000) {
    M5.Display.clear();
    M5.Display.setCursor(0, 0);
    M5.Display.println("RTC Test");
  }
}
```

在程序中填写要连接的 Wi-Fi 名称及密码、你的当地时区，点击上传按钮，即可显示实时时钟。

#> 注意 | 程序中的时区定义 `NTP_TIMEZONE` 遵循 POSIX 标准，与常见的人类易读格式相反，比如 `"UTC+0"` 表示 UTC London，`"UTC-8"` 表示 UTC+8 Beijing，`"UTC+5"` 表示 UTC-5 New York。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/689/Paper_Arduino_wifi.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/689/Paper_Arduino_RTC1.jpeg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/689/Paper_Arduino_RTC2.jpeg" width="50%">

## API

Paper RTC 实时时钟部分使用了 `M5Unified` 库中的 `RTC8563_Class`，更多相关的API可以参考下方文档：

- [M5Unified - RTC8563 Class](/zh_CN/arduino/m5unified/rtc8563_class)