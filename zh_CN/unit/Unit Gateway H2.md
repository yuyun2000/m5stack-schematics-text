# Unit Gateway H2

<span class="product-sku">SKU:U195</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195-weight.jpg">
</PictureViewer>

## 描述

**Unit Gateway H2** 是一款全新形态的网关单元，基于 **ESP32-H2-MINI-1-N2** 芯片打造，内置 **RISC-V** 架构的 32 位单核 MCU，集成 **IEEE 802.15.4** 无线通信功能，支持 **Zigbee**、**Thread** 以及基于 Thread 的 **Matter** 互联协议。同时，它还配备了硬件加密引擎，满足高安全性物联网应用的需求。该产品通过 **Grove (Port C)** 接口与 M5 系列主机进行串口（UART）通信，实现数据交互。**Unit Gateway H2** 可灵活扮演网关 (如 Thread Border Router) 或终端设备的角色，与主机协同构建跨生态互联，或独立运行物联网应用。此外，它预留了标准的程序下载接口和 **Type-C** 接口，用于 H2 芯片固件烧录与调试。该产品适用于智能家居、环境监测、传感器网络以及低功耗无线通信节点等多种场景。

## 产品特性

- Zigbee，Thread 和 Matter 等无线通信协议支持
- 集成了 IEEE 802.15.4 技术
- 串口通信
- 支持硬件加密功能
- 低功耗
  - Arduino IDE
  - ESP-IDF

## 包装内容

- 1 x Unit Gateway H2
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 智能家居
- 工业自动化
- 医疗保健
- 消费电子产品
- 智慧农业

## 规格参数

| 规格         | 参数                                                                                                           |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| SoC          | 内置 ESP32-H2 芯片，RISC-V 32 位单核处理器，主频高达 96 MHz @IEEE 802.15.4                                     |
| Flash        | 2MB                                                                                                            |
| 天线         | 模组板载 PCB 天线                                                                                              |
| 支持通信协议 | IEEE 802.15.4 (包括 Zigbee 3.0, Thread 1.3, Matter)                                                            |
| 功耗         | 工作电流: (thread 组网) DC 5V@26.08mA <br/> 待机电流: DC 5V@16.16mA <br/>休眠电流：(Grove 口供电) DC 5V@92.7uA |
| 工作温度     | 0-40°C                                                                                                         |
| 产品尺寸     | 48.0 x 24.0 x 8.0mm                                                                                            |
| 产品重量     | 6.9g                                                                                                           |
| 包装尺寸     | 138.0 x 93.0 x 9.0mm                                                                                           |
| 毛重         | 12.3g                                                                                                          |

## 操作说明

### 下载程序

> 长按 Boot 按键，然后将数据线插入设备。待数据线连接稳定后，松开 Boot 按键，即可进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_download_mode1.gif" width="20%">

## 认证信息

- [ESP32-H2-MINI-1 模组认证信息](https://www.espressif.com.cn/en/support/documents/certificates?keys=&field_certificate_product_tid%5B%5D=2241)

## 原理图

- [Unit Gateway H2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_Sch_Unit_Gateway_H2_v0.3.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_Sch_Unit_Gateway_H2_v0.3_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Gateway H2

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_Model_Size.jpg" width="100%">

## 结构文件

- [Unit Gateway H2 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U195_Unit_Gateway_H2/Structures)

## 数据手册

- [ESP32-H2-MINI-1-N2模组](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/esp32-h2-mini-1_mini-1u_datasheet_cn.pdf)

## 软件开发

### Arduino

- [Unit Gateway H2 Arduino 使用教程](/zh_CN/arduino/projects/unit/unit_gateway_h2)

### UiFlow2

- [Unit GatewayH2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/gateway_h2.html)

### ESP-IDF

- [ESP Thread Boarder Router Guide](/zh_CN/esp_idf/thread/unit_gateway_h2/thread_border_router)
- [ESP Zigbee Gateway Guide](/zh_CN/esp_idf/zigbee/unit_gateway_h2/zigbee_gateway)
- [ESP Zigbee NCP Guide](/zh_CN/esp_idf/zigbee/unit_gateway_h2/zigbee_ncp)
- [ESP32-H2 ESP-IDF Docs](https://github.com/espressif/esp-idf)
- [ESP Zigbee SDK](https://github.com/espressif/esp-zigbee-sdk)
- [ESP Thread Boarder Router SDK](https://github.com/Ocean-lhy/esp-thread-br)

## 相关视频

- Unit Gateway H2 产品介绍和案例展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_Unit_Gateway_H2_vodeo.mp4" type="video/mp4"></video>
