# IoTBase NBIoT

<span class="product-sku">SKU:K064</span>

## 描述

**IoTBase NBIoT** 是一款专门针对物联网 NB-IoT 数据传输场景设计的功能底座。套件配套强力核心主控 BASIC（内置 ESP32，集成 Wi-Fi），集成丰富的接口资源（I2C、UART、GPIO、RS485 等），适配多种工业现场常用协议（如 ModBus 等）。内置 SIM7020G 模组，覆盖多数 Cat-NB 频段，集成 SMA 外部天线接口，提升设备通信质量与信号的稳定性。配套多功能导轨固定底座，完美嵌入工业应用场景。

## 产品特性

- SIM7020G/Global 版本 / 多频段支持
- 信号接入能力强
- AT 指令控制
- SIM 卡类型: MicroSIM
- 外置天线：SMA 天线
- 串行通信：UART 115200bps
- RS485 通信接口 (带 12V 输入，内置 DC-DC 12V to 5v)
- 配套多功能导轨固定底板
- NB 模组状态指示灯
- 配套 BASIC 主机
- Grove 拓展接口:
  - I2C x1
  - GPIO x1
  - UART x1
- SIM 卡槽规格: MicroSIM
- Cat-NB 频段:
  - B1/B2/B3/B4/B5/B8/ B12/B13/B17/B18/B19/ B20/B25/B26/B28/ B66/B70/B71/B85
- 数据传输 (kbps):
  - 126(DL)/150(UL)
- 网络协议:
  - TCP/UDP/HTTP/HTTPS/ TLS/DTLS/DNS/NTP/ PING/LWM2M/COAP/ MQTT/MQTTS

## 包装内容

- 1 x IoTBase NBIoT
- 1 x BASIC 主控
- 1 x 12V DC 电源适配器
- 1 x VH-3.96-2P 端子
- 1 x VH-3.96-4P 端子
- 1 x Din-moute 导轨固定底板
- 1 x SMA 天线
- 2 x M3\*28 螺丝
- 1 x M3 六角扳手

## 应用场景

- 智能表计
- 远程监控
- 共享单车

## 规格参数

| 规格             | 参数                                                                     |
| ---------------- | ------------------------------------------------------------------------ |
| 通信模组         | SIM7020G                                                                 |
| 支持 Cat-NB 频段 | B1/B2/B3/B4/B5/B8/ B12/B13/B17/B18/B19/ B20/B25/B26/B28/ B66/B70/B71/B85 |
| 数据传输速度     | 126 (DL)/150 (UL)                                                        |
| 网络协议         | TCP/UDP/HTTP/HTTPS/ TLS/DTLS/DNS/NTP/ PING/LWM2M/COAP/ MQTT/MQTTS        |
| 接口资源         | I2C, UART, GPIO, RS485 (支持 ModBus Master/Slave)                        |
| 供电方式         | USB 供电 /12V DC 电源适配器供电                                          |
| 通讯方式         | UART 115200bps                                                           |
| 产品重量         | 71.3g                                                                    |
| 毛重             | 197g                                                                     |
| 产品尺寸         | 80 x 54 x 33mm                                                           |
| 包装尺寸         | 105.0 x 100.0 x 58mm                                                     |

## 认证信息

- RoHS/REACH/RCM/Telstra/CE(RED)/GCF/ATEX/TIM/Deutsche Telekom/Vodafone/FCC/PTCRB/T-Mobile/IC

### 运营商认证

- Telstra\*/Vodafone/Deutsche Telekom

## 原理图

<img src = "https://static-cdn.m5stack.com/resource/docs/products/base/iot_base_nb_cn/iot_base_nb_sch_01.webp" width="80%">

## 管脚映射

### RS485

| CORE  | G15 | G13 | 5V  | GND |
| ----- | --- | --- | --- | --- |
| RS485 | TX  | RX  | VIN | GND |

### SIM7020G

| CORE     | G0     | G35    | G12    |
| -------- | ------ | ------ | ------ |
| SIM7020G | NB-RXD | NB-TXD | PWRKEY |

### HY2.0-4P

| CORE     | G21 | G22 | 5V  | GND |
| -------- | --- | --- | --- | --- |
| I2C PORT | SDA | SCL | VIN | GND |

| CORE      | G17 | G16 | 5V  | GND |
| --------- | --- | --- | --- | --- |
| UART PORT | TX  | RX  | VIN | GND |

| CORE      | G36 | G26 | 5V  | GND |
| --------- | --- | --- | --- | --- |
| GPIO PORT | ADC | DAC | VIN | GND |

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

- [IoTBase NBIoT MQTT Client Example](https://github.com/m5stack/IoT_BASE_SIM7020/tree/master/examples/MQTT)

- [IoTBase NBIoT ModBus RTU Master Example](https://github.com/m5stack/IoT_BASE_SIM7020/tree/master/examples/Modbus/ModBus-RTU/Master)

- [IoTBase NBIoT ModBus RTU Slave Example](https://github.com/m5stack/IoT_BASE_SIM7020/tree/master/examples/Modbus/ModBus-RTU/Slave)

- [IoTBase NBIoT_Factory Test](https://github.com/m5stack/IoT_BASE_NB_FactoryTest)

- [ArduinoModbus Library](https://github.com/m5stack/ArduinoModbus)

- [Arduino485 Library](https://github.com/m5stack/ArduinoRS485)

- [TinyGSM Library](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/arduino/lib/TinyGSM.zip)

### UiFlow1

- [IoTBase NBIoT UiFlow1 文档](/zh_CN/uiflow/blockly/module/iot_base_nb)

### 通信协议

- [SIM7020 Series_AT Command Manual_V1.05](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/nbiot/SIM7020%20Series_AT%20Command%20Manual_V1.05.pdf)
