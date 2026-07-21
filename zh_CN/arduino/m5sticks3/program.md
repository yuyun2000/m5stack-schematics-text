# StickS3 Arduino 示例程序编译与烧录

## 1. 准备工作

- 1\. Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2\. 板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5StickS3`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/quickstart_arduino_sticks3_select_board.png" width="70%" />

- 3\. 依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`，`M5GFX`驱动库安装，并根据提示安装全部依赖库。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_arduino_lib_01.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/sticks3_arduino_lib_02.png" width="70%" />

## 2. 下载模式

长按机身侧边复位按键（大约2秒），当设备内部绿色 LED 闪烁时，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/stickS3_operate_01.gif" width="50%">

## 3. 端口选择

将设备通过 USB 线连接至电脑，在设备进入下载模式后， Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/quickstart_arduino_sticks3_select_port.png" width="70%" />

## 4. 程序编译 & 烧录

打开驱动库中的案例程序 “ScrollGraph”, 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/quickstart_arduino_sticks3_select_demo.png" width="70%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/quickstart_arduino_sticks3_select_demoupload.png" width="70%">

显示效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_demo.jpg" width="40%">

## 5. 相关资源

- **Arduino Library**
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- **Arduino API & Examples**
  - [Battery](/zh_CN/arduino/m5sticks3/battery)
  - [Button](/zh_CN/arduino/m5sticks3/button)
  - [Display](/zh_CN/arduino/m5sticks3/display)
  - [IMU](/zh_CN/arduino/m5sticks3/imu)
  - [IR NEC](/zh_CN/arduino/m5sticks3/ir_nec)
  - [Mic](/zh_CN/arduino/m5sticks3/mic)
  - [Speaker](/zh_CN/arduino/m5sticks3/speaker)
  - [Wakeup](/zh_CN/arduino/m5sticks3/wakeup)
