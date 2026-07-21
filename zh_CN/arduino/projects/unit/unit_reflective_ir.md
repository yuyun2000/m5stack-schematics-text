# Unit Reflective IR Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit Reflective IR](https://shop.m5stack.com/products/infrared-reflective-sensor-unit)


<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Reflective%20IR/img-c4f17c7c-e508-4876-8135-4f3a7c6e1f9a.webp" width="20%">


## 2.案例程序

#>案例说明|Unit Reflective IR 是一款机械式继电器，主要用于检测目标物体的反射红外光，并通过模拟信号和数字信号输出来指示检测状态。本案例将读取 Unit Reflective IR 输出数字信号与模拟信号，并进行显示。注：读取的模拟信号值与数字信号主要用区分障碍物红外反射光状态。并不能转换为精确的测量距离。


```cpp line-num
#include <M5Unified.h>
#include <Arduino.h>

#define IR_ANALOG_PIN  8
#define IR_DIGITAL_PIN 9

void setup()
{
    M5.begin();
    M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
    pinMode(IR_ANALOG_PIN, INPUT);
    pinMode(IR_DIGITAL_PIN, INPUT);
}

void loop()
{
    int analog  = analogRead(IR_ANALOG_PIN);
    int digital = digitalRead(IR_DIGITAL_PIN);

    M5.Display.clear();
    M5.Display.setCursor(20, 40);
    M5.Display.printf("analog: %d", analog);
    M5.Display.setCursor(20, 80);
    M5.Display.printf("digital: %d", digital);

    Serial.printf("analog: %d\r\n", analog);
    Serial.printf("digital: %d\r\n", digital);
    delay(1000);
}
```


## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">


- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/747/unit_reflective_ir_example_01.jpg" width="70%">


## 4.检测数据读取

读取 Unit Reflective IR 输出数字信号与模拟信号，并进行显示。


<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/747/unit_reflective_ir_example_02.jpg" width="70%">
