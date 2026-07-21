# Unit Ultrasonic-I2C Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-Sonic](https://github.com/m5stack/M5Unit-Sonic)

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit Ultrasonic-I2C](https://shop.m5stack.com/products/ultrasonic-distance-unit-i2c-rcwl-9620)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ULTRASONIC%20I2C/img-b83c05bf-93e6-4e85-8399-a2e2152f2b19.webp" width="20%">


## 2.案例程序

#>案例说明 | 本案例将使用 Unit Ultrasonic-I2C ，实现超声波测距功能，并将测量结果显示到屏幕上。

```cpp line-num
#include <M5Unified.h>
#include <Unit_Sonic.h>

SONIC_I2C sensor;

void setup()
{
    M5.begin();
    // sensor.begin(TwoWire* wire, uint8_t addr, uint8_t sda, uint8_t scl, uint32_t speed);
    sensor.begin(&Wire, 0x57, 2, 1, 400000U);
    M5.Display.setColorDepth(1);
    M5.Display.setFont(&fonts::Orbitron_Light_32);
    M5.Display.setTextDatum(middle_center);
}

int point      = 0;
int last_point = 0;

void loop()
{
    float Distance = sensor.getDistance();
    Serial.printf("Distance: %.2fmm\r\n", Distance);
    M5.Display.fillScreen(TFT_BLACK);
    M5.Display.drawString(String(Distance) + "mm", M5.Display.width() / 2, M5.Display.height() / 2);
    delay(100);
}
```

## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/697/unit_ultrasonic_i2c_example_01.jpg" width="70%">


## 4.超声波测距

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/697/unit_ultrasonic_i2c_example_02.jpg" width="50%">


