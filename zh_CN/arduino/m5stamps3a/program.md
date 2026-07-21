# Stamp-S3A Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5StampS3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/quickstart_arduino_stamps3a_select_board.png" width="70%" />

## 2.下载模式

按住 Stamp-S3A 上的 G0 按键不松手, 将设备通过USB线连接至电脑, 此时电脑上可识别到端口，表示设备已进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Stamp-S3A.gif" width="30%"/>

## 3.端口选择

等待设备识别端口成功，在Arduino IDE中选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/quickstart_arduino_stamps3a_selectport.png" width="70%" />

## 4.程序编译&烧录

在 Arduino IDE 工作区输入下方代码, 点击上传按钮，将自动进行程序编译与烧录。

#>说明：|1.本案例基于[FastLED](https://github.com/FastLED/FastLED)库实现, 使用前请通过库管理安装[FastLED](https://github.com/FastLED/FastLED)依赖库。   
2.为了控制待机功耗，Stamp-S3A RGB LED 需要使能灯珠，即需要高电平控制下方代码中的 `LED_EN` 。

```cpp line-num
#include <Arduino.h>
#include <FastLED.h>

#define PIN_BUTTON 0
#define PIN_LED    21
#define NUM_LEDS   1
#define LED_EN     38

CRGB leds[NUM_LEDS];
uint8_t led_ih             = 0;
uint8_t led_status         = 0;
String led_status_string[] = {"Rainbow", "Red", "Green", "Blue"};

void setup() {
    Serial.begin(115200);
    Serial.println("Stamp-S3A demo!");

    pinMode(LED_EN, OUTPUT);
    digitalWrite(LED_EN, HIGH);
    pinMode(PIN_BUTTON, INPUT);

    FastLED.addLeds<WS2812, PIN_LED, GRB>(leds, NUM_LEDS);
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

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/quickstart_arduino_stamps3a_example.png" width="70%">

上传代码后，Stamp-S3A 设备上的 RGB LED 灯将自动亮起。通过按动按钮可循环切换 LED 的显示颜色，同时设备会通过串口输出当前的灯光状态信息（如颜色值或模式），方便调试与交互反馈。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/quickstart_arduino_stamps3a_examplepic.jpg" width="50%">
 