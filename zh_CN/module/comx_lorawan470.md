# Module COMX LoRaWAN470

<span class="product-sku">SKU:M031-C2</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan470/comx_lorawan470_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan470/comx_lorawan470_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan470/comx_lorawan470_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan470/comx_lorawan470_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan470/comx_lorawan470_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan470/comx_lorawan470_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan470/comx_lorawan470_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan470/comx_lorawan470_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan470/comx_lorawan470_09.webp">
</PictureViewer>

## 描述

**Module COMX LoRaWAN470** 是 M5Stack 推出的适用于 470MHz 频率的 LoRaWAN 通讯模块。模块采用 ASR6501 方案 ，支持远距离通信的同时兼具超低功耗与高灵敏度特性。模组集成 LoRaWAN 协议栈，采用串口通信接口 (使用 AT 指令集进行控制) ，使用时可作为采集节点大量接入网关进行数据收集管理。
提供外部电源接口 (通过切换拨码开关可以调整 5V/12V 两种电压电源输入) ，该模块适合应用于长距离的低功耗物联网通信应用，如环境监测节点部署等。

## 注意事项

?> 兼容性 | 搭配 Fire 主控使用时候，由于 PSRAM 引脚（G16/G17）冲突，使用时候请将模块底座拨码开关引脚切换至 TX (G0/G13),RX (G5/G15)。

## 产品特性

- ASR6501
- 工作频率：470MHz
- SMA 天线
- 指令协议：AT 命令
- UART 通信接口：
  - 波特率：115200
  - 停止位：1
  - 数据位：8
  - 校验位：无
  - 结束符：无

## 包装内容

- 1 x Module COMX LoRaWAN470
- 1 x SMA 天线

## 应用场景

- 自动远程抄表
- 智能交通智能停车场
- 远程灌溉及环境监测

## 规格参数

| 规格        | 参数                 |
| ----------- | -------------------- |
| UART 波特率 | 115200               |
| DC 接口规格 | 5.5mm                |
| 产品重量    | 35g                  |
| 毛重        | 72g                  |
| 产品尺寸    | 54.2 x 54.2 x 13.2mm |
| 包装尺寸    | 165 x 60 x 36mm      |

## 操作说明

### CN470 支持的主要国家及地区

**中国**

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan470/lorawan470_support_area.webp">

\#> 供电切换 | 模块底座带有 DC 电源输入接口，使用该接口接入电源请严格按照输入范围 (5-12V) 防止模块损坏。内部电源拨码开关可调节内部的端子 VIN 的电压水平，用于适配不同模块。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte/comx_lte_dc_power.webp" width="70%">

## 原理图

### Module COMX 模块插接底板原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan470/comx_lorawan470_sch_01.webp" width="80%">

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

- [Module COMX LoRaWAN470 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX_page_01.png" width="100%">

## 数据手册

- [LoRaWAN 区域参数](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/lorawantm_regional_parameters_v1.1rb_-_final.pdf)

## 软件开发

### Arduino

- [Module COMX LoRaWAN470 Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/COM_LoRaWAN470)

### UiFlow1

- [Module COMX LoRaWAN470 UiFlow1 文档](/zh_CN/uiflow/blockly/module/comx_lorawan_470)

### 通信协议

- [Module COMX LoRaWAN470 AT 指令集](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/COM.LoRaWAN.Ra-07.asr6501-asr6502-at-commands-introduction-v4.3.pdf)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/COM.LoRaWAN470.mp4" type="video/mp4">
</video>
