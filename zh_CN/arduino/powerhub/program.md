# PowerHub Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE 安装：参考 [Arduino IDE 安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2.板管理安装：参考[板管理安装教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5PowerHub`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_board.png" width="70%">

- 3.驱动库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`驱动库安装，并根据提示安装全部依赖库。

?>兼容性提示|最新版 M5Unified 驱动基于 ESP-IDF v5.x，不支持 ESP-IDF v4.x，因此支持 Arduino IDE 但不支持 PlatformIO。

## 2.端口选择

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Download_mode.gif" width="50%">

将设备通过 USB-C 数据线连接至电脑，长按侧面的 BtnPWR 按键 3 秒直到黑色天线旁边的指示灯蓝色闪烁多次，此时设备进入下载模式，可在 Arduino IDE 中选择对应的主控和设备端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_port.png" width="70%">

## 3.程序编译&烧录

```cpp line-num
#include <M5Unified.h>

void setup() {
  M5.begin();
  M5.Led.setBrightness(127);
}

void loop() {
  M5.update();

  M5.Led.setAllColor(TFT_WHITE);
  M5.Led.display();
  delay(500);

  M5.Led.setAllColor(TFT_BLACK);
  M5.Led.display();
  delay(500);
}
```

将以上程序复制到 Arduino IDE，点击上传按钮，程序编译上传后所有 LED 灯将会白色闪烁：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_program.gif" width="50%">

## 4.相关资源

- Arduino Library
  - [M5Unified](https://github.com/m5stack/M5Unified)
- Arduino API & Examples
  - [Button](/zh_CN/arduino/powerhub/button)
  - [CAN](/zh_CN/arduino/powerhub/can)
  - [Power](/zh_CN/arduino/powerhub/power)
  - [RGB LED](/zh_CN/arduino/powerhub/rgb)
  - [RS485](/zh_CN/arduino/powerhub/rs485)
  - [RTC](/zh_CN/arduino/powerhub/rtc)
  - [Wakeup](/zh_CN/arduino/powerhub/wakeup)