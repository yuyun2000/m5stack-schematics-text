# Module LoRa868 v1.2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module LoRa868 v1.2 |
| SKU | M029-V12 |
| 产品 ID | `module-lora868-v1-2-7e034afde4eb` |
| 源文档 | `zh_CN/module/Module-LoRa868_V1.2.md` |

## 概述

Module LoRa868 v1.2 以 U2 E22-900M22S 为无线模组，通过 SPI 的 MOSI、MISO、SCK 连接 J2 M5Stack_BUS。SW1 八位拨码开关为 RST、BUSY 和 NSS 提供多组主机 GPIO 选择，SW2 三位拨码开关为 IRQ 提供 GPIO35/GPIO34/GPIO26 选择。J2 pin28 的 +5 V 经 U1 VRH3301NLEX 转换为 +3.3 V，再通过 FB1 向 U2 VCC 供电；原理图只画出 U2 ANT pin21，未展开外部天线连接器。

## 检索关键词

`Module LoRa868 v1.2`、`M029-V12`、`E22-900M22S`、`SX1262`、`VRH3301NLEX`、`M5Stack_BUS`、`SPI`、`MOSI`、`MISO`、`SCK`、`NSS`、`BUSY`、`RST`、`NRST`、`IRQ`、`DIO1`、`ANT`、`SW DIP-8`、`SW DIP-3`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO25`、`GPIO13`、`GPIO36`、`GPIO2`、`GPIO15`、`GPIO12`、`GPIO5`、`GPIO0`、`GPIO35`、`GPIO34`、`GPIO26`、`R1 33R`、`FB1 120Ω/MB`、`+5V`、`+3.3V`、`SMA`、`868MHz`、`850-930MHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | E22-900M22S | LoRa 无线模组，提供 SPI、NRST、BUSY、DIO1/IRQ、ANT 与 3.3 V 电源接口 | 图 4bf982015f09 / 第 1 页 / B1-C2 U2 E22-900M22S pins1-22 |
| U1 | VRH3301NLEX | 从 +5 V 产生 +3.3 V 的稳压器，EN 直接接 +5 V | 图 4bf982015f09 / 第 1 页 / A1-A2 U1 VRH3301NLEX pins1-5 |
| SW1 | SW DIP-8 | 为 RST、BUSY 和 NSS 选择多个 M5-Bus GPIO 的八位拨码开关 | 图 4bf982015f09 / 第 1 页 / B3-C3 SW1 SW DIP-8 pins1-16 |
| SW2 | SW DIP-3 | 为 IRQ 选择 GPIO35、GPIO34 或 GPIO26 的三位拨码开关 | 图 4bf982015f09 / 第 1 页 / C3 SW2 SW DIP-3 pins1-6 |
| J2 | M5Stack_BUS | 30 针主机接口，提供 +5 V、HPWR、SPI 与可切换的 RST/BUSY/NSS/IRQ GPIO | 图 4bf982015f09 / 第 1 页 / B4-C4 J2 M5Stack_BUS pins1-30 |
| FB1 | 120Ω/MB | +3.3 V 到 U2 VCC 的串联磁珠/滤波器件 | 图 4bf982015f09 / 第 1 页 / C1 FB1 120Ω/MB、U2 VCC pin9 |
| R1 | 33R | U2 SCK 到 J2 GPIO18/pin11 的串联阻尼电阻 | 图 4bf982015f09 / 第 1 页 / C4 SCK/R1 33R/J2 pin11 |
| C1-C6 | 22uF / 100nF | U1 输入/输出及 U2 VCC 的电源储能和高频去耦 | 图 4bf982015f09 / 第 1 页 / A1-A2 C1-C4；C1 C5/C6 |

## 系统结构

### Module LoRa868 v1.2 系统架构

U2 E22-900M22S 通过固定 SPI 与可拨码选择的 RST/BUSY/NSS/IRQ 连接 J2 M5Stack_BUS，U1 将 +5 V 转换为 +3.3 V 并经 FB1 为模组供电。

- 参数与网络：`radio_module=U2 E22-900M22S`；`host=J2 M5Stack_BUS`；`bus=SPI`；`switched_controls=RST, BUSY, NSS, IRQ`；`power=+5V -> U1 VRH3301NLEX -> +3.3V -> FB1 -> U2 VCC`
- 证据：图 4bf982015f09 / 第 1 页 / 整页 U1/U2/SW1/SW2/J2 连接

## 核心器件

### E22-900M22S 引脚分组

U2 pins1-5、10-12、20、22 为 GND，pin9 VCC，pin13 DIO1/IRQ，pin14 BUSY，pin15 NRST/RST，pins16/17/18/19 为 MISO/MOSI/SCK/NSS，pin21 ANT；RXEN/TXEN/DIO2 pins6-8 未连接。

- 参数与网络：`ground=pins1-5/10-12/20/22`；`power=pin9 VCC`；`irq=pin13 DIO1`；`busy=pin14 BUSY`；`reset=pin15 NRST`；`spi=pin16 MISO; pin17 MOSI; pin18 SCK; pin19 NSS`；`rf=pin21 ANT`；`unused=pin6 RXEN; pin7 TXEN; pin8 DIO2`
- 证据：图 4bf982015f09 / 第 1 页 / B1-C2 U2 pins1-22 labels

## 电源

### +5 V 至 +3.3 V 稳压

J2 pin28 的 +5 V 连接 U1 VIN pin4 和 EN pin3，U1 VOUT pin1 形成 +3.3 V；VSS pins2/5 接 GND。

- 参数与网络：`input=+5V from J2 pin28`；`regulator=U1 VRH3301NLEX`；`vin=pin4`；`enable=pin3 tied +5V`；`output=pin1 +3.3V`；`ground=pins2/5`
- 证据：图 4bf982015f09 / 第 1 页 / A1-A2 +5V/U1/+3.3V；C4 J2 pin28

### 稳压器输入输出电容

U1 输入配置 C1 22 uF 与 C2 100 nF，输出配置 C3 22 uF 与 C4 100 nF，全部对地。

- 参数与网络：`input_caps=C1 22uF; C2 100nF`；`output_caps=C3 22uF; C4 100nF`；`input_rail=+5V`；`output_rail=+3.3V`
- 证据：图 4bf982015f09 / 第 1 页 / A1-A2 U1/C1-C4

### 无线模组 VCC 滤波

+3.3 V 经 FB1 120 Ω/MB 串联到 U2 VCC pin9，VCC 节点由 C5 22 uF 与 C6 100 nF 对地去耦。

- 参数与网络：`source=+3.3V`；`filter=FB1 120Ω/MB`；`rail=VCC`；`load=U2 pin9`；`decoupling=C5 22uF; C6 100nF`
- 证据：图 4bf982015f09 / 第 1 页 / C1 +3.3V/FB1/VCC/C5/C6/U2 pin9

## 接口

### M5Stack_BUS 已用网络

J2 使用 pins1/3/5 GND、pin7 GPIO23/MOSI、pin9 GPIO19/MISO、pin11 GPIO18/SCK、pin28 +5 V；拨码候选为 pins2/26/10 GPIO35/GPIO34/GPIO26（IRQ）、pins8/22 GPIO25/GPIO13（RST）、pins4/19 GPIO36/GPIO2（BUSY）及 pins23/21/20/24 GPIO15/GPIO12/GPIO5/GPIO0（NSS）。

- 参数与网络：`ground=pins1/3/5`；`spi=pin7 GPIO23 MOSI; pin9 GPIO19 MISO; pin11 GPIO18 SCK`；`irq=pin2 GPIO35; pin26 GPIO34; pin10 GPIO26`；`reset=pin8 GPIO25; pin22 GPIO13`；`busy=pin4 GPIO36; pin19 GPIO2`；`nss=pin23 GPIO15; pin21 GPIO12; pin20 GPIO5; pin24 GPIO0`；`power=pin28 +5V`；`hpwr=pins25/27/29 tied HPWR`；`battery=pin30 BAT not connected`
- 证据：图 4bf982015f09 / 第 1 页 / B4-C4 J2 M5Stack_BUS pins1-30

### 未使用的 RXEN/TXEN/DIO2

U2 RXEN pin6、TXEN pin7 与 DIO2 pin8 在页面上标记为未连接，没有路由到 J2 或开关。

- 参数与网络：`unused=RXEN pin6; TXEN pin7; DIO2 pin8`；`host_route=none shown`
- 证据：图 4bf982015f09 / 第 1 页 / C1 U2 pins6-8 red no-connect marks

## 总线

### E22-900M22S SPI 主机连接

U2 MOSI pin17 直接连接 J2 pin7/GPIO23，MISO pin16 直接连接 J2 pin9/GPIO19，SCK pin18 经 R1 33 Ω 连接 J2 pin11/GPIO18；NSS 由 SW1 选择。

- 参数与网络：`device=U2 E22-900M22S`；`mosi=J2 pin7 GPIO23 -> U2 pin17 MOSI`；`miso=U2 pin16 MISO -> J2 pin9 GPIO19`；`clock=J2 pin11 GPIO18 -> R1 33R -> U2 pin18 SCK`；`chip_select=U2 pin19 NSS via SW1`；`direction=MOSI/SCK/NSS host-to-module; MISO module-to-host`
- 证据：图 4bf982015f09 / 第 1 页 / C2 U2 pins16-19；C4 J2 pins7/9/11 and R1

## GPIO 与控制信号

### RST GPIO 选择

U2 NRST pin15 的 RST 网络连接 SW1 公共侧 pins9/10，可通过开关选择 GPIO25/J2 pin8 或 GPIO13/J2 pin22。

- 参数与网络：`source=U2 NRST pin15`；`net=RST`；`switch=SW1 pins9/10`；`option_1=GPIO25 J2 pin8`；`option_2=GPIO13 J2 pin22`；`direction=host-to-module`
- 证据：图 4bf982015f09 / 第 1 页 / C2 RST；B3-C3 SW1 rows GPIO25/GPIO13；J2 pins8/22

### BUSY GPIO 选择

U2 BUSY pin14 连接 SW1 公共侧 pins11/12，可通过开关选择 GPIO36/J2 pin4 或 GPIO2/J2 pin19。

- 参数与网络：`source=U2 BUSY pin14`；`net=BUSY`；`switch=SW1 pins11/12`；`option_1=GPIO36 J2 pin4`；`option_2=GPIO2 J2 pin19`；`direction=module-to-host`
- 证据：图 4bf982015f09 / 第 1 页 / C2 BUSY；B3-C3 SW1 rows GPIO36/GPIO2；J2 pins4/19

### NSS GPIO 选择

U2 NSS pin19 连接 SW1 公共侧 pins13-16，可通过四个开关选择 GPIO15/J2 pin23、GPIO12/J2 pin21、GPIO5/J2 pin20 或 GPIO0/J2 pin24。

- 参数与网络：`source=U2 NSS pin19`；`net=NSS`；`switch=SW1 pins13-16`；`options=GPIO15 pin23; GPIO12 pin21; GPIO5 pin20; GPIO0 pin24`；`direction=host-to-module`
- 证据：图 4bf982015f09 / 第 1 页 / C2 NSS；B3-C3 SW1 rows GPIO15/GPIO12/GPIO5/GPIO0；J2

### IRQ GPIO 选择

U2 DIO1 pin13 的 IRQ 网络连接 SW2 公共侧 pins4-6，可通过三个开关选择 GPIO35/J2 pin2、GPIO34/J2 pin26 或 GPIO26/J2 pin10。

- 参数与网络：`source=U2 DIO1 pin13`；`net=IRQ`；`switch=SW2 pins4-6`；`options=GPIO35 pin2; GPIO34 pin26; GPIO26 pin10`；`direction=module-to-host`
- 证据：图 4bf982015f09 / 第 1 页 / C2 IRQ；C3 SW2 GPIO35/GPIO34/GPIO26；J2 pins2/26/10

## 复位

### 无线模组复位

U2 NRST pin15 仅通过 RST 网络与 SW1 相连，页面未画外部上拉、下拉或 RC 复位网络。

- 参数与网络：`target=U2 NRST pin15`；`net=RST`；`host_selection=SW1 GPIO25/GPIO13`；`pullup=not shown`；`pulldown=not shown`；`rc=not shown`
- 证据：图 4bf982015f09 / 第 1 页 / U2 NRST pin15-to-RST direct line and SW1

## 保护电路

### 接口保护器件

SPI、RST、BUSY、NSS、IRQ 与 ANT 路径上未画 ESD/TVS、串联保护或射频匹配器件；只有 SCK 配置 R1 33 Ω 串联电阻。

- 参数与网络：`esd_tvs=not shown`；`rf_matching=not shown`；`spi_series=R1 33R on SCK only`；`control_series=not shown`
- 证据：图 4bf982015f09 / 第 1 页 / U2-to-SW1/SW2/J2 direct signal paths and ANT pin21

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module LoRa868 v1.2 系统架构 | `radio_module=U2 E22-900M22S`；`host=J2 M5Stack_BUS`；`bus=SPI`；`switched_controls=RST, BUSY, NSS, IRQ`；`power=+5V -> U1 VRH3301NLEX -> +3.3V -> FB1 -> U2 VCC` |
| 核心器件 | E22-900M22S 引脚分组 | `ground=pins1-5/10-12/20/22`；`power=pin9 VCC`；`irq=pin13 DIO1`；`busy=pin14 BUSY`；`reset=pin15 NRST`；`spi=pin16 MISO; pin17 MOSI; pin18 SCK; pin19 NSS`；`rf=pin21 ANT`；`unused=pin6 RXEN; pin7 TXEN; pin8 DIO2` |
| 电源 | +5 V 至 +3.3 V 稳压 | `input=+5V from J2 pin28`；`regulator=U1 VRH3301NLEX`；`vin=pin4`；`enable=pin3 tied +5V`；`output=pin1 +3.3V`；`ground=pins2/5` |
| 电源 | 稳压器输入输出电容 | `input_caps=C1 22uF; C2 100nF`；`output_caps=C3 22uF; C4 100nF`；`input_rail=+5V`；`output_rail=+3.3V` |
| 电源 | 无线模组 VCC 滤波 | `source=+3.3V`；`filter=FB1 120Ω/MB`；`rail=VCC`；`load=U2 pin9`；`decoupling=C5 22uF; C6 100nF` |
| 总线 | E22-900M22S SPI 主机连接 | `device=U2 E22-900M22S`；`mosi=J2 pin7 GPIO23 -> U2 pin17 MOSI`；`miso=U2 pin16 MISO -> J2 pin9 GPIO19`；`clock=J2 pin11 GPIO18 -> R1 33R -> U2 pin18 SCK`；`chip_select=U2 pin19 NSS via SW1`；`direction=MOSI/SCK/NSS host-to-module; MISO module-to-host` |
| GPIO 与控制信号 | RST GPIO 选择 | `source=U2 NRST pin15`；`net=RST`；`switch=SW1 pins9/10`；`option_1=GPIO25 J2 pin8`；`option_2=GPIO13 J2 pin22`；`direction=host-to-module` |
| GPIO 与控制信号 | BUSY GPIO 选择 | `source=U2 BUSY pin14`；`net=BUSY`；`switch=SW1 pins11/12`；`option_1=GPIO36 J2 pin4`；`option_2=GPIO2 J2 pin19`；`direction=module-to-host` |
| GPIO 与控制信号 | NSS GPIO 选择 | `source=U2 NSS pin19`；`net=NSS`；`switch=SW1 pins13-16`；`options=GPIO15 pin23; GPIO12 pin21; GPIO5 pin20; GPIO0 pin24`；`direction=host-to-module` |
| GPIO 与控制信号 | IRQ GPIO 选择 | `source=U2 DIO1 pin13`；`net=IRQ`；`switch=SW2 pins4-6`；`options=GPIO35 pin2; GPIO34 pin26; GPIO26 pin10`；`direction=module-to-host` |
| 复位 | 无线模组复位 | `target=U2 NRST pin15`；`net=RST`；`host_selection=SW1 GPIO25/GPIO13`；`pullup=not shown`；`pulldown=not shown`；`rc=not shown` |
| 接口 | M5Stack_BUS 已用网络 | `ground=pins1/3/5`；`spi=pin7 GPIO23 MOSI; pin9 GPIO19 MISO; pin11 GPIO18 SCK`；`irq=pin2 GPIO35; pin26 GPIO34; pin10 GPIO26`；`reset=pin8 GPIO25; pin22 GPIO13`；`busy=pin4 GPIO36; pin19 GPIO2`；`nss=pin23 GPIO15; pin21 GPIO12; pin20 GPIO5; pin24 GPIO0`；`power=pin28 +5V`；`hpwr=pins25/27/29 tied HPWR`；`battery=pin30 BAT not connected` |
| 接口 | 未使用的 RXEN/TXEN/DIO2 | `unused=RXEN pin6; TXEN pin7; DIO2 pin8`；`host_route=none shown` |
| 保护电路 | 接口保护器件 | `esd_tvs=not shown`；`rf_matching=not shown`；`spi_series=R1 33R on SCK only`；`control_series=not shown` |
| 核心器件 | SX1262 内部芯片 | `schematic_module=E22-900M22S`；`document_chip=SX1262`；`chip_reference=not shown` |
| 射频 | 频段与射频性能 | `document_band=850-930MHz`；`document_power=+22dBm`；`document_sensitivity=-147dBm`；`document_distance=4km at 125KHz`；`document_bitrate=300kbps`；`schematic_parameters=not shown` |
| 射频 | 外置 SMA 天线 | `document_connector=SMA`；`document_antenna=5dBi 195 x 13mm`；`schematic_rf_pin=U2 ANT pin21`；`connector_reference=null`；`matching=not shown` |
| 电源 | 休眠、待机与收发电流 | `document_sleep=5V@26.31uA`；`document_standby=5V@529.34uA`；`document_rx=5V@2.75mA or 8.62mA`；`document_tx=5V@11.08mA or 79.52mA`；`schematic_measurement=not shown` |

## 待确认事项

- `component.internal-radio-chip`：产品正文称 E22-900M22S 基于 SX1262，但原理图只把 U2 作为完整模组并标 E22-900M22S，没有单独显示 SX1262 位号。（证据：图 4bf982015f09 / 第 1 页 / U2 E22-900M22S module block）
- `rf.frequency-performance`：产品正文列出 850-930 MHz、+22 dBm、-147 dBm、4 km 与最高 300 kbps，但这些频段和性能数值未印在原理图。（证据：图 4bf982015f09 / 第 1 页 / U2 block lacks RF performance table）
- `rf.external-antenna`：产品正文称默认外置 SMA 天线，原理图仅显示 U2 ANT pin21 的短引出线，没有 SMA 连接器位号、匹配网络或天线规格。（证据：图 4bf982015f09 / 第 1 页 / U2 pin21 ANT without downstream connector）
- `power.consumption`：产品正文给出多组 5 V 休眠、待机、接收与发送电流，但原理图没有测试条件、电流测量点或带宽/功率配置。（证据：图 4bf982015f09 / 第 1 页 / +5V/U1/U2 power path lacks current annotations）
- `review.internal-radio-chip`：请用 E22-900M22S BOM 或模组规格确认内部射频芯片为 SX1262。；原因：原理图只显示完整模组，没有展开内部芯片。
- `review.frequency-performance`：请用已确认模组版本的数据手册和测试配置复核频段、功率、灵敏度、距离与比特率。；原因：这些参数未印在原理图。
- `review.external-antenna`：请用 PCB、BOM 和装配资料确认 SMA 连接器、匹配网络及随附天线规格。；原因：原理图在 ANT pin21 后没有画出连接器。
- `review.power-consumption`：请按明确频宽、发射功率、供电和固件模式复测休眠、待机、接收与发送电流。；原因：原理图没有电流值或测试条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `4bf982015f09ceac8bbd0816d8e5051e9b5731bab5bb5f779baf719160637a9a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/639/SCH_Module_LoRa_SX1262_V1.0_sch_01.png` |

---

源文档：`zh_CN/module/Module-LoRa868_V1.2.md`

源文档 SHA-256：`a94517d83b2cc68d608473962bade871c392fcbe241ef478e531e8e10d8b8b5a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
