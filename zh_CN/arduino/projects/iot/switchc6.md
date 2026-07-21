# SwitchC6 Arduino 使用教程

## 1.准备工作

- 环境配置：参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide) 完成 IDE 安装，并根据实际使用的开发板安装对应的板管理与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5SwitchC6-ESP-NOW](https://github.com/m5stack/M5SwitchC6-ESP-NOW)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/Arduino_library.png" width="70%">

- 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [SwitchC6](https://shop.m5stack.com/products/single-live-wire-wi-fi-smart-switch-esp32-c6)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/k140_switchc6_02.webp" width="20%">

## 2.案例程序

#> 编译要求 | M5Stack 板管理版本 >= 3.2.2<br>M5Unified 库版本 >= 0.2.7<br>M5GFX 库版本 >= 0.2.9<br>M5SwitchC6-ESP-NOW 库版本 >= 0.0.1

### 扫描广播

打开 M5SwitchC6-ESP-NOW 库自带的示例程序`Broadcast_Scan`，编译上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/Arduino_example.png" width="70%">

长按 SwitchC6 的按键 5 秒钟，它会向周围广播自身的状态信息，包括 MAC 地址、信道、开关状态、电容电压等。短按一次按键会先切换开关状态，然后广播状态信息。而运行该示例程序的主控设备会扫描读取此广播，将格式化的信息打印到串口（主控屏幕上不显示内容），如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/Broadcast_Scan.png" width="90%">

### 控制开关

首先从 SwitchC6 的贴纸或广播信息中获得 MAC 地址。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/MAC_Address.png" width="60%">

打开 M5SwitchC6-ESP-NOW 库自带的示例程序`Controller`，将所要控制的 SwitchC6 的 MAC 地址（格式为`XXXX-XXXX-XXXX`）、主机要连接的 Wi-Fi 名称和密码填入程序中，编译上传。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/Arduino_example.png" width="70%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/Controller.png" width="90%">

点击主控屏幕上的左侧按钮开启开关，中间按钮关闭开关，右侧按钮查询开关状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/Controller_CoreS3.jpeg" width="50%">

## 3.API

- [SwitchC6 ESP-NOW 控制协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1159/SwitchC6-ESP-NOW-Protocol-CN.pdf)
- [M5SwitchC6-ESP-NOW - GitHub](https://github.com/m5stack/M5SwitchC6-ESP-NOW)
- [ESP-NOW Espressif Doc](https://docs.espressif.com/projects/esp-idf/zh_CN/v5.5/esp32s3/api-reference/network/esp_now.html)