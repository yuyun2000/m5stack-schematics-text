# Unit AIN4-20mA 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit AIN4-20mA |
| SKU | U162 |
| 产品 ID | `unit-ain4-20ma-d3746bdaf710` |
| 源文档 | `zh_CN/unit/AIN4-20mA Unit.md` |

## 概述

Unit AIN4-20mA 以 HCNR200-500E 线性光耦隔离单通道电流输入：MI+/MI- 侧由 U2 SGM321YC5/TR、Q1 和 U1A/U1B 构成输入闭环，隔离后的 U1C 光电流由 U3 SGM321YC5/TR 转换为 VOUT。U14 STM32G030F6 在 PA1 采集 VOUT，并通过 Grove I2C 与主机通信；U15 HX6306P332MR 将 VCC_5V 转为 VCC_3V3。P1 提供 24V、GND_ISO、IN+、IN-，P2/P3 跳帽按照图纸注释配置有源或无源输入接线。正文给出的 0x55、200Ω 典型输入阻抗和 4-20mA 精度/标定参数未在图纸中完整标注，需固件与测试资料确认。

## 检索关键词

`Unit AIN4-20mA`、`U162`、`STM32G030F6`、`HCNR200-500E`、`SGM321YC5/TR`、`HX6306P332MR`、`BC807-40W,115`、`BZT52C5V1S`、`I2C`、`0x55`、`4-20mA`、`IN+`、`IN-`、`MI+`、`MI-`、`VOUT`、`PA1`、`24V`、`GND_ISO`、`VCC_5V`、`VCC_3V3`、`R5 24R`、`R1 62K`、`active input`、`passive input`、`P2`、`P3`、`SWD`、`analog isolation`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U14 | STM32G030F6 | I2C 通信与 VOUT ADC 采样 MCU | 图 d18acd6ea198 / 第 1 页 / 第 1 页 B3-C4 U14 STM32G030F6 |
| U1A/U1B/U1C | HCNR200-500E | 输入侧 LED/反馈光电二极管与输出侧光电二极管组成的线性模拟隔离器 | 图 d18acd6ea198 / 第 1 页 / 第 1 页 B1-C3 U1A/U1B/U1C HCNR200-500E |
| U2/U3 | SGM321YC5/TR | HCNR200 输入反馈驱动与隔离侧光电流到 VOUT 的跨阻/放大运放 | 图 d18acd6ea198 / 第 1 页 / 第 1 页 B1-C3 U2/U3 SGM321YC5/TR |
| U15 | HX6306P332MR | VCC_5V 到 VCC_3V3 的稳压器 | 图 d18acd6ea198 / 第 1 页 / 第 1 页 A1-A2 U15 |
| Q1 | BC807-40W,115 | U2 控制的 HCNR200 输入 LED 驱动晶体管 | 图 d18acd6ea198 / 第 1 页 / 第 1 页 B2-C2 Q1 |
| D1 | BZT52C5V1S | MI+/MI- 模拟输入节点的 5.1V 钳位器件 | 图 d18acd6ea198 / 第 1 页 / 第 1 页 B2-C2 D1 |
| P1 | HT3.96 4P | 24V、GND_ISO、IN+、IN- 现场端子 | 图 d18acd6ea198 / 第 1 页 / 第 1 页 D1 P1 |
| P2/P3 | Header 4 / Header 2 | 有源/无源 4-20mA 输入接线模式跳帽矩阵 | 图 d18acd6ea198 / 第 1 页 / 第 1 页 D2 P2/P3 与接线注释 |
| J1 | GROVE_IO | SCL、SDA、VCC_5V、GND I2C/电源接口 | 图 d18acd6ea198 / 第 1 页 / 第 1 页 A1 J1 GROVE_IO |
| J2 | SWD_5P | VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST、GND 调试接口 | 图 d18acd6ea198 / 第 1 页 / 第 1 页 D3 J2 SWD_5P |
| R5 | 24R | MI- 输入支路串联电阻 | 图 d18acd6ea198 / 第 1 页 / 第 1 页 C1 R5 24R |

## 系统结构

### Unit AIN4-20mA

P1/P2/P3 配置现场电流回路，U2/Q1/HCNR200 输入侧将信号线性隔离，U3 输出 VOUT 给 U14 PA1，U14 通过 I2C 向主机报告。

- 参数与网络：`field_input=P1/P2/P3`；`isolation=U1 HCNR200-500E`；`input_amp=U2 SGM321YC5/TR`；`output_amp=U3 SGM321YC5/TR`；`mcu=U14 STM32G030F6`；`adc_net=VOUT`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页完整功能分区

## 电源

### VCC_5V/VCC_3V3

J1 VCC_5V 为 U3 隔离输出运放供电，并进入 U15 HX6306P332MR；U15 输出 VCC_3V3 为 U14 和 I2C 上拉供电，输入 C4/C6、输出 C2/C3 配置图示去耦。

- 参数与网络：`input=VCC_5V`；`regulator=U15 HX6306P332MR`；`output=VCC_3V3`；`input_caps=C4/C6`；`output_caps=C2/C3`；`loads=U14,R6,R7`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 A1-A2 U15 与全图电源网

## 接口

### P1 HT3.96 4P

P1.1=24V、P1.2=GND_ISO、P1.3=IN+、P1.4=IN-。

- 参数与网络：`pin_1=24V`；`pin_2=GND_ISO`；`pin_3=IN+`；`pin_4=IN-`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 D1 P1

### P2/P3 跳线

P2.1=24V、P2.2=IN+、P2.3=MI-、P2.4=GND_ISO；P3.1=MI+、P3.2=IN-。

- 参数与网络：`P2_1=24V`；`P2_2=IN+`；`P2_3=MI-`；`P2_4=GND_ISO`；`P3_1=MI+`；`P3_2=IN-`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 D2 P2/P3

### 有源/无源传感器跳帽

图纸注释：Active Input 短接 P2.1-P2.2、P2.3-P2.4、P3.1-P3.2；Passive Input 短接 P2.2-P3.1、P2.3-P3.2。

- 参数与网络：`active=P2.1-P2.2;P2.3-P2.4;P3.1-P3.2`；`passive=P2.2-P3.1;P2.3-P3.2`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 D2 Active Input/Passive Input 注释

### J1 GROVE_IO

J1 针脚为 IO2/SCL、IO1/SDA、VCC_5V、GND。

- 参数与网络：`pin_scl=IO2 SCL`；`pin_sda=IO1 SDA`；`power=VCC_5V`；`ground=GND`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 A1 J1

## 总线

### U14 I2C

J1 SCL/SDA 分别连接 U14 PB7/PB8 pin1 和 PB9/PC14 pin2，R6/R7 各 4.7K 上拉至 VCC_3V3。

- 参数与网络：`scl=J1 SCL -> U14 PB7/PB8 pin1`；`sda=J1 SDA -> U14 PB9/PC14 pin2`；`pullups=R6/R7 4.7K`；`rail=VCC_3V3`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 A1 J1/R6/R7 与 B3 U14

## 时钟

### U14 时钟

U14 PC14-OSC32_IN/PC15-OSC32_OUT 未连接，完整页面未显示外部晶振或振荡器。

- 参数与网络：`osc32_in=NC`；`osc32_out=NC`；`crystal_shown=false`；`oscillator_shown=false`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 U14 pin2/pin3 与完整图

## 保护电路

### MI+/MI- 钳位与滤波

D1 BZT52C5V1S 和 C2 100nF 跨接 MI+/MI- 输入域，R5 24R 串联在 MI-；图中未画现场端 TVS 阵列或保险丝。

- 参数与网络：`zener=D1 BZT52C5V1S`；`capacitor=C2 100nF`；`series_resistor=R5 24R`；`field_tvs_array_shown=false`；`fuse_shown=false`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 B2-C2 D1/C2/R5

## 内存与 Flash

### 外部存储器

完整原理图未展示 U14 之外的 Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页完整图无外部存储器

## 调试与烧录

### U14 SWD/NRST

J2.1=VCC_3V3、2=MCU_SWCLK、3=MCU_SWDIO、4=NRST、5=GND；NRST 由 R27 10K 上拉 VCC_3V3、C20 100nF 对地，R26 DNP 从 SWCLK 到 GND。

- 参数与网络：`swd=J2 1:VCC_3V3,2:SWCLK,3:SWDIO,4:NRST,5:GND`；`reset=R27 10K,C20 100nF`；`optional_pulldown=R26 DNP`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 B3-D3 U14/J2/R26/R27/C20

## 模拟电路

### MI+/MI- 隔离输入侧

MI- 经 R5 24R 进入输入网络；U1B 光电二极管与 R2/R4 各 10K 形成 U2 反馈，U2 输出经 C3 1nF 和 Q1 BC807-40W,115 驱动 U1A 光耦 LED。

- 参数与网络：`input_nets=MI+,MI-`；`series=R5 24R`；`feedback=U1B,R2 10K,R4 10K,U2 SGM321`；`driver=Q1 BC807-40W,115`；`led=U1A`；`compensation=C3 1nF`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 B1-C2 U1A/U1B/U2/Q1/R5

### U1C/U3 VOUT

隔离侧 U1C 光电二极管连接 U3 SGM321；R1 62K 与 C1 1nF 并联构成反馈，U3 输出形成 VOUT。

- 参数与网络：`photodiode=U1C HCNR200-500E`；`opamp=U3 SGM321YC5/TR`；`feedback=R1 62K parallel C1 1nF`；`output=VOUT`；`supply=VCC_5V`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 B2-C3 U1C/U3/R1/C1

### U14 VOUT 采样

VOUT 直接连接 U14 PA1 pin8；U14 由 VCC_3V3 供电，图中未画 VOUT 到 PA1 的额外分压或钳位。

- 参数与网络：`net=VOUT`；`mcu_pin=U14 PA1 pin8`；`mcu_supply=VCC_3V3`；`divider_shown=false`；`adc_clamp_shown=false`
- 证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 U3 VOUT 到 U14 PA1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit AIN4-20mA | `field_input=P1/P2/P3`；`isolation=U1 HCNR200-500E`；`input_amp=U2 SGM321YC5/TR`；`output_amp=U3 SGM321YC5/TR`；`mcu=U14 STM32G030F6`；`adc_net=VOUT` |
| 接口 | P1 HT3.96 4P | `pin_1=24V`；`pin_2=GND_ISO`；`pin_3=IN+`；`pin_4=IN-` |
| 接口 | P2/P3 跳线 | `P2_1=24V`；`P2_2=IN+`；`P2_3=MI-`；`P2_4=GND_ISO`；`P3_1=MI+`；`P3_2=IN-` |
| 接口 | 有源/无源传感器跳帽 | `active=P2.1-P2.2;P2.3-P2.4;P3.1-P3.2`；`passive=P2.2-P3.1;P2.3-P3.2` |
| 模拟电路 | MI+/MI- 隔离输入侧 | `input_nets=MI+,MI-`；`series=R5 24R`；`feedback=U1B,R2 10K,R4 10K,U2 SGM321`；`driver=Q1 BC807-40W,115`；`led=U1A`；`compensation=C3 1nF` |
| 模拟电路 | U1C/U3 VOUT | `photodiode=U1C HCNR200-500E`；`opamp=U3 SGM321YC5/TR`；`feedback=R1 62K parallel C1 1nF`；`output=VOUT`；`supply=VCC_5V` |
| 模拟电路 | U14 VOUT 采样 | `net=VOUT`；`mcu_pin=U14 PA1 pin8`；`mcu_supply=VCC_3V3`；`divider_shown=false`；`adc_clamp_shown=false` |
| 保护电路 | MI+/MI- 钳位与滤波 | `zener=D1 BZT52C5V1S`；`capacitor=C2 100nF`；`series_resistor=R5 24R`；`field_tvs_array_shown=false`；`fuse_shown=false` |
| 总线 | U14 I2C | `scl=J1 SCL -> U14 PB7/PB8 pin1`；`sda=J1 SDA -> U14 PB9/PC14 pin2`；`pullups=R6/R7 4.7K`；`rail=VCC_3V3` |
| 总线地址 | Unit AIN4-20mA I2C 地址 | `documented_address=0x55`；`address_hardware_shown=false`；`firmware_controlled=true` |
| 接口 | J1 GROVE_IO | `pin_scl=IO2 SCL`；`pin_sda=IO1 SDA`；`power=VCC_5V`；`ground=GND` |
| 电源 | VCC_5V/VCC_3V3 | `input=VCC_5V`；`regulator=U15 HX6306P332MR`；`output=VCC_3V3`；`input_caps=C4/C6`；`output_caps=C2/C3`；`loads=U14,R6,R7` |
| 调试与烧录 | U14 SWD/NRST | `swd=J2 1:VCC_3V3,2:SWCLK,3:SWDIO,4:NRST,5:GND`；`reset=R27 10K,C20 100nF`；`optional_pulldown=R26 DNP` |
| 其他事实 | 正文 4-20mA 与输入阻抗 | `documented_range=4-20mA`；`documented_impedance=200Ω typical`；`visible_series_resistor=R5 24R`；`accuracy=null`；`calibration=null` |
| 时钟 | U14 时钟 | `osc32_in=NC`；`osc32_out=NC`；`crystal_shown=false`；`oscillator_shown=false` |
| 内存与 Flash | 外部存储器 | `flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `address.documented-0x55`：正文列出 I2C 地址 0x55，原理图没有地址选择硬件或地址标注，地址由 U14 固件决定。（证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 U14/J1 I2C 无地址标注）
- `other.documented-input-spec`：正文称测量 4-20mA 且 IN+/IN- 典型输入阻抗 200Ω；原理图显示 R5 24R 和闭环光耦/运放网络，但未直接标 200Ω 或转换精度、量程和标定公式。（证据：图 d18acd6ea198 / 第 1 页 / 第 1 页 MI+/MI- 模拟链路无 200Ω/精度标注）
- `review.i2c-address`：请通过 U162 固件或 I2C 扫描确认默认地址 0x55。；原因：原理图没有地址配置硬件。
- `review.input-spec`：请依据模拟设计计算、BOM 公差和标定报告确认 200Ω 输入阻抗、4-20mA 转换公式与精度。；原因：单页原理图未直接标出这些系统级参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d18acd6ea19824fe4946091ca9b1c9fdd510bd8d6f072449df151a003296172d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/617/SCH_UNIT_AIN4-20mA_V1.01_sch_01.png` |

---

源文档：`zh_CN/unit/AIN4-20mA Unit.md`

源文档 SHA-256：`39901b6c910788dd259ee9ef8b953530ff4877506e9b1dc779c1f5aa79971f7e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
