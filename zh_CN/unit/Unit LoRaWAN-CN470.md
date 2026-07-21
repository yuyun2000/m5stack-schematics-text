# Unit LoRaWAN-CN470

<span class="product-sku">SKU:U184-CN470</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/10.webp">
</PictureViewer>

## 描述

**Unit LoRaWAN-CN470** 是一款基于 LoRa 技术的 LoRaWAN 通讯模块，专为 CN470 频段设计，适用于中国及其他使用 CN470 频段的地区。该模块采用 **STM32WLE5** 方案，支持远距离通信，兼具低功耗与高灵敏度特性。模组内置 LoRaWAN 协议栈，支持 **Class A、Class B 和 Class C** 三种工作模式配置，模块还支持点对点 (P2P) 通信模式，并采用 UART 通信接口 ( 使用 AT 指令集进行控制 ) 实现灵活配置。此外，该产品采用高性能 **胶棒天线**，天线结构优化设计，可提供更稳定的信号覆盖与更长的通信距离，适用于多种复杂环境。该模块可作为采集节点接入网关，用于数据收集与管理，或在无需网关的场景中实现设备间直接通信，适用于智慧农业、工业监测、环境监测节点部署等长距离、低功耗的物联网通信场景。

## 产品特性

- 遵循 LoRaWAN® 1.0.3 协议
- 支持 CN470 频段
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

- 1 x Unit LoRaWAN-CN470
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 胶棒天线 (@0.5dBi 总长 195mm SMA 内针)

## 应用场景

- 智慧农业
- 工业监测
- 环境监测节点部署

## 规格参数

| 规格             | 参数                                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| LoRa 方案        | STM32WLE5 @256 KB 闪存，64 KB RAM                                                                                               |
| 支持频段         | CN470 (470-510 MHz)                                                                                                             |
| 协议支持         | LoRaWAN® 1.0.3 协议 (Class A、Class B、Class C)                                                                                 |
| 接收灵敏度       | -137 dBm                                                                                                                        |
| LoRaWAN 激活模式 | OTAA，ABP                                                                                                                       |
| 通信模式         | LoRaWAN 和点对点 (P2P)                                                                                                          |
| 接口类型         | UART 串口 @默认波特率 115200，支持 AT 指令                                                                                      |
| 天线类型         | 高性能胶棒天线，50 欧姆阻抗 @0.5dBi 总长 195mm SMA 内针                                                                         |
| 通讯距离 (P2P)   | 2300m (125Kbps)，1300m (500Kbps)                                                                                                |
| 待机功耗         | 空闲状态：DC 5V/7.23mA<br/>休眠状态：DC 5V/28.61uA                                                                              |
| 工作电流         | (500Kbps) 数据接收：DC 5V/9.20mA<br/>数据发送：DC 5V/11.36mA<br/> (125Kbps) 数据接收：DC 5V/8.43mA<br/>数据发送：DC 5V/117.16mA |
| 工作温度         | 0 ~ 40°C                                                                                                                        |
| 产品尺寸         | 71.4 x 24.0 x 8.0mm                                                                                                             |
| 产品重量         | 28.8g                                                                                                                           |
| 包装尺寸         | 243.0 x 93.0 x 9.0mm                                                                                                            |
| 毛重             | 35.5g                                                                                                                           |

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

- [Unit LoRaWAN-CN470 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/Sch_UNIT-LoRaWAN-RAK.pdf)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/schematic.png" width="100%">

## 管脚映射

### Unit LoRaWAN-CN470

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/model%20size.jpg" width="100%">

## 数据手册

- [Unit LoRaWAN-CN470 数据手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/data%20sheet.pdf)

## 软件开发

### Arduino

- [Unit LoRaWAN-CN470 Arduino 驱动库](https://github.com/m5stack/M5-LoRaWAN-RAK)

### UiFlow1

coming soon...

### UiFlow2

coming soon...

### 通信协议

- [Unit LoRaWAN-CN470 AT 命令手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/AT%20command%20manual.pdf)

## 相关视频

- Unit LoRaWAN-CN470 产品介绍和案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-US915/LoRaWAN%20Video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113819535804254&bvid=BV1hXcyeuEaL&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/dhQtwxG1Sy0?si=NEU8eB0nY21RKDnG" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比表       | [Unit LoRaWAN-CN470](/zh_CN/unit/Unit%20LoRaWAN-CN470) ![Unit LoRaWAN-CN470](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/8.webp)                         | [Unit LoRaWAN470](/zh_CN/unit/lorawan470) ![Unit LoRaWAN470](https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan470/lorawan470_02.webp)                         |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 芯片模组         | STM32WLE5                                                                                                                                                                                                  | ASR6501                                                                                                                                                                        |
| 接收灵敏度       | 最低 -137 dBm                                                                                                                                                                                              | 最低 -137 dBm                                                                                                                                                                  |
| 接口类型         | UART @波特率默认：115200                                                                                                                                                                                   | UART@波特率默认：115200                                                                                                                                                        |
| LoRaWAN 协议版本 | LoRaWAN 1.0.3，支持 Class A/B/C                                                                                                                                                                            | LoRaWAN 1.0.1，支持 Class A/C                                                                                                                                                  |
| 发射功率         | 最大 22 dBm                                                                                                                                                                                                | 最大 21 dBm                                                                                                                                                                    |
| 协议栈支持       | LoRaWAN 协议栈内置                                                                                                                                                                                         | LoRaWAN 协议栈内置                                                                                                                                                             |
| 通信模式         | LoRaWAN 和点对点 (P2P)                                                                                                                                                                                     | LoRaWAN                                                                                                                                                                        |
::
