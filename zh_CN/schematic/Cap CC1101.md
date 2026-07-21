# Cap CC1101 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Cap CC1101 |
| SKU | U219 |
| 产品 ID | `cap-cc1101-bc3594f2539a` |
| 源文档 | `zh_CN/cap/Cap_CC1101.md` |

## 概述

Cap CC1101 通过共享 SPI 总线连接 CC1101RGPR Sub-1GHz 收发器与 ST25R3916-AQWT NFC 控制器，并由 P1 2×7P Cap-Bus 引出片选、中断、射频开关、GDO 和电源控制信号。CC1101 的差分 RF 经 B0310J50100AHF 巴伦、两颗 BGS13SN8E6327XTSA1 射频开关和 315/433/868-915MHz 三路匹配网络汇聚到 E1 SMA 天线；ST25R3916 使用独立差分 ANT_NFC 线圈和 27.12MHz 晶振。JW5712 将 +5VOUT 转换为 VDD_3V3，POWER_EN 控制稳压器；原理图射频真值表与产品正文的 315MHz 控制组合不一致，需按硬件版本复核。

## 检索关键词

`Cap CC1101`、`U219`、`CC1101RGPR`、`ST25R3916-AQWT`、`JW5712`、`BGS13SN8E6327XTSA1`、`B0310J50100AHF`、`SPI`、`SPI_SCLK`、`SPI_MOSI`、`SPI_MISO`、`CC1101_CS`、`CC1101_G0`、`CC1101_RF_SW0`、`CC1101_RF_SW1`、`NFC_CS`、`NFC_IRQ`、`POWER_EN`、`VDD_3V3`、`+5VOUT`、`315MHz`、`433MHz`、`868MHz`、`915MHz`、`ANT_NFC`、`CC1101_RF`、`RFI_P`、`RFI_N`、`ANT_P`、`ANT_N`、`27.12MHz`、`26MHz`、`SMA`、`Grove`、`SP3T`、`NFC`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | JW5712 | 由 +5VOUT 产生 VDD_3V3 的同步降压转换器 | 图 7306e2a34d40 / 第 1 页 / B1-C2：U1 JW5712、POWER_EN、VIN/SW/VOS/VSEL1~3、L1 与电容 |
| L1 | MWTC201608S2R2 | JW5712 降压输出电感 | 图 7306e2a34d40 / 第 1 页 / B2：L1 MWTC201608S2R2 位于 U1 SW 与 VDD_3V3 之间 |
| P1 | HDR_14P-2.54 | 2×7P Cap-Bus 主连接器，连接电源、共享 SPI、NFC、CC1101 与控制网络 | 图 7306e2a34d40 / 第 1 页 / B3-C4：P1 HDR_14P-2.54 1~14 脚和 Cardputer-Adv PIN MAP |
| J1 | GROVE 4P | SCL、SDA、+5VOUT、GND 的 Grove 扩展接口 | 图 7306e2a34d40 / 第 1 页 / C1-D1：J1 GROVE 4P、SCL/SDA/+5VOUT/GND |
| U2 | ST25R3916-AQWT | SPI NFC 读写/卡模拟前端，驱动 ANT_NFC 差分天线 | 图 da5bc52a4444 / 第 1 页 / B1-C3：U2 ST25R3916-AQWT、SPI/IRQ、RFI/RFO 与供电脚 |
| Y1 | 27.12MHZ | ST25R3916 XTI/XTO 参考晶振 | 图 da5bc52a4444 / 第 1 页 / C1-C2：Y1 27.12MHZ、C19/C20 6.0pF、U2 XTO/XTI |
| L2/L3 | 270nH 5% | ST25R3916 RFO1/RFO2 到 NFC 差分匹配网络的串联电感 | 图 da5bc52a4444 / 第 1 页 / B2-B3：U2 RFO1-L2、RFO2-L3 与 ANT1_P/ANT1_N 网络 |
| ANT1 | ANT_NFC | ST25R3916 的差分 NFC 线圈天线 | 图 da5bc52a4444 / 第 1 页 / B3：ANT1 线圈，R2/R3 1.5Ω 串联，网络名 ANT_NFC |
| U3 | CC1101RGPR | 共享 SPI 的 Sub-1GHz 射频收发器 | 图 85f5c961e5cc / 第 1 页 / A1-B2：U3 CC1101RGPR、SPI/GDO、RF_P/RF_N、XOSC_Q1/Q2 |
| Y2 | Y2016 26MHz | CC1101 XOSC_Q1/XOSC_Q2 参考晶振 | 图 85f5c961e5cc / 第 1 页 / A2-B2：Y2 Y2016 26MHz、C47/C49 12pF 与 U3 XOSC_Q1/Q2 |
| B1 | B0310J50100AHF | CC1101 RF_P/RF_N 差分到单端的巴伦/匹配器件 | 图 85f5c961e5cc / 第 1 页 / A2-B3：B1 B0310J50100AHF，Balanced/Unbalanced 引脚与 ANT_P/ANT_N |
| U4/U5 | BGS13SN8E6327XTSA1 | 双 SP3T 射频开关，选择 315/433/868-915MHz 匹配支路并汇聚到天线 | 图 85f5c961e5cc / 第 1 页 / C1-D3：U4/U5 BGS13SN8E6327XTSA1、RFin/RF1/RF2/RF3、V1/V2 |
| L6/L7/L8/L17/C50/C51 | 315MHz matching | 315MHz 频段匹配支路 | 图 85f5c961e5cc / 第 1 页 / B1-C3：315MHz频段，L6 10nH、L7 0R、L8 10nH、L17 3.6nH、C50 8pF、C51 DNP |
| L10/L11/L12/L13/C53/C54/C55 | 433MHz matching | 433MHz 频段匹配支路 | 图 85f5c961e5cc / 第 1 页 / C1-C3：433MHz频段，L10/L11/L13 0R、L12 15nH、C53 10pF、C54 NC、C55 6.2pF |
| L15/L16/C58/C59 | 868/915MHz matching | 868/915MHz 频段匹配支路 | 图 85f5c961e5cc / 第 1 页 / C1-D3：868MHz频段，L15 0R、L16 10nH、C58 NC、C59 DNP；真值表列 868MHz/915MHz |
| E1 | SMA-TH_KH-SMA-KE-Z | CC1101_RF 外部 SMA 天线连接器 | 图 85f5c961e5cc / 第 1 页 / D3-D4：E1 SMA-TH_KH-SMA-KE-Z、R7 0R、CC1101_RF 与 GND |
| D1/C60/C61 | NC | SMA 端口预留的未装保护/匹配器件 | 图 85f5c961e5cc / 第 1 页 / D3-D4：E1 旁 D1 NC、C60 NC、C61 NC |

## 系统结构

### Cap CC1101 系统架构

模块由 CC1101 Sub-1GHz 射频链、ST25R3916 NFC 差分天线链、JW5712 3.3V 电源和 P1/J1 外部接口组成；CC1101 与 ST25R3916 共用 SPI_SCLK/SPI_MOSI/SPI_MISO。

- 参数与网络：`sub_1ghz=U3 CC1101RGPR`；`nfc=U2 ST25R3916-AQWT`；`power=U1 JW5712`；`host=P1 HDR_14P-2.54`；`grove=J1 GROVE 4P`；`shared_bus=SPI_SCLK,SPI_MOSI,SPI_MISO`
- 证据：图 7306e2a34d40 / 第 1 页 / B1-D4：电源、P1 与 J1; 图 da5bc52a4444 / 第 1 页 / B1-C4：ST25R3916 NFC; 图 85f5c961e5cc / 第 1 页 / A1-D4：CC1101 与多频段射频链

## 核心器件

### U3 CC1101RGPR 数字连接

U3.1/2/20/7 分别连接 SPI_SCLK、SPI_MISO、SPI_MOSI、CC1101_CS；GDO0 经 R4 330Ω连接 CC1101_G0，GDO2 直接连接 CC1101_RF_SW1。

- 参数与网络：`sclk=U3.1`；`miso=U3.2`；`mosi=U3.20`；`csn=U3.7 CC1101_CS`；`gdo0=U3.6-R4 330Ω-CC1101_G0`；`gdo2=U3.3 CC1101_RF_SW1`
- 证据：图 85f5c961e5cc / 第 1 页 / A1-A2：U3 SCLK/MISO/MOSI/CSN/GDO0/GDO2 与 R4

## 电源

### U1 JW5712

U1 VIN 接 +5/+5VOUT，POWER_EN 接 EN；SW 经 L1 MWTC201608S2R2 产生 VDD_3V3，图面标注 IOUT 0~0.6A。

- 参数与网络：`input=+5 / +5VOUT`；`enable=POWER_EN`；`converter=JW5712`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`output_current_note=0~0.6A`
- 证据：图 7306e2a34d40 / 第 1 页 / B1-C2：U1、L1、+5/+5VOUT、POWER_EN、VDD_3V3 与 IOUT 注释

### JW5712 输入输出网络

输入端使用 C5 22uF 与 C6 100nF；R1 100KΩ将 POWER_EN 上拉到 +5/+5VOUT；输出端包含 C1 1nF 与 C2/C3/C4 各 22uF。

- 参数与网络：`input_caps=C5 22uF,C6 100nF`；`enable_pullup=R1 100KΩ`；`switch_cap=C1 1nF`；`output_caps=C2,C3,C4 22uF`
- 证据：图 7306e2a34d40 / 第 1 页 / B1-C3：R1、C1~C6 与 U1/L1

### JW5712 VSEL1~VSEL3

U1 的 VSEL1、VSEL2、VSEL3 均连接 +5 网络。

- 参数与网络：`vsel1=U1.C1 to +5`；`vsel2=U1.D1 to +5`；`vsel3=U1.D2 to +5`
- 证据：图 7306e2a34d40 / 第 1 页 / B1-C2：U1 VSEL1/C1、VSEL2/D1、VSEL3/D2 共接 +5

### ST25R3916 供电

U2 的 VDD_IO 接 VDD_3V3；图中 VDD、VDD_RF、VDD_TX 等电源脚配置 C21~C36 的 10nF/10uF 去耦组，部分主电源节点标注 +5V。

- 参数与网络：`io_supply=U2.1 VDD_IO=VDD_3V3`；`power_pins=VDD_D,VDD_A,VDD,VDD_RF,VDD_TX,VDD_AM,VDD_DR,AGDC`；`decoupling=C21~C36 alternating 10nF/10uF`；`five_volt_labels=visible on VDD/VDD_TX-area rails`
- 证据：图 da5bc52a4444 / 第 1 页 / C2-C4：U2 电源脚、VDD_3V3/+5V 标注与 C21~C36

### CC1101 VDD_3V3

U3 DVDD 与各 AVDD 脚连接 VDD_3V3，并由 C37~C41 五颗 100nF 电容去耦；DCOUPL 以 C48 100nF 对 GND，RBIAS 以 R6 56KΩ接 GND。

- 参数与网络：`supply=VDD_3V3`；`supply_pins=U3.4 DVDD,U3.9/11/14/15/18 AVDD`；`supply_caps=C37~C41 100nF`；`dcoupl=U3.5-C48 100nF-GND`；`rbias=U3.17-R6 56KΩ-GND`
- 证据：图 85f5c961e5cc / 第 1 页 / A1-B2：U3 电源脚、C37~C41、DCOUPL/C48、RBIAS/R6

## 接口

### P1 HDR_14P-2.54

P1.1=CC1101_G0，2=CC1101_RF_SW0，3=SCL/G1，4=SDA/G0，5=+5VOUT，6=GND，7=+5VIN，8=POWER_EN/G3，9=NFC_IRQ/G4，10=NFC_CS/G6，11=SPI_SCLK/G40，12=SPI_MOSI/G14，13=SPI_MISO/G39，14=CC1101_CS/G5。

- 参数与网络：`pins_1_7=1:CC1101_G0/G15,2:CC1101_RF_SW0/G13,3:SCL/G1,4:SDA/G0,5:+5VOUT,6:GND,7:+5VIN`；`pins_8_14=8:POWER_EN/G3,9:NFC_IRQ/G4,10:NFC_CS/G6,11:SPI_SCLK/G40,12:SPI_MOSI/G14,13:SPI_MISO/G39,14:CC1101_CS/G5`
- 证据：图 7306e2a34d40 / 第 1 页 / B3-C4：P1 1~14 脚、左右网络与 Cardputer-Adv PIN MAP

### J1 GROVE 4P

J1.1=SCL，J1.2=SDA，J1.3=+5VOUT，J1.4=GND。

- 参数与网络：`pin_1=SCL`；`pin_2=SDA`；`pin_3=+5VOUT`；`pin_4=GND`
- 证据：图 7306e2a34d40 / 第 1 页 / C1-D1：J1 GROVE 4P 四脚网络

### E1 SMA 天线接口

U5.RFin 经 L9 2.2nH 形成 CC1101_RF；E1 中心端经 R7 0Ω连接同名 CC1101_RF，外壳接 GND。D1、C60、C61 均标记 NC。

- 参数与网络：`switch_output=U5.6 RFin`；`series_inductor=L9 2.2nH`；`rf_net=CC1101_RF`；`connector=E1 SMA-TH_KH-SMA-KE-Z`；`series_link=R7 0R`；`ground=E1 shell`；`not_fitted=D1,C60,C61 NC`
- 证据：图 85f5c961e5cc / 第 1 页 / C3-D4：U5 RFin、C52/L9/CC1101_RF、E1、D1/C60/R7/C61

## 总线

### 共享 SPI 总线

SPI_SCLK、SPI_MOSI、SPI_MISO 从 P1.11/12/13 同时连接 U2 ST25R3916 的 SCLK/MOSI/MISO 和 U3 CC1101 的 SCLK/MOSI/MISO；两器件使用独立 NFC_CS 与 CC1101_CS。

- 参数与网络：`sclk=P1.11-U2.30-U3.1`；`mosi=P1.12-U2.31-U3.20`；`miso=P1.13-U2.32-U3.2`；`nfc_cs=P1.10 NFC_CS-U2.29 BSS`；`cc1101_cs=P1.14 CC1101_CS-U3.7 CSN`
- 证据：图 7306e2a34d40 / 第 1 页 / B3-C4：P1 SPI 与片选网络; 图 da5bc52a4444 / 第 1 页 / B1-C2：U2 NFC_CS/SCLK/MOSI/MISO; 图 85f5c961e5cc / 第 1 页 / A1-A2：U3 SCLK/MISO/MOSI/CSN

## GPIO 与控制信号

### NFC_IRQ

U2.27 IRQ 连接 NFC_IRQ，并从 P1.9（INT/G4）引出；U2.28 MCU_CLK 标记未连接。

- 参数与网络：`irq=U2.27 NFC_IRQ-P1.9/G4`；`mcu_clk=U2.28 no-connect`
- 证据：图 da5bc52a4444 / 第 1 页 / B1-C2：U2 IRQ/MCU_CLK; 图 7306e2a34d40 / 第 1 页 / B3：P1.9 NFC_IRQ G4

### U4/U5 射频开关控制

U4.V1=CC1101_RF_SW1、U4.V2=CC1101_RF_SW0；U5.V1=CC1101_RF_SW0、U5.V2=CC1101_RF_SW1。CC1101_RF_SW0 从 P1.2 引入，CC1101_RF_SW1 由 U3 GDO2 输出。

- 参数与网络：`u4_v1=CC1101_RF_SW1`；`u4_v2=CC1101_RF_SW0`；`u5_v1=CC1101_RF_SW0`；`u5_v2=CC1101_RF_SW1`；`rf_sw0_source=P1.2/G13`；`rf_sw1_source=U3.3 GDO2`
- 证据：图 7306e2a34d40 / 第 1 页 / B3-C4：P1.2 CC1101_RF_SW0; 图 85f5c961e5cc / 第 1 页 / A1 与 C1-D3：U3 GDO2=CC1101_RF_SW1，U4/U5 V1/V2

## 时钟

### Y1 / ST25R3916

U2 XTO/XTI 使用 Y1 27.12MHz 晶振，两端各以 C19/C20 6.0pF 对 GND。

- 参数与网络：`crystal=Y1 27.12MHz`；`pins=U2.4 XTO,U2.5 XTI`；`load_caps=C19 6.0pF,C20 6.0pF`
- 证据：图 da5bc52a4444 / 第 1 页 / C1-C2：U2 XTO/XTI、Y1、C19/C20

### Y2 / CC1101

U3 XOSC_Q1/XOSC_Q2 使用 Y2 Y2016 26MHz 晶振，两端各以 C47/C49 12pF 对 GND。

- 参数与网络：`crystal=Y2 Y2016 26MHz`；`pins=U3.8 XOSC_Q1,U3.10 XOSC_Q2`；`load_caps=C47 12pF,C49 12pF`
- 证据：图 85f5c961e5cc / 第 1 页 / A2-B2：U3 XOSC_Q1/Q2、Y2、C47/C49

## 复位

### P1 RESET / POWER_EN

P1.8 的连接器功能名为 RESET，但板内网络名为 POWER_EN，并连接 U1 EN；R1 100KΩ将该网络上拉到 +5/+5VOUT。

- 参数与网络：`connector_pin=P1.8 RESET`；`board_net=POWER_EN`；`destination=U1.EN`；`pullup=R1 100KΩ to +5/+5VOUT`
- 证据：图 7306e2a34d40 / 第 1 页 / B1 与 B3：POWER_EN 到 U1.EN；P1.8 RESET/POWER_EN G3

## 保护电路

### SMA 端口保护预留

E1 信号端到 GND 的 D1 保护位以及 C60/C61 匹配位均标记 NC，因此当前原理图未装这些保护/调谐器件。

- 参数与网络：`esd_position=D1 NC`；`shunt_caps=C60 NC,C61 NC`；`series=R7 0R`
- 证据：图 85f5c961e5cc / 第 1 页 / D3-D4：E1 旁 D1/C60/C61 的 NC 标注

## 存储

### 存储/FIFO

三张原理图未绘制独立 Flash、EEPROM、SD 卡或外部 FIFO 存储器；器件内部存储容量不在图面标注。

- 参数与网络：`flash=none shown`；`eeprom=none shown`；`sd=none shown`；`external_fifo=none shown`
- 证据：图 7306e2a34d40 / 第 1 页 / 电源/接口页无存储器; 图 da5bc52a4444 / 第 1 页 / NFC 页仅 U2、晶振、匹配与去耦; 图 85f5c961e5cc / 第 1 页 / Sub-1GHz 页仅 U3、RF 开关与匹配网络

## 内存与 Flash

### 外部 RAM

三张原理图未绘制独立 RAM 或其他外部易失性存储器。

- 参数与网络：`ram=none shown`
- 证据：图 7306e2a34d40 / 第 1 页 / 电源/接口页全页无 RAM; 图 da5bc52a4444 / 第 1 页 / NFC 页全页无 RAM; 图 85f5c961e5cc / 第 1 页 / Sub-1GHz 页全页无 RAM

## 音频

### 音频电路

三张原理图未绘制音频编解码器、麦克风、扬声器或音频接口。

- 参数与网络：`codec=none shown`；`microphone=none shown`；`speaker=none shown`
- 证据：图 7306e2a34d40 / 第 1 页 / 电源/接口页无音频器件; 图 da5bc52a4444 / 第 1 页 / NFC 页无音频器件; 图 85f5c961e5cc / 第 1 页 / Sub-1GHz 页无音频器件

## 射频

### ST25R3916 NFC 天线链

U2 RFO1/RFO2 分别经 L2/L3 270nH 进入 ANT1_P/ANT1_N 匹配网络，最终经 R2/R3 1.5Ω驱动差分 ANT1；RFI1/RFI2 分别形成 RFI_P/RFI_N 返回路径。

- 参数与网络：`tx_positive=U2.13 RFO1-L2 270nH-ANT1_P-R2 1.5Ω-ANT1`；`tx_negative=U2.15 RFO2-L3 270nH-ANT1_N-R3 1.5Ω-ANT1`；`rx_positive=U2.22 RFI1/RFI_P`；`rx_negative=U2.23 RFI2/RFI_N`；`antenna=ANT1 ANT_NFC`
- 证据：图 da5bc52a4444 / 第 1 页 / B2-B4：U2 RFO/RFI、L2/L3、C7~C18、R2/R3 与 ANT1

### ANT_NFC 匹配网络

NFC 网络包含 C7/C10/C18 220pF、C8/C17 10pF、C11/C13 680pF、C12/C14 150pF、C15 180pF，C9/C16 标记 DNP。

- 参数与网络：`220pf=C7,C10,C18`；`10pf=C8,C17`；`680pf=C11,C13`；`150pf=C12,C14`；`180pf=C15`；`dnp=C9,C16`
- 证据：图 da5bc52a4444 / 第 1 页 / A3-C4：C7~C18 数值与 ANT1_P/ANT1_N/RFI_P/RFI_N

### CC1101 差分到单端匹配

U3 RF_N/RF_P 经 C42/C46 100pF、C43 0.6pF 等网络形成 ANT_N/ANT_P，并送入 B1 B0310J50100AHF；B1 单端侧继续经 L4 3.3nH、L5 6.8nH、R5 0Ω和 C45 1.2pF 到频段开关。

- 参数与网络：`rf_negative=U3.13 RF_N`；`rf_positive=U3.12 RF_P`；`series_caps=C42 100pF,C46 100pF`；`cross_cap=C43 0.6pF`；`balun=B1 B0310J50100AHF`；`single_ended_matching=L4 3.3nH,L5 6.8nH,R5 0R,C45 1.2pF`；`dnp=C44 DNP`
- 证据：图 85f5c961e5cc / 第 1 页 / A2-B4：U3 RF_N/RF_P、C42/C43/C46、B1、L4/L5、C44/C45、R5

### 射频频段选择真值表

原理图真值表明确给出 RF_SW0/RF_SW1=0/1 选择 315MHz，1/0 选择 433MHz，1/1 选择 868MHz/915MHz。

- 参数与网络：`315mhz=RF_SW0=0,RF_SW1=1`；`433mhz=RF_SW0=1,RF_SW1=0`；`868_915mhz=RF_SW0=1,RF_SW1=1`；`00=not listed`
- 证据：图 85f5c961e5cc / 第 1 页 / D1：RF_SW0/RF_SW1 与 315MHz/433MHz/868MHz-915MHz 真值表

### 315MHz 匹配支路

315MHz 支路连接 U4.RF1 与 U5.RF1，串联 L6 10nH、L7 0R、L8 10nH；L17 3.6nH 与 C50 8pF 组成对地支路，C51 为 DNP。

- 参数与网络：`path=U4.RF1-L6-L7-L8-U5.RF1`；`series=L6 10nH,L7 0R,L8 10nH`；`shunt=L17 3.6nH + C50 8pF to GND`；`dnp=C51`
- 证据：图 85f5c961e5cc / 第 1 页 / B1-C3：315MHz频段完整支路

### 433MHz 匹配支路

433MHz 支路连接 U4.RF2 与 U5.RF2，串联 L10 0R、L11 0R、L12 15nH、L13 0R；C53 10pF 与 C55 6.2pF 对地，C54 标记 NC。

- 参数与网络：`path=U4.RF2-L10-L11-L12-L13-U5.RF2`；`series=L10 0R,L11 0R,L12 15nH,L13 0R`；`shunt=C53 10pF,C55 6.2pF`；`nc=C54`
- 证据：图 85f5c961e5cc / 第 1 页 / C1-C3：433MHz频段完整支路

### 868/915MHz 匹配支路

868MHz 标注支路连接 U4.RF3 与 U5.RF3，串联 L15 0R、L16 10nH，C58 标记 NC、C59 标记 DNP；真值表将该支路标为 868MHz/915MHz。

- 参数与网络：`path=U4.RF3-L15-L16-U5.RF3`；`series=L15 0R,L16 10nH`；`nc=C58`；`dnp=C59`；`truth_table_band=868MHz/915MHz`
- 证据：图 85f5c961e5cc / 第 1 页 / C1-D3：868MHz频段支路与 D1 真值表 868MHz/915MHz 列

## 调试与烧录

### 调试接口

原理图未绘制 JTAG/SWD 或专用调试连接器；可访问控制与总线信号均通过 P1 和 J1 引出。

- 参数与网络：`jtag=none shown`；`swd=none shown`；`available_headers=P1 HDR_14P-2.54,J1 GROVE 4P`
- 证据：图 7306e2a34d40 / 第 1 页 / 接口页仅 P1/J1，无 JTAG/SWD

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Cap CC1101 系统架构 | `sub_1ghz=U3 CC1101RGPR`；`nfc=U2 ST25R3916-AQWT`；`power=U1 JW5712`；`host=P1 HDR_14P-2.54`；`grove=J1 GROVE 4P`；`shared_bus=SPI_SCLK,SPI_MOSI,SPI_MISO` |
| 电源 | U1 JW5712 | `input=+5 / +5VOUT`；`enable=POWER_EN`；`converter=JW5712`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`output_current_note=0~0.6A` |
| 电源 | JW5712 输入输出网络 | `input_caps=C5 22uF,C6 100nF`；`enable_pullup=R1 100KΩ`；`switch_cap=C1 1nF`；`output_caps=C2,C3,C4 22uF` |
| 电源 | JW5712 VSEL1~VSEL3 | `vsel1=U1.C1 to +5`；`vsel2=U1.D1 to +5`；`vsel3=U1.D2 to +5` |
| 接口 | P1 HDR_14P-2.54 | `pins_1_7=1:CC1101_G0/G15,2:CC1101_RF_SW0/G13,3:SCL/G1,4:SDA/G0,5:+5VOUT,6:GND,7:+5VIN`；`pins_8_14=8:POWER_EN/G3,9:NFC_IRQ/G4,10:NFC_CS/G6,11:SPI_SCLK/G40,12:SPI_MOSI/G14,13:SPI_MISO/G39,14:CC1101_CS/G5` |
| 接口 | J1 GROVE 4P | `pin_1=SCL`；`pin_2=SDA`；`pin_3=+5VOUT`；`pin_4=GND` |
| 总线 | 共享 SPI 总线 | `sclk=P1.11-U2.30-U3.1`；`mosi=P1.12-U2.31-U3.20`；`miso=P1.13-U2.32-U3.2`；`nfc_cs=P1.10 NFC_CS-U2.29 BSS`；`cc1101_cs=P1.14 CC1101_CS-U3.7 CSN` |
| GPIO 与控制信号 | NFC_IRQ | `irq=U2.27 NFC_IRQ-P1.9/G4`；`mcu_clk=U2.28 no-connect` |
| 复位 | P1 RESET / POWER_EN | `connector_pin=P1.8 RESET`；`board_net=POWER_EN`；`destination=U1.EN`；`pullup=R1 100KΩ to +5/+5VOUT` |
| 时钟 | Y1 / ST25R3916 | `crystal=Y1 27.12MHz`；`pins=U2.4 XTO,U2.5 XTI`；`load_caps=C19 6.0pF,C20 6.0pF` |
| 时钟 | Y2 / CC1101 | `crystal=Y2 Y2016 26MHz`；`pins=U3.8 XOSC_Q1,U3.10 XOSC_Q2`；`load_caps=C47 12pF,C49 12pF` |
| 射频 | ST25R3916 NFC 天线链 | `tx_positive=U2.13 RFO1-L2 270nH-ANT1_P-R2 1.5Ω-ANT1`；`tx_negative=U2.15 RFO2-L3 270nH-ANT1_N-R3 1.5Ω-ANT1`；`rx_positive=U2.22 RFI1/RFI_P`；`rx_negative=U2.23 RFI2/RFI_N`；`antenna=ANT1 ANT_NFC` |
| 射频 | ANT_NFC 匹配网络 | `220pf=C7,C10,C18`；`10pf=C8,C17`；`680pf=C11,C13`；`150pf=C12,C14`；`180pf=C15`；`dnp=C9,C16` |
| 电源 | ST25R3916 供电 | `io_supply=U2.1 VDD_IO=VDD_3V3`；`power_pins=VDD_D,VDD_A,VDD,VDD_RF,VDD_TX,VDD_AM,VDD_DR,AGDC`；`decoupling=C21~C36 alternating 10nF/10uF`；`five_volt_labels=visible on VDD/VDD_TX-area rails` |
| 核心器件 | U3 CC1101RGPR 数字连接 | `sclk=U3.1`；`miso=U3.2`；`mosi=U3.20`；`csn=U3.7 CC1101_CS`；`gdo0=U3.6-R4 330Ω-CC1101_G0`；`gdo2=U3.3 CC1101_RF_SW1` |
| 电源 | CC1101 VDD_3V3 | `supply=VDD_3V3`；`supply_pins=U3.4 DVDD,U3.9/11/14/15/18 AVDD`；`supply_caps=C37~C41 100nF`；`dcoupl=U3.5-C48 100nF-GND`；`rbias=U3.17-R6 56KΩ-GND` |
| 射频 | CC1101 差分到单端匹配 | `rf_negative=U3.13 RF_N`；`rf_positive=U3.12 RF_P`；`series_caps=C42 100pF,C46 100pF`；`cross_cap=C43 0.6pF`；`balun=B1 B0310J50100AHF`；`single_ended_matching=L4 3.3nH,L5 6.8nH,R5 0R,C45 1.2pF`；`dnp=C44 DNP` |
| GPIO 与控制信号 | U4/U5 射频开关控制 | `u4_v1=CC1101_RF_SW1`；`u4_v2=CC1101_RF_SW0`；`u5_v1=CC1101_RF_SW0`；`u5_v2=CC1101_RF_SW1`；`rf_sw0_source=P1.2/G13`；`rf_sw1_source=U3.3 GDO2` |
| 射频 | 射频频段选择真值表 | `315mhz=RF_SW0=0,RF_SW1=1`；`433mhz=RF_SW0=1,RF_SW1=0`；`868_915mhz=RF_SW0=1,RF_SW1=1`；`00=not listed` |
| 射频 | 315MHz 控制组合 | `schematic=RF_SW0=0,RF_SW1=1`；`product_document=RF_SW0=0,RF_SW1=0`；`affected_band=315MHz` |
| 射频 | 315MHz 匹配支路 | `path=U4.RF1-L6-L7-L8-U5.RF1`；`series=L6 10nH,L7 0R,L8 10nH`；`shunt=L17 3.6nH + C50 8pF to GND`；`dnp=C51` |
| 射频 | 433MHz 匹配支路 | `path=U4.RF2-L10-L11-L12-L13-U5.RF2`；`series=L10 0R,L11 0R,L12 15nH,L13 0R`；`shunt=C53 10pF,C55 6.2pF`；`nc=C54` |
| 射频 | 868/915MHz 匹配支路 | `path=U4.RF3-L15-L16-U5.RF3`；`series=L15 0R,L16 10nH`；`nc=C58`；`dnp=C59`；`truth_table_band=868MHz/915MHz` |
| 接口 | E1 SMA 天线接口 | `switch_output=U5.6 RFin`；`series_inductor=L9 2.2nH`；`rf_net=CC1101_RF`；`connector=E1 SMA-TH_KH-SMA-KE-Z`；`series_link=R7 0R`；`ground=E1 shell`；`not_fitted=D1,C60,C61 NC` |
| 保护电路 | SMA 端口保护预留 | `esd_position=D1 NC`；`shunt_caps=C60 NC,C61 NC`；`series=R7 0R` |
| 存储 | 存储/FIFO | `flash=none shown`；`eeprom=none shown`；`sd=none shown`；`external_fifo=none shown` |
| 内存与 Flash | 外部 RAM | `ram=none shown` |
| 调试与烧录 | 调试接口 | `jtag=none shown`；`swd=none shown`；`available_headers=P1 HDR_14P-2.54,J1 GROVE 4P` |
| 音频 | 音频电路 | `codec=none shown`；`microphone=none shown`；`speaker=none shown` |

## 待确认事项

- `rf.truth-table-doc-conflict`：当前原理图将 315MHz 组合标为 RF_SW0/RF_SW1=0/1，而产品正文表格写为 0/0；应以对应硬件版本实测或设计资料确认软件配置。（证据：图 85f5c961e5cc / 第 1 页 / D1：原理图真值表 0/1 行在 315MHz 列打勾，未列 0/0 行）
- `review.rf-truth-table`：请确认 V0.3 硬件的 315MHz 射频开关组合，并同步修正产品正文或原理图真值表。；原因：原理图明确标为 RF_SW0/RF_SW1=0/1，而产品正文当前写为 0/0；软件按错误组合配置会选错或无法选中频段。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7306e2a34d408b373ef45a1b5c775f4e3ebbd03451ac92417031fc072943d3b1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1250/SCH_Cap_CC1101_SCH_V0.3_20260528_page_01.png` |
| 2 | 1 | `da5bc52a4444fd37e4d5516f9ccb265d6bbba5902f8c3fdb1069cf934a4f5d54` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1250/SCH_Cap_CC1101_SCH_V0.3_20260528_page_02.png` |
| 3 | 1 | `85f5c961e5cc5014d2afcede3106042298ba5970c8739d01b29f398c9d4a04cf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1250/SCH_Cap_CC1101_SCH_V0.3_20260528_page_03.png` |

---

源文档：`zh_CN/cap/Cap_CC1101.md`

源文档 SHA-256：`a877984b1cb12b19502e2d2e20a19ac42bc3cd6fe0006b2682936adb6ab3d0f4`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
