# Stamp-S3A PIN1.27 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-S3A PIN1.27 |
| SKU | S007-PIN127-V033 |
| 产品 ID | `stamp-s3a-pin1-27-5dd833869320` |
| 源文档 | `zh_CN/core/Stamp-S3A_PIN127.md` |

## 概述

Stamp-S3A PIN1.27 以 U1 ESP32-S3FN8 为主控，连接 40MHz 晶振、板载天线、原生 USB、WS2812、GPIO0 用户按键和 SPI LCD 接口。VIN_5V 经 U4 JW5712 降压为 VDD_3V3，U2 AW35122FDR 再由 GPIO38/DISP_BL 控制 BL_3V3，同时为 LCD 背光和 RGB LED 供电。M1 引出 28 个电源与信号焊盘，J1/J3 提供 12P/8P LCD FPC 接口。

## 检索关键词

`Stamp-S3A PIN1.27`、`S007-PIN127-V033`、`ESP32-S3FN8`、`JW5712`、`AW35122FDR`、`MWTC201608S2R2`、`WS2812`、`STAMP-S3M`、`40MHz`、`USB Type-C`、`USB_DU_P`、`USB_DU_N`、`USB_D_P`、`USB_D_N`、`VIN_5V`、`VDD_3V3`、`BL_3V3`、`ESP_EN`、`GPIO0`、`GPIO21 SK_DIN`、`GPIO38 DISP_BL`、`DISP_RST`、`DISP_RS`、`DISP_MOSI`、`DISP_SCK`、`DISP_CS`、`GPIO33`、`GPIO34`、`GPIO35`、`GPIO36`、`GPIO37`、`GPIO46`、`UART TX RX`、`HDGC/0.5K-HX-8PWB/NC`、`HDGC/0.5K-HX-12PWB/NC`、`PESDNC2FD3V3B`、`PESDNC2FD5VB`、`6V/1A/PPTC`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-S3FN8 | 主控 SoC，连接射频、USB、RGB LED、用户按键、LCD 和外部 GPIO | 图 1156e645de35 / 第 1 页 / 第1页网格 A2-C2：U1 ESP32-S3FN8 及 GPIO/电源引脚 |
| U4 | JW5712 | VIN_5V 到 VDD_3V3 的降压转换器 | 图 1156e645de35 / 第 1 页 / 第1页网格 D1-D2：DCDC 区 U4 JW5712 |
| L4 | MWTC201608S2R2 | U4 开关节点到 VDD_3V3 的降压储能电感 | 图 1156e645de35 / 第 1 页 / 第1页网格 D2：L4，标注 MWTC201608S2R2 |
| U2 | AW35122FDR | 由 DISP_BL 控制的 VDD_3V3 到 BL_3V3 负载开关 | 图 1156e645de35 / 第 1 页 / 第1页网格 A3：LCD 区 U2 AW35122FDR |
| U3 | WS2812 | 由 GPIO21/SK_DIN 驱动、BL_3V3 供电的可编程 RGB LED | 图 1156e645de35 / 第 1 页 / 第1页网格 B3-B4：RGB LED 区 U3 WS2812 |
| X1 | 40MHz | ESP32-S3 主时钟晶体 | 图 1156e645de35 / 第 1 页 / 第1页网格 B1：X1 40MHz、L3、C9、C14 |
| ANT1 | 未标注 | 经匹配网络连接 U1 LNA_IN 的板载射频天线 | 图 1156e645de35 / 第 1 页 / 第1页网格 A1：ANT1 与 L6/C19/C20/L1/C2/C1 匹配网络 |
| S1 | SMT_SW_1TS026A | 按下时将 GPIO0 拉到 GND 的用户/启动按键 | 图 1156e645de35 / 第 1 页 / 第1页网格 C3：BTN-USER 区 S1 |
| J2 | USB-TYPEC | 原生 USB 数据接口和 5V 电源输入 | 图 1156e645de35 / 第 1 页 / 第1页网格 D3-D4：Type-A USB 区 J2 USB-TYPEC |
| J3 | HDGC/0.5K-HX-8PWB/NC | 8 针 LCD 背光、电源、SPI 和控制信号 FPC 接口 | 图 1156e645de35 / 第 1 页 / 第1页网格 A3-A4：J3 pins1-8 |
| J1 | HDGC/0.5K-HX-12PWB/NC | 12 针 LCD 与 GPIO16-GPIO18、VIN_5V FPC 接口 | 图 1156e645de35 / 第 1 页 / 第1页网格 A4：J1 pins1-12 |
| M1 | STAMP-S3M | 模组 28 针电源、控制、UART 和 GPIO 外部接口 | 图 1156e645de35 / 第 1 页 / 第1页网格 C3-C4：M1 STAMP-S3M pins1-28 |
| F1 | 6V/1A/PPTC | USB VCC 到 VIN_5V 的自恢复保险丝 | 图 1156e645de35 / 第 1 页 / 第1页网格 D4：F1 6V/1A/PPTC |
| L5 | 未标注 | USB_DU_P/USB_DU_N 与连接器侧 USB_D_P/USB_D_N 之间的双线共模器件 | 图 1156e645de35 / 第 1 页 / 第1页网格 D3：USB 数据线上的 L5 |
| D1,D2,D3,D4,D14 | PESDNC2FD3V3B / PESDNC2FD5VB | GPIO0、VDD_3V3、USB D+/D- 和 VIN_5V 的瞬态保护器件 | 图 1156e645de35 / 第 1 页 / 第1页 C3/C4/D3/D4：D1/D2/D3/D4 PESDNC2FD3V3B 与 D14 PESDNC2FD5VB |

## 系统结构

### Stamp-S3A PIN1.27 架构

U1 ESP32-S3FN8 连接板载天线、40MHz 晶体、原生 USB、WS2812、GPIO0 按键和 SPI LCD；U4 生成 VDD_3V3，U2 生成受控 BL_3V3，M1/J1/J3 引出外部接口。

- 参数与网络：`soc=U1 ESP32-S3FN8`；`power=U4 JW5712`；`backlight_switch=U2 AW35122FDR`；`rgb=U3 WS2812`；`external_interfaces=M1,J1,J2,J3`
- 证据：图 1156e645de35 / 第 1 页 / 第1页完整单页系统分区：ESP32/LCD/RGB LED/BTN-USER/DCDC/USB

## 电源

### VIN_5V 到 VDD_3V3

U4 JW5712 的 VIN 接 VIN_5V，EN 由 R16 100KΩ 上拉到 VIN_5V；SW 经 L4 MWTC201608S2R2 输出 VDD_3V3，VOS 采样 VDD_3V3。图中标注输出电流 0~0.6A。

- 参数与网络：`converter=U4 JW5712`；`input=VIN_5V`；`enable_pullup=R16 100KΩ to VIN_5V`；`inductor=L4 MWTC201608S2R2`；`output=VDD_3V3`；`output_current=0~0.6A`；`input_caps=C16 10uF/10V; C18 100nF/25V`；`output_caps=C21/C22/C25 10uF/10V`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 D1-D2：U4/R16/L4/C16/C18/C21/C22/C25

### USB 5V 输入

J2 的 VCC 经 F1 6V/1A/PPTC 形成 VIN_5V；CC1、CC2 分别由 R1、R2 5.1KΩ 下拉，D14 PESDNC2FD5VB 对 VIN_5V 提供保护。

- 参数与网络：`connector=J2 USB-TYPEC`；`vbus_path=J2 VCC -> F1 -> VIN_5V`；`fuse=F1 6V/1A/PPTC`；`cc1=R1 5.1KΩ to GND`；`cc2=R2 5.1KΩ to GND`；`vbus_esd=D14 PESDNC2FD5VB`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 D4：J2/F1/R1/R2/D14

### LCD 背光与 RGB 复用电源

U2 AW35122FDR 的 VIN 接 VDD_3V3，EN 接 DISP_BL，VOUT 形成 BL_3V3；BL_3V3 同时连接 J3 pin8 和 U3 WS2812 VDD，C17 10uF/10V 对地。

- 参数与网络：`switch=U2 AW35122FDR`；`input=VDD_3V3`；`enable=DISP_BL / GPIO38`；`output=BL_3V3`；`loads=J3 pin8; U3 VDD pin4`；`output_cap=C17 10uF/10V`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 A3-B4：U2 VOUT/BL_3V3、J3 pin8、U3 VDD/C17

### ESP32-S3 电源轨与去耦

U1 的 VDD3P3、VDD3P3_RTC、VDD3P3_CPU、VDDA1、VDDA2 接 VDD_3V3；VDD3P3 支路含 L2 2nH，并配置 C5-C8、C10-C13 去耦，VDD_SPI 使用独立 FLASH_VCC 标号。

- 参数与网络：`main_rail=VDD_3V3`；`soc_domains=VDD3P3,VDD3P3_RTC,VDD3P3_CPU,VDDA1,VDDA2`；`filter=L2 2nH`；`decoupling=C5,C6,C7,C8,C10,C11,C12,C13`；`flash_rail=FLASH_VCC`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 B1-C2：U1 电源 pins2/3/20/46/55/56 与 L2/C5-C13

## 接口

### J3 8P LCD 接口

J3 pins1-8 依次为 DISP_CS、VDD_3V3、DISP_SCK、DISP_MOSI、DISP_RS、DISP_RST、GND、BL_3V3。

- 参数与网络：`connector=J3 HDGC/0.5K-HX-8PWB/NC`；`pin1=DISP_CS`；`pin2=VDD_3V3`；`pin3=DISP_SCK`；`pin4=DISP_MOSI`；`pin5=DISP_RS`；`pin6=DISP_RST`；`pin7=GND`；`pin8=BL_3V3`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 A3-A4：J3 PIN1-PIN8

### J1 12P LCD/GPIO 接口

J1 pins1-12 依次为 GND、DISP_CS、NC、DISP_SCK、DISP_MOSI、DISP_RS、DISP_RST、NC、GPIO16、GPIO17、GPIO18、VIN_5V。

- 参数与网络：`connector=J1 HDGC/0.5K-HX-12PWB/NC`；`pin1=GND`；`pin2=DISP_CS`；`pin3=NC`；`pin4=DISP_SCK`；`pin5=DISP_MOSI`；`pin6=DISP_RS`；`pin7=DISP_RST`；`pin8=NC`；`pin9=GPIO16`；`pin10=GPIO17`；`pin11=GPIO18`；`pin12=VIN_5V`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 A4：J1 pins1-12

### M1 STAMP-S3M 28 针接口

M1 pins1-17 引出 GPIO1-GPIO10、GND、VIN_5V、GPIO11-GPIO15；pins18-28 引出 GND、GPIO39、GPIO0、GPIO40、EN、GPIO41、RX、GPIO42、TX、GPIO46、VDD_3V3。

- 参数与网络：`pins1_10=GPIO1,GPIO2,GPIO3,GPIO4,GPIO5,GPIO6,GPIO7,GPIO8,GPIO9,GPIO10`；`pin11=GND`；`pin12=VIN_5V`；`pins13_17=GPIO11,GPIO12,GPIO13,GPIO14,GPIO15`；`pins18_28=GND,GPIO39,GPIO0,GPIO40,EN,GPIO41,RX,GPIO42,TX,GPIO46,VDD_3V3`；`logic_level=VDD_3V3`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 C3-C4：M1 pins1-28

## 总线

### ESP32-S3 原生 USB

U1 GPIO20 pin26 为 USB_DU_P、GPIO19 pin25 为 USB_DU_N，两线经 L5 后成为连接器侧 USB_D_P/USB_D_N，并分别连接 J2 的 DP1/DP2 和 DN1/DN2。

- 参数与网络：`controller_dp=U1 GPIO20 pin26 / USB_DU_P`；`controller_dm=U1 GPIO19 pin25 / USB_DU_N`；`filter=L5`；`connector_dp=USB_D_P -> J2 A6/B6`；`connector_dm=USB_D_N -> J2 A7/B7`；`direction=bidirectional`
- 证据：图 1156e645de35 / 第 1 页 / 第1页 U1 pins25-26 与网格 D3-D4 L5/J2

### LCD SPI 与控制信号

U1 GPIO35、GPIO36、GPIO37 分别形成 DISP_MOSI、DISP_SCK、DISP_CS，GPIO33、GPIO34 分别形成 DISP_RST、DISP_RS，GPIO38 形成 DISP_BL；这些网络连接 J3，并除 DISP_BL 外连接 J1。

- 参数与网络：`controller=U1 ESP32-S3FN8`；`mosi=GPIO35 / DISP_MOSI / J3 pin4 / J1 pin5`；`sck=GPIO36 / DISP_SCK / J3 pin3 / J1 pin4`；`cs=GPIO37 / DISP_CS / J3 pin1 / J1 pin2`；`reset=GPIO33 / DISP_RST / J3 pin6 / J1 pin7`；`data_command=GPIO34 / DISP_RS / J3 pin5 / J1 pin6`；`backlight_enable=GPIO38 / DISP_BL`；`logic_rail=VDD_3V3`；`direction=MOSI/SCK/CS/RS/RST/BL are controller outputs`
- 证据：图 1156e645de35 / 第 1 页 / 第1页 U1 pins38-43 GPIO33-GPIO38 与网格 A3-A4 J3/J1

## GPIO 与控制信号

### GPIO0 用户/启动按键

S1 按下时将 GPIO0 接地；R4 10KΩ 将 GPIO0 上拉到 VDD_3V3，D1 PESDNC2FD3V3B 从 GPIO0 对地保护。GPIO0 同时引到 M1 pin20。

- 参数与网络：`gpio=GPIO0`；`switch=S1 SMT_SW_1TS026A`；`active_level=low`；`pullup=R4 10KΩ to VDD_3V3`；`esd=D1 PESDNC2FD3V3B`；`external_pin=M1 pin20 G0/Boot`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 C3：S1/R4/D1 与 M1 pin20 G0/Boot

### WS2812 控制

U1 GPIO21 pin27 形成 SK_DIN 并连接 U3 DI pin3；U3 DO pin1 为 SK_DOUT，U3 由受 DISP_BL/GPIO38 控制的 BL_3V3 供电。

- 参数与网络：`controller=U1 GPIO21 pin27`；`data_in=SK_DIN -> U3 DI pin3`；`data_out=U3 DO pin1 -> SK_DOUT`；`supply=BL_3V3`；`supply_enable=U1 GPIO38 / DISP_BL`
- 证据：图 1156e645de35 / 第 1 页 / 第1页 U1 GPIO21/GPIO38 与网格 B3-B4 U3

### 启动相关 GPIO 引出

GPIO0 连接低有效按键并从 M1 pin20 以 G0/Boot 引出；GPIO46 从 U1 pin52 引到 M1 pin27，并在 M1 标为 G46。

- 参数与网络：`gpio0=U1 GPIO0 pin5; S1; M1 pin20 G0/Boot`；`gpio46=U1 GPIO46 pin52; M1 pin27 G46`
- 证据：图 1156e645de35 / 第 1 页 / 第1页 U1 GPIO0/GPIO46 与 M1 pins20/27

## 时钟

### 40MHz 主时钟

X1 40MHz 连接 U1 XTAL_P pin54 与 XTAL_N pin53；XTAL_P 支路串 L3 10nH，C9 与 C14 各 12pF 对地。

- 参数与网络：`crystal=X1 40MHz`；`positive=U1 XTAL_P pin54`；`negative=U1 XTAL_N pin53`；`series=L3 10nH`；`load_caps=C9 12pF; C14 12pF`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 B1-B2：X1/L3/C9/C14 与 U1 pins53-54

## 复位

### ESP_EN 复位使能网络

U1 CHIP_PU pin4 经 L7 0Ω连接 ESP_EN；C24 3pF 从 CHIP_PU 侧对地，ESP_EN 由 R7 10KΩ 上拉到 VDD_3V3，并由 C23 1uF 对地。

- 参数与网络：`soc_pin=U1 CHIP_PU pin4`；`net=ESP_EN`；`series=L7 0Ω`；`chip_pu_cap=C24 3pF`；`pullup=R7 10KΩ to VDD_3V3`；`reset_cap=C23 1uF to GND`；`external_alias=EN`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 A2 U1 CHIP_PU/L7/C24 与网格 D1 R7/C23 ESP_EN

## 保护电路

### USB 数据与电源保护

D3、D4 PESDNC2FD3V3B 分别保护 USB_D_P、USB_D_N，D14 PESDNC2FD5VB 保护 VIN_5V，F1 提供 USB VCC 输入过流保护。

- 参数与网络：`data_esd=D3/D4 PESDNC2FD3V3B`；`power_esd=D14 PESDNC2FD5VB`；`overcurrent=F1 6V/1A/PPTC`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 D3-D4：D3/D4/D14/F1

### 外部电源轨与按键网络保护

D1 PESDNC2FD3V3B 从 GPIO0 对地，D2 PESDNC2FD3V3B 从 M1 的 VDD_3V3 对地，分别保护用户按键网络和 3.3V 外部电源轨。

- 参数与网络：`gpio0_esd=D1 PESDNC2FD3V3B`；`vdd3v3_esd=D2 PESDNC2FD3V3B`；`protected_connector=M1`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 C3-C4：D1、D2 PESDNC2FD3V3B

## 内存与 Flash

### ESP32-S3FN8 存储连接可见性

U1 标为 ESP32-S3FN8，VDD_SPI pin29 接 FLASH_VCC 并由 C26 100nF/25V、C4 1uF/10V 去耦；SPIHD、SPIWP、SPICS0、SPICLK、SPIQ、SPID pins30-35 均标为未连接，图中没有独立外部 Flash 或 PSRAM。

- 参数与网络：`soc=U1 ESP32-S3FN8`；`flash_rail=FLASH_VCC`；`decoupling=C26 100nF/25V; C4 1uF/10V`；`external_flash_shown=false`；`external_psram_shown=false`；`unconnected_pins=U1 pins30-35 SPIHD/SPIWP/SPICS0/SPICLK/SPIQ/SPID`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 A2：U1 pin29-pins35、FLASH_VCC、C26/C4

## 射频

### 板载天线与匹配

ANT1 经 L6/C19/C20/L1/C2/C1 构成的匹配网络连接 U1 LNA_IN；图中明确标出 L1 2.2nH、C19 4.3nH、C20 NC、C2 2.2pF、C1 1.8pF。

- 参数与网络：`antenna=ANT1`；`soc_pin=U1 LNA_IN pin1`；`network=L6,C19,C20,L1,C2,C1`；`L1=2.2nH`；`C19=4.3nH`；`C20=NC`；`C2=2.2pF`；`C1=1.8pF`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 A1-A2：ANT1 到 U1 LNA_IN 的 L6/C19/C20/L1/C2/C1 网络

## 调试与烧录

### UART0 TX/RX 引出

U1 U0TXD pin49 经 R5 510Ω/1% 形成 TX 并连接 M1 pin26；U1 U0RXD pin50 形成 RX 并连接 M1 pin24。M1 标注 TX 为 G43/Tx、RX 为 G44/Rx。

- 参数与网络：`tx=U1 U0TXD pin49 -> R5 510Ω/1% -> TX -> M1 pin26 G43/Tx`；`rx=U1 U0RXD pin50 -> RX -> M1 pin24 G44/Rx`；`logic_level=VDD_3V3`；`direction=TX output; RX input`
- 证据：图 1156e645de35 / 第 1 页 / 第1页网格 C2 U1 pins49-50/R5 与网格 C4 M1 pins24/26

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-S3A PIN1.27 架构 | `soc=U1 ESP32-S3FN8`；`power=U4 JW5712`；`backlight_switch=U2 AW35122FDR`；`rgb=U3 WS2812`；`external_interfaces=M1,J1,J2,J3` |
| 电源 | VIN_5V 到 VDD_3V3 | `converter=U4 JW5712`；`input=VIN_5V`；`enable_pullup=R16 100KΩ to VIN_5V`；`inductor=L4 MWTC201608S2R2`；`output=VDD_3V3`；`output_current=0~0.6A`；`input_caps=C16 10uF/10V; C18 100nF/25V`；`output_caps=C21/C22/C25 10uF/10V` |
| 电源 | USB 5V 输入 | `connector=J2 USB-TYPEC`；`vbus_path=J2 VCC -> F1 -> VIN_5V`；`fuse=F1 6V/1A/PPTC`；`cc1=R1 5.1KΩ to GND`；`cc2=R2 5.1KΩ to GND`；`vbus_esd=D14 PESDNC2FD5VB` |
| 电源 | LCD 背光与 RGB 复用电源 | `switch=U2 AW35122FDR`；`input=VDD_3V3`；`enable=DISP_BL / GPIO38`；`output=BL_3V3`；`loads=J3 pin8; U3 VDD pin4`；`output_cap=C17 10uF/10V` |
| 总线 | ESP32-S3 原生 USB | `controller_dp=U1 GPIO20 pin26 / USB_DU_P`；`controller_dm=U1 GPIO19 pin25 / USB_DU_N`；`filter=L5`；`connector_dp=USB_D_P -> J2 A6/B6`；`connector_dm=USB_D_N -> J2 A7/B7`；`direction=bidirectional` |
| 保护电路 | USB 数据与电源保护 | `data_esd=D3/D4 PESDNC2FD3V3B`；`power_esd=D14 PESDNC2FD5VB`；`overcurrent=F1 6V/1A/PPTC` |
| 时钟 | 40MHz 主时钟 | `crystal=X1 40MHz`；`positive=U1 XTAL_P pin54`；`negative=U1 XTAL_N pin53`；`series=L3 10nH`；`load_caps=C9 12pF; C14 12pF` |
| 射频 | 板载天线与匹配 | `antenna=ANT1`；`soc_pin=U1 LNA_IN pin1`；`network=L6,C19,C20,L1,C2,C1`；`L1=2.2nH`；`C19=4.3nH`；`C20=NC`；`C2=2.2pF`；`C1=1.8pF` |
| 复位 | ESP_EN 复位使能网络 | `soc_pin=U1 CHIP_PU pin4`；`net=ESP_EN`；`series=L7 0Ω`；`chip_pu_cap=C24 3pF`；`pullup=R7 10KΩ to VDD_3V3`；`reset_cap=C23 1uF to GND`；`external_alias=EN` |
| GPIO 与控制信号 | GPIO0 用户/启动按键 | `gpio=GPIO0`；`switch=S1 SMT_SW_1TS026A`；`active_level=low`；`pullup=R4 10KΩ to VDD_3V3`；`esd=D1 PESDNC2FD3V3B`；`external_pin=M1 pin20 G0/Boot` |
| GPIO 与控制信号 | WS2812 控制 | `controller=U1 GPIO21 pin27`；`data_in=SK_DIN -> U3 DI pin3`；`data_out=U3 DO pin1 -> SK_DOUT`；`supply=BL_3V3`；`supply_enable=U1 GPIO38 / DISP_BL` |
| 总线 | LCD SPI 与控制信号 | `controller=U1 ESP32-S3FN8`；`mosi=GPIO35 / DISP_MOSI / J3 pin4 / J1 pin5`；`sck=GPIO36 / DISP_SCK / J3 pin3 / J1 pin4`；`cs=GPIO37 / DISP_CS / J3 pin1 / J1 pin2`；`reset=GPIO33 / DISP_RST / J3 pin6 / J1 pin7`；`data_command=GPIO34 / DISP_RS / J3 pin5 / J1 pin6`；`backlight_enable=GPIO38 / DISP_BL`；`logic_rail=VDD_3V3`；`direction=MOSI/SCK/CS/RS/RST/BL are controller outputs` |
| 接口 | J3 8P LCD 接口 | `connector=J3 HDGC/0.5K-HX-8PWB/NC`；`pin1=DISP_CS`；`pin2=VDD_3V3`；`pin3=DISP_SCK`；`pin4=DISP_MOSI`；`pin5=DISP_RS`；`pin6=DISP_RST`；`pin7=GND`；`pin8=BL_3V3` |
| 接口 | J1 12P LCD/GPIO 接口 | `connector=J1 HDGC/0.5K-HX-12PWB/NC`；`pin1=GND`；`pin2=DISP_CS`；`pin3=NC`；`pin4=DISP_SCK`；`pin5=DISP_MOSI`；`pin6=DISP_RS`；`pin7=DISP_RST`；`pin8=NC`；`pin9=GPIO16`；`pin10=GPIO17`；`pin11=GPIO18`；`pin12=VIN_5V` |
| 接口 | M1 STAMP-S3M 28 针接口 | `pins1_10=GPIO1,GPIO2,GPIO3,GPIO4,GPIO5,GPIO6,GPIO7,GPIO8,GPIO9,GPIO10`；`pin11=GND`；`pin12=VIN_5V`；`pins13_17=GPIO11,GPIO12,GPIO13,GPIO14,GPIO15`；`pins18_28=GND,GPIO39,GPIO0,GPIO40,EN,GPIO41,RX,GPIO42,TX,GPIO46,VDD_3V3`；`logic_level=VDD_3V3` |
| 调试与烧录 | UART0 TX/RX 引出 | `tx=U1 U0TXD pin49 -> R5 510Ω/1% -> TX -> M1 pin26 G43/Tx`；`rx=U1 U0RXD pin50 -> RX -> M1 pin24 G44/Rx`；`logic_level=VDD_3V3`；`direction=TX output; RX input` |
| GPIO 与控制信号 | 启动相关 GPIO 引出 | `gpio0=U1 GPIO0 pin5; S1; M1 pin20 G0/Boot`；`gpio46=U1 GPIO46 pin52; M1 pin27 G46` |
| 内存与 Flash | ESP32-S3FN8 存储连接可见性 | `soc=U1 ESP32-S3FN8`；`flash_rail=FLASH_VCC`；`decoupling=C26 100nF/25V; C4 1uF/10V`；`external_flash_shown=false`；`external_psram_shown=false`；`unconnected_pins=U1 pins30-35 SPIHD/SPIWP/SPICS0/SPICLK/SPIQ/SPID` |
| 内存与 Flash | 集成 Flash 容量 | `documented_capacity=8MB`；`schematic_part_number=ESP32-S3FN8`；`explicit_capacity_field_on_schematic=false` |
| 保护电路 | 外部电源轨与按键网络保护 | `gpio0_esd=D1 PESDNC2FD3V3B`；`vdd3v3_esd=D2 PESDNC2FD3V3B`；`protected_connector=M1` |
| 电源 | ESP32-S3 电源轨与去耦 | `main_rail=VDD_3V3`；`soc_domains=VDD3P3,VDD3P3_RTC,VDD3P3_CPU,VDDA1,VDDA2`；`filter=L2 2nH`；`decoupling=C5,C6,C7,C8,C10,C11,C12,C13`；`flash_rail=FLASH_VCC` |

## 待确认事项

- `memory.flash-capacity`：产品正文标称 8MB Flash；原理图仅打印 U1 料号 ESP32-S3FN8 和 FLASH_VCC，未另设容量字段。（证据：图 1156e645de35 / 第 1 页 / 第1页网格 A2-C2：U1 ESP32-S3FN8 与 FLASH_VCC）
- `review.flash-capacity`：S007-PIN127-V033 的 U1 集成 Flash 容量是否应作为 8MB 原理图确定事实？；原因：8MB 来自产品正文；原理图只显示 ESP32-S3FN8 料号和 FLASH_VCC，没有独立容量字段。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1156e645de35fe68e6458e9131657c8f02045bbcd14f97ab190bb1486ee7a1c5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3_page_01.png` |

---

源文档：`zh_CN/core/Stamp-S3A_PIN127.md`

源文档 SHA-256：`5b126a0bd8ac5088ba5f79cc675def1a4c8bb9d1238f92ab17208784e1a37b89`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
