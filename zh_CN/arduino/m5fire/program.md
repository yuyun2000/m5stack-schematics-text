# Fire Arduino 示例程序编译与烧录

## 1.准备工作

- 1.Arduino IDE 安装：参考 [Arduino IDE 安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2.板管理安装：参考[板管理安装教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5Fire`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/quickstart_arduino_fire_select_board.png" width="70%">

- 3.驱动库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5Unified`、`M5GFX`驱动库安装，并根据提示安装全部依赖库。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/fire_arduino_lib_01.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/fire_arduino_lib_02.png" width="70%">

## 2.USB驱动安装

点击下方链接下载并安装对应操作系统的驱动程序。

目前存在两种驱动芯片版本：CP210x（适用于 `CP2104`）和 CH9102（适用于 `CH9102`）。若您不确定您的设备所用的 USB 芯片，可同时安装两种驱动。

在使用时，若出现无法正常下载程序（提示超时或者 Failed to write to target RAM）的情况，可尝试重新安装设备驱动。

| 驱动名称               | 适用驱动芯片 | 下载链接                                                                                             |
| ---------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows     | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS       | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux       | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_MacOS_v1.7  | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

#> 注意 | CH9102_VCP_MacOS_v1.7 在安装过程中可能出现系统报错，但实际上已经完成安装，忽略即可。

## 3.端口选择

将设备通过 USB-C 数据线连接至电脑。完成上述步骤后，可在 Arduino IDE 中选择对应的主控和设备端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/quickstart_arduino_fire_selectport.png" width="70%">

## 4.程序编译&烧录

打开`M5GFX`库中的示例程序`Basic -> BarGraph`，点击上传按钮，程序将编译并上传至 Fire。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/quickstart_arduino_fire_select_demo.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/quickstart_arduino_fire_select_demoupload.png" width="70%">

运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/Arduino_BarGragh.jpg" width="50%">

## 5.相关资源

- Arduino Library
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
- Arduino API & Examples
  - [Battery](/zh_CN/arduino/m5fire/battery)
  - [Button](/zh_CN/arduino/m5fire/button)
  - [Display](/zh_CN/arduino/m5fire/display)
  - [IMU](/zh_CN/arduino/m5fire/mpu6886)
  - [microSD](/zh_CN/arduino/m5fire/microsd)
  - [RGB LED](/zh_CN/arduino/m5fire/rgb)
  - [Speaker](/zh_CN/arduino/m5fire/speaker)
  - [Wakeup](/zh_CN/arduino/m5fire/wakeup)