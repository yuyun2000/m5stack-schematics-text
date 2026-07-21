# Module COMX LoRaWAN868 v2.0

<span class="product-sku">SKU:M031-C4</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan868_2.0/comx_lorawan868_2.0_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan868_2.0/comx_lorawan868_2.0_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan868_2.0/comx_lorawan868_2.0_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan868_2.0/comx_lorawan868_2.0_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan868_2.0/comx_lorawan868_2.0_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan868_2.0/comx_lorawan868_2.0_06.webp">
</PictureViewer>

## 描述

**Module COMX LoRaWAN868 v2.0** 是 M5Stack 推出的适用于 868MHz 频率的 LoRaWAN 通讯模块。模块采用 ASR6501 方案 ，支持远距离通信的同时兼具高灵敏度特性。模组集成 LoRaWAN 协议栈，采用串口通信接口 (使用 AT 指令集进行控制) ，使用时可作为采集节点大量接入网关进行数据收集管理。该模块适合应用于长距离的低功耗物联网通信应用，如环境监测节点部署等。

## 注意事项

?> 兼容性 | 搭配 Fire 主控使用时候，由于 PSRAM 引脚（G16/G17）冲突，使用时候请将模块底座拨码开关引脚切换至 TX (G0/G13),RX (G5/G15)。

## 产品特性

- ASR6501
- 工作频率：868MHz
- SMA 天线
- 通信接口: UART
- 指令协议：AT 命令

## 包装内容

- 1 x Module COMX LoRaWAN868 v2.0
- 1 x SMA 天线

## 应用场景

- 自动远程抄表
- 智能交通智能停车场
- 远程灌溉及环境监测

## 规格参数

| 规格           | 参数                      |
| -------------- | ------------------------- |
| 通信芯片       | ASR6501                   |
| 工作频率       | 868MHz                    |
| LoRaWAN 版本   | v1.0.1                    |
| 最小接收灵敏度 | -137dBm (SF=12/BW=125KHz) |
| 最大发射功率   | +21dBm                    |
| 通讯方式       | UART 115200bps            |
| 产品重量       | 27.4g                     |
| 毛重           | 70.4g                     |
| 产品尺寸       | 54.2 x 54.2 x 13.2mm      |
| 包装尺寸       | 165 x 60 x 36mm           |

## 操作说明

### 868Mhz 支持的主要国家及地区

**阿尔巴尼亚 / 安道尔 / 亚美尼亚 / 奥地利 / 巴林 / 孟加拉国 / 白俄罗斯 / 比利时 / 缅甸 / 波斯尼亚和黑塞哥维那 / 文莱达鲁萨兰国 / 保加利亚 / 柬埔寨 / 柬埔寨 / 克罗地亚 / 塞浦路斯 / 丹麦 / 埃及 / 爱沙尼亚 / 芬兰 / 法国 / 德国 / 德国危地马拉 / 匈牙利 / 冰岛 / 伊朗 / 爱尔兰 / 意大利 / 老挝 / 拉脱维亚 / 黎巴嫩 / 列支敦斯登 / 立陶宛 / 卢森堡 / 马其顿，前南斯拉夫联盟共和国 / 马耳他 / 摩尔多瓦 / 黑山 / 摩洛哥 / 荷兰 / 荷兰 / 纽西兰 尼日利亚 / 挪威 / 阿曼 / 巴基斯坦 / 波兰 / 葡萄牙 / 卡塔尔 / 罗马尼亚 / 沙特阿拉伯 / 塞尔维亚 / 新加坡 / 斯洛文尼亚 / 南非 / 西班牙 / 瑞典 / 瑞士 / 突尼斯 / 土耳其 / 乌克兰 / 阿联酋 / 英国 / 越南**

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan868_2.0/comx_lorawan868_2.0_support_area.webp">

\#> 供电切换 | 模块底座带有 DC 电源输入接口，使用该接口接入电源请严格按照输入范围 (5-12V) 防止模块损坏。内部电源拨码开关可调节内部的端子 VIN 的电压水平，用于适配不同模块。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte/comx_lte_dc_power.webp" width="70%">

## 原理图

### Module COMX 模块插接底板原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lorawan868_2.0/comx_lorawan868_2.0_sch_01.webp" width="80%">

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

- [Module COMX LoRaWAN868 v2.0](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX_page_01.png" width="100%">

## 数据手册

- [LoRaWAN 区域参数](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/lorawantm_regional_parameters_v1.1rb_-_final.pdf)

## 软件开发

### Arduino

- [COM.LoRaWAN868 v2.0 OTAA with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/COM_LoRaWAN915)

### 通信协议

- [LoRaWAN868 AT 指令集](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/COM.LoRaWAN.Ra-07.asr6501-asr6502-at-commands-introduction-v4.3.pdf)
