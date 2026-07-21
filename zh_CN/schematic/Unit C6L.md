# Unit C6L 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit C6L |
| SKU | U202 |
| 产品 ID | `unit-c6l-978d685b24b9` |
| 源文档 | `zh_CN/unit/Unit_C6L.md` |

## 概述

Unit C6L 由载板 U8 M5Stack_Lora_C6 模组构成，模组内部以 U4 ESP32-C6 为主控、U5 128Mbit 串行 Flash 为存储，并通过 SPI/控制网络连接 U1 SX1262 及 FM8625H、SGM13005L4、0900FM15K0039 射频前端。SX1262 与 ESP32-C6 分别具有独立 IPEX4 天线端口，载板提供两组 IPEX4 到 SMA 转接。USB-C 经 FU1、AW32901FCR 和 D3 形成 VBUS_5V，模组内 U6 JW5712WLCSPC#TR 再生成 VDD_3V3；载板还连接 OLED FPC、Grove、蜂鸣器、用户键、启动/复位电路和 WS2812C RGB。PI4IOE5V6408 通过 GPIO8/GPIO10 I2C 受控，并输出 SX_LNA_EN、SX_ANT_SW、SX_NRST 等射频控制信号。

## 检索关键词

`Unit C6L`、`U202`、`M5Stack_Lora_C6`、`ESP32-C6`、`SX1262`、`GD25Q128`、`W25Q128`、`128Mbit Flash`、`PI4IOE5V6408`、`JW5712WLCSPC#TR`、`AW32901FCR`、`FM8625H`、`SGM13005L4`、`0900FM15K0039`、`SPI_CLK`、`SPI_MOSI`、`SPI_MISO`、`SX_NSS`、`SX_BUSY`、`LORA_IRQ`、`SX_NRST`、`SX_LNA_EN`、`SX_ANT_SW`、`USB_DP`、`USB_DM`、`OLED_MOSI`、`OLED_SCK`、`OLED_DC`、`OLED_RST`、`OLED_CS`、`G4_GROVE_1`、`G5_GROVE_0`、`GPIO11_BEEP`、`LED_DAT`、`SYS_KEY1`、`VBUS_5V`、`SYS_3.3V`、`VDD_3V3`、`IPEX4`、`RP-SMA`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U8 (carrier) | M5Stack_Lora_C6 | Stamp C6LoRa 模组，向载板引出 ESP32-C6 GPIO、USB、OLED、Grove、HMI、电源和射频相关网络 | 图 8a035a05960d / 第 1 页 / source_004 网格 A2-C3，U8 M5Stack_Lora_C6 pins1-70 |
| U4 (module) | ESP32-C6 | 模组主控 SoC，连接 Flash、USB、LoRa SPI/状态、IO 扩展器、UART 与外部 GPIO | 图 abbe84dc95af / 第 1 页 / source_002 网格 B1-C2，U4 ESP32-C6 pins1-41 |
| U5 (module) | GD25Q128/W25Q128/128Mbit/3.3V | ESP32-C6 外部 128Mbit 串行 Flash | 图 abbe84dc95af / 第 1 页 / source_002 网格 D1-D2，U5 与 FLASH_CS0/CLK/D/Q/WP/HD |
| U7 (module) | PI4IOE5V6408 | I2C GPIO 扩展器，控制 SX_LNA_EN、SX_ANT_SW、SX_NRST 并提供 EXT_P0-P4 | 图 abbe84dc95af / 第 1 页 / source_002 网格 B3-C3，U7 PI4IOE5V6408 SCL/SDA/INT/RESET/ADDR/P0-P7 |
| U1 (module RF) | SX1262 | LoRa 射频收发器，连接 SPI、BUSY/DIO、32MHz 参考与收发射频前端 | 图 9d4e7673922d / 第 1 页 / source_001 网格 A1-C1，U1 SX1262 pins1-25 |
| U2 (module RF) | 0900FM15K0039 | SX1262 RFO 与差分 RFI_P/RFI_N 到 SX_SRFI/SX_SRFO 的射频匹配/切换网络 | 图 9d4e7673922d / 第 1 页 / source_001 网格 B2，U2 0900FM15K0039，RFO/RFI_P/RFI_N/SW_RFI/SW_RFO |
| U3 (module RF) | FM8625H | 由 SX_DIO2 控制的 LoRa 射频天线开关 | 图 9d4e7673922d / 第 1 页 / source_001 网格 A3-B3，U3 FM8625H RF1/RF2/RFC/CTRL/VDD/GND |
| U8 (module RF) | SGM13005L4 | SX_SRFI_T 到 SX_SRFI 的接收放大器，SX_LNA_EN 控制使能 | 图 9d4e7673922d / 第 1 页 / source_001 网格 B3-C3，U8 SGM13005L4 RFOUT/IN/EN/VDD/GND |
| X1 (module RF) | X1G0041310042 | SX1262 的外部有源参考时钟源，输出 SX_32M_REF | 图 9d4e7673922d / 第 1 页 / source_001 网格 D2，X1、VDD_OCXO、R2/C7 与 SX_32M_REF |
| X2,Y1 (module) | 40MHz/10ppm/20pF/2016 / X1A0001210005 | ESP32-C6 40MHz 主时钟与 XTAL_32K_P/N 低频晶体网络 | 图 abbe84dc95af / 第 1 页 / source_002 网格 B4-C4，X2 40MHz、Y1、R8/R10、C19/C22/C24/C25 |
| J1,J2 (module) | IPEX4 | 分别连接 SX1262 LoRa RF_OUT 与 ESP32-C6 ESP_ANT 的模组射频端口 | 图 9d4e7673922d / 第 1 页 / source_001 网格 A4，J1 IPEX4 与 RF_OUT; 图 abbe84dc95af / 第 1 页 / source_002 网格 A3-A4，J2 IPEX4 与 ESP_ANT_T |
| U6 (module power) | JW5712WLCSPC#TR | VBAT 至 VDD_3V3 的开关稳压器 | 图 6e202f438471 / 第 1 页 / source_003 网格 B2-B3，U6 JW5712WLCSPC#TR、FB2、L5 与输入输出电容 |
| J1 (carrier USB) | USB_C_16P_Horizontal | USB-C 数据与电源输入接口 | 图 8a035a05960d / 第 1 页 / source_004 网格 A1，J1 USB-C、VBUS/DP/DM/CC/SHELL |
| U2 (carrier OVP) | AW32901FCR | EXUSB 输入过压保护器，输出经 D3 形成 VBUS_5V | 图 8a035a05960d / 第 1 页 / source_004 网格 B1，U2 AW32901FCR 与 EXUSB/D3/VBUS_5V |
| J2 (carrier OLED) | FH34SRJ-20S-0.5SH | OLED 20 针 FPC，连接 SPI/控制、电源和电容网络 | 图 8a035a05960d / 第 1 页 / source_004 网格 A4-B4，J2 pins1-20 与 OLED_MOSI/SCK/DC/RST/CS |
| J3 | CON4 | Grove 扩展接口，提供 G4_GROVE_1、G5_GROVE_0、VBUS_5V 与 GND | 图 8a035a05960d / 第 1 页 / source_004 网格 B4-C4，J3 CON4 pins1-4 与 TVS3/TVS4 |
| BZ1,Q1 | LMBR4010BST5G / AHKY2102EI | GPIO11_BEEP 控制的蜂鸣器及低侧驱动网络 | 图 8a035a05960d / 第 1 页 / source_004 网格 C1-D1，BZ1/Q1/D1/D2/R8/C18 与 GPIO11_BEEP |
| S2 | SW | SYS_KEY1 到 GND 的用户按键，带 TVS11 | 图 8a035a05960d / 第 1 页 / source_004 网格 C2-D2，S2 SYS_KEY1 与 TVS11 |
| U1 (carrier RGB) | WS2812C 2020 | LED_DAT 控制的单颗 RGB LED | 图 8a035a05960d / 第 1 页 / source_004 网格 C3-D3，U1 WS2812C 2020 |
| J4,J5,J6,J7 | IPEX-4 / SMA | 两组 IPEX4 到 SMA 天线转接连接器 | 图 8a035a05960d / 第 1 页 / source_004 网格 C4-D4，J4-J6 与 J5-J7 两组同轴连接 |

## 系统结构

### Unit C6L 系统架构

载板 U8 M5Stack_Lora_C6 内部由 ESP32-C6、128Mbit Flash、SX1262、PI4IOE5V6408、射频前端与 JW5712 电源构成；载板连接 USB-C/OVP、OLED、Grove、蜂鸣器、按键、RGB 和两组 SMA 转接。

- 参数与网络：`module=U8 M5Stack_Lora_C6`；`controller=U4 ESP32-C6`；`storage=U5 128Mbit Flash`；`lora=U1 SX1262`；`expander=U7 PI4IOE5V6408`；`module_power=U6 JW5712WLCSPC#TR`；`carrier=USB-C,OLED,Grove,buzzer,buttons,RGB,SMA`
- 证据：图 9d4e7673922d / 第 1 页 / source_001 完整 SX1262/RF 页; 图 abbe84dc95af / 第 1 页 / source_002 完整 ESP32-C6/Flash/IO 页; 图 6e202f438471 / 第 1 页 / source_003 完整模组电源页; 图 8a035a05960d / 第 1 页 / source_004 完整 Unit C6L 载板页

## 电源

### 模组 VBAT 至 VDD_3V3

VBAT_IN 经 FB2 BLM15AX601SN1D 形成 VBAT，送入 U6 JW5712WLCSPC#TR VIN；SW 经 L5 输出 VDD_3V3，MODULE_EN 接 EN，输入配置 C43/C36/C37，输出配置 C33/C34/C35。

- 参数与网络：`input=VBAT_IN -> FB2 -> VBAT`；`converter=U6 JW5712WLCSPC#TR`；`enable=MODULE_EN`；`inductor=L5 FTC121065S2R2MBCA`；`output=VDD_3V3`；`input_caps=C43/C36 10uF/10V,C37 100nF/25V`；`output_caps=C33 1nF/25V,C34/C35 10uF/10V`
- 证据：图 6e202f438471 / 第 1 页 / source_003 完整 VBAT/U6/L5/VDD_3V3 电源页

### EXUSB 过压保护到 VBUS_5V

EXUSB 进入 U2 AW32901FCR 三组 IN，三组 OUT 汇合后经 D3 1N5819WS 输出 VBUS_5V；C10/C11 各 1uF/25V 位于输入/输出侧，U2 GND/nEN 接地。

- 参数与网络：`input=EXUSB`；`ovp=U2 AW32901FCR`；`diode=D3 1N5819WS`；`output=VBUS_5V`；`caps=C10/C11 1uF/25V`；`enable=nEN=GND`
- 证据：图 8a035a05960d / 第 1 页 / source_004 网格 B1 OVP 区

### 电池与充电路径

四页原理图未显示电池连接器、充电器或电池监测；载板将 VBUS_5V 接入模组 VBAT pins29/30，模组内部再生成 VDD_3V3。

- 参数与网络：`battery_connector=null`；`charger=null`；`battery_monitor=null`；`carrier_supply=VBUS_5V -> module VBAT pins29/30`；`module_conversion=VBAT -> JW5712 -> VDD_3V3`
- 证据：图 8a035a05960d / 第 1 页 / source_004 U8 VBAT/VBUS_5V; 图 6e202f438471 / 第 1 页 / source_003 VBAT 电源页

## 接口

### USB-C 电源与数据

J1 USB-C 的 DP1/DP2 汇合为 USB_DP、DM1/DM2 汇合为 USB_DM，CC1/CC2 分别经 R4/R5 5.1K/1% 接 GND；VBUS 经 FU1 1A/6V 形成 EXUSB，D+/D- 分别由 TVS1/TVS2 PESDNC2FD3V3B 保护。

- 参数与网络：`connector=J1 USB_C_16P_Horizontal`；`dp=DP1/DP2=USB_DP`；`dm=DM1/DM2=USB_DM`；`cc=R4/R5 5.1K/1% to GND`；`power=VBUS -> FU1 1A/6V -> EXUSB`；`esd=TVS1/TVS2 PESDNC2FD3V3B`
- 证据：图 8a035a05960d / 第 1 页 / source_004 网格 A1 USB-C 区

### J3 Grove 扩展口

J3 pin1=GND、pin2=VBUS_5V、pin3=G5_GROVE_0、pin4=G4_GROVE_1；信号分别连接模组 GPIO5 pin44 与 GPIO4 pin43，并由 TVS4/TVS3 PESDNC2FD3V3B 对地保护。

- 参数与网络：`pin1=GND`；`pin2=VBUS_5V`；`pin3=G5_GROVE_0 -> module GPIO5 pin44`；`pin4=G4_GROVE_1 -> module GPIO4 pin43`；`protection=TVS4 on G5,TVS3 on G4`
- 证据：图 8a035a05960d / 第 1 页 / source_004 网格 B3-C4 Grove 区

### 两组 IPEX4-SMA 转接

载板 J4 IPEX-4 与 J6 SMA 同轴连接，J5 IPEX-4 与 J7 SMA 同轴连接，两组屏蔽端均接 GND；该页未给两组标注 Wi-Fi 或 LoRa 名称。

- 参数与网络：`pair1=J4 IPEX-4 -> J6 SMA`；`pair2=J5 IPEX-4 -> J7 SMA`；`grounds=pins2=GND`；`function_labels=null`
- 证据：图 8a035a05960d / 第 1 页 / source_004 网格 C4-D4 SMA 区

## 总线

### ESP32-C6 到 SX1262 SPI

ESP32-C6 GPIO20/21/22/23 分别形成 SPI_CLK/SPI_MOSI/SPI_MISO/SX_NSS，并连接 SX1262 SCK pin18、MOSI pin17、MISO pin16、NSS pin19；MOSI 串联 R7 22R/1%。

- 参数与网络：`controller=U4 ESP32-C6`；`device=U1 SX1262`；`sck=GPIO20 -> SPI_CLK -> SX1262 pin18`；`mosi=GPIO21 -> R7 22R/1% -> SPI_MOSI -> pin17`；`miso=GPIO22 <- SPI_MISO <- pin16`；`nss=GPIO23 -> SX_NSS -> pin19`
- 证据：图 abbe84dc95af / 第 1 页 / source_002 U4 GPIO20-GPIO23; 图 9d4e7673922d / 第 1 页 / source_001 U1 SX1262 pins16-19

### PI4IOE5V6408 I2C 与端口映射

ESP32-C6 GPIO8 接 U7 SCL pin13、GPIO10 接 SDA pin14；U7 ADDR pin9 接 GND、RESET pin10 接 ESP_nRST、INT pin1 通过 IRQ_LINE 接 ESP32-C6 GPIO3，P0-P4 为 EXT_P0-P4，P5/P6/P7 为 SX_LNA_EN/SX_ANT_SW/SX_NRST。

- 参数与网络：`scl=ESP32-C6 GPIO8 -> U7 pin13`；`sda=GPIO10 -> pin14`；`interrupt=U7 pin1 IRQ_LINE -> GPIO3 with R13 100K/1% pullup`；`address_pin=pin9 ADDR=GND`；`reset=pin10 RESET=ESP_nRST`；`ports=P0 EXT_P0,P1 EXT_P1,P2 EXT_P2,P3 EXT_P3,P4 EXT_P4,P5 SX_LNA_EN,P6 SX_ANT_SW,P7 SX_NRST`
- 证据：图 abbe84dc95af / 第 1 页 / source_002 网格 B2-C3，U4 GPIO3/8/10 与 U7

### ESP32-C6 原生 USB 映射

载板 USB_DP/USB_DM 分别经 R21/R22 22R/1% 连接模组 G13/USB_D+ pin40 与 G12/USB_D- pin39；模组内对应 ESP32-C6 GPIO13 USB_D_P 与 GPIO12 USB_D_N。

- 参数与网络：`dp=J1 USB_DP -> R21 22R/1% -> module pin40 G13/USB_D+ -> ESP32-C6 GPIO13`；`dm=J1 USB_DM -> R22 22R/1% -> module pin39 G12/USB_D- -> ESP32-C6 GPIO12`
- 证据：图 8a035a05960d / 第 1 页 / source_004 U8 pins39/40 与 USB_DP/USB_DM; 图 abbe84dc95af / 第 1 页 / source_002 U4 GPIO12/GPIO13 USB 网络

### OLED SPI 与控制映射

模组 G21/G20/GPIO18/GPIO15/GPIO6 分别形成 OLED_MOSI/OLED_SCK/OLED_DC/OLED_RST/OLED_CS，并连接 J2 pins15/14/13/12/11。

- 参数与网络：`mosi=module pin51 G21/SPI_MOSI -> J2 pin15`；`clock=pin50 G20/SPI_CLK -> pin14`；`dc=pin49 GPIO18 -> pin13`；`reset=pin46 GPIO15 -> pin12`；`chip_select=pin45 GPIO6 -> pin11`；`supply=SYS_3.3V on J2 pins6/7`
- 证据：图 8a035a05960d / 第 1 页 / source_004 网格 A2-B4，U8 OLED_* 与 J2

## GPIO 与控制信号

### LoRa BUSY、复位与射频控制

SX1262 BUSY pin14 通过 SX_BUSY 连接 ESP32-C6 GPIO19；SX_NRST、SX_LNA_EN、SX_ANT_SW 分别来自 PI4IOE5V6408 P7/P5/P6，SX_DIO2 控制 FM8625H CTRL。

- 参数与网络：`busy=SX1262 pin14 SX_BUSY -> ESP32-C6 GPIO19`；`reset=U7 P7 -> SX_NRST -> SX1262 pin15 NRESET`；`lna_enable=U7 P5 -> SX_LNA_EN -> SGM13005L4 EN`；`antenna_switch_supply=U7 P6 -> SX_ANT_SW -> R1 -> FM8625H VDD`；`rf_switch_control=SX1262 pin12 DIO2 -> SX_DIO2 -> R9 -> FM8625H CTRL`
- 证据：图 9d4e7673922d / 第 1 页 / source_001 SX1262 BUSY/NRESET/DIO2 与 U3/U8; 图 abbe84dc95af / 第 1 页 / source_002 U4 GPIO19 与 U7 P5-P7

### 用户按键

S2 将 SYS_KEY1 按下接 GND，SYS_KEY1 连接模组 EXT_P0 pin7；TVS11 PESDNC2FD3V3B 从 SYS_KEY1 接 GND。

- 参数与网络：`switch=S2`；`net=SYS_KEY1`；`module_pin=U8 pin7 EXT_P0`；`active_level=low`；`protection=TVS11 PESDNC2FD3V3B`
- 证据：图 8a035a05960d / 第 1 页 / source_004 网格 C2-D2 USER BTN 与 U8 pin7

### WS2812C RGB

模组 GPIO2 pin41 的 LED_DAT 连接 U1 WS2812C 2020 DIN，U1 VDD 接 SYS_3.3V、VSS 接 GND，C2 1uF/16V 去耦。

- 参数与网络：`controller=module GPIO2 pin41 LED_DAT`；`led=U1 WS2812C 2020`；`supply=SYS_3.3V`；`ground=GND`；`decoupling=C2 1uF/16V`
- 证据：图 8a035a05960d / 第 1 页 / source_004 网格 C3-D3 RGB 区与 U8 pin41

## 时钟

### ESP32-C6 外部时钟

X2 标为 40MHz/10ppm/20pF/2016，连接 U4 XTAL_40M_P/N 并配 R8、C19/C22；Y1 跨接 XTAL_32K_P/N，R10 1M/1% 跨接两端，C24/C25 各 6pF/50V 对地。

- 参数与网络：`main_crystal=X2 40MHz/10ppm/20pF/2016`；`main_pins=U4 XTAL_P/XTAL_N`；`low_frequency=Y1 X1A0001210005 on XTAL_32K_P/N`；`feedback=R10 1M/1%`；`load_caps=C24/C25 6pF/50V`
- 证据：图 abbe84dc95af / 第 1 页 / source_002 网格 B4-C4，X2/Y1 时钟网络

### SX1262 32M 参考

X1 X1G0041310042 由 VDD_OCXO 3.0V 供电，输出经 R2 220R/1% 与 C7 10nF/5% 形成 SX_32M_REF并进入 SX1262 XTA pin3；XTB pin4 未连接，DIO3 pin6 连接 VDD_OCXO。

- 参数与网络：`source=X1 X1G0041310042`；`supply=VDD_OCXO 3.0V`；`output=SX_32M_REF`；`path=X1 pin3 -> R2 220R/1%/C7 10nF/5% -> SX1262 pin3 XTA`；`xtb=pin4 NC`；`dio3=pin6 VDD_OCXO`
- 证据：图 9d4e7673922d / 第 1 页 / source_001 网格 A1/D2，SX1262 XTA/XTB/DIO3 与 X1

## 复位

### 启动与复位网络

模组 ESP_nRST pin64 形成 MCU_RST 测试点 TP7；GPIO9/BOOT pin8 引出 G9_BOOT/TP4。载板 S1 与 Q2/Q3/D4/C1/LED1/LED2 构成 SYS_SW、MCU_RST 的启动/复位指示控制网络。

- 参数与网络：`reset=module pin64 ESP_nRST -> MCU_RST/TP7`；`boot=module pin8 GPIO9/BOOT -> G9_BOOT/TP4`；`switch=S1`；`control=Q2/Q3 2N7002DW,D4,C1`；`indicators=LED1/LED2`
- 证据：图 8a035a05960d / 第 1 页 / source_004 网格 A2-D2，U8 ESP_nRST/GPIO9-BOOT 与 BOOT 区

## 保护电路

### 模组射频口保护

LoRa RF_OUT 端由 D1 H3V3U10B 对地保护，ESP_ANT_T 端由 D2 H3V3U10B 对地保护；两端分别连接 J1/J2 IPEX4。

- 参数与网络：`lora=D1 H3V3U10B at RF_OUT/J1`；`esp=D2 H3V3U10B at ESP_ANT_T/J2`
- 证据：图 9d4e7673922d / 第 1 页 / source_001 J1/D1; 图 abbe84dc95af / 第 1 页 / source_002 J2/D2

## 内存与 Flash

### ESP32-C6 外部 Flash

U5 标为 GD25Q128/W25Q128/128Mbit/3.3V，通过 FLASH_CS0/CLK/D/Q/WP/HD 连接 U4 ESP32-C6 的 SPICS0/SPICLK/SPID/SPIQ/SPIWP/SPIHD。

- 参数与网络：`reference=U5`；`capacity=128Mbit`；`equivalent_bytes=16MB`；`supply=FLASH_VCC 3.3V`；`signals=FLASH_CS0,FLASH_CLK,FLASH_D,FLASH_Q,FLASH_WP,FLASH_HD`；`series=R14 22R/1% on FLASH_CLK`
- 证据：图 abbe84dc95af / 第 1 页 / source_002 网格 B1-D2，U4 SPI Flash pins与 U5

## 音频

### GPIO11 蜂鸣器驱动

模组 GPIO11 pin9 形成 GPIO11_BEEP，经 C18/R8/D2 驱动 Q1 AHKY2102EI，Q1 低侧控制 BZ1 LMBR4010BST5G；D1 并接蜂鸣器支路。

- 参数与网络：`gpio=module pin9 GPIO11_BEEP`；`driver=Q1 AHKY2102EI`；`buzzer=BZ1 LMBR4010BST5G`；`input_network=C18 1uF/16V,R8 2K/1%,D2`；`flyback=D1 LMBR4010BST5G`
- 证据：图 8a035a05960d / 第 1 页 / source_004 网格 C1-D1 BUZZER 区与 U8 pin9

## 射频

### SX1262 LoRa 射频前端

SX1262 RFO 与 RFI_P/RFI_N 进入 U2 0900FM15K0039，形成 SX_SRFO/SX_SRFI；接收路径可经 U8 SGM13005L4，U3 FM8625H 在发射/接收路径间切换，共同端经 C1/L3 输出 RF_OUT 到 J1 IPEX4。

- 参数与网络：`transceiver=U1 SX1262`；`matching=U2 0900FM15K0039`；`lna=U8 SGM13005L4`；`switch=U3 FM8625H`；`output=RF_OUT`；`connector=J1 IPEX4`；`impedance_labels=RF_50R`
- 证据：图 9d4e7673922d / 第 1 页 / source_001 网格 A1-C4，完整 SX1262 RF 链

### ESP32-C6 射频天线路径

U4 ANT pin1 形成 ESP_ANT，经 L4/C20/C21/L6/C38 匹配网络形成 ESP_ANT_T，D2 H3V3U10B 对地保护并连接 J2 IPEX4。

- 参数与网络：`source=U4 ESP32-C6 pin1 ANT`；`input_net=ESP_ANT`；`output_net=ESP_ANT_T`；`matching=L4 2.4nH,C20 2.0pF,C21 1.8pF,L6 1.5pF,C38 3.5nH`；`protection=D2 H3V3U10B`；`connector=J2 IPEX4`
- 证据：图 abbe84dc95af / 第 1 页 / source_002 网格 A3-B4，ESP_ANT 至 J2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit C6L 系统架构 | `module=U8 M5Stack_Lora_C6`；`controller=U4 ESP32-C6`；`storage=U5 128Mbit Flash`；`lora=U1 SX1262`；`expander=U7 PI4IOE5V6408`；`module_power=U6 JW5712WLCSPC#TR`；`carrier=USB-C,OLED,Grove,buzzer,buttons,RGB,SMA` |
| 内存与 Flash | ESP32-C6 外部 Flash | `reference=U5`；`capacity=128Mbit`；`equivalent_bytes=16MB`；`supply=FLASH_VCC 3.3V`；`signals=FLASH_CS0,FLASH_CLK,FLASH_D,FLASH_Q,FLASH_WP,FLASH_HD`；`series=R14 22R/1% on FLASH_CLK` |
| 总线 | ESP32-C6 到 SX1262 SPI | `controller=U4 ESP32-C6`；`device=U1 SX1262`；`sck=GPIO20 -> SPI_CLK -> SX1262 pin18`；`mosi=GPIO21 -> R7 22R/1% -> SPI_MOSI -> pin17`；`miso=GPIO22 <- SPI_MISO <- pin16`；`nss=GPIO23 -> SX_NSS -> pin19` |
| GPIO 与控制信号 | LoRa BUSY、复位与射频控制 | `busy=SX1262 pin14 SX_BUSY -> ESP32-C6 GPIO19`；`reset=U7 P7 -> SX_NRST -> SX1262 pin15 NRESET`；`lna_enable=U7 P5 -> SX_LNA_EN -> SGM13005L4 EN`；`antenna_switch_supply=U7 P6 -> SX_ANT_SW -> R1 -> FM8625H VDD`；`rf_switch_control=SX1262 pin12 DIO2 -> SX_DIO2 -> R9 -> FM8625H CTRL` |
| 总线 | PI4IOE5V6408 I2C 与端口映射 | `scl=ESP32-C6 GPIO8 -> U7 pin13`；`sda=GPIO10 -> pin14`；`interrupt=U7 pin1 IRQ_LINE -> GPIO3 with R13 100K/1% pullup`；`address_pin=pin9 ADDR=GND`；`reset=pin10 RESET=ESP_nRST`；`ports=P0 EXT_P0,P1 EXT_P1,P2 EXT_P2,P3 EXT_P3,P4 EXT_P4,P5 SX_LNA_EN,P6 SX_ANT_SW,P7 SX_NRST` |
| 时钟 | ESP32-C6 外部时钟 | `main_crystal=X2 40MHz/10ppm/20pF/2016`；`main_pins=U4 XTAL_P/XTAL_N`；`low_frequency=Y1 X1A0001210005 on XTAL_32K_P/N`；`feedback=R10 1M/1%`；`load_caps=C24/C25 6pF/50V` |
| 时钟 | SX1262 32M 参考 | `source=X1 X1G0041310042`；`supply=VDD_OCXO 3.0V`；`output=SX_32M_REF`；`path=X1 pin3 -> R2 220R/1%/C7 10nF/5% -> SX1262 pin3 XTA`；`xtb=pin4 NC`；`dio3=pin6 VDD_OCXO` |
| 射频 | SX1262 LoRa 射频前端 | `transceiver=U1 SX1262`；`matching=U2 0900FM15K0039`；`lna=U8 SGM13005L4`；`switch=U3 FM8625H`；`output=RF_OUT`；`connector=J1 IPEX4`；`impedance_labels=RF_50R` |
| 射频 | ESP32-C6 射频天线路径 | `source=U4 ESP32-C6 pin1 ANT`；`input_net=ESP_ANT`；`output_net=ESP_ANT_T`；`matching=L4 2.4nH,C20 2.0pF,C21 1.8pF,L6 1.5pF,C38 3.5nH`；`protection=D2 H3V3U10B`；`connector=J2 IPEX4` |
| 保护电路 | 模组射频口保护 | `lora=D1 H3V3U10B at RF_OUT/J1`；`esp=D2 H3V3U10B at ESP_ANT_T/J2` |
| 电源 | 模组 VBAT 至 VDD_3V3 | `input=VBAT_IN -> FB2 -> VBAT`；`converter=U6 JW5712WLCSPC#TR`；`enable=MODULE_EN`；`inductor=L5 FTC121065S2R2MBCA`；`output=VDD_3V3`；`input_caps=C43/C36 10uF/10V,C37 100nF/25V`；`output_caps=C33 1nF/25V,C34/C35 10uF/10V` |
| 接口 | USB-C 电源与数据 | `connector=J1 USB_C_16P_Horizontal`；`dp=DP1/DP2=USB_DP`；`dm=DM1/DM2=USB_DM`；`cc=R4/R5 5.1K/1% to GND`；`power=VBUS -> FU1 1A/6V -> EXUSB`；`esd=TVS1/TVS2 PESDNC2FD3V3B` |
| 总线 | ESP32-C6 原生 USB 映射 | `dp=J1 USB_DP -> R21 22R/1% -> module pin40 G13/USB_D+ -> ESP32-C6 GPIO13`；`dm=J1 USB_DM -> R22 22R/1% -> module pin39 G12/USB_D- -> ESP32-C6 GPIO12` |
| 电源 | EXUSB 过压保护到 VBUS_5V | `input=EXUSB`；`ovp=U2 AW32901FCR`；`diode=D3 1N5819WS`；`output=VBUS_5V`；`caps=C10/C11 1uF/25V`；`enable=nEN=GND` |
| 总线 | OLED SPI 与控制映射 | `mosi=module pin51 G21/SPI_MOSI -> J2 pin15`；`clock=pin50 G20/SPI_CLK -> pin14`；`dc=pin49 GPIO18 -> pin13`；`reset=pin46 GPIO15 -> pin12`；`chip_select=pin45 GPIO6 -> pin11`；`supply=SYS_3.3V on J2 pins6/7` |
| 接口 | J3 Grove 扩展口 | `pin1=GND`；`pin2=VBUS_5V`；`pin3=G5_GROVE_0 -> module GPIO5 pin44`；`pin4=G4_GROVE_1 -> module GPIO4 pin43`；`protection=TVS4 on G5,TVS3 on G4` |
| 音频 | GPIO11 蜂鸣器驱动 | `gpio=module pin9 GPIO11_BEEP`；`driver=Q1 AHKY2102EI`；`buzzer=BZ1 LMBR4010BST5G`；`input_network=C18 1uF/16V,R8 2K/1%,D2`；`flyback=D1 LMBR4010BST5G` |
| GPIO 与控制信号 | 用户按键 | `switch=S2`；`net=SYS_KEY1`；`module_pin=U8 pin7 EXT_P0`；`active_level=low`；`protection=TVS11 PESDNC2FD3V3B` |
| GPIO 与控制信号 | WS2812C RGB | `controller=module GPIO2 pin41 LED_DAT`；`led=U1 WS2812C 2020`；`supply=SYS_3.3V`；`ground=GND`；`decoupling=C2 1uF/16V` |
| 复位 | 启动与复位网络 | `reset=module pin64 ESP_nRST -> MCU_RST/TP7`；`boot=module pin8 GPIO9/BOOT -> G9_BOOT/TP4`；`switch=S1`；`control=Q2/Q3 2N7002DW,D4,C1`；`indicators=LED1/LED2` |
| 接口 | 两组 IPEX4-SMA 转接 | `pair1=J4 IPEX-4 -> J6 SMA`；`pair2=J5 IPEX-4 -> J7 SMA`；`grounds=pins2=GND`；`function_labels=null` |
| 电源 | 电池与充电路径 | `battery_connector=null`；`charger=null`；`battery_monitor=null`；`carrier_supply=VBUS_5V -> module VBAT pins29/30`；`module_conversion=VBAT -> JW5712 -> VDD_3V3` |
| GPIO 与控制信号 | LoRa IRQ 到 GPIO7 的跨页对应 | `sx1262=pin13 DIO1=LORA_IRQ`；`carrier_module_pin=pin42 GPIO7=G7_LORA_IRQ`；`esp32_page=GPIO7 label only`；`confirmed_cross_sheet_net=false` |
| 内存与 Flash | 正文 ESP32-C6 内核与频率 | `soc=U4 ESP32-C6`；`documented_main_core=RISC-V 32-bit 160MHz`；`documented_low_power_core=RISC-V 32-bit 20MHz`；`external_flash=128Mbit`；`schematic_cpu_detail=null` |
| 接口 | 正文 OLED 型号、尺寸与分辨率 | `documented_controller=SSD1306`；`documented_size=0.66 inch`；`documented_resolution=64x48`；`connector=J2 FH34SRJ-20S-0.5SH`；`schematic_display_part=null` |
| 射频 | 正文 LoRa 与 Wi-Fi 性能 | `documented_lora_band=868-923MHz`；`documented_lora_tx=+22dBm`；`documented_lora_sensitivity=-147dBm`；`documented_wifi=2.4GHz Wi-Fi 6`；`region_config=null`；`test_conditions=null` |
| 射频 | 正文 RP-SMA 天线规格与端口对应 | `documented_wifi_antenna=84mm,2.4GHz,3dBi,RP-SMA`；`documented_lora_antenna=108mm,868MHz,3dBi,RP-SMA`；`pair1=J4/J6`；`pair2=J5/J7`；`mapping=null` |
| 电源 | 正文各模式功耗 | `documented_grove_sleep=696.86uA`；`documented_usb_sleep=866.42uA`；`documented_usb_lora_rx=85.18mA`；`documented_usb_lora_tx=80.02mA`；`test_conditions=null` |
| 保护电路 | AW32901FCR 过压保护阈值 | `device=U2 AW32901FCR`；`input=EXUSB`；`output=VBUS_5V via D3`；`ovp_threshold=null`；`recovery_threshold=null`；`current_limit=null`；`response_time=null` |
| 其他事实 | 正文 Meshtastic 与下载模式行为 | `documented_firmware=Meshtastic`；`documented_download_action=hold reset 3s`；`documented_led_transition=green to red`；`firmware_version=null`；`timing_implementation=null` |

## 待确认事项

- `gpio.lora-irq-cross-page`：SX1262 DIO1 pin13 在 source_001 标为 LORA_IRQ，载板模组 pin42 标为 GPIO7/G7_LORA_IRQ；但 source_002 ESP32-C6 GPIO7 只标 GPIO7，未显示同名 LORA_IRQ 连线，跨页网络连续性不能仅由页面标签闭环。（证据：图 9d4e7673922d / 第 1 页 / source_001 U1 pin13 DIO1/LORA_IRQ; 图 abbe84dc95af / 第 1 页 / source_002 U4 GPIO7; 图 8a035a05960d / 第 1 页 / source_004 U8 pin42 G7_LORA_IRQ）
- `memory.documented-soc-spec`：正文称 ESP32-C6 包含 160MHz 高性能 RISC-V 核和 20MHz 低功耗 RISC-V 核；原理图确认 U4 型号与 128Mbit 外部 Flash，但未展开 CPU 架构或运行频率。（证据：图 abbe84dc95af / 第 1 页 / source_002 U4 ESP32-C6 与 U5 Flash）
- `interface.documented-oled`：正文称 OLED 为 SSD1306、0.66英寸、64×48；原理图只显示 J2 FPC 与 OLED_MOSI/SCK/DC/RST/CS、电源和电容，没有显示 SSD1306 位号、尺寸或分辨率。（证据：图 8a035a05960d / 第 1 页 / source_004 OLED 区 J2，无显示器型号文字）
- `rf.documented-radio-performance`：正文称 LoRa 工作 868-923MHz、最大发射 +22dBm、接收灵敏度 -147dBm，并支持 2.4GHz Wi-Fi 6；原理图确认 SX1262/ESP32-C6 与射频匹配和天线端口，但未标区域配置、功率、灵敏度、协议模式或整机射频测试结果。（证据：图 9d4e7673922d / 第 1 页 / source_001 SX1262/RF_OUT; 图 abbe84dc95af / 第 1 页 / source_002 ESP32-C6/ESP_ANT）
- `rf.documented-antennas`：正文列出 2.4GHz 84mm 3dBi 和 868MHz 108mm 3dBi 两根 RP-SMA 天线；载板只显示 J4/J6 与 J5/J7 两组转接，未标哪组对应 LoRa/Wi-Fi，也未标长度、增益或频段。（证据：图 8a035a05960d / 第 1 页 / source_004 SMA 区，无 Wi-Fi/LoRa 标签）
- `power.documented-consumption`：正文列出 Grove/USB 休眠、LoRa 接收等待和最大功率连续发送电流；原理图只确认电源路径，没有固件模式、射频配置、测试电压、外设状态、温度或容差。（证据：图 8a035a05960d / 第 1 页 / source_004 USB/OVP/VBUS_5V/模块电源入口; 图 6e202f438471 / 第 1 页 / source_003 模组 3.3V 电源）
- `protection.ovp-thresholds`：原理图确认 AW32901FCR 位于 EXUSB 到 VBUS_5V 路径，但未标过压阈值、恢复阈值、限流、响应时间、额定电压或 nACK 行为。（证据：图 8a035a05960d / 第 1 页 / source_004 OVP 区 U2）
- `other.documented-meshtastic`：正文称支持 Meshtastic，并描述长按复位键 3秒后绿灯变红进入下载模式；原理图确认 BOOT/RESET/LED 控制网络，但未给固件版本、长按计时逻辑、LED 状态机或 Meshtastic 功能配置。（证据：图 8a035a05960d / 第 1 页 / source_004 BOOT/MCU_RST/LED1/LED2 电路）
- `review.lora-irq-cross-page`：请用完整网表或 PCB 确认 SX1262 DIO1/LORA_IRQ 是否实际连接 ESP32-C6 GPIO7 及载板 pin42。；原因：三页间网络标签不完全一致，无法从同名网络闭环。
- `review.soc-spec`：请用 ESP32-C6 datasheet 和固件配置确认双 RISC-V 核角色、160MHz/20MHz 时钟与可用内存。；原因：板级原理图不展开 SoC 内部资源。
- `review.oled`：请用 OLED BOM 或规格确认 SSD1306、0.66英寸、64×48 与 J2 完整引脚定义。；原因：原理图只显示 FPC 接口。
- `review.radio-performance`：请用区域配置、天线与整机测试确认 868-923MHz、+22dBm、-147dBm 和 Wi-Fi 6 性能。；原因：射频性能受匹配、天线、固件与法规区域影响。
- `review.antennas`：请用装配图/BOM 确认 J4/J6 与 J5/J7 哪组对应 LoRa/Wi-Fi，以及两根 RP-SMA 天线的频段、长度和增益。；原因：载板天线转接对没有功能标签。
- `review.power-consumption`：请确认各功耗数值的供电电压、固件、LoRa 配置、OLED/RGB/蜂鸣器状态、温度和测量容差。；原因：原理图不能证明动态整机功耗。
- `review.ovp-thresholds`：请用 AW32901FCR datasheet/BOM 确认 OVP、恢复、限流、响应和额定边界。；原因：原理图未标保护阈值。
- `review.meshtastic-download`：请用出厂固件确认 Meshtastic 版本/配置、3秒长按下载逻辑与 LED 状态定义。；原因：原理图只显示 BOOT/RESET/LED 硬件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `9d4e7673922d89a85b5b848fe64e9e84f57b09569608d200784f892b18257fe2` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/U202-SCH_Sch_M5_C6_Lora_v0.2.3_2025_06_25_16_54_56_page_01.png` |
| 2 | 1 | `abbe84dc95af45e1b8338043446af91c1cc95dc3571ba21f5b2e3bdd7914fa4f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/U202-SCH_Sch_M5_C6_Lora_v0.2.3_2025_06_25_16_54_56_page_02.png` |
| 3 | 1 | `6e202f43847140e47d47998687c4de410b32bc64967106d0f1c2d73f5e142a31` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/U202-SCH_Sch_M5_C6_Lora_v0.2.3_2025_06_25_16_54_56_page_03.png` |
| 4 | 1 | `8a035a05960da742909c00446285caaf883409f8bcf4ca453fd5e2d72e93315d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/U202-SCH_Unit_C6L_SCH_B0.4.1_20250826_2025_08_26_16_13_36_page_01.png` |

---

源文档：`zh_CN/unit/Unit_C6L.md`

源文档 SHA-256：`f2f9d49b98cb40f61369bda85eb54e409835659f3b88953fbddfd3ccef2ab936`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
