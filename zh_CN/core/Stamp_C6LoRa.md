# Stamp C6LoRa

<span class="product-sku">SKU:S012</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_main_pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_main_pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_main_pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_main_pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_main_pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_main_pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_main_pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_main_pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_main_pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_main_pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012-weight.jpg">
</PictureViewer>

## 描述

**Stamp C6LoRa** 是一款适用于 850 ~ 960 MHz 的高性能可编程 LoRa 模组，采用 SMD 贴片封装，整体体积小巧紧凑，便于高密度嵌入式集成。模组核心由 ESP32-C6 SoC + SX1262 LoRa 射频芯片以及 LNA 信号放大芯片组成。板载两个 IPEX-4 天线座分别用于外接 Wi-Fi 与 LoRa 天线。LoRa 射频芯片最大发射功率可达 +22dBm , 灵敏度可达 - 148dBm。核心主控 ESP32-C6 芯片集成丰富外设接口资源，能支持二次开发更多拓展功能。同时支持 2.4GHz Wi-Fi 6 ，能够提供更多物联网应用可能。内部还集成了 PI4IOE5V6408 IO 拓展芯片，用于 LoRa 模组收发电路控制与信号放大器使能控制，提供更好的功耗控制表现，同时也提供更多可用 IO 资源。支持 DC 3.3 ~ 5V 供电输入，适配不同的硬件部署情况。适用于智能灌溉，远程抄表，电力设备控制等远距离通信场景。

## 产品特性

- ESP32-C6 核心主控
- 2.4 GHz Wi-Fi 6
- SX1262 LoRa 收发器
- LoRa 工作频率: 850 ~ 960 MHz
- 内置低噪声放大器（LNA），有效提升信号接收质量
- SMD 贴片封装，体积小巧，易于集成
- IPEX-4 天线座子

## 包装内容

- 1 x Stamp C6LoRa

## 应用场景

- 智慧农业
- 工业监测
- 户外通信

## 规格参数

| 规格                | 参数                                                                                                             |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| SoC                 | ESP32-C6 (RISC-V 32 位高性能单核处理器 160MHz + RISC-V 32 位低功耗单核处理器 20 MHz)                             |
| Flash               | 16MB                                                                                                             |
| Wi-Fi               | 2.4GHz Wi-Fi 6                                                                                                   |
| LoRa 芯片           | SX1262                                                                                                           |
| LoRa 工作频率       | 850 ~ 960 MHz                                                                                                    |
| LoRa 发射功率       | 最大发射功率: +22dBm / 最大灵敏度: -148dBm                                                                       |
| 天线座子规格        | IPEX-4                                                                                                           |
| 低噪声放大器（LNA） | SGM13005L4                                                                                                       |
| GPIO 引出           | 16x GPIO (G9/G11/G8/G10/G2/G7/G4/G5/G6/G15/G16/G17/G18/G20/G21/G22) + 5x EXT_IO 拓展 (PI4IOE5V6408: EXT_P0 ~ P4) |
| 工作电源            | 支持 DC 3.7 ~ 5V，通过 BAT 引脚输入供电 / DC 3.3V 通过 VDD_3V3 引脚输入供电                                      |
| 产品尺寸（SMD）     | 18.0 x 15.0 x 2.3mm                                                                                              |
| 产品重量            | 1.7g                                                                                                             |
| 包装尺寸            | 138.0 x 93.0 x 7.0mm                                                                                             |
| 包装重量            | 4.5g                                                                                                             |

## 操作说明

### 固件烧录

Stamp C6LoRa 支持通过 UART 或 USB 接口下载程序，下载前需要控制 Boot 引脚 (GPIO9) 保持低电平，然后复位模组使其进入下载模式。

- 通过 UART 方式下载需搭配 USB-TTL 转接板，下方接线示意图以 [ESP32 Downloader](https://shop.m5stack.com/products/esp32-downloader-kit) 转接板为例连接 Stamp C6LoRa 的 UART 程序下载接口。
- ESP32 Downloader 带自动下载电路，烧录程序运行时将自动控制模组进入下载模式。
- 通过 USB 方式下载，需控制 Boot 引脚保持低电平的状态，通过 RST 引脚复位模组 (低电平 -> 高电平)，进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/stamp_c6lora_download.png" width="90%" />

### 天线安装

Stamp C6LoRa 采用 IPEX‑4 规格天线连接器，LoRa 与 Wi‑Fi 天线接口位置如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/stamp_c6lora_antenna.png" width="60%" />

### 模组供电

Stamp C6LoRa 的 BAT 引脚支持 DC 3.7 ~ 5V 输入供电，**仅当通过 BAT 引脚供电时，需要拉高 MODULE_EN 引脚以完成供电使能**；若通过 VDD_3V3 引脚输入 DC 3.3V 供电，则无需操作 MODULE_EN 引脚。

## 原理图

- [Stamp C6LoRa 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012-SCH_Sch_M5_C6_Lora_v0.2.3_2025_12_02_19_14_35.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012-SCH_Sch_M5_C6_Lora_v0.2.3_2025_12_02_19_14_35_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012-SCH_Sch_M5_C6_Lora_v0.2.3_2025_12_02_19_14_35_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012-SCH_Sch_M5_C6_Lora_v0.2.3_2025_12_02_19_14_35_page_03.png">
</SchViewer>

## 管脚映射

### 引脚图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012-stamp-c6lora-pin-map-pic.png">

### Stamp C6LoRa

| ESP32-C6 | G21  | G22  | G20 | G23 | G19  | G7  |
| -------- | ---- | ---- | --- | --- | ---- | --- |
| SX1262   | MOSI | MISO | SCK | CS  | BUSY | IRQ |

| ESP32-C6     | G8  | G10 | G3  | ESP_RST |
| ------------ | --- | --- | --- | ------- |
| PI4IOE5V6408 | SCL | SDA | INT | RST     |

| PI4IOE5V6408 | E0.P5     | E0.P6     | E0.P7   |
| ------------ | --------- | --------- | ------- |
| SX1262       | SX_LNA_EN | SX_ANT_SW | SX_NRST |

LoRa 模组初始化需要执行以下操作：

- 复位 LoRa 模组：将 SX_NRST 设置为低电平，持续 100 ms 后重新置为高电平。
- 使能射频天线开关：将 SX_ANT_SW 设置为高电平
- 使能 LNA 芯片开关： 将 SX_LNA_EN 设置为高电平

## 尺寸图

- [Stamp C6LoRa 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_Stamp_C6LoRa_model_size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012_Stamp_C6LoRa_model_size_page_01.png" width="100%">

## PCB

- [Stamp C6LoRa PcbDoc](https://github.com/m5stack/M5_Hardware/tree/master/Products/S012_Stamp_C6LoRa/Footprint)
- [Stamp C6LoRa KiCad Footprint Library](https://github.com/m5stack/M5_Hardware/blob/master/KiCad/Footprints/M5Stack.pretty/Stamp_C6LoRa_SMD.kicad_mod)

## 结构文件

- [Stamp C6LoRa 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/S012_Stamp_C6LoRa/Structures)

## 软件开发

### Arduino

- [Stamp C6LoRa Arduino 快速上手](/zh_CN/arduino/m5stamp_c6lora/program)

### PlatformIO

```bash
[env:m5stack-stamp-c6lora]
platform = https://github.com/pioarduino/platform-espressif32.git#55.03.37
board = esp32-c6-devkitc-1
framework = arduino
upload_speed = 1500000
monitor_speed = 115200
build_flags =
    -D ARDUINO_USB_MODE=1
    -DARDUINO_USB_CDC_ON_BOOT=0
    ; -DCORE_DEBUG_LEVEL=5
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
	RadioLib=https://github.com/jgromes/RadioLib
```

## 相关视频

- Stamp C6LoRa 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012-Stamp-C6LoRa-intro-video_ZH.mp4" type="video/mp4"></video>
