# Atom VoiceS3R Arduino 示例程序编译与烧录

## 1. 准备工作

- 1.Arduino IDE 安装：参考 [Arduino IDE 安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2\. 板管理安装：参考[板管理安装教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5AtomS3R`（Atom VoiceS3R 与 AtomS3R 使用相同主控）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/Arduino_board.png" width="70%">

- 3\. 驱动库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`、`M5GFX`驱动库安装，并根据提示安装全部依赖库。

## 2. 端口选择

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/Atom_EchoS3R_opera_01.gif" width="30%">

将设备通过 USB-C 数据线连接至电脑，长按侧面的复位按键 3 秒直到绿灯闪烁，此时设备进入下载模式，可在 Arduino IDE 中选择对应的主控和设备端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/Arduino_port.png" width="70%">

## 3. 程序编译 & 烧录

```cpp line-num
#include "M5Unified.h"

void setup() {
  M5.begin();
}

void loop() {
  M5.Speaker.tone(7000, 100);  // frequency, duration
  delay(1000);
  M5.Speaker.tone(4000, 20);  // frequency, duration
  delay(1000);
}
```

将以上程序复制到 Arduino IDE，点击上传按钮，程序编译上传后将使用扬声器播放蜂鸣声。

## 4. 相关资源

- Arduino Library
  - [M5Unified - GitHub](https://github.com/m5stack/M5Unified)
- Arduino API & Examples
  - [Button](/zh_CN/arduino/atom_echos3r/button)
  - [IR](/zh_CN/arduino/atom_echos3r/ir)
  - [Mic](/zh_CN/arduino/atom_echos3r/mic)
  - [Speaker](/zh_CN/arduino/atom_echos3r/speaker)
