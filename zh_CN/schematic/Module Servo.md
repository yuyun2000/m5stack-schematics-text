# Module Servo 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module Servo |
| SKU | M014 |
| 产品 ID | `module-servo-47e4512cdf0a` |
| 源文档 | `zh_CN/module/servo.md` |

## 概述

Module Servo 以 U2 ATMEGA328 为 12 路舵机控制器，CH0–CH11 分别连接 P2–P13 三针接口，每路同时提供 VCC 与 GND。U2 通过 SDA/SCL 与 J4 M5Stack_BUS 通信，RESET 连接主机 EN，J1 提供 ISP，Y1 16 MHz 晶振提供时钟。P1 外部 VCC 经 U1 LM2596SX-5.0/NOPB 转换为 +5 V，为 U2、ISP 与 M5-Bus 供电；舵机接口自身使用原始 VCC。

## 检索关键词

`Module Servo`、`M014`、`ATMEGA328`、`LM2596SX-5.0/NOPB`、`16MHz`、`I2C`、`0x53`、`SDA`、`SCL`、`GPIO21`、`GPIO22`、`RESET`、`EN`、`ISP_Download`、`MOSI`、`MISO`、`SCK`、`CH0`、`CH1`、`CH2`、`CH3`、`CH4`、`CH5`、`CH6`、`CH7`、`CH8`、`CH9`、`CH10`、`CH11`、`P2-P13`、`servo`、`VCC`、`+5V`、`+3V3`、`M5Stack_BUS`、`XT30`、`DC 5-7V`、`14W`、`L1 0630/330`、`R1/R2 470Ω`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ATMEGA328 | 12 路舵机 PWM 控制与 I2C 从机 MCU | 图 6fdc02048c87 / 第 1 页 / 中央 U2 ATMEGA328 pins1-32 |
| U1 | LM2596SX-5.0/NOPB | 从外部 VCC 产生 +5 V 的固定输出开关稳压器 | 图 6fdc02048c87 / 第 1 页 / 左上 U1 LM2596SX-5.0/NOPB/L1/C1-C4 |
| P2-P13 | Header 3 | 12 组舵机接口，每组提供 GND、VCC 与 CH0-CH11 控制信号 | 图 6fdc02048c87 / 第 1 页 / 左侧 P2-P13 Header 3、CH0-CH11 |
| P1 | Header 2 | 外部 VCC 与 GND 两针电源输入接口 | 图 6fdc02048c87 / 第 1 页 / 左上 P1 Header 2/VCC/GND |
| J1 | ISP_Download | ATMEGA328 的 +5 V、RESET、SCK、MISO、MOSI、GND 六针下载接口 | 图 6fdc02048c87 / 第 1 页 / 右上 J1 ISP_Download pins1-6 |
| J4 | M5Stack_BUS | 30 针主机接口，提供 +5 V、+3V3、I2C、EN 与 GPIO 网络 | 图 6fdc02048c87 / 第 1 页 / 右下 J4 M5Stack_BUS pins1-30 |
| Y1/C5/C6 | 16MHz / 22pF / 22pF | ATMEGA328 外部 16 MHz 晶振与负载电容 | 图 6fdc02048c87 / 第 1 页 / 上中 Y1 16MHz/C5/C6/XTAL1/XTAL2 |
| R1/R2/R3/R7 | 470Ω / 470Ω / 470Ω / 10KΩ | SDA/SCL/RESET 串联电阻与 RESET/EN 的 3.3 V 上拉 | 图 6fdc02048c87 / 第 1 页 / 中右 SDA/R1、SCL/R2、RESET/R3、EN/R7 |
| R4-R6 | 0Ω | U2 PB0/PB1/PB2 到 GND 的三个 0 Ω 配置位置 | 图 6fdc02048c87 / 第 1 页 / 中左 R4/R5/R6 0Ω to GND at U2 PB0-PB2 |
| L1/C1-C4 | 0630/330 / 100uF/100nF | LM2596 输入输出储能、滤波与去耦网络 | 图 6fdc02048c87 / 第 1 页 / 左上 L1 0630/330/C1-C4/VCC/+5V |

## 系统结构

### Module Servo 系统架构

U2 ATMEGA328 控制 P2-P13 十二路舵机接口，通过 I2C 连接 J4 主机并通过 J1 ISP 编程；U1 将外部 VCC 转换为系统 +5 V。

- 参数与网络：`controller=U2 ATMEGA328`；`channels=P2-P13 / CH0-CH11`；`host=J4 M5Stack_BUS`；`bus=I2C`；`debug=J1 ISP_Download`；`power=P1 VCC -> U1 LM2596SX-5.0/NOPB -> +5V`
- 证据：图 6fdc02048c87 / 第 1 页 / 整页 P1/U1/P2-P13/U2/J1/J4

## 核心器件

### ATMEGA328 舵机通道映射

CH0-CH3 连接 U2 PD0-PD3 pins30/31/32/1，CH4-CH7 连接 PD4-PD7 pins2/9/10/11，CH8-CH11 连接 PC0-PC3 pins23-26。

- 参数与网络：`ch0_ch3=CH0 PD0 pin30; CH1 PD1 pin31; CH2 PD2 pin32; CH3 PD3 pin1`；`ch4_ch7=CH4 PD4 pin2; CH5 PD5 pin9; CH6 PD6 pin10; CH7 PD7 pin11`；`ch8_ch11=CH8 PC0 pin23; CH9 PC1 pin24; CH10 PC2 pin25; CH11 PC3 pin26`
- 证据：图 6fdc02048c87 / 第 1 页 / U2 left-side CH0-CH11 pin labels

## 电源

### 外部 VCC 输入

P1 Header 2 pin1 接 VCC、pin2 接 GND；VCC 同时进入 U1 VIN 并直接供给 P2-P13 舵机接口 pin2。

- 参数与网络：`connector=P1 Header 2`；`positive=pin1 VCC`；`negative=pin2 GND`；`loads=U1 VIN pin1 and servo headers pin2`
- 证据：图 6fdc02048c87 / 第 1 页 / P1 VCC/GND; U1 VIN; P2-P13 VCC

### LM2596 固定 5 V 输出

U1 LM2596SX-5.0/NOPB VIN pin1 接 VCC、ON/OFF pin5 未外接、GND pin3 接地、OUT pin2 经 L1 输出 +5 V，FB pin4 取样输出节点。

- 参数与网络：`input=VCC -> VIN pin1`；`converter=U1 LM2596SX-5.0/NOPB`；`enable=ON/OFF pin5 not connected`；`ground=pin3`；`switch_output=OUT pin2 -> L1`；`feedback=FB pin4 -> +5V`；`output=+5V`
- 证据：图 6fdc02048c87 / 第 1 页 / Left top U1/L1/+5V

### 稳压器输入输出滤波

VCC 输入配置 C3 100 nF 与 C1 100 uF，+5 V 输出配置 C4 100 nF 与 C2 100 uF，L1 标记 0630/330。

- 参数与网络：`input_caps=C3 100nF; C1 100uF`；`output_caps=C4 100nF; C2 100uF`；`inductor=L1 0630/330`；`input_rail=VCC`；`output_rail=+5V`
- 证据：图 6fdc02048c87 / 第 1 页 / Left top C1-C4/L1/VCC/+5V

### ATMEGA328 5 V 供电

U2 VCC pins4/6 与 AVCC pin18 接 +5 V，GND pins3/5/21 接地；J1 ISP pin1 和 J4 pin28 也接 +5 V。

- 参数与网络：`mcu_vcc=pins4/6 +5V`；`mcu_avcc=pin18 +5V`；`mcu_ground=pins3/5/21`；`isp=J1 pin1 +5V`；`m5bus=J4 pin28 +5V`
- 证据：图 6fdc02048c87 / 第 1 页 / U2 power pins; J1 VCC; J4 +5V

## 接口

### 12 组三针舵机接口

P2-P13 每个 Header 3 的 pin1 接 GND、pin2 接 VCC、pin3 分别接 CH0-CH11。

- 参数与网络：`connectors=P2-P13`；`ground=pin1`；`power=pin2 VCC`；`signal=pin3 CH0-CH11`；`count=12`
- 证据：图 6fdc02048c87 / 第 1 页 / Left P2-P13 Header 3 rows

### M5Stack_BUS 使用网络

J4 使用 pins1/3/5 GND、pin6 EN/RESET、pin12 +3V3、pin17 GPIO21/SDA、pin18 GPIO22/SCL 与 pin28 +5 V；其余页面未连接功能网络。

- 参数与网络：`ground=pins1/3/5`；`reset=pin6 EN`；`3v3=pin12`；`i2c=pin17 GPIO21 SDA; pin18 GPIO22 SCL`；`5v=pin28`
- 证据：图 6fdc02048c87 / 第 1 页 / Right bottom J4 M5Stack_BUS pins1-30

## 总线

### ATMEGA328 I2C

U2 SDA pin27 经 R1 470 Ω 连接 GPIO21/J4 pin17，SCL pin28 经 R2 470 Ω 连接 GPIO22/J4 pin18；页面未画 I2C 上拉。

- 参数与网络：`device=U2 ATMEGA328`；`sda=pin27 -> R1 470Ω -> GPIO21/J4 pin17`；`scl=pin28 -> R2 470Ω -> GPIO22/J4 pin18`；`pullups=not shown`；`direction=bidirectional SDA; host clock SCL`
- 证据：图 6fdc02048c87 / 第 1 页 / U2 SDA/SCL and R1/R2 to J4 GPIO21/GPIO22

## GPIO 与控制信号

### PB0/PB1/PB2 下拉配置

U2 PB0 pin12、PB1 pin13、PB2 pin14 分别通过 R4/R5/R6 0 Ω 直接接 GND。

- 参数与网络：`pb0=pin12 -> R4 0Ω -> GND`；`pb1=pin13 -> R5 0Ω -> GND`；`pb2=pin14 -> R6 0Ω -> GND`
- 证据：图 6fdc02048c87 / 第 1 页 / Middle left R4-R6/U2 PB0-PB2

## 时钟

### 16 MHz MCU 时钟

U2 XTAL1 pin7 与 XTAL2 pin8 连接 Y1 16 MHz 晶振，C5/C6 各 22 pF 对地。

- 参数与网络：`xtal1=U2 pin7`；`xtal2=U2 pin8`；`crystal=Y1 16MHz`；`load_caps=C5/C6 22pF to GND`
- 证据：图 6fdc02048c87 / 第 1 页 / Top middle U2 XTAL1/XTAL2/Y1/C5/C6

## 复位

### ATMEGA328 RESET 与主机 EN

U2 RESET pin29 经 R3 470 Ω 连接 J4 EN pin6，R7 10 kΩ 将 EN 侧上拉到 +3V3；RESET 同时连接 J1 ISP pin2。

- 参数与网络：`target=U2 RESET pin29`；`series=R3 470Ω`；`host=J4 pin6 EN`；`pullup=R7 10K to +3V3`；`debug=J1 pin2 RESET`
- 证据：图 6fdc02048c87 / 第 1 页 / U2 RESET/R3/EN/R7/+3V3; J1 RESET

## 保护电路

### 外部电源保护

P1 到舵机 VCC 和 U1 的路径上未画保险丝、TVS、反接保护或独立负载开关。

- 参数与网络：`fuse=not shown`；`tvs=not shown`；`reverse_protection=not shown`；`load_switch=not shown`；`path=P1 VCC directly to servo headers and U1 VIN`
- 证据：图 6fdc02048c87 / 第 1 页 / P1/VCC/U1/P2-P13 direct path

## 调试与烧录

### ATMEGA328 ISP 下载口

J1 ISP_Download pins1-6 分别为 +5 V、RESET、SCK、MISO、MOSI、GND，并连接 U2 对应引脚。

- 参数与网络：`pin1=+5V`；`pin2=RESET`；`pin3=SCK`；`pin4=MISO`；`pin5=MOSI`；`pin6=GND`；`device=U2 ATMEGA328`
- 证据：图 6fdc02048c87 / 第 1 页 / Right top J1 ISP_Download and U2 SPI/reset labels

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module Servo 系统架构 | `controller=U2 ATMEGA328`；`channels=P2-P13 / CH0-CH11`；`host=J4 M5Stack_BUS`；`bus=I2C`；`debug=J1 ISP_Download`；`power=P1 VCC -> U1 LM2596SX-5.0/NOPB -> +5V` |
| 核心器件 | ATMEGA328 舵机通道映射 | `ch0_ch3=CH0 PD0 pin30; CH1 PD1 pin31; CH2 PD2 pin32; CH3 PD3 pin1`；`ch4_ch7=CH4 PD4 pin2; CH5 PD5 pin9; CH6 PD6 pin10; CH7 PD7 pin11`；`ch8_ch11=CH8 PC0 pin23; CH9 PC1 pin24; CH10 PC2 pin25; CH11 PC3 pin26` |
| 接口 | 12 组三针舵机接口 | `connectors=P2-P13`；`ground=pin1`；`power=pin2 VCC`；`signal=pin3 CH0-CH11`；`count=12` |
| 电源 | 外部 VCC 输入 | `connector=P1 Header 2`；`positive=pin1 VCC`；`negative=pin2 GND`；`loads=U1 VIN pin1 and servo headers pin2` |
| 电源 | LM2596 固定 5 V 输出 | `input=VCC -> VIN pin1`；`converter=U1 LM2596SX-5.0/NOPB`；`enable=ON/OFF pin5 not connected`；`ground=pin3`；`switch_output=OUT pin2 -> L1`；`feedback=FB pin4 -> +5V`；`output=+5V` |
| 电源 | 稳压器输入输出滤波 | `input_caps=C3 100nF; C1 100uF`；`output_caps=C4 100nF; C2 100uF`；`inductor=L1 0630/330`；`input_rail=VCC`；`output_rail=+5V` |
| 电源 | ATMEGA328 5 V 供电 | `mcu_vcc=pins4/6 +5V`；`mcu_avcc=pin18 +5V`；`mcu_ground=pins3/5/21`；`isp=J1 pin1 +5V`；`m5bus=J4 pin28 +5V` |
| 总线 | ATMEGA328 I2C | `device=U2 ATMEGA328`；`sda=pin27 -> R1 470Ω -> GPIO21/J4 pin17`；`scl=pin28 -> R2 470Ω -> GPIO22/J4 pin18`；`pullups=not shown`；`direction=bidirectional SDA; host clock SCL` |
| 复位 | ATMEGA328 RESET 与主机 EN | `target=U2 RESET pin29`；`series=R3 470Ω`；`host=J4 pin6 EN`；`pullup=R7 10K to +3V3`；`debug=J1 pin2 RESET` |
| 时钟 | 16 MHz MCU 时钟 | `xtal1=U2 pin7`；`xtal2=U2 pin8`；`crystal=Y1 16MHz`；`load_caps=C5/C6 22pF to GND` |
| 调试与烧录 | ATMEGA328 ISP 下载口 | `pin1=+5V`；`pin2=RESET`；`pin3=SCK`；`pin4=MISO`；`pin5=MOSI`；`pin6=GND`；`device=U2 ATMEGA328` |
| GPIO 与控制信号 | PB0/PB1/PB2 下拉配置 | `pb0=pin12 -> R4 0Ω -> GND`；`pb1=pin13 -> R5 0Ω -> GND`；`pb2=pin14 -> R6 0Ω -> GND` |
| 接口 | M5Stack_BUS 使用网络 | `ground=pins1/3/5`；`reset=pin6 EN`；`3v3=pin12`；`i2c=pin17 GPIO21 SDA; pin18 GPIO22 SCL`；`5v=pin28` |
| 保护电路 | 外部电源保护 | `fuse=not shown`；`tvs=not shown`；`reverse_protection=not shown`；`load_switch=not shown`；`path=P1 VCC directly to servo headers and U1 VIN` |
| 总线地址 | Module Servo I2C 地址 | `document_address=0x53`；`device=U2 ATMEGA328`；`schematic_address=not printed`；`implementation=firmware-dependent` |
| 电源 | XT30 与 5.5×2.1 mm 输入接口 | `document_connector_1=XT30 female`；`document_connector_2=5.5mm x 2.1mm`；`schematic_connector=P1 Header 2`；`connector_references=not shown separately` |
| 电源 | DC 5–7 V 输入范围 | `document_range=DC5-7V`；`schematic_rail=VCC`；`minimum=not printed`；`maximum=not printed` |
| 电源 | 14 W 最大功率 | `document_power=14W`；`schematic_current=not shown`；`connector_rating=not shown`；`thermal_conditions=not shown` |

## 待确认事项

- `address.i2c`：产品正文声明 I2C 地址为 0x53，但原理图只显示 ATMEGA328 SDA/SCL，数值地址由固件实现且未打印在页面。（证据：图 6fdc02048c87 / 第 1 页 / U2 SDA/SCL without address label）
- `power.input-connectors`：产品正文称具有 XT30 母头和 5.5×2.1 mm 适配器接口，但原理图只画 P1 Header 2，未给两个连接器位号或机械规格。（证据：图 6fdc02048c87 / 第 1 页 / P1 Header 2 is only external power connector shown）
- `power.input-range`：产品正文声明 DC 5–7 V 输入，原理图仅用 VCC 网络名连接 P1、舵机和 U1，没有打印允许输入范围。（证据：图 6fdc02048c87 / 第 1 页 / P1/VCC/U1 input path lacks voltage range）
- `power.maximum-output`：产品正文称最大功率 14 W，但原理图没有电流额定值、铜箔/连接器限制、散热条件或功率标注。（证据：图 6fdc02048c87 / 第 1 页 / VCC/servo headers/U1 path lacks power rating）
- `review.i2c-address`：请用 ATMEGA328 内置固件或 I2C 扫描确认 Module Servo 地址为 0x53。；原因：地址由固件实现，未印在原理图。
- `review.input-connectors`：请用 PCB/BOM/装配资料确认 XT30 与 5.5×2.1 mm 两种电源连接器的位号和极性。；原因：当前原理图只显示通用两针 P1。
- `review.input-range`：请用舵机电源规格、U1 输入要求和实板测试确认 DC 5–7 V 输入边界。；原因：允许电压范围未标在原理图。
- `review.maximum-output`：请按连接器、电源走线、散热和多舵机负载条件复核 14 W 最大功率。；原因：原理图没有额定电流或热条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6fdc02048c87a6c7bfd12ce4c8c24902d2502095362098e407ff295e339f496b` | `https://static-cdn.m5stack.com/resource/docs/products/module/servo/servo_sch_01.webp` |

---

源文档：`zh_CN/module/servo.md`

源文档 SHA-256：`bb9932fc06e33e20f30115b484678405ea3a52e56132eb48c58c37364c49a4eb`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
