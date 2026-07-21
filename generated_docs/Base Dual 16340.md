# Base Dual 16340 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base Dual 16340 |
| SKU | A179 |
| 产品 ID | `base-dual-16340-262bfa1373e8` |
| 源文档 | `zh_CN/base/Base_Dual_16340.md` |

## 概述

Base Dual 16340 将 BAT1、BAT2 两节电池分别经 LP3218DT1G 与 2N7002W 前端支路汇合，并通过 DW01A、DMM3016LFDE-7 双 MOSFET、F1 自恢复保险丝和 20mΩ 分流电阻构成保护与监测路径。INA226AIDGSR 由 BUS_3V3 供电，以 I2C 地址 0x45 采集 SEN_P/SEN_N 分流压差和 BUS_BAT 总线电压。SW1 产生 OUT_EN，经 Q7 控制 Q5 高边输出开关，将 BAT_OUT 送至 M5Stack_BUS 的 BATTERY/BUS_BAT，并同时提供 Grove IO 与 Grove UART 接口。

## 检索关键词

`Base Dual 16340`、`A179`、`DW01A`、`INA226AIDGSR`、`0x45`、`LP3218DT1G`、`2N7002W`、`DMM3016LFDE-7`、`BSMD0805L-150`、`20mR`、`BAT_1`、`BAT_2`、`BAT_OUT`、`BUS_BAT`、`BUS_3V3`、`BUS_5V`、`SEN_P`、`SEN_N`、`OUT_EN`、`HP_PWR`、`I2C_SCL`、`I2C_SDA`、`G16_RXD`、`G17_TXD`、`G36`、`G26`、`M5Stack_BUS`、`Grove_IO`、`Grove_UART`、`SW1`、`16340`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| BAT1/BAT2 | 未标注 | 两节独立电池源，负端共接 BAT_GND，正端分别形成 BAT_2 与 BAT_1 | 图 20a51e19df4f / 第 1 页 / B1-C1：BAT1/BAT2 电池符号、BAT_1/BAT_2 与 BAT_GND |
| Q1/Q3 | LP3218DT1G | BAT_1 与 BAT_2 两路正端到公共电池正母线的串联 MOSFET | 图 20a51e19df4f / 第 1 页 / B1-C2：Q1/Q3 LP3218DT1G 位于 BAT_1/BAT_2 与公共节点之间 |
| Q2/Q4 | 2N7002W | 分别与 Q1/Q3 和 R3/R4 100KΩ 配合的电池输入控制/保护 MOSFET | 图 20a51e19df4f / 第 1 页 / B1-C2：Q2/Q4 2N7002W 与 R3/R4 100KΩ 支路 |
| U1 | DW01A | 电池保护控制器，通过 OD/OC 控制双 MOSFET | 图 20a51e19df4f / 第 1 页 / B2-C2：U1 DW01A、VDD/VSS/OD/OC/CSI |
| Q11/Q6 | DMM3016LFDE-7 | 由 DW01A 的 OD/OC 驱动的背靠背双 MOSFET 电池保护开关 | 图 20a51e19df4f / 第 1 页 / B2-C2：Q11/Q6，标注 DMM3016LFDE-7，栅极连接 U1 OD/OC |
| F1 | BSMD0805L-150 | 公共电池正母线到分流电阻前的串联自恢复保险丝 | 图 20a51e19df4f / 第 1 页 / A2-B2：F1 BSMD0805L-150 位于公共电池正母线与 R1 之间 |
| R1 | 20mR/1% | INA226 电流采样分流电阻 | 图 20a51e19df4f / 第 1 页 / A2-B3：R1 20mR/1%，两端经 R2/R5 接 SEN_P/SEN_N |
| U3 | INA226AIDGSR | I2C 电流、电压和功率监测器，采集 SEN_P/SEN_N 与 BUS_BAT | 图 20a51e19df4f / 第 1 页 / D1-D2：U3 INA226AIDGSR、VIN+/VIN-/VBUS、SCL/SDA、ADDR:0X45 |
| Q5 | LP3218DT1G | BAT_OUT 到 BUS_BAT 的高边输出开关 | 图 20a51e19df4f / 第 1 页 / B2-C3：Q5 LP3218DT1G 串联在 BAT_OUT 与 BUS_BAT 之间 |
| Q7 | 2N7002W | 由 OUT_EN 驱动并下拉 Q5 栅极的输出使能 MOSFET | 图 20a51e19df4f / 第 1 页 / C2-C3：Q7 2N7002W、OUT_EN、R9 与 Q5 栅极 |
| SW1 | KEY SW1 | 在 BAT_OUT、OUT_EN 与 GND 之间切换的电池输出控制开关 | 图 20a51e19df4f / 第 1 页 / C2-C3：SW1 三脚开关，1=BAT_OUT、2=OUT_EN、3=GND |
| LED1 | 绿色 | OUT_EN 状态指示 LED，串联 R11 10KΩ | 图 20a51e19df4f / 第 1 页 / C2：OUT_EN-R11 10KΩ-LED1 绿色-GND |
| J1 | M5Stack_BUS | 30 Pin M5Stack 主总线连接器，提供电池、电源、I2C、UART 和 GPIO | 图 20a51e19df4f / 第 1 页 / B3-D4：J1 M5Stack_BUS 1~30 脚网络标注 |
| J2 | Grove_IO | 四针 Grove 通用 GPIO 接口，连接 G36、G26、BUS_5V 和 GND | 图 20a51e19df4f / 第 1 页 / A3-B4：J2 Grove_IO 1~4 脚 |
| J3 | Grove_UART | 四针 Grove UART 接口，连接 G16_RXD、G17_TXD、BUS_5V 和 GND | 图 20a51e19df4f / 第 1 页 / B3：J3 Grove_UART 1~4 脚 |

## 系统结构

### Base Dual 16340 系统架构

两路电池输入经独立 MOSFET 前端汇合，随后通过 DW01A 保护、F1、20mΩ 分流电阻和 Q5 输出开关形成 BUS_BAT；INA226 监测该路径并由 M5Stack 总线 I2C 访问。

- 参数与网络：`battery_inputs=BAT_1,BAT_2`；`protection=U1 DW01A + Q11/Q6 DMM3016LFDE-7 + F1`；`monitor=U3 INA226AIDGSR`；`output=BAT_OUT-Q5-BUS_BAT`；`host=J1 M5Stack_BUS`
- 证据：图 20a51e19df4f / 第 1 页 / A1-D4：双电池、保护、监测、输出开关和 M5Stack_BUS 完整电路

## 电源

### BAT1/BAT2 输入

BAT1 与 BAT2 的负端均接 BAT_GND，正端分别形成 BAT_2 与 BAT_1；BAT_1 经 Q1、BAT_2 经 Q3 汇合到公共正母线。

- 参数与网络：`battery_1_positive=BAT_2`；`battery_2_positive=BAT_1`；`common_negative=BAT_GND`；`upper_path=BAT_1-Q1 LP3218DT1G-common rail`；`lower_path=BAT_2-Q3 LP3218DT1G-common rail`
- 证据：图 20a51e19df4f / 第 1 页 / B1-C2：BAT1/BAT2 符号、BAT_1/BAT_2、BAT_GND、Q1/Q3

### BAT_OUT 到 BUS_BAT 输出开关

Q5 LP3218DT1G 串联在 BAT_OUT 与 BUS_BAT 之间；R8 100KΩ连接 BAT_OUT 与 Q5 栅极，Q7 2N7002W 在 OUT_EN 控制下将 Q5 栅极拉向 GND。

- 参数与网络：`high_side=Q5 LP3218DT1G`；`input=BAT_OUT`；`output=BUS_BAT`；`gate_pullup=R8 100KΩ to BAT_OUT`；`gate_pull_down=Q7 2N7002W to GND`；`control=OUT_EN`
- 证据：图 20a51e19df4f / 第 1 页 / B2-C3：BAT_OUT-Q5-BUS_BAT、R8、Q7、OUT_EN

### LED1

OUT_EN 经 R11 10KΩ和 LED1（绿色）串联到 GND，构成输出使能指示支路。

- 参数与网络：`source=OUT_EN`；`resistor=R11 10KΩ`；`indicator=LED1 green`；`return=GND`
- 证据：图 20a51e19df4f / 第 1 页 / C2：OUT_EN-R11-LED1-GND

### 电池充电路径

原理图绘制电池保护、监测和输出控制，但未绘制专用锂电池充电控制器或从 BUS_5V 到 BAT_1/BAT_2 的充电路径。

- 参数与网络：`charger_ic=none shown`；`bus_5v_to_battery_charge_path=none shown`；`present_functions=protection,monitoring,output switching`
- 证据：图 20a51e19df4f / 第 1 页 / 全页电源路径检查：BUS_5V 仅到 J2/J3/J1，未连接 BAT_1/BAT_2；无充电 IC

## 接口

### J1 M5Stack_BUS

J1 为 30 Pin M5Stack 总线，连接 GND、HP_PWR、BUS_3V3、BUS_5V、BUS_BAT、UART、I2C 与 G36/G26。

- 参数与网络：`pins_1_10=1:GND,2:GPIO35,3:GND,4:GPIO36/G36,5:GND,6:EN,7:GPIO23,8:GPIO25,9:GPIO19,10:GPIO26/G26`；`pins_11_20=11:GPIO18,12:+3.3V/BUS_3V3,13:GPIO3,14:GPIO1,15:GPIO16/G16_RXD,16:GPIO17/G17_TXD,17:GPIO21/I2C_SDA,18:GPIO22/I2C_SCL,19:GPIO2,20:GPIO5`；`pins_21_30=21:GPIO12,22:GPIO13,23:GPIO15,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,28:+5V/BUS_5V,29:HPWR,30:BATTERY/BUS_BAT`
- 证据：图 20a51e19df4f / 第 1 页 / B3-D4：J1 1~30 脚逐脚网络标注

### J2 Grove_IO

J2.1=G36/D1，J2.2=G26/D2，J2.3=BUS_5V/5V，J2.4=GND。

- 参数与网络：`pin_1=G36 / D1 / J1.4 GPIO36`；`pin_2=G26 / D2 / J1.10 GPIO26`；`pin_3=BUS_5V / 5V`；`pin_4=GND`
- 证据：图 20a51e19df4f / 第 1 页 / A3-B4：J2 Grove_IO 1~4 脚

### J3 Grove_UART

J3.1=G16_RXD/S_RX，J3.2=G17_TXD/S_TX，J3.3=BUS_5V/5V，J3.4=GND。

- 参数与网络：`pin_1=G16_RXD / S_RX / J1.15 GPIO16`；`pin_2=G17_TXD / S_TX / J1.16 GPIO17`；`pin_3=BUS_5V / 5V`；`pin_4=GND`
- 证据：图 20a51e19df4f / 第 1 页 / B3-B4：J3 Grove_UART 1~4 脚

## 总线

### INA226 I2C

U3.5 SCL 接 I2C_SCL，U3.4 SDA 接 I2C_SDA；R6、R7 均为 2.2KΩ并上拉到 BUS_3V3。

- 参数与网络：`scl=U3.5 I2C_SCL / J1.18 GPIO22`；`sda=U3.4 I2C_SDA / J1.17 GPIO21`；`scl_pullup=R6 2.2KΩ to BUS_3V3`；`sda_pullup=R7 2.2KΩ to BUS_3V3`
- 证据：图 20a51e19df4f / 第 1 页 / D1-D2：U3 SCL/SDA、R6/R7、BUS_3V3；C3-D4：J1 I2C_SDA/I2C_SCL

### Grove UART

J1.15 GPIO16 通过 G16_RXD 到 J3 S_RX，J1.16 GPIO17 通过 G17_TXD 到 J3 S_TX；原理图未绘制额外 UART 收发器或电平转换器。

- 参数与网络：`rx=J1.15 GPIO16-G16_RXD-J3.1 S_RX`；`tx=J1.16 GPIO17-G17_TXD-J3.2 S_TX`；`transceiver=none shown`
- 证据：图 20a51e19df4f / 第 1 页 / B3-D4：J3 与 J1.15/J1.16 同名网络

## 总线地址

### U3 INA226AIDGSR

原理图在 U3 下方明确标注 ADDR:0X45，A0 与 A1 地址脚均连接 BUS_3V3。

- 参数与网络：`address=0x45`；`a0=U3.2 BUS_3V3`；`a1=U3.1 BUS_3V3`
- 证据：图 20a51e19df4f / 第 1 页 / D1-D2：U3 A0/A1 到 BUS_3V3，器件下方 ADDR:0X45

## GPIO 与控制信号

### OUT_EN / SW1

SW1.1 接 BAT_OUT、SW1.2 接 OUT_EN、SW1.3 接 GND；OUT_EN 由 R9 10KΩ下拉，并驱动 Q7 栅极。

- 参数与网络：`switch_pin_1=BAT_OUT`；`switch_pin_2=OUT_EN`；`switch_pin_3=GND`；`pulldown=R9 10KΩ`；`mosfet=Q7 gate`
- 证据：图 20a51e19df4f / 第 1 页 / C2-C3：SW1 1/2/3 脚、OUT_EN、R9、Q7

### G36/G26

J1.4 GPIO36 通过 G36 连接 J2.1，J1.10 GPIO26 通过 G26 连接 J2.2。

- 参数与网络：`g36=J1.4 GPIO36-J2.1 D1`；`g26=J1.10 GPIO26-J2.2 D2`
- 证据：图 20a51e19df4f / 第 1 页 / A3-D4：J2 G36/G26 与 J1.4/J1.10

## 时钟

### 时钟

原理图未绘制晶振或有源时钟；唯一时钟命名信号为 I2C_SCL。

- 参数与网络：`crystal=none shown`；`active_clock=none shown`；`serial_clock=I2C_SCL`
- 证据：图 20a51e19df4f / 第 1 页 / 全页器件检查，无晶振/时钟芯片；U3/J1 仅见 I2C_SCL

## 复位

### 复位网络

J1.6 引出主机 EN，但板上 U1 DW01A 和 U3 INA226 未绘制独立复位引脚或复位按钮。

- 参数与网络：`host_enable=J1.6 EN`；`local_reset_button=none shown`；`ina226_reset=none shown`；`dw01a_reset=none shown`
- 证据：图 20a51e19df4f / 第 1 页 / B2-D4：J1.6 EN；U1/U3 与 SW1，无独立 RESET 按钮

## 保护电路

### 双电池输入 MOSFET 网络

BAT_1 支路使用 Q1 LP3218DT1G、Q2 2N7002W 和 R3 100KΩ；BAT_2 支路使用 Q3 LP3218DT1G、Q4 2N7002W 和 R4 100KΩ，两路结构对称。

- 参数与网络：`bat_1=Q1 LP3218DT1G + Q2 2N7002W + R3 100KΩ`；`bat_2=Q3 LP3218DT1G + Q4 2N7002W + R4 100KΩ`
- 证据：图 20a51e19df4f / 第 1 页 / B1-C2：Q1/Q2/R3 与 Q3/Q4/R4 对称支路

### U1 DW01A 保护控制

U1 VDD 接公共电池正母线、VSS 接 BAT_GND，OD 与 OC 分别控制 Q11/Q6；CSI 经 R10 1KΩ 接 GND，NC 脚未连接。

- 参数与网络：`vdd=U1.5 common battery positive`；`vss=U1.6 BAT_GND`；`od=U1.1 to Q11 gate`；`oc=U1.3 to Q6 gate`；`csi=U1.2 through R10 1KΩ to GND`；`nc=U1.4 no-connect`
- 证据：图 20a51e19df4f / 第 1 页 / B2-C2：U1 DW01A 六脚与 Q11/Q6、R10

### F1

F1 BSMD0805L-150 串联在公共电池正母线与 R1 分流电阻之前。

- 参数与网络：`device=BSMD0805L-150`；`position=common battery positive before R1`；`series_path=battery rail-F1-R1-BAT_OUT`
- 证据：图 20a51e19df4f / 第 1 页 / A2-B3：公共正母线-F1-R1-BAT_OUT

## 关键网络

### M5Stack 电源网络

J1.12 的 +3.3V 形成 BUS_3V3，J1.28 的 +5V 形成 BUS_5V，J1.30 的 BATTERY 连接 BUS_BAT，J1.25/27/29 连接 HP_PWR。

- 参数与网络：`bus_3v3=J1.12`；`bus_5v=J1.28`；`bus_bat=J1.30`；`hp_pwr=J1.25,J1.27,J1.29`
- 证据：图 20a51e19df4f / 第 1 页 / C3-D4：J1.12/25/27/28/29/30 与 BUS_3V3/HP_PWR/BUS_5V/BUS_BAT

## 存储

### 存储器

原理图未绘制 Flash、EEPROM、SD 卡或其他存储器。

- 参数与网络：`flash=none shown`；`eeprom=none shown`；`sd=none shown`
- 证据：图 20a51e19df4f / 第 1 页 / 全页主要器件为 U1 DW01A、U3 INA226 与 MOSFET/接口，无存储器

## 内存与 Flash

### 易失性存储

原理图未绘制独立 RAM 或其他易失性存储器件。

- 参数与网络：`ram=none shown`
- 证据：图 20a51e19df4f / 第 1 页 / 全页器件检查，无 RAM 器件

## 音频

### 音频电路

原理图未绘制音频编解码器、麦克风、扬声器或音频接口。

- 参数与网络：`codec=none shown`；`microphone=none shown`；`speaker=none shown`
- 证据：图 20a51e19df4f / 第 1 页 / 全页器件与接口检查，无音频功能块

## 传感器

### U3 INA226AIDGSR

U3 VIN+ 接 SEN_P、VIN- 接 SEN_N，VBUS 接 BUS_BAT，VS+ 由 BUS_3V3 供电；因此图面提供分流压差与输出总线电压采样路径。

- 参数与网络：`vin_plus=U3.10 SEN_P`；`vin_minus=U3.9 SEN_N`；`vbus=U3.8 BUS_BAT`；`supply=U3.6 BUS_3V3`；`ground=U3.7 GND`；`decoupling=C1 1uF/25V`
- 证据：图 20a51e19df4f / 第 1 页 / D1-D2：U3 VIN-/VIN+/VBUS/VS+/GND 与 C1

## 射频

### 射频电路

原理图未绘制天线、射频收发器或射频匹配网络。

- 参数与网络：`antenna=none shown`；`rf_transceiver=none shown`；`matching_network=none shown`
- 证据：图 20a51e19df4f / 第 1 页 / 全页器件检查，无射频功能块

## 调试与烧录

### 调试接口

原理图未绘制 JTAG、SWD 或专用调试连接器，调试可见信号仅通过 J1/J2/J3 引出。

- 参数与网络：`jtag=none shown`；`swd=none shown`；`breakouts=J1 M5Stack_BUS,J2 Grove_IO,J3 Grove_UART`
- 证据：图 20a51e19df4f / 第 1 页 / 全页接口检查：仅 J1/J2/J3，无专用调试座

## 模拟电路

### R1 电流分流器

R1 为 20mΩ/1% 分流电阻；F1 侧经 R2 0Ω形成 SEN_P，BAT_OUT 侧经 R5 0Ω形成 SEN_N。

- 参数与网络：`shunt=R1 20mR/1%`；`positive_sense=R2 0R to SEN_P`；`negative_sense=R5 0R to SEN_N`；`output_side=BAT_OUT`
- 证据：图 20a51e19df4f / 第 1 页 / A2-B3：R1、R2/SEN_P、R5/SEN_N、BAT_OUT

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base Dual 16340 系统架构 | `battery_inputs=BAT_1,BAT_2`；`protection=U1 DW01A + Q11/Q6 DMM3016LFDE-7 + F1`；`monitor=U3 INA226AIDGSR`；`output=BAT_OUT-Q5-BUS_BAT`；`host=J1 M5Stack_BUS` |
| 电源 | BAT1/BAT2 输入 | `battery_1_positive=BAT_2`；`battery_2_positive=BAT_1`；`common_negative=BAT_GND`；`upper_path=BAT_1-Q1 LP3218DT1G-common rail`；`lower_path=BAT_2-Q3 LP3218DT1G-common rail` |
| 保护电路 | 双电池输入 MOSFET 网络 | `bat_1=Q1 LP3218DT1G + Q2 2N7002W + R3 100KΩ`；`bat_2=Q3 LP3218DT1G + Q4 2N7002W + R4 100KΩ` |
| 保护电路 | U1 DW01A 保护控制 | `vdd=U1.5 common battery positive`；`vss=U1.6 BAT_GND`；`od=U1.1 to Q11 gate`；`oc=U1.3 to Q6 gate`；`csi=U1.2 through R10 1KΩ to GND`；`nc=U1.4 no-connect` |
| 保护电路 | F1 | `device=BSMD0805L-150`；`position=common battery positive before R1`；`series_path=battery rail-F1-R1-BAT_OUT` |
| 模拟电路 | R1 电流分流器 | `shunt=R1 20mR/1%`；`positive_sense=R2 0R to SEN_P`；`negative_sense=R5 0R to SEN_N`；`output_side=BAT_OUT` |
| 传感器 | U3 INA226AIDGSR | `vin_plus=U3.10 SEN_P`；`vin_minus=U3.9 SEN_N`；`vbus=U3.8 BUS_BAT`；`supply=U3.6 BUS_3V3`；`ground=U3.7 GND`；`decoupling=C1 1uF/25V` |
| 总线 | INA226 I2C | `scl=U3.5 I2C_SCL / J1.18 GPIO22`；`sda=U3.4 I2C_SDA / J1.17 GPIO21`；`scl_pullup=R6 2.2KΩ to BUS_3V3`；`sda_pullup=R7 2.2KΩ to BUS_3V3` |
| 总线地址 | U3 INA226AIDGSR | `address=0x45`；`a0=U3.2 BUS_3V3`；`a1=U3.1 BUS_3V3` |
| 电源 | BAT_OUT 到 BUS_BAT 输出开关 | `high_side=Q5 LP3218DT1G`；`input=BAT_OUT`；`output=BUS_BAT`；`gate_pullup=R8 100KΩ to BAT_OUT`；`gate_pull_down=Q7 2N7002W to GND`；`control=OUT_EN` |
| GPIO 与控制信号 | OUT_EN / SW1 | `switch_pin_1=BAT_OUT`；`switch_pin_2=OUT_EN`；`switch_pin_3=GND`；`pulldown=R9 10KΩ`；`mosfet=Q7 gate` |
| 电源 | LED1 | `source=OUT_EN`；`resistor=R11 10KΩ`；`indicator=LED1 green`；`return=GND` |
| 接口 | J1 M5Stack_BUS | `pins_1_10=1:GND,2:GPIO35,3:GND,4:GPIO36/G36,5:GND,6:EN,7:GPIO23,8:GPIO25,9:GPIO19,10:GPIO26/G26`；`pins_11_20=11:GPIO18,12:+3.3V/BUS_3V3,13:GPIO3,14:GPIO1,15:GPIO16/G16_RXD,16:GPIO17/G17_TXD,17:GPIO21/I2C_SDA,18:GPIO22/I2C_SCL,19:GPIO2,20:GPIO5`；`pins_21_30=21:GPIO12,22:GPIO13,23:GPIO15,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,28:+5V/BUS_5V,29:HPWR,30:BATTERY/BUS_BAT` |
| 关键网络 | M5Stack 电源网络 | `bus_3v3=J1.12`；`bus_5v=J1.28`；`bus_bat=J1.30`；`hp_pwr=J1.25,J1.27,J1.29` |
| 接口 | J2 Grove_IO | `pin_1=G36 / D1 / J1.4 GPIO36`；`pin_2=G26 / D2 / J1.10 GPIO26`；`pin_3=BUS_5V / 5V`；`pin_4=GND` |
| 接口 | J3 Grove_UART | `pin_1=G16_RXD / S_RX / J1.15 GPIO16`；`pin_2=G17_TXD / S_TX / J1.16 GPIO17`；`pin_3=BUS_5V / 5V`；`pin_4=GND` |
| 总线 | Grove UART | `rx=J1.15 GPIO16-G16_RXD-J3.1 S_RX`；`tx=J1.16 GPIO17-G17_TXD-J3.2 S_TX`；`transceiver=none shown` |
| GPIO 与控制信号 | G36/G26 | `g36=J1.4 GPIO36-J2.1 D1`；`g26=J1.10 GPIO26-J2.2 D2` |
| 复位 | 复位网络 | `host_enable=J1.6 EN`；`local_reset_button=none shown`；`ina226_reset=none shown`；`dw01a_reset=none shown` |
| 时钟 | 时钟 | `crystal=none shown`；`active_clock=none shown`；`serial_clock=I2C_SCL` |
| 存储 | 存储器 | `flash=none shown`；`eeprom=none shown`；`sd=none shown` |
| 内存与 Flash | 易失性存储 | `ram=none shown` |
| 调试与烧录 | 调试接口 | `jtag=none shown`；`swd=none shown`；`breakouts=J1 M5Stack_BUS,J2 Grove_IO,J3 Grove_UART` |
| 音频 | 音频电路 | `codec=none shown`；`microphone=none shown`；`speaker=none shown` |
| 射频 | 射频电路 | `antenna=none shown`；`rf_transceiver=none shown`；`matching_network=none shown` |
| 电源 | 电池充电路径 | `charger_ic=none shown`；`bus_5v_to_battery_charge_path=none shown`；`present_functions=protection,monitoring,output switching` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `20a51e19df4f774087d4c07fbc35e872326804e77a09caf7dc3b3ca22edf4924` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1251/SCH_Base_Dual_16340_v0.2_2025_11_17_11_56_09_page_01.png` |

---

源文档：`zh_CN/base/Base_Dual_16340.md`

源文档 SHA-256：`f62afb694e24507baaccc2ad865287ab32b71251eb39b5cac1f83bf63b3341d7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
