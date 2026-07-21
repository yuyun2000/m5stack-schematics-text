# Station Arduino 示例程序编译与烧录

## 1. 准备工作

- 1.Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2\. 板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板 `M5Station`。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/520/quickstart_arduino_station_select_board.png" width="70%" />

- 3\. 依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成 `M5Unified` ， `M5GFX` 驱动库安装，并根据提示安装全部依赖库。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/520/station_arduino_lib_01.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/520/station_arduino_lib_02.png" width="70%" />

## 2.USB 驱动安装

\#> 驱动程序安装提示 | 点击下方连接下载匹配操作系统的驱动程序。目前存在两种驱动芯片版本，CP210X (适用于`CP2104`版本)/CP34X (适用于`CH9102`版本) 驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。`CH9102_VCP_SER_MacOS v1.7`在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。)

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CP210x_VCP_Windows        | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Windows.zip)     |
| CP210x_VCP_MacOS          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_MacOS.zip)       |
| CP210x_VCP_Linux          | CP2104       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CP210x_VCP_Linux.zip)       |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

## 3. 端口选择

将设备通过 USB 线连接至电脑，在完成驱动安装后， Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/520/quickstart_arduino_station_selectport.png" width="70%" />

## 4. 程序编译 & 烧录

打开 M5GFX 驱动库中的案例程序 "Button", 点击上传按钮，将自动进行程序编译与烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/520/quickstart_arduino_station_select_demo.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/520/quickstart_arduino_station_select_demoupload.png" width="70%">

按动按键，按键所对应的区域将发生颜色变化，按键位置如下图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/520/station_arduino_example.jpg" width="50%" />

## 5. 相关资源

- **Arduino Library**

  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- **Arduino API & Examples**
  - [Battery](/zh_CN/arduino/m5station/battery)
  - [Button](/zh_CN/arduino/m5station/button)
  - [Display](/zh_CN/arduino/m5station/display)
  - [Grove Power](/zh_CN/arduino/m5station/power)
  - [IMU](/zh_CN/arduino/m5station/imu)
  - [RGB LED](/zh_CN/arduino/m5station/rgb)
  - [RTC](/zh_CN/arduino/m5station/rtc)
  - [Wakeup](/zh_CN/arduino/m5station/wakeup)
