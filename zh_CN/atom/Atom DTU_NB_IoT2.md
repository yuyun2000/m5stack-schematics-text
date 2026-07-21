# Atom DTU NBIoT2

<span class="product-sku">SKU:K059-B</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/16.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/13.webp">
</PictureViewer>

## 描述

**Atom DTU NBIoT2** 是一款适用于全球 Cat-NB 频段的 NB-IoT 可编程无线数据传输单元 (DTU)。内置 SIM7028 通讯模组，采用串口通信（通过 AT 指令集控制），集成 SMA 外部天线接口，显著提升设备的通信质量与信号稳定性。SIM7028 模块覆盖多数 Cat-NB 频段，确保在全球范围内的适用性。与一般仅具备数据透传功能的 DTU 不同，Atom DTU 系列采用更为开放的架构设计。控制器 AtomS3-Lite 可根据实际业务随意修改程序，整机预留多种接口（RS485、I2C、自定义接口）供用户拓展，便于传感器与执行器的快速接入。自带导轨夹持结构，完美嵌入到各类工业控制现场。**Atom DTU NBIoT2** 非常适合应用在各种低延迟、低吞吐量应用场景，如远程控制、资产跟踪、远程监控、远程医疗、共享单车等。

## 产品特性

- Global 版本 / 多频段支持
- 信号接入能力强
- AT 指令控制
- SIM 卡类型: Micro SIM
- 外置天线：SMA 天线
- 串行通信：UART 115200bps
- 数据传输 (kbps):127 (DL)/159 (UL)
- 支持多种网络协议
- 无线电、环保、运营商等多重标准认证
- 多种供电方式

## 包装内容

- 1 x AtomS3-Lite
- 1 x Atom DTU NBIoT2
- 1 x 胶棒天线 (2.5dBi 总长 110mm SMA 内针)
- 1 x SMA 天线红色帽
- 1 x M2 六角扳手
- 1 x M2x16 螺丝
- 1 x HT3.96-4P 端子

## 应用场景

- 资产跟踪
- 远程监控 / 控制
- 共享单车

## 规格参数

| 规格               | 参数                                                                  |
| ------------------ | --------------------------------------------------------------------- |
| 通信模组           | SIM7028                                                               |
| 支持 Cat-NB 频段   | B1/B2/B3/B4/B5/B8/B12/B13/B14/B17/B18/B19/B20/B25/B26/B28/B66/B70/B85 |
| 网络协议           | TCP/UDP/HTTP/TLS\*/DTLS\*/DNS/NTP/PING/LWM2M/COAP\*/MQTT/MQTTS/SSL    |
| 运营商认证         | Deutsche Telekom/Vodafone/Telefonica/ 中国电信 / 中国移动 / 中国联通  |
| 通讯方式           | UART 115200bps                                                        |
| 天线               | 胶棒天线 @2.5dBi 总长 110mm SMA 内针                                  |
| 供电方式           | RS485 端口 (HT396 接口 9-24V)<br/>USB 5V                              |
| Grove 接口带载能力 | DC 5V/0.9A                                                            |
| 工作温度           | 0 ~ 40°C                                                              |
| 产品尺寸           | 65.3 x 28.7 x 24mm                                                    |
| 产品重量           | 24.6g                                                                 |
| 包装尺寸           | 168 x 117 x 19.7mm                                                    |
| 毛重               | 38.7g                                                                 |

### RS485 通讯测试

- 测试条件：AB 加上 120Ω 终端电阻

| 通讯距离 | 数据速率                                                 |
| -------- | -------------------------------------------------------- |
| 5 米     | 最大数据速率 750Kbps，接收发送正常，丢包率 0%，错误率 0% |
| 20 米    | 最大数据速率 750Kbps，接收发送正常，丢包率 0%，错误率 0% |
| 50 米    | 最大数据速率 750Kbps，接收发送正常，丢包率 0%，错误率 2% |
| 100 米   | 最大数据速率 512Kbps，接收发送正常，丢包率 0%，错误率 0% |

### 功耗测试

| 参数类别                     | 规格参数                                                   |
| ---------------------------- | ---------------------------------------------------------- |
| 待机电流 (带 Atom-Lite 主机) | DC 9V@36.00mA <br/> DC 12V@28.95mA <br/> DC 24V@17.00mA    |
| 工作电流 (带 Atom-Lite 主机) | DC 9V@58.81.00mA <br/> DC 12V@48.52mA <br/> DC 24V@25.00mA |

## 认证信息

### 无线电和通信设备认证

- **SRRC**,**NAL**,**CE-RED**,**GCF**,**CCC**

### 安全和环境认证

- **CCC**,**RoHS**,**REACH**

### 运营商认证

- **Deutsche Telekom**,**Vodafone**,**Telefonica**,**中国电信**,**中国移动**,**中国联通**

## 原理图

- [Atom DTU NBIoT2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/542/SCH_AtomNB-DTU2_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/542/SCH_AtomNB-DTU2_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

::m5-bus-table
| PIN    | LEFT | RIGHT | PIN            |
| ------ | ---- | ----- | -------------- |
|        |      | 1     | 3V3            |
| PORT.A | 2    | 3     | NBIoT2_UART_RX |
| PORT.A | 4    | 5     | NBIoT2_UART_TX |
| 5V     | 6    | 7     | RS485_TX       |
| GND    | 8    | 9     | RS485_RX       |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 数据手册

- [SIM7028_Specification](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028_%E4%BA%A7%E5%93%81%E8%A7%84%E6%A0%BC%E4%B9%A6_20211215.pdf>)
- [SIM7028 Series_Network Searching_Application Note_V1.00](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028%20Series_Network%20Searching_Application%20Note_V1.00.pdf>)
- [SIM7028 Series_Low Power Mode_Application Note_V1.01](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028%20Series_Low%20Power%20Mode_Application%20Note_V1.01.pdf>)
- [SIM7028_NCC_Certificate_20230421](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028_NCC_%E8%AF%81%E4%B9%A6_20230421.pdf>)
- [SIM7028 Series_TCPIP_Application Note_V1.04](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028%20Series_TCPIP_Application%20Note_V1.04.pdf>)
- [SIM7028 Series_SSL_Application Note_V1.00](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028%20Series_SSL_Application%20Note_V1.00.pdf>)
- [SIM7028 Series_MQTT(S)_Application Note_V1.03](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028%20Series_MQTT(S)_Application%20Note_V1.03.pdf>)
- [SIM7028 Series_LwM2M_Application Note_V1.02](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028%20Series_LwM2M_Application%20Note_V1.02.pdf>)
- [SIM7028 Series_HTTP(S)_Application Note_V1.04](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028%20Series_HTTP(S)_Application%20Note_V1.04.pdf>)
- [SIM7028 Series_FOTA_Application Note_V1.00](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028%20Series_FOTA_Application%20Note_V1.00.pdf>)
- [SIM7028 Series_COAP_Application Note_V1.00](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028%20Series_COAP_Application%20Note_V1.00.pdf>)
- [NB-EVB_User_Guide_Manual_V1.00](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/NB-EVB_User_Guide_Manual_V1.00.pdf>)
- [RSU062-EE-EUT Photo-SIM7028](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/2307RSU062-EE-EUT%20Photo-SIM7028.pdf>)
- [RSU062-E6-CE EMC Test Report](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/2307RSU062-E6-CE%20EMC%20Test%20Report.pdf>)
- [RSU062-E5-3GPP (LTE Band 5) Test Report](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/2307RSU062-E5-3GPP%20(LTE%20Band%205)%20Test%20Report.pdf>)

## 软件开发

### Arduino

- [Atom DTU NBIoT2 Arduino 驱动库](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/542/ATOM_DTU_NB2_ARDUINO.zip)

- 下载库文件，手动添加至 Arduino 库文件夹路径，或通过 Arduino IDE 直接导入。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/ea27b454819858ec750081252272052.png" width="30%" />

### UiFlow2

- [Atom DTU NBIoT2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/dtu_nbiot2.html)

### PlatformIO

- [Atom DTU NBIoT2 Project Demo for PlatformIO](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/542/ATOM_DTU_NB2_PIO.zip)

- 在`platformio.ini`文件中指定依赖库版本。

```bash
lib_deps =
    m5stack/M5Unified@^0.1.13
	m5stack/M5AtomS3@^1.0.0
	fastled/FastLED@^3.6.0
	knolleary/PubSubClient@^2.8
	vshymanskyy/StreamDebugger@^1.0.1
	https://github.com/m5stack/TinyGSM/archive/refs/tags/v0.12.0-patch-1.zip
	arduino-libraries/ArduinoHttpClient@^0.6.0
	bakercp/CRC32@^2.0.0
```

### 通信协议

- [SIM7028 Series_AT Command Manual_V1.00](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028%20Series_AT%20Command%20Manual_V1.00.pdf>)

## 相关视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/719dbbd4009f13a6893266f53b301f71.mp4" type="video/mp4"></video>

## 产品对比

| 产品             | SKU    | 模组                                     | Cat-NB 频段                                                                                                     | 数据传输速率                                        | 通信协议                                                                           |
| ---------------- | ------ | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Atom DTU-NB-IoT  | K059   | <span style="color:red;">SIM7020G</span> | B1/B2/B3/B4/B5/B8/B12/<br/>B13/B17/B18/B19/B20/B25/B26<br/>/B28/B66/B70/<span style="color:red;">B71</span>/B85 | <span style="color:red;">126 (DL) / 150 (UL)</span> | TCP/UDP/HTTP/HTTPS/TLS\*/<br/>DTLS\*/DNS/NTP/PING/LWM2M/<br/>COAP\*/MQTT/MQTTS/SSL |
| Atom DTU-NB-IoT2 | K059-B | <span style="color:red;">SIM7028</span>  | B1/B2/B3/B4/B5/B8/B12/<br/>B13/<span style="color:red;">B14</span>/B17/B18/B19/B20/B25/<br/>B26/B28/B66/B70/B85 | <span style="color:red;">127 (DL) / 159 (UL)</span> | TCP/UDP/HTTP/HTTPS/TLS\*/<br/>DTLS\*/DNS/NTP/PING/LWM2M/<br/>COAP\*/MQTT/MQTTS/SSL |

\#> 区别概况 | SIM7028 和 SIM7020G 的主要区别在于频段支持和数据传输速率。SIM7028 支持更多的频段和稍高的数据传输速率，适用于更多市场和更高带宽需求的应用。而 SIM7020G 虽然频段支持稍少，但也覆盖了大部分市场，适用于一般物联网应用。两者在网络协议和功能特性上较为相似，以及广泛的国际和运营商认证。
