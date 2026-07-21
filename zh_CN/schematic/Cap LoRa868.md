# Cap LoRa868 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Cap LoRa868 |
| SKU | U201 |
| 产品 ID | `cap-lora868-cadd64e8b186` |
| 源文档 | `zh_CN/cap/Cap_LoRa868.md` |

## 概述

Cap LoRa868 主板通过 P1 14 Pin Cap-Bus 接入外部主机，M1 LoRa1262 使用 GPIO40/14/39/5 SPI 与 GPIO3/4/6 复位、中断和忙信号，M2 GP-02 通过 GPIO13/15 UART 提供 GNSS。+5VOUT 经 U3 JW5712 生成 VDD_3V3，再向 LoRa 模组、GNSS 模组和 MAX2659 GNSS LNA 供电；LoRa 连接 E4 SMA-KE，GNSS 经 MAX2659 和 J1 ANT181804 陶瓷天线接收。第二张页面展开 SX1262、32MHz 有源时钟、868M 发射/接收匹配、FM8625H RF 开关和可选接收 LNA，但该页文件名标为 OLD-868/V0.1，其与当前量产模块的修订关系需要确认。

## 检索关键词

`Cap LoRa868`、`U201`、`LoRa1262`、`SX1262`、`GP-02`、`MAX2659`、`JW5712`、`FM8625H`、`SGM13005LA`、`P14IOE5V6408ZTAEX`、`SMA-KE`、`ANT181804`、`868M`、`SPI`、`NSS GPIO5`、`SCK GPIO40`、`MOSI GPIO14`、`MISO GPIO39`、`RST GPIO3`、`IRQ GPIO4`、`BUSY GPIO6`、`GPS-RX GPIO13`、`GPS-TX GPIO15`、`+5VOUT`、`VDD_3V3`、`+3.3V`、`SX_RFO`、`SX_RFI_P`、`SX_RFI_N`、`PA_TX`、`PX_RX`、`RF_OUT`、`SX_DIO2`、`SX_32M_REF`、`VDD_OCXO`、`BT1 Battery`、`Cap-Bus`、`RP-SMA`、`GNSS UART`、`LoRa SPI`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | LoRa1262 | SX1262 LoRa Stamp 模组，连接 SPI、RESET/IRQ/BUSY、电源和外置 SMA 天线 | 图 479f1fb13612 / 第 1 页 / source_001 网格 A4-B4：M1 LoRa1262 pins1-12 与 ANT/3V3/BYPASS/SHUT DOWN/IRQ/BUSY/RST/SPI |
| U1 (Stamp) | SX1262 | LoRa 射频收发器，连接 SPI、DIO、32MHz 参考、内部电源和差分/单端 RF 网络 | 图 53862f11d5ee / 第 1 页 / source_002 网格 A1-B2：U1 SX1262 全部引脚 |
| M2 | GP-02 | GNSS 模组，连接 UART、VBAT/VCC、RF 天线输入和控制/扩展引脚 | 图 479f1fb13612 / 第 1 页 / source_001 网格 C2-D3：M2 GP-02 pins1-18 |
| U1 (Cap) | MAX2659 | GNSS 陶瓷天线到 GP-02 ANT 的低噪声放大器 | 图 479f1fb13612 / 第 1 页 / source_001 网格 C3：U1 MAX2659，RFIN/RFOUT/VCC/SHDN/GND |
| U3 | JW5712 | 把 +5VOUT 转换为 VDD_3V3 的 0-0.6A 开关稳压器 | 图 479f1fb13612 / 第 1 页 / source_001 网格 A1-A2：U3 JW5712、IOUT 0~0.6A、L2 与 VDD_3V3 |
| E4 | SMA-KE | LoRa1262 ANT 的外部 SMA 射频连接器 | 图 479f1fb13612 / 第 1 页 / source_001 网格 A3：E4 SMA-KE 到 M1 ANT 的 R2/可选保护匹配路径 |
| J1 (GNSS antenna) | ANT181804 | GNSS 内置陶瓷天线，经 L1/C5 接 MAX2659 RFIN | 图 479f1fb13612 / 第 1 页 / source_001 网格 C3-C4：J1 ANT181804、C5 470pF、L1 6.8nH 与 U1 RFIN |
| P1 | HDR-SMD_14P-P2.54 | 14 Pin Cap-Bus，连接 LoRa SPI/控制、GNSS UART、I2C 和 5V 电源 | 图 479f1fb13612 / 第 1 页 / source_001 网格 D3-D4：P1 pins1-14 及 GPIO/信号标签 |
| BT1 | Battery | 连接 GP-02 VBAT 的 GNSS 备用电池 | 图 479f1fb13612 / 第 1 页 / source_001 网格 D1-D2：BT1 Battery 到 M2 pin6 VBAT |
| U2/NC (Cap) | P14IOE5V6408ZTAEX | 未装的 I2C GPIO 扩展器选项，P0/P1 预连接 BYPASS/SHUT_DOWN | 图 479f1fb13612 / 第 1 页 / source_001 网格 B1-C2：U2/NC P14IOE5V6408ZTAEX、R5/R6/R7/C13/C14 均带 NC |
| X1 | X1G0041310042 | SX1262 的 32MHz 有源参考时钟源 | 图 53862f11d5ee / 第 1 页 / source_002 网格 C1-C2：X1 X1G0041310042、VDD 3.0V、C34/R3 与 SX_32M_REF |
| U2 (Stamp) | FM8625H | 由 SX_DIO2 控制的 LoRa 发射/接收 RF 开关 | 图 53862f11d5ee / 第 1 页 / source_002 网格 C3-C4：U2 FM8625H，RF1 PA_TX、RF2 PA_RX_SWC、RFC RF_OUT、CTRL SX_DIO2 |
| U4/NC | SGM13005LA/NC | 未装的可选接收 LNA 路径，位于 PX_RX 与 PA_RX_SWC 之间 | 图 53862f11d5ee / 第 1 页 / source_002 网格 D3：U4/NC SGM13005LA/NC 与 L6/L7/R6/C10/C13 NC |
| D1 (Stamp) | H3V3U10B | RF_OUT 到 GND 的射频口保护二极管 | 图 53862f11d5ee / 第 1 页 / source_002 网格 C4：RF_OUT 节点 D1 H3V3U10B 到 GND |
| L1-L3,C3,C4,C7,C8,C12,C14,C28,C33 | 868M RF matching network | SX1262 868M 发射与差分接收匹配网络 | 图 53862f11d5ee / 第 1 页 / source_002 网格 A3-B4：标注 868M 的 SX_RFO 到 PA_TX 及 SX_RFI_P/N 到 PX_RX 网络 |

## 系统结构

### Cap LoRa868 系统架构

P1 接入外部主机；U3 生成 3.3V，M1 LoRa1262 经 SPI/控制线和 E4 SMA 工作，M2 GP-02 经 UART、MAX2659 与陶瓷天线工作，第二页展开 M1 内部 SX1262 RF 电路。

- 参数与网络：`host=P1 Cap-Bus`；`power=+5VOUT -> U3 JW5712 -> VDD_3V3/+3.3V`；`lora=M1 LoRa1262 / internal U1 SX1262`；`lora_antenna=E4 SMA-KE`；`gnss=M2 GP-02`；`gnss_rf=J1 ANT181804 -> U1 MAX2659 -> M2 ANT`
- 证据：图 479f1fb13612 / 第 1 页 / source_001 完整 Cap 主板; 图 53862f11d5ee / 第 1 页 / source_002 完整 Stamp LoRa-1262 内部电路

### 未显示的系统功能

两张页面未画出通用主控、存储器、音频、环境传感器或专用 JTAG/SWD 调试连接器；控制由 P1 外部主机承担。

- 参数与网络：`general_mcu_shown=false`；`storage_shown=false`；`audio_shown=false`；`environment_sensor_shown=false`；`dedicated_debug_connector_shown=false`；`external_host=P1 Cap-Bus`
- 证据：图 479f1fb13612 / 第 1 页 / source_001 完整主板; 图 53862f11d5ee / 第 1 页 / source_002 完整 Stamp 内部页

## 核心器件

### 可选 I2C GPIO 扩展器

U2 P14IOE5V6408ZTAEX 及 R5/R6/R7/C13/C14 均标 NC；若装配，SCL/SDA 来自 P1 GPIO1/GPIO0，P0/P1 连接 BYPASS/SHUT_DOWN。

- 参数与网络：`reference=U2/NC`；`part=P14IOE5V6408ZTAEX`；`populated=false`；`i2c=SCL/SDA from P1 G1/G0`；`outputs=P0 BYPASS; P1 SHUT_DOWN`；`optional_support=R5/R6/R7/C13/C14 NC`
- 证据：图 479f1fb13612 / 第 1 页 / source_001 网格 B1-C2：U2/NC 及所有 NC 支持件

### SX1262 电源与内部稳压网络

SX1262 VDD_IN pin1、VBAT pin10 和 VBAT_IO pin11 接 VDD_3V3，VREG pin7 形成 SX_VREG，DCC_SW pin9 经 L5 FTW1608FE150/15uH/200mA 接 SX_VREG，VR_PA pin24 接 SX_PAVDD。

- 参数与网络：`input_supply=VDD_3V3 to pins1,10,11`；`regulated_net=pin7 VREG -> SX_VREG`；`dc_dc=pin9 DCC_SW -> L5 15uH/200mA -> SX_VREG`；`pa_supply=pin24 VR_PA -> SX_PAVDD`；`grounds=pins2,5,8,20,25`
- 证据：图 53862f11d5ee / 第 1 页 / source_002 网格 A1-B2：SX1262 VDD/VBAT/VREG/DCC_SW/VR_PA/L5/GND

## 电源

### +5VOUT 到 VDD_3V3

+5VOUT 接 U3 JW5712 VIN，R1 10KΩ 把 EN 上拉到 +5VOUT；SW 经 L2 MWTC201608S2R2 输出 VDD_3V3，页面标注 IOUT 0~0.6A。

- 参数与网络：`input=+5VOUT`；`converter=U3 JW5712`；`enable=R1 10KΩ to +5VOUT`；`inductor=L2 MWTC201608S2R2`；`output=VDD_3V3`；`annotated_output_current=0-0.6A`；`input_caps=C15 22uF; C16 100nF`；`output_caps=C2/C3/C4 22uF; C1 1nF`
- 证据：图 479f1fb13612 / 第 1 页 / source_001 网格 A1-A2：+5VOUT/R1/U3/L2/C1-C4/VDD_3V3

### GP-02 主电源与备用电池

M2 VCC pin8 经 FB3 120Ω/MB 接 +3.3V，并由 C8 22uF/C9 100nF 去耦；VBAT pin6 连接 BT1 Battery，ON/OFF pin5 通过 R3 10KΩ 上拉到 +3.3V。

- 参数与网络：`main_supply=+3.3V -> FB3 120Ω/MB -> M2 pin8 VCC`；`decoupling=C8 22uF; C9 100nF`；`backup=BT1 Battery -> M2 pin6 VBAT`；`on_off=M2 pin5 ON/OFF with R3 10KΩ to +3.3V`
- 证据：图 479f1fb13612 / 第 1 页 / source_001 网格 C1-D3：M2 VCC/VBAT/ON-OFF、BT1、FB3、R3、C8/C9

## 接口

### P1 Cap-Bus 针脚映射

P1 pins8-14 分别为 RESET/GPIO3、INT/GPIO4、BUSY/GPIO6、SCK/GPIO40、MOSI/GPIO14、MISO/GPIO39、CS/GPIO5；pins1-7 分别为 GPS-TX/GPIO15、GPS-RX/GPIO13、SCL/GPIO1、SDA/GPIO0、5VOUT、GND、5VIN。

- 参数与网络：`pin1=GPS-TX / G15`；`pin2=GPS-RX / G13`；`pin3=SCL / G1`；`pin4=SDA / G0`；`pin5=5VOUT`；`pin6=GND`；`pin7=5VIN`；`pin8=RESET / G3`；`pin9=INT / G4`；`pin10=BUSY / G6`；`pin11=SCK / G40`；`pin12=MOSI / G14`；`pin13=MISO / G39`；`pin14=CS / G5`
- 证据：图 479f1fb13612 / 第 1 页 / source_001 网格 D3-D4：P1 pins1-14

## 总线

### 主机到 LoRa1262 SPI

P1 GPIO40/14/39/5 分别通过 SCK/MOSI/MISO/NSS 连接 M1 pins11/10/9/12，并在内部页连接 SX1262 SCK pin18、MOSI pin17、MISO pin16、NSS pin19。

- 参数与网络：`controller=external host`；`device=M1 LoRa1262 / SX1262`；`sck=GPIO40 -> M1 pin11 -> SX1262 pin18`；`mosi=GPIO14 -> M1 pin10 -> SX1262 pin17`；`miso=GPIO39 <- M1 pin9 <- SX1262 pin16`；`nss=GPIO5 -> M1 pin12 -> SX1262 pin19`
- 证据：图 479f1fb13612 / 第 1 页 / source_001 M1 与 P1 的 NSS/SCK/MOSI/MISO; 图 53862f11d5ee / 第 1 页 / source_002 U1 SX1262 SPI pins16-19

### GP-02 GNSS UART

M2 TXD1 pin2 经 R4 0Ω 连接 G15/P1 pin1 GPS-TX，M2 RXD1 pin3 连接 G13/P1 pin2 GPS-RX。

- 参数与网络：`gnss_tx=M2 pin2 TXD1 -> R4 0Ω -> G15 -> P1 pin1 GPS-TX`；`gnss_rx=P1 pin2 GPS-RX -> G13 -> M2 pin3 RXD1`；`host_rx_gpio=GPIO15`；`host_tx_gpio=GPIO13`；`baud_rate_shown=null`
- 证据：图 479f1fb13612 / 第 1 页 / source_001 网格 C2-D4：M2 TXD1/RXD1、R4、G15/G13 与 P1

## GPIO 与控制信号

### LoRa RESET/IRQ/BUSY

P1 GPIO3/GPIO4/GPIO6 分别通过 RST/IRQ/BUSY 连接 M1 pins8/6/7；内部页对应 SX1262 NRESET pin15、DIO1 pin13 和 BUSY pin14。

- 参数与网络：`reset=GPIO3 -> M1 pin8 RST -> SX1262 pin15 NRESET`；`interrupt=SX1262 pin13 DIO1 -> M1 pin6 IRQ -> GPIO4`；`busy=SX1262 pin14 BUSY -> M1 pin7 BUSY -> GPIO6`
- 证据：图 479f1fb13612 / 第 1 页 / source_001 M1 RST/IRQ/BUSY 与 P1; 图 53862f11d5ee / 第 1 页 / source_002 SX1262 NRESET/DIO1/BUSY

## 时钟

### SX1262 32MHz 参考时钟

X1 X1G0041310042 由 VDD_OCXO 3.0V 供电，输出经 C34 10pF 和 R3 220Ω 形成 SX_32M_REF，连接 SX1262 XTA pin3；XTB pin4 未连接，DIO3 pin6 提供 VDD_OCXO。

- 参数与网络：`source=X1 X1G0041310042`；`frequency=32MHz from SX_32M_REF naming`；`supply=VDD_OCXO 3.0V`；`path=X1 pin3 -> C34 10pF -> R3 220Ω -> SX1262 pin3 XTA`；`xtb=SX1262 pin4 NC`；`supply_control=SX1262 DIO3 pin6 -> VDD_OCXO`
- 证据：图 53862f11d5ee / 第 1 页 / source_002 网格 A1/C1-C2：SX1262 XTA/XTB/DIO3 与 X1/C34/R3/VDD_OCXO

## 射频

### LoRa 外部 SMA 天线

M1 ANT pin1 经 R2 0Ω 连接 E4 SMA-KE；D1、C10、C11 均标 NC，C12 470uF 从 M1 3V3 接 GND。

- 参数与网络：`module=M1 LoRa1262`；`antenna_pin=pin1 ANT`；`connector=E4 SMA-KE`；`series=R2 0Ω`；`optional_parts=D1/C10/C11 NC`；`bulk_decoupling=C12 470uF`
- 证据：图 479f1fb13612 / 第 1 页 / source_001 网格 A3-A4：E4/R2/D1/C10/C11/M1 ANT/C12

### GNSS 陶瓷天线与 MAX2659

J1 ANT181804 经 C5 470pF 和 L1 6.8nH 连接 U1 MAX2659 RFIN pin3，MAX2659 RFOUT pin6 连接 M2 ANT pin11；VCC pin4 与 SHDN pin5 接经 FB2 120Ω/MB 的 +3.3V。

- 参数与网络：`antenna=J1 ANT181804`；`input_match=C5 470pF; L1 6.8nH`；`lna=U1 MAX2659`；`rf_path=J1 -> C5/L1 -> RFIN pin3 -> RFOUT pin6 -> M2 pin11 ANT`；`supply=+3.3V via FB2 120Ω/MB to VCC/SHDN`；`decoupling=C6 100nF; C7 33nF`
- 证据：图 479f1fb13612 / 第 1 页 / source_001 网格 C3-D4：J1/L1/C5/U1 MAX2659/FB2/C6/C7/M2 ANT

### SX1262 868M 发射与接收匹配

SX_RFO 通过标注 868M 的 L1/L2/L3、C3/C4/C8/C12 网络形成 PA_TX；SX_RFI_N/P 通过 L11、C14、C33 网络形成 PX_RX。

- 参数与网络：`tx_input=SX1262 pin23 RFO / SX_RFO`；`tx_output=PA_TX`；`tx_network=L1/L2/L3,C3/C4/C8/C12 labeled 868M`；`rx_input=SX1262 pins21/22 RFI_P/RFI_N`；`rx_output=PX_RX`；`rx_network=L11,C14,C33 labeled 868M`；`impedance_labels=RF_50R`
- 证据：图 53862f11d5ee / 第 1 页 / source_002 网格 A3-B4：SX_RFO/PA_TX 与 SX_RFI_P/N/PX_RX 的 868M 网络

### FM8625H 天线开关与 RF_OUT

U2 FM8625H 的 RF1 接 PA_TX、RF2 接 PA_RX_SWC、RFC 经 C1 与 L4 0R/TBD 接 RF_OUT；CTRL pin6 经 R2 100Ω 接 SX_DIO2，RF_OUT 由 D1 H3V3U10B 对地保护。

- 参数与网络：`switch=U2 FM8625H`；`tx=RF1 <- PA_TX`；`rx=RF2 <- PA_RX_SWC`；`common=RFC -> C1 -> L4 0R/TBD -> RF_OUT`；`control=SX1262 DIO2 -> SX_DIO2 -> R2 100Ω -> CTRL`；`protection=D1 H3V3U10B to GND`
- 证据：图 53862f11d5ee / 第 1 页 / source_002 网格 C3-C4：U2/C1/L4/D1/R2/SX_DIO2/RF_OUT

### 可选接收 LNA 路径

U4 SGM13005LA 及 L6/L7/R6/C10/C13 标 NC，R4/R5 0Ω 绘制 PX_RX 到 PA_RX_SWC 的旁路，因此当前图示装配不使用该 LNA。

- 参数与网络：`lna=U4/NC SGM13005LA/NC`；`populated=false`；`optional_parts=L6/L7/R6/C10/C13 NC`；`bypass=PX_RX -> R4 0Ω -> R5 0Ω -> PA_RX_SWC`
- 证据：图 53862f11d5ee / 第 1 页 / source_002 网格 D3：U4/NC、R4/R5 与所有 NC 支持件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Cap LoRa868 系统架构 | `host=P1 Cap-Bus`；`power=+5VOUT -> U3 JW5712 -> VDD_3V3/+3.3V`；`lora=M1 LoRa1262 / internal U1 SX1262`；`lora_antenna=E4 SMA-KE`；`gnss=M2 GP-02`；`gnss_rf=J1 ANT181804 -> U1 MAX2659 -> M2 ANT` |
| 接口 | P1 Cap-Bus 针脚映射 | `pin1=GPS-TX / G15`；`pin2=GPS-RX / G13`；`pin3=SCL / G1`；`pin4=SDA / G0`；`pin5=5VOUT`；`pin6=GND`；`pin7=5VIN`；`pin8=RESET / G3`；`pin9=INT / G4`；`pin10=BUSY / G6`；`pin11=SCK / G40`；`pin12=MOSI / G14`；`pin13=MISO / G39`；`pin14=CS / G5` |
| 电源 | +5VOUT 到 VDD_3V3 | `input=+5VOUT`；`converter=U3 JW5712`；`enable=R1 10KΩ to +5VOUT`；`inductor=L2 MWTC201608S2R2`；`output=VDD_3V3`；`annotated_output_current=0-0.6A`；`input_caps=C15 22uF; C16 100nF`；`output_caps=C2/C3/C4 22uF; C1 1nF` |
| 总线 | 主机到 LoRa1262 SPI | `controller=external host`；`device=M1 LoRa1262 / SX1262`；`sck=GPIO40 -> M1 pin11 -> SX1262 pin18`；`mosi=GPIO14 -> M1 pin10 -> SX1262 pin17`；`miso=GPIO39 <- M1 pin9 <- SX1262 pin16`；`nss=GPIO5 -> M1 pin12 -> SX1262 pin19` |
| GPIO 与控制信号 | LoRa RESET/IRQ/BUSY | `reset=GPIO3 -> M1 pin8 RST -> SX1262 pin15 NRESET`；`interrupt=SX1262 pin13 DIO1 -> M1 pin6 IRQ -> GPIO4`；`busy=SX1262 pin14 BUSY -> M1 pin7 BUSY -> GPIO6` |
| 射频 | LoRa 外部 SMA 天线 | `module=M1 LoRa1262`；`antenna_pin=pin1 ANT`；`connector=E4 SMA-KE`；`series=R2 0Ω`；`optional_parts=D1/C10/C11 NC`；`bulk_decoupling=C12 470uF` |
| 总线 | GP-02 GNSS UART | `gnss_tx=M2 pin2 TXD1 -> R4 0Ω -> G15 -> P1 pin1 GPS-TX`；`gnss_rx=P1 pin2 GPS-RX -> G13 -> M2 pin3 RXD1`；`host_rx_gpio=GPIO15`；`host_tx_gpio=GPIO13`；`baud_rate_shown=null` |
| 电源 | GP-02 主电源与备用电池 | `main_supply=+3.3V -> FB3 120Ω/MB -> M2 pin8 VCC`；`decoupling=C8 22uF; C9 100nF`；`backup=BT1 Battery -> M2 pin6 VBAT`；`on_off=M2 pin5 ON/OFF with R3 10KΩ to +3.3V` |
| 射频 | GNSS 陶瓷天线与 MAX2659 | `antenna=J1 ANT181804`；`input_match=C5 470pF; L1 6.8nH`；`lna=U1 MAX2659`；`rf_path=J1 -> C5/L1 -> RFIN pin3 -> RFOUT pin6 -> M2 pin11 ANT`；`supply=+3.3V via FB2 120Ω/MB to VCC/SHDN`；`decoupling=C6 100nF; C7 33nF` |
| 核心器件 | 可选 I2C GPIO 扩展器 | `reference=U2/NC`；`part=P14IOE5V6408ZTAEX`；`populated=false`；`i2c=SCL/SDA from P1 G1/G0`；`outputs=P0 BYPASS; P1 SHUT_DOWN`；`optional_support=R5/R6/R7/C13/C14 NC` |
| 核心器件 | SX1262 电源与内部稳压网络 | `input_supply=VDD_3V3 to pins1,10,11`；`regulated_net=pin7 VREG -> SX_VREG`；`dc_dc=pin9 DCC_SW -> L5 15uH/200mA -> SX_VREG`；`pa_supply=pin24 VR_PA -> SX_PAVDD`；`grounds=pins2,5,8,20,25` |
| 时钟 | SX1262 32MHz 参考时钟 | `source=X1 X1G0041310042`；`frequency=32MHz from SX_32M_REF naming`；`supply=VDD_OCXO 3.0V`；`path=X1 pin3 -> C34 10pF -> R3 220Ω -> SX1262 pin3 XTA`；`xtb=SX1262 pin4 NC`；`supply_control=SX1262 DIO3 pin6 -> VDD_OCXO` |
| 射频 | SX1262 868M 发射与接收匹配 | `tx_input=SX1262 pin23 RFO / SX_RFO`；`tx_output=PA_TX`；`tx_network=L1/L2/L3,C3/C4/C8/C12 labeled 868M`；`rx_input=SX1262 pins21/22 RFI_P/RFI_N`；`rx_output=PX_RX`；`rx_network=L11,C14,C33 labeled 868M`；`impedance_labels=RF_50R` |
| 射频 | FM8625H 天线开关与 RF_OUT | `switch=U2 FM8625H`；`tx=RF1 <- PA_TX`；`rx=RF2 <- PA_RX_SWC`；`common=RFC -> C1 -> L4 0R/TBD -> RF_OUT`；`control=SX1262 DIO2 -> SX_DIO2 -> R2 100Ω -> CTRL`；`protection=D1 H3V3U10B to GND` |
| 射频 | 可选接收 LNA 路径 | `lna=U4/NC SGM13005LA/NC`；`populated=false`；`optional_parts=L6/L7/R6/C10/C13 NC`；`bypass=PX_RX -> R4 0Ω -> R5 0Ω -> PA_RX_SWC` |
| 其他事实 | Stamp LoRa-1262 内部页修订对应关系 | `main_resource=SCH_Cap_LoRa868_SCH_V1.0`；`stamp_resource=OLD-868-SCH_Stamp_LoRa-1262_SCH_V0.1`；`current_bom_alignment=null` |
| 核心器件 | GP-02 与 ATGM336H-6N/AT6668 对应关系 | `schematic_module=M2 GP-02`；`documented_module=ATGM336H-6N`；`documented_chip=AT6668`；`assembly_mapping_confirmed=false` |
| 其他事实 | 正文中的 LoRa 与 GNSS 性能 | `documented_lora_band=868-923MHz`；`documented_lora_tx=+20dBm`；`documented_lora_sensitivity=-147dBm`；`documented_lora_rate=300kbps`；`documented_gnss_uart=115200bps 8N1`；`documented_gnss_update=10Hz max`；`documented_gnss_accuracy=<1.5m CEP50`；`schematic_lora=SX1262 with 868M matching`；`schematic_gnss=M2 GP-02` |
| 系统结构 | 未显示的系统功能 | `general_mcu_shown=false`；`storage_shown=false`；`audio_shown=false`；`environment_sensor_shown=false`；`dedicated_debug_connector_shown=false`；`external_host=P1 Cap-Bus` |

## 待确认事项

- `other.stamp-schematic-revision`：资源清单把第二页 URL 标为 OLD-868 与 V0.1，而主板资源标 V1.0；该旧版内部页是否精确对应当前 M1 LoRa1262 量产 BOM 无法由两页本身确认。（证据：图 479f1fb13612 / 第 1 页 / source_001 M1 LoRa1262 外部接口; 图 53862f11d5ee / 第 1 页 / source_002 完整 SX1262/868M 内部电路）
- `component.gnss-module-identity`：原理图 M2 明确标 GP-02，产品正文写 ATGM336H-6N@AT6668；当前页面未在 M2 型号字段中标出 ATGM336H-6N 或 AT6668，量产模组与内部芯片对应关系需 BOM 确认。（证据：图 479f1fb13612 / 第 1 页 / source_001 网格 C2-D3：M2 型号仅标 GP-02）
- `other.documented-radio-gnss-performance`：正文列出 868-923MHz、+20dBm、-147dBm、300kbps、GNSS 系统/频点、115200bps、10Hz、精度、灵敏度和功耗；原理图只确认器件与连接，无法验证区域配置、固件和整机性能。（证据：图 479f1fb13612 / 第 1 页 / source_001 M1/M2/P1 与天线/电源; 图 53862f11d5ee / 第 1 页 / source_002 SX1262 及 868M RF 网络，图中无整机性能表）
- `review.stamp-schematic-revision`：OLD-868/V0.1 的 Stamp LoRa-1262 内部页是否就是 U201 当前 M1 的正式量产原理图和 BOM？；原因：资源命名明确标 OLD 与 V0.1，而主板为 V1.0，需要版本记录或当前 Stamp 原理图确认。
- `review.gnss-module-identity`：U201 当前 M2 GP-02 的量产模组和内部芯片是否分别对应 ATGM336H-6N 与 AT6668？；原因：产品正文与原理图型号字段使用不同名称，需 BOM 或模组丝印闭环。
- `review.radio-gnss-performance`：U201 当前固件、区域配置和整机测试确认的 LoRa 频段/功率/灵敏度/速率及 GNSS 系统/精度/更新率/功耗是什么？；原因：这些参数受固件、匹配、天线、区域和测试条件影响，连接原理图不能证明整机指标。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `479f1fb13612b9ae0587299482d8e3c7557314c534deb878608f9b6055b853f3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1177/SCH_Cap_LoRa868_SCH_V1.0_20250815_2025_08_18_18_57_08_page_01.png` |
| 2 | 1 | `53862f11d5ee552fee250d4078afd2de929831e6e1cc89636c0072b00964a43e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1177/OLD-868-SCH_Stamp_LoRa-1262_SCH_V0.1_20250815_2025_08_28_11_44_10_page_01.png` |

---

源文档：`zh_CN/cap/Cap_LoRa868.md`

源文档 SHA-256：`9eddc1c2fa95ac22d54eb7e4fc8e5874931268a1bca0417e178248408bc551b3`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
