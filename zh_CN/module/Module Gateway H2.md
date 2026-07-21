# Module Gateway H2

<span class="product-sku">SKU:M141</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/M141_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/M141_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/M141_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/M141_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/M141_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/M141_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/M141_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/M141_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/951/M141-weight.jpg">
</PictureViewer>

## 描述

**Module Gateway H2** 是一款基于 ESP32-H2-MINI-1 模组的堆叠式网关开发模块，专为 M5 系列主机设计。它内置低功耗、基于 **RISC-V** 的 32 位单核 MCU ，并支持 **Zigbee**、**Thread** 以及基于 Thread 的 Matter 互联协议。模块集成了 **IEEE 802.15.4** 无线通信功能，能够与 M5 主机协同构建 Matter over Thread 的终端设备，实现多生态系统间的互联互通。
此外，Module Gateway H2 还内置硬件加密引擎，满足对数据安全性要求较高的物联网应用需求。模块上配有拨码开关，用户可灵活切换通信接口模式，同时预留了标准的程序下载接口，便于固件烧录与调试。支持多模块堆叠扩展，适合应用于智能家居、环境监测、传感器网络以及低功耗无线通信节点等场景，助力开发者快速进行原型验证和产品开发。

## 产品特性

- Zigbee，Thread 和 Matter 等无线通信协议支持
- 集成了 IEEE 802.15.4 技术
- 拨码开关配置
- 支持硬件加密功能
- 堆叠扩展
- 低功耗
- 开发平台
  - Arduino IDE
  - ESP-IDF

## 包装内容

- 1 x Module Gateway H2

## 应用场景

- 智能家居
- 工业自动化
- 医疗保健
- 消费电子产品
- 智慧农业

## 规格参数

| 规格         | 参数                                                                       |
| ------------ | -------------------------------------------------------------------------- |
| SoC          | 内置 ESP32-H2 芯片，RISC-V 32 位单核处理器，主频高达 96 MHz @IEEE 802.15.4 |
| Flash        | 2MB                                                                        |
| 天线         | 板载 PCB 天线                                                              |
| 支持通信协议 | IEEE 802.15.4 (包括 Zigbee 3.0, Thread 1.3, Matter)                        |
| 功耗         | 待机电流: DC3.3V/8.55mA <br/>工作电流: thread 组网：DC3.3V/18.35mA         |
| 拨码开关     | 8 位拨码开关，接口切换（UART/SPI）、无线功能控制                           |
| 工作温度     | 0 ~ 40°C                                                                   |
| 产品尺寸     | 54.0 x 54.0 x 13.1mm                                                       |
| 产品重量     | 11.7g                                                                      |
| 包装尺寸     | 132.0 x 95.0 x 16.0mm                                                      |
| 毛重         | 25.3g                                                                      |

## 操作说明

### 下载程序

使用[ESP32 Downloader](https://shop.m5stack.com/products/esp32-downloader-kit)给 ESP32-H2 下载程序

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/esp_downloader_01.jpg" width="30%">

## 认证信息

- RCM/TELEC/CE/FCC/IC/BQB 认证

## 原理图

- [Module Gateway H2原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/Sch_Module-Gateway_H2_v0.4.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/Sch_Module-Gateway_H2_v0.4_sch_01.png" width="100%">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN       | LEFT | RIGHT | PIN         |
| --------- | ---- | ----- | ----------- |
| GND       | 1    | 2     | RXD         |
| GND       | 3    | 4     |             |
| GND       | 5    | 6     |             |
| SPI_MOSI  | 7    | 8     | BT_PRIORITY |
| SPI_MISO  | 9    | 10    |             |
| SPI_CLK   | 11   | 12    | 3V3         |
|           | 13   | 14    |             |
| G9        | 15   | 16    |             |
|           | 17   | 18    |             |
|           | 19   | 20    |             |
| BT_ACTIVE | 21   | 22    | H2-EN       |
| SPI_CS    | 23   | 24    | WL_ACTIVE   |
| HPWR      | 25   | 26    |             |
| HPWR      | 27   | 28    | 5V          |
| HPWR      | 29   | 30    | BAT         |
::

## 尺寸图

<img alt="module size" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/gatewayh2_sch_01.png" width="100%" />

## 数据手册

- [ESP32-H2-MINI-1模组数据手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/esp32-h2-mini-1_mini-1u_datasheet_cn.pdf)

## 软件开发

### Arduino

- [Module Gateway H2 Arduino 使用教程](/zh_CN/arduino/projects/module/module_gateway_h2)

### UiFlow2

- [Module Gateway H2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/gateway_h2.html)

### ESP-IDF

- [ESP Thread Boarder Router Guide](/zh_CN/esp_idf/thread/module_gateway_h2/thread_border_router)
- [ESP Zigbee Gateway Guide](/zh_CN/esp_idf/zigbee/module_gateway_h2/zigbee_gateway)
- [ESP Zigbee NCP Guide](/zh_CN/esp_idf/zigbee/module_gateway_h2/zigbee_ncp)
- [ESP32-H2 ESP-IDF Docs](https://github.com/espressif/esp-idf)
- [ESP Zigbee SDK](https://github.com/espressif/esp-zigbee-sdk)
- [ESP Thread Boarder Router SDK](https://github.com/Ocean-lhy/esp-thread-br)

## 相关视频

- Module Gateway H2 产品介绍和案例展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/M141_Module_Gateway_H2_video.mp4" type="video/mp4"></video>
