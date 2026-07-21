# Unit CatM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit CatM |
| SKU | U128 |
| 产品 ID | `unit-catm-8f4ee0c8d6cd` |
| 源文档 | `zh_CN/unit/cat_m.md` |

## 概述

Unit CatM 以 SIM7080G（M1）为蜂窝通信核心，UART1_TXD/RXD 经 Q3/Q2 两组 SS8050 电平转换连接 HY-2.0_UART 接口 J1。+5V 经 SY8003ADFC（U1）、L1 和反馈网络转换为 +3.3V，为 M1 VBAT 供电；M1 VDD_EXT 另产生 +1.8V，供 UART 模组侧上拉并通过 R6 连接 PWRKEY。SIM 卡座 U3 的 DATA/CLK/RST 具有 22Ω 串联、33pF 对地滤波和 SMF05CT1G 防护，M1 ANT pin 32 直接连接 E1 ANT_IPEX。NETLIGHT 经 Q1 驱动 D1 指示灯；原理图未给出 UART 波特率或蜂窝频段表。

## 检索关键词

`Unit CatM`、`U128`、`SIM7080G`、`SY8003ADFC`、`WPN3012H2R2MT`、`SMF05CT1G`、`SS8050 Y1`、`Cat-M`、`NB-IoT`、`UART1_TXD`、`UART1_RXD`、`U1_TX`、`U1_RX`、`NB_TX`、`NB_RX`、`HY-2.0_UART`、`SIM_DATA`、`SIM_CLK`、`SIM_RST`、`SIM_VCC`、`ANT_IPEX`、`NETLIGHT`、`STATUS`、`PWRKEY`、`VDD_EXT`、`VBAT`、`+5V`、`+3.3V`、`+1.8V`、`22Ω`、`33pF`、`115200 8N1`、`UART2`、`USB_DP`、`USB_DM`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | SIM7080G | 蜂窝通信模组，提供 UART1、SIM、ANT、状态、USB、UART2 与电源控制接口 | 图 dd379979d003 / 第 1 页 / 页 1 中央 M1 SIM7080G，pins 1~42 的 UART/SIM/ANT/VBAT/VDD_EXT/NETLIGHT/STATUS/PWRKEY 标注 |
| U1 | SY8003ADFC | 从 +5V 产生 +3.3V 的同步降压转换器 | 图 dd379979d003 / 第 1 页 / 页 1 左上 U1 SY8003ADFC，IN/EN/LX/FB/PG/PGND/SGND 与 +5V/+3.3V 网络 |
| L1/R4/R5 | WPN3012H2R2MT / 68KΩ / 15KΩ | U1 降压输出电感与反馈分压网络 | 图 dd379979d003 / 第 1 页 / 页 1 左上：U1 LX pin 6-L1-+3.3V，R4 68KΩ/R5 15KΩ 连接 FB pin 1 |
| C1-C4 | 22uF / 22pF / 22uF / 22uF | U1 输入、反馈补偿和 +3.3V 输出滤波电容 | 图 dd379979d003 / 第 1 页 / 页 1 左上：C1 22uF 接 +5V，C2 22pF 位于输出/FB 网络，C3/C4 各 22uF 接 +3.3V |
| U2 | SMF05CT1G | SIM_VCC、SIM_DATA、SIM_CLK、SIM_RST 接口的多通道防护阵列 | 图 dd379979d003 / 第 1 页 / 页 1 中左 U2 SMF05CT1G，连接 SIM_VCC、GND 及三条 SIM 信号 |
| U3 | SIM | 外部 SIM 卡座，连接 SIM_VCC、RST、CLK、I/O 和 GND | 图 dd379979d003 / 第 1 页 / 页 1 中左 U3 SIM：pin 1 VCC、2 RST、3 CLK、5 GND、6 VPP、7 I/O |
| R7/R8/R9 | 22Ω | SIM_DATA、SIM_CLK、SIM_RST 到卡座的串联电阻 | 图 dd379979d003 / 第 1 页 / 页 1 中左：M1 pins 15/16/17 到 U3 I/O/CLK/RST 路径上的 R7/R8/R9 22Ω |
| C6/C7/C8 | 33pF | SIM_DATA、SIM_CLK、SIM_RST 的对地滤波电容 | 图 dd379979d003 / 第 1 页 / 页 1 中下：三条 SIM 信号各有 C6/C7/C8 33pF 到 GND |
| E1 | ANT_IPEX | SIM7080G ANT 的 IPEX 蜂窝天线连接器 | 图 dd379979d003 / 第 1 页 / 页 1 中右：M1 ANT pin 32 直接连接 E1 ANT_IPEX，外壳接 GND |
| J1 | HY-2.0_UART | 外部 UART、+5V 与 GND 接口 | 图 dd379979d003 / 第 1 页 / 页 1 右中 J1 HY-2.0_UART：pin 1 RX/NB_TX、pin 2 TX/NB_RX、pin 3 VCC/+5V、pin 4 GND |
| Q2/R10/R11/R12 | SS8050 Y1 / 4.7KΩ / 47KΩ / 4.7KΩ | 外部 NB_RX 与模组 U1_RX 之间的 3.3V/1.8V 电平转换网络 | 图 dd379979d003 / 第 1 页 / 页 1 右下上半：NB_RX、Q2 SS8050 Y1、R11 47KΩ 到 +3.3V、R10/R12 4.7KΩ 到 +1.8V/U1_RX |
| Q3/R13/R14/R15 | SS8050 Y1 / 4.7KΩ / 4.7KΩ / 4.7KΩ | 模组 U1_TX 与外部 NB_TX 之间的 1.8V/3.3V 电平转换网络 | 图 dd379979d003 / 第 1 页 / 页 1 右下下半：NB_TX、Q3 SS8050 Y1、R14 4.7KΩ 到 +3.3V、R13/R15 4.7KΩ 到 +1.8V/U1_TX |
| Q1/D1/R1/R2/R3 | SS8050 Y1 / 0603 / 1KΩ / 1KΩ / 10KΩ | NETLIGHT 控制的 +5V 指示灯驱动电路 | 图 dd379979d003 / 第 1 页 / 页 1 右上：+5V-R1-D1-Q1-GND，NETLIGHT 经 R2 驱动 Q1，R3 下拉到 GND |
| C5/R6 | 22uF / 0Ω | VDD_EXT +1.8V 去耦以及 PWRKEY 到 +1.8V 的连接 | 图 dd379979d003 / 第 1 页 / 页 1 中右：M1 VDD_EXT pin 40 的 +1.8V/C5 22uF，以及 PWRKEY pin 39 经 R6 0Ω 接 +1.8V |

## 系统结构

### Unit CatM

J1 提供 +5V 与外部 UART，U1 产生 +3.3V 供 M1 SIM7080G VBAT；M1 UART1 经 Q2/Q3 电平转换连接 J1，SIM 接口连接 U3 并由 U2 防护，ANT pin 32 连接 E1 ANT_IPEX。

- 参数与网络：`cellular_module=M1 SIM7080G`；`power=+5V->U1 SY8003ADFC->+3.3V`；`uart=J1<->Q2/Q3<->M1 UART1`；`sim=M1<->R7/R8/R9,U2,C6/C7/C8<->U3`；`rf=M1 ANT pin 32->E1 ANT_IPEX`
- 证据：图 dd379979d003 / 第 1 页 / 整页：U1/M1/U2/U3/E1/J1/Q1-Q3 及全部电源、UART、SIM、RF 网络

## 核心器件

### M1 SIM7080G 主要引脚

M1 UART1_TXD/RXD 为 pins 1/2，SIM_DATA/CLK/RST/VDD 为 pins 15/16/17/18，UART2_RXD/TXD 为 pins 23/22，USB_VBUS/DP/DM 为 pins 24/25/26，ANT 为 pin 32，VBAT 为 pins 34/35，PWRKEY/VDD_EXT/NETLIGHT/STATUS 为 pins 39/40/41/42。

- 参数与网络：`uart1=TXD1,RXD2`；`sim=DATA15,CLK16,RST17,VDD18`；`uart2=RXD23,TXD22`；`usb=VBUS24,DP25,DM26`；`antenna=ANT32`；`vbat=34,35`；`control_status=PWRKEY39,VDD_EXT40,NETLIGHT41,STATUS42`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 中央 M1 SIM7080G 左右两侧全部引脚号和名称

## 电源

### U1 SY8003ADFC

U1 IN pin 3 与 EN pin 7 接 +5V，LX pin 6 经 L1 WPN3012H2R2MT 输出 +3.3V，FB pin 1 接 R4 68KΩ/R5 15KΩ 分压；PG pin 2 未接，PGND pins 4/9 与 SGND pin 8 接 GND。

- 参数与网络：`input=+5V at IN pin 3`；`enable=EN pin 7 to +5V`；`switch=LX pin 6`；`inductor=L1 WPN3012H2R2MT`；`output=+3.3V`；`feedback=R4 68KΩ,R5 15KΩ to FB pin 1`；`power_good=PG pin 2 no-connect`；`grounds=pins 4,8,9`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 左上：U1 pins 1~9、L1、R4/R5 与 +5V/+3.3V/GND

### U1 输入/输出滤波

+5V 输入由 C1 22uF 对地去耦；+3.3V 输出由 C3/C4 各 22uF 对地去耦，C2 22pF 连接输出与反馈节点。

- 参数与网络：`input_capacitor=C1 22uF`；`output_capacitors=C3 22uF,C4 22uF`；`feedback_capacitor=C2 22pF`；`input_rail=+5V`；`output_rail=+3.3V`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 左上 U1 周围 C1/C2/C3/C4

### M1 VBAT

M1 VBAT pins 34/35 连接 +3.3V；GND pins 8/13/19/21/27/30/31/33/36/37 连接地。

- 参数与网络：`supply=+3.3V`；`vbat_pins=34,35`；`ground_pins=8,13,19,21,27,30,31,33,36,37`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 中央 M1 右侧 VBAT pins 34/35 与多组 GND pin 汇线

### M1 VDD_EXT

M1 VDD_EXT pin 40 形成 +1.8V 网络，C5 22uF 接地去耦；+1.8V 同时连接 UART 模组侧电阻网络。

- 参数与网络：`source=M1 VDD_EXT pin 40`；`rail=+1.8V`；`decoupling=C5 22uF to GND`；`uart_loads=R10,R12,R13,R15`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 中右 M1 pin 40/+1.8V/C5 及右下两组 UART 电阻的 +1.8V

## 接口

### J1 HY-2.0_UART

J1 pin 1 标 RX 并连接 NB_TX，pin 2 标 TX 并连接 NB_RX，pin 3 标 VCC 并接 +5V，pin 4 标 GND 并接地。

- 参数与网络：`pin_1=RX,NB_TX`；`pin_2=TX,NB_RX`；`pin_3=VCC,+5V`；`pin_4=GND`；`perspective=external host labels`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 右中 J1 pins 1~4、RX/TX/VCC/GND 与 NB_TX/NB_RX/+5V/GND

### NB_RX 到 U1_RX 电平转换

NB_RX 侧由 R11 47KΩ 接 +3.3V，U1_RX 侧由 R12 4.7KΩ 接 +1.8V，Q2 SS8050 Y1 与 R10 4.7KΩ 构成两侧之间的转换网络。

- 参数与网络：`external_net=NB_RX`；`external_pull=R11 47KΩ to +3.3V`；`transistor=Q2 SS8050 Y1`；`module_net=U1_RX`；`module_pull=R12 4.7KΩ to +1.8V`；`cross_resistor=R10 4.7KΩ`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 右下上半 Q2/R10/R11/R12/NB_RX/U1_RX/+3.3V/+1.8V

### U1_TX 到 NB_TX 电平转换

NB_TX 侧由 R14 4.7KΩ 接 +3.3V，U1_TX 侧由 R15 4.7KΩ 接 +1.8V，Q3 SS8050 Y1 与 R13 4.7KΩ 构成两侧之间的转换网络。

- 参数与网络：`external_net=NB_TX`；`external_pull=R14 4.7KΩ to +3.3V`；`transistor=Q3 SS8050 Y1`；`module_net=U1_TX`；`module_pull=R15 4.7KΩ to +1.8V`；`cross_resistor=R13 4.7KΩ`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 右下下半 Q3/R13/R14/R15/NB_TX/U1_TX/+3.3V/+1.8V

### 未使用的 SIM7080G 引脚

UART1_RTS/CTS/DCD/DTR/RI pins 3~7、PCM pins 9~12、GPIO5 pin 14、USB_BOOT pin 20、UART2 pins 22/23、USB_VBUS/DP/DM pins 24~26、NC pins 28/29 和 ADC pin 38 在页面标记未连接。

- 参数与网络：`uart1_modem=pins 3-7 NC`；`pcm=pins 9-12 NC`；`gpio5=pin 14 NC`；`usb_boot=pin 20 NC`；`uart2=pins 22,23 NC`；`usb=pins 24,25,26 NC`；`dedicated_nc=pins 28,29`；`adc=pin 38 NC`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 中央 M1 各红色 no-connect 标记：pins 3~7/9~12/14/20/22~26/28/29/38

## 总线

### SIM7080G UART1

M1 UART1_TXD pin 1 的 U1_TX 经 Q3 电平转换为 NB_TX，到 J1 pin 1 RX；J1 pin 2 TX 的 NB_RX 经 Q2 电平转换为 U1_RX，到 M1 UART1_RXD pin 2。

- 参数与网络：`module_tx_path=M1 pin1 U1_TX->Q3->NB_TX->J1 pin1 RX`；`module_rx_path=J1 pin2 TX->NB_RX->Q2->U1_RX->M1 pin2`；`module_domain=+1.8V`；`external_domain=+3.3V`；`direction_reference=SIM7080G`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 中央 M1 pins 1/2、右下 Q2/Q3 网络及右中 J1 NB_TX/NB_RX

### SIM_DATA/SIM_CLK/SIM_RST

SIM_DATA、SIM_CLK、SIM_RST 分别经过 R7、R8、R9 三只 22Ω 串联电阻到 U3，并分别由 C6、C7、C8 三只 33pF 电容接 GND。

- 参数与网络：`data=R7 22Ω,C6 33pF`；`clock=R8 22Ω,C7 33pF`；`reset=R9 22Ω,C8 33pF`；`device=M1`；`connector=U3`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 中左至中下 R7/R8/R9 与 C6/C7/C8 三条并行 SIM 信号路径

## GPIO 与控制信号

### M1 STATUS

M1 STATUS pin 42 连接名为 STATUS 的网络，但该网络在本页没有继续连接到 J1、LED 或其他器件。

- 参数与网络：`module_pin=STATUS pin 42`；`net=STATUS`；`external_connector=null`；`indicator=null`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 中右 M1 pin 42 STATUS 的水平网络终点

## 时钟

### 外部时钟

本页没有绘出晶振、振荡器或外部时钟网络；SIM_CLK 是 M1 与 SIM 卡座之间的卡接口时钟，不是板级晶振输入。

- 参数与网络：`external_crystal=null`；`external_oscillator=null`；`sim_clock=M1 pin 16 SIM_CLK to U3 pin 3`
- 证据：图 dd379979d003 / 第 1 页 / 整页无 Y/X 晶振位号；唯一 CLK 名为 M1 SIM_CLK pin 16 到 U3 pin 3

## 复位

### M1 PWRKEY

M1 PWRKEY pin 39 通过 R6 0Ω 连接 +1.8V，原理图未画外部按键或主控驱动器。

- 参数与网络：`control_pin=PWRKEY pin 39`；`resistor=R6 0Ω`；`rail=+1.8V`；`external_switch=null`；`external_driver=null`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 中右：M1 PWRKEY pin 39-R6 0Ω-+1.8V

## 保护电路

### U2 SMF05CT1G

U2 位于 U3 卡座与 M1 SIM 接口之间，连接 SIM_VCC、GND 以及 SIM_DATA/SIM_CLK/SIM_RST 三条信号。

- 参数与网络：`device=SMF05CT1G`；`power_reference=SIM_VCC`；`ground=GND`；`protected_signals=SIM_DATA,SIM_CLK,SIM_RST`；`location=between U3 and M1`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 中左 U2 六针阵列及与 SIM_VCC/GND/三条 SIM 线的节点

## 关键网络

### Unit CatM 关键网络索引

关键网络为 +5V→U1→+3.3V→M1 VBAT，M1 VDD_EXT→+1.8V，J1 RX/NB_TX↔Q3↔U1_TX，J1 TX/NB_RX↔Q2↔U1_RX，以及 M1 SIM_DATA/CLK/RST/VDD↔U3。

- 参数与网络：`main_power=+5V-U1-+3.3V-M1 VBAT`；`low_voltage=M1 VDD_EXT-+1.8V`；`tx_path=M1 U1_TX-Q3-NB_TX-J1.1`；`rx_path=J1.2-NB_RX-Q2-U1_RX-M1`；`sim_path=M1 pins 15-18-U2/R7/R8/R9/C6/C7/C8-U3`
- 证据：图 dd379979d003 / 第 1 页 / 整页同名 +5V/+3.3V/+1.8V/U1_TX/U1_RX/NB_TX/NB_RX/SIM_* 网络

## 存储

### U3 SIM 卡座

U3 VCC pin 1 接 SIM_VCC/M1 SIM_VDD pin 18，RST pin 2 接 SIM_RST/M1 pin 17，CLK pin 3 接 SIM_CLK/M1 pin 16，I/O pin 7 接 SIM_DATA/M1 pin 15，GND pin 5 接地，VPP pin 6 未接。

- 参数与网络：`vcc=U3.1 SIM_VCC->M1.18`；`reset=U3.2 SIM_RST->M1.17`；`clock=U3.3 SIM_CLK->M1.16`；`data=U3.7 SIM_DATA->M1.15`；`ground=U3.5 GND`；`vpp=U3.6 no-connect`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 中左 U3 pins 1/2/3/5/6/7 与 M1 SIM pins 15~18

## 射频

### E1 ANT_IPEX

M1 ANT pin 32 直接连接 E1 ANT_IPEX 中心端，E1 地端接 GND；页面未绘出串联/并联射频匹配器件或天线 ESD 器件。

- 参数与网络：`module_pin=M1 ANT pin 32`；`connector=E1 ANT_IPEX`；`shield=GND`；`matching_network=null`；`rf_esd=null`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 中右 M1 ANT pin 32 到 E1 的直连线及 GND

## 调试与烧录

### NETLIGHT 指示灯

M1 NETLIGHT pin 41 经 R2 1KΩ驱动 Q1 SS8050 Y1，R3 10KΩ将 NETLIGHT 下拉到 GND；+5V 经 R1 1KΩ和 D1 0603 接到 Q1，再由 Q1 接地。

- 参数与网络：`module_pin=NETLIGHT pin 41`；`base_resistor=R2 1KΩ`；`pulldown=R3 10KΩ`；`transistor=Q1 SS8050 Y1`；`led_path=+5V-R1 1KΩ-D1 0603-Q1-GND`
- 证据：图 dd379979d003 / 第 1 页 / 页 1 右上 NETLIGHT/R2/R3/Q1/D1/R1/+5V/GND 电路

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit CatM | `cellular_module=M1 SIM7080G`；`power=+5V->U1 SY8003ADFC->+3.3V`；`uart=J1<->Q2/Q3<->M1 UART1`；`sim=M1<->R7/R8/R9,U2,C6/C7/C8<->U3`；`rf=M1 ANT pin 32->E1 ANT_IPEX` |
| 电源 | U1 SY8003ADFC | `input=+5V at IN pin 3`；`enable=EN pin 7 to +5V`；`switch=LX pin 6`；`inductor=L1 WPN3012H2R2MT`；`output=+3.3V`；`feedback=R4 68KΩ,R5 15KΩ to FB pin 1`；`power_good=PG pin 2 no-connect`；`grounds=pins 4,8,9` |
| 电源 | U1 输入/输出滤波 | `input_capacitor=C1 22uF`；`output_capacitors=C3 22uF,C4 22uF`；`feedback_capacitor=C2 22pF`；`input_rail=+5V`；`output_rail=+3.3V` |
| 电源 | M1 VBAT | `supply=+3.3V`；`vbat_pins=34,35`；`ground_pins=8,13,19,21,27,30,31,33,36,37` |
| 电源 | M1 VDD_EXT | `source=M1 VDD_EXT pin 40`；`rail=+1.8V`；`decoupling=C5 22uF to GND`；`uart_loads=R10,R12,R13,R15` |
| 复位 | M1 PWRKEY | `control_pin=PWRKEY pin 39`；`resistor=R6 0Ω`；`rail=+1.8V`；`external_switch=null`；`external_driver=null` |
| 核心器件 | M1 SIM7080G 主要引脚 | `uart1=TXD1,RXD2`；`sim=DATA15,CLK16,RST17,VDD18`；`uart2=RXD23,TXD22`；`usb=VBUS24,DP25,DM26`；`antenna=ANT32`；`vbat=34,35`；`control_status=PWRKEY39,VDD_EXT40,NETLIGHT41,STATUS42` |
| 接口 | J1 HY-2.0_UART | `pin_1=RX,NB_TX`；`pin_2=TX,NB_RX`；`pin_3=VCC,+5V`；`pin_4=GND`；`perspective=external host labels` |
| 总线 | SIM7080G UART1 | `module_tx_path=M1 pin1 U1_TX->Q3->NB_TX->J1 pin1 RX`；`module_rx_path=J1 pin2 TX->NB_RX->Q2->U1_RX->M1 pin2`；`module_domain=+1.8V`；`external_domain=+3.3V`；`direction_reference=SIM7080G` |
| 接口 | NB_RX 到 U1_RX 电平转换 | `external_net=NB_RX`；`external_pull=R11 47KΩ to +3.3V`；`transistor=Q2 SS8050 Y1`；`module_net=U1_RX`；`module_pull=R12 4.7KΩ to +1.8V`；`cross_resistor=R10 4.7KΩ` |
| 接口 | U1_TX 到 NB_TX 电平转换 | `external_net=NB_TX`；`external_pull=R14 4.7KΩ to +3.3V`；`transistor=Q3 SS8050 Y1`；`module_net=U1_TX`；`module_pull=R15 4.7KΩ to +1.8V`；`cross_resistor=R13 4.7KΩ` |
| 总线 | 外部 UART 配置 | `physical_bus=UART1`；`schematic_baud=null`；`schematic_frame=null`；`configuration_source_needed=module firmware and host protocol` |
| 存储 | U3 SIM 卡座 | `vcc=U3.1 SIM_VCC->M1.18`；`reset=U3.2 SIM_RST->M1.17`；`clock=U3.3 SIM_CLK->M1.16`；`data=U3.7 SIM_DATA->M1.15`；`ground=U3.5 GND`；`vpp=U3.6 no-connect` |
| 总线 | SIM_DATA/SIM_CLK/SIM_RST | `data=R7 22Ω,C6 33pF`；`clock=R8 22Ω,C7 33pF`；`reset=R9 22Ω,C8 33pF`；`device=M1`；`connector=U3` |
| 保护电路 | U2 SMF05CT1G | `device=SMF05CT1G`；`power_reference=SIM_VCC`；`ground=GND`；`protected_signals=SIM_DATA,SIM_CLK,SIM_RST`；`location=between U3 and M1` |
| 射频 | E1 ANT_IPEX | `module_pin=M1 ANT pin 32`；`connector=E1 ANT_IPEX`；`shield=GND`；`matching_network=null`；`rf_esd=null` |
| 射频 | 蜂窝模式与频段 | `module=SIM7080G`；`antenna=ANT_IPEX`；`schematic_modes=null`；`schematic_bands=null`；`schematic_tx_power=null`；`schematic_data_rates=null` |
| 调试与烧录 | NETLIGHT 指示灯 | `module_pin=NETLIGHT pin 41`；`base_resistor=R2 1KΩ`；`pulldown=R3 10KΩ`；`transistor=Q1 SS8050 Y1`；`led_path=+5V-R1 1KΩ-D1 0603-Q1-GND` |
| GPIO 与控制信号 | M1 STATUS | `module_pin=STATUS pin 42`；`net=STATUS`；`external_connector=null`；`indicator=null` |
| 接口 | 未使用的 SIM7080G 引脚 | `uart1_modem=pins 3-7 NC`；`pcm=pins 9-12 NC`；`gpio5=pin 14 NC`；`usb_boot=pin 20 NC`；`uart2=pins 22,23 NC`；`usb=pins 24,25,26 NC`；`dedicated_nc=pins 28,29`；`adc=pin 38 NC` |
| 时钟 | 外部时钟 | `external_crystal=null`；`external_oscillator=null`；`sim_clock=M1 pin 16 SIM_CLK to U3 pin 3` |
| 关键网络 | Unit CatM 关键网络索引 | `main_power=+5V-U1-+3.3V-M1 VBAT`；`low_voltage=M1 VDD_EXT-+1.8V`；`tx_path=M1 U1_TX-Q3-NB_TX-J1.1`；`rx_path=J1.2-NB_RX-Q2-U1_RX-M1`；`sim_path=M1 pins 15-18-U2/R7/R8/R9/C6/C7/C8-U3` |

## 待确认事项

- `bus.uart-configuration-not-shown`：原理图只显示 UART1_TXD/RXD 电气路径，没有打印波特率、数据位、停止位或校验配置。（证据：图 dd379979d003 / 第 1 页 / 页 1 M1 UART1 pins 1/2、Q2/Q3 和 J1 路径，页面无 baud/8N1 字样）
- `rf.modes-bands-not-shown`：原理图可确认 M1 型号为 SIM7080G 和 ANT_IPEX 连接，但页面未打印 Cat-M/NB-IoT 模式、频段、发射功率或数据速率。（证据：图 dd379979d003 / 第 1 页 / 页 1 M1 SIM7080G 与 E1 ANT_IPEX，页面无 RF 参数表）
- `review.uart-configuration`：Unit CatM 当前模组固件和主机接口使用的 UART 波特率与帧格式是什么？；原因：原理图仅给出 UART1_TXD/RXD 和电平转换，没有串口配置文字，需要模组固件、AT 手册或实测确认。
- `review.rf-modes-bands`：本产品装配的 SIM7080G 变体支持哪些 Cat-M/NB-IoT 频段、发射功率和数据速率？；原因：这些射频能力由模组变体、固件和认证配置决定，原理图只显示模块型号与天线连接。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `dd379979d0031cf6f8baae204861f10734ec71b0aeab340c10e0b7fb89935a8e` | `https://static-cdn.m5stack.com/resource/docs/products/unit/cat_m/cat_m_sch_01.webp` |

---

源文档：`zh_CN/unit/cat_m.md`

源文档 SHA-256：`9fe7f5cbfdf317f7ff5ffe8a99a63443272088d92d5b5feb0e70976bd597ebfe`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
