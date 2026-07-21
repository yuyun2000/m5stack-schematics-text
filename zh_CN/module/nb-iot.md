# Module NBIoT

<span class="product-sku">SKU:M028</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot/nb-iot_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot/nb-iot_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot/nb-iot_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot/nb-iot_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot/nb-iot_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot/nb-iot_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot/nb-iot_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot/nb-iot_09.webp">
</PictureViewer>

## 描述

**Module NBIoT** 是 M5Stack 堆叠模块系列中的一款 NB-IoT 通信模块。内部集成高性能 NB-IoT 全网通无线通信模组 **M5311** 。低功耗设计可以帮助客户获得更长的终端使用寿命。M5311 提供丰富的外部接口和协议栈，支持外接传感器设备，为用户的产品开发提供了极大的便利。同时支持 OneNET 云平台协议，真正实现无缝对接，快速开发。
该模块特别适用于以超低功耗、超小尺寸为核心需求的智能表计、智能穿戴、智能停车、市政管理等 IoT 行业。

## 产品特性

- SIM 卡类型: Nano
- 状态信号：两路 LED 指示灯
- 单路开关机按钮
- 板载天线可选：默认板载弹簧天线 (或通过跳线切换至 IPEX 座)
- 串行通信：Uart2 16/17
- 工作温度范围:-40°C 至 + 85°C
- NB-IoT: 支持 LTE Cat NB2\*
- 频段:
  - B3/B5/B8
- 数据传输:
  - LTE Cat NB1 速率 (kbps):
    - Single Tone 15.625(UL)/21.25(DL)
    - Multi Tone 62.5(UL)/21.25(DL)
  - SMS: 支持 PDU/TEXT 模式
  - SMS 支持 PDU/TEXT 模式
  - 网络协议 IPv4/IPv6/UDP/TCP/CoAP/LwM2M/HTTP/MQTT/TLS
- 电气特性:
  - 耗流:
    - 3uA@PSM
    - 0.4mA@ldle, mode(DRx=1.28S)
    - 167mA@Tx(23dBm/15kHzST)
    - 54mA@Rx
  - 输出功率: 23dBm±2dB
  - 灵敏度:
    - 114dBm (无重传)
    - 130dBm (开启重传)

## 包装内容

- 1 x Module NBIoT

## 应用场景

- 智能表计
- 智能停车
- 市政管理

## 规格参数

| 规格     | 参数                |
| -------- | ------------------- |
| 产品重量 | 13g                 |
| 毛重     | 24g                 |
| 产品尺寸 | 54.2 x 54.2 x 2.8mm |
| 包装尺寸 | 60 x 57 x 17mm      |

## 操作说明

### 部分国家运营商频段

以下内容非实时信息，仅供参考。

| North America                      | B4 (1700), B12 (700), B66 (1700), B71 (600), B26 (850)                      |
| ---------------------------------- | --------------------------------------------------------------------------- |
| Asia Pacific                       | B1(2100), B3(1800), B5(850), B8(900), B18(850), B20(800), B26(850),B28(700) |
| Europe:                            | B3 (1800), B8 (900) , B20 (800)                                             |
| Latin America                      | B2(1900), B3(1800), B5(850), B28(700)                                       |
| Commonwealth of Independent States | B3 (1800), B8 (900), B20 (800)                                              |
| Sub-Saharan Africa                 | B3(1800), B8(900)                                                           |
| Middle East, North Africa          | B8(900), B20(800)                                                           |

补充说明:

- GPIO2 维持高电平 2s 开机
- GPIO2 维持高电平 8s 关机
- 电源按钮长按 2s 开机
- 电源按钮长按 8s 关机
- GPIO26 高电平模块复位

?> 兼容性 | 搭配 Fire 主控使用时候，由于 PSRAM 引脚（G16/G17）冲突，需要飞线引至另一组 UART 引脚。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot/nb-iot_05.webp" width="100%">

## 原理图

- [NB-IoT Plus Module](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Modules/module_nb_iot_sch.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/955/M028-module_nb_iot_sch_page_01.png" width="100%">

## 管脚映射

### M5-Bus

\#> Fly Wire | 下方 M5-Bus 中标记 `FW` 的引脚，可通过飞线进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN        | LEFT | RIGHT | PIN       |
| ---------- | ---- | ----- | --------- |
| GND        | 1    | 2     |           |
| GND        | 3    | 4     |           |
| GND        | 5    | 6     |           |
|            | 7    | 8     |           |
|            | 9    | 10    | RST       |
|            | 11   | 12    | 3V3       |
|            | 13   | 14    |           |
| TXD (FW)   | 15   | 16    | RXD (FW)  |
|            | 17   | 18    |           |
| PWR        | 19   | 20    | RXD (FW)  |
| TXD (FW)   | 21   | 22    | RXD (FW)  |
| TXD (FW)   | 23   | 24    |           |
|            | 25   | 26    |           |
|            | 27   | 28    |           |
|            | 29   | 30    |           |
::

## 数据手册

- [M5311](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M5311_cn.pdf)

## 软件开发

### Arduino

- [Module NBIoT Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/NB-IoT_M5311LV).

### 通信协议

- [M5311 AT指令表](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M5311_AT_Command_Interface_Specification_en.pdf)

### Easyloader

| Easyloader                                  | 下载链接                                                                                               | 备注 |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---- |
| Module NBIoT Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_NBIOT_MODULE.exe) | /    |
