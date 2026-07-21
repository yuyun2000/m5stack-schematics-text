# Dial Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE 安装：参考[Arduino IDE 安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2.板管理安装：参考[板管理安装教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板 `M5dial`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5dial/quickstart_arduino_dial_select_board.png" width="70%">

- 3.驱动库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成 `M5dial` 驱动库安装，并根据提示下载全部依赖库。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5dial/quickstart_arduino_dial_download_library.png" width="70%">

## 2.下载模式

按住产品背面 Stamp 模组上的 G0 按键，通过 USB-C 数据线连接至电脑后松开按键，设备将进入下载模式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/dial%20(2).gif" width="30%">

## 3.端口选择

完成上述步骤后，可在 Arduino IDE 中选择对应的控制板和设备端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5dial/quickstart_arduino_dial_select_port.png" width="70%">

## 4.程序编译&烧录

打开 `M5Dial` 库示例程序中的 `display`，点击上传代码。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5dial/quickstart_arduino_dial_select_demo.png" width="70%">

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5dial/quickstart_arduino_dial_select_demoupload.png" width="70%">

编译、上传完成后，屏幕显示效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/Arduino_display.gif" width="30%">

## 5.相关资源

- **GitHub**
  - [M5Dial Library](https://github.com/m5stack/M5Dial)
- **Arduino API & Examples**
  - [Button](/zh_CN/arduino/m5dial/button)
  - [Buzzer](/zh_CN/arduino/m5dial/buzzer)
  - [Display](/zh_CN/arduino/m5dial/display)
  - [Encoder](/zh_CN/arduino/m5dial/encoder)
  - [RFID](/zh_CN/arduino/m5dial/rfid)
  - [RTC](/zh_CN/arduino/m5dial/rtc)
  - [Touch](/zh_CN/arduino/m5dial/touch)
  - [Wakeup](/zh_CN/arduino/m5dial/wakeup)