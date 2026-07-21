# PowerHub RTC 实时时钟

PowerHub RTC 实时时钟相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.3
- 开发板选项 = M5PowerHub
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#define WIFI_SSID "********"
#define WIFI_PSWD "********"

#define NTP_TIMEZONE "UTC-8"  // POSIX standard, in which "UTC+0" is UTC London, "UTC-8" is UTC+8 Beijing, "UTC+5" is UTC-5 New York
#define NTP_SERVER1 "0.pool.ntp.org"
#define NTP_SERVER2 "1.pool.ntp.org"
#define NTP_SERVER3 "2.pool.ntp.org"
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
  Serial.begin(115200);
  Serial.println("PowerHub RTC Test");

  if (!M5.Rtc.isEnabled()) {
    Serial.println("RTC not found");
    while (true) {
      delay(500);
    }
  }
  Serial.println("RTC found");

  Serial.print("WiFi: ");
  WiFi.begin(WIFI_SSID, WIFI_PSWD);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("\nWiFi connected");

  configTzTime(NTP_TIMEZONE, NTP_SERVER1, NTP_SERVER2, NTP_SERVER3);

  Serial.print("NTP: ");
#if SNTP_ENABLED
  while (sntp_get_sync_status() != SNTP_SYNC_STATUS_COMPLETED) {
    Serial.print(".");
    delay(500);
  }
#else
  struct tm timeInfo;
  while (!getLocalTime(&timeInfo, 1000)) {
    Serial.print(".");
    delay(500);
  }
#endif
  Serial.println("\nNTP connected");

  time_t t = time(nullptr) + 1;  // Advance one second
  while (t > time(nullptr))
    ;  // Synchronization in seconds
  M5.Rtc.setDateTime(gmtime(&t));

  delay(1000);
}

void loop() {
  M5.update();

  // RTC timer
  auto dt = M5.Rtc.getDateTime();
  Serial.printf("RTC   UTC  : ");
  Serial.printf("%04d/%02d/%02d(%s) ", dt.date.year, dt.date.month, dt.date.date, wd[dt.date.weekDay]);
  Serial.printf("%02d:%02d:%02d\n", dt.time.hours, dt.time.minutes, dt.time.seconds);

  // ESP32 internal timer
  auto t = time(nullptr);
  {
    auto tm = gmtime(&t);  // for UTC
    Serial.printf("ESP32 UTC  : ");
    Serial.printf("%04d/%02d/%02d(%s) ", tm->tm_year + 1900, tm->tm_mon + 1, tm->tm_mday, wd[tm->tm_wday]);
    Serial.printf("%02d:%02d:%02d\n", tm->tm_hour, tm->tm_min, tm->tm_sec);
  }
  {
    auto tm = localtime(&t);  // for local timezone
    Serial.printf("ESP32 %s: ", NTP_TIMEZONE);
    Serial.printf("%04d/%02d/%02d(%s) ", tm->tm_year + 1900, tm->tm_mon + 1, tm->tm_mday, wd[tm->tm_wday]);
    Serial.printf("%02d:%02d:%02d\n\n", tm->tm_hour, tm->tm_min, tm->tm_sec);
  }

  delay(1000);
}
```

在程序中填写要连接的 Wi-Fi 名称及密码、你的当地时区，点击上传按钮将程序上传至 PowerHub，打开串口监视器即可显示实时时钟。

#> 注意 | 程序中的时区定义 `NTP_TIMEZONE` 遵循 POSIX 标准，与常见的人类易读格式相反，比如 `"UTC+0"` 表示 UTC London，`"UTC-8"` 表示 UTC+8 Beijing，`"UTC+5"` 表示 UTC-5 New York。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_wifi.png" width="90%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_RTC.png" width="90%">

## API

PowerHub RTC 实时时钟部分驱动使用了`M5Unified`库中的`RTC8563_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - RTC8563 Class](/zh_CN/arduino/m5unified/rtc8563_class)