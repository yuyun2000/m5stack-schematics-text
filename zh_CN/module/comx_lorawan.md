# Module COMX LoRaWAN868

<span class="product-sku">SKU:M031-C</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan/comx_lorawan_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan/comx_lorawan_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan/comx_lorawan_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan/comx_lorawan_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan/comx_lorawan_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan/comx_lorawan_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan/comx_lorawan_07.webp">
</PictureViewer>

## 描述

**Module COMX LoRaWAN868** 是 M5Stack 堆叠模块系列中的一款 LoRaWAN 通讯模块 ，支持节点到节点或 LoRaWAN 通讯。其中 LoRaWAN 模组基于 ASR6501 设计，封装了 PSoC4000 与 SX1262 芯片 ，支持 868MHz 频段，基于超低功耗设计，深度睡眠模式下消耗电流极低 (3.5μA)。为了方便用户配置引脚，采用拨码开关对硬件串口引脚进行设置，用户只需根据需要将相应引脚拨至 ON，在程序中指定引脚即可。在模块下方设计有 DC 电源插座，可通过外部电源供电，搭配外置天线可获得较好的信号质量。该模块特别适用于以超低功耗、超小尺寸为核心需求的远程低功耗传输应用场景。
LoRaWAN 基于 LoRa 远距离通信网络设计的一套通讯协议和系统架构。如果按协议分层来说 LoRaWAN 是媒体访问控制 (MAC) 层，LoRa 是物理层。它是由 LoRa 联盟维护的路由协议，主要用作管理 LPWAN 网关和端节点设备之间的通信的网络协议。

## 注意事项

?> 兼容性 | 搭配 Fire 主控使用时候，由于 PSRAM 引脚（G16/G17）冲突，使用时候请将模块底座拨码开关引脚切换至 TX (G0/G13),RX (G5/G15)。

## 产品特性

- 可堆叠式设计
- 支持 LoRa 与 LoRaWAN
- 模组：基于 ASR6501
- 支持频段：868MHz
- Radio IC: SX1262
- 微处理器：PSoC® 4000 series MCU (ARM® Cortex® M0+ Core)
- 接口: UART
- 指令协议：AT 命令
- 超低功耗
- UART 通信接口：
  - 波特率：115200
  - 停止位：1
  - 数据位：8
  - 校验位：无
  - 结束符：无

## 包装内容

- 1 x Module COMX LoRaWAN868
- 1 x SMA 天线

## 应用场景

- 自动远程抄表
- 智能交通智能停车场
- 远程灌溉及环境监测

## 规格参数

| 规格        | 参数                 |
| ----------- | -------------------- |
| DC 接口规格 | 5.5mm                |
| 产品重量    | 40g                  |
| 毛重        | 75g                  |
| 产品尺寸    | 54.2 x 54.2 x 13.2mm |
| 包装尺寸    | 165 x 60 x 36mm      |

## 操作说明

### EU868 支持的主要国家及地区

**奥地利 / 比利时 / 捷克共和国 / 丹麦 / 芬兰 / 法国 / 德国 / 意大利 / 荷兰 / 瑞典 / 英国 / 安哥拉 / 安道尔 / 保加利亚 / 爱沙尼亚 / 印度 / 马耳他 / 菲律宾 / 葡萄牙 / 俄罗斯 / 西班牙 / 瑞士 / 赞比亚**

\#> 供电切换 | 模块底座带有 DC 电源输入接口，使用该接口接入电源请严格按照输入范围 (5-12V) 防止模块损坏。内部电源拨码开关可调节内部的端子 VIN 的电压水平，用于适配不同模块。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte/comx_lte_dc_power.webp" width="70%">

## 原理图

### Module COMX 模块插接底板原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan/comx_lorawan_sch_01.webp" width="80%">

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

- [Module COMX LoRaWAN868 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX_page_01.png" width="100%">

## 数据手册

- [LoRaWAN 区域参数](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/lorawantm_regional_parameters_v1.1rb_-_final.pdf)

## 软件开发

### Arduino

- [Module COMX LoRaWAN868 Example Easyloader with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/LoRaWAN_RHF76_052)

### UiFlow1

- [Module COMX LoRaWAN868 UiFlow1 Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Module/COM_LoRaWAN/UIFlow)

### UiFlow2

- [Module COMX LoRaWAN868 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/lorawan868.html)

### 通信协议

- [LoRaWAN 的 AT 指令集](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/CubeCell_Series_AT_Command_User_Manual_V0.5.pdf)

### Easyloader

| Easyloader                                            | 下载链接                                                                                                      | 备注 |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---- |
| Module COMX LoRaWAN868 Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_COM_LoraWAN.zip) | /    |
