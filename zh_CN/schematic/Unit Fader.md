# Unit Fader 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Fader |
| SKU | U123 |
| 产品 ID | `unit-fader-21ccf33d2601` |
| 源文档 | `zh_CN/unit/fader.md` |

## 概述

Unit Fader 从 J1 接收 +5V，由 U1 HT7533 生成 +3.3V；R3 B10K/10K 推子跨接 +3.3V 与 GND，滑臂 RP1 经 C5 100nF 滤波后从 J1 pin1 输出模拟电压。J1 pin2 的 RGB 控制网由 R6 4.7KΩ 上拉到 +3.3V并进入 LED1，板上共画出 LED1-LED14 十四颗 +5V 供电的 SK6812，每颗配置 100nF 去耦。原理图明确画出 LED1-LED7 与 LED8-LED14 两段级联，但前段末端标为 RGB-1、后段起点标为 RGB-13，两网名称不一致，因此完整十四灯单链连接需复核。板上未显示主控、存储器、复位、时钟、调试或接口保护器件。

## 检索关键词

`Unit Fader`、`U123`、`HT7533`、`B10K`、`R3 10KΩ`、`slide potentiometer`、`RP1`、`analog output`、`SK6812`、`LED1-LED14`、`RGB`、`RGB-1`、`RGB-13`、`DIN`、`DOUT`、`HY-2.0_IO`、`Grove`、`J1 pin1 I`、`J1 pin2 O`、`+5V`、`+3.3V`、`R6 4.7KΩ`、`C1 22uF`、`C2 22uF`、`C5 100nF`、`C7-C20 100nF`、`RGB single-wire`、`fader voltage`、`VDD`、`VSS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | HT7533 | 将 J1 输入的 +5V 稳压为 +3.3V，供推子分压和 RGB 数据上拉使用 | 图 0f063bdd9d05 / 第 1 页 / 第 1 页左上 U1 HT7533，VIN pin2、VOUT pin3、GND pin1 |
| R3 | B10K / 10KΩ | 跨接 +3.3V 与 GND 的滑动电位器，滑臂形成 RP1 模拟输出 | 图 0f063bdd9d05 / 第 1 页 / 第 1 页上部中央 R3 B10K/10K，可调端标 RP1 |
| J1 | HY-2.0_IO | 四针 Grove 接口，引出 RP1 模拟信号、RGB 控制信号、+5V 和 GND | 图 0f063bdd9d05 / 第 1 页 / 第 1 页右上 J1 HY-2.0_IO，pin1-pin4 |
| LED1-LED14 | SK6812 | 十四颗 +5V 供电的可编程 RGB LED，使用 DIN/DOUT 串行数据连接 | 图 0f063bdd9d05 / 第 1 页 / 第 1 页中下部 LED1-LED14，每颗标 SK6812、DIN/DOUT/VDD/VSS |
| R6 | 4.7KΩ | 将 J1 RGB/LED1 DIN 数据网络上拉到 +3.3V | 图 0f063bdd9d05 / 第 1 页 / 第 1 页左中 R6 4.7KΩ，+3.3V 至 RGB/LED1 DIN |
| C1/C2 | 22uF | HT7533 的 +5V 输入和 +3.3V 输出滤波电容 | 图 0f063bdd9d05 / 第 1 页 / 第 1 页左上 C1/C2 22uF，分别接 +5V/+3.3V 到 GND |
| C5 | 100nF | RP1 推子滑臂模拟输出到 GND 的滤波电容 | 图 0f063bdd9d05 / 第 1 页 / 第 1 页上部中央 C5 100nF，RP1 至 GND |
| C7-C20 | 100nF | 十四颗 SK6812 的 +5V 电源去耦电容 | 图 0f063bdd9d05 / 第 1 页 / 第 1 页底部 C7-C20，各 100nF 跨接 +5V 与 GND |

## 系统结构

### Unit Fader 系统结构

J1 提供 +5V、GND、RGB 控制输入和 RP1 模拟输出；U1 生成 +3.3V，R3/C5 构成推子模拟链，LED1-LED14 构成原理图中的 RGB 灯阵列。

- 参数与网络：`host_connector=J1 HY-2.0_IO`；`regulator=U1 HT7533`；`analog=R3 B10K + C5`；`rgb_devices=LED1-LED14 SK6812`；`onboard_controller_shown=false`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页完整原理图：U1、R3/C5、J1、LED1-LED14

## 电源

### U1 HT7533

U1 VIN pin2 接 +5V、VOUT pin3 输出 +3.3V、GND pin1 接地；图中没有使能脚或外部电源开关。

- 参数与网络：`input=U1 pin2 +5V`；`output=U1 pin3 +3.3V`；`ground=U1 pin1 GND`；`enable_pin_shown=false`；`power_switch_shown=false`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页左上 U1 HT7533 电源引脚

### HT7533 输入输出滤波

C1 22uF 跨接 +5V 与 GND，C2 22uF 跨接 +3.3V 与 GND，分别位于 U1 输入和输出侧。

- 参数与网络：`input_cap=C1 22uF from +5V to GND`；`output_cap=C2 22uF from +3.3V to GND`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页左上 U1/C1/C2

### LED1-LED14 供电

十四颗 SK6812 的 VDD pin4 均接 +5V，VSS pin2 均接 GND；LED 数据上拉电源为 +3.3V，与 LED VDD 电源轨不同。

- 参数与网络：`devices=LED1-LED14`；`vdd=pin4 +5V`；`vss=pin2 GND`；`data_pullup_supply=+3.3V via R6`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页 LED1-LED14 VDD/VSS 与 R6 +3.3V

### LED 阵列去耦

C7-C20 共十四颗 100nF 电容分别跨接 +5V 与 GND，数量与 LED1-LED14 相同。

- 参数与网络：`capacitors=C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20`；`value=100nF`；`rail=+5V to GND`；`count=14`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页底部 C7-C20 100nF 去耦阵列

## 接口

### J1 HY-2.0_IO

J1 pin1 标 I 并接 RP1，pin2 标 O 并接 RGB，pin3 标 VCC 并接 +5V，pin4 标 GND 并接地；相对外部主机，RP1 是来自本板的模拟信号，RGB 是送入本板 LED 的控制信号。

- 参数与网络：`pin_1=I / RP1 / unit-to-host analog`；`pin_2=O / RGB / host-to-unit data`；`pin_3=VCC / +5V / power input`；`pin_4=GND`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页右上 J1 pin1 RP1、pin2 RGB、pin3 +5V、pin4 GND

## 总线

### LED1-LED7 SK6812 数据链

RGB 进入 LED1 DIN，LED1 至 LED7 依次以 DOUT pin1 连接下一颗 DIN pin3，LED7 DOUT 的页内网络标注为 RGB-1。

- 参数与网络：`input=RGB -> LED1 DIN pin3`；`chain=LED1->LED2->LED3->LED4->LED5->LED6->LED7`；`output=LED7 DOUT pin1 -> RGB-1`；`devices=7`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页中部上排 LED1-LED7 DIN/DOUT 连线与右端 RGB-1

### LED8-LED14 SK6812 数据链

RGB-13 网络进入 LED8 DIN，LED8 至 LED14 依次以 DOUT pin1 连接下一颗 DIN pin3；LED14 DOUT pin1 在页面上未继续连接。

- 参数与网络：`input=RGB-13 -> LED8 DIN pin3`；`chain=LED8->LED9->LED10->LED11->LED12->LED13->LED14`；`output=LED14 DOUT pin1 no visible connection`；`devices=7`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页中部下排 RGB-13 与 LED8-LED14 DIN/DOUT 连线

## 总线地址

### 总线地址

原理图未显示 I2C、SPI 片选或其他带设备地址的控制总线，也未打印任何器件地址；RGB 使用 J1 pin2 的单线数据连接。

- 参数与网络：`i2c_shown=false`；`spi_chip_select_shown=false`；`address_printed=false`；`control_interface=RGB single-wire via J1 pin2`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页 J1 与 LED1-LED14 控制路径，无地址脚或地址标注

## GPIO 与控制信号

### RGB 控制网络

J1 pin2 的 RGB 网络直接连接 LED1 DIN pin3，并由 R6 4.7KΩ 上拉到 +3.3V；图中未显示串联数据电阻或电平转换器。

- 参数与网络：`source=J1 pin2`；`net=RGB`；`destination=LED1 DIN pin3`；`pullup=R6 4.7KΩ to +3.3V`；`series_resistor_shown=false`；`level_shifter_shown=false`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页 J1 RGB、R6 与 LED1 DIN pin3 同名网络

## 时钟

### 时钟、复位与调试

完整原理图未显示晶振、振荡器、时钟网、复位/BOOT 网络、调试接口或下载连接器。

- 参数与网络：`clock_shown=false`；`crystal_shown=false`；`reset_shown=false`；`boot_shown=false`；`debug_connector_shown=false`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页完整图无时钟、复位、BOOT 或调试电路

## 保护电路

### J1 接口保护

完整原理图未在 J1 的 +5V、RP1、RGB 或 GND 路径画出 TVS、ESD 阵列、保险丝、反接保护或过流保护器件。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`overcurrent_protection_shown=false`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页 J1 至 U1/R3/LED1 的全部路径

## 关键网络

### +5V、+3.3V、RP1 与 RGB

+5V 从 J1 pin3 供给 U1 VIN 和全部 SK6812；+3.3V 从 U1 VOUT 供给 R3 上端与 R6；RP1 从 R3 滑臂到 J1 pin1，RGB 从 J1 pin2 到 LED1 DIN。

- 参数与网络：`5v=J1.3,U1 VIN,LED1-LED14 VDD,C1,C7-C20`；`3v3=U1 VOUT,R3 high,R6,C2`；`rp1=R3 wiper,C5,J1.1`；`rgb=J1.2,R6,LED1 DIN`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页完整 +5V/+3.3V/RP1/RGB 网络

## 内存与 Flash

### 主控与存储

完整原理图未显示 MCU、协处理器、Flash、EEPROM、RAM、SD 卡或其他存储器；控制与采样由 J1 外部主机承担。

- 参数与网络：`mcu_shown=false`；`coprocessor_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页完整图仅有稳压器、推子、LED 与无源器件

## 模拟电路

### R3 推子分压器

R3 标注 B10K/10KΩ，上端接 +3.3V、下端接 GND，滑臂网络为 RP1；该连接使滑臂电压位于两条电源轨之间。

- 参数与网络：`reference=R3`；`value=B10K / 10KΩ`；`high_terminal=+3.3V`；`low_terminal=GND`；`wiper=RP1`；`output_range_by_connection=GND to +3.3V`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页上部中央 R3 两端电源与 RP1 滑臂

### RP1 模拟输出滤波

RP1 与 R3 滑臂、J1 pin1 同网，并由 C5 100nF 直接旁路到 GND；图中未画运算放大器、缓冲器或 ADC。

- 参数与网络：`net=RP1`；`connector=J1 pin1`；`filter=C5 100nF to GND`；`buffer_shown=false`；`adc_shown=false`
- 证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页 R3 RP1/C5 与右上 J1 pin1 RP1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Fader 系统结构 | `host_connector=J1 HY-2.0_IO`；`regulator=U1 HT7533`；`analog=R3 B10K + C5`；`rgb_devices=LED1-LED14 SK6812`；`onboard_controller_shown=false` |
| 电源 | U1 HT7533 | `input=U1 pin2 +5V`；`output=U1 pin3 +3.3V`；`ground=U1 pin1 GND`；`enable_pin_shown=false`；`power_switch_shown=false` |
| 电源 | HT7533 输入输出滤波 | `input_cap=C1 22uF from +5V to GND`；`output_cap=C2 22uF from +3.3V to GND` |
| 模拟电路 | R3 推子分压器 | `reference=R3`；`value=B10K / 10KΩ`；`high_terminal=+3.3V`；`low_terminal=GND`；`wiper=RP1`；`output_range_by_connection=GND to +3.3V` |
| 模拟电路 | RP1 模拟输出滤波 | `net=RP1`；`connector=J1 pin1`；`filter=C5 100nF to GND`；`buffer_shown=false`；`adc_shown=false` |
| 接口 | J1 HY-2.0_IO | `pin_1=I / RP1 / unit-to-host analog`；`pin_2=O / RGB / host-to-unit data`；`pin_3=VCC / +5V / power input`；`pin_4=GND` |
| GPIO 与控制信号 | RGB 控制网络 | `source=J1 pin2`；`net=RGB`；`destination=LED1 DIN pin3`；`pullup=R6 4.7KΩ to +3.3V`；`series_resistor_shown=false`；`level_shifter_shown=false` |
| 总线 | LED1-LED7 SK6812 数据链 | `input=RGB -> LED1 DIN pin3`；`chain=LED1->LED2->LED3->LED4->LED5->LED6->LED7`；`output=LED7 DOUT pin1 -> RGB-1`；`devices=7` |
| 总线 | LED8-LED14 SK6812 数据链 | `input=RGB-13 -> LED8 DIN pin3`；`chain=LED8->LED9->LED10->LED11->LED12->LED13->LED14`；`output=LED14 DOUT pin1 no visible connection`；`devices=7` |
| 总线 | 十四颗 SK6812 完整级联 | `documented_led_count=14`；`upper_end=LED7 DOUT -> RGB-1`；`lower_start=RGB-13 -> LED8 DIN`；`net_names_match=false`；`continuous_chain_confirmed=false` |
| 电源 | LED1-LED14 供电 | `devices=LED1-LED14`；`vdd=pin4 +5V`；`vss=pin2 GND`；`data_pullup_supply=+3.3V via R6` |
| 电源 | LED 阵列去耦 | `capacitors=C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20`；`value=100nF`；`rail=+5V to GND`；`count=14` |
| 关键网络 | +5V、+3.3V、RP1 与 RGB | `5v=J1.3,U1 VIN,LED1-LED14 VDD,C1,C7-C20`；`3v3=U1 VOUT,R3 high,R6,C2`；`rp1=R3 wiper,C5,J1.1`；`rgb=J1.2,R6,LED1 DIN` |
| 保护电路 | J1 接口保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`overcurrent_protection_shown=false` |
| 时钟 | 时钟、复位与调试 | `clock_shown=false`；`crystal_shown=false`；`reset_shown=false`；`boot_shown=false`；`debug_connector_shown=false` |
| 内存与 Flash | 主控与存储 | `mcu_shown=false`；`coprocessor_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false` |
| 总线地址 | 总线地址 | `i2c_shown=false`；`spi_chip_select_shown=false`；`address_printed=false`；`control_interface=RGB single-wire via J1 pin2` |

## 待确认事项

- `bus.full-led-chain-continuity`：产品正文描述十四颗可编程 RGB 灯，但原理图上排 LED7 的输出网标为 RGB-1，下排 LED8 的输入网标为 RGB-13，两个名称不一致且页面未画直接连线，因此无法从原理图确认 LED7 与 LED8 连续级联。（证据：图 0f063bdd9d05 / 第 1 页 / 第 1 页上排右端 LED7/RGB-1 与下排左端 RGB-13/LED8）
- `review.led-chain-continuity`：请依据 PCB 网表、修订版原理图或实物测试确认 LED7 DOUT 与 LED8 DIN 是否相连，并核对 RGB-1/RGB-13 网络名。；原因：本页将前段末端标为 RGB-1、后段起点标为 RGB-13，网络名不一致且没有直接连线。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `0f063bdd9d059b9ee01c00a92e9e64a9abe106dff1791e852004c772b93ff3d3` | `https://static-cdn.m5stack.com/resource/docs/products/unit/fader/fader_sch_01.webp` |

---

源文档：`zh_CN/unit/fader.md`

源文档 SHA-256：`d3c4fe3884d5f70f12d7c34556ce570323b137e1853e07b31f00dd1d4c077066`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
