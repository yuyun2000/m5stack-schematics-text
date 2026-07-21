# Hat Mini EncoderC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat Mini EncoderC |
| SKU | U157 |
| 产品 ID | `hat-mini-encoderc-9161059da3b0` |
| 源文档 | `zh_CN/hat/MiniEncoderC Hat.md` |

## 概述

Hat Mini EncoderC 以 U1 STM32F030F4P6 为协处理器，采集 SW1 EC11 的 A/B 相与按键，并通过 RGB 网络驱动 U2 SK6812-3535。主机经 P1 的 SCL/SDA 与 MCU 通信，同一总线也引到 J1 Grove；J2 提供 SWDIO、SWCLK 和 NRST 调试。P1 的 3V3 为 MCU 和 RGB LED 供电，5V 供给 Grove，BAT 与 J3 电池接口直连，页面未显示充电器、LDO 或其他电源转换器。

## 检索关键词

`Hat Mini EncoderC`、`U157`、`STM32F030F4P6`、`EC11`、`SK6812-3535`、`I2C`、`0x42`、`SCL`、`SDA`、`AD0`、`AD1`、`BTN`、`RGB`、`PA0`、`PA5`、`PA6`、`PA7`、`PA9`、`PA10`、`SWDIO`、`SWCLK`、`NRST`、`BOOT0`、`STICKIO HAT`、`GROVE`、`BAT`、`3V3`、`5V`、`R4 10KΩ`、`C1 100nF`、`rotary encoder`、`200mAh`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | 采集编码器和按键、驱动 RGB LED，并通过 I2C 与主机通信的协处理器 | 图 7a1f416e205c / 第 1 页 / B1-C2，U1 STM32F030F4P6 及 RGB/BTN/AD1/AD0/SCL/SDA/SWD/NRST/BOOT0 |
| SW1 | EC11 | 带按压开关的增量式旋转编码器，A/B 相接 AD1/AD0，按键接 BTN | 图 7a1f416e205c / 第 1 页 / B2-B3，SW1 EC11，A=AD1、B=AD0、C=GND、D=BTN、E/F=GND |
| U2 | SK6812-3535 | 由 U1 RGB 网络驱动的可编程 RGB LED | 图 7a1f416e205c / 第 1 页 / B4，U2 SK6812-3535，DI=RGB、VDD=3V3、GND、DO 未连接 |
| P1 | HAT 8-pin connector | 主机 HAT 接口，承载 GND、5V、SCL、SDA、BAT 与 3V3 | 图 7a1f416e205c / 第 1 页 / D3，P1 HAT pins 1-8 与 GND/5V/SCL/G36/SDA/BAT/3V3/5VIN |
| J1 | GROVE HY2.0-4P | 导出 SCL、SDA、5V 与 GND 的 Grove 接口 | 图 7a1f416e205c / 第 1 页 / D2-D3，J1 GROVE，IO2=SCL、IO1=SDA、5V、GND |
| J2 | SWD_5P | U1 的 5 针 SWD 调试与复位接口 | 图 7a1f416e205c / 第 1 页 / C1-D2，J2 SWD_5P：VCC/SWCLK/SWDIO/NRST/GND |
| J3 | SMT_HDR_2x1.25mm | BAT 与 GND 的双触点电池连接器 | 图 7a1f416e205c / 第 1 页 / D4，J3 SMT_HDR_2x1.25mm，BAT 正端与 GND 负端 |
| R1/R2/R3 | 10KΩ / 10KΩ / 10KΩ | BTN、AD0、AD1 输入上拉至 3V3 | 图 7a1f416e205c / 第 1 页 / B2-B3，R1 BTN、R2 AD0、R3 AD1，均为 10KΩ 到 3V3 |
| R4/R5/C1 | 10KΩ / 10KΩ / 100nF | BOOT0 下拉与 NRST 上拉/复位滤波网络 | 图 7a1f416e205c / 第 1 页 / B1-C2，BOOT0-R4-GND 与 3V3-R5-NRST-C1-GND |
| C2/C3/C4/C5/C6 | 100nF / 10uF / 1uF / 100nF / 100nF | MCU、Grove 5V 和编码器 A/B 相的去耦/滤波电容 | 图 7a1f416e205c / 第 1 页 / C1-C3 与 D2-D3：C2/C3 供电去耦、C4 Grove 5V、C5 AD0、C6 AD1 |

## 系统结构

### 编码器 HAT 架构

U1 STM32F030F4P6 读取 SW1 EC11 的 AD0/AD1 与 BTN，驱动 U2 SK6812-3535，并通过 P1 的 SCL/SDA 与主机通信。

- 参数与网络：`coprocessor=U1 STM32F030F4P6`；`encoder=SW1 EC11`；`rgb=U2 SK6812-3535`；`host_bus=I2C SCL/SDA`；`debug=J2 SWD_5P`
- 证据：图 7a1f416e205c / 第 1 页 / 整页：MCU、EC11、RGB、HAT、Grove、SWD 与 BAT 分区

## 核心器件

### STM32F030F4P6 协处理器

U1 为 STM32F030F4P6，VDD pin16 与 VDDA pin5 接 3V3，VSS pin15 接 GND；C2 100 nF 与 C3 10 µF 对地去耦。

- 参数与网络：`reference=U1`；`part_number=STM32F030F4P6`；`vdd=pin16 3V3`；`vdda=pin5 3V3`；`vss=pin15 GND`；`decoupling=C2 100nF; C3 10uF`
- 证据：图 7a1f416e205c / 第 1 页 / B1-C2，U1 电源脚与 C2/C3

## 电源

### HAT 电源轨分配

P1 3V3 为 U1 与 U2 供电，P1 5V 直接供给 J1 Grove，P1 BAT 直接连接 J3；页面未显示 LDO、DC/DC、负载开关或充电 IC。

- 参数与网络：`3v3_source=P1 pin2`；`3v3_loads=U1/U2`；`5v_source=P1 pin7`；`5v_load=J1 Grove`；`battery_net=P1 pin3 BAT to J3`；`ldo=none shown`；`dc_dc=none shown`；`charger=none shown`；`load_switch=none shown`
- 证据：图 7a1f416e205c / 第 1 页 / 整页 3V3/5V/BAT 网络与 P1/J1/J3

## 接口

### P1 HAT 接口

P1 pin8 GND、pin7 5V、pin6 SCL、pin4 SDA、pin3 BAT、pin2 3V3 被使用；pin5 G36 与 pin1 5VIN 标为未连接。

- 参数与网络：`reference=P1`；`pin1=5VIN NC`；`pin2=3V3`；`pin3=BAT`；`pin4=SDA`；`pin5=G36 NC`；`pin6=SCL`；`pin7=5V`；`pin8=GND`
- 证据：图 7a1f416e205c / 第 1 页 / D3，P1 HAT pins 1-8 与网络/NC 标记

### J1 Grove 接口

J1 IO2 接 SCL、IO1 接 SDA，并提供 5V 与 GND；C4 1 µF 跨接 5V 与 GND。

- 参数与网络：`reference=J1`；`io2=SCL bidirectional`；`io1=SDA bidirectional`；`power=5V`；`ground=GND`；`decoupling=C4 1uF`
- 证据：图 7a1f416e205c / 第 1 页 / D2-D3，J1 GROVE 与 C4 1uF

### J3 电池接口

J3 为 SMT_HDR_2x1.25mm，正触点连接 BAT，负触点连接 GND；BAT 网络与 P1 pin3 直连。

- 参数与网络：`reference=J3`；`part_number=SMT_HDR_2x1.25mm`；`positive=BAT`；`negative=GND`；`host_connection=P1 pin3 BAT`
- 证据：图 7a1f416e205c / 第 1 页 / D3-D4，P1 BAT 网络与 J3 BAT/GND

## 总线

### 主机 I2C 接口

U1 PA9 pin17 连接 SCL，PA10 pin18 连接 SDA；SCL/SDA 同时连接 P1 HAT 与 J1 Grove，页面未显示本板 I2C 上拉电阻。

- 参数与网络：`controller=external host`；`device=U1 STM32F030F4P6`；`scl=U1 PA9 pin17 / P1 pin6 / J1 IO2`；`sda=U1 PA10 pin18 / P1 pin4 / J1 IO1`；`level=3.3V MCU domain`；`onboard_pullups=none shown`；`direction=bidirectional`
- 证据：图 7a1f416e205c / 第 1 页 / U1 PA9/PA10 与 P1/J1 的 SCL/SDA 网络

## GPIO 与控制信号

### EC11 A/B 相输入

SW1 A 相连接 AD1/U1 PA6 pin12，B 相连接 AD0/U1 PA7 pin13，共端 C 接 GND；AD1 与 AD0 分别由 R3/R2 10 kΩ 上拉并由 C6/C5 100 nF 对地滤波。

- 参数与网络：`phase_a=SW1 A -> AD1 -> U1 PA6 pin12`；`phase_b=SW1 B -> AD0 -> U1 PA7 pin13`；`common=SW1 C GND`；`phase_a_filter=R3 10KΩ to 3V3; C6 100nF to GND`；`phase_b_filter=R2 10KΩ to 3V3; C5 100nF to GND`；`direction=inputs to U1`
- 证据：图 7a1f416e205c / 第 1 页 / U1 PA6/PA7 与 SW1 A/B、R2/R3、C5/C6 连线

### EC11 按键输入

SW1 按键 D 端连接 BTN/U1 PA5 pin11，E/F 端接 GND；BTN 由 R1 10 kΩ 上拉到 3V3。

- 参数与网络：`signal=BTN`；`mcu_pin=U1 PA5 pin11`；`switch_terminal=SW1 D`；`return=SW1 E/F GND`；`pullup=R1 10KΩ to 3V3`；`active_level=low when pressed`
- 证据：图 7a1f416e205c / 第 1 页 / U1 PA5 BTN 与 SW1 D/E/F、R1 10KΩ

### SK6812 数据输出

U1 PA0 pin6 通过 RGB 网络连接 U2 DI pin3；U2 VDD pin4 接 3V3、GND pin2 接 GND，DO pin1 未连接。

- 参数与网络：`mcu_pin=U1 PA0 pin6`；`net=RGB`；`destination=U2 pin3 DI`；`led=SK6812-3535`；`supply=U2 pin4 3V3`；`data_out=U2 pin1 DO NC`；`direction=U1 output to U2`
- 证据：图 7a1f416e205c / 第 1 页 / U1 PA0 RGB 与 B4 U2 SK6812-3535

### MCU BOOT0 配置

U1 BOOT0 pin1 通过 R4 10 kΩ 固定下拉到 GND，页面未显示 BOOT 跳线或按键。

- 参数与网络：`pin=U1 pin1 BOOT0`；`pulldown=R4 10KΩ to GND`；`jumper=none shown`；`button=none shown`
- 证据：图 7a1f416e205c / 第 1 页 / B1-B2，U1 BOOT0-R4 10KΩ-GND

## 时钟

### 外部时钟连接

U1 PF0-OSC_IN pin2 与 PF1-OSC_OUT pin3 均未连接，原理图未显示晶振或外部时钟源。

- 参数与网络：`osc_in=U1 pin2 NC`；`osc_out=U1 pin3 NC`；`crystal=none shown`；`external_clock=none shown`
- 证据：图 7a1f416e205c / 第 1 页 / B1-B2，U1 PF0-OSC_IN/PF1-OSC_OUT 开路

## 复位

### MCU 复位网络

U1 NRST pin4 由 R5 10 kΩ 上拉到 3V3，并由 C1 100 nF 对地；NRST 同时引到 J2。

- 参数与网络：`pin=U1 pin4 NRST`；`pullup=R5 10KΩ to 3V3`；`capacitor=C1 100nF to GND`；`debug_connector=J2 NRST`
- 证据：图 7a1f416e205c / 第 1 页 / B2-C2，3V3-R5-NRST-C1-GND 与 J2 NRST

## 调试与烧录

### STM32 SWD 调试口

J2 SWD_5P 依次提供 VCC=3V3、SWCLK=MCU_SWCLK、SWDIO=MCU_SWDIO、NRST 和 GND，并连接 U1 PA14、PA13 与 NRST。

- 参数与网络：`reference=J2`；`vcc=3V3`；`swclk=U1 PA14 pin20 MCU_SWCLK`；`swdio=U1 PA13 pin19 MCU_SWDIO`；`reset=U1 pin4 NRST`；`ground=GND`
- 证据：图 7a1f416e205c / 第 1 页 / C1-D2，U1 PA13/PA14/NRST 与 J2 SWD_5P

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 编码器 HAT 架构 | `coprocessor=U1 STM32F030F4P6`；`encoder=SW1 EC11`；`rgb=U2 SK6812-3535`；`host_bus=I2C SCL/SDA`；`debug=J2 SWD_5P` |
| 核心器件 | STM32F030F4P6 协处理器 | `reference=U1`；`part_number=STM32F030F4P6`；`vdd=pin16 3V3`；`vdda=pin5 3V3`；`vss=pin15 GND`；`decoupling=C2 100nF; C3 10uF` |
| GPIO 与控制信号 | EC11 A/B 相输入 | `phase_a=SW1 A -> AD1 -> U1 PA6 pin12`；`phase_b=SW1 B -> AD0 -> U1 PA7 pin13`；`common=SW1 C GND`；`phase_a_filter=R3 10KΩ to 3V3; C6 100nF to GND`；`phase_b_filter=R2 10KΩ to 3V3; C5 100nF to GND`；`direction=inputs to U1` |
| GPIO 与控制信号 | EC11 按键输入 | `signal=BTN`；`mcu_pin=U1 PA5 pin11`；`switch_terminal=SW1 D`；`return=SW1 E/F GND`；`pullup=R1 10KΩ to 3V3`；`active_level=low when pressed` |
| GPIO 与控制信号 | SK6812 数据输出 | `mcu_pin=U1 PA0 pin6`；`net=RGB`；`destination=U2 pin3 DI`；`led=SK6812-3535`；`supply=U2 pin4 3V3`；`data_out=U2 pin1 DO NC`；`direction=U1 output to U2` |
| 总线 | 主机 I2C 接口 | `controller=external host`；`device=U1 STM32F030F4P6`；`scl=U1 PA9 pin17 / P1 pin6 / J1 IO2`；`sda=U1 PA10 pin18 / P1 pin4 / J1 IO1`；`level=3.3V MCU domain`；`onboard_pullups=none shown`；`direction=bidirectional` |
| 接口 | P1 HAT 接口 | `reference=P1`；`pin1=5VIN NC`；`pin2=3V3`；`pin3=BAT`；`pin4=SDA`；`pin5=G36 NC`；`pin6=SCL`；`pin7=5V`；`pin8=GND` |
| 接口 | J1 Grove 接口 | `reference=J1`；`io2=SCL bidirectional`；`io1=SDA bidirectional`；`power=5V`；`ground=GND`；`decoupling=C4 1uF` |
| 调试与烧录 | STM32 SWD 调试口 | `reference=J2`；`vcc=3V3`；`swclk=U1 PA14 pin20 MCU_SWCLK`；`swdio=U1 PA13 pin19 MCU_SWDIO`；`reset=U1 pin4 NRST`；`ground=GND` |
| 复位 | MCU 复位网络 | `pin=U1 pin4 NRST`；`pullup=R5 10KΩ to 3V3`；`capacitor=C1 100nF to GND`；`debug_connector=J2 NRST` |
| GPIO 与控制信号 | MCU BOOT0 配置 | `pin=U1 pin1 BOOT0`；`pulldown=R4 10KΩ to GND`；`jumper=none shown`；`button=none shown` |
| 时钟 | 外部时钟连接 | `osc_in=U1 pin2 NC`；`osc_out=U1 pin3 NC`；`crystal=none shown`；`external_clock=none shown` |
| 电源 | HAT 电源轨分配 | `3v3_source=P1 pin2`；`3v3_loads=U1/U2`；`5v_source=P1 pin7`；`5v_load=J1 Grove`；`battery_net=P1 pin3 BAT to J3`；`ldo=none shown`；`dc_dc=none shown`；`charger=none shown`；`load_switch=none shown` |
| 接口 | J3 电池接口 | `reference=J3`；`part_number=SMT_HDR_2x1.25mm`；`positive=BAT`；`negative=GND`；`host_connection=P1 pin3 BAT` |
| 总线地址 | STM32 I2C 地址 | `claimed_address=0x42`；`device=U1 STM32F030F4P6`；`schematic_address=not printed`；`address_straps=none shown` |
| 核心器件 | 编码器每圈脉冲数 | `reference=SW1`；`part_number=EC11`；`claimed_pulses_per_revolution=30`；`schematic_resolution=not printed` |
| 电源 | 内置电池容量 | `claimed_capacity=200mAh`；`schematic_interface=J3 BAT/GND`；`cell_part_number=not printed`；`protection=not shown`；`charging=not shown` |

## 待确认事项

- `address.i2c`：产品正文给出 I2C 地址 0x42，但原理图只显示 SCL/SDA 连接，没有印出从机地址或地址配置电阻。（证据：图 7a1f416e205c / 第 1 页 / U1/P1/J1 SCL/SDA 网络，页面无 0x42 标注）
- `component.encoder-resolution`：产品正文称编码器每旋转一周产生 30 个脉冲，但原理图仅标 SW1 EC11，没有印出机械分辨率或脉冲数。（证据：图 7a1f416e205c / 第 1 页 / SW1 EC11 符号及 A/B/C/D/E/F 连接）
- `power.battery-capacity`：产品正文给出 200 mAh 聚合物锂电池，但原理图只显示 J3 BAT/GND 接口，未标容量、电芯型号、保护或充电参数。（证据：图 7a1f416e205c / 第 1 页 / D4，J3 仅标 BAT/GND 和 SMT_HDR_2x1.25mm）
- `review.i2c-address`：请用 U1 固件或通信协议确认 7-bit I2C 地址是否为 0x42。；原因：地址由 MCU 固件决定，原理图未印出地址。
- `review.encoder-resolution`：请用 EC11 具体料号/BOM 或实测确认每圈 30 脉冲。；原因：EC11 系列存在不同机械规格，原理图没有完整料号或分辨率。
- `review.battery-capacity`：请用电池标签或 BOM 确认 200 mAh 容量、电芯型号及保护/充电边界。；原因：原理图只显示 BAT 连接器，不包含电池规格或充电保护电路。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7a1f416e205c02adb23659d58519cf1d891081f5f761c76030a48353a1f47514` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/611/SCH_HAT_MiniEncoderC_V1.0_sch_01.png` |

---

源文档：`zh_CN/hat/MiniEncoderC Hat.md`

源文档 SHA-256：`b5b9059db179dfaefc12af535ad5cf9b6e507a678639d56a109b03d9b44f2a81`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
