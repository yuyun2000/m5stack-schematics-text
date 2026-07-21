# Module LoRaWAN-EU868 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module LoRaWAN-EU868 |
| SKU | M148 |
| 产品 ID | `module-lorawan-eu868-17765fac0b44` |
| 源文档 | `zh_CN/module/Module_LoRaWAN-EU868.md` |

## 概述

单页原理图展示 Module LoRaWAN-EU868 HW1.0：U1 RAK3172-8-SM-I 由 3V3 供电，UART2 经 22ohm 串联电阻连接 RX/TX 公共网络，SW1 十二位拨码将 TX、RX 和 RST 分别路由到多组 M5-Bus GPIO。J1 为 30-pin M5Stack_BUS，U2 LP5907_3.3V 从 +5V 生成 3V3，JP2 引出 3V3/BOOT0/RST/RX/TX/GND，RF 脚经预留匹配位连接 ANT_IPEX。图面未标 STM32WLE5 内部容量、EU868 频率、LoRaWAN 协议版本、射频性能、串口格式、外置 SMA 天线参数或工作电流。

## 检索关键词

`Module LoRaWAN-EU868`、`M148`、`HW1.0`、`RAK3172-8-SM-I`、`RAK3172`、`STM32WLE5`、`EU868`、`863-870MHz`、`LoRa`、`LoRaWAN 1.0.3`、`Class A`、`Class B`、`Class C`、`OTAA`、`ABP`、`P2P`、`LP5907_3.3V`、`M5Stack_BUS`、`SW1`、`DIP Switch`、`UART2_TX`、`UART2_RX`、`RX`、`TX`、`RST`、`BOOT0`、`ANT_IPEX`、`SMA antenna`、`G1`、`G17`、`G15`、`G12`、`G0`、`G3`、`G16`、`G13`、`G34`、`G35`、`G25`、`115200bps`、`AT command`、`-137dBm`、`19dBm`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | RAK3172-8-SM-I | LoRaWAN 核心模组，使用 UART2、复位、启动和 RF 接口 | 图 4e46330743c1 / 第 1 页 / B2-C2 U1 RAK3172-8-SM-I |
| U2 | LP5907_3.3V | +5V 到 3V3 的线性稳压器 | 图 4e46330743c1 / 第 1 页 / C4 U2 LP5907_3.3V、C8/C9 与 +5/3V3 |
| SW1 | SW DIP-12 | TX、RX 与 RST 到 M5-Bus GPIO 的选择开关 | 图 4e46330743c1 / 第 1 页 / C3 SW1 pins1-24 与 G1/G17/G15/G12/G0/G3/G16/G13/G34/G35/G25 |
| J1 | M5Stack_BUS | 30-pin M5-Bus 堆叠连接器 | 图 4e46330743c1 / 第 1 页 / B4 J1 M5Stack_BUS pins1-30 |
| E2,C6,L1,C7 | ANT_IPEX / NC matching network | RAK3172 RF 引脚到 IPEX 天线口的预留匹配链路 | 图 4e46330743c1 / 第 1 页 / B2-B3 U1 pin12 RF、C6/L1/C7 NC 与 E2 ANT_IPEX |
| JP2 | 1x6 service header | 3V3、BOOT0、RST、RX、TX 和 GND 服务接口 | 图 4e46330743c1 / 第 1 页 / C4-D4 JP2 pins1-6 |

## 系统结构

### RAK3172-8-SM-I 核心模组

U1 明确标为 RAK3172-8-SM-I，VDD 连接 3V3，pins23/17/18/28 接 GND；UART2、BOOT0、RST、RF 和部分调试引脚在本页展开。

- 参数与网络：`module=RAK3172-8-SM-I`；`supply=3V3`
- 证据：图 4e46330743c1 / 第 1 页 / B2-C2 U1、3V3、GND、UART2、BOOT0/RST/RF

## 电源

### +5V 到 3V3 稳压

J1 pin28 的 +5V 网络经 U2 LP5907_3.3V 生成 3V3，输入与输出各配置 C8/C9 1uF；3V3 为 U1 VDD 和本地控制网络供电。

- 参数与网络：`input=+5V`；`output=3V3`；`regulator=LP5907_3.3V`
- 证据：图 4e46330743c1 / 第 1 页 / B4-C4 J1 pin28、U2、C8/C9 与 U1 VDD

## 接口

### RAK3172 UART2 与主机 RX/TX 网络

U1 UART2_TX 经 R1 22ohm 连接公共 RX 网络，UART2_RX 经 R2 22ohm 连接公共 TX 网络；UART1_TX/RX pins4/5 在本页未使用。

- 参数与网络：`module_tx=UART2_TX`；`host_net_rx=RX`；`module_rx=UART2_RX`；`host_net_tx=TX`；`series_resistors_ohm=22`
- 证据：图 4e46330743c1 / 第 1 页 / C2 U1 UART2_TX/RX、R1/R2 与 RX/TX

### 十二位拨码 UART 与复位路由

SW1 pins1-5 把 TX 选择到 G1/G17/G15/G12/G0，pins6-10 把 RX 选择到 G3/G16/G13/G34/G35，pins11-12 把 RST 选择到 G13/G25。

- 参数与网络：`tx_candidates=G1,G17,G15,G12,G0`；`rx_candidates=G3,G16,G13,G34,G35`；`reset_candidates=G13,G25`
- 证据：图 4e46330743c1 / 第 1 页 / C3 SW1 left common nets TX/RX/RST 与 right GPIO labels

### M5-Bus 可选 UART 与复位脚

J1 上 G35/G3/G16/G13/G34 对应可选 RX，G1/G17/G12/G15/G0 对应可选 TX，G25 与 G13 对应可选 RST；pins25/27/29 为 HPWR，pin28 为 +5V。

- 参数与网络：`connector=M5Stack_BUS`；`rx_pins=2,13,15,22,26`；`tx_pins=14,16,21,23,24`；`reset_pins=8,22`
- 证据：图 4e46330743c1 / 第 1 页 / B4 J1 pins2/8/13-16/21-29 与彩色 GPIO 网络

## 复位

### BOOT0、RST 与服务接口

BOOT0 由 R4 10K 下拉到 GND，RST 由 R3 10K 上拉到 3V3 并由 C5 1uF 接地；JP2 依次引出 3V3、BOOT0、RST、RX、TX 与 GND。

- 参数与网络：`boot0_default=low`；`reset_default=high`；`service_header=3V3,BOOT0,RST,RX,TX,GND`
- 证据：图 4e46330743c1 / 第 1 页 / B1-C2 R3/R4/C5 与 C4-D4 JP2

## 射频

### IPEX 天线口与预留匹配网络

U1 pin12 RF 经串联 L1 位置连接 E2 ANT_IPEX，C6/C7 为对地匹配位置；C6、L1、C7 均标为 NC，形成可调但默认不装的匹配网络。

- 参数与网络：`antenna_connector=ANT_IPEX`；`matching_components=C6,L1,C7`；`population=NC`
- 证据：图 4e46330743c1 / 第 1 页 / B2-B3 U1 RF、C6/L1/C7 与 E2 ANT_IPEX

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | RAK3172-8-SM-I 核心模组 | `module=RAK3172-8-SM-I`；`supply=3V3` |
| 电源 | +5V 到 3V3 稳压 | `input=+5V`；`output=3V3`；`regulator=LP5907_3.3V` |
| 接口 | RAK3172 UART2 与主机 RX/TX 网络 | `module_tx=UART2_TX`；`host_net_rx=RX`；`module_rx=UART2_RX`；`host_net_tx=TX`；`series_resistors_ohm=22` |
| 接口 | 十二位拨码 UART 与复位路由 | `tx_candidates=G1,G17,G15,G12,G0`；`rx_candidates=G3,G16,G13,G34,G35`；`reset_candidates=G13,G25` |
| 接口 | M5-Bus 可选 UART 与复位脚 | `connector=M5Stack_BUS`；`rx_pins=2,13,15,22,26`；`tx_pins=14,16,21,23,24`；`reset_pins=8,22` |
| 复位 | BOOT0、RST 与服务接口 | `boot0_default=low`；`reset_default=high`；`service_header=3V3,BOOT0,RST,RX,TX,GND` |
| 射频 | IPEX 天线口与预留匹配网络 | `antenna_connector=ANT_IPEX`；`matching_components=C6,L1,C7`；`population=NC` |
| 核心器件 | 内置 STM32WLE5 与存储容量 | `documented_mcu=STM32WLE5`；`documented_flash_kb=256`；`documented_ram_kb=64` |
| 射频 | EU868 863-870MHz 工作频段 | `documented_region=EU868`；`documented_frequency_mhz=863-870` |
| 射频 | 接收灵敏度与最大发射功率 | `documented_sensitivity_dbm=-137`；`documented_max_tx_dbm=19` |
| 系统结构 | LoRaWAN 1.0.3、Class A/B/C、OTAA/ABP 与 P2P | `documented_protocol=LoRaWAN 1.0.3`；`documented_classes=A,B,C`；`documented_activation=OTAA,ABP`；`documented_modes=LoRaWAN,P2P` |
| 接口 | UART 115200bps 与 AT 指令 | `documented_baud=115200`；`documented_protocol=AT command` |
| 射频 | 外置 SMA 胶棒天线规格 | `documented_connector=SMA female thread male pin`；`documented_size_mm=198x13`；`documented_gain_dbi=2.8`；`documented_vswr_max=1.3` |
| 电源 | 待机、休眠、接收与连续发送电流 | `documented_standby_5v_ma=6.7`；`documented_sleep_5v_ua=9`；`documented_sleep_3v3_ua=3.69`；`documented_rx_5v_ma=8.27`；`documented_tx_5v_ma=80.38`；`documented_bandwidth_khz=125` |

## 待确认事项

- `component.documented-stm32wle5-memory`：正文称 RAK3172-8-SM-I 内置 STM32WLE5，并配置 256KB Flash 与 64KB RAM；原理图只显示封装模组 U1，没有展开内部 MCU、Flash 或 RAM。（证据：图 4e46330743c1 / 第 1 页 / U1 只标 RAK3172-8-SM-I，未展开内部芯片）
- `rf.documented-eu868-band`：正文称产品针对 EU868 并工作于 863-870MHz；原理图没有频率标注、射频滤波参数、匹配值或区域版本配置，无法仅由本页验证频段范围。（证据：图 4e46330743c1 / 第 1 页 / RF 链路只有 ANT_IPEX 与 NC 匹配位，无频段标注）
- `rf.documented-performance`：正文给出 -137dBm 接收灵敏度和最大 19dBm 发射功率；原理图没有射频测试点、增益路径、校准条件、带宽或扩频因子，无法验证这些性能指标。（证据：图 4e46330743c1 / 第 1 页 / RF 链路无灵敏度、功率或测试条件）
- `system.documented-lorawan-modes`：正文称内置 LoRaWAN 1.0.3 协议栈，支持 Class A/Class B/Class C、OTAA/ABP 激活与 LoRa P2P；这些能力由 RAK3172 固件实现，原理图不包含协议栈或固件版本。（证据：图 4e46330743c1 / 第 1 页 / 硬件原理图无协议栈或固件信息）
- `interface.documented-uart-at`：正文称 UART 默认 115200bps 并使用 AT 指令；原理图只确认 UART2_TX/RX、电阻和拨码路由，不包含波特率、帧格式、流控或 AT 固件版本。（证据：图 4e46330743c1 / 第 1 页 / U1 UART2 与 SW1 仅显示电气路由）
- `rf.documented-sma-stick-antenna`：正文称配套 198x13mm 胶棒天线，SMA 内螺内针，工作 863-870MHz，增益 2.8dBi、驻波比不高于 1.3；主板原理图只显示 ANT_IPEX，没有 SMA 转接、天线结构或射频实测数据。（证据：图 4e46330743c1 / 第 1 页 / 图面天线端仅标 E2 ANT_IPEX）
- `power.documented-current-modes`：正文给出 5V 待机 6.70mA、5V 休眠 9uA、3.3V 休眠 3.69uA、125K 带宽 P2P 接收 5V 8.27mA、连续发送 5V 80.38mA；原理图没有电流检测、测试点、射频配置或工作状态边界。（证据：图 4e46330743c1 / 第 1 页 / U2 与 U1 供电路径无电流测量或模式边界）
- `review.stm32wle5-memory`：RAK3172-8-SM-I 量产版本内部是否为 STM32WLE5 及 256KB Flash 和 64KB RAM；原因：核心 MCU 与容量被封装在模组内，原理图没有展开。
- `review.eu868-band`：量产 RF 配置是否完整覆盖 EU868 863-870MHz 及哪些区域法规；原因：图面没有频段、滤波参数或区域配置。
- `review.rf-performance`：-137dBm 灵敏度和 19dBm 发射功率适用哪些 LoRa 参数、频点和测试条件；原因：原理图没有射频性能或校准边界。
- `review.lorawan-modes`：量产 RAK3172 固件的 LoRaWAN 协议版本、Class、激活与 P2P 能力是什么；原因：协议能力取决于模组固件，图面不能验证。
- `review.uart-at`：UART 默认帧格式、流控与 RAK3172 AT 指令固件版本是什么；原因：图面只确认串口电气路由。
- `review.sma-antenna`：IPEX 到 SMA 的转接结构及胶棒天线尺寸、增益和驻波比如何验证；原因：主板图只显示 IPEX 天线口，未包含外置天线结构和测试数据。
- `review.current-modes`：各待机、休眠、接收和发送电流对应哪些供电路径、固件与射频配置；原因：原理图没有电流测量电路或工作模式测试条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `4e46330743c14ea4a19441741bee84678fd842d410c5ae23e91e9c22bd14ef37` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/SCH_LoRaWAN868_HW1.0_2026_04_20_16_29_29_page_01.png` |

---

源文档：`zh_CN/module/Module_LoRaWAN-EU868.md`

源文档 SHA-256：`7dcb2417b14ad9308c67c338c309460b3048f493642b81a2f5b72dfb407ce221`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
