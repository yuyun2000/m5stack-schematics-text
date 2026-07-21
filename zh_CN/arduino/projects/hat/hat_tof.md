# Hat ToF Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库:

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [VL53L0X](https://github.com/pololu/vl53l0x-arduino)

- 使用到的硬件产品:
  - [StickC-Plus2](https://shop.m5stack.com/products/m5stickc-plus2-esp32-mini-iot-development-kit)
  - [Hat ToF](https://shop.m5stack.com/products/m5stickc-tof-hatvl53l0x)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5StickC%20PLUS2/3.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-tof/hat-tof_cover_01.webp" width="20%">

## 2. 案例程序

\#> 案例说明 | Hat ToF 是一款专为 SticKC 设计的高精度激光测距传感器，内部集成 ST 激光测距芯片 VL53L0X、940nm VCSEL 发射器，通过测量激光信号到被测物体的往返时间，能够在不到 30ms 的时间内测量 2m 范围内的绝对距离。本案例将使用 StickC-Plus2 通过 I2C 接口来驱动控制 Hat ToF，并在 StickC-Plus2 的屏幕和电脑的串口监视器打印数据。

### 完整程序

```cpp line-num
#include <M5Unified.h>
#include <Wire.h>
#include <VL53L0X.h>

VL53L0X sensor;

void setup() {
    M5.begin();
    Serial.begin(115200);

    // I2C initialization (SDA: G0, SCL: G26)
    Wire.begin(0, 26);

    // Sensor initialization
    sensor.setTimeout(500);
    if (!sensor.init()) {
        Serial.println("Sensor init failed!");
        while (1);
    }

    // Set measuring mode (default: 120cm)
    sensor.setMeasurementTimingBudget(200000);

    Serial.println("Hat ToF Ready");
}

void loop() {
    M5.update();

    uint16_t distance = sensor.readRangeSingleMillimeters();

    if (sensor.timeoutOccurred()) {
        Serial.println("Timeout!");
    } else {
        Serial.printf("Distance: %.1f cm\n", distance / 10.0);
        M5.Display.fillScreen(BLACK);
        M5.Display.setRotation(1);
        M5.Display.setTextSize(2);
        M5.Display.setCursor(10, 40, 2);
        M5.Display.setTextColor(WHITE);
        M5.Display.printf("Distance: %.1f cm\n", distance / 10.0);
    }

    delay(100);
}
```

## 3. 编译上传

1. 进入下载模式：不同的 Stick 设备进行程序烧录前需要安装对应的驱动程序，不同的主控设备使用的驱动与安装步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体设备对应的操作方式。

2. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/854/arduino_hat_tof_example_01.png" width="70%">

## 4.Hat ToF 激光测距传感器数据显示

该程序将检测 Hat ToF 的激光测距传感器的数据，并在 StickC-Plus2 的屏幕和电脑的串口监视器打印数据：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/854/arduino_hat_tof_example_02.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/854/arduino_hat_tof_example_serial_03.png" width="70%">
