# StamPLC Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5StamPLC`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_arduino_select_board_01.jpg" width="70%">

- 3.依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5StamPLC`，`M5Unified`，`M5GFX`驱动库安装。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_arduino_lib_01.jpg" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_arduino_lib_02.jpg" width="70%">

## 2.下载模式

- 长按StamPLC上的Boot按键, 等待红灯亮起后释放，此时设备进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_download_mode.gif" width="50%" />

## 3.端口选择

- 将设备通过USB线连接至电脑，在设备进入下载模式后， Arduino IDE中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_arduino_select_port_01.jpg" width="70%">

## 4.程序编译&烧录

- 打开驱动库中的案例程序"display", 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_arduino_example_01.jpg" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_arduino_example_02.jpg" width="70%">

效果如下图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/stamplc_arduino_example_03.jpg" width="70%">

## 5.相关资源

- **Github**
  - [M5StamPLC Library](https://github.com/m5stack/M5StamPLC)

- **Arduino API & Examples**
  - [Button](/zh_CN/arduino/m5stamplc/button)
  - [Buzzer](/zh_CN/arduino/m5stamplc/buzzer)
  - [CAN](/zh_CN/arduino/m5stamplc/can)
  - [Display](/zh_CN/arduino/m5stamplc/display)
  - [Input & Output](/zh_CN/arduino/m5stamplc/input_output)
  - [Modbus](/zh_CN/arduino/m5stamplc/modbus)
  - [RGB LED](/zh_CN/arduino/m5stamplc/rgb_led)
  - [RTC](/zh_CN/arduino/m5stamplc/rtc)
  - [SDCard](/zh_CN/arduino/m5stamplc/sd_card)
  - [Sensor](/zh_CN/arduino/m5stamplc/sensor)