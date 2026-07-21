# Unit C6L Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE 安装：参考 [Arduino IDE 安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2.板管理安装：参考[板管理安装教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5UnitC6L`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Arduino_board.png" width="70%">

- 3.驱动库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`、`M5GFX`驱动库安装，并根据提示安装全部依赖库。

## 2.端口选择

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/Download_mode.gif" width="30%">

将设备通过 USB-C 数据线连接至电脑，长按侧面的复位按键 3 秒直到绿灯变红，此时设备进入下载模式，可在 Arduino IDE 中选择对应的主控和设备端口。

## 3.程序编译&烧录

打开`M5GFX`库中的示例程序`Basic -> GameOfLife`，点击上传按钮，程序将编译并上传至 Unit C6L。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/GameOfLife.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/upload.png" width="70%">

运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/GameOfLife.jpeg" width="50%">

## 4.相关资源

- Arduino Library
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
- Arduino API & Examples
  - [Button](/zh_CN/arduino/unit_c6l/button)
  - [Buzzer](/zh_CN/arduino/unit_c6l/buzzer)
  - [Display](/zh_CN/arduino/unit_c6l/display)
  - [LoRa](/zh_CN/arduino/unit_c6l/lora)
  - [RGB LED](/zh_CN/arduino/unit_c6l/rgb)