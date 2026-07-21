# Tough Arduino 示例程序编译与烧录

## 1. 准备工作

- 1.Arduino IDE 安装：参考 [Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。

- 2\. 板管理安装：参考 [基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板 `M5Tough`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5tough/quickstart_arduino_tough_select_board.png" width="70%"/>

- 3\. 依赖库安装：参考 [库管理安装教程](/zh_CN/arduino/arduino_library)，完成最新版 `M5Unified`、`M5GFX` 驱动库安装，并根据提示安装全部依赖库。

\#> M5Unified 版本 >= `0.2.5`，M5GFX 版本 >= `0.2.7`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/Tough_Arduino_M5Unified.png" width="50%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/Tough_Arduino_M5GFX.png" width="50%"/>

## 2.USB 驱动安装

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

\#> 注意 | **CH9102_VCP_MacOS_v1.7** 在安装过程中可能出现系统报错，但实际上已经完成安装，忽略即可。

## 3. 端口选择

将设备通过 USB 线连接至电脑，如果 USB 驱动已正常安装，则可以在 Arduino IDE 中选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5tough/quickstart_arduino_tough_select_port.png" width="70%"/>

## 4. 程序编译 & 烧录

打开 `M5GFX` 驱动库中的案例程序 `BarGraph`，点击上传按钮，程序将开始编译与烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5papers3/bar_example_01.jpg" width="70%"/>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/Tough_Arduino_bargraph.jpeg" width="30%"/>

## 5. 相关资源

- **GitHub**

  - [M5Unified Library](https://github.com/m5stack/M5Unified)
  - [M5GFX Library](https://github.com/m5stack/M5GFX)

- **Arduino API & Examples**

  - [RTC](/zh_CN/arduino/m5tough/rtc)
  - [SD Card](/zh_CN/arduino/m5tough/sdcard)
  - [Speaker](/zh_CN/arduino/m5tough/speaker)
  - [Touch](/zh_CN/arduino/m5tough/touch)
  - [Wakeup](/zh_CN/arduino/m5tough/wakeup)

- **Deprecated Examples**
  - [M5Tough 库中的示例程序](https://github.com/m5stack/M5Tough/tree/master/examples) <br/>该库已停止更新，推荐使用上述的 M5Unified 与 M5GFX 库。旧库中的示例程序可参考 [迁移至 M5Unified](/zh_CN/arduino/m5unified/migration) 做相应的更改。
