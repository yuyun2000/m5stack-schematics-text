# Module COMX LTE-Data

<span class="product-sku">SKU:M031-E</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte-data/comx_lte-data_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte-data/comx_lte-data_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte-data/comx_lte-data_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte-data/comx_lte-data_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte-data/comx_lte-data_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte-data/comx_lte-data_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte-data/comx_lte-data_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte-data/comx_lte-data_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte-data/comx_lte-data_09.webp">
</PictureViewer>

## 描述

**Module COMX LTE-Data** 是一款可堆叠的多功能 LTE 通信模块，内置 LTE 通讯模组 A7600C1 ，支持 LTE-TDD/LTE-FDD/EDGE/GPRS 和 GSM 等频段 ，传输速率为 LTE.CAT4 标准。其性能稳定 ，外观小巧 ，性价比高 ，可以低功耗实现数据信息的传输。模块带有 DC 电源输入 ，可通过外部电源提供 5 ~ 12V 供电。为了方便用户配置引脚，采用拨码开关对引脚进行设置。该模块特别适用于以低功耗、超小尺寸为核心需求的远程抄表、智能停车、市政管理等 IoT 行业。

## 注意事项

?> 兼容性 | 搭配 Fire 主控使用时候，由于 PSRAM 引脚（G16/G17）冲突，使用时候请将模块底座拨码开关引脚切换至 TX (G0/G13),RX (G5/G15)。

## 产品特性

- 可堆叠设计
- 可外部独立供电
- AT 指令控制
- SIM 卡类型: MicroSIM
- 状态信号：两路 LED 指示灯
- 外置天线：SMA 天线
- 串行通信：UART 115200bps
- 频段:
  - LTE-TDD B34/B38/B39/B40/B41
  - LTE-FDD B1/B3/B5/B8
  - GSM/GPRS/EDGE 900/1800 MHz
- 数据传输:
- LTE Cat 1
  - 上行最大 5Mbps
  - 下行最大 10Mbps
- EDGE
  - 上行 / 下行最大 236.8Kbps
- GPRS
  - 上行 / 下行最大 85.6Kbps
- 支持协议
  - TCP/IP/IPV4/IPV6/MultiPDP/FTP/FTPS/HTTP/HTTPS/DNS
  - RNDIS/PPP/ECM
  - SSL

## 包装内容

- 1 x Module COMX LTE-Data
- 1 x SMA 天线

## 应用场景

- 智能表计
- 智能停车
- 市政管理

## 规格参数

| 规格        | 参数                            |
| ----------- | ------------------------------- |
| 支持频段    | LTE-TD/LTE-FDD/GPRS/EDGE/GSM    |
| 网络协议    | TCP/IP/UDP/HTTP/MQTT/FTP/DNS 等 |
| 通讯方式    | UART 115200bps                  |
| DC 接口规格 | 5.5mm                           |
| 产品重量    | 54g                             |
| 毛重        | 89g                             |
| 产品尺寸    | 54 x 54 x 13.2mm                |
| 包装尺寸    | 165 x 60 x 36mm                 |

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

\#> 供电切换 | 模块底座带有 DC 电源输入接口，使用该接口接入电源请严格按照输入范围 (5-12V) 防止模块损坏。内部电源拨码开关可调节内部的端子 VIN 的电压水平，用于适配不同模块。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte/comx_lte_dc_power.webp" width="70%">

## 原理图

### Module COMX 模块插接底板原理图

<img src = "https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte-data/comx_lte-data_sch_01.webp" width="80%">

## 管脚映射

### M5-Bus

\#> Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN       | LEFT | RIGHT | PIN       |
| --------- | ---- | ----- | --------- |
| GND       | 1    | 2     |           |
| GND       | 3    | 4     |           |
| GND       | 5    | 6     |           |
|           | 7    | 8     |           |
|           | 9    | 10    |           |
|           | 11   | 12    | 3V3       |
|           | 13   | 14    |           |
| TXD (SW)  | 15   | 16    | RXD (SW)  |
|           | 17   | 18    |           |
|           | 19   | 20    | TXD (SW)  |
|           | 21   | 22    | RXD (SW)  |
| TXD (SW)  | 23   | 24    | RXD (SW)  |
|           | 25   | 26    |           |
|           | 27   | 28    | 5V        |
|           | 29   | 30    |           |
::

## 尺寸图

- [Module COMX LTE-Data 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX_page_01.png" width="100%">

## 软件开发

### Arduino

- [Module COMX LTE-Data Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/COM_LTE-DATA).

### 通信协议

- [A7600C1 AT 指令表](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/SIM7500_SIM7600%20Series_AT%20Command%20Manual%20_V1.10.pdf)

### Easyloader

| Easyloader                                          | 下载链接                                                                                                       | 备注 |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---- |
| Module COMX LTE-Data Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_COM_LTE_DATA.exe) | /    |

### 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/COM.LTE-DATA.mp4">
</video>
