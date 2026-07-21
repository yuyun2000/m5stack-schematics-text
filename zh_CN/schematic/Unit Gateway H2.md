# Unit Gateway H2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Gateway H2 |
| SKU | U195 |
| 产品 ID | `unit-gateway-h2-3d4f3f01cf7e` |
| 源文档 | `zh_CN/unit/Unit Gateway H2.md` |

## 概述

Unit Gateway H2 以 M1 ESP32-H2-MINI-1 为主控与板载天线无线模组，通过 J2 HY-2.0_UART 的 H2-TX0/H2-RX0 与外部主机通信，并提供 J3 USB Type-C 和 J1 六针下载接口。J2 的 VCC 与 Type-C VBUS/D8 汇入 VCC，经过 F1 形成 +5V，再由 U1 BL8075CB5TR33 生成 +3.3V 为模组供电。板上还包含 H2-G9 低有效按键、H2-EN RC、32.768 kHz 晶振、UART/USB/电源 ESD 以及 GPIO 测试引出；N2/2MB、无线协议版本和性能参数未直接印在原理图上。

## 检索关键词

`Unit Gateway H2`、`U195`、`ESP32-H2-MINI-1`、`ESP32-H2`、`BL8075CB5TR33`、`HY-2.0_UART`、`Grove Port C`、`USB Type-C`、`USB_D_P`、`USB_D_N`、`H2-TX0`、`H2-RX0`、`H2-EN`、`H2-G9`、`H2-G0`、`H2-G1`、`H2-G2`、`H2-G3`、`H2-G4`、`H2-G5`、`H2-G12`、`G22`、`G25`、`DownloadSocket`、`32.768KHz`、`OSCI`、`OSCO`、`+3.3V`、`+5V`、`VCC`、`B5819W SL`、`F1 6V@1A`、`ESD5Z3V3`、`RLSD52A031V`、`LESD3Z5.0CMT1G`、`UART`、`IEEE 802.15.4`、`Zigbee`、`Thread`、`Matter`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | ESP32-H2-MINI-1 | 主控与无线模组，提供 UART0、USB D+/D-、GPIO、EN、32.768 kHz 时钟端和板载天线 | 图 b8b19d02862f / 第 1 页 / 第1页网格 A2-B2，M1 ESP32-H2-MINI-1 pins1-36 与天线图形 |
| U1 | BL8075CB5TR33 | 将 +5V 稳压为 +3.3V 的五脚 LDO，EN 与 VIN 接输入电源 | 图 b8b19d02862f / 第 1 页 / 第1页网格 D1-D2，U1 BL8075CB5TR33 pins1-5、+5V、+3.3V |
| J2 | HY-2.0_UART | 四针 Grove UART 与供电接口，引出 RX、TX、VCC、GND | 图 b8b19d02862f / 第 1 页 / 第1页网格 D3，J2 HY-2.0_UART pins1-4 |
| J3 | USB_TYPEC | USB Type-C 设备接口，提供 VBUS、并联 D+/D-、CC1/CC2 下拉、GND 与屏蔽连接 | 图 b8b19d02862f / 第 1 页 / 第1页网格 B3-B4，J3 USB_TYPEC A5/B5/A6/B6/A7/B7/VCC/GND/SHELL |
| J1 | DownloadSocket | 六针下载调试接口，引出 3.3V、UART、EN、启动网络与 GND | 图 b8b19d02862f / 第 1 页 / 第1页网格 D4，J1 DownloadSocket pins1-6 |
| S1 | SMT_SW_PTS_820 | 将 H2-G9 按下接地的启动/用户按键 | 图 b8b19d02862f / 第 1 页 / 第1页网格 A4，S1 SMT_SW_PTS_820、H2-G9、GND |
| Y1/C6/C7/R6 | 32.768KHz ±20ppm 12.5pF / 6.0pF / 6.0pF / 5.1MΩ/NC | M1 OSCI/OSCO 的 32.768 kHz 晶振、负载电容及未装反馈电阻网络 | 图 b8b19d02862f / 第 1 页 / 第1页网格 B1-B2，OSCI/OSCO、Y1、C6/C7、R6 |
| F1 | 6V@1A | 串接 VCC 与 +5V 电源域的保险/限流器件 | 图 b8b19d02862f / 第 1 页 / 第1页网格 D2-D3，F1 6V@1A 位于 +5V 与 VCC 之间 |
| D8 | B5819W SL | 串接 USB Type-C VBUS 与板上 VCC 网络的肖特基二极管 | 图 b8b19d02862f / 第 1 页 / 第1页网格 B3，D8 B5819W SL、VCC 与 J3 VCC |
| D1/D2（USB区） | RLSD52A031V | USB_D_P 与 USB_D_N 到 GND 的双路 ESD/瞬态保护 | 图 b8b19d02862f / 第 1 页 / 第1页网格 B4，USB_D_P/USB_D_N 两侧 D1/D2 RLSD52A031V |
| D3/D4/D5/D6/D7 | RLSD52A031V / LESD3Z5.0CMT1G / RLSD52A031V / RLSD52A031V / ESD5Z3V3 | +3.3V、VCC、两路 UART 与 H2-G9 的对地 ESD/瞬态保护器件 | 图 b8b19d02862f / 第 1 页 / 第1页网格 A4、D1、D3：D3-D7 及各自 +3.3V/VCC/H2-RX0/H2-TX0/H2-G9 网络 |
| R1/C4 | 10KΩ / 1.0uF | H2-EN 的 3.3V 上拉与对地 RC 网络 | 图 b8b19d02862f / 第 1 页 / 第1页网格 A1-B1，R1 10KΩ、C4 1.0uF、H2-EN、M1 EN pin8 |
| R2/R3/R7 | 10KΩ / 10KΩ / 0Ω | M1 GPIO8/GPIO9 上拉及 VBAT 到 3.3V 的连接电阻 | 图 b8b19d02862f / 第 1 页 / 第1页网格 B1-B2，M1 底边 R2/R3 10KΩ 与 R7 0Ω |
| JP1/JP2 | 未标注 | 分别引出 USB_D_P/USB_D_N 与 G25/G22 的两组未标型号连接点 | 图 b8b19d02862f / 第 1 页 / 第1页网格 B2，JP1 邻近 USB_D_P/USB_D_N，JP2 邻近 G25/G22 |
| D1/D2/R4/R5（灰显LED区） | 0603 / 1KΩ | 灰显的 G25/G22 到 +3.3V 指示灯支路，位号与 USB 区器件重复，装配状态待确认 | 图 b8b19d02862f / 第 1 页 / 第1页网格 B2-B3，灰显方框内 G25/G22、D1/D2 0603、R4/R5 1KΩ |

## 系统结构

### Unit Gateway H2 系统架构

M1 ESP32-H2-MINI-1 是单页原理图中的主控与无线模组，连接 Grove UART、原生 USB-C、六针下载座、H2-G9 按键、32.768 kHz 晶振及 GPIO 引出；U1 从 +5V 生成 +3.3V。

- 参数与网络：`controller=M1 ESP32-H2-MINI-1`；`host_interface=J2 HY-2.0_UART`；`usb=J3 USB_TYPEC`；`download=J1 DownloadSocket`；`regulator=U1 BL8075CB5TR33`；`clock=Y1 32.768KHz`；`button=S1 H2-G9`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页整页，M1/U1/J1/J2/J3/S1/Y1 功能分区

## 核心器件

### M1 模组标识

原理图将 M1 标为 ESP32-H2-MINI-1，列出 36 个模组引脚并在符号内部画出天线图形；页面没有在型号后标 N2。

- 参数与网络：`reference=M1`；`schematic_part_number=ESP32-H2-MINI-1`；`pins=36`；`antenna_symbol=shown`；`n2_suffix=not shown`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 A2-B2，M1 标题、pins1-36 与天线图形

## 电源

### VCC 与 +5V 输入路径

J2 pin3 接 VCC；J3 Type-C 的 VCC 端经 D8 B5819W SL 连接 VCC；VCC 再经 F1 6V@1A 串接到 +5V，C11 100nF 从 VCC 对地。

- 参数与网络：`grove=J2 pin3 VCC`；`usb=J3 VCC through D8 B5819W SL`；`common_rail=VCC`；`series_protection=F1 6V@1A`；`internal_rail=+5V`；`vcc_cap=C11 100nF`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B3-D3，J3 VCC/D8/VCC/J2 pin3/F1/+5V/C11

### U1 3.3V 稳压

U1 BL8075CB5TR33 的 VIN pin1 与 EN pin3 接 +5V，GND pin2 接地，NC pin4 未连接，VOUT pin5 输出 +3.3V。

- 参数与网络：`regulator=U1 BL8075CB5TR33`；`vin_pin=1 / +5V`；`enable_pin=3 / +5V`；`ground_pin=2 / GND`；`nc_pin=4`；`vout_pin=5 / +3.3V`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 D1-D2，U1 pins1-5 与 +5V/+3.3V

### U1 输入输出电容

U1 输入侧 +5V 配置 C10 1.0uF 与 C12 22uF 对地；输出侧 +3.3V 配置 C8 22uF、C5 1.0uF 和 C9 100nF 对地。

- 参数与网络：`input_rail=+5V`；`input_caps=C10 1.0uF; C12 22uF`；`output_rail=+3.3V`；`output_caps=C8 22uF; C5 1.0uF; C9 100nF`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 D1-D2，U1 周围 C5/C8/C9/C10/C12

### M1 3.3V 去耦

M1 pin3 的 +3.3V 输入配置 C1 22uF、C2 22uF 与 C3 100nF 对地。

- 参数与网络：`load=M1 pin3 3V3`；`rail=+3.3V`；`capacitors=C1 22uF; C2 22uF; C3 100nF`；`ground=GND`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 A1-A2，+3.3V/C1/C2/C3/M1 pin3

### M1 VBAT 连接

M1 VBAT pin15 通过 R7 0Ω 接 +3.3V，页面未画独立电池、充电器或电池监测链路。

- 参数与网络：`target=M1 VBAT pin15`；`series=R7 0Ω`；`source=+3.3V`；`battery=not shown`；`charger=not shown`；`monitor=not shown`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B1-B2，M1 VBAT pin15、R7 0Ω、+3.3V

## 接口

### J2 Grove UART 针脚

J2 HY-2.0_UART pin1 标 RX 并接 H2-TX0，pin2 标 TX 并接 H2-RX0，pin3 接 VCC，pin4 接 GND。

- 参数与网络：`connector=J2 HY-2.0_UART`；`pin1=RX / H2-TX0 / module-to-host`；`pin2=TX / H2-RX0 / host-to-module`；`pin3=VCC`；`pin4=GND`；`logic_rail=+3.3V`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 D3，J2 pins1-4 与 H2-TX0/H2-RX0/VCC/GND

### J3 USB Type-C 信号

J3 的 DP1 A6 与 DP2 B6 并接 USB_D_P，DN1 A7 与 DN2 B7 并接 USB_D_N；CC1 A5 和 CC2 B5 分别经 R4/R5 5.1KΩ 下拉到 GND，GND2 与 SHELL 接地。

- 参数与网络：`connector=J3 USB_TYPEC`；`dp=A6/B6 -> USB_D_P`；`dn=A7/B7 -> USB_D_N`；`cc1=A5 -> R4 5.1KΩ -> GND`；`cc2=B5 -> R5 5.1KΩ -> GND`；`ground=GND2 and SHELL -> GND`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B3-B4，J3 A5/B5/A6/B6/A7/B7、R4/R5 与 GND

### JP1/JP2 引出点

JP1 位于 USB_D_P/USB_D_N 两线引出端，JP2 位于 G25/G22 两线引出端；页面未标两者的连接器型号、针脚编号或装配属性。

- 参数与网络：`jp1_nets=USB_D_P; USB_D_N`；`jp2_nets=G25; G22`；`part_number=null`；`pin_numbers=not shown`；`population=not shown`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B2，JP1/JP2 与邻接的两组网络

## 总线

### M1 UART0 路由

M1 TX0 pin31 的 H2-TX0 同时连接 J2 RX pin1 与 J1 TXD pin2；M1 RX0 pin30 的 H2-RX0 同时连接 J2 TX pin2 与 J1 RXD pin3。

- 参数与网络：`controller_tx=M1 TX0 pin31 / H2-TX0`；`tx_destinations=J2 pin1 RX; J1 pin2 TXD`；`controller_rx=M1 RX0 pin30 / H2-RX0`；`rx_sources=J2 pin2 TX; J1 pin3 RXD`；`bus=UART0`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B2、D3-D4，M1 TX0/RX0、J2、J1 同名网络

### M1 原生 USB 数据路由

M1 IO27 pin27 直接接 USB_D_P，IO26 pin26 直接接 USB_D_N，两网络连接 J3 并由 JP1 一组连接点引出；页面未画 USB-UART 桥接 IC。

- 参数与网络：`controller_dp=M1 IO27 pin27`；`controller_dn=M1 IO26 pin26`；`nets=USB_D_P; USB_D_N`；`connector=J3 USB_TYPEC`；`breakout=JP1`；`usb_uart_bridge=not shown`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B2-B4，M1 IO27/IO26、USB_D_P/USB_D_N、JP1、J3

## GPIO 与控制信号

### H2-G9 按键与启动网络

H2-G9 连接 M1 GPIO9、S1 与 J1 pin5；R3 10KΩ 上拉至 +3.3V，按下 S1 将网络接 GND，D7 ESD5Z3V3 从该网络对地。

- 参数与网络：`net=H2-G9`；`module_gpio=GPIO9`；`pullup=R3 10KΩ to +3.3V`；`button=S1 to GND`；`download=J1 pin5 labeled G0`；`protection=D7 ESD5Z3V3 to GND`；`active_level=low`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 A4、B2、D4，H2-G9/R3/S1/D7/J1 pin5

### M1 底边上拉与 VBAT 电阻

R2 10KΩ 将 M1 GPIO8 上拉到 +3.3V，R3 10KΩ 将 H2-G9 上拉到 +3.3V；R7 0Ω 将 VBAT 接 +3.3V。

- 参数与网络：`gpio8=R2 10KΩ to +3.3V`；`gpio9=R3 10KΩ to +3.3V`；`vbat=R7 0Ω to +3.3V`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B1-B2，M1 底边 R2/R3/R7 与 +3.3V

### M1 命名 GPIO 网络

原理图从 M1 明确标出 H2-G2、H2-G3、H2-G0、H2-G1、H2-G12、H2-G4、H2-G5、H2-G9、G22 与 G25；JP2 位于 G25/G22 引出端。

- 参数与网络：`left_nets=H2-G2; H2-G3; H2-G0; H2-G1`；`bottom_nets=H2-G12; H2-G4; H2-G5; H2-G9; G22`；`right_net=G25`；`breakout=JP2 for G25/G22`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 A2-B3，M1 周边命名网络与 JP2

## 时钟

### 32.768 kHz 外部晶振

Y1 标为 32.768KHz ±20ppm、12.5pF，跨接 OSCI/OSCO；C6、C7 各 6.0pF 从两端对地，R6 5.1MΩ/NC 跨接两端，OSCI/OSCO 接 M1 底边时钟端。

- 参数与网络：`crystal=Y1 32.768KHz ±20ppm 12.5pF`；`nets=OSCI; OSCO`；`load_caps=C6 6.0pF; C7 6.0pF`；`feedback=R6 5.1MΩ / NC`；`population=Y1/C6/C7 not marked NC`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B1-B2，Y1/C6/C7/R6/OSCI/OSCO

## 复位

### H2-EN 使能/复位网络

M1 EN pin8 接 H2-EN，R1 10KΩ 将 H2-EN 上拉到 +3.3V，C4 1.0uF 从 H2-EN 对地；同一网络引到 J1 pin4 EN。

- 参数与网络：`target=M1 EN pin8`；`net=H2-EN`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C4 1.0uF to GND`；`external_control=J1 pin4 EN`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 A1-B2 与 D4，R1/C4/M1 EN/J1 EN

## 保护电路

### USB 数据线保护

USB 区 D1 RLSD52A031V 从 USB_D_P 对地，D2 RLSD52A031V 从 USB_D_N 对地。

- 参数与网络：`dp_protection=D1 RLSD52A031V to GND`；`dn_protection=D2 RLSD52A031V to GND`；`protected_nets=USB_D_P; USB_D_N`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B4，USB_D_P/D1 与 USB_D_N/D2

### 电源、UART 与按键保护

D3 RLSD52A031V 保护 +3.3V，D4 LESD3Z5.0CMT1G 保护 VCC，D5/D6 RLSD52A031V 分别保护 H2-RX0/H2-TX0，D7 ESD5Z3V3 保护 H2-G9，器件另一端均接 GND。

- 参数与网络：`three_v_three=D3 RLSD52A031V`；`vcc=D4 LESD3Z5.0CMT1G`；`uart_rx=D5 RLSD52A031V`；`uart_tx=D6 RLSD52A031V`；`button=D7 ESD5Z3V3`；`return=GND`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 A4、D1、D3，D3-D7 与各保护网络

## 存储

### 外部存储器

该原理图页未画独立 Flash、PSRAM、EEPROM、SD 卡或其他外部存储器位号；存储若存在则位于 M1 模组内部。

- 参数与网络：`external_flash=not shown`；`psram=not shown`；`eeprom=not shown`；`sd=not shown`；`module=M1 ESP32-H2-MINI-1`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页完整单页器件清单与 M1 模组边界

## 射频

### 板载天线边界

M1 符号内画有集成天线，页面未从 M1 引出独立 RF 网络，也未画外置天线连接器或匹配网络。

- 参数与网络：`module=M1 ESP32-H2-MINI-1`；`antenna=integrated symbol`；`external_rf_net=not shown`；`external_connector=not shown`；`matching_network=not shown`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 A2，M1 内部天线图形与全部外围连接

## 调试与烧录

### J1 下载接口

J1 pin1 为 +3.3V，pin2 TXD 接 H2-TX0，pin3 RXD 接 H2-RX0，pin4 EN 接 H2-EN，pin5 标 G0 但连接 H2-G9，pin6 接 GND。

- 参数与网络：`connector=J1 DownloadSocket`；`pin1=+3.3V`；`pin2=TXD / H2-TX0`；`pin3=RXD / H2-RX0`；`pin4=EN / H2-EN`；`pin5=G0 label / H2-G9 net`；`pin6=GND`
- 证据：图 b8b19d02862f / 第 1 页 / 第1页网格 D4，J1 pins1-6 及左侧网络名

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Gateway H2 系统架构 | `controller=M1 ESP32-H2-MINI-1`；`host_interface=J2 HY-2.0_UART`；`usb=J3 USB_TYPEC`；`download=J1 DownloadSocket`；`regulator=U1 BL8075CB5TR33`；`clock=Y1 32.768KHz`；`button=S1 H2-G9` |
| 核心器件 | M1 模组标识 | `reference=M1`；`schematic_part_number=ESP32-H2-MINI-1`；`pins=36`；`antenna_symbol=shown`；`n2_suffix=not shown` |
| 射频 | 板载天线边界 | `module=M1 ESP32-H2-MINI-1`；`antenna=integrated symbol`；`external_rf_net=not shown`；`external_connector=not shown`；`matching_network=not shown` |
| 电源 | VCC 与 +5V 输入路径 | `grove=J2 pin3 VCC`；`usb=J3 VCC through D8 B5819W SL`；`common_rail=VCC`；`series_protection=F1 6V@1A`；`internal_rail=+5V`；`vcc_cap=C11 100nF` |
| 电源 | U1 3.3V 稳压 | `regulator=U1 BL8075CB5TR33`；`vin_pin=1 / +5V`；`enable_pin=3 / +5V`；`ground_pin=2 / GND`；`nc_pin=4`；`vout_pin=5 / +3.3V` |
| 电源 | U1 输入输出电容 | `input_rail=+5V`；`input_caps=C10 1.0uF; C12 22uF`；`output_rail=+3.3V`；`output_caps=C8 22uF; C5 1.0uF; C9 100nF` |
| 电源 | M1 3.3V 去耦 | `load=M1 pin3 3V3`；`rail=+3.3V`；`capacitors=C1 22uF; C2 22uF; C3 100nF`；`ground=GND` |
| 电源 | M1 VBAT 连接 | `target=M1 VBAT pin15`；`series=R7 0Ω`；`source=+3.3V`；`battery=not shown`；`charger=not shown`；`monitor=not shown` |
| 接口 | J2 Grove UART 针脚 | `connector=J2 HY-2.0_UART`；`pin1=RX / H2-TX0 / module-to-host`；`pin2=TX / H2-RX0 / host-to-module`；`pin3=VCC`；`pin4=GND`；`logic_rail=+3.3V` |
| 总线 | M1 UART0 路由 | `controller_tx=M1 TX0 pin31 / H2-TX0`；`tx_destinations=J2 pin1 RX; J1 pin2 TXD`；`controller_rx=M1 RX0 pin30 / H2-RX0`；`rx_sources=J2 pin2 TX; J1 pin3 RXD`；`bus=UART0` |
| 接口 | J3 USB Type-C 信号 | `connector=J3 USB_TYPEC`；`dp=A6/B6 -> USB_D_P`；`dn=A7/B7 -> USB_D_N`；`cc1=A5 -> R4 5.1KΩ -> GND`；`cc2=B5 -> R5 5.1KΩ -> GND`；`ground=GND2 and SHELL -> GND` |
| 总线 | M1 原生 USB 数据路由 | `controller_dp=M1 IO27 pin27`；`controller_dn=M1 IO26 pin26`；`nets=USB_D_P; USB_D_N`；`connector=J3 USB_TYPEC`；`breakout=JP1`；`usb_uart_bridge=not shown` |
| 保护电路 | USB 数据线保护 | `dp_protection=D1 RLSD52A031V to GND`；`dn_protection=D2 RLSD52A031V to GND`；`protected_nets=USB_D_P; USB_D_N` |
| 调试与烧录 | J1 下载接口 | `connector=J1 DownloadSocket`；`pin1=+3.3V`；`pin2=TXD / H2-TX0`；`pin3=RXD / H2-RX0`；`pin4=EN / H2-EN`；`pin5=G0 label / H2-G9 net`；`pin6=GND` |
| 复位 | H2-EN 使能/复位网络 | `target=M1 EN pin8`；`net=H2-EN`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C4 1.0uF to GND`；`external_control=J1 pin4 EN` |
| GPIO 与控制信号 | H2-G9 按键与启动网络 | `net=H2-G9`；`module_gpio=GPIO9`；`pullup=R3 10KΩ to +3.3V`；`button=S1 to GND`；`download=J1 pin5 labeled G0`；`protection=D7 ESD5Z3V3 to GND`；`active_level=low` |
| GPIO 与控制信号 | M1 底边上拉与 VBAT 电阻 | `gpio8=R2 10KΩ to +3.3V`；`gpio9=R3 10KΩ to +3.3V`；`vbat=R7 0Ω to +3.3V` |
| GPIO 与控制信号 | M1 命名 GPIO 网络 | `left_nets=H2-G2; H2-G3; H2-G0; H2-G1`；`bottom_nets=H2-G12; H2-G4; H2-G5; H2-G9; G22`；`right_net=G25`；`breakout=JP2 for G25/G22` |
| 时钟 | 32.768 kHz 外部晶振 | `crystal=Y1 32.768KHz ±20ppm 12.5pF`；`nets=OSCI; OSCO`；`load_caps=C6 6.0pF; C7 6.0pF`；`feedback=R6 5.1MΩ / NC`；`population=Y1/C6/C7 not marked NC` |
| 保护电路 | 电源、UART 与按键保护 | `three_v_three=D3 RLSD52A031V`；`vcc=D4 LESD3Z5.0CMT1G`；`uart_rx=D5 RLSD52A031V`；`uart_tx=D6 RLSD52A031V`；`button=D7 ESD5Z3V3`；`return=GND` |
| 接口 | JP1/JP2 引出点 | `jp1_nets=USB_D_P; USB_D_N`；`jp2_nets=G25; G22`；`part_number=null`；`pin_numbers=not shown`；`population=not shown` |
| 存储 | 外部存储器 | `external_flash=not shown`；`psram=not shown`；`eeprom=not shown`；`sd=not shown`；`module=M1 ESP32-H2-MINI-1` |
| 内存与 Flash | M1 N2 变体与 Flash 容量 | `document_module=ESP32-H2-MINI-1-N2`；`document_flash=2MB`；`schematic_module=ESP32-H2-MINI-1`；`schematic_capacity=null`；`external_memory=not shown` |
| 射频 | IEEE 802.15.4、Zigbee、Thread 与 Matter | `document_protocols=IEEE 802.15.4; Zigbee 3.0; Thread 1.3; Matter`；`schematic_protocols=not shown`；`firmware=not shown`；`frequency=not shown`；`role=not shown` |
| 核心器件 | CPU 架构、主频与加密能力 | `document_cpu=32-bit single-core RISC-V`；`document_frequency=up to 96MHz`；`document_security=hardware encryption engine`；`schematic_details=not shown` |
| 电源 | Grove 与 USB 同时供电行为 | `grove_source=J2 pin3 VCC`；`usb_source=J3 VCC through D8`；`diode=D8 B5819W SL`；`fuse=F1 6V@1A`；`priority=not specified`；`backfeed_limits=not specified` |
| 接口 | 灰显 LED 支路装配状态 | `led_nets=G25; G22`；`gray_branch=D1/D2 0603; R4/R5 1KΩ`；`usb_duplicates=D1/D2 RLSD52A031V; R4/R5 5.1KΩ`；`population=not specified`；`issue=duplicate reference designators` |
| 总线 | Grove UART 通信参数 | `tx=H2-TX0`；`rx=H2-RX0`；`baud_rate=not shown`；`frame_format=not shown`；`flow_control=not shown`；`protocol=not shown` |
| 电源 | 工作、待机与休眠电流 | `document_thread=DC 5V@26.08mA`；`document_standby=DC 5V@16.16mA`；`document_sleep=Grove DC 5V@92.7uA`；`schematic_measurement=not shown`；`test_conditions=not shown` |
| 其他事实 | 工作温度与电气额定值 | `document_temperature=0-40°C`；`input_tolerance=not shown`；`ldo_load=not shown`；`esd_rating=not shown`；`schematic_temperature=not shown` |

## 待确认事项

- `memory.module-variant-capacity`：产品正文称 ESP32-H2-MINI-1-N2 和 2MB Flash，但本页 M1 只标 ESP32-H2-MINI-1，未给 N2 后缀、内部 Flash 容量或独立存储器型号。（证据：图 b8b19d02862f / 第 1 页 / 第1页网格 A2，M1 标识 ESP32-H2-MINI-1，无 N2/容量字段）
- `rf.protocol-support`：产品正文列出 IEEE 802.15.4、Zigbee 3.0、Thread 1.3 和 Matter；原理图只显示 M1 型号与天线图形，未写无线协议、协议版本、射频频段或固件角色。（证据：图 b8b19d02862f / 第 1 页 / 第1页网格 A2，M1 型号与天线图形，无协议表）
- `component.cpu-security`：产品正文称 32 位单核 RISC-V、最高 96MHz 和硬件加密引擎；本页 M1 方框只显示模组型号与引脚，没有这些内部参数。（证据：图 b8b19d02862f / 第 1 页 / 第1页网格 A2-B2，M1 模组方框仅含型号、天线和引脚）
- `power.source-priority`：图纸给出 J2 VCC、J3 VBUS、D8、F1 与 +5V 的电气连线，但未说明两路同时接入时的电源优先级、允许反灌条件或热插拔约束。（证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B3-D3，J2/J3/D8/F1/VCC/+5V 连线，无电源策略注记）
- `interface.led-refdes-collision`：G25/G22 旁灰显方框画有 D1/D2 0603 与 R4/R5 1KΩ 到 +3.3V，但 USB 区也使用 D1/D2 作为 ESD、R4/R5 作为 CC 电阻；页面未给灰显支路 NC 标记或 BOM 规则。（证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B2-B4，对比灰显 LED 方框与 J3 USB 区重复 D1/D2/R4/R5）
- `bus.uart-protocol`：原理图确认 H2-TX0/H2-RX0 路由，但未标 UART 波特率、帧格式、流控、上层命令协议或主机固件接口。（证据：图 b8b19d02862f / 第 1 页 / 第1页网格 B2-D4，H2-TX0/H2-RX0/J2/J1，无串口参数注记）
- `power.performance`：产品正文给出 5V Thread 组网 26.08mA、待机 16.16mA、Grove 供电休眠 92.7uA；原理图未提供测试点、固件状态、无线条件或测量方法。（证据：图 b8b19d02862f / 第 1 页 / 第1页 VCC/F1/+5V/U1/M1 供电路径，无电流测量数据）
- `other.operating-limits`：产品正文给出 0-40°C，但原理图没有系统工作温度、USB/Grove 输入容差、LDO 最大负载或保护器件脉冲额定值。（证据：图 b8b19d02862f / 第 1 页 / 第1页完整单页，无温度或系统额定参数表）
- `review.module-variant-capacity`：请用 U195 BOM 或实装模组丝印确认 M1 是否为 ESP32-H2-MINI-1-N2，并核对内部 Flash 为 2MB。；原因：产品正文包含 N2/2MB，原理图 M1 型号缺少 N2 后缀且没有容量字段。
- `review.protocol-support`：请结合实装模组、ESP-IDF 配置和发布固件确认 IEEE 802.15.4、Zigbee、Thread、Matter 的支持范围与版本。；原因：协议与角色属于芯片和固件能力，原理图没有协议版本表。
- `review.cpu-security`：请用实装 ESP32-H2 模组对应 datasheet 复核 CPU 架构、最高主频和硬件加密能力。；原因：这些参数只在产品正文出现，没有印在原理图。
- `review.source-priority`：请核对 D8 极性、F1 料号及 USB-C 与 Grove 同时供电时的优先级、反灌和热插拔限制。；原因：连线可见，但图纸没有双电源使用策略或完整器件额定说明。
- `review.led-refdes-collision`：请用源工程与 BOM 确认灰显 G25/G22 LED 支路是否装配，并纠正其与 USB 区重复的 D1/D2/R4/R5 位号。；原因：单页出现重复位号且灰显支路没有明确 NC/装配标识，无法唯一绑定实物器件。
- `review.uart-protocol`：请从 U195 发布固件或实测确认 Grove UART 的波特率、帧格式、流控和上层命令协议。；原因：原理图只确认物理网络与方向，不含通信参数。
- `review.power-performance`：请按发布固件、Thread 网络状态和明确供电路径复测工作、待机与休眠电流。；原因：正文电流值没有对应的原理图测试条件或测量点。
- `review.operating-limits`：请用整机规格、BOM 器件额定值和环境测试报告确认 0-40°C、输入容差、LDO 带载与 ESD 等级。；原因：这些整机性能和额定值未印在原理图上。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `b8b19d02862f0e5792b4015b1f096a61ebb24476614c3fb8712c0cc0d2cb8989` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1128/U195_Sch_Unit_Gateway_H2_v0.3_sch_01.png` |

---

源文档：`zh_CN/unit/Unit Gateway H2.md`

源文档 SHA-256：`aca8722fdd0fd5f4a0485cfbc4591a45887ff3ea1889bbb43d73659f30e7291a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
