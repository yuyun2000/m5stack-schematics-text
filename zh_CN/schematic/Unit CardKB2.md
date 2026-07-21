# Unit CardKB2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit CardKB2 |
| SKU | U215 |
| 产品 ID | `unit-cardkb2-f04738bf1335` |
| 源文档 | `zh_CN/unit/Unit_CardKB2.md` |

## 概述

Unit CardKB2 以图面标注 U5 ESP32-C6IHF4 为控制核心，使用 4 条 ROW 与 11 条 COM 网络扫描 S3-S44 共 42 个按键，每个键带独立二极管，列线另有 ESD5311 防护。USB Type-C 的 CC 下拉、USB 数据共模滤波和 ESD 后直接连接主控原生 USB；电源经 U2 AW32901FCR、U3 CH213K、D43 与 U4 TPAP7343D-33FS4 形成 VUSB_5V、VBUS_5V 和 VSYS_3V3。板上还包含 40MHz 晶振、2.4GHz 天线匹配、复位与 Boot 按键、XL-1615RGBC-RF RGB LED，以及引出 G25/G26 和 5V 的 JP1 四针接口。图面与概览块的保护器件型号、主控字符存在差异，I2C 地址、通信固件、无线能力、Flash/频率、功耗和机械参数需进一步确认。

## 检索关键词

`Unit CardKB2`、`U215`、`ESP32-C6IHF4`、`ESP32-C61HF4`、`AW32901FCR`、`AW32902`、`CH213K`、`RB162VAM-20TR`、`TPAP7343D-33FS4`、`USB_C_16P_Horizontal`、`SDMM0806H-2-900T`、`ESD5311`、`XL-1615RGBC-RF`、`40MHz_10PPM_10PF`、`VSYS_3V3`、`VUSB_5V`、`VBUS_5V`、`USB_D_P`、`USB_D_N`、`ROW0_G0`、`ROW1_G1`、`ROW2_G2`、`ROW3_G3`、`COM0_G4`、`COM5_G29`、`COM10_G24`、`G9_BOOT`、`G27_RGB_R`、`G28_RGB_G`、`JP1`、`G25`、`G26`、`HY2.0-4P`、`I2C`、`UART`、`BLE HID`、`ESP-NOW`、`42-key matrix`、`S3-S44`、`D1-D42`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U5 | ESP32-C6IHF4 | 键盘矩阵、USB、RGB、Grove 和 2.4GHz 射频的主控制器 | 图 078a523f0f1c / 第 1 页 / 页面下中 U5 ESP32-C6IHF4 pins1-41 |
| J1 | USB_C_16P_Horizontal | USB 供电、原生 USB 数据与 CC 配置连接器 | 图 078a523f0f1c / 第 1 页 / 页面左上 J1 USB_C_16P_Horizontal |
| FT1 | SDMM0806H-2-900T | USB D+/D- 双线共模滤波器 | 图 078a523f0f1c / 第 1 页 / 页面左上 FT1 SDMM0806H-2-900T，USBC_P/USBC_N 到 USB_D_P/USB_D_N |
| DR1,DR2 | ESD5311 | USB Type-C 数据线静电保护 | 图 078a523f0f1c / 第 1 页 / 页面左上 USBC_P/USBC_N 上的 DR1/DR2 ESD5311 |
| U2 | AW32901FCR | USB_IN 到 VUSB_5V 的输入保护器件 | 图 078a523f0f1c / 第 1 页 / 页面上中 U2 AW32901FCR，IN/OUT/OVLO/EN#/ACOK# |
| U3 | CH213K | VUSB_5V 到 VBUS_5V 电源路径中的三脚串联器件 | 图 078a523f0f1c / 第 1 页 / 页面上中 U3 CH213K pins1-3，VUSB_5V/VBUS_5V |
| D43 | RB162VAM-20TR | VBUS_5V 到 U4 VIN 的串联二极管 | 图 078a523f0f1c / 第 1 页 / 页面右上 D43 RB162VAM-20TR |
| U4 | TPAP7343D-33FS4 | VBUS_5V 路径到 VSYS_3V3 的常开 LDO | 图 078a523f0f1c / 第 1 页 / 页面右上 U4 TPAP7343D-33FS4，VIN/EN/OUT/VSYS_3V3 |
| ANT1 | 未标注 | ESP32 ANT_2G 的 2.4GHz 天线端 | 图 078a523f0f1c / 第 1 页 / 页面左下 ANT1、L4、C14/C15 与 U5 ANT_2G |
| X1 | 40MHz_10PPM_10PF | ESP32 XTAL_P/XTAL_N 的 40MHz 晶振 | 图 078a523f0f1c / 第 1 页 / 页面右中 X1 40MHz_10PPM_10PF、C6/C11 |
| S1,S2 | 未标注 | ESP_EN 复位与 G9_BOOT 启动模式按键 | 图 2acbf26b875b / 第 1 页 / 页面左上 S1 ESP_EN 与 S2 G9_BOOT |
| RGB1 | XL-1615RGBC-RF | 由 G27/G28/G9 控制的共阳三色状态 LED | 图 2acbf26b875b / 第 1 页 / 页面上中 RGB1 XL-1615RGBC-RF、R5/R6/R7 |
| JP1 | Header 4 | GND、VBUS_5V、G26、G25 的四针 Grove 接口 | 图 2acbf26b875b / 第 1 页 / 页面右上 JP1 pins1-4 与 G25/G26/VBUS_5V/GND |
| S3-S44 | 未标注 | ROW0-ROW3 与 COM0-COM10 组成的 42 个键盘开关 | 图 2acbf26b875b / 第 1 页 / 页面 B-D 区键盘矩阵 S3-S44 |
| D1-D42 | 未标注 | 42 个按键各自串联的矩阵隔离二极管 | 图 2acbf26b875b / 第 1 页 / 页面 B-D 区每个 S3-S44 上方对应 D1-D42 |
| DR7-DR17 | ESD5311 | COM0-COM10 十一条键盘列线的静电保护 | 图 2acbf26b875b / 第 1 页 / 页面底部 COM0-COM10 下方 DR7-DR17 ESD5311 |

## 系统结构

### Unit CardKB2 硬件架构

U5 控制 42 键矩阵、原生 USB、RGB1、JP1 G25/G26 和 ANT1 射频网络；J1 USB-C 输入经 U2/U3/D43/U4 形成 VUSB_5V、VBUS_5V 与 VSYS_3V3，S1/S2 分别连接 ESP_EN 与 G9_BOOT。

- 参数与网络：`controller=U5 ESP32-C6IHF4`；`keyboard=S3-S44 42-key matrix`；`usb=J1 native USB`；`power=U2 AW32901FCR,U3 CH213K,D43,U4 TPAP7343D-33FS4`；`rf=ANT1`；`interface=JP1 G25/G26`
- 证据：图 92a65e41156c / 第 1 页 / 页面 A-D 区系统框图、主控引脚和键盘布局; 图 078a523f0f1c / 第 1 页 / 页面 A-D 区 USB、电源、主控、晶振和天线; 图 2acbf26b875b / 第 1 页 / 页面 A-D 区按键、RGB、Grove 与矩阵

## 核心器件

### U5 ESP32-C6IHF4 主控引脚域

U5 图符标为 ESP32-C6IHF4，使用 GPIO0-GPIO29 中的多组引脚连接 4 条 ROW、11 条 COM、G25/G26、RGB 和 USB；ANT_2G、XTAL_P/XTAL_N、CHIP_PU、VDD_SPI 与电源地脚也在图中展开。

- 参数与网络：`reference=U5`；`schematic_label=ESP32-C6IHF4`；`gpio_range_used=GPIO0-GPIO29`；`rf_pin=ANT_2G`；`crystal=XTAL_P,XTAL_N`；`enable=CHIP_PU / ESP_EN`；`usb=GPIO13 USB_D+,GPIO12 USB_D-`
- 证据：图 078a523f0f1c / 第 1 页 / 页面下中 U5 pins1-41

## 电源

### USB_IN 到 VUSB_5V 输入保护

USB_IN 连接 U2 AW32901FCR 三个 IN 脚，U2 三个 OUT 脚并为 VUSB_5V；EN# 经 R9 0R 接 GND，OVLO 节点使用 R8 NC 与 R9，C5 10uF 位于 USB_IN 侧，C12 22uF 位于 VUSB_5V 侧。

- 参数与网络：`protection=U2 AW32901FCR`；`input=USB_IN`；`output=VUSB_5V`；`enable=EN# via R9 0R to GND`；`ovlo_upper=R8 NC`；`input_cap=C5 10uF/25V`；`output_cap=C12 22uF/10V`
- 证据：图 078a523f0f1c / 第 1 页 / 页面上中 U2、R8/R9、C5/C12

### VUSB_5V 到 VBUS_5V 电源路径

VUSB_5V 进入 U3 CH213K IN+ pin3，U3 VOUT pin2 输出 VBUS_5V；VBUS_5V 再经 D43 RB162VAM-20TR 接 U4 VIN，D43 后配置 C1/C22 各 22uF。

- 参数与网络：`input=VUSB_5V`；`series_device=U3 CH213K`；`intermediate=VBUS_5V`；`diode=D43 RB162VAM-20TR`；`destination=U4 VIN`；`caps=C1/C22 22uF/10V`
- 证据：图 078a523f0f1c / 第 1 页 / 页面上中至右 U3、VBUS_5V、D43、C1/C22、U4

### U4 VSYS_3V3 LDO

U4 TPAP7343D-33FS4 的 VIN 与 EN 都接 D43 后节点，OUT pin1 输出 VSYS_3V3，C2 10uF 为输出电容；概览页把该 LDO 标为 Always On。

- 参数与网络：`regulator=U4 TPAP7343D-33FS4`；`input=D43 output`；`enable=tied to VIN`；`output=VSYS_3V3`；`output_cap=C2 10uF/10V`；`mode=Always On`
- 证据：图 078a523f0f1c / 第 1 页 / 页面右上 U4、C2 与 VSYS_3V3; 图 92a65e41156c / 第 1 页 / 页面 A3 Power Network 中 TPAP7343D LDO Always On

## 接口

### J1 USB Type-C 连接

J1 的 A4/B9 与 B4/A9 VBUS 脚并入 USB_IN，A6/B6 并为 USBC_P，A7/B7 并为 USBC_N；CC1/CC2 分别经 R1/R2 5.1K 接 GND，GND 与外壳脚接地。

- 参数与网络：`connector=J1 USB_C_16P_Horizontal`；`vbus=A4/B9,B4/A9 -> USB_IN`；`dp=A6/B6 -> USBC_P`；`dm=A7/B7 -> USBC_N`；`cc1=R1 5.1K to GND`；`cc2=R2 5.1K to GND`
- 证据：图 078a523f0f1c / 第 1 页 / 页面左上 J1、R1/R2 与 USB_IN/USBC_P/USBC_N

### ESP32 原生 USB 引脚

USB_D_P 接 U5 GPIO13(USB_D+) pin29，USB_D_N 接 U5 GPIO12(USB_D-) pin28；图中没有独立 USB-UART 桥。

- 参数与网络：`usb_dp=USB_D_P -> U5 GPIO13 pin29`；`usb_dn=USB_D_N -> U5 GPIO12 pin28`；`usb_uart_bridge_shown=false`
- 证据：图 078a523f0f1c / 第 1 页 / 页面下右 U5 pins28/29 与 USB_D_N/USB_D_P

### 42 键矩阵拓扑

S3-S44 共 42 个开关分布在 ROW0_G0、ROW1_G1、ROW2_G2、ROW3_G3 与 COM0_G4 至 COM10_G24 之间；每个开关支路串联一颗对应的 D1-D42。

- 参数与网络：`switches=S3-S44`；`switch_count=42`；`rows=ROW0_G0,ROW1_G1,ROW2_G2,ROW3_G3`；`columns=COM0_G4..COM10_G24`；`diodes=D1-D42 one per switch`
- 证据：图 2acbf26b875b / 第 1 页 / 页面 B-D 区 S3-S44、D1-D42、ROW0-ROW3、COM0-COM10

### XL-1615RGBC-RF RGB LED

RGB1 共阳端接 VSYS_3V3，红、绿、蓝三路分别经 R5/R6/R7 1K 接 G27_RGB_R、G28_RGB_G、G9_BOOT；蓝色通道与 Boot 按键共用 GPIO9 网络。

- 参数与网络：`led=RGB1 XL-1615RGBC-RF`；`common=VSYS_3V3`；`red=R5 1K -> GPIO27`；`green=R6 1K -> GPIO28`；`blue=R7 1K -> GPIO9/G9_BOOT`；`shared_boot_gpio=true`
- 证据：图 2acbf26b875b / 第 1 页 / 页面上中 RGB1、R5/R6/R7 与 G27/G28/G9

### JP1 四针接口

JP1 pin1 接 GND，pin2 接 VBUS_5V，pin3 接 G26，pin4 接 G25；VBUS_5V 侧配置 C13/C21 各 22uF/10V。

- 参数与网络：`connector=JP1 Header 4`；`pin1=GND`；`pin2=VBUS_5V`；`pin3=G26`；`pin4=G25`；`bulk_caps=C13/C21 22uF/10V`
- 证据：图 2acbf26b875b / 第 1 页 / 页面右上 JP1、C13/C21、G25/G26/VBUS_5V/GND

## GPIO 与控制信号

### 键盘行 GPIO 映射

ROW0_G0、ROW1_G1、ROW2_G2、ROW3_G3 分别连接 U5 GPIO0、GPIO1、GPIO2、GPIO3。

- 参数与网络：`row0=GPIO0`；`row1=GPIO1`；`row2=GPIO2`；`row3=GPIO3`
- 证据：图 078a523f0f1c / 第 1 页 / 页面下中 U5 pins6-9 ROW0_G0 至 ROW3_G3; 图 2acbf26b875b / 第 1 页 / 页面左侧 ROW0_G0 至 ROW3_G3

### 键盘列 GPIO 映射

COM0-COM10 依次映射 GPIO4、GPIO5、GPIO6、GPIO7、GPIO8、GPIO29、GPIO10、GPIO11、GPIO22、GPIO23、GPIO24。

- 参数与网络：`com0=GPIO4`；`com1=GPIO5`；`com2=GPIO6`；`com3=GPIO7`；`com4=GPIO8`；`com5=GPIO29`；`com6=GPIO10`；`com7=GPIO11`；`com8=GPIO22`；`com9=GPIO23`；`com10=GPIO24`
- 证据：图 078a523f0f1c / 第 1 页 / 页面下中 U5 COM0_G4 至 COM10_G24 网络; 图 2acbf26b875b / 第 1 页 / 页面底部 COM0_G4 至 COM10_G24

## 时钟

### 40MHz 主晶振

X1 标为 40MHz_10PPM_10PF，连接 U5 XTAL_P/XTAL_N；XTAL_P 侧 C6 为 15pF/50V，XTAL_N 侧 C11 为 12pF/50V。

- 参数与网络：`crystal=X1 40MHz_10PPM_10PF`；`pins=XTAL_P,XTAL_N`；`load_caps=C6 15pF/50V,C11 12pF/50V`
- 证据：图 078a523f0f1c / 第 1 页 / 页面右中 X1、C6/C11 与 XTAL_P/XTAL_N

## 复位

### ESP_EN 复位按键

ESP_EN 由 R3 10K 上拉到 VSYS_3V3，S1 按下时拉到 GND；C19 1uF/25V 与 DR3 ESD5311 均从 ESP_EN 接 GND。

- 参数与网络：`net=ESP_EN`；`pullup=R3 10K to VSYS_3V3`；`button=S1 to GND`；`capacitor=C19 1uF/25V`；`esd=DR3 ESD5311`
- 证据：图 2acbf26b875b / 第 1 页 / 页面左上 ESP_EN、R3、C19、DR3、S1

## 保护电路

### USB 数据共模滤波与 ESD

USBC_P/USBC_N 各有 DR1/DR2 ESD5311 对地保护，并通过 FT1 SDMM0806H-2-900T 转为 USB_D_P/USB_D_N。

- 参数与网络：`connector_side=USBC_P,USBC_N`；`esd=DR1/DR2 ESD5311`；`common_mode_filter=FT1 SDMM0806H-2-900T`；`mcu_side=USB_D_P,USB_D_N`
- 证据：图 078a523f0f1c / 第 1 页 / 页面左上 DR1/DR2、FT1 与 USB 数据网络

### 键盘列线 ESD 防护

COM0-COM10 每条列线分别配置 DR7-DR17 ESD5311 到 GND。

- 参数与网络：`protected_nets=COM0-COM10`；`devices=DR7-DR17 ESD5311`；`reference=GND`
- 证据：图 2acbf26b875b / 第 1 页 / 页面 D1-D4 底部 DR7-DR17

### JP1 电源与信号 ESD 防护

JP1 的 VBUS_5V、G26、G25 分别配置 DR18、DR5、DR6 ESD5311 到 GND。

- 参数与网络：`vbus=DR18 ESD5311`；`g26=DR5 ESD5311`；`g25=DR6 ESD5311`；`reference=GND`
- 证据：图 2acbf26b875b / 第 1 页 / 页面右上 JP1 左侧 DR18/DR5/DR6

## 射频

### ANT1 到 ANT_2G 匹配网络

ANT1 pin1 经 C14 2.7pF 对地、L4 2.2nH 串联和 C15 2.7pF 对地连接 U5 ANT_2G；ANT1 pin2 接 GND，图中在 L4 两端标出 Z=50R。

- 参数与网络：`antenna=ANT1`；`mcu_pin=U5 ANT_2G`；`series=L4 2.2nH`；`shunt_caps=C14 2.7pF,C15 2.7pF`；`impedance_marks=Z=50R`
- 证据：图 078a523f0f1c / 第 1 页 / 页面左下 ANT1、C14/L4/C15 与 ANT_2G

## 调试与烧录

### G9_BOOT 启动按键

G9_BOOT 由 R4 10K 上拉到 VSYS_3V3，S2 按下时拉到 GND；C20 10pF/25V 与 DR4 ESD5311 均从 G9_BOOT 接 GND。

- 参数与网络：`net=G9_BOOT`；`gpio=9`；`pullup=R4 10K to VSYS_3V3`；`button=S2 to GND`；`capacitor=C20 10pF/25V`；`esd=DR4 ESD5311`
- 证据：图 2acbf26b875b / 第 1 页 / 页面左上 G9_BOOT、R4、C20、DR4、S2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit CardKB2 硬件架构 | `controller=U5 ESP32-C6IHF4`；`keyboard=S3-S44 42-key matrix`；`usb=J1 native USB`；`power=U2 AW32901FCR,U3 CH213K,D43,U4 TPAP7343D-33FS4`；`rf=ANT1`；`interface=JP1 G25/G26` |
| 核心器件 | U5 ESP32-C6IHF4 主控引脚域 | `reference=U5`；`schematic_label=ESP32-C6IHF4`；`gpio_range_used=GPIO0-GPIO29`；`rf_pin=ANT_2G`；`crystal=XTAL_P,XTAL_N`；`enable=CHIP_PU / ESP_EN`；`usb=GPIO13 USB_D+,GPIO12 USB_D-` |
| 接口 | J1 USB Type-C 连接 | `connector=J1 USB_C_16P_Horizontal`；`vbus=A4/B9,B4/A9 -> USB_IN`；`dp=A6/B6 -> USBC_P`；`dm=A7/B7 -> USBC_N`；`cc1=R1 5.1K to GND`；`cc2=R2 5.1K to GND` |
| 保护电路 | USB 数据共模滤波与 ESD | `connector_side=USBC_P,USBC_N`；`esd=DR1/DR2 ESD5311`；`common_mode_filter=FT1 SDMM0806H-2-900T`；`mcu_side=USB_D_P,USB_D_N` |
| 接口 | ESP32 原生 USB 引脚 | `usb_dp=USB_D_P -> U5 GPIO13 pin29`；`usb_dn=USB_D_N -> U5 GPIO12 pin28`；`usb_uart_bridge_shown=false` |
| 电源 | USB_IN 到 VUSB_5V 输入保护 | `protection=U2 AW32901FCR`；`input=USB_IN`；`output=VUSB_5V`；`enable=EN# via R9 0R to GND`；`ovlo_upper=R8 NC`；`input_cap=C5 10uF/25V`；`output_cap=C12 22uF/10V` |
| 电源 | VUSB_5V 到 VBUS_5V 电源路径 | `input=VUSB_5V`；`series_device=U3 CH213K`；`intermediate=VBUS_5V`；`diode=D43 RB162VAM-20TR`；`destination=U4 VIN`；`caps=C1/C22 22uF/10V` |
| 电源 | U4 VSYS_3V3 LDO | `regulator=U4 TPAP7343D-33FS4`；`input=D43 output`；`enable=tied to VIN`；`output=VSYS_3V3`；`output_cap=C2 10uF/10V`；`mode=Always On` |
| 射频 | ANT1 到 ANT_2G 匹配网络 | `antenna=ANT1`；`mcu_pin=U5 ANT_2G`；`series=L4 2.2nH`；`shunt_caps=C14 2.7pF,C15 2.7pF`；`impedance_marks=Z=50R` |
| 时钟 | 40MHz 主晶振 | `crystal=X1 40MHz_10PPM_10PF`；`pins=XTAL_P,XTAL_N`；`load_caps=C6 15pF/50V,C11 12pF/50V` |
| 接口 | 42 键矩阵拓扑 | `switches=S3-S44`；`switch_count=42`；`rows=ROW0_G0,ROW1_G1,ROW2_G2,ROW3_G3`；`columns=COM0_G4..COM10_G24`；`diodes=D1-D42 one per switch` |
| GPIO 与控制信号 | 键盘行 GPIO 映射 | `row0=GPIO0`；`row1=GPIO1`；`row2=GPIO2`；`row3=GPIO3` |
| GPIO 与控制信号 | 键盘列 GPIO 映射 | `com0=GPIO4`；`com1=GPIO5`；`com2=GPIO6`；`com3=GPIO7`；`com4=GPIO8`；`com5=GPIO29`；`com6=GPIO10`；`com7=GPIO11`；`com8=GPIO22`；`com9=GPIO23`；`com10=GPIO24` |
| 保护电路 | 键盘列线 ESD 防护 | `protected_nets=COM0-COM10`；`devices=DR7-DR17 ESD5311`；`reference=GND` |
| 复位 | ESP_EN 复位按键 | `net=ESP_EN`；`pullup=R3 10K to VSYS_3V3`；`button=S1 to GND`；`capacitor=C19 1uF/25V`；`esd=DR3 ESD5311` |
| 调试与烧录 | G9_BOOT 启动按键 | `net=G9_BOOT`；`gpio=9`；`pullup=R4 10K to VSYS_3V3`；`button=S2 to GND`；`capacitor=C20 10pF/25V`；`esd=DR4 ESD5311` |
| 接口 | XL-1615RGBC-RF RGB LED | `led=RGB1 XL-1615RGBC-RF`；`common=VSYS_3V3`；`red=R5 1K -> GPIO27`；`green=R6 1K -> GPIO28`；`blue=R7 1K -> GPIO9/G9_BOOT`；`shared_boot_gpio=true` |
| 接口 | JP1 四针接口 | `connector=JP1 Header 4`；`pin1=GND`；`pin2=VBUS_5V`；`pin3=G26`；`pin4=G25`；`bulk_caps=C13/C21 22uF/10V` |
| 保护电路 | JP1 电源与信号 ESD 防护 | `vbus=DR18 ESD5311`；`g26=DR5 ESD5311`；`g25=DR6 ESD5311`；`reference=GND` |
| 核心器件 | 主控准确型号字符 | `detailed_schematic=ESP32-C6IHF4`；`overview=ESP32-C61`；`source_document=ESP32-C61HF4`；`confirmed_part_number=null` |
| 保护电路 | USB 输入保护器件型号差异 | `detailed_schematic=U2 AW32901FCR`；`overview_block=AW32902 PROTECTION`；`production_part=null`；`ovp_threshold=null` |
| 总线 | JP1 的 I2C 与 UART 固件复用 | `documented_g26=SDA / UART_RX`；`documented_g25=SCL / UART_TX`；`i2c_address=null`；`uart_baud=null`；`logic_level=VSYS_3V3 domain not explicitly annotated at JP1` |
| 射频 | Wi-Fi 6、BLE HID 与 ESP-NOW | `documented_wifi=2.4GHz Wi-Fi 6`；`documented_ble=BLE HID`；`documented_esp_now=true`；`schematic_rf_path=ANT1 -> ANT_2G`；`tx_power=null`；`certification=null` |
| 内存与 Flash | 4MB Flash 与 120MHz 主频 | `documented_cpu=RISC-V 32-bit single-core`；`documented_frequency_mhz=120`；`documented_flash_mb=4`；`flash_component_shown=false`；`schematic_capacity=null` |
| 系统结构 | 键盘通信模式与指示行为 | `documented_modes=I2C,UART,ESP-NOW,BLE HID`；`documented_default=I2C`；`mode_keys=Fn+Sym+1..4`；`state_persistence=documented`；`firmware_version=null` |
| 调试与烧录 | USB 下载与默认日志参数 | `documented_usb_use=power and programming`；`documented_log=115200bps 8N1`；`hardware_usb=U5 GPIO13/GPIO12 native USB`；`download_protocol=null` |
| 电源 | Grove 供电待机功耗 | `documented_supply_v=5`；`documented_current_ma=19.31`；`documented_condition=Grove power standby`；`test_point=null`；`firmware_state=null` |
| 系统结构 | 产品机械尺寸与重量 | `documented_size_mm=84.7x54.3x1.0`；`documented_weight_g=22.4`；`mechanical_drawing_in_assets=false` |
| 系统结构 | 三张页面与 U215 量产版本的对应关系 | `product=Unit CardKB2`；`sku=U215`；`schematic_revision=null`；`schematic_date=null`；`title_block_product=null` |

## 待确认事项

- `component.controller-label`：详细图 U5 标签显示 ESP32-C6IHF4，概览/引脚页与源文档使用 ESP32-C61 或 ESP32-C61HF4；字母 I 与数字 1 的准确料号字符不能由当前图片唯一确定。（证据：图 078a523f0f1c / 第 1 页 / 页面下中 U5 型号标签; 图 92a65e41156c / 第 1 页 / 页面 A3-A4 系统框图 ESP32-C61 与左上引脚图标签）
- `protection.input-device-label`：详细电路 U2 标为 AW32901FCR，概览页 Power Network 方框标为 AW32902 PROTECTION；量产 BOM 采用的准确型号及保护阈值不能由两页唯一确定。（证据：图 078a523f0f1c / 第 1 页 / 页面上中 U2 AW32901FCR; 图 92a65e41156c / 第 1 页 / 页面 A2 Power Network 的 AW32902 PROTECTION 方框）
- `bus.documented-i2c-uart`：源文档把 JP1 G26 定义为 SDA/UART_RX、G25 定义为 SCL/UART_TX，并称固件支持 I2C 与 UART 模式；原理图只标 G25/G26，没有总线方向、I2C 地址、UART 波特率或电平时序标注。（证据：图 2acbf26b875b / 第 1 页 / 页面右上 JP1 仅标 G25/G26/VBUS_5V/GND）
- `rf.documented-wireless-modes`：源文档称设备支持 2.4GHz Wi-Fi 6、BLE HID 与 ESP-NOW；原理图确认 ANT1 到 ANT_2G 射频路径，但未标无线协议版本、发射功率、接收灵敏度、认证参数或固件模式实现。（证据：图 078a523f0f1c / 第 1 页 / 页面左下 ANT1 匹配到 U5 ANT_2G，无协议参数）
- `memory.documented-flash-frequency`：源文档规格称主控为 RISC-V 32 位单核 120MHz 并带 4MB Flash；原理图未画独立 Flash 颗粒，也未直接标主频、Flash 容量或存储接口容量。（证据：图 078a523f0f1c / 第 1 页 / U5 与 VDD_SPI 区域，无独立 Flash 颗粒或容量文字）
- `system.documented-firmware-behavior`：源文档称预置固件支持 I2C、UART、ESP-NOW、BLE HID 四种模式，使用 Fn+Sym+数字键切换并保存，Aa/Fn 状态由 RGB 指示；原理图只确认按键矩阵与 RGB 硬件，不能确认固件版本、键值映射、状态保存或 LED 时序。（证据：图 92a65e41156c / 第 1 页 / 页面下半键帽布局，仅有硬件矩阵示意; 图 2acbf26b875b / 第 1 页 / 页面上中 RGB1 与 B-D 区 S3-S44，无固件状态机）
- `debug.documented-usb-log`：源文档称 USB Type-C 用于供电与程序下载，默认固件日志为 115200bps 8N1；原理图确认 J1 连接 U5 原生 USB，但不包含 Boot ROM、下载协议、虚拟串口配置或波特率参数。（证据：图 078a523f0f1c / 第 1 页 / J1 到 U5 GPIO13/GPIO12 的原生 USB 电路，无日志参数）
- `power.documented-standby`：源文档规格列 Grove 供电条件下待机功耗为 5V@19.31mA；原理图没有电流测试点、工作模式、固件版本、测量仪器或环境条件。（证据：图 2acbf26b875b / 第 1 页 / JP1 VBUS_5V 供电电路，无电流或待机状态标注）
- `system.documented-mechanical`：源文档规格列产品尺寸 84.7x54.3x1.0mm、产品重量 22.4g；当前三张电气原理图没有板框、固定孔尺寸、机械公差或质量信息。（证据：图 92a65e41156c / 第 1 页 / 系统与键盘布局页无尺寸标注）
- `system.asset-version-binding`：三张本地页面未显示完整标题栏、产品名、U215、Revision 或发布日期；资源 URL 使用 Unit_CardKB2 名称，但图面本身不能独立证明与当前量产版本完全一致。（证据：图 92a65e41156c / 第 1 页 / 页面边框无产品标题、SKU、Revision 或日期; 图 078a523f0f1c / 第 1 页 / 页面边框无标题栏版本信息; 图 2acbf26b875b / 第 1 页 / 页面边框无标题栏版本信息）
- `review.controller-label`：U215 量产 BOM 与芯片丝印中的主控准确型号是 ESP32-C6IHF4 还是 ESP32-C61HF4？；原因：详细图、概览块和源文档对 I/1 字符的写法不一致。
- `review.input-protection`：USB 输入保护实际采用 AW32901FCR 还是 AW32902，其过压、过流和反向保护阈值分别是多少？；原因：详细页与概览页型号不一致，页面也未给保护阈值。
- `review.i2c-uart`：默认 I2C 地址、寄存器协议、G25/G26 上拉配置，以及 UART 波特率、帧格式和方向是什么？；原因：原理图只给 GPIO 网络，源文档把协议细节指向外部用户手册。
- `review.wireless-modes`：U215 固件与射频认证实际支持哪些 Wi-Fi 6、BLE HID 和 ESP-NOW 参数及限制？；原因：图面只确认 2.4GHz 天线网络，未给协议与射频性能。
- `review.flash-frequency`：主控准确子型号、120MHz 工作频率与 4MB Flash 容量应由哪份 BOM 或 datasheet 版本确认？；原因：原理图未画存储颗粒或容量，也没有直接标主频。
- `review.firmware-behavior`：当前出厂固件版本的四种模式、键值表、Fn/Sym/Aa 组合、模式持久化和 RGB 指示时序是什么？；原因：这些行为不在电气原理图中。
- `review.usb-log`：USB 下载协议、虚拟串口实现及默认 115200bps 8N1 日志参数适用于哪个固件版本？；原因：原理图只有原生 USB 硬件路径，没有软件枚举和串口配置。
- `review.standby-power`：5V@19.31mA 待机功耗的固件状态、无线状态、测量点、仪器和环境条件是什么？；原因：图面没有测量条件，功耗数值无法由器件连接直接验证。
- `review.mechanical`：84.7x54.3x1.0mm 外形与 22.4g 重量由哪份当前机械图和量产配置确认？；原因：三张电气图不含机械尺寸、公差或质量信息。
- `review.asset-version-binding`：这三张页面对应 U215 的哪个 PCB Revision 和发布日期，是否与当前量产版本一致？；原因：本地页面没有产品标题、SKU、Revision 或日期。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `92a65e41156c664449ace7b3576f05903ed952d7808517711e74f30eff87294c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/Unit_CardKB2_page_02.png` |
| 2 | 1 | `078a523f0f1cf9a67a5818b30ebdb25eb525107efbf0bab0d1c39620cbb901ce` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/Unit_CardKB2_page_03.png` |
| 3 | 1 | `2acbf26b875b959dad9566ff59b3a6f5c99e784a0c6383679d5e70581e027ba6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1225/Unit_CardKB2_page_04.png` |

---

源文档：`zh_CN/unit/Unit_CardKB2.md`

源文档 SHA-256：`e0c6c2ce6f5c7473dfcfff8903ddbd54ea3ae1dc8bc3fbe1dbe803dc688b6ea8`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
