# Module LTE 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module LTE |
| SKU | M027 |
| 产品 ID | `module-lte-893b13655c18` |
| 源文档 | `zh_CN/module/lte.md` |

## 概述

Module LTE 以 M8321 蜂窝通信模块为核心，通过 TXS0104E 电平转换器把主通信 UART 接到 M5-Bus 的 GPIO16/GPIO17，并从 M5-Bus 5V 经 JW5033H 生成约 4V 的 VBAT 模组电源。电路提供双 IPEX 主/分集天线、Nano SIM 接口、USB 与调试信号、三路状态指示和开关机控制。独立的 TLV320AIC3100 音频编解码器通过 PCM、MCLK 和 I2C 与 M8321 连接，驱动板载麦克风和扬声器，外部低速接口和音频端口均配置了可见的 TVS 防护。

## 检索关键词

`Module LTE`、`M027`、`M8321`、`TXS0104E`、`TLV320AIC3100`、`JW5033H`、`LTE`、`M5-Bus`、`UART0`、`UART2`、`GPIO16`、`GPIO17`、`I2C`、`PCM`、`MCLK`、`USB_DP`、`USB_DN`、`USIM`、`SIM_IO`、`SIM_CLK`、`SIM_RST`、`SIM_VCC`、`MAIN_ANT`、`DIV_ANT`、`IPEX`、`VBAT`、`+4V`、`PWR_KEY`、`S_PWR`、`NET_STA`、`MOD_STA`、`MIC_P`、`MIC_N`、`SPK_P`、`SPK_N`、`SMF05CT1G`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | M8321 | LTE 蜂窝通信核心模组 | 图 2a5aa3d24386 / 第 1 页 / 网格 2A-3D，U4 M8321 的电源、UART、USB、USIM、PCM、I2C、射频和控制引脚 |
| U3 | TXS0104E | VDD_EXT 与 3.3V 域之间的四通道双向电平转换器 | 图 2a5aa3d24386 / 第 1 页 / 网格 1A，U3 TXS0104E，VCCA=VDD_EXT、VCCB=+3.3V，连接 DEBUG_RXD/TXD 与 UART0_RXD/TXD |
| U1 | tlv320aic3100 | PCM/I2C 音频编解码器、麦克风输入和差分扬声器驱动 | 图 2a5aa3d24386 / 第 2 页 / 网格 2A-3C，U1 tlv320aic3100 的 PCM、I2C、RESET、MIC1 和 SPK 引脚 |
| U7 | JW5033H | M5-Bus 5V 到 LTE 模组 VBAT 的降压转换器 | 图 2a5aa3d24386 / 第 4 页 / 网格 1A-2B，U7 JW5033H、L1、+5V 输入及 +4V/VBAT 输出 |
| J1 | M5Stack_BUS | 30 针 M5-Bus 主机、电源和扩展接口 | 图 2a5aa3d24386 / 第 1 页 / 网格 4C-D，J1 M5Stack_BUS，GPIO16、GPIO17、S_PWR、+3.3V、+5V、GND 等引脚 |
| U6 | SIM | Nano SIM 卡连接器 | 图 2a5aa3d24386 / 第 1 页 / 网格 1D，U6 SIM，CLK、RST、VCC、IO、VPP 和 GND 引脚 |
| U5 | SMF05CT1G | SIM_CLK、SIM_RST、SIM_VCC 和 SIM_IO 多通道 TVS 防护器件 | 图 2a5aa3d24386 / 第 1 页 / 网格 1C-D，U5 SMF05CT1G 接入 SIM_IO、SIM_CLK、SIM_RST、SIM_VCC |
| E1 | ANT_IPEX | LTE 分集天线接口 | 图 2a5aa3d24386 / 第 1 页 / 网格 4B，E1 ANT_IPEX 经 R12 0Ω 连接 U4 DIV_ANT |
| E2 | ANT_IPEX | LTE 主天线接口 | 图 2a5aa3d24386 / 第 1 页 / 网格 4B-C，E2 ANT_IPEX 经 R17 0Ω 连接 U4 MAIN_ANT |
| S1 | SW-PB | LTE 模组开关机按键 | 图 2a5aa3d24386 / 第 1 页 / 网格 1C，S1 SW-PB、S_PWR、R19 和 Q3/PWR_KEY 控制电路 |
| Q3 | SS8050 Y1 | 由 S_PWR 控制的 PWR_KEY 下拉晶体管 | 图 2a5aa3d24386 / 第 1 页 / 网格 1C，Q3 SS8050 Y1，基极经 R18 接 S_PWR，集电极接 PWR_KEY，发射极接 GND |
| Q2 | SS8050 Y1 | MOD_STA 状态 LED 低端驱动晶体管 | 图 2a5aa3d24386 / 第 1 页 / 网格 1B，Q2 由 MOD_STA 经 R15 驱动并控制 D6 |
| Q1 | SS8050 Y1 | NET_STA 状态 LED 低端驱动晶体管 | 图 2a5aa3d24386 / 第 1 页 / 网格 1B，Q1 由 NET_STA 经 R16 驱动并控制 D7 |
| D5 | 红灯 0603 | VBAT 电源指示 LED | 图 2a5aa3d24386 / 第 1 页 / 网格 2A，D5 红灯 0603 从 VBAT 经 R10 1kΩ 接地 |
| U2 | MIC | 板载模拟麦克风 | 图 2a5aa3d24386 / 第 2 页 / 网格 1C-D，U2 MIC 连接 MIC_P、MIC_N 并由 D1/D2 防护 |
| LS1 | Speaker | 板载差分扬声器 | 图 2a5aa3d24386 / 第 2 页 / 网格 3C-D，LS1 Speaker 经 R7/R9 连接 SPK_P/SPK_N 并由 D3/D4 防护 |
| D1,D2 | TVS | 麦克风差分输入静电防护 | 图 2a5aa3d24386 / 第 2 页 / 网格 1C-D，D1/D2 分别从 MIC_P/MIC_N 接地 |
| D3,D4 | TVS | 扬声器差分输出静电防护 | 图 2a5aa3d24386 / 第 2 页 / 网格 3C-D，D3/D4 分别从 SPK_P/SPK_N 接地 |

## 系统结构

### M8321 LTE 核心架构

U4 M8321 集成主/分集射频、USIM、USB、UART0、UART1 调试、UART2、PCM、I2C、开关机和状态接口，是 Module LTE 的通信核心。

- 参数与网络：`reference=U4`；`part_number=M8321`；`main_power=VBAT`；`io_power=VDD_EXT`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 2A-3D，U4 M8321 完整符号与外围网络

### 原理图层次分区

顶层页将设计划分为 U_Power、U_LTE_Module 和 U_Codec 三个功能分区，LTE_Module 与 CODEC_Module 通过层次 Harness 相连。

- 参数与网络：`power_sheet=Power.SchDoc`；`lte_sheet=LTE_Module.SchDoc`；`codec_sheet=Codec.SchDoc`；`interconnect=LTE_Module to CODEC_Module`
- 证据：图 2a5aa3d24386 / 第 3 页 / 网格 1A-3B，U_Power、U_LTE_Module、U_Codec 层次块和 Harness

## 电源

### LTE 主电源转换

M5-Bus 的 +5V 进入 U7 JW5033H 降压电路，经 L1 4.7uH 输出标注为 +4V 的 VBAT 电源轨。

- 参数与网络：`converter=U7 JW5033H`；`input_voltage=+5V`；`output_voltage=+4V`；`output_net=VBAT`；`inductor=L1 4.7uH`
- 证据：图 2a5aa3d24386 / 第 4 页 / 网格 1A-2B，+5V、U7、L1、+4V 与 VBAT 连续电源路径

### M8321 VBAT 供电

VBAT 连接 U4 的 VBAT_BB 引脚 18/19 和 VBAT_RF 引脚 38/39，并配置 C19、C20、C25-C28 去耦。

- 参数与网络：`baseband_pins=18,19`；`rf_pins=38,39`；`net=VBAT`；`bulk_capacitance=C19=100uF, C20=680uF`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 2B-D，U4 VBAT_BB/VBAT_RF 引脚及底部 VBAT 去耦电容组

### 音频编解码器电源域

U1 IOVDD/DVDD 使用 VDD_EXT，HPVDD 和 AVDD 使用 +3.3V，SPKVDD 使用 +5V，并分别配置本地去耦。

- 参数与网络：`digital_io_supply=VDD_EXT`；`headphone_analog_supply=+3.3V`；`speaker_supply=+5V`；`codec=U1 tlv320aic3100`
- 证据：图 2a5aa3d24386 / 第 2 页 / 网格 2A-3C，U1 IOVDD/DVDD、HPVDD、AVDD、SPKVDD 与 C1/C3-C5/C8/C9

## 接口

### M5Stack 30 针总线

J1 为 M5Stack_BUS，原理图实际使用 GND、GPIO16、GPIO17、GPIO2/S_PWR、+3.3V 和 +5V；HPWR 引脚 27/29 在本页标记为未连接。

- 参数与网络：`connector=J1`；`gnd_pins=1,3,5`；`gpio16_pin=15`；`gpio17_pin=16`；`s_pwr_pin=19`；`three_v_three_pin=14`；`five_v_pin=30`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 4C-D，J1 M5Stack_BUS 全部 30 针及连接/未连接标记

### Nano SIM 信号连接

U6 SIM 卡座的 SIM_IO、SIM_RST、SIM_CLK 和 SIM_VCC 分别经 33Ω 串联电阻连接 U4 的 USIM_DATA、USIM_RST、USIM_CLK 和 USIM_VDD。

- 参数与网络：`connector=U6`；`io=SIM_IO to USIM_DATA`；`reset=SIM_RST to USIM_RST`；`clock=SIM_CLK to USIM_CLK`；`supply=SIM_VCC to USIM_VDD`；`series_resistance=33Ω`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 1C-D 的 U6 和 R24 电阻阵列，与网格 2C-D 的 U4 USIM 引脚

### M8321 USB 数据接口

U4 USB_IN 和 USB_DP 分别连接外部网络 USB_DN 与 USB_DP，邻近引脚 76、77 为地，原理图未在该页画出 USB 连接器。

- 参数与网络：`dm_pin=U4 pin74 USB_IN`；`dm_net=USB_DN`；`dp_pin=U4 pin75 USB_DP`；`dp_net=USB_DP`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 2A-3A，U4 顶部引脚 74 USB_IN、75 USB_DP 及 USB_DN/USB_DP 网络

## 总线

### M5-Bus 主通信 UART

U4 UART0_TXD 经 U3 第三通道和 R20 0Ω 接 M5-Bus GPIO16；U4 UART0_RXD 经 U3 第四通道和 R21 0Ω 接 M5-Bus GPIO17。

- 参数与网络：`modem_tx=U4 pin29 UART0_TXD`；`host_gpio_rx=J1 pin15 GPIO16`；`modem_rx=U4 pin30 UART0_RXD`；`host_gpio_tx=J1 pin16 GPIO17`；`level_shifter=U3 TXS0104E`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 1A 的 U3 A3/A4-B3/B4、网格 2C 的 U4 UART0 与网格 4C 的 J1 GPIO16/GPIO17

### M8321 UART2

U4 直接引出 UART2_RXD 和 UART2_TXD，分别位于引脚 14 和 15。

- 参数与网络：`rx_pin=14`；`tx_pin=15`；`rx_net=UART2_RXD`；`tx_net=UART2_TXD`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 2B-C，U4 左侧引脚 14 UART2_RXD 与引脚 15 UART2_TXD

### 音频编解码器控制总线

U4 I2C1_SDA 和 I2C1_SCL 形成 I2C_SDA、I2C_SCL，并连接 U1 TLV320AIC3100 的 SDA、SCL。

- 参数与网络：`controller=U4 M8321`；`device=U1 tlv320aic3100`；`sda=I2C_SDA`；`scl=I2C_SCL`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 2B 的 U4 I2C1_SDA/SCL 与网格 4A Harness; 图 2a5aa3d24386 / 第 2 页 / 网格 1A-2B Harness 到 U1 pin9 SDA、pin10 SCL

## GPIO 与控制信号

### M8321 开关机控制

M5-Bus 的 S_PWR 经 R22 0Ω 驱动 Q3 基极，Q3 导通时把 U4 PWR_KEY 拉向 GND；板载 S1 与 R19 组成同一 S_PWR 按键网络。

- 参数与网络：`host_net=S_PWR`；`modem_pin=U4 pin17 PWR_KEY`；`transistor=Q3 SS8050 Y1`；`base_resistor=R18 1kΩ`；`bus_link=R22 0Ω`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 1C 的 S1/Q3/PWR_KEY 与网格 4C 的 J1 pin19、R22、S_PWR

### 模组状态指示

MOD_STA 经 R15 驱动 Q2 并控制 D6，NET_STA 经 R16 驱动 Q1 并控制 D7；D5 则从 VBAT 经 R10 1kΩ 直接接地作为电源指示。

- 参数与网络：`module_status=MOD_STA -> R15 -> Q2 -> D6`；`network_status=NET_STA -> R16 -> Q1 -> D7`；`power_indicator=VBAT -> D5 -> R10 1kΩ -> GND`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 1A-B 的 D6/Q2、D7/Q1 与网格 2A 的 D5/R10

## 复位

### TLV320AIC3100 复位

CODEC_RST 连接 U1 RESET，引脚通过 R2 100kΩ 上拉到 VDD_EXT，并预留 R1 0Ω 到 GND 的装配位置。

- 参数与网络：`net=CODEC_RST`；`codec_pin=U1 pin31 RESET`；`pullup=R2 100kΩ to VDD_EXT`；`optional_pulldown=R1 0Ω`
- 证据：图 2a5aa3d24386 / 第 2 页 / 网格 2A-3A，CODEC_RST、U1 RESET、R1 和 R2

## 保护电路

### SIM 接口防护

U5 SMF05CT1G 对 SIM_IO、SIM_RST、SIM_CLK 和 SIM_VCC 提供接地 TVS 箝位，SIM_CLK/RST/VCC 另各有 33pF 对地电容。

- 参数与网络：`protector=U5 SMF05CT1G`；`protected_nets=SIM_IO, SIM_RST, SIM_CLK, SIM_VCC`；`capacitors=C22=33pF, C23=33pF, C24=33pF`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 1C-D，U5 SMF05CT1G、C22、C23、C24 与 SIM 网络

## 关键网络

### VDD_EXT I/O 电源轨

U4 VDD_EXT 引脚 61 输出到 VDD_EXT 网络，该网络为 U3 TXS0104E 的 VCCA、U1 TLV320AIC3100 的数字 I/O 电源和 CODEC_RST 上拉供电。

- 参数与网络：`source=U4 pin61 VDD_EXT`；`consumers=U3 VCCA, U1 IOVDD/DVDD, R2 CODEC_RST pull-up`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 3A-B，U4 pin61 VDD_EXT 与 C14；网格 1A U3 VCCA; 图 2a5aa3d24386 / 第 2 页 / 网格 2A-3B，U1 IOVDD/DVDD 和 R2 上拉均连接 VDD_EXT

## 音频

### M8321 与音频编解码器 PCM 总线

U4 的 PCM_DIN、PCM_DOUT、PCM_FS、PCM_CLK 和 MCLK 通过层次 Harness 连接到 U1 TLV320AIC3100 的 DOUT、DIN、WCLK、BCLK 和 MCLK。

- 参数与网络：`modem_pcm_pins=21 PCM_DIN, 22 PCM_DOUT, 23 PCM_FS, 24 PCM_CLK`；`modem_mclk_pin=73`；`codec=U1 tlv320aic3100`；`nets=PCM_DIN, PCM_DOUT, PCM_FS, PCM_CLK, MCLK`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 2C-D 的 U4 PCM 引脚、网格 3A-4A 的 LTE_Module Harness; 图 2a5aa3d24386 / 第 2 页 / 网格 1A-3B 的 CODEC_Module Harness 和 U1 DOUT/DIN/WCLK/BCLK/MCLK

### 板载麦克风输入

U2 板载麦克风输出 MIC_P/MIC_N，经 R6/R8 0Ω 和 C6/C7 1uF 交流耦合连接 U1 MIC1LP/MIC1LM；D1/D2 对两路麦克风线提供 TVS 防护。

- 参数与网络：`microphone=U2 MIC`；`codec_inputs=U1 MIC1LP, MIC1LM`；`coupling=C6=1uF, C7=1uF`；`protection=D1,D2 TVS`
- 证据：图 2a5aa3d24386 / 第 2 页 / 网格 1B-D，U1 MIC1 输入偏置网络、U2、R6/R8、C6/C7、D1/D2

### 板载扬声器输出

U1 的 SPKP/SPKM 差分输出形成 SPK_P/SPK_N，经 R7/R9 0Ω 驱动 LS1；D3/D4 分别从 SPK_P/SPK_N 接地提供 TVS 防护。

- 参数与网络：`codec_outputs=U1 SPKP, SPKM`；`speaker=LS1`；`series_links=R7=0Ω, R9=0Ω`；`protection=D3,D4 TVS`
- 证据：图 2a5aa3d24386 / 第 2 页 / 网格 3B-D，U1 SPKP/SPKM、SPK_P/SPK_N、R7/R9、LS1、D3/D4

## 射频

### LTE 主天线和分集天线

U4 MAIN_ANT 经 R17 0Ω 连接 E2 ANT_IPEX，DIV_ANT 经 R12 0Ω 连接 E1 ANT_IPEX，两路接口均以独立 IPEX 连接器引出。

- 参数与网络：`main_pin=U4 pin47 MAIN_ANT`；`main_connector=E2`；`diversity_pin=U4 pin58 DIV_ANT`；`diversity_connector=E1`；`series_links=R17=0Ω, R12=0Ω`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 3B-4C，U4 MAIN_ANT/DIV_ANT、R12、R17、E1、E2

## 调试与烧录

### M8321 调试串口

U4 UART1_RXD 和 UART1_TXD 分别形成 DEBUG_RXD、DEBUG_TXD，并通过 U3 TXS0104E 在 VDD_EXT 与 3.3V 电平域间转换。

- 参数与网络：`modem_rx_pin=3`；`modem_tx_pin=4`；`rx_net=DEBUG_RXD`；`tx_net=DEBUG_TXD`；`level_shifter=U3 TXS0104E`
- 证据：图 2a5aa3d24386 / 第 1 页 / 网格 1A U3 A1/A2-B1/B2 与网格 2B U4 UART1_RXD/UART1_TXD

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | M8321 LTE 核心架构 | `reference=U4`；`part_number=M8321`；`main_power=VBAT`；`io_power=VDD_EXT` |
| 电源 | LTE 主电源转换 | `converter=U7 JW5033H`；`input_voltage=+5V`；`output_voltage=+4V`；`output_net=VBAT`；`inductor=L1 4.7uH` |
| 电源 | M8321 VBAT 供电 | `baseband_pins=18,19`；`rf_pins=38,39`；`net=VBAT`；`bulk_capacitance=C19=100uF, C20=680uF` |
| 总线 | M5-Bus 主通信 UART | `modem_tx=U4 pin29 UART0_TXD`；`host_gpio_rx=J1 pin15 GPIO16`；`modem_rx=U4 pin30 UART0_RXD`；`host_gpio_tx=J1 pin16 GPIO17`；`level_shifter=U3 TXS0104E` |
| 调试与烧录 | M8321 调试串口 | `modem_rx_pin=3`；`modem_tx_pin=4`；`rx_net=DEBUG_RXD`；`tx_net=DEBUG_TXD`；`level_shifter=U3 TXS0104E` |
| 总线 | M8321 UART2 | `rx_pin=14`；`tx_pin=15`；`rx_net=UART2_RXD`；`tx_net=UART2_TXD` |
| 接口 | M5Stack 30 针总线 | `connector=J1`；`gnd_pins=1,3,5`；`gpio16_pin=15`；`gpio17_pin=16`；`s_pwr_pin=19`；`three_v_three_pin=14`；`five_v_pin=30` |
| GPIO 与控制信号 | M8321 开关机控制 | `host_net=S_PWR`；`modem_pin=U4 pin17 PWR_KEY`；`transistor=Q3 SS8050 Y1`；`base_resistor=R18 1kΩ`；`bus_link=R22 0Ω` |
| 接口 | Nano SIM 信号连接 | `connector=U6`；`io=SIM_IO to USIM_DATA`；`reset=SIM_RST to USIM_RST`；`clock=SIM_CLK to USIM_CLK`；`supply=SIM_VCC to USIM_VDD`；`series_resistance=33Ω` |
| 保护电路 | SIM 接口防护 | `protector=U5 SMF05CT1G`；`protected_nets=SIM_IO, SIM_RST, SIM_CLK, SIM_VCC`；`capacitors=C22=33pF, C23=33pF, C24=33pF` |
| 射频 | LTE 主天线和分集天线 | `main_pin=U4 pin47 MAIN_ANT`；`main_connector=E2`；`diversity_pin=U4 pin58 DIV_ANT`；`diversity_connector=E1`；`series_links=R17=0Ω, R12=0Ω` |
| 接口 | M8321 USB 数据接口 | `dm_pin=U4 pin74 USB_IN`；`dm_net=USB_DN`；`dp_pin=U4 pin75 USB_DP`；`dp_net=USB_DP` |
| GPIO 与控制信号 | 模组状态指示 | `module_status=MOD_STA -> R15 -> Q2 -> D6`；`network_status=NET_STA -> R16 -> Q1 -> D7`；`power_indicator=VBAT -> D5 -> R10 1kΩ -> GND` |
| 音频 | M8321 与音频编解码器 PCM 总线 | `modem_pcm_pins=21 PCM_DIN, 22 PCM_DOUT, 23 PCM_FS, 24 PCM_CLK`；`modem_mclk_pin=73`；`codec=U1 tlv320aic3100`；`nets=PCM_DIN, PCM_DOUT, PCM_FS, PCM_CLK, MCLK` |
| 总线 | 音频编解码器控制总线 | `controller=U4 M8321`；`device=U1 tlv320aic3100`；`sda=I2C_SDA`；`scl=I2C_SCL` |
| 复位 | TLV320AIC3100 复位 | `net=CODEC_RST`；`codec_pin=U1 pin31 RESET`；`pullup=R2 100kΩ to VDD_EXT`；`optional_pulldown=R1 0Ω` |
| 音频 | 板载麦克风输入 | `microphone=U2 MIC`；`codec_inputs=U1 MIC1LP, MIC1LM`；`coupling=C6=1uF, C7=1uF`；`protection=D1,D2 TVS` |
| 音频 | 板载扬声器输出 | `codec_outputs=U1 SPKP, SPKM`；`speaker=LS1`；`series_links=R7=0Ω, R9=0Ω`；`protection=D3,D4 TVS` |
| 电源 | 音频编解码器电源域 | `digital_io_supply=VDD_EXT`；`headphone_analog_supply=+3.3V`；`speaker_supply=+5V`；`codec=U1 tlv320aic3100` |
| 关键网络 | VDD_EXT I/O 电源轨 | `source=U4 pin61 VDD_EXT`；`consumers=U3 VCCA, U1 IOVDD/DVDD, R2 CODEC_RST pull-up` |
| 系统结构 | 原理图层次分区 | `power_sheet=Power.SchDoc`；`lte_sheet=LTE_Module.SchDoc`；`codec_sheet=Codec.SchDoc`；`interconnect=LTE_Module to CODEC_Module` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1, 2, 3, 4 | `2a5aa3d243864df9f47ccaf015a81286e51c9746d8e2fd30c542cbe2ed8ff1ed` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Modules/module_lte_sch.pdf` |

---

源文档：`zh_CN/module/lte.md`

源文档 SHA-256：`61c421174f33636f2f9b3e428535fe25a7205a69181dc27211ebf7d75fb3d6e4`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
