# Stamp-S3Bat Arduino 示例程序编译与烧录

## 1. 准备工作

- 1. Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2. 板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5StampS3Bat`。
- 3. 依赖库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成最新版 `M5PM1` 驱动库安装，并根据提示安装全部依赖库。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1221/arduino_stamp_s3bat_select_board.png" width="70%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1221/arduino_stamp_s3bat_lib_01.png" width="70%" />

## 2. 下载模式

将设备通过 USB 线连接至电脑，长按 `PWR` 按钮大约 3s，进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1222/bat-operate_01.gif" width="30%">

## 3. 端口选择

在 Arduino IDE 中选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1221/arduino_stamp_s3bat_select_port.png" width="70%" />

## 4. 程序编译 & 烧录

在 Arduino IDE 工作区粘贴下方代码，点击上传按钮，将自动进行程序编译与烧录。

### Hello World

```cpp line-num
#include "Arduino.h"

void setup()
{
    Serial.begin(115200);
}

void loop()
{
    delay(1000);
    Serial.println("Hello, world!");
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1221/arduino_stamp_s3bat_example_01.png" width="70%">

## 5. 相关资源

- GitHub

  - [M5PM1 Library](https://github.com/m5stack/M5PM1)

- Arduino Example

  - [RGB LED](/zh_CN/arduino/m5stamp_s3bat/rgb_led)
  - [Wakeup](/zh_CN/arduino/m5stamp_s3bat/wakeup)
  - [M5PM1 PMIC](/zh_CN/arduino/m5stamp_s3bat/m5pm1)
