# StamPLC PoE 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StamPLC PoE |
| SKU | A165 |
| 产品 ID | `stamplc-poe-c8d18c868a51` |
| 源文档 | `zh_CN/stamplc/StamPLC_PoE.md` |

## 概述

两张原理图页面覆盖 StamPLC PoE 的 W5500 以太网、HJB-6118ANL RJ45/MagJack、StamPLC SPI 总线和多源电源。W5500 通过 25MHz 晶体工作，PHYTX/PHYRX 差分对经阻抗网络连接 MagJack，SPI 映射到 G8/G9/G7/G11，RST/INT 使用 G3/G14。PoE 中心抽头进入 DP1435 并形成 +12V，TPS560200 再生成 +5V，LP5907 生成 D3V3/A3V3；SYS_VIN 与 EXT_5V 提供替代电源入口。图面未标 IEEE802.3af 输入范围与功率、W5500 协议/速率/Socket 能力、UDP 唤醒、宿主侧共享线影响或机械安装参数。

## 检索关键词

`StamPLC PoE`、`A165`、`W5500`、`HJB-6118ANL`、`DP1435`、`TPS560200`、`LP5907MFX-3.3/NOPB`、`PoE`、`IEEE802.3af`、`RJ45`、`MagJack`、`PHYTX_P`、`PHYTX_N`、`PHYRX_P`、`PHYRX_N`、`SPI_MOSI`、`SPI_MISO`、`SPI_SCK`、`SPI_CS_EXT`、`G8`、`G9`、`G7`、`G11`、`G3_SYS_RST`、`G14_SYS_INT`、`SYS_VIN`、`EXT_5V`、`SYS_12V`、`+12`、`+5`、`D3V3`、`A3V3`、`25MHz`、`10/100M`、`TCP`、`UDP`、`8 Socket`、`ACTLED`、`LINKLED`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | W5500 | SPI 以太网控制器，连接 MAC/PHY 差分对、复位、中断、时钟与链路指示 | 图 f495246d1551 / 第 1 页 / B3-C3 U3 W5500 pins1-48 |
| U1 | HJB-6118ANL | 带磁性器件、链路 LED 和 PoE 中心抽头的 RJ45 接口 | 图 f495246d1551 / 第 1 页 / C1-D2 U1 HJB-6118ANL、TD/RD、ACTLED/LINKLED 与 VC 中心抽头 |
| U2 | DP1435 | 由 RJ45 PoE 中心抽头供电并输出 SYS_12V 的受电电源模块 | 图 705be4f8ba4d / 第 1 页 / B2 U2 DP1435、VC2+/VC2-/VC+/VC- 与 SYS_12V |
| U4 | TPS560200 | +12V 到 +5V 的降压转换器 | 图 705be4f8ba4d / 第 1 页 / B2-C3 U4 TPS560200、L2 与 +12/+5 |
| U5 | LP5907MFX-3.3/NOPB | +5V 到 D3V3 的低噪声 LDO，并经滤波形成 A3V3 | 图 705be4f8ba4d / 第 1 页 / D2-D3 U5 LP5907、L3/L4 与 D3V3/A3V3 |
| H1,U7 | 2x8 StamPLC-Bus connectors | StamPLC 主机电源、I2C、SPI、复位、中断与扩展信号连接 | 图 f495246d1551 / 第 1 页 / A1 H1 与 B1 U7 2x8 connectors |
| X1 | 25M CL20pF | W5500 外部 25MHz 晶体 | 图 f495246d1551 / 第 1 页 / C2 X1 25M、R14/R20 与 C24/C25 |

## 系统结构

### W5500 以太网控制核心

U3 明确标为 W5500，页面展开 PHYTX/PHYRX、MOSI/MISO/SCLK/SCSn、INTn、RSTn、XI/XO、ACTLED/LINKLED 以及数字/模拟电源引脚。

- 参数与网络：`controller=W5500`
- 证据：图 f495246d1551 / 第 1 页 / B3-C3 U3 W5500

## 电源

### PoE 中心抽头到 12V 电源路径

U1 MagJack 的 VC2+/VC2-/VC+/VC- 四条 PoE 中心抽头网络进入 U2 DP1435，U2 输出 SYS_12V，经 L1 0ohm、F1 和 D1 SS54 形成 +12V。

- 参数与网络：`poe_module=DP1435`；`intermediate_net=SYS_12V`；`output_net=+12`
- 证据：图 f495246d1551 / 第 1 页 / C1 U1 VC center taps; 图 705be4f8ba4d / 第 1 页 / B2 U2 DP1435、L1/F1/D1 与 +12

### 12V、SYS_VIN 与 EXT_5V 多源电源路径

SYS_VIN 通过 D2 1N5819HW 接入 +12 节点，U4 TPS560200 将 +12 经 L2 10uH 降压为 +5，+5 再通过 D3 1N5819HW 连接 EXT_5V；该结构提供 PoE、SYS_VIN 和 EXT_5V 三个物理供电入口。

- 参数与网络：`input_paths=PoE,SYS_VIN,EXT_5V`；`buck=TPS560200`；`five_v_net=+5`
- 证据：图 705be4f8ba4d / 第 1 页 / B1-C3 D2/U4/L2/D3、SYS_VIN/+12/+5/EXT_5V

### D3V3 与 A3V3 分离供电

U5 LP5907MFX-3.3/NOPB 由 +5 生成 D3V3，R18 0ohm 与 L3/L4 120ohm@100MHz 滤波网络形成 A3V3，R19 0ohm 连接数字地与 AGND。

- 参数与网络：`regulator=LP5907MFX-3.3/NOPB`；`digital_rail=D3V3`；`analog_rail=A3V3`
- 证据：图 705be4f8ba4d / 第 1 页 / D2-D3 U5/R18/R19/L3/L4

## 接口

### W5500 PHY 到 RJ45 MagJack

W5500 PHYTX_P/N 与 PHYRX_P/N 经 R21-R24 各 33ohm 及 100ohm 差分阻抗网络连接 U1 HJB-6118ANL 的 TD+/TD-/RD+/RD-，ACTLED/LINKLED 连接 MagJack 指示灯。

- 参数与网络：`magjack=HJB-6118ANL`；`series_resistors_ohm=33`；`differential_impedance_ohm=100`
- 证据：图 f495246d1551 / 第 1 页 / B2-C2 W5500 PHY、R21-R24 与 U1 TD/RD/LED

### 双 2x8 StamPLC-Bus 连接

H1 与 U7 将 SYS_VIN、EXT_5V、GND、G13_SYS_SDA、G15_SYS_SCL、G3_SYS_RST、G14_SYS_INT、G8/G9/G7/G11 SPI 和 EXT_G40/EXT_G41 引入并贯通模块。

- 参数与网络：`connectors=H1,U7`；`bus_pins_each=16`；`signals=VIN,5V,I2C,RST,INT,SPI,EXT`
- 证据：图 f495246d1551 / 第 1 页 / A1 H1 与 B1 U7 net labels

## 总线

### StamPLC 到 W5500 的 SPI 映射

W5500 MOSI、MISO、SCLK、SCSn 经 RP3 22ohm 阵列分别连接 G8_SPI_MOSI、G9_SPI_MISO、G7_SPI_SCK、G11_SPI_CS_EXT。

- 参数与网络：`mosi=G8`；`miso=G9`；`sck=G7`；`cs=G11`；`series_ohm=22`
- 证据：图 f495246d1551 / 第 1 页 / B3 U3 pins32-35、RP3 与 G8/G9/G7/G11

## 时钟

### W5500 25MHz 参考时钟

W5500 XI/XCLKIN 与 XO 连接 X1 25M CL20pF 晶体，C24/C25 各 22pF，R14 1M 跨接晶体，R20 0ohm 串接 XI。

- 参数与网络：`frequency_mhz=25`；`load_cap_pf=22`
- 证据：图 f495246d1551 / 第 1 页 / C2 W5500 XI/XO 与 X1/R14/R20/C24/C25

## 复位

### W5500 复位与中断网络

W5500 RSTn 连接 G3_SYS_RST 并由 RP1 10K 上拉到 D3V3，INTn 连接 G14_SYS_INT；U7 侧 R9 将 G14_SYS_INT 上拉，R12 将 G11_SPI_CS_EXT 上拉。

- 参数与网络：`reset=G3_SYS_RST`；`interrupt=G14_SYS_INT`；`reset_pullup=10K to D3V3`
- 证据：图 f495246d1551 / 第 1 页 / A3-B3 RP1/U3 RSTn/INTn 与 B1 U7 R9/R12

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | W5500 以太网控制核心 | `controller=W5500` |
| 接口 | W5500 PHY 到 RJ45 MagJack | `magjack=HJB-6118ANL`；`series_resistors_ohm=33`；`differential_impedance_ohm=100` |
| 总线 | StamPLC 到 W5500 的 SPI 映射 | `mosi=G8`；`miso=G9`；`sck=G7`；`cs=G11`；`series_ohm=22` |
| 复位 | W5500 复位与中断网络 | `reset=G3_SYS_RST`；`interrupt=G14_SYS_INT`；`reset_pullup=10K to D3V3` |
| 时钟 | W5500 25MHz 参考时钟 | `frequency_mhz=25`；`load_cap_pf=22` |
| 接口 | 双 2x8 StamPLC-Bus 连接 | `connectors=H1,U7`；`bus_pins_each=16`；`signals=VIN,5V,I2C,RST,INT,SPI,EXT` |
| 电源 | PoE 中心抽头到 12V 电源路径 | `poe_module=DP1435`；`intermediate_net=SYS_12V`；`output_net=+12` |
| 电源 | 12V、SYS_VIN 与 EXT_5V 多源电源路径 | `input_paths=PoE,SYS_VIN,EXT_5V`；`buck=TPS560200`；`five_v_net=+5` |
| 电源 | D3V3 与 A3V3 分离供电 | `regulator=LP5907MFX-3.3/NOPB`；`digital_rail=D3V3`；`analog_rail=A3V3` |
| 接口 | 10/100M、协议栈与 8 路硬件 Socket | `documented_rate_mbps=10,100`；`documented_sockets=8`；`documented_protocols=TCP,UDP,ICMP,IPv4,ARP,IGMP,PPPoE` |
| 电源 | IEEE802.3af、37-57V 与 13W PoE 额定 | `documented_standard=IEEE802.3af`；`documented_input_v=37-57`；`documented_max_w=13` |
| 接口 | UDP 以太网唤醒 | `documented_feature=UDP wake over Ethernet` |
| 系统结构 | StamPLC 宿主共享 RST 与 INT 冲突 | `reset_net=G3_SYS_RST`；`interrupt_net=G14_SYS_INT`；`documented_host_device=PI4IOE,LCD` |
| 系统结构 | DIN 导轨、挂孔与外形参数 | `documented_installation=DIN rail,hanging hole`；`documented_size_mm=77.0x38.0x27.1` |

## 待确认事项

- `interface.documented-network-features`：正文称 W5500 集成 10/100M MAC/PHY、自适应全双工/半双工、8 路硬件 Socket，并支持 TCP、UDP、ICMP、IPv4、ARP、IGMP、PPPoE；原理图确认 W5500 和以太网物理连接，但不包含协议栈版本、Socket 配置或链路性能。（证据：图 f495246d1551 / 第 1 页 / W5500 与 PHY 硬件，无协议或性能标注）
- `power.documented-poe-rating`：正文称 PoE 符合 IEEE802.3af，输入范围 DC 37-57V，最大功率 13W；原理图确认 RJ45 中心抽头与 DP1435 电源路径，但没有标准分类、电压范围、功率、热设计或隔离耐压标注。（证据：图 705be4f8ba4d / 第 1 页 / DP1435 路径无 IEEE 分类、输入范围或功率标注）
- `interface.documented-udp-wake`：正文称支持通过 UDP 实现以太网唤醒；原理图没有唤醒状态机、主机低功耗域、唤醒触发路径或固件配置，实际行为需由 W5500 驱动与 StamPLC 固件确认。（证据：图 f495246d1551 / 第 1 页 / 硬件图无 UDP 或唤醒状态机）
- `system.documented-shared-reset-interrupt`：正文称 G3_SYS_RST 同时连接 StamPLC LCD、PI4IOE 和外部 W5500，G14_SYS_INT 与 PI4IOE 中断共享，驱动初始化需避免复位屏幕并屏蔽 PI4IOE 中断；模块图只确认 W5500 使用 G3/G14，宿主内部连接需由 StamPLC 原理图和软件验证。（证据：图 f495246d1551 / 第 1 页 / 本模块只显示 W5500 RSTn/INTn 到 G3/G14）
- `system.documented-mechanical-installation`：正文称支持 DIN 导轨和挂孔安装，产品尺寸 77.0x38.0x27.1mm；当前两页电气原理图没有板框、外壳、导轨卡扣、孔位或机械公差。（证据：图 f495246d1551 / 第 1 页 / 电气页无机械结构）
- `review.network-features`：量产 W5500 固件的 10/100M、双工、自适应、8 Socket 和协议支持如何验证；原因：原理图只确认 W5500 物理硬件。
- `review.poe-rating`：IEEE802.3af 分类、37-57V 输入、13W 功率、热设计和隔离额定如何确认；原因：DP1435 电源路径没有这些额定参数。
- `review.udp-wake`：UDP 唤醒的触发包、低功耗状态、主机唤醒路径与驱动版本是什么；原因：该能力由协议与固件实现，图面没有状态机。
- `review.shared-lines`：StamPLC 主板上 G3 RST 与 G14 INT 的完整共享拓扑和驱动规避策略是什么；原因：当前资源只包含扩展模块，缺少宿主 LCD/PI4IOE 原理图。
- `review.mechanical-installation`：DIN 导轨、挂孔、外形尺寸和机械公差由哪份结构图确认；原因：当前资源只有电气原理图。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f495246d1551b5334338cd70057575408ab667db0657ad3be496f982f4cf161a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/SCH_StamPLC_PoE_SCH_MAIN_V1.0_20251104_2025_12_02_17_25_33_page_01.png` |
| 2 | 1 | `705be4f8ba4d9f620979dae7113fa84df0f44fb98a7f8a120cbd090f538c1f8b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1202/SCH_StamPLC_PoE_SCH_MAIN_V1.0_20251104_2025_12_02_17_25_33_page_02.png` |

---

源文档：`zh_CN/stamplc/StamPLC_PoE.md`

源文档 SHA-256：`50a71d2f9aced5d29901b16d291ee5aeb4a8cec7c7637af7ab1692b34dbe768e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
