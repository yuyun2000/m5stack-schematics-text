# Module LLM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module LLM |
| SKU | M140 |
| 产品 ID | `module-llm-f66d28e8903c` |
| 源文档 | `zh_CN/module/Module-LLM.md` |

## 概述

九张本地原理图页面覆盖 Module LLM 的 AX630C 主控、电源树、启动与时钟、LPDDR4、eMMC、MicroSD、模拟音频、USB Type-C、UART/I2C、M5-Bus、RGB 状态灯及调试 FPC。图面确认 AX630C、MSM421A 系列麦克风、AW8737A 功放、LP5562 和主要接口连线，但 LPDDR4/eMMC 容量、NPU 算力、功耗、扬声器机械规格、网络速率及软件模型能力未直接标注。

## 检索关键词

`Module LLM`、`M140`、`AX630C`、`LPDDR4`、`eMMC 5.1`、`MicroSD`、`TF card`、`MSM421A`、`MSM421A3729H9KRMC`、`AW8737A`、`LP5562`、`LED-2020-RGB`、`SGM7220`、`SGM2578`、`AW32901`、`SY8089A1AAA`、`JW5255A`、`WL2811EA-5/TR`、`USB Type-C`、`USB OTG`、`TRM_TXD`、`TRM_RXD`、`DBG_TXD`、`DBG_RXD`、`BUS_SCL`、`BUS_SDA`、`M.BUS_Core2`、`EPHY_TX`、`EPHY_RX`、`24MHz`、`32.768kHz`、`VCORE_0V8`、`VDDR_1V1`、`VDD_1V8`、`VDD_3V3`、`VDD_5V`、`StackFlow`、`Qwen2.5-0.5B`、`KWS`、`ASR`、`TTS`、`3.2 TOPS`、`115200 8N1`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | AX630C | 主 SoC，连接电源、DDR、存储、音频、USB、UART/I2C、以太网 PHY 与启动控制 | 图 04d8e4d3a1f4 / 第 1 页 / 原 PDF 第2页 U1A/U1L AX630C 电源与地; 图 d660230e4d50 / 第 1 页 / 原 PDF 第3页 U1B/U1E AX630C 启动、时钟、USB、UART 与 I2C |
| U2 | AW32901 | VIN_5V 到 VDD_5V 的输入保护与受控通路 | 图 04d8e4d3a1f4 / 第 1 页 / 原 PDF 第2页右上 U2 AW32901、VIN_5V/VDD_5V 与 OVLO 分压 |
| U3,U4,U6 | SY8089A1AAA | 从 VDD_5V 生成 3.3V、1.8V 和 DDR 1.1V 的三路降压转换器 | 图 04d8e4d3a1f4 / 第 1 页 / 原 PDF 第2页 U3/U4/U6 SY8089A1AAA 与 L1/L2/L3 |
| U5,U7 | LP5907MFX-1.8/NOPB / JW5255A | 分别生成 AVDD_1V8 模拟电源和 VCORE_0V8 核心电源 | 图 04d8e4d3a1f4 / 第 1 页 / 原 PDF 第2页 U5 LP5907 与 U7 JW5255A |
| X1,Y1 | 24MHz/12pF/2520 / 32.768kHz/12.5pF/3215 | AX630C 主时钟与低速时钟晶体 | 图 d660230e4d50 / 第 1 页 / 原 PDF 第3页右侧 X1 24MHz 与 Y1 32.768kHz |
| U8 | LPDDR4 | AX630C 外部 LPDDR4 内存器件 | 图 a26d069d6b4e / 第 1 页 / 原 PDF 第4页 U8A/U8B/U8C LPDDR4 与 DDR_DQ0-15 |
| U11 | EMMC_V5.1 | AX630C 的 eMMC 5.1 启动与存储器件 | 图 b3098cc77650 / 第 1 页 / 原 PDF 第5页 U11 EMMC_V5.1、EMMC_D0-7/CMD/CLK/DS/RSTN |
| U9,U10,FET3,VT1 | WL2811EA-5/TR / MicroSD / CJ2301 / PMBT3904 | MicroSD 卡座及其 IO 电源、卡电源开关和检测链路 | 图 b3098cc77650 / 第 1 页 / 原 PDF 第5页 U9/U10/FET3/VT1 与 SDCARD 信号 |
| U12 | MSM421A3729H9KRMC | 差分模拟麦克风，连接 AX630C AUDIO_IN_P/N | 图 00b1d013437d / 第 1 页 / 原 PDF 第6页 U12 MSM421A3729H9KRMC 与 C128/C132 |
| U13 | AW8737A | 由 AX630C AUDIO_OUT_P/N 驱动的差分扬声器功放 | 图 00b1d013437d / 第 1 页 / 原 PDF 第6页 U13 AW8737A 与 SPK_VOP/SPK_VON |
| J1,U14,U16 | USB Type-C / SGM7220 / SGM2578 | USB Type-C 数据、CC/ID 检测和 VBUS 电源角色控制 | 图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页上方 J1/U14/U16、USB_ID、USB_D_P/N 与 VUSB_5V |
| U20,U18,U21,U22 | LP5562 / LED-2020-RGB | I2C 控制的三颗共用 RGB 通道状态灯 | 图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页中下 U20 LP5562 与 U18/U21/U22 LED-2020-RGB |
| J2 | FPC-SMD_8P-P0.50 | 引出 EPHY_TX/RX 差分对和 DBG_TXD/RXD 的调试接口 | 图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页左中 J2 FPC 8-pin |
| J4,Tie1-Tie8 | M.BUS_Core2 / Net-Tie | M5-Bus 主连接器和终端 UART 引脚选择焊盘 | 图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页底部 J4 与 Tie1-Tie8 |
| U15,D2,D10,D11 | SRV05-4 / WS05DLC-B | USB、SD 卡和终端 UART 信号的 ESD 保护 | 图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页 U15、D10/D11; 图 b3098cc77650 / 第 1 页 / 原 PDF 第5页 D2 WS05DLC-B 阵列 |

## 系统结构

### AX630C 主控硬件范围

U1 标为 AX630C，其分单元连接电源与地、DDR、eMMC、SD 卡、模拟音频、USB、UART、I2C、以太网 PHY、启动脚、时钟和复位网络。

- 参数与网络：`soc=AX630C`；`schematic_assets=9`
- 证据：图 04d8e4d3a1f4 / 第 1 页 / 原 PDF 第2页 U1A/U1L; 图 d660230e4d50 / 第 1 页 / 原 PDF 第3页 U1B/U1E/U1O

### eMMC 默认启动与下载模式选择

R18/R19/R20 将 AX_BOND0、AX_BOND1、AX_GPIOA3 下拉，AX_GPIOA2_BOOT 由 R17 上拉；图中启动表对应默认 EMMC UDA，按下 GPIOA2_BOOT 到地后进入 USB DL、SD Card 或 UART 下载组合。

- 参数与网络：`default_boot=EMMC UDA`；`download_sources=USB DL,SD Card,UART`
- 证据：图 d660230e4d50 / 第 1 页 / 原 PDF 第3页 AX_BOND0/1、AX_GPIOA2_BOOT、AX_GPIOA3 与 BOOT OPTION 表

## 电源

### 5V 输入保护与多路 SoC 电源树

VIN_5V 经 U2 AW32901 形成 VDD_5V；U3/U4/U6 SY8089A1AAA 分别生成 VDD_3V3、VDD_1V8、VDDR_1V1，U5 LP5907 生成 AVDD_1V8，U7 JW5255A 生成 VCORE_0V8。

- 参数与网络：`input=VIN_5V`；`rails=VDD_5V,VDD_3V3,VDD_1V8,VDDR_1V1,AVDD_1V8,VCORE_0V8`
- 证据：图 04d8e4d3a1f4 / 第 1 页 / 原 PDF 第2页 U2-U7 与 L1-L4

## 接口

### USB Type-C 数据与角色控制硬件

J1 引出 CC1/CC2、USB_D_E_P/N 与 VUSB_5V；U14 SGM7220 连接 CC1/CC2、USB_ID、SYS_SDA/SCL 和 USB_DET，U16 SGM2578 与 FET4 依据 USB_ID 控制 VIN_5V 到 VUSB_5V 的供电通路，U15/L5 保护并滤波 USB D+/D-。

- 参数与网络：`connector=USB Type-C`；`cc_controller=SGM7220`；`vbus_switch=SGM2578`
- 证据：图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页上方 J1/U14/U15/U16/L5/FET4; 图 d660230e4d50 / 第 1 页 / 原 PDF 第3页 U1O USB_D_P/N 与 U1E USB_ID

### 调试 UART、终端 UART 与系统 I2C

AX630C UART0 连接 DBG_TXD/DBG_RXD，UART1 连接 TRM_TXD/TRM_RXD；I2C0 连接 BUS_SCL/BUS_SDA，并由 R24/R69 各 2.2K 上拉到 VDD_3V3。

- 参数与网络：`debug_uart=DBG_TXD,DBG_RXD`；`terminal_uart=TRM_TXD,TRM_RXD`；`i2c=BUS_SCL,BUS_SDA`
- 证据：图 d660230e4d50 / 第 1 页 / 原 PDF 第3页 U1E UART0/UART1/I2C0 与 R24/R69

### M5-Bus UART Net-Tie 选择

J4 M.BUS_Core2 接入 VIN_5V、MBUS_3V3、MBUS_RST、BUS_SDA/BUS_SCL；Tie1-Tie4 将 TRM_RXD 选择到 BUS_G17/G13/G6/G0，Tie5-Tie8 将 TRM_TXD 选择到 BUS_G18/G7/G14/G10。

- 参数与网络：`rx_candidates=G17,G13,G6,G0`；`tx_candidates=G18,G7,G14,G10`；`method=Net-Tie cut and jumper`
- 证据：图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页底部 J4 与 Tie1-Tie8

### LP5562 驱动三颗并联 RGB LED

U20 LP5562 通过 SYS_SDA/SYS_SCL 接入系统 I2C，R/G/B 三路输出分别连接 U18/U21/U22 三颗 LED-2020-RGB 的同名颜色通道，AD0 与 AD1 接地。

- 参数与网络：`driver=LP5562`；`led_count=3`；`led_package=LED-2020-RGB`；`address_pins=AD0=0,AD1=0`
- 证据：图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页 U20/U18/U21/U22

### 未连接的 DVP 与 MIPI 并行视频引脚

原理图把 AX630C U1G 的 DVP_IN、U1H 的 JMIPI_TX 和最后一页 MIPI_RX 差分引脚全部标为未连接；板上没有由这些引脚构成的摄像头或显示连接器。

- 参数与网络：`unused_interfaces=DVP_IN,JMIPI_TX,MIPI_RX`
- 证据：图 e996fa2558a7 / 第 1 页 / 原 PDF 第8页 U1G/U1H 全部视频信号 NC; 图 225a0cfb34ba / 第 1 页 / 原 PDF 第10页 MIPI_RX 全部差分对 NC

## 时钟

### 24MHz 与 32.768kHz 时钟

AX_24M_XIN/XOUT 连接 X1 24MHz/12pF/2520 晶体，AX_32K_XIN/XOUT 连接 Y1 32.768kHz/12.5pF/3215 晶体；两组均配置负载电容。

- 参数与网络：`main_clock_mhz=24`；`low_speed_clock_khz=32.768`
- 证据：图 d660230e4d50 / 第 1 页 / 原 PDF 第3页右侧 X1/Y1 与 C70/C72-C74

## 复位

### M5-Bus 到 AX630C 的复位链路

J4 的 MBUS_RST 经 FET1 CJ3139K、FET2 2N7002 与 SYS_RST_IN NetTie 驱动 AX630C 复位输入，R23/C71 提供上拉和 RC 网络。

- 参数与网络：`source_reset=MBUS_RST`；`soc_reset=SYS_RST_IN`
- 证据：图 d660230e4d50 / 第 1 页 / 原 PDF 第3页中部 MBUS_RST、FET1/FET2 与 SYS_RST_IN; 图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页 J4 pin6 MBUS_RST

## 存储

### eMMC 5.1 存储接口

U11 标为 EMMC_V5.1，通过 EMMC_D0-7、CMD、CLK、DS 与 RSTN 连接 AX630C；VCC 连接 VDD_3V3，VCCQ 连接 VDD_1V8。

- 参数与网络：`interface=eMMC 5.1`；`data_bits=8`；`vcc=VDD_3V3`；`vccq=VDD_1V8`
- 证据：图 b3098cc77650 / 第 1 页 / 原 PDF 第5页 U1M/U11 eMMC 总线

### MicroSD 四位总线与受控供电

U10 MicroSD 卡座连接 SDCARD_DAT0-3、CMD、CLK 与 SD_DET_N；U9 生成 VDDIO_SDCARD，FET3/VT1 由 SD_PWR_EN 控制 VDD_SDCARD，D2 对卡信号提供 ESD 保护。

- 参数与网络：`data_bits=4`；`card_detect=SD_DET_N`；`power_enable=SD_PWR_EN`
- 证据：图 b3098cc77650 / 第 1 页 / 原 PDF 第5页 U9/U10/FET3/VT1/D2

## 内存与 Flash

### AX630C 外部 LPDDR4

U8 标为 LPDDR4，通过 DDR_DQ0-15、DQS0/1、DM0/1、CA0-5、CLK、CKE、CS 与 RESET_N 连接 AX630C，器件使用 VDDR_1V1 与 VDD_1V8 电源。

- 参数与网络：`memory_type=LPDDR4`；`data_bits=16`；`io_rail=VDDR_1V1`；`core_rail=VDD_1V8`
- 证据：图 a26d069d6b4e / 第 1 页 / 原 PDF 第4页 U1D 与 U8A/U8B/U8C DDR 总线

## 音频

### MSM421A 模拟麦克风输入

U12 MSM421A3729H9KRMC 由 AVDD_1V8 经 FB3 滤波供电，其差分输出经 C128/C132 交流耦合到 AX630C AUDIO_IN_P/N。

- 参数与网络：`microphone=MSM421A3729H9KRMC`；`supply=AVDD_1V8`；`soc_input=AUDIO_IN_P,AUDIO_IN_N`
- 证据：图 00b1d013437d / 第 1 页 / 原 PDF 第6页 U12/FB3/C128/C132 与 U1F

### AW8737A 差分扬声器功放

AX630C AUDIO_OUT_P/N 经输入网络送到 U13 AW8737A，AUDIO_AP_EN 控制 AMP_EN，功放由 VDD_5V 供电并通过 FB4/FB5 输出 SPK_VOP/SPK_VON。

- 参数与网络：`amplifier=AW8737A`；`supply=VDD_5V`；`output=SPK_VOP,SPK_VON`
- 证据：图 00b1d013437d / 第 1 页 / 原 PDF 第6页 U13、AUDIO_OUT_P/N、AMP_EN 与 SPK_VOP/VON

## 调试与烧录

### 调试 FPC 的 EPHY 与内核串口

J2 8-pin FPC 引出 EPHY_TX_P/N、EPHY_RX_P/N、DBG_TXD、DBG_RXD 和两脚 GND；EPHY 差分对直接来自 AX630C U1J 内置 PHY 分单元。

- 参数与网络：`connector=FPC 8-pin 0.50mm`；`signals=EPHY_TX_P/N,EPHY_RX_P/N,DBG_TXD,DBG_RXD`
- 证据：图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页 J2 FPC; 图 141a3b26d17b / 第 1 页 / 原 PDF 第9页 U1J EPHY_TX/RX

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | AX630C 主控硬件范围 | `soc=AX630C`；`schematic_assets=9` |
| 电源 | 5V 输入保护与多路 SoC 电源树 | `input=VIN_5V`；`rails=VDD_5V,VDD_3V3,VDD_1V8,VDDR_1V1,AVDD_1V8,VCORE_0V8` |
| 时钟 | 24MHz 与 32.768kHz 时钟 | `main_clock_mhz=24`；`low_speed_clock_khz=32.768` |
| 系统结构 | eMMC 默认启动与下载模式选择 | `default_boot=EMMC UDA`；`download_sources=USB DL,SD Card,UART` |
| 复位 | M5-Bus 到 AX630C 的复位链路 | `source_reset=MBUS_RST`；`soc_reset=SYS_RST_IN` |
| 内存与 Flash | AX630C 外部 LPDDR4 | `memory_type=LPDDR4`；`data_bits=16`；`io_rail=VDDR_1V1`；`core_rail=VDD_1V8` |
| 存储 | eMMC 5.1 存储接口 | `interface=eMMC 5.1`；`data_bits=8`；`vcc=VDD_3V3`；`vccq=VDD_1V8` |
| 存储 | MicroSD 四位总线与受控供电 | `data_bits=4`；`card_detect=SD_DET_N`；`power_enable=SD_PWR_EN` |
| 音频 | MSM421A 模拟麦克风输入 | `microphone=MSM421A3729H9KRMC`；`supply=AVDD_1V8`；`soc_input=AUDIO_IN_P,AUDIO_IN_N` |
| 音频 | AW8737A 差分扬声器功放 | `amplifier=AW8737A`；`supply=VDD_5V`；`output=SPK_VOP,SPK_VON` |
| 接口 | USB Type-C 数据与角色控制硬件 | `connector=USB Type-C`；`cc_controller=SGM7220`；`vbus_switch=SGM2578` |
| 接口 | 调试 UART、终端 UART 与系统 I2C | `debug_uart=DBG_TXD,DBG_RXD`；`terminal_uart=TRM_TXD,TRM_RXD`；`i2c=BUS_SCL,BUS_SDA` |
| 接口 | M5-Bus UART Net-Tie 选择 | `rx_candidates=G17,G13,G6,G0`；`tx_candidates=G18,G7,G14,G10`；`method=Net-Tie cut and jumper` |
| 调试与烧录 | 调试 FPC 的 EPHY 与内核串口 | `connector=FPC 8-pin 0.50mm`；`signals=EPHY_TX_P/N,EPHY_RX_P/N,DBG_TXD,DBG_RXD` |
| 接口 | LP5562 驱动三颗并联 RGB LED | `driver=LP5562`；`led_count=3`；`led_package=LED-2020-RGB`；`address_pins=AD0=0,AD1=0` |
| 接口 | 未连接的 DVP 与 MIPI 并行视频引脚 | `unused_interfaces=DVP_IN,JMIPI_TX,MIPI_RX` |
| 核心器件 | AX630C CPU 与 NPU 性能 | `documented_cpu=Dual Cortex-A53 1.2GHz`；`documented_int4_tops=12.8`；`documented_int8_tops=3.2` |
| 内存与 Flash | 4GB LPDDR4 与 1GB/3GB 分配 | `documented_total_gb=4`；`documented_system_gb=1`；`documented_accelerator_gb=3` |
| 存储 | 32GB eMMC 5.1 容量 | `documented_capacity_gb=32`；`documented_standard=eMMC 5.1` |
| 电源 | 5V 空载与满载功耗 | `documented_idle_w=0.5`；`documented_full_load_w=1.5`；`input_v=5` |
| 音频 | 8ohm 1W 2014 腔体扬声器 | `documented_impedance_ohm=8`；`documented_power_w=1`；`documented_size=2014 cavity` |
| 接口 | UART 默认 115200 8N1 | `documented_baud=115200`；`documented_format=8N1`；`documented_adjustable=true` |
| 接口 | USB OTG 自动切换与 ADB | `documented_modes=USB host,USB device,ADB`；`documented_device_example=USB camera` |
| 接口 | 调试套件百兆以太网 | `documented_rate_mbps=100`；`required_accessory=LLM debug kit` |
| 系统结构 | Ubuntu、StackFlow 与预装 AI 模型 | `documented_os=Ubuntu`；`documented_framework=StackFlow`；`documented_model=Qwen2.5-0.5B`；`documented_pipeline=KWS,ASR,LLM,TTS` |
| 存储 | SD 卡与 Type-C 固件升级 | `documented_upgrade_media=SD card,USB Type-C`；`documented_modes=cold update,hot update` |
| 接口 | RGB 工作与升级状态含义 | `documented_work_states=red initializing,green ready`；`documented_update_states=blue blinking updating,red failed,green success` |

## 待确认事项

- `component.documented-soc-performance`：正文称 AX630C 包含双 Cortex-A53 1.2GHz，最高 12.8 TOPS INT4 和 3.2 TOPS INT8；原理图只确认器件型号和电气连接，没有 CPU 频率、NPU 架构或算力参数。（证据：图 04d8e4d3a1f4 / 第 1 页 / 原 PDF 第2页 U1 仅标 AX630C）
- `memory.documented-4gb-partition`：正文称板载 4GB LPDDR4，其中 1GB 为系统内存、3GB 为硬件加速专用；U8 图符只标 LPDDR4，没有制造商料号、密度、容量或软件内存分区。（证据：图 a26d069d6b4e / 第 1 页 / 原 PDF 第4页 U8 仅标 LPDDR4）
- `storage.documented-32gb-emmc`：正文称板载 32GB eMMC 5.1；U11 只标 EMMC_V5.1，没有具体料号或容量，因此 32GB 容量和量产颗粒需由 BOM 或器件标识确认。（证据：图 b3098cc77650 / 第 1 页 / 原 PDF 第5页 U11 仅标 EMMC_V5.1）
- `power.documented-consumption`：正文给出空载 5V@0.5W、满载 5V@1.5W；原理图没有电流检测、负载条件、模型工作负载或测试点，无法验证功耗数值和测量边界。（证据：图 04d8e4d3a1f4 / 第 1 页 / 原 PDF 第2页仅显示电源树，无功耗测量电路）
- `audio.documented-speaker`：正文称扬声器为 8ohm、1W、2014 腔体；原理图仅把 AW8737A 输出命名为 SPK_VOP/SPK_VON，没有扬声器器件、连接器、阻抗、功率或机械尺寸。（证据：图 00b1d013437d / 第 1 页 / 原 PDF 第6页仅显示 SPK_VOP/SPK_VON 输出网络）
- `interface.documented-uart-format`：正文称串口默认 115200、8N1 且可调；原理图确认 DBG 与 TRM 两组 UART 信号，但不包含波特率、帧格式、流控策略或固件配置。（证据：图 d660230e4d50 / 第 1 页 / 原 PDF 第3页 UART0/UART1 仅显示电气网络）
- `interface.documented-usb-otg-adb`：正文称 Type-C 支持主从自动切换、ADB 调试和外接 USB 摄像头；原理图确认 Type-C、CC/ID 与 VBUS 角色控制硬件，但角色策略、ADB 服务、摄像头兼容和固件行为无法由图面确认。（证据：图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页 Type-C 角色硬件，无软件策略）
- `interface.documented-100m-ethernet`：正文称 LLM 调试套件扩展百兆以太网；板上 J2 只引出 AX630C EPHY_TX/RX 差分对，没有磁性器件、RJ45、链路 LED 或速率标注，完整 100M 接口依赖外部调试板。（证据：图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页 J2 仅引出 EPHY 差分对; 图 141a3b26d17b / 第 1 页 / 原 PDF 第9页 U1J EPHY，无外部磁性器件）
- `system.documented-ai-software-stack`：正文称系统内置 Ubuntu 与 StackFlow，预装 Qwen2.5-0.5B，并提供 KWS、ASR、LLM、TTS 和 pipeline；原理图不包含软件镜像、版本、模型文件或运行时配置，实际出厂软件需由镜像清单确认。（证据：图 04d8e4d3a1f4 / 第 1 页 / 原理图仅含硬件，未记录软件镜像或模型）
- `storage.documented-upgrade-paths`：正文称 SD 卡支持固件冷升级与热升级，Type-C 也可作为升级接口；原理图确认 MicroSD、USB 下载启动组合和 Type-C 硬件，但升级包格式、热升级流程、回滚与版本兼容由固件决定。（证据：图 d660230e4d50 / 第 1 页 / 原 PDF 第3页启动表含 USB DL/SD Card; 图 b3098cc77650 / 第 1 页 / 原 PDF 第5页 MicroSD 硬件）
- `interface.documented-rgb-status-semantics`：正文定义红色初始化、绿色就绪，以及蓝闪更新、红色失败、绿色成功；原理图只确认 LP5562 和三颗 RGB LED 的电气连接，颜色状态与闪烁逻辑由软件实现。（证据：图 3cd38ef8bf5d / 第 1 页 / 原 PDF 第7页 LP5562 与 RGB LED，无状态逻辑）
- `review.soc-performance`：AX630C 的 CPU 主频与 INT4/INT8 NPU 算力适用哪些运行条件；原因：原理图只确认 AX630C 型号，不含性能参数。
- `review.lpddr4-capacity`：量产 LPDDR4 的具体料号、4GB 容量和 1GB/3GB 分配由哪份 BOM 与软件配置确认；原因：U8 图符没有料号、密度或软件分区。
- `review.emmc-capacity`：量产 eMMC 的具体料号和 32GB 容量是什么；原因：U11 只标接口标准 EMMC_V5.1。
- `review.power-consumption`：0.5W 空载与 1.5W 满载功耗的模型负载、外设状态和测量边界是什么；原因：原理图没有电流检测或性能测试条件。
- `review.speaker-spec`：量产扬声器是否为 8ohm 1W 2014 腔体及其具体料号和连接方式；原因：原理图只有功放差分输出网络。
- `review.uart-format`：TRM UART 与 DBG UART 的默认波特率、帧格式、流控和可调范围是什么；原因：原理图只确认 UART 电气网络。
- `review.usb-otg-adb`：USB 主从自动切换、ADB 与外设兼容由哪个系统镜像和驱动版本保证；原因：原理图只确认 Type-C 角色检测与供电硬件。
- `review.ethernet-debug-kit`：LLM 调试套件如何完成百兆以太网磁性器件、RJ45、PHY 配置与认证；原因：主板只在 FPC 上引出 EPHY 差分对。
- `review.ai-software-stack`：量产镜像实际预装哪些 Ubuntu、StackFlow、模型和 KWS/ASR/LLM/TTS 版本；原因：原理图不能验证软件镜像和模型内容。
- `review.upgrade-paths`：SD 卡冷升级、热升级和 Type-C 升级的包格式、版本兼容与失败回滚流程是什么；原因：原理图只确认启动介质和物理接口。
- `review.rgb-status-semantics`：RGB 工作与升级状态定义适用哪些固件版本和异常状态；原因：LP5562 电路不包含软件状态机。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `04d8e4d3a1f437648d64f0954da6e7d4209fe030dd80e12e5d0fc21294ab27df` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_02.png` |
| 2 | 1 | `d660230e4d50db57eb25c1a5b8f9316e1cded68db9b69c0f3c6db53fd77037fc` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_03.png` |
| 3 | 1 | `a26d069d6b4ed101321cf768d1a0ffaea0206507b2c1300b7e61028077627767` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_04.png` |
| 4 | 1 | `b3098cc77650a26b76198ae615d4047069e89cf24f3e9c681b172d35b936f3f1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_05.png` |
| 5 | 1 | `00b1d013437da8f15a51912587a12f6c6eaf685c768689d73d16de0b171bcee3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_06.png` |
| 6 | 1 | `3cd38ef8bf5d582ca4f6ded3f8b34f5f26951091096fa3c8fbc35fac9b7ee71a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_07.png` |
| 7 | 1 | `e996fa2558a73720ba0f6b541a2d5ab8057c28f5039b8e41d8241da1263d2408` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_08.png` |
| 8 | 1 | `141a3b26d17b1ea2281ff2704819e269f807faf914febf0a5bffb52d34561338` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_09.png` |
| 9 | 1 | `225a0cfb34baeb01152e260ae545722a1e21cf41ed2af775108486e605f7f161` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/992/M140_Sch_M5_Module-LLM_page_10.png` |

---

源文档：`zh_CN/module/Module-LLM.md`

源文档 SHA-256：`e07eddde2c93dbc85c24820c2cfaa3afcaefbce4a637cb9649ff1caf71520b71`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
