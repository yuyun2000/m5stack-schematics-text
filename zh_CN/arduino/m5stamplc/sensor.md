# StamPLC Sensor 检测温度、电压、电流

StamPLC 内置温度传感器与电压电流检测相关API与案例程序。

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
}

void loop()
{
    M5StamPLC.update();
    /* Print sensors values */
    printf("Temp: %.2f°C\n", M5StamPLC.getTemp());
    printf("Power: %.2fV\n", M5StamPLC.getPowerVoltage());
    printf("Io: %.2fA\n", M5StamPLC.getIoSocketOutputCurrent());

    delay(1000);
}
```

