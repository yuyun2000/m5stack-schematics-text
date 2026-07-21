# StopWatch Arduino 示例程序编译与烧录

## 1. 准备工作

- 1. Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2\.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板 `M5StopWatch`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/quickstart_arduino_StopWatch_select_board.png" width="70%" />

- 3\.依赖库安装: 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`、`M5GFX`驱动库安装，并根据提示安装全部依赖库。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/StopWatch_arduino_lib_01.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/StopWatch_arduino_lib_02.png" width="70%">

## 2. 下载模式

- 长按复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/C132-download-mode.gif" width="40%"/>

## 3. 端口选择

将设备通过 USB 线连接至电脑, Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/quickstart_arduino_StopWatch_select_port.png" width="70%"/>

## 4. 程序编译 & 烧录

打开驱动库中的案例程序 “BarGraph”, 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/quickstart_arduino_StopWatch_select_demo.png" width="70%"/>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/quickstart_arduino_StopWatch_select_demoupload.png" width="70%"/>

例程效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1242/quickstart_arduino_StopWatch_example.jpg" width="40%"/>

## 5. 相关资源

- Arduino Library
  - [M5Unified](https://github.com/m5stack/M5Unified)
- Arduino API & Examples
  - [Battery](/zh_CN/arduino/stopwatch/battery)
  - [Button](/zh_CN/arduino/stopwatch/button)
  - [Display](/zh_CN/arduino/stopwatch/display)
  - [IMU](/zh_CN/arduino/stopwatch/imu)
  - [MIC](/zh_CN/arduino/stopwatch/mic)
  - [RTC](/zh_CN/arduino/stopwatch/rtc)
  - [Speaker](/zh_CN/arduino/stopwatch/speaker)
  - [Touch](/zh_CN/arduino/stopwatch/touch)
  - [Vibration](/zh_CN/arduino/stopwatch/vibration)
  - [M5PM1 & M5IOE1](/zh_CN/arduino/stopwatch/m5pm1&m5ioe1)