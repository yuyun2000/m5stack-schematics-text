# CoreS3-SE

<span class="product-sku">SKU:K128-SE</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/14.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128-SE_01.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128-SE_02.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128-SE_03.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128-SE_04.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128-SE_05.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128-SE_06.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128-SE_07.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128-SE_Weight.jpg">
</PictureViewer>

## 描述

**CoreS3-SE** 是 M5Stack 开发套件系列的第三代主机 CoreS3 的轻量级版本，其核心主控采用 ESP32-S3 方案，双核 Xtensa LX7 处理器，主频 240 MHz ，自带（2.4G）Wi-Fi 功能，板载 16MB Flash 和 8MB PSRAM。可通过 USB Type-C 接口下载程序，支持 OTG 和 CDC 功能，方便外接 USB 设备和烧录固件。正面搭载一块 2.0 寸电容触摸 IPS 屏，面板采用高强度玻璃材质。电源部分采用 AXP2101 电源管理芯片及 4 路电源流向控制回路，整体采用低功耗设计。板载 microSD 卡槽。板载 BM8563 RTC 芯片，提供精确计时及休眠 - 定时唤醒功能。声音输出采用高保真 16bits-I2S 功放芯片 AW88298，机身内置 1w 扬声器。声音输入采用 ES7210 音频解码芯片 + 双麦克风输入。在机身侧边配有独立电源按键与重启 (RST) 按键，自建延时电路，长按复位键便可进入程序下载模式。本成品适用于物联网开发、各种 DIY 项目开发、智能家居控制系统和工业自动化控制系统等场景。

## 教程 & 快速上手

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5cores3/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 CoreS3-SE 设备 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5cores3_se/program) | 本教程介绍如何通过 Arduino IDE 编程控制 CoreS3-SE 设备。 |

## 产品特性

- 基于 ESP32-S3 开发，支持 Wi-Fi @16MB Flash，8MB PSRAM
- 扬声器，双麦克风
- 电容式触摸屏幕
- microSD 卡插槽
- 高强度玻璃材质
- 支持 OTG 和 CDC 功能
- 采用 AXP2101 电源管理，低功耗设计
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 × CoreS3-SE
- 1 × 内六角扳手 L 形 2.0mm (适配 M2.5 螺丝)

## 应用场景

- 物联网开发
- 各种 DIY 项目开发
- 智能家居控制系统
- 工业自动化控制系统

## 规格参数

| 规格                            | 参数                                                                                                           |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| SoC                             | ESP32-S3@Xtensa LX7 双核，主频 240MHz                                                                          |
| USB                             | USB OTG, USB Serial/JTAG                                                                                       |
| Flash                           | 16MB                                                                                                           |
| PSRAM                           | 8MB Quad                                                                                                       |
| Wi-Fi                           | 2.4 GHz Wi-Fi                                                                                                  |
| 触摸                            | FT6336U@电容触摸，触摸区域像素 320 x 280                                                                       |
| LCD 屏幕                        | 2.0"@320 x 240 ILI9342C，SPI 通讯                                                                              |
| 电源管理芯片                    | AXP2101                                                                                                        |
| RTC                             | BM8563                                                                                                         |
| 扬声器                          | 1W@9028                                                                                                        |
| 功放                            | 16bits-I2S 功放芯片 AW88298                                                                                    |
| 音频解码芯片                    | ES7210，双麦克风输入                                                                                           |
| BUS 总线引脚                    | G0/G1/G2/G5/G6/G7/G8/G9/G10/G11/G12/G13/G14/G17/G18/G35/G36/G37/G43/G44                                        |
| 锂电池充电电流                  | 5V@198mA                                                                                                       |
| Grove 输出最大电流 (锂电池供电) | DC 4.2V@940mA                                                                                                  |
| Grove 输出最大电流 (USB 供电)   | DC 5V@680mA                                                                                                    |
| 工作温度                        | 0 ~ 40°C                                                                                                       |
| 功耗                            | 电池供电：待机模式： DC 4.2V@104.64uA；工作模式下 DC 4.2V@109.67mA<br/> USB 供电： 工作模式下： DC 5V@166.27mA |
| 产品尺寸                        | 54.0 x 54.0 x 15.5mm                                                                                           |
| 产品重量                        | 37.8g                                                                                                          |
| 包装尺寸                        | 133.0 x 93.5 x 22.5mm                                                                                          |
| 毛重                            | 54.5g                                                                                                          |

## 操作说明

### 进入下载模式

下载程序前，长按复位按键 3S（亮绿灯）进入下载模式。<br/><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128_SE_Download_Mode.gif" width="30%">

### 开关机操作

- 开机：单击左侧电源键
- 关机：长按 6 秒左侧电源键 ①
- 复位：单击底侧 RST 复位按键 ② <br/><img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/button.png" width="25%">

### 电源管理

CoreS3-SE 采用 AXP2101 电源管理芯片搭配 AW9523B IO 拓展芯片实现对电源输入输出方向的控制。参考下图`BUS_OUT_EN`与`USB_OTG_EN`的引脚状态设置电源的输入输出方向，具体设置代码可参考 [CoreS3 电源管理案例](/zh_CN/arduino/m5cores3/power)。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CoreS3/%E7%94%B5%E6%BA%90.png" width="70%">

## 原理图

- [CoreS3-SE 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/Sch_M5_CoreS3_SE_v1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/Sch_M5_CoreS3_SE_v1.0_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/Sch_M5_CoreS3_SE_v1.0_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/Sch_M5_CoreS3_SE_v1.0_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/Sch_M5_CoreS3_SE_v1.0_page_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/Sch_M5_CoreS3_SE_v1.0_page_05.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/Sch_M5_CoreS3_SE_v1.0_page_06.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/Sch_M5_CoreS3_SE_v1.0_page_07.png">
</SchViewer>

## 管脚映射

### LCD 屏幕 & microSD

LCD 像素：320x240

\#> microSD 容量要求 | microSD 卡最大支持 16GB。

| ESP32-S3 | G37      | G36     | G3  | G35      | G4    |
| -------- | -------- | ------- | --- | -------- | ----- |
| ILI9342C | MOSI     | SCK     | CS  | DC       |       |
| TF Card  | SPI_MOSI | SPI_SCK |     | SPI_MISO | TF_CS |

| AW9523B (0x58) | P1_1    |
| -------------- | ------- |
| ILI9342C       | LCD_RST |

| AXP2101 (0x34) | DCDO1 | LX1 |
| -------------- | ----- | --- |
| ILI9342C       | BL    | PWR |

### CAP.TOUCH

| ESP32-S3       | G12         | G11         | AW9523B_P1_2 | AW9523B_P0_0 |
| -------------- | ----------- | ----------- | ------------ | ------------ |
| FT6336U (0x38) | I2C_SYS_SDA | I2C_SYS_SCL | TOUCH_INT    | TOUCH_RST    |

| ESP32-S3 | G12         | G11         |
| -------- | ----------- | ----------- |
| FT6336U  | I2C_SYS_SDA | I2C_SYS_SCL |

| AW9523B | P0_0      | P1_2      |
| ------- | --------- | --------- |
| FT6336U | TOUCH_RST | TOUCH_INT |

### 麦克风 & 功放

| ESP32-S3       | G12         | G11         | G34     | G33     | G13      | G14      | G0       |
| -------------- | ----------- | ----------- | ------- | ------- | -------- | -------- | -------- |
| ES7210 (0x40)  | I2C_SYS_SDA | I2C_SYS_SCL | I2S_BCK | I2S_WCK | I2S_DATO |          | I2S_MCLK |
| AW88298 (0x36) | I2C_SYS_SDA | I2C_SYS_SCL | I2S_BCK | I2S_WCK |          | I2S_DATI |          |

| AW9523B | P0_2   | P1_3   |
| ------- | ------ | ------ |
| AW88298 | AW_RST | AW_INT |

### AXP 电源指示灯

| AXP2101 | AXP_CHG_LED |
| ------- | ----------- |
| Red LED | RTC_VDD     |

### RTC

| ESP32-S3      | G12         | G11         |
| ------------- | ----------- | ----------- |
| BM8563 (0x51) | I2C_SYS_SDA | I2C_SYS_SCL |

| AXP2101 | IRQ        |
| ------- | ---------- |
| BM8563  | AXP_WAKEUP |

### 内部 I2C 连接

| ESP32-S3 | G12         | G11         |
| -------- | ----------- | ----------- |
| AXP2101  | I2C_SYS_SDA | I2C_SYS_SCL |
| BM8563   | I2C_SYS_SDA | I2C_SYS_SCL |
| ES7210   | I2C_SYS_SDA | I2C_SYS_SCL |
| AW88298  | I2C_SYS_SDA | I2C_SYS_SCL |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G2     | G1    |
| PORT.B   | GND   | 5V  | G9     | G8    |
| PORT.C   | GND   | 5V  | G17    | G18   |
::

### CoreS3-SE M5-Bus 示意图

::m5-bus-table
| FUNC       | PIN | LEFT | RIGHT | PIN | FUNC       |
| ---------- | --- | ---- | ----- | --- | ---------- |
|            | GND | 1    | 2     | G10 | ADC        |
|            | GND | 3    | 4     | G8  | PB_IN      |
|            | GND | 5    | 6     | RST | EN         |
| MOSI       | G37 | 7    | 8     | G5  | GPIO       |
| MISO       | G35 | 9    | 10    | G9  | PB_OUT     |
| SCK        | G36 | 11   | 12    | 3V3 |            |
| RXD0       | G44 | 13   | 14    | G43 | TXD0       |
| PC_RX      | G18 | 15   | 16    | G17 | PC_TX      |
| Int SDA    | G12 | 17   | 18    | G11 | Int SCL    |
| PORT.A SDA | G2  | 19   | 20    | G1  | PORT.A SCL |
| GPIO       | G6  | 21   | 22    | G7  | GPIO       |
| I2S_DOUT   | G13 | 23   | 24    | G0  | I2S_LRCK   |
|            | NC  | 25   | 26    | G14 | I2S_DIN    |
|            | NC  | 27   | 28    | 5V  |            |
|            | NC  | 29   | 30    | BAT |            |
::

### Core 系列主机引脚映射对比

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/7d8564d8e14a62cbb1f6b8a718ceb9c.png" width = "100%">

## 尺寸图

[CoreS3-SE 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1162/cores3-lite.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1162/cores3-lite_page_01.png" width="100%">

## 结构文件

- [CoreS3-SE 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K128-SE_CoreS3-SE/Structures)

## 数据手册

- [esp32-s3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/esp32-s3_technical_reference_manual_cn.pdf)
- [ES7210](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/ES7210.PDF)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BM8563.PDF)
- [AXP2101](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/AXP2101_Datasheet_V1.0_en.pdf)
- [AW88298](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/AW88298.PDF)
- [AW9523B](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CoreS3/AW9523B-CN.pdf)

## 软件开发

### 快速上手

- [CoreS3-SE OpenAI 语音助手](/zh_CN/guide/realtime/openai/m5cores3)
- [CoreS3-SE 小智语音助手](/zh_CN/guide/realtime/xiaozhi/m5cores3)

### Arduino

\#> 注意 | CoreS3-SE 与 CoreS3 存在硬件的差别，库文件中涉及摄像头、接近传感器、IMU、磁力传感器部分的代码不适配 CoreS3-SE。

- [CoreS3-SE Arduino 快速上手](/zh_CN/arduino/m5cores3_se/program)
- [CoreS3-SE Arduino 驱动库](https://github.com/m5stack/M5CoreS3)

### UiFlow2

- [CoreS3-SE UiFlow2 快速上手](/zh_CN/uiflow2/m5cores3/program)

### PlatformIO

- [CoreS3-SE 出厂固件 (pio)](https://github.com/m5stack/CoreS3-UserDemo)

### Easyloader

| Easyloader                    | 下载链接                                                                                                                      | 备注 |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---- |
| CoreS3-SE 出厂固件 Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/CoreS3%20SE%20Firmware.exe) | /    |

## 相关视频

- CoreS3-SE 功能介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/K128-SE%20M5CoreS3%20SE%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| 硬件外设                   | [CoreS3-Lite](/zh_CN/core/CoreS3-Lite) ![CoreS3-Lite](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1162/K128-Lite-02.webp) | [CoreS3](/zh_CN/core/CoreS3) ![ CoreS3](https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp) | [CoreS3-SE](/zh_CN/core/M5CoreS3%20SE) ![ CoreS3-SE](https://static-cdn.m5stack.com/resource/docs/products/core/M5CORES3%20SE/3.webp) |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 摄像头 (GC0308)            | ✅                                                                                                                              | ✅                                                                                                                                                        | ❌                                                                                                                                     |
| 接近传感器 (LTR-553ALS-WA) | ✅                                                                                                                              | ✅                                                                                                                                                        | ❌                                                                                                                                     |
| IMU (BMI270)               | ✅                                                                                                                              | ✅                                                                                                                                                        | ❌                                                                                                                                     |
| 磁罗盘 (BMM150)            | ✅                                                                                                                              | ✅                                                                                                                                                        | ❌                                                                                                                                     |
| RTC                        | ✅                                                                                                                              | ✅                                                                                                                                                        | ✅                                                                                                                                     |
| 麦克风                     | ✅                                                                                                                              | ✅                                                                                                                                                        | ✅                                                                                                                                     |
| 扬声器                     | ✅                                                                                                                              | ✅                                                                                                                                                        | ✅                                                                                                                                     |
| PIMC (AXP2101)             | ✅                                                                                                                              | ✅                                                                                                                                                        | ✅                                                                                                                                     |
| 16MB Flash 和 8MB PSRAM    | ✅                                                                                                                              | ✅                                                                                                                                                        | ✅                                                                                                                                     |
| 触摸                       | ✅                                                                                                                              | ✅                                                                                                                                                        | ✅                                                                                                                                     |
| 背板                       | Cover For CoreS3                                                                                                               | Base DIN                                                                                                                                                 | Cover For CoreS3                                                                                                                      |
| 电池容量                   | 200mAh                                                                                                                         | 500mAh                                                                                                                                                   | ❌                                                                                                                                     |
::

如需对比控制器系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5core_compare?select=K128-SE)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
