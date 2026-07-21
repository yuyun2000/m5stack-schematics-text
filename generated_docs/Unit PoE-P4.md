# Unit PoE-P4 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit PoE-P4 |
| SKU | U213 |
| 产品 ID | `unit-poe-p4-ad6370b7c836` |
| 源文档 | `zh_CN/unit/Unit_PoE-P4.md` |

## 概述

Unit PoE-P4 的六页原理图覆盖主板四页、电源板一页和 Hat 转接板一页。主板以 ESP32-P4 为核心，连接外部串行 Flash、40MHz 时钟、双路 MIPI DSI/CSI FPC、IP101GRI RMII 以太网、两路 USB-C、RGB、红外、按键及 Grove/SDIO/ISP/Hat 扩展。电源板用双桥整流和 TPS23753APWR 接收 RJ45 PoE 绕组中心抽头，经开关管、HR051067 变压器、次级整流与光耦反馈生成 PSU_5V，并通过 AW32901FCR 电源路径汇入 SYS_5V。图面能确认硬件网络，但 SoC 子型号与容量、10/100M 性能、IEEE802.3at/6W、显示分辨率、USB 运行角色、固件行为、功耗和机械参数仍需外部资料确认；Hat2 文档针号与原理图 J2 针号方向相反。

## 检索关键词

`Unit PoE-P4`、`U213`、`ESP32-P4`、`ESP32-P4NRW32`、`XM25UH128BHQIGT`、`IP101GRI`、`TPS23753APWR`、`ME2212`、`SY8089AAAC`、`AW32901FCR`、`MIPI DSI`、`MIPI CSI`、`RMII`、`RJ45`、`PoE`、`IEEE802.3at`、`USB Type-C Host`、`USB OTG`、`SYS_5V`、`SYS_3.3V`、`SOC_VHP`、`CAM_1.8V`、`CAM_2.8V`、`LCD_DSI_CK`、`CAM_CSI_CK`、`RMII_MDC`、`RMII_MDIO`、`NH-B2020RGBA-HF`、`MHS153IRCT`、`PORT.CUSTOM`、`SDIO-Bus`、`ISP-Bus`、`Hat2-Bus`、`G14 IR_TX`、`G45 USER_KEY`、`G53`、`G54`、`16MB Flash`、`32MB PSRAM`、`poe-p4.local`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 (MAIN) | ESP32-P4 | 主控 SoC，连接 Flash、MIPI、RMII、USB、GPIO 与扩展总线 | 图 c0b2494a0a75 / 第 1 页 / A1-D2 U1 ESP32-P4 pins1-104 |
| U3 (MAIN) | XM25UH128BHQIGT | 连接 ESP32-P4 FLASH_CS/DO/SCK/DI/WP/HOLD 的串行 Flash | 图 c0b2494a0a75 / 第 1 页 / B3 U3 XM25UH128BHQIGT |
| X1 (MAIN) | 40MHz crystal | ESP32-P4 XTALP/XTALN 主时钟晶体 | 图 c0b2494a0a75 / 第 1 页 / A3 X1 40MHz、C32/C33、R7/R8 |
| U2,U4 (MAIN) | SY8089AAAC | SYS_5V 到 SYS_3.3V、SYS_3.3V 到 SOC_VHP 的两路降压电源 | 图 c0b2494a0a75 / 第 1 页 / C3 U2/L1 与 U4/L2 SY8089AAAC |
| U8 (MAIN) | ME2212 | LCD LEDA/LEDK 背光电源电路 | 图 f743dd8defe9 / 第 1 页 / A1-B2 U8 ME2212、L3、D7、FB1/FB2 |
| U6,U7 (MAIN) | SSP7615-18DFR / SSP7615-28DFR | SYS_3.3V 到 CAM_1.8V 与 CAM_2.8V 的摄像头电源 | 图 f743dd8defe9 / 第 1 页 / B1-C1 U6 SSP7615-18DFR、U7 SSP7615-28DFR |
| U9,U10 (MAIN) | TXS0102DCUR / SN74LVC1T45DCKR | 摄像头 SCL/SDA 与 MCLK 的 3.3V/1.8V 电平转换 | 图 f743dd8defe9 / 第 1 页 / C2-D2 U9 TXS0102DCUR、U10 SN74LVC1T45DCKR |
| J6,J7 (MAIN) | FPC_24P | LCD MIPI DSI/TP/BL 与 Camera MIPI CSI 扩展接口 | 图 f743dd8defe9 / 第 1 页 / A4-B4 J6 LCD FPC_24P 与 B4-D4 J7 CAM FPC_24P |
| U11 (MAIN) | IP101GRI | ESP32-P4 RMII 到以太网模拟差分对的 PHY | 图 5b4b45cd6f88 / 第 1 页 / A1-B2 U11 IP101GRI pins0-32 |
| T1,T2,FT3,FT4 (MAIN) | GA021G00 / CC2012A-801 | PHY TX/RX 到 RJ45 的变压器与共模器件 | 图 5b4b45cd6f88 / 第 1 页 / A3-B3 T1/T2 GA021G00、FT3/FT4 CC2012A-801 |
| J8 (MAIN) | RC01835 | TX/RX、PoE 4/5 与 7/8、双色 LED 的 RJ45 接口 | 图 5b4b45cd6f88 / 第 1 页 / A4-B4 J8 RC01835 pins1-14 |
| U2 (POWER) | TPS23753APWR | PoE 受电与开关电源控制器 | 图 daf839941913 / 第 1 页 / A2-B2 U2 TPS23753APWR pins1-14 |
| D2,D3 (POWER) | UM10B | TX_CM/RX_CM 与 POE_45/POE_78 的两路桥式整流 | 图 daf839941913 / 第 1 页 / A1-B1 D2/D3 UM10B |
| T1 (POWER) | HR051067 | TPS23753A 开关级到 PSU_5V 次级的电源变压器 | 图 daf839941913 / 第 1 页 / A3 T1 HR051067 与 D7、PSU_5V |
| U5 (MAIN); U1,U3 (POWER) | AW32901FCR | EXUSB_OTG、USB_SUB、PSU_5V 与 SYS_5V 之间的三组电源路径 | 图 20002ec75f4a / 第 1 页 / A2 U5 AW32901FCR，EXUSB_OTG 到 SYS_5V; 图 daf839941913 / 第 1 页 / C2 U1 USB_SUB 到 SYS_5V 与 C3 U3 PSU_5V 到 SYS_5V |
| J1 (MAIN USB) | USB_C_16P_Horizontal | USB_HOST_DP/DM 与 EXUSB_OTG 的 Type-C 接口 | 图 20002ec75f4a / 第 1 页 / A1 J1 USB_C_16P_Horizontal、FT1、R19/R20 |
| J3 (POWER USB) | USB_C_16P_Horizontal | USB_DP/DM 与 USB_SUB 的 Type-C 接口 | 图 daf839941913 / 第 1 页 / C1 J3 USB_C_16P_Horizontal、R1/R2 |
| LED2 (MAIN) | NH-B2020RGBA-HF | SYS_3.3V 共阳极、G15/G16/G17 分色控制的 RGB LED | 图 20002ec75f4a / 第 1 页 / A3 LED2 NH-B2020RGBA-HF、R22/R23/R24 |
| LED1 (MAIN) | MHS153IRCT | 由 G14 IR 网络和 Q2 驱动的红外发射 LED | 图 20002ec75f4a / 第 1 页 / B3-C3 LED1、R25、Q2 与 G14 IR |
| S1,Q1A,Q1B (MAIN) | TS-1145 / 2N7002DW | USER_KEY、SYS_BOOT 与 SOC_RST 的按键和 MOSFET 网络 | 图 20002ec75f4a / 第 1 页 / B1-C2 S1 TS-1145、Q1A/Q1B 2N7002DW、SYS_BOOT/SOC_RST/G45 USER_KEY |
| J2,J3,J4,J5 (MAIN); J1,J2 (HAT) | 2.54MM_9P / CON6 / CON4_SMD / FPC_16P / 2X8 | SDIO、ISP、Grove 与 Hat2 GPIO/电源扩展连接器 | 图 20002ec75f4a / 第 1 页 / B1-C3 J2 SDIO、J3 ISP、J4 Grove、J5 HAT; 图 d77c58a08024 / 第 1 页 / B2-B3 HAT board J1 FPC_16P 与 J2 2X8 |

## 系统结构

### ESP32-P4 主控与功能网络

U1 标为 ESP32-P4，图面引出 FLASH、LCD DSI、CAM CSI、USB_HOST、USB_DEVICE、RMII、SYS I2C、RGB、IR、USER_KEY、SDIO、UART 与扩展 GPIO 网络。

- 参数与网络：`soc_label=ESP32-P4`；`major_buses=FLASH,MIPI DSI,MIPI CSI,USB2,RMII,I2C,SDIO,UART`
- 证据：图 c0b2494a0a75 / 第 1 页 / A1-D2 U1 ESP32-P4 pins1-104

## 电源

### SYS_5V 到 SYS_3.3V 降压

U2 SY8089AAAC 以 SYS_5V 为输入，LX 经 L1 2.2uH/2.5A 输出 SYS_3.3V；反馈为 R10 100K、R11 22K，输出并联 C37/C39 22uF。

- 参数与网络：`converter=U2 SY8089AAAC`；`input=SYS_5V`；`output=SYS_3.3V`；`inductor=L1 2.2uH/2.5A`；`feedback=R10=100K,R11=22K`
- 证据：图 c0b2494a0a75 / 第 1 页 / C3 U2/L1/R10/R11/C37/C39

### SYS_3.3V 到 SOC_VHP 降压

U4 SY8089AAAC 以 SYS_3.3V 为输入，LX 经 L2 2.2uH/2.5A 输出 SOC_VHP；VHP_DCDC_EN 与 VHP_DCDC_DVFS 连接其 EN/FB 控制网络。

- 参数与网络：`converter=U4 SY8089AAAC`；`input=SYS_3.3V`；`output=SOC_VHP`；`inductor=L2 2.2uH/2.5A`；`controls=VHP_DCDC_EN,VHP_DCDC_DVFS`
- 证据：图 c0b2494a0a75 / 第 1 页 / C3-D3 U4/L2/R15/R16/C40/C41

### LCD 背光电源

SYS_5V 经 FB1、L3、U8 ME2212、D7 1N5819WS 与 FB2 形成 LCD_LEDA 路径，LCD_LEDK 连接 U8 FB 网络；G33 LCD_BL 连接 U8 EN。

- 参数与网络：`driver=U8 ME2212`；`input=SYS_5V`；`outputs=LCD_LEDA,LCD_LEDK`；`enable=G33 LCD_BL`；`inductor=L3 2.2uH/2.5A`
- 证据：图 f743dd8defe9 / 第 1 页 / A1-B2 FB1/L3/U8/D7/FB2/LCD_LEDA/LCD_LEDK

### CAM_1.8V 与 CAM_2.8V

U6 SSP7615-18DFR 将 SYS_3.3V 输出为 CAM_1.8V，U7 SSP7615-28DFR 将 SYS_3.3V 输出为 CAM_2.8V；两路 EN 均接 SYS_3.3V。

- 参数与网络：`camera_1v8=U6 SSP7615-18DFR`；`camera_2v8=U7 SSP7615-28DFR`；`input=SYS_3.3V`
- 证据：图 f743dd8defe9 / 第 1 页 / B1-C1 U6/U7 与 CAM_1.8V/CAM_2.8V

### PoE 双桥整流与 TPS23753A

电源板 D2/D3 UM10B 分别整流 TX_CM/RX_CM 与 POE_45/POE_78，整流总线由 D4 SMF58A 钳位并送入 U2 TPS23753APWR 的 VDD/VDD1、DEN、CLS 等 PoE 输入与分类网络。

- 参数与网络：`bridges=D2 UM10B,D3 UM10B`；`inputs=TX_CM,RX_CM,POE_45,POE_78`；`controller=U2 TPS23753APWR`；`tvs=D4 SMF58A`
- 证据：图 daf839941913 / 第 1 页 / A1-B2 D2/D3/D4/U2 TPS23753APWR

### PoE 变压器、次级整流与 PSU_5V

U2 GATE 驱动 Q1 开关并连接 T1 HR051067 初级，次级经 D7 DSK34 与 C13/C14/C16 47uF 输出 PSU_5V；PC1 EL3H7、D6 MM3Z4V3 和相关阻容构成跨变压器反馈路径。

- 参数与网络：`switch=Q1`；`transformer=T1 HR051067`；`rectifier=D7 DSK34`；`output=PSU_5V`；`feedback=PC1 EL3H7,D6 MM3Z4V3`
- 证据：图 daf839941913 / 第 1 页 / A2-B3 Q1/T1/D7/PC1/D6/PSU_5V

### EXUSB_OTG、USB_SUB、PSU_5V 到 SYS_5V 路径

主板 U5 AW32901FCR 的 IN 接 EXUSB_OTG、OUT 接 SYS_5V；电源板 U1 AW32901FCR 的 IN 接 USB_SUB、OUT 接 SYS_5V；电源板 U3 AW32901FCR 的 IN 接 PSU_5V、OUT 接 SYS_5V。

- 参数与网络：`main_usb_path=EXUSB_OTG -> U5 -> SYS_5V`；`download_usb_path=USB_SUB -> U1 -> SYS_5V`；`poe_path=PSU_5V -> U3 -> SYS_5V`
- 证据：图 20002ec75f4a / 第 1 页 / A2 U5 AW32901FCR EXUSB_OTG/SYS_5V; 图 daf839941913 / 第 1 页 / C2-C3 U1/U3 AW32901FCR USB_SUB/PSU_5V/SYS_5V

## 接口

### J6 LCD 24-pin FPC

J6 引出 LCD_LEDA/LEDK、SYS_3.3V、TP_RST G3、TP_INT G2、SYS_SDA G0、SYS_SCL G1、LCD_RST G4，以及 LCD_DSI_CK、D1、D0 的正负差分对和多组 GND。

- 参数与网络：`connector=J6 FPC_24P`；`mipi=LCD_DSI_CK_P/N,LCD_DSI_D1_P/N,LCD_DSI_D0_P/N`；`touch=G0 SYS_SDA,G1 SYS_SCL,G3 TP_RST,G2 TP_INT`；`backlight=LCD_LEDA,LCD_LEDK`；`reset=G4 LCD_RST`
- 证据：图 f743dd8defe9 / 第 1 页 / A4-B4 J6 LCD FPC_24P pins1-24

### J7 Camera 24-pin FPC

J7 引出 CAM_SCL_1V8、CAM_SDA_1V8、CAM_MCLK_1V8、CAM_RST_1V8、CAM_CSI_CK、D1、D0 的正负差分对、CAM_2.8V、CAM_1.8V 与多组 GND。

- 参数与网络：`connector=J7 FPC_24P`；`mipi=CAM_CSI_CK_P/N,CAM_CSI_D1_P/N,CAM_CSI_D0_P/N`；`control=CAM_SCL_1V8,CAM_SDA_1V8,CAM_MCLK_1V8,CAM_RST_1V8`；`rails=CAM_2.8V,CAM_1.8V`
- 证据：图 f743dd8defe9 / 第 1 页 / B4-D4 J7 CAM FPC_24P pins1-24

### ESP32-P4 到 IP101GRI RMII

U11 IP101GRI 的 MDC/MDIO 接 G31/G52，RESET_N 接 G51，TXD0/TXD1/TXEN 接 G34/G35/G49，RXD0/RXD1/RXDV 接 G29/G30/G28，RMII_CLK 接 G50。

- 参数与网络：`phy=IP101GRI`；`management=G31 RMII_MDC,G52 RMII_MDIO,G51 RMII_RST`；`tx=G34 TXD0,G35 TXD1,G49 TXEN`；`rx=G29 RXD0,G30 RXD1,G28 RXDV`；`clock=G50 RMII_CLK`
- 证据：图 5b4b45cd6f88 / 第 1 页 / A1-B2 U11 IP101GRI RMII 网络

### PHY 到 RJ45 差分与 PoE 抽头

IP101GRI 的 PHY_TP/TN 与 PHY_RP/RN 分别经 T1/T2 GA021G00 和 FT3/FT4 CC2012A-801 到 J8 TX+/TX- 与 RX+/RX-；J8 的 POE_45、POE_78 以及 TX_CM、RX_CM 通过 J9 引到电源板。

- 参数与网络：`tx_path=PHY_TP/TN -> T1 -> FT3 -> J8 TX+/TX-`；`rx_path=PHY_RP/RN -> T2 -> FT4 -> J8 RX+/RX-`；`poe_nets=TX_CM,RX_CM,POE_45,POE_78`
- 证据：图 5b4b45cd6f88 / 第 1 页 / A3-B4 T1/T2/FT3/FT4/J8/J9

### 主板 USB-C HOST 连接器

主板 J1 的 DP1/DP2 与 DM1/DM2 合并后经 FT1 接 USB_HOST_DP/DM，CC1/CC2 分别经 R19/R20 5.1K 接地，VBUS 网络标为 EXUSB_OTG。

- 参数与网络：`connector=J1 USB_C_16P_Horizontal`；`data=USB_HOST_DP,USB_HOST_DM`；`cc=R19=5.1K,R20=5.1K to GND`；`vbus=EXUSB_OTG`
- 证据：图 20002ec75f4a / 第 1 页 / A1 J1/FT1/R19/R20

### 电源板 USB-C 下载连接器

电源板 J3 的 DP1/DP2 合并为 USB_DP、DM1/DM2 合并为 USB_DM，CC1/CC2 分别经 R1/R2 5.1K 接地，VBUS 网络标为 USB_SUB；USB_DP/DM 通过板间 J2/J10 和 FT2 连接 U1 的 USB_DEVICE_DP/DM。

- 参数与网络：`connector=J3 USB_C_16P_Horizontal`；`data=USB_DP,USB_DM -> FT2 -> USB_DEVICE_DP,USB_DEVICE_DM`；`cc=R1=5.1K,R2=5.1K to GND`；`vbus=USB_SUB`
- 证据：图 daf839941913 / 第 1 页 / C1-C2 J3/R1/R2/J2 USB_DP/DM; 图 5b4b45cd6f88 / 第 1 页 / C4 J10/FT2 USB_DEVICE_DP/DM

### NH-B2020RGBA-HF RGB LED

LED2 NH-B2020RGBA-HF 的公共端接 SYS_3.3V，蓝、绿、红三路分别经 R22/R23/R24 1K 接 G16 LED_B、G15 LED_G、G17 LED_R。

- 参数与网络：`led=NH-B2020RGBA-HF`；`blue=G16 through R22 1K`；`green=G15 through R23 1K`；`red=G17 through R24 1K`；`common=SYS_3.3V`
- 证据：图 20002ec75f4a / 第 1 页 / A3 LED2/R22/R23/R24

### G14 红外发射电路

G14 IR 经 C46/R26/D6 网络驱动 Q2，Q2 控制从 SYS_3.3V 经 LED1 MHS153IRCT 与 R25 22R 到地的红外发射路径。

- 参数与网络：`gpio=G14 IR`；`emitter=LED1 MHS153IRCT`；`switch=Q2`；`series_resistor=R25 22R`
- 证据：图 20002ec75f4a / 第 1 页 / B3-C3 G14 IR、C46/R26/D6/Q2/LED1/R25

### 用户按键、BOOT 与复位网络

S1 TS-1145 与 R17 2.2K、Q1A/Q1B 2N7002DW、D1/D2/D3、LED3 RED 连接 G45 USER_KEY、SYS_BOOT 和 SOC_RST；SOC_RST 在 SoC 页另由 R14 10K 上拉并通过 C35 1uF 接地。

- 参数与网络：`button=S1 TS-1145`；`user_net=G45 USER_KEY`；`boot_net=SYS_BOOT`；`reset_net=SOC_RST`；`mosfet=Q1A/Q1B 2N7002DW`
- 证据：图 20002ec75f4a / 第 1 页 / B1-C2 S1/Q1A/Q1B/D1-D3/LED3/G45/SYS_BOOT/SOC_RST; 图 c0b2494a0a75 / 第 1 页 / A3 R14/C35/SOC_RST

### HY2.0-4P Grove 扩展

主板 J4 CON4_SMD 的 pin1 接 GND、pin2 接 SYS_5V、pin3 接 G53、pin4 接 G54，外壳 SH 接地。

- 参数与网络：`connector=J4 CON4_SMD`；`pin1=GND`；`pin2=SYS_5V`；`pin3=G53`；`pin4=G54`
- 证据：图 20002ec75f4a / 第 1 页 / B2 J4 CON4_SMD GROVE

### SDIO 9P 与 ISP 6P 扩展

J2 9P 依次引出 G13、G12、G11、G10、G9、G8、G27 USB1_DP、G26 USB1_DM、SYS_5V；J3 6P 引出 GND、SYS_BOOT、SOC_RST、G38 UART0_RX、G37 UART0_TX、SYS_3.3V。

- 参数与网络：`sdio_j2=1=G13,2=G12,3=G11,4=G10,5=G9,6=G8,7=G27 USB1_DP,8=G26 USB1_DM,9=SYS_5V`；`isp_j3=1=GND,2=SYS_BOOT,3=SOC_RST,4=G38 UART0_RX,5=G37 UART0_TX,6=SYS_3.3V`
- 证据：图 20002ec75f4a / 第 1 页 / B1 J2 2.54MM_9P SDIO 与 J3 CON6 ISP

### Hat 板 J2 2x8 原理图针号

Hat 板 J2 原理图标注 pin1 SYS_5V、pin2 G22、pin3 SYS_3.3V、pin4 G23、pin5 NC、pin6 G39、pin7 G19、pin8 G40、pin9 G20、pin10 G41、pin11 G21、pin12 G42、pin13 SYS_5V、pin14 G43、pin15 GND、pin16 G44。

- 参数与网络：`pinout=1=SYS_5V,2=G22,3=SYS_3.3V,4=G23,5=NC,6=G39,7=G19,8=G40,9=G20,10=G41,11=G21,12=G42,13=SYS_5V,14=G43,15=GND,16=G44`
- 证据：图 d77c58a08024 / 第 1 页 / B3 J2 2X8 pins1-16

## 总线

### Camera SCL/SDA 电平转换

U9 TXS0102DCUR 的 3.3V 侧连接 G1 SYS_SCL 与 G0 SYS_SDA，1.8V 侧经 R33/R34 5.1K 上拉到 CAM_1.8V 并输出 CAM_SCL_1V8/CAM_SDA_1V8。

- 参数与网络：`translator=U9 TXS0102DCUR`；`side_3v3=G1 SYS_SCL,G0 SYS_SDA`；`side_1v8=CAM_SCL_1V8,CAM_SDA_1V8`；`pullups=R33=5.1K,R34=5.1K`
- 证据：图 f743dd8defe9 / 第 1 页 / D2 U9 TXS0102DCUR 与 R33/R34

## 时钟

### ESP32-P4 40MHz 晶体

X1 标为 40MHz，连接 XTAP/XTAN，经 R8/R7 0R 串联；C32/C33 各 15pF 接地。

- 参数与网络：`crystal=X1 40MHz`；`soc_nets=XTAP,XTAN`；`series=R8=0R,R7=0R`；`load_caps=C32=15pF,C33=15pF`
- 证据：图 c0b2494a0a75 / 第 1 页 / A3 X1、R7/R8、C32/C33

### Camera 24MHz MCLK 路径

X2 以 SYS_3.3V 供电并输出 PXT_24M，经 R30 22R 接 U10 B 端；U10 SN74LVC1T45DCKR 从 SYS_3.3V/CAM_1.8V 两侧转换后，经 R36 22R 输出 CAM_MCLK_1V8，G36 CAM_MCLK 的 R28 位置标为 NC。

- 参数与网络：`oscillator=X2 24MHz`；`default_source=PXT_24M through R30 22R`；`level_shifter=U10 SN74LVC1T45DCKR`；`output=CAM_MCLK_1V8`；`optional_source=G36 CAM_MCLK through R28 NC`
- 证据：图 f743dd8defe9 / 第 1 页 / B2-C2 X2/R30/R28/U10/R36

### IP101GRI 25MHz 晶体

X3 标为 25MHz 18pF/10PPM，连接 U11 XI/XO pins2/3，C65/C66 各 20pF 接地。

- 参数与网络：`crystal=X3 25MHz 18pF/10PPM`；`phy_pins=XI pin2,XO pin3`；`load_caps=C65=20pF,C66=20pF`
- 证据：图 5b4b45cd6f88 / 第 1 页 / B2 X3、C65/C66、U11 XI/XO

## 存储

### XM25UH128BHQIGT 串行 Flash

U3 XM25UH128BHQIGT 的 CS、SO、SCLK、SI、WP#、HOLD# 分别连接 FLASH_CS、FLASH_DO、FLASH_SCK、FLASH_DI、FLASH_WP、FLASH_HOLD，VCC 接 ESP_LDO1，GND 接地。

- 参数与网络：`part=XM25UH128BHQIGT`；`signals=FLASH_CS,FLASH_DO,FLASH_SCK,FLASH_DI,FLASH_WP,FLASH_HOLD`；`supply=ESP_LDO1`
- 证据：图 c0b2494a0a75 / 第 1 页 / B3 U3 XM25UH128BHQIGT pins1-8

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | ESP32-P4 主控与功能网络 | `soc_label=ESP32-P4`；`major_buses=FLASH,MIPI DSI,MIPI CSI,USB2,RMII,I2C,SDIO,UART` |
| 存储 | XM25UH128BHQIGT 串行 Flash | `part=XM25UH128BHQIGT`；`signals=FLASH_CS,FLASH_DO,FLASH_SCK,FLASH_DI,FLASH_WP,FLASH_HOLD`；`supply=ESP_LDO1` |
| 时钟 | ESP32-P4 40MHz 晶体 | `crystal=X1 40MHz`；`soc_nets=XTAP,XTAN`；`series=R8=0R,R7=0R`；`load_caps=C32=15pF,C33=15pF` |
| 电源 | SYS_5V 到 SYS_3.3V 降压 | `converter=U2 SY8089AAAC`；`input=SYS_5V`；`output=SYS_3.3V`；`inductor=L1 2.2uH/2.5A`；`feedback=R10=100K,R11=22K` |
| 电源 | SYS_3.3V 到 SOC_VHP 降压 | `converter=U4 SY8089AAAC`；`input=SYS_3.3V`；`output=SOC_VHP`；`inductor=L2 2.2uH/2.5A`；`controls=VHP_DCDC_EN,VHP_DCDC_DVFS` |
| 接口 | J6 LCD 24-pin FPC | `connector=J6 FPC_24P`；`mipi=LCD_DSI_CK_P/N,LCD_DSI_D1_P/N,LCD_DSI_D0_P/N`；`touch=G0 SYS_SDA,G1 SYS_SCL,G3 TP_RST,G2 TP_INT`；`backlight=LCD_LEDA,LCD_LEDK`；`reset=G4 LCD_RST` |
| 电源 | LCD 背光电源 | `driver=U8 ME2212`；`input=SYS_5V`；`outputs=LCD_LEDA,LCD_LEDK`；`enable=G33 LCD_BL`；`inductor=L3 2.2uH/2.5A` |
| 接口 | J7 Camera 24-pin FPC | `connector=J7 FPC_24P`；`mipi=CAM_CSI_CK_P/N,CAM_CSI_D1_P/N,CAM_CSI_D0_P/N`；`control=CAM_SCL_1V8,CAM_SDA_1V8,CAM_MCLK_1V8,CAM_RST_1V8`；`rails=CAM_2.8V,CAM_1.8V` |
| 电源 | CAM_1.8V 与 CAM_2.8V | `camera_1v8=U6 SSP7615-18DFR`；`camera_2v8=U7 SSP7615-28DFR`；`input=SYS_3.3V` |
| 时钟 | Camera 24MHz MCLK 路径 | `oscillator=X2 24MHz`；`default_source=PXT_24M through R30 22R`；`level_shifter=U10 SN74LVC1T45DCKR`；`output=CAM_MCLK_1V8`；`optional_source=G36 CAM_MCLK through R28 NC` |
| 总线 | Camera SCL/SDA 电平转换 | `translator=U9 TXS0102DCUR`；`side_3v3=G1 SYS_SCL,G0 SYS_SDA`；`side_1v8=CAM_SCL_1V8,CAM_SDA_1V8`；`pullups=R33=5.1K,R34=5.1K` |
| 接口 | ESP32-P4 到 IP101GRI RMII | `phy=IP101GRI`；`management=G31 RMII_MDC,G52 RMII_MDIO,G51 RMII_RST`；`tx=G34 TXD0,G35 TXD1,G49 TXEN`；`rx=G29 RXD0,G30 RXD1,G28 RXDV`；`clock=G50 RMII_CLK` |
| 时钟 | IP101GRI 25MHz 晶体 | `crystal=X3 25MHz 18pF/10PPM`；`phy_pins=XI pin2,XO pin3`；`load_caps=C65=20pF,C66=20pF` |
| 接口 | PHY 到 RJ45 差分与 PoE 抽头 | `tx_path=PHY_TP/TN -> T1 -> FT3 -> J8 TX+/TX-`；`rx_path=PHY_RP/RN -> T2 -> FT4 -> J8 RX+/RX-`；`poe_nets=TX_CM,RX_CM,POE_45,POE_78` |
| 电源 | PoE 双桥整流与 TPS23753A | `bridges=D2 UM10B,D3 UM10B`；`inputs=TX_CM,RX_CM,POE_45,POE_78`；`controller=U2 TPS23753APWR`；`tvs=D4 SMF58A` |
| 电源 | PoE 变压器、次级整流与 PSU_5V | `switch=Q1`；`transformer=T1 HR051067`；`rectifier=D7 DSK34`；`output=PSU_5V`；`feedback=PC1 EL3H7,D6 MM3Z4V3` |
| 接口 | 主板 USB-C HOST 连接器 | `connector=J1 USB_C_16P_Horizontal`；`data=USB_HOST_DP,USB_HOST_DM`；`cc=R19=5.1K,R20=5.1K to GND`；`vbus=EXUSB_OTG` |
| 接口 | 电源板 USB-C 下载连接器 | `connector=J3 USB_C_16P_Horizontal`；`data=USB_DP,USB_DM -> FT2 -> USB_DEVICE_DP,USB_DEVICE_DM`；`cc=R1=5.1K,R2=5.1K to GND`；`vbus=USB_SUB` |
| 电源 | EXUSB_OTG、USB_SUB、PSU_5V 到 SYS_5V 路径 | `main_usb_path=EXUSB_OTG -> U5 -> SYS_5V`；`download_usb_path=USB_SUB -> U1 -> SYS_5V`；`poe_path=PSU_5V -> U3 -> SYS_5V` |
| 接口 | NH-B2020RGBA-HF RGB LED | `led=NH-B2020RGBA-HF`；`blue=G16 through R22 1K`；`green=G15 through R23 1K`；`red=G17 through R24 1K`；`common=SYS_3.3V` |
| 接口 | G14 红外发射电路 | `gpio=G14 IR`；`emitter=LED1 MHS153IRCT`；`switch=Q2`；`series_resistor=R25 22R` |
| 接口 | 用户按键、BOOT 与复位网络 | `button=S1 TS-1145`；`user_net=G45 USER_KEY`；`boot_net=SYS_BOOT`；`reset_net=SOC_RST`；`mosfet=Q1A/Q1B 2N7002DW` |
| 接口 | HY2.0-4P Grove 扩展 | `connector=J4 CON4_SMD`；`pin1=GND`；`pin2=SYS_5V`；`pin3=G53`；`pin4=G54` |
| 接口 | SDIO 9P 与 ISP 6P 扩展 | `sdio_j2=1=G13,2=G12,3=G11,4=G10,5=G9,6=G8,7=G27 USB1_DP,8=G26 USB1_DM,9=SYS_5V`；`isp_j3=1=GND,2=SYS_BOOT,3=SOC_RST,4=G38 UART0_RX,5=G37 UART0_TX,6=SYS_3.3V` |
| 接口 | Hat 板 J2 2x8 原理图针号 | `pinout=1=SYS_5V,2=G22,3=SYS_3.3V,4=G23,5=NC,6=G39,7=G19,8=G40,9=G20,10=G41,11=G21,12=G42,13=SYS_5V,14=G43,15=GND,16=G44` |
| 内存与 Flash | ESP32-P4 子型号、CPU 与存储容量 | `documented_soc=ESP32-P4NRW32`；`documented_cpu=dual-core 360MHz plus LP-core 40MHz`；`documented_flash_mb=16`；`documented_psram_mb=32`；`documented_psram_bus=Octal` |
| 接口 | 10/100M 自适应以太网 | `documented_speed_mbps=10/100 auto-negotiation`；`phy=IP101GRI` |
| 电源 | IEEE802.3at 与 PoE 最大 6W | `documented_standard=IEEE802.3at`；`documented_max_power_w=6` |
| 接口 | MIPI DSI 最高显示分辨率 | `documented_resolution=1920x1080 maximum`；`documented_lanes=2` |
| 接口 | USB 2.0 Host、OTG 与下载功能 | `documented_host=USB 2.0 Host`；`documented_device=USB 2.0 OTG and firmware download` |
| 系统结构 | 下载模式与出厂 Web 控制页面 | `documented_download_hold_s=3`；`documented_download_led=green`；`documented_hostname=poe-p4.local`；`documented_web_functions=RGB,button count,GPIO mode and level` |
| 电源 | 工作、IR、RGB、满载与休眠电流 | `documented_work_ma=73.82`；`documented_ir_ma=23.57`；`documented_rgb_ma=75.32`；`documented_full_load_ma=277.1`；`documented_deep_sleep_ma=19.85` |
| 系统结构 | 工作温度与机械参数 | `documented_temperature_c=0-40`；`documented_product_size_mm=64.0x24.0x20.2`；`documented_product_weight_g=28.2`；`documented_package_size_mm=65.0x33.0x21.2`；`documented_gross_weight_g=35.0` |
| 接口 | Hat2-Bus 文档与原理图针号方向 | `documented_start=1=GND,2=G44`；`documented_end=15=5V,16=G22`；`schematic_start=1=SYS_5V,2=G22`；`schematic_end=15=GND,16=G44` |

## 待确认事项

- `memory.documented-soc-capacity`：源文档称 SoC 为 ESP32-P4NRW32，包含双核 360MHz、LP 单核 40MHz、16MB Flash 和 32MB Octal PSRAM；原理图 U1 仅标 ESP32-P4，U3 标出 Flash 型号但未写容量，图面没有单独 PSRAM 容量标注。（证据：图 c0b2494a0a75 / 第 1 页 / U1 仅标 ESP32-P4，U3 未标容量）
- `interface.documented-ethernet-speed`：源文档称 IP101GRI 支持 10/100M 自适应以太网；原理图能确认 IP101GRI、RMII 与 RJ45 连接，但不包含链路协商结果或速率测试。（证据：图 5b4b45cd6f88 / 第 1 页 / U11 IP101GRI、RMII 与 J8 RJ45，无速率测试）
- `power.documented-poe-standard-power`：源文档称 PoE 符合 IEEE802.3at 且最大功率 6W；电源板确认 TPS23753APWR PoE 电路与 PSU_5V 输出，但没有标准符合性声明或 6W 负载测试。（证据：图 daf839941913 / 第 1 页 / TPS23753APWR 与 PSU_5V 电路，无标准或功率标注）
- `interface.documented-display-resolution`：源文档称 2-lane MIPI DSI 屏最高支持 1920x1080，并受 lane 与帧率限制；原理图只确认两条 DSI 数据 lane、时钟、触摸和背光网络，未给出面板时序与分辨率。（证据：图 f743dd8defe9 / 第 1 页 / J6 DSI CK/D1/D0 差分对，无面板时序）
- `interface.documented-usb-roles`：源文档称一只 Type-C 为 USB 2.0 Host，另一只支持 USB 2.0 OTG 与固件下载；原理图用 USB_HOST 与 USB_DEVICE 网络区分两路硬件，但不包含主从切换、枚举或烧录协议行为。（证据：图 20002ec75f4a / 第 1 页 / J1 USB_HOST_DP/DM 硬件网络; 图 daf839941913 / 第 1 页 / J3 USB_DP/DM 硬件网络）
- `system.documented-factory-firmware`：源文档称长按侧键 3 秒至绿灯亮可进入下载模式，并称出厂固件提供 poe-p4.local Web 页面、IP 显示、RGB、按键计数和 GPIO 控制；原理图不能确认按键时长、LED 状态、固件版本或网络服务。（证据：图 20002ec75f4a / 第 1 页 / S1/G45/SYS_BOOT/SOC_RST/RGB 硬件图，无固件行为）
- `power.documented-consumption`：源文档列出工作 5V@73.82mA、红外瞬时 3.3V@23.57mA、RGB 5V@75.32mA、满载 277.10mA、深度休眠 5V@19.85mA；原理图没有这些状态的测量点、负载条件或测试结果。（证据：图 c0b2494a0a75 / 第 1 页 / 电源与负载电路，无整机电流测试）
- `system.documented-mechanical-temperature`：源文档称工作温度 0-40C、产品尺寸 64.0x24.0x20.2mm、重量 28.2g，包装尺寸 65.0x33.0x21.2mm、毛重 35.0g；六页电气原理图没有环境等级、外壳、机械公差或质量信息。（证据：图 d77c58a08024 / 第 1 页 / Hat 电气图无机械与环境信息）
- `interface.documented-hat2-numbering`：源文档 Hat2-Bus 表把 pin1 标为 GND、pin2 为 G44，至 pin15 为 5V、pin16 为 G22；Hat 板原理图 J2 则把 pin1 标为 SYS_5V、pin2 为 G22，至 pin15 为 GND、pin16 为 G44，16 针顺序完全反向。（证据：图 d77c58a08024 / 第 1 页 / B3 J2 2X8 原理图 pins1-16）
- `review.soc-capacity`：确认 U213 量产 SoC 完整子型号、CPU 配置、Flash 与 Octal PSRAM 容量；原因：图面只标 ESP32-P4 和 Flash 型号，没有 SoC 后缀或容量标注。
- `review.ethernet-speed`：确认 IP101GRI 的 10/100M 自适应配置、链路协商与量产测试结果；原因：原理图只能确认 PHY/RMII/RJ45 硬件连接。
- `review.poe-standard-power`：以正式符合性和负载测试确认 IEEE802.3at 声明与 PoE 最大 6W 输出；原因：图面没有标准符合性或 6W 负载结果。
- `review.display-resolution`：确认 2-lane MIPI DSI 在目标面板和帧率下的最高 1920x1080 支持边界；原因：原理图没有面板时序、像素格式或帧率。
- `review.usb-roles`：确认两路 USB-C 的 USB 2.0 Host、OTG、下载角色切换与支持设备范围；原因：硬件图只给出 USB_HOST/USB_DEVICE 网络，不包含协议行为。
- `review.factory-firmware`：确认量产固件版本、3 秒下载模式动作、LED 状态和 poe-p4.local Web 功能；原因：这些是固件和运行环境行为，原理图不能确认。
- `review.consumption`：确认工作、IR、RGB、满载与深度休眠电流的测试条件和量产容差；原因：电气原理图没有整机电流测量结果。
- `review.mechanical-temperature`：确认 0-40C 工作温度、64.0x24.0x20.2mm 外形与 28.2g 重量；原因：电气原理图没有环境和机械信息。
- `review.hat2-numbering`：确认 Hat2-Bus 的用户视图方向与 pin1 标记，避免按反向针号接线；原因：源文档表与 Hat 板 J2 原理图的 16 针编号顺序完全反向。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c0b2494a0a7527bfb3254d7d85ae4f7c34d80df9db4b3c107e492147382ade91` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1217/SCH_StickPoE_SCH_Main_V0.2_20250829_2026_02_02_17_17_04_page_01.png` |
| 2 | 1 | `f743dd8defe9ecb18a0b8d963e8daf277d5a905a9deeefd9107a2e5c15f9401b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1217/SCH_StickPoE_SCH_Main_V0.2_20250829_2026_02_02_17_17_04_page_02.png` |
| 3 | 1 | `5b4b45cd6f88b3919e644003403593c13e23133967534e9db37a2c8a79c46fea` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1217/SCH_StickPoE_SCH_Main_V0.2_20250829_2026_02_02_17_17_04_page_03.png` |
| 4 | 1 | `20002ec75f4a5d2fd30e1d52873b8e4db86855958e2cd1bbad1d9a78cdf936d1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1217/SCH_StickPoE_SCH_Main_V0.2_20250829_2026_02_02_17_17_04_page_04.png` |
| 5 | 1 | `daf839941913ae6ec5b66ed8bd042d7e3fc139b27a095eddc1eb875f9f8dbe64` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1217/SCH_StickPoE_SCH_POWER_V0.2_20250731_2026_02_02_17_17_39_page_01.png` |
| 6 | 1 | `d77c58a08024fca692565d635f2b431b4418f1e9e90195bf77899f5af172397d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1217/SCH_StickPoE_SCH_Hat_V0.2_20250801_2026_02_02_17_16_35_page_01.png` |

---

源文档：`zh_CN/unit/Unit_PoE-P4.md`

源文档 SHA-256：`055dc980cfa0774f9ef75392a0ec57310bb7d5aaa1da5043482de2292f6554cf`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
