# Module13.2 RS232F 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 RS232F |
| SKU | M130 |
| 产品 ID | `module13-2-rs232f-18a695a51a0b` |
| 源文档 | `zh_CN/module/RS232F Module 13.2.md` |

## 概述

Module13.2 RS232F 以 U2 TD301D232H 实现 M5-Bus TTL UART 与隔离侧 RS-232 的全双工转换，SW1/SW2 分别把 RX/TX 选择到多组主机 GPIO，S1 SS-1260 可将 DB9 的 TXD1/RXD1 设置为直通或交叉。HPWR 经 U3 ME3116 生成 ISO_5V，U1 F0505S-2WR3 将其隔离为 BUS_5V，U4 HX6306P332MR 再生成 VCC_3V3。R_IN/T_OUT 配置 60V 自恢复保险丝、SMAJ18CA、GDT 与 ISO_GND-EARTH 耦合网络，并同时引至 DB9 Female 和 P2 HT3.96-4P。

## 检索关键词

`Module13.2 RS232F`、`M130`、`TD301D232H`、`F0505S-2WR3`、`ME3116`、`HX6306P332MR`、`RS232`、`DB9 Female`、`RX`、`TX`、`RXD1`、`TXD1`、`R_IN`、`T_OUT`、`Passthrough`、`Cross`、`S1 SS-1260`、`SW1`、`SW2`、`GPIO35`、`GPIO34`、`GPIO13`、`GPIO16`、`GPIO3`、`GPIO0`、`GPIO12`、`GPIO15`、`GPIO17`、`GPIO1`、`HPWR`、`ISO_5V`、`BUS_5V`、`VCC_3V3`、`ISO_GND`、`EARTH`、`SMAJ30CA`、`SMAJ18CA`、`GDT1`、`GDT2`、`M5_BUS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | TD301D232H | 隔离式 TTL/CMOS 与 RS-232 全双工收发器 | 图 3edc796ea913 / 第 1 页 / 页面 B1-B2 U2 TD301D232H，RXD/TXD/VCC/GND 与 RIN/TOUT/RGND 引脚 |
| U3 | ME3116 | HPWR 至 ISO_5V 的降压转换器 | 图 3edc796ea913 / 第 1 页 / 页面 A1-A2 U3 ME3116，VIN/EN/BST/LX/FB/GND 与 L1/D4 周边 |
| U1 | F0505S-2WR3 | ISO_5V/ISO_GND 至 BUS_5V/GND 的隔离 DC/DC | 图 3edc796ea913 / 第 1 页 / 页面 A3 U1 F0505S-2WR3，输入 ISO_5V/ISO_GND，输出 BUS_5V/GND |
| U4 | HX6306P332MR | BUS_5V 至 VCC_3V3 的稳压器 | 图 3edc796ea913 / 第 1 页 / 页面 A4 U4 HX6306P332MR，Vin 接 BUS_5V、Vout 接 VCC_3V3 |
| P1,D6 | DC050-T; SMAJ30CA | HPWR 直流输入插座与输入浪涌钳位 | 图 3edc796ea913 / 第 1 页 / 页面 A1 P1 DC050-T 输入 HPWR，D6 SMAJ30CA 跨接 HPWR 与 ISO_GND |
| L1,D4 | 6.8uH; DSS34 | ME3116 降压输出电感与续流肖特基二极管 | 图 3edc796ea913 / 第 1 页 / 页面 A2 U3 右侧 L1 6.8uH 串联到 ISO_5V，D4 DSS34 接开关节点与 ISO_GND |
| F1,F2 | 60V 100mA/JK-NSMD010; 60V 100mA/JK-NSMD010 | R_IN 与 T_OUT RS-232 信号的串联自恢复保险丝 | 图 3edc796ea913 / 第 1 页 / 页面 B2 U2 RIN/TOUT 右侧 F1/F2，均标 60V 100mA/JK-NSMD010 |
| D3,D5 | SMAJ18CA; SMAJ18CA | R_IN 与 T_OUT 对 ISO_GND 的双向 TVS 保护 | 图 3edc796ea913 / 第 1 页 / 页面 B2-C2 D3/D5 SMAJ18CA 分别跨接 R_IN/T_OUT 与 ISO_GND |
| GDT1,GDT2 | GDT; GDT | R_IN 与 T_OUT 到 EARTH 的气体放电浪涌保护 | 图 3edc796ea913 / 第 1 页 / 页面 B2 两个气体放电管符号 GDT1/GDT2，分别连接 R_IN/T_OUT 与 EARTH 公共端 |
| R8,C8 | 1MΩ; 1nF/2KV | ISO_GND 与 EARTH 之间的高阻/高压电容耦合 | 图 3edc796ea913 / 第 1 页 / 页面 C2 R8 1MΩ 与 C8 1nF/2KV 并联在 ISO_GND 和 EARTH 之间 |
| S1 | SS-1260 | R_IN/T_OUT 到 RXD1/TXD1 的直通或交叉线序切换 | 图 3edc796ea913 / 第 1 页 / 页面 B3 S1 SS-1260，R_IN/T_OUT2 公共端与 Passthrough/Cross 两组 RXD1/TXD1 |
| J1 | DB9 Female | RS-232 母头，使用 pin 2 TXD1、pin 3 RXD1、pin 5 ISO_GND，外壳接 EARTH | 图 3edc796ea913 / 第 1 页 / 页面 B4-C4 J1 DB9 Female，TXD1/RXD1/ISO_GND 与 shield 10/11 EARTH |
| P2 | HT3.96 4P | R_IN、T_OUT、HPWR 与 ISO_GND 工业端子 | 图 3edc796ea913 / 第 1 页 / 页面 C3 P2 HT3.96 4P，pin 4 R_IN、3 T_OUT、2 HPWR、1 ISO_GND |
| SW1 | 5-position selector | RX 到 GPIO35/GPIO34/GPIO13/GPIO16/GPIO3 的路由选择 | 图 3edc796ea913 / 第 1 页 / 页面 D2 SW1，左侧 pin 1-5 共接 RX，右侧 pin 10-6 为 GPIO35/GPIO34/GPIO13/GPIO16/GPIO3 |
| SW2 | 5-position selector | TX 到 GPIO0/GPIO12/GPIO15/GPIO17/GPIO1 的路由选择 | 图 3edc796ea913 / 第 1 页 / 页面 D2-D3 SW2，左侧 pin 1-5 共接 TX，右侧 pin 10-6 为 GPIO0/GPIO12/GPIO15/GPIO17/GPIO1 |
| J3 | M5_BUS | 30 针主机堆叠接口，提供可选 UART GPIO、BUS_5V 与 GND | 图 3edc796ea913 / 第 1 页 / 页面 D3-D4 J3 M5_BUS，pin 1-30 及外部 GPIO/BUS_5V/BAT 网络 |

## 系统结构

### Module13.2 RS232F 系统架构

模块由 HPWR 降压与隔离电源、TD301D232H 隔离式 RS-232 收发、SW1/SW2 UART GPIO 选择、S1 直通/交叉切换、DB9/HT3.96 接口及多级浪涌保护组成。

- 参数与网络：`transceiver=U2 TD301D232H`；`primary_converter=U3 ME3116`；`isolated_dcdc=U1 F0505S-2WR3`；`logic_regulator=U4 HX6306P332MR`；`host_connector=J3 M5_BUS`；`rs232_connector=J1 DB9 Female`；`line_selector=S1 SS-1260`
- 证据：图 3edc796ea913 / 第 1 页 / 完整单页 A1-D4 电源、收发、保护、切换与接口分区

## 核心器件

### U2 TD301D232H 引脚与隔离域

U2 逻辑侧 pin 1/VCC 接 VCC_3V3、pin 2/GND 接 GND、pin 3/TXD 接 TX、pin 4/RXD 接 RX；RS-232 侧 pin 6/RIN、pin 7/TOUT、pin 8/RGND 接 ISO_GND。

- 参数与网络：`logic_side=1:VCC/VCC_3V3,2:GND,3:TXD/TX,4:RXD/RX`；`rs232_side=6:RIN,7:TOUT,8:RGND/ISO_GND`；`logic_domain=VCC_3V3/GND`；`line_domain=R_IN/T_OUT/ISO_GND`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 B1-B2 U2 左右引脚、VCC_3V3/GND 与 ISO_GND

## 电源

### HPWR 外部输入与浪涌钳位

P1 DC050-T 将外部电源送入 HPWR，D6 SMAJ30CA 跨接 HPWR 与 ISO_GND；C1 10uF、C5 10uF、C4 100nF 并联滤波，R1 100KΩ 将 U3 EN 上拉到 HPWR。

- 参数与网络：`connector=P1 DC050-T`；`rail=HPWR`；`tvs=D6 SMAJ30CA`；`return=ISO_GND`；`filter=C1 10uF,C5 10uF,C4 100nF`；`enable_pullup=R1 100KΩ`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 A1 P1/HPWR/D6/C1/C5/C4/R1

### U3 ISO_5V 降压

U3 ME3116 的 VIN/EN 接 HPWR，LX 经 L1 6.8uH 输出 ISO_5V，D4 DSS34连接开关节点与 ISO_GND；R2 210KΩ、R3 40.2KΩ 构成 FB 分压，C9 100pF 跨接上臂。

- 参数与网络：`converter=U3 ME3116`；`input=HPWR`；`inductor=L1 6.8uH`；`diode=D4 DSS34`；`output=ISO_5V`；`feedback=R2 210KΩ,R3 40.2KΩ,C9 100pF`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 A2 U3/L1/D4/R2/R3/C9/C10/C11 与 ISO_5V

### ISO_5V 到 BUS_5V 隔离

U1 F0505S-2WR3 的输入侧接 ISO_5V/ISO_GND，输出侧 +VO/0V 形成 BUS_5V/GND；C2 10uF、C6 100nF 并联在 BUS_5V 与 GND，D2 也跨接该输出域。

- 参数与网络：`converter=U1 F0505S-2WR3`；`input_domain=ISO_5V/ISO_GND`；`output_domain=BUS_5V/GND`；`output_caps=C2 10uF,C6 100nF`；`output_protector=D2, part number not printed`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 A3 U1 与 C2/C6/D2/BUS_5V/GND

### VCC_3V3 逻辑电源

U4 HX6306P332MR 的 Vin 接 BUS_5V、Vout 输出 VCC_3V3、GND 接逻辑地；C12 10uF 与 C13 10uF 分别位于输入和输出。

- 参数与网络：`regulator=U4 HX6306P332MR`；`input=BUS_5V`；`output=VCC_3V3`；`ground=GND`；`input_cap=C12 10uF`；`output_cap=C13 10uF`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 A4 U4/C12/C13/BUS_5V/VCC_3V3

## 接口

### J1 DB9 Female 针脚

J1 DB9 Female 使用 pin 2/TXD1、pin 3/RXD1、pin 5/ISO_GND；pin 1、4、6、7、8、9 未连接，外壳 pin 10、11 接 EARTH。

- 参数与网络：`tx=pin 2/TXD1`；`rx=pin 3/RXD1`；`signal_ground=pin 5/ISO_GND`；`unused=pins 1,4,6,7,8,9`；`shield=pins 10,11/EARTH`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 B4-C4 J1 DB9 Female 全部针脚与网络

### S1 直通/交叉线序

S1 SS-1260 的公共端接 R_IN 与 T_OUT2；Passthrough 位置将 R_IN 接 RXD1、T_OUT2 接 TXD1，Cross 位置将 R_IN 接 TXD1、T_OUT2 接 RXD1。

- 参数与网络：`switch=S1 SS-1260`；`passthrough=R_IN -> RXD1,T_OUT2 -> TXD1`；`cross=R_IN -> TXD1,T_OUT2 -> RXD1`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 B3 S1 pin 1-6 与 Passthrough/Cross 标注

### P2 HT3.96 4P 针脚

P2 pin 4 为 R_IN、pin 3 为 T_OUT、pin 2 为 HPWR、pin 1 为 ISO_GND，提供 RS-232 信号与外部电源端子。

- 参数与网络：`pinout=1:ISO_GND,2:HPWR,3:T_OUT,4:R_IN`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 C3 P2 HT3.96 4P pin 1-4

### J3 M5_BUS 已用针脚

J3 使用 pin 1/GPIO35、pin 13/GPIO1、pin 15/GPIO17、pin 21/GPIO13、pin 23/GPIO0、pin 25/GPIO34、pin 14/GPIO3、pin 16/GPIO16、pin 22/GPIO12、pin 24/GPIO15 作为 UART 候选；pin 2/4/6 接 GND，pin 27 接 BUS_5V，pin 29 BAT 带未连接标记。

- 参数与网络：`rx_candidates=GPIO35 pin1,GPIO34 pin25,GPIO13 pin21,GPIO16 pin16,GPIO3 pin14`；`tx_candidates=GPIO0 pin23,GPIO12 pin22,GPIO15 pin24,GPIO17 pin15,GPIO1 pin13`；`ground=pins 2,4,6`；`supply=pin 27/BUS_5V`；`battery=pin 29/BAT no-connect mark`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 D3-D4 J3 M5_BUS 外部红色 GPIO/BUS_5V/BAT 网络

## 总线

### SW1 RX GPIO 路由

U2 pin 4/RXD 连接 RX，RX 共接 SW1 pin 1-5；五个开关分别连接 pin 10/GPIO35、9/GPIO34、8/GPIO13、7/GPIO16、6/GPIO3，对应 J3 可选主机输入。

- 参数与网络：`source=U2 pin 4/RXD -> RX`；`selector=SW1`；`routes=1-10:GPIO35,2-9:GPIO34,3-8:GPIO13,4-7:GPIO16,5-6:GPIO3`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 B1 U2 RX 与 D2 SW1 RX-GPIO35/GPIO34/GPIO13/GPIO16/GPIO3

### SW2 TX GPIO 路由

U2 pin 3/TXD 连接 TX，TX 共接 SW2 pin 1-5；五个开关分别连接 pin 10/GPIO0、9/GPIO12、8/GPIO15、7/GPIO17、6/GPIO1，对应 J3 可选主机输出。

- 参数与网络：`destination=TX -> U2 pin 3/TXD`；`selector=SW2`；`routes=1-10:GPIO0,2-9:GPIO12,3-8:GPIO15,4-7:GPIO17,5-6:GPIO1`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 B1 U2 TX 与 D2-D3 SW2 TX-GPIO0/GPIO12/GPIO15/GPIO17/GPIO1

## 总线地址

### 总线地址可见性

模块使用 UART/RS-232 点对点信号，没有 I2C、SPI 或数值设备地址。

- 参数与网络：`uart_address_visible=false`；`i2c_visible=false`；`spi_visible=false`；`numeric_address_visible=false`
- 证据：图 3edc796ea913 / 第 1 页 / 完整单页所有通信接口，无设备地址

## GPIO 与控制信号

### GPIO12 下拉

J3 pin 22/GPIO12 网络经 R4 2KΩ 下拉到 GND，同时作为 SW2 的 TX 候选。

- 参数与网络：`net=GPIO12`；`bus_pin=J3 pin 22`；`pulldown=R4 2KΩ to GND`；`selector=SW2 pin 9`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 D3-D4 GND-R4 2K-GPIO12/J3 pin 22

## 时钟

### 时钟、复位与调试可见性

原理图未绘出 MCU、晶体、振荡器、复位、BOOT、SWD/JTAG 或专用调试连接器。

- 参数与网络：`mcu_visible=false`；`crystal_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false`
- 证据：图 3edc796ea913 / 第 1 页 / 完整单页器件与接口，无时钟/复位/调试器件

## 保护电路

### R_IN/T_OUT 多级保护

R_IN 与 T_OUT 各串联 F1/F2 60V 100mA 自恢复保险丝，各由 D3/D5 SMAJ18CA 对 ISO_GND 钳位，并分别通过 GDT1/GDT2 向 EARTH 泄放浪涌。

- 参数与网络：`series_fuses=F1 R_IN,F2 T_OUT; 60V 100mA/JK-NSMD010`；`tvs=D3 R_IN,D5 T_OUT; SMAJ18CA to ISO_GND`；`gas_discharge=GDT1 R_IN,GDT2 T_OUT to EARTH`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 B2-C2 U2 RIN/TOUT 至 F1/F2、D3/D5、GDT1/GDT2

### ISO_GND 与 EARTH 耦合

R8 1MΩ 与 C8 1nF/2KV 并联连接 ISO_GND 与 EARTH；DB9 外壳和 GDT 公共端连接 EARTH，信号参考地为 ISO_GND。

- 参数与网络：`resistor=R8 1MΩ`；`capacitor=C8 1nF/2KV`；`from=ISO_GND`；`to=EARTH`；`earth_loads=DB9 shield,GDT1/GDT2 common`
- 证据：图 3edc796ea913 / 第 1 页 / 页面 C2 R8/C8 ISO_GND-EARTH 与 B4 DB9 shield

## 内存与 Flash

### 存储器与内存可见性

原理图没有 Flash、EEPROM、RAM、SD 卡或其他存储器件。

- 参数与网络：`flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`
- 证据：图 3edc796ea913 / 第 1 页 / 完整单页全部器件，无存储位号

## 其他事实

### 其他功能分区可见性

原理图未绘出 I2C、SPI、CAN、RS-485、USB、SDIO、MIPI、I2S、射频、音频、传感器或模拟采样链；核心功能为隔离 RS-232 和电源转换。

- 参数与网络：`i2c_visible=false`；`spi_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false`
- 证据：图 3edc796ea913 / 第 1 页 / 完整单页功能分区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 RS232F 系统架构 | `transceiver=U2 TD301D232H`；`primary_converter=U3 ME3116`；`isolated_dcdc=U1 F0505S-2WR3`；`logic_regulator=U4 HX6306P332MR`；`host_connector=J3 M5_BUS`；`rs232_connector=J1 DB9 Female`；`line_selector=S1 SS-1260` |
| 电源 | HPWR 外部输入与浪涌钳位 | `connector=P1 DC050-T`；`rail=HPWR`；`tvs=D6 SMAJ30CA`；`return=ISO_GND`；`filter=C1 10uF,C5 10uF,C4 100nF`；`enable_pullup=R1 100KΩ` |
| 电源 | U3 ISO_5V 降压 | `converter=U3 ME3116`；`input=HPWR`；`inductor=L1 6.8uH`；`diode=D4 DSS34`；`output=ISO_5V`；`feedback=R2 210KΩ,R3 40.2KΩ,C9 100pF` |
| 电源 | ISO_5V 到 BUS_5V 隔离 | `converter=U1 F0505S-2WR3`；`input_domain=ISO_5V/ISO_GND`；`output_domain=BUS_5V/GND`；`output_caps=C2 10uF,C6 100nF`；`output_protector=D2, part number not printed` |
| 电源 | VCC_3V3 逻辑电源 | `regulator=U4 HX6306P332MR`；`input=BUS_5V`；`output=VCC_3V3`；`ground=GND`；`input_cap=C12 10uF`；`output_cap=C13 10uF` |
| 电源 | DC 输入电压范围 | `documented_range=9-24V`；`schematic_range_visible=false`；`input_net=HPWR` |
| 核心器件 | U2 TD301D232H 引脚与隔离域 | `logic_side=1:VCC/VCC_3V3,2:GND,3:TXD/TX,4:RXD/RX`；`rs232_side=6:RIN,7:TOUT,8:RGND/ISO_GND`；`logic_domain=VCC_3V3/GND`；`line_domain=R_IN/T_OUT/ISO_GND` |
| 总线 | SW1 RX GPIO 路由 | `source=U2 pin 4/RXD -> RX`；`selector=SW1`；`routes=1-10:GPIO35,2-9:GPIO34,3-8:GPIO13,4-7:GPIO16,5-6:GPIO3` |
| 总线 | SW2 TX GPIO 路由 | `destination=TX -> U2 pin 3/TXD`；`selector=SW2`；`routes=1-10:GPIO0,2-9:GPIO12,3-8:GPIO15,4-7:GPIO17,5-6:GPIO1` |
| 总线 | RS-232 通讯速率 | `documented_max_baud=115200`；`schematic_baud_visible=false`；`frame_format_visible=false` |
| 接口 | J1 DB9 Female 针脚 | `tx=pin 2/TXD1`；`rx=pin 3/RXD1`；`signal_ground=pin 5/ISO_GND`；`unused=pins 1,4,6,7,8,9`；`shield=pins 10,11/EARTH` |
| 接口 | S1 直通/交叉线序 | `switch=S1 SS-1260`；`passthrough=R_IN -> RXD1,T_OUT2 -> TXD1`；`cross=R_IN -> TXD1,T_OUT2 -> RXD1` |
| 接口 | P2 HT3.96 4P 针脚 | `pinout=1:ISO_GND,2:HPWR,3:T_OUT,4:R_IN` |
| 保护电路 | R_IN/T_OUT 多级保护 | `series_fuses=F1 R_IN,F2 T_OUT; 60V 100mA/JK-NSMD010`；`tvs=D3 R_IN,D5 T_OUT; SMAJ18CA to ISO_GND`；`gas_discharge=GDT1 R_IN,GDT2 T_OUT to EARTH` |
| 保护电路 | ISO_GND 与 EARTH 耦合 | `resistor=R8 1MΩ`；`capacitor=C8 1nF/2KV`；`from=ISO_GND`；`to=EARTH`；`earth_loads=DB9 shield,GDT1/GDT2 common` |
| 接口 | J3 M5_BUS 已用针脚 | `rx_candidates=GPIO35 pin1,GPIO34 pin25,GPIO13 pin21,GPIO16 pin16,GPIO3 pin14`；`tx_candidates=GPIO0 pin23,GPIO12 pin22,GPIO15 pin24,GPIO17 pin15,GPIO1 pin13`；`ground=pins 2,4,6`；`supply=pin 27/BUS_5V`；`battery=pin 29/BAT no-connect mark` |
| GPIO 与控制信号 | GPIO12 下拉 | `net=GPIO12`；`bus_pin=J3 pin 22`；`pulldown=R4 2KΩ to GND`；`selector=SW2 pin 9` |
| 总线地址 | 总线地址可见性 | `uart_address_visible=false`；`i2c_visible=false`；`spi_visible=false`；`numeric_address_visible=false` |
| 时钟 | 时钟、复位与调试可见性 | `mcu_visible=false`；`crystal_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false` |
| 内存与 Flash | 存储器与内存可见性 | `flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false` |
| 其他事实 | 其他功能分区可见性 | `i2c_visible=false`；`spi_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false` |

## 待确认事项

- `power.documented-input-range`：产品正文记载 DC 电源接口输入为 9-24V；原理图只显示 HPWR、ME3116 与 SMAJ30CA，没有打印 9V/24V 工作范围。（证据：图 3edc796ea913 / 第 1 页 / 页面 A1-A2 HPWR 输入与 U3 电源区，无输入范围文字）
- `bus.documented-baud`：产品正文记载通讯速率最高 115200bps；原理图仅显示 UART/RS-232 信号与切换网络，没有打印波特率或帧格式。（证据：图 3edc796ea913 / 第 1 页 / 页面 U2 RX/TX、SW1/SW2 与 DB9 路径，无速率文字）
- `review.input-range`：Module13.2 RS232F 的正式 DC 输入范围是否确认为 9-24V？；原因：原理图显示 HPWR 电源链但未打印允许输入范围。
- `review.max-baud`：当前 TD301D232H 方案的产品保证通讯速率是否最高为 115200bps？；原因：速率来自产品正文，原理图没有波特率或帧格式。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3edc796ea9139db47274196067b570b9cfca9860e986dc2fa8ee072ec52db346` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/557/SCH_Module_13.2_RS232F_V1.0_sch_01.png` |

---

源文档：`zh_CN/module/RS232F Module 13.2.md`

源文档 SHA-256：`f5b49b4e7a1b53c92f717776611c2d6afe4ce3393eca6b100456cb0e5cb362e5`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
