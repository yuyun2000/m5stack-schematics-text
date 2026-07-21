# Atom DTU LoRaWAN470

<span class="product-sku">SKU:K062</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_lorawan470/atom_dtu_lorawan470_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_lorawan470/atom_dtu_lorawan470_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_lorawan470/atom_dtu_lorawan470_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_lorawan470/atom_dtu_lorawan470_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_lorawan470/atom_dtu_lorawan470_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_lorawan470/atom_dtu_lorawan470_06.webp">
</PictureViewer>

## 教程 & 快速上手

learn>| ![TTN(The Things Network)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lorawan/ttn_01.jpg) | [TTN(The Things Network)](/zh_CN/guide/lora/lorawan/ttn) | 本教程将向你说明如何在 TTN 中创建应用与节点设备并实现设备到云端的数据发送与接收。|

## 描述

**Atom DTU LoRaWAN470** 是一款适用于 470MHz 频率的 LoRaWAN 可编程数据传输单元 (DTU) 。模块采用 ASR6501 方案，支持远距离通信的同时兼具超低功耗与高灵敏度特性。模组集成 LoRaWAN 协议栈，采用串口通信接口 (使用 AT 指令集进行控制) ，使用时可作为采集节点大量接入网关进行数据收集管理。集成 SMA 外部天线接口，提升设备通信质量与信号的稳定性。与一般仅具备数据透传功能的 DTU 不同，**Atom DTU LoRaWAN470** 系列采用更为开放的架构设计。控制器 Atom-Lite 可根据实际业务随意修改程序，整机预留多种接口 (RS485, I2C, 自定义接口) 供用户拓展，便于传感器与执行器的快速接入。自带导轨夹持结构，完美嵌入到各类工业控制现场。

## 产品特性

- ASR6501
- 工作频率：470MHz
- 串行通信：UART 115200bps (AT 指令)
- 具备超强的抗干扰能力，能够在复杂干扰环境下正常工作
- RS485 通信接口 (带 12V 输入接口，内部集成 DC-DC 降压 5V)
- Modbus Master/slave
- 信号接入能力强
- 外置天线：SMA 天线接口
- Grove 拓展接口:
  - I2C x1
  - 自定义 x1
- 自带导轨夹持

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic DTU LoRaWAN470 Base
- 1 x SMA 天线
- 1 x SMA 红色帽
- 1 x M2 六角扳手
- 1 x M2x16 螺丝
- 1 x HT3.96-4P 端子

## 应用场景

- 自动远程抄表
- 智能交通智能停车场
- 远程灌溉及环境监测

## 规格参数

| 规格           | 参数                      |
| -------------- | ------------------------- |
| 通信芯片       | ASR6501                   |
| 工作频率       | 470MHz                    |
| LoRaWAN 版本   | v1.0.1                    |
| 最小接收灵敏度 | -137dBm (SF=12/BW=125KHz) |
| 最大发射功率   | +21dBm                    |
| 通讯方式       | UART 115200bps            |
| 产品尺寸       | 64 x 24 x 29mm            |
| 产品重量       | 32.0g                     |
| 包装尺寸       | 91 x 42 x 24.5mm          |
| 毛重           | 40.0g                     |

## 操作说明

### 470Mhz 支持的主要国家及地区

**中国**

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan470/lorawan470_support_area.webp">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_lorawan470/atom_dtu_lorawan470_sch_01.webp" width="80%">

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

- LoRaWAN470

| Atom       | G22(TX) | G19(RX) | 5V  | GND |
| ---------- | ------- | ------- | --- | --- |
| LoRaWAN470 | RX      | TX      | VIN | GND |

- RS485

| Atom  | G23 | G33 | 5V  | GND |
| ----- | --- | --- | --- | --- |
| RS485 | TX  | RX  | VIN | GND |

- I2C

| Atom | G25 | G21 | 5V  | GND |
| ---- | --- | --- | --- | --- |
| I2C  | SDA | SCL | VIN | GND |

## 数据手册

- [LoRaWAN 区域参数](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/lorawantm_regional_parameters_v1.1rb_-_final.pdf)

## 软件开发

### Arduino

- Examples
  - [Atom DTU LoRaWAN ABP Example](https://github.com/m5stack/ATOM_DTU_LoRaWAN/tree/master/examples/LoRaWAN_ABP)
  - [Atom DTU LoRaWAN OTAA Example](https://github.com/m5stack/ATOM_DTU_LoRaWAN/tree/master/examples/LoRaWAN_OTAA)
  - [Atom DTU LoRaWAN ModBus RTU Master Example](https://github.com/m5stack/ATOM_DTU_LoRaWAN/tree/master/examples/Modbus/ModBus-RTU/Master)
  - [Atom DTU LoRaWAN ModBus RTU Slave Example](https://github.com/m5stack/ATOM_DTU_LoRaWAN/tree/master/examples/Modbus/ModBus-RTU/Slave)
  - [Atom DTU LoRaWAN - Send Msg to Gateway](https://github.com/m5stack/ATOM_DTU_LoRaWAN)
- Libraries
  - [ArduinoModbus Library](https://github.com/m5stack/ArduinoModbus)
  - [Arduino485 Library](https://github.com/m5stack/ArduinoRS485)
  - [UNIT_LoRaWAN Library](https://github.com/m5stack/UNIT_LoRaWAN)
  - [M5Atom Library](https://github.com/m5stack/M5Atom)
  - [FastLED Library](https://github.com/FastLED/FastLED)

### UiFlow1

- [Atom DTU LoRaWAN470 UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/dtu_lorawan_470)
- [Atom DTU LoRaWAN470 UiFlow OTAA Example](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/m5f/DTU/atom_dtu_lorawan_470_uiflow_example_01.m5f)

### 通信协议

- [COM.LoRaWAN470 AT指令集](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/COM.LoRaWAN.Ra-07.asr6501-asr6502-at-commands-introduction-v4.3.pdf)
