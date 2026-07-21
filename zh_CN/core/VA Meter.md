# VAMeter

<span class="product-sku">SKU:K136</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/17.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/13.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/16.webp">
</PictureViewer>

## 描述

**VAMeter** 是一款专业的可编程高精度功率计，主要用于高精度的电压和电流测量。该产品基于 **Stamp-S3** 主控模块，具备 Wi-Fi 功能，内置了两路串联的 **INA226** 电流电压测量电路，拥有 2.5uA 和 250uA 的电流检测分辨率，测量范围支持 0-5A、5-24V （隔离模式下为 1-24V） 。该产品的供电方式灵活，支持通过 USB-C 接口或 Base 端子输入电源，并且具备内置的电源隔离与信号隔离功能。用户可通过拨动开关，在 USB 供电的隔离测量和直接电源取电的非隔离测量之间进行选择，满足不同的应用需求。随产品附赠的扩展 BASE 带有继电器通断控制和 Grove 端口，为二次开发提供了便利。此外，该仪器支持 OTA 固件升级、USB MSC/OTG 功能，用户能够在 PC 上对存储在主控文件系统中的数据及配置文件进行编辑和查看。M5 官方还提供了免费的线上数据 API 接口，方便用户将测试数据上传至 **EZData** 平台，实现远程访问和浏览，大大简化了物联网应用的开发过程。VAMeter 是一款实用性和可开发性都很强的仪器，特别适用于那些对精确电流和电压测量有需求的工程项目，以及工业自动化、设备监控、智能电网等领域。

## 教程 & 快速上手

learn>| ![VAMeter](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/10.webp) | [Quick Start](/zh_CN/guide/iot_tools/vameter/usage) | 本教程将向你介绍 VAMeter 的使用示例。 |

## 产品特性

- 高精度电流检测 (2.5uA/250uA 分辨率切换)
- 宽电压输入 (5-24V)
- 云端 (EZData) 数据显示
- PD 输入 (内部不包含 PD 诱骗)
- 多种供电方式 (PD INPUT/StampS3 / 外部接线端子)
- 电源与信号隔离
- USB MSC/OTG 功能
- 开源软硬件
- 无线升级 OTA
- 开发平台
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x VAMeter
- 1 x VAMeter Base
- 2 x 3.81-2P 端子
- 4 x 吊架 (小)

## 应用场景

- 工业自动化
- 设备监控
- 电源测试与分析
- 物联网 (IoT) 设备
- 远程监控与数据采集

## 规格参数

| 规格               | 参数                                                                                                  |
| ------------------ | ----------------------------------------------------------------------------------------------------- |
| SoC                | ESP32S3FN8@Xtensa 32 位 LX7 双核处理器，主频 240MHz                                                   |
| 功率检测芯片       | INA226                                                                                                |
| Flash              | 8MB                                                                                                   |
| Wi-Fi              | 2.4 GHz Wi-Fi                                                                                         |
| INA226 通讯地址    | 两路检测芯片 INA226:0x40/0x41                                                                         |
| 屏幕               | 1.3 Inch@ 240 x 240 Pixel                                                                             |
| 屏幕驱动           | ST7789                                                                                                |
| PD 输入电源        | 5-24V@0-5A                                                                                            |
| 电流检测分辨率     | 2.5uA/250uA                                                                                           |
| 电流采样误差       | 小电流 (1-100mA) 采样误差：1.01%<br/>大电流 (100mA-5A) 采样误差：0.94%<br/>uA 级电流采样误差：0.69%   |
| 电压采样误差       | 测量误差：0.11%                                                                                       |
| 功耗 (出厂固件)    | STAMP_S3 上 USB 供电： DC 5V@123.5mA <br/>PD INPUT 供电： DC 5V@118mA    DC 12V@66.8mA    DC 24V@26mA |
| PD OUTPUT 输出能力 | DC 24V@3A 68℃ <br/>DC 24V@5A 92℃                                                                      |
| 用户交互           | 旋转编码器开关，复位按键，Boot 按键和板载蜂鸣器                                                       |
| 继电器             | DC 5 ~ 24V@5A                                                                                         |
| 工作温度           | 0 ~ 40°C                                                                                              |
| 产品尺寸           | 51.5 x 48.0 x 40.5mm                                                                                  |
| 产品重量           | 43.4g                                                                                                 |
| 包装尺寸           | 160.9 x 93.0 x 31.6mm                                                                                 |
| 毛重               | 68.4g                                                                                                 |

## 操作说明

### 进入下载模式

如果要进入下载模式，请在开机前按住 VAMeter 上的 G0 按键，通电之后再松开。<br/><img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/M5PPT%20(1135%20x%201080%20%E5%83%8F%E7%B4%A0).gif" width="30%" />

### M5 EZData 云端平台示例

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/c12028ed506f1fa2ad551f468d89ab2.png" width="70%" />

## 原理图

- [VAMeter 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/518/Sch_VAMeter_V1.2.pdf)
- [VAMeter Base 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/518/Sch_VAMeter_base_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/518/Sch_VAMeter_V1.2_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/518/Sch_VAMeter_base_V1.0_sch_01.png">
</SchViewer>

### VAMeter 内部电路逻辑图

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/01.png" width="20%" />

## 管脚映射

### VAMeter(INA226 & BUZZER)

\#> 注意 | INA226 (0x40) 与 INA226 (0x41) 用于不同分辨率和大小的测量

| ESP32S3FN8   | G5   | G6   | G41    | G40    | G14     |
| ------------ | ---- | ---- | ------ | ------ | ------- |
| INA226(0x40) | FSDA | FSCL | ALERT1 |        |         |
| INA226(0x41) | FSDA | FSCL |        | ALERT2 |         |
| BUZZER       |      |      |        |        | BUZ_PWM |

### VAMeter 拓展输出引脚

| ESP32S3FN8 | G10     | G9     | G8     | G42     |
| ---------- | ------- | ------ | ------ | ------- |
| 拓展引脚   | EXT_G10 | EXT_G9 | EXT_G8 | EXT_G42 |

### VAMeter Base

| ESP32S3FN8 | G10     |
| ---------- | ------- |
| Relay      | G10_REL |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G8     | G9    |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/7658e330231814126dd64b55760eaea.png" width="100%" />

## 结构文件

- [VAMeter 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K136_VAMeter/Structures)

## PCB

- [VAMeter Base Board PCB Size](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/VAMeter_base_board.dxf)

## 数据手册

- [INA226](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/ina226.pdf)

## 软件开发

### 快速上手

- [VAMeter使用示例](/zh_CN/guide/iot_tools/vameter/usage)

### ESP-IDF

- [VAMeter 出厂固件](https://github.com/m5stack/VAMeter-Firmware)

### Easyloader

| Easyloader                  | 下载链接                                                                                                               | 备注 |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---- |
| VAMeter Firmware Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/VAMETER%20FIRMWARE.exe) | /    |

### 其他

- [VAMeter 恢复出厂固件教程](/zh_CN/guide/restore_factory/vameter)

## 相关视频

- VAMeter 功能介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/K136%20VA%20Meter%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

## 产品对比

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/VA%20Meter/bee092896d7696d76da369b27cbab69.png" width="90%" />
