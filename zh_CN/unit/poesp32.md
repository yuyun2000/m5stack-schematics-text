# Unit PoESP32

<span class="product-sku">SKU:U138</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poesp32/poesp32_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poesp32/poesp32_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/832/U138-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poesp32/poesp32_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poesp32/poesp32_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poesp32/poesp32_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/poesp32/poesp32_06.webp">
</PictureViewer>

## 描述

**Unit PoESP32** 是一款集成 **PoE**（ Power Over Ethernet ）功能的 **ESP32 以太网控制器**。采用 **ESP32 内置 MAC** + **IP101G 物理层收发器** 方案。模组默认搭载 **ESP-AT** 固件，支持 **TCP**，**MQTT**，**HTTP** 等多种协议栈控制命令，通过串口通信，简单几条的 AT 指令即可实现服务器对接，实现数据通信以及远程控制等功能。支持 PoE 供电的它除了能够为你节省不必要的供电导线，还能为你的设备提供一定的负载能力。该模组预留二次开发接口，借助 ESP32 开发平台中丰富的案例与协议栈支持，能够根据你的使用场景，快速实现功能定制化。

## 产品特性

- 内嵌 ESP32 主控核心
- PHY 方案:
  - 收发器型号 IP101G
  - IEEE 802.3/802.3u 标准
- 以太网接口：
  - PoE 标准：PoE IEEE802.3 AF / 支持最大负载功率 6W
  - RJ45 网口 10/100Mbps
- 通信 / 下载接口:
  - 默认固件为 ESP-AT / 支持二次开发实现 TCP Client/HTTP/CoAP 等等协议栈
  - 可编程 / 支持二次开发，预留程序下载接口
- 供电方式：
  - HY2.0-4P 接口 5V 供电
  - PoE 供电 (PoE IEEE802.3 AF)
- 开发方式：
  - AT 指令，UART: 9600bps 默认
  - 开发平台: UiFlow (coming soon)，Arduino，ESP-IDF

## 包装内容

- 1 x Unit PoESP32
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 以太网控制器
- 数据通信以及远程控制

## 规格参数

| 规格             | 参数                                                                                |
| ---------------- | ----------------------------------------------------------------------------------- |
| ESP32-WROOM-32U  | 240MHz dual core，600 DMIPS，520KB SRAM (不集成 3D 天线，不支持 WiFi\&BLE 无线功能) |
| Flash            | 4MB                                                                                 |
| PHY              | IP101G: IEEE 802.3/802.3u                                                           |
| MAC-PHY 接口类型 | RMII                                                                                |
| PoE 规范         | PoE IEEE802.3 AF 规范 / 最大功率 6W / 供电电压 DC 37-57V                            |
| 以太网接口规格   | RJ45 10/100Mbps                                                                     |
| 预留接口         | 1x HY2.0-4P 接口，1x 程序下载接口                                                   |
| 通信接口         | UART 9600bps 8N1 AT 指令控制                                                        |
| 通信逻辑电平     | 3.3V                                                                                |
| 产品重量         | 26.2g                                                                               |
| 毛重             | 32.8g                                                                               |
| 产品尺寸         | 72 x 26 x 19.2mm                                                                    |
| 包装尺寸         | 75 x 36 x 20.5mm                                                                    |

## 操作说明

### 程序下载

如需进行二次开发，可拆卸设备外壳，通过预留的二次开发接口连接 [ESP32 Downloader](https://shop.m5stack.com/products/esp32-downloader-kit)，进行程序下载。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/832/U138_operation.jpg" width="50%">

## 原理图

- [Unit PoESP32 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/597/SCH_UNIT-PoESP32.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/597/SCH_UNIT-PoESP32_sch_01.png">
</SchViewer>

## 管脚映射

### IP101G (ETH_ADDR = 1)

| IPG101G (RMII PHY) | ESP32 |
| ------------------ | ----- |
| TX_EN              | G21   |
| TX0                | G19   |
| TX1                | G22   |
| RX0                | G25   |
| RX1                | G26   |
| CRS_DV             | G27   |

| IPG101G (SMI) | ESP32 |
| ------------- | ----- |
| MDC           | G23   |
| MDIO          | G18   |

### HY2.0-4P

| PoESP32 | RXD | TXD |
| ------- | --- | --- |
| M5CORE  | G16 | G17 |

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/829/U129_Model_Size_page_01.png" width="70%">

## 数据手册

- [ESP32-WROOM-32U/D](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/esp32-wroom-32d_esp32-wroom-32u_datasheet_cn.pdf)
- [IP101G](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/poesp32/C336124_IP101GA_2018-11-27.PDF)

## 软件开发

### Arduino

- TCP Client
  - [PoESP32 with M5Core-TCP Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5Core/TCP_CLIENT/TCP_CLIENT.ino)
  - [PoESP32 with M5Core2-TCP Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5Core2/TCP_CLIENT/TCP_CLIENT.ino)
  - [PoESP32 with M5Atom-TCP Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5Atom/TCP_CLIENT/TCP_CLIENT.ino)
  - [PoESP32 with M5StickC-TCP Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5StickC/TCP_CLIENT/TCP_CLIENT.ino)
  - [PoESP32 with M5StickC Plus-TCP Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5StickCPlus/TCP_CLIENT/TCP_CLIENT.ino)
- HTTP Client
  - [PoESP32 with M5Core-HTTP Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5Core/HTTP_CLIENT/HTTP_CLIENT.ino)
  - [PoESP32 with M5Core2-HTTP Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5Core2/HTTP_CLIENT/HTTP_CLIENT.ino)
  - [PoESP32 with M5Atom-HTTP Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5Atom/HTTP_CLIENT/HTTP_CLIENT.ino)
  - [PoESP32 with M5StickC-HTTP Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5StickC/HTTP_CLIENT/HTTP_CLIENT.ino)
  - [PoESP32 with M5StickC Plus-HTTP Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5StickCPlus/HTTP_CLIENT/HTTP_CLIENT.ino)
- MQTT Client
  - [PoESP32 with M5Core-MQTT Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5Core/MQTT_CLIENT/MQTT_CLIENT.ino)
  - [PoESP32 with M5Core2-MQTT Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5Core2/MQTT_CLIENT/MQTT_CLIENT.ino)
  - [PoESP32 with M5Atom-MQTT Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5Atom/MQTT_CLIENT/MQTT_CLIENT.ino)
  - [PoESP32 with M5StickC-MQTT Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5StickC/MQTT_CLIENT/MQTT_CLIENT.ino)
  - [PoESP32 with M5StickC Plus-MQTT Client](https://github.com/m5stack/M5Unit-PoESP32/blob/master/examples/Unit_PoESP32_M5StickCPlus/MQTT_CLIENT/MQTT_CLIENT.ino)

### 内置固件

- [Unit PoESP32 Internal Firmware / ESP-AT](https://github.com/espressif/esp-at)
- [ESP-AT Documentation](https://docs.espressif.com/projects/esp-at/zh_CN/latest/esp32/Get_Started/What_is_ESP-AT.html)

## 相关视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/poesp32/POESP32%E6%9C%8D%E5%8A%A1%E8%B4%A8%E9%87%8F%E8%AF%84%E4%BB%B7%E7%BB%88%E7%AB%AF(1).mp4" type="video/mp4"></video>
