# StamPLC Buzzer 蜂鸣器

StamPLC Buzzer蜂鸣器相关API与案例程序。

## 案例程序

```cpp line-num
/*
 *SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
 *
 *SPDX-License-Identifier: MIT
 */
#include <Arduino.h>
#include <M5StamPLC.h>

void setup()
{
    /* Init M5StamPLC */
    M5StamPLC.begin();

    /* Play tone */
    // M5StamPLC.tone(frequency, duration);

    /* Stop playing tone */
    // M5StamPLC.noTone();
}

void loop()
{
    M5StamPLC.tone(523, 50);
    delay(1000);
    M5StamPLC.tone(659, 50);
    delay(1000);
    M5StamPLC.tone(880, 50);
    delay(1000);
}
```


## tone


函数原型:

```cpp
void tone(unsigned int frequency, unsigned long duration = 0UL);
```

功能说明:

- 驱动蜂鸣器播放指定频率，并设定播放时长。

传入参数:

- unsigned int frequency:
  - 驱动频率(Hz)
- unsigned long duration:
  - 播放持续时间(ms)

返回值:

- null


## noTone

函数原型:

```cpp
void noTone();
```

功能说明:

- 停止蜂鸣器播放

传入参数:

- null

返回值:

- null
