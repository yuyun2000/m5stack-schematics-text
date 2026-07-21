# CoreS3 Thread BR

<span class="product-sku">SKU:K149</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/K149-CoreS3-Thread-BR-main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/K149-CoreS3-Thread-BR-main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/K149-CoreS3-Thread-BR-main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/Thread-BR-main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/Thread-BR-main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/Thread-BR-main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/Thread-BR-main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/Thread-BR-main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/Thread-BR-main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/Thread-BR-main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/Thread-BR-main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/Thread-BR-main-pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/K149-weight.jpg">
</PictureViewer>

## 描述

CoreS3 Thread BR 是一款 Thread 边界路由器套件。核心部件由 CoreS3 控制器与 Module Gateway H2 无线模块组成。其中 CoreS3 作为边界路由器的控制核心，运行用户应用与 OpenThread 协议栈。
CoreS3 控制器采用 ESP32-S3 SoC，板载 16MB Flash 和 8MB PSRAM 内存组合。支持 2.4 GHz Wi-Fi 功能，集成 2.0" 触控 LCD 显示屏，摄像头，麦克风，扬声器，RTC，六轴姿态传感器等丰富外设。Module Gateway H2 模块内置了 ESP32-H2-MINI-1 模组，支持 IEEE 802.15.4 无线通信。作为 OpenThread Radio 协处理器 (RCP) 为核心主控 CoreS3 提供 Thread 数据包转发功能。CoreS3 Thread BR 适合应用于智能家居、环境监测、传感器网络以及低功耗无线通信节点等场景，助力开发者快速进行原型验证和产品开发。

## 产品特性

- CoreS3 核心控制器

  - ESP32-S3
  - 16MB Flash
  - 8MB PSRAM
  - microSD 卡槽
  - 九轴 IMU 传感器: BMI270 + BMM150
  - RTC: BM8563
  - USB-OTG
  - 0.3MP 摄像头 GC0308
  - 接近传感器 LTR-553ALS-WA
  - 音频编码芯片 ES7210
  - 双麦克风输入
  - 高保真功放芯片 AW88298 + 1W 扬声器

- Module Gateway H2 (RCP)

  - ESP32-H2-MINI-1
  - IEEE 802.15.4
  - Zigbee、Thread、Matter

- Base DIN
  - 导轨固定设计
  - 内置 500mAh 锂电池
  - 支持 DC 9~ 24V 输入供电
  - 独立电源开关
  - 2x HY2.-4P 拓展接口

## 包装内容

- 1 x CoreS3 Thread BR
- 1 x 内六角扳手 L 形 2.5mm (适配 M3 螺丝)
- 4 x 螺丝卡扣
- 1 x 导轨底座卡扣

## 应用场景

- 智能家居
- 传感器网络

## 规格参数

| 规格              | 参数                                                  |
| ----------------- | ----------------------------------------------------- |
| SoC               | ESP32-S3 @ Xtensa 32 位 LX7 双核处理器，主频 240MHz   |
| Flash             | 16MB                                                  |
| PSRAM             | 8MB                                                   |
| Wi-Fi             | 2.4 GHz Wi-Fi                                         |
| 触摸 IPS LCD 屏幕 | 2.0"@320 x 240 ILI9342C                               |
| 摄像头            | GC0308@ 0.3MP                                         |
| 接近传感器        | LTR-553ALS-WA                                         |
| 电源管理芯片      | AXP2101                                               |
| 六轴姿态传感器    | BMI270                                                |
| 三轴磁力计        | BMM150                                                |
| RTC               | BM8563                                                |
| 扬声器            | 16bits-I2S 功放芯片 AW88298@1W                        |
| 音频编码芯片      | ES7210，双麦克风输入                                  |
| RCP               | ESP32-H2-MINI-1 @ RISC-V 32 位单核处理器，主频 96 MHz |
| Base DIN 锂电池   | 充电芯片：TP4057<br>电池容量：500mAh                  |
| 产品尺寸          | 54.0 x 54.0 x 38.1mm                                  |
| 产品重量          | 91.0g                                                 |
| 包装尺寸          | 101.0 x 64.0 x 41.0mm                                 |
| 毛重              | 115.7g                                                |

## 原理图

- [CoreS3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0.pdf)
- [Base DIN 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/559/SCH_DinBase_V1.1.pdf)
- [Module Gateway H2原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/Sch_Module-Gateway_H2_v0.4.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_05.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_06.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_07.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/559/SCH_DinBase_V1.1_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/464/Sch_Module-Gateway_H2_v0.4_sch_01.png" width="100%">
</SchViewer>

## 管脚映射

### LCD

| ESP32-S3 | G37  | G36 | G3  | G35 |
| -------- | ---- | --- | --- | --- |
| ILI9342C | MOSI | SCK | CS  | DC  |

### Touch

| ESP32-S3       | G12         | G11         |
| -------------- | ----------- | ----------- |
| FT6336U (0x38) | I2C_SYS_SDA | I2C_SYS_SCL |

### IMU

| ESP32-S3      | G12         | G11         |
| ------------- | ----------- | ----------- |
| BMI270 (0x69) | I2C_SYS_SDA | I2C_SYS_SCL |

| ESP32-S3      | BMI270_ASDx | BMI270_ASCx |
| ------------- | ----------- | ----------- |
| BMM150 (0x10) | BMM_SDA     | BMM_SCL     |

### RTC

| ESP32-S3      | G12         | G11         |
| ------------- | ----------- | ----------- |
| BM8563 (0x51) | I2C_SYS_SDA | I2C_SYS_SCL |

| AXP2101 | IRQ        |
| ------- | ---------- |
| BM8563  | AXP_WAKEUP |

### Audio

| ESP32-S3       | G12         | G11         | G34     | G33     | G13      | G14      | G0       |
| -------------- | ----------- | ----------- | ------- | ------- | -------- | -------- | -------- |
| ES7210 (0x40)  | I2C_SYS_SDA | I2C_SYS_SCL | I2S_BCK | I2S_WCK | I2S_DATO |          | I2S_MCLK |
| AW88298 (0x36) | I2C_SYS_SDA | I2C_SYS_SCL | I2S_BCK | I2S_WCK |          | I2S_DATI |          |

### ALS & PS Sensor

| ESP32-S3             | G12         | G11         |
| -------------------- | ----------- | ----------- |
| LTR-553ALS-WA (0x23) | I2C_SYS_SDA | I2C_SYS_SCL |

### IO Expansion (AW9523B)

| ESP32-S3       | G12         | G11         |
| -------------- | ----------- | ----------- |
| AW9523B (0x58) | I2C_SYS_SDA | I2C_SYS_SCL |

| AW9523B       | P0_0      | P0_1       | P0_2   | P0_3   | P0_4  | P0_5       |
| ------------- | --------- | ---------- | ------ | ------ | ----- | ---------- |
| FT6336U       | TOUCH_RST |            |        |        |       |            |
| Power Control |           | BUS_OUT_EN |        |        |       |            |
| AW88298       |           |            | AW_RST |        |       |            |
| ES7210        |           |            |        | ES_INT |       |            |
| microSD       |           |            |        |        | TF_SW |            |
| Power Control |           |            |        |        |       | USB_OTG_EN |

| AW9523B       | P1_0    | P1_1    | P1_2      | P1_3   | P1_7     |
| ------------- | ------- | ------- | --------- | ------ | -------- |
| Camera        | CAM_RST |         |           |        |          |
| LCD           |         | LCD_RST |           |        |          |
| Touch         |         |         | TOUCH_INT |        |          |
| AW88298       |         |         |           | AW_INT |          |
| Power Control |         |         |           |        | BOOST_EN |

### microSD

| ESP32-S3 | G35  | G37  | G36 | G4  |
| -------- | ---- | ---- | --- | --- |
| microSD  | MISO | MOSI | SCK | CS  |

### Camera

| GC0308               | Camera Pin | ESP32-S3 |
| -------------------- | ---------- | -------- |
| SCCB Clock           | SIOC       | G11      |
| SCCB Data            | SIOD       | G12      |
| System Clock         | XCLK       | -1       |
| Vertical Sync        | VSYNC      | G46      |
| Horizontal Reference | HREF       | G38      |
| Pixel Clock          | PCLK       | G45      |
| Pixel Data Bit 0     | D0         | G39      |
| Pixel Data Bit 1     | D1         | G40      |
| Pixel Data Bit 2     | D2         | G41      |
| Pixel Data Bit 3     | D3         | G42      |
| Pixel Data Bit 4     | D4         | G15      |
| Pixel Data Bit 5     | D5         | G16      |
| Pixel Data Bit 6     | D6         | G48      |
| Pixel Data Bit 7     | D7         | G47      |
| Camera Reset         | RESET      | -1       |
| Camera Power Down    | PWDN       | -1       |

### Module Gateway H2 (RCP)

| Module Gateway H2 | ESP32-S3 |
| ----------------- | -------- |
| RXD               | G10      |
| TXD               | G17      |
| MOSI              | G37      |
| MISO              | G35      |
| CLK               | G36      |
| CS                | G13      |
| WL_ACTIVE         | G0       |
| BT_PRIORITY       | G5       |
| BT_ACTIVE         | G6       |
| EN                | G7       |
| G9                | G18      |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G2     | G1    |
| PORT.B   | GND   | 5V  | G9     | G8    |
| PORT.C   | GND   | 5V  | G17    | G18   |
::

### CoreS3 M5-Bus

::m5-bus-table
| FUNC       | PIN            | LEFT | RIGHT | PIN | FUNC       |
| ---------- | -------------- | ---- | ----- | --- | ---------- |
|            | GND            | 1    | 2     | G10 | ADC        |
|            | GND            | 3    | 4     | G8  | PB_IN      |
|            | GND            | 5    | 6     | RST | EN         |
| MOSI       | G37            | 7    | 8     | G5  | GPIO       |
| MISO       | G35            | 9    | 10    | G9  | PB_OUT     |
| SCK        | G36            | 11   | 12    | 3V3 |            |
| RXD0       | G44            | 13   | 14    | G43 | TXD0       |
| PC_RX      | G18            | 15   | 16    | G17 | PC_TX      |
| Int SDA    | G12            | 17   | 18    | G11 | Int SCL    |
| PORT.A SDA | G2             | 19   | 20    | G1  | PORT.A SCL |
| GPIO       | G6             | 21   | 22    | G7  | GPIO       |
| I2S_DOUT   | G13            | 23   | 24    | G0  | I2S_LRCK   |
|            | HVIN(Base DIN) | 25   | 26    | G14 | I2S_DIN    |
|            | HVIN(Base DIN) | 27   | 28    | 5V  |            |
|            | HVIN(Base DIN) | 29   | 30    | BAT |            |
::

## 尺寸图

- [CoreS3 Thread BR 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/K149-CORES3-Thread-BR.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/K149-CORES3-Thread-BR_page_01.png" width="100%">

## 结构文件

- [CoreS3 Thread BR 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K149_CoreS3_Thread_BR/Structures)

## 软件开发

### ESP-IDF

- [ESP Thread BR ESP Zigbee Gateway](/zh_CN/esp_idf/zigbee/module_gateway_h2/zigbee_gateway)
- [ESP Thread BR ESP Thread Boarder Router](/zh_CN/esp_idf/thread/module_gateway_h2/thread_border_router)
- [ESP Thread BR Bi-directional IPv6 Connectivity](https://docs.espressif.com/projects/esp-thread-br/zh-cn/latest/codelab/connectivity.html#bi-directional-ipv6-connectivity)
- [ESP Thread BR NAT64](https://docs.espressif.com/projects/esp-thread-br/zh-cn/latest/codelab/nat64.html#hardware-prerequisites)
- [ESP Thread Border Router SDK](https://github.com/Ocean-lhy/esp-thread-br)

### 其他

- [CoreS3 Thread BR 恢复出厂固件教程](/zh_CN/guide/restore_factory/cores3_thread_br)

## 相关视频

- CoreS3 Thread BR 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1209/K149-CoreS3-Thread-BR-video-ZH.mp4" type="video/mp4"></video>
