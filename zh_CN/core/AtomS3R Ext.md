# AtomS3R-Ext

<span class="product-sku">SKU:C126-Ext</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Ext/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Ext/13.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Ext/16.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Ext/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Ext/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Ext/14.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Ext/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Ext/12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/682/C126-Ext-weight.jpg">
</PictureViewer>

## 描述

**AtomS3R-Ext** 是一款基于 ESP32-S3 主控的 **原型开发扩展** 可编程控制器，专为原型验证和扩展开发设计。其顶部配备了 **万能扩展板**，方便用户引出多个 **IO** 口进行连接和调试，适合各种外设模块的扩展和功能验证。内部集成了 **ESP32-S3-PICO-1-N8R8** 主控，支持 Wi-Fi 功能，带有 8MB 片上 **Flash** 和 8MB **PSRAM**，并配有 5V 转 **3.3V/2.8V/1.2V** 的电源电路。内置三轴 **BMM150** 地磁传感器和六轴 **BMI270** 姿态传感器。控制器配备 **USB Type-C** 接口用于供电和固件下载，并具有 **HY2.0-4P** 扩展端口，六个 **GPIO** 和电源引脚，方便功能扩展。相比之前的 ATOM 系列主机产品，**AtomS3R-Ext** 的 **3D 天线** 经过增强，提供了更好的信号性能和稳定性。尺寸仅为 **24.0 x 24.0 x 12.0mm** ，非常适合嵌入式智能设备的原型开发和验证应用场景。

## 产品特性

- 集成 ESP32-S3-PICO-1-N8R8 主控
- 九轴传感器系统 (BMI270 六轴 + BMM150 三轴地磁传感器)
- 8MB Flash 和 8MB PSRAM
- 支持红外发射控制功能
- 可扩展的引脚与接口
- 洞洞板
- 开发平台
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x AtomS3R-Ext

## 应用场景

- 运动检测方向感知
- 智能设备控制
- 物联网应用

## 规格参数

| 规格                      | 参数                                                                                                            |
| ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| SoC                       | ESP32-S3-PICO-1-N8R8@双核 Xtensa LX7 处理器，主频高达 240MHz                                                    |
| USB                       | USB OTG, USB Serial/JTAG                                                                                        |
| Flash                     | 8MB                                                                                                             |
| PSRAM                     | 8MB Octal                                                                                                       |
| Wi-Fi                     | 2.4 GHz Wi-Fi                                                                                                   |
| 六轴姿态传感器 (BMI270)   | 精度：0.05% (加速度)，0.05°/s (角速度) <br/>I2C 地址：0x68                                                      |
| 三轴地磁式传感器 (BMM150) | 精度：0.3 μT <br/>挂载在 BMI270 上，通过 BMI270 获取磁力计数据                                                  |
| 红外 IR                   | ∠180° 时红外线发射距离：12.46m (无遮挡情况下)                                                                   |
| 休眠电流                  | GPIO-5V 供电：DC 5V@11.63 uA<br/>Grove-5V 供电：DC 5V@10.75 uA<br/>USB-5V 供电：DC 5V@92.50 uA (含 PD 电阻损耗) |
| 万能扩展板规格            | 5 x 6@2.54mm                                                                                                    |
| 底部预留 GPIO             | G5/G6/G7/G8/G38/G39                                                                                             |
| 洞洞板预留 GPIO           | G3/G4/G9/G10/G11/G12/G13/G14/G17/G21/G40/G42/G46/G48                                                            |
| 工作温度                  | 0 ~ 40°C                                                                                                        |
| 产品尺寸                  | 24.0 x 24.0 x 12.0mm                                                                                            |
| 产品重量                  | 7.0g                                                                                                            |
| 包装尺寸                  | 85.0 x 65.0 x 15.2mm                                                                                            |
| 毛重                      | 13.6g                                                                                                           |

## 操作说明

\#>Proto Board | 顶部 Proto Board 通过 FPC 排线连接至底座主控，其中丝印标注部分连接了主控对应引脚，5x6@2.54mm 部分为自定焊接区域，无线路连接。

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 进入下载模式

如需烧录固件，请长按复位按键（大约 2 秒）直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Ext/download%20mode.gif" width="30%" />

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/682/IMU-AtomS3R-Ext.jpg" width="70%">

## 原理图

- [AtomS3R-Ext main board 原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/main_board_schematic.pdf)
- [AtomS3R-Ext ext board 原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/ext_board_schematic.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/main_board_schematic_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/ext_board_schematic_page_01.png">
</SchViewer>

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/682/C126-Ext_PinMap_01.jpg" width="100%" />

### BMI270 & IR & BUTTON

| ESP32-S3-PICO-1-N8R8 | G0      | G45     | G47        | G41      |
| -------------------- | ------- | ------- | ---------- | -------- |
| BMI270               | SYS_SCL | SYS_SDA |            |          |
| IR                   |         |         | IR_LED_DRV |          |
| BUTTON               |         |         |            | USER_BUT |

### BMM150

| BMI270 | BMI270_ASDx | BMI270_ASCx |
| ------ | ----------- | ----------- |
| BMM150 | A_SDA       | A_SCL       |

\#> BMM150 挂载于 BMI270 | 通过 BMI270 的 Sensor Hub 辅助 I2C 接口接入 BMM150，实现统一的 9 轴传感数据采集。

### Proto Pin

| Proto Board | ESP32-S3-PICO-1-N8R8 |
| ----------- | -------------------- |
| 1           | 3.3V                 |
| 2           | 1.2V                 |
| 3           | 2.8V                 |
| 4           | RST                  |
| 5           | G3                   |
| 6           | G4                   |
| 7           | G9                   |
| 8           | G10                  |
| 9           | G11                  |
| 10          | G12                  |
| 11          | G13                  |
| 12          | G17                  |
| 13          | G21                  |
| 14          | G40                  |
| 15          | G42                  |
| 16          | G46                  |
| 17          | G48                  |
| 18          | GND                  |
| 19          | GND                  |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G2     | G1    |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Ext/%E5%B0%BA%E5%AF%B8%E5%9B%BE.png" width="100%" />

## PCB

- [AtomS3R-Ext PcbDoc](https://github.com/m5stack/M5_Hardware/tree/master/Products/C126-Ext_AtomS3R-Ext/Footprints)

## 结构文件

- [AtomS3R-Ext 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C126-Ext_AtomS3R-Ext/Structures)

## 数据手册

- [ESP32-S3-PICO-1-N8R8](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/esp32-s3-pico-1_datasheet_en.pdf)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMM150.PDF)

## 软件开发

### Arduino

- [AtomS3R-Ext Arduino 驱动库](https://github.com/m5stack/M5AtomS3)

### PlatformIO

```bash
[env:m5stack-atoms3r]
platform = espressif32@6.7.0
board = esp32-s3-devkitc-1
framework = arduino
board_build.arduino.memory_type = qio_opi
build_flags =
    -DESP32S3
    -DBOARD_HAS_PSRAM
    -mfix-esp32-psram-cache-issue
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
	-DARDUINO_USB_MODE=1
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

## 相关视频

- AtomS3R-Ext 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R%20Ext/AtomS3R-Ext-VIDEO.mp4" type="video/mp4"></video>

## 产品对比

如需对比 Atom 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5atom_compare?select=C126-Ext)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
