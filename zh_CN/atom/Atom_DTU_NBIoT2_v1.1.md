# Atom DTU NBIoT2 v1.1

<span class="product-sku">SKU:A106-V21</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_01.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_02.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_03.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_04.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_05.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_06.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_07.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_08.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_09.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_10.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_11.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_12.jpg">
</PictureViewer>

## 描述

**Atom DTU NBIoT2 v1.1** 是一款适用于全球 Cat-NB 频段的 NB-IoT 可编程无线数据传输单元 (DTU)，在上一代产品基础上进行了升级，主要增加了 IO 拓展芯片，实现对通信模组电源使能与软件复位的控制，可以减少功耗，以及保证在模块出现异常的状况下，无需断电即可完成 SIM 模组复位。同时，新增 ADC 监测电路，支持实时采集 HT3.96-4P 接口输入的电源电压，实现电源状态监控。
本单元内置 SIM7028 通讯模组，采用串口通信（通过 AT 指令集控制），集成 SMA 外部天线接口，具有良好的通信质量与信号稳定性。SIM7028 模块覆盖多个 Cat-NB 频段，能在全球范围内适用。与一般仅具备数据透传功能的 DTU 相比，Atom DTU 系列采用更为开放的架构设计，整机预留多种接口（RS485、I2C / 自定义 Grove 接口）供用户拓展，便于传感器与执行器的快速接入；自带的导轨夹持结构可嵌入到各类工业控制现场，适合应用在各种低延迟、低吞吐量场景，如远程控制、资产跟踪、远程监控、远程医疗、共享单车等。

## 产品特性

- Global 版本 / 多频段支持，全球范围内适用
- SIM7028 模组，AT 指令控制
- Micro-SIM 物联卡
- IO 拓展芯片控制通信模组电源使能与软件复位
- ADC 监测电路，支持电源状态监控
- 外置 SMA 天线接口
- 预留 RS485、I2C / 自定义 Grove 接口
- 数据传输速率 (kbps): 127 (DL) / 159 (UL)
- 支持 MQTT、HTTP 等多种网络协议
- 多种供电方式

## 包装内容

- 1 x Atom DTU NBIoT2 v1.1
- 1 x 850 ~ 1900 MHz SMA 胶棒天线
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)
- 1 x M2 \* 16mm 螺丝 (杯头，机械牙)
- 1 x HT3.96-4P 端子
- 1 x I/O 贴纸

## 应用场景

- 资产跟踪
- 远程监控 / 控制
- 共享单车

## 规格参数

| 规格               | 参数                                                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| 通信模组           | SIM7028                                                                                                             |
| 支持 Cat-NB 频段   | B1/B2/B3/B4/B5/B8/B12/B13/B14/B17/B18/B19/B20/B25/B26/B28/B66/B70/B85                                               |
| 网络协议           | TCP/UDP/HTTP/TLS/DTLS/DNS/NTP/PING/LWM2M/COAP/MQTT/MQTTS/SSL                                                        |
| 运营商             | Deutsche Telekom / Vodafone / Telefonica / 中国电信 / 中国移动 / 中国联通                                           |
| 通讯方式           | UART 115200bps @ 8N                                                                                                 |
| IO 拓展管理芯片    | M5IOE1                                                                                                              |
| 天线规格           | 尺寸 108 x 10mm，接口类型 SMA（内螺内孔），工作频段 850 ~ 1900 MHz，增益 2.0 士 05，驻波比 ≤ 3.0                    |
| 供电方式           | RS485 端口（HT3.96R-4P 接口）：9~24V                                                                                |
| 功耗               | SIM 模组断电：24V@9mA（RS485 供电）<br> 待机：5V@8.82mA<br> 工作（连续收发数据）：5V@43.91mA                        |
| Grove 接口带载能力 | DC 5V@1.3A（RS485 供电）                                                                                            |
| 工作温度           | 0°C ~ 40°C                                                                                                          |
| 安装方式           | DIN 导轨安装 / 挂孔                                                                                                 |
| 产品尺寸           | 64.3 x 24.0 x 28.7mm                                                                                                |
| 产品重量           | 30.0g                                                                                                               |
| 包装尺寸           | 170.0 x 120.0 x 27.0mm                                                                                              |
| 毛重               | 51.2g                                                                                                               |

### RS485 通讯测试

- 测试条件：AB 加上 120Ω 终端电阻

| 通讯距离 | 数据速率                                                 |
| -------- | -------------------------------------------------------- |
| 100 米   | 最大数据速率 512Kbps，接收发送正常，丢包率 0%，错误率 0% |

## 原理图

- [Atom DTU NBIoT2 v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/SCH_Atom_DTU_NBIoT_v1.1_2025_11_06_19_20_28.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/SCH_Atom_DTU_NBIoT_v1.1_2025_11_06_19_20_28_page_01.png">
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

- [Atom DTU NBIoT2 v1.1模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-atomdtu.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-atomdtu_page_01.png" width="100%">

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

- [Atom DTU NBIoT2 v1.1 Arduino 快速上手](/zh_CN/arduino/projects/atom_dtu/atom_dtu_nblot2_v1.1)
- [Atom DTU NBIoT2 v1.1 Arduino IO拓展驱动库](https://github.com/m5stack/M5IOE1)
- [TinyGSM 驱动库](https://github.com/m5stack/TinyGSM)

### UiFlow2

- [Atom DTU NBIoT2 v1.1 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/base/dtu_nbiot2v11.html)

### 通信协议

- [M5IOE1 IO拓展管理芯片](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/IO_Expander_Datasheet_CN.pdf)
- [SIM7028 Series_AT Command Manual_V1.00](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20NB-IoT2%20(SIM7028)/SIM7028%20Series_AT%20Command%20Manual_V1.00.pdf>)

## 相关视频

- Atom DTU NBIoT2 v1.1 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21_Atom_DTU_NBoT2_v1.1_video_ZH.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 产品对比表         | [Atom DTU NBIoT2 v1.1](/zh_CN/atom/Atom_DTU_NBIoT2_v1.1) ![Atom DTU NBIoT2 v1.1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_02.jpg) | [Atom DTU NBIoT2](/zh_CN/atom/Atom%20DTU_NB_IoT2) ![Atom DTU NBIoT2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atom%20DTU-NB-IoT2/11.webp) | [Atom DTU NBIoT](/zh_CN/atom/atom_dtu_nb) ![Atom DTU NBIoT](https://static-cdn.m5stack.com/resource/docs/products/atom/atom_dtu_nb/atom_dtu_nb_02.webp) |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 套装包含 Atom 主控 | <mark>不包含</mark>                                                                                                                                                   | <mark>AtomS3-Lite</mark>                                                                                                                                                  | <mark>Atom-Lite</mark>                                                                                                                                  |
| 通信模组           | <mark>SIM7028</mark>                                                                                                                                                  | <mark>SIM7028</mark>                                                                                                                                                      | <mark>SIM7020G</mark>                                                                                                                                   |
| Cat-NB 频段        | B1/B2/B3/B4/B5/B8/B12/<br/>B13/<mark>B14</mark>/B17/B18/B19/B20/B25/<br/>B26/B28/B66/B70/B85                                                                          | B1/B2/B3/B4/B5/B8/B12/<br/>B13/<mark>B14</mark>/B17/B18/B19/B20/B25/<br/>B26/B28/B66/B70/B85                                                                              | B1/B2/B3/B4/B5/B8/B12/<br/>B13/B17/B18/B19/B20/B25/B26<br/>/B28/B66/B70/<mark>B71</mark>/B85                                                            |
| 数据传输速率       | <mark>127 (DL) / 159 (UL)</mark>                                                                                                                                      | <mark>127 (DL) / 159 (UL)</mark>                                                                                                                                          | <mark>126 (DL) / 150 (UL)</mark>                                                                                                                        |
| 通信模组电源使能   | <mark>IO 拓展芯片 控制</mark>                                                                                                                                         | <mark>电源直连</mark>                                                                                                                                                     | <mark>电源直连</mark>                                                                                                                                   |
| 通信模组复位       | <mark>IO 拓展芯片 控制</mark>                                                                                                                                         | <mark>无</mark>                                                                                                                                                           | <mark>无</mark>                                                                                                                                         |
| 电源状态监控       | <mark>IO 拓展芯片 ADC 采集</mark>                                                                                                                                     | <mark>无</mark>                                                                                                                                                           | <mark>无</mark>                                                                                                                                         |
::
