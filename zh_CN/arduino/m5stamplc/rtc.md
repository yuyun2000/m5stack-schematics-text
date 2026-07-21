# StamPLC RTC 实时时钟

StamPLC RTC时钟相关API与案例程序。

## 案例程序


```cpp line-num
/*
 * SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
 *
 * SPDX-License-Identifier: MIT
 */
#include <Arduino.h>
#include <M5StamPLC.h>

void setup()
{
    /* Init M5StamPLC */
    M5StamPLC.begin();

    /* Set RTC time */
    struct tm time;
    time.tm_year = 2077 - 1900;
    time.tm_mon  = 3 - 1;
    time.tm_mday = 7;
    time.tm_hour = 11;
    time.tm_min  = 45;
    time.tm_sec  = 14;
    M5StamPLC.setRtcTime(&time);
}

void loop()
{
    M5StamPLC.update();

    /* Print RTC time */
    static struct tm time;
    M5StamPLC.getRtcTime(&time);
    printf("Time: %d/%d/%d %d:%d:%d\n", time.tm_year + 1900, time.tm_mon + 1, time.tm_mday, time.tm_hour, time.tm_min,
           time.tm_sec);
    delay(1000);
}
```
