# LLM630 Compute Kit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | LLM630 Compute Kit |
| SKU | K143 |
| 产品 ID | `llm630-compute-kit-6280ac7a8617` |
| 源文档 | `zh_CN/core/LLM630 Compute Kit.md` |

## 概述

LLM630 Compute Kit 当前原理图展示 AX630C 计算模组的底板接口：中央多针模组连接器引出 MIPI DSI/CSI、音频、TF、I2C、UART、以太网 MDI 和电源控制。底板集成双 USB-C、CH9102F、AW32001ECSR 充电、BQ27220YZFR 电量计、BMI270、NS4150B、LCD/Camera 电源与电平转换、microSD、双 Grove、RJ45 磁性接口及按键/LED/电源时序控制。SYS_I2C_SCL/SDA 连接充电、电量计、BMI270、PI4IOE5V6408 与 MIPI 外设控制，CAM 使用 2.8V/1.2V/1.8V，LCD 使用 3.3V 与背光驱动。AX630C/NPU、4GB LPDDR4、32GB eMMC、ESP32-C6/JL2101 以及性能和软件能力位于模组或正文范围，当前底板页不能直接验证。

## 检索关键词

`LLM630 Compute Kit`、`K143`、`AX630C`、`AW32001ECSR`、`BQ27220YZFR`、`BMI270`、`NS4150B`、`CH9102F`、`PI4IOE5V6408`、`PMS150G-U6`、`AW99703CSR`、`WL2863E28-5/TR`、`ME6211A12M3G-N`、`TXS0102DCUR`、`MIPI DSI`、`MIPI CSI`、`MIPI_TX0`、`MIPI_RX0`、`CAM_2.8V`、`CAM_1.2V`、`CAM_1.8V`、`LCD_LEDA`、`LCD_KEY`、`SYS_I2C_SCL`、`SYS_I2C_SDA`、`TRM_TXD`、`TRM_RXD`、`USB_D_P`、`USB_D_N`、`OTG_DP`、`OTG_DM`、`microSD`、`TF_CLK`、`TF_CMD`、`RJ45`、`MDI0`、`MDI1`、`SOC_VIN`、`SYS_VIN`、`SYS_VBAT`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| AX630C 模组连接器 | 未标注 | 中央多针计算模组接口，承载电源、MIPI、音频、TF、I2C、UART 与以太网 MDI | 图 40ac0b8ed636 / 第 1 页 / 网格 A3-C4，中央 74 针模组连接器，SOC_VIN/MIPI/AUDIO/TF/I2C/MDI 网络 |
| USB 调试口 | USB C 16P Horizontal | USB_VIN 与 USB_D_P/USB_D_N 的 Type-C 调试/串口接口 | 图 40ac0b8ed636 / 第 1 页 / 网格 A1，左上 USB C 16P Horizontal、USB_VIN、USB_D_P/N |
| U4 | CH9102F | USB_D_P/USB_D_N 到 DBG_RXD/DBG_TXD 的 USB-UART 桥 | 图 40ac0b8ed636 / 第 1 页 / 网格 A2，U4 CH9102F、USB_D_P/N、DBG_RXD/DBG_TXD |
| OTG USB-C | USB C 16P Horizontal | OTG_VBUS、OTG_DP/OTG_DM 的第二路 Type-C 接口 | 图 40ac0b8ed636 / 第 1 页 / 网格 A1-B1，左侧第二个 USB C 16P Horizontal、OTG_VBUS/DP/DM |
| D4,D5 | ESD0524P | 两路 USB-C 数据/CC 信号的多通道 ESD 保护 | 图 40ac0b8ed636 / 第 1 页 / 网格 A1-B1，D4/D5 ESD0524P 与 USB/OTG 数据线 |
| U6,U16 | LPW5209AB5F | 受 OTG_EN 控制的 USB/系统电源开关路径 | 图 40ac0b8ed636 / 第 1 页 / 网格 A2-B3，U6/U16 LPW5209AB5F、OTG_VBUS/SOC_VIN/SYS_VIN 与 Q4/Q8 |
| J1 | 1.25mm 5P | AGND、麦克风差分输入与 SPK_P/SPK_N 音频接口 | 图 40ac0b8ed636 / 第 1 页 / 网格 B1，AUDIO J1 5P、AGND、AUDIO_IN_L_P/N、SPK_P/N |
| U14 | NS4150B | AUDIO_OUT_L_P/N 到 SPK_P/SPK_N 的差分 D 类扬声器功放 | 图 40ac0b8ed636 / 第 1 页 / 网格 B2-C3，U14 NS4150B、INP/INN、SPK_EN、SPK_P/N |
| J2 | 1.25mm 2P | EXT_VBAT 与 GND 的外接电池接口 | 图 40ac0b8ed636 / 第 1 页 / 网格 B1，BAT J2、EXT_VBAT 与保护器件 |
| U3 | AW32001ECSR | SYS_VIN 输入、SYS_VBAT 输出并连接 SYS_I2C 的电池充电管理器 | 图 40ac0b8ed636 / 第 1 页 / 网格 C2-C3，U3 AW32001ECSR、SYS_VIN/SYS_VBAT、SYS_I2C_SCL/SDA |
| U8 | BQ27220YZFR | SYS_VBAT/EXT_VBAT 电量检测并通过 SYS_I2C 通信 | 图 40ac0b8ed636 / 第 1 页 / 网格 C3-C4，U8 BQ27220YZFR、SRP/SRN、BAT、SYS_I2C_SCL/SDA |
| U9 | BMI270 | SYS_I2C_SCL/SDA 六轴惯性传感器 | 图 40ac0b8ed636 / 第 1 页 / 网格 C4，U9 BMI270、SYS_I2C_SCL/SDA、SOC_3.3V |
| U7 | PI4IOE5V6408 | SYS_I2C 八位 GPIO 扩展器，控制 LCD/CAM 复位、系统 LED、电源与外部 LED 网络 | 图 40ac0b8ed636 / 第 1 页 / 网格 D2-D3，U7 PI4IOE5V6408、P0-P7、SYS_I2C_SCL/SDA |
| U2 | PMS150G-U6 | MPWR_EN/SW_PWR/BOOT_RST 等电源按键与时序辅助控制器 | 图 40ac0b8ed636 / 第 1 页 / 网格 D1-D2，U2 PMS150G-U6、MPWR_EN/SW_PWR/BOOT_RST |
| U1 | WPN3012H2R2MT | SYS_VBUS 输入、MPWR_EN 控制并输出 SOC_VIN 的 DC/DC | 图 40ac0b8ed636 / 第 1 页 / 网格 C1-C2，U1 WPN3012H2R2MT、SYS_VBUS、MPWR_EN、SOC_VIN |
| U10 | AW99703CSR | SYS_I2C 控制的 LCD 背光升压/LED 驱动器，输出 LCD_LEDA/LCD_LEDK | 图 40ac0b8ed636 / 第 1 页 / 网格 A6，U10 AW99703CSR、SYS_I2C、LCD_LEDA/LCD_LEDK |
| J11 | FPC-24P | MIPI DSI LCD、I2C、触摸中断/复位和显示电源接口 | 图 40ac0b8ed636 / 第 1 页 / 网格 A7-A8，J11 FPC-24P、MIPI_TX、SYS_I2C、TP_INT/TP_RST、LCD_LEDA/LEDK |
| U12 | WL2863E28-5/TR | CAM_VIN 输入、CAM_2.8V 输出的摄像头 LDO | 图 40ac0b8ed636 / 第 1 页 / 网格 B6-B7，U12 WL2863E28-5/TR、CAM_VIN、CAM_2.8V |
| U11 | ME6211A12M3G-N | CAM_1.8V 输入、CAM_1.2V 输出的摄像头 LDO | 图 40ac0b8ed636 / 第 1 页 / 网格 B6-C7，U11 ME6211A12M3G-N、CAM_1.8V、CAM_1.2V |
| U13 | TXS0102DCUR | SOC_3.3V 与 CAM_1.8V 之间的 CAM_SCL/CAM_SDA 双向电平转换 | 图 40ac0b8ed636 / 第 1 页 / 网格 C7-C8，U13 TXS0102DCUR、CAM_SCL/CAM_SDA、CAM_1.8V |
| CAM 连接器 | FPC-30P | 四通道 MIPI CSI、时钟、I2C、复位和 2.8V/1.8V/1.2V 电源接口 | 图 40ac0b8ed636 / 第 1 页 / 网格 B7-C8，CAM FPC-30P、MIPI_RX0-RX3、CAM_MCLK/RSTN/SCL/SDA 与电源 |
| J8,J9 | GROVE CON4 | 分别引出 TRM_TXD/TRM_RXD 与 SYS_I2C_SDA/SCL 的两路 Grove 接口 | 图 40ac0b8ed636 / 第 1 页 / 网格 C6-C7，J8 BLUE GROVE 与 J9 RED GROVE |
| J14 | RF_COAXIAL | 预留外部射频同轴接口 | 图 40ac0b8ed636 / 第 1 页 / 网格 C5-C6，J14 RF_COAXIAL |
| RJ45 磁性接口 | RMT-410B-10V4-NL-Y | MDI0/MDI1 四对差分网络到 RJ45 与链路 LED 的千兆以太网磁性接口 | 图 40ac0b8ed636 / 第 1 页 / 网格 D5-D7，RMT-410B-10V4-NL-Y、MDI0/MDI1、RJ45 与 LED |
| J10 | TF_CARD_SOCKET | TF_D0-D3、TF_CMD、TF_CLK 与卡检测的 microSD 卡座 | 图 40ac0b8ed636 / 第 1 页 / 网格 D7-D8，J10 TF_CARD_SOCKET、TF_D0-D3/TF_CMD/TF_CLK/SD_DETN |
| S1,S2 | SW | BOOT/用户及系统电源交互按键 | 图 40ac0b8ed636 / 第 1 页 / 网格 D4-D5，S1/S2、BOOT/USER/VIN_DET 网络与绿色 LED |

## 系统结构

### LLM630 Compute Kit 底板架构

中央 AX630C 模组接口连接双 USB-C/CH9102F、MIPI LCD/Camera、音频、TF、I2C、UART、以太网 MDI 和电源控制；底板另集成 AW32001ECSR、BQ27220YZFR、BMI270、PI4IOE5V6408、NS4150B 与 RJ45/microSD/Grove。

- 参数与网络：`compute_interface=central 74-pin AX630C module connector`；`usb_uart=U4 CH9102F`；`power=U1/U3/U6/U16`；`battery=AW32001ECSR + BQ27220YZFR`；`sensor=BMI270`；`audio=NS4150B + J1`；`display=J11 MIPI DSI`；`camera=CAM FPC-30P MIPI CSI`；`network=MDI0/MDI1 RJ45`；`storage=J10 microSD`
- 证据：图 40ac0b8ed636 / 第 1 页 / 完整单页 A1-D8 全部功能分区

## 电源

### USB_VIN、SYS_VIN、OTG_VBUS 与 SOC_VIN

USB 调试口 USB_VIN 经 D2 DSK34 接 SYS_VIN；OTG_VBUS 经受控开关网络连接 SOC_VIN/SYS_VIN；U1 WPN3012H2R2MT 以 SYS_VBUS 为输入、MPWR_EN 为使能并输出 SOC_VIN。

- 参数与网络：`debug_input=USB_VIN -> D2 DSK34 -> SYS_VIN`；`otg_input=OTG_VBUS via U6/U16/Q4/Q8`；`converter=U1 WPN3012H2R2MT`；`converter_input=SYS_VBUS`；`enable=MPWR_EN`；`output=SOC_VIN`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 A1-C2，D2、U6/U16、U1 与 USB_VIN/SYS_VIN/SOC_VIN

### AW32001ECSR 电池充电路径

U3 AW32001ECSR 的 VIN 接 SYS_VIN，BAT 输出 SYS_VBAT，NTC/TS 连接电池温度网络，SCL/SDA 接 SYS_I2C_SCL/SDA；J2 EXT_VBAT 通过保护/开关网络进入系统电池路径。

- 参数与网络：`charger=U3 AW32001ECSR`；`input=SYS_VIN`；`battery_output=SYS_VBAT`；`temperature=NTC/TS network`；`bus=SYS_I2C_SCL/SYS_I2C_SDA`；`external_connector=J2 EXT_VBAT/GND`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 B1-C3，J2/U3/SYS_VIN/SYS_VBAT/SYS_I2C

### LCD 背光驱动

U10 AW99703CSR 由 SOC_VIN 供电，通过 SYS_I2C_SCL/SDA 控制，SW 经 L1 WPN3012H100MT 与 D15 B5819WS 升压形成 LCD_LEDA，并输出 LCD_LEDK 回路到 J11。

- 参数与网络：`driver=U10 AW99703CSR`；`input=SOC_VIN`；`bus=SYS_I2C_SCL/SDA`；`inductor=L1 WPN3012H100MT`；`diode=D15 B5819WS`；`outputs=LCD_LEDA,LCD_LEDK`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 A6-A8，U10/L1/D15/J11 LCD_LEDA/LEDK

### Camera 2.8V、1.8V 与 1.2V

SOC_VIN 经 FB1 进入 CAM_VIN，U12 WL2863E28-5/TR 输出 CAM_2.8V；CAM_1.8V 由模组接口提供并作为 U11 ME6211A12M3G-N 输入，U11 输出 CAM_1.2V；R40 连接 SOC_1.8V 与 CAM_1.8V。

- 参数与网络：`camera_input=SOC_VIN -> FB1 -> CAM_VIN`；`analog=U12 WL2863E28-5/TR -> CAM_2.8V`；`io=SOC_1.8V/R40 -> CAM_1.8V`；`core=U11 ME6211A12M3G-N CAM_1.8V -> CAM_1.2V`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 B6-C8，FB1/U12/U11/R40/CAM rails

## 接口

### J1 麦克风与扬声器接口

J1 5P 引出 AGND、MIC 差分支路 AUDIO_IN_L_P/AUDIO_IN_L_N，以及 SPK_P/SPK_N；麦克风输入经电阻/电容交流耦合到模组 AUDIO_IN_L_P/N，扬声器输出来自 U14 NS4150B。

- 参数与网络：`connector=J1 1.25mm 5P`；`ground=AGND`；`microphone=AUDIO_IN_L_P/AUDIO_IN_L_N`；`speaker=SPK_P/SPK_N`；`amplifier=U14 NS4150B`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 B1-B3，J1 音频接口及输入/功放网络

### 双 Grove 接口

J8 BLUE GROVE pin1/2=GND/SOC_VIN、pin3/4=TRM_TXD/TRM_RXD；J9 RED GROVE pin1/2=GND/SOC_VIN、pin3/4=SYS_I2C_SDA/SYS_I2C_SCL，两接口均配置 ESD0524P 保护。

- 参数与网络：`blue=J8 GND,SOC_VIN,TRM_TXD,TRM_RXD`；`red=J9 GND,SOC_VIN,SYS_I2C_SDA,SYS_I2C_SCL`；`protection=D11/D12 ESD0524P`；`uart_direction=TRM_TXD output,TRM_RXD input`；`i2c_direction=bidirectional`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 C6-C7，J8/J9/D11/D12

### 以太网 MDI 与 RJ45

中央模组的 MDI0_P/N、MDI1_P/N 经 R29-R36 22Ω、TVS4-TVS7 和 RMT-410B-10V4-NL-Y 磁性器件连接 RJ45 J1A-J8D 差分触点，接口还引出绿色/黄色链路 LED。

- 参数与网络：`module_pairs=MDI0_P/N,MDI1_P/N`；`series=R29-R36 22Ω`；`tvs=TVS4-TVS7 W903DLC-B`；`magnetics=RMT-410B-10V4-NL-Y`；`connector=RJ45 J1A-J8D`；`leds=LED_GREEN,link LED`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 D5-D7，MDI0/MDI1/R29-R36/TVS4-TVS7/RJ45

## 总线

### 第二路 USB OTG 硬件

第二个 Type-C 连接器引出 OTG_DP、OTG_DM、OTG_VBUS 与 CC1/CC2，D5 ESD0524P 保护高速/CC 网络；OTG_VBUS 进入 U6/U16 LPW5209AB5F 与 Q4/Q8 组成的受 OTG_EN 控制电源路径。

- 参数与网络：`data=OTG_DP/OTG_DM`；`power=OTG_VBUS`；`cc=OTG_CC1/OTG_CC2`；`esd=D5 ESD0524P`；`switches=U6/U16 LPW5209AB5F,Q4/Q8`；`enable=OTG_EN`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 A1-B3，OTG USB-C/D5/U6/U16/Q4/Q8

### SYS_I2C_SCL/SYS_I2C_SDA

SYS_I2C_SCL/SDA 由中央模组接口引出，并连接 U3 AW32001ECSR、U8 BQ27220YZFR、U9 BMI270、U7 PI4IOE5V6408、U10 LCD 背光驱动、J9 Grove 及 LCD/Camera 控制网络。

- 参数与网络：`controller=AX630C module interface I2C`；`signals=SYS_I2C_SCL,SYS_I2C_SDA`；`devices=AW32001ECSR,BQ27220YZFR,BMI270,PI4IOE5V6408,AW99703CSR`；`external=J9 RED GROVE,LCD/Camera`
- 证据：图 40ac0b8ed636 / 第 1 页 / 完整单页 SYS_I2C_SCL/SDA 网络，网格 A6-D3

### LCD MIPI DSI 与控制

J11 FPC-24P 引出 MIPI_TX0_P/N、MIPI_TX1_P/N、MIPI_TX_C_P/N 两数据通道加时钟，另含 SYS_I2C_SCL/SDA、TP_INT、TP_RST、LCD_RST、LCD_LEDA/LCD_LEDK、SOC_3.3V 和 GND。

- 参数与网络：`connector=J11 FPC-24P`；`lanes=MIPI_TX0,MIPI_TX1`；`clock=MIPI_TX_C`；`control=SYS_I2C_SCL/SDA,TP_INT,TP_RST,LCD_RST`；`power=SOC_3.3V,LCD_LEDA,LCD_LEDK`；`direction=module -> display`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 A7-A8，J11 pins1-24

### Camera MIPI CSI 与控制

CAM FPC-30P 引出 MIPI_RX0-RX3 四数据通道、MIPI_RX_C 时钟、CAM_MCLK、CAM_RSTN、CAM_SCL_1V8/CAM_SDA_1V8，以及 CAM_2.8V/CAM_1.8V/CAM_1.2V 和 GND。

- 参数与网络：`connector=CAM FPC-30P`；`lanes=MIPI_RX0,MIPI_RX1,MIPI_RX2,MIPI_RX3`；`clock=MIPI_RX_C`；`master_clock=CAM_MCLK`；`reset=CAM_RSTN`；`control=CAM_SCL_1V8,CAM_SDA_1V8`；`rails=CAM_2.8V,CAM_1.8V,CAM_1.2V`；`direction=camera -> module`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 B7-C8，CAM FPC-30P pins1-30

### Camera I2C 电平转换

U13 TXS0102DCUR 的 B 侧由 SOC_3.3V 供电并连接 CAM_SCL/CAM_SDA，A 侧由 CAM_1.8V 供电并经 R49/R50 15KΩ 输出 CAM_SCL_1V8/CAM_SDA_1V8。

- 参数与网络：`translator=U13 TXS0102DCUR`；`b_supply=SOC_3.3V`；`b_signals=CAM_SCL,CAM_SDA`；`a_supply=CAM_1.8V`；`a_signals=CAM_SCL_1V8,CAM_SDA_1V8`；`resistors=R49/R50 15KΩ`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 C7-C8，U13/R41/R42/R49/R50

## GPIO 与控制信号

### PI4IOE5V6408 控制网络

U7 PI4IOE5V6408 通过 SYS_I2C 控制 P0-P7，页面标出的输出包括 LCD_RST、LCD_KEY、SYS_LED、VIN_DET、POWER_PULSE 与 EXT_LED；INT 连接 SYS_INT，RESET 有 RC 网络。

- 参数与网络：`device=U7 PI4IOE5V6408`；`bus=SYS_I2C_SCL/SDA`；`outputs=LCD_RST,LCD_KEY,SYS_LED,VIN_DET,POWER_PULSE,EXT_LED`；`interrupt=SYS_INT`；`reset=RC reset network`；`supply=SOC_3.3V`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 D2-D3，U7 PI4IOE5V6408 P0-P7

## 复位

### 电源按键、Boot 与复位控制

U2 PMS150G-U6 连接 MPWR_EN、SW_PWR 与 BOOT_RST；下方 Q1-Q5/D3-D8/R/C 网络形成 PWRKEY_PULSE、BOOT_CTRL、SYS_VBUS 与 SOC_3.3V 的电源/复位时序，S1/S2 提供用户与电源交互。

- 参数与网络：`controller=U2 PMS150G-U6`；`signals=MPWR_EN,SW_PWR,BOOT_RST,PWRKEY_PULSE,BOOT_CTRL`；`switches=Q1-Q5`；`buttons=S1,S2`；`rails=SYS_VBUS,SOC_3.3V`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 D1-D5，U2、Q1-Q5、D3-D8、S1/S2 与 Boot/Power 网络

## 保护电路

### 外部接口 ESD 与滤波

两路 USB 使用 D4/D5 ESD0524P，Grove 使用 D11/D12，microSD 使用 D13/D14；以太网四对差分线使用 TVS4-TVS7，音频/电源/MIPI 接口还配置磁珠、串联电阻和去耦电容。

- 参数与网络：`usb=D4,D5 ESD0524P`；`grove=D11,D12 ESD0524P`；`microsd=D13,D14 ESD0524P`；`ethernet=TVS4-TVS7 W903DLC-B`；`other=ferrite beads,series resistors,decoupling`
- 证据：图 40ac0b8ed636 / 第 1 页 / 完整单页各外部连接器周边保护器件

## 存储

### microSD 四位接口

J10 TF_CARD_SOCKET 引出 TF_D0、TF_D1、TF_D2、TF_D3、TF_CMD、TF_CLK、SD_DETN 和 TF_VDD；D13/D14 ESD0524P 保护数据/命令/时钟，R43/R44/R45 为相关串联或上拉网络。

- 参数与网络：`connector=J10 TF_CARD_SOCKET`；`data=TF_D0,TF_D1,TF_D2,TF_D3`；`command=TF_CMD`；`clock=TF_CLK`；`detect=SD_DETN`；`supply=TF_VDD`；`esd=D13/D14 ESD0524P`；`resistors=R43/R44/R45`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 D7-D8，D13/D14/R43-R45/J10

## 音频

### NS4150B 扬声器功放

模组 AUDIO_OUT_L_P/N 经 R55/R56 47KΩ 和 C4/C5 100nF 进入 U14 NS4150B INP/INN，SPK_EN 控制 CTRL；U14 VOP/VON 经 FB2/FB3 输出 SPK_P/SPK_N，供电为 SOC_VIN。

- 参数与网络：`amplifier=U14 NS4150B`；`inputs=AUDIO_OUT_L_P/N via R55/R56 47KΩ,C4/C5 100nF`；`enable=SPK_EN`；`outputs=VOP/VON -> FB2/FB3 -> SPK_P/SPK_N`；`supply=SOC_VIN`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 B2-C3，U14/R55/R56/C4/C5/FB2/FB3

## 传感器

### BMI270 六轴传感器

U9 BMI270 由 SOC_3.3V 供电，SCx/SDx 接 SYS_I2C_SCL/SDA；INT1/INT2 引脚在本页未连接，CSB 接 SOC_3.3V。

- 参数与网络：`sensor=U9 BMI270`；`supply=SOC_3.3V`；`scl=SYS_I2C_SCL`；`sda=SYS_I2C_SDA`；`csb=SOC_3.3V`；`interrupts=INT1/INT2 not connected`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 C4，U9 BMI270、SOC_3.3V、SYS_I2C

## 调试与烧录

### USB-C 调试串口

USB 调试 Type-C 的 DP/DM 形成 USB_D_P/USB_D_N，经 D4 ESD0524P 保护后连接 U4 CH9102F DP/DM；U4 TXD 经 R19 1KΩ 接 DBG_RXD，RXD 经 R20 1KΩ 接 DBG_TXD，并由 USB_VIN 供电。

- 参数与网络：`connector=USB C 16P Horizontal`；`bridge=U4 CH9102F`；`usb=USB_D_P/USB_D_N`；`uart=TXD -> R19 1KΩ -> DBG_RXD; RXD -> R20 1KΩ -> DBG_TXD`；`esd=D4 ESD0524P`；`supply=USB_VIN`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 A1-A3，USB 调试口/D4/U4/R19/R20

## 模拟电路

### BQ27220 电量检测

U8 BQ27220YZFR 的 SRP/SRN 跨接电池采样电阻，BAT/VDD 接 SYS_VBAT/EXT_VBAT 电池路径，SCL/SDA 接 SYS_I2C；R25 标注 R010/1% 作为电流采样元件。

- 参数与网络：`gauge=U8 BQ27220YZFR`；`bus=SYS_I2C_SCL/SYS_I2C_SDA`；`sense=SRP/SRN`；`shunt=R25 R010/1%`；`battery_nets=SYS_VBAT,EXT_VBAT`
- 证据：图 40ac0b8ed636 / 第 1 页 / 网格 C3-C4，U8/R25/SYS_VBAT/EXT_VBAT

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | LLM630 Compute Kit 底板架构 | `compute_interface=central 74-pin AX630C module connector`；`usb_uart=U4 CH9102F`；`power=U1/U3/U6/U16`；`battery=AW32001ECSR + BQ27220YZFR`；`sensor=BMI270`；`audio=NS4150B + J1`；`display=J11 MIPI DSI`；`camera=CAM FPC-30P MIPI CSI`；`network=MDI0/MDI1 RJ45`；`storage=J10 microSD` |
| 调试与烧录 | USB-C 调试串口 | `connector=USB C 16P Horizontal`；`bridge=U4 CH9102F`；`usb=USB_D_P/USB_D_N`；`uart=TXD -> R19 1KΩ -> DBG_RXD; RXD -> R20 1KΩ -> DBG_TXD`；`esd=D4 ESD0524P`；`supply=USB_VIN` |
| 总线 | 第二路 USB OTG 硬件 | `data=OTG_DP/OTG_DM`；`power=OTG_VBUS`；`cc=OTG_CC1/OTG_CC2`；`esd=D5 ESD0524P`；`switches=U6/U16 LPW5209AB5F,Q4/Q8`；`enable=OTG_EN` |
| 电源 | USB_VIN、SYS_VIN、OTG_VBUS 与 SOC_VIN | `debug_input=USB_VIN -> D2 DSK34 -> SYS_VIN`；`otg_input=OTG_VBUS via U6/U16/Q4/Q8`；`converter=U1 WPN3012H2R2MT`；`converter_input=SYS_VBUS`；`enable=MPWR_EN`；`output=SOC_VIN` |
| 接口 | J1 麦克风与扬声器接口 | `connector=J1 1.25mm 5P`；`ground=AGND`；`microphone=AUDIO_IN_L_P/AUDIO_IN_L_N`；`speaker=SPK_P/SPK_N`；`amplifier=U14 NS4150B` |
| 音频 | NS4150B 扬声器功放 | `amplifier=U14 NS4150B`；`inputs=AUDIO_OUT_L_P/N via R55/R56 47KΩ,C4/C5 100nF`；`enable=SPK_EN`；`outputs=VOP/VON -> FB2/FB3 -> SPK_P/SPK_N`；`supply=SOC_VIN` |
| 电源 | AW32001ECSR 电池充电路径 | `charger=U3 AW32001ECSR`；`input=SYS_VIN`；`battery_output=SYS_VBAT`；`temperature=NTC/TS network`；`bus=SYS_I2C_SCL/SYS_I2C_SDA`；`external_connector=J2 EXT_VBAT/GND` |
| 模拟电路 | BQ27220 电量检测 | `gauge=U8 BQ27220YZFR`；`bus=SYS_I2C_SCL/SYS_I2C_SDA`；`sense=SRP/SRN`；`shunt=R25 R010/1%`；`battery_nets=SYS_VBAT,EXT_VBAT` |
| 总线 | SYS_I2C_SCL/SYS_I2C_SDA | `controller=AX630C module interface I2C`；`signals=SYS_I2C_SCL,SYS_I2C_SDA`；`devices=AW32001ECSR,BQ27220YZFR,BMI270,PI4IOE5V6408,AW99703CSR`；`external=J9 RED GROVE,LCD/Camera` |
| 传感器 | BMI270 六轴传感器 | `sensor=U9 BMI270`；`supply=SOC_3.3V`；`scl=SYS_I2C_SCL`；`sda=SYS_I2C_SDA`；`csb=SOC_3.3V`；`interrupts=INT1/INT2 not connected` |
| GPIO 与控制信号 | PI4IOE5V6408 控制网络 | `device=U7 PI4IOE5V6408`；`bus=SYS_I2C_SCL/SDA`；`outputs=LCD_RST,LCD_KEY,SYS_LED,VIN_DET,POWER_PULSE,EXT_LED`；`interrupt=SYS_INT`；`reset=RC reset network`；`supply=SOC_3.3V` |
| 复位 | 电源按键、Boot 与复位控制 | `controller=U2 PMS150G-U6`；`signals=MPWR_EN,SW_PWR,BOOT_RST,PWRKEY_PULSE,BOOT_CTRL`；`switches=Q1-Q5`；`buttons=S1,S2`；`rails=SYS_VBUS,SOC_3.3V` |
| 总线 | LCD MIPI DSI 与控制 | `connector=J11 FPC-24P`；`lanes=MIPI_TX0,MIPI_TX1`；`clock=MIPI_TX_C`；`control=SYS_I2C_SCL/SDA,TP_INT,TP_RST,LCD_RST`；`power=SOC_3.3V,LCD_LEDA,LCD_LEDK`；`direction=module -> display` |
| 电源 | LCD 背光驱动 | `driver=U10 AW99703CSR`；`input=SOC_VIN`；`bus=SYS_I2C_SCL/SDA`；`inductor=L1 WPN3012H100MT`；`diode=D15 B5819WS`；`outputs=LCD_LEDA,LCD_LEDK` |
| 总线 | Camera MIPI CSI 与控制 | `connector=CAM FPC-30P`；`lanes=MIPI_RX0,MIPI_RX1,MIPI_RX2,MIPI_RX3`；`clock=MIPI_RX_C`；`master_clock=CAM_MCLK`；`reset=CAM_RSTN`；`control=CAM_SCL_1V8,CAM_SDA_1V8`；`rails=CAM_2.8V,CAM_1.8V,CAM_1.2V`；`direction=camera -> module` |
| 电源 | Camera 2.8V、1.8V 与 1.2V | `camera_input=SOC_VIN -> FB1 -> CAM_VIN`；`analog=U12 WL2863E28-5/TR -> CAM_2.8V`；`io=SOC_1.8V/R40 -> CAM_1.8V`；`core=U11 ME6211A12M3G-N CAM_1.8V -> CAM_1.2V` |
| 总线 | Camera I2C 电平转换 | `translator=U13 TXS0102DCUR`；`b_supply=SOC_3.3V`；`b_signals=CAM_SCL,CAM_SDA`；`a_supply=CAM_1.8V`；`a_signals=CAM_SCL_1V8,CAM_SDA_1V8`；`resistors=R49/R50 15KΩ` |
| 接口 | 双 Grove 接口 | `blue=J8 GND,SOC_VIN,TRM_TXD,TRM_RXD`；`red=J9 GND,SOC_VIN,SYS_I2C_SDA,SYS_I2C_SCL`；`protection=D11/D12 ESD0524P`；`uart_direction=TRM_TXD output,TRM_RXD input`；`i2c_direction=bidirectional` |
| 接口 | 以太网 MDI 与 RJ45 | `module_pairs=MDI0_P/N,MDI1_P/N`；`series=R29-R36 22Ω`；`tvs=TVS4-TVS7 W903DLC-B`；`magnetics=RMT-410B-10V4-NL-Y`；`connector=RJ45 J1A-J8D`；`leds=LED_GREEN,link LED` |
| 存储 | microSD 四位接口 | `connector=J10 TF_CARD_SOCKET`；`data=TF_D0,TF_D1,TF_D2,TF_D3`；`command=TF_CMD`；`clock=TF_CLK`；`detect=SD_DETN`；`supply=TF_VDD`；`esd=D13/D14 ESD0524P`；`resistors=R43/R44/R45` |
| 保护电路 | 外部接口 ESD 与滤波 | `usb=D4,D5 ESD0524P`；`grove=D11,D12 ESD0524P`；`microsd=D13,D14 ESD0524P`；`ethernet=TVS4-TVS7 W903DLC-B`；`other=ferrite beads,series resistors,decoupling` |
| 系统结构 | AX630C、NPU、LPDDR4、eMMC 与无线/PHY | `documented_soc=AX630C dual Cortex-A53 1.2GHz`；`documented_npu=3.2TOPs INT8,12.8TOPs INT4`；`documented_ram=4GB LPDDR4`；`documented_emmc=32GB eMMC5.1`；`documented_wifi=ESP32-C6`；`documented_ethernet_phy=JL2101B-N040C`；`schematic_internal_parts=null` |
| 总线地址 | 底板 I2C 设备地址 | `charger=AW32001ECSR`；`gauge=BQ27220YZFR`；`imu=BMI270`；`expander=PI4IOE5V6408`；`backlight=AW99703CSR`；`addresses=null` |
| 电源 | 3.7V 电池与充放电边界 | `documented_battery=3.7V lithium`；`connector=J2 1.25mm 2P`；`charger=AW32001ECSR`；`gauge=BQ27220YZFR`；`capacity=null`；`chemistry=null`；`protection=null`；`charge_current=null`；`termination_voltage=null` |
| 核心器件 | MIPI 显示与摄像头性能 | `documented_dsi=2-lane max 1080p@30fps`；`documented_csi=4-lane max 4K@30fps`；`schematic_dsi_lanes=2`；`schematic_csi_lanes=4`；`display_model=null`；`camera_model=null`；`validated_timing=null` |
| 音频 | 麦克风、功放与全双工音频性能 | `microphone_model=null`；`amplifier=NS4150B`；`documented_mode=full duplex`；`mic_sensitivity=null`；`mic_snr=null`；`speaker_impedance=null`；`speaker_power=null`；`sample_rate=null`；`thd=null` |
| 射频 | Wi-Fi、SMA 与千兆网络性能 | `documented_wifi=ESP32-C6 2.4GHz`；`documented_antenna=SMA`；`documented_ethernet=JL2101B-N040C 1GbE`；`documented_bridge=Wi-Fi/Ethernet bridge`；`schematic_rf=J14 RF_COAXIAL only`；`schematic_phy=null`；`throughput=null`；`gain=null`；`certification=null` |
| 其他事实 | StackFlow 与 AI 模型能力 | `documented_framework=StackFlow`；`documented_models=Yolov11,DepthAnything,InternVL2.5,Qwen2.5,Llama3.2,Whisper,MeloTTS`；`firmware_version=null`；`api_version=null`；`model_versions=null`；`latency=null`；`concurrency=null`；`update_behavior=null` |
| 其他事实 | USB Host/Device 与 OTG 行为 | `documented_usb=USB 2.0 Host or Device,OTG`；`data=OTG_DP/OTG_DM`；`power=OTG_VBUS via LPW5209AB5F/Q4/Q8`；`role_detection=null`；`current_limit=null`；`protocol_stack=null`；`supported_classes=null` |

## 待确认事项

- `system.documented-compute-module`：正文称计算模组包含 AX630C、3.2TOPs INT8 NPU、4GB LPDDR4、32GB eMMC、ESP32-C6 与 JL2101B-N040C；当前原理图仅展示底板到模组的接口网络，没有这些芯片的位号、供电、内存总线或模组内部连接。（证据：图 40ac0b8ed636 / 第 1 页 / 中央模组连接器仅引出接口，整页无 AX630C/LPDDR4/eMMC/ESP32-C6/JL2101 器件本体）
- `address.system-i2c-devices`：原理图确认 AW32001ECSR、BQ27220YZFR、BMI270、PI4IOE5V6408 和 AW99703CSR 共用 SYS_I2C，但页面没有标注任何 7 位地址或地址选择状态。（证据：图 40ac0b8ed636 / 第 1 页 / SYS_I2C_SCL/SDA 连接的 U3/U8/U9/U7/U10 区域，无地址文字）
- `power.documented-battery-spec`：正文称可接 3.7V 锂电池并使用 AW32001ECSR/BQ27220YZFR；原理图确认 J2、充电和电量采样路径，但未给出电芯容量、化学体系、极性容错、保护板、充电电流/终止电压、温度范围或续航。（证据：图 40ac0b8ed636 / 第 1 页 / 网格 B1-C4，J2/U3/U8 电池路径，无电芯与充电性能表）
- `component.documented-mipi-performance`：正文称 DSI 为 2-lane、最高 1080p@30fps，CSI 为 4-lane、最高 4K@30fps；原理图确认两路 DSI 数据通道和四路 CSI 数据通道，但不能证明面板/摄像头兼容型号、分辨率、帧率、时序或信号完整性余量。（证据：图 40ac0b8ed636 / 第 1 页 / 网格 A7-C8，J11 LCD 与 CAM FPC 的 MIPI 差分网络，无性能表）
- `audio.documented-performance`：正文称底板支持麦克风、扬声器和全双工通信；原理图只确认模拟麦克风差分接口和 NS4150B 扬声器功放连接，未标麦克风型号、灵敏度/SNR、扬声器阻抗/功率、采样率或整机失真。（证据：图 40ac0b8ed636 / 第 1 页 / 网格 B1-C3，J1/U14 音频电路，无性能参数）
- `rf.documented-network-performance`：正文称 ESP32-C6 2.4GHz Wi-Fi、SMA 天线、JL2101B-N040C 1GbE 和 Wi-Fi/以太网桥接；当前底板页只画 J14 RF_COAXIAL、MDI0/MDI1 与 RJ45 磁性接口，未画无线芯片/PHY 或给出增益、吞吐、桥接行为与认证。（证据：图 40ac0b8ed636 / 第 1 页 / 网格 C5-D7，J14 与 MDI/RJ45 区，无 ESP32-C6/JL2101B 器件）
- `other.documented-stackflow-models`：正文描述 StackFlow、视觉/语音/LLM pipeline、模型热更新和多种具体模型；原理图只能证明底板硬件接口，不能验证系统镜像、API、模型版本、推理性能、并发、更新机制或后续支持计划。（证据：图 40ac0b8ed636 / 第 1 页 / 完整底板原理图，无软件/模型/性能信息）
- `other.documented-usb-behavior`：正文称 USB 2.0 可作为 Host 或 Device 并支持 OTG；原理图确认 OTG_DP/DM、OTG_VBUS 和受控电源开关，但不能证明角色检测、VBus 电流限制、协议栈、支持设备类别或量产固件行为。（证据：图 40ac0b8ed636 / 第 1 页 / 网格 A1-B3，OTG USB-C 与电源开关硬件，无软件行为）
- `review.compute-module`：请提供 AX630C 计算模组原理图/BOM，确认 AX630C、NPU、4GB LPDDR4、32GB eMMC、ESP32-C6 与 JL2101B-N040C 的具体连接和料号。；原因：当前资源仅为底板接口页。
- `review.i2c-addresses`：AW32001ECSR、BQ27220YZFR、BMI270、PI4IOE5V6408 与 AW99703CSR 的量产 7 位 I2C 地址及地址脚状态是什么？；原因：原理图未标地址。
- `review.battery-spec`：请确认支持电芯的容量/化学体系/极性/保护板，以及 AW32001ECSR 充电电流、终止条件、温度保护和 BQ27220 配置。；原因：原理图没有电芯与充放电安全边界。
- `review.mipi-performance`：请确认已验证的 DSI/CSI 面板和摄像头型号、lane速率、分辨率、帧率、时序与信号完整性测试结果。；原因：连接图只能确认 lane 数和网络。
- `review.audio-performance`：请用麦克风/扬声器 BOM、NS4150B datasheet 和整机实测确认全双工、灵敏度、SNR、阻抗、功率、采样率与失真。；原因：原理图仅显示模拟输入和功放连接。
- `review.network-rf`：请提供 ESP32-C6/JL2101B-N040C 模组证据、SMA/射频路径、天线增益、1GbE吞吐、桥接固件行为和认证结果。；原因：当前底板页只显示 RF_COAXIAL 和 MDI/RJ45 接口。
- `review.stackflow-models`：当前系统镜像、StackFlow/API 和各 AI 模型的正式版本、资源占用、性能、并发与热更新边界是什么？；原因：软件能力不属于原理图可验证内容。
- `review.usb-otg`：量产固件如何选择 USB Host/Device，OTG VBus 电流限制和支持的 USB 类别是什么？；原因：原理图只能确认 OTG 硬件网络。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `40ac0b8ed6362568031542b4550b7d882491b078d17e2de5d0ee2dfb735a9fa7` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/459/SCH_LLM630_Compute_Kit_page_01.png` |

---

源文档：`zh_CN/core/LLM630 Compute Kit.md`

源文档 SHA-256：`4c1de8a6445f6a3ab028ebdf245acc70e947a84d5ed9e3941ef91e244ca4fdad`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
