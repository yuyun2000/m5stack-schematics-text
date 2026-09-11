# Faces_Calculator3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Faces_Calculator3 |
| SKU | A005-V3 |
| 产品 ID | `faces-calculator3-f4573557e7cb` |
| 源文档 | `zh_CN/faces/Faces_Calculator3.md` |

## 概述

Faces Calculator3 以 STM32G031G8U6 为控制器，扫描由 S1-S20 组成的 5 行 4 列计算器按键矩阵。模块通过 22 针 M5 BUS 引出 3.3V、GND、SDA、SCL 和 G35_INT，其中 I2C 与中断线均有 3.3V 上拉。矩阵的 A-E 行和 Col0-Col3 列各自配置 PESDNC2FD5VB 对地保护，并提供独立的 5 针 SWD 调试接口和 RC 复位网络。

## 检索关键词

`Faces Calculator3`、`Faces_Calculator3`、`A005-V3`、`STM32G031G8U6`、`M5_BUS_22P`、`SWD_5P`、`4x5按键矩阵`、`20键计算器键盘`、`3x4x2.5按键`、`PESDNC2FD5VB`、`I2C`、`SDA`、`SCL`、`G35_INT`、`AD35`、`VCC_3V3`、`NRST`、`MCU_SWCLK`、`MCU_SWDIO`、`PA0-PA5`、`PA11`、`PA12`、`PA13`、`PA14-BOOT0`、`PB0`、`PB1`、`PB3`、`PB4`、`Col0-Col3`、`A-E矩阵行`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | STM32G031G8U6 | 扫描 5×4 按键矩阵，并通过 SDA、SCL 与 G35_INT 同主机连接的控制器。 | 图 139fbe970908 / 第 1 页 / 页1 C1-C2 区域，U2 标注 STM32G031G8U6，左右引脚连接 A-E、Col0-Col3、SDA、SCL、G35_INT、NRST 和 SWD 网络。 |
| J1 | M5_BUS_22P | 22 针主机连接器，实际接出 GND、VCC_3V3、G35_INT、SDA 和 SCL。 | 图 139fbe970908 / 第 1 页 / 页1 A-B3 区域，J1 标注 M5_BUS_22P；pin 2、3、4、15、17 分别连接 GND、VCC_3V3、G35_INT、SDA、SCL。 |
| J2 | SWD_5P | 控制器下载与调试连接器，引出 VCC、SWCLK、SWDIO、NRST 和 GND。 | 图 139fbe970908 / 第 1 页 / 页1 D2 区域，J2 标注 SWD_5P，五个端子依次标为 VCC、SWCLK、SWDIO、NRST、GND。 |
| S1-S20 | 3x4x2.5 | 组成 5 行 4 列计算器键盘的 20 个按键开关。 | 图 139fbe970908 / 第 1 页 / 页1 A-B1-2 区域，S1-S20 排列为 A-E 五行与 Col0-Col3 四列，每个开关旁均标注 3x4x2.5。 |
| D1-D9 | PESDNC2FD5VB | 分别将五条矩阵行线和四条矩阵列线接至 GND 的保护器件。 | 图 139fbe970908 / 第 1 页 / 页1 A-B1-2 区域，D1-D5 接在 A-E 与 GND 之间，D6-D9 接在 Col0-Col3 与 GND 之间，型号均标注 PESDNC2FD5VB。 |
| C1 | 100nF | 连接在 VCC_3V3 与 GND 之间的控制器电源去耦电容。 | 图 139fbe970908 / 第 1 页 / 页1 C1 区域，C1 标注 100nF，与 C2 并接在 U2 VDD/VDDA 的 VCC_3V3 和 GND 之间。 |
| C2 | 10uF | 连接在 VCC_3V3 与 GND 之间的控制器电源储能/滤波电容。 | 图 139fbe970908 / 第 1 页 / 页1 C1 区域，C2 标注 10uF，与 C1 并接在 U2 VDD/VDDA 的 VCC_3V3 和 GND 之间。 |
| R1 | 10K | NRST 到 VCC_3V3 的上拉电阻。 | 图 139fbe970908 / 第 1 页 / 页1 D1 区域，R1 标注 10K，上端连接 VCC_3V3，下端连接 NRST。 |
| C3 | 100nF | NRST 到 GND 的复位电容。 | 图 139fbe970908 / 第 1 页 / 页1 D1 区域，C3 标注 100nF，上端连接 NRST，下端连接 GND。 |
| R2,R3 | 4.7K | SDA 与 SCL 到 VCC_3V3 的 I2C 上拉电阻。 | 图 139fbe970908 / 第 1 页 / 页1 C2 区域，R2、R3 均标注 4.7K，上端连接 VCC_3V3，下端分别连接 SDA、SCL。 |
| R4 | 10K | G35_INT 到 VCC_3V3 的上拉电阻。 | 图 139fbe970908 / 第 1 页 / 页1 C1 区域，R4 标注 10K，连接在 VCC_3V3 与 U2 pin 11 的 G35_INT 之间。 |

## 系统结构

### 按键扫描架构

U2 STM32G031G8U6 通过 A-E 五条行线和 Col0-Col3 四条列线扫描 S1-S20，共形成 5×4 的 20 键矩阵；主机侧连接集中在 J1。

- 参数与网络：`controller=U2 STM32G031G8U6`；`row_count=5`；`column_count=4`；`switch_count=20`；`host_connector=J1 M5_BUS_22P`
- 证据：图 139fbe970908 / 第 1 页 / 页1 A-C1-3 区域，S1-S20 的 A-E/Col0-Col3 矩阵连接至 U2，U2 的 SDA、SCL、G35_INT 与供电再连接 J1。

## 核心器件

### 按键开关标注

S1-S20 的器件图形旁均标注 3x4x2.5。

- 参数与网络：`references=S1-S20`；`marking=3x4x2.5`；`quantity=20`
- 证据：图 139fbe970908 / 第 1 页 / 页1 A-B1-2 区域，每个 S1-S20 开关符号下方均重复标注 3x4x2.5。

## 电源

### 主机侧 3.3V 供电

J1 pin 3 的 3V3 脚直接形成模块的 VCC_3V3 电源轨，J1 pin 2 接 GND。

- 参数与网络：`supply_connector=J1 pin 3`；`supply_net=VCC_3V3`；`ground_connector=J1 pin 2`；`ground_net=GND`
- 证据：图 139fbe970908 / 第 1 页 / 页1 A-B3 区域，J1 pin 3 标注 3V3 并连接 VCC_3V3，pin 2 标注 GND 并连接地符号。

### U2 电源连接

U2 pin 3 VDD/VDDA 连接 VCC_3V3，pin 4 VSS/VSSA 连接 GND。

- 参数与网络：`positive_pin=U2 pin 3 VDD/VDDA`；`positive_net=VCC_3V3`；`ground_pin=U2 pin 4 VSS/VSSA`；`ground_net=GND`
- 证据：图 139fbe970908 / 第 1 页 / 页1 C1 区域，U2 左上 pin 3 VDD/VDDA 接 VCC_3V3，pin 4 VSS/VSSA 接 GND。

### U2 供电去耦

C1 100nF 与 C2 10uF 并联在 VCC_3V3 和 GND 之间，并布置在 U2 的 VDD/VDDA 供电节点。

- 参数与网络：`capacitor_1=C1 100nF`；`capacitor_2=C2 10uF`；`rail=VCC_3V3`；`return=GND`
- 证据：图 139fbe970908 / 第 1 页 / 页1 C1 区域，C1/C2 上端共接 VCC_3V3 与 U2 pin 3，下端共接 GND 与 U2 pin 4。

## 接口

### J1 M5 BUS 有效连接

J1 上可见的实际网络连接为 pin 2 GND、pin 3 VCC_3V3、pin 4 G35_INT（连接器脚名 AD35）、pin 15 SDA 和 pin 17 SCL；pin 1 的 5V 脚在本页未接入模块电路。

- 参数与网络：`pin_2=GND`；`pin_3=VCC_3V3 (3V3)`；`pin_4=G35_INT (AD35)`；`pin_15=SDA`；`pin_17=SCL`；`pin_1_5v=未连接`
- 证据：图 139fbe970908 / 第 1 页 / 页1 A-B3 区域，J1 M5_BUS_22P 两侧逐脚网络：2=GND、4=AD35/G35_INT、3=3V3/VCC_3V3、15=SDA、17=SCL，1=5V 仅有悬空短线。

### G35_INT 中断连接

U2 pin 11 PA5 连接 G35_INT；该网络由 R4 10K 上拉至 VCC_3V3，并接到 J1 pin 4 的 AD35 脚。

- 参数与网络：`mcu_pin=U2 pin 11 PA5`；`net=G35_INT`；`pullup=R4 10K`；`connector_pin=J1 pin 4 AD35`
- 证据：图 139fbe970908 / 第 1 页 / 页1 C1 与 A-B3 区域，U2 pin 11 PA5 标注 G35_INT，经 R4 10K 上拉；J1 pin 4 的 AD35 接同名 G35_INT 网络。

## 总线

### I2C SDA

SDA 从 U2 pin 19（PA12 [PA10]）连接到 J1 pin 15，并由 R2 4.7K 上拉到 VCC_3V3。

- 参数与网络：`mcu_pin=U2 pin 19 PA12 [PA10]`；`connector_pin=J1 pin 15 SDA`；`pullup=R2 4.7K`；`pullup_rail=VCC_3V3`
- 证据：图 139fbe970908 / 第 1 页 / 页1 C2 与 A-B3 区域，U2 pin 19 标注 PA12 [PA10]/SDA，R2 4.7K 上拉至 VCC_3V3，J1 pin 15 标注 SDA。

### I2C SCL

SCL 从 U2 pin 18（PA11 [PA9]）连接到 J1 pin 17，并由 R3 4.7K 上拉到 VCC_3V3。

- 参数与网络：`mcu_pin=U2 pin 18 PA11 [PA9]`；`connector_pin=J1 pin 17 SCL`；`pullup=R3 4.7K`；`pullup_rail=VCC_3V3`
- 证据：图 139fbe970908 / 第 1 页 / 页1 C2 与 A-B3 区域，U2 pin 18 标注 PA11 [PA9]/SCL，R3 4.7K 上拉至 VCC_3V3，J1 pin 17 标注 SCL。

## GPIO 与控制信号

### 矩阵行 GPIO 映射

矩阵行 A、B、C、D、E 分别连接 U2 的 PA0、PA1、PA2、PA3、PA4（pin 6、7、8、9、10）。

- 参数与网络：`A=U2 pin 6 PA0`；`B=U2 pin 7 PA1`；`C=U2 pin 8 PA2`；`D=U2 pin 9 PA3`；`E=U2 pin 10 PA4`
- 证据：图 139fbe970908 / 第 1 页 / 页1 C1 区域，U2 左侧连续显示 A/PA0/pin6、B/PA1/pin7、C/PA2/pin8、D/PA3/pin9、E/PA4/pin10。

### 矩阵列 GPIO 映射

矩阵列 Col0、Col1、Col2、Col3 分别连接 U2 的 PB0、PB1、PB3、PB4（pin 14、15、23、24）。

- 参数与网络：`Col0=U2 pin 14 PB0`；`Col1=U2 pin 15 PB1`；`Col2=U2 pin 23 PB3`；`Col3=U2 pin 24 PB4`
- 证据：图 139fbe970908 / 第 1 页 / 页1 C1-C2 区域，U2 显示 Col0/PB0/pin14、Col1/PB1/pin15、Col2/PB3/pin23、Col3/PB4/pin24。

## 时钟

### U2 低速晶振引脚

U2 pin 1 PC14-OSC32IN 与 pin 2 PC15-OSC32OUT 均以 no-connect 标记结束，本页未连接外部 32 kHz 晶振网络。

- 参数与网络：`osc32in=U2 pin 1 PC14-OSC32IN, no-connect`；`osc32out=U2 pin 2 PC15-OSC32OUT, no-connect`
- 证据：图 139fbe970908 / 第 1 页 / 页1 C1 区域，U2 pin1 与 pin2 左侧均有红色 no-connect 叉号，分别对应 PC14-OSC32IN、PC15-OSC32OUT。

## 复位

### U2 NRST 网络

U2 pin 5 PF2-NRST 接 NRST；R1 10K 将 NRST 上拉至 VCC_3V3，C3 100nF 将 NRST 接至 GND，NRST 同时引到 J2。

- 参数与网络：`mcu_pin=U2 pin 5 PF2-NRST`；`pullup=R1 10K to VCC_3V3`；`capacitor=C3 100nF to GND`；`debug_connector=J2 NRST`
- 证据：图 139fbe970908 / 第 1 页 / 页1 C1 与 D1-D2 区域，U2 pin5 标注 PF2-NRST/NRST；R1 从 VCC_3V3 上拉，C3 到 GND，J2 有 NRST 端子。

## 保护电路

### 矩阵行线保护

A、B、C、D、E 五条行线分别通过 D1、D2、D3、D4、D5（PESDNC2FD5VB）连接至 GND。

- 参数与网络：`A=D1 PESDNC2FD5VB`；`B=D2 PESDNC2FD5VB`；`C=D3 PESDNC2FD5VB`；`D=D4 PESDNC2FD5VB`；`E=D5 PESDNC2FD5VB`；`return=GND`
- 证据：图 139fbe970908 / 第 1 页 / 页1 A-B1 区域，A-E 每条水平行线左端各有 D1-D5，器件另一端均连接 GND。

### 矩阵列线保护

Col0、Col1、Col2、Col3 四条列线分别通过 D6、D7、D8、D9（PESDNC2FD5VB）连接至 GND。

- 参数与网络：`Col0=D6 PESDNC2FD5VB`；`Col1=D7 PESDNC2FD5VB`；`Col2=D8 PESDNC2FD5VB`；`Col3=D9 PESDNC2FD5VB`；`return=GND`
- 证据：图 139fbe970908 / 第 1 页 / 页1 B1-B2 区域，Col0-Col3 四条竖直列线底端各有 D6-D9，器件另一端均连接 GND。

## 关键网络

### 矩阵 A 行键位

A 行从 Col0 到 Col3 依次为 S1 AC、S2 M、S3 %、S4 +。

- 参数与网络：`row=A`；`Col0=S1 AC`；`Col1=S2 M`；`Col2=S3 %`；`Col3=S4 +`
- 证据：图 139fbe970908 / 第 1 页 / 页1 A1-A2 区域，A 行横向经过 S1-S4，紫色功能字符依次为 AC、M、%、+，右端分别落在 Col0-Col3。

### 矩阵 B 行键位

B 行从 Col0 到 Col3 依次为 S5 7、S6 8、S7 9、S8 *。

- 参数与网络：`row=B`；`Col0=S5 7`；`Col1=S6 8`；`Col2=S7 9`；`Col3=S8 *`
- 证据：图 139fbe970908 / 第 1 页 / 页1 A-B1-2 区域，B 行横向经过 S5-S8，紫色功能字符依次为 7、8、9、*，右端分别落在 Col0-Col3。

### 矩阵 C 行键位

C 行从 Col0 到 Col3 依次为 S9 4、S10 5、S11 6、S12 -。

- 参数与网络：`row=C`；`Col0=S9 4`；`Col1=S10 5`；`Col2=S11 6`；`Col3=S12 -`
- 证据：图 139fbe970908 / 第 1 页 / 页1 A-B1-2 区域，C 行横向经过 S9-S12，紫色功能字符依次为 4、5、6、-，右端分别落在 Col0-Col3。

### 矩阵 D 行键位

D 行从 Col0 到 Col3 依次为 S13 1、S14 2、S15 3、S16 +。

- 参数与网络：`row=D`；`Col0=S13 1`；`Col1=S14 2`；`Col2=S15 3`；`Col3=S16 +`
- 证据：图 139fbe970908 / 第 1 页 / 页1 B1-B2 区域，D 行横向经过 S13-S16，紫色功能字符依次为 1、2、3、+，右端分别落在 Col0-Col3。

### 矩阵 E 行键位

E 行从 Col0 到 Col3 依次经过 S17、S18、S19、S20；图中 S17、S18、S19 的可见字符分别为 .、0、+/-，S20 未显示功能字符。

- 参数与网络：`row=E`；`Col0=S17 .`；`Col1=S18 0`；`Col2=S19 +/-`；`Col3=S20（未显示功能字符）`
- 证据：图 139fbe970908 / 第 1 页 / 页1 B1-B2 区域，E 行横向经过 S17-S20；S17-S19 上方可见 .、0、+/-，S20 上方没有紫色功能字符。

### 主机信号上拉

SDA、SCL、G35_INT 分别通过 R2 4.7K、R3 4.7K、R4 10K 上拉到 VCC_3V3。

- 参数与网络：`SDA=R2 4.7K to VCC_3V3`；`SCL=R3 4.7K to VCC_3V3`；`G35_INT=R4 10K to VCC_3V3`
- 证据：图 139fbe970908 / 第 1 页 / 页1 C1-C2 区域，R2/R3 顶端共接 VCC_3V3、下端接 SDA/SCL；R4 一端接 VCC_3V3、另一端接 G35_INT。

## 调试与烧录

### SWD 调试接口

J2 提供 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST 和 GND；MCU_SWCLK 连接 U2 pin 21 PA14-BOOT0，MCU_SWDIO 连接 U2 pin 20 PA13。

- 参数与网络：`connector=J2 SWD_5P`；`clock=MCU_SWCLK -> U2 pin 21 PA14-BOOT0`；`data=MCU_SWDIO -> U2 pin 20 PA13`；`reset=NRST`；`supply=VCC_3V3`；`ground=GND`
- 证据：图 139fbe970908 / 第 1 页 / 页1 C2 与 D2 区域，U2 pin21/pin20 分别标注 MCU_SWCLK/MCU_SWDIO；J2 五针端子接 VCC_3V3、两条 SWD 网络、NRST、GND。

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 按键扫描架构 | `controller=U2 STM32G031G8U6`；`row_count=5`；`column_count=4`；`switch_count=20`；`host_connector=J1 M5_BUS_22P` |
| 接口 | J1 M5 BUS 有效连接 | `pin_2=GND`；`pin_3=VCC_3V3 (3V3)`；`pin_4=G35_INT (AD35)`；`pin_15=SDA`；`pin_17=SCL`；`pin_1_5v=未连接` |
| 电源 | 主机侧 3.3V 供电 | `supply_connector=J1 pin 3`；`supply_net=VCC_3V3`；`ground_connector=J1 pin 2`；`ground_net=GND` |
| 电源 | U2 电源连接 | `positive_pin=U2 pin 3 VDD/VDDA`；`positive_net=VCC_3V3`；`ground_pin=U2 pin 4 VSS/VSSA`；`ground_net=GND` |
| 电源 | U2 供电去耦 | `capacitor_1=C1 100nF`；`capacitor_2=C2 10uF`；`rail=VCC_3V3`；`return=GND` |
| 总线 | I2C SDA | `mcu_pin=U2 pin 19 PA12 [PA10]`；`connector_pin=J1 pin 15 SDA`；`pullup=R2 4.7K`；`pullup_rail=VCC_3V3` |
| 总线 | I2C SCL | `mcu_pin=U2 pin 18 PA11 [PA9]`；`connector_pin=J1 pin 17 SCL`；`pullup=R3 4.7K`；`pullup_rail=VCC_3V3` |
| 接口 | G35_INT 中断连接 | `mcu_pin=U2 pin 11 PA5`；`net=G35_INT`；`pullup=R4 10K`；`connector_pin=J1 pin 4 AD35` |
| GPIO 与控制信号 | 矩阵行 GPIO 映射 | `A=U2 pin 6 PA0`；`B=U2 pin 7 PA1`；`C=U2 pin 8 PA2`；`D=U2 pin 9 PA3`；`E=U2 pin 10 PA4` |
| GPIO 与控制信号 | 矩阵列 GPIO 映射 | `Col0=U2 pin 14 PB0`；`Col1=U2 pin 15 PB1`；`Col2=U2 pin 23 PB3`；`Col3=U2 pin 24 PB4` |
| 关键网络 | 矩阵 A 行键位 | `row=A`；`Col0=S1 AC`；`Col1=S2 M`；`Col2=S3 %`；`Col3=S4 +` |
| 关键网络 | 矩阵 B 行键位 | `row=B`；`Col0=S5 7`；`Col1=S6 8`；`Col2=S7 9`；`Col3=S8 *` |
| 关键网络 | 矩阵 C 行键位 | `row=C`；`Col0=S9 4`；`Col1=S10 5`；`Col2=S11 6`；`Col3=S12 -` |
| 关键网络 | 矩阵 D 行键位 | `row=D`；`Col0=S13 1`；`Col1=S14 2`；`Col2=S15 3`；`Col3=S16 +` |
| 关键网络 | 矩阵 E 行键位 | `row=E`；`Col0=S17 .`；`Col1=S18 0`；`Col2=S19 +/-`；`Col3=S20（未显示功能字符）` |
| 核心器件 | 按键开关标注 | `references=S1-S20`；`marking=3x4x2.5`；`quantity=20` |
| 保护电路 | 矩阵行线保护 | `A=D1 PESDNC2FD5VB`；`B=D2 PESDNC2FD5VB`；`C=D3 PESDNC2FD5VB`；`D=D4 PESDNC2FD5VB`；`E=D5 PESDNC2FD5VB`；`return=GND` |
| 保护电路 | 矩阵列线保护 | `Col0=D6 PESDNC2FD5VB`；`Col1=D7 PESDNC2FD5VB`；`Col2=D8 PESDNC2FD5VB`；`Col3=D9 PESDNC2FD5VB`；`return=GND` |
| 复位 | U2 NRST 网络 | `mcu_pin=U2 pin 5 PF2-NRST`；`pullup=R1 10K to VCC_3V3`；`capacitor=C3 100nF to GND`；`debug_connector=J2 NRST` |
| 调试与烧录 | SWD 调试接口 | `connector=J2 SWD_5P`；`clock=MCU_SWCLK -> U2 pin 21 PA14-BOOT0`；`data=MCU_SWDIO -> U2 pin 20 PA13`；`reset=NRST`；`supply=VCC_3V3`；`ground=GND` |
| 时钟 | U2 低速晶振引脚 | `osc32in=U2 pin 1 PC14-OSC32IN, no-connect`；`osc32out=U2 pin 2 PC15-OSC32OUT, no-connect` |
| 关键网络 | 主机信号上拉 | `SDA=R2 4.7K to VCC_3V3`；`SCL=R3 4.7K to VCC_3V3`；`G35_INT=R4 10K to VCC_3V3` |
| 总线地址 | I2C 从机地址 | `schematic_address_annotation=未标注`；`source_document_value=0x08`；`verification_needed=固件或通信协议` |
| 其他事实 | S20 键功能 | `reference=S20`；`matrix_position=E × Col3`；`visible_legend=无` |

## 待确认事项

- `address.i2c-address-not-shown`：原理图页只给出 SDA、SCL 连接与上拉，没有标注 I2C 从机地址，因此无法仅依据该页确认具体地址。（证据：图 139fbe970908 / 第 1 页 / 页1 C2 与 A-B3 区域，U2/J1 之间仅出现 SDA、SCL 网络及 R2/R3 上拉，页内没有地址或地址选择脚标注。）
- `other.s20-function-unlabeled`：S20 明确位于 E 行与 Col3 的交点，但原理图未显示其功能字符，无法从本页确认该键的具体功能。（证据：图 139fbe970908 / 第 1 页 / 页1 B2 区域，S20 开关连接 E 行和 Col3，S20 上方未见与其他按键相同的紫色功能字符。）
- `review.i2c-address`：Faces Calculator3 的固件实际使用的 I2C 从机地址是否为产品正文所列的 0x08？；原因：原理图只展示 I2C 物理连接，不包含地址标注或地址选择配置。
- `review.s20-key-function`：S20（E×Col3）的键帽或固件功能是什么？；原因：该矩阵位置和位号可确认，但原理图未给出 S20 的功能字符。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `139fbe9709080097d0c3b8a11222343efee1fa85c8089d4ef100e4f094cf6615` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1272/A005-V3-Faces_Calculator3_Sche_page_01.png` |

---

源文档：`zh_CN/faces/Faces_Calculator3.md`

源文档 SHA-256：`66b9157a4825efa4ee153170205ba344f18d14f83ed0e3b84d123f5215651ab0`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
