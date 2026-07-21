# StamPLC RGB LED 状态灯

StamPLC 状态灯相关API与案例程序。

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
}

void loop()
{
    /* Set status light to red */
    M5StamPLC.setStatusLight(1, 0, 0);
    printf("Set status light to red\n");
    delay(1000);

    /* Set status light to green */
    M5StamPLC.setStatusLight(0, 1, 0);
    printf("Set status light to green\n");
    delay(1000);

    /* Set status light to blue */
    M5StamPLC.setStatusLight(0, 0, 1);
    printf("Set status light to blue\n");
    delay(1000);

    /* Set status light to white */
    M5StamPLC.setStatusLight(1, 1, 1);
    printf("Set status light to white\n");
    delay(1000);

    /* Set status light to black */
    M5StamPLC.setStatusLight(0, 0, 0);
    printf("Set status light to black\n");
    delay(1000);
}
```

## API

### setStatusLight

**函数原型:**

```cpp
void setStatusLight(const uint8_t& r, const uint8_t& g, const uint8_t& b);
```

**功能说明:**

- 进行RGB LED灯颜色设置。需注意，RGB LED由IO拓展芯片引脚驱动，故无法进行亮度调节 。 

**传入参数:**

- const uint8_t& r：
  - 1: 点亮红灯
  - 0: 熄灭红灯
- const uint8_t& g：
  - 1: 点亮绿灯
  - 0: 熄灭绿灯
- const uint8_t& b：
  - 1: 点亮蓝灯
  - 0: 熄灭蓝灯

**返回值:**

- null

