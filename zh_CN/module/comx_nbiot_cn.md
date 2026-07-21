# Module COMX NBIoT-CN

<span class="product-sku">SKU:M031-B2</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_08.webp">
</PictureViewer>

## 描述

**Module COMX NBIoT-CN** 是一款匹配 **中国地区** Cat-NB 频段的 **NB-IoT** 无线通信模块。内置 **SIM7020C** 通讯模组，采用串口通信（AT 指令集控制），集成 SMA 外部天线接口，提升设备通信质量与信号的稳定性。SIM7020C 模块是低延迟、低吞吐量应用的最优解决方案，非常适用于如表计、远程控制、资产跟踪、远程监控、远程医疗、共享单车等物联网应用。

## 注意事项

?> 兼容性 | 搭配 Fire 主控使用时候，由于 PSRAM 引脚（G16/G17）冲突，使用时候请将模块底座拨码开关引脚切换至 TX (G0/G13),RX (G5/G15)。

## 产品特性

- 适用于中国地区
- 可堆叠设计
- 信号接入能力强
- 可外部独立供电
- AT 指令控制
- SIM 卡类型: Nano
- 外置天线：SMA 天线
- 串行通信：UART 115200bps
- Cat-NB 频段:
  - B1/B3/B5/B8
- 数据传输 (kbps):
  - 26.15(DL)/62.5(UL)
- 网络协议:
  - TCP/UDP/LWM2M/COAP/ MQTT/HTTP/HTTPS/ TLS/DTLS/DNS/NTP/ PING/OneNET/ 电信云 / 艾拉云 \*

## 包装内容

- 1 x Module COMX NBIoT-CN
- 1 x SMA 天线

## 应用场景

- 智能表计
- 远程监控
- 共享单车

## 认证信息

- RoHS/REACH/CCC/CTA/SRRC/Mobile/Unicom/Telecom/ATEX
- 中国电信 / 中国联通 / 中国移动

## 规格参数

| 规格             | 参数                                                                                   |
| ---------------- | -------------------------------------------------------------------------------------- |
| 通信模组         | SIM7020C                                                                               |
| 支持 Cat-NB 频段 | B1/B3/B5/B8                                                                            |
| 网络协议         | TCP/UDP/LWM2M/COAP/ MQTT/HTTP/HTTPS/ TLS/DTLS/DNS/NTP/ PING/OneNET/ 电信云 / 艾拉云 \* |
| 通讯方式         | UART 115200bps                                                                         |
| DC 接口规格      | 5.5mm                                                                                  |
| 产品重量         | 40g                                                                                    |
| 毛重             | 75g                                                                                    |
| 产品尺寸         | 54 x 54 x 13.2mm                                                                       |
| 包装尺寸         | 165 x 60 x 36mm                                                                        |

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

<SchViewer>
<img src = "https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_sch_01.webp">
<img src = "https://static-cdn.m5stack.com/resource/docs/products/module/comx_nbiot_cn/comx_nbiot_cn_sch_02.webp">
</SchViewer>

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

- [Module COMX NBIoT-CN 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX_page_01.png" width="100%">

## 数据手册

- **Datasheet**
  - [SIM7020 Series datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020_Series_SPEC_20201104.pdf)
  - [SIM7020 Series_Ayla_Application Note_V1.03](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_Ayla_Application%20Note_V1.03.pdf)
  - [SIM7020 Series_CTBURST_Application Note_V1.01](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_CTBURST_Application%20Note_V1.01.pdf)
  - [SIM7020 Series_CoAP_Application Note_V1.03](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_CoAP_Application%20Note_V1.03.pdf)
  - [SIM7020 Series_EAT_Environment & Compilation & Burning Guide_V1.02.](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_EAT_Environment%20%26amp%3B%20Compilation%20%26amp%3B%20Burning%20Guide_V1.02.pdf)
  - [SIM7020 Series_FOTA_Application_Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_FOTA_Application_Note_V1.02.pdf)
  - [SIM7020 Series_HTTP(S)_Application Note_V1.04](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_HTTP(S)_Application%20Note_V1.04.pdf>)
  - [SIM7020 Series_LWM2M_Application Note_V1.03](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_LWM2M_Application%20Note_V1.03.pdf)
  - [SIM7020 Series_Low Power Mode_Application Note_V1.05](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_Low%20Power%20Mode_Application%20Note_V1.05.pdf)
  - [SIM7020 Series_MQTT(S)_Application Note_V1.05](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_MQTT(S)_Application%20Note_V1.05.pdf>)
  - [SIM7020 Series_NVRAM_Application Note_V1.02](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_NVRAM_Application%20Note_V1.02.pdf)
  - [SIM7020 Series_SAT_Application Note_V1.01](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_SAT_Application%20Note_V1.01.pdf)
  - [SIM7020 Series_SNTP_Application Note_V1.03](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_SNTP_Application%20Note_V1.03.pdf)
  - [SIM7020 Series_TCPIP_Application Note_V1.04](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_TCPIP_Application%20Note_V1.04.pdf)
- **AT Command**
  - [SIM7020 Series_AT Command Manual_V1.05](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_AT%20Command%20Manual_V1.05.pdf)

## 软件开发

### Arduino

- [Module COMX NBIoT-CN Example with M5Core](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Module/COMX_NB-IoT)
