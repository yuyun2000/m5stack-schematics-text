# Stamp-C3 Arduino 示例程序编译与烧录

## 1. 准备工作

- 1.Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2\. 板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5StampC3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/quickstart_arduino_stampc3_select_board.png" width="70%" />

## 2.USB 驱动安装

\#> 驱动程序安装提示 | 点击下方连接下载匹配操作系统的驱动程序。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(`CH9102_VCP_SER_MacOS v1.7`在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。)

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

## 3. 端口选择

将设备通过 USB 线连接至电脑，在 Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/quickstart_arduino_stampc3_selectport.png" width="70%" />

## 4. 程序编译 & 烧录

?> 注意：| 请设置 Arduino IDE 中 `Tools` -> `USB-CDC On Boot` 选项为 `Disabled`，否则无法使用串口，选项位置如下图。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/quickstart_arduino_stampc3_USB_CDC.png" width="70%" />

在 Arduino IDE 工作区输入下方代码，点击上传按钮，将自动进行程序编译与烧录。

\#> 说明：| 本案例基于[FastLED](https://github.com/FastLED/FastLED)库实现，使用前请通过库管理安装[FastLED](https://github.com/FastLED/FastLED)依赖库。

```cpp line-num
#include <Arduino.h>
#include <FastLED.h>

#define PIN_BUTTON 3
#define PIN_LED    2
#define NUM_LEDS   1

CRGB leds[NUM_LEDS];
uint8_t led_ih             = 0;
uint8_t led_status         = 0;
String led_status_string[] = {"Rainbow", "Red", "Green", "Blue"};

void setup() {
    Serial.begin(115200);
    Serial.println("Stamp-C3 demo!");

    pinMode(PIN_BUTTON, INPUT_PULLUP);

    FastLED.addLeds<SK6812, PIN_LED, GRB>(leds, NUM_LEDS);
}

void loop() {
    switch (led_status) {
        case 0:
            leds[0] = CHSV(led_ih, 255, 255);
            break;
        case 1:
            leds[0] = CRGB::Red;
            break;
        case 2:
            leds[0] = CRGB::Green;
            break;
        case 3:
            leds[0] = CRGB::Blue;
            break;
        default:
            break;
    }
    FastLED.show();
    led_ih++;
    delay(15);

    if (!digitalRead(PIN_BUTTON)) {
        delay(5);
        if (!digitalRead(PIN_BUTTON)) {
            led_status++;
            if (led_status > 3) led_status = 0;
            while (!digitalRead(PIN_BUTTON))
                ;
            Serial.print("LED status updated: ");
            Serial.println(led_status_string[led_status]);
        }
    }
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/quickstart_arduino_stampc3_example.png" width="70%">

上传代码后，Stamp-C3 设备上的 RGB LED 灯将自动亮起。通过按动按钮可循环切换 LED 的显示颜色，同时设备会通过串口输出当前的灯光状态信息（如颜色值或模式），方便调试与交互反馈。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/quickstart_arduino_stampc3_examplepic.jpg" width="50%">
