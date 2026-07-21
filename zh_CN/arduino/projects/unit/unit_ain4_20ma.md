# Unit AIN4-20mA Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Moudle-4-20mA](https://github.com/m5stack/M5Module-4-20mA)（本模块与 Module13.2 AIN4-20mA 共用同一个驱动库）

\#> 注意 | 需要在 GitHub 上下载最新的库版本，库地址: [M5Moudle-4-20mA - M5Stack GitHub](https://github.com/m5stack/M5Module-4-20mA)，请勿在 Arduino Library 中下载。（如有疑问，请参考[此教程](/zh_CN/arduino/arduino_library#git%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85)）

- 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit AIN4-20mA](https://shop.m5stack.com/products/ain4-20ma-unit)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/unit/AIN4-20mA%20Unit/img-3edfd1af-26f2-41e4-82cd-2050ac7e1177.webp" width="20%"/>

## 2. 注意事项

\#> 跳线帽的连接说明 | 在产品包装中配备了 3 个跳线帽，可根据电流型传感器的有无源状态进行切换。

- 使用**无源电流型传感器**时，请连接 DC 24V 供电输入，传感器信号接入 IN+，IN-，并将跳线帽调整为下图所示（注意信号正负）：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/743/unit_ain4_20ma_passive_sensor_connect_01.png" width="60%">

- 使用**有源电流型传感器**时，请将传感器信号接入 IN+，IN-，并将跳线帽调整为下图所示（注意信号正负）：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/743/unit_ain4_20ma_active_sensor_connect_01.png" width="60%">

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/arduino/projects/unit/unit_ain4_20ma)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U162" type="UNIT"></ProductCompatible> 

## 3. 案例程序

- 本教程中使用的主控设备为 CoreS3 ，搭配 Unit AIN4-20mA。本电流型模拟量采集模块采用 I2C 的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的串口 IO 为 `G1 (SCL)`，`G2 (SDA)`。

```cpp line-num
#include <M5Unified.h>
#include "MODULE_4_20MA.h"
#include <M5GFX.h>

MODULE_4_20MA meter;

void show_current_value(void) {
    M5.Display.fillScreen(WHITE);
    M5.Display.setCursor(0, 0);
    M5.Display.println("Unit 4-20mA Demo");
    M5.Display.setCursor(0, 50);
    M5.Display.printf("Current:%.2fmA\r\n", (float)(meter.getCurrentValue(0)) / 100.0);
    M5.Display.printf("ADC_Value:%.2f\r\n", (float)(meter.getADC12BitsValue(0)) / 100.0);
    M5.Display.printf("Cal_Current:%.2fmA", (float)(meter.getCurrentValue(0)));
}

void setup() {
    M5.begin();
    Serial.begin(115200);
    M5.Display.fillScreen(WHITE);
    M5.Display.setTextColor(BLACK);
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    M5.Display.setCursor(0, 0);
    while (!(meter.begin(&Wire, MODULE_4_20MA_ADDR, 2, 1, 100000UL))) {
        M5.Display.println("No Module!");
    }
}

void loop() {
    show_current_value();
    delay(1000);
}
```

## 4. 编译上传

- 下载模式：不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- CoreS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="30%">

- 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/module_fan_v1.1_arduino_example_01.jpg" width="70%">

## 5. 电流量采集

- 本实验选用 PT100 热电偶温度传感器搭配无源电流型传感器使用。完成硬件接线后，烧录代码即可看到采集到的电流模拟量数据。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/743/Unit_AIN4_20mA_1.jpg" width="70%">

- 当传感器温度上升时，电流传感器获取到的电流值也随之上升。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/743/Unit_AIN4_20mA_2.jpg" width="70%">
