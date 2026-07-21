# Cap LoRa-1262 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Cap LoRa-1262 |
| SKU | U214 |
| 产品 ID | `cap-lora-1262-be2dc05fa52a` |
| 源文档 | `zh_CN/cap/Cap_LoRa-1262.md` |

## 概述

Cap LoRa-1262 主板以 P1 14-pin Cap-Bus 接收 LoRa SPI、GNSS UART、I2C 和 5V 电源，U3 JW5712 生成 VDD_3V3，M1 Stamp LoRa-1262 Mini 接 E4 SMA-KE，M2 GP-02 GNSS 经 MAX2659 LNA 与 ANT181804 陶瓷天线接收信号。U2 PI4IOE5V6408ZTAEX 通过 I2C 控制 M1 的 BYPASS/SHUT_DOWN 网络，并把 I2C 与 +5VOUT 引到 J2 Grove。Stamp 子板原理图进一步展开 U1 SX1262、0900FM15K0039 射频前端、FM8625H 开关、32MHz 有源时钟和 IPEX4 天线口；两张图的天线接口与控制网络需要结合 BOM/PCB 确认最终装配拓扑。

## 检索关键词

`Cap LoRa-1262`、`U214`、`SX1262`、`Stamp LoRa-1262 Mini`、`JW5712`、`PI4IOE5V6408ZTAEX`、`GP-02`、`ATGM336H-6N`、`AT6668`、`MAX2659`、`0900FM15K0039`、`FM8625H`、`ANT181804`、`SMA-KE`、`IPEX4`、`LoRa SPI`、`SPI_CLK`、`SPI_MOSI`、`SPI_MISO`、`SX_NSS`、`LORA_IRQ`、`SX_BUSY`、`SX_NRST`、`SX_DIO2`、`SX_DIO3`、`GPS-TX`、`GPS-RX`、`G15`、`G13`、`I2C_SDA`、`I2C_SCL`、`BYPASS`、`SHUT_DOWN`、`SX_ANT_SW`、`VDD_3V3`、`+5VOUT`、`+5VIN`、`GROVE 4P`、`0x68`、`0x69`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 [Cap main] | JW5712 | +5VOUT 至 VDD_3V3 的 0~0.6A 降压转换器 | 图 ca8220583ff6 / 第 1 页 / 网格 A1-A2，U3 JW5712、L2、VDD_3V3，IOUT:0~0.6A |
| M1 [Cap main] | Stamp LoRa-1262 Mini | LoRa 子模块，通过 SPI/IRQ/BUSY/RST 与 Cap-Bus 通信，并引出 ANT、BYPASS 和 3V3 | 图 ca8220583ff6 / 第 1 页 / 网格 A3-A4，M1 Stamp LoRa-1262 Mini pins1-13 |
| U2 [Cap main] | PI4IOE5V6408ZTAEX | I2C IO 扩展器，P0/P1 分别连接 BYPASS/SHUT_DOWN | 图 ca8220583ff6 / 第 1 页 / 网格 B1-C2，U2 PI4IOE5V6408ZTAEX，SCL/SDA/P0/P1/ADDR/RESET |
| E4 [Cap main] | SMA-KE | 主板 LoRa 外置天线连接器，经 R2 0Ω 与 M1 ANT 相连 | 图 ca8220583ff6 / 第 1 页 / 网格 A2-A4，E4 SMA-KE、D1/C10/C11/R2 至 M1 ANT |
| M2 [Cap main] | GP-02 | GNSS 模组，通过 TXD1/RXD1 UART 连接 Cap-Bus，并连接备份电池与外部 LNA/陶瓷天线 | 图 ca8220583ff6 / 第 1 页 / 网格 C1-D3，M2 GP-02，TXD1/RXD1/VBAT/VCC/ANT/ON-OFF |
| U1 [Cap main] | MAX2659 | GNSS 射频低噪声放大器，RFIN 接陶瓷天线，RFOUT 接 M2 ANT | 图 ca8220583ff6 / 第 1 页 / 网格 C2-C4，U1 MAX2659，RFIN/RFOUT/VCC/SHDN/GND |
| J1 [Cap main] | ANT181804 | GNSS 内置陶瓷天线，经 C5/L1 连接 MAX2659 RFIN | 图 ca8220583ff6 / 第 1 页 / 网格 C3-C4，J1 ANT181804、C5 470pF、L1 6.8nH 至 MAX2659 |
| BT1 [Cap main] | +Battery | GP-02 VBAT 备用电源 | 图 ca8220583ff6 / 第 1 页 / 网格 D1-D2，BT1 +Battery 连接 M2 pin6 VBAT |
| J2 [Cap main] | GROVE 4P | 外部 I2C/5V 扩展接口，提供 SCL、SDA、+5VOUT、GND | 图 ca8220583ff6 / 第 1 页 / 网格 C1，J2 GROVE 4P，SCL/SDA/5V/GND |
| P1 [Cap main] | HDR-SMD_14P-P2.54 | 14-pin Cap-Bus 主机连接器，承载 LoRa、GNSS、I2C 与双 5V 网络 | 图 ca8220583ff6 / 第 1 页 / 网格 D3-D4，P1 HDR-SMD_14P-P2.54 pins1-14 |
| U1 [Stamp] | SX1262 | Stamp 内部 LoRa 收发器，连接 SPI、DIO、32MHz 参考时钟与射频前端 | 图 77b258457736 / 第 1 页 / 网格 A1-A2，U1 SX1262，SPI/DIO/RF/XTAL/电源引脚 |
| U3 [Stamp] | 0900FM15K0039 | SX1262 RFO/RFLP/RFLN 与 SX_SRFI/SX_SRFO 之间的射频前端/匹配器件 | 图 77b258457736 / 第 1 页 / 网格 A3-A4，U3 0900FM15K0039，RFO/RFLP/RFLN/SW_RFI/SW_RFO |
| U2 [Stamp] | FM8625H | Stamp 射频天线开关，RF1/RF2 选择到 RFC 天线端，控制网络为 SX_ANT_SW/SX_DIO2 | 图 77b258457736 / 第 1 页 / 网格 A5-A6，U2 FM8625H，RF1/RF2/RFC/VDD/CTRL/GND |
| X1 [Stamp] | X1G0041310042 | 3.0V 有源参考时钟源，输出经 R3/C6 形成 SX_32M_REF | 图 77b258457736 / 第 1 页 / 网格 B2-B4，X1 X1G0041310042、VDD:3.0V、R3 220R、C6 10nF、SX_32M_REF |
| J1 [Stamp] | IPEX4 | Stamp 子板射频天线连接器，前级含匹配位和 ESD 保护 | 图 77b258457736 / 第 1 页 / 网格 A7-A8，J1 IPEX4，C1/L2/C2/C3/D1 射频网络 |

## 系统结构

### Cap LoRa-1262 系统架构

主板由 Stamp LoRa-1262 Mini、GP-02 GNSS、MAX2659 LNA、PI4IOE5V6408、JW5712 电源、SMA/Grove/Cap-Bus 接口组成；第二资产展开 Stamp 内部 SX1262、射频前端、开关、时钟与 IPEX4。

- 参数与网络：`lora_module=M1 Stamp LoRa-1262 Mini`；`lora_ic=U1 [Stamp] SX1262`；`gnss=M2 GP-02`；`gnss_lna=U1 [Cap] MAX2659`；`io_expander=U2 [Cap] PI4IOE5V6408ZTAEX`；`buck=U3 [Cap] JW5712`；`host=P1 14-pin`
- 证据：图 ca8220583ff6 / 第 1 页 / 主板整页功能分区; 图 77b258457736 / 第 1 页 / Stamp 整页 SX1262/RF/Clock/Connector

## 核心器件

### Stamp 内部 SX1262

第二资产 U1 明确标为 SX1262，SPI_CLK/MOSI/MISO/NSS、LORA_IRQ、SX_BUSY、SX_NRST、SX_DIO2/SX_DIO3 与射频/电源网络均从该芯片引出。

- 参数与网络：`reference=U1 [Stamp]`；`part_number=SX1262`；`spi=SPI_CLK,SPI_MOSI,SPI_MISO,SX_NSS`；`control=LORA_IRQ,SX_BUSY,SX_NRST,SX_DIO2,SX_DIO3`；`rf=SX_RFO,SX_RFL_P,SX_RFL_N`；`clock=SX_32M_REF`
- 证据：图 77b258457736 / 第 1 页 / 网格 A1-A2，U1 SX1262 全部网络

### GP-02 GNSS 模组

主板 M2 标为 GP-02，TXD1/RXD1 连接 G15/G13，VBAT 接 BT1，VCC 经 FB3 供电，ANT 接 MAX2659 RFOUT；1PPS、NRST、SCL/SDA 等多脚未连接。

- 参数与网络：`reference=M2`；`schematic_model=GP-02`；`uart=pin2 TXD1/G15,pin3 RXD1/G13`；`backup=pin6 VBAT/BT1`；`main_power=pin8 VCC via FB3`；`antenna=pin11 ANT`；`unused=1PPS,NRST,SCL,SDA,VCC_RF`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 C1-D3，M2 GP-02 pins1-18

## 电源

### JW5712 3.3V 电源

U3 JW5712 的 VIN 接 +5V/+5VOUT，EN 经 R1 10K 上拉，SW 经 L2 WPN201610U2R2MT 输出 VDD_3V3；页内标注 IOUT 0~0.6A。

- 参数与网络：`converter=U3 JW5712`；`input=+5V,+5VOUT`；`enable=R1 10K pull-up`；`inductor=L2 WPN201610U2R2MT`；`output=VDD_3V3`；`current_mark=0~0.6A`；`output_caps=C2,C3,C4 22uF`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 A1-A2，U3/R1/L2/C1-C4/VDD_3V3

### 主板 5V 与 3.3V 分配

+5VOUT 同时供给 JW5712 和 J2 Grove；VDD_3V3 供给 M1、U2、M2、MAX2659 与相关逻辑。P1 另有独立 +5VIN pin7，在本页未显示其他负载。

- 参数与网络：`5vout=P1 pin5,J2 pin3,U3 VIN`；`5vin=P1 pin7 only on page`；`3v3=U3 output VDD_3V3`；`3v3_loads=M1,U2,M2,U1 MAX2659`
- 证据：图 ca8220583ff6 / 第 1 页 / 整页 +5VOUT/+5VIN/VDD_3V3 网络

### Stamp 子板 3.3V 滤波

VIN_3V3 经 FB2 BLM15AX601SN1D 形成 VDD_3V3，配置 C18/C10 10uF、C11/C12 1uF、C13/C14 100nF 去耦；SX_VREG 与 SX_PAVDD 另有 C15/C16/C17。

- 参数与网络：`input=VIN_3V3`；`ferrite=FB2 BLM15AX601SN1D`；`output=VDD_3V3`；`bulk_caps=C18,C10 10uF/10V`；`mid_caps=C11,C12 1uF/10V`；`hf_caps=C13,C14 100nF/25V`；`rf_rails=SX_VREG,SX_PAVDD`
- 证据：图 77b258457736 / 第 1 页 / 网格 B1-C4，FB2/C10-C18/VDD_3V3/SX_VREG/SX_PAVDD

### GNSS 主电源与备份电源

M2 VCC pin8 从 +3.3V 经 FB3 120Ω/MB 供电，并以 C8 22uF/C9 100nF 去耦；VBAT pin6 接 BT1 +Battery；ON/OFF pin5 由 R3 10K 上拉到 +3.3V。

- 参数与网络：`main_supply=+3.3V -> FB3 120Ω/MB -> M2.8 VCC`；`decoupling=C8 22uF,C9 100nF`；`backup=BT1 -> M2.6 VBAT`；`on_off=M2.5 with R3 10K pull-up`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 C1-D3，M2 VCC/VBAT/ON-OFF、FB3/C8/C9/R3/BT1

## 接口

### P1 14-pin Cap-Bus

P1 pins8~14 分别为 RST、IRQ、BUSY、SCK、MOSI、MISO、NSS；pins1/2 为 GPS-TX/GPS-RX，pins3/4 为 SCL/SDA，pin5 +5VOUT、pin6 GND、pin7 +5VIN。

- 参数与网络：`pin1=GPS-TX/G15`；`pin2=GPS-RX/G13`；`pin3=SCL`；`pin4=SDA`；`pin5=+5VOUT`；`pin6=GND`；`pin7=+5VIN`；`pin8=RST/G3`；`pin9=IRQ/G4`；`pin10=BUSY/G6`；`pin11=SCK/G40`；`pin12=MOSI/G14`；`pin13=MISO/G39`；`pin14=NSS/G5`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 D3-D4，P1 HDR-SMD_14P-P2.54 pin1-14

### J2 HY2.0-4P/Grove 接口

J2 GROVE 4P 从上到下引出 SCL、SDA、+5VOUT、GND，并与 P1/U2 共用 I2C 网络。

- 参数与网络：`reference=J2`；`pin1=SCL`；`pin2=SDA`；`pin3=+5VOUT`；`pin4=GND`；`bus=shared with P1 and U2`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 C1，J2 GROVE 4P

## 总线

### Cap-Bus 到 Stamp LoRa SPI

P1 SCK/G40、MOSI/G14、MISO/G39、NSS/G5 分别连接 M1 SCK pin6、MOSI pin7、MISO pin8、NSS pin9；RST/G3、BUSY/G6、IRQ/G4 连接 M1 对应控制脚。

- 参数与网络：`sck=P1.11 G40 -> M1.6`；`mosi=P1.12 G14 -> M1.7`；`miso=P1.13 G39 -> M1.8`；`chip_select=P1.14 G5 -> M1.9 NSS`；`reset=P1.8 G3 -> M1.2 RST`；`busy=P1.10 G6 -> M1.3 BUSY`；`interrupt=M1.4 IRQ -> P1.9 G4`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 A3-D4，M1 SPI/控制网络到 P1

### PI4IOE5V6408 与 Grove I2C

P1 SDA/SCL 连接 U2 PI4IOE5V6408 pins14/13 并延伸到 J2 SDA/SCL；R5/R6 10K 上拉位置均标 NC，因此主板不装这两颗 I2C 上拉。

- 参数与网络：`controller=P1 pins4/3`；`device=U2 pins14 SDA,13 SCL`；`extension=J2 SDA,SCL`；`sda_pullup=R5 10K NC`；`scl_pullup=R6 10K NC`；`rail=VDD_3V3`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 B1-C2/D4，P1/J2/U2 I2C 与 R5/R6 NC

### Cap-Bus 到 GNSS UART

M2 TXD1 pin2 经 R4 0Ω 连接 G15 并到 P1 pin1 GPS-TX；M2 RXD1 pin3 连接 G13 并到 P1 pin2 GPS-RX。

- 参数与网络：`device_tx=M2.2 TXD1 -> R4 0Ω -> G15 -> P1.1 GPS-TX`；`device_rx=P1.2 GPS-RX/G13 -> M2.3 RXD1`；`device=M2 GP-02`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 C1-D4，M2 TXD1/RXD1 到 P1 pins1/2

## 总线地址

### PI4IOE5V6408 地址选择

U2 ADDR pin9 接 GND；原理图未标出该绑带对应的数值 I2C 地址。

- 参数与网络：`device=U2 PI4IOE5V6408ZTAEX`；`address_pin=pin9 ADDR`；`strap=GND`；`numeric_address=null`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 B1-C2，U2 ADDR pin9 接 GND

## GPIO 与控制信号

### Stamp RF 开关控制

FM8625H CTRL pin6 经 R2 100R/1% 接 SX_DIO2，并以 C5 100pF/25V 对地；VDD pin4 通过 R1 100R/1% 接 SX_ANT_SW，并以 C4 100pF/25V 对地。

- 参数与网络：`switch=U2 [Stamp] FM8625H`；`control=pin6 CTRL -> R2 100R -> SX_DIO2`；`supply_control=pin4 VDD -> R1 100R -> SX_ANT_SW`；`control_caps=C4,C5 100pF/25V`
- 证据：图 77b258457736 / 第 1 页 / 网格 A5-A6，U2 FM8625H、R1/R2、C4/C5、SX_ANT_SW/SX_DIO2

### PI4IOE5V6408 输出映射

U2 P0 pin12 连接 BYPASS 并到 M1 pin10，P1 pin11 连接 SHUT_DOWN；P2~P7 未连接。

- 参数与网络：`p0=pin12 BYPASS -> M1 pin10`；`p1=pin11 SHUT_DOWN`；`unused=P2-P7 NC`；`interrupt=pin1 INT no external net`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 B1-C2，U2 P0/P1/P2-P7 与 M1 BYPASS

## 时钟

### SX1262 32MHz 参考时钟

X1 X1G0041310042 标注 VDD 3.0V，输出 pin3 经 R3 220R/1% 和 C6 10nF/5% 形成 SX_32M_REF；VDD_OCXO 由 SX_DIO3 经 FB1 600R/0201 滤波供电。

- 参数与网络：`oscillator=X1 X1G0041310042`；`frequency_net=SX_32M_REF`；`supply_mark=3.0V`；`output_chain=pin3 -> R3 220R/1% -> C6 10nF/5%`；`supply_chain=SX_DIO3 -> FB1 600R/0201 -> VDD_OCXO`；`decoupling=C7,C8,C9 100nF/25V`
- 证据：图 77b258457736 / 第 1 页 / 网格 B1-B4，X1/FB1/R3/C6-C9/SX_32M_REF

## 复位

### LoRa 复位网络

P1 pin8 G3/RST 连接 M1 pin2 RST；Stamp 内部该信号为 SX_NRST 并连接 SX1262 NRRESET。

- 参数与网络：`host=P1.8 G3/RST`；`module=M1.2 RST`；`internal_net=SX_NRST`；`target=U1 [Stamp] NRRESET`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 A3-D4，P1 RST 到 M1; 图 77b258457736 / 第 1 页 / 网格 A1，SX_NRST 到 SX1262 NRRESET

## 保护电路

### Stamp IPEX 天线保护与匹配

FM8625H RFC 经 C1 串联、L2 0R/TBD 与 C2/C3/L4 匹配位到 J1 IPEX4，D1 H3V3U10B/TBD 从天线节点对地保护；L4 标 NC。

- 参数与网络：`connector=J1 IPEX4`；`series_cap=C1`；`series_inductor=L2 0R/TBD`；`shunt_options=C2 TBD,C3 TBD,L4 NC`；`esd=D1 H3V3U10B/TBD`
- 证据：图 77b258457736 / 第 1 页 / 网格 A6-A8，FM8625H RFC 到 J1 IPEX4 的 C1/L2/C2/C3/L4/D1

## 关键网络

### LoRa 与 GNSS 关键连接

LoRa 路径为 P1 SPI/控制 -> M1 -> SX1262/RF 前端 -> 天线接口；GNSS 路径为 ANT181804 -> MAX2659 -> M2 GP-02，定位数据由 M2 UART -> G15/G13 -> P1。

- 参数与网络：`lora_control=P1 -> M1 -> SX1262`；`lora_rf=SX1262 -> 0900FM15K0039 -> FM8625H -> antenna`；`gnss_rf=ANT181804 -> MAX2659 -> M2 ANT`；`gnss_data=M2 TXD1/RXD1 -> G15/G13 -> P1`
- 证据：图 ca8220583ff6 / 第 1 页 / 主板 LoRa/GNSS 网络; 图 77b258457736 / 第 1 页 / Stamp SX1262 射频链

## 存储

### 板级存储

两张原理图未显示外部 Flash、EEPROM、eMMC 或存储卡接口。

- 参数与网络：`flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null`
- 证据：图 ca8220583ff6 / 第 1 页 / 主板整页无存储器件; 图 77b258457736 / 第 1 页 / Stamp 整页无外部存储器件

## 内存与 Flash

### 外部内存

两张原理图未显示独立 RAM、PSRAM 或 DDR 器件；SX1262 与 GP-02 的内部存储未展开。

- 参数与网络：`ram=null`；`psram=null`；`ddr=null`；`internal_memory=not shown`
- 证据：图 ca8220583ff6 / 第 1 页 / 主板 M1/M2 模组符号，无外部 memory; 图 77b258457736 / 第 1 页 / Stamp SX1262 外围，无 RAM/DDR

## 音频

### 音频电路

两张原理图未显示音频编解码器、麦克风、扬声器或 I2S 网络。

- 参数与网络：`codec=null`；`microphone=null`；`speaker=null`；`i2s=null`
- 证据：图 ca8220583ff6 / 第 1 页 / 主板整页无音频分区; 图 77b258457736 / 第 1 页 / Stamp 整页无音频分区

## 传感器

### GNSS 定位接收链

M2 GP-02 与 J1 ANT181804/MAX2659 组成 GNSS 接收链，数据通过 UART 输出；原理图未展开卫星基带内部结构。

- 参数与网络：`module=M2 GP-02`；`antenna=J1 ANT181804`；`lna=U1 MAX2659`；`data=TXD1/RXD1 UART`；`internal_baseband=not shown`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 C1-D4，GP-02/MAX2659/ANT181804/UART

## 射频

### SX1262 射频前端

SX1262 的 SX_RFO、SX_RFL_P、SX_RFL_N 进入 U3 0900FM15K0039，输出 SX_SRFI/SX_SRFO 再进入 U2 FM8625H 的 RF2/RF1，RFC 通过匹配网络到 J1 IPEX4。

- 参数与网络：`transceiver=U1 SX1262`；`front_end=U3 0900FM15K0039`；`switch=U2 FM8625H`；`tx_rx_nets=SX_RFO,SX_RFL_P,SX_RFL_N,SX_SRFI,SX_SRFO`；`antenna_connector=J1 IPEX4`
- 证据：图 77b258457736 / 第 1 页 / 网格 A1-A8，SX1262 经 U3/U2 到 IPEX4

### 主板 SMA LoRa 天线路径

M1 ANT pin12 经 R2 0Ω 到 E4 SMA-KE；D1、C10、C11 均标 NC，构成未装的保护/匹配位置。

- 参数与网络：`source=M1 pin12 ANT`；`series=R2 0Ω`；`connector=E4 SMA-KE`；`shunt_protection=D1 NC`；`matching_caps=C10 NC,C11 NC`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 A2-A4，M1 ANT/R2/D1/C10/C11/E4

### GNSS 陶瓷天线与 LNA

J1 ANT181804 经 C5 470pF 与 L1 6.8nH/5% 连接 MAX2659 RFIN pin3；MAX2659 RFOUT pin6 连接 M2 ANT pin11，VCC/SHDN 共接滤波后的 3.3V。

- 参数与网络：`antenna=J1 ANT181804`；`matching=C5 470pF,L1 6.8nH 5%`；`lna=U1 MAX2659`；`input=RFIN pin3`；`output=RFOUT pin6 -> M2 pin11 ANT`；`supply=3.3V via FB2 120Ω/MB`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 C2-D4，J1/L1/C5/U1 MAX2659 到 M2 ANT

## 调试与烧录

### 调试接口

两张原理图均未显示 SWD/JTAG 或专用调试连接器；可观测信号主要通过 P1、J2 与 Stamp 12-pin 焊盘引出。

- 参数与网络：`swd=null`；`jtag=null`；`debug_connector=null`；`signal_connectors=P1,J2,Stamp J1 1x12`
- 证据：图 ca8220583ff6 / 第 1 页 / 主板整页无 Debug/SWD/JTAG; 图 77b258457736 / 第 1 页 / Stamp 整页无 Debug/SWD/JTAG

## 模拟电路

### GNSS 射频匹配与滤波

GNSS 天线输入串联 C5 470pF 与 L1 6.8nH；MAX2659 电源经 FB2 120Ω/MB，C6 100nF 与 C7 33nF 对地去耦。

- 参数与网络：`series_cap=C5 470pF`；`series_inductor=L1 6.8nH 5%`；`supply_ferrite=FB2 120Ω/MB`；`decoupling=C6 100nF,C7 33nF`
- 证据：图 ca8220583ff6 / 第 1 页 / 网格 C2-C4，MAX2659/J1 周边 L1/C5/FB2/C6/C7

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Cap LoRa-1262 系统架构 | `lora_module=M1 Stamp LoRa-1262 Mini`；`lora_ic=U1 [Stamp] SX1262`；`gnss=M2 GP-02`；`gnss_lna=U1 [Cap] MAX2659`；`io_expander=U2 [Cap] PI4IOE5V6408ZTAEX`；`buck=U3 [Cap] JW5712`；`host=P1 14-pin` |
| 电源 | JW5712 3.3V 电源 | `converter=U3 JW5712`；`input=+5V,+5VOUT`；`enable=R1 10K pull-up`；`inductor=L2 WPN201610U2R2MT`；`output=VDD_3V3`；`current_mark=0~0.6A`；`output_caps=C2,C3,C4 22uF` |
| 电源 | 主板 5V 与 3.3V 分配 | `5vout=P1 pin5,J2 pin3,U3 VIN`；`5vin=P1 pin7 only on page`；`3v3=U3 output VDD_3V3`；`3v3_loads=M1,U2,M2,U1 MAX2659` |
| 接口 | P1 14-pin Cap-Bus | `pin1=GPS-TX/G15`；`pin2=GPS-RX/G13`；`pin3=SCL`；`pin4=SDA`；`pin5=+5VOUT`；`pin6=GND`；`pin7=+5VIN`；`pin8=RST/G3`；`pin9=IRQ/G4`；`pin10=BUSY/G6`；`pin11=SCK/G40`；`pin12=MOSI/G14`；`pin13=MISO/G39`；`pin14=NSS/G5` |
| 总线 | Cap-Bus 到 Stamp LoRa SPI | `sck=P1.11 G40 -> M1.6`；`mosi=P1.12 G14 -> M1.7`；`miso=P1.13 G39 -> M1.8`；`chip_select=P1.14 G5 -> M1.9 NSS`；`reset=P1.8 G3 -> M1.2 RST`；`busy=P1.10 G6 -> M1.3 BUSY`；`interrupt=M1.4 IRQ -> P1.9 G4` |
| 核心器件 | Stamp 内部 SX1262 | `reference=U1 [Stamp]`；`part_number=SX1262`；`spi=SPI_CLK,SPI_MOSI,SPI_MISO,SX_NSS`；`control=LORA_IRQ,SX_BUSY,SX_NRST,SX_DIO2,SX_DIO3`；`rf=SX_RFO,SX_RFL_P,SX_RFL_N`；`clock=SX_32M_REF` |
| 射频 | SX1262 射频前端 | `transceiver=U1 SX1262`；`front_end=U3 0900FM15K0039`；`switch=U2 FM8625H`；`tx_rx_nets=SX_RFO,SX_RFL_P,SX_RFL_N,SX_SRFI,SX_SRFO`；`antenna_connector=J1 IPEX4` |
| GPIO 与控制信号 | Stamp RF 开关控制 | `switch=U2 [Stamp] FM8625H`；`control=pin6 CTRL -> R2 100R -> SX_DIO2`；`supply_control=pin4 VDD -> R1 100R -> SX_ANT_SW`；`control_caps=C4,C5 100pF/25V` |
| 时钟 | SX1262 32MHz 参考时钟 | `oscillator=X1 X1G0041310042`；`frequency_net=SX_32M_REF`；`supply_mark=3.0V`；`output_chain=pin3 -> R3 220R/1% -> C6 10nF/5%`；`supply_chain=SX_DIO3 -> FB1 600R/0201 -> VDD_OCXO`；`decoupling=C7,C8,C9 100nF/25V` |
| 电源 | Stamp 子板 3.3V 滤波 | `input=VIN_3V3`；`ferrite=FB2 BLM15AX601SN1D`；`output=VDD_3V3`；`bulk_caps=C18,C10 10uF/10V`；`mid_caps=C11,C12 1uF/10V`；`hf_caps=C13,C14 100nF/25V`；`rf_rails=SX_VREG,SX_PAVDD` |
| 射频 | 主板 SMA LoRa 天线路径 | `source=M1 pin12 ANT`；`series=R2 0Ω`；`connector=E4 SMA-KE`；`shunt_protection=D1 NC`；`matching_caps=C10 NC,C11 NC` |
| 保护电路 | Stamp IPEX 天线保护与匹配 | `connector=J1 IPEX4`；`series_cap=C1`；`series_inductor=L2 0R/TBD`；`shunt_options=C2 TBD,C3 TBD,L4 NC`；`esd=D1 H3V3U10B/TBD` |
| 总线 | PI4IOE5V6408 与 Grove I2C | `controller=P1 pins4/3`；`device=U2 pins14 SDA,13 SCL`；`extension=J2 SDA,SCL`；`sda_pullup=R5 10K NC`；`scl_pullup=R6 10K NC`；`rail=VDD_3V3` |
| 总线地址 | PI4IOE5V6408 地址选择 | `device=U2 PI4IOE5V6408ZTAEX`；`address_pin=pin9 ADDR`；`strap=GND`；`numeric_address=null` |
| GPIO 与控制信号 | PI4IOE5V6408 输出映射 | `p0=pin12 BYPASS -> M1 pin10`；`p1=pin11 SHUT_DOWN`；`unused=P2-P7 NC`；`interrupt=pin1 INT no external net` |
| 接口 | J2 HY2.0-4P/Grove 接口 | `reference=J2`；`pin1=SCL`；`pin2=SDA`；`pin3=+5VOUT`；`pin4=GND`；`bus=shared with P1 and U2` |
| 核心器件 | GP-02 GNSS 模组 | `reference=M2`；`schematic_model=GP-02`；`uart=pin2 TXD1/G15,pin3 RXD1/G13`；`backup=pin6 VBAT/BT1`；`main_power=pin8 VCC via FB3`；`antenna=pin11 ANT`；`unused=1PPS,NRST,SCL,SDA,VCC_RF` |
| 总线 | Cap-Bus 到 GNSS UART | `device_tx=M2.2 TXD1 -> R4 0Ω -> G15 -> P1.1 GPS-TX`；`device_rx=P1.2 GPS-RX/G13 -> M2.3 RXD1`；`device=M2 GP-02` |
| 电源 | GNSS 主电源与备份电源 | `main_supply=+3.3V -> FB3 120Ω/MB -> M2.8 VCC`；`decoupling=C8 22uF,C9 100nF`；`backup=BT1 -> M2.6 VBAT`；`on_off=M2.5 with R3 10K pull-up` |
| 射频 | GNSS 陶瓷天线与 LNA | `antenna=J1 ANT181804`；`matching=C5 470pF,L1 6.8nH 5%`；`lna=U1 MAX2659`；`input=RFIN pin3`；`output=RFOUT pin6 -> M2 pin11 ANT`；`supply=3.3V via FB2 120Ω/MB` |
| 复位 | LoRa 复位网络 | `host=P1.8 G3/RST`；`module=M1.2 RST`；`internal_net=SX_NRST`；`target=U1 [Stamp] NRRESET` |
| 关键网络 | LoRa 与 GNSS 关键连接 | `lora_control=P1 -> M1 -> SX1262`；`lora_rf=SX1262 -> 0900FM15K0039 -> FM8625H -> antenna`；`gnss_rf=ANT181804 -> MAX2659 -> M2 ANT`；`gnss_data=M2 TXD1/RXD1 -> G15/G13 -> P1` |
| 模拟电路 | GNSS 射频匹配与滤波 | `series_cap=C5 470pF`；`series_inductor=L1 6.8nH 5%`；`supply_ferrite=FB2 120Ω/MB`；`decoupling=C6 100nF,C7 33nF` |
| 调试与烧录 | 调试接口 | `swd=null`；`jtag=null`；`debug_connector=null`；`signal_connectors=P1,J2,Stamp J1 1x12` |
| 存储 | 板级存储 | `flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null` |
| 内存与 Flash | 外部内存 | `ram=null`；`psram=null`；`ddr=null`；`internal_memory=not shown` |
| 音频 | 音频电路 | `codec=null`；`microphone=null`；`speaker=null`；`i2s=null` |
| 传感器 | GNSS 定位接收链 | `module=M2 GP-02`；`antenna=J1 ANT181804`；`lna=U1 MAX2659`；`data=TXD1/RXD1 UART`；`internal_baseband=not shown` |
| 核心器件 | GNSS 模组具体型号 | `reference=M2`；`schematic_model=GP-02`；`documented_module=ATGM336H-6N`；`documented_chip=AT6668`；`assembled_model=null` |
| 射频 | LoRa 天线连接器拓扑 | `main_board_connector=E4 SMA-KE`；`stamp_connector=J1 IPEX4`；`main_path=M1 ANT -> R2 -> E4`；`stamp_path=FM8625H -> matching -> J1`；`assembled_topology=null` |
| GPIO 与控制信号 | IO 扩展 P0 与射频开关使能 | `documented_action=PI4IOE P0 high`；`main_schematic=U2 P0/BYPASS -> M1 pin10`；`stamp_switch_supply=SX_ANT_SW`；`stamp_switch_control=SX_DIO2`；`verified_cross_board_mapping=null` |
| 射频 | LoRa 频段与射频性能 | `documented_frequency=868~923MHz`；`documented_tx_power=+22dBm`；`documented_sensitivity=-147dBm`；`documented_bitrate=300kbps max`；`schematic_performance=null` |
| 传感器 | GNSS 星座、精度与启动性能 | `documented_constellations=GPS,QZSS,BD2,BD3,GAL,GLO`；`documented_channels=50`；`documented_accuracy=<1.5m CEP50`；`documented_update_rate=10Hz max`；`documented_uart=115200 8N1`；`schematic_performance=null` |
| 总线地址 | PI4IOE5V6408 数值地址 | `device=U2 PI4IOE5V6408ZTAEX`；`strap=ADDR=GND`；`address_7bit=null` |

## 待确认事项

- `component.gnss-model`：产品正文称 GPS 模组为 ATGM336H-6N@AT6668，但主板原理图 M2 仅标 GP-02，未在器件符号中出现 ATGM336H-6N 或 AT6668。（证据：图 ca8220583ff6 / 第 1 页 / 网格 C1-D3，M2 器件文字 GP-02）
- `rf.antenna-connector-topology`：主板图显示 M1 ANT 经 R2 到 E4 SMA-KE；Stamp 子板图显示 FM8625H 经匹配网络到 J1 IPEX4。两资产未提供连接关系说明，无法确认量产件是否同时装配两种接口或其中一个仅为子板选件。（证据：图 ca8220583ff6 / 第 1 页 / 主板网格 A2-A4，E4 SMA-KE; 图 77b258457736 / 第 1 页 / Stamp 网格 A6-A8，J1 IPEX4）
- `gpio.documented-antenna-enable`：正文要求 PI4IOE P0 置高以使能 FM8625H；主板图 P0 标为 BYPASS 并连接 M1 pin10，而 Stamp 图控制网名为 SX_ANT_SW/SX_DIO2，未直接展示 BYPASS 到 SX_ANT_SW 的内部映射。（证据：图 ca8220583ff6 / 第 1 页 / 主板网格 B2/A3，U2 P0 BYPASS 到 M1 pin10; 图 77b258457736 / 第 1 页 / Stamp 网格 A5-A6，FM8625H SX_ANT_SW/SX_DIO2）
- `rf.documented-lora-performance`：正文称支持 868~923MHz、+22dBm 发射、-147dBm 接收和最高 300kbps；原理图确认 SX1262 与射频前端，但没有这些频段、功率、灵敏度或速率的配置/测试数据。（证据：图 77b258457736 / 第 1 页 / Stamp SX1262/RF 前端图，无频段/功率/灵敏度/速率表）
- `sensor.documented-gnss-performance`：正文列出多星座、多频点、50通道、<1.5m CEP50、10Hz 和启动/灵敏度指标；原理图只确认 GP-02、UART、LNA 与天线，未提供这些运行参数。（证据：图 ca8220583ff6 / 第 1 页 / 主板 M2 GP-02/MAX2659/ANT181804 图，无 GNSS 性能表）
- `address.io-expander-numeric`：U2 ADDR 接 GND，但当前原理图未给出对应 7-bit I2C 地址，需要 datasheet 或总线扫描确认。（证据：图 ca8220583ff6 / 第 1 页 / 网格 B1-C2，U2 ADDR pin9 接 GND，无地址注记）
- `review.gnss-model`：请用量产 BOM 或 M2 丝印确认 GP-02 是否对应 ATGM336H-6N 模组及 AT6668 芯片。；原因：产品正文与原理图采用不同层级/名称，页内不能直接等同。
- `review.lora-antenna-topology`：请用主板/Stamp PCB、BOM 与装配图确认 E4 SMA-KE 和 Stamp J1 IPEX4 的实际连接及装配状态。；原因：两个正式资源分别显示不同 LoRa 天线连接器，未给跨板说明。
- `review.antenna-enable`：请用 Stamp 引脚定义或 PCB 网表确认主板 P0/BYPASS 到 Stamp SX_ANT_SW/FM8625H 的实际映射与有效电平。；原因：两张图使用 BYPASS 与 SX_ANT_SW/SX_DIO2 不同网名，未直接给出跨板映射。
- `review.lora-performance`：请依据 SX1262 配置、射频 BOM、认证报告和实测确认 868~923MHz、+22dBm、-147dBm 与 300kbps 指标。；原因：原理图不包含射频性能测试数据。
- `review.gnss-performance`：请依据实际 GNSS 模组 datasheet、固件和定位测试确认星座、通道、精度、更新率、UART 与启动/灵敏度指标。；原因：主板图仅给出模组连接，且具体 GNSS 型号尚需确认。
- `review.io-expander-address`：请依据 PI4IOE5V6408ZTAEX datasheet 或 I2C 扫描确认 ADDR 接 GND 时的 7-bit 地址。；原因：原理图只给出地址绑带，没有数值地址。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ca8220583ff646b8466fd2161672edd74d905b6693d3850f4ceeef666333b39c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1208/U214-sche-Cap-LoRa1262_SCH_1.1_20251029_2025_11_07_22_53_19_page_02.png` |
| 2 | 1 | `77b258457736a07175c6c3b8c8706d047d959da1093bfeb48e9aadaade91bc30` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1208/NEW-1262-SCH_A1-Lora_2025_08_27_10_58_52_page_01.png` |

---

源文档：`zh_CN/cap/Cap_LoRa-1262.md`

源文档 SHA-256：`c62c7c05757b90bb7ccccafdeecc0e172e4ebafcc7308761bb12e9d42d33e337`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
