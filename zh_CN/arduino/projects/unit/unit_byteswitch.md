# Unit ByteSwitch Arduino 使用教程

## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-ByteButton](https://github.com/m5stack/M5Unit-ByteButton)

#>驱动库|Unit ByteSwitch 在设计上与 Unit ByteButton 非常相似， 因此我们将复用 M5Unit-ByteButton 库进行驱动。

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit ByteSwitch](https://shop.m5stack.com/products/byte-switch-unit-with-8x-switches-stm32g031)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit%20ByteSwitch/3.webp" width="20%">


## 2.案例程序

#>案例说明|Unit ByteSwitch提供了8个钮子开关输入与9个可编程RGB LED, 适合多开关输入应用场景。 其中RGB LED支持两种工作模式, 自动模式(可配置扭子开关不同状态下其对应的RGB LED颜色, 实现灯光同步开关状态), 自定义模式(用户自定义控制当前灯光颜色显示)。


### 输入读取

```cpp line-num
#include <M5Unified.h>
#include "unit_byte.hpp"

uint32_t color_list[]   = {0xff0000, 0x00ff00, 0x0000ff};
uint8_t color_index     = 0;
time_t last_update_time = 0;
uint8_t switchId        = 0x46;
UnitByte dev;

void setup()
{
    M5.begin();
    Serial.begin(115200);
    M5.Display.setFont(&fonts::lgfxJapanMinchoP_20);

    while (!dev.begin(&Wire, switchId, 2, 1, 400000)) {
        M5.Display.drawString("Unit ByteSwitch init Fail!", 0, 0);
        delay(1000);
    }
    dev.setLEDShowMode(BYTE_LED_USER_DEFINED);
    for (uint8_t i = 0; i <= 8; i++) {
        dev.setLEDBrightness(i, 250);
    }
}

void loop()
{
    // M5.Display.clear();
    M5.Display.setCursor(0, 0);
    for (uint8_t i = 0; i < 8; i++) {
        uint8_t switchStatus8Bytes = dev.getSwitchStatus(i);
        M5.Display.printf("CH[%d]: %d\r\n", i, switchStatus8Bytes);
    }

    if (millis() - last_update_time > 1000) {
        color_index = (color_index + 1) % 3;
        for (int i = 0; i <= 8; i++) {
            dev.setRGB888(i, color_list[color_index]);
        }
        last_update_time = millis();
    }
}
```

### RGB LED 自动模式

可配置按键在不同状态下其对应的RGB LED颜色, 实现灯光同步开关状态。

```cpp line-num
const uint32_t colors[] = {
    0xFF0000, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF, 0xFFFFFF, 0xFFA500, 0x808080, 0x00FF00,
};
dev.setLEDShowMode(BYTE_LED_MODE_DEFAULT);
Serial.println("Set LED show sys define.");
delay(1000);
dev.setRGB233(8, colors[1]);
delay(1000);
dev.setFlashWriteBack();
delay(1000);
for (int i = 0; i < 8; i++) {
    dev.setSwitchOffRGB888(i, colors[i]);
    // Output the hexadecimal value of the current color
    Serial.printf("Set Switch Off RGB to %06X\n", (unsigned int)colors[i]);
}
delay(1000);
for (int i = 0; i < 8; i++) {
    dev.setSwitchOnRGB888(i, colors[9 - i]);
    // Output the hexadecimal value of the current color
    Serial.printf("Set Switch On RGB to %06X\n", (unsigned int)colors[i]);
}
delay(1000);
dev.setFlashWriteBack();
```



### 修改I2C地址

Unit ByteSwitch支持修改I2C地址, 便于同时挂载多个设备。参考以下API, 在初始化I2C总线后进行设备地址修改。


```cpp line-num
dev.begin(&Wire, 2, 1, 400000);
dev.setI2CAddress(new_addr);
```

## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">

- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/820/unit_byteswitch_arduino_example_01.jpg" width="70%">


## 4.开关状态与灯光控制

实时显示开关状态与控制 RGB LED颜色切换。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/820/unit_byteswitch_arduino_example_02.jpg" width="50%">





