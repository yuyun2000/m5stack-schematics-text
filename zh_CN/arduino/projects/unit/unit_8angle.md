# Unit 8Angle Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。
- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-8Angle](https://github.com/m5stack/M5Unit-8Angle)

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit 8Angle](https://shop.m5stack.com/products/8-angle-unit-with-potentiometer)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Angle/img-a0f2ee3f-5068-4926-9224-1d1986cb71be.webp" width="20%">


## 2.案例程序

#>案例说明 | Unit 8Angle 是一款集成 8 路可调电位器的输入单元，同时集成了 9 颗可编程的 RGB LED 灯 与 1个切换开关。在本案例中，我们将借助 CoreS3 主控，通过其 PORT.A 拓展接口，读取各个通道电位器的输入状态和切换开关的状态，同时 对 RGB LED 灯进行控制。


```cpp line-num
#include <M5Unified.h>
#include "M5_ANGLE8.h"

M5_ANGLE8 dev;
uint32_t color_list[]   = {0xff0000, 0x00ff00, 0x0000ff};
uint8_t color_index     = 0;
time_t last_update_time = 0;

void setup()
{
    M5.begin();
    Serial.begin(115200);
    M5.Display.setFont(&fonts::lgfxJapanMinchoP_20);
    Wire.begin(2, 1, 100000L);
    while (!dev.begin(ANGLE8_I2C_ADDR)) {
        M5.Display.drawString("Unit 8Angle init Fail!", M5.Display.width() / 2, M5.Display.height() / 2);
        delay(1000);
    }
}

void loop()
{
    bool switch_status = dev.getDigitalInput();
    M5.Display.clear();
    M5.Display.setCursor(0, 0);
    M5.Display.printf("Switch: %s\r\n", switch_status ? "ON" : "OFF");
    for (uint8_t i = 0; i < ANGLE8_TOTAL_ADC; i++) {
        uint16_t adc_v = dev.getAnalogInput(i, _12bit);
        M5.Display.printf("CH[%d]: %d\r\n", i, adc_v);
    }
    if (millis() - last_update_time > 1000) {
        color_index = (color_index + 1) % 3;
        for (uint8_t i = 0; i < ANGLE8_TOTAL_LED; i++) {
            dev.setLEDColor(i, color_list[color_index], 80);
        }
        last_update_time = millis();
    }
    delay(100);
}
```

## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。


<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/811/unit_8angle_arduino_example_01.jpg" width="70%">


## 4.旋钮状态读取

读取与显示旋钮和开关状态，同时控制间隔1s切换 RGB LED颜色。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/811/unit_8angle_arduino_example_02.jpg" width="50%">

