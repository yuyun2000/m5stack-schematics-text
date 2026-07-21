# StamPLC

<span class="product-sku">SKU:K141</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_Weight.jpg">
</PictureViewer>

## 描述

**StamPLC** 是一款物联网可编程逻辑控制器，专为工业自动化与远程监控设计。产品采用 **Stamp-S3A** 控制模组，不仅提供强大的处理能力，还实现了高效 **无线** 连接。在 **控制方面**，StamPLC 提供 8 路光耦隔离数字输入和 4 路继电器输出（支持交 / 直流负载），加上 GPIO.EXT 与 2 个 HY2.0-4P 接口，使各类传感器和执行器的接入更加简单可靠；同时，通过板载的 **PWR-CAN** 和 **PWR-485** 接口，设备能够无缝集成进工业现场总线网络，实现远程数据传输与集中控制。人机交互方面，产品搭载了 1.14 英寸彩色 **显示屏**，RESET/BOOT 按键，3 个用户按键及 **蜂鸣器**，方便用户进行实时参数配置和状态监控，并能在异常时及时报警。为了适应严苛工业环境，StamPLC 支持 DC 6～36V 宽压供电，并设计为 **DIN** 导轨安装，确保设备稳固安装；内置 **microSD** 卡槽则便于数据存储和固件更新。此外，其环境监测系统集成了 LM75 温度传感器与 INA226 电压 / 电流传感器，用于实时反馈设备运行状态，而 RTC（RX8130CE）模块则确保时间同步和日志记录的准确性。出厂固件默认将数据上传至 M5 的 **EZData** 云平台，自动生成监控页面，为用户提供便捷的远程云端**访问和控制**方式。该产品适用于工业自动化、远程监控、智能制造等领域。

## 教程 & 快速上手

learn>| ![StamPLC](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_02.webp) | [Quick Start](/zh_CN/guide/industrial_control/stamplc/usage) | StamPLC 内置固件使用教程。|

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5stamplc/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 StamPLC 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/stamplc/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 StamPLC 设备。 |

learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hhome_assistant_cover_02.jpg) | [Home Assistant](/zh_CN/homeassistant/kit/stamplc) | 本案例介绍如何将设备添加至 Home Assistant |

## 注意事项

### 电源注意事项

StamPLC 的 PWR-CAN 和 PWR-485 输出供电引脚直接与整机输入电源相连，因此在使用过程中请务必确保输入电压与外接扩展设备的供电要求一致。例如，在使用 StamPLC 控制 Unit Roller485 或 Unit RollerCAN 时，建议将输入电压控制在 DC 6～16V 范围内，以防止因电压不匹配而造成设备损坏。

## 产品特性

- Stamp-S3A 控制模组（ESP32-S3FN8）
- EZData 云监控
- 8 路光耦隔离数字输入
- 4 路继电器输出（交 / 直流）
- 1.14 英寸彩屏 (ST7789v2)
- PWR-CAN & PWR-485 接口
- 宽压输入（DC 6 ~ 36V）
- 集成 INA226 电压 / 电流传感器，可测量 DC 电源接口及 EXT 拓展接口 VIN 输入的电压与电流
- 内部温度传感器
- 用户按键
- microSD 卡槽
- DIN 导轨安装
- 蜂鸣器
- HY2.0-4P 接口
- RTC 模块
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x StamPLC
- 4 x 固定小件
- 4 x 螺丝卡扣固定件

## 应用场景

- 工业自动化与远程控制
- 分布式控制系统
- 智能制造

## 规格参数

| 规格          | 参数                                                                                                                              |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 模组型号      | Stamp-S3A 控制模组                                                                                                                |
| SoC           | ESP32-S3FN8@Xtensa LX7 双核，主频高达 240MHz                                                                                      |
| Flash         | 8MB                                                                                                                               |
| Wi-Fi         | 2.4 GHz Wi-Fi                                                                                                                     |
| 数字输入      | 8 路光耦隔离数字输入，输入电压范围: DC 5~36V                                                                                      |
| 数字输出      | 4 路继电器输出                                                                                                                    |
| 继电器        | AC 5A@250V<br/>DC 5A@28V                                                                                                          |
| DC 供电电源   | 支持 DC 6 ~ 36V @ 1A 宽压供电 <br/>DC 电源接口：DC5521 母头 5.5 x 2.1mm (内正外负)                                                |
| 扩展接口      | GPIO.EXT 接口，2 个 HY2.0-4P 接口                                                                                                 |
| 通讯接口      | 板载 PWR-CAN 与 PWR-485 接口                                                                                                      |
| PWR-CAN 接口  | XT30 (2+2) PW-M                                                                                                                   |
| PWR-485 接口  | HT3.96-4P                                                                                                                         |
| 显示          | 1.14 英寸彩色显示屏（135×240 分辨率）, 驱动芯片 ST7789v2                                                                          |
| 交互控制      | 1 个 RESET/BOOT 按键，3 个用户按键，蜂鸣器                                                                                        |
| 数据存储      | 内置 microSD 卡槽                                                                                                                 |
| 传感器        | LM75 温度传感器，INA226 电压 / 电流传感器，RTC（RX8130CE）                                                                        |
| IO 口带载能力 | 2x8 扩展接口最大带载能力: DC 4.76V@700mA<br/>HY2.0-4P 口带载能力测试: DC 4.81V@700mA                                              |
| 功耗          | 待机电流: (5V 供电) DC 5V @ 21.60mA, (12V 供电) DC 12V@15.22mA <br/> 工作电流: (5V 供电) DC 5V@93.89mA, (12V 供电) DC 12V@47.84mA |
| 安装方式      | DIN 导轨安装                                                                                                                      |
| 工作温度      | 0 ~ 40°C                                                                                                                          |
| 产品尺寸      | 72.0 × 80.0 × 33.4mm                                                                                                              |
| 产品重量      | 138.9g                                                                                                                            |
| 包装尺寸      | 102.0 x 94.0 x 33.4mm                                                                                                             |
| 毛重          | 177.5g                                                                                                                            |

## 操作说明

### 进入下载模式

如果要进入下载模式，连接数据线之后，按住 Boot 按键，直到红色指示灯亮起，放开 Boot 按键即可进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_download_mode.gif" width="30%" />

### 信号输入传感器接线方式

输入通道集成光耦隔离，支持 DC5~36V 高电平 / 低电平信号输入采集，适配不同类型的传感器输入。

- 低电平信号输入传感器接线方式：<br/>- COM 连接传感器电源正极 <br/>- INPUT 连接传感器输入信号<br/><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_Relay_control_mode_01.png" width="30%" />
- 高电平信号输入传感器接线方式：<br/>- COM 连接传感器电源负极<br/>- INPUT 连接传感器输入信号<br/><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_Relay_control_mode_02.png" width="30%" />

## 原理图

- [Stamp-S3A main board 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_sch_StamPLC_V10_CPU.pdf)
- [StamPLC_IO 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_sch_StamPLC_V10_IO.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_sch_StamPLC_V10_CPU_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_sch_StamPLC_V10_IO_sch_01.png">
</SchViewer>

## 管脚映射

### PWR-485 & PWR-CAN

| ESP32-S3FN8 | G42    | G43    | G0            | G39      | G46       |
| ----------- | ------ | ------ | ------------- | -------- | --------- |
| PWR-CAN     | CAN_TX | CAN_RX |               |          |           |
| PWR-485     |        |        | RS485_TX/BOOT | RS485_RX | RS485_DIR |

### RGB & 用户按键 A/B/C

- 通过 PI4IOE5V6408 控制

| ESP32-S3FN8        | G15 | G13 | G14 | G3  |
| ------------------ | --- | --- | --- | --- |
| PI4IOE5V6408(0x43) | SCL | SDA | INT | RST |

| PI4IOE5V6408 | P6  | P5  | P4  | P2   | P1   | P0   |
| ------------ | --- | --- | --- | ---- | ---- | ---- |
| RGB          | R   | G   | B   |      |      |      |
| Button       |     |     |     | KEYA | KEYB | KEYC |

\#> RGB LED 控制说明 | RGB LED 仅支持通过 R/G/B 三个独立通道的亮灭组合实现色彩，不支持 PWM 调光控制亮度或渐变效果。

### microSD 卡槽

| ESP32-S3FN8 | G9   | G10 | G7  | G8   |
| ----------- | ---- | --- | --- | ---- |
| microSD     | MISO | CS  | SCK | MOSI |

### 传感器

| ESP32-S3FN8         | G15 | G13 | G14 |
| ------------------- | --- | --- | --- |
| INA226AIDGSR (0x40) | SCL | SDA | INT |
| LM75BDP (0x48)      | SCL | SDA | INT |
| RX8130CE (0x32)     | SCL | SDA | INT |

### LCD

| ESP32-S3FN8 | G8   | G7  | G6  | G12 | G3  |
| ----------- | ---- | --- | --- | --- | --- |
| LCD         | MOSI | SCK | RS  | CS  | RST |

| PI4IOE5V6408 | P7     |
| ------------ | ------ |
| LCD          | LCD_BL |

### 蜂鸣器

| ESP32-S3FN8 | G44        |
| ----------- | ---------- |
| Buzzer      | BUZZER_PWM |

### 继电器与光耦

- 通过 AW9523B 控制 (0x59)

| ESP32-S3FN8   | G15 | G13 | G14 | G3  |
| ------------- | --- | --- | --- | --- |
| AW9523B(0x59) | SCL | SDA | INT | RST |

- 继电器控制

| AW9523B | P0_0     | P0_1     | P0_2     | P0_3     |
| ------- | -------- | -------- | -------- | -------- |
| Relay   | RLY_DRV1 | RLY_DRV2 | RLY_DRV3 | RLY_DRV4 |

- 光耦输出

| AW9523B | P0_4    | P0_5    | P0_6    | P0_7    | P1_4    | P1_5    | P1_6    | P1_7    |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| EL3H4   | SYS_IN1 | SYS_IN2 | SYS_IN3 | SYS_IN4 | SYS_IN5 | SYS_IN6 | SYS_IN7 | SYS_IN8 |

- 光耦输入

| EL3H4     | 功能说明       |
| --------- | -------------- |
| EXCOM_IN1 | 外部输入信号 1 |
| EXCOM_IN2 | 外部输入信号 2 |
| EXCOM_IN3 | 外部输入信号 3 |
| EXCOM_IN4 | 外部输入信号 4 |
| EXCOM_IN5 | 外部输入信号 5 |
| EXCOM_IN6 | 外部输入信号 6 |
| EXCOM_IN7 | 外部输入信号 7 |
| EXCOM_IN8 | 外部输入信号 8 |
| EXCOM_COM | 公共端         |

### StamPLC-Bus

::m5-bus-table
| FUNC    | PIN | LEFT | RIGHT | PIN    | FUNC   |
| ------- | --- | ---- | ----- | ------ | ------ |
|         | VIN | 1    | 2     | GND    |        |
|         | GND | 3    | 4     | GND    |        |
|         | GND | 5    | 6     | 5V_OUT |        |
| SCL     | G15 | 7    | 8     | G13    | SDA    |
| PHY_RST | G3  | 9    | 10    | G14    | INT    |
| MISO    | G9  | 11   | 12    | G7     | SCK    |
| MOSI    | G8  | 13   | 14    | G11    | CS     |
| Custom  | G40 | 15   | 16    | G41    | Custom |
::

### HY2.0-4P

- PORT.A

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G2     | G1    |
::

- PORT.C

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.C   | GND   | 5V  | G5     | G4    |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/K141_Model_Size_sch_01.png" width="100%">

## 结构文件

- [StamPLC 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K141_StamPLC/Structures)

## 数据手册

- [INA226AIDGSR](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/INA226AIDGSR.pdf)
- [LM75BDP](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/LM75B.pdf)
- [ST7789V2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/ST7789V.pdf)
- [PWR-485](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/SIT3088EEUA.pdf)
- [PRW-CAN](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/SIT1044QTK.pdf)
- [AW9523B](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/AW9523B.pdf)
- [PI4IOE5V6408](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/PI4IOE5V6408.pdf)
- [EL3H4](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/EL3H4.pdf)
- [RX8130CE 技术手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/RX8130CE_cn.pdf)
- [RX8130CE 寄存器手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/RX8130CE_cn-Register-Datasheet.pdf)

## 软件开发

### 快速上手

- [StamPLC 快速上手](/zh_CN/guide/industrial_control/stamplc/usage)
- [StamPLC 控制器 Home Assistant 集成](/zh_CN/homeassistant/kit/stamplc)

### Arduino

- [StamPLC Arduino 快速上手](/zh_CN/arduino/m5stamplc/program)
- [StamPLC Arduino 驱动库](https://github.com/m5stack/M5StamPLC)

### UiFlow2

- [StamPLC UiFlow2 快速上手](/zh_CN/uiflow2/stamplc/program)

### ESP-IDF

- [StamPLC 出厂固件](https://github.com/m5stack/M5StamPLC-UserDemo)

### PlatformIO

```bash
[env:m5stack-stamp-s3]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
upload_speed = 1500000
build_flags =
    -DESP32S3
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
	-DARDUINO_USB_MODE=1

lib_deps =
    M5StamPLC=https://github.com/m5stack/M5StamPLC
    M5Unified=https://github.com/m5stack/M5Unified
```

### 通信协议

- Modbus

> StamPLC 固件默认启动后将自动初始化 Modbus 从机，外部设备可通过 PWR-485 接口，使用 Modbus RTU 协议对设备进行控制，具体寄存器协议如下。

Register Map:

1. Coils (Read/Write)

- Address 0: Relay 1 output (true/false)
- Address 1: Relay 2 output (true/false)
- Address 2: Relay 3 output (true/false)
- Address 3: Relay 4 output (true/false)

2. Input Registers (Read-only)

- Address 0-7: Inputs (true/false) - 8 registers
- Address 8-9: Temperature (FLOAT32) - 2 registers
- Address 10-11: Bus Voltage (FLOAT32) - 2 registers
- Address 12-13: Shunt Current (FLOAT32) - 2 registers

### Easyloader

| Easyloader                   | 下载链接                                                                                | 备注 |
| ---------------------------- | --------------------------------------------------------------------------------------- | ---- |
| StamPLC User Demo Easyloader | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/StamPLC_User_Demo.exe) | /    |

### 其他

- [StamPLC 恢复出厂固件教程](/zh_CN/guide/restore_factory/stamplc)

## 相关视频

- StamPLC 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/m5stamplc/K141_video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114199824958678&bvid=BV17CX6YnEZx&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/hYcIfaQ9DT8?si=-pGsYcteNOuaKhdq" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
