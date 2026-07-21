# Module LoRa868 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module LoRa868 |
| SKU | M029 |
| 产品 ID | `module-lora868-e0f14d8b25dd` |
| 源文档 | `zh_CN/module/lora868.md` |

## 概述

Module LoRa868 的原理图以 M1 `Ra-01 Module` 作为完整 LoRa 子模块，通过 MOSI/MISO/SCK/CS 接入 M5-Bus SPI，并以 RST 与 IRQ 连接 GPIO26/GPIO36。J1 的 +5V 经 VR1 AMS1117-3.3 生成 3V3 供 M1，C1 为输出侧对地电容。页面没有展开 LoRa 芯片、晶振、天线或 RF 匹配；产品正文的 Ra-01H、803~930MHz、调制方式、灵敏度和比特率无法由本页独立确认。

## 检索关键词

`Module LoRa868`、`M029`、`Ra-01 Module`、`Ra-01H`、`AMS1117-3.3`、`SPI`、`MOSI`、`MISO`、`SCK`、`CS`、`NSS`、`RST`、`RESET`、`IRQ`、`DIO0`、`DIO1`、`DIO2`、`DIO3`、`DIO4`、`DIO5`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO5`、`GPIO26`、`GPIO36`、`+5V`、`3V3`、`803~930MHz`、`868MHz`、`LoRa`、`FSK`、`GFSK`、`MSK`、`GMSK`、`OOK`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | Ra-01 Module | LoRa 射频子模块，提供 SPI、RESET、DIO0~DIO5、电源与接地引脚 | 图 527262b7369d / 第 1 页 / 第 1 页左上 M1 Ra-01 Module，1~16 脚 |
| J1 | M5Stack_BUS | 30 针堆叠接口，引出 LoRa SPI、CS、RST、IRQ、+5V 与 GND | 图 527262b7369d / 第 1 页 / 第 1 页右上 J1 M5Stack_BUS，1~30 脚及 MOSI/MISO/SCK/IRQ/RST/CS/+5V 网络 |
| VR1 | AMS1117-3.3 | 将 +5V 转换为 M1 使用的 3V3 | 图 527262b7369d / 第 1 页 / 第 1 页左下 VR1 AMS1117-3.3，Vin +5V、Vout 3V3、GND |
| C1 | 未标注 | VR1 3V3 输出对 GND 的极性电容；页面未标容量 | 图 527262b7369d / 第 1 页 / 第 1 页左下 VR1 Vout 右侧 C1，跨接 3V3 与 GND |

## 系统结构

### Module LoRa868

M1 Ra-01 Module 通过 SPI、CS、RST、IRQ 接入 J1 M5Stack_BUS，VR1 从 J1 +5V 生成 3V3 为 M1 供电。

- 参数与网络：`radio_module=M1 Ra-01 Module`；`host_connector=J1 M5Stack_BUS`；`bus=SPI`；`control=CS,RST,IRQ`；`regulator=VR1 AMS1117-3.3`
- 证据：图 527262b7369d / 第 1 页 / 第 1 页 M1、J1、VR1 及同名网络

## 核心器件

### M1

原理图中 M1 的器件文本为 `Ra-01 Module`，未显示内部射频芯片型号。

- 参数与网络：`reference=M1`；`schematic_part_number=Ra-01 Module`；`internal_ic=null`
- 证据：图 527262b7369d / 第 1 页 / 第 1 页 M1 符号底部 Ra-01 Module

## 电源

### VR1 AMS1117-3.3

VR1 Vin 接 +5V，Vout 输出 3V3，GND 接地；C1 从 3V3 接 GND，但容量未标注。

- 参数与网络：`input=+5V`；`output=3V3`；`ground=GND`；`output_capacitor=C1 value not shown`
- 证据：图 527262b7369d / 第 1 页 / 第 1 页左下 VR1/C1 电源网络

### M1 3V3 与 GND

M1.3 接 3V3，M1.1/.2/.9/.16 接 GND；3V3 来源为 VR1，+5V 来源为 J1.28。

- 参数与网络：`supply_pin=M1.3 3V3`；`ground_pins=M1.1,M1.2,M1.9,M1.16`；`regulator=VR1`；`bus_5v=J1.28`
- 证据：图 527262b7369d / 第 1 页 / 第 1 页 M1 电源/地引脚、VR1 与 J1.28 +5V

## 接口

### J1 M5Stack_BUS 已用针脚

J1.1/.3/.5 接 GND，J1.4=IRQ/GPIO36，J1.7=MOSI/GPIO23，J1.9=MISO/GPIO19，J1.10=RST/GPIO26，J1.11=SCK/GPIO18，J1.20=CS/GPIO5，J1.28=+5V。

- 参数与网络：`pins_1_3_5=GND`；`pin_4=IRQ GPIO36`；`pin_7=MOSI GPIO23`；`pin_9=MISO GPIO19`；`pin_10=RST GPIO26`；`pin_11=SCK GPIO18`；`pin_20=CS GPIO5`；`pin_28=+5V`
- 证据：图 527262b7369d / 第 1 页 / 第 1 页 J1 外部网络标签及符号内 GPIO 对应

## 总线

### M1 SPI

M1.14 MOSI 接 J1.7 GPIO23，M1.13 MISO 接 J1.9 GPIO19，M1.12 SCK 接 J1.11 GPIO18，M1.15 NSS 通过 CS 接 J1.20 GPIO5。

- 参数与网络：`mosi=M1.14 -> MOSI -> J1.7 GPIO23`；`miso=M1.13 -> MISO -> J1.9 GPIO19`；`sck=M1.12 -> SCK -> J1.11 GPIO18`；`chip_select=M1.15 NSS -> CS -> J1.20 GPIO5`；`address=null`
- 证据：图 527262b7369d / 第 1 页 / 第 1 页 M1 右侧 NSS/MOSI/MISO/SCK 与 J1 CS/MOSI/MISO/SCK

## GPIO 与控制信号

### M1 IRQ

M1.5 DIO0 通过 IRQ 网络连接 J1.4 GPIO36，方向为 M1 向主机的中断输出。

- 参数与网络：`source=M1.5 DIO0`；`net=IRQ`；`bus_pin=J1.4`；`host_gpio=GPIO36`；`direction=M1 to host`
- 证据：图 527262b7369d / 第 1 页 / 第 1 页 M1.5 DIO0/IRQ 与 J1.4 GPIO36/IRQ

### M1 未用 DIO

M1.6 DIO1、M1.7 DIO2、M1.8 DIO3、M1.10 DIO4、M1.11 DIO5 在图中标为未连接。

- 参数与网络：`DIO1=M1.6 NC`；`DIO2=M1.7 NC`；`DIO3=M1.8 NC`；`DIO4=M1.10 NC`；`DIO5=M1.11 NC`
- 证据：图 527262b7369d / 第 1 页 / 第 1 页 M1 左侧 DIO1~DIO3 与右侧 DIO4/DIO5 的红色未连接标记

## 复位

### M1 RESET

M1.4 RESET 通过 RST 网络连接 J1.10 GPIO26，页面未显示复位上拉、下拉或 RC 网络。

- 参数与网络：`radio_pin=M1.4 RESET`；`net=RST`；`bus_pin=J1.10`；`host_gpio=GPIO26`；`bias_shown=false`
- 证据：图 527262b7369d / 第 1 页 / 第 1 页 M1.4 RESET/RST 与 J1.10 GPIO26/RST

## 内存与 Flash

### 存储器

页面未展示 M1 之外的 Flash、EEPROM、RAM、SD 卡或其他外部存储器及其总线。

- 参数与网络：`external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_shown=false`
- 证据：图 527262b7369d / 第 1 页 / 第 1 页全图无独立存储器件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module LoRa868 | `radio_module=M1 Ra-01 Module`；`host_connector=J1 M5Stack_BUS`；`bus=SPI`；`control=CS,RST,IRQ`；`regulator=VR1 AMS1117-3.3` |
| 核心器件 | M1 | `reference=M1`；`schematic_part_number=Ra-01 Module`；`internal_ic=null` |
| 总线 | M1 SPI | `mosi=M1.14 -> MOSI -> J1.7 GPIO23`；`miso=M1.13 -> MISO -> J1.9 GPIO19`；`sck=M1.12 -> SCK -> J1.11 GPIO18`；`chip_select=M1.15 NSS -> CS -> J1.20 GPIO5`；`address=null` |
| 复位 | M1 RESET | `radio_pin=M1.4 RESET`；`net=RST`；`bus_pin=J1.10`；`host_gpio=GPIO26`；`bias_shown=false` |
| GPIO 与控制信号 | M1 IRQ | `source=M1.5 DIO0`；`net=IRQ`；`bus_pin=J1.4`；`host_gpio=GPIO36`；`direction=M1 to host` |
| GPIO 与控制信号 | M1 未用 DIO | `DIO1=M1.6 NC`；`DIO2=M1.7 NC`；`DIO3=M1.8 NC`；`DIO4=M1.10 NC`；`DIO5=M1.11 NC` |
| 电源 | VR1 AMS1117-3.3 | `input=+5V`；`output=3V3`；`ground=GND`；`output_capacitor=C1 value not shown` |
| 电源 | M1 3V3 与 GND | `supply_pin=M1.3 3V3`；`ground_pins=M1.1,M1.2,M1.9,M1.16`；`regulator=VR1`；`bus_5v=J1.28` |
| 接口 | J1 M5Stack_BUS 已用针脚 | `pins_1_3_5=GND`；`pin_4=IRQ GPIO36`；`pin_7=MOSI GPIO23`；`pin_9=MISO GPIO19`；`pin_10=RST GPIO26`；`pin_11=SCK GPIO18`；`pin_20=CS GPIO5`；`pin_28=+5V` |
| 核心器件 | 正文 Ra-01H 与图纸 Ra-01 Module | `documented_model=Ra-01H`；`schematic_label=Ra-01 Module`；`confirmed_assembly_model=null` |
| 射频 | 正文中的 LoRa 频段 | `product_band_name=868MHz`；`documented_range=803~930MHz`；`frequency_on_schematic=null`；`rf_ic_shown=false`；`matching_network_shown=false` |
| 射频 | 正文中的调制与性能 | `documented_modulations=FSK,GFSK,MSK,GMSK,LoRa,OOK`；`documented_sensitivity=-140dBm minimum`；`documented_max_bitrate=300Kbps`；`parameters_on_schematic=null` |
| 射频 | 天线与 RF 端口 | `documented_internal_antenna=flexible PCB antenna`；`documented_external_antenna=true`；`antenna_on_schematic=false`；`rf_connector=null`；`matching_network=null`；`rf_esd=null` |
| 时钟 | LoRa 子模块时钟 | `crystal_shown=false`；`oscillator_shown=false`；`clock_frequency=null`；`load_capacitors=null` |
| 保护电路 | 电源、SPI 与射频保护 | `5v_input_protection_shown=false`；`regulator_input_cap_shown=false`；`spi_esd_shown=false`；`c1_value=null`；`rf_protection_shown=false` |
| 内存与 Flash | 存储器 | `external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `component.documented-ra01h-conflict`：产品正文列出 Ra-01H，而原理图器件文本为 Ra-01 Module，当前页面无法确认量产 M029 的准确子模块型号与版本。（证据：图 527262b7369d / 第 1 页 / 第 1 页 M1 仅标 Ra-01 Module，无 H 后缀或版本）
- `rf.documented-frequency-range`：产品名与正文描述 868MHz，并列出 803~930MHz 工作范围；原理图没有频率、射频芯片、天线或匹配元件标注，频段需由实际 M1 型号与 RF 设计确认。（证据：图 527262b7369d / 第 1 页 / 第 1 页 M1 作为封装子模块，无 RF 频率或匹配网络）
- `rf.documented-modulation-performance`：产品正文列出 FSK/GFSK/MSK/GMSK/LoRa/OOK、最低 -140dBm 灵敏度和最高 300Kbps；这些参数均未出现在原理图上，需由准确子模块与芯片 datasheet 确认。（证据：图 527262b7369d / 第 1 页 / 第 1 页仅给 M1 数字接口，无调制、灵敏度或比特率标注）
- `rf.antenna-not-visible`：产品正文称内置柔性 PCB 天线和外部天线接口，但当前原理图未画天线、连接器、RF 引脚、匹配网络、开关或 ESD 保护。（证据：图 527262b7369d / 第 1 页 / 第 1 页全图无天线或 RF 网络）
- `clock.radio-clock-not-visible`：M1 以封装模块表示，页面未显示晶振、振荡器、时钟频率或负载电容，内部时钟实现无法确认。（证据：图 527262b7369d / 第 1 页 / 第 1 页 M1 外部仅 SPI/DIO/电源，无时钟器件）
- `protection.interfaces-not-visible`：页面未展示 +5V 输入保护、VR1 输入电容、SPI/控制线 ESD、3V3 去耦容量或射频端保护，实际保护与稳定性器件需结合 PCB/BOM 确认。（证据：图 527262b7369d / 第 1 页 / 第 1 页完整图仅含 M1、J1、VR1、C1）
- `review.radio-module-model`：请用 M029 当前量产 BOM、模块丝印或正式版本原理图确认 M1 是 Ra-01H 还是其他 Ra-01 版本。；原因：产品正文与原理图器件文本不一致。
- `review.frequency-range`：请确认 M029 实际中心频段、可调范围和区域法规配置。；原因：原理图未展开 RF 芯片与频率网络，且准确 M1 版本待定。
- `review.modulation-performance`：请以实际 Ra-01 子模块 datasheet 确认调制模式、接收灵敏度和最大比特率。；原因：这些性能参数未标在当前图纸。
- `review.antenna`：请提供 M1/PCB 的 RF 页面，确认内置天线、外部天线连接器、匹配、切换和 ESD 设计。；原因：当前原理图完全未展示 RF 路径。
- `review.radio-clock`：请确认 LoRa 子模块内部晶振/时钟源、频率和精度。；原因：M1 内部电路未展开。
- `review.protection-decoupling`：请确认 +5V/3V3 去耦与保护、SPI ESD 和 RF 端保护是否在 PCB 或模块内部实现。；原因：当前页面只画一只未标容量的 C1，未展示其他保护。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `527262b7369d077899599a3e8d25ebab57ab5a8665c82d5434c0618df1557591` | `https://static-cdn.m5stack.com/resource/docs/products/module/lora/lora_sch_01.webp` |

---

源文档：`zh_CN/module/lora868.md`

源文档 SHA-256：`5a8511269fd8f4f0e763137dad8a23aa8fd5f0024958f79d65380744d1e03c65`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
