# Hat CBack Driver Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Hat-CBack-Driver](https://github.com/m5stack/M5Hat-CBack-Driver)

- 3.使用到的硬件产品:
  - [StickC-Plus2](https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit)
  - [Hat CBack Driver](https://shop.m5stack.com/products/c-back-hat-with-servo-driver-stm32f0)
  - [Servo Kit 180°](https://shop.m5stack.com/products/servo-kit-180)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5StickC%20PLUS2/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/hat/c_back_driver/c_back_driver_cover_01.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/servo_kit/servo_kit_180_07.webp" width="20%">


## 2.案例程序

#>案例说明 | Hat CBack Driver 是一款为 StickC 主控系列设计的舵机驱动板，提供了 4 通道舵机控制与两个 Grove 拓展接口（I2C+GPIO）。 其中舵机的供电的供电将直接连接至 StickC 主控电池，以获得较好的供电能力。本案例将演示基本的舵机驱动控制，以及对 GPIO 拓展接口（黑色接口）实现基本的数字信号输出，模拟信号输入。

### 舵机接线

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/873/hat_cback_driver_servo_connect_01.jpg" width="50%">


### 完整程序


```cpp line-num
#include <M5Unified.h>
#include "M5HatCBackDriver.h"

M5HatCBackDriver driver;

void setup()
{
   M5.begin();
   Serial.begin(115200);
   Wire.begin(0, 26);
   M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
   M5.Display.setRotation(1);
   while (!driver.begin(&Wire, M5_HAT_CBACK_DRIVER_I2C_ADDR)) {
       M5.Display.fillScreen(YELLOW);
       Serial.println("Hat CBack Driver Init Fail");
       M5.Display.setCursor(0, 0);
       M5.Display.println("Hat CBack Driver Init Fail");
       delay(1000);
   };
   M5.Display.setCursor(0, 0);
   M5.Display.fillScreen(GREEN);
   Serial.println("Hat CBack Driver Init OK");
   M5.Display.println("Hat CBack Driver Init OK");
   M5.Display.println("Start Control Servo");
}

void loop()
{
   for (int i = 0; i <= 3; i++) {   // channel 0-3
       driver.setServoAngle(i, 0);  // 0-180 degree
       // driver.setServoPulse(i,500); // 500-2500us
       delay(200);
   }
   for (int i = 0; i <= 3; i++) {     // channel 0-3
       driver.setServoAngle(i, 180);  // 0-180 degree
       // driver.setServoPulse(i,2500);  // 500-2500us
       delay(200);
   }
   driver.digitalWritePortB(1);
   delay(1000);
   driver.digitalWritePortB(0);
   Serial.print("PortB Analog Read: ");
   Serial.println(driver.analogReadPortB());
}
```


## 3.编译上传

- 1.下载模式: 不同的Stick设备进行程序烧录前需要安装对应的驱动程序, 不同的主控设备使用的驱动与安装步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体设备对应的操作方式。

- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/873/hat_cback_driver_arduino_example_01.jpg" width="70%">

## 4.舵机驱动

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/873/hat_cback_driver_arduino_example_02.jpg" width="50%">


