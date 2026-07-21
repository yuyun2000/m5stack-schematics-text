# Module LoRaWAN-EU868

<span class="product-sku">SKU:M148</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_14.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-weight.jpg">
</PictureViewer>

## 描述

Module LoRaWAN-EU868 是一款基于 LoRa 调制技术的远距离低功耗无线通信模块，面向长距离、低功耗物联网应用场景。模块采用 RAK3172-8-SM-I（内置 STM32WLE5）核心方案，具备远距离传输、低功耗、高接收灵敏度特性。产品针对 **EU868 频段** 设计，符合欧洲地区射频规范，适用于欧盟及采用 EU868 频段的区域。模块内置完整 LoRaWAN 协议栈，支持 Class A/Class B/Class C 三种工作模式，同时兼容点对点（P2P）通信。支持低功耗休眠，满足长续航终端需求。
硬件上集成拨码开关，可灵活切换 UART 通信引脚，适配不同主控平台引脚分配。模块采用标准 AT 指令控制，支持多模块堆叠部署，便于功能扩展。配套高性能胶棒天线，可提升信号稳定性、覆盖范围与通信距离，适应复杂工业与户外环境。本模块可作为采集节点接入 LoRaWAN 网关，实现数据采集与远程管理；也可在无网关场景下通过 P2P 模式实现设备间直连通信。典型应用包括智慧农业、工业监测、环境监测等长距离低功耗物联网通信场景。

## 产品特性

- 遵循 LoRaWAN 1.0.3 协议
- 支持 EU868 频段
- 支持 LoRa P2P (点对点) 通信
- LoRaWAN 激活模式：OTAA、ABP
- 串口通信 (AT 指令)
- 采用高灵敏度胶棒天线
- 低功耗
- 开发平台
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Module LoRaWAN-EU868
- 1 x 胶棒天线

## 应用场景

- 智慧农业
- 工业监测
- 环境监测节点部署

## 规格参数

| 规格             | 参数                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------ |
| LoRa 方案        | STM32WLE5 @256 KB 闪存，64 KB RAM                                                          |
| 支持频段         | EU868 (863~870 MHz)                                                                        |
| 协议支持         | LoRaWAN 1.0.3 协议 (Class A/Class B/Class C)                                               |
| 接收灵敏度       | -137 dBm                                                                                   |
| 发射功率         | 最大 19dBm                                                                                 |
| LoRaWAN 激活模式 | OTAA、ABP                                                                                  |
| 通信模式         | LoRaWAN 和点对点 (P2P)                                                                     |
| 接口类型         | UART @ 115200bps，支持 AT 指令                                                             |
| 天线规格         | 尺寸 198 x 13mm，接口类型 SMA（内螺内针），工作频段 863 ~ 870 MHz，增益 2.8dBi，驻波比≤1.3 |
| 待机功耗         | 待机状态：DC 5V@6.70mA<br/>休眠状态：DC 5V@9uA 或 3.3V@3.69uA                              |
| 工作电流         | P2P 模式接收数据（带宽 125K）：5V@8.27mA<br/>P2P 模式连续发送数据（带宽 125K）：5V@80.38mA |
| 工作温度         | 0 ~ 40°C                                                                                   |
| 产品尺寸         | 54.0 x 63.6 x 7.6mm                                                                        |
| 产品重量         | 16.1g                                                                                      |
| 包装尺寸         | 134.0 x 95.0 x 15.7mm                                                                      |
| 毛重             | 54.2g                                                                                      |

### 操作说明

## 工作模式说明

LoRaWAN 工作模式对比

| 模式    | 下行实时性 | 功耗 | 应用场景                     |
| ------- | ---------- | ---- | ---------------------------- |
| Class A | 最低       | 最低 | 周期性数据上传，低功耗传感器 |
| Class B | 中等       | 中等 | 定时控制设备                 |
| Class C | 最高       | 最高 | 实时控制设备，如工业自动化   |

## 认证信息

- [RAK3172 Module Certification Information](https://downloads.rakwireless.com/#LoRa/RAK3172/Certification)

## 原理图

- [Module LoRaWAN-EU868 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/SCH_LoRaWAN868_HW1.0_2026_04_20_16_29_29.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/SCH_LoRaWAN868_HW1.0_2026_04_20_16_29_29_page_01.png" width="100%">

## 管脚映射

### M5-Bus

\#> DIP Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN           |
| ------- | ---- | ----- | ------------- |
| GND     | 1    | 2     | RX (SW)       |
| GND     | 3    | 4     |               |
| GND     | 5    | 6     |               |
|         | 7    | 8     | RST (SW)      |
|         | 9    | 10    |               |
|         | 11   | 12    |               |
| RX (SW) | 13   | 14    | TX (SW)       |
| RX (SW) | 15   | 16    | TX (SW)       |
|         | 17   | 18    |               |
|         | 19   | 20    |               |
| TX (SW) | 21   | 22    | RST/RX (SW)   |
| TX (SW) | 23   | 24    | TX (SW)       |
| HPWR    | 25   | 26    | RX (SW)       |
| HPWR    | 27   | 28    | 5V            |
| HPWR    | 29   | 30    |               |
::

## 尺寸图

- [Module LoRaWAN-EU868 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/m148-module-lorawan-eu868-model-size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/m148-module-lorawan-eu868-model-size_page_01.png" width="100%">

## 数据手册

- [RAK3172 数据手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/data%20sheet.pdf)

## 软件开发

### Arduino

- [Module LoRaWAN-EU868 Arduino 驱动库](https://github.com/m5stack/M5-LoRaWAN-RAK)

### 通信协议

- [Module LoRaWAN-EU868 AT命令手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/AT%20command%20manual.pdf)

## 相关视频

- Module LoRaWAN-EU868 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LORWAN-EU868-video-ZH.mp4" type="video/mp4"></video>