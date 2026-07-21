# Module COMX Cat1

<span class="product-sku">SKU:M031-H</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_cat1/comx_cat1_01.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_cat1/comx_cat1_02.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_cat1/comx_cat1_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_cat1/comx_cat1_04.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_cat1/comx_cat1_05.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_cat1/comx_cat1_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_cat1/comx_cat1_07.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_cat1/comx_cat1_08.webp"><img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_cat1/comx_cat1_09.webp">
</PictureViewer>

## 描述

**Module COMX Cat1** 是一款 LTE CAT1 数据通信模块，内置适配中国地区 LTE CAT1 频段的 SIM-A7680C 模组，支持 LTE-TDD/LTE-FDD 无线通信制式。模块集成 SMA 外部天线接口，保障设备通信质量与信号的稳定性。集成 DC 5 ~ 12V 电源输入接口，供电方式更多选择。兼容 M5Stack 堆叠体系，能够与同系列模块堆叠实现功能拓展。与 NB-IoT 相比，CAT1 有着更强的数据传输能力。最大下行速率可达 10Mbps （上行） / 5Mbps （下行） 。该模块非常适合应用在对于数据传输速率有所要求的应用场景 （远程控制 / 数据透传等） 。

## 产品特性

- SIM-A7680C
  - 适用于中国地区 CAT1 频段
  - LTE CAT1 模块，支持 LTE-TDD/LTE-FDD 无线通信制式
  - 最大下行速率 10Mbps / 最大上行速率 5Mbps。
  - UART 接口 / AT 指令控制
  - 卡槽规格：Nano
- 模块接口：
  - 1 x DC 5/12V POWER INPUT
  - SMA 天线接口
  - 底座集成拨码开关，支持通信引脚切换
- 5 x 5cm 规格，兼容 M5Stack 堆叠体系
- 开发平台:
  - [UiFlow](http://flow.m5stack.com)
  - [Arduino](http://www.arduino.cc)

## 包装内容

- 1 x Module COMX Cat1
- 1 x SMA 天线

## 应用场景

- 远程控制 / 数据采集
- 数据上云应用

## 认证信息

### SIM-A7680C 模块认证

- 3C/SRRC/NAL/RoHS/REACH

## 规格参数

| 规格           | 参数                                                                            |
| -------------- | ------------------------------------------------------------------------------- |
| 通信模组       | SIM-A7680C                                                                      |
| 上下行速度     | 最大下行速率 10Mbps / 最大上行速率 5Mbps                                        |
| 支持 CAT1 频段 | LTE-TDD: B34/B38/B39/B40/B41<br/>LTE-FDD: B1/B3/B5/B8                           |
| 网络协议       | TCP/IP/IPV4/IPV6/MultiPDP/FTP/HTTP/DNS/RNDIS/ECM/PPP/TLS/LBS/TTS/MQTT/WiFi Scan |
| 通讯方式       | UART 115200bps 8N1                                                              |
| SIM 卡槽规格   | Nano                                                                            |
| 输入电源       | M5-Bus (5V) / DC INPUT (5V/12V)                                                 |
| 产品重量       | 28.6g                                                                           |
| 毛重           | 78.0g                                                                           |
| 产品尺寸       | 54.2 x 54.2 x 13.2mm                                                            |
| 包装尺寸       | 165 x 60 x 36mm                                                                 |

## 操作说明

\#> 供电切换 | 模块底座带有 DC 电源输入接口，使用该接口接入电源请严格按照输入范围 (5-12V) 防止模块损坏。内部电源拨码开关可调节内部的端子 VIN 的电压水平，用于适配不同模块。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte/comx_lte_dc_power.webp" width="70%">

## 原理图

### Module COMX 模块插接底板原理图

<img src = "https://static-cdn.m5stack.com/resource/docs/products/module/comx_cat1/comx_cat1_sch_01.webp" width="80%">

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

- [Module COMX Cat1 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX_page_01.png" width="100%">

## 数据手册

- Application
  - [A76XX Series_Audio_Application Note_V1.02.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_Audio_Application%20Note_V1.02.pdf)
  - [A76XX Series_Blue Tooth_Application Note_V1.02.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_Blue%20Tooth_Application%20Note_V1.02.pdf)
  - [A76XX Series_CTBURST_Application Note_V1.00.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_CTBURST_Application%20Note_V1.00.pdf)
  - [A76XX Series_CTBURST_Application Note_V1.00.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_CTBURST_Application%20Note_V1.00.pdf)
  - [A76XX Series_FOTA_Application Note_V1.00.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_FOTA_Application%20Note_V1.00.pdf)
  - [A76XX Series_FTP(S)_Application Note_V1.02.pdf](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_FTP(S)_Application%20Note_V1.02.pdf>)
  - [A76XX Series_GNSS_Application Note_V1.02.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_GNSS_Application%20Note_V1.02.pdf)
  - [A76XX Series_GNSS_Dynamic_Loading_Instructions_Application Note_V1.00.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_GNSS_Dynamic_Loading_Instructions_Application%20Note_V1.00.pdf)
  - [A76XX Series_HTTP(S)_Application Note_V1.02.pdf](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_HTTP(S)_Application%20Note_V1.02.pdf>)
  - [A76XX Series_LBS_Application Note_V1.02.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_LBS_Application%20Note_V1.02.pdf)
  - [A76XX Series_MQTT(S)_Application Note_V1.02.pdf](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_MQTT(S)_Application%20Note_V1.02.pdf>)
  - [A76XX Series_SSL_Application Note_V1.02.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_SSL_Application%20Note_V1.02.pdf)
  - [A76XX Series_Sleep Mode_Application Note_V1.02.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_Sleep%20Mode_Application%20Note_V1.02.pdf)
  - [A76XX Series_TCPIP_Application Note_V1.02.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_TCPIP_Application%20Note_V1.02.pdf)
  - [A76XX Series_UART_Application Note_V1.02.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_UART_Application%20Note_V1.02.pdf)
  - [A76XX Series_UIM HOT SWAP_Application Note_V1.02.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_UIM%20HOT%20SWAP_Application%20Note_V1.02.pdf)
  - [A76XX 系列云平台协议应用文档_V1.01.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%E7%B3%BB%E5%88%97_%E4%BA%91%E5%B9%B3%E5%8F%B0%E5%8D%8F%E8%AE%AE_%E5%BA%94%E7%94%A8%E6%96%87%E6%A1%A3_V1.01.pdf)
- AT Command
  - [A76XX Series MQTT_EX_AT Command Manual_V1.00.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series%20MQTT_EX_AT%20Command%20Manual_V1.00.pdf)
  - [A76XX Series_AT_Command_Manual_V1.06.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_AT_Command_Manual_V1.06.pdf)

## 软件开发

### Arduino

- Examples
  - [Module COMX Cat1 MQTT Client with M5Core](https://github.com/m5stack/M5Stack/blob/master/examples/Modules/COM_CAT1_SIM7680/COM_CAT1_SIM7680.ino)
  - [Module COMX Cat1 MQTT Client with M5Core2](https://github.com/m5stack/M5Core2/blob/master/examples/Module/COM_CAT1_SIM7680/COM_CAT1_SIM7680.ino)
- Libraries
  - [TinyGSM](https://github.com/vshymanskyy/TinyGSM)
  - [PubSubClient](https://github.com/knolleary/pubsubclient.git)

### UiFlow1

- [Module COMX Cat1 UiFlow1 文档](/zh_CN/uiflow/blockly/module/comx_cat1)
