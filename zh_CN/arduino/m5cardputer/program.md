# Cardputer Arduino 示例程序编译与烧录

本页面内容适用于 Cardputer 和 Cardputer-Adv。

## 1.准备工作

- 1.Arduino IDE 安装：参考[Arduino IDE 安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2.板管理安装：参考[板管理安装教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5Cardputer`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5cardputer/quickstart_arduino_cardputer_select_board.png" width="70%">

- 3.依赖库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Cardputer`驱动库安装，并根据提示下载全部依赖库。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5cardputer/quickstart_arduino_cardputer_download_library.png" width="70%">

## 2.下载模式

将产品上侧面的开关置于 OFF，按住旁边的 G0 按键，通过 USB-C 数据线连接至电脑后松开按键，设备将进入下载模式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Cardputer/cardputer%20(2).gif" width="50%">

## 3.端口选择

完成上述步骤后，可在 Arduino IDE 中选择对应的开发板和设备端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5cardputer/quickstart_arduino_cardputer_select_port.png" width="70%">

## 4.程序编译&烧录

打开`M5Cardputer`驱动库中的示例程序`Basic -> display`，点击上传按钮，将程序编译并烧录至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Arduino_example.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5cardputer/quickstart_arduino_cardputer_select_demoupload.png" width="70%">

运行效果如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Arduino_display.gif" width="50%">

## 5.相关资源

- GitHub
  - [M5Cardputer Library](https://github.com/m5stack/M5Cardputer)

- Arduino API & Examples
  - [Battery](/zh_CN/arduino/m5cardputer/battery)
  - [Button](/zh_CN/arduino/m5cardputer/button)
  - [Display](/zh_CN/arduino/m5cardputer/display)
  - [IMU](/zh_CN/arduino/m5cardputer/imu)
  - [IR](/zh_CN/arduino/m5cardputer/ir_nec)
  - [Keyboard](/zh_CN/arduino/m5cardputer/keyboard)
  - [Mic](/zh_CN/arduino/m5cardputer/mic)
  - [microSD](/zh_CN/arduino/m5cardputer/sdcard)
  - [Speaker](/zh_CN/arduino/m5cardputer/speaker)