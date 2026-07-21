# Atomic HDriver Base Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 使用到的硬件产品：
  - [AtomS3](https://shop.m5stack.com/products/atoms3-dev-kit-w-0-85-inch-screen)
  - [Atomic HDriver Base](https://shop.m5stack.com/products/atomic-h-bridge-driver-base-drv8876)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic%20H-Driver%20Base/img-c5e7a086-4f4c-4893-a94c-0fd07fdc6699.webp" width="20%">

## 2. 案例程序

- 本教程中使用的主控设备为 AtomS3 ，搭配 Atomic HDriver Base，信号输出引脚为 `G6(IN1)` 、`G7(IN2)`。

```cpp line-num
#include "M5Unified.h"

const int IN1_PIN       = 6;
const int IN2_PIN       = 7;
const int VIN_PIN       = 8;
const int FAULT_PIN     = 5;

int freq          = 10000;
int resolution    = 10;
bool direction    = true;

void setup() {
    M5.begin();

    M5.Display.setTextColor(GREEN);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setFont(&fonts::Orbitron_Light_24);
    M5.Display.drawString("H-Driver", M5.Display.width() / 2, M5.Display.height() / 2);

    ledcAttach(IN1_PIN, freq, resolution);
    ledcAttach(IN2_PIN, freq, resolution);
    pinMode(VIN_PIN, INPUT);
    pinMode(FAULT_PIN, INPUT);
    ledcWrite(IN1_PIN, 0);
    ledcWrite(IN2_PIN, 0);
}

void loop() {
    if (M5.BtnA.pressedFor(1000)) {
        ledcWrite(IN1_PIN, 0);
        ledcWrite(IN2_PIN, 0);
    }

    if (M5.BtnA.wasPressed()) {
        if (direction) {
            ledcWrite(IN1_PIN, 300);
            ledcWrite(IN2_PIN, 0);
        } else {
            ledcWrite(IN1_PIN, 0);
            ledcWrite(IN2_PIN, 300);
        }
        direction = !direction;
    }

    M5.update();
    if (digitalRead(FAULT_PIN) == 0) {
        M5.Display.clear();
        M5.Display.drawString("FAULT!", M5.Display.width() / 2, M5.Display.height() / 2);
    }
}
```

## 3. 编译上传

- 1\. AtomS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

#> 说明| 不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3/download%20mode1.gif" width="30%">

- 2\. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/Atomic_HDriver_Base_Arduino_example.jpg" width="70%">

## 4. 直流电机控制

- 设备上电后，按动主控屏幕，直流电机将开始正转，再次按动屏幕，电机反转。长按屏幕 1 秒，电机可停止转动。（下方视频中使用的是 N20 直流震动电机）

<video style="width:40vw;max-width:40%;height:auto;" controls>
	<source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/931/Atomic_HDriver_Base_Arduino_example.mp4" type="video/mp4"></video>

