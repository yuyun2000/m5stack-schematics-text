# Unit NFC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit NFC |
| SKU | U216 |
| 产品 ID | `unit-nfc-003c544bf944` |
| 源文档 | `zh_CN/unit/Unit_NFC.md` |

## 概述

Unit NFC 的单页原理图以 U1 ST25R3916-AQWT 为近场通信前端，J1 Grove 提供 +5V、GND、SCL 和 SDA，U3 TPAP7343D-33FS4 将 +5V 转换为 VCC_3V3。I2C_EN 经 R5 上拉到 3.3V，SCL/SDA 分别使用 R3/R4 2.2K 上拉；SPI 相关脚、IRQ、MCU_CLK 与 AAT_A/AAT_B 在图中未连接。X1 27.12MHz 晶振为 U1 提供时钟，RFO1/RFO2 与 RFI1/RFI2 通过 L1/L2、C1-C13、R1/R2 构成差分匹配网络并连接 ANT1 线圈天线。I2C 地址/速率、NFC 协议与读距、自动调谐、功耗及机械参数来自产品正文，需 datasheet、BOM、固件或实测进一步确认。

## 检索关键词

`Unit NFC`、`U216`、`ST25R3916-AQWT`、`ST25R3916`、`NFC`、`RFID`、`I2C_EN`、`SCL`、`SDA`、`0x50`、`100K`、`400K`、`TPAP7343D-33FS4`、`VCC_3V3`、`+5V`、`Grove`、`27.12MHz`、`13.56MHz`、`RFO1`、`RFO2`、`RFI1`、`RFI2`、`ANT1_P`、`ANT1_N`、`ANT_NFC`、`ISO14443A`、`ISO14443B`、`FeliCa`、`ISO15693`、`NFC-A`、`NFC-B`、`NFC-F`、`NFC-V`、`AAT_A`、`AAT_B`、`IRQ`、`L1 270nH`、`L2 270nH`、`R1 2.4R`、`R2 2.4R`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ST25R3916-AQWT | I2C 控制、RF 发射/接收、时钟与天线接口的 NFC 前端 | 图 653fd96aeca2 / 第 1 页 / 网格 A2-B3 U1 ST25R3916-AQWT pins1-33 |
| U3 | TPAP7343D-33FS4 | +5V 到 VCC_3V3 的常开 LDO | 图 653fd96aeca2 / 第 1 页 / 网格 C1 U3 TPAP7343D-33FS4、C29/C30 |
| J1 | Grove | SCL、SDA、+5V、GND 四针主机接口 | 图 653fd96aeca2 / 第 1 页 / 网格 C2 J1 Grove pins1-4 |
| X1 | 27.12MHZ CL20pF | U1 XTO/XTI 的外部时钟晶体 | 图 653fd96aeca2 / 第 1 页 / 网格 B1-B2 X1 27.12MHZ CL20pF、C12/C14 |
| ANT1 | ANT_NFC | ANT1_P 与 ANT1_N 之间的差分 NFC 线圈天线 | 图 653fd96aeca2 / 第 1 页 / 网格 A4 ANT1/ANT_NFC 线圈 |
| L1,L2 | 270nH 5% | RFO1/RFO2 到天线匹配网络的对称串联电感 | 图 653fd96aeca2 / 第 1 页 / 网格 A3 L1/L2 270nH 5% |
| R1,R2 | 2.4R | ANT1_P/ANT1_N 到线圈两端的对称串联电阻 | 图 653fd96aeca2 / 第 1 页 / 网格 A3-A4 R1/R2 2.4R 与 ANT1 |
| C1-C13 | RF matching capacitors | RFO/RFI 到 ANT1_P/ANT1_N 的差分接收、发射和调谐电容网络 | 图 653fd96aeca2 / 第 1 页 / 网格 A3-A4 C1-C13 差分 RF 匹配区 |
| R3,R4 | 2.2K | SCL 与 SDA 到 VCC_3V3 的 I2C 上拉电阻 | 图 653fd96aeca2 / 第 1 页 / 网格 C2 R3/R4 2.2K 与 SCL/SDA |
| R5 | 10K/1% | U1 I2C_EN 到 VCC_3V3 的模式选择上拉 | 图 653fd96aeca2 / 第 1 页 / 网格 A1-A2 R5 10K/1% 与 U1 I2C_EN pin20 |
| C15-C28,C31,C32 | power decoupling network | U1 VDD_IO/VDD_D/VDD_A/VDD/VDD_RF/VDD_TX/VDD_AM/VDD_DR/AGDC 的去耦 | 图 653fd96aeca2 / 第 1 页 / 网格 B2-B4 U1 电源脚与 C15-C28/C31/C32 |

## 系统结构

### Unit NFC 系统架构

J1 以 +5V 供电并引出 I2C，U3 生成 VCC_3V3；U1 ST25R3916-AQWT 通过 SCL/SDA 与主机通信，使用 X1 27.12MHz 晶振，并经差分 RFO/RFI 匹配网络连接 ANT1 NFC 线圈。

- 参数与网络：`nfc_frontend=U1 ST25R3916-AQWT`；`host_interface=J1 I2C`；`power=U3 TPAP7343D-33FS4`；`clock=X1 27.12MHz`；`antenna=ANT1 ANT_NFC`；`rf_paths=RFO1/RFO2,RFI1/RFI2`
- 证据：图 653fd96aeca2 / 第 1 页 / 完整单页网格 A1-D4

## 核心器件

### ST25R3916-AQWT NFC 前端

U1 明确标为 ST25R3916-AQWT，展开 I2C/SPI 控制脚、IRQ/MCU_CLK、XTO/XTI、RFI1/RFI2、RFO1/RFO2、AAT_A/AAT_B、AGDC 与多组电源地脚。

- 参数与网络：`reference=U1`；`part_number=ST25R3916-AQWT`；`control=I2C_EN,CSI,IRQ,MCU_CLK,BSS,SCLK,MOSI,MISO,CSO`；`rf=RFI1,RFI2,RFO1,RFO2,AAT_A,AAT_B`；`clock=XTO,XTI`
- 证据：图 653fd96aeca2 / 第 1 页 / 网格 A2-B3 U1 pins1-33

## 电源

### +5V 到 VCC_3V3 LDO

U3 TPAP7343D-33FS4 的 VIN pin4 与 EN pin3 同接 +5V，VOUT pin1 输出 VCC_3V3，GND pin2 与 EP pin5 接 GND；C29/C30 各 1uF/50V 位于输入与输出侧。

- 参数与网络：`regulator=U3 TPAP7343D-33FS4`；`input=+5V`；`enable=+5V`；`output=VCC_3V3`；`input_cap=C29 1uF/50V`；`output_cap=C30 1uF/50V`
- 证据：图 653fd96aeca2 / 第 1 页 / 网格 C1 U3、C29/C30、+5V/VCC_3V3

### U1 多电源域与去耦

U1 的 VDD_IO、VDD_D、VDD_A、VDD、VDD_RF、VDD_TX、VDD_AM、VDD_DR 与 AGDC 均连接 VCC_3V3 或各自去耦节点；C15-C28、C31/C32 构成 10nF、1uF 与 10uF 的本地去耦网络。

- 参数与网络：`supply=VCC_3V3`；`domains=VDD_IO,VDD_D,VDD_A,VDD,VDD_RF,VDD_TX,VDD_AM,VDD_DR,AGDC`；`decoupling=C15-C28,C31,C32`；`values=10nF,1uF,10uF`
- 证据：图 653fd96aeca2 / 第 1 页 / 网格 B2-B4 U1 pins1/3/7-11/14/24 与 C15-C28/C31/C32

## 接口

### J1 Grove 四针接口

J1 Grove pin1=SCL、pin2=SDA、pin3=+5V、pin4=GND。

- 参数与网络：`connector=J1 Grove`；`pin1=SCL`；`pin2=SDA`；`pin3=+5V`；`pin4=GND`
- 证据：图 653fd96aeca2 / 第 1 页 / 网格 C2 J1 pins1-4

### 未连接的控制与调谐脚

U1 CSI pin25、IRQ pin27、MCU_CLK pin28、BSS pin29、MOSI pin31、CSO pin2、AAT_A pin18、AAT_B pin19 与 EXT_LM pin17 均在图中标为未连接。

- 参数与网络：`unused=CSI pin25,IRQ pin27,MCU_CLK pin28,BSS pin29,MOSI pin31,CSO pin2,AAT_A pin18,AAT_B pin19,EXT_LM pin17`
- 证据：图 653fd96aeca2 / 第 1 页 / 网格 A2-B2 U1 左右两侧红色 NC 标记

## 总线

### U1 I2C 模式与总线连接

U1 I2C_EN pin20 通过 R5 10K/1% 上拉到 VCC_3V3；SCLK pin30 连接 SCL，MISO pin32 连接 SDA，MOSI pin31 与 CSO pin2 标为未连接。

- 参数与网络：`mode_select=I2C_EN pin20 via R5 10K to VCC_3V3`；`scl=U1 SCLK pin30`；`sda=U1 MISO pin32`；`mosi=pin31 NC`；`cso=pin2 NC`
- 证据：图 653fd96aeca2 / 第 1 页 / 网格 A1-B2 R5、U1 I2C_EN/SCLK/MISO/MOSI/CSO

### I2C 上拉电阻

SCL 与 SDA 分别通过 R3 与 R4 2.2K 上拉到 VCC_3V3，并直接连接 J1 pins1/2。

- 参数与网络：`scl_pullup=R3 2.2K to VCC_3V3`；`sda_pullup=R4 2.2K to VCC_3V3`；`connector=J1 pin1 SCL,pin2 SDA`
- 证据：图 653fd96aeca2 / 第 1 页 / 网格 C2 R3/R4 与 J1 SCL/SDA

## 时钟

### 27.12MHz 外部晶振

X1 标为 27.12MHZ CL20pF，连接 U1 XTO pin4 与 XTI pin5；C12/C14 各 6.0pF/50V 分别从晶振两端接 GND。

- 参数与网络：`crystal=X1 27.12MHZ CL20pF`；`xout=U1 XTO pin4`；`xin=U1 XTI pin5`；`load_caps=C12/C14 6.0pF/50V`
- 证据：图 653fd96aeca2 / 第 1 页 / 网格 B1-B2 X1、C12/C14、U1 XTO/XTI

## 射频

### RFO1/RFO2 差分发射路径

U1 RFO1 pin13 经 L1 270nH 5% 进入上支路，RFO2 pin15 经 L2 270nH 5% 进入下支路；两支路通过对称电容网络连接 ANT1_P/ANT1_N，再经 R1/R2 2.4R 接 ANT1 线圈两端。

- 参数与网络：`positive=RFO1 pin13 -> L1 270nH -> ANT1_P -> R1 2.4R`；`negative=RFO2 pin15 -> L2 270nH -> ANT1_N -> R2 2.4R`；`antenna=ANT1 ANT_NFC`
- 证据：图 653fd96aeca2 / 第 1 页 / 网格 A2-A4 U1 RFO1/RFO2、L1/L2、R1/R2、ANT1

### RFI1/RFI2 差分接收路径

U1 RFI1 pin22 连接 RFI_P，RFI2 pin23 连接 RFI_N；RFI_P/RFI_N 分别经 C2/C11 10pF 与天线差分节点耦合，并各有 C1/C13 220pF 对地。

- 参数与网络：`positive=RFI1 pin22 -> RFI_P -> C2 10pF -> ANT1_P`；`negative=RFI2 pin23 -> RFI_N -> C11 10pF -> ANT1_N`；`shunt_caps=C1/C13 220pF to GND`
- 证据：图 653fd96aeca2 / 第 1 页 / 网格 A2-A4 U1 RFI1/RFI2、RFI_P/RFI_N、C1/C2/C11/C13

### 天线匹配电容配置

上支路使用 C4 150pF、C5 680pF、C6 180pF，下支路使用 C9 150pF、C7 680pF、C8 180pF；C3 与 C10 标为 NC。

- 参数与网络：`upper=C4 150pF,C5 680pF,C6 180pF`；`lower=C9 150pF,C7 680pF,C8 180pF`；`not_populated=C3,C10 NC`；`voltage_rating=50V`
- 证据：图 653fd96aeca2 / 第 1 页 / 网格 A3-A4 C3-C10 匹配网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit NFC 系统架构 | `nfc_frontend=U1 ST25R3916-AQWT`；`host_interface=J1 I2C`；`power=U3 TPAP7343D-33FS4`；`clock=X1 27.12MHz`；`antenna=ANT1 ANT_NFC`；`rf_paths=RFO1/RFO2,RFI1/RFI2` |
| 核心器件 | ST25R3916-AQWT NFC 前端 | `reference=U1`；`part_number=ST25R3916-AQWT`；`control=I2C_EN,CSI,IRQ,MCU_CLK,BSS,SCLK,MOSI,MISO,CSO`；`rf=RFI1,RFI2,RFO1,RFO2,AAT_A,AAT_B`；`clock=XTO,XTI` |
| 电源 | +5V 到 VCC_3V3 LDO | `regulator=U3 TPAP7343D-33FS4`；`input=+5V`；`enable=+5V`；`output=VCC_3V3`；`input_cap=C29 1uF/50V`；`output_cap=C30 1uF/50V` |
| 接口 | J1 Grove 四针接口 | `connector=J1 Grove`；`pin1=SCL`；`pin2=SDA`；`pin3=+5V`；`pin4=GND` |
| 总线 | U1 I2C 模式与总线连接 | `mode_select=I2C_EN pin20 via R5 10K to VCC_3V3`；`scl=U1 SCLK pin30`；`sda=U1 MISO pin32`；`mosi=pin31 NC`；`cso=pin2 NC` |
| 总线 | I2C 上拉电阻 | `scl_pullup=R3 2.2K to VCC_3V3`；`sda_pullup=R4 2.2K to VCC_3V3`；`connector=J1 pin1 SCL,pin2 SDA` |
| 接口 | 未连接的控制与调谐脚 | `unused=CSI pin25,IRQ pin27,MCU_CLK pin28,BSS pin29,MOSI pin31,CSO pin2,AAT_A pin18,AAT_B pin19,EXT_LM pin17` |
| 时钟 | 27.12MHz 外部晶振 | `crystal=X1 27.12MHZ CL20pF`；`xout=U1 XTO pin4`；`xin=U1 XTI pin5`；`load_caps=C12/C14 6.0pF/50V` |
| 射频 | RFO1/RFO2 差分发射路径 | `positive=RFO1 pin13 -> L1 270nH -> ANT1_P -> R1 2.4R`；`negative=RFO2 pin15 -> L2 270nH -> ANT1_N -> R2 2.4R`；`antenna=ANT1 ANT_NFC` |
| 射频 | RFI1/RFI2 差分接收路径 | `positive=RFI1 pin22 -> RFI_P -> C2 10pF -> ANT1_P`；`negative=RFI2 pin23 -> RFI_N -> C11 10pF -> ANT1_N`；`shunt_caps=C1/C13 220pF to GND` |
| 射频 | 天线匹配电容配置 | `upper=C4 150pF,C5 680pF,C6 180pF`；`lower=C9 150pF,C7 680pF,C8 180pF`；`not_populated=C3,C10 NC`；`voltage_rating=50V` |
| 电源 | U1 多电源域与去耦 | `supply=VCC_3V3`；`domains=VDD_IO,VDD_D,VDD_A,VDD,VDD_RF,VDD_TX,VDD_AM,VDD_DR,AGDC`；`decoupling=C15-C28,C31,C32`；`values=10nF,1uF,10uF` |
| 总线地址 | I2C 地址与速率 | `documented_address=0x50`；`documented_speeds=100K,400K`；`address_shown_on_schematic=false`；`address_select_shown=false` |
| 射频 | NFC 协议与工作模式 | `documented_reader=NFC-A/B,NFC-F,NFC-V`；`documented_standards=ISO14443A,ISO14443B,FeliCa,ISO15693`；`documented_emulation=NFC-A,NFC-F`；`documented_custom_protocol=true`；`firmware_version=null` |
| 射频 | 13.56MHz 工作频率与读写距离 | `documented_carrier_mhz=13.56`；`documented_max_distance_mm=40`；`crystal_mhz=27.12`；`test_card=null`；`field_strength=null` |
| 射频 | 自动天线调谐能力 | `documented_auto_tuning=true`；`aat_a=pin18 NC`；`aat_b=pin19 NC`；`tuning_method=null`；`tuning_range=null` |
| 电源 | 各工作状态功耗 | `sleep=5V@19.33uA`；`unconfigured=5V@19.79uA`；`continuous_read=5V@67.65mA`；`intermittent_read=5V@66.48mA`；`test_conditions=null` |
| 系统结构 | 产品尺寸与重量 | `documented_size_mm=48.0x24.0x8.0`；`documented_weight_g=5.9`；`mechanical_drawing_in_assets=false` |
| 系统结构 | 产品认证声明 | `documented_certifications=CE,FCC,RoHS,WEEE,MIC`；`certificate_numbers=null`；`standards=null` |
| 系统结构 | 原理图版本与 U216 对应关系 | `resource_version=V0.1`；`resource_date=2025-11-28`；`title_block_date=11/28/2025`；`title=null`；`number=null`；`revision=null`；`sku_mark=null` |

## 待确认事项

- `address.documented-i2c-address-speed`：源文档规格称 I2C 地址为 0x50，支持 100K 与 400K；原理图确认 I2C 模式和 SCL/SDA 连接，但没有打印地址、地址选择引脚、速率或时序参数。（证据：图 653fd96aeca2 / 第 1 页 / U1 I2C_EN/SCLK/MISO 与 J1 SCL/SDA，页面无 0x50 或速率文字）
- `rf.documented-protocols-modes`：源文档称支持 ISO14443A/B、FeliCa、ISO15693，以及读写器、卡模拟和自定义协议模式；原理图只描述 ST25R3916、天线与 I2C 硬件，未列协议栈、固件版本或模式限制。（证据：图 653fd96aeca2 / 第 1 页 / U1 与 ANT1 硬件图，无协议或模式文字）
- `rf.documented-frequency-distance`：源文档规格称工作频率为 13.56MHz、读写距离不超过 40mm；原理图标出 27.12MHz 晶振和 ANT1 匹配网络，但未标载波频率、卡片类型、场强、天线方向或距离测试条件。（证据：图 653fd96aeca2 / 第 1 页 / X1 27.12MHz 与 ANT1 匹配网络，无 13.56MHz/40mm 标注）
- `rf.documented-automatic-tuning`：源文档描述自动天线调谐能力，而原理图将 U1 AAT_A pin18 与 AAT_B pin19 标为未连接；当前页面无法确认该产品使用的调谐机制、调谐范围或固件配置。（证据：图 653fd96aeca2 / 第 1 页 / U1 AAT_A/AAT_B pins18/19 红色 NC 标记）
- `power.documented-consumption`：源文档列休眠 5V@19.33uA、上电未设置 5V@19.79uA、连续读卡 5V@67.65mA、间断读卡 5V@66.48mA；原理图没有电流测试点、固件状态、卡片条件、仪器或环境参数。（证据：图 653fd96aeca2 / 第 1 页 / +5V/VCC_3V3 电源图，无电流或状态标注）
- `system.documented-mechanical`：源文档规格列产品尺寸 48.0x24.0x8.0mm、产品重量 5.9g；当前电气原理图没有板框、天线外形、LEGO 孔尺寸、机械公差或质量信息。（证据：图 653fd96aeca2 / 第 1 页 / 电气原理图无机械尺寸或质量标注）
- `system.documented-certifications`：源文档列 CE、FCC、RoHS、WEEE 与 MIC；原理图没有证书编号、测试报告、适用地区、标准版本或认证标识。（证据：图 653fd96aeca2 / 第 1 页 / 完整页面无认证编号或标识）
- `system.asset-version-binding`：资源文件名包含 SCH_Unit_NFC_V0.1 与 2025_11_28，标题栏日期为 11/28/2025；标题、Number、Revision 和 Drawn By 字段为空，页面未打印 U216，无法由图面独立确认该版本与当前量产硬件完全一致。（证据：图 653fd96aeca2 / 第 1 页 / 网格 D3-D4 标题栏与日期 11/28/2025）
- `review.i2c-address-speed`：U216 的 7-bit I2C 地址是否固定为 0x50，100K/400K 的时序边界和总线条件是什么？；原因：地址与速率仅见于源文档，原理图没有地址或时序标注。
- `review.protocols-modes`：当前硬件与驱动库实际覆盖哪些 ISO14443A/B、FeliCa、ISO15693、卡模拟和自定义协议功能及限制？；原因：协议与模式取决于芯片能力、固件和驱动，图面没有协议栈信息。
- `review.frequency-distance`：13.56MHz 载波与不超过 40mm 读写距离使用的卡片类型、姿态、场强和环境条件是什么？；原因：原理图只有晶振和匹配网络，没有载波或距离测试条件。
- `review.automatic-tuning`：源文档所称自动天线调谐如何实现，AAT_A/AAT_B 未连接时使用哪些测量和调谐路径？；原因：图面将 AAT_A/AAT_B 标为 NC，与功能描述无法直接闭环。
- `review.power-consumption`：四组功耗数值的固件版本、卡片、天线姿态、测量点、仪器和环境条件是什么？；原因：原理图无法验证运行状态和电流测试条件。
- `review.mechanical`：48.0x24.0x8.0mm 外形与 5.9g 重量由哪份当前机械图和量产配置确认？；原因：当前资产仅含电气原理图。
- `review.certifications`：CE、FCC、RoHS、WEEE、MIC 的证书编号、标准版本、适用型号和地区是什么？；原因：源文档只有认证名称，原理图没有证书或测试信息。
- `review.asset-version-binding`：V0.1、2025-11-28 原理图对应 U216 的哪个 PCB Revision，是否与当前量产硬件一致？；原因：标题栏 Revision、Number 和产品/SKU 字段为空。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `653fd96aeca26bcf340c4f8aed60a290bda122da875673aa4e4c87e153e59741` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/SCH_Unit_NFC_V0.1_2025_11_28_12_15_35_page_01.png` |

---

源文档：`zh_CN/unit/Unit_NFC.md`

源文档 SHA-256：`1bad8e7b1b1f1ad680e4bf8eb3045697b85d067192f6c4379ccc7d66fa726d7a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
