# Servo Kit 180°/360° Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [ESP32Servo](https://github.com/madhephaestus/ESP32Servo)

- 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Servo Kit 180°](https://shop.m5stack.com/products/servo-kit-180)
  - [Servo Kit 360°](https://shop.m5stack.com/products/servo-kit-360)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/servo_kit/servo_kit_180_02.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/accessory/servo_kit/servo_kit_360_02.webp" width="20%"/>

## 2. 案例程序

- 本教程中使用的主控设备为 CoreS3 ，搭配 Servo Kit 180°/360°。本舵机与主机之间需要通过转接头连接，连接方式如下图所示。根据实际的电路连接修改程序中的引脚定义，设备连接后对应的控制 IO 为 `G2`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1165/Servo_Kit_connection.jpg" width="50%">

- 下方例程主要通过 `writeMicroseconds` 函数控制舵机的转动位置，适用于 Servo Kit 180° 和 Servo Kit 360°。其中 `COUNT_LOW` 和 `COUNT_HIGH` 分别对应舵机的最小和最大脉冲宽度，`STEP` 定义了脉冲宽度的增量步长，`SERVO_PIN` 定义了连接舵机信号线的数字引脚。  
  对于 **Servo Kit 180°**，`COUNT_LOW` 通常对应舵机的 0° 位置，`COUNT_HIGH` 对应 180° 位置。使用 `writeMicroseconds` 函数后，舵机会根据传入的脉冲宽度值转动到相应的位置且维持在该位置，下方例程中 `servo.writeMicroseconds(1500)` 会使 Servo Kit 180° 转动到 90° 位置并保持。  
  对于 **Servo Kit 360°**，`writeMicroseconds` 函数中传入的值控制舵机的旋转速度和方向，`COUNT_LOW` 对应顺时针最大速度，`COUNT_HIGH` 对应逆时针最大速度，而中间值则表示停止转动。`COUNT_LOW ~ 中间值`范围内为顺时针转动，数值越大舵机旋转速度越慢；`中间值 ~ COUNT_HIGH`范围内为逆时针转动，数值越大舵机旋转速度越快，下方例程中`servo.writeMicroseconds(1500)` 会使 Servo Kit 360° 维持停止状态。

```cpp line-num
#include "M5Unified.h"
#include "M5GFX.h"
#include "ESP32Servo.h"       

// Macro definitions for servo control parameters
#define COUNT_LOW  500     // Minimum pulse width in microseconds (μs) for the servo (typically corresponds to 0° position)
#define COUNT_HIGH 2500    // Maximum pulse width in microseconds (μs) for the servo (typically corresponds to 180° position)
#define STEP       100      // Increment step for pulse width (controls how smoothly the servo moves between positions)
#define SERVO_PIN  2       // Digital pin connected to the servo motor's signal wire

Servo servo;              

void setup() {
  M5.begin();
  servo.attach(SERVO_PIN, COUNT_LOW, COUNT_HIGH); // Attach the servo to the specified pin, with defined min (COUNT_LOW) and max (COUNT_HIGH) pulse widths
  M5.Lcd.setFont(&fonts::FreeMonoBoldOblique12pt7b);
  M5.Lcd.drawCenterString("SERVO", 160, 110);
}

void loop() {
  servo.writeMicroseconds(500); 
  delay(2000);
  servo.writeMicroseconds(1500); // 90° for 180° Kit, Stop for 360° Kit
  delay(2000);
  servo.writeMicroseconds(2500);
  delay(2000);
  servo.writeMicroseconds(1500); // 90° for 180° Kit, Stop for 360° Kit
  delay(2000);
}
```

## 3. 编译上传

- 1\. 下载模式：不同设备进行程序烧录前需要下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- CoreS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="30%">

- 2\. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1165/Servo_Kit_Arduino_example.png" width="70%">

## 4. 舵机控制效果

\?> 注意 | 运行过程中请勿手动旋转舵机，以免损坏舵机电机。

- Servo Kit 180° 会依次转动到 0°、90°、180°、90° 位置并循环往复。

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1165/Servo_180_Kit.mp4" type="video/mp4"></video>

- Servo Kit 360° 会依次以最小速度逆时针转动、停止、以最小速度顺时针转动、停止并循环往复。

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1165/Servo_360_Kit.mp4" type="video/mp4"></video>




