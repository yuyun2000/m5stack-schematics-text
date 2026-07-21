# Unit 4Relay 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit 4Relay |
| SKU | U097 |
| 产品 ID | `unit-4relay-30ce3c3f2670` |
| 源文档 | `zh_CN/unit/4relay.md` |

## 概述

Unit 4Relay 以 U1 STM32F030F4P6 作为 I2C 控制器，PA0~PA3 经 RP2 和 Q1~Q4 驱动四只 5V 继电器，PA4~PA7 经 RP1 驱动四颗状态 LED。J5 Grove 提供 SCL、SDA、5V、GND，U2 XC6206 将 5V 稳压为 MCU 使用的 VCC，J6 提供 SWD。每路继电器线圈均有反向二极管，触点引到 J1~J4 四针端子，但图中未标清 COM/NO/NC 针序且未配置触点吸收网络。正文给出的 I2C 0x26、AC/DC 负载额定、LED 同步模式和物理隔离能力需结合固件、BOM、PCB 与测试确认。

## 检索关键词

`Unit 4Relay`、`U097`、`STM32F030F4P6`、`XC6206`、`I2C`、`0x26`、`Grove`、`SCL`、`SDA`、`PA0`、`PA1`、`PA2`、`PA3`、`PA4`、`PA5`、`PA6`、`PA7`、`RL1`、`RL2`、`RL3`、`RL4`、`LED1`、`LED2`、`LED3`、`LED4`、`SS8050 Y1`、`RELAY-TH_932-XXVDC-SL-AH`、`CON4`、`SWD`、`NRST`、`5V`、`VCC`、`AC 250V`、`DC 28V`、`10A`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | I2C 从设备 MCU，控制四路继电器和四颗状态 LED | 图 9b13baae39ff / 第 1 页 / 第 1 页 B2-C3 U1 STM32F030F4P6 |
| U2 | XC6206 | 5V 到 VCC 的线性稳压器 | 图 9b13baae39ff / 第 1 页 / 第 1 页 B1 U2 XC6206 |
| K1/K2/K3/K4 | RELAY-TH_932-XXVDC-SL-AH | 四路 5V 线圈机械继电器，触点分别接 J1/J2/J3/J4 | 图 9b13baae39ff / 第 1 页 / 第 1 页 A2-B3 K1-K4 |
| Q1/Q2/Q3/Q4 | SS8050 Y1 | 四路继电器线圈低侧驱动晶体管 | 图 9b13baae39ff / 第 1 页 / 第 1 页 B1-C2 Q1-Q4 |
| D1/D2/D3/D4 | 未标注 | 四路继电器线圈反向续流二极管 | 图 9b13baae39ff / 第 1 页 / 第 1 页 B2-B3 D1-D4 |
| J1/J2/J3/J4 | CON4 | 四组继电器触点四针输出端子 | 图 9b13baae39ff / 第 1 页 / 第 1 页 A2 J1-J4 CON4 |
| J5 | GROVE | SCL、SDA、5V、GND 四针 I2C/电源接口 | 图 9b13baae39ff / 第 1 页 / 第 1 页 B3-C3 J5 GROVE |
| J6 | SWD_5p | VCC、SWCLK、SWDIO、NRST、GND 调试接口 | 图 9b13baae39ff / 第 1 页 / 第 1 页 C3-D3 J6 SWD_5p |
| RP1/RP2 | 1K | 四路 LED 和四路继电器晶体管基极的电阻阵列 | 图 9b13baae39ff / 第 1 页 / 第 1 页 B2-C2 RP1/RP2 1K |
| LED1/LED2/LED3/LED4 | LED | 四路由 MCU 独立控制的状态指示灯 | 图 9b13baae39ff / 第 1 页 / 第 1 页 C1-C2 LED1-LED4 |

## 系统结构

### Unit 4Relay

U1 通过 J5 I2C 接收控制，使用 PA0~PA3 驱动四路继电器、PA4~PA7 驱动四颗 LED；U2 由 5V 生成 VCC，J6 提供 SWD。

- 参数与网络：`mcu=U1 STM32F030F4P6`；`relays=K1-K4`；`drivers=Q1-Q4`；`indicators=LED1-LED4`；`host=J5 Grove I2C`；`regulator=U2 XC6206`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页完整功能分区

## 核心器件

### K1-K4 线圈驱动

每只继电器线圈一端接 5V，另一端由对应 Q1~Q4 下拉；D1/D2/D3/D4 分别跨 K4/K3/K2/K1 线圈反向连接。

- 参数与网络：`K1=Q1/RL1,D4 flyback`；`K2=Q2/RL2,D3 flyback`；`K3=Q3/RL3,D2 flyback`；`K4=Q4/RL4,D1 flyback`；`coil_supply=5V`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页 A2-B3 K1-K4/D1-D4 与 B1-C2 Q1-Q4

## 电源

### U2 XC6206

U2 VIN 接 5V、OUT 输出 VCC、GND 接地；输入 C1 104/C2 106，输出 C3 106/C4 104。5V 还直接供四路继电器线圈。

- 参数与网络：`input=5V`；`output=VCC`；`input_caps=C1 104,C2 106`；`output_caps=C3 106,C4 104`；`relay_coil_rail=5V`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页 B1 U2 与 K1-K4 线圈 5V

## 接口

### J5 GROVE

J5 针脚为 1=GND、2=5V、3=SDA、4=SCL。

- 参数与网络：`pin_1=GND`；`pin_2=5V`；`pin_3=SDA`；`pin_4=SCL`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页 B3-C3 J5

## 总线

### U1 I2C

J5.4 SCL 连接 U1 PA9 pin17，J5.3 SDA 连接 U1 PA10 pin18；当前页没有画 SCL/SDA 上拉电阻。

- 参数与网络：`scl=J5.4 -> U1 PA9 pin17`；`sda=J5.3 -> U1 PA10 pin18`；`pullups_shown=false`；`controller=external host`；`device=U1`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页 U1 SCL/SDA 与 J5

## GPIO 与控制信号

### 四路继电器控制

U1 PA0/PA1/PA2/PA3 分别通过 RP2 四个 1K 电阻驱动 Q1/Q2/Q3/Q4，对应 RL1/RL2/RL3/RL4。

- 参数与网络：`relay_1=U1 PA0 -> RP2 -> Q1 -> RL1`；`relay_2=U1 PA1 -> RP2 -> Q2 -> RL2`；`relay_3=U1 PA2 -> RP2 -> Q3 -> RL3`；`relay_4=U1 PA3 -> RP2 -> Q4 -> RL4`；`resistors=RP2 1K`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页 B1-C2 U1 PA0-PA3、RP2、Q1-Q4

### 四路状态 LED

U1 PA4/PA5/PA6/PA7 通过 RP1 1K 分别连接 LED2/LED3/LED1/LED4，各 LED 另一端接 GND。

- 参数与网络：`PA4=LED2`；`PA5=LED3`；`PA6=LED1`；`PA7=LED4`；`resistors=RP1 1K`；`return=GND`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页 C1-C2 U1 PA4-PA7、RP1、LED1-4

## 时钟

### U1 时钟

U1 PF1-OSC 未连接，完整页面未显示外部晶振或振荡器。

- 参数与网络：`PF1=NC`；`crystal_shown=false`；`oscillator_shown=false`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页 U1 PF1-OSC 与完整图

## 复位

### U1 NRST

U1 NRST pin4 连接 NRST 网络，并由 C5 104 对 GND；J6.4 引出 NRST，图中未画外部复位上拉。

- 参数与网络：`mcu_pin=U1.4 NRST`；`capacitor=C5 104`；`debug_pin=J6.4`；`external_pullup_shown=false`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页 C3 U1 NRST/C5/J6

## 保护电路

### 继电器线圈保护

D1~D4 分别反向跨接四路线圈，用于抑制低侧晶体管关断时的感性尖峰。

- 参数与网络：`diodes=D1,D2,D3,D4`；`protected=K4,K3,K2,K1 coils`；`drivers=Q4,Q3,Q2,Q1`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页 B2-B3 D1-D4

### 继电器触点保护

K1~K4 触点到 J1~J4 的路径未画 RC 吸收、MOV、TVS、保险丝或过流保护。

- 参数与网络：`snubber_shown=false`；`mov_shown=false`；`tvs_shown=false`；`fuse_shown=false`；`overcurrent_shown=false`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页 A2 K1-K4/J1-J4 触点路径

## 内存与 Flash

### 外部存储器

完整原理图未展示 U1 之外的 Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页完整图无外部存储器

## 调试与烧录

### J6 SWD

J6.1=VCC、2=SWCLK、3=SWDIO、4=NRST、5=GND；SWCLK/SWDIO 连接 U1 PA14/PA13。

- 参数与网络：`pin_1=VCC`；`pin_2=SWCLK U1 PA14`；`pin_3=SWDIO U1 PA13`；`pin_4=NRST`；`pin_5=GND`
- 证据：图 9b13baae39ff / 第 1 页 / 第 1 页 C3-D3 J6

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit 4Relay | `mcu=U1 STM32F030F4P6`；`relays=K1-K4`；`drivers=Q1-Q4`；`indicators=LED1-LED4`；`host=J5 Grove I2C`；`regulator=U2 XC6206` |
| 总线 | U1 I2C | `scl=J5.4 -> U1 PA9 pin17`；`sda=J5.3 -> U1 PA10 pin18`；`pullups_shown=false`；`controller=external host`；`device=U1` |
| 总线地址 | Unit 4Relay I2C 地址 | `documented_address=0x26`；`address_hardware_shown=false`；`firmware_controlled=true` |
| 接口 | J5 GROVE | `pin_1=GND`；`pin_2=5V`；`pin_3=SDA`；`pin_4=SCL` |
| GPIO 与控制信号 | 四路继电器控制 | `relay_1=U1 PA0 -> RP2 -> Q1 -> RL1`；`relay_2=U1 PA1 -> RP2 -> Q2 -> RL2`；`relay_3=U1 PA2 -> RP2 -> Q3 -> RL3`；`relay_4=U1 PA3 -> RP2 -> Q4 -> RL4`；`resistors=RP2 1K` |
| GPIO 与控制信号 | 四路状态 LED | `PA4=LED2`；`PA5=LED3`；`PA6=LED1`；`PA7=LED4`；`resistors=RP1 1K`；`return=GND` |
| 电源 | U2 XC6206 | `input=5V`；`output=VCC`；`input_caps=C1 104,C2 106`；`output_caps=C3 106,C4 104`；`relay_coil_rail=5V` |
| 核心器件 | K1-K4 线圈驱动 | `K1=Q1/RL1,D4 flyback`；`K2=Q2/RL2,D3 flyback`；`K3=Q3/RL3,D2 flyback`；`K4=Q4/RL4,D1 flyback`；`coil_supply=5V` |
| 接口 | J1-J4 CON4 | `relay_1=K1 -> J1`；`relay_2=K2 -> J2`；`relay_3=K3 -> J3`；`relay_4=K4 -> J4`；`connector_pins=1,2,3,4`；`com_no_nc_order=null` |
| 保护电路 | 继电器线圈保护 | `diodes=D1,D2,D3,D4`；`protected=K4,K3,K2,K1 coils`；`drivers=Q4,Q3,Q2,Q1` |
| 保护电路 | 继电器触点保护 | `snubber_shown=false`；`mov_shown=false`；`tvs_shown=false`；`fuse_shown=false`；`overcurrent_shown=false` |
| 复位 | U1 NRST | `mcu_pin=U1.4 NRST`；`capacitor=C5 104`；`debug_pin=J6.4`；`external_pullup_shown=false` |
| 调试与烧录 | J6 SWD | `pin_1=VCC`；`pin_2=SWCLK U1 PA14`；`pin_3=SWDIO U1 PA13`；`pin_4=NRST`；`pin_5=GND` |
| 其他事实 | 正文控制寄存器与 LED 模式 | `mode_register=0x10`；`control_register=0x11`；`documented_modes=Manual,Auto LED sync`；`firmware_behavior_on_schematic=null` |
| 其他事实 | 正文继电器额定 | `documented_ac=250V 10A`；`documented_dc=28V 10A`；`documented_inrush=16A`；`schematic_part=RELAY-TH_932-XXVDC-SL-AH`；`test_conditions=null` |
| 时钟 | U1 时钟 | `PF1=NC`；`crystal_shown=false`；`oscillator_shown=false` |
| 内存与 Flash | 外部存储器 | `flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `address.documented-0x26`：正文和通信协议列出 I2C 地址 0x26，原理图没有地址选择硬件或地址标注，地址由 U1 固件决定。（证据：图 9b13baae39ff / 第 1 页 / 第 1 页 U1/J5 I2C 网络无地址标注）
- `interface.relay-terminals`：K1/K2/K3/K4 的触点分别引到 J1/J2/J3/J4 四针端子；原理图未使用 COM/NO/NC 网络名，无法从本页可靠给出四针端子的功能顺序。（证据：图 9b13baae39ff / 第 1 页 / 第 1 页 A2 K1-K4 与 J1-J4，无触点网络名）
- `other.documented-firmware`：正文定义 0x10 模式寄存器、0x11 继电器/LED 控制寄存器以及 Manual/Auto LED 同步模式；原理图只显示独立 GPIO 路径，不能确认寄存器和固件行为。（证据：图 9b13baae39ff / 第 1 页 / 第 1 页 U1 GPIO 硬件无寄存器标注）
- `other.documented-ratings`：正文列出 AC 250V/DC 28V、10A 和 16A 瞬时电流；原理图继电器值为通用 RELAY-TH_932-XXVDC-SL-AH 占位式料号，未标负载类别、温升、寿命或安规条件。（证据：图 9b13baae39ff / 第 1 页 / 第 1 页 K1-K4 未标额定条件）
- `review.i2c-address`：请通过固件或 I2C 扫描确认默认地址 0x26。；原因：原理图没有地址选择硬件或地址标注。
- `review.terminal-pinout`：请依据 PCB/端子丝印确认 J1~J4 四针的 COM、NO、NC 及重复触点顺序。；原因：原理图只画触点到 1~4 针，没有功能网络名。
- `review.firmware-registers`：请依据 U097 内置固件确认 0x10/0x11 寄存器位定义和 LED Manual/Auto 行为。；原因：这些行为不能由 GPIO 原理图推导。
- `review.relay-ratings`：请依据量产继电器准确料号、PCB 间距和测试报告确认 AC/DC 额定、瞬时电流和隔离能力。；原因：原理图料号为通用占位形式且没有系统级额定条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9b13baae39ff2dd57896bc4b564668a1a2fc15c4f3d820d4a03fbb6480202e35` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/589/Sch_UNIT-4RELAY_sch_01.png` |

---

源文档：`zh_CN/unit/4relay.md`

源文档 SHA-256：`a74e094ee835082dabdc5996f5baf3f77e25cea5593093176277c5e5d1de9a0d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
