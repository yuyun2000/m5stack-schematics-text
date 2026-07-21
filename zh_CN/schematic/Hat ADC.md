# Hat ADC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat ADC |
| SKU | U069 |
| 产品 ID | `hat-adc-9bc52b24bfa8` |
| 源文档 | `zh_CN/hat/hat-adc.md` |

## 概述

Hat ADC 以 U1 ADS1100 为核心，通过 StickIO 接口连接主机 I2C，总线 SCL/SDA 分别映射到 G26/G0。模拟输入由 P2 两针端子接入，高端经 R3 300 kΩ 与 R4 100 kΩ 分压后送到 VIN+，低端连接 VIN- 并通过 R5 0 Ω 接地。ADS1100 使用 3.3 V 供电，I2C 两线各由 4.7 kΩ 上拉。

## 检索关键词

`Hat ADC`、`U069`、`ADS1100`、`I2C`、`SCL`、`SDA`、`G26`、`G0`、`STICKIO`、`VIN+`、`VIN-`、`P2 Header 2`、`R3 300K`、`R4 100K`、`R5 0R`、`R1 4.7K`、`R2 4.7K`、`+3.3V`、`0x48`、`16-bit ADC`、`0-12V`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ADS1100 | I2C 模数转换器，采样 VIN+/VIN- 差分输入 | 图 78b330bd3a0d / 第 1 页 / B2-C3，U1 ADS1100，VIN+/VIN-/SCL/SDA/VDD/GND |
| P1 | STICKIO | 8 针 StickC HAT 接口，提供 I2C、3.3 V、5 V 与地 | 图 78b330bd3a0d / 第 1 页 / B3-C3，P1 STICKIO pins 1-8 |
| P2 | Header 2 | 两针模拟电压输入端子 | 图 78b330bd3a0d / 第 1 页 / B1-C1，P2 Header 2 pins 1/2 |
| R3/R4 | 300KΩ / 100KΩ | 输入高端到 VIN+ 的电阻缩放网络 | 图 78b330bd3a0d / 第 1 页 / B1-B2，P2 pin1、R3 300KΩ、R4 100KΩ、U1 VIN+ |
| R5 | 0Ω | 将 P2 输入低端/VIN- 连接到 GND | 图 78b330bd3a0d / 第 1 页 / C2，R5 0Ω，VIN- 到 GND |
| R1/R2 | 4.7KΩ | SCL 与 SDA 的 3.3 V I2C 上拉电阻 | 图 78b330bd3a0d / 第 1 页 / B3，R1/R2 4.7KΩ、+3.3V、SCL/SDA |
| C1 | 100nF | ADS1100 3.3 V 电源去耦电容 | 图 78b330bd3a0d / 第 1 页 / C2，C1 100nF、U1 VDD、+3.3V/GND |

## 系统结构

### ADC HAT 架构

P2 模拟输入经 300 kΩ/100 kΩ 电阻网络送入 U1 ADS1100，ADS1100 通过 StickIO I2C 与主机通信并由 3.3 V 供电。

- 参数与网络：`adc=U1 ADS1100`；`input=P2 Header 2`；`input_network=R3 300K; R4 100K; R5 0R`；`host_interface=P1 STICKIO`；`bus=I2C`；`supply=+3.3V`
- 证据：图 78b330bd3a0d / 第 1 页 / 整页：P2/R3/R4/R5/U1/R1/R2/P1

## 核心器件

### ADS1100

U1 原理图值为 ADS1100，pins 1/6 为 VIN+/VIN-，pins 3/4 为 SCL/SDA，pin 5 为 VDD，pin 2 为 GND。

- 参数与网络：`reference=U1`；`part_number=ADS1100`；`pin1=VIN+`；`pin6=VIN-`；`pin3=SCL`；`pin4=SDA`；`pin5=VDD/+3.3V`；`pin2=GND`
- 证据：图 78b330bd3a0d / 第 1 页 / U1 ADS1100 pins 1-6

## 电源

### ADC 3.3 V 电源

U1 VDD 与 C1 100 nF 连接 +3.3 V，U1 GND 与 C1 另一端接地。

- 参数与网络：`device=U1 ADS1100`；`supply=+3.3V`；`decoupling=C1 100nF`；`ground=GND`
- 证据：图 78b330bd3a0d / 第 1 页 / U1 VDD/GND 与 C1 100nF

## 接口

### StickIO 引脚使用

P1 pin1 接 GND，pin2 接 VCC/5VOUT，pin3 接 SCL/G26，pin5 接 SDA/G0，pin7 接 +3.3V/3V3；pins 4/6/8 未连接。

- 参数与网络：`pin1=GND`；`pin2=VCC/5VOUT`；`pin3=SCL/G26`；`pin4=NC/G36`；`pin5=SDA/G0`；`pin6=NC/BAT`；`pin7=+3.3V/3V3`；`pin8=NC/5VIN`
- 证据：图 78b330bd3a0d / 第 1 页 / P1 STICKIO pins 1-8 与连接/NC 标记

### 两针模拟输入

P2 pin1 为输入高端，经 R3 300 kΩ 进入 VIN+ 缩放节点；pin2 为输入低端，直接连接 VIN- 并经 R5 0 Ω 接地。

- 参数与网络：`reference=P2`；`pin1=input high -> R3 300KΩ`；`pin2=input low -> VIN- -> R5 0Ω -> GND`
- 证据：图 78b330bd3a0d / 第 1 页 / P2 pin1/pin2 到 R3/R4/R5/U1 VIN+/VIN-

## 总线

### 主机 I2C

ADS1100 SCL/SDA 连接 P1 StickIO 的 G26/G0，并分别由 R1/R2 4.7 kΩ 上拉到 +3.3 V。

- 参数与网络：`device=U1 ADS1100`；`scl=SCL -> P1 pin3/G26`；`sda=SDA -> P1 pin5/G0`；`scl_pullup=R1 4.7KΩ`；`sda_pullup=R2 4.7KΩ`；`level=+3.3V`
- 证据：图 78b330bd3a0d / 第 1 页 / U1 SCL/SDA、R1/R2 与 P1 G26/G0

## 模拟电路

### 输入缩放网络

R3 300 kΩ 串接输入高端，R4 100 kΩ 跨接 VIN+ 与 VIN-，VIN- 通过 R5 0 Ω 接地，形成以 VIN- 为参考的输入缩放。

- 参数与网络：`series_resistor=R3 300KΩ`；`lower_resistor=R4 100KΩ`；`reference_link=R5 0Ω to GND`；`adc_inputs=VIN+; VIN-`
- 证据：图 78b330bd3a0d / 第 1 页 / R3/R4/R5 与 U1 VIN+/VIN- 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | ADC HAT 架构 | `adc=U1 ADS1100`；`input=P2 Header 2`；`input_network=R3 300K; R4 100K; R5 0R`；`host_interface=P1 STICKIO`；`bus=I2C`；`supply=+3.3V` |
| 核心器件 | ADS1100 | `reference=U1`；`part_number=ADS1100`；`pin1=VIN+`；`pin6=VIN-`；`pin3=SCL`；`pin4=SDA`；`pin5=VDD/+3.3V`；`pin2=GND` |
| 总线 | 主机 I2C | `device=U1 ADS1100`；`scl=SCL -> P1 pin3/G26`；`sda=SDA -> P1 pin5/G0`；`scl_pullup=R1 4.7KΩ`；`sda_pullup=R2 4.7KΩ`；`level=+3.3V` |
| 接口 | StickIO 引脚使用 | `pin1=GND`；`pin2=VCC/5VOUT`；`pin3=SCL/G26`；`pin4=NC/G36`；`pin5=SDA/G0`；`pin6=NC/BAT`；`pin7=+3.3V/3V3`；`pin8=NC/5VIN` |
| 接口 | 两针模拟输入 | `reference=P2`；`pin1=input high -> R3 300KΩ`；`pin2=input low -> VIN- -> R5 0Ω -> GND` |
| 模拟电路 | 输入缩放网络 | `series_resistor=R3 300KΩ`；`lower_resistor=R4 100KΩ`；`reference_link=R5 0Ω to GND`；`adc_inputs=VIN+; VIN-` |
| 电源 | ADC 3.3 V 电源 | `device=U1 ADS1100`；`supply=+3.3V`；`decoupling=C1 100nF`；`ground=GND` |
| 总线地址 | ADS1100 I2C 地址 | `reference=U1`；`part_number=ADS1100`；`claimed_address_7bit=0x48`；`schematic_address_text=not printed` |
| 模拟电路 | 模块输入量程 | `confirmed_network=R3 300KΩ; R4 100KΩ; R5 0Ω`；`claimed_module_range=0-12V`；`claimed_adc_range=-5V to +5V differential` |
| 模拟电路 | ADC 分辨率、增益与数据率 | `claimed_resolution=16-bit`；`claimed_pga=1; 2; 4; 8`；`claimed_data_rate=8-128SPS`；`claimed_noise=4uVp-p`；`claimed_calibration=continuous self-calibration` |

## 待确认事项

- `address.ads1100`：产品正文给出 ADS1100 地址 0x48，但原理图只标器件型号和 I2C 网络，未直接印出十六进制地址或地址选择后缀。（证据：图 78b330bd3a0d / 第 1 页 / U1 ADS1100 与 SCL/SDA，未见 0x48）
- `analog.input-range`：原理图确认 300 kΩ/100 kΩ/0 Ω 输入网络，但未直接标注整机 0–12 V 输入范围或允许的 ADC 差分输入范围。（证据：图 78b330bd3a0d / 第 1 页 / P2/R3/R4/R5/U1 输入网络无电压范围文本）
- `analog.adc-capabilities`：原理图未直接标注 ADS1100 的 16 位分辨率、PGA 1/2/4/8、8–128 SPS、噪声或自校准能力。（证据：图 78b330bd3a0d / 第 1 页 / U1 仅标 ADS1100，不列性能参数）
- `review.ads1100-address`：请用 ADS1100 完整订货后缀或 datasheet 确认 7-bit I2C 地址 0x48。；原因：原理图未直接印出地址。
- `review.input-range`：请用 ADS1100 datasheet 与容差分析复核模块 0–12 V 量程和 ADC 差分输入限制。；原因：原理图只给出电阻网络，不列额定量程。
- `review.adc-capabilities`：请用 ADS1100 datasheet 复核分辨率、PGA、数据率、噪声与自校准参数。；原因：这些器件性能未印在原理图中。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `78b330bd3a0d7bad366fcbaf4358f95d70b51618bc27551ab4752599ed36dc7c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/865/U069-StickHat_ADC-SCHE_page_01.png` |

---

源文档：`zh_CN/hat/hat-adc.md`

源文档 SHA-256：`19f7ddc741ee89e46aa6f37c32ecc3cc5cdeb742e541f3eb93275dfc40dd8afc`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
