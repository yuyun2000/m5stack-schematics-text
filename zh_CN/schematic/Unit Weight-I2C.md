# Unit Weight-I2C 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Weight-I2C |
| SKU | U180 |
| 产品 ID | `unit-weight-i2c-6c9d7b7fb61d` |
| 源文档 | `zh_CN/unit/Unit-Weight I2C.md` |

## 概述

Unit Weight-I2C 以 U3 STM32F030F4P6 为 I2C 控制器，通过 PA5/PA6 的 HX711_OUT/HX711_SCK 连接 U2 HX711，并由 P1 引出 E+/E-/S-/S+ 四线称重桥接口。J1 Grove 输入 BUS_5V 并提供 3.3V 上拉的 SCL/SDA，U1 HX6306P332MR 将 BUS_5V 转为 3V3，为 MCU 和 I2C 上拉供电。HX711 的数字电源经 FB1 取自 BUS_5V，模拟电源由 Q1 S8550、BASE/AVDD/VFB 网络产生，S+/S- 经 100Ω 与 100nF 滤波后进入 INA+/INA-；J2 提供完整 SWD 调试连接。

## 检索关键词

`Unit Weight-I2C`、`U180`、`STM32F030F4P6`、`HX711`、`HX6306P332MR`、`S8550`、`GROVE 4P`、`Header 4`、`SWD`、`I2C`、`0x26`、`24Bit`、`BUS_5V`、`3V3`、`SCL`、`SDA`、`PA9`、`PA10`、`HX711_OUT`、`HX711_SCK`、`PA5`、`PA6`、`E+`、`E-`、`S+`、`S-`、`INA+`、`INA-`、`AVDD`、`DVDD`、`VFB`、`VBG`、`MCU_SWCLK`、`MCU_SWDIO`、`NRST`、`BOOT0`、`FB1`、`GZ1005D331TF`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030F4P6 | 主控 MCU，将 Grove I2C 转换为 HX711 时钟/数据控制，并提供 SWD、复位与 BOOT0 | 图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C1-D2，U3 STM32F030F4P6 pin1-pin20 |
| U2 | HX711 | 称重桥模拟前端与串行 ADC，接收 INA+/INA- 并通过 DOUT/PD_SCK 与 U3 通讯 | 图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C3-D4，U2 HX711 pin1-pin16 |
| U1 | HX6306P332MR | 将 BUS_5V 转换为 3V3 的稳压器 | 图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 B2-B3，U1 HX6306P332MR，Vin/Vout/GND |
| Q1 | S8550 | HX711 BASE/AVDD/VFB 外部模拟电源调整网络中的 PNP 三极管 | 图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C3，Q1 S8550 与 BUS_5V、U2 BASE/AVDD、R5/R6 |
| J1 | GROVE 4P | 外部 I2C 与电源接口，提供 SCL、SDA、BUS_5V、GND | 图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 B2，J1 GROVE 4P 的 SCL/SDA/5V/GND |
| P1 | Header 4 | 四线称重桥接口，pin1-pin4 分别为 E+、E-、S-、S+ | 图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C3-D3，P1 Header 4，E+/E-/S-/S+ |
| J2 | SWD | 五针调试与烧录接口，连接 3V3、SWCLK、SWDIO、NRST、GND | 图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 D2，J2 SWD pin1-pin5 |
| FB1 | 330R/GZ1005D331TF | BUS_5V 至 HX711 DVDD 的串联磁珠/阻抗器件 | 图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C4，FB1 330R/GZ1005D331TF 位于 BUS_5V 与 U2 DVDD pin16 之间 |

## 系统结构

### Unit Weight-I2C 系统架构

J1 提供 BUS_5V 和 SCL/SDA，U1 生成 3V3；U3 STM32F030F4P6 作为 I2C 控制器，通过 HX711_OUT/HX711_SCK 连接 U2 HX711。U2 的 INA+/INA- 接 P1 称重桥信号，Q1 与反馈网络提供 AVDD/E+ 激励，J2 引出 SWD。

- 参数与网络：`controller=U3 STM32F030F4P6`；`adc=U2 HX711`；`host_interface=J1 SCL/SDA`；`load_cell=P1 E+/E-/S-/S+`；`power=BUS_5V -> U1 HX6306P332MR -> 3V3`；`debug=J2 SWD`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页完整 B2-D4 电路区域

### 独立存储、协处理器、射频与音频

唯一原理图页面未画出独立存储器、额外协处理器、射频、音频、USB、CAN、RS-485、UART 或显示电路；主要功能分区为 MCU、HX711 模拟前端、称重桥接口、I2C Grove、电源和 SWD。

- 参数与网络：`external_storage=null`；`coprocessor=null`；`rf=null`；`audio=null`；`usb=null`；`can=null`；`rs485=null`；`uart=null`；`display=null`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页完整 A1-D4，唯一原理图页面

## 电源

### BUS_5V 至 3V3 稳压

BUS_5V 接 U1 HX6306P332MR Vin，Vout 输出 3V3，GND 接地；C2 100nF 位于输入端，C8 100nF 与 C9 10uF 位于 3V3 输出端。

- 参数与网络：`input=BUS_5V`；`regulator=U1 HX6306P332MR`；`output=3V3`；`input_cap=C2 100nF`；`output_caps=C8 100nF,C9 10uF`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 B2-B3，U1、C2、C8、C9 与 BUS_5V/3V3

### STM32 3V3 供电

U3 VDD pin16 与 VDDA pin5 均接 3V3，VSS pin15 接 GND，C3 100nF 从 3V3 接 GND；同一 3V3 轨还为 I2C 上拉和 J2 pin1 供电。

- 参数与网络：`device=U3 STM32F030F4P6`；`digital_supply=VDD pin16 3V3`；`analog_supply=VDDA pin5 3V3`；`ground=VSS pin15 GND`；`decoupling=C3 100nF`；`other_loads=R9/R10,J2 pin1`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 D1-D2，U3 VDD/VDDA/VSS、C3 与 3V3

### HX711 数字与输入电源

U2 VSUP pin1 接 BUS_5V；DVDD pin16 经 FB1 330R/GZ1005D331TF 接 BUS_5V，并由 C11 10uF 对地去耦。RATE pin15 接 GND。

- 参数与网络：`device=U2 HX711`；`vsup=pin1 BUS_5V`；`dvdd=pin16 via FB1 to BUS_5V`；`filter=FB1 330R/GZ1005D331TF`；`decoupling=C11 10uF`；`rate=pin15 GND`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C3-C4，U2 pins1/15/16、FB1、C11 与 BUS_5V/GND

### HX711 AVDD 与桥路激励

Q1 S8550 接在 BUS_5V 与 HX711 模拟电源网络之间，U2 BASE pin2 驱动外部调整网络，AVDD pin3 输出至 P1 E+；R5 20KΩ 与 R6 8.2KΩ 构成 VFB pin4 的反馈分压，C10 10uF 为 AVDD 去耦，P1 E- 接 AGND/GND。

- 参数与网络：`transistor=Q1 S8550`；`source=BUS_5V`；`control=U2 BASE pin2`；`output=U2 AVDD pin3 -> P1 E+`；`feedback=R5 20KΩ,R6 8.2KΩ -> VFB pin4`；`decoupling=C10 10uF`；`bridge_return=P1 E- -> AGND/GND`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C3，Q1、R5/R6、C10、U2 BASE/AVDD/VFB 与 P1 E+/E-

## 接口

### J1 Grove 四针接口

J1 GROVE 4P 从上到下标为 SCL、SDA、5V、GND，对应网络 SCL、SDA、BUS_5V、GND；BUS_5V 是板上电源输入，SCL/SDA 为 3V3 上拉的双向 I2C 信号。

- 参数与网络：`connector=J1 GROVE 4P`；`pin_scl=SCL, bidirectional`；`pin_sda=SDA, bidirectional`；`pin_5v=BUS_5V, power input`；`pin_gnd=GND`；`logic_level=3V3 pull-up`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 B2，J1 GROVE 4P 与 SCL/SDA/BUS_5V/GND

### P1 四线称重桥接口

P1 Header 4 的 pin1=E+、pin2=E-、pin3=S-、pin4=S+。E+ 由 HX711 AVDD 激励，E- 接 GND；S-/S+ 为桥路差分信号输入。

- 参数与网络：`connector=P1 Header 4`；`pin1=E+ analog excitation output`；`pin2=E- GND return`；`pin3=S- differential input`；`pin4=S+ differential input`；`direction=E+/E- excitation; S+/S- sensor input`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C3-D3，P1 pin1-pin4 与 E+/E-/S-/S+

## 总线

### STM32 至 Grove 的 I2C 总线

U3 PA9 pin17 接 SCL，PA10 pin18 接 SDA；R9/R10 各 4.7KΩ 将 SCL/SDA 上拉到 3V3，网络直接连接 J1。

- 参数与网络：`controller=U3 STM32F030F4P6`；`scl=PA9 pin17 -> SCL -> J1`；`sda=PA10 pin18 -> SDA -> J1`；`pullups=R9/R10 4.7KΩ to 3V3`；`logic_level=3V3`；`direction=bidirectional`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 B2 的 J1/R9/R10 与网格 C1-D2 的 U3 PA9/PA10

## GPIO 与控制信号

### STM32 与 HX711 串行连接

U2 DOUT pin12 的 HX711_OUT 接 U3 PA5 pin11，方向为 HX711 到 MCU；U2 PD_SCK pin11 的 HX711_SCK 接 U3 PA6 pin12，方向为 MCU 到 HX711。

- 参数与网络：`data=U2 DOUT pin12 -> HX711_OUT -> U3 PA5 pin11`；`clock=U3 PA6 pin12 -> HX711_SCK -> U2 PD_SCK pin11`；`data_direction=HX711 to MCU`；`clock_direction=MCU to HX711`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C1-D2 的 U3 PA5/PA6 与网格 C3-D4 的 U2 DOUT/PD_SCK

### STM32 BOOT0 配置

U3 BOOT0 pin1 通过 R7 10KΩ 下拉至 GND。

- 参数与网络：`controller_pin=U3 BOOT0 pin1`；`default=pulled low`；`resistor=R7 10KΩ to GND`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C1-D1，U3 BOOT0 pin1 与 R7 10KΩ/GND

## 时钟

### MCU 与 HX711 时钟连接

U3 PF0-OSC_IN pin2 与 PF1-OSC_OUT pin3 未连接外部晶振；U2 XI pin14 与 XO pin13 也未画外部晶体或振荡器。唯一原理图页面没有标注外部时钟频率。

- 参数与网络：`mcu_osc_in=U3 PF0 pin2 no connection`；`mcu_osc_out=U3 PF1 pin3 no connection`；`hx711_xi=U2 XI pin14 no external clock shown`；`hx711_xo=U2 XO pin13 no external clock shown`；`external_frequency=null`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C1 的 U3 PF0/PF1 与网格 C4 的 U2 XI/XO，均无外部晶振

## 复位

### STM32 NRST 网络

U3 NRST pin4 接 NRST，R1 10KΩ 将该网络上拉到 3V3，C1 100nF 将其接至 GND；NRST 同时引出到 J2 pin4。

- 参数与网络：`controller_pin=U3 NRST pin4`；`network=NRST`；`pullup=R1 10KΩ to 3V3`；`capacitor=C1 100nF to GND`；`debug_header=J2 pin4`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C1-D2，U3 NRST、R1、C1 与 J2 NRST

## 保护电路

### 电源与模拟输入滤波

FB1 隔离 BUS_5V 与 HX711 DVDD，R4/R8 各 100Ω 和 C5 100nF 构成称重差分输入滤波；图中未画 Grove 专用 ESD、过流保险丝、反接保护或浪涌抑制器件。

- 参数与网络：`digital_power_filter=FB1 330R/GZ1005D331TF`；`analog_series=R4/R8 100Ω`；`analog_differential_cap=C5 100nF`；`grove_esd=null`；`input_fuse=null`；`reverse_protection=null`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页 J1 至 BUS_5V 电源路径、U2/FB1 及 P1/R4/R8/C5，唯一原理图页面

## 调试与烧录

### J2 SWD 调试接口

J2 pin1 接 3V3，pin2 接 SWCLK/U3 PA14 pin20，pin3 接 SWDIO/U3 PA13 pin19，pin4 接 NRST，pin5 接 GND。

- 参数与网络：`connector=J2 SWD`；`pin1=3V3`；`pin2=SWCLK -> U3 PA14 pin20`；`pin3=SWDIO -> U3 PA13 pin19`；`pin4=NRST`；`pin5=GND`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 D2，J2 pin1-pin5 与 U3 PA13/PA14

## 模拟电路

### 称重桥信号滤波与 HX711 A 通道

P1 S- 经 R8 100Ω 接 U2 INA- pin7，P1 S+ 经 R4 100Ω 接 INA+ pin8；C5 100nF 跨接 INA-/INA+ 差分节点，C6 10uF 跨接 E+/E- 激励节点。

- 参数与网络：`negative_input=P1 S- -> R8 100Ω -> U2 INA- pin7`；`positive_input=P1 S+ -> R4 100Ω -> U2 INA+ pin8`；`differential_cap=C5 100nF`；`excitation_cap=C6 10uF across E+/E-`；`channel=HX711 channel A`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C3-D3，P1 S-/S+、R8/R4、C5/C6 与 U2 INA-/INA+

### HX711 VBG 与未用 B 通道

U2 VBG pin6 通过 C4 100nF 接 AGND/GND；INB+ pin10 与 INB- pin9 均接 GND，因此本页只使用 INA+/INA- 的 A 通道。

- 参数与网络：`vbg=pin6 via C4 100nF to AGND`；`channel_b_positive=INB+ pin10 GND`；`channel_b_negative=INB- pin9 GND`；`used_channel=INA+/INA-`
- 证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C3-D4，U2 pins6/9/10、C4 与 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Weight-I2C 系统架构 | `controller=U3 STM32F030F4P6`；`adc=U2 HX711`；`host_interface=J1 SCL/SDA`；`load_cell=P1 E+/E-/S-/S+`；`power=BUS_5V -> U1 HX6306P332MR -> 3V3`；`debug=J2 SWD` |
| 系统结构 | 独立存储、协处理器、射频与音频 | `external_storage=null`；`coprocessor=null`；`rf=null`；`audio=null`；`usb=null`；`can=null`；`rs485=null`；`uart=null`；`display=null` |
| 接口 | J1 Grove 四针接口 | `connector=J1 GROVE 4P`；`pin_scl=SCL, bidirectional`；`pin_sda=SDA, bidirectional`；`pin_5v=BUS_5V, power input`；`pin_gnd=GND`；`logic_level=3V3 pull-up` |
| 总线 | STM32 至 Grove 的 I2C 总线 | `controller=U3 STM32F030F4P6`；`scl=PA9 pin17 -> SCL -> J1`；`sda=PA10 pin18 -> SDA -> J1`；`pullups=R9/R10 4.7KΩ to 3V3`；`logic_level=3V3`；`direction=bidirectional` |
| 电源 | BUS_5V 至 3V3 稳压 | `input=BUS_5V`；`regulator=U1 HX6306P332MR`；`output=3V3`；`input_cap=C2 100nF`；`output_caps=C8 100nF,C9 10uF` |
| 电源 | STM32 3V3 供电 | `device=U3 STM32F030F4P6`；`digital_supply=VDD pin16 3V3`；`analog_supply=VDDA pin5 3V3`；`ground=VSS pin15 GND`；`decoupling=C3 100nF`；`other_loads=R9/R10,J2 pin1` |
| 电源 | HX711 数字与输入电源 | `device=U2 HX711`；`vsup=pin1 BUS_5V`；`dvdd=pin16 via FB1 to BUS_5V`；`filter=FB1 330R/GZ1005D331TF`；`decoupling=C11 10uF`；`rate=pin15 GND` |
| 电源 | HX711 AVDD 与桥路激励 | `transistor=Q1 S8550`；`source=BUS_5V`；`control=U2 BASE pin2`；`output=U2 AVDD pin3 -> P1 E+`；`feedback=R5 20KΩ,R6 8.2KΩ -> VFB pin4`；`decoupling=C10 10uF`；`bridge_return=P1 E- -> AGND/GND` |
| 接口 | P1 四线称重桥接口 | `connector=P1 Header 4`；`pin1=E+ analog excitation output`；`pin2=E- GND return`；`pin3=S- differential input`；`pin4=S+ differential input`；`direction=E+/E- excitation; S+/S- sensor input` |
| 模拟电路 | 称重桥信号滤波与 HX711 A 通道 | `negative_input=P1 S- -> R8 100Ω -> U2 INA- pin7`；`positive_input=P1 S+ -> R4 100Ω -> U2 INA+ pin8`；`differential_cap=C5 100nF`；`excitation_cap=C6 10uF across E+/E-`；`channel=HX711 channel A` |
| 模拟电路 | HX711 VBG 与未用 B 通道 | `vbg=pin6 via C4 100nF to AGND`；`channel_b_positive=INB+ pin10 GND`；`channel_b_negative=INB- pin9 GND`；`used_channel=INA+/INA-` |
| GPIO 与控制信号 | STM32 与 HX711 串行连接 | `data=U2 DOUT pin12 -> HX711_OUT -> U3 PA5 pin11`；`clock=U3 PA6 pin12 -> HX711_SCK -> U2 PD_SCK pin11`；`data_direction=HX711 to MCU`；`clock_direction=MCU to HX711` |
| 复位 | STM32 NRST 网络 | `controller_pin=U3 NRST pin4`；`network=NRST`；`pullup=R1 10KΩ to 3V3`；`capacitor=C1 100nF to GND`；`debug_header=J2 pin4` |
| GPIO 与控制信号 | STM32 BOOT0 配置 | `controller_pin=U3 BOOT0 pin1`；`default=pulled low`；`resistor=R7 10KΩ to GND` |
| 调试与烧录 | J2 SWD 调试接口 | `connector=J2 SWD`；`pin1=3V3`；`pin2=SWCLK -> U3 PA14 pin20`；`pin3=SWDIO -> U3 PA13 pin19`；`pin4=NRST`；`pin5=GND` |
| 时钟 | MCU 与 HX711 时钟连接 | `mcu_osc_in=U3 PF0 pin2 no connection`；`mcu_osc_out=U3 PF1 pin3 no connection`；`hx711_xi=U2 XI pin14 no external clock shown`；`hx711_xo=U2 XO pin13 no external clock shown`；`external_frequency=null` |
| 保护电路 | 电源与模拟输入滤波 | `digital_power_filter=FB1 330R/GZ1005D331TF`；`analog_series=R4/R8 100Ω`；`analog_differential_cap=C5 100nF`；`grove_esd=null`；`input_fuse=null`；`reverse_protection=null` |
| 总线地址 | Unit Weight-I2C 对外 I2C 地址 | `documented_address=0x26`；`controller=U3 STM32F030F4P6`；`bus=PA9 SCL,PA10 SDA`；`schematic_address=null`；`address_selector=null` |
| 模拟电路 | 重量采集分辨率 | `documented_resolution=24Bit`；`adc=U2 HX711`；`sample_rate=null`；`gain=null`；`noise=null`；`accuracy=null`；`load_range=null`；`calibration=null` |

## 待确认事项

- `address.documented-0x26`：产品正文给出 I2C 地址 0x26；原理图只确认 U3 PA9/PA10 连接 J1 SCL/SDA，未在页内标注 0x26、地址选择引脚、拨码开关或固件协议。（证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页 J1 SCL/SDA 与 U3 PA9/PA10，图中无数字地址）
- `analog.documented-resolution`：产品正文称重量测量为 24Bit；原理图确认 ADC 型号为 HX711，但未在页内印出分辨率、采样率、增益、噪声、精度、量程或校准参数。（证据：图 cd4c9919b9b3 / 第 1 页 / 第 1 页网格 C3-D4，U2 仅标 HX711 型号和引脚，无性能参数）
- `review.i2c-address`：请通过当前固件协议或总线扫描确认 Unit Weight-I2C 的默认 I2C 地址为 0x26，并确认是否支持改址。；原因：原理图没有数字地址或地址选择电路，0x26 仅来自产品正文。
- `review.measurement-performance`：请依据 HX711 datasheet、量产固件和整机测试确认 24-bit 表述、实际采样率/增益/有效分辨率、支持的称重桥范围与校准要求。；原因：原理图只确认 HX711 连接，不能证明整机测量性能。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `cd4c9919b9b3b317f9d0db70941eff24a939254f29ba380220037ddcd94f1fac` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/632/SCH_UNIT_WEIGHT_I2C_sch_01.png` |

---

源文档：`zh_CN/unit/Unit-Weight I2C.md`

源文档 SHA-256：`91c18b63c5cdfc0bdb0adc8b1fff0aa77feb73099c7e3942cd08426e1bec81dd`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
