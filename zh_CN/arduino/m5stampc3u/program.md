# Stamp-C3U Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5StampC3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/quickstart_arduino_stampc3_select_board.png" width="70%" />

## 2.下载模式

按住 Stamp-C3U 上的 IO 按键不松手, 将设备通过USB线连接至电脑, 此时电脑上可识别到端口，表示设备已进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/525/StampC3U.gif" width="30%"/>

## 3.端口选择

等待设备识别端口成功，在Arduino IDE中选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/525/quickstart_arduino_stampc3u_selectport.png" width="70%" />

## 4.程序编译&烧录

?>注意：|请设置 Arduino IDE 中 `Tools` -> `USB-CDC On Boot` 选项为 `Enabled`，否则无法使用串口，选项位置如下图。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/525/quickstart_arduino_stampc3u_USB_CDC.png" width="70%" />

在 Arduino IDE 工作区输入下方代码, 点击上传按钮，将自动进行程序编译与烧录。

#>说明：|本案例基于[FastLED](https://github.com/FastLED/FastLED)库实现, 使用前请通过库管理安装[FastLED](https://github.com/FastLED/FastLED)依赖库。  

```cpp line-num
#include <Arduino.h>
#include <FastLED.h>

#define PIN_BUTTON 9
#define PIN_LED    2
#define NUM_LEDS   1

CRGB leds[NUM_LEDS];
uint8_t led_ih             = 0;
uint8_t led_status         = 0;
String led_status_string[] = {"Rainbow", "Red", "Green", "Blue"};

void setup() {
    Serial.begin(115200);
    Serial.println("Stamp-C3U demo!");

    pinMode(PIN_BUTTON, INPUT);

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

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/525/quickstart_arduino_stampc3u_example.png" width="70%">

上传代码后即可看到 Stamp-C3U 设备上的 RGB LED 灯亮起，按动 IO 按键可以切换显示颜色，打开串口监视器即可查看返回的灯光状态信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/525/quickstart_arduino_stampc3u_examplepic.jpg" width="50%">
 