# Atom-Lite

<span class="product-sku">SKU:C008</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Lite/img-b87e8051-87c6-41d7-a710-eb27f62eb785.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Lite/img-57446929-03e0-45dd-8263-ce96023a73ee.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Lite/img-7554f11c-8ba5-4201-b98d-fca8db536d0b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Lite/img-d066cf3f-63a8-4866-bed2-2c2a6d9c034e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Lite/img-e5d5d67b-4f0f-4815-9cda-64c198c516c3.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/C008.webp">
</PictureViewer>

## 描述

**Atom-Lite** 是 M5Stack 开发套件系列中一款非常小巧的开发板，其大小 **只有 24.0 x 24.0 mm** ，提供更多 GPIO 供用户自定义，非常适合做嵌入式的智能硬件开发。主控采用了 **ESP32-PICO-D4** 方案，集成 **Wi-Fi** 模块，内置 3D 天线，拥有 **4 MB** 的 SPI 闪存，提供 Infra-Red 、RGB Led 、按键和 GROVE/HY2.0 接口。板载 USB Type-C 接口可以快速实现程序上传下载，背面提供一个 M2 螺丝孔用于固定。

## 教程 & 快速上手

learn>| ![UiFlow1](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow/uiflow1.0_banner_01.png) | [UiFlow1](/zh_CN/uiflow/m5atom_lite/program) | 本教程将向你介绍，如何通过 UiFlow1 图形化编程平台控制 Atom-Lite 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/atomlite/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Atom-Lite 设备。 |

## 产品特性

- 基于 ESP32 开发
- 机身小巧
- 内置红外发射功能
- 带有可编程按键
- RGB LED 指示灯
- 可扩展的引脚与接口
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Atom-Lite

## 应用场景

- 物联网节点
- 微型控制器
- 可穿戴设备

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
| RGB LED  | SK6812 3535 x 1                          |
| IR       | IR 发射管                                |
| 按键     | 自定义按键 x 1                           |
| 天线     | 2.4G 3D 天线                             |
| 工作温度 | 0 ~ 40°C                                 |
| 外壳材质 | Plastic ( PC ) + ABS                     |
| 产品尺寸 | 24.0 x 24.0 x 9.5mm                      |
| 产品重量 | 5.5g                                     |
| 包装尺寸 | 81.0 x 65.0 x 13.0mm                     |
| 毛重     | 10.9g                                    |

## 原理图

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM Lite/img-2e58eac3-d9ef-4be4-b486-d4dd9a8324fa.webp">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/673/C008_PinMap_01.jpg" width="100%" >

### RGB & Button & IR & I2C

| ESP32-PICO-D4 | G27 | G39    | G12 | G21 | G25 |
| ------------- | --- | ------ | --- | --- | --- |
| RGB           | RGB |        |     |     |     |
| Button        |     | Button |     |     |     |
| IR            |     |        | IR  |     |     |
| I2C           |     |        |     | SCL | SDA |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G26    | G32   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/ATOM%20Lite/model%20size.jpg" width="80%">

## 结构文件

- [ATOM Lite 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C008_Atom-Lite/Structures)

## 数据手册

- [ESP32-PICO](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/669/esp32-pico_series_datasheet_cn.pdf)

## 软件开发

### Arduino

- [Atom Arduino 驱动库](https://github.com/m5stack/M5Atom)

### UiFlow1

- [Atom-Lite UiFlow1 快速上手](/zh_CN/uiflow/m5atom_lite/program)
- [Atom-Lite 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Core/Atom/Atom%20Lite)

### UiFlow2

- [Atom-Lite UiFlow2 快速上手](/zh_CN/uiflow2/atomlite/program)
- [Atom-Lite 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Core/Atom/Atom%20Lite)

### Home Assistant

- [Home Assistant 集成](/zh_CN/homeassistant/light/atom_lite_light)

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

> Atom-Lite 在部分系统中，可能无法免驱工作，用户可以通过手动安装 FTDI VCP 驱动修复该问题。以 win10 环境为例，下载匹配操作系统的驱动文件，并解压，通过设备管理器进行安装。(注：某些系统环境下，需要安装两次，驱动才会生效，未识别的设备名通常为**M5Stack**或**USB Serial**，Windows 推荐使用驱动文件在设备管理器直接进行安装 (自定义更新)，可执行文件安装方式可能无法正常工作)。

[FTDI VCP 驱动下载页面：](https://ftdichip.com/drivers/vcp-drivers/)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-02.png" width="100%">

**安装方法：**

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/U082-X-USB-note-01.png" width="100%">

### Easyloader

| Easyloader                        | 下载链接                                                                                                                      | 备注 |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---- |
| Atom-Lite Factory Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/ATOM%20Lite/Atom%20Lite%20RGB%20Demo.exe) | /    |

## 相关视频

通过变色呼吸灯程序，测试 RGB LED 与按键是否工作正常

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/ATOM_LITE.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1005907310&bvid=BV1Ux4y1474R&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/uPXMTFF-D8A?si=LauhF-lJ77Yf03eB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

如需对比 Atom 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5atom_compare?select=C008)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
