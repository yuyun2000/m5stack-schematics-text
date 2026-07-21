# NanoC6 Arduino 示例程序编译与烧录

## 1. 准备工作

- 1.Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2\. 板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5NanoC6`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/505/quickstart_arduino_nanoc6_select_board.png" width="70%" />

## 2. 下载模式

按住按键 GPIO9，然后接上数据线即可进入下载模式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5NanoC6/M5PPT%20(4).gif" width="70%">

## 3. 端口选择

将设备通过 USB 线连接至电脑，在 Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/505/quickstart_arduino_nanoc6_selectport.png" width="70%" />

## 4. 程序编译 & 烧录

在 Arduino IDE 工作区输入下方代码，点击上传按钮，将自动进行程序编译与烧录。

\#> 说明：|1. 本案例基于[Adafruit NeoPixel](https://github.com/adafruit/Adafruit_NeoPixel)库实现，使用前请通过库管理安装[Adafruit NeoPixel](https://github.com/adafruit/Adafruit_NeoPixel)依赖库。
2\. 为了控制待机功耗，M5NanoC6 RGB LED 需要使能灯珠，即需要高电平控制下方代码中的 `ENABLE_PIN` 。

```cpp line-num
#include <Adafruit_NeoPixel.h>

#define LED_PIN    20
#define ENABLE_PIN 19
#define NUM_LEDS   1

Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pinMode(ENABLE_PIN, OUTPUT);
  digitalWrite(ENABLE_PIN, HIGH);
  strip.begin();
  strip.show();
}

void loop() {
    //RED
    strip.setPixelColor(0, strip.Color(255, 0, 0));
    strip.show();
    delay(100);

    //GREEN
    strip.setPixelColor(0, strip.Color(0, 255, 0));
    strip.show();
    delay(100);

    //BLUE
    strip.setPixelColor(0, strip.Color(0, 0, 255));
    strip.show();
    delay(100);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/505/quickstart_arduino_nanoc6_example.png" width="70%">

上传代码后即可看到 M5NanoC6 设备上的 RGB LED 灯循环亮起红绿蓝三色。

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/505/nanoc6_Arduino_rgb.mp4" type="video/mp4"></video>

## 5. 相关资源

- GitHub

  - [NanoC6 Library](https://github.com/m5stack/M5NanoC6)

- Arduino Example

  - [Botton](/zh_CN/arduino/m5nanoc6/button)
  - [LED](/zh_CN/arduino/m5nanoc6/led)
  - [IR NEC](/zh_CN/arduino/m5nanoc6/ir_nec)
  - [Thread](/zh_CN/arduino/m5nanoc6/thread)
  - [Zigbee](/zh_CN/arduino/m5nanoc6/zigbee)
