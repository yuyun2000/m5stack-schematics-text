# Atom DTU NBIoT-CN

<span class="product-sku">SKU:K060</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_nb_cn/atom_dtu_nb_cn_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_nb_cn/atom_dtu_nb_cn_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_nb_cn/atom_dtu_nb_cn_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_nb_cn/atom_dtu_nb_cn_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_nb_cn/atom_dtu_nb_cn_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_nb_cn/atom_dtu_nb_cn_06.webp">
</PictureViewer>

## 描述

**Atom DTU NBIoT-CN** 是一款集成 NB-IoT 通信功能的可编程数据传输单元 (DTU) 。内置 SIM7020C 模组，覆盖多数 Cat-NB 频段，集成 SMA 外部天线接口，提升设备通信质量与信号的稳定性。与一般仅具备数据透传功能的 DTU 不同，**Atom DTU NBIoT-CN** 系列采用更为开放的架构设计。控制器 Atom-Lite 可根据实际业务随意修改程序，整机预留多种接口 (RS485, I2C, 自定义接口) 供用户拓展，便于传感器与执行器的快速接入。自带导轨夹持结构，完美嵌入到各类工业控制现场。**Atom DTU NBIoT-CN** 非常适合应用在各种低延迟、低吞吐量应用场景 (如远程控制、资产跟踪、远程监控、远程医疗、共享单车等) 。

## 产品特性

- SIM7020C / 适用于中国地区
- RS485 通信接口 (带 12V 输入接口，内部集成 DC-DC 降压 5V)
- Modbus Master/slave
- 信号接入能力强
- AT 指令控制
- SIM 卡类型: MicroSIM
- 外置天线：SMA 天线接口
- Grove 拓展接口:
  - I2C x1
  - 自定义 x1
- 串行通信：UART 115200bps
- 自带导轨夹持
- Cat-NB 频段:
  - B1/B3/B5/B8
- 数据传输 (kbps):
  - 26.15(DL)/62.5(UL)
- 网络协议:
  - TCP/UDP/LWM2M/COAP/ MQTT/HTTP/HTTPS/ TLS/DTLS/DNS/NTP/ PING/OneNET/ 电信云 / 艾拉云

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic DTU NBIoT-CN Base
- 1 x SMA 天线
- 1 x SMA 红色帽
- 1 x M2 六角扳手
- 1 x M2x16 螺丝
- 1 x HT3.96-4P 端子
- 1 x NB-IoT 流量卡 (移动 NB 流量：300M)

## 应用场景

- 智能表计
- 远程监控
- 共享单车

## 规格参数

| 规格             | 参数                                                                                |
| ---------------- | ----------------------------------------------------------------------------------- |
| 通信模组         | SIM7020C                                                                            |
| 支持 Cat-NB 频段 | B1/B3/B5/B8                                                                         |
| 网络协议         | TCP/UDP/LWM2M/COAP/ MQTT/HTTP/HTTPS/ TLS/DTLS/DNS/NTP/ PING/OneNET/ 电信云 / 艾拉云 |
| 通讯方式         | UART 115200bps                                                                      |
| 产品尺寸         | 64 x 24 x 29mm                                                                      |
| 产品重量         | 32g                                                                                 |
| 包装尺寸         | 91 x 42 x 24.5mm                                                                    |
| 毛重             | 40g                                                                                 |

## 认证信息

- RoHS/REACH/CCC/CTA/SRRC/Mobile/Unicom/Telecom/ATEX

### 运营商认证

- 中国电信 / 中国联通 / 中国移动

## 原理图

<img src = "https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_nb/atom_dtu_nb_sch_01.webp" width="80%">

## 管脚映射

- SIMCOM7020C

| Atom        | G22(TX) | G19(RX) | 5V  | GND |
| ----------- | ------- | ------- | --- | --- |
| SIMCOM7020C | RX      | TX      | VIN | GND |

- RS485

| Atom  | G23 | G33 | 5V  | GND |
| ----- | --- | --- | --- | --- |
| RS485 | TX  | RX  | VIN | GND |

- I2C

| Atom | G25 | G21 | 5V  | GND |
| ---- | --- | --- | --- | --- |
| I2C  | SDA | SCL | VIN | GND |

## 数据手册

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

## 软件开发

### Arduino

- Examples
  - [Atom DTU NBIoT-CN MQTT Client Example](https://github.com/m5stack/ATOM_DTU_NB/tree/master/examples/MQTT)
  - [Atom DTU NBIoT-CN HTTP Client Example](https://github.com/m5stack/ATOM_DTU_NB/tree/master/examples/HTTP)
  - [Atom DTU NBIoT-CN ModBus RTU Master Example](https://github.com/m5stack/ATOM_DTU_NB/tree/master/examples/Modbus/ModBus-RTU/Master)
  - [Atom DTU NBIoT-CN ModBus RTU Slave Example](https://github.com/m5stack/ATOM_DTU_NB/tree/master/examples/Modbus/ModBus-RTU/Slave)
- Libraries
  - [ArduinoModbus Library](https://github.com/m5stack/ArduinoModbus)
  - [Arduino485 Library](https://github.com/m5stack/ArduinoRS485)
  - [TinyGSM Library](https://github.com/vshymanskyy/TinyGSM)
  - [PubSubClient Library](https://github.com/knolleary/pubsubclient.git)
  - [ArduinoHttpClient Library](https://github.com/arduino-libraries/ArduinoHttpClient)

### UiFlow1

- [Atom DTU NBIoT-CN UiFlow1 文档](/zh_CN/uiflow/blockly/atomic_base/dtu_nb_iot)

- [Atom DTU NBIoT-CN MQTT 测试程序](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/m5f/DTU/ATOM-DTU-NB-MQTT.m5f)

\#> 案例描述 | 连接 MQTT 服务器，实行消息订阅与发布，当接收到新的订阅消息时，会调用 callback 函数并传递 topic 名称和数据内容，输出结果将打印到 USB 串口。

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_nb/atom_dtu_nb_uiflow_06.webp" width="30%">

### 通信协议

- [SIM7020 Series_AT Command Manual_V1.05](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_AT%20Command%20Manual_V1.05.pdf)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOMDTU_NB-IOT_VIDEO.mp4" type="video/mp4">
</video>
