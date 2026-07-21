# StackChan RTC 实时时钟

StackChan RTC 时钟相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5CoreS3
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#if defined(ARDUINO)

#define WIFI_SSID     "***********"
#define WIFI_PASSWORD "***********"
#define NTP_TIMEZONE  "UTC-8"
#define NTP_SERVER1   "0.pool.ntp.org"
#define NTP_SERVER2   "1.pool.ntp.org"
#define NTP_SERVER3   "2.pool.ntp.org"

#include <WiFi.h>

// Different versions of the framework have different SNTP header file names and
// availability.
#if __has_include(<esp_sntp.h>)
#include <esp_sntp.h>
#define SNTP_ENABLED 1
#elif __has_include(<sntp.h>)
#include <sntp.h>
#define SNTP_ENABLED 1
#endif

#endif

#ifndef SNTP_ENABLED
#define SNTP_ENABLED 0
#endif

#include <M5Unified.h>

void setup(void) {
    M5.begin();
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);

    if (!M5.Rtc.isEnabled()) {
        Serial.println("RTC not found.");
        for (;;) {
            vTaskDelay(500);
        }
    }

    Serial.println("RTC found.");

    // It is recommended to set UTC for the RTC and ESP32 internal clocks.
    /* /// setup RTC ( direct setting )
      //                      YYYY  MM  DD      hh  mm  ss
      M5.Rtc.setDateTime( { { 2021, 12, 31 }, { 12, 34, 56 } } );

    //*/

    /// setup RTC ( NTP auto setting )

    M5.Display.println("WiFi Connecting...");

    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print('.');
        delay(500);
    }
    M5.Display.println("WiFi Connected.");
    Serial.println("\r\n WiFi Connected.");

    configTzTime(NTP_TIMEZONE, NTP_SERVER1, NTP_SERVER2, NTP_SERVER3);

#if SNTP_ENABLED
    while (sntp_get_sync_status() != SNTP_SYNC_STATUS_COMPLETED) {
        Serial.print('.');
        delay(1000);
    }
    Serial.println("\r\n NTP Connected.");
    M5.Display.println("NTP Connected");
#else
    delay(1600);
    struct tm timeInfo;
    while (!getLocalTime(&timeInfo, 1000)) {
        Serial.print('.');
    };
#endif

    time_t t = time(nullptr) + 1;  // Advance one second.
    while (t > time(nullptr))
        ;  /// Synchronization in seconds
    M5.Rtc.setDateTime(gmtime(&t));
    M5.Display.clear();
}

void loop(void) {
    static constexpr const char* const wd[7] = {"Sun", "Mon", "Tue", "Wed",
                                                "Thr", "Fri", "Sat"};

    delay(500);

    auto dt = M5.Rtc.getDateTime();
    Serial.printf("RTC   UTC  :%04d/%02d/%02d (%s)  %02d:%02d:%02d\r\n",
                  dt.date.year, dt.date.month, dt.date.date,
                  wd[dt.date.weekDay], dt.time.hours, dt.time.minutes,
                  dt.time.seconds);
    M5.Display.setCursor(0, 0);
    M5.Display.printf("RTC   UTC  :%04d/%02d/%02d (%s)  %02d:%02d:%02d\n",
                          dt.date.year, dt.date.month, dt.date.date,
                          wd[dt.date.weekDay], dt.time.hours, dt.time.minutes,
                          dt.time.seconds);

    /// ESP32 internal timer
    auto t = time(nullptr);
    {
        auto tm = gmtime(&t);  // for UTC.
        Serial.printf("ESP32 UTC  :%04d/%02d/%02d (%s)  %02d:%02d:%02d\r\n",
                      tm->tm_year + 1900, tm->tm_mon + 1, tm->tm_mday,
                      wd[tm->tm_wday], tm->tm_hour, tm->tm_min, tm->tm_sec);
        M5.Display.printf("ESP32 UTC  :%04d/%02d/%02d (%s)  %02d:%02d:%02d\n",
                              tm->tm_year + 1900, tm->tm_mon + 1, tm->tm_mday,
                              wd[tm->tm_wday], tm->tm_hour, tm->tm_min,
                              tm->tm_sec);
    }

    {
        auto tm = localtime(&t);  // for local timezone.
        Serial.printf("ESP32 %s:%04d/%02d/%02d (%s)  %02d:%02d:%02d\r\n",
                      NTP_TIMEZONE, tm->tm_year + 1900, tm->tm_mon + 1,
                      tm->tm_mday, wd[tm->tm_wday], tm->tm_hour, tm->tm_min,
                      tm->tm_sec);
        M5.Display.printf("ESP32 %s:%04d/%02d/%02d (%s)  %02d:%02d:%02d\n",
                              NTP_TIMEZONE, tm->tm_year + 1900, tm->tm_mon + 1,
                              tm->tm_mday, wd[tm->tm_wday], tm->tm_hour,
                              tm->tm_min, tm->tm_sec);
    }
}
```

烧录成功后，StackChan 屏幕上会显示当前的 RTC 时间以及 ESP32 内部时钟的时间信息。RTC 时间是通过 NTP 同步设置的，而 ESP32 内部时钟则是通过系统时间函数获取的，它们应该是同步的。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/StackChan_RTC.jpg" width="40%">

## API

StackChan RTC 时钟部分使用了 M5Unified 库中的`RTC8563_Class`, 更多相关的 API 可以参考下方文档:

- [M5Unified - RTC8563 Class](/zh_CN/arduino/m5unified/rtc8563_class)
