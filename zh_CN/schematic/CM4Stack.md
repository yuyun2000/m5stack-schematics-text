# CM4Stack 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | CM4Stack |
| SKU | K127 |
| 产品 ID | `cm4stack-c8ed4963c06f` |
| 源文档 | `zh_CN/core/CM4Stack.md` |

## 概述

CM4Stack 原理图展示一块 2023-01-05 的 Raspberry Pi CM4 载板：12V DC 输入经 MP8759 生成 5V，AW32901 切换系统 5V，CM4 再提供 3.3V/1.8V，RS3236 与 SY8003 补充 2.5V/1.1V。载板将 CM4 的千兆以太网、USB 2.0 OTG、PCIe、HDMI0 和 GPIO 引至 RJ45、USB-C、ASM3042 双 USB 3.x、HDMI、LCD/触摸、UART/I2C Grove、调试口与风扇；BM8563 提供 RTC，ATECC608B-TNGTLSU-G 提供安全功能，AW88298 通过 I2C/I2S 驱动差分扬声器。CM4 模块具体内存/eMMC、LCD/触摸器件和扬声器额定规格未在图面标出，单列为待确认。

## 检索关键词

`CM4Stack`、`K127`、`K127-US`、`K127-EU`、`Raspberry Pi CM4`、`RPI-CM4`、`CM4104032`、`MP8759`、`AW32901`、`SY8003`、`RS3236-2.5YF5`、`BM8563`、`ATECC608B-TNGTLSU-G`、`ATECC608B`、`ASM3042`、`GD25Q40CEIGR`、`ME1502AM5G`、`AW88298`、`DC 12V`、`VCC_5V`、`VCC_5V_SYS`、`VCC_3V3`、`VCC_2V5`、`VCC_1V8`、`VCC_1V1`、`PCIe`、`USB 3`、`USB OTG`、`USB Type-C`、`HDMI0`、`Gigabit Ethernet`、`RJ45`、`SCL0`、`SDA0`、`I2S_BCK`、`I2S_WCK`、`I2S_DAT`、`LCD_SPI`、`LCD_TOUCH`、`FAN_PWM`、`EXT_I2C_SCL1`、`EXT_I2C_SDA1`、`EXT_TXD3`、`EXT_RXD3`、`GLOBAL_EN`、`nRPI_BOOT`、`SPK_VOP`、`SPK_VON`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3A/U3B/U3C/U3D/U3E/U3F/U3G/U3H/U3I/U3J/U3K/U3L/U3M/U3N | RPI-CM4(DF40HC(3.0)-100DS-0.4v) | Raspberry Pi CM4 核心模块接口，承载电源、控制、GPIO、以太网、USB、PCIe、HDMI、SD、摄像头和显示信号 | 图 e7cec62f297b / 第 1 页 / A2-PWR 网格 C1-D2，U3B/U3L CM4 地与电源; 图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 A1-B2，U3M GPIO |
| U2 | MP8759 | VIN_12V 至 VCC_5V 的主降压转换器 | 图 e7cec62f297b / 第 1 页 / A2-PWR 网格 B1-B3，U2 MP8759、L2 与反馈网络 |
| U26 | AW32901 | VCC_5V 至 VCC_5V_SYS 的受控电源路径 | 图 e7cec62f297b / 第 1 页 / A2-PWR 网格 A4-C4，U26 AW32901、R53/R54 |
| U4,U5 | RS3236-2.5YF5 / SY8003 | 分别由 3.3V 和 5V_SYS 生成 VCC_2V5 与 VCC_1V1 | 图 e7cec62f297b / 第 1 页 / A2-PWR 网格 C2-D3，U4 RS3236-2.5YF5 与 U5 SY8003 |
| U6 | BM8563 | 带后备电池和 32.768kHz 晶体的 I2C RTC | 图 5827982711c4 / 第 1 页 / A3-PI_SYS 网格 B1-C2，U6 BM8563、Y1、BAT1 |
| J1 | RB1-2S5BAK1A | 带 LED 的四对以太网 RJ45 连接器 | 图 983e328ee808 / 第 1 页 / A4-ETH 网格 A3-B4，J1 RB1-2S5BAK1A |
| J2 | HDGC TYPE C-CQ-106PWB | CM4 USB 2.0 OTG 与 5V 电源的 USB-C 接口 | 图 3a741c6f2a08 / 第 1 页 / A5-USB_OTG 网格 B1-B2，J2 USB-C、R17/R18、U24、D2 |
| U11A/U11B/U11C/U11D | ASM3042 | 将 CM4 PCIe 转换为两路 USB 3.x 主机端口 | 图 21cab0d24f14 / 第 1 页 / A6-USB3_BRIDGE 网格 A1-D2，U11 ASM3042 全部单元 |
| U12 | GD25Q40CEIGR | ASM3042 的预烧写 SPI Flash | 图 21cab0d24f14 / 第 1 页 / A6-USB3_BRIDGE 网格 A3-B4，U12 GD25Q40CEIGR 与 ASM_FLASH_* |
| U15,U18 | ME1502AM5G | 两路 USB-A VBUS 电源开关，接收 PRON_A/B 并反馈 OCI_A#/B# | 图 cc7b1de97b07 / 第 1 页 / A6.1-USB3_CONN 网格 B1-D2，U15/U18 ME1502AM5G |
| J3A,J3B | AUSB0289-K001C | 双层 USB-A 连接器，分别承载 USB2 D+/D-、SuperSpeed RX/TX 和 VBUS | 图 cc7b1de97b07 / 第 1 页 / A6.1-USB3_CONN 网格 A4-C4，J3A/J3B |
| J4 | BOOMELE HDMI-001 19P | CM4 HDMI0 输出连接器 | 图 e4600891aacd / 第 1 页 / A7-HDMI_OUT0 网格 A3-C4，J4 HDMI-001 19P |
| P1 | HDGC 0.5K-A-16PB | 16 针 LCD、SPI、I2C 触摸和背光接口 | 图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 C1-D2，P1 pins 1-16 |
| U22,J7 | ME1502AM5G / KH-ZH1.5LF-02A | GPIO20 PWM 控制的风扇电源开关与两针风扇接口 | 图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 A3-B4，U22 FAN_PWM/FAN_PWR 与 J7 |
| U25 | ATECC608B-TNGTLSU-G | 接入 SCL0/SDA0 的安全认证器件 | 图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 C3-D4，U25 ATECC608B-TNGTLSU-G |
| J5,J6,J10 | PH2.0_4P_SMT / HDGC_0.5K-A-4PBF | UART、I2C Grove 扩展与调试 UART 接口 | 图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 B2-C3，J5/J6/J10 |
| U1 | AW88298 | I2C 配置、I2S 输入的差分扬声器功放 | 图 f34dae3a04da / 第 1 页 / A8.1-AUDIO 网格 A1-B2，U1 AW88298 |
| J9 | KH-ZH1.5LF-02A | SPK_VOP/SPK_VON 两针差分扬声器接口 | 图 f34dae3a04da / 第 1 页 / A8.1-AUDIO 网格 A2，J9 与 SPK_VOP/SPK_VON |

## 系统结构

### CM4Stack 载板架构

载板围绕 U3 Raspberry Pi CM4 接口构建，包含 12V 转多路电源、RJ45、USB-C OTG、ASM3042 双 USB 3.x、HDMI0、LCD/触摸、UART/I2C Grove、RTC、安全芯片、风扇和 I2S 功放。

- 参数与网络：`compute=U3 RPI-CM4`；`power=MP8759/AW32901/RS3236/SY8003`；`network=J1 RJ45`；`usb_otg=J2 USB-C`；`usb_host=U11 ASM3042,J3A/J3B`；`display=J4 HDMI0,P1 LCD`；`rtc=U6 BM8563`；`security=U25 ATECC608B-TNGTLSU-G`；`audio=U1 AW88298`
- 证据：图 e7cec62f297b / 第 1 页 / A2-PWR 整页; 图 21cab0d24f14 / 第 1 页 / A6-USB3_BRIDGE 整页; 图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 整页

### 载板原理图日期

十张原理图页面标题栏均显示 Date 1/05/2023，文件分区从 A2-PWR 到 A9-DUMMY。

- 参数与网络：`date=1/05/2023`；`first_sheet=A2-PWR`；`last_sheet=A9-DUMMY`；`local_pages=10`
- 证据：图 e7cec62f297b / 第 1 页 / A2-PWR 网格 D3-D4 标题栏; 图 c3a5aba9a1c8 / 第 1 页 / A9-DUMMY 网格 D3-D4 标题栏

### 未使用的 CM4 高速接口

A9-DUMMY 页将 HDMI1、SD_CMD/CLK/DAT0~7、CAM0/CAM1 和 DSI0/DSI1 的全部列出引脚标为未连接。

- 参数与网络：`unused=HDMI1,SD,CAM0,CAM1,DSI0,DSI1`
- 证据：图 c3a5aba9a1c8 / 第 1 页 / A9-DUMMY 网格 A1-C3，U3K/U3E/U3F/U3G/U3H/U3I 全部 NC 标记

## 核心器件

### Raspberry Pi CM4 接口

U3 分页单元统一标为 RPI-CM4，并通过 DF40HC(3.0)-100DS-0.4v 接口引出 5V 输入、3.3V/1.8V 输出、控制、GPIO、以太网、USB、PCIe 和 HDMI0。

- 参数与网络：`reference=U3`；`symbol=RPI-CM4(DF40HC(3.0)-100DS-0.4v)`；`input=+5V`；`outputs=CM4_3.3V,CM4_1.8V`；`interfaces=GPIO,Ethernet,USB2,PCIe,HDMI0`
- 证据：图 e7cec62f297b / 第 1 页 / A2-PWR 网格 C1-D2，U3B/U3L; 图 983e328ee808 / 第 1 页 / A4-ETH 网格 A1-B1，U3C; 图 21cab0d24f14 / 第 1 页 / A6-USB3_BRIDGE 网格 A1，U3D

### BM8563 RTC

U6 BM8563 通过 SCL0/SDA0 接 CM4，Y1 TXC/9H0320 与 C22/C23 7pF 组成时钟网络，INT 输出为 nRTC_INT。

- 参数与网络：`reference=U6`；`part_number=BM8563`；`bus=SCL0,SDA0`；`interrupt=nRTC_INT`；`crystal=Y1 TXC/9H0320`；`load_caps=C22 7pF,C23 7pF`
- 证据：图 5827982711c4 / 第 1 页 / A3-PI_SYS 网格 B1-C2，U6/Y1/C22/C23

### ATECC608B 安全器件

U25 标为 ATECC608B-TNGTLSU-G，VCC 接 VCC_3V3，SCL/SDA 接 SCL0/SDA0，地引脚接 GND。

- 参数与网络：`reference=U25`；`part_number=ATECC608B-TNGTLSU-G`；`bus=SCL0,SDA0`；`supply=VCC_3V3`
- 证据：图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 C3-D4，U25

## 电源

### 12V DC 输入保护

J8 DC 插座的 VIN_PLUG 经 FUSE1 30V/2A/PPTC 与 L1 SMW5045S102LTT 到 VIN_12V，输入侧有 C1~C4 10uF/50V 和 D1 SMBJ24CA。

- 参数与网络：`connector=J8 XKB DC-005A-2.5A-1.65`；`input_net=VIN_PLUG`；`fuse=FUSE1 30V/2A/PPTC`；`filter=L1 SMW5045S102LTT`；`protected_net=VIN_12V`；`tvs=D1 SMBJ24CA`
- 证据：图 e7cec62f297b / 第 1 页 / A2-PWR 网格 A1-A4，VIN_PLUG/FUSE1/L1/D1/J8

### MP8759 主 5V 电源

U2 MP8759 以 VIN_12V 供电，EN 接 VIN_EN，SW 经 L2 CKST353220-1.5uH 输出 VCC_5V，反馈分压为 R4 41.2K/1% 与 R5 5.6K/1%。

- 参数与网络：`reference=U2`；`part_number=MP8759`；`input=VIN_12V`；`enable=VIN_EN`；`output=VCC_5V`；`inductor=L2 CKST353220-1.5uH`；`feedback=R4 41.2K,R5 5.6K`
- 证据：图 e7cec62f297b / 第 1 页 / A2-PWR 网格 B1-B3，U2/L2/R4/R5/VCC_5V

### AW32901 系统 5V 路径

U26 AW32901 的三个 IN 接 VCC_5V、三个 OUT 接 VCC_5V_SYS，OVLO 由 R53 35.7K 与 R54 10.2K 分压，EN 与 GND 引脚接地。

- 参数与网络：`reference=U26`；`part_number=AW32901`；`input=VCC_5V`；`output=VCC_5V_SYS`；`ovlo_divider=R53 35.7K,R54 10.2K`；`enable_connection=GND`
- 证据：图 e7cec62f297b / 第 1 页 / A2-PWR 网格 A4-C4，U26/R53/R54

### CM4 5V 输入与 3.3V/1.8V 输出

U3L 的六个 +5V Input 引脚接 VCC_5V_SYS；CM4_3.3V Output 接 VCC_3V3，CM4_1.8V Output 接 VCC_1V8。

- 参数与网络：`module_input=VCC_5V_SYS`；`module_3v3_output=VCC_3V3`；`module_1v8_output=VCC_1V8`
- 证据：图 e7cec62f297b / 第 1 页 / A2-PWR 网格 C1-C2，U3L +5V/CM4_3.3V/CM4_1.8V

### 2.5V 与 1.1V 辅助电源

U4 RS3236-2.5YF5 将 VCC_3V3 转为 VCC_2V5；U5 SY8003 将 VCC_5V_SYS 经 L3 WPN3012H2R2MT 转为 VCC_1V1，反馈为 R6 100K/R7 120K。

- 参数与网络：`vcc_2v5=U4 RS3236-2.5YF5 from VCC_3V3`；`vcc_1v1=U5 SY8003 from VCC_5V_SYS`；`inductor=L3 WPN3012H2R2MT`；`feedback=R6 100K,R7 120K`
- 证据：图 e7cec62f297b / 第 1 页 / A2-PWR 网格 C2-D3，U4/U5/L3/R6/R7

### RTC 后备电源

BAT1 XH414HG-IV01E 接 BM8563 VDD，VCC_3V3 经 D4 1N5819 和 R11 100R 向该节点供电，C24 100nF 与 C25 22uF 对地。

- 参数与网络：`battery=BAT1 XH414HG-IV01E`；`charge_path=VCC_3V3->D4 1N5819->R11 100R`；`rtc_supply=U6 VDD`；`caps=C24 100nF,C25 22uF`
- 证据：图 5827982711c4 / 第 1 页 / A3-PI_SYS 网格 B2-C3，BAT1/D4/R11/C24/C25

### 双 USB-A VBUS 开关

U15/U18 ME1502AM5G 分别把 VCC_5V_SYS 切换为 VBUS1/VBUS2，EN 接 PRON_A/PRON_B，过流反馈为 OCI_A#/OCI_B#，并各使用 2N7002 调整 RSET 网络。

- 参数与网络：`port1=U15 VCC_5V_SYS->VBUS1,PRON_A,OCI_A#`；`port2=U18 VCC_5V_SYS->VBUS2,PRON_B,OCI_B#`；`rset_fets=FET1/FET2 2N7002 controlled by VIN_PRE`
- 证据：图 cc7b1de97b07 / 第 1 页 / A6.1-USB3_CONN 网格 B1-D2，U15/U18/FET1/FET2

### LCD 背光控制

VCC_3V3 经 R51 0R 和 FET3 SI2301 输出 LCD_BL，FET3 栅极由 LCD_BL_PWM 控制，并以 R47 10K 拉至 VCC_3V3 侧。

- 参数与网络：`input=VCC_3V3`；`series=R51 0R`；`switch=FET3 SI2301`；`control=LCD_BL_PWM GPIO6`；`gate_resistor=R47 10K`；`output=LCD_BL`
- 证据：图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 D2-D3，FET3/R51/R47/LCD_BL_PWM

### PWM 风扇电源

U22 ME1502AM5G 以 VCC_5V 供电，EN 接 FAN_PWM，RSET 由 R52 120K 接地，输出 FAN_PWR 至 J7 两针风扇接口。

- 参数与网络：`reference=U22`；`part_number=ME1502AM5G`；`input=VCC_5V`；`enable=FAN_PWM GPIO20`；`rset=R52 120K`；`output=FAN_PWR`；`connector=J7`
- 证据：图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 A3-B4，U22/J7

## 接口

### CM4 四对以太网接口

CM4 U3C 的 Ethernet_Pair0~3 差分对连接 J1 的 TD1~TD4；Ethernet_nLED1 与 Ethernet_nLED2 分别经 R15/R16 470R 驱动 RJ45 绿色与黄色 LED。

- 参数与网络：`pairs=ETH_P0_P/N,ETH_P1_P/N,ETH_P2_P/N,ETH_P3_P/N`；`connector=J1 RB1-2S5BAK1A`；`led_green=ETH_LEDG via R15 470R`；`led_yellow=ETH_LEDY via R16 470R`
- 证据：图 983e328ee808 / 第 1 页 / A4-ETH 网格 A1-B4，U3C/J1/R15/R16

### USB-C USB 2.0 OTG

CM4 U3N 的 USB_P/USB_N 直连 USB_D_P/USB_D_N 至 J2 USB-C 的 DP1/DP2 与 DN1/DN2；USB_OTG_ID 经 R50 10K 接 VIN_PRE。

- 参数与网络：`connector=J2 HDGC TYPE C-CQ-106PWB`；`data_plus=USB_D_P`；`data_minus=USB_D_N`；`otg_id=U3N pin101 through R50 10K to VIN_PRE`；`vbus=VCC_5V`
- 证据：图 3a741c6f2a08 / 第 1 页 / A5-USB_OTG 网格 A1-B3，U3N/J2/R50

### CM4 PCIe 至 ASM3042

CM4 PCIe_CLK、PCIe_RX、PCIe_TX、PCIe_nREQ、PCIe_nRST 接 U11 ASM3042 的 PE_CLK、PTX0、PRX0、PECLKREQ#、PE_RST#，时钟串联 R20/R22 33R，接收链路含 C33/C34 100nF。

- 参数与网络：`bridge=U11 ASM3042`；`clock=PCIE_CLK_P/N through R20/R22 33R`；`cm4_rx=PCIE_RX_P/N via C33/C34 100nF from PTX_0`；`cm4_tx=PCIE_TX_P/N to PRX0`；`control=PCIE_nREQ,PCIE_nRST`
- 证据：图 21cab0d24f14 / 第 1 页 / A6-USB3_BRIDGE 网格 A1-A3，U3D/U11A/R20/R22/C33/C34

### 双 USB-A 主机接口

ASM3042 输出 USB1/USB2 的 D+/D- 与 SuperSpeed TX/RX 差分对至 J3A/J3B；TX 对经 C61~C64 100nF 交流耦合，RX 对经 R27~R30 0R。

- 参数与网络：`connector=J3A/J3B AUSB0289-K001C`；`usb2=USB1_D_P/N,USB2_D_P/N`；`superspeed_tx=C61-C64 100nF`；`superspeed_rx=R27-R30 0R`；`ports=2`
- 证据：图 cc7b1de97b07 / 第 1 页 / A6.1-USB3_CONN 网格 A1-C4，J3A/J3B 与 USB1/USB2 信号

### CM4 HDMI0 输出

CM4 HDMI0 的 CLK、TX0、TX1、TX2 差分对及 CEC、HPD、SCL、SDA 连接 J4 19 针 HDMI 接口。

- 参数与网络：`connector=J4 BOOMELE HDMI-001 19P`；`video_pairs=HDMI_CLK,HDMI_TX0,HDMI_TX1,HDMI_TX2`；`control=HDMI_CEC,HDMI_HPD,HDMI_SCL,HDMI_SDA`
- 证据：图 e4600891aacd / 第 1 页 / A7-HDMI_OUT0 网格 A1-C4，U3J/J4

### LCD 与触摸 16 针接口

P1 引出 LCD_BL、LCD_SPI_DC/SCK/CS/MISO/RES/MOSI、VCC_3V3、SCL0/SDA0、LCD_TOUCH_RST/INT 与多针 GND。

- 参数与网络：`connector=P1 HDGC 0.5K-A-16PB`；`backlight=pins1-2 LCD_BL`；`spi=pin4 DC,pin5 SCK,pin7 CS,pin8 MISO,pin9 RES,pin10 MOSI`；`power=pin6 VCC_3V3`；`touch_i2c=pin12 SCL0,pin13 SDA0`；`touch_control=pin14 RST,pin15 INT`
- 证据：图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 C1-D2，P1 pins 1-16

### UART、I2C 与调试接口

J5 通过 R39/R41 47R 引出 EXT_TXD3/EXT_RXD3，J6 通过 R44/R45 47R 引出 EXT_I2C_SCL1/SDA1；两口均由 VCC_5V 经 0.5A/16V 保险丝供电，J10 引出 DBG_TXD0/DBG_RXD0/VCC_5V_SYS/GND。

- 参数与网络：`uart_port=J5 EXT_TXD3 GPIO12,EXT_RXD3 GPIO4`；`i2c_port=J6 EXT_I2C_SCL1 GPIO3,EXT_I2C_SDA1 GPIO2`；`power=VCC_5V through FUSE3/FUSE4 0.5A/16V`；`debug=J10 DBG_TXD0 GPIO14,DBG_RXD0 GPIO15,VCC_5V_SYS,GND`
- 证据：图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 A1-C3，U3M/J5/J6/J10

## 总线

### 板载与外部 I2C 上拉

SCL0/SDA0 由 R40/R42 2.2K 上拉到 VCC_3V3，EXT_I2C_SCL1/SDA1 由 R43/R46 2.2K 上拉到 VCC_3V3。

- 参数与网络：`i2c0=R40/R42 2.2K to VCC_3V3`；`i2c1=R43/R46 2.2K to VCC_3V3`
- 证据：图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 B1-C2，R40/R42/R43/R46

### AW88298 I2C 与 I2S

AW88298 的 SDA/SCL 接 SDA0/SCL0；BCK/WCK/DATAI 分别接 I2S_BCK、I2S_WCK、I2S_DAT，DATAO 未连接。

- 参数与网络：`i2c=SDA0,SCL0`；`i2s_bck=GPIO18 I2S_BCK`；`i2s_wck=GPIO19 I2S_WCK`；`i2s_data_in=GPIO21 I2S_DAT`；`data_out=NC`
- 证据：图 f34dae3a04da / 第 1 页 / A8.1-AUDIO 网格 B1-B2，U1 SDA/SCL/BCK/WCK/DATAI/DATAO; 图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 A1-B1，U3M I2S GPIO 映射

## GPIO 与控制信号

### CM4 外设 GPIO 映射

GPIO21/19/18 分别为 I2S_DAT/I2S_WCK/I2S_BCK，GPIO20 为 FAN_PWM，GPIO6 为 LCD_BL_PWM；GPIO7/11/8/25/10/22 分别为 LCD_SPI_SCK/CS/MISO/RES/MOSI/DC，GPIO24/23 为 LCD_TOUCH_RST/INT。

- 参数与网络：`audio=GPIO21 I2S_DAT,GPIO19 I2S_WCK,GPIO18 I2S_BCK`；`fan=GPIO20 FAN_PWM`；`backlight=GPIO6 LCD_BL_PWM`；`lcd_spi=GPIO7 SCK,GPIO11 CS,GPIO8 MISO,GPIO25 RES,GPIO10 MOSI,GPIO22 DC`；`touch=GPIO24 RST,GPIO23 INT`
- 证据：图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 A1-B2，U3M GPIO 信号

## 时钟

### ASM3042 20MHz 晶振

X1 标注 20MHz/10ppm/2520/20pF，连接 ASM_XI/ASM_XO，两端各由 C75/C76 20pF 接地。

- 参数与网络：`reference=X1`；`frequency=20MHz`；`tolerance=10ppm`；`package=2520`；`load=20pF`；`caps=C75 20pF,C76 20pF`
- 证据：图 21cab0d24f14 / 第 1 页 / A6-USB3_BRIDGE 网格 B3-B4，X1/C75/C76

## 复位

### CM4 下载与全局使能

CM4 nRPIBOOT 接 nRPI_BOOT，S1 按下将该网络接地；GLOBAL_EN 由 U7 SN74LVC1G125 输出驱动，nEXTRST 以 R55 10K 下拉。

- 参数与网络：`boot_net=nRPI_BOOT`；`boot_switch=S1 to GND`；`global_enable=U7 output GLOBAL_EN`；`external_reset=nEXTRST with R55 10K to GND`
- 证据：图 5827982711c4 / 第 1 页 / A3-PI_SYS 网格 A1-D3，U3A/S1/U7/R55

## 保护电路

### 以太网差分对 ESD

U9 PESDALC10N5VU 保护 ETH_P0 与 ETH_P1，U10 PESDALC10N5VU 保护 ETH_P2 与 ETH_P3，器件地引脚均接 GND。

- 参数与网络：`protector_1=U9 PESDALC10N5VU for pairs 0/1`；`protector_2=U10 PESDALC10N5VU for pairs 2/3`
- 证据：图 983e328ee808 / 第 1 页 / A4-ETH 网格 A2-B3，U9/U10

### USB-C CC、数据与 VBUS 保护

J2 CC1/CC2 各通过 R17/R18 5.1K 接地；USB_D_P/N 由 U24 PESDALC10N5VU 保护，VCC_5V 由 D2 SMAJ5.0A 对地钳位。

- 参数与网络：`cc1=R17 5.1K to GND`；`cc2=R18 5.1K to GND`；`data_esd=U24 PESDALC10N5VU`；`vbus_tvs=D2 SMAJ5.0A`
- 证据：图 3a741c6f2a08 / 第 1 页 / A5-USB_OTG 网格 B1-C3，R17/R18/U24/D2

### 双 USB-A 数据 ESD

U13/U14 分别保护 USB1 的 USB2 与 SuperSpeed 信号，U16/U17 分别保护 USB2 的 USB2 与 SuperSpeed 信号，器件均为 PESDALC10N5VU。

- 参数与网络：`port1=U13 USB1_D_P/N,U14 USB1_SS_R/T`；`port2=U16 USB2_D_P/N,U17 USB2_SS_R/T`；`part_number=PESDALC10N5VU`
- 证据：图 cc7b1de97b07 / 第 1 页 / A6.1-USB3_CONN 网格 A2-D3，U13/U14/U16/U17

### HDMI0 ESD 与 5V 保护

U19/U20 PESDALC10N5VU 保护四组 HDMI 高速差分对，U21 保护 CEC/SCL/SDA/HPD；VCC_5V 经 FUSE2 0.5A/16V 输出 HDMI_5V，并由 C69 22uF 去耦。

- 参数与网络：`high_speed_esd=U19/U20 PESDALC10N5VU`；`control_esd=U21 PESDALC10N5VU`；`power=VCC_5V->FUSE2 0.5A/16V->HDMI_5V`；`cap=C69 22uF`
- 证据：图 e4600891aacd / 第 1 页 / A7-HDMI_OUT0 网格 A2-C4，U19/U20/U21/FUSE2/C69

## 存储

### ASM3042 配置 Flash

U12 GD25Q40CEIGR 标注为需预烧写，通过 ASM_FLASH_CS/CLK/DO/DI 接 U11C SPI 接口，nWP/IO2 经 R21 0R 接地，nHOLD/IO3 接 VCC_3V3。

- 参数与网络：`reference=U12`；`part_number=GD25Q40CEIGR`；`note=需要预烧写`；`signals=ASM_FLASH_CS,ASM_FLASH_CLK,ASM_FLASH_DO,ASM_FLASH_DI`；`wp=R21 0R to GND`；`hold=VCC_3V3`
- 证据：图 21cab0d24f14 / 第 1 页 / A6-USB3_BRIDGE 网格 A3-B4，U12/U11C

## 音频

### AW88298 音频功放

U1 AW88298 的 IOVDD 接 VCC_3V3、DVDD 接 VCC_1V8、VDD 接 VCC_5V，PVDD/VBST 接 AW_PVDD，RSTN 接 nEXTRST，AD1 与 AD2 接地。

- 参数与网络：`reference=U1`；`part_number=AW88298`；`iovdd=VCC_3V3`；`dvdd=VCC_1V8`；`vdd=VCC_5V`；`boost=L4 WPN201610M1R0MT,AW_PVDD`；`reset=nEXTRST`；`address_pins=AD1=GND,AD2=GND`
- 证据：图 f34dae3a04da / 第 1 页 / A8.1-AUDIO 网格 A1-C2，U1 电源/复位/AD1/AD2

### 差分扬声器输出

AW88298 的 VOP/VON 输出为 SPK_VOP/SPK_VON 并接 J9 pins 1/2，两路各有 C78/C77 0.1nF/25V 对地。

- 参数与网络：`positive=U1 VOP->SPK_VOP->J9 pin1,C78 0.1nF to GND`；`negative=U1 VON->SPK_VON->J9 pin2,C77 0.1nF to GND`；`connector=J9 KH-ZH1.5LF-02A`
- 证据：图 f34dae3a04da / 第 1 页 / A8.1-AUDIO 网格 A1-A3，U1 VOP/VON、C77/C78、J9

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | CM4Stack 载板架构 | `compute=U3 RPI-CM4`；`power=MP8759/AW32901/RS3236/SY8003`；`network=J1 RJ45`；`usb_otg=J2 USB-C`；`usb_host=U11 ASM3042,J3A/J3B`；`display=J4 HDMI0,P1 LCD`；`rtc=U6 BM8563`；`security=U25 ATECC608B-TNGTLSU-G`；`audio=U1 AW88298` |
| 系统结构 | 载板原理图日期 | `date=1/05/2023`；`first_sheet=A2-PWR`；`last_sheet=A9-DUMMY`；`local_pages=10` |
| 核心器件 | Raspberry Pi CM4 接口 | `reference=U3`；`symbol=RPI-CM4(DF40HC(3.0)-100DS-0.4v)`；`input=+5V`；`outputs=CM4_3.3V,CM4_1.8V`；`interfaces=GPIO,Ethernet,USB2,PCIe,HDMI0` |
| 电源 | 12V DC 输入保护 | `connector=J8 XKB DC-005A-2.5A-1.65`；`input_net=VIN_PLUG`；`fuse=FUSE1 30V/2A/PPTC`；`filter=L1 SMW5045S102LTT`；`protected_net=VIN_12V`；`tvs=D1 SMBJ24CA` |
| 电源 | MP8759 主 5V 电源 | `reference=U2`；`part_number=MP8759`；`input=VIN_12V`；`enable=VIN_EN`；`output=VCC_5V`；`inductor=L2 CKST353220-1.5uH`；`feedback=R4 41.2K,R5 5.6K` |
| 电源 | AW32901 系统 5V 路径 | `reference=U26`；`part_number=AW32901`；`input=VCC_5V`；`output=VCC_5V_SYS`；`ovlo_divider=R53 35.7K,R54 10.2K`；`enable_connection=GND` |
| 电源 | CM4 5V 输入与 3.3V/1.8V 输出 | `module_input=VCC_5V_SYS`；`module_3v3_output=VCC_3V3`；`module_1v8_output=VCC_1V8` |
| 电源 | 2.5V 与 1.1V 辅助电源 | `vcc_2v5=U4 RS3236-2.5YF5 from VCC_3V3`；`vcc_1v1=U5 SY8003 from VCC_5V_SYS`；`inductor=L3 WPN3012H2R2MT`；`feedback=R6 100K,R7 120K` |
| 复位 | CM4 下载与全局使能 | `boot_net=nRPI_BOOT`；`boot_switch=S1 to GND`；`global_enable=U7 output GLOBAL_EN`；`external_reset=nEXTRST with R55 10K to GND` |
| 核心器件 | BM8563 RTC | `reference=U6`；`part_number=BM8563`；`bus=SCL0,SDA0`；`interrupt=nRTC_INT`；`crystal=Y1 TXC/9H0320`；`load_caps=C22 7pF,C23 7pF` |
| 电源 | RTC 后备电源 | `battery=BAT1 XH414HG-IV01E`；`charge_path=VCC_3V3->D4 1N5819->R11 100R`；`rtc_supply=U6 VDD`；`caps=C24 100nF,C25 22uF` |
| 接口 | CM4 四对以太网接口 | `pairs=ETH_P0_P/N,ETH_P1_P/N,ETH_P2_P/N,ETH_P3_P/N`；`connector=J1 RB1-2S5BAK1A`；`led_green=ETH_LEDG via R15 470R`；`led_yellow=ETH_LEDY via R16 470R` |
| 保护电路 | 以太网差分对 ESD | `protector_1=U9 PESDALC10N5VU for pairs 0/1`；`protector_2=U10 PESDALC10N5VU for pairs 2/3` |
| 接口 | USB-C USB 2.0 OTG | `connector=J2 HDGC TYPE C-CQ-106PWB`；`data_plus=USB_D_P`；`data_minus=USB_D_N`；`otg_id=U3N pin101 through R50 10K to VIN_PRE`；`vbus=VCC_5V` |
| 保护电路 | USB-C CC、数据与 VBUS 保护 | `cc1=R17 5.1K to GND`；`cc2=R18 5.1K to GND`；`data_esd=U24 PESDALC10N5VU`；`vbus_tvs=D2 SMAJ5.0A` |
| 接口 | CM4 PCIe 至 ASM3042 | `bridge=U11 ASM3042`；`clock=PCIE_CLK_P/N through R20/R22 33R`；`cm4_rx=PCIE_RX_P/N via C33/C34 100nF from PTX_0`；`cm4_tx=PCIE_TX_P/N to PRX0`；`control=PCIE_nREQ,PCIE_nRST` |
| 存储 | ASM3042 配置 Flash | `reference=U12`；`part_number=GD25Q40CEIGR`；`note=需要预烧写`；`signals=ASM_FLASH_CS,ASM_FLASH_CLK,ASM_FLASH_DO,ASM_FLASH_DI`；`wp=R21 0R to GND`；`hold=VCC_3V3` |
| 时钟 | ASM3042 20MHz 晶振 | `reference=X1`；`frequency=20MHz`；`tolerance=10ppm`；`package=2520`；`load=20pF`；`caps=C75 20pF,C76 20pF` |
| 接口 | 双 USB-A 主机接口 | `connector=J3A/J3B AUSB0289-K001C`；`usb2=USB1_D_P/N,USB2_D_P/N`；`superspeed_tx=C61-C64 100nF`；`superspeed_rx=R27-R30 0R`；`ports=2` |
| 电源 | 双 USB-A VBUS 开关 | `port1=U15 VCC_5V_SYS->VBUS1,PRON_A,OCI_A#`；`port2=U18 VCC_5V_SYS->VBUS2,PRON_B,OCI_B#`；`rset_fets=FET1/FET2 2N7002 controlled by VIN_PRE` |
| 保护电路 | 双 USB-A 数据 ESD | `port1=U13 USB1_D_P/N,U14 USB1_SS_R/T`；`port2=U16 USB2_D_P/N,U17 USB2_SS_R/T`；`part_number=PESDALC10N5VU` |
| 接口 | CM4 HDMI0 输出 | `connector=J4 BOOMELE HDMI-001 19P`；`video_pairs=HDMI_CLK,HDMI_TX0,HDMI_TX1,HDMI_TX2`；`control=HDMI_CEC,HDMI_HPD,HDMI_SCL,HDMI_SDA` |
| 保护电路 | HDMI0 ESD 与 5V 保护 | `high_speed_esd=U19/U20 PESDALC10N5VU`；`control_esd=U21 PESDALC10N5VU`；`power=VCC_5V->FUSE2 0.5A/16V->HDMI_5V`；`cap=C69 22uF` |
| GPIO 与控制信号 | CM4 外设 GPIO 映射 | `audio=GPIO21 I2S_DAT,GPIO19 I2S_WCK,GPIO18 I2S_BCK`；`fan=GPIO20 FAN_PWM`；`backlight=GPIO6 LCD_BL_PWM`；`lcd_spi=GPIO7 SCK,GPIO11 CS,GPIO8 MISO,GPIO25 RES,GPIO10 MOSI,GPIO22 DC`；`touch=GPIO24 RST,GPIO23 INT` |
| 接口 | LCD 与触摸 16 针接口 | `connector=P1 HDGC 0.5K-A-16PB`；`backlight=pins1-2 LCD_BL`；`spi=pin4 DC,pin5 SCK,pin7 CS,pin8 MISO,pin9 RES,pin10 MOSI`；`power=pin6 VCC_3V3`；`touch_i2c=pin12 SCL0,pin13 SDA0`；`touch_control=pin14 RST,pin15 INT` |
| 电源 | LCD 背光控制 | `input=VCC_3V3`；`series=R51 0R`；`switch=FET3 SI2301`；`control=LCD_BL_PWM GPIO6`；`gate_resistor=R47 10K`；`output=LCD_BL` |
| 接口 | UART、I2C 与调试接口 | `uart_port=J5 EXT_TXD3 GPIO12,EXT_RXD3 GPIO4`；`i2c_port=J6 EXT_I2C_SCL1 GPIO3,EXT_I2C_SDA1 GPIO2`；`power=VCC_5V through FUSE3/FUSE4 0.5A/16V`；`debug=J10 DBG_TXD0 GPIO14,DBG_RXD0 GPIO15,VCC_5V_SYS,GND` |
| 总线 | 板载与外部 I2C 上拉 | `i2c0=R40/R42 2.2K to VCC_3V3`；`i2c1=R43/R46 2.2K to VCC_3V3` |
| 核心器件 | ATECC608B 安全器件 | `reference=U25`；`part_number=ATECC608B-TNGTLSU-G`；`bus=SCL0,SDA0`；`supply=VCC_3V3` |
| 电源 | PWM 风扇电源 | `reference=U22`；`part_number=ME1502AM5G`；`input=VCC_5V`；`enable=FAN_PWM GPIO20`；`rset=R52 120K`；`output=FAN_PWR`；`connector=J7` |
| 音频 | AW88298 音频功放 | `reference=U1`；`part_number=AW88298`；`iovdd=VCC_3V3`；`dvdd=VCC_1V8`；`vdd=VCC_5V`；`boost=L4 WPN201610M1R0MT,AW_PVDD`；`reset=nEXTRST`；`address_pins=AD1=GND,AD2=GND` |
| 总线 | AW88298 I2C 与 I2S | `i2c=SDA0,SCL0`；`i2s_bck=GPIO18 I2S_BCK`；`i2s_wck=GPIO19 I2S_WCK`；`i2s_data_in=GPIO21 I2S_DAT`；`data_out=NC` |
| 音频 | 差分扬声器输出 | `positive=U1 VOP->SPK_VOP->J9 pin1,C78 0.1nF to GND`；`negative=U1 VON->SPK_VON->J9 pin2,C77 0.1nF to GND`；`connector=J9 KH-ZH1.5LF-02A` |
| 系统结构 | 未使用的 CM4 高速接口 | `unused=HDMI1,SD,CAM0,CAM1,DSI0,DSI1` |
| 内存与 Flash | CM4 模块内存与 eMMC 配置 | `source_document_module=CM4104032`；`source_document_ram=4GB`；`source_document_emmc=32GB`；`schematic=generic RPI-CM4 symbol` |
| 核心器件 | LCD 与触摸控制器型号 | `source_document_lcd=ST7789V2`；`source_document_touch=GT911`；`schematic=P1 interface only` |
| 音频 | 扬声器输出规格 | `source_document=16-bit I2S,2W speaker`；`schematic=AW88298 and J9 differential output only` |
| 接口 | USB 主机协议版本 | `source_document=USB 3.2`；`schematic=ASM3042 with USB2 and SuperSpeed pairs`；`ports=2` |
| 接口 | RJ45 以太网速率 | `source_document=1Gbps`；`schematic=four Ethernet pairs`；`connector=J1 RB1-2S5BAK1A` |

## 待确认事项

- `memory.cm4-configuration`：产品源文档标注 CM4104032、4GB RAM 和 32GB eMMC，但原理图仅显示通用 RPI-CM4 接口符号，未标出安装模块 SKU、RAM 或 eMMC 容量。（证据：图 e7cec62f297b / 第 1 页 / A2-PWR 网格 C1-D2，U3B/U3L 仅标 RPI-CM4 接口）
- `component.display-controller`：产品源文档标注 ST7789V2 与 GT911，原理图只给出 P1 的 LCD_SPI、SCL0/SDA0 和触摸复位/中断信号，未显示这两颗控制器。（证据：图 6bd2eda0b779 / 第 1 页 / A8-RPI_GPIO 网格 C1-D2，P1 仅示接口信号）
- `audio.output-rating`：产品源文档标注 AW88298 16-bit I2S 与 2W 扬声器，但功放页未给出音频位宽、扬声器型号、阻抗或额定功率。（证据：图 f34dae3a04da / 第 1 页 / A8.1-AUDIO 网格 A1-C3，U1/J9 未标位宽、阻抗或功率）
- `interface.usb-standard`：产品源文档称两个接口支持 USB 3.2；原理图可确认 ASM3042、两路 USB2 和 SuperSpeed 差分对，但未直接标注 USB 3.2 代际或链路速率。（证据：图 21cab0d24f14 / 第 1 页 / A6-USB3_BRIDGE 网格 A1-C2，ASM3042 信号; 图 cc7b1de97b07 / 第 1 页 / A6.1-USB3_CONN 网格 A1-C4，双 USB-A SuperSpeed 信号）
- `interface.ethernet-speed`：产品源文档标注 1Gbps；原理图显示 CM4 四对 Ethernet_Pair0~3 和 RJ45，但未在页内标注协商速率。（证据：图 983e328ee808 / 第 1 页 / A4-ETH 网格 A1-B4，四对 Ethernet 与 J1，未标速率）
- `review.cm4-configuration`：量产 CM4Stack 安装的 CM4 是否确认为 CM4104032、4GB RAM 和 32GB eMMC？；原因：原理图使用通用 RPI-CM4 接口符号，未显示模块 SKU 和容量。
- `review.display-controller`：P1 所接显示与触摸模组是否分别使用 ST7789V2 和 GT911？；原因：原理图只显示接口与 GPIO，没有显示控制器器件型号。
- `review.audio-rating`：CM4Stack 的扬声器具体型号、阻抗、额定 2W 条件和 I2S 位宽是什么？；原因：AW88298 页只给出连接，未给出负载或数字音频格式参数。
- `review.usb-standard`：ASM3042 双主机口对应的准确 USB 3.2 代际与标称链路速率是什么？；原因：原理图有 SuperSpeed 信号，但没有直接标注协议代际或速率。
- `review.ethernet-speed`：CM4Stack RJ45 的量产配置是否保证 1Gbps 链路能力？；原因：原理图显示四对以太网信号，但未直接标注速率。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e7cec62f297b44514f2d4817136aa181819818f9b0dd84f9eb6091d1d9e952d5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/484/Sch_M5_EdgeCM4_sch_02.png` |
| 2 | 1 | `5827982711c4ed76d6ae534c029ee55422dd82547b8c86612796e3a5a98a185b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/484/Sch_M5_EdgeCM4_sch_03.png` |
| 3 | 1 | `983e328ee8083dda0fbb7bb36fabfae002d76f7a0fe0e113bd087729ed4df217` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/484/Sch_M5_EdgeCM4_sch_04.png` |
| 4 | 1 | `3a741c6f2a088d35cc136beecfa28dd7ed5c899baea0ff396008749a80e2c4d9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/484/Sch_M5_EdgeCM4_sch_05.png` |
| 5 | 1 | `21cab0d24f141221881f50cc3eba7f5163aa0512a7a642726e996b9654577337` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/484/Sch_M5_EdgeCM4_sch_06.png` |
| 6 | 1 | `cc7b1de97b07f1817d5deeffff34178de945414027b87cbffd6ac03831f02a57` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/484/Sch_M5_EdgeCM4_sch_07.png` |
| 7 | 1 | `e4600891aacd480c560a21485d85b31cff39e1ff5414c450403c8304c34a96f8` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/484/Sch_M5_EdgeCM4_sch_08.png` |
| 8 | 1 | `6bd2eda0b7790cced3493781de59f44bf470e06ca3ccb186725f03363bf8791e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/484/Sch_M5_EdgeCM4_sch_09.png` |
| 9 | 1 | `f34dae3a04daf524a8a9d40b5c941994e8a9810cfe57bbe7a2bbf3713cb910dc` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/484/Sch_M5_EdgeCM4_sch_10.png` |
| 10 | 1 | `c3a5aba9a1c820c30ed45af3cfa6f25245fac617e840d6a5e5871af656363c61` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/484/Sch_M5_EdgeCM4_sch_11.png` |

---

源文档：`zh_CN/core/CM4Stack.md`

源文档 SHA-256：`6bf2f4bc9c749594bd7afa60840c5bd845ac0bf95be8cf4b79c02e2e435f3e49`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
