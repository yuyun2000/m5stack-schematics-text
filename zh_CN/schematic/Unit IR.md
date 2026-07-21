# Unit IR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit IR |
| SKU | U002 |
| 产品 ID | `unit-ir-0f40b3a22490` |
| 源文档 | `zh_CN/unit/ir.md` |

## 概述

Unit IR 通过 J1 Grove 接口提供独立的红外接收 INPUT 和发射控制 OUTPUT。U1 IRM-3638T 由 VCC/GND 供电，接收输出形成 INPUT 并由 R4 4.7KΩ 上拉到 VCC；OUTPUT 经 R2 1KΩ 驱动 Q1 SS8050 Y1，Q1 低边控制 VCC 经 R1 50Ω 和 D1 IR 的发射电流，R3 4.7KΩ将 OUTPUT 下拉。VCC 由 C1/C2 各 100nF 去耦，板上没有稳压器、主控、通信总线、时钟或外部存储。正文给出的 5V 供电、940nm 波长、38kHz 解调、NEC 等协议与不大于 5m 距离未直接印在图纸上，需结合器件资料或实测确认。

## 检索关键词

`Unit IR`、`U002`、`IRM-3638T`、`SS8050 Y1`、`D1 IR`、`infrared transmitter`、`infrared receiver`、`INPUT`、`OUTPUT`、`IR_RX`、`IR_TX`、`J1 Grove`、`VCC`、`5V`、`GND`、`R1 50Ω`、`R2 1KΩ`、`R3 4.7KΩ`、`R4 4.7KΩ`、`C1 100nF`、`C2 100nF`、`940nm`、`38kHz`、`NEC protocol`、`5m`、`low-side driver`、`active-high transmit`、`HY2.0-4P`、`remote control`、`hardware demodulation`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | IRM-3638T | 红外接收与解调模块，输出 INPUT 信号 | 图 ff191a12ad17 / 第 1 页 / 第 1 页左下 U1 IRM-3638T，VCC/OUT/GND |
| Q1 | SS8050 Y1 | 由 OUTPUT 控制的红外 LED NPN 低边驱动晶体管 | 图 ff191a12ad17 / 第 1 页 / 第 1 页左上 Q1 SS8050 Y1，基极/集电极/发射极连接 |
| D1 | IR | VCC 经 R1 供电、由 Q1 低边开关控制的红外发射二极管 | 图 ff191a12ad17 / 第 1 页 / 第 1 页左上 D1 IR，R1 与 Q1 之间 |
| J1 | Grove | 引出 INPUT、OUTPUT、VCC、GND 的四针接口 | 图 ff191a12ad17 / 第 1 页 / 第 1 页右中 J1 Grove pin1-pin4 |
| R1 | 50Ω | D1 红外发射支路的串联限流电阻 | 图 ff191a12ad17 / 第 1 页 / 第 1 页左上 VCC-R1 50Ω-D1-Q1 串联路径 |
| R2 | 1KΩ | OUTPUT 到 Q1 基极的串联限流电阻 | 图 ff191a12ad17 / 第 1 页 / 第 1 页左上 R2 1KΩ，OUTPUT 至 Q1 基极 |
| R3/R4 | 4.7KΩ | 分别将 OUTPUT 下拉到 GND、将 INPUT 上拉到 VCC | 图 ff191a12ad17 / 第 1 页 / 第 1 页 R3 OUTPUT-GND 与 R4 INPUT-VCC |
| C1/C2 | 100nF | J1 VCC 与 U1 VCC 的电源去耦电容 | 图 ff191a12ad17 / 第 1 页 / 第 1 页右侧 C1 100nF 与左下 C2 100nF |

## 系统结构

### Unit IR 系统结构

J1 pin1 接收 INPUT 来自 U1 IRM-3638T，J1 pin2 发射控制 OUTPUT 经 R2/Q1 驱动 D1 IR；VCC/GND 同时供给接收和发射两部分。

- 参数与网络：`receiver=U1 IRM-3638T`；`transmitter=D1 IR + Q1 SS8050 Y1`；`connector=J1 Grove`；`receive_net=INPUT`；`transmit_net=OUTPUT`；`onboard_mcu_shown=false`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页完整原理图接收、发射、J1 与电源区

## 核心器件

### D1/Q1 红外发射级

发射电流路径为 VCC→R1 50Ω→D1 IR→Q1 集电极，Q1 发射极接 GND，构成 NPN 低边开关。

- 参数与网络：`supply=VCC`；`current_limiter=R1 50Ω`；`emitter=D1 IR`；`switch=Q1 SS8050 Y1`；`return=Q1 emitter to GND`；`topology=low-side NPN`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页左上 VCC/R1/D1/Q1/GND 发射路径

## 电源

### VCC 电源轨

J1 pin3 输入 VCC，VCC 直接供给 U1 接收头、R4 INPUT 上拉以及 R1/D1 发射支路；C1/C2 各 100nF 从 VCC 接 GND，图中没有稳压器或电源开关。

- 参数与网络：`source=J1 pin3`；`loads=U1 VCC,R4,R1/D1`；`decoupling=C1 100nF,C2 100nF`；`regulator_shown=false`；`power_switch_shown=false`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页完整 VCC 网络与 C1/C2

## 接口

### J1 Grove

J1 pin1 标 I 并连接 INPUT，pin2 标 O 并连接 OUTPUT，pin3 标 VCC，pin4 标 GND；INPUT 方向为本板到主机，OUTPUT 方向为主机到本板。

- 参数与网络：`pin_1=I / INPUT / unit-to-host`；`pin_2=O / OUTPUT / host-to-unit`；`pin_3=VCC / power input`；`pin_4=GND`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页右中 J1 pin1-pin4 与 INPUT/OUTPUT/VCC/GND

## 总线地址

### 通信总线与地址

原理图未显示 I2C、SPI、UART、CAN、RS-485、USB 或设备地址；J1 使用两路独立 GPIO 型 INPUT/OUTPUT 信号。

- 参数与网络：`i2c_shown=false`；`spi_shown=false`；`uart_shown=false`；`can_shown=false`；`rs485_shown=false`；`usb_shown=false`；`device_address=null`；`interface=INPUT/OUTPUT GPIO`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页完整图仅有 INPUT/OUTPUT/VCC/GND

## GPIO 与控制信号

### INPUT 接收输出

U1 OUT 与 J1 pin1 共用 INPUT 网络，R4 4.7KΩ 将 INPUT 上拉到 VCC；图中未显示缓冲器、电平转换器或串联保护电阻。

- 参数与网络：`source=U1 OUT pin1`；`net=INPUT`；`destination=J1 pin1`；`pullup=R4 4.7KΩ to VCC`；`buffer_shown=false`；`level_shifter_shown=false`；`series_protection_shown=false`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页 U1 OUT/INPUT/R4 与 J1 pin1

### OUTPUT 发射控制

J1 pin2 的 OUTPUT 经 R2 1KΩ 连接 Q1 基极，R3 4.7KΩ 将 OUTPUT 下拉到 GND；OUTPUT 高电平向 Q1 基极提供驱动，OUTPUT 悬空时由 R3 保持低电平。

- 参数与网络：`source=J1 pin2`；`net=OUTPUT`；`base_resistor=R2 1KΩ`；`pulldown=R3 4.7KΩ to GND`；`transistor=Q1 SS8050 Y1`；`active_drive_level=high`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页 J1 OUTPUT、R2/R3 与 Q1 基极

## 时钟

### 时钟电路

完整原理图未显示晶振、振荡器或板级时钟网络；接收头内部解调时钟未展开。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`board_clock_net_shown=false`；`receiver_internal_clock_expanded=false`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页完整图无时钟器件或网络

## 复位

### 复位、BOOT 与调试

完整原理图未显示 MCU、RESET、BOOT、调试、下载或测试点接口。

- 参数与网络：`mcu_shown=false`；`reset_shown=false`；`boot_shown=false`；`debug_connector_shown=false`；`download_connector_shown=false`；`testpoint_shown=false`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页完整图无主控、复位或调试电路

## 保护电路

### Grove 与红外电路保护

完整原理图未显示 TVS、ESD 阵列、保险丝、反接保护或过流保护；发射支路仅由 R1 50Ω 限流，控制基极由 R2 1KΩ 限流。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`transmit_current_limiter=R1 50Ω`；`base_current_limiter=R2 1KΩ`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页 J1/U1/D1/Q1 全部路径

## 关键网络

### 红外收发关键网络

接收路径为 U1 OUT→INPUT→J1 pin1；发射控制路径为 J1 pin2→OUTPUT→R2→Q1，光电流路径为 VCC→R1→D1→Q1→GND。

- 参数与网络：`receive_path=U1.1->INPUT->J1.1`；`transmit_control=J1.2->OUTPUT->R2->Q1 base`；`transmit_current=VCC->R1->D1->Q1 collector/emitter->GND`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页完整 INPUT/OUTPUT 与发射电流路径

## 内存与 Flash

### 主控与存储器

完整原理图未显示 MCU、协处理器、Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`mcu_shown=false`；`coprocessor_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页完整图仅含红外器件、晶体管和无源器件

## 传感器

### U1 IRM-3638T

U1 VCC pin3 接 VCC、GND pin2 接地、OUT pin1 形成 INPUT 网络；C2 100nF 跨接 VCC 与 GND。

- 参数与网络：`vcc=U1 pin3 VCC`；`ground=U1 pin2 GND`；`output=U1 pin1 INPUT`；`decoupling=C2 100nF`
- 证据：图 ff191a12ad17 / 第 1 页 / 第 1 页左下 U1/C2 与 INPUT

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit IR 系统结构 | `receiver=U1 IRM-3638T`；`transmitter=D1 IR + Q1 SS8050 Y1`；`connector=J1 Grove`；`receive_net=INPUT`；`transmit_net=OUTPUT`；`onboard_mcu_shown=false` |
| 接口 | J1 Grove | `pin_1=I / INPUT / unit-to-host`；`pin_2=O / OUTPUT / host-to-unit`；`pin_3=VCC / power input`；`pin_4=GND` |
| 传感器 | U1 IRM-3638T | `vcc=U1 pin3 VCC`；`ground=U1 pin2 GND`；`output=U1 pin1 INPUT`；`decoupling=C2 100nF` |
| GPIO 与控制信号 | INPUT 接收输出 | `source=U1 OUT pin1`；`net=INPUT`；`destination=J1 pin1`；`pullup=R4 4.7KΩ to VCC`；`buffer_shown=false`；`level_shifter_shown=false`；`series_protection_shown=false` |
| GPIO 与控制信号 | OUTPUT 发射控制 | `source=J1 pin2`；`net=OUTPUT`；`base_resistor=R2 1KΩ`；`pulldown=R3 4.7KΩ to GND`；`transistor=Q1 SS8050 Y1`；`active_drive_level=high` |
| 核心器件 | D1/Q1 红外发射级 | `supply=VCC`；`current_limiter=R1 50Ω`；`emitter=D1 IR`；`switch=Q1 SS8050 Y1`；`return=Q1 emitter to GND`；`topology=low-side NPN` |
| 电源 | VCC 电源轨 | `source=J1 pin3`；`loads=U1 VCC,R4,R1/D1`；`decoupling=C1 100nF,C2 100nF`；`regulator_shown=false`；`power_switch_shown=false` |
| 电源 | J1 VCC 输入电压 | `documented_input=5V`；`schematic_net=VCC`；`voltage_printed_on_schematic=false`；`regulator_shown=false` |
| 传感器 | 红外波长、载波与距离 | `documented_wavelength=940nm`；`documented_receiver_frequency=38kHz`；`documented_protocols=NEC and other standard IR protocols`；`documented_distance=<=5m`；`specs_printed_on_schematic=false` |
| 关键网络 | 红外收发关键网络 | `receive_path=U1.1->INPUT->J1.1`；`transmit_control=J1.2->OUTPUT->R2->Q1 base`；`transmit_current=VCC->R1->D1->Q1 collector/emitter->GND` |
| 保护电路 | Grove 与红外电路保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`transmit_current_limiter=R1 50Ω`；`base_current_limiter=R2 1KΩ` |
| 总线地址 | 通信总线与地址 | `i2c_shown=false`；`spi_shown=false`；`uart_shown=false`；`can_shown=false`；`rs485_shown=false`；`usb_shown=false`；`device_address=null`；`interface=INPUT/OUTPUT GPIO` |
| 时钟 | 时钟电路 | `crystal_shown=false`；`oscillator_shown=false`；`board_clock_net_shown=false`；`receiver_internal_clock_expanded=false` |
| 复位 | 复位、BOOT 与调试 | `mcu_shown=false`；`reset_shown=false`；`boot_shown=false`；`debug_connector_shown=false`；`download_connector_shown=false`；`testpoint_shown=false` |
| 内存与 Flash | 主控与存储器 | `mcu_shown=false`；`coprocessor_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false` |

## 待确认事项

- `power.documented-5v-input`：产品正文 Grove 映射将 VCC 标为 5V，但原理图只标 VCC，没有打印允许电压或标称值。（证据：图 ff191a12ad17 / 第 1 页 / 第 1 页 J1 pin3 VCC 与完整 VCC 电源轨，页面无电压数值）
- `sensor.documented-ir-specs`：产品正文描述 940nm 发射、38kHz 硬件解调、NEC 等协议和不大于 5m 有效距离；原理图仅标 D1 IR 与 U1 IRM-3638T，没有打印波长、载波、协议或距离。（证据：图 ff191a12ad17 / 第 1 页 / 第 1 页 D1 IR 与 U1 IRM-3638T，页面无光学/载波/距离参数）
- `review.vcc-input`：请依据整板电气规格或实物确认 J1 VCC 的标称输入为 5V。；原因：5V 来自产品正文 Grove 映射，原理图仅标 VCC。
- `review.ir-specs`：请依据 D1/U1 数据手册与整板实测确认 940nm、38kHz、NEC 协议兼容性和不大于 5m 距离。；原因：这些参数来自产品正文，原理图未打印光学、载波、协议或距离规格。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ff191a12ad178cce870ac6589d4805a5ffcfca214e4ad13a520e938d39b5ec1a` | `https://static-cdn.m5stack.com/resource/docs/products/unit/ir/ir_sch_01.webp` |

---

源文档：`zh_CN/unit/ir.md`

源文档 SHA-256：`53f1506c9c0bcf3aaa7d42dccd0e408d232cbcd591f4421f472c74fa4edab1fa`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
