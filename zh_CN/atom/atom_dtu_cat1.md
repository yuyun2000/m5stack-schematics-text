# Atom DTU Cat1

<span class="product-sku">SKU:K120/A120</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_cat1/atom_dtu_cat1_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_cat1/atom_dtu_cat1_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_cat1/atom_dtu_cat1_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_cat1/atom_dtu_cat1_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_cat1/atom_dtu_cat1_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_cat1/atom_dtu_cat1_06.webp">
</PictureViewer>

\#> 清单 | SKU 为 A120 的是不带 Atom-Lite 主机的。

## 描述

**Atom DTU Cat1** 是一款可编程 LTE CAT1 数据传输单元 (DTU) 。内置适配中国地区 LTE CAT1 频段的 SIM-A7680C 模组，支持 LTE-TDD/LTE-FDD 无线通信制式。与 NB-IoT 相比，CAT1 有着更强的数据传输能力。最大下行速率可达 10Mbps (上行) /5Mbps (下行) 。集成 SMA 外部天线接口，提升设备通信质量与信号的稳定性。与一般仅具备数据透传功能的 DTU 不同，**Atom DTU Cat1** 系列采用更为开放的架构设计。控制器 Atom-Lite 可根据实际业务随意修改程序，整机预留多种接口 (RS485, I2C, 自定义接口) 供用户拓展，便于传感器与执行器的快速接入。自带导轨夹持结构，完美嵌入到各类工业控制现场。非常适合应用在对于数据传输速率有所要求的应用场景 (远程控制 / 数据透传等) 。

## 产品特性

- SIM-A7680C
  - 适用于中国地区 CAT1 频段
  - LTE CAT1 模块，支持 LTE-TDD/LTE-FDD 无线通信制式
  - 最大下行速率 10Mbps / 最大上行速率 5Mbps。
  - UART 接口 / AT 指令控制
  - 卡槽规格：MicroSIM
- 底座拓展接口:
  - 1 x PWR485 (RS485 (支持 Modbus Master/Slave) + DC 12V POWER INPUT)
  - 1 x I2C
- ATOM 主控拓展接口:
  - 1 x 全功能 GPIO
- 自带导轨夹持
- 开发平台:
  - [UiFlow](http://flow.m5stack.com)
  - [Arduino](http://www.arduino.cc)

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic DTU Cat1 Base
- 1 x SMA 天线
- 1 x SMA 红色帽
- 1 x M2 六角扳手
- 1 x M2x16 螺丝
- 1 x HT3.96-4P 端子

## 应用场景

- 远程控制 / 数据采集
- 数据上云应用

## 规格参数

| 规格           | 参数                                                                            |
| -------------- | ------------------------------------------------------------------------------- |
| 通信模组       | SIM-A7680C                                                                      |
| 上下行速度     | 最大下行速率 10Mbps / 最大上行速率 5Mbps                                        |
| 支持 CAT1 频段 | LTE-TDD: B34/B38/B39/B40/B41<br/>LTE-FDD: B1/B3/B5/B8                           |
| 网络协议       | TCP/IP/IPV4/IPV6/MultiPDP/FTP/HTTP/DNS/RNDIS/ECM/PPP/TLS/LBS/TTS/MQTT/WiFi Scan |
| 通讯方式       | UART 115200bps 8N1                                                              |
| RS485 IC       | SP3485EN-L/TR                                                                   |
| 输入电压       | Atom-Lite (DC 5V), RS485 侧输入 (DC 12V)                                        |
| 产品尺寸       | 64 x 24 x 29mm                                                                  |
| 产品重量       | 32.0g                                                                           |
| 包装尺寸       | 91 x 42 x 24.5mm                                                                |
| 毛重           | 47.0g                                                                           |

## 认证信息

### SIM-A7680C 模块认证

- 3C/SRRC/NAL/RoHS/REACH

## 原理图

<SchViewer>
<img src = "https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_cat1/atom_dtu_cat1_sch_01.webp" width="80%">
<img src = "https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_cat1/atom_dtu_cat1_sch_02.webp" width="80%">
</SchViewer>

## 管脚映射

::m5-bus-table
| PIN    | LEFT | RIGHT | PIN      |
| ------ | ---- | ----- | -------- |
|        |      | 1     | 3V3      |
| PORT.A | 2    | 3     | UART_RX  |
| PORT.A | 4    | 5     | UART_TX  |
| 5V     | 6    | 7     | RS485_RX |
| GND    | 8    | 9     | RS485_TX |
::

- SIM-A7680C

| Atom       | G22(TX) | G19(RX) | 5V  | GND |
| ---------- | ------- | ------- | --- | --- |
| SIM-A7680C | RX      | TX      | VIN | GND |

- RS485

| Atom  | G23 | G33 | 5V  | GND |
| ----- | --- | --- | --- | --- |
| RS485 | TX  | RX  | VIN | GND |

- I2C

| Atom | G25 | G21 | 5V  | GND |
| ---- | --- | --- | --- | --- |
| I2C  | SDA | SCL | VIN | GND |

## 数据手册

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
- [A76XX系列_云平台协议_应用文档_V1.01.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%E7%B3%BB%E5%88%97_%E4%BA%91%E5%B9%B3%E5%8F%B0%E5%8D%8F%E8%AE%AE_%E5%BA%94%E7%94%A8%E6%96%87%E6%A1%A3_V1.01.pdf)

## 软件开发

### Arduino

- Examples
  - [Atom DTU Cat1 MQTT Client](https://github.com/m5stack/ATOM_DTU_CAT1/tree/master/examples/MQTT)
  - [Atom DTU Cat1 ModBus RTU Master](https://github.com/m5stack/ATOM_DTU_CAT1/tree/master/examples/Modbus/ModBus-RTU/Master)
  - [Atom DTU Cat1 ModBus RTU Slave](https://github.com/m5stack/ATOM_DTU_CAT1/tree/master/examples/Modbus/ModBus-RTU/Slave)
- Libraries
  - [ArduinoModbus](https://github.com/m5stack/ArduinoModbus)
  - [Arduino485](https://github.com/m5stack/ArduinoRS485)
  - [TinyGSM](https://github.com/vshymanskyy/TinyGSM)
  - [PubSubClient](https://github.com/knolleary/pubsubclient.git)

### UiFlow1

- [Atom DTU Cat1 UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/dtu_cat1)

### 通信协议

- [A76XX Series MQTT_EX_AT Command Manual_V1.00.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series%20MQTT_EX_AT%20Command%20Manual_V1.00.pdf)
- [A76XX Series_AT_Command_Manual_V1.06.pdf](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/sim7680/A76XX%20Series_AT_Command_Manual_V1.06.pdf)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_DTU_CAT1_VIDEO.mp4" type="video/mp4">
</video>

## 版本变更

| 上市日期 | 产品变动 | 备注                           |
| -------- | -------- | ------------------------------ |
| 2023.7   | 增加 SKU | 不搭配主机 Atom-Lite, 优化电路 |
| -------  | 首次发售 | /                              |
