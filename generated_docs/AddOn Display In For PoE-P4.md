# AddOn Display In For PoE-P4 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AddOn Display In For PoE-P4 |
| SKU | U220 |
| 产品 ID | `addon-display-in-for-poe-p4-09beae90926b` |
| 源文档 | `zh_CN/addon/AddOn_Display_In_For_PoE-P4.md` |

## 概述

该页以 LT6911D 为核心，将 J1 的 HDMI TMDS、DDC、CEC 与 HPD 信号接入接收端，并从 M0/M1/MC 端口输出两条 MIPI 数据差分对和一条时钟差分对。板上同时提供 microSD/SDIO、USB Type-A、24P FPC 以及辅助连接器，并以 ESD 器件覆盖 HDMI、USB 和 SDIO 外部信号。电源部分从 VCC_5V 生成 LT6911D 所需的 1.2 V 域，结合 VCC_3V3、磁珠分域、24 MHz 晶振、复位转换和 3.3 V/1.8 V I2C 电平转换完成接口配套。

## 检索关键词

`AddOn Display In For PoE-P4`、`U220`、`Unit PoE-P4 Display IN`、`LT6911D`、`HDMI`、`HDMI-001 19PCBTP`、`TMDS`、`MIPI1`、`2-Lane MIPI`、`MIPI1_lane0`、`MIPI1_lane1`、`MIPI1_CLK`、`I2C 0x56`、`SYS_SCL`、`SYS_SDA`、`RX_SCL`、`RX_SDA`、`RX_HPD`、`CEC`、`SY8003`、`MT9700-N`、`MTXS0102DQER`、`USB Type-A`、`USB1_D_P`、`USB1_D_N`、`microSD`、`TF_Card`、`SDIO`、`G37_TF_DET`、`G38`、`VCC_1V2`、`VCC_3V3`、`VCC_5V`、`VCC_1V8`、`RST_1V8`、`24MHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | LT6911D | HDMI 接收与 MIPI 差分输出桥接核心，连接 TMDS、DDC、CEC、HPD、控制 I2C 和两条 MIPI 数据通道 | 图 77cf16236c92 / 第 1 页 / 第1页 B3-C6，LT6911D 分区 U3 及其 1-65 脚网络 |
| U1 | SY8003 | VCC_5V 到 VCC_1V2 的降压稳压器 | 图 77cf16236c92 / 第 1 页 / 第1页 A2-A3，POWER 1V2 分区 U1 |
| L1 | FTC201208S1R0MBCD | SY8003 LX 端的降压电感 | 图 77cf16236c92 / 第 1 页 / 第1页 A3，U1 LX 与 VCC_1V2 之间的 L1 |
| FB1, FB2, FB3, FB4, FB5 | BLM15PX800SN1D | 从 1.2 V 和 3.3 V 主电源轨分隔 LT6911D 各接收、发送与内核电源域 | 图 77cf16236c92 / 第 1 页 / 第1页 A4-A6，VCC_1V2/VCC_3V3 至 VDD、VCC12_TX、VCC12A_RX、VCC33_TX、VCC33_RX 的磁珠 |
| U4 | MT9700-N | USB_5V 限流电源开关，SET 脚由 R12 配置 | 图 77cf16236c92 / 第 1 页 / 第1页 B1-B2，USB A 分区 U4、R12 与 USB_5V |
| USB1 | USB-AF-DIP-154-HW-S | USB Type-A 母座，承载 USB_5V、USB1_D_N、USB1_D_P 和 GND | 图 77cf16236c92 / 第 1 页 / 第1页 B2，USB A 分区 USB1 四脚连接器 |
| DR1, DR2 | ESD5311 | USB1_D_N 与 USB1_D_P 到地的 ESD 保护器件 | 图 77cf16236c92 / 第 1 页 / 第1页 B2，USB1 数据线下方 DR1/DR2 |
| J2 | TF_Card | microSD/TF 卡连接器，连接六线 SDIO、3.3 V、地和卡检测触点 | 图 77cf16236c92 / 第 1 页 / 第1页 C1-D2，TF CARD 分区 J2 |
| D6, D7, D8, D9, D10, D11, D12 | ESD5311 | SDIO 数据、时钟、命令及 TF_DET 网络的 ESD 保护器件 | 图 77cf16236c92 / 第 1 页 / 第1页 D1-D3，TF CARD 分区底部 ESD5311 阵列 |
| J1 | HDMI-001 19PCBTP | 19 针 HDMI 输入连接器，承载三组数据差分对、时钟差分对、CEC、DDC、5 V 与 HPD | 图 77cf16236c92 / 第 1 页 / 第1页 A7-B8，HDMI 分区 J1 |
| D3, D4 | LRC1043-04DT1G | 四组 HDMI TMDS 差分对的 ESD 保护阵列 | 图 77cf16236c92 / 第 1 页 / 第1页 B7-B8，D3 连接 D2/D1，D4 连接 D0/CLK |
| D5 | ESD0524P | HDMI RX_SCL、RX_SDA 与 RX_HPD 控制线的 ESD 保护阵列 | 图 77cf16236c92 / 第 1 页 / 第1页 B7，D5 的 IN1/IN2/IN3 分别连接 RX_SCL/RX_SDA/RX_HPD |
| X1 | 24MHz(XL7EL89CKI-111YLC-24M) | LT6911D 的 24 MHz 晶体时钟源 | 图 77cf16236c92 / 第 1 页 / 第1页 B5-B6，XTALI/XTALO 之间的 X1 |
| JP1 | CON24_FPC | 24 针 FPC 接口，承载 1.8 V I2C、复位、两条 MIPI 数据通道、MIPI 时钟、1.8 V 与多脚接地 | 图 77cf16236c92 / 第 1 页 / 第1页 C7-D8，MIPI 分区 JP1 |
| JP2 | 未标注 | 9 针辅助接口，承载 SDIO 六线、USB 差分对与 VCC_5V | 图 77cf16236c92 / 第 1 页 / 第1页 C7，MIPI 分区左侧 JP2 |
| JP3 | 未标注 | 6 针辅助接口，承载 G38、G37_TF_DET、VCC_3V3 与 GND | 图 77cf16236c92 / 第 1 页 / 第1页 C7，MIPI 分区左侧 JP3 |
| U5 | MTXS0102DQER | SYS_SCL/SYS_SDA 的 3.3 V 到 1.8 V 双通道电平转换器 | 图 77cf16236c92 / 第 1 页 / 第1页 D7-D8，MIPI 分区 U5，VCCB=VCC_3V3、VCCA=VCC_1V8 |
| Q1, Q2 | 2N7002KM; S8050 | RST_1V8 到 RST_N 的晶体管复位接口 | 图 77cf16236c92 / 第 1 页 / 第1页 C6，Q1 2N7002KM、Q2 S8050、R28/R29 复位电路 |
| U2 | 未标注 | VCC_5V 到 HDMI_5V 的可选电源器件位置；U2 及其外围在图中标注 NC | 图 77cf16236c92 / 第 1 页 / 第1页 B1-B2，POWER 5V 分区 U2、C8/C9/C10、R10 的 NC 标注 |
| D1, D2 | 未标注 | HDMI_5V、RX_5V 与 DDC 上拉供电之间的可选二极管位置；两者均标注 NC | 图 77cf16236c92 / 第 1 页 / 第1页 A7，HDMI 分区 HDMI_5V 下方 D1/D2 NC 网络 |

## 系统结构

### 原理图页身份

当前附着页面标题为 Unit PoE-P4 Display IN，图号栏为 2/2，修订为 V0.3，日期为 3/26/2026。

- 参数与网络：`title=Unit PoE-P4 Display IN`；`sheet_number=2/2`；`revision=V0.3`；`date=3/26/2026`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 D7-D8 标题栏

### 视频信号路径

J1 的 HDMI TMDS 时钟和三组数据差分对进入 U3 LT6911D，U3 从 MC、M0、M1 端口输出一组 MIPI 时钟和两组 MIPI 数据差分对。

- 参数与网络：`input_connector=J1`；`bridge=U3 LT6911D`；`output_clock=MIPI1_CLK_P/N`；`output_data=MIPI1_lane0_P/N; MIPI1_lane1_P/N`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 A7-C6，J1 TMDS 网络、U3 HRX 输入及 M0/M1/MC 输出

## 核心器件

### U3 LT6911D

U3 器件标注为 LT6911D，并同时连接 HDMI 接收、MIPI 发送、DDC、CEC、HPD、系统 I2C、复位和晶体时钟网络。

- 参数与网络：`reference=U3`；`part_number=LT6911D`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B3-C6，U3 LT6911D 器件框

## 电源

### USB 5 V 电源开关

U4 MT9700-N 的 VIN 和 EN 均连接 VCC_5V，VOUT 输出 USB_5V，SET 经 R12 10K 接地；图注给出 I limit=6.8K/RL=680mA。

- 参数与网络：`input=VCC_5V`；`output=USB_5V`；`set_resistor=R12 10K`；`current_limit_note=680mA`；`input_capacitor=C13 10uF/10V`；`output_capacitor=C14 10uF/10V`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B1-B2，USB A 分区 U4、R12、C13/C14 与限流图注

### VCC_1V2 降压电源

U1 SY8003 从 VCC_5V 输入，经 L1 输出 VCC_1V2；R1/R4 均为 150K/1%，C1 为 22pF/50V，图注给出 Vout=1.2V 和 I max out=3A。

- 参数与网络：`input=VCC_5V`；`output=VCC_1V2`；`controller=U1 SY8003`；`inductor=L1 FTC201208S1R0MBCD`；`feedback=R1 150K/1%; R4 150K/1%; C1 22pF/50V`；`output_note=1.2V; I max out=3A`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 A1-A4，POWER 1V2 的 U1/L1/R1/R4/C1 与图注

### 1V2_EN 配置

U1 EN 脚使用 1V2_EN 网络；R3 0R 将 1V2_EN 连接 VCC_5V，R2 从 VCC_3V3 到 1V2_EN 的位置标注 NC。

- 参数与网络：`enable_net=1V2_EN`；`installed_path=R3 0R to VCC_5V`；`nc_path=R2 NC to VCC_3V3`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 A1-A2，R2/R3、1V2_EN 与 U1 pin7

### 1.2 V 电源域分配

VCC_1V2 经 FB1、FB3、FB5 BLM15PX800SN1D 分别形成 VDD、VCC12_TX、VCC12A_RX。

- 参数与网络：`fb1=VDD`；`fb3=VCC12_TX`；`fb5=VCC12A_RX`；`part_number=BLM15PX800SN1D`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 A4-A5，VCC_1V2 后的 FB1/FB3/FB5

### 3.3 V 电源域分配

VCC_3V3 经 FB2 和 FB4 BLM15PX800SN1D 分别形成 VCC33_TX 与 VCC33_RX，磁珠输入侧由 C4 100nF/25V 对地去耦。

- 参数与网络：`fb2=VCC33_TX`；`fb4=VCC33_RX`；`input_capacitor=C4 100nF/25V`；`part_number=BLM15PX800SN1D`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 A5-A6，VCC_3V3、C4、FB2/FB4

### LT6911D 分域去耦

VCC33_TX、VCC33_RX、VDD、VCC12A_RX、VCC12_TX 各自配置一只 10uF/10V 电容及多只 100nF/25V 电容到地。

- 参数与网络：`vcc33_tx=C19 10uF/10V; C20/C21/C22/C24/C25 100nF/25V`；`vcc33_rx=C26 10uF/10V; C27/C28 100nF/25V`；`vdd=C29 10uF/10V; C30/C31/C32 100nF/25V`；`vcc12a_rx=C36 10uF/10V; C37/C38/C39/C33 100nF/25V`；`vcc12_tx=C40 10uF/10V; C41/C42/C43/C34 100nF/25V`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 D3-D6，C19-C43 的五组电源去耦

## 接口

### J1 HDMI TMDS 引脚

J1 的 1/3、4/6、7/9 和 10/12 脚分别连接 TMDS_D2_P/N、TMDS_D1_P/N、TMDS_D0_P/N 和 TMDS_CLK_P/N。

- 参数与网络：`connector=J1`；`data2=pin1 TMDS_D2_P; pin3 TMDS_D2_N`；`data1=pin4 TMDS_D1_P; pin6 TMDS_D1_N`；`data0=pin7 TMDS_D0_P; pin9 TMDS_D0_N`；`clock=pin10 TMDS_CLK_P; pin12 TMDS_CLK_N`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 A7-A8，J1 的 D2/D1/D0/CLK 引脚与 TMDS 网络

### J1 HDMI 控制与供电脚

J1 的 13、15、16、17、18、19 脚分别连接 CEC、RX_SCL、RX_SDA、DDC/CEC GND、RX_5V 和 RX_HPD，20-23 脚为连接器接地/屏蔽脚。

- 参数与网络：`cec=pin13 CEC`；`ddc=pin15 RX_SCL; pin16 RX_SDA`；`ddc_ground=pin17`；`five_volt=pin18 RX_5V`；`hotplug=pin19 RX_HPD`；`grounds=pins20-23`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 A7-B8，J1 的 CEC/DDC/+5V/HOTPLUG 与接地引脚

### HDMI TMDS 差分阻抗

TMDS 差分网络在 HDMI 连接器侧和 LT6911D 接收侧均标注 Z=100R。

- 参数与网络：`impedance_annotation=Z=100R`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 A7 与 B3，TMDS 网络旁 Z=100R 注记

### LT6911D MIPI 输出映射

U3 的 M0_P1/M0_N1、M1_P1/M1_N1、MC_P1/MC_N1 分别连接 MIPI1_lane0_P/N、MIPI1_lane1_P/N、MIPI1_CLK_P/N。

- 参数与网络：`lane0=U3 pin35 M0_P1 -> MIPI1_lane0_P; pin36 M0_N1 -> MIPI1_lane0_N`；`lane1=U3 pin37 M1_P1 -> MIPI1_lane1_P; pin38 M1_N1 -> MIPI1_lane1_N`；`clock=U3 pin39 MC_P1 -> MIPI1_CLK_P; pin40 MC_N1 -> MIPI1_CLK_N`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B5-C6，U3 35-40 脚与 MIPI1 网络

### LT6911D 未用 MIPI 通道

U3 的 M2_P1/M2_N1 与 M3_P1/M3_N1（41-44 脚）均画有未连接标记。

- 参数与网络：`unused_pins=41 M2_P1; 42 M2_N1; 43 M3_P1; 44 M3_N1`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B5，U3 41-44 脚红色未连接标记

### MIPI 差分阻抗

MIPI1_lane0、MIPI1_lane1 和 MIPI1_CLK 差分网络标注 Z=100R。

- 参数与网络：`impedance_annotation=Z=100R`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B5-C7，U3 输出与 JP1 MIPI 网络旁 Z=100R 注记

### JP1 24P FPC 引脚

JP1 的 2/3 脚为 SCL_1V8/SDA_1V8，8 脚为 RST_1V8，10/11 脚为 MIPI1_lane1_P/N，13/14 脚为 MIPI1_CLK_P/N，16/17 脚为 MIPI1_lane0_P/N，22 脚为 VCC_1V8；6、19、23 脚标为未连接，其余所示信号脚接地。

- 参数与网络：`i2c=pin2 SCL_1V8; pin3 SDA_1V8`；`reset=pin8 RST_1V8`；`lane1=pin10 P; pin11 N`；`clock=pin13 P; pin14 N`；`lane0=pin16 P; pin17 N`；`supply=pin22 VCC_1V8`；`nc=pins6,19,23`；`ground=pins1,4,5,7,9,12,15,18,20,21,24 and SH`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 C7-D8，JP1 CON24_FPC 的 1-24/SH 引脚

### JP2 辅助接口

JP2 的 1-9 脚依次连接 SDIO_G13_CMD、SDIO_G12_CK、SDIO_G11_D3、SDIO_G10_D2、SDIO_G9_D1、SDIO_G8_D0、USB1_D_P、USB1_D_N、VCC_5V。

- 参数与网络：`pins=1 CMD; 2 CK; 3 D3; 4 D2; 5 D1; 6 D0; 7 USB1_D_P; 8 USB1_D_N; 9 VCC_5V`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 C7，JP2 1-9 脚网络标注

### JP3 辅助接口

JP3 的 1 脚接地，2/3 脚标为未连接，4 脚为 G38，5 脚为 G37_TF_DET，6 脚为 VCC_3V3，并由 C18 10uF/10V 对地去耦。

- 参数与网络：`pins=1 GND; 2 NC; 3 NC; 4 G38; 5 G37_TF_DET; 6 VCC_3V3`；`decoupling=C18 10uF/10V`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 C7，JP3 与 C18

### USB1 Type-A 接口

USB1 的 1-4 脚依次为 USB_5V、USB1_D_N、USB1_D_P 和 GND，连接器型号标注 USB-AF-DIP-154-HW-S。

- 参数与网络：`pin1=USB_5V`；`pin2=USB1_D_N`；`pin3=USB1_D_P`；`pin4=GND`；`part_number=USB-AF-DIP-154-HW-S`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B2，USB1 连接器引脚

### USB 差分阻抗

USB1_D_P 与 USB1_D_N 差分网络在 USB1 和 JP2 侧均标注 Z=90R。

- 参数与网络：`impedance_annotation=Z=90R`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B2 与 C7，USB 差分网络旁 Z=90R 注记

## 总线

### LT6911D 系统 I2C

U3 的 CSCL 和 CSDA（21、22 脚）连接 SYS_SCL 和 SYS_SDA，R17/R18 分别以 4.7K 上拉到 VCC_3V3。

- 参数与网络：`scl=U3 pin21 CSCL; SYS_SCL; R17 4.7K`；`sda=U3 pin22 CSDA; SYS_SDA; R18 4.7K`；`pullup_supply=VCC_3V3`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B3-C4，R17/R18、SYS_SCL/SYS_SDA 与 U3 21/22 脚

### 3.3 V/1.8 V I2C 电平转换

U5 MTXS0102DQER 以 VCCB=VCC_3V3、VCCA=VCC_1V8 工作，将 B1/B2 的 SYS_SCL/SYS_SDA 对接到 A1/A2 的 SCL_1V8/SDA_1V8；OE 接 VCC_1V8 并由 R20 100K 下拉。

- 参数与网络：`reference=U5`；`b_side=VCC_3V3; SYS_SCL; SYS_SDA`；`a_side=VCC_1V8; SCL_1V8; SDA_1V8`；`oe=VCC_1V8; R20 100K to GND`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 D7-D8，U5、R20、C45/C46

### SDIO 上拉网络

R22、R23、R24、R25、R26、R27 均为 10K，并分别把 D2、D3、CMD、CK、D0、D1 网络上拉到 VCC_3V3。

- 参数与网络：`data2=R22 10K`；`data3=R23 10K`；`cmd=R24 10K`；`clock=R25 10K`；`data0=R26 10K`；`data1=R27 10K`；`supply=VCC_3V3`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 C1-C2，R22-R27 与六条 SDIO 网络

## 总线地址

### LT6911D I2C 地址

LT6911D 分区明确标注 IIC Address:0x56。

- 参数与网络：`address=0x56`；`notation=IIC Address`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B3，LT6911D 标题下方 IIC Address:0x56 注记

## GPIO 与控制信号

### 本地 TF_DET 检测节点

J2 的 K 触点连接 TF_DET，TF_DET 由 R13 100K 上拉到 VCC_3V3，并由 C16 2nF/50V 对地滤波。

- 参数与网络：`connector_contact=J2 pin9 K`；`pullup=R13 100K to VCC_3V3`；`filter=C16 2nF/50V to GND`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 C2，J2 pin9、TF_DET、R13、C16

### 分辨率变化指示

图面注记说明分辨率变化时 GPIO5 产生 200ms 高电平脉冲；GPIO5 经 R14 0R 连接 G38，并引到 JP3 的 4 脚。

- 参数与网络：`source_pin=U3 pin26 INTIO_GPIO5`；`pulse=200ms high-level`；`series_resistor=R14 0R`；`host_net=G38`；`connector_pin=JP3 pin4`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 C4-C7，GPIO5-R14-G38、设计注记与 JP3 pin4

## 时钟

### LT6911D 晶体时钟

X1 标注 24MHz(XL7EL89CKI-111YLC-24M)，连接 U3 的 XTALI/XTALO；R7 为 0R，R9 为 1M，C7/C11 均为 8pF/50V。

- 参数与网络：`crystal=X1 24MHz(XL7EL89CKI-111YLC-24M)`；`series_resistor=R7 0R`；`feedback_resistor=R9 1M`；`load_capacitors=C7 8pF/50V; C11 8pF/50V`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B5-B6，XTALI/XTALO、X1、R7/R9、C7/C11

## 复位

### LT6911D RST_N 上电网络

U3 的 RST_N（20 脚）连接 RST_N 网络，该网络由 R16 1K 上拉到 VCC_3V3，并由 C17 1uF/16V 对地。

- 参数与网络：`reset_pin=U3 pin20 RST_N`；`pullup=R16 1K to VCC_3V3`；`capacitor=C17 1uF/16V to GND`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 C3-C4，U3 pin20、R16、C17 与 RST_N

### RST_1V8 到 RST_N 接口

RST_1V8 经 R29 5.1K 驱动 Q2 S8050，Q2 集电极连接 Q1 2N7002KM 栅极；该栅极由 R28 100K 上拉到 VCC_3V3，Q1 漏极连接 RST_N、源极接地。

- 参数与网络：`input=RST_1V8`；`base_resistor=R29 5.1K`；`bjt=Q2 S8050`；`mosfet=Q1 2N7002KM`；`gate_pullup=R28 100K to VCC_3V3`；`output=RST_N`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 C6，RST_N/RST_1V8、Q1/Q2、R28/R29

## 保护电路

### HDMI TMDS ESD 保护

D3 LRC1043-04DT1G 保护 TMDS_D2 与 TMDS_D1，D4 LRC1043-04DT1G 保护 TMDS_D0 与 TMDS_CLK，两个阵列的 GND 脚接地。

- 参数与网络：`d3_channels=TMDS_D2_P/N; TMDS_D1_P/N`；`d4_channels=TMDS_D0_P/N; TMDS_CLK_P/N`；`part_number=LRC1043-04DT1G`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B7-B8，D3/D4 输入网络标注

### HDMI DDC 与 HPD ESD 保护

D5 ESD0524P 的 IN1、IN2、IN3 分别连接 RX_SCL、RX_SDA、RX_HPD，IN4 在图中标为未连接。

- 参数与网络：`part_number=ESD0524P`；`in1=RX_SCL`；`in2=RX_SDA`；`in3=RX_HPD`；`in4=NC`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B7，D5 ESD0524P

### HDMI 屏蔽地耦合

J1 屏蔽地节点与板级 GND 之间并联 R11 0R 和 C12 1nF/2KV。

- 参数与网络：`resistor=R11 0R`；`capacitor=C12 1nF/2KV`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B7-B8，D5 右侧 R11/C12 与两种接地符号

### USB 数据线保护

USB1_D_N 和 USB1_D_P 分别通过 DR1、DR2 ESD5311 接地保护。

- 参数与网络：`d_minus=DR1 ESD5311`；`d_plus=DR2 ESD5311`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 B2，USB1_D_N/P 下方 DR1/DR2

### SDIO 与卡检测保护

D6/D8/D10/D12 分别保护 SDIO_G8_D0、SDIO_G9_D1、SDIO_G10_D2、SDIO_G11_D3，D7/D9/D11 分别保护 SDIO_G12_CK、SDIO_G13_CMD、TF_DET，器件均标注 ESD5311。

- 参数与网络：`data_lines=D6 D0; D8 D1; D10 D2; D12 D3`；`control_lines=D7 CK; D9 CMD; D11 TF_DET`；`part_number=ESD5311`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 D1-D3，D6-D12 与对应网络标签

## 关键网络

### HDMI 控制网络到 LT6911D

RX_SDA、RX_SCL、RX_HPD 和 CEC 分别接入 U3 的 HRX_DSDA、HRX_DSCL、HRX_HPD 和 CEC 引脚。

- 参数与网络：`rx_sda=U3 pin15 HRX_DSDA`；`rx_scl=U3 pin16 HRX_DSCL`；`rx_hpd=U3 pin23 HRX_HPD`；`cec=U3 pin33 CEC`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 A7-C6，J1 控制网络与 U3 对应引脚

## 存储

### J2 microSD/TF 卡引脚

J2 的 DATA2、CD/DATA3、CMD、CLK、DATA0、DATA1 分别连接 SDIO_G10_D2、SDIO_G11_D3、SDIO_G13_CMD、SDIO_G12_CK、SDIO_G8_D0、SDIO_G9_D1，VDD 接 VCC_3V3，VSS 与 GND 脚接地。

- 参数与网络：`pin1=DATA2 -> SDIO_G10_D2`；`pin2=CD/DATA3 -> SDIO_G11_D3`；`pin3=CMD -> SDIO_G13_CMD`；`pin4=VDD -> VCC_3V3`；`pin5=CLK -> SDIO_G12_CK`；`pin6=VSS -> GND`；`pin7=DATA0 -> SDIO_G8_D0`；`pin8=DATA1 -> SDIO_G9_D1`；`pin10=GND`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 C1-D2，J2 1-10 脚

## 调试与烧录

### 调试测试点

TP3 接地，TP4 连接 RST_N，TP6 连接 SYS_SCL，TP7 连接 SYS_SDA。

- 参数与网络：`tp3=GND`；`tp4=RST_N`；`tp6=SYS_SCL`；`tp7=SYS_SDA`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 C3，TP3/TP4/TP6/TP7 网络

## 模拟电路

### LT6911D REXT

U3 的 REXT 引脚通过 R19 7.68K/1% 接地。

- 参数与网络：`pin=U3 pin60 REXT`；`resistor=R19 7.68K/1%`
- 证据：图 77cf16236c92 / 第 1 页 / 第1页 C3，U3 REXT 网络与 R19

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 原理图页身份 | `title=Unit PoE-P4 Display IN`；`sheet_number=2/2`；`revision=V0.3`；`date=3/26/2026` |
| 系统结构 | 视频信号路径 | `input_connector=J1`；`bridge=U3 LT6911D`；`output_clock=MIPI1_CLK_P/N`；`output_data=MIPI1_lane0_P/N; MIPI1_lane1_P/N` |
| 核心器件 | U3 LT6911D | `reference=U3`；`part_number=LT6911D` |
| 总线地址 | LT6911D I2C 地址 | `address=0x56`；`notation=IIC Address` |
| 接口 | J1 HDMI TMDS 引脚 | `connector=J1`；`data2=pin1 TMDS_D2_P; pin3 TMDS_D2_N`；`data1=pin4 TMDS_D1_P; pin6 TMDS_D1_N`；`data0=pin7 TMDS_D0_P; pin9 TMDS_D0_N`；`clock=pin10 TMDS_CLK_P; pin12 TMDS_CLK_N` |
| 接口 | J1 HDMI 控制与供电脚 | `cec=pin13 CEC`；`ddc=pin15 RX_SCL; pin16 RX_SDA`；`ddc_ground=pin17`；`five_volt=pin18 RX_5V`；`hotplug=pin19 RX_HPD`；`grounds=pins20-23` |
| 关键网络 | HDMI 控制网络到 LT6911D | `rx_sda=U3 pin15 HRX_DSDA`；`rx_scl=U3 pin16 HRX_DSCL`；`rx_hpd=U3 pin23 HRX_HPD`；`cec=U3 pin33 CEC` |
| 保护电路 | HDMI TMDS ESD 保护 | `d3_channels=TMDS_D2_P/N; TMDS_D1_P/N`；`d4_channels=TMDS_D0_P/N; TMDS_CLK_P/N`；`part_number=LRC1043-04DT1G` |
| 保护电路 | HDMI DDC 与 HPD ESD 保护 | `part_number=ESD0524P`；`in1=RX_SCL`；`in2=RX_SDA`；`in3=RX_HPD`；`in4=NC` |
| 保护电路 | HDMI 屏蔽地耦合 | `resistor=R11 0R`；`capacitor=C12 1nF/2KV` |
| 接口 | HDMI TMDS 差分阻抗 | `impedance_annotation=Z=100R` |
| 接口 | LT6911D MIPI 输出映射 | `lane0=U3 pin35 M0_P1 -> MIPI1_lane0_P; pin36 M0_N1 -> MIPI1_lane0_N`；`lane1=U3 pin37 M1_P1 -> MIPI1_lane1_P; pin38 M1_N1 -> MIPI1_lane1_N`；`clock=U3 pin39 MC_P1 -> MIPI1_CLK_P; pin40 MC_N1 -> MIPI1_CLK_N` |
| 接口 | LT6911D 未用 MIPI 通道 | `unused_pins=41 M2_P1; 42 M2_N1; 43 M3_P1; 44 M3_N1` |
| 接口 | MIPI 差分阻抗 | `impedance_annotation=Z=100R` |
| 总线 | LT6911D 系统 I2C | `scl=U3 pin21 CSCL; SYS_SCL; R17 4.7K`；`sda=U3 pin22 CSDA; SYS_SDA; R18 4.7K`；`pullup_supply=VCC_3V3` |
| 总线 | 3.3 V/1.8 V I2C 电平转换 | `reference=U5`；`b_side=VCC_3V3; SYS_SCL; SYS_SDA`；`a_side=VCC_1V8; SCL_1V8; SDA_1V8`；`oe=VCC_1V8; R20 100K to GND` |
| 接口 | JP1 24P FPC 引脚 | `i2c=pin2 SCL_1V8; pin3 SDA_1V8`；`reset=pin8 RST_1V8`；`lane1=pin10 P; pin11 N`；`clock=pin13 P; pin14 N`；`lane0=pin16 P; pin17 N`；`supply=pin22 VCC_1V8`；`nc=pins6,19,23`；`ground=pins1,4,5,7,9,12,15,18,20,21,24 and SH` |
| 接口 | JP2 辅助接口 | `pins=1 CMD; 2 CK; 3 D3; 4 D2; 5 D1; 6 D0; 7 USB1_D_P; 8 USB1_D_N; 9 VCC_5V` |
| 接口 | JP3 辅助接口 | `pins=1 GND; 2 NC; 3 NC; 4 G38; 5 G37_TF_DET; 6 VCC_3V3`；`decoupling=C18 10uF/10V` |
| 电源 | USB 5 V 电源开关 | `input=VCC_5V`；`output=USB_5V`；`set_resistor=R12 10K`；`current_limit_note=680mA`；`input_capacitor=C13 10uF/10V`；`output_capacitor=C14 10uF/10V` |
| 接口 | USB1 Type-A 接口 | `pin1=USB_5V`；`pin2=USB1_D_N`；`pin3=USB1_D_P`；`pin4=GND`；`part_number=USB-AF-DIP-154-HW-S` |
| 保护电路 | USB 数据线保护 | `d_minus=DR1 ESD5311`；`d_plus=DR2 ESD5311` |
| 接口 | USB 差分阻抗 | `impedance_annotation=Z=90R` |
| 存储 | J2 microSD/TF 卡引脚 | `pin1=DATA2 -> SDIO_G10_D2`；`pin2=CD/DATA3 -> SDIO_G11_D3`；`pin3=CMD -> SDIO_G13_CMD`；`pin4=VDD -> VCC_3V3`；`pin5=CLK -> SDIO_G12_CK`；`pin6=VSS -> GND`；`pin7=DATA0 -> SDIO_G8_D0`；`pin8=DATA1 -> SDIO_G9_D1`；`pin10=GND` |
| 总线 | SDIO 上拉网络 | `data2=R22 10K`；`data3=R23 10K`；`cmd=R24 10K`；`clock=R25 10K`；`data0=R26 10K`；`data1=R27 10K`；`supply=VCC_3V3` |
| 保护电路 | SDIO 与卡检测保护 | `data_lines=D6 D0; D8 D1; D10 D2; D12 D3`；`control_lines=D7 CK; D9 CMD; D11 TF_DET`；`part_number=ESD5311` |
| GPIO 与控制信号 | 本地 TF_DET 检测节点 | `connector_contact=J2 pin9 K`；`pullup=R13 100K to VCC_3V3`；`filter=C16 2nF/50V to GND` |
| 电源 | VCC_1V2 降压电源 | `input=VCC_5V`；`output=VCC_1V2`；`controller=U1 SY8003`；`inductor=L1 FTC201208S1R0MBCD`；`feedback=R1 150K/1%; R4 150K/1%; C1 22pF/50V`；`output_note=1.2V; I max out=3A` |
| 电源 | 1V2_EN 配置 | `enable_net=1V2_EN`；`installed_path=R3 0R to VCC_5V`；`nc_path=R2 NC to VCC_3V3` |
| 电源 | 1.2 V 电源域分配 | `fb1=VDD`；`fb3=VCC12_TX`；`fb5=VCC12A_RX`；`part_number=BLM15PX800SN1D` |
| 电源 | 3.3 V 电源域分配 | `fb2=VCC33_TX`；`fb4=VCC33_RX`；`input_capacitor=C4 100nF/25V`；`part_number=BLM15PX800SN1D` |
| 电源 | LT6911D 分域去耦 | `vcc33_tx=C19 10uF/10V; C20/C21/C22/C24/C25 100nF/25V`；`vcc33_rx=C26 10uF/10V; C27/C28 100nF/25V`；`vdd=C29 10uF/10V; C30/C31/C32 100nF/25V`；`vcc12a_rx=C36 10uF/10V; C37/C38/C39/C33 100nF/25V`；`vcc12_tx=C40 10uF/10V; C41/C42/C43/C34 100nF/25V` |
| 时钟 | LT6911D 晶体时钟 | `crystal=X1 24MHz(XL7EL89CKI-111YLC-24M)`；`series_resistor=R7 0R`；`feedback_resistor=R9 1M`；`load_capacitors=C7 8pF/50V; C11 8pF/50V` |
| 模拟电路 | LT6911D REXT | `pin=U3 pin60 REXT`；`resistor=R19 7.68K/1%` |
| 复位 | LT6911D RST_N 上电网络 | `reset_pin=U3 pin20 RST_N`；`pullup=R16 1K to VCC_3V3`；`capacitor=C17 1uF/16V to GND` |
| 复位 | RST_1V8 到 RST_N 接口 | `input=RST_1V8`；`base_resistor=R29 5.1K`；`bjt=Q2 S8050`；`mosfet=Q1 2N7002KM`；`gate_pullup=R28 100K to VCC_3V3`；`output=RST_N` |
| GPIO 与控制信号 | 分辨率变化指示 | `source_pin=U3 pin26 INTIO_GPIO5`；`pulse=200ms high-level`；`series_resistor=R14 0R`；`host_net=G38`；`connector_pin=JP3 pin4` |
| 调试与烧录 | 调试测试点 | `tp3=GND`；`tp4=RST_N`；`tp6=SYS_SCL`；`tp7=SYS_SDA` |
| 系统结构 | 原理图资源完整性 | `attached_pages=1`；`visible_sheet_number=2/2`；`missing_sheet=1/2` |
| 电源 | HDMI_5V 生成路径 | `input=VCC_5V`；`output=HDMI_5V`；`nc_references=U2,C8,C9,C10,R10` |
| 电源 | HDMI DDC 上拉与 RX_5V 供电 | `nc_references=D1,D2`；`resistors=R5 47K; R6 47K; R21 0R`；`nets=HDMI_5V; RX_5V; RX_SCL; RX_SDA` |
| GPIO 与控制信号 | 主机侧 TF 卡检测 | `host_net=G37_TF_DET`；`local_net=TF_DET`；`link=R15 NC`；`host_pin=JP3 pin5` |
| 接口 | 支持的视频输入时序 | `source_claim=1280 x 720 @ 60Hz; 1920 x 1080 @ 30Hz`；`schematic_annotation=not shown` |
| 电源 | USB 对外带载能力 | `source_claim=5V@0.5A`；`schematic_limit_note=680mA` |
| 电源 | 整机待机与工作功耗 | `standby_claim=DC 5V@30.75mA`；`working_claim=DC 5V@388.13mA`；`schematic_measurement=not shown` |
| 接口 | 24P FPC 机械规格与主机兼容性 | `source_claim=24P FPC, 0.5mm pitch, Unit PoE-P4`；`schematic_label=JP1 CON24_FPC` |

## 待确认事项

- `uncertain.asset_completeness`：asset_manifest 仅附着当前一张图，而该图标题栏标为 2/2；Sheet 1/2 未在本产品资源清单中出现，因此无法确认未附页所包含的电路范围。（证据：图 77cf16236c92 / 第 1 页 / 第1页 D7-D8 标题栏显示 2/2；asset_manifest 仅列出此页）
- `uncertain.hdmi_5v_path`：POWER 5V 分区画出 VCC_5V 经 U2 到 HDMI_5V 的通路，但 U2、C8、C9、C10、R10 均标注 NC，当前装配版是否生成 HDMI_5V 未确认。（证据：图 77cf16236c92 / 第 1 页 / 第1页 B1-B2，POWER 5V 分区全部器件的 NC 标注）
- `uncertain.hdmi_ddc_pullup_supply`：HDMI_5V 到 RX_5V/DDC 上拉网络之间的 D1、D2 均标注 NC；R5/R6 为 47K、R21 为 0R，但当前装配的 DDC 上拉供电路径未确认。（证据：图 77cf16236c92 / 第 1 页 / 第1页 A7-A8，D1/D2 NC、R5/R6/R21 与 RX_5V/RX_SCL/RX_SDA）
- `uncertain.host_tf_detect`：G37_TF_DET 到本地 TF_DET 的串联位置 R15 标注 NC，因此 JP3 pin5 是否能读取 J2 卡检测触点状态未确认。（证据：图 77cf16236c92 / 第 1 页 / 第1页 C2 与 C7，R15 NC、G37_TF_DET、TF_DET、JP3 pin5）
- `uncertain.video_timings`：源文档声明 1280 x 720 @ 60Hz 与 1920 x 1080 @ 30Hz，但当前附着原理图未标注输入时序或分辨率能力，需由器件资料或硬件测试确认。（证据：图 77cf16236c92 / 第 1 页 / 第1页 LT6911D 与 HDMI/MIPI 分区未见时序或分辨率参数；源文档产品特性/规格参数含该声明）
- `uncertain.usb_load_rating`：源文档声明 USB 带载能力为 5V@0.5A，图面仅给出 U4 的 680mA 限流设计注记；连接器、电源压降与整机条件下的 0.5A 带载结果仍需实测确认。（证据：图 77cf16236c92 / 第 1 页 / 第1页 B1-B2，U4 MT9700-N、R12 10K 与 680mA 限流注记；源文档规格参数含 5V@0.5A）
- `uncertain.power_consumption`：源文档列出 DC 5V@30.75mA 待机功耗和 DC 5V@388.13mA 工作功耗，当前原理图只描述电源拓扑，未提供这两项整机测量条件或结果。（证据：图 77cf16236c92 / 第 1 页 / 第1页 POWER 1V2/POWER 5V 仅含电路与限流注记；源文档规格参数含功耗声明）
- `uncertain.fpc_mechanical`：源文档声明 24P FPC 为 0.5mm 间距并适配 Unit PoE-P4，图面只标注 JP1=CON24_FPC 及其电气引脚，未给出间距、触点方向和机械配合尺寸。（证据：图 77cf16236c92 / 第 1 页 / 第1页 C7-D8，JP1 仅标 CON24_FPC 与电气引脚；源文档规格参数/包装内容含 0.5mm 声明）
- `review.asset_completeness`：能否补充该原理图的 Sheet 1/2，并确认资源清单已覆盖完整设计？；原因：现有唯一页面标题栏为 2/2，未附页面会限制对整板架构和其他电路的完整核对。
- `review.hdmi_5v_path`：量产装配中 U2 及其 NC 外围是否贴装，HDMI_5V 由哪一路实际生成？；原因：该分区的电源器件和全部外围均标注 NC，图面无法证明实际 HDMI_5V 通路。
- `review.hdmi_ddc_pullup_supply`：D1/D2 的量产装配状态及 RX_5V、RX_SCL、RX_SDA 的实际上拉供电路径是什么？；原因：D1/D2 标注 NC，而 R5/R6/R21 仍保留在图中，不能仅凭连线确认当前装配拓扑。
- `review.host_tf_detect`：R15 是否在量产板上贴装，JP3 pin5 的 G37_TF_DET 是否应连接本地 TF_DET？；原因：R15 明确标注 NC，使主机侧 G37_TF_DET 与卡座检测节点在图示装配状态下断开。
- `review.video_timings`：当前硬件与固件组合是否已验证 720p60 和 1080p30 HDMI 输入时序？；原因：这些性能参数来自源文档，原理图未提供时序能力或测试结果。
- `review.usb_load_rating`：USB1 在整机工作条件下的 5V@0.5A 带载能力是否有压降、温升和保护动作测试记录？；原因：图面只确认 U4 的 680mA 限流设计，不能替代端口额定带载验证。
- `review.power_consumption`：待机 30.75mA 和工作 388.13mA 的测试配置、屏幕状态、视频时序及统计边界是什么？；原因：功耗数值来自源文档，当前原理图没有整机测量条件。
- `review.fpc_mechanical`：JP1 的 0.5mm 间距、触点方向、线缆方向和 Unit PoE-P4 机械兼容性由哪份连接器或装配图确认？；原因：器件级原理图只给出 CON24_FPC 电气连接，不含机械接口细节。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `77cf16236c929ab6319960b70476507679474b940981415dd7ceeb6ad3a1c84a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1265/SCH_UnitPoEP4_display_in_V0.3_SCH_PDF_20260326_2026_03_26_16_04_18_page_01.png` |

---

源文档：`zh_CN/addon/AddOn_Display_In_For_PoE-P4.md`

源文档 SHA-256：`53863546dde232609a3fd40d9d42e6b4d1c055bc352a11f01d43792193ea0d93`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
