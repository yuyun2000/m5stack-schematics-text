# Hat Servo Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库:

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 使用到的硬件产品:
  - [StickC-Plus2](https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit)
  - [Hat Servo](https://shop.m5stack.com/products/m5stickc-servo-hat)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5StickC%20PLUS2/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-servo/hat-servo_cover_01.webp" width="20%">

## 2. 案例程序

\#> 案例说明 | Hat Servo 是一款供 StickC 使用的伺服电机模块。 舵机型号为 ES9251II，运动角度为 165° ± 10°，采用 PWM 的控制方式控制旋转角度。本案例将使用 StickC-Plus2 通过 GPIO 26 引脚输出 PWM 信号来控制 Hat Servo 的旋转角度，并在 M5StickC Plus2 的屏幕和电脑的串口监视器打印当前角度和状态信息。

### 完整程序

```cpp line-num
#include <M5Unified.h>

const int servo_pin = 26;
const int freq = 50;
const int resolution = 16;  // Use high resolution

void setup() {
    M5.begin();
    Serial.begin(115200);
    ledcAttach(servo_pin, freq, resolution);
}

int angleToDuty(int angle) {
    int min_us = 600;
    int max_us = 2400;

    // Ensure angle is within range
    angle = constrain(angle, 0, 165);

    int pulse_us = map(angle, 0, 165, min_us, max_us);
    int duty = (pulse_us * 65535L) / 20000;

    return duty;
}

void loop() {
    M5.Display.fillRect(0, 100, 320, 60, BLACK);
    M5.Display.setCursor(20, 100, 2);
    M5.Display.print("Moving 0->165");
    Serial.println("Moving 0->165");

    for(int angle = 0; angle <= 165; angle ++) {
        int duty = angleToDuty(angle);
        ledcWrite(servo_pin, duty);

         // Display current angle on M5StickC-Plus2
        M5.Display.fillRect(20, 120, 100, 20, BLACK);
        M5.Display.setCursor(20, 120, 2);
        M5.Display.printf("Angle: %3d", angle);
        Serial.printf("Angle: %3d\n", angle);

        delay(50);  // Control rotation speed
    }

    delay(1000);

    M5.Display.fillRect(0, 100, 320, 60, BLACK);
    M5.Display.setCursor(20, 100, 2);
    M5.Display.print("Moving 165->0");
    Serial.println("Moving 165->0");

    for(int angle = 165; angle >= 0; angle --) {
        int duty = angleToDuty(angle);
        ledcWrite(servo_pin, duty);

        M5.Display.fillRect(20, 120, 100, 20, BLACK);
        M5.Display.setCursor(20, 120, 2);
        M5.Display.printf("Angle: %3d", angle);
        Serial.printf("Angle: %3d\n", angle);

        delay(50);  // Control rotation speed
    }

    delay(1000);
}
```

## 3. 编译上传

1. 进入下载模式：不同的 Stick 设备进行程序烧录前需要安装对应的驱动程序，不同的主控设备使用的驱动与安装步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体设备对应的操作方式。

2. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/870/arduino_hat_servo_example_01.png" width="70%">

## 4.Hat Servo 当前角度和状态信息显示

该程序将控制 Hat Servo 的旋转角度，并在 StickC-Plus2 的屏幕和电脑的串口监视器打印当前角度和状态信息：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/870/arduino_hat_servo_example_02.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/870/arduino_hat_servo_example_serial_03.png" width="70%">
