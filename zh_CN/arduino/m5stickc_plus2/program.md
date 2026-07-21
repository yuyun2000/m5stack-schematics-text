# StickC-Plus2 Arduino 示例程序编译与烧录

## 1. 准备工作

- 1.Arduino IDE 安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成 IDE 安装。
- 2\. 板管理安装：参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成 M5Stack 板管理安装并选择开发板`M5StickCPlus2`。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5stickc_plus2/quickstart_arduino_stickcplus2_select_board.png" width="70%" />

- 3\. 依赖库安装： 参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成`M5StickCPlus2`驱动库安装，并根据提示下载全部依赖库。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5stickc_plus2/quickstart_arduino_stickcplus2_download_library.png" width="70%" />

## 2.USB 驱动安装

\#> 驱动程序安装提示 | 点击下方连接下载匹配操作系统的驱动程序。CP34X (适用于`CH9102`) 驱动程序压缩包。在解压压缩包后，选择对应操作系统位数的安装包进行安装。 在使用时，若出现无法正常下载程序 (提示超时或者是 Failed to write to target RAM) 的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

## 3. 端口选择

将设备通过 USB 线连接至电脑，在完成驱动安装后， Arduino IDE 中可选中对应设备的端口。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5stickc_plus2/quickstart_arduino_stickcplus2_select_port.png" width="70%" />

## 4. 程序编译 & 烧录

打开驱动库中的案例程序 “display”, 点击上传按钮，将自动进行程序编译，与程序烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5stickc_plus2/quickstart_arduino_stickcplus2_select_demo.png" width="70%" />

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/m5stickc_plus2/quickstart_arduino_stickcplus2_select_demoupload.png" width="70%">

效果如下图：

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5StickC%20PLUS2/download%20demo.gif" width="30%" />

## 5. 相关资源

- **Github**

  - [M5StickCPlus2 Library](https://github.com/m5stack/M5StickCPlus2)

- **Arduino API & Examples**
  - [Battery](/zh_CN/arduino/m5stickc_plus2/battery)
  - [Button](/zh_CN/arduino/m5stickc_plus2/button)
  - [Buzzer](/zh_CN/arduino/m5stickc_plus2/buzzer)
  - [Display](/zh_CN/arduino/m5stickc_plus2/display)
  - [IMU](/zh_CN/arduino/m5stickc_plus2/imu)
  - [IR NEC](/zh_CN/arduino/m5stickc_plus2/ir_nec)
  - [LED](/zh_CN/arduino/m5stickc_plus2/led)
  - [Mic](/zh_CN/arduino/m5stickc_plus2/mic)
  - [RTC](/zh_CN/arduino/m5stickc_plus2/rtc)
  - [Wakeup](/zh_CN/arduino/m5stickc_plus2/wakeup)
