# PaperColor RTC 时钟

PaperColor RTC 时钟相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.7
- 开发板选项 = M5PaperColor
- M5Unified 库版本 >= 0.2.15
- M5GFX 库版本 >= 0.2.21
- M5PM1 库版本 >= 1.0.1

### 配置本地时间

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>
#include <M5PM1.h>

M5Canvas canvas(&M5.Display);
M5PM1 pm1;

static constexpr const char* const wd[7] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
static int last_drawn_minute = -1;
static bool pm1_ready = false;

static void drawScreen(const m5::rtc_datetime_t& dt)
{
    const int w = M5.Display.width();
    const int h = M5.Display.height();

    char date_buf[32];
    char hm_buf[16];

    snprintf(date_buf, sizeof(date_buf), "%04d/%02d/%02d", dt.date.year, dt.date.month, dt.date.date);
    snprintf(hm_buf, sizeof(hm_buf), "%02d:%02d", dt.time.hours, dt.time.minutes);

    canvas.fillSprite(WHITE);
    canvas.setTextDatum(top_center);
    canvas.setTextSize(1);

    canvas.setFont(&fonts::FreeSansBold24pt7b);
    canvas.setTextColor(BLACK);
    canvas.drawString("PAPER COLOR RTC", w / 2, 18);

    canvas.setFont(&fonts::FreeSansBold24pt7b);
    canvas.setTextSize(2);
    canvas.setTextColor(RED);
    canvas.drawString(hm_buf, w / 2, h / 2 - 36);

    canvas.setTextSize(1);
    canvas.setFont(&fonts::FreeSansBold18pt7b);
    canvas.setTextColor(BLUE);
    canvas.drawString(date_buf, w / 2, h / 2 + 42);

    canvas.setFont(&fonts::FreeSansBold18pt7b);
    canvas.setTextColor(GREEN);
    canvas.drawString(wd[dt.date.weekDay], w / 2, h / 2 + 86);

    canvas.pushSprite(0, 0);
}

static void drawErrorScreen(const char* message)
{
    const int w = M5.Display.width();
    const int h = M5.Display.height();

    canvas.fillSprite(WHITE);
    canvas.setTextDatum(middle_center);
    canvas.setFont(&fonts::FreeSansBold24pt7b);
    canvas.setTextColor(RED);
    canvas.drawString(message, w / 2, h / 2);
    canvas.pushSprite(0, 0);
}

void setup(void)
{
    auto cfg          = M5.config();
    cfg.clear_display = false;
    M5.begin(cfg);
    Serial.begin(115200);
    M5.Display.setEpdMode(epd_mode_t::epd_fastest);
    M5.Display.setRotation(1);

    canvas.createSprite(M5.Display.width(), M5.Display.height());

    m5pm1_err_t err = pm1.begin(&M5.In_I2C, M5PM1_DEFAULT_ADDR, M5PM1_I2C_FREQ_100K);
    pm1_ready       = (err == M5PM1_OK);

    if (pm1_ready) {
        pm1.setLdoEnable(true);
    }

    if (!M5.Rtc.isEnabled()) {
        Serial.println("RTC not found.");
        drawErrorScreen("RTC not found.");
        for (;;) {
            vTaskDelay(pdMS_TO_TICKS(1000));
        }
    }

    Serial.println("RTC found.");

    M5.Rtc.setDateTime({{2026, 5, 8}, {12, 0, 0}});

    Serial.println("RTC demo time set to 2026/05/08 12:00:00");

    auto dt = M5.Rtc.getDateTime();
    drawScreen(dt);
    last_drawn_minute = dt.time.minutes;
}

void loop(void)
{
    auto dt = M5.Rtc.getDateTime();
    if (dt.time.minutes != last_drawn_minute) {
        last_drawn_minute = dt.time.minutes;
        Serial.printf("RTC: %04d/%02d/%02d (%s) %02d:%02d:%02d\r\n", dt.date.year, dt.date.month, dt.date.date,
                      wd[dt.date.weekDay], dt.time.hours, dt.time.minutes, dt.time.seconds);

        drawScreen(dt);
    }

    delay(100);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_rtc_demo_01.jpg" width="50%">

### SNTP 网络时间

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>
#include <M5PM1.h>
#include <WiFi.h>
#include <esp_sntp.h>
#include <sntp.h>

#define NTP_TIMEZONE "UTC-8"
#define NTP_SERVER1  "0.pool.ntp.org"
#define NTP_SERVER2  "1.pool.ntp.org"
#define NTP_SERVER3  "2.pool.ntp.org"

static constexpr uint32_t WIFI_CONNECT_TIMEOUT_MS = 20000;
static constexpr uint32_t SNTP_SYNC_TIMEOUT_MS    = 30000;

M5Canvas canvas(&M5.Display);
M5PM1 pm1;

const char* ssid     = "ssid";
const char* password = "password";

static constexpr const char* const wd[7] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
static int last_drawn_minute = -1;
static bool pm1_ready = false;

static void drawScreen(const m5::rtc_datetime_t& dt)
{
    const int w = M5.Display.width();
    const int h = M5.Display.height();

    char date_buf[32];
    char hm_buf[16];

    snprintf(date_buf, sizeof(date_buf), "%04d/%02d/%02d", dt.date.year, dt.date.month, dt.date.date);
    snprintf(hm_buf, sizeof(hm_buf), "%02d:%02d", dt.time.hours, dt.time.minutes);

    canvas.fillSprite(WHITE);
    canvas.setTextDatum(top_center);
    canvas.setTextSize(1);

    canvas.setFont(&fonts::FreeSansBold24pt7b);
    canvas.setTextColor(BLACK);
    canvas.drawString("PAPER COLOR RTC", w / 2, 18);

    canvas.setFont(&fonts::FreeSansBold18pt7b);
    canvas.setTextColor(YELLOW);
    canvas.drawString("SNTP", w / 2, 66);

    canvas.setFont(&fonts::FreeSansBold24pt7b);
    canvas.setTextSize(2);
    canvas.setTextColor(RED);
    canvas.drawString(hm_buf, w / 2, h / 2 - 22);

    canvas.setTextSize(1);
    canvas.setFont(&fonts::FreeSansBold18pt7b);
    canvas.setTextColor(BLUE);
    canvas.drawString(date_buf, w / 2, h / 2 + 56);

    canvas.setFont(&fonts::FreeSansBold18pt7b);
    canvas.setTextColor(GREEN);
    canvas.drawString(wd[dt.date.weekDay], w / 2, h / 2 + 100);

    canvas.pushSprite(0, 0);
}

static void drawSyncScreen()
{
    const int w = M5.Display.width();
    const int h = M5.Display.height();

    canvas.fillSprite(WHITE);
    canvas.setTextDatum(middle_center);
    canvas.setTextSize(1);

    canvas.setFont(&fonts::FreeSansBold18pt7b);
    canvas.setTextColor(BLACK);
    canvas.drawString("SNTP Sync....", w / 2, h / 2 - 18);

    canvas.setFont(&fonts::FreeSansBold12pt7b);
    canvas.setTextColor(BLUE);
    canvas.drawString("Please wait", w / 2, h / 2 + 28);

    canvas.pushSprite(0, 0);
}

static void drawErrorScreen(const char* message)
{
    const int w = M5.Display.width();
    const int h = M5.Display.height();

    canvas.fillSprite(WHITE);
    canvas.setTextDatum(middle_center);
    canvas.setFont(&fonts::FreeSansBold24pt7b);
    canvas.setTextColor(RED);
    canvas.drawString(message, w / 2, h / 2);
    canvas.pushSprite(0, 0);
}

static bool connectWiFi()
{
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);

    const uint32_t start_ms = millis();
    while (WiFi.status() != WL_CONNECTED) {
        if (millis() - start_ms >= WIFI_CONNECT_TIMEOUT_MS) {
            return false;
        }
        delay(250);
    }

    Serial.printf("WiFi connected, IP: %s\r\n", WiFi.localIP().toString().c_str());
    return true;
}

static bool syncRtcFromSntp()
{
    Serial.println("SNTP sync start...");
    configTzTime(NTP_TIMEZONE, NTP_SERVER1, NTP_SERVER2, NTP_SERVER3);

    const uint32_t start_ms = millis();
    while (sntp_get_sync_status() != SNTP_SYNC_STATUS_COMPLETED) {
        if (millis() - start_ms >= SNTP_SYNC_TIMEOUT_MS) {
            return false;
        }
        delay(500);
    }

    time_t now = time(nullptr) + 1;
    while (now > time(nullptr)) {
        delay(10);
    }

    auto local_tm = localtime(&now);
    if (local_tm == nullptr) {
        return false;
    }

    M5.Rtc.setDateTime(local_tm);
    Serial.printf("RTC synced from SNTP: %04d/%02d/%02d %02d:%02d:%02d (%s)\r\n",
                  local_tm->tm_year + 1900,
                  local_tm->tm_mon + 1,
                  local_tm->tm_mday,
                  local_tm->tm_hour,
                  local_tm->tm_min,
                  local_tm->tm_sec,
                  NTP_TIMEZONE);
    return true;
}

void setup(void)
{
    auto cfg          = M5.config();
    cfg.clear_display = false;
    M5.begin(cfg);
    Serial.begin(115200);
    M5.Display.setEpdMode(epd_mode_t::epd_fastest);
    M5.Display.setRotation(1);

    canvas.createSprite(M5.Display.width(), M5.Display.height());

    m5pm1_err_t err = pm1.begin(&M5.In_I2C, M5PM1_DEFAULT_ADDR, M5PM1_I2C_FREQ_100K);
    pm1_ready       = (err == M5PM1_OK);

    if (pm1_ready) {
        pm1.setLdoEnable(true);
    }

    drawSyncScreen();

    if (!M5.Rtc.isEnabled()) {
        Serial.println("RTC not found.");
        drawErrorScreen("RTC not found.");
        for (;;) {
            vTaskDelay(pdMS_TO_TICKS(1000));
        }
    }

    Serial.println("RTC found.");

    if (!connectWiFi()) {
        Serial.println("WiFi connect failed.");
        drawErrorScreen("WiFi failed");
        for (;;) {
            vTaskDelay(pdMS_TO_TICKS(1000));
        }
    }

    if (!syncRtcFromSntp()) {
        Serial.println("SNTP sync failed.");
        drawErrorScreen("SNTP failed");
        for (;;) {
            vTaskDelay(pdMS_TO_TICKS(1000));
        }
    }

    auto dt = M5.Rtc.getDateTime();
    Serial.printf("SNTP sync done. RTC: %04d/%02d/%02d (%s) %02d:%02d:%02d\r\n", dt.date.year, dt.date.month,
                  dt.date.date, wd[dt.date.weekDay], dt.time.hours, dt.time.minutes, dt.time.seconds);
    drawScreen(dt);
    last_drawn_minute = dt.time.minutes;
}

void loop(void)
{
    auto dt = M5.Rtc.getDateTime();
    if (dt.time.minutes != last_drawn_minute) {
        last_drawn_minute = dt.time.minutes;
        Serial.printf("RTC: %04d/%02d/%02d (%s) %02d:%02d:%02d\r\n", dt.date.year, dt.date.month, dt.date.date,
                      wd[dt.date.weekDay], dt.time.hours, dt.time.minutes, dt.time.seconds);

        drawScreen(dt);
    }

    delay(100);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_sntp_demo_01.jpg" width="50%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1239/arduino_papercolor_sntp_demo_02.jpg" width="50%">

## API

RTC 时钟部分使用了 M5Unified 库中的 `RTC_Class`，更多 API 可参考下方文档：

- [M5Unified - RTC Class](/zh_CN/arduino/m5unified/rtc8563_class)
