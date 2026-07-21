# Hat CBack Driver 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat CBack Driver |
| SKU | A100 |
| 产品 ID | `hat-cback-driver-a569848f16dc` |
| 源文档 | `zh_CN/hat/c_back_driver.md` |

## 概述

Hat CBack Driver 以 STM32F030F4P6（U1）为主控，通过 SCL/SDA 与 STICKIO 主机接口连接，并输出 CH1~CH4 四路控制信号。P3/P4 为四路三线输出提供 CHx、+BAT 和 GND，J1 引出 I2C 与 +5V，J2 引出 INPUT/OUTPUT 与 +5V。+3.3V、+5V 和 +BAT 均由 STICKIO 分别引入，原理图未显示板载电源转换器；P1 提供 SWD 调试和复位连接。

## 检索关键词

`Hat CBack Driver`、`A100`、`STM32F030F4P6`、`U1`、`STICKIO`、`P2`、`I2C`、`SCL`、`SDA`、`G26`、`G0`、`CH1`、`CH2`、`CH3`、`CH4`、`+BAT`、`+5V`、`+3.3V`、`INPUT`、`OUTPUT`、`SWD`、`SWCLK`、`SWDIO`、`NRST`、`BOOT0`、`PA0`、`PA1`、`PA2`、`PA3`、`PA9`、`PA10`、`0x38`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | 主控 MCU，连接 I2C、四路 CH 输出、扩展 INPUT/OUTPUT、复位与 SWD 调试信号 | 图 38624912fb91 / 第 1 页 / 页面左中 U1：STM32F030F4P6，1~20 脚及 BOOT0、CH1~CH4、INPUT/OUTPUT、SCL/SDA、SWDIO/SWCLK 网络 |
| P1 | SWD_5p | 5 针 SWD 调试接口，引出 +3.3V、SWCLK、SWDIO、NRST 和 GND | 图 38624912fb91 / 第 1 页 / 页面右上 P1 SWD_5p：1~5 脚标注 VCC、SWCLK、SWDIO、RST、GND |
| P2 | STICKIO | 8 针主机接口，引入 GND、+5V、SCL、INPUT、SDA、+BAT 和 +3.3V | 图 38624912fb91 / 第 1 页 / 页面右中 P2 STICKIO：1~8 脚 GND/5VOUT/G26/G36/G0/BAT/3V3/5VIN 与左侧网络 |
| J1 | HY-2.0_IIC | 4 针 I2C 扩展接口，引出 SCL、SDA、+5V 和 GND | 图 38624912fb91 / 第 1 页 / 页面右下 J1 HY-2.0_IIC：1~4 脚 IIC_SCL/IIC_SDA/VCC/GND |
| J2 | HY-2.0_IO | 4 针通用 I/O 扩展接口，引出 INPUT、OUTPUT、+5V 和 GND | 图 38624912fb91 / 第 1 页 / 页面右下 J2 HY-2.0_IO：1~4 脚 I/O/VCC/GND，左侧网络为 INPUT/OUTPUT/+5V/GND |
| P3 | Header 3X2 | CH1/CH2 三线输出接口，每路包含控制信号、+BAT 和 GND | 图 38624912fb91 / 第 1 页 / 页面下中 P3 Header 3X2：奇数侧 CH2/+BAT/GND，偶数侧 CH1/+BAT/GND |
| P4 | Header 3X2 | CH3/CH4 三线输出接口，每路包含控制信号、+BAT 和 GND | 图 38624912fb91 / 第 1 页 / 页面底部 P4 Header 3X2：奇数侧 CH4/+BAT/GND，偶数侧 CH3/+BAT/GND |
| R1 | 10KΩ | 将 U1 BOOT0 下拉至 GND | 图 38624912fb91 / 第 1 页 / 页面左中 U1.1 BOOT0 左侧：R1 10KΩ 连接 BOOT0 与 GND |
| R2/C1 | 10KΩ / 100nF | NRST 上拉与对地电容组成的复位网络 | 图 38624912fb91 / 第 1 页 / 页面左侧 NRST 网络：R2 10KΩ 接 +3.3V，C1 100nF 接 GND，并连接 U1.4 |
| C2/C3 | 100nF / 22uF | +3.3V 电源轨对 GND 的去耦与储能电容 | 图 38624912fb91 / 第 1 页 / 页面中央 U1 右侧：C2 100nF、C3 22uF 均跨接 +3.3V 与 GND |
| C4/C5 | 100nF / 100nF | J1 与 J2 各自 +5V 端口的对地去耦电容 | 图 38624912fb91 / 第 1 页 / 页面右下：C4 位于 J1 +5V-GND，C5 位于 J2 +5V-GND，均标注 100nF |
| C6/C7 | 22uF / 22uF | P3 与 P4 附近 +BAT 电源的对地储能电容 | 图 38624912fb91 / 第 1 页 / 页面下中：P3 右侧 C6 22uF、P4 右侧 C7 22uF 均跨接 +BAT 与 GND |

## 系统结构

### Hat CBack Driver

U1 STM32F030F4P6 通过 SCL/SDA 连接主机与 J1，并从 PA0~PA3 输出 CH1~CH4；PA4/PA5 分别连接 OUTPUT/INPUT。

- 参数与网络：`controller=U1 STM32F030F4P6`；`host_bus=SCL/SDA`；`channel_outputs=CH1, CH2, CH3, CH4`；`extended_io=OUTPUT, INPUT`
- 证据：图 38624912fb91 / 第 1 页 / 全页：U1 左右两侧网络与 P2、J1、J2、P3、P4 的同名网络连接

## 核心器件

### U1 STM32F030F4P6

U1 已用功能脚为 PA0/CH1、PA1/CH2、PA2/CH3、PA3/CH4、PA4/OUTPUT、PA5/INPUT、PA9/SCL、PA10/SDA、PA13/SWDIO、PA14/SWCLK；VDDA/VDD 接 +3.3V，VSS 接 GND。

- 参数与网络：`pin_5=VDDA +3.3V`；`pin_6=PA0 CH1`；`pin_7=PA1 CH2`；`pin_8=PA2 CH3`；`pin_9=PA3 CH4`；`pin_10=PA4 OUTPUT`；`pin_11=PA5 INPUT`；`pin_15=VSS GND`；`pin_16=VDD +3.3V`；`pin_17=PA9 SCL`；`pin_18=PA10 SDA`；`pin_19=PA13 SWDIO`；`pin_20=PA14 SWCLK`
- 证据：图 38624912fb91 / 第 1 页 / 页面左中 U1：5~20 脚编号、端口名和相邻网络标签

## 电源

### 外部供电结构

P2.7 直接引入 +3.3V 供 U1、P1 和复位网络使用；P2.2 直接引入 +5V 供 J1/J2；P2.6 直接引入 +BAT 供 P3/P4。原理图未显示这三条电源轨之间的板载转换器。

- 参数与网络：`3v3_input=P2.7 3V3`；`5v_input=P2.2 5VOUT`；`battery_input=P2.6 BAT`；`onboard_converter=not shown`
- 证据：图 38624912fb91 / 第 1 页 / 全页 +3.3V、+5V、+BAT 同名网络：从 P2 分别连接 U1/P1、J1/J2、P3/P4，未见转换器符号

### +3.3V 电源轨

U1.5 VDDA 与 U1.16 VDD 均接 +3.3V，U1.15 VSS 接 GND；C2 100nF 与 C3 22uF 均跨接 +3.3V 和 GND。

- 参数与网络：`analog_supply=U1.5 VDDA +3.3V`；`digital_supply=U1.16 VDD +3.3V`；`ground=U1.15 VSS GND`；`capacitors=C2 100nF; C3 22uF`
- 证据：图 38624912fb91 / 第 1 页 / 页面 U1.5/U1.15/U1.16 与右侧 C2/C3 的 +3.3V/GND 连接

### +5V 端口电源

+5V 从 P2.2 连接 J1.3 和 J2.3；C4 100nF、C5 100nF 分别在 J1、J2 侧跨接 +5V 与 GND。

- 参数与网络：`source=P2.2 5VOUT`；`loads=J1.3 VCC; J2.3 VCC`；`decoupling=C4 100nF; C5 100nF`
- 证据：图 38624912fb91 / 第 1 页 / 页面 P2.2、J1.3/C4 与 J2.3/C5 的 +5V 同名网络

### +BAT 通道电源

+BAT 从 P2.6 分配到 P3.3/P3.4 与 P4.3/P4.4；C6 22uF 和 C7 22uF 分别在 P3、P4 侧跨接 +BAT 与 GND。

- 参数与网络：`source=P2.6 BAT`；`p3_power=P3.3, P3.4 +BAT`；`p4_power=P4.3, P4.4 +BAT`；`capacitors=C6 22uF; C7 22uF`
- 证据：图 38624912fb91 / 第 1 页 / 页面 P2.6 与 P3/P4 中行、C6/C7 上端的 +BAT 同名网络

## 接口

### P2 STICKIO

P2.1~P2.8 依次标为 GND、5VOUT、G26、G36、G0、BAT、3V3、5VIN；板上网络依次为 GND、+5V、SCL、INPUT、SDA、+BAT、+3.3V，P2.8 未连接。

- 参数与网络：`pin_1=GND`；`pin_2=5VOUT +5V`；`pin_3=G26 SCL`；`pin_4=G36 INPUT`；`pin_5=G0 SDA`；`pin_6=BAT +BAT`；`pin_7=3V3 +3.3V`；`pin_8=5VIN NC`
- 证据：图 38624912fb91 / 第 1 页 / 页面右中 P2 STICKIO：引脚编号、符号内名称、左侧网络及 8 脚未连接标记

### J1 HY-2.0_IIC

J1.1 为 SCL/IIC_SCL，J1.2 为 SDA/IIC_SDA，J1.3 为 +5V/VCC，J1.4 为 GND。

- 参数与网络：`pin_1=SCL IIC_SCL`；`pin_2=SDA IIC_SDA`；`pin_3=+5V VCC`；`pin_4=GND`；`signal_level=U1 powered by +3.3V; no level shifter shown`
- 证据：图 38624912fb91 / 第 1 页 / 页面右下 J1：左侧网络、1~4 脚编号及符号内 IIC_SCL/IIC_SDA/VCC/GND

### J2 HY-2.0_IO

J2.1 INPUT（I）连接 U1.11 PA5 与 P2.4 G36，J2.2 OUTPUT（O）连接 U1.10 PA4；J2.3 为 +5V/VCC，J2.4 为 GND。

- 参数与网络：`pin_1=INPUT I, U1.11 PA5, P2.4 G36`；`pin_2=OUTPUT O, U1.10 PA4`；`pin_3=+5V VCC`；`pin_4=GND`；`input_direction=to U1 PA5`；`output_direction=from U1 PA4`
- 证据：图 38624912fb91 / 第 1 页 / 页面 U1.10/U1.11、P2.4 与 J2.1/J2.2 的 INPUT/OUTPUT 同名网络

### P3 Header 3X2

P3.1/P3.3/P3.5 分别为 CH2/+BAT/GND，P3.2/P3.4/P3.6 分别为 CH1/+BAT/GND。

- 参数与网络：`pin_1=CH2`；`pin_2=CH1`；`pin_3=+BAT`；`pin_4=+BAT`；`pin_5=GND`；`pin_6=GND`
- 证据：图 38624912fb91 / 第 1 页 / 页面下中 P3：1~6 脚编号和左右 CH2/CH1、+BAT、GND 网络

### P4 Header 3X2

P4.1/P4.3/P4.5 分别为 CH4/+BAT/GND，P4.2/P4.4/P4.6 分别为 CH3/+BAT/GND。

- 参数与网络：`pin_1=CH4`；`pin_2=CH3`；`pin_3=+BAT`；`pin_4=+BAT`；`pin_5=GND`；`pin_6=GND`
- 证据：图 38624912fb91 / 第 1 页 / 页面底部 P4：1~6 脚编号和左右 CH4/CH3、+BAT、GND 网络

## 总线

### SCL/SDA

SCL 同名网络连接 P2.3 G26、U1.17 PA9 和 J1.1 IIC_SCL；SDA 连接 P2.5 G0、U1.18 PA10 和 J1.2 IIC_SDA。

- 参数与网络：`scl=P2.3 G26 - U1.17 PA9 - J1.1 IIC_SCL`；`sda=P2.5 G0 - U1.18 PA10 - J1.2 IIC_SDA`；`level_rail=+3.3V MCU supply`；`direction=bidirectional bus`
- 证据：图 38624912fb91 / 第 1 页 / 页面 U1.17/U1.18、P2.3/P2.5、J1.1/J1.2 的 SCL/SDA 同名网络

### I2C 上拉

本页 SCL 与 SDA 路径上未显示上拉电阻、串联电阻或专用保护器件。

- 参数与网络：`scl_pullup=not shown`；`sda_pullup=not shown`；`series_resistors=not shown`；`protection=not shown`
- 证据：图 38624912fb91 / 第 1 页 / 页面 U1、P2 与 J1 之间的 SCL/SDA 全部可见路径，未画外围电阻或保护符号

## GPIO 与控制信号

### BOOT0

U1.1 BOOT0 通过 R1 10KΩ 固定下拉至 GND。

- 参数与网络：`mcu_pin=U1.1 BOOT0`；`resistor=R1 10KΩ`；`strap=GND`
- 证据：图 38624912fb91 / 第 1 页 / 页面左中 U1.1 BOOT0：R1 10KΩ 串接至左侧 GND

### CH1~CH4

U1.6 PA0、U1.7 PA1、U1.8 PA2、U1.9 PA3 分别映射到 CH1、CH2、CH3、CH4，并直接连接 P3/P4 信号脚。

- 参数与网络：`CH1=U1.6 PA0 to P3.2`；`CH2=U1.7 PA1 to P3.1`；`CH3=U1.8 PA2 to P4.2`；`CH4=U1.9 PA3 to P4.1`；`direction=from U1 to channel connectors`
- 证据：图 38624912fb91 / 第 1 页 / 页面 U1.6~U1.9 与 P3/P4 顶行的 CH1~CH4 同名网络

## 时钟

### U1 PF0/PF1 时钟脚

U1.2 PF0/OSC_IN 与 U1.3 PF1/OSC_OUT 在原理图上标为未连接，页面未显示外部晶振或谐振器。

- 参数与网络：`osc_in=U1.2 PF0/OSC_IN NC`；`osc_out=U1.3 PF1/OSC_OUT NC`；`external_crystal=not shown`
- 证据：图 38624912fb91 / 第 1 页 / 页面左中 U1.2/U1.3：PF0/OSC_IN 和 PF1/OSC_OUT 左侧均有未连接标记

## 复位

### NRST

U1.4 NRST 连接 P1.4 RST；R2 10KΩ 将 NRST 上拉到 +3.3V，C1 100nF 将 NRST 接至 GND。

- 参数与网络：`mcu_pin=U1.4 NRST`；`debug_pin=P1.4 RST`；`pull_up=R2 10KΩ to +3.3V`；`capacitor=C1 100nF to GND`
- 证据：图 38624912fb91 / 第 1 页 / 页面左侧 U1.4 NRST 与 R2/C1；页面右上 P1.4 的 NRST 同名网络

## 保护电路

### 外部接口保护

本页 P2、J1、J2、P3、P4 的外部信号与电源路径上未显示 TVS、保险丝、反接保护或专用电平转换器。

- 参数与网络：`tvs=not shown`；`fuse=not shown`；`reverse_polarity=not shown`；`level_shifter=not shown`
- 证据：图 38624912fb91 / 第 1 页 / 全页外部连接器 P2/J1/J2/P3/P4 至 U1 或电源网络的完整可见路径

## 调试与烧录

### P1 SWD_5p

P1.1~P1.5 依次为 +3.3V、SWCLK、SWDIO、NRST、GND；SWCLK/SWDIO 分别连接 U1.20 PA14 与 U1.19 PA13。

- 参数与网络：`pin_1=+3.3V VCC`；`pin_2=SWCLK to U1.20 PA14`；`pin_3=SWDIO to U1.19 PA13`；`pin_4=NRST`；`pin_5=GND`
- 证据：图 38624912fb91 / 第 1 页 / 页面右上 P1 1~5 脚与页面左中 U1.19/U1.20 同名 SWDIO/SWCLK 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat CBack Driver | `controller=U1 STM32F030F4P6`；`host_bus=SCL/SDA`；`channel_outputs=CH1, CH2, CH3, CH4`；`extended_io=OUTPUT, INPUT` |
| 核心器件 | U1 STM32F030F4P6 | `pin_5=VDDA +3.3V`；`pin_6=PA0 CH1`；`pin_7=PA1 CH2`；`pin_8=PA2 CH3`；`pin_9=PA3 CH4`；`pin_10=PA4 OUTPUT`；`pin_11=PA5 INPUT`；`pin_15=VSS GND`；`pin_16=VDD +3.3V`；`pin_17=PA9 SCL`；`pin_18=PA10 SDA`；`pin_19=PA13 SWDIO`；`pin_20=PA14 SWCLK` |
| 时钟 | U1 PF0/PF1 时钟脚 | `osc_in=U1.2 PF0/OSC_IN NC`；`osc_out=U1.3 PF1/OSC_OUT NC`；`external_crystal=not shown` |
| 复位 | NRST | `mcu_pin=U1.4 NRST`；`debug_pin=P1.4 RST`；`pull_up=R2 10KΩ to +3.3V`；`capacitor=C1 100nF to GND` |
| GPIO 与控制信号 | BOOT0 | `mcu_pin=U1.1 BOOT0`；`resistor=R1 10KΩ`；`strap=GND` |
| 调试与烧录 | P1 SWD_5p | `pin_1=+3.3V VCC`；`pin_2=SWCLK to U1.20 PA14`；`pin_3=SWDIO to U1.19 PA13`；`pin_4=NRST`；`pin_5=GND` |
| 接口 | P2 STICKIO | `pin_1=GND`；`pin_2=5VOUT +5V`；`pin_3=G26 SCL`；`pin_4=G36 INPUT`；`pin_5=G0 SDA`；`pin_6=BAT +BAT`；`pin_7=3V3 +3.3V`；`pin_8=5VIN NC` |
| 总线 | SCL/SDA | `scl=P2.3 G26 - U1.17 PA9 - J1.1 IIC_SCL`；`sda=P2.5 G0 - U1.18 PA10 - J1.2 IIC_SDA`；`level_rail=+3.3V MCU supply`；`direction=bidirectional bus` |
| 总线 | I2C 上拉 | `scl_pullup=not shown`；`sda_pullup=not shown`；`series_resistors=not shown`；`protection=not shown` |
| 总线地址 | Hat CBack Driver I2C 地址 | `documented_address=0x38`；`schematic_address_label=not shown`；`address_straps=not shown` |
| 接口 | J1 HY-2.0_IIC | `pin_1=SCL IIC_SCL`；`pin_2=SDA IIC_SDA`；`pin_3=+5V VCC`；`pin_4=GND`；`signal_level=U1 powered by +3.3V; no level shifter shown` |
| 接口 | J2 HY-2.0_IO | `pin_1=INPUT I, U1.11 PA5, P2.4 G36`；`pin_2=OUTPUT O, U1.10 PA4`；`pin_3=+5V VCC`；`pin_4=GND`；`input_direction=to U1 PA5`；`output_direction=from U1 PA4` |
| GPIO 与控制信号 | CH1~CH4 | `CH1=U1.6 PA0 to P3.2`；`CH2=U1.7 PA1 to P3.1`；`CH3=U1.8 PA2 to P4.2`；`CH4=U1.9 PA3 to P4.1`；`direction=from U1 to channel connectors` |
| 接口 | P3 Header 3X2 | `pin_1=CH2`；`pin_2=CH1`；`pin_3=+BAT`；`pin_4=+BAT`；`pin_5=GND`；`pin_6=GND` |
| 接口 | P4 Header 3X2 | `pin_1=CH4`；`pin_2=CH3`；`pin_3=+BAT`；`pin_4=+BAT`；`pin_5=GND`；`pin_6=GND` |
| 电源 | 外部供电结构 | `3v3_input=P2.7 3V3`；`5v_input=P2.2 5VOUT`；`battery_input=P2.6 BAT`；`onboard_converter=not shown` |
| 电源 | +3.3V 电源轨 | `analog_supply=U1.5 VDDA +3.3V`；`digital_supply=U1.16 VDD +3.3V`；`ground=U1.15 VSS GND`；`capacitors=C2 100nF; C3 22uF` |
| 电源 | +5V 端口电源 | `source=P2.2 5VOUT`；`loads=J1.3 VCC; J2.3 VCC`；`decoupling=C4 100nF; C5 100nF` |
| 电源 | +BAT 通道电源 | `source=P2.6 BAT`；`p3_power=P3.3, P3.4 +BAT`；`p4_power=P4.3, P4.4 +BAT`；`capacitors=C6 22uF; C7 22uF` |
| 保护电路 | 外部接口保护 | `tvs=not shown`；`fuse=not shown`；`reverse_polarity=not shown`；`level_shifter=not shown` |

## 待确认事项

- `address.i2c-0x38`：产品正文标注 I2C 地址为 0x38，但本地原理图页面未标注 0x38、地址寄存器或地址选择网络，无法仅由原理图确认该地址。（证据：图 38624912fb91 / 第 1 页 / 全页 U1 与 SCL/SDA 网络：未见 0x38 文本、地址选择引脚或地址电阻）
- `review.i2c-address-0x38`：I2C 从设备地址 0x38 是否由 U1 固件固定实现？；原因：产品正文给出 0x38，但原理图只显示 SCL/SDA 连接，未显示地址文本、地址选择网络或固件依据。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `38624912fb9135b9b6b37974f2d7311e75a49e5973e6544ee964d0aec3d97a4a` | `https://static-cdn.m5stack.com/resource/docs/products/hat/c_back_driver/c_back_driver_sch_01.webp` |

---

源文档：`zh_CN/hat/c_back_driver.md`

源文档 SHA-256：`97b74f90000915e38135af1d13918e4ff2e09974d937cc8624a4739cc71074d7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
