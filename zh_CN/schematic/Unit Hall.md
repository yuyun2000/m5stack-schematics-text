# Unit Hall 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Hall |
| SKU | U084 |
| 产品 ID | `unit-hall-5e561c7d32c0` |
| 源文档 | `zh_CN/unit/hall.md` |

## 概述

Unit Hall 使用 U1-U3 三颗 A3144E 霍尔开关产生 A、B、C 三路信号，每路由 820Ω 上拉至 +3.3V并以 20pF 电容对地滤波。U4 74HC08D 先计算 A 与 B，再将结果与 C 相与，形成 OUT；OUT 引至 J1 pin1，并在低电平时为 D1 红色 LED 提供灌电流路径。U5 HT7533 将 J1 VCC 稳压为 +3.3V，为传感器、逻辑门和指示灯供电，J1 pin2 IO 未连接。正文所述 5V Grove 供电和特定磁极方向触发低电平未直接印在原理图上，需结合 A3144E 资料或实测确认。

## 检索关键词

`Unit Hall`、`U084`、`A3144E`、`U1-U3`、`74HC08D`、`HT7533`、`Hall sensor`、`A AND B AND C`、`OUT`、`MISO`、`active low`、`D1 red LED 0603`、`R1-R3 820Ω`、`C1-C3 20pF`、`R4 1KΩ`、`VCC`、`+3.3V`、`5V Grove`、`GROVE_IO`、`J1 pin1`、`J1 pin2 NC`、`magnetic switch`、`S pole front`、`N pole back`、`C4 C5 100nF`、`C6 C7 10uF`、`digital output`、`door sensor`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1/U2/U3 | A3144E | 三颗霍尔开关，分别产生 A、B、C 三路数字感应信号 | 图 772ba2dc08da / 第 1 页 / 第 1 页上部 U1/U2/U3 A3144E，VCC/OUT/GND 引脚 |
| U4 | 74HC08D | 用两级二输入与门合并 A、B、C，生成 OUT | 图 772ba2dc08da / 第 1 页 / 第 1 页右中 U4 74HC08D pin1-pin14 |
| U5 | HT7533 | 将 J1 VCC 稳压为 +3.3V | 图 772ba2dc08da / 第 1 页 / 第 1 页左下 U5 HT7533，VIN/VOUT/GND |
| J1 | GROVE_IO | 外部电源与数字输出接口，pin1 输出 OUT/MISO，pin3 输入 VCC | 图 772ba2dc08da / 第 1 页 / 第 1 页下部中央 J1 GROVE_IO pin1-pin4 |
| D1 | 红灯 0603 | OUT 低电平状态指示 LED | 图 772ba2dc08da / 第 1 页 / 第 1 页中央 D1 红灯 0603，R4 与 OUT 之间 |
| R1/R2/R3 | 820Ω | 分别将 A、B、C 三路 A3144E 输出上拉到 +3.3V | 图 772ba2dc08da / 第 1 页 / 第 1 页上部 R1/R2/R3 820Ω 与 A/B/C |
| C1/C2/C3 | 20pF | 分别将 A、B、C 三路信号旁路到 GND 的小电容 | 图 772ba2dc08da / 第 1 页 / 第 1 页上部 C1/C2/C3 20pF 至 GND |
| R4 | 1KΩ | D1 红色 LED 从 +3.3V 到 OUT 的串联限流电阻 | 图 772ba2dc08da / 第 1 页 / 第 1 页中央 R4 1KΩ、D1、OUT |
| C4/C5/C6/C7 | 100nF / 100nF / 10uF / 10uF | VCC 与 +3.3V 电源轨的输入输出去耦和滤波 | 图 772ba2dc08da / 第 1 页 / 第 1 页下部 C4-C7，VCC/+3.3V 到 GND |

## 系统结构

### Unit Hall 系统结构

U1-U3 产生 A/B/C，U4 两级与门生成 OUT，D1 指示 OUT 低电平，J1 引出 OUT/VCC/GND，U5 从 VCC 生成 +3.3V。

- 参数与网络：`sensors=U1,U2,U3 A3144E`；`logic=U4 74HC08D`；`output=OUT to J1 pin1`；`indicator=D1 red LED`；`regulator=U5 HT7533`；`host_connector=J1 GROVE_IO`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页完整原理图全部功能区

## 核心器件

### U4 74HC08D 逻辑级联

U4 pin1 1A 接 A、pin2 1B 接 B，pin3 1Y 连接 pin4 2A；pin5 2B 接 C，pin6 2Y 输出 OUT，pin14 VCC 接 +3.3V，pin7 GND 接地。

- 参数与网络：`first_gate=A pin1 AND B pin2 -> 1Y pin3`；`cascade=pin3 1Y -> pin4 2A`；`second_gate=2A pin4 AND C pin5 -> OUT pin6`；`supply=pin14 +3.3V`；`ground=pin7 GND`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页右中 U4 pin1-pin7/pin14 与 A/B/C/OUT

### U4 未使用门

U4 的第三、第四与门引脚 pin8-pin13 在页面上未连接；原理图未显示这些未用输入的外部固定电平。

- 参数与网络：`unused_pins=pin8 3Y,pin9 3A,pin10 3B,pin11 4Y,pin12 4A,pin13 4B`；`external_tie_shown=false`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页右中 U4 右侧 pin8-pin13 无外部连线

## 电源

### U5 HT7533

U5 VIN pin2 接 J1 VCC，VOUT pin3 输出 +3.3V，GND pin1 接地；图中没有使能、负载开关、充电或电池路径。

- 参数与网络：`input=VCC at pin2`；`output=+3.3V at pin3`；`ground=GND at pin1`；`enable_shown=false`；`load_switch_shown=false`；`battery_shown=false`；`charger_shown=false`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页左下 U5 HT7533 与 J1 VCC

### VCC 与 +3.3V 滤波

VCC 侧配置 C4 100nF 和 C7 10uF 到 GND，+3.3V 侧配置 C5 100nF 和 C6 10uF 到 GND。

- 参数与网络：`vcc_caps=C4 100nF,C7 10uF`；`3v3_caps=C5 100nF,C6 10uF`；`return=GND`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页下部 C4-C7 与 U5 输入输出

## 接口

### J1 GROVE_IO

J1 pin1 标 MISO 并连接 OUT，pin2 标 IO 但未连接，pin3 标 VCC 并连接 U5 VIN，pin4 标 GND 并接地。

- 参数与网络：`pin_1=MISO / OUT / unit-to-host digital`；`pin_2=IO / no visible connection`；`pin_3=VCC / power input`；`pin_4=GND`；`output_direction=unit to host`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页下部中央 J1 GROVE_IO pin1-pin4

## 总线地址

### 通信总线与地址

原理图未显示 I2C、SPI、UART、CAN、RS-485、USB 或其他带地址的通信总线，J1 仅提供单路数字 OUT；页面无设备地址。

- 参数与网络：`i2c_shown=false`；`spi_shown=false`；`uart_shown=false`；`can_shown=false`；`rs485_shown=false`；`usb_shown=false`；`device_address=null`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页完整图仅有 A/B/C/OUT 与电源网络

## GPIO 与控制信号

### OUT 数字输出

按 U4 的两级与门连接，OUT=A AND B AND C；只有 A、B、C 均为高时 OUT 为高，任一路为低时 OUT 为低。

- 参数与网络：`expression=OUT=A&B&C`；`high_condition=A=1,B=1,C=1`；`low_condition=A=0 or B=0 or C=0`；`connector=J1 pin1`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页 U4 A/B 两级与门及 OUT 到 J1 pin1

### D1 输出状态指示

D1 红色 LED 与 R4 1KΩ 串联在 +3.3V 和 OUT 之间，因此 OUT 低电平时形成从 +3.3V 经 R4/D1 到 OUT 的电流路径，OUT 高电平时两端压差减小。

- 参数与网络：`supply=+3.3V`；`resistor=R4 1KΩ`；`led=D1 red 0603`；`sink_net=OUT`；`indicated_level=low`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页中央 +3.3V/R4/D1/OUT 串联路径

## 时钟

### 时钟电路

完整原理图未显示主控、晶振、振荡器或时钟网络；U4 为组合逻辑连接。

- 参数与网络：`mcu_shown=false`；`crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false`；`logic_type=combinational`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页完整图无时钟源或时钟网络

## 复位

### 复位、BOOT 与调试

完整原理图未显示 RESET、BOOT、使能控制、下载或调试接口。

- 参数与网络：`reset_shown=false`；`boot_shown=false`；`enable_control_shown=false`；`debug_connector_shown=false`；`download_connector_shown=false`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页完整图无复位、BOOT 或调试电路

## 保护电路

### J1 接口保护

完整原理图未在 J1 VCC、OUT、IO 或 GND 路径画出 TVS、ESD 阵列、保险丝、反接保护或串联信号保护器件。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`series_signal_protection_shown=false`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页 J1 至 U5/U4/D1 的全部路径

## 关键网络

### A/B/C 到 OUT 路径

关键路径为 U1 OUT→A→U4 1A、U2 OUT→B→U4 1B、U3 OUT→C→U4 2B，U4 1Y 反馈到 2A，最终 2Y→OUT→J1 pin1/D1。

- 参数与网络：`path_a=U1.2 A -> U4.1`；`path_b=U2.2 B -> U4.2`；`path_c=U3.2 C -> U4.5`；`cascade=U4.3 -> U4.4`；`output=U4.6 OUT -> J1.1 and D1`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页 A/B/C/U4/OUT 全信号链

## 内存与 Flash

### 主控与存储器

完整原理图未显示 MCU、协处理器、Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`mcu_shown=false`；`coprocessor_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页完整图仅含传感器、逻辑门、稳压器和无源器件

## 传感器

### U1-U3 A3144E

U1、U2、U3 的 pin1 VCC 均接 +3.3V、pin3 GND 均接地，pin2 OUT 分别形成 A、B、C 网络。

- 参数与网络：`u1=pin1 +3.3V,pin2 A,pin3 GND`；`u2=pin1 +3.3V,pin2 B,pin3 GND`；`u3=pin1 +3.3V,pin2 C,pin3 GND`；`count=3`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页上部 U1-U3 A3144E pin1-pin3

## 模拟电路

### A/B/C 输入整形

A、B、C 分别由 R1、R2、R3 820Ω 上拉到 +3.3V，并分别由 C1、C2、C3 20pF 连接到 GND。

- 参数与网络：`A=R1 820Ω to +3.3V,C1 20pF to GND`；`B=R2 820Ω to +3.3V,C2 20pF to GND`；`C=R3 820Ω to +3.3V,C3 20pF to GND`
- 证据：图 772ba2dc08da / 第 1 页 / 第 1 页上部 R1-R3/C1-C3 与 A/B/C 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Hall 系统结构 | `sensors=U1,U2,U3 A3144E`；`logic=U4 74HC08D`；`output=OUT to J1 pin1`；`indicator=D1 red LED`；`regulator=U5 HT7533`；`host_connector=J1 GROVE_IO` |
| 传感器 | U1-U3 A3144E | `u1=pin1 +3.3V,pin2 A,pin3 GND`；`u2=pin1 +3.3V,pin2 B,pin3 GND`；`u3=pin1 +3.3V,pin2 C,pin3 GND`；`count=3` |
| 模拟电路 | A/B/C 输入整形 | `A=R1 820Ω to +3.3V,C1 20pF to GND`；`B=R2 820Ω to +3.3V,C2 20pF to GND`；`C=R3 820Ω to +3.3V,C3 20pF to GND` |
| 核心器件 | U4 74HC08D 逻辑级联 | `first_gate=A pin1 AND B pin2 -> 1Y pin3`；`cascade=pin3 1Y -> pin4 2A`；`second_gate=2A pin4 AND C pin5 -> OUT pin6`；`supply=pin14 +3.3V`；`ground=pin7 GND` |
| GPIO 与控制信号 | OUT 数字输出 | `expression=OUT=A&B&C`；`high_condition=A=1,B=1,C=1`；`low_condition=A=0 or B=0 or C=0`；`connector=J1 pin1` |
| 核心器件 | U4 未使用门 | `unused_pins=pin8 3Y,pin9 3A,pin10 3B,pin11 4Y,pin12 4A,pin13 4B`；`external_tie_shown=false` |
| 接口 | J1 GROVE_IO | `pin_1=MISO / OUT / unit-to-host digital`；`pin_2=IO / no visible connection`；`pin_3=VCC / power input`；`pin_4=GND`；`output_direction=unit to host` |
| 电源 | U5 HT7533 | `input=VCC at pin2`；`output=+3.3V at pin3`；`ground=GND at pin1`；`enable_shown=false`；`load_switch_shown=false`；`battery_shown=false`；`charger_shown=false` |
| 电源 | VCC 与 +3.3V 滤波 | `vcc_caps=C4 100nF,C7 10uF`；`3v3_caps=C5 100nF,C6 10uF`；`return=GND` |
| 电源 | J1 VCC 输入电压 | `documented_input=5V`；`schematic_net=VCC`；`regulator=U5 HT7533`；`voltage_printed_on_schematic=false` |
| GPIO 与控制信号 | D1 输出状态指示 | `supply=+3.3V`；`resistor=R4 1KΩ`；`led=D1 red 0603`；`sink_net=OUT`；`indicated_level=low` |
| 关键网络 | A/B/C 到 OUT 路径 | `path_a=U1.2 A -> U4.1`；`path_b=U2.2 B -> U4.2`；`path_c=U3.2 C -> U4.5`；`cascade=U4.3 -> U4.4`；`output=U4.6 OUT -> J1.1 and D1` |
| 保护电路 | J1 接口保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`series_signal_protection_shown=false` |
| 总线地址 | 通信总线与地址 | `i2c_shown=false`；`spi_shown=false`；`uart_shown=false`；`can_shown=false`；`rs485_shown=false`；`usb_shown=false`；`device_address=null` |
| 时钟 | 时钟电路 | `mcu_shown=false`；`crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false`；`logic_type=combinational` |
| 复位 | 复位、BOOT 与调试 | `reset_shown=false`；`boot_shown=false`；`enable_control_shown=false`；`debug_connector_shown=false`；`download_connector_shown=false` |
| 内存与 Flash | 主控与存储器 | `mcu_shown=false`；`coprocessor_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false` |
| 传感器 | A3144E 磁极响应 | `documented_front_trigger=S pole`；`documented_back_trigger=N pole`；`documented_output=low`；`orientation_printed_on_schematic=false`；`threshold_printed_on_schematic=false` |

## 待确认事项

- `power.documented-5v-input`：产品正文的 Grove 映射将 J1 VCC 标为 5V，但原理图只标网络名 VCC 并接入 HT7533，没有直接打印输入电压数值。（证据：图 772ba2dc08da / 第 1 页 / 第 1 页 J1 pin3 VCC 至 U5 VIN，页面无 5V 标注）
- `sensor.documented-magnetic-polarity`：产品正文描述 S 极靠近正面或 N 极靠近背面时产生低电平；原理图只显示 A3144E 型号与电气连接，没有磁极方向、安装朝向或磁场阈值标注。（证据：图 772ba2dc08da / 第 1 页 / 第 1 页 U1-U3 A3144E，无磁极方向或阈值标注）
- `review.vcc-input`：请依据整板电气规格或实物确认 J1 VCC 的标称输入为 5V。；原因：5V 来自产品正文的 Grove 映射，原理图仅标 VCC。
- `review.magnetic-polarity`：请依据 A3144E 数据手册、PCB 安装朝向或实物测试确认正面 S 极/背面 N 极触发及低电平行为。；原因：原理图未定义传感器正反面、磁极方向或工作点。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `772ba2dc08da6b7c31fe5c7686c43d04a329caa4b636faceac91c25951a5056b` | `https://static-cdn.m5stack.com/resource/docs/products/unit/hall/hall_sch_01.webp` |

---

源文档：`zh_CN/unit/hall.md`

源文档 SHA-256：`8c67c5a625317000895f8d24e3eb45f6dd7b98d56771108390f318380d15bd0c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
