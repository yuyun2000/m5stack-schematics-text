# Atom-Matrix v1.1

<span class="product-sku">SKU:C008-B-V11</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-weight.jpg">
</PictureViewer>

## 描述

**Atom-Matrix v1.1** 是 Atom-Matrix 的迭代升级版本，该产品将前代搭载的 MPU6886 替换为 BMI270 六轴 IMU 姿态传感器，有效提升姿态检测精度与响应速度，更适配运动捕捉、姿态控制等高精度应用场景。
主控采用 ESP32-PICO-D4 方案，集成 Wi-Fi 通信功能，板载 4 MB SPI 闪存；同时配备红外发射管与 5×5 RGB LED 矩阵屏，LED 矩阵下方设有一颗可编程按键，支持自定义触发逻辑，可便捷实现红外遥控、可视化交互与指令触发等功能。本产品适用于需要高精度姿态检测、红外遥控及可视化交互反馈的嵌入式开发与原型设计场景。

## 注意事顶

在使用 RGB LED 时建议调节到适中亮度，请不要设置过高的亮度数值，以免损坏 LED 和亚克力屏幕。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5atom/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Atom-Matrix v1.1 设备。 |

learn>| ![UiFlow1](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow1](/zh_CN/uiflow/m5atom_matrix/program) | 本教程将向你介绍，如何通过 UiFlow1 图形化编程平台控制 Atom-Matrix v1.1 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/atommatrix/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Atom-Matrix v1.1 设备。 |

## 产品特性

- 基于 ESP32 开发
- 机身小巧
- 内置 3 轴陀螺仪和 3 轴加速计 (I2C Address:0x68)
- 可编程按键
- RGB LED 点阵屏
- 红外发射功能
- 可扩展的引脚与接口
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Atom-Matrix v1.1

## 应用场景

- 体感遥控器
- 运动捕捉 / 姿态分析
- 智能家居中控节点

## 规格参数

| 规格     | 参数                                     |
| -------- | ---------------------------------------- |
| SoC      | ESP32-PICO-D4@双核处理器，主频 240MHz    |
| DMIPS    | 600                                      |
| SRAM     | 520KB                                    |
| Flash    | 4MB                                      |
| Wi-Fi    | 2.4 GHz Wi-Fi                            |
| 输入电压 | 5V @ 500mA                               |
| 主机接口 | USB Type-C x 1，Grove (I2C+I/O+UART) x 1 |
| RGB 灯珠 | 25 颗 WS2812C-2020                       |
| MEMS     | BMI270 (I2C Address: 0x68)               |
| 红外功能 | 支持红外发射                             |
| 按键     | 自定义按键 x 1                           |
| 天线     | 2.4G 3D 天线                             |
| 工作温度 | 0 ~ 60°C                                 |
| 整机功耗 | 5V @ 61.65mA                             |
| 产品尺寸 | 24.0 x 24.0 x 13.9mm                     |
| 产品重量 | 7.3g                                     |
| 包装尺寸 | 85.0 x 66.0 x 15.0mm                     |
| 毛重     | 13.5g                                    |

## 操作说明

### RGB LED 矩阵灯序示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/Light-num.jpg" width="30%">

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/IMU-Atom-Matrix-v1.1.jpg" width="70%">

## 原理图

- [Atom-Matrix v1.1 灯板原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/SCH_ATOM_KEYPAD_V1.2_20251211_2025_12_13_11_18_14.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/SCH_Atom_Matrix_V1_1.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/SCH_ATOM_KEYPAD_V1.2_20251211_2025_12_13_11_18_14_page_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11_PinMap.jpg" width="100%">

### RGB & BUTTON & IR & BMI270

| ESP32-PICO-D4 | G27  | G39    | G12   | G21 | G25 |
| ------------- | ---- | ------ | ----- | --- | --- |
| RGB Led       | Data |        |       |     |     |
| Btn           |      | Button |       |     |     |
| IR            |      |        | IR_TX |     |     |
| BMI270 (0x68) |      |        |       | SCL | SDA |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G26    | G32   |
::

## 尺寸图

- [Atom-Matrix v1.1 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/c008b-model-size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/c008b-model-size_page_01.png" width="100%">

## 结构文件

- [Atom-Matrix v1.1 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C008-B-V11_Atom-Matrix_v1.1/Structures)

## 数据手册

- [ESP32-PICO](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/esp32-pico_series_datasheet_cn.pdf)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [WS2812C-2020](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/WS2812C-2020_V1.2.pdf)

## 软件开发

### Arduino

- [Atom-Matrix v1.1 Arduino 快速上手](/zh_CN/arduino/m5atom/program)

### UiFlow1

- [Atom-Matrix v1.1 UiFlow1 快速上手](/zh_CN/uiflow/m5atom_matrix/program)

### UiFlow2

- [Atom-Matrix v1.1 UiFlow2 快速上手](/zh_CN/uiflow2/atommatrix/program)

### PlatformIO

```bash
[env:m5stack-atom]
platform = espressif32@6.7.0
board = m5stack-atom
framework = arduino
upload_speed = 1500000
monitor_speed = 115200
build_flags =
    -DCORE_DEBUG_LEVEL=5
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### USB 驱动

> Atom-Matrix v1.1 在部分系统中，可能无法免驱工作，用户可以通过手动安装 FTDI VCP 驱动修复该问题，请下载匹配操作系统的驱动文件并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为**M5Stack**或**USB Serial**，Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新)，可执行文件安装方式可能无法正常工作)。

[FTDI VCP 驱动下载页面：](https://ftdichip.com/drivers/vcp-drivers/)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/VCP_Drivers.png" width="80%">

**安装方法：**

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-01.png" width="100%">

## 相关视频

- Atom-Matrix v1.1 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-video-ZH.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比表          | [Atom-Matrix v1.1](/zh_CN/core/Atom-Matrix_v1.1) ![Atom-Matrix v1.1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/C008-B-V11-Atom-Matrix-v1.1-main-pictures_02.webp) | [Atom-Matrix](/zh_CN/core/ATOM%20Matrix) ![Atom-Matrix](https://static-cdn.m5stack.com/resource/docs/products/core/ATOM%20Matrix/img-c3488647-a432-47c1-8990-a873a8e62804.webp) |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 6 轴 IMU 姿态传感器 | BMI270                                                                                                                                                                        | MPU6886                                                                                                                                                                         |
::

如需对比 Atom 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5atom_compare)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
