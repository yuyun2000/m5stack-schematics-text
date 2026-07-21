# Unit LoRaWAN-EU868

<span class="product-sku">SKU:U184-EU868</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-EU868/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-EU868/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-EU868/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-EU868/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-EU868/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-EU868/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-EU868/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-EU868/10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/695/U184-EU868_Weight.jpg">
</PictureViewer>

## 描述

**Unit LoRaWAN-EU868** 是一款基于 LoRa 技术的 LoRaWAN 通讯模块，专为 EU868 频段设计，适用于欧洲及其他使用 EU868 频段的地区。该模块采用 **STM32WLE5** 方案，支持远距离通信，兼具低功耗与高灵敏度特性。模组内置 LoRaWAN 协议栈，支持 **Class A、Class B 和 Class C** 三种工作模式配置，模块还支持点对点 (P2P) 通信模式，并采用 UART 通信接口 (使用 AT 指令集进行控制) 实现灵活配置。此外，该产品采用高性能 **胶棒天线**，天线结构优化设计，可提供更稳定的信号覆盖与更长的通信距离，适用于多种复杂环境。该模块可作为采集节点接入网关，用于数据收集与管理，或在无需网关的场景中实现设备间直接通信，适用于智慧农业、工业监测、环境监测节点部署等长距离、低功耗的物联网通信场景。

## 产品特性

- 遵循 LoRaWAN® 1.0.3 协议
- 支持 EU868 频段
- 支持 LoRa® P2P (点对点) 通信
- LoRaWAN 激活模式：OTAA，ABP
- 串口通信 (AT 指令)
- 采用高灵敏度 胶棒天线
- 低功耗
- 兼容乐高孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit LoRaWAN-EU868
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 胶棒天线 (@2.8dBi 总长 195mm SMA 内针)

## 应用场景

- 智慧农业
- 工业监测
- 环境监测节点部署

## 规格参数

| 规格             | 参数                                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| LoRa 方案        | STM32WLE5 @256 KB 闪存，64 KB RAM                                                                                               |
| 支持频段         | EU868 (863-870 MHz)                                                                                                             |
| 协议支持         | LoRaWAN® 1.0.3 协议 (Class A、Class B、Class C)                                                                                 |
| 接收灵敏度       | -137 dBm                                                                                                                        |
| LoRaWAN 激活模式 | OTAA，ABP                                                                                                                       |
| 通信模式         | LoRaWAN 和点对点 (P2P)                                                                                                          |
| 通讯距离 (P2P)   | 2300m (125Kbps)，1300m (500Kbps)                                                                                                |
| 接口类型         | UART 串口 @默认波特率 115200，支持 AT 指令                                                                                      |
| 天线类型         | 高性能胶棒天线，50 欧姆阻抗 @2.8dBi 总长 195mm SMA 内针                                                                         |
| 待机功耗         | 空闲状态：DC 5V/7.23mA<br/>休眠状态：DC 5V/28.61uA                                                                              |
| 工作电流         | (500Kbps) 数据接收：DC 5V/9.20mA<br/>数据发送：DC 5V/11.36mA<br/> (125Kbps) 数据接收：DC 5V/8.43mA<br/>数据发送：DC 5V/117.16mA |
| 工作温度         | 0 ~ 40°C                                                                                                                        |
| 产品尺寸         | 71.4 x 24.0 x 8.0mm                                                                                                             |
| 产品重量         | 11.9g                                                                                                                           |
| 包装尺寸         | 243.0 x 93.0 x 9.0mm                                                                                                            |
| 毛重             | 38.6g                                                                                                                           |

## 操作说明

LoRaWAN 工作模式对比

| 模式    | 下行实时性 | 功耗 | 应用场景                     |
| ------- | ---------- | ---- | ---------------------------- |
| Class A | 最低       | 最低 | 周期性数据上传，低功耗传感器 |
| Class B | 中等       | 中等 | 定时控制设备                 |
| Class C | 最高       | 最高 | 实时控制设备，如工业自动化   |

## 认证信息

- [RAK3172 Module Certification Information](https://downloads.rakwireless.com/#LoRa/RAK3172/Certification)

## 原理图

- [Unit LoRaWAN-EU868原理图PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/Sch_UNIT-LoRaWAN-RAK.pdf)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/schematic.png" width="100%">

## 管脚映射

### Unit LoRaWAN-EU868

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/model%20size.jpg" width="100%">

## 数据手册

- [Unit LoRaWAN-EU868 数据手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/data%20sheet.pdf)

## 软件开发

### Arduino

- [Unit LoRaWAN-EU868 Arduino 驱动库](https://github.com/m5stack/M5-LoRaWAN-RAK)

### UiFlow1

coming soon...

### UiFlow2

coming soon...

### 通信协议

- [Unit LoRaWAN-EU868 AT命令手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/AT%20command%20manual.pdf)

## 相关视频

- Unit LoRaWAN-EU868 产品介绍和案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-US915/LoRaWAN%20Video.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比表       | [Unit LoRaWAN-EU868](/zh_CN/unit/Unit%20LoRaWAN-EU868) ![Unit LoRaWAN-EU868](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-EU868/8.webp)                         | [Unit LoRaWAN 868MHz](/zh_CN/unit/lorawan868) ![Unit LoRaWAN 868MHz](https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan868/lorawan868_02.webp)                         |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 芯片模组         | STM32WLE5                                                                                                                                                                                                  | ASR6501                                                                                                                                                                                |
| 接收灵敏度       | 最低 -137 dBm                                                                                                                                                                                              | 最低 -137 dBm                                                                                                                                                                          |
| 接口类型         | UART@波特率默认：115200                                                                                                                                                                                    | UART@波特率默认：115200                                                                                                                                                                |
| LoRaWAN 协议版本 | LoRaWAN 1.0.3，支持 Class A/B/C                                                                                                                                                                            | LoRaWAN 1.0.1，支持 Class A/C                                                                                                                                                          |
| 发射功率         | 最大 22 dBm                                                                                                                                                                                                | 最大 21 dBm                                                                                                                                                                            |
| 协议栈支持       | LoRaWAN 协议栈内置                                                                                                                                                                                         | LoRaWAN 协议栈内置                                                                                                                                                                     |
| 通信模式         | LoRaWAN 和点对点 (P2P)                                                                                                                                                                                     | LoRaWAN                                                                                                                                                                                |
::
