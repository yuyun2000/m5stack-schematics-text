# Arduino Nesso N1 示例程序编译与烧录

## 1. 准备工作

1. Arduino IDE 安装：参考 [Arduino IDE 安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
2. 板管理安装：参考[板管理安装教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`ArduinoNessoN1`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_select_board.png" width="70%">

3. 依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`，`M5GFX`驱动库安装，并根据提示安装全部依赖库。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_lib_01.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_lib_02.png" width="70%" />

## 2. 下载模式

设备连接 USB 线，长按机身左侧复位按键。当设备内部蓝色 LED 闪烁时，表示设备已成功进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001_operate_01.gif" width="50%">

## 3. 端口选择

将设备通过 USB 线连接至电脑并进入下载模式后， Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_select_port.png" width="70%" />

## 4. 程序编译 & 烧录

打开 M5GFX 驱动库中的案例程序**BarGraph**, 点击上传按钮，将自动进行程序编译与烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_bargraph_example_01.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_bargraph_example_02.png" width="70%">

效果如下图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_bargraph_example_03.jpg" width="50%" />

## 5. 相关资源

- Arduino Library
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
- [Arduino Nesso N1 User Manual](https://docs.arduino.cc/tutorials/nesso-n1/user-manual/)
- Arduino API & Examples
  - [Button](/zh_CN/arduino/arduino_nesso_n1/button)
  - [Display](/zh_CN/arduino/arduino_nesso_n1/display)
  - [Touch](/zh_CN/arduino/arduino_nesso_n1/touch)
  - [Buzzer](/zh_CN/arduino/arduino_nesso_n1/buzzer)
  - [IMU](/zh_CN/arduino/arduino_nesso_n1/imu)
  - [Power](/zh_CN/arduino/arduino_nesso_n1/power)
  - [LoRa](/zh_CN/arduino/arduino_nesso_n1/lora)
  - [LED](/zh_CN/arduino/arduino_nesso_n1/led)
  - [IR NEC](/zh_CN/arduino/arduino_nesso_n1/ir_nec)
