# Module GPS v2.0/v2.1 Arduino 使用教程

## 1. 准备工作

- 1\. 环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 2\. 使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [TinyGPSPlus](https://github.com/m5stack/TinyGPSPlus)

- 3\. 使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Module GPS v2.0](https://shop.m5stack.com/products/gps-module-v2-0-with-external-antenna-at6668)
  - [Module GPS v2.1](https://shop.m5stack.com/products/gps-module-v2-1-with-antenna-atgm336h)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/3.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/Module_GPS_v2.1_02.webp" width="20%">

\#>TinyGPSPlus 库安装 | 由于 Arduino library 管理中的 TinyGPSPlus 版本较旧且未完全兼容，需要访问[TinyGPSPlus - M5Stack Github](https://github.com/m5stack/TinyGPSPlus), 手动下载。并安装放置到 Arduino 库文件路径中。

\#> 库管理路径 | **Windows**: `C:\Users\{username}\Documents\Arduino`<br/>**macOS**: `/Users/{username}/Documents/Arduino`<br/>**Linux**: `/home/{username}/Arduino`

## 2. 案例程序

- 1\. 根据实际连接的设备，在程序中修改实际使用的 IO 信息。本教程中使用的主控设备为 CoreS3, Module GPS v2.0/v2.1 堆叠后其对应的 M5-Bus 总线 IO 为`G18(RX)`,`G17(TX)`。  
Module GPS v2.0/v2.1 还支持通过底部的 DIP 拨码开关切换引脚的连接，可根据实际需求进行调整。下方左图为 Module GPS v2.0，右图为 Module GPS v2.1，其中黄线框住的部分是 v2.1 相较于 v2.0 多出的可选择引脚。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/950/module_gps_v2.0_dip_switch.jpg" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/module_gps_v2.1_dip_switch.jpg" width="40%">

- 2\. 参考[TinyGPSPlus](https://github.com/m5stack/TinyGPSPlus)中的`UnitGPSExample`案例程序，修改对应的 UART 初始化引脚 IO。基于 M5Unified 和 M5GFX 为该案例程序添加基础的坐标显示功能。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/module/module_gps_v2.0/module_gps_v2.0_example_01.jpg" width="70%">

```cpp line-num
/*
 *SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
 *
 *SPDX-License-Identifier: MIT
 */

#include "M5Unified.h"
#include "M5GFX.h"
#include "MultipleSatellite.h"

static const int RXPin = 18, TXPin = 17;
static const uint32_t GPSBaud = 115200;
MultipleSatellite gps(Serial1, GPSBaud, SERIAL_8N1, RXPin, TXPin);

void displayInfo();

void setup()
{
    M5.begin();
    Serial.begin(115200);
    gps.begin();
    gps.setSystemBootMode(BOOT_FACTORY_START);
    Serial.println(F("DeviceExample.ino"));
    Serial.println(F("A simple demonstration of TinyGPSPlus with an attached GPS module"));
    Serial.print(F("Testing TinyGPSPlus library v. "));
    Serial.println(TinyGPSPlus::libraryVersion());
    Serial.println(F("by Mikal Hart"));
    Serial.println();
    String version = gps.getGNSSVersion();
    Serial.printf("GNSS SW=%s\r\n", version.c_str());
    delay(1000);
    // Set satellite mode
    gps.setSatelliteMode(SATELLITE_MODE_GPS);
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
}
void loop()
{
    // Update data
    gps.updateGPS();
    displayInfo();
    delay(10);
}

void displayInfo()
{
    Serial.print(F("Location: "));
    Serial.printf("satellites:%d\n", gps.satellites.value());
    if (gps.location.isUpdated()) {
        Serial.print(gps.location.lat(), 6);
        Serial.print(F(","));
        Serial.print(gps.location.lng(), 6);
        Serial.print(F("\n"));

        M5.Display.fillRect(0, 0, 320, 60, BLACK);
        M5.Display.setCursor(0, 0);
        M5.Display.printf("Location: \nLat: %f\nlng: %f\n", gps.location.lat(), gps.location.lng());

    } else {
        M5.Display.fillRect(0, 0, 320, 60, BLACK);
        M5.Display.setCursor(0, 0);
        M5.Display.print("Location: \n");
        M5.Display.print("Lat: ---------\n");
        M5.Display.print("lng: ---------\n");
        Serial.print(F("INVALID\n"));
    }

    Serial.print(F("  Date/Time: "));
    if (gps.date.isUpdated()) {
        Serial.print(gps.date.month());
        Serial.print(F("/"));
        Serial.print(gps.date.day());
        Serial.print(F("/"));
        Serial.print(gps.date.year());

        M5.Display.fillRect(0, 100, 320, 60, BLACK);
        M5.Display.setCursor(0, 100);
        M5.Display.printf("Date/Time: %d/%d/%d\n", gps.date.month(), gps.date.day(), gps.date.year());

    } else {
        Serial.print(F("INVALID"));
    }

    Serial.print(F(" "));
    if (gps.time.isUpdated()) {
        if (gps.time.hour() < 10) Serial.print(F("0"));
        Serial.print(gps.time.hour());
        Serial.print(F(":"));
        if (gps.time.minute() < 10) Serial.print(F("0"));
        Serial.print(gps.time.minute());
        Serial.print(F(":"));
        if (gps.time.second() < 10) Serial.print(F("0"));
        Serial.print(gps.time.second());
        Serial.print(F("."));
        if (gps.time.centisecond() < 10) Serial.print(F("0"));
        Serial.print(gps.time.centisecond());

        M5.Display.fillRect(0, 160, 320, 60, BLACK);
        M5.Display.setCursor(0, 160);
        M5.Display.printf("Time: %d:%d:%d.%d\n", gps.time.hour(), gps.time.minute(), gps.time.second(),
                          gps.time.centisecond());

    } else {
        Serial.print(F("INVALID"));
    }

    Serial.println();
    delay(1000);
}
```

## 3. 编译上传

- 1\. 下载模式：不同设备进行程序烧录前需要下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- CoreS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

- 2\. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/module/module_gps_v2.0/module_gps_v2.0_example_02.jpg" width="70%">

## 4. 卫星定位

连接配套的外置天线，将天线放置在窗边或是户外空旷区域，等待设备成功搜索卫星与获取坐标。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/projects/module/module_gps_v2.0/module_gps_v2.0_with_cores3_02.jpg" width="70%">
