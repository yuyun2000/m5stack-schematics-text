# Cardputer Mesh Kit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Cardputer Mesh Kit |
| SKU | K152 |
| 产品 ID | `cardputer-mesh-kit-baeceb0b9c86` |
| 源文档 | `zh_CN/core/Cardputer_Mesh_Kit.md` |

## 概述

Cardputer Mesh Kit 由以 ESP32-S3FN8 为核心的 Cardputer-Adv 主机和 Cap LoRa-1262 扩展组成。主机原理图覆盖充电与多路电源、56 键 TCA8418 键盘、LCD、microSD、BMI270、ES8311/NS4150B 音频、Grove 与 14 Pin 扩展口；扩展模块包含 SX1262 射频链、GP-02 GNSS、MAX2659、PI4IOE5V6408 和 Grove 接口。

## 检索关键词

`Cardputer Mesh Kit`、`K152`、`Cardputer-Adv`、`Cap LoRa-1262`、`Stamp-S3A`、`ESP32-S3FN8`、`SX1262`、`GP-02`、`MAX2659`、`PI4IOE5V6408`、`0900FM15K0039`、`FM8625H`、`TCA8418RTWR`、`0x34`、`BMI270`、`0x69`、`ES8311`、`NS4150B`、`TP4057`、`SY7088`、`SY8089`、`JW5712`、`AW35122FDR`、`WS2812`、`microSD`、`EXT 2.54-14P`、`Grove`、`I2C`、`SPI`、`GNSS`、`LoRa`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1/U1 (Stamp-S3A) | ESP32-S3FN8 | Cardputer-Adv 主控制器与 Stamp-S3A 核心模组 | 图 b721dfa2ce19 / 第 1 页 / D2-D3 M1 STAMP-S3-DIP-1.27 及 P1/P2 引脚连接; 图 1156e645de35 / 第 1 页 / A2-C3 U1 主控符号，底部标注 ESP32-S3FN8 |
| U1 (charger) | TP4057 | 单节锂电池充电管理 | 图 b721dfa2ce19 / 第 1 页 / A1 U1 TP4057，连接 +5VIN、VBAT_IN 和 PROG R5 |
| U2/U4 (mainboard power) | SY7088/SY8089 | 主板 5 V 升压与 3.3 V 降压转换 | 图 b721dfa2ce19 / 第 1 页 / A3-A4 U2 SY7088 +5VOUT 电路及 B3 U4 SY8089 +3.3V 电路 |
| U9 | TCA8418RTWR | 56 键矩阵键盘 I2C 控制器 | 图 cf469cc225c4 / 第 1 页 / B1 U9 TCA8418RTWR 及 ROW0-6/COL0-7 键盘矩阵 |
| U7 | BMI270 | 六轴惯性传感器 | 图 3162cda432ca / 第 1 页 / A1-B1 U7 BMI270，标注 7-bit Address 69H |
| U6 | ES8311 | 音频编解码器 | 图 3162cda432ca / 第 1 页 / C1-C2 U6 ES8311，连接 G8/G9 和 I2S 信号 |
| U5 | NS4150B | 扬声器 Class-D 音频功率放大器 | 图 3162cda432ca / 第 1 页 / B2-B3 U5 NS4150B 及 J4 差分扬声器输出 |
| U8 (microphone) | MSM381A3729H9BPC | 模拟 MEMS 麦克风 | 图 3162cda432ca / 第 1 页 / C1-D1 U8 麦克风符号，输出 MIC_P/MIC_N |
| J3 | TF-015 | microSD 卡座 | 图 b721dfa2ce19 / 第 1 页 / D1 J3 TF-015，连接 G12/G14/G40/G39 |
| P3 | HDR-SMD_14P-P2.54 | Cardputer-Adv 与 Cap LoRa-1262 的 14 Pin 扩展接口 | 图 6f970d99f036 / 第 1 页 / B2-C3 P3 HDR-SMD_14P-P2.54 完整引脚表 |
| U4 (Stamp-S3A) | JW5712 | Stamp-S3A 5 V 至 3.3 V 降压转换器 | 图 1156e645de35 / 第 1 页 / D1-D3 DCDC 区域 U4 JW5712、L4 和 VDD_3V3 输出 |
| U2 (LCD power) | AW35122FDR | LCD 背光电源/使能器件 | 图 1156e645de35 / 第 1 页 / A3 LCD 区域 U2 AW35122FDR，EN 接 DISP_BL，输出 BL_3V3 |
| U3 (RGB) | WS2812 | Stamp-S3A RGB LED | 图 1156e645de35 / 第 1 页 / B3 RGB LED 区域 U3 WS2812，DI=SK_DIN、DO=SK_DOUT |
| M1 (LoRa module) | Stamp LoRa-1262 Mini | Cap LoRa-1262 的 LoRa 子模组 | 图 ca8220583ff6 / 第 1 页 / A3-A4 M1 Stamp LoRa-1262 Mini，列出 RST/BUSY/IRQ/SCK/MOSI/MISO/NSS/BYPASS/ANT |
| U2 (Cap IO) | PI4IOE5V6408ZTAEX | Cap LoRa-1262 I2C IO 扩展器 | 图 ca8220583ff6 / 第 1 页 / B1-C2 U2 PI4IOE5V6408ZTAEX，P0=BYPASS、P1=SHUT_DOWN |
| M2 | GP-02 | GNSS 接收模块 | 图 ca8220583ff6 / 第 1 页 / C2-D3 M2 GP-02，TXD1/RXD1、VBAT、VCC、ANT 引脚 |
| U1 (GNSS LNA) | MAX2659 | GNSS 天线低噪声放大器 | 图 ca8220583ff6 / 第 1 页 / C3 U1 MAX2659，RFIN 连接天线匹配，RFOUT 连接 GP-02 ANT |
| U1 (LoRa RF) | SX1262 | LoRa 收发器 | 图 77b258457736 / 第 1 页 / A1-A3 U1 SX1262，列出 SX_NRST、SPI、BUSY、DIO1/2/3 和 RF 引脚 |
| U3 (LoRa switch) | 0900FM15K0039 | SX1262 RFO/RFIP/RFIN 射频路径切换 | 图 77b258457736 / 第 1 页 / A3-A4 U3 0900FM15K0039，连接 SX_RFO、SX_RFIP、SX_RFIN 与 SX_SRFI/SX_SRFO |
| U2 (LoRa RF) | FM8625H | LoRa 天线射频开关/放大路径器件 | 图 77b258457736 / 第 1 页 / A5-A6 U2 FM8625H，RF1/RF2 接 SX_SRFO/SX_SRFI，CTRL 接 SX_DIO2 |

## 系统结构

### Cardputer-Adv 主控制器

Cardputer-Adv 使用 Stamp-S3A 形态的 M1 模组；模组内部 U1 标注为 ESP32-S3FN8，并通过两侧排针引出 GPIO0–18、GPIO33–46、EN、TX、RX、5V 和 3V3。

- 参数与网络：`module=Stamp-S3A`；`soc=ESP32-S3FN8`；`mainboard_reference=M1`；`module_reference=U1`
- 证据：图 b721dfa2ce19 / 第 1 页 / D2-D3 M1 STAMP-S3-DIP-1.27 与 P1/P2 排针; 图 1156e645de35 / 第 1 页 / A2-C3 U1 ESP32-S3FN8 及右侧 GPIO 网络

## 电源

### Cardputer-Adv 充电链

U1 TP4057 的 VCC 经 R1 0.8 Ω 接 +5VIN，BAT 接 VBAT_IN，PROG 经 R5 3.3 kΩ 接地；VBAT_IN 通过 Q1 LP3218DT1G 电源路径形成 VBAT_OUT。

- 参数与网络：`charger=TP4057`；`input=+5VIN via R1 0.8R`；`battery_node=VBAT_IN`；`program_resistor=R5 3.3k`；`power_path=Q1 LP3218DT1G to VBAT_OUT`
- 证据：图 b721dfa2ce19 / 第 1 页 / A1-A3 U1 TP4057、R1/R5、VBAT_IN、Q1 和 VBAT_OUT 网络

### Cardputer-Adv 5 V 与 3.3 V 电源

U2 SY7088 以 VBAT_OUT 为输入，经 L1 1.5 µH 生成 +5VOUT；U4 SY8089 以 VBAT_OUT 为输入，经 L2 4.7 µH 生成 +3.3V。

- 参数与网络：`boost_converter=U2 SY7088`；`boost_inductor=L1 1.5uH`；`boost_output=+5VOUT`；`buck_converter=U4 SY8089`；`buck_inductor=L2 4.7uH`；`buck_output=+3.3V`
- 证据：图 b721dfa2ce19 / 第 1 页 / A3-A4 U2 SY7088 +5VOUT 区域及 B3 U4 SY8089 +3.3V 区域

### Stamp-S3A 模组电源

Stamp-S3A 内部 U4 JW5712 以 VIN_5V 为输入，经 L4 MWTC201608S2R2 生成 VDD_3V3，图面标注输出电流范围 0–0.6 A。

- 参数与网络：`converter=U4 JW5712`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 MWTC201608S2R2`；`output_current_a=0-0.6`
- 证据：图 1156e645de35 / 第 1 页 / D1-D3 DCDC 区域 U4 JW5712、VIN_5V、L4 和 VDD_3V3

### Cap LoRa-1262 3.3 V 电源

Cap 板 U3 JW5712 以 +5V/+5VOUT 为输入，经 L2 WPN201610U2R2MT 生成 VDD_3V3，图面标注输出电流范围 0–0.6 A。

- 参数与网络：`converter=U3 JW5712`；`input=+5V/+5VOUT`；`output=VDD_3V3`；`inductor=L2 WPN201610U2R2MT`；`output_current_a=0-0.6`
- 证据：图 ca8220583ff6 / 第 1 页 / A1-A3 U3 JW5712、L2 与 VDD_3V3 电源链

## 接口

### Cardputer-Adv HY2.0 I2C 接口

J2 HY-2.0_IIC 的 1–4 脚依次为 IIC_SCL/G1、IIC_SDA/G0、VCC、GND；SCL/SDA 由 R3/R10 10 kΩ 上拉到 3.3 V，VCC 通过 SW2 在 +5VOUT 与 +5VIN 间选择。

- 参数与网络：`pinout=1:SCL/G1,2:SDA/G0,3:VCC,4:GND`；`pullups=R3=10k,R10=10k`；`power_selector=SW2:+5VOUT/+5VIN`
- 证据：图 b721dfa2ce19 / 第 1 页 / C3-C4 SW2、+5VGrove、R3/R10、D6-D8 与 J2 HY-2.0_IIC

### Cardputer-Adv EXT 2.54-14P

P3 的 1–14 脚依次为 RESET/G3、INT/G4、BUSY/G6、SCK/G40、MOSI/G14、MISO/G39、CS/G5、GPS-TX/G15、GPS-RX/G13、SCL/G9、SDA/G8、5VOUT、GND、5VIN。

- 参数与网络：`reference=P3`；`pinout=1:RESET/G3,2:INT/G4,3:BUSY/G6,4:SCK/G40,5:MOSI/G14,6:MISO/G39,7:CS/G5,8:GPS-TX/G15,9:GPS-RX/G13,10:SCL/G9,11:SDA/G8,12:5VOUT,13:GND,14:5VIN`
- 证据：图 6f970d99f036 / 第 1 页 / B2-C3 P3 HDR-SMD_14P-P2.54 两侧 1–14 脚网络

### Stamp-S3A LCD 接口

ESP32-S3FN8 的 LCD 信号为 DISP_RST=GPIO33、DISP_RS=GPIO34、DISP_MOSI=GPIO35、DISP_SCK=GPIO36、DISP_CS=GPIO37、DISP_BL=GPIO38；U2 AW35122FDR 由 DISP_BL 使能并输出 BL_3V3。

- 参数与网络：`reset=GPIO33`；`data_command=GPIO34`；`mosi=GPIO35`；`sck=GPIO36`；`chip_select=GPIO37`；`backlight_enable=GPIO38`；`backlight_power=U2 AW35122FDR/BL_3V3`
- 证据：图 1156e645de35 / 第 1 页 / A2-A4 U1 GPIO33-38 LCD 网络及 U2/J3 LCD 电路

### Stamp-S3A USB Type-C

J2 USB Type-C 的 D- 与 D+ 经 L5 共模器件连接 ESP32-S3FN8 GPIO19/USB_DU_N 与 GPIO20/USB_DU_P；CC1/CC2 各有 5.1 kΩ 下拉，VIN_5V 经 F1 6 V/1 A PPTC 保护。

- 参数与网络：`connector=J2 USB-TYPEC`；`usb_d_minus=GPIO19`；`usb_d_plus=GPIO20`；`cc_resistors=R1=5.1k,R2=5.1k`；`fuse=F1 6V/1A/PPTC`
- 证据：图 1156e645de35 / 第 1 页 / D3-D4 Type-A USB 标题区域 J2 USB-TYPEC、L5、R1/R2、F1 与 USB_DU_N/P

### Cap LoRa-1262 14 Pin 接口

Cap 板 P1 的 1–14 脚依次为 GPS-TX/G15、GPS-RX/G13、SCL/G1、SDA/G0、5VOUT、GND、5VIN、RST/G3、IRQ/G4、BUSY/G6、SCK/G40、MOSI/G14、MISO/G39、NSS/G5，与 Cardputer-Adv P3 信号逐项对应。

- 参数与网络：`reference=P1`；`pinout=1:GPS-TX/G15,2:GPS-RX/G13,3:SCL/G1,4:SDA/G0,5:5VOUT,6:GND,7:5VIN,8:RST/G3,9:IRQ/G4,10:BUSY/G6,11:SCK/G40,12:MOSI/G14,13:MISO/G39,14:NSS/G5`
- 证据：图 ca8220583ff6 / 第 1 页 / D3-D4 P1 HDR-SMD_14P-P2.54 两侧 1–14 脚网络; 图 6f970d99f036 / 第 1 页 / B2-C3 Cardputer-Adv P3 对应信号表

### Cap LoRa-1262 Grove 接口

J2 GROVE 4P 的引脚依次为 SCL、SDA、5V、GND，5V 引脚连接 +5VOUT。

- 参数与网络：`pinout=SCL,SDA,5V,GND`；`supply=+5VOUT`
- 证据：图 ca8220583ff6 / 第 1 页 / C1-D1 J2 GROVE 4P 的 SCL/SDA/5V/GND 网络

## 总线

### 56 键矩阵键盘

U9 TCA8418RTWR 使用 ROW0–ROW6 与 COL0–COL7 形成 7×8 矩阵并连接 S1–S56；SDA=G8、SCL=G9、INT=G11，三路由 3.3 kΩ 电阻上拉到 3.3 V。

- 参数与网络：`controller=TCA8418RTWR`；`matrix=7x8`；`keys=56`；`sda=G8`；`scl=G9`；`interrupt=G11`；`pullups=R35-R37 3.3k`
- 证据：图 cf469cc225c4 / 第 1 页 / B1-D4 U9、ROW0-6/COL0-7 和 S1-S56 完整键盘矩阵

### Cap PI4IOE5V6408 控制

U2 PI4IOE5V6408ZTAEX 通过 SCL/SDA 接入 Cap I2C，总线由未装配的 R5/R6 10 kΩ 上拉位置预留；P0 输出 BYPASS，P1 输出 SHUT_DOWN。

- 参数与网络：`part_number=PI4IOE5V6408ZTAEX`；`scl=SCL`；`sda=SDA`；`optional_pullups=R5/R6 10k NC`；`p0=BYPASS`；`p1=SHUT_DOWN`
- 证据：图 ca8220583ff6 / 第 1 页 / B1-C2 U2 PI4IOE5V6408ZTAEX、R5/R6 NC、P0 BYPASS、P1 SHUT_DOWN

## 总线地址

### 键盘控制器 I2C 地址

TCA8418RTWR 上方标注 7-bit Address 34H，即 7 位 I2C 地址 0x34。

- 参数与网络：`part_number=TCA8418RTWR`；`i2c_address=0x34`
- 证据：图 cf469cc225c4 / 第 1 页 / B1 U9 下方 7-bit Address 34H 注记

## GPIO 与控制信号

### EN、Boot 与红外发射

BTN1 按下时将 EN 接地，BTN2 按下时将 G0 接地，两路均有 10 kΩ 上拉和 PESDNC2FD3V3B 保护；红外发射管 IR1 由 G44 驱动并串联 R14 22 Ω 到地。

- 参数与网络：`reset_button=BTN1/EN`；`boot_button=BTN2/G0`；`pullups=R15=10k,R18=10k`；`esd=D4,D5 PESDNC2FD3V3B`；`ir_gpio=G44`；`ir_resistor=R14 22R`
- 证据：图 b721dfa2ce19 / 第 1 页 / C1 BTN1/BTN2 及 D4/D5/R15/R18；D4 右侧 IR1-G44-R14 网络

### Stamp-S3A RGB LED 与用户键

U3 WS2812 的 DI=SK_DIN，SK_DIN 连接 ESP32-S3FN8 GPIO21；用户键 S1 连接 GPIO0，按下时接地并由 R4 10 kΩ 上拉到 VDD_3V3。

- 参数与网络：`rgb_led=U3 WS2812`；`rgb_data=GPIO21/SK_DIN`；`user_button=S1/GPIO0`；`button_pullup=R4 10k`
- 证据：图 1156e645de35 / 第 1 页 / B3 RGB LED U3 WS2812 及 B3-C3 BTN-USER S1/GPIO0 电路

## 时钟

### SX1262 参考时钟

X1 X1G0041310042 为 SX1262 提供 32 MHz 参考，输出经 R3 220 Ω 和 C6 10 nF 连接 SX_32M_REF；振荡器电源 VDD_OCXO 由 SX_DIO3 经 FB1 滤波提供。

- 参数与网络：`oscillator=X1 X1G0041310042`；`frequency_mhz=32`；`output_network=R3 220R,C6 10nF`；`power_control=SX_DIO3 via FB1`
- 证据：图 77b258457736 / 第 1 页 / B2-B4 X1 X1G0041310042、VDD_OCXO、SX_DIO3、FB1、R3/C6 与 SX_32M_REF

## 存储

### Cardputer-Adv microSD

J3 TF-015 的 CS=G12、MOSI=G14、CLK=G40、MISO=G39，四路均串联 33 Ω 电阻并配置 PESDNC2FD3V3B 对地保护。

- 参数与网络：`chip_select=G12`；`mosi=G14`；`clock=G40`；`miso=G39`；`series_resistors=R19-R22 33R`；`protection=D9-D12 PESDNC2FD3V3B`
- 证据：图 b721dfa2ce19 / 第 1 页 / D1 J3 TF-015、G12/G14/G40/G39、R19-R22 和 D9-D12

## 音频

### ES8311 音频接口

U6 ES8311 的控制总线 CCLK=G9、C_DATA=G8；数字音频 SCLK=G41、ASDOUT=G46、LRCK=G43、DSDIN=G42，模拟麦克风 MIC_P/MIC_N 经 C22/C23 两只 1 µF 电容接入 MIC1P/MIC1N。

- 参数与网络：`codec=ES8311`；`i2c_scl=G9`；`i2c_sda=G8`；`i2s_sclk=G41`；`i2s_asdout=G46`；`i2s_lrck=G43`；`i2s_dsdin=G42`；`microphone_inputs=MIC_P,MIC_N`
- 证据：图 3162cda432ca / 第 1 页 / C1-C2 U6 ES8311 的 G8/G9/G41/G46/G43/G42 与 C22/C23 MIC_P/MIC_N 网络

### 扬声器与耳机输出

DAC_P 经 U5 NS4150B 放大后由 VOP/VON 经 FB1/FB2 输出到 J4 两针扬声器接口；DAC_P 还连接 PJ-342 音频插座，HP_DET 通过该插座检测，AMP_EN 控制放大器使能。

- 参数与网络：`amplifier=NS4150B`；`speaker_connector=J4`；`speaker_outputs=VOP,VON via FB1,FB2`；`headphone_connector=PJ-342`；`detect=HP_DET`；`enable=AMP_EN`
- 证据：图 3162cda432ca / 第 1 页 / B2-B3 U5 NS4150B-J4 差分输出及 C3-D3 DAC_P/HP_DET/AMP_EN-PJ-342 电路

## 传感器

### BMI270 IMU

U7 BMI270 的 SDX/SDA=G8、SCX/SCL=G9；SDO 由 R43 3.3 kΩ 上拉到 3.3 V，图面标注 7 位地址 0x69。

- 参数与网络：`part_number=BMI270`；`sda=G8`；`scl=G9`；`sdo_pullup=R43 3.3k`；`i2c_address=0x69`
- 证据：图 3162cda432ca / 第 1 页 / A1-B1 U7 BMI270、G8/G9、R43 与 7-bit Address 69H

## 射频

### Cap GNSS 接口与射频链

M2 GP-02 的 TXD1=G15、RXD1=G13；GNSS 天线 J1 ANT181804 经 C5 470 pF、L1 6.8 nH 接 U1 MAX2659 RFIN，MAX2659 RFOUT 连接 GP-02 ANT。

- 参数与网络：`gnss_module=M2 GP-02`；`uart_tx=G15`；`uart_rx=G13`；`antenna=J1 ANT181804`；`lna=U1 MAX2659`；`matching=C5 470pF,L1 6.8nH`
- 证据：图 ca8220583ff6 / 第 1 页 / C2-D4 M2 GP-02 的 G15/G13 与 U1 MAX2659-L1-C5-J1 GNSS 射频链

### SX1262 数字接口

SX1262 使用 SX_NRST、SX_BUSY、SX_NSS、SPI_MISO、SPI_MOSI、SPI_CLK 和 LORA_IRQ/DIO1；通过 Cap 14 Pin 接口分别映射到 G3、G6、G5、G39、G14、G40、G4。

- 参数与网络：`reset=G3`；`busy=G6`；`chip_select=G5`；`miso=G39`；`mosi=G14`；`sck=G40`；`irq_dio1=G4`
- 证据：图 77b258457736 / 第 1 页 / A1-A3 U1 SX1262 的 NRST/BUSY/NSS/MISO/MOSI/SCK/DIO1 网络; 图 ca8220583ff6 / 第 1 页 / D3-D4 P1 对应 G3/G6/G5/G39/G14/G40/G4 映射

### SX1262 射频前端

SX1262 的 SX_RFO/SX_RFIP/SX_RFIN 经 U3 0900FM15K0039 形成 SX_SRFI/SX_SRFO，随后进入 U2 FM8625H；FM8625H CTRL 连接 SX_DIO2，RFC 经末级匹配连接 J1 IPEX4。

- 参数与网络：`transceiver=SX1262`；`rf_switch=0900FM15K0039`；`rf_frontend=FM8625H`；`control=SX_DIO2`；`antenna_connector=J1 IPEX4`
- 证据：图 77b258457736 / 第 1 页 / A2-A8 U1 SX1262、U3 0900FM15K0039、U2 FM8625H 与 J1 IPEX4 射频链

## 模拟电路

### 电池电压监测

电池开关链后的 BAT 节点通过 R8/R12 两只 100 kΩ 分压并由 C10 100 nF 滤波后连接 G10。

- 参数与网络：`adc_gpio=G10`；`upper_resistor=R8 100k`；`lower_resistor=R12 100k`；`filter_capacitor=C10 100nF`
- 证据：图 b721dfa2ce19 / 第 1 页 / B1-B2 BAT、Q2/Q3、R8/R12、C10 与 G10 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Cardputer-Adv 主控制器 | `module=Stamp-S3A`；`soc=ESP32-S3FN8`；`mainboard_reference=M1`；`module_reference=U1` |
| 电源 | Cardputer-Adv 充电链 | `charger=TP4057`；`input=+5VIN via R1 0.8R`；`battery_node=VBAT_IN`；`program_resistor=R5 3.3k`；`power_path=Q1 LP3218DT1G to VBAT_OUT` |
| 电源 | Cardputer-Adv 5 V 与 3.3 V 电源 | `boost_converter=U2 SY7088`；`boost_inductor=L1 1.5uH`；`boost_output=+5VOUT`；`buck_converter=U4 SY8089`；`buck_inductor=L2 4.7uH`；`buck_output=+3.3V` |
| 模拟电路 | 电池电压监测 | `adc_gpio=G10`；`upper_resistor=R8 100k`；`lower_resistor=R12 100k`；`filter_capacitor=C10 100nF` |
| GPIO 与控制信号 | EN、Boot 与红外发射 | `reset_button=BTN1/EN`；`boot_button=BTN2/G0`；`pullups=R15=10k,R18=10k`；`esd=D4,D5 PESDNC2FD3V3B`；`ir_gpio=G44`；`ir_resistor=R14 22R` |
| 存储 | Cardputer-Adv microSD | `chip_select=G12`；`mosi=G14`；`clock=G40`；`miso=G39`；`series_resistors=R19-R22 33R`；`protection=D9-D12 PESDNC2FD3V3B` |
| 接口 | Cardputer-Adv HY2.0 I2C 接口 | `pinout=1:SCL/G1,2:SDA/G0,3:VCC,4:GND`；`pullups=R3=10k,R10=10k`；`power_selector=SW2:+5VOUT/+5VIN` |
| 接口 | Cardputer-Adv EXT 2.54-14P | `reference=P3`；`pinout=1:RESET/G3,2:INT/G4,3:BUSY/G6,4:SCK/G40,5:MOSI/G14,6:MISO/G39,7:CS/G5,8:GPS-TX/G15,9:GPS-RX/G13,10:SCL/G9,11:SDA/G8,12:5VOUT,13:GND,14:5VIN` |
| 总线 | 56 键矩阵键盘 | `controller=TCA8418RTWR`；`matrix=7x8`；`keys=56`；`sda=G8`；`scl=G9`；`interrupt=G11`；`pullups=R35-R37 3.3k` |
| 总线地址 | 键盘控制器 I2C 地址 | `part_number=TCA8418RTWR`；`i2c_address=0x34` |
| 传感器 | BMI270 IMU | `part_number=BMI270`；`sda=G8`；`scl=G9`；`sdo_pullup=R43 3.3k`；`i2c_address=0x69` |
| 音频 | ES8311 音频接口 | `codec=ES8311`；`i2c_scl=G9`；`i2c_sda=G8`；`i2s_sclk=G41`；`i2s_asdout=G46`；`i2s_lrck=G43`；`i2s_dsdin=G42`；`microphone_inputs=MIC_P,MIC_N` |
| 音频 | 扬声器与耳机输出 | `amplifier=NS4150B`；`speaker_connector=J4`；`speaker_outputs=VOP,VON via FB1,FB2`；`headphone_connector=PJ-342`；`detect=HP_DET`；`enable=AMP_EN` |
| 接口 | Stamp-S3A LCD 接口 | `reset=GPIO33`；`data_command=GPIO34`；`mosi=GPIO35`；`sck=GPIO36`；`chip_select=GPIO37`；`backlight_enable=GPIO38`；`backlight_power=U2 AW35122FDR/BL_3V3` |
| GPIO 与控制信号 | Stamp-S3A RGB LED 与用户键 | `rgb_led=U3 WS2812`；`rgb_data=GPIO21/SK_DIN`；`user_button=S1/GPIO0`；`button_pullup=R4 10k` |
| 电源 | Stamp-S3A 模组电源 | `converter=U4 JW5712`；`input=VIN_5V`；`output=VDD_3V3`；`inductor=L4 MWTC201608S2R2`；`output_current_a=0-0.6` |
| 接口 | Stamp-S3A USB Type-C | `connector=J2 USB-TYPEC`；`usb_d_minus=GPIO19`；`usb_d_plus=GPIO20`；`cc_resistors=R1=5.1k,R2=5.1k`；`fuse=F1 6V/1A/PPTC` |
| 接口 | Cap LoRa-1262 14 Pin 接口 | `reference=P1`；`pinout=1:GPS-TX/G15,2:GPS-RX/G13,3:SCL/G1,4:SDA/G0,5:5VOUT,6:GND,7:5VIN,8:RST/G3,9:IRQ/G4,10:BUSY/G6,11:SCK/G40,12:MOSI/G14,13:MISO/G39,14:NSS/G5` |
| 电源 | Cap LoRa-1262 3.3 V 电源 | `converter=U3 JW5712`；`input=+5V/+5VOUT`；`output=VDD_3V3`；`inductor=L2 WPN201610U2R2MT`；`output_current_a=0-0.6` |
| 总线 | Cap PI4IOE5V6408 控制 | `part_number=PI4IOE5V6408ZTAEX`；`scl=SCL`；`sda=SDA`；`optional_pullups=R5/R6 10k NC`；`p0=BYPASS`；`p1=SHUT_DOWN` |
| 射频 | Cap GNSS 接口与射频链 | `gnss_module=M2 GP-02`；`uart_tx=G15`；`uart_rx=G13`；`antenna=J1 ANT181804`；`lna=U1 MAX2659`；`matching=C5 470pF,L1 6.8nH` |
| 接口 | Cap LoRa-1262 Grove 接口 | `pinout=SCL,SDA,5V,GND`；`supply=+5VOUT` |
| 射频 | SX1262 数字接口 | `reset=G3`；`busy=G6`；`chip_select=G5`；`miso=G39`；`mosi=G14`；`sck=G40`；`irq_dio1=G4` |
| 时钟 | SX1262 参考时钟 | `oscillator=X1 X1G0041310042`；`frequency_mhz=32`；`output_network=R3 220R,C6 10nF`；`power_control=SX_DIO3 via FB1` |
| 射频 | SX1262 射频前端 | `transceiver=SX1262`；`rf_switch=0900FM15K0039`；`rf_frontend=FM8625H`；`control=SX_DIO2`；`antenna_connector=J1 IPEX4` |
| 射频 | LoRa 天线末级匹配 | `shunt_l4=NC`；`series_position=0R/TBD`；`shunt_c3=TBD`；`connector=J1 IPEX4` |

## 待确认事项

- `rf.lora_output_matching`：FM8625H RFC 至 J1 IPEX4 的末级网络包含 L4=NC、一个标注 0R/TBD 的串联匹配位置和 C3=TBD 的对地位置，实际装配值未在图面确定。（证据：图 77b258457736 / 第 1 页 / A6-A8 FM8625H RFC 至 J1 IPEX4 之间的 L4 NC、0R/TBD 与 C3 TBD 匹配网络）
- `review.lora_output_matching`：量产版 Stamp LoRa-1262 Mini 的 FM8625H 至 IPEX4 末级匹配网络中，0R/TBD 串联位置和 C3 的实际装配值及 DNP 状态是什么？；原因：图面仅给出 L4=NC、串联位置 0R/TBD、C3=TBD，无法从现有页面确认最终射频匹配 BOM。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `b721dfa2ce1979194d19c425fe1a2ac842b7e0b1846722fde165fcf0dca7a3d9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_01.png` |
| 2 | 1 | `cf469cc225c427da5cc46f197ddbd728e3c5b1ebad65a0d1749150d89757bacf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_02.png` |
| 3 | 1 | `3162cda432ca2cb9e6a3f732d063942dcdbb152f79a64f1f9eaae487e1cd009b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_03.png` |
| 4 | 1 | `6f970d99f03603ac21277e9305132a80d16424d6656ab3cf62a1f743e79a7923` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_04.png` |
| 5 | 1 | `1156e645de35fe68e6458e9131657c8f02045bbcd14f97ab190bb1486ee7a1c5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3_page_01.png` |
| 6 | 1 | `ca8220583ff646b8466fd2161672edd74d905b6693d3850f4ceeef666333b39c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1208/U214-sche-Cap-LoRa1262_SCH_1.1_20251029_2025_11_07_22_53_19_page_02.png` |
| 7 | 1 | `77b258457736a07175c6c3b8c8706d047d959da1093bfeb48e9aadaade91bc30` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1208/NEW-1262-SCH_A1-Lora_2025_08_27_10_58_52_page_01.png` |

---

源文档：`zh_CN/core/Cardputer_Mesh_Kit.md`

源文档 SHA-256：`785843898ccaafa174eed5ca7b141d838c71004bfd1e8ccf3767fd04f5a2d6b6`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
