# Atom-Matrix

<span class="product-sku">SKU:C008-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Matrix/img-bc9c8013-4f56-43ff-9dc5-0f6b8558790c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Matrix/img-00b551c1-39bd-4ff5-bf92-9488afb74efc.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/674/C008-B-weight.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Matrix/img-50177ce7-b140-44cd-a8e4-5df73b0054cf.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Matrix/img-6140cbe8-b833-446e-aebf-4e1cb3545f69.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Matrix/img-695ed4da-4ff3-4a46-bc09-a4afab9fded1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Matrix/img-78bfc578-d6af-469d-a150-9729f30af98b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Matrix/img-ae3786cd-7586-44db-bfff-cd2cb2159a9b.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/674/C008-B_Weight.jpg">
</PictureViewer>

## 描述

**Atom-Matrix** 是 M5Stack 开发套件系列中一款非常小巧的开发板，其大小**只有 24.0 x 24.0 mm**，提供更多 GPIO 供用户自定义，非常适合做嵌入式的智能硬件。主控采用**ESP32-PICO-D4** 方案，集成 **Wi-Fi** 模块，拥有 **4 MB** 的 SPI 闪存。板载 IR (红外发射管)，面板上有 5\*5 RGB Led 矩阵、内置 IMU 姿态传感器 (MPU6886)，在 Neo Led 矩阵下方隐藏一颗可编程按键。板载 USB Type-C 接口可以快速实现程序上传下载，此外还提供一个 HY2.0-4P 接口用于连接外设。背面具有一个 M2 螺丝孔用于固定。

## 注意事顶

在使用 FastLED lib 时 RGB LED 的建议亮度值为 20，请不要将其设置过高的亮度数值，以免损坏 LED 和亚克力屏幕。(在 Atom-Matrix lib 中，我们已将其合适的亮度范围映射为 0~100)，**亮度不能太高不能全亮，会产生高温导致外壳损坏**。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5atom/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Atom-Matrix 设备。 |

learn>| ![UiFlow1](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow1](/zh_CN/uiflow/m5atom_matrix/program) | 本教程将向你介绍，如何通过 UiFlow1 图形化编程平台控制 Atom-Matrix 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/atommatrix/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Atom-Matrix 设备。 |

## 产品特性

- 基于 ESP32 开发
- 机身小巧
- 内置 3 轴陀螺仪和 3 轴加速计 (I2CAddress:0x68)
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

- 1x Atom-Matrix

## 应用场景

- 物联网节点
- 微型控制器

## 规格参数

| 规格     | 参数                                     |
| -------- | ---------------------------------------- |
| SoC      | ESP32-PICO-D4@双核处理器，主频 240MHz    |
| DMIPS    | 600                                      |
| SRAM     | 520KB                                    |
| Flash    | 4MB                                      |
| Wi-Fi    | 2.4 GHz Wi-Fi                            |
| 输入电压 | 5V@500mA                                 |
| 主机接口 | USB Type-C x 1，GROVE (I2C+I/O+UART) x 1 |
| PIN 接口 | G19，G21，G22，G23，G25，G33             |
| RGB LED  | WS2812C 2020 x 25                        |
| MEMS     | MPU6886 (I2CAddress: 0x68)               |
| IR       | Infrared transmission                    |
| 按键     | 自定义按键 x 1                           |
| 天线     | 2.4G 3D 天线                             |
| 工作温度 | 0 ~ 60°C                                 |
| 外壳材质 | Plastic ( PC )                           |
| 产品尺寸 | 24.0 x 24.0 x 13.8mm                     |
| 产品重量 | 7.3g                                     |
| 包装尺寸 | 85.0 x 66.0 x 15.0mm                     |
| 毛重     | 12.6g                                    |

## 操作说明

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/674/IMU-Atom-Matrix.jpg" width="70%">

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Matrix/img-fa9922b3-727d-4598-8d16-84611248a3c6.webp" width="100%" />

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/674/C008-B_PinMap_01.jpg" width="100%">

### RGB & BUTTON & IR & MPU6886

| ESP32-PICO-D4  | G27 | G39    | G12   | G21 | G25 |
| -------------- | --- | ------ | ----- | --- | --- |
| RGB Led        | RGB |        |       |     |     |
| Btn            |     | Button |       |     |     |
| IR             |     |        | IR_TX |     |     |
| MPU6886 (0x68) |     |        |       | SCL | SDA |

### Grove

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G26    | G32   |
::

## 尺寸图

- [Atom-Matrix 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/c008b-model-size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1228/c008b-model-size_page_01.png" width="100%">

## 结构文件

- [Atom-Matrix 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C008-B_Atom-Matrix/Structures)

## 数据手册

- [ESP32-PICO](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/esp32-pico_series_datasheet_cn.pdf)
- [MPU6886](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf)
- [WS2812C-2020](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/WS2812C-2020_V1.2.pdf)

## 软件开发

### Arduino

- [Atom-Matrix Arduino 快速上手](/zh_CN/arduino/m5atom/program)
- [Atom-Matrix Arduino 驱动库](https://github.com/m5stack/M5Atom)
- [Atom-Matrix 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Core/Atom/Atom%20Matrix)

### UiFlow1

- [Atom-Matrix UiFlow1 快速上手](/zh_CN/uiflow/m5atom_matrix/program)

### UiFlow2

- [Atom-Matrix UiFlow2 快速上手](/zh_CN/uiflow2/atommatrix/program)

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

> Atom-Matrix 在部分系统中，可能无法免驱工作，用户可以通过手动安装 FTDI VCP 驱动修复该问题。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为**M5Stack**或**USB Serial**，Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新)，可执行文件安装方式可能无法正常工作)。

[FTDI VCP 驱动下载页面：](https://ftdichip.com/drivers/vcp-drivers/)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-02.png" width="100%">

**安装方法：**

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-01.png" width="100%">

### Easyloader

| Easyloader                          | 下载链接                                                                                                                               | 备注 |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atom-Matrix Factory Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/core/ATOM%20Matrix/ezLoader-3a928963-8187-43f9-bf6a-330ea2aa0949.exe) | /    |

## 相关视频

- Atom-Matrix 示例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/ATOM_MATRIX.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1305946230&bvid=BV1gM4m1U7a6&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/0ueXzELY5Rc?si=A9k-IlMVrbo2xG61" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

如需对比 Atom 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5atom_compare?select=C008-B)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
