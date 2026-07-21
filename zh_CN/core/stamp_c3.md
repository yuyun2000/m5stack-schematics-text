# Stamp-C3

<span class="product-sku">SKU:C056-B</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/C056-B_01.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/C056-B_02.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/C056-B_03.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/C056-B_04.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/C056-B_05.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/C056-B_06.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/C056-B_07.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/C056-B_08.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/C056-B_09.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/523/K056_and_C056-B_weight.jpg">
</PictureViewer>

## 描述

**Stamp-C3** 是一款具有高性价比的 RISC-V 最小核心板。采用乐鑫 **ESP32-C3** 主控芯片，内置 **RISC-V** 32 bit 单核处理器，时钟频率可高达 160 MHz 。其内置 400 KB SRAM + 4MB FLASH ，并且集成了 2.4 GHz Wi-Fi 。该核心板支持安全启动、Flash 加密、数字签名等安全机制。其体积小巧，但功能却十分强大，能够满足多样化的物联网应用需求。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5stampc3/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Stamp-C3 设备。 |

## 产品特性

- 支持多种应用形态（SMT，DIP，飞线）
- 配有高温塑料铠装，支持 SMT 过炉温度 (230°C)
- 内含 5V->3.3V DC/DC 电路，GPIOx13
- Type-C 接口
- 可编程 RGB 灯 x1，复位按钮 x1，按键 x1
- 高性能 3D 天线，提供稳定可靠的无线通信质量
- ESP32 最小系统板
- 开发平台
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 5 x Stamp-C3
- 5 x 耐高温贴纸

## 应用场景

- DIY 原型制作
- 工业自动化
- 智能家居

## 规格参数

| 规格             | 参数                                                               |
| ---------------- | ------------------------------------------------------------------ |
| SoC              | ESP32-C3@32 位 RISC-V 单核处理器，主频高达 160MHz                  |
| Flash            | 4MB                                                                |
| SRAM             | 400KB                                                              |
| ROM              | 384KB                                                              |
| RTC SRAM         | 8KB                                                                |
| Wi-Fi            | 2.4 GHz Wi-Fi (支持 20/40MHz 频宽，802.11 b/g/n, 速率高达 150Mbps) |
| 输入电压         | 5V@500mA                                                           |
| 人机交互         | 可编程物理按键 x 1，复位调试按键 x 1，可编程 RGB LED (SK6812) x 1  |
| USB 接口         | USB Type-C x1                                                      |
| 天线类型         | 2.4G 3D 天线                                                       |
| 模组外设接口资源 | ADC、GPIO、SPI、UART、I2C、I2S、PWM、RMT、DMA、USB 串口、TWAI      |
| IO 接口 x13      | G21，G20，G9，G18，G19，G1，G0，G10，G8，G7，G6，G5，G4            |
| IO 接口间距      | 2.54mm                                                             |
| 固定螺丝规格     | M2 x 4 沉头内六角机械牙                                            |
| 产品尺寸         | 34.0 x 20.0 x 4.6mm                                                |
| 单个产品重量     | 4.1g                                                               |
| 包装尺寸         | 138.0 x 93.0 x 5.6mm                                               |
| 毛重             | 23.3g                                                              |

## 操作说明

### 外壳支持回流焊温度曲线

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/stamp_pico/stamp_pico_11_cn.webp">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/stamp_c3/stamp_c3_sch_01.webp" width="80%">

## 管脚映射

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/524/C056-B_PinMap_01.jpg" width="100%">

### SK6812，Button

| ESP32-C3 | G2  | G3  |
| -------- | --- | --- |
| SK6812   | DI  | /   |
| Button   | /   | SW  |

## 尺寸图

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/stamp_c3u/stamp_c3&c3u_size_01.webp" width="100%">

## 结构文件

- [Stamp-C3 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C056-B_Stamp-C3/Structures)

## PCB

- [Stamp-C3 KiCad 封装库](https://github.com/m5stack/M5_Hardware/blob/master/KiCad/Footprints/M5Stack.pretty/Stamp-C3.kicad_mod)
- [Stamp-C3 PcbDoc](https://github.com/m5stack/M5_Hardware/tree/master/Products/C056-B_Stamp-C3/Footprint)

## 数据手册

- [ESP32-C3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/525/esp32-c3_datasheet_cn.pdf)

## 软件开发

### Arduino

- [Stamp-C3 Arduino 快速上手](/zh_CN/arduino/m5stampc3/program)
- [Stamp-C3 测试程序](https://github.com/m5stack/STAMP-C3/tree/master/Arduino)

### ESP-IDF

- [Stamp-C3 RGB LED Control 使用示例](https://github.com/m5stack/STAMP-C3/tree/master/idf/RGB_LED_Control)

### USB 驱动

点击下方连接下载匹配操作系统的驱动程序。目选择对应操作系统位数的安装包进行安装。(若您不确定您的设备所使用的 USB 芯片，可同时安装两种驱动。**CH9102_VCP_SER_MacOS v1.7**在安装过程中，可能出现报错，但实际上已经完成安装，忽略即可。) 在使用时，若出现无法正常下载程序（提示超时或者是 Failed to write to target RAM）的情况，可尝试重新安装设备驱动。

| 驱动名称                  | 适用驱动芯片 | 下载链接                                                                                             |
| ------------------------- | ------------ | ---------------------------------------------------------------------------------------------------- |
| CH9102_VCP_SER_Windows    | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_SER_Windows.exe) |
| CH9102_VCP_SER_MacOS v1.7 | CH9102       | [Download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/drivers/CH9102_VCP_MacOS_v1.7.zip)  |

## 产品对比

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/stamp/对比.png" width="80%">

如需对比 Stamp 系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5stamp_compare?select=C056-B)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
