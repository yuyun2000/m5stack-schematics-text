# Stamp C6LoRa 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp C6LoRa |
| SKU | S012 |
| 产品 ID | `stamp-c6lora-8e0b68b10cfd` |
| 源文档 | `zh_CN/core/Stamp_C6LoRa.md` |

## 概述

Stamp C6LoRa S012 的三页 v0.2.3 原理图以 ESP32-C6 和 SX1262 为核心，配有 128Mbit 外部 Flash、PI4IOE5V6408 IO 扩展器、0900FM15K0039 与 FM8625H 射频开关、SGM13005L4 低噪声放大器，以及独立 LoRa/Wi-Fi IPEX4 天线座。VBAT_IN 经 JW5712 生成 VDD_3V3，ESP32-C6 通过 SPI 控制 SX1262，并由 IO 扩展器控制 LoRa 复位、LNA 和天线开关。

## 检索关键词

`Stamp C6LoRa`、`S012`、`ESP32-C6`、`SX1262`、`PI4IOE5V6408`、`SGM13005L4`、`0900FM15K0039`、`FM8625H`、`GD25Q128`、`W25Q128`、`JW5712WLCSPC#TR`、`IPEX4`、`LoRa`、`Wi-Fi 6`、`SPI_CLK`、`SPI_MOSI`、`SPI_MISO`、`SX_NSS`、`SX_BUSY`、`LORA_IRQ`、`SX_LNA_EN`、`SX_ANT_SW`、`SX_NRST`、`SX_DIO2`、`SX_32M_REF`、`EXT_P0`、`EXT_P1`、`EXT_P2`、`EXT_P3`、`EXT_P4`、`MODULE_EN`、`VBAT_IN`、`VDD_3V3`、`USB_D_N`、`USB_D_P`、`ESP_U0TXD`、`ESP_U0RXD`、`ESP_ANT`、`RF_50R`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SX1262 | LoRa 射频收发器，通过 SPI、BUSY、DIO 和复位网络连接 ESP32-C6 与射频前端 | 图 82e3d6f9ae74 / 第 1 页 / 页 1 A1-C2，U1 SX1262 |
| U2 | 0900FM15K0039 | SX1262 RFO 与差分 RFI_P/RFI_N 之间的射频收发切换器件 | 图 82e3d6f9ae74 / 第 1 页 / 页 1 B2，U2 0900FM15K0039，RFO/RFI_P/RFI_N 与 SW_RFI/SW_RFO |
| U3 | FM8625H | 由 SX_DIO2 控制的 LoRa 天线收发路径开关 | 图 82e3d6f9ae74 / 第 1 页 / 页 1 B3，U3 FM8625H，RF1/RF2/RFC/CTRL |
| U8 | SGM13005L4 | 由 SX_LNA_EN 控制的 LoRa 接收低噪声放大器 | 图 82e3d6f9ae74 / 第 1 页 / 页 1 C3，U8 SGM13005L4，SX_SRFI_T 到 SX_SRFI |
| J1 | IPEX4 | LoRa 外接天线座 | 图 82e3d6f9ae74 / 第 1 页 / 页 1 B4，J1 IPEX4 与 RF_50R 天线网络 |
| X1 | X1G0041310042 | SX1262 的 32MHz 有源参考时钟 | 图 82e3d6f9ae74 / 第 1 页 / 页 1 D2，X1 X1G0041310042，VDD_OCXO 与 SX_32M_REF |
| U4 | ESP32-C6 | 主控 SoC，连接 Flash、LoRa SPI/控制、IO 扩展、USB、UART、时钟和 Wi-Fi 天线 | 图 1555dbd67766 / 第 1 页 / 页 2 B1-C2，U4 ESP32-C6 |
| U5 | GD25Q128/W25Q128/128Mbit/3.3V | ESP32-C6 外部 128Mbit SPI Flash | 图 1555dbd67766 / 第 1 页 / 页 2 D1-D2，U5 GD25Q128/W25Q128/128Mbit/3.3V |
| U7 | PI4IOE5V6408 | I2C 8-bit IO 扩展器，提供 EXT_P0-P4 并控制 SX_LNA_EN、SX_ANT_SW、SX_NRST | 图 1555dbd67766 / 第 1 页 / 页 2 C2-C3，U7 PI4IOE5V6408 |
| X2 | 40MHz/10ppm/20pF/2016 | ESP32-C6 40MHz 主晶振 | 图 1555dbd67766 / 第 1 页 / 页 2 B4，X2 40MHz/10ppm/20pF/2016 |
| Y1 | X1A0001210005 | 连接 XTAL_32K_P/N 的低频晶体 | 图 1555dbd67766 / 第 1 页 / 页 2 C4，Y1 X1A0001210005 与 XTAL_32K_P/N |
| J2 | IPEX4 | ESP32-C6 Wi-Fi 外接天线座 | 图 1555dbd67766 / 第 1 页 / 页 2 A3-A4，ESP_ANT 匹配网络、D2 与 J2 IPEX4 |
| U6 | JW5712WLCSPC#TR | MODULE_EN 控制的 VBAT 到 VDD_3V3 电源转换器 | 图 5dc352ecc789 / 第 1 页 / 页 3 B2-C3，U6 JW5712WLCSPC#TR |
| D1,D2 | H3V3U10B | LoRa 与 Wi-Fi IPEX 天线端口的射频 ESD 保护 | 图 82e3d6f9ae74 / 第 1 页 / 页 1 B4，D1 H3V3U10B; 图 1555dbd67766 / 第 1 页 / 页 2 A4，D2 H3V3U10B |

## 系统结构

### Stamp C6LoRa 三页架构

U4 ESP32-C6 连接 U5 128Mbit Flash、USB/UART、J2 Wi-Fi 天线和 U7 IO 扩展器；U1 SX1262 通过 SPI 与控制网络连接主控，经 U2/U3 射频开关、U8 LNA 和 J1 LoRa 天线形成收发链路；U6 将 VBAT 输入转换为全板 VDD_3V3。

- 参数与网络：`schematic_revision=v0.2.3`；`schematic_date=2025-12-02`；`page_count=3`
- 证据：图 82e3d6f9ae74 / 第 1 页 / 页 1 SX1262 与 LoRa RF 前端全页; 图 1555dbd67766 / 第 1 页 / 页 2 ESP32-C6、Flash、IO 扩展与 Wi-Fi RF 全页; 图 5dc352ecc789 / 第 1 页 / 页 3 VBAT 到 VDD_3V3 电源全页

## 电源

### VBAT_IN 到 VDD_3V3

VBAT_IN 经 FB2 BLM15AX601SN1D 形成 VBAT 并进入 U6 JW5712WLCSPC#TR；U6 EN 接 MODULE_EN，SW 经 L5 输出 VDD_3V3，输入和输出均配置多颗去耦电容。

- 参数与网络：`input=VBAT_IN`；`internal_input=VBAT`；`output=VDD_3V3`；`enable=MODULE_EN`
- 证据：图 5dc352ecc789 / 第 1 页 / 页 3 B1-C4，FB2/U6/L5、MODULE_EN、VBAT 与 VDD_3V3

### SX1262 电源与内部稳压网络

U1 VDD_IN、VBAT 与 VBAT_IO 接 VDD_3V3，VREG/DCC_SW 通过 SX_VREG 与 L2 MWSD1008FE150 构成内部稳压网络，VR_PA 连接 SX_PAVDD 并经 L1 接射频功放路径，DIO3 输出 VDD_OCXO 为 X1 参考时钟供电。

- 参数与网络：`main_supply=VDD_3V3`；`regulator_net=SX_VREG`；`pa_supply=SX_PAVDD`；`clock_supply=VDD_OCXO`
- 证据：图 82e3d6f9ae74 / 第 1 页 / 页 1 A1-D2，U1 VDD_IN/VBAT/VBAT_IO/VREG/DCC_SW/VR_PA/DIO3 与 L1/L2/X1

## 接口

### ESP32-C6 USB 与 UART 下载接口网络

U4 GPIO12/GPIO13 分别连接 USB_D_N/USB_D_P；U0TXD/U0RXD 经 SDMM0806H-2-900T 与 R6 499Ω 网络输出 ESP_U0TXD/ESP_U0RXD，形成原生 USB 数据与 UART0 信号路径。

- 参数与网络：`usb_dm_gpio=12`；`usb_dp_gpio=13`；`uart_tx=ESP_U0TXD`；`uart_rx=ESP_U0RXD`
- 证据：图 1555dbd67766 / 第 1 页 / 页 2 B1-C2，U4 GPIO12/13、U0TXD/U0RXD 与 USB/UART 网络

## 总线

### ESP32-C6 到 SX1262 SPI 与状态线

U4 GPIO20 经 R7 22Ω 连接 SPI_CLK，GPIO21 连接 SPI_MOSI，GPIO22 连接 SPI_MISO，GPIO23 连接 SX_NSS，GPIO19 连接 SX_BUSY；这些网络分别接 U1 SCK/MOSI/MISO/NSS/BUSY。

- 参数与网络：`sck_gpio=20`；`mosi_gpio=21`；`miso_gpio=22`；`nss_gpio=23`；`busy_gpio=19`
- 证据：图 82e3d6f9ae74 / 第 1 页 / 页 1 B1-B2，U1 BUSY/NSS/MISO/MOSI/SCK; 图 1555dbd67766 / 第 1 页 / 页 2 C1-C2，U4 GPIO19-23 与 SX_BUSY/SPI/SX_NSS

### PI4IOE5V6408 I2C 控制

U7 PI4IOE5V6408 的 SCL/SDA 分别连接 U4 GPIO8/GPIO10，R4/R12 各 2.2K 上拉到 VDD_3V3；INT 输出 IRQ_LINE 并连接 U4 GPIO3，RESET 接 ESP_nRST，ADDR 接地。

- 参数与网络：`scl_gpio=8`；`sda_gpio=10`；`interrupt_gpio=3`；`address_pin=GND`
- 证据：图 1555dbd67766 / 第 1 页 / 页 2 B2-C3，U4 GPIO3/8/10、R4/R12/R13 与 U7 SCL/SDA/INT/ADDR/RESET

## GPIO 与控制信号

### PI4IOE5V6408 P0-P7 映射

U7 P0-P4 分别引出 EXT_P0、EXT_P1、EXT_P2、EXT_P3、EXT_P4，P5/P6/P7 分别连接 SX_LNA_EN、SX_ANT_SW、SX_NRST。

- 参数与网络：`p0=EXT_P0`；`p1=EXT_P1`；`p2=EXT_P2`；`p3=EXT_P3`；`p4=EXT_P4`；`p5=SX_LNA_EN`；`p6=SX_ANT_SW`；`p7=SX_NRST`
- 证据：图 1555dbd67766 / 第 1 页 / 页 2 C2-C3，U7 P0-P7 网络

## 时钟

### ESP32-C6 40MHz 晶振

X2 标注 40MHz/10ppm/20pF/2016，连接 XTAL_40M_P/N；P 端串联 R8 24nH，C19 27pF 与 C22 24pF 分别从 P/N 对地。

- 参数与网络：`frequency_mhz=40`；`tolerance_ppm=10`；`load_pf=20`
- 证据：图 1555dbd67766 / 第 1 页 / 页 2 B4，X2/R8/C19/C22 与 XTAL_40M_P/N

### ESP32-C6 XTAL_32K_P/N 晶体

Y1 X1A0001210005 连接 XTAL_32K_P/N，R10 1M 跨接两端，C24/C25 各 6pF 对地；图面网络名含 32K，但未单独写出晶体的精确频率或公差。

- 参数与网络：`network=XTAL_32K_P/N`；`parallel_resistor_ohm=1000000`；`load_capacitor_pf=6`
- 证据：图 1555dbd67766 / 第 1 页 / 页 2 C4，Y1/R10/C24/C25

### SX1262 32MHz 有源参考

X1 X1G0041310042 由 VDD_OCXO 供电，输出经 R2 220Ω 与 C7 10nF 串联形成 SX_32M_REF，并接 U1 XTA；U1 XTB 标为未连接。

- 参数与网络：`reference_net=SX_32M_REF`；`supply=VDD_OCXO`；`annotated_supply_v=3.0`
- 证据：图 82e3d6f9ae74 / 第 1 页 / 页 1 D2，X1/R2/C7 与 U1 XTA/XTB

## 复位

### ESP_nRST 与 LoRa 复位控制

ESP_nRST 由 R3 10K 上拉到 VDD_3V3、C16 1uF 对地，并连接 U4 CHIP_PU 与 U7 RESET；U7 P7 输出 SX_NRST 到 U1 NRESET，实现主控侧控制 LoRa 复位。

- 参数与网络：`system_reset=ESP_nRST`；`lora_reset=SX_NRST`；`lora_reset_expander_pin=P7`
- 证据：图 82e3d6f9ae74 / 第 1 页 / 页 1 A1/D1，U1 NRESET、R3/C16; 图 1555dbd67766 / 第 1 页 / 页 2 B1-C3，U4 CHIP_PU、U7 RESET/P7

## 存储

### 128Mbit 外部 SPI Flash

U5 明确标注 GD25Q128/W25Q128/128Mbit/3.3V，nCS/CLK/DI/DO/nWP/nHOLD 分别连接 FLASH_CS0、FLASH_CLK、FLASH_D、FLASH_Q、FLASH_WP、FLASH_HD；FLASH_CLK 串联 R14 22Ω。128Mbit 换算为 16MB。

- 参数与网络：`capacity_mbit=128`；`capacity_mb=16`；`supply_v=3.3`
- 证据：图 1555dbd67766 / 第 1 页 / 页 2 D1-D2，U5 GD25Q128/W25Q128/128Mbit/3.3V

## 射频

### SX1262 差分接收与单端发射切换

U2 0900FM15K0039 的 RFO 端接 SX_RFO，RFI_P/RFI_N 接 SX_RFI_P/N，SW_RFO 输出 SX_SRFO，SW_RFI 输出 SX_SRFI；U3 FM8625H 在 SX_SRFO 与 SX_SRFI_T 之间选择并通过 RFC 接 LoRa 天线，CTRL 由 SX_DIO2 经 R9 100Ω 驱动。

- 参数与网络：`transmit_net=SX_SRFO`；`receive_net=SX_SRFI_T`；`switch_control=SX_DIO2`
- 证据：图 82e3d6f9ae74 / 第 1 页 / 页 1 A1-C4，U1/U2/U3 射频网络与 SX_DIO2

### LoRa 接收 LNA 与电源控制

U8 SGM13005L4 的 IN 接 SX_SRFI_T，RFOUT 输出 SX_SRFI，EN 接 SX_LNA_EN，VDD 由 VDD_3V3 经 L8 MLG0603P24NHTZ10 供电；SX_LNA_EN 由 PI4IOE5V6408 P5 控制。

- 参数与网络：`lna=SGM13005L4`；`enable=SX_LNA_EN`；`expander_pin=P5`
- 证据：图 82e3d6f9ae74 / 第 1 页 / 页 1 C3，U8/L7/L8/C44; 图 1555dbd67766 / 第 1 页 / 页 2 C2-C3，U7 P5=SX_LNA_EN

### LoRa IPEX4 天线与匹配保护

U3 RFC 通过 C1 39pF、L3 0R 与预留 C2/C3 NC 接到 J1 IPEX4，D1 H3V3U10B 对地保护；路径多处标注 RF_50R。

- 参数与网络：`connector=IPEX4`；`impedance_ohm=50`；`esd=H3V3U10B`
- 证据：图 82e3d6f9ae74 / 第 1 页 / 页 1 B3-B4，U3 RFC、C1-C3、L3、D1 与 J1

### ESP32-C6 IPEX4 天线匹配

U4 ANT 输出 ESP_ANT，经 C20 2.0pF、L4 2.4nH、C21 1.8pF、L6 1.5pF 与 C38 3.5nH 匹配网络形成 ESP_ANT_T，D2 H3V3U10B 对地保护后连接 J2 IPEX4；路径标注 RF_50R。

- 参数与网络：`connector=IPEX4`；`impedance_ohm=50`；`esd=H3V3U10B`
- 证据：图 1555dbd67766 / 第 1 页 / 页 2 A3-A4，ESP_ANT/C20/L4/C21/L6/C38/D2/J2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp C6LoRa 三页架构 | `schematic_revision=v0.2.3`；`schematic_date=2025-12-02`；`page_count=3` |
| 电源 | VBAT_IN 到 VDD_3V3 | `input=VBAT_IN`；`internal_input=VBAT`；`output=VDD_3V3`；`enable=MODULE_EN` |
| 电源 | BAT 与 VDD_3V3 外部供电范围 | `documented_bat_range_v=3.7-5`；`documented_direct_rail_v=3.3`；`documented_bat_enable=MODULE_EN high` |
| 电源 | SX1262 电源与内部稳压网络 | `main_supply=VDD_3V3`；`regulator_net=SX_VREG`；`pa_supply=SX_PAVDD`；`clock_supply=VDD_OCXO` |
| 存储 | 128Mbit 外部 SPI Flash | `capacity_mbit=128`；`capacity_mb=16`；`supply_v=3.3` |
| 时钟 | ESP32-C6 40MHz 晶振 | `frequency_mhz=40`；`tolerance_ppm=10`；`load_pf=20` |
| 时钟 | ESP32-C6 XTAL_32K_P/N 晶体 | `network=XTAL_32K_P/N`；`parallel_resistor_ohm=1000000`；`load_capacitor_pf=6` |
| 时钟 | SX1262 32MHz 有源参考 | `reference_net=SX_32M_REF`；`supply=VDD_OCXO`；`annotated_supply_v=3.0` |
| 总线 | ESP32-C6 到 SX1262 SPI 与状态线 | `sck_gpio=20`；`mosi_gpio=21`；`miso_gpio=22`；`nss_gpio=23`；`busy_gpio=19` |
| GPIO 与控制信号 | SX1262 DIO1/LORA_IRQ 到 ESP32-C6 GPIO7 | `documented_gpio=7`；`sx1262_net=LORA_IRQ`；`esp32_net=GPIO7` |
| 总线 | PI4IOE5V6408 I2C 控制 | `scl_gpio=8`；`sda_gpio=10`；`interrupt_gpio=3`；`address_pin=GND` |
| GPIO 与控制信号 | PI4IOE5V6408 P0-P7 映射 | `p0=EXT_P0`；`p1=EXT_P1`；`p2=EXT_P2`；`p3=EXT_P3`；`p4=EXT_P4`；`p5=SX_LNA_EN`；`p6=SX_ANT_SW`；`p7=SX_NRST` |
| 复位 | ESP_nRST 与 LoRa 复位控制 | `system_reset=ESP_nRST`；`lora_reset=SX_NRST`；`lora_reset_expander_pin=P7` |
| 射频 | SX1262 差分接收与单端发射切换 | `transmit_net=SX_SRFO`；`receive_net=SX_SRFI_T`；`switch_control=SX_DIO2` |
| 射频 | LoRa 接收 LNA 与电源控制 | `lna=SGM13005L4`；`enable=SX_LNA_EN`；`expander_pin=P5` |
| 射频 | LoRa IPEX4 天线与匹配保护 | `connector=IPEX4`；`impedance_ohm=50`；`esd=H3V3U10B` |
| 射频 | LoRa 频段、发射功率与灵敏度 | `documented_frequency_mhz=850-960`；`documented_tx_power_dbm=22`；`documented_sensitivity_dbm=-148` |
| 射频 | ESP32-C6 IPEX4 天线匹配 | `connector=IPEX4`；`impedance_ohm=50`；`esd=H3V3U10B` |
| 射频 | 2.4GHz Wi-Fi 6 能力 | `documented_frequency_ghz=2.4`；`documented_protocol=Wi-Fi 6` |
| 接口 | ESP32-C6 USB 与 UART 下载接口网络 | `usb_dm_gpio=12`；`usb_dp_gpio=13`；`uart_tx=ESP_U0TXD`；`uart_rx=ESP_U0RXD` |

## 待确认事项

- `power.documented-input-ranges`：正文称 BAT 支持 DC 3.7–5V，且仅 BAT 供电时需拉高 MODULE_EN；VDD_3V3 支持直接 DC 3.3V 输入。原理图显示 VBAT_IN、MODULE_EN、U6 和 VDD_3V3，但没有外部引脚、允许电压范围、反灌保护或直接 3.3V 供电边界标注。（证据：图 5dc352ecc789 / 第 1 页 / 页 3，VBAT_IN/MODULE_EN/U6/VDD_3V3，无电压范围标注）
- `gpio.lora-irq-mapping`：正文把 SX1262 IRQ 映射到 ESP32-C6 GPIO7；原理图第一页只把 U1 DIO1 命名为 LORA_IRQ，第二页 U4 GPIO7 只命名 GPIO7，两个页面没有同名网络或直接连线，当前无法确认这条内部映射。（证据：图 82e3d6f9ae74 / 第 1 页 / 页 1 B1，U1 DIO1=LORA_IRQ; 图 1555dbd67766 / 第 1 页 / 页 2 B1-C2，U4 GPIO7 仅标 GPIO7）
- `rf.documented-lora-performance`：正文称 LoRa 工作于 850–960MHz，最大发射功率 +22dBm、最大灵敏度 -148dBm；三页原理图确认 SX1262、SGM13005L4 和 50Ω 射频前端，但没有频段、功率、灵敏度、匹配目标或测试条件标注。（证据：图 82e3d6f9ae74 / 第 1 页 / 页 1 SX1262、RF 开关、LNA 与 RF_50R 链路，无频段/功率/灵敏度标注）
- `rf.documented-wifi6`：正文称 ESP32-C6 支持 2.4GHz Wi-Fi 6；原理图确认 ESP32-C6 和独立 50Ω IPEX4 天线链路，但没有频段、协议版本、射频功率或认证条件标注。（证据：图 1555dbd67766 / 第 1 页 / 页 2 U4 ESP32-C6 与 J2 IPEX4 RF_50R 链路，无频段/协议标注）
- `review.input-ranges`：Stamp C6LoRa 的 BAT 与 VDD_3V3 外部供电范围及反灌边界是否与正文一致；原因：原理图只显示 VBAT_IN 经 U6 到 VDD_3V3，未显示外部引脚范围、直接 3.3V 供电和保护边界。
- `review.lora-irq-mapping`：SX1262 DIO1/LORA_IRQ 是否在模组内部连接 ESP32-C6 GPIO7；原因：正文给出 GPIO7，但两张原理图分别使用 LORA_IRQ 和 GPIO7，不存在同名网络或直接连线。
- `review.lora-performance`：量产 Stamp C6LoRa 在 850–960MHz 的 +22dBm 发射功率和 -148dBm 灵敏度测试条件是什么；原因：原理图未标频段、功率、灵敏度、匹配目标、LoRa 调制参数或测试条件。
- `review.wifi6-spec`：ESP32-C6 在该模组上的 2.4GHz Wi-Fi 6 能力与射频认证边界是否已由对应 datasheet 和测试确认；原因：原理图只显示 ESP32-C6 和 50Ω 天线链路，没有协议、频率或认证参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `82e3d6f9ae74de7321fb0964e7e2f398210887f2fbb077049ae810824ae1b64a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012-SCH_Sch_M5_C6_Lora_v0.2.3_2025_12_02_19_14_35_page_01.png` |
| 2 | 1 | `1555dbd67766bda8f2e01581410470bef192b199ec067db37360cab6757bfe22` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012-SCH_Sch_M5_C6_Lora_v0.2.3_2025_12_02_19_14_35_page_02.png` |
| 3 | 1 | `5dc352ecc7892c933c4490929480ab92c7ae1b50c650163fb3ab90268f855c64` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/S012-SCH_Sch_M5_C6_Lora_v0.2.3_2025_12_02_19_14_35_page_03.png` |

---

源文档：`zh_CN/core/Stamp_C6LoRa.md`

源文档 SHA-256：`53fa875ed26e1f57470dc214477b6a78285987b6eca5358b6249686b88f0b01d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
