# AddOn_Display_Out_For_PoE-P4 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AddOn_Display_Out_For_PoE-P4 |
| SKU | U221 |
| 产品 ID | `addon-display-out-for-poe-p4-33184beb8d4b` |
| 源文档 | `zh_CN/addon/AddOn_Display_Out_For_PoE-P4.md` |

## 概述

AddOn_Display_Out_For_PoE-P4 V0.2 的本地原理图页以 U3 LT8912B 为核心，将 JP1 输入的两通道 MIPI DSI 时钟/数据差分对转换为 J1 HDMI Type-A 的三路 TMDS 数据、时钟、DDC 与热插拔信号。U1 SY8003 从 VCC_5V 产生 VCC_1V8，再经三颗磁珠形成 1V8_VDD、1V8_VCCA 和 1V8_VCCA_HDMIPLL；U2/U4 MT9700-N 分别生成 HDMI_5V 与 USB_5V。板上还包含 JP4 触摸接口、USB1 Type-A、J2 TF 卡、双向 I2C 电平转换、复位/中断电平转换以及 HDMI/USB/SDIO ESD 防护。资源仅包含图框标为 2/2 的一页，且 JP2 与 J2 的 SDIO 网络后缀映射不同，完整跨页连接和器件地址需要第 1 页或网表复核。

## 检索关键词

`AddOn_Display_Out_For_PoE-P4`、`U221`、`UnitPoEP4_DSI_TO_HDMI`、`V0.2`、`LT8912B`、`SY8003`、`MT9700-N`、`2N7002DW`、`MMBT3904TT1G`、`MIPI DSI 2-Lane`、`HDMI Type-A`、`HDMI-001 19PCBTP`、`F-FPCOM24P-C310`、`USB-AF-DIP-154-HW-S`、`TF_Card`、`SYS_SCL`、`SYS_SDA`、`S_SCL`、`S_SDA`、`TP_RST`、`TP_INT`、`RESET_N`、`RST_N`、`HPD_DET`、`HPD_CBUS`、`VCC_5V`、`VCC_3V3`、`VCC_1V8`、`1V8_VDD`、`1V8_VCCA`、`1V8_VCCA_HDMIPLL`、`HDMI_5V`、`USB_5V`、`SDIO_G13_CMD`、`SDIO_G12_CK`、`MIPI_DSI_CK_P`、`MIPI_DSI_D0_P`、`TX_SCL`、`TX_SDA`、`25M-12pF`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | LT8912B | MIPI DSI 接收与 HDMI/TMDS 输出桥接器，连接 DSI、TMDS、DDC、HPD、I2C、复位和 25MHz 晶体 | 图 907de836daf1 / 第 1 页 / 第 1 页（图框 2/2）网格 B3-D6，U3 LT8912B pins1-65 |
| U1 | SY8003 | VCC_5V 到 VCC_1V8 的降压转换器，反馈分压设定 1.8V | 图 907de836daf1 / 第 1 页 / 第 1 页网格 A1-A3，POWER 1V8 区 U1 SY8003、L1、R4/R5 |
| U2,U4 | MT9700-N | 两路 5V 限流负载开关，U2 输出 HDMI_5V，U4 输出 USB_5V | 图 907de836daf1 / 第 1 页 / 第 1 页网格 B1-B3，POWER 5V 的 U2 与 USB A 的 U4 MT9700-N |
| Q1,Q2 | 2N7002DW | 双 N 沟道 MOSFET 电平转换器，分别处理 RESET_N/RST_N、TP_INT/INT 与 SYS_SCL/SDA 到 S_SCL/SDA | 图 907de836daf1 / 第 1 页 / 第 1 页网格 A4-A6，Q1A/Q1B/Q2A/Q2B 2N7002DW 电平转换 |
| Q3 | MMBT3904TT1G | HDMI 热插拔检测路径中的晶体管，连接 HPD_DET、HPD_CBUS 与 1V8_VCCA | 图 907de836daf1 / 第 1 页 / 第 1 页网格 C7，Q3 MMBT3904TT1G、HPD_DET、HPD_CBUS |
| X1 | 25M-12pF(X322525MOB4SI) | LT8912B 的 25MHz 晶体时钟，配套 R10 1MΩ 与 C6/C8 12pF | 图 907de836daf1 / 第 1 页 / 第 1 页网格 B5，X1 25M-12pF、XTALI/XTALO、R10、C6、C8 |
| JP1 | F-FPCOM24P-C310 | 24 针 FPC 输入，承载触摸控制、MIPI DSI、RESET_N、3.3V 与 GND | 图 907de836daf1 / 第 1 页 / 第 1 页网格 A7-A8，JP1 F-FPCOM24P-C310 pins1-24 与 SH |
| JP2 | 未标注 | 9 针输入连接器，承载 SDIO、USB1 D+/D- 与 VCC_5V | 图 907de836daf1 / 第 1 页 / 第 1 页网格 A6-A7，JP2 pins1-9，SDIO/USB1/VCC_5V |
| JP3 | 未标注 | 6 针电源连接器，仅 pin1 GND 与 pin6 VCC_3V3 有效，C7 提供 3.3V 去耦 | 图 907de836daf1 / 第 1 页 / 第 1 页网格 A6-A7，JP3 pins1-6 与 C7 10uF/10V |
| JP4 | 未标注 | 6 针触摸接口，引出 3.3V、TP_RST、SYS_SCL、SYS_SDA、TP_INT 与 GND | 图 907de836daf1 / 第 1 页 / 第 1 页网格 D1-D3，TOUCH 区 JP4 pins1-6/SH |
| J1 | HDMI-001 19PCBTP | HDMI Type-A 输出连接器，承载三路 TMDS 数据、时钟、DDC、+5V 与 HOTPLUG | 图 907de836daf1 / 第 1 页 / 第 1 页网格 B7-C8，J1 HDMI-001 19PCBTP pins1-23 |
| USB1 | USB-AF-DIP-154-HW-S | USB Type-A 母座，连接 USB_5V、USB1_D_N、USB1_D_P 和 GND | 图 907de836daf1 / 第 1 页 / 第 1 页网格 B2，USB A 区 USB1 pins1-4 |
| J2 | TF_Card | microSD/TF 卡座，连接 DATA0-DATA3、CMD、CLK、3.3V、GND 与 TF_DET | 图 907de836daf1 / 第 1 页 / 第 1 页网格 C1-C3，TF CARD 区 J2 pins1-10 |
| L1 | FTC25012S2R2MBCA | SY8003 降压电源输出电感，连接 LX 与 VCC_1V8 | 图 907de836daf1 / 第 1 页 / 第 1 页网格 A2，L1 FTC25012S2R2MBCA |
| FB1,FB2,FB3 | BLM15PX221SN1D | 把 VCC_1V8 分隔为 LT8912B 的数字、模拟与 HDMI PLL 三路 1.8V 电源轨 | 图 907de836daf1 / 第 1 页 / 第 1 页网格 A3，FB1/FB2/FB3 BLM15PX221SN1D |
| DR1,DR2 | ESD351 | USB1 D- 与 D+ 到 GND 的单线 ESD 防护器件 | 图 907de836daf1 / 第 1 页 / 第 1 页网格 B2，DR1/DR2 ESD351 与 USB1_D_N/P |
| D3,D4,D5 | ESD0524P | HDMI TMDS、DDC 与 HPD 信号的多通道 ESD 防护阵列 | 图 907de836daf1 / 第 1 页 / 第 1 页网格 D7-D8，D3/D4/D5 ESD0524P |
| TVS1,TVS2,TVS3,TVS4,TVS5,TVS6,TVS7 | 未标注 | TF 卡 SDIO 与 TF_DET 信号到 GND 的离散 TVS/ESD 防护 | 图 907de836daf1 / 第 1 页 / 第 1 页网格 D1-D3，TVS1-TV7 连接 SDIO_G8-G13/TF_DET |
| R21,C18 | 0R/5% / 1nF/2KV | GND 与 HDMI 机壳地 HFGND 之间的并联直流/高频耦合网络 | 图 907de836daf1 / 第 1 页 / 第 1 页网格 D8，R21 0R/5% 与 C18 1nF/2KV 并联至 HFGND |

## 系统结构

### 显示输出系统架构

U3 LT8912B 接收 JP1 的 MIPI_DSI_CK_P/N、MIPI_DSI_D0_P/N 与 MIPI_DSI_D1_P/N，输出 TX_D0/D1/D2/CK 差分对至 J1 HDMI，并通过 TX_SCL/TX_SDA 与 HPD_CBUS 完成 DDC 和热插拔路径。

- 参数与网络：`bridge=U3 LT8912B`；`input=2-lane MIPI DSI`；`output=HDMI TMDS D0/D1/D2/CLK`；`control=S_SCL/S_SDA, RST_N`；`ddc=TX_SCL/TX_SDA`；`hotplug=HPD_DET/HPD_CBUS`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 A7-D8，JP1、U3 LT8912B 与 J1 HDMI 全链路

## 电源

### VCC_5V 到 VCC_1V8 降压

U1 SY8003 的 IN 与 EN 接 VCC_5V，LX 经 L1 输出 VCC_1V8；R4 200KΩ/1% 与 R5 100KΩ/1% 构成 1V8_FB 分压，图中公式标明 Vout=0.6(1+R4/R5)=1.8V。

- 参数与网络：`input=VCC_5V`；`converter=U1 SY8003`；`enable=U1 EN=VCC_5V`；`inductor=L1 FTC25012S2R2MBCA`；`feedback=R4 200K/1%, R5 100K/1%`；`output=VCC_1V8`；`voltage=1.8V`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 A1-A3，POWER 1V8 完整转换路径与 Vout 公式

### LT8912B 三路 1.8V 电源域

VCC_1V8 分别经过 FB1、FB2、FB3 BLM15PX221SN1D，生成 1V8_VDD、1V8_VCCA、1V8_VCCA_HDMIPLL；C19-C30 对数字、模拟和 HDMI PLL 电源域去耦。

- 参数与网络：`source=VCC_1V8`；`digital=FB1 -> 1V8_VDD`；`analog=FB2 -> 1V8_VCCA`；`hdmi_pll=FB3 -> 1V8_VCCA_HDMIPLL`；`decoupling=C19-C30`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 A3 与 D3-D6，FB1-FB3、1V8_VDD/VCCA/VCCA_HDMIPLL、C19-C30

### HDMI 5V 供电路径

U2 MT9700-N 的 VIN 与 EN 接 VCC_5V，VOUT 输出 HDMI_5V；R12 13KΩ 接 SET，图中标注 Ilimit=6.8K/RL=523mA，C11/C12 为输入去耦，C9 为输出去耦。

- 参数与网络：`input=VCC_5V`；`switch=U2 MT9700-N`；`enable=EN=VCC_5V`；`output=HDMI_5V`；`set_resistor=R12 13K`；`annotated_limit=523mA`；`capacitors=C11/C12/C9 10uF/10V`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 B1-B3，POWER 5V 区 U2/R12/C11/C12/C9

### USB Type-A 5V 供电路径

U4 MT9700-N 的 VIN 与 EN 接 VCC_5V，VOUT 输出 USB_5V 到 USB1 pin1；R15 10KΩ 接 SET，图中标注 Ilimit=6.8K/RL=680mA。

- 参数与网络：`input=VCC_5V`；`switch=U4 MT9700-N`；`enable=EN=VCC_5V`；`output=USB_5V -> USB1 pin1 VCC`；`set_resistor=R15 10K`；`annotated_limit=680mA`；`capacitors=C13 10uF/10V,C14 22uF/10V`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 B1-B3，USB A 区 U4/R15/C13/C14/USB1

### 本页供电边界

本页从 JP2 VCC_5V 与 JP3/JP1 VCC_3V3 取电，显示 SY8003 降压与两个 MT9700-N 负载开关；页面未显示电池、充电器、升压、USB 供电协商或电源监测器。

- 参数与网络：`inputs=VCC_5V,VCC_3V3`；`buck=U1 SY8003`；`load_switches=U2/U4 MT9700-N`；`battery=null`；`charger=null`；`boost=null`；`power_monitor=null`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页 POWER 1V8、POWER 5V、INPUT 全部电源区域

## 接口

### JP1 24P FPC 针脚映射

JP1 pins1-6 未连接；pin7=TP_RST、pin8=TP_INT、pin9=SYS_SDA、pin10=SYS_SCL、pin11=MIPI_DSI_CK_N、pin12=MIPI_DSI_CK_P、pin13=GND、pin14=MIPI_DSI_D1_N、pin15=MIPI_DSI_D1_P、pin16=GND、pin17=MIPI_DSI_D0_N、pin18=MIPI_DSI_D0_P、pin19=GND、pin20=RESET_N、pin21=GND、pins22-24=VCC_3V3，SH 接 GND。

- 参数与网络：`connector=JP1 F-FPCOM24P-C310`；`pins1_6=NC`；`pin7=TP_RST`；`pin8=TP_INT`；`pin9=SYS_SDA`；`pin10=SYS_SCL`；`pin11_12=MIPI_DSI_CK_N/P`；`pin13=GND`；`pin14_15=MIPI_DSI_D1_N/P`；`pin16=GND`；`pin17_18=MIPI_DSI_D0_N/P`；`pin19=GND`；`pin20=RESET_N`；`pin21=GND`；`pins22_24=VCC_3V3`；`shield=GND`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 A7-A8，JP1 pins1-24 与 SH 逐针标注

### JP2 SDIO/USB/5V 输入针脚

JP2 pin1=SDIO_G13_CMD、pin2=SDIO_G12_CK、pin3=SDIO_G11_D3、pin4=SDIO_G10_D2、pin5=SDIO_G9_D1、pin6=SDIO_G8_D0、pin7=USB1_D_P、pin8=USB1_D_N、pin9=VCC_5V。

- 参数与网络：`connector=JP2 9-pin`；`pin1=SDIO_G13_CMD`；`pin2=SDIO_G12_CK`；`pin3=SDIO_G11_D3`；`pin4=SDIO_G10_D2`；`pin5=SDIO_G9_D1`；`pin6=SDIO_G8_D0`；`pin7=USB1_D_P`；`pin8=USB1_D_N`；`pin9=VCC_5V`；`usb_impedance_note=Z=90R`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 A6-A7，INPUT 区 JP2 pins1-9

### JP3 3.3V/GND 输入针脚

JP3 pin1 接 GND，pins2-5 未连接，pin6 接 VCC_3V3；C7 10uF/10V 从 VCC_3V3 接 GND。

- 参数与网络：`connector=JP3 6-pin`；`pin1=GND`；`pins2_5=NC`；`pin6=VCC_3V3`；`decoupling=C7 10uF/10V`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 A6-A7，JP3 pins1-6 与 C7

### JP4 触摸接口针脚

JP4 pin1=VCC_3V3、pin2=TP_RST、pin3=SYS_SCL、pin4=SYS_SDA、pin5 经 R23 0Ω 连接 TP_INT、pin6=GND，SH 接 GND；C31 10uF/10V 跨接 VCC_3V3 与 GND。

- 参数与网络：`connector=JP4 6-pin plus SH`；`pin1=VCC_3V3`；`pin2=TP_RST`；`pin3=SYS_SCL`；`pin4=SYS_SDA`；`pin5=R23 0R -> TP_INT`；`pin6=GND`；`shield=GND`；`decoupling=C31 10uF/10V`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 D1-D3，TOUCH 区 JP4/R23/C31

### USB Type-A 信号与方向

JP2 pins7/8 的 USB1_D_P/USB1_D_N 分别连接 USB1 pin3 D+ 与 pin2 D-，USB1 pin1 由 USB_5V 供电、pin4 接 GND；差分对标注 Z=90R，DR1/DR2 ESD351 分别从 D-/D+ 接 GND。

- 参数与网络：`upstream=JP2 pin7 USB1_D_P, pin8 USB1_D_N`；`connector=USB1 USB-AF-DIP-154-HW-S`；`pin1=USB_5V VCC`；`pin2=USB1_D_N D-`；`pin3=USB1_D_P D+`；`pin4=GND`；`direction=bidirectional USB data; power output at USB1 VCC`；`impedance_note=Z=90R`；`protection=DR1/DR2 ESD351`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 A6-A7 与 B1-B3，JP2 USB1_D_P/N 到 USB1、U4、DR1/DR2

### J1 HDMI 信号映射

J1 pin1 D2+=TX_D2_P、pin3 D2-=TX_D2_N、pin4 D1+=TX_D1_P、pin6 D1-=TX_D1_N、pin7 D0+=TX_D0_P、pin9 D0-=TX_D0_N、pin10 CLK+=TX_CK_P、pin12 CLK-=TX_CK_N、pin15 SCL=TX_SCL、pin16 SDA=TX_SDA、pin17 为 DDC/CEC GND、pin18=HDMI_5V、pin19 HOTPLUG 经 HPD_DET 路径；CEC 与 NC 未连接。

- 参数与网络：`connector=J1 HDMI-001 19PCBTP`；`data2=pins1/3 TX_D2_P/N`；`data1=pins4/6 TX_D1_P/N`；`data0=pins7/9 TX_D0_P/N`；`clock=pins10/12 TX_CK_P/N`；`ddc=pin15 TX_SCL,pin16 TX_SDA,pin17 GND`；`power=pin18 HDMI_5V`；`hotplug=pin19 HPD_DET`；`cec=NC`；`impedance_note=Z=100R`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 B7-C8，J1 HDMI pins1-19 与 TX_D*/TX_CK*/TX_SCL/TX_SDA/HPD_DET

## 总线

### MIPI DSI 两通道输入

JP1 的 MIPI_DSI_D0_P/N 连接 U3 MIPIRX0_DP/DN pins1/2，MIPI_DSI_D1_P/N 连接 MIPIRX1_DP/DN pins3/4，MIPI_DSI_CK_P/N 连接 MIPIRX_CKP/CKN pins7/8；图中对差分组标注 Z=100R。

- 参数与网络：`controller=external host through JP1`；`device=U3 LT8912B`；`lane0=MIPI_DSI_D0_P/N -> U3 pins1/2`；`lane1=MIPI_DSI_D1_P/N -> U3 pins3/4`；`clock=MIPI_DSI_CK_P/N -> U3 pins7/8`；`lanes=2`；`impedance_note=Z=100R`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 B3-C4，JP1 MIPI_DSI_* 到 U3 MIPIRX0/1/CK

### 3.3V/1.8V I2C 电平转换

SYS_SCL/SYS_SDA 位于 3.3V 侧并由 R3/R9 2KΩ 上拉至 VCC_3V3，经 Q2A/Q2B 2N7002DW 转换到 S_SCL/S_SDA；1.8V 侧由 R2/R8 2KΩ 上拉至 1V8_VCCA并连接 U3。JP1 与 JP4 共用 SYS_SCL/SYS_SDA。

- 参数与网络：`controller_side=SYS_SCL/SYS_SDA at VCC_3V3`；`device_side=S_SCL/S_SDA at 1V8_VCCA`；`translator=Q2A/Q2B 2N7002DW`；`pullups_3v3=R3/R9 2K`；`pullups_1v8=R2/R8 2K`；`connectors=JP1 pins10/9, JP4 pins3/4`；`device=U3 LT8912B`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 A5-A6 与 B4-B5，Q2A/Q2B、R2/R3/R8/R9、SYS_SCL/SDA、S_SCL/SDA、U3

### TF 卡 SDIO 偏置与防护

R24-R29 六个 10KΩ 电阻把 J2 的 SDIO_G8_D2、SDIO_G9_D3、SDIO_G10_CMD、SDIO_G11_CK、SDIO_G12_D0、SDIO_G13_D1 拉至 VCC_3V3；TVS1-TV7 对六条 SDIO 信号及 TF_DET 提供到 GND 的防护。

- 参数与网络：`pullups=R24-R29 10K to VCC_3V3`；`signals=SDIO_G8_D2,SDIO_G9_D3,SDIO_G10_CMD,SDIO_G11_CK,SDIO_G12_D0,SDIO_G13_D1`；`protection=TVS1-TV7 to GND`；`detect=TF_DET`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 C1-D3，R24-R29 与 TVS1-TV7

### HDMI DDC I2C 路径

U3 的 TX_SCL/TX_SDA 连接 J1 pins15/16，并分别由 R13/R14 2KΩ 经 D1/D2 接 HDMI_5V；D4 ESD0524P 对 TX_SCL、TX_SDA 与 HPD_DET 提供 ESD 防护。

- 参数与网络：`controller=U3 LT8912B`；`clock=TX_SCL -> J1 pin15`；`data=TX_SDA -> J1 pin16`；`pullups=R13/R14 2K through D1/D2 to HDMI_5V`；`protection=D4 ESD0524P`；`testpoints=TP7 TX_SCL,TP8 TX_SDA`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 B7-D8，TX_SCL/TX_SDA、R13/R14、D1/D2、D4、J1 pins15/16

## GPIO 与控制信号

### 触摸复位与中断网络

TP_RST 在 JP1 pin7 与 JP4 pin2 之间直接引出；TP_INT 在 JP1 pin8 与 JP4 pin5 之间引出，并经 Q1B 2N7002DW 转换为 1.8V 侧 INT，R6 10KΩ 上拉 INT 至 1V8_VCCA，R7 为未装的 3.3V 侧上拉。

- 参数与网络：`touch_reset=JP1 pin7 TP_RST <-> JP4 pin2`；`touch_interrupt=JP4 pin5 via R23 0R -> TP_INT -> JP1 pin8`；`translated_interrupt=TP_INT <-> Q1B <-> INT`；`pullup_1v8=R6 10K to 1V8_VCCA`；`pullup_3v3=R7 NC to VCC_3V3`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 A4-A5、A7-A8、D1-D3，Q1B/INT/TP_INT 与 JP1/JP4

## 时钟

### LT8912B 25MHz 晶体时钟

X1 标注 25M-12pF(X322525MOB4SI)，跨接 U3 XTALI/XTALO；R10 1MΩ 跨接晶体两端，C6 与 C8 各 12pF/50V 接 GND。

- 参数与网络：`device=U3 LT8912B`；`crystal=X1 25M-12pF(X322525MOB4SI)`；`frequency=25MHz`；`pins=XTALI/XTALO`；`feedback=R10 1M`；`load_caps=C6/C8 12pF/50V to GND`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 B5，U3 XTALI/XTALO、X1、R10、C6、C8

## 复位

### LT8912B 复位路径

JP1 pin20 的 RESET_N 经 Q1A 2N7002DW 转换为 RST_N；3.3V 侧 R1 标记 NC，RST_N 侧由 R11 100KΩ 上拉至 1V8_VCCA并由 C10 100nF/25V 接地形成 RC，TP4 引出 RST_N。

- 参数与网络：`external=JP1 pin20 RESET_N`；`translator=Q1A 2N7002DW`；`internal=RST_N`；`pullup_3v3=R1 NC`；`pullup_1v8=R11 100K to 1V8_VCCA`；`capacitor=C10 100nF/25V to GND`；`testpoint=TP4 RST_N`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 A4-A5、B3-B4、A7-A8，Q1A/R1/R11/C10/JP1 pin20/TP4

## 保护电路

### HDMI ESD 与机壳地

D3 ESD0524P 保护 TX_D2_P/N 与 TX_D1_P/N，D5 保护 TX_D0_P/N 与 TX_CK_P/N，D4 保护 TX_SCL、TX_SDA 与 HPD_DET；J1 屏蔽端接 HFGND，HFGND 通过并联的 R21 0Ω/5% 与 C18 1nF/2KV 连接 GND。

- 参数与网络：`tmds_upper=D3 ESD0524P`；`tmds_lower_clock=D5 ESD0524P`；`ddc_hpd=D4 ESD0524P`；`shield_ground=HFGND`；`bonding=R21 0R/5% parallel C18 1nF/2KV to GND`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 D7-D8，D3/D4/D5、J1 屏蔽、HFGND、R21/C18

## 关键网络

### HDMI 热插拔检测

J1 pin19 HOTPLUG 进入 HPD_DET，R16/R17 均为 100KΩ；Q3 MMBT3904TT1G 与 1V8_VCCA、R18 100KΩ 组成 HPD_CBUS 电平路径，HPD_CBUS 连接 U3，D4 同时保护 HPD_DET。

- 参数与网络：`connector=J1 pin19 HOTPLUG`；`external_net=HPD_DET`；`resistors=R16 100K,R17 100K`；`transistor=Q3 MMBT3904TT1G`；`internal_net=HPD_CBUS`；`internal_pull=R18 100K to GND`；`supply=1V8_VCCA`；`protection=D4 ESD0524P`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 C7-C8，J1 pin19、HPD_DET、R16/R17、Q3、HPD_CBUS、R18、U3

## 存储

### J2 TF 卡针脚与检测

J2 pin1 DATA2=SDIO_G8_D2、pin2 CD/DATA3=SDIO_G9_D3、pin3 CMD=SDIO_G10_CMD、pin4 VDD=VCC_3V3、pin5 CLK=SDIO_G11_CK、pin6 VSS=GND、pin7 DATA0=SDIO_G12_D0、pin8 DATA1=SDIO_G13_D1、pin9 K=TF_DET、pin10=GND；TF_DET 由 R20 100KΩ 上拉并由 C17 2nF/50V 滤波。

- 参数与网络：`connector=J2 TF_Card`；`pin1=SDIO_G8_D2`；`pin2=SDIO_G9_D3`；`pin3=SDIO_G10_CMD`；`pin4=VCC_3V3`；`pin5=SDIO_G11_CK`；`pin6=GND`；`pin7=SDIO_G12_D0`；`pin8=SDIO_G13_D1`；`pin9=TF_DET`；`pin10=GND`；`detect_pullup=R20 100K`；`detect_filter=C17 2nF/50V`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 C1-C3，J2 pins1-10、R20、C17、TF_DET

## 调试与烧录

### 电源与控制测试点

TP1=VCC_5V、TP2=VCC_1V8、TP3=GND、TP4=RST_N、TP5=SYS_SCL、TP6=SYS_SDA、TP7=TX_SCL、TP8=TX_SDA。

- 参数与网络：`TP1=VCC_5V`；`TP2=VCC_1V8`；`TP3=GND`；`TP4=RST_N`；`TP5=SYS_SCL`；`TP6=SYS_SDA`；`TP7=TX_SCL`；`TP8=TX_SDA`
- 证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 D3-D4，TP1-TP8 网络标注

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 显示输出系统架构 | `bridge=U3 LT8912B`；`input=2-lane MIPI DSI`；`output=HDMI TMDS D0/D1/D2/CLK`；`control=S_SCL/S_SDA, RST_N`；`ddc=TX_SCL/TX_SDA`；`hotplug=HPD_DET/HPD_CBUS` |
| 电源 | VCC_5V 到 VCC_1V8 降压 | `input=VCC_5V`；`converter=U1 SY8003`；`enable=U1 EN=VCC_5V`；`inductor=L1 FTC25012S2R2MBCA`；`feedback=R4 200K/1%, R5 100K/1%`；`output=VCC_1V8`；`voltage=1.8V` |
| 电源 | LT8912B 三路 1.8V 电源域 | `source=VCC_1V8`；`digital=FB1 -> 1V8_VDD`；`analog=FB2 -> 1V8_VCCA`；`hdmi_pll=FB3 -> 1V8_VCCA_HDMIPLL`；`decoupling=C19-C30` |
| 电源 | HDMI 5V 供电路径 | `input=VCC_5V`；`switch=U2 MT9700-N`；`enable=EN=VCC_5V`；`output=HDMI_5V`；`set_resistor=R12 13K`；`annotated_limit=523mA`；`capacitors=C11/C12/C9 10uF/10V` |
| 电源 | USB Type-A 5V 供电路径 | `input=VCC_5V`；`switch=U4 MT9700-N`；`enable=EN=VCC_5V`；`output=USB_5V -> USB1 pin1 VCC`；`set_resistor=R15 10K`；`annotated_limit=680mA`；`capacitors=C13 10uF/10V,C14 22uF/10V` |
| 接口 | JP1 24P FPC 针脚映射 | `connector=JP1 F-FPCOM24P-C310`；`pins1_6=NC`；`pin7=TP_RST`；`pin8=TP_INT`；`pin9=SYS_SDA`；`pin10=SYS_SCL`；`pin11_12=MIPI_DSI_CK_N/P`；`pin13=GND`；`pin14_15=MIPI_DSI_D1_N/P`；`pin16=GND`；`pin17_18=MIPI_DSI_D0_N/P`；`pin19=GND`；`pin20=RESET_N`；`pin21=GND`；`pins22_24=VCC_3V3`；`shield=GND` |
| 接口 | JP2 SDIO/USB/5V 输入针脚 | `connector=JP2 9-pin`；`pin1=SDIO_G13_CMD`；`pin2=SDIO_G12_CK`；`pin3=SDIO_G11_D3`；`pin4=SDIO_G10_D2`；`pin5=SDIO_G9_D1`；`pin6=SDIO_G8_D0`；`pin7=USB1_D_P`；`pin8=USB1_D_N`；`pin9=VCC_5V`；`usb_impedance_note=Z=90R` |
| 接口 | JP3 3.3V/GND 输入针脚 | `connector=JP3 6-pin`；`pin1=GND`；`pins2_5=NC`；`pin6=VCC_3V3`；`decoupling=C7 10uF/10V` |
| 接口 | JP4 触摸接口针脚 | `connector=JP4 6-pin plus SH`；`pin1=VCC_3V3`；`pin2=TP_RST`；`pin3=SYS_SCL`；`pin4=SYS_SDA`；`pin5=R23 0R -> TP_INT`；`pin6=GND`；`shield=GND`；`decoupling=C31 10uF/10V` |
| 总线 | MIPI DSI 两通道输入 | `controller=external host through JP1`；`device=U3 LT8912B`；`lane0=MIPI_DSI_D0_P/N -> U3 pins1/2`；`lane1=MIPI_DSI_D1_P/N -> U3 pins3/4`；`clock=MIPI_DSI_CK_P/N -> U3 pins7/8`；`lanes=2`；`impedance_note=Z=100R` |
| 总线 | 3.3V/1.8V I2C 电平转换 | `controller_side=SYS_SCL/SYS_SDA at VCC_3V3`；`device_side=S_SCL/S_SDA at 1V8_VCCA`；`translator=Q2A/Q2B 2N7002DW`；`pullups_3v3=R3/R9 2K`；`pullups_1v8=R2/R8 2K`；`connectors=JP1 pins10/9, JP4 pins3/4`；`device=U3 LT8912B` |
| GPIO 与控制信号 | 触摸复位与中断网络 | `touch_reset=JP1 pin7 TP_RST <-> JP4 pin2`；`touch_interrupt=JP4 pin5 via R23 0R -> TP_INT -> JP1 pin8`；`translated_interrupt=TP_INT <-> Q1B <-> INT`；`pullup_1v8=R6 10K to 1V8_VCCA`；`pullup_3v3=R7 NC to VCC_3V3` |
| 复位 | LT8912B 复位路径 | `external=JP1 pin20 RESET_N`；`translator=Q1A 2N7002DW`；`internal=RST_N`；`pullup_3v3=R1 NC`；`pullup_1v8=R11 100K to 1V8_VCCA`；`capacitor=C10 100nF/25V to GND`；`testpoint=TP4 RST_N` |
| 存储 | J2 TF 卡针脚与检测 | `connector=J2 TF_Card`；`pin1=SDIO_G8_D2`；`pin2=SDIO_G9_D3`；`pin3=SDIO_G10_CMD`；`pin4=VCC_3V3`；`pin5=SDIO_G11_CK`；`pin6=GND`；`pin7=SDIO_G12_D0`；`pin8=SDIO_G13_D1`；`pin9=TF_DET`；`pin10=GND`；`detect_pullup=R20 100K`；`detect_filter=C17 2nF/50V` |
| 总线 | TF 卡 SDIO 偏置与防护 | `pullups=R24-R29 10K to VCC_3V3`；`signals=SDIO_G8_D2,SDIO_G9_D3,SDIO_G10_CMD,SDIO_G11_CK,SDIO_G12_D0,SDIO_G13_D1`；`protection=TVS1-TV7 to GND`；`detect=TF_DET` |
| 接口 | USB Type-A 信号与方向 | `upstream=JP2 pin7 USB1_D_P, pin8 USB1_D_N`；`connector=USB1 USB-AF-DIP-154-HW-S`；`pin1=USB_5V VCC`；`pin2=USB1_D_N D-`；`pin3=USB1_D_P D+`；`pin4=GND`；`direction=bidirectional USB data; power output at USB1 VCC`；`impedance_note=Z=90R`；`protection=DR1/DR2 ESD351` |
| 接口 | J1 HDMI 信号映射 | `connector=J1 HDMI-001 19PCBTP`；`data2=pins1/3 TX_D2_P/N`；`data1=pins4/6 TX_D1_P/N`；`data0=pins7/9 TX_D0_P/N`；`clock=pins10/12 TX_CK_P/N`；`ddc=pin15 TX_SCL,pin16 TX_SDA,pin17 GND`；`power=pin18 HDMI_5V`；`hotplug=pin19 HPD_DET`；`cec=NC`；`impedance_note=Z=100R` |
| 总线 | HDMI DDC I2C 路径 | `controller=U3 LT8912B`；`clock=TX_SCL -> J1 pin15`；`data=TX_SDA -> J1 pin16`；`pullups=R13/R14 2K through D1/D2 to HDMI_5V`；`protection=D4 ESD0524P`；`testpoints=TP7 TX_SCL,TP8 TX_SDA` |
| 关键网络 | HDMI 热插拔检测 | `connector=J1 pin19 HOTPLUG`；`external_net=HPD_DET`；`resistors=R16 100K,R17 100K`；`transistor=Q3 MMBT3904TT1G`；`internal_net=HPD_CBUS`；`internal_pull=R18 100K to GND`；`supply=1V8_VCCA`；`protection=D4 ESD0524P` |
| 时钟 | LT8912B 25MHz 晶体时钟 | `device=U3 LT8912B`；`crystal=X1 25M-12pF(X322525MOB4SI)`；`frequency=25MHz`；`pins=XTALI/XTALO`；`feedback=R10 1M`；`load_caps=C6/C8 12pF/50V to GND` |
| 保护电路 | HDMI ESD 与机壳地 | `tmds_upper=D3 ESD0524P`；`tmds_lower_clock=D5 ESD0524P`；`ddc_hpd=D4 ESD0524P`；`shield_ground=HFGND`；`bonding=R21 0R/5% parallel C18 1nF/2KV to GND` |
| 调试与烧录 | 电源与控制测试点 | `TP1=VCC_5V`；`TP2=VCC_1V8`；`TP3=GND`；`TP4=RST_N`；`TP5=SYS_SCL`；`TP6=SYS_SDA`；`TP7=TX_SCL`；`TP8=TX_SDA` |
| 电源 | 本页供电边界 | `inputs=VCC_5V,VCC_3V3`；`buck=U1 SY8003`；`load_switches=U2/U4 MT9700-N`；`battery=null`；`charger=null`；`boost=null`；`power_monitor=null` |
| 系统结构 | 本地资源页范围 | `local_pages=1`；`title_block_sheet=2/2`；`revision=V0.2`；`date=3/19/2026`；`missing_sheet=1/2`；`complete_architecture=null` |
| 总线 | JP2 与 J2 的 SDIO 网络映射 | `jp2=G13_CMD,G12_CK,G11_D3,G10_D2,G9_D1,G8_D0`；`j2=G10_CMD,G11_CK,G9_D3,G8_D2,G13_D1,G12_D0`；`direct_name_match=false`；`cross_page_mapping=null`；`controller=null` |
| 总线地址 | LT8912B 与外部触摸 I2C 地址 | `lt8912_bus=S_SCL/S_SDA`；`lt8912_address=null`；`address_strap=null`；`touch_bus=SYS_SCL/SYS_SDA`；`touch_controller=null`；`touch_address=null` |
| 其他事实 | 正文 HDMI 输出分辨率 | `documented_mode_1=1280x720@60Hz`；`documented_mode_2=1920x1080@30Hz`；`schematic_timing=null`；`pixel_clock=null`；`register_configuration=null` |

## 待确认事项

- `system.local-sheet-scope`：资源清单仅包含一张本地页面，而该页面图框标记 Sheet 2/2、Revision V0.2、日期 3/19/2026；因此本页可确认 LT8912B、接口和电源电路，但不能据此排除第 1 页存在其他器件、配置或跨页连接。（证据：图 907de836daf1 / 第 1 页 / 第 1 页右下图框 UnitPoEP4_DSI_TO_HDMI，Number 2/2，Revision V0.2）
- `bus.sdio-cross-page-mapping`：本页 JP2 使用 SDIO_G13_CMD/G12_CK/G11_D3/G10_D2/G9_D1/G8_D0，而 J2 TF 卡使用 SDIO_G10_CMD/G11_CK/G9_D3/G8_D2/G13_D1/G12_D0；两组网络名不逐项相同，本页未显示它们之间的直接连接或重映射器件。（证据：图 907de836daf1 / 第 1 页 / 第 1 页网格 A6-A7 的 JP2 SDIO 标签与网格 C1-C3 的 J2 TF 卡 SDIO 标签对照）
- `address.lt8912-and-touch`：原理图显示 S_SCL/S_SDA 连接 LT8912B，SYS_SCL/SYS_SDA 同时引到 JP1/JP4，但本页未标 LT8912B I2C 地址、地址选择脚状态、外部触摸控制器型号或触摸地址。（证据：图 907de836daf1 / 第 1 页 / 第 1 页 Q2A/Q2B、U3 S_SCL/S_SDA 与 JP1/JP4 SYS_SCL/SYS_SDA，无地址标注）
- `other.documented-video-modes`：产品正文列出 1280x720@60Hz 与 1920x1080@30Hz；本页原理图只显示 LT8912B、时钟和信号连接，没有像素时钟、MIPI 时序、PLL 配置、寄存器初始化或视频模式表。（证据：图 907de836daf1 / 第 1 页 / 第 1 页 U3 LT8912B、X1 与 HDMI 区，无分辨率或视频时序文字）
- `review.missing-sheet-one`：请补充并核对正式原理图第 1/2 页或完整网表，确认是否还有主控、配置存储、跨页网络、保护和电源器件。；原因：本地资源只有一页，图框明确标记为 2/2。
- `review.sdio-mapping`：请用第 1 页、网表或 PCB 连通性确认 JP2 六条 SDIO 网络如何连接 J2 TF 卡，以及 G8-G13 后缀与 CMD/CK/D0-D3 的最终对应关系。；原因：JP2 与 J2 所示完整网络名不逐项匹配，本页没有可见重映射路径。
- `review.i2c-addresses`：请由 LT8912B datasheet、配置页和目标触摸模组确认 I2C 地址、地址选择、总线速率、电平兼容及是否存在地址冲突。；原因：本页只显示 I2C 网络和电平转换，未显示地址或外部触摸控制器型号。
- `review.video-modes`：请用 LT8912B 初始化配置、MIPI 输入时序和实机显示测试确认 720p60 与 1080p30 模式及其限制。；原因：原理图未给出分辨率、像素时钟或寄存器配置。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `907de836daf1a0850e151f1b08cc83d2de27aba9d54d23d606dbc28749d729c7` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1253/SCH_Unit_PoE-P4_Display_OUT_V0.2_SCH_PDF_20260319_2026_03_19_16_32_08_page_01.png` |

---

源文档：`zh_CN/addon/AddOn_Display_Out_For_PoE-P4.md`

源文档 SHA-256：`4693c97ef76bf66b5107c1b3d9043bea8a645bc07abab70440ae88b18daf593f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
