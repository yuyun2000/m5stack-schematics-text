# Module Stepmotor 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module Stepmotor |
| SKU | M012 |
| 产品 ID | `module-stepmotor-fd1897c65a3e` |
| 源文档 | `zh_CN/module/stepmotor.md` |

## 概述

Module Stepmotor 以 U1 ATMEGA328 控制三块标为 A4988_M 的步进驱动插座 M1–M3，分别使用 PX/DX、PY/DY、PZ/DZ 作为 X/Y/Z 的 STEP/DIR，并共享 OE 与 MS1/MS2/MS3。J3/J4/J5 四针端子分别输出三台双极步进电机的 2B/2A/1A/1B 绕组，驱动功率使用外部 VCC，逻辑使用 U2 LM2596SX-5.0/NOPB 生成的 +5 V。U1 通过 SDA/SCL 与 M5-Bus 通信，并提供 P2 调试/扩展排针；原理图没有显示 RS-485 收发器。

## 检索关键词

`Module Stepmotor`、`M012`、`ATMEGA328`、`A4988_M`、`DRV8825`、`LM2596SX-5.0/NOPB`、`I2C`、`0x70`、`GRBL`、`PX`、`DX`、`PY`、`DY`、`PZ`、`DZ`、`STEP_X`、`DIR_X`、`STEP_Y`、`DIR_Y`、`STEP_Z`、`DIR_Z`、`OE`、`MS1`、`MS2`、`MS3`、`J3`、`J4 motor`、`J5`、`2B`、`2A`、`1A`、`1B`、`VCC`、`+5V`、`M5Stack_BUS`、`SDA`、`SCL`、`GPIO16`、`GPIO17`、`XT30`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ATMEGA328 | 三轴步进控制 MCU，生成 X/Y/Z STEP/DIR、OE、微步配置并通过 I2C 通信 | 图 17b7ea817633 / 第 1 页 / 上中 U1 ATMEGA328 pins1-32 |
| M1/M2/M3 | A4988_M | X/Y/Z 三轴步进驱动模块插座，接收 STEP/DIR/OE/MS1-MS3 并输出两相绕组 | 图 17b7ea817633 / 第 1 页 / 下部 M1/M2/M3 A4988_M pins1-16 |
| U2 | LM2596SX-5.0/NOPB | 从外部 VCC 生成 +5 V 逻辑电源的固定输出开关稳压器 | 图 17b7ea817633 / 第 1 页 / 左上 U2 LM2596SX-5.0/NOPB/L1/C1-C3 |
| J3/J4/J5 | Header 4 | X/Y/Z 三台双极步进电机的四线绕组输出端子 | 图 17b7ea817633 / 第 1 页 / 下部 J3/J4/J5 Header 4 connected to M1/M2/M3 outputs |
| P1 | Header 2 | 外部 VCC 与 GND 电源输入接口 | 图 17b7ea817633 / 第 1 页 / 左上 P1 Header 2/VCC/GND |
| P2 | Header 7X2 | ATMEGA328 SPI、RESET、PB0-PB2、A0-A3、+5 V 与 GND 扩展/下载排针 | 图 17b7ea817633 / 第 1 页 / 中左 P2 Header 7X2 pins1-14 |
| J1 | M5Stack_BUS | 30 针主机接口，提供 +5 V、+3V3、I2C、GPIO16/17 与其他通用 GPIO | 图 17b7ea817633 / 第 1 页 / 右下 J1 M5Stack_BUS pins1-30 |
| D1/R1 | LED / 470Ω | +5 V 电源指示灯及限流电阻 | 图 17b7ea817633 / 第 1 页 / 右中 +5V/R1 470Ω/D1/GND |
| L1/C1-C3 | 0630/330 / 100uF/100nF/10uF | LM2596 输出储能、滤波与去耦网络 | 图 17b7ea817633 / 第 1 页 / 左上 L1 0630/330/C1-C3/+5V |

## 系统结构

### Module Stepmotor 系统架构

U1 ATMEGA328 通过 I2C 接收主机命令，驱动三块 M1-M3 A4988_M 模块控制 X/Y/Z 电机；U2 从外部 VCC 生成 +5 V 逻辑电源。

- 参数与网络：`controller=U1 ATMEGA328`；`drivers=M1/M2/M3 A4988_M`；`axes=X/Y/Z`；`host=J1 M5Stack_BUS`；`bus=I2C`；`power=P1 VCC -> U2 LM2596SX-5.0/NOPB -> +5V`；`motor_power=VCC`
- 证据：图 17b7ea817633 / 第 1 页 / 整页 P1/U2/U1/M1-M3/J1

## 核心器件

### ATMEGA328 三轴 STEP/DIR

U1 PX pin32/DX pin9 控制 X 轴，PY pin1/DY pin10 控制 Y 轴，PZ pin2/DZ pin11 控制 Z 轴，并分别连接 M1/M2/M3 STEP/DIR pins7/8。

- 参数与网络：`x=U1 PX pin32 -> M1 STEP pin7; DX pin9 -> M1 DIR pin8`；`y=U1 PY pin1 -> M2 STEP pin7; DY pin10 -> M2 DIR pin8`；`z=U1 PZ pin2 -> M3 STEP pin7; DZ pin11 -> M3 DIR pin8`
- 证据：图 17b7ea817633 / 第 1 页 / U1 PD2-PD7 PX/PY/PZ/DX/DY/DZ and M1-M3 STEP/DIR

## 电源

### 步进驱动功率与逻辑供电

M1-M3 VMOT pin16 接外部 VCC、VDD pin9 接 +5 V，GND pins10/15 接地；RST/SLEEP pins5/6 连接 +5 V。

- 参数与网络：`motor_supply=VMOT pin16 VCC`；`logic_supply=VDD pin9 +5V`；`ground=pins10/15`；`reset_sleep=pins5/6 +5V`；`drivers=M1/M2/M3`
- 证据：图 17b7ea817633 / 第 1 页 / Lower M1-M3 VMOT/VDD/GND/RST/SLEEP

### 外部 VCC 电源输入

P1 Header 2 pin1 接 VCC、pin2 接 GND；VCC 直接连接 U2 VIN 与三块驱动的 VMOT。

- 参数与网络：`connector=P1 Header 2`；`positive=pin1 VCC`；`negative=pin2 GND`；`loads=U2 VIN; M1-M3 VMOT`
- 证据：图 17b7ea817633 / 第 1 页 / P1/VCC/U2 VIN and M1-M3 VMOT

### LM2596 5 V 逻辑电源

U2 LM2596SX-5.0/NOPB VIN pin1 接 VCC、OUT pin2 经 L1 输出 +5 V、FB pin4取样 +5 V、GND pin3 接地，ON/OFF pin5 未外接。

- 参数与网络：`input=VCC`；`converter=U2 LM2596SX-5.0/NOPB`；`output=+5V`；`inductor=L1 0630/330`；`feedback=FB pin4`；`enable=ON/OFF pin5 not connected`；`output_caps=C2 100nF; C3 10uF; C1 100uF`
- 证据：图 17b7ea817633 / 第 1 页 / Left top U2/L1/C1-C3/+5V

### ATMEGA328 供电

U1 VCC pins4/6 与 AVCC pin18 接 +5 V，GND pins3/5/21 接地；D1 经 R1 470 Ω 从 +5 V 到 GND 指示电源。

- 参数与网络：`vcc=pins4/6 +5V`；`avcc=pin18 +5V`；`ground=pins3/5/21`；`indicator=+5V -> R1 470Ω -> D1 -> GND`
- 证据：图 17b7ea817633 / 第 1 页 / U1 VCC/AVCC/GND and right D1/R1

## 接口

### 三路四线电机输出

M1/M2/M3 的 2B/2A/1A/1B pins14/13/12/11 分别连接 J3/J4/J5 pins4/3/2/1。

- 参数与网络：`x_connector=J3`；`y_connector=J4`；`z_connector=J5`；`pin4=2B`；`pin3=2A`；`pin2=1A`；`pin1=1B`；`connector_type=Header 4`
- 证据：图 17b7ea817633 / 第 1 页 / Lower M1-J3, M2-J4, M3-J5 output wiring

### GPIO16/GPIO17 主机映射

U1 PD1 pin31 标 GPIO16、PD0 pin30 标 GPIO17，并分别连接 J1 M5-Bus pins15/16；这些网络与 X/Y/Z STEP/DIR 为不同引脚。

- 参数与网络：`gpio16=U1 PD1 pin31 -> J1 pin15`；`gpio17=U1 PD0 pin30 -> J1 pin16`；`step_dir=PX/PY/PZ/DX/DY/DZ on PD2-PD7`
- 证据：图 17b7ea817633 / 第 1 页 / U1 GPIO16/GPIO17 labels and J1 pins15/16

### M5Stack_BUS 使用网络

J1 使用 pins1/3/5 GND、pin12 +3V3、pins15/16 GPIO16/GPIO17、pins17/18 SDA/SCL、pin28 +5 V；GPIO36、GPIO26、GPIO13 等总线标签在本页未连接功能电路。

- 参数与网络：`ground=pins1/3/5`；`3v3=pin12`；`mcu_gpio=pin15 GPIO16; pin16 GPIO17`；`i2c=pin17 SDA; pin18 SCL`；`5v=pin28`；`unused_labels=GPIO36/GPIO26/GPIO13 and others`
- 证据：图 17b7ea817633 / 第 1 页 / Right bottom J1 M5Stack_BUS pins1-30

## 总线

### ATMEGA328 I2C

U1 SDA pin27 与 SCL pin28 连接 J1 M5-Bus 对应 SDA/GPIO21 pin17 和 SCL/GPIO22 pin18；页面未画 I2C 上拉电阻。

- 参数与网络：`device=U1 ATMEGA328`；`sda=U1 pin27 -> SDA -> J1 pin17 GPIO21`；`scl=U1 pin28 -> SCL -> J1 pin18 GPIO22`；`pullups=not shown`
- 证据：图 17b7ea817633 / 第 1 页 / U1 SDA/SCL and J1 pin17/18

## GPIO 与控制信号

### 共享 OE 与微步配置

M1-M3 的 ENA pin1 共用 OE，MS1/MS2/MS3 pins2/3/4 分别共用同名网络；OE 来自 U1 PB0 pin12。

- 参数与网络：`enable=U1 PB0 pin12 OE -> M1-M3 ENA pin1`；`microstep_1=MS1 -> all driver pin2`；`microstep_2=MS2 -> all driver pin3`；`microstep_3=MS3 -> all driver pin4`
- 证据：图 17b7ea817633 / 第 1 页 / U1 PB0/OE and lower M1-M3 OE/MS1/MS2/MS3

## 时钟

### ATMEGA328 时钟引脚

U1 XTAL1 pin7 与 XTAL2 pin8 只标网络名，页面没有画晶振、谐振器、负载电容或频率。

- 参数与网络：`xtal1=pin7`；`xtal2=pin8`；`crystal=not shown`；`frequency=not shown`；`load_caps=not shown`
- 证据：图 17b7ea817633 / 第 1 页 / U1 XTAL1/XTAL2 pins7/8

## 保护电路

### 电机电源保护

P1 VCC 到 M1-M3 VMOT 与 U2 VIN 的路径上未画保险丝、TVS、反接保护或负载开关。

- 参数与网络：`fuse=not shown`；`tvs=not shown`；`reverse_protection=not shown`；`load_switch=not shown`；`path=P1 VCC directly to VMOT/U2 VIN`
- 证据：图 17b7ea817633 / 第 1 页 / P1/VCC/U2/M1-M3 direct path

## 调试与烧录

### P2 调试扩展排针

P2 Header 7X2 引出 SCK、MISO、MOSI、PB2、PB1、PB0、+5 V、RESET、A3、A2、A1、A0 与 GND。

- 参数与网络：`connector=P2 Header 7X2`；`left=SCK/MISO/MOSI/PB2/PB1/PB0/+5V`；`right=RESET/A3/A2/A1/A0/GND`；`device=U1 ATMEGA328`
- 证据：图 17b7ea817633 / 第 1 页 / Middle left P2 Header 7X2 labels

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module Stepmotor 系统架构 | `controller=U1 ATMEGA328`；`drivers=M1/M2/M3 A4988_M`；`axes=X/Y/Z`；`host=J1 M5Stack_BUS`；`bus=I2C`；`power=P1 VCC -> U2 LM2596SX-5.0/NOPB -> +5V`；`motor_power=VCC` |
| 核心器件 | ATMEGA328 三轴 STEP/DIR | `x=U1 PX pin32 -> M1 STEP pin7; DX pin9 -> M1 DIR pin8`；`y=U1 PY pin1 -> M2 STEP pin7; DY pin10 -> M2 DIR pin8`；`z=U1 PZ pin2 -> M3 STEP pin7; DZ pin11 -> M3 DIR pin8` |
| GPIO 与控制信号 | 共享 OE 与微步配置 | `enable=U1 PB0 pin12 OE -> M1-M3 ENA pin1`；`microstep_1=MS1 -> all driver pin2`；`microstep_2=MS2 -> all driver pin3`；`microstep_3=MS3 -> all driver pin4` |
| 电源 | 步进驱动功率与逻辑供电 | `motor_supply=VMOT pin16 VCC`；`logic_supply=VDD pin9 +5V`；`ground=pins10/15`；`reset_sleep=pins5/6 +5V`；`drivers=M1/M2/M3` |
| 接口 | 三路四线电机输出 | `x_connector=J3`；`y_connector=J4`；`z_connector=J5`；`pin4=2B`；`pin3=2A`；`pin2=1A`；`pin1=1B`；`connector_type=Header 4` |
| 电源 | 外部 VCC 电源输入 | `connector=P1 Header 2`；`positive=pin1 VCC`；`negative=pin2 GND`；`loads=U2 VIN; M1-M3 VMOT` |
| 电源 | LM2596 5 V 逻辑电源 | `input=VCC`；`converter=U2 LM2596SX-5.0/NOPB`；`output=+5V`；`inductor=L1 0630/330`；`feedback=FB pin4`；`enable=ON/OFF pin5 not connected`；`output_caps=C2 100nF; C3 10uF; C1 100uF` |
| 电源 | ATMEGA328 供电 | `vcc=pins4/6 +5V`；`avcc=pin18 +5V`；`ground=pins3/5/21`；`indicator=+5V -> R1 470Ω -> D1 -> GND` |
| 总线 | ATMEGA328 I2C | `device=U1 ATMEGA328`；`sda=U1 pin27 -> SDA -> J1 pin17 GPIO21`；`scl=U1 pin28 -> SCL -> J1 pin18 GPIO22`；`pullups=not shown` |
| 接口 | GPIO16/GPIO17 主机映射 | `gpio16=U1 PD1 pin31 -> J1 pin15`；`gpio17=U1 PD0 pin30 -> J1 pin16`；`step_dir=PX/PY/PZ/DX/DY/DZ on PD2-PD7` |
| 调试与烧录 | P2 调试扩展排针 | `connector=P2 Header 7X2`；`left=SCK/MISO/MOSI/PB2/PB1/PB0/+5V`；`right=RESET/A3/A2/A1/A0/GND`；`device=U1 ATMEGA328` |
| 时钟 | ATMEGA328 时钟引脚 | `xtal1=pin7`；`xtal2=pin8`；`crystal=not shown`；`frequency=not shown`；`load_caps=not shown` |
| 接口 | M5Stack_BUS 使用网络 | `ground=pins1/3/5`；`3v3=pin12`；`mcu_gpio=pin15 GPIO16; pin16 GPIO17`；`i2c=pin17 SDA; pin18 SCL`；`5v=pin28`；`unused_labels=GPIO36/GPIO26/GPIO13 and others` |
| 保护电路 | 电机电源保护 | `fuse=not shown`；`tvs=not shown`；`reverse_protection=not shown`；`load_switch=not shown`；`path=P1 VCC directly to VMOT/U2 VIN` |
| 总线地址 | Module Stepmotor I2C 地址 | `document_address=0x70`；`device=U1 ATMEGA328`；`schematic_address=not printed`；`implementation=firmware-dependent` |
| 核心器件 | A4988 与 DRV8825 驱动板型号 | `schematic=M1/M2/M3 A4988_M`；`document=3x DRV8825`；`resolved_variant=null` |
| GPIO 与控制信号 | 最高 1/32 微步能力 | `document_max=1/32`；`visible_control=MS1/MS2/MS3`；`schematic_driver=A4988_M`；`document_driver=DRV8825`；`confirmed_max=null` |
| 电源 | DC 9–24 V 与 XT30/HY2.0 接口 | `document_voltage=DC9-24V`；`document_power_connector=XT30`；`document_motor_connector=HY2.0-4P`；`schematic_power=P1 Header 2`；`schematic_motor=J3/J4/J5 Header 4` |

## 待确认事项

- `address.i2c`：产品正文声明 I2C 地址为 0x70，但原理图只显示 ATMEGA328 SDA/SCL，数值地址由固件实现且未打印在页面。（证据：图 17b7ea817633 / 第 1 页 / U1 SDA/SCL without address label）
- `component.driver-variant`：原理图 M1-M3 明确标 A4988_M，产品正文称集成三片 DRV8825 驱动板，当前资料存在驱动型号冲突。（证据：图 17b7ea817633 / 第 1 页 / M1-M3 A4988_M markings）
- `gpio.microstep-capability`：产品正文称最高 1/32 微步，原理图只确认 MS1/MS2/MS3 三根配置线；因驱动型号存在 A4988/DRV8825 冲突，无法由页面确认最大微步倍率。（证据：图 17b7ea817633 / 第 1 页 / M1-M3 MS1/MS2/MS3 and A4988_M）
- `power.input-interface`：产品正文称电源为 DC 9–24 V、XT30，电机接口为 HY2.0-4P；原理图只标 P1 Header 2 与 J3-J5 Header 4，未给机械连接器型号或电压范围。（证据：图 17b7ea817633 / 第 1 页 / P1 and J3-J5 generic header symbols）
- `review.i2c-address`：请用 ATMEGA328 GRBL 固件或 I2C 扫描确认地址为 0x70。；原因：地址由固件实现，未印在原理图。
- `review.driver-variant`：请用 BOM、驱动板丝印或实物确认三个插座实际装配 A4988 还是 DRV8825。；原因：原理图和产品正文型号冲突。
- `review.microstep-capability`：请在确认驱动型号后按 MS1/MS2/MS3 真值表复核最大微步倍率。；原因：A4988 与 DRV8825 的微步能力不同。
- `review.input-interface`：请用 PCB/BOM/装配资料确认 DC 9–24 V、XT30 与 HY2.0-4P 接口规格和极性。；原因：原理图只使用通用 Header 符号且未标输入范围。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `17b7ea817633473514370e6bf1cce8fa75ce842fa14bd1b559ecba9a1d073677` | `https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor/stepmotor_sch_01.webp` |

---

源文档：`zh_CN/module/stepmotor.md`

源文档 SHA-256：`5ce1a89012e69a723a425a560ca69a8d6398a10e0bf5e71ca00fc0e7590442e9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
