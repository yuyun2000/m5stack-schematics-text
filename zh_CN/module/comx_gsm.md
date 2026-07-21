# Module COMX GSM

<span class="product-sku">SKU:M031-D</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gsm/comx_gsm_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gsm/comx_gsm_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gsm/comx_gsm_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gsm/comx_gsm_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gsm/comx_gsm_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_gsm/comx_gsm_06.webp">
</PictureViewer>

## 描述

**Module COMX GSM** 是一款可堆叠的 2G 通信模块 ，内置通讯模组为 SIM800C ，工作频率为 GSM/GPRS 850/900/1800/1900MHz ，以低功耗实现 SMS 文本和数据信息的传输。模块带有 DC 电源输入 ，可通过外部电源提供 5 ~ 12V 供电。为了方便用户配置引脚 ，采用拨码开关对引脚进行设置。该模块特别适用于以超低功耗、超小尺寸为核心需求的远程抄表、智能穿戴、智能停车、市政管理等 IoT 行业。

## 注意事项

?> 兼容性 | 搭配 Fire 主控使用时候，由于 PSRAM 引脚（G16/G17）冲突，使用时候请将模块底座拨码开关引脚切换至 TX (G0/G13),RX (G5/G15)。

## 产品特性

- 可堆叠设计
- 支持 SMS 文本、数据传输
- 可外部独立供电
- AT 指令控制
- SIM 卡类型: MicroSIM
- 状态信号：两路 LED 指示灯 (电源 / 网络状态)
- 供电电压：3.4-4.4V
- 休眠模式下典型功耗：0.88mA
- 外置天线：2.5dB SMA 天线
- 串行通信：UART 115200bsp
- 工作温度范围:-40°C 至 + 85°C
- 频段:
  - 四频 850/900/1800/1900MHz
  - GPRS multi-slot class 12/10
  - GPRS mobile station class B
- 数据传输:
  - PRS class 12: 最大 85.6 kbps (上行 / 下行速率)
  - 支持 PBCCH (Packet Broadcast Control Channel)
  - 编码方案：CS 1, 2, 3, 4
  - 集成 TCP/IP、UDP、HTTP、FTP 等协议
  - 支持 USSD (Unstructured Supplementary Services Data)

## 包装内容

- 1 x Module COMX GSM
- 1 x SMA 天线

## 应用场景

- 智能表计
- 智能停车
- 市政管理

## 规格参数

| 规格        | 参数                                         |
| ----------- | -------------------------------------------- |
| 频段        | GSM/GPRS 850/900/1800/1900MHz                |
| 网络协议    | TCP/IP/UDP/FTP/HTTP 等                       |
| 天线增益    | 2.5dB 1880-1900MHZ/2320-2370MHZ 2575-2635MHZ |
| 通讯方式    | UART 115200bps                               |
| DC 接口规格 | 5.5mm                                        |
| 产品重量    | 40g                                          |
| 毛重        | 75g                                          |
| 模块尺寸    | 54 x 54 x 13.2mm                             |
| 包装尺寸    | 165 x 60 x 36mm                              |

## 操作说明

\#> 供电切换 | 模块底座带有 DC 电源输入接口，使用该接口接入电源请严格按照输入范围 (5-12V) 防止模块损坏。内部电源拨码开关可调节内部的端子 VIN 的电压水平，用于适配不同模块。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte/comx_lte_dc_power.webp" width="70%">

## 原理图

### Module COMX 模块插接底板原理图

<img src = "https://static-cdn.m5stack.com/resource/docs/products/module/comx_gsm/comx_gsm_sch_01.webp" width="80%">

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

- [Module COMX GSM 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX_page_01.png" width="100%">

## 数据手册

- [SIM800C datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/SIM800C_datasheet.pdf)

## 软件开发

### Arduino

- [Module COMX GSM Example - with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/GSM_M6315).

### UiFlow1

- [Module COMX GSM UiFlow1 文档](/zh_CN/uiflow/blockly/module/comx_gsm)

### 通信协议

- [SIM800C AT 指令表](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/SIM800_Series_AT_Command_Manual_V1.09.pdf)

### Easyloader

| Easyloader                                     | 下载链接                                                                                                   | 备注 |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---- |
| Module COMX GSM Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_COMX_GSM.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/COM.GSM.mp4" type="video/mp4">
</video>
