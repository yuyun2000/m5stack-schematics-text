# CoreS3

<span class="product-sku">SKU:K128</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-96063e2a-637a-4d11-ac47-1ce4f1cdfd3e.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/K128_main_pictures_01.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-9618aed2-e595-4bb4-ac53-e0b9772aefd6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-5aff2ea4-1943-4349-a70a-5d0c3e8b4214.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-ac385703-414f-46dd-80b9-b49ebc68fdff.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-520d34df-79e2-4905-a8e8-ef7629de6945.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-8845a4bb-1da2-46a2-85f8-8d787e6fe5e5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-150d1624-71b3-4d56-b19c-ace73b1ea407.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-3e707c18-8110-47f9-af1c-ae3c056447d2.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/K128-weight.jpg">
</PictureViewer>

## 描述

**CoreS3** 是 M5Stack 开发套件系列的第三代主机，其核心主控采用 **ESP32-S3** 方案，双核 Xtensa LX7 处理器，主频 240MHz，自带 Wi-Fi 功能，板载 16MB Flash 和 8MB PSRAM，可通过 USB Type-C 接口下载程序，支持 **OTG 和 CDC** 功能，方便外接 USB 设备和烧录固件，正面搭载一块 2.0 寸电容触摸 IPS 屏，面板采用高强度玻璃材质，屏幕下方内置一个 0.3MP 的摄像头 GC0308，附带接近传感器 LTR-553ALS-WA，电源部分采用 AXP2101 电源管理芯片及 4 路电源流向控制回路，整体采用低功耗设计，板载六轴姿态传感器 BMI270 和磁力计 BMM150，板载 TF-card (microSD) 卡槽，板载 BM8563 RTC 芯片，提供精确计时及休眠 - 定时唤醒功能，声音输出方面采用高保真 16bits-I2S 功放芯片 AW88298，机身内置 1w 扬声器，声音输入方面采用 ES7210 音频编码芯片 + 双麦克风输入，在机身侧边配有独立电源按键与重启 (RST) 按键，自建延时电路，长按复位键便可进入程序下载模式。CoreS3 套装默认附带 DinBase 底座，方便实现 Din 导轨、挂墙以及螺丝固定，可外部 DC 12V (支持 9 ~ 24V) 或者内部 500mAh 锂电池供电，DinBase 预留多处 proto 的位置，方便用户 DIY。本成品适用于物联网开发、各种 DIY 项目开发、智能家居控制系统和工业自动化控制系统等场景。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5cores3/program) | 本教程介绍如何通过 Arduino IDE 编程控制 CoreS3 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5cores3/program) | 本教程介绍如何通过 UiFlow2 图形化编程平台控制 CoreS3 设备。 |

learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hhome_assistant_cover_02.jpg) | [Home Assistant](/zh_CN/homeassistant/voice_assistant/cores3_voice_assistant) | 本教程介绍如何通过 CoreS3 连接 Home Assistant。 |

learn>| ![CoreS3小聆语音助手](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/903/coreS3-xiaoling-06.jpg) | [CoreS3小聆语音助手](/zh_CN/guide/realtime/xiaoling/m5cores3) | 本教程将向你介绍使用 CoreS3 主控，通过 M5Burner 烧录 小聆语音助手 固件，构建个人语音助手应用。 |

learn>| ![CoreS3 ESP-Claw 固件烧录](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/CoreS3-ESP-Claw-cover.jpg) | [CoreS3 ESP-Claw 固件烧录](/zh_CN/guide/agent/esp_claw/cores3) | 本教程介绍如何在 StickS3 上烧录 ESP-Claw 固件，帮助用户快速将 CoreS3 设备配置为支持 AI 交互、硬件编程与自动化控制的智能终端。 |

## 产品特性

- 基于 ESP32 开发，支持 Wi-Fi @16MB Flash，8MB PSRAM
- 内置摄像头、接近传感器、扬声器，电源指示灯，RTC，I2S 功放，双麦克风，电容式触摸屏幕，电源键，复位按键，陀螺仪
- microSD 插槽
- 高强度玻璃材质
- 支持 OTG 和 CDC 功能
- 采用 AXP2101 电源管理，低功耗设计
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 × CoreS3
- 1 × DinBase
- 1 x 内六角扳手 L 形 2.5mm (适配 M3 螺丝)
- 4 x 螺丝卡扣
- 1 x 导轨底座卡扣

## 应用场景

- 物联网开发
- 各种 DIY 项目开发
- 智能家居控制系统
- 工业自动化控制系统

## 规格参数

| 规格              | 参数                                                                                            |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| SoC               | ESP32-S3@双核 Xtensa LX7 处理器，主频 240MHz                                                    |
| Flash             | 16MB                                                                                            |
| PSRAM             | 8MB Quad                                                                                        |
| Wi-Fi             | 2.4 GHz Wi-Fi                                                                                   |
| 触摸 IPS LCD 屏幕 | 2.0"@320 x 240 ILI9342C                                                                         |
| 摄像头            | GC0308@ 0.3MP                                                                                   |
| 接近传感器        | LTR-553ALS-WA                                                                                   |
| 电源管理芯片      | AXP2101                                                                                         |
| 六轴姿态传感器    | BMI270                                                                                          |
| 三轴磁力计        | BMM150                                                                                          |
| RTC               | BM8563                                                                                          |
| 扬声器            | 16bits-I2S 功放芯片 AW88298@1W                                                                  |
| 音频编码芯片      | ES7210，双麦克风输入                                                                            |
| 产品尺寸          | 整机套件（CoreS3+DinBase）：69.0 x 54.0 x 31.5mm <br/> 主机部分（CoreS3）：54.0 x 54.0 x 15.5mm |
| 产品重量          | 72.7g                                                                                           |
| 包装尺寸          | 105.6 x 66.0 x 35.3mm                                                                           |
| 毛重              | 101.8g                                                                                          |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

### 进入下载模式

下载程序之前需长按复位按键 3S（亮绿灯）进入下载模式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="30%">

### 开关机操作

- 开机：单击左侧电源键
- 关机：长按 6 秒左侧电源键
- 复位： 单击底侧 RST 按键

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/IMU-CoreS3.jpg" width="70%">

### 电源管理

CoreS3 采用 AXP2101 电源管理芯片搭配 AW9523B IO 拓展芯片实现对电源输入输出方向的控制。参考下图`BUS_OUT_EN`与`USB_OTG_EN`的引脚状态设置电源的输入输出方向，具体设置代码可参考 [CoreS3 电源管理案例](/zh_CN/arduino/m5cores3/power)。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CoreS3/%E7%94%B5%E6%BA%90.png" width="70%">

## 认证信息

- CE/MIC/FCC/SAR

## 原理图

- [CoreS3 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0.pdf)
- [Base DIN 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/559/SCH_DinBase_V1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_04.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_05.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_06.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_07.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/559/SCH_DinBase_V1.1_sch_01.png">
</SchViewer>

## 管脚映射

### LCD 屏幕

LCD 像素：320x240

| ESP32-S3 | G37  | G36 | G3  | G35 |
| -------- | ---- | --- | --- | --- |
| ILI9342C | MOSI | SCK | CS  | DC  |

| AW9523B (0x58) | P1_1 |
| -------------- | ---- |
| ILI9342C       | RST  |

| AXP2101 (0x34) | DLDO1 | LX1 |
| -------------- | ----- | --- |
| ILI9342C       | BL    | PWR |

### microSD

microSD 最大支持 16GB

| ESP32-S3 | G35  | G37  | G36 | G4  |
| -------- | ---- | ---- | --- | --- |
| TF Card  | MISO | MOSI | SCK | CS  |

### 摄像头 & 接近传感器 LTR-553ALS-WA

| ESP32-S3             | G12         | G11         | G45      | G46       | G38      |
| -------------------- | ----------- | ----------- | -------- | --------- | -------- |
| GC0308 (0x21)        | I2C_SYS_SDA | I2C_SYS_SCL | CAM_PCLK | CAM_VSYNC | CAM_HREF |
| LTR-553ALS-WA (0x23) | I2C_SYS_SDA | I2C_SYS_SCL |          |           |          |

| AW9523B | P1_0    |
| ------- | ------- |
| GC0308  | CAM_RST |

> LTR-553ALS-WA 接近传感器和摄像头集成在一条排线上，使用 I2C 进行通讯，详细通讯地址查看上表。

#### GC0308

| 接口                 | Camera Pin | ESP32-S3 |
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

### CAP.TOUCH

| ESP32-S3       | G12         | G11         |
| -------------- | ----------- | ----------- |
| FT6336U (0x38) | I2C_SYS_SDA | I2C_SYS_SCL |

| AW9523B | P0_0      | P1_2      |
| ------- | --------- | --------- |
| FT6336U | TOUCH_RST | TOUCH_INT |

### 麦克风 & 功放

| ESP32-S3      | G12         | G11         | G34     | G33     | G13      | G14      | G0       |
| ------------- | ----------- | ----------- | ------- | ------- | -------- | -------- | -------- |
| ES7210 (0x40) | I2C_SYS_SDA | I2C_SYS_SCL | I2S_BCK | I2S_WCK |          | I2S_DATI | I2S_MCLK |
| AW88298(0x36) | I2C_SYS_SDA | I2C_SYS_SCL | I2S_BCK | I2S_WCK | I2S_DATO |          |          |

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

### IMU（3 轴陀螺仪 + 3 轴加速计 +3 轴磁力计）

| ESP32-S3      | G12         | G11         |
| ------------- | ----------- | ----------- |
| BMI270 (0x69) | I2C_SYS_SDA | I2C_SYS_SCL |

### 内部 I2C 连接

| ESP32-S3 | G12         | G11         |
| -------- | ----------- | ----------- |
| BMI270   | I2C_SYS_SDA | I2C_SYS_SCL |
| AXP2101  | I2C_SYS_SDA | I2C_SYS_SCL |
| BM8563   | I2C_SYS_SDA | I2C_SYS_SCL |
| ES7210   | I2C_SYS_SDA | I2C_SYS_SCL |
| AW88298  | I2C_SYS_SDA | I2C_SYS_SCL |

### BMM150

| BMI270        | BMI270_ASDx | BMI270_ASCx |
| ------------- | ----------- | ----------- |
| BMM150 (0x10) | BMM_SDA     | BMM_SCL     |

\#> BMM150 挂载于 BMI270 | 通过 BMI270 的 Sensor Hub 辅助 I2C 接口接入 BMM150，实现统一的 9 轴传感数据采集。

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G2     | G1    |
| PORT.B   | GND   | 5V  | G9     | G8    |
| PORT.C   | GND   | 5V  | G17    | G18   |
::

### CoreS3 M5-Bus 示意图

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

### Core 系列主机引脚映射对比

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/c9024cfa50b8d7c31ca7505668770ee.png" width = "100%">

## 尺寸图

- [Cores3 模型尺寸 DXF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CoreS3/cores3.dxf)

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CoreS3/%E5%B0%BA%E5%AF%B8%E5%9B%BE.png" width="100%" />

## PCB

- [Cores3 PcbDoc](https://github.com/m5stack/M5_Hardware/blob/master/Common/Module_Type_A/Footprints/Module_Type_A_CoreS3_M5_Bus.PcbDoc)

\#> 说明 | 该文件可用于 DIY 适配 CoreS3 Module Type A 拓展模块。

## 结构文件

- [CoreS3 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K128_CoreS3/Structures)

## 数据手册

- [ESP32-S3](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/esp32-s3_technical_reference_manual_cn.pdf)
- [LTR-553ALS-WA](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/LTR-553ALS-WA.PDF)
- [GC0308](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/GC0308.PDF)
- [ES7210](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/ES7210.PDF)
- [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMM150.PDF)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BM8563.PDF)
- [AXP2101](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/AXP2101_Datasheet_V1.0_en.pdf)
- [AW88298](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/AW88298.PDF)
- [AW9523B](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CoreS3/AW9523B-CN.pdf)

## 软件开发

### 快速上手

- [CoreS3 OpenAI 语音助手](/zh_CN/guide/realtime/openai/m5cores3)
- [CoreS3 XiaoZhi 语音助手](/zh_CN/guide/realtime/xiaozhi/m5cores3)
- [CoreS3 HA 语音助手](/zh_CN/homeassistant/voice_assistant/cores3_voice_assistant)
- [CoreS3 ESP-Claw 固件烧录](/zh_CN/guide/agent/esp_claw/cores3)

### Arduino

- [CoreS3 Arduino 快速上手](/zh_CN/arduino/m5cores3/program)
- [CoreS3 Arduino 驱动库](https://github.com/m5stack/M5CoreS3)
- [CoreS3 Arduino M5Unified 驱动库](https://github.com/m5stack/M5Unified)
- [CoreS3 Arduino M5GFX 驱动库](https://github.com/m5stack/M5GFX)

### UiFlow2

- [CoreS3 UiFlow2 快速上手](/zh_CN/uiflow2/m5cores3/program)
- [CoreS3 UiFlow2 Book](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CoreS3/CoreS3%20Development%20Kit-compressed%20(1).pdf>)

### PlatformIO

- [CoreS3 出厂固件](https://github.com/m5stack/CoreS3-UserDemo/tree/main/firmware)

```bash
[env:m5stack-cores3]
platform = espressif32@6.7.0
board = esp32-s3-devkitc-1
framework = arduino
upload_speed = 1500000
monitor_speed = 115200
build_flags =
    -DESP32S3
    -DBOARD_HAS_PSRAM
    -mfix-esp32-psram-cache-issue
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
	-DARDUINO_USB_MODE=1
lib_deps =
    M5Unified=https://github.com/m5stack/M5Unified
```

### ESP-IDF

- [Espressif's Board Support Packages - CoreS3](https://github.com/espressif/esp-bsp/tree/master/bsp/m5stack_core_s3)
- [CoreS3 ESP-IDF BSP 使用教程](/zh_CN/esp_idf/m5cores3/bsp)

### Easyloader

| Easyloader                 | 下载链接                                                                                            | 备注 |
| -------------------------- | --------------------------------------------------------------------------------------------------- | ---- |
| CoreS3 出厂固件 Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/M5Core/K128%20CoreS3/CoreS3.exe) | /    |

<EspWebTool manifest="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/esp-web-tools/cores3_factory.json">使用 Web Tools 烧录 CoreS3 出厂固件</EspWebTool>

### 其他

- [CoreS3 恢复出厂固件教程](/zh_CN/guide/restore_factory/m5cores3)
- I2C 通讯地址

| Chip         | ADDRESS |
| ------------ | ------- |
| AW88298 Addr | 0x36    |
| AW9523 Addr  | 0x58    |
| AXP2101 Addr | 0x34    |
| BM8563 Addr  | 0x51    |
| BMI270 Addr  | 0x69    |
| BMM150 Addr  | 0x10    |
| ES7210 Addr  | 0x40    |
| FT6336 Addr  | 0x38    |
| GC0308 Addr  | 0x21    |
| LTR553 Addr  | 0x23    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/M5Core/K128%20CoreS3/cores3.mp4" type="video/mp4">
</video>

- 如何使用 USB 在 UiFlow2 中编程

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CoreS3/How%20to%20use%20USB%20port%20execute%20code%20on%20UIFlow%202.0.mp4" type="video/mp4"></video>

- 烧录 UIFLow2x 到 CoreS3

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CoreS3/Burning%20UIFLow2x%20to%20CoreS3-ch.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009263381356&bvid=BV1b2WUeuE96&p=1&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/vpUuPiPSN04?si=nlw_JEL-os4B_4_A" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113791584964532&bvid=BV1RJrhYREji&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/poTxhY3Vhhg?si=GeS61Hj7pZhZvmra" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

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
| 背板                       | Cover For CoreS3                                                                                                               | Base DIN                                                                                                                                                 | ❌                                                                                                                                     |
| 电池容量                   | 200mAh                                                                                                                         | 500mAh                                                                                                                                                   | ❌                                                                                                                                     |
::

如需对比控制器系列产品信息，可访问[产品选型表](/zh_CN/products_selector/m5core_compare?select=K128)，勾选目标产品即可获取对比结果。选型表涵盖核心参数、功能特性等关键信息，支持多产品同步比对。
