# Hat PowerC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat PowerC |
| SKU | U081 |
| 产品 ID | `hat-powerc-5d32112284e6` |
| 源文档 | `zh_CN/hat/hat-powerc.md` |

## 概述

Hat PowerC 以 IP5209（U2）实现 VIN 输入、电池连接、VOUT/5VOUT 输出、USB 数据识别和 I2C/INT 管理，并以 IP3005（U1）连接 BAT-/P- 负端保护路径。USB-C J1 的 VBUS 经 F1 进入 VIN，电池正端 P+ 经 0.01R 电流采样与 L1 1uH 连接 U2，VOUT 同时供 USB-A J2、I2C 扩展口 J3 和 STICKIO P3。P1 引出 P+/BAT-，BT1 与 U1 组成电池保护区域；S1 接 U2 KEY，SCL/SDA/INT 通过 Rp1 上拉到 VREG。

## 检索关键词

`Hat PowerC`、`U081`、`IP5209`、`IP3005`、`USB-C`、`USB_TYPE_A`、`STICKIO`、`HY-2.0_IIC`、`VIN`、`VOUT`、`5VOUT`、`VBAT`、`BAT+`、`BAT-`、`P+`、`P-`、`VREG`、`CSIN`、`CSIN_S`、`LX`、`I2C`、`SCL`、`SDA`、`INT`、`0x75`、`G26`、`G36`、`G0`、`L1 0420 1uH`、`R5 0.01R`、`F1 Fuse`、`S1 KEY`、`USB_N`、`USB_P`、`16340`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | IP5209 | 电源管理 IC，连接 VIN、电池、升压电感、VOUT、USB D+/D-、I2C、INT、KEY 和配置网络 | 图 6b43fc29c96e / 第 1 页 / 页面中央 U2 IP5209：1~25 脚及 VIN/VBAT/CSIN/LX/VREG/KEY/VOUT/DM/DP/INT/SDA/SCL 等网络 |
| U1 | IP3005 | 电池负端保护 IC，VDD 由 BAT+ 经 R1 供电，GND/EPAD 接 BAT-，VM 接 P- | 图 6b43fc29c96e / 第 1 页 / 页面右上 U1 IP3005：VDD、GND、EPAD、VM、NC 引脚与 BAT+/BAT-/P- 网络 |
| J1 | USB-C | USB-C 电源输入接口，VBUS 经 F1 连接 VIN，外壳与 GND 脚接地 | 图 6b43fc29c96e / 第 1 页 / 页面左上 J1 USB-C：VBUS、CC1、CC2、GND 与 7~10 外壳脚，VBUS 侧连接 F1/VIN |
| J2 | USB_TYPE_A | USB-A 输出接口，引出 VOUT、USB_N、USB_P 和 GND | 图 6b43fc29c96e / 第 1 页 / 页面中右 J2 USB_TYPE_A：1 VBUS/VOUT、2 D-/USB_N、3 D+/USB_P、4 GND |
| J3 | HY-2.0_IIC | 四针 I2C 扩展接口，引出 SCL、SDA、5VOUT 和 GND | 图 6b43fc29c96e / 第 1 页 / 页面右中 J3 HY-2.0_IIC：1~4 脚 IIC_SCL/IIC_SDA/VCC/GND 与 SCL/SDA/5VOUT/GND |
| P3 | STICKIO | 8 针主机接口，引出 GND、5VOUT、SCL/G26、INT/G36、SDA/G0 和 BAT+ | 图 6b43fc29c96e / 第 1 页 / 页面下中 P3 STICKIO：1~8 脚 GND/5VOUT/G26/G36/G0/BAT/3V3/5VIN 与左侧网络 |
| P1 | Header 2 | 两针电池连接口，引出 P+ 与 BAT- | 图 6b43fc29c96e / 第 1 页 / 页面上中 P1 Header 2：1 脚 P+，2 脚 BAT- |
| BT1 | Battery | 电池元件，正端接 BAT+/P+，负端接 BAT- | 图 6b43fc29c96e / 第 1 页 / 页面右上 BT1 Battery：上端 BAT+/P+，下端 BAT- |
| F1 | Fuse | USB-C VBUS 到 VIN 之间的输入保险丝 | 图 6b43fc29c96e / 第 1 页 / 页面左上 J1 VBUS 右侧：F1 Fuse 串联至 VIN |
| L1 | 0420 1uH | P+ 电流采样节点与 U2 LX 开关脚之间的储能电感 | 图 6b43fc29c96e / 第 1 页 / 页面中左 U2 左侧：L1 0420 1uH 从 CSIN/CSIN_S 节点连接 U2.13/14/15 LX |
| R5 | 0.01R | P+ 与 CSIN/CSIN_S 节点之间的电流采样电阻 | 图 6b43fc29c96e / 第 1 页 / 页面中左 P+ 右侧：R5 0.01R 串联到 U2.10 CSIN/U2.11 CSIN_S 与 L1 左端节点 |
| S1 | SW-PB | 将 U2.8 KEY 瞬时接地的按键 | 图 6b43fc29c96e / 第 1 页 / 页面中下 S1 SW-PB：一端接 U2.8 KEY，另一端接 GND |
| Rp1 | 1KΩ (102) ±5% | 由 VREG 向 SCL、INT、SDA 等控制信号提供上拉的电阻阵列 | 图 6b43fc29c96e / 第 1 页 / 页面下中 Rp1：顶部接 VREG，标注 1KΩ (102) ±5%，底部连接 SCL/INT/SDA 走线 |
| R1/C1/C2 | 100Ω / 4.7uF / 2.2uF | IP3005 的 VDD 限流/滤波及 BAT-/P- 侧电容网络 | 图 6b43fc29c96e / 第 1 页 / 页面右上 U1 左侧：R1 100Ω 从 BAT+ 至 VDD，C1 4.7uF 至 BAT-，C2 2.2uF 跨 BAT-/P- |
| C3/C4/C5 | 2.2nF / 22uF / 22uF | VOUT 开关节点吸收与输出储能电容网络 | 图 6b43fc29c96e / 第 1 页 / 页面中上 VOUT 区域：C3 2.2nF 从 VOUT 至 LX，C4/C5 22uF 从 VOUT 至 GND |

## 系统结构

### Hat PowerC

J1 USB-C 经 F1 向 U2 IP5209 提供 VIN；U2 连接 P+ 电池路径、L1/LX、VOUT、USB-A、I2C/INT 与 KEY；U1 IP3005 位于 BAT-/P- 电池负端保护区域。

- 参数与网络：`power_manager=U2 IP5209`；`battery_protector=U1 IP3005`；`input=J1 USB-C via F1 to VIN`；`battery_path=P+, BAT-, P-`；`output=VOUT/5VOUT`；`interfaces=J2 USB-A; J3 I2C; P3 STICKIO`
- 证据：图 6b43fc29c96e / 第 1 页 / 全页 J1/F1、U2、U1/BT1、J2/J3/P3 之间的同名电源和信号网络

## 核心器件

### U2 IP5209

U2 的 VIN 为 20/21，NTC 为 6，VBAT 为 9，CSIN/CSIN_S 为 10/11，LX 为 13/14/15，VREG 为 3，VSET 为 23，KEY 为 8；VOUT 为 16/17，DM/DP 为 18/19，INT/SDA/SCL 为 2/1/24。

- 参数与网络：`VIN=pins 20,21`；`NTC=pin 6`；`VBAT=pin 9`；`CSIN=pin 10`；`CSIN_S=pin 11`；`LX=pins 13,14,15`；`VREG=pin 3`；`VSET=pin 23 NC`；`KEY=pin 8`；`VOUT=pins 16,17`；`DM=pin 18 USB_N`；`DP=pin 19 USB_P`；`INT=pin 2`；`SDA=pin 1`；`SCL=pin 24`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面中央 U2 IP5209 符号左右两侧的引脚编号、名称与网络标签

## 电源

### VIN 输入路径

J1 VBUS 经 F1 形成 VIN，VIN 连接 U2.20/U2.21；C6 10uF 对地，另一路经 R3 0Ω 与 C7 10uF 接地。

- 参数与网络：`source=J1 VBUS`；`fuse=F1`；`rail=VIN`；`manager_pins=U2.20, U2.21`；`capacitors=C6 10uF; R3 0Ω plus C7 10uF`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面左上至中央：J1/F1/VIN、U2.20/21 与 C6/R3/C7 输入网络

### P+ 电池与升压路径

P+ 连接 U2.9 VBAT，并经 R5 0.01R 到 U2.10 CSIN/U2.11 CSIN_S 与 L1 左端；L1 0420 1uH 的另一端连接 U2.13/U2.14/U2.15 LX。

- 参数与网络：`battery_positive=P+ to U2.9 VBAT`；`sense_resistor=R5 0.01R`；`sense_pins=U2.10 CSIN; U2.11 CSIN_S`；`inductor=L1 0420 1uH`；`switch_pins=U2.13,14,15 LX`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面中左 P+、R5、CSIN/CSIN_S、L1 与三路 LX 引脚的连接

### VOUT/5VOUT

U2.16/U2.17 产生 VOUT，VOUT 连接 J2.1 USB-A VBUS，并以 5VOUT 同名网络连接 J3.3 和 P3.2；C4/C5 各 22uF 跨接 VOUT 与 GND。

- 参数与网络：`source=U2.16,17 VOUT`；`usb_a=J2.1 VBUS`；`i2c_port=J3.3 5VOUT`；`stickio=P3.2 5VOUT`；`output_caps=C4 22uF; C5 22uF`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面 U2.16/17 VOUT、J2.1、J3.3、P3.2 与 C4/C5 的 VOUT/5VOUT 网络

### IP3005 电池保护路径

BT1 正端为 BAT+/P+；BAT+ 经 R1 100Ω 向 U1.6 VDD 供电，U1.5/U1.7/U1.8 GND 与 U1.9 EPAD 接 BAT-，U1.2/U1.3/U1.4 VM 接 P-，U1.1 NC。

- 参数与网络：`battery_positive=BAT+/P+`；`vdd=U1.6 via R1 100Ω`；`raw_negative=BAT- to U1.5,7,8 GND and U1.9 EPAD`；`protected_negative=P- to U1.2,3,4 VM`；`nc=U1.1`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面右上 BT1/R1/U1 IP3005/C1/C2 的 BAT+/BAT-/P- 连接

## 接口

### J1 USB-C

J1 的 VBUS 端通过 F1 Fuse 串联到 VIN，J1 的 GND 与外壳接地；该页未显示 USB-C 数据线连接。

- 参数与网络：`power_path=J1 VBUS via F1 to VIN`；`ground=J1 GND and shell pins 7-10`；`usb_data=not shown`；`input_protection=F1 Fuse`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面左上 J1 USB-C 与 F1/VIN 连接，GND 和 7~10 外壳脚接地

### J2 USB_TYPE_A

J2.1 VBUS 接 VOUT，J2.2 D- 接 USB_N/U2.18 DM，J2.3 D+ 接 USB_P/U2.19 DP，J2.4 接 GND。

- 参数与网络：`pin_1=VBUS VOUT`；`pin_2=D- USB_N U2.18 DM`；`pin_3=D+ USB_P U2.19 DP`；`pin_4=GND`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面中右 J2 1~4 脚与 U2.16/17 VOUT、U2.18 DM、U2.19 DP 的网络

### J3 HY-2.0_IIC

J3.1 为 SCL/IIC_SCL，J3.2 为 SDA/IIC_SDA，J3.3 为 5VOUT/VCC，J3.4 为 GND。

- 参数与网络：`pin_1=SCL IIC_SCL`；`pin_2=SDA IIC_SDA`；`pin_3=5VOUT VCC`；`pin_4=GND`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面右中 J3：1~4 脚、IIC_SCL/IIC_SDA/VCC/GND 与左侧网络

### P3 STICKIO

P3.1~P3.8 依次为 GND、5VOUT、G26/SCL、G36/INT、G0/SDA、BAT/BAT+、3V3/未连接、5VIN/未连接。

- 参数与网络：`pin_1=GND`；`pin_2=5VOUT`；`pin_3=G26 SCL`；`pin_4=G36 INT`；`pin_5=G0 SDA`；`pin_6=BAT BAT+`；`pin_7=3V3 NC`；`pin_8=5VIN NC`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面下中 P3 STICKIO：1~8 脚、符号内名称、左侧网络及 7/8 脚短线未连接

### P1 Header 2

P1.1 接 P+，P1.2 接 BAT-，用于引出电池正端与保护前负端。

- 参数与网络：`pin_1=P+`；`pin_2=BAT-`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面上中 P1 Header 2 左侧 P+/BAT- 标签与 1/2 脚

## 总线

### U2 I2C 与中断

U2.24 L1/SCL 连接 SCL，U2.1 L2/SDA 连接 SDA，U2.2 L3 连接 INT；SCL/SDA/INT 连接 P3 的 G26/G0/G36，其中 SCL/SDA 也连接 J3。

- 参数与网络：`scl=U2.24 to P3.3 G26 and J3.1`；`sda=U2.1 to P3.5 G0 and J3.2`；`interrupt=U2.2 to P3.4 G36`；`pullups=Rp1 1KΩ to VREG`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面 U2 右侧 SCL/SDA/INT 网络、下方 Rp1/P3 与右侧 J3 的同名连接

## GPIO 与控制信号

### S1 KEY

S1 SW-PB 按下时将 U2.8 KEY 接至 GND。

- 参数与网络：`switch=S1 SW-PB`；`controller_pin=U2.8 KEY`；`active_connection=GND`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面中下 S1：右端连接 U2.8 KEY，左端接 GND

### U2 LIGHT/RSET

U2.22 LIGHT 通过 R6 0Ω 接 GND，U2.5 RSET 通过 R7 100KΩ 接 GND；U2.23 VSET 标为未连接。

- 参数与网络：`LIGHT=U2.22 via R6 0Ω to GND`；`RSET=U2.5 via R7 100KΩ to GND`；`VSET=U2.23 NC`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面 U2 右下 LIGHT/RSET 支路与左下 VSET 未连接标记

## 时钟

### 时钟、复位与调试

该页未显示外部晶振、时钟源、复位网络、BOOT 或调试接口。

- 参数与网络：`external_clock=not shown`；`reset=not shown`；`boot=not shown`；`debug=not shown`
- 证据：图 6b43fc29c96e / 第 1 页 / 全页 U1/U2 与所有接口及外围器件，无晶振、复位、BOOT 或调试符号

## 保护电路

### USB-C 输入保护

F1 Fuse 串联在 J1 VBUS 与 VIN 之间。

- 参数与网络：`protector=F1 Fuse`；`input=J1 VBUS`；`output=VIN`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面左上 J1 VBUS 至 VIN 的水平线上 F1 Fuse

## 模拟电路

### U2 NTC 配置

U2.6 NTC 连接 R2 2MΩ 与 R4 1MΩ 的分压节点，R4 下端接 GND。

- 参数与网络：`ntc_pin=U2.6 NTC`；`upper_resistor=R2 2MΩ`；`lower_resistor=R4 1MΩ to GND`
- 证据：图 6b43fc29c96e / 第 1 页 / 页面中左 U2.6 NTC 左侧：R2 2MΩ/R4 1MΩ 中点连接 NTC，R4 接 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat PowerC | `power_manager=U2 IP5209`；`battery_protector=U1 IP3005`；`input=J1 USB-C via F1 to VIN`；`battery_path=P+, BAT-, P-`；`output=VOUT/5VOUT`；`interfaces=J2 USB-A; J3 I2C; P3 STICKIO` |
| 核心器件 | U2 IP5209 | `VIN=pins 20,21`；`NTC=pin 6`；`VBAT=pin 9`；`CSIN=pin 10`；`CSIN_S=pin 11`；`LX=pins 13,14,15`；`VREG=pin 3`；`VSET=pin 23 NC`；`KEY=pin 8`；`VOUT=pins 16,17`；`DM=pin 18 USB_N`；`DP=pin 19 USB_P`；`INT=pin 2`；`SDA=pin 1`；`SCL=pin 24` |
| 接口 | J1 USB-C | `power_path=J1 VBUS via F1 to VIN`；`ground=J1 GND and shell pins 7-10`；`usb_data=not shown`；`input_protection=F1 Fuse` |
| 接口 | J2 USB_TYPE_A | `pin_1=VBUS VOUT`；`pin_2=D- USB_N U2.18 DM`；`pin_3=D+ USB_P U2.19 DP`；`pin_4=GND` |
| 接口 | J3 HY-2.0_IIC | `pin_1=SCL IIC_SCL`；`pin_2=SDA IIC_SDA`；`pin_3=5VOUT VCC`；`pin_4=GND` |
| 接口 | P3 STICKIO | `pin_1=GND`；`pin_2=5VOUT`；`pin_3=G26 SCL`；`pin_4=G36 INT`；`pin_5=G0 SDA`；`pin_6=BAT BAT+`；`pin_7=3V3 NC`；`pin_8=5VIN NC` |
| 总线 | U2 I2C 与中断 | `scl=U2.24 to P3.3 G26 and J3.1`；`sda=U2.1 to P3.5 G0 and J3.2`；`interrupt=U2.2 to P3.4 G36`；`pullups=Rp1 1KΩ to VREG` |
| 总线地址 | IP5209 I2C 地址 | `documented_address=0x75`；`schematic_address_label=not shown`；`address_straps=not shown` |
| 电源 | VIN 输入路径 | `source=J1 VBUS`；`fuse=F1`；`rail=VIN`；`manager_pins=U2.20, U2.21`；`capacitors=C6 10uF; R3 0Ω plus C7 10uF` |
| 电源 | P+ 电池与升压路径 | `battery_positive=P+ to U2.9 VBAT`；`sense_resistor=R5 0.01R`；`sense_pins=U2.10 CSIN; U2.11 CSIN_S`；`inductor=L1 0420 1uH`；`switch_pins=U2.13,14,15 LX` |
| 电源 | VOUT/5VOUT | `source=U2.16,17 VOUT`；`usb_a=J2.1 VBUS`；`i2c_port=J3.3 5VOUT`；`stickio=P3.2 5VOUT`；`output_caps=C4 22uF; C5 22uF` |
| 电源 | 5VOUT 输出额定值 | `schematic_voltage_label=5VOUT`；`documented_current=1.5A`；`schematic_current_rating=not shown` |
| 电源 | IP3005 电池保护路径 | `battery_positive=BAT+/P+`；`vdd=U1.6 via R1 100Ω`；`raw_negative=BAT- to U1.5,7,8 GND and U1.9 EPAD`；`protected_negative=P- to U1.2,3,4 VM`；`nc=U1.1` |
| 接口 | P1 Header 2 | `pin_1=P+`；`pin_2=BAT-` |
| 电源 | 电池数量与连接方式 | `documented_cells=2 x 16340`；`schematic_symbol=BT1 Battery`；`series_parallel=not shown`；`cell_voltage=not shown` |
| GPIO 与控制信号 | S1 KEY | `switch=S1 SW-PB`；`controller_pin=U2.8 KEY`；`active_connection=GND` |
| GPIO 与控制信号 | U2 LIGHT/RSET | `LIGHT=U2.22 via R6 0Ω to GND`；`RSET=U2.5 via R7 100KΩ to GND`；`VSET=U2.23 NC` |
| 模拟电路 | U2 NTC 配置 | `ntc_pin=U2.6 NTC`；`upper_resistor=R2 2MΩ`；`lower_resistor=R4 1MΩ to GND` |
| 保护电路 | USB-C 输入保护 | `protector=F1 Fuse`；`input=J1 VBUS`；`output=VIN` |
| 时钟 | 时钟、复位与调试 | `external_clock=not shown`；`reset=not shown`；`boot=not shown`；`debug=not shown` |

## 待确认事项

- `address.i2c-0x75`：产品正文标注 I2C 地址为 0x75，但原理图只显示 U2 的 SCL/SDA 连接，未标注 0x75 或地址选择网络，无法仅由该页确认地址。（证据：图 6b43fc29c96e / 第 1 页 / 全页 U2 IP5209 与 SCL/SDA 网络，未见 0x75 或地址配置器件）
- `power.output-rating-5v-1p5a`：原理图网络名明确为 5VOUT，但产品正文声明的 1.5A 输出电流未在该页标注，无法仅由原理图确认完整的 5V/1.5A 额定值。（证据：图 6b43fc29c96e / 第 1 页 / 页面 J3.3/P3.2 的 5VOUT 标签与 U2 VOUT 路径，未见 1.5A 标注）
- `power.battery-configuration-16340`：产品正文描述可安装两节 16340 电池，但原理图仅以单个 BT1 Battery 等效符号表示，未标注两节电池的串联/并联方式或单节规格。（证据：图 6b43fc29c96e / 第 1 页 / 页面右上仅显示单个 BT1 Battery 符号及 BAT+/BAT-，无电池数量或串并联标注）
- `review.i2c-address-0x75`：IP5209 在本产品上的 7 位 I2C 地址是否固定为 0x75？；原因：产品正文给出 0x75，但原理图未标注地址或地址选择网络。
- `review.output-current-1p5a`：5VOUT 的持续输出电流 1.5A 适用于哪些输入、电池和散热条件？；原因：原理图标注 5VOUT，但没有 1.5A 额定值或热设计条件。
- `review.battery-configuration`：两节 16340 电池在实际电池座中采用串联还是并联，单节极性如何布置？；原因：正文描述两节 16340，但原理图仅有单个 BT1 等效符号，未说明数量和串并联。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6b43fc29c96e29b72347fef9ff8dc25868a116e45f870e8a6a1bbc2fb3df221b` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat-powerc/hat-powerc_sch_01.webp` |

---

源文档：`zh_CN/hat/hat-powerc.md`

源文档 SHA-256：`70933c63ffbea210c0df2fa86077b0b295a333fea94703f10d5074330a6f95c8`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
