# Module13.2 4In8Out 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 4In8Out |
| SKU | M122 |
| 产品 ID | `module13-2-4in8out-af00e1ccbdea` |
| 源文档 | `zh_CN/module/4in8out.md` |

## 概述

Module13.2 4In8Out 以 U2 STM32F030F4P6 作为 I2C IO 协处理器，采集 4 路共地下拉式接点输入，并控制 8 路 AO3400A 低侧 MOS 输出。每路输出具有串联保险丝和 1N4007W 至 +VIN 的续流二极管，负载公共正端由 +VIN 提供。P6 接收标注为 DC 9-24V 的输入，U1 MP1584EN 降压生成 +5V 并送至 M5-Bus；逻辑 3.3 V 由 M5-Bus 提供。

## 检索关键词

`Module13.2 4In8Out`、`M122`、`STM32F030F4P6`、`MP1584EN`、`AO3400A`、`1N4007W`、`SS54`、`I2C`、`0x45`、`SDA`、`SCL`、`M5Stack_BUS`、`DC 9-24V`、`+VIN`、`+5V`、`+3.3V`、`IN1`、`IN2`、`IN3`、`IN4`、`PIN1`、`PIN2`、`PIN3`、`PIN4`、`OUT1`、`OUT2`、`OUT3`、`OUT4`、`OUT5`、`OUT6`、`OUT7`、`OUT8`、`POUT1`、`POUT8`、`SWDIO`、`SWCLK`、`BOOT0`、`low-side MOSFET`、`dry contact`、`5V/3A`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | STM32F030F4P6 | I2C IO 协处理器，读取 4 路输入并控制 8 路输出 | 图 ecc34e3694e0 / 第 1 页 / C2-C4，U2 STM32F030F4P6 与 IN1-IN4、OUT1-OUT8、SDA/SCL、SWD、BOOT0 |
| U1 | MP1584EN | +VIN 至 +5V 的降压转换器 | 图 ecc34e3694e0 / 第 1 页 / A1-A3，U1 MP1584EN、L1 10uH、D1 SS54、R1/R2 反馈与 +5V |
| Q1-Q8 | AO3400A | OUT1-OUT8 八路低侧 N 沟道 MOSFET 开关 | 图 ecc34e3694e0 / 第 1 页 / C4-C8，Q1-Q8 AO3400A，源极接 GND、漏极接 OUT1-OUT8 |
| D4-D11 | 1N4007W | 八路输出从 POUTx 到 +VIN 的续流钳位二极管 | 图 ecc34e3694e0 / 第 1 页 / C4-C8，D4-D11 1N4007W 跨接 POUT1-POUT8 与 +VIN |
| F2-F9 | Fuse | 每路 POUTx 到 OUTx 的串联保险丝 | 图 ecc34e3694e0 / 第 1 页 / C4-C8，F2-F9 均标 Fuse，串联 POUT1-POUT8 与 OUT1-OUT8 |
| RP1/RP2 | 4.7KΩ (472) ±5% | 四路输入串联限流与 3.3 V 上拉电阻阵列 | 图 ecc34e3694e0 / 第 1 页 / A6-A7，IN1-IN4-RP1-PIN1-PIN4-RP2-+3.3V |
| RP3/RP4 | 4.7KΩ (472) ±5% | 八路 MCU 输出至 MOSFET 栅极的串联电阻阵列 | 图 ecc34e3694e0 / 第 1 页 / C1-C3，RP3 对应 OUT5-OUT8，RP4 对应 OUT1-OUT4 |
| J1 | M5Stack_BUS | M5-Bus 主机、I2C 和电源接口 | 图 ecc34e3694e0 / 第 1 页 / A7-B8，J1 M5Stack_BUS pins 1-30，SDA/SCL/+3.3V/+5V/+VIN/HPWR |
| P1-P4 | Header 2 | PIN1-PIN4 与公共 GND 的四路输入端子 | 图 ecc34e3694e0 / 第 1 页 / A5-A6，P1-P4 Header 2，PIN1-PIN4 与公共 GND |
| P6 | Header 2 | 标注 POWER IN DC 9-24V 的 +VIN/GND 电源输入 | 图 ecc34e3694e0 / 第 1 页 / A5，P6 Header 2，POWER IN DC 9-24V、+VIN、GND |
| P7-P14 | Header 2 | 八路 +VIN/POUT1-POUT8 负载输出端子 | 图 ecc34e3694e0 / 第 1 页 / A5-B7，P7-P14 Header 2 与 +VIN/POUT1-POUT8 |
| P5 | SWD_5p | STM32 的 SWCLK、SWDIO、NRST 调试接口 | 图 ecc34e3694e0 / 第 1 页 / A7，P5 SWD_5p：3.3V/SWCLK/SWDIO/NRST/GND |
| S1 | SW-SPDT | BOOT0 运行/下载模式选择开关 | 图 ecc34e3694e0 / 第 1 页 / C1-C3，S1 SW-SPDT、BOOT0、GND 与 R5 10KΩ 上拉 |
| F1/D2/D3 | 1.5A/24V / SS54 / LESD3Z5.0CMT1G | 输入保险与 +VIN、+5V 电源钳位保护 | 图 ecc34e3694e0 / 第 1 页 / A1-A4，F1 1.5A/24V、D2 SS54 于 Vin、D3 LESD3Z5.0CMT1G 于 +5V |

## 系统结构

### 4 输入 8 输出架构

U2 STM32F030F4P6 通过 I2C 连接 M5-Bus，读取 IN1-IN4，并通过 OUT1-OUT8 控制八颗 AO3400A 低侧 MOSFET；U1 MP1584EN 将 +VIN 降压为 +5V。

- 参数与网络：`mcu=U2 STM32F030F4P6`；`inputs=4`；`outputs=8`；`output_switches=Q1-Q8 AO3400A`；`power_converter=U1 MP1584EN`；`host_bus=I2C`
- 证据：图 ecc34e3694e0 / 第 1 页 / 整页电源、接口、MCU、输入与八路输出分区

## 电源

### 9-24 V 输入路径

P6 标注 POWER IN DC 9-24V，正端连接 +VIN；+VIN 经 F1 1.5A/24V 后成为 Vin，D2 SS54、C2 10 µF 与 C3 100 nF 接于 Vin 输入保护/滤波节点。

- 参数与网络：`connector=P6`；`range_printed=DC 9-24V`；`rail=+VIN`；`fuse=F1 1.5A/24V`；`clamp=D2 SS54`；`input_caps=C2 10uF; C3 100nF`
- 证据：图 ecc34e3694e0 / 第 1 页 / A1-A2 与 A5，P6/+VIN/F1/D2/C2/C3

### MP1584 5 V 降压

U1 MP1584EN 与 L1 10 µH、D1 SS54 构成降压级，R1 51 kΩ/R2 10 kΩ 为 FB 分压，C4/C5/C6 各 22 µF 滤波，输出网络标为 +5V。

- 参数与网络：`converter=U1 MP1584EN`；`inductor=L1 10uH`；`catch_diode=D1 SS54`；`feedback=R1 51KΩ; R2 10KΩ`；`output_caps=C4/C5/C6 22uF`；`output=+5V`
- 证据：图 ecc34e3694e0 / 第 1 页 / A2-A4，U1/L1/D1/R1/R2/C4-C6/+5V

## 接口

### 四路无源接点输入

P1-P4 每路端子由 PINx 与公共 GND 构成；PINx 经 RP2 4.7 kΩ 上拉至 +3.3V，并经 RP1 4.7 kΩ 串联到 MCU INx。触点将 PINx 接地时形成低电平输入。

- 参数与网络：`terminals=P1-P4`；`channels=PIN1-PIN4`；`common=GND`；`pullups=RP2 4.7KΩ each to +3.3V`；`series=RP1 4.7KΩ each`；`active_level=low when contact closes`
- 证据：图 ecc34e3694e0 / 第 1 页 / A5-A7，P1-P4、RP1/RP2、PIN1-PIN4、IN1-IN4

### 八路低侧输出

P7-P14 每路端子提供公共 +VIN 与 POUTx；POUTx 经 F2-F9 连接 OUTx/MOSFET 漏极，Q1-Q8 源极接 GND，构成共正极低侧开关。

- 参数与网络：`terminals=P7-P14`；`positive=+VIN`；`switched_nodes=POUT1-POUT8`；`fuses=F2-F9`；`mosfets=Q1-Q8 AO3400A`；`topology=low-side common-positive`
- 证据：图 ecc34e3694e0 / 第 1 页 / A5-B7 端子与 C4-C8 MOSFET 输出级

### M5-Bus 使用网络

J1 将 SDA/SCL 接到 pins 17/18，将 +3.3V 接 pin12、+5V 接 pin28，并在底部引出 +VIN/HPWR 网络；多个 GND 引脚连接公共地。

- 参数与网络：`reference=J1`；`sda=pin17`；`scl=pin18`；`3v3=pin12`；`5v=pin28`；`high_power=+VIN/HPWR on lower bus pins`；`ground=multiple GND pins`
- 证据：图 ecc34e3694e0 / 第 1 页 / A7-B8，J1 M5Stack_BUS 外部网络标签

## 总线

### M5-Bus I2C

U2 PA10 pin18 为 SDA，PA9 pin17 为 SCL；SDA 与 SCL 分别连接 J1 M5-Bus pins 17 与 18。

- 参数与网络：`controller=external M5Stack host`；`device=U2 STM32F030F4P6`；`sda=U2 PA10 pin18 / J1 pin17`；`scl=U2 PA9 pin17 / J1 pin18`；`direction=bidirectional`；`logic_rail=+3.3V`
- 证据：图 ecc34e3694e0 / 第 1 页 / U2 PA10/PA9 SDA/SCL 与 J1 pins 17/18

## GPIO 与控制信号

### 四路输入 MCU 映射

IN1、IN2、IN3、IN4 分别连接 U2 PB1 pin14、PA7 pin13、PA6 pin12、PA5 pin11。

- 参数与网络：`IN1=U2 PB1 pin14`；`IN2=U2 PA7 pin13`；`IN3=U2 PA6 pin12`；`IN4=U2 PA5 pin11`；`direction=inputs to U2`
- 证据：图 ecc34e3694e0 / 第 1 页 / C3-C4，U2 right-side IN1-IN4

### 八路输出 MCU 映射

OUT1-OUT4 经 RP4 分别连接 U2 PA4 pin10、PA3 pin9、PA2 pin8、PA1 pin7；OUT5 接 PA0 pin6，OUT6 接 PF1 pin3，OUT7 接 PF0 pin2，OUT8 经 RP3 复用 SWDIO/PA13 pin19。

- 参数与网络：`OUT1=PA4 pin10`；`OUT2=PA3 pin9`；`OUT3=PA2 pin8`；`OUT4=PA1 pin7`；`OUT5=PA0 pin6`；`OUT6=PF1 pin3`；`OUT7=PF0 pin2`；`OUT8=PA13 pin19 SWDIO`；`series_resistors=RP3/RP4 4.7KΩ`
- 证据：图 ecc34e3694e0 / 第 1 页 / C1-C4，RP3/RP4 至 U2 left pins，OUT8 标注 SWDIO 网络

### BOOT0 开关

U2 BOOT0 pin1 由 R5 10 kΩ 上拉到 +3.3V；S1 SW-SPDT 可将 BOOT0 连接到 GND，另一档释放后由 R5 拉高。

- 参数与网络：`pin=U2 pin1 BOOT0`；`pullup=R5 10KΩ to +3.3V`；`switch=S1 SW-SPDT`；`low=connected to GND`；`high=released and pulled up`
- 证据：图 ecc34e3694e0 / 第 1 页 / C1-C3，S1/BOOT0/R5/+3.3V/GND

## 复位

### MCU 复位网络

U2 NRST pin4 由 R6 10 kΩ 上拉至 +3.3V，并由 C8 100 nF 对地；NRST 同时引到 P5。

- 参数与网络：`pin=U2 pin4 NRST`；`pullup=R6 10KΩ`；`capacitor=C8 100nF`；`debug=P5 NRST`
- 证据：图 ecc34e3694e0 / 第 1 页 / C1-C3，R6/C8/NRST/U2/P5

## 保护电路

### 输出续流保护

D4-D11 均为 1N4007W，分别从 POUT1-POUT8 接至 +VIN，为八路感性负载提供并联钳位路径。

- 参数与网络：`diodes=D4-D11 1N4007W`；`channels=POUT1-POUT8`；`clamp_rail=+VIN`
- 证据：图 ecc34e3694e0 / 第 1 页 / C4-C8，D4-D11 与 POUT1-POUT8/+VIN

## 调试与烧录

### SWD 调试与 OUT8 复用

P5 提供 3.3V、SWCLK、SWDIO、NRST 与 GND；SWCLK 接 U2 PA14 pin20，SWDIO 接 PA13 pin19，而 OUT8 也连接 SWDIO 网络。

- 参数与网络：`connector=P5 SWD_5p`；`swclk=U2 PA14 pin20`；`swdio=U2 PA13 pin19`；`reset=NRST`；`shared_function=OUT8 shares SWDIO`
- 证据：图 ecc34e3694e0 / 第 1 页 / A7 P5 与 C1-C4 U2/RP3 OUT8-SWDIO

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 4 输入 8 输出架构 | `mcu=U2 STM32F030F4P6`；`inputs=4`；`outputs=8`；`output_switches=Q1-Q8 AO3400A`；`power_converter=U1 MP1584EN`；`host_bus=I2C` |
| 总线 | M5-Bus I2C | `controller=external M5Stack host`；`device=U2 STM32F030F4P6`；`sda=U2 PA10 pin18 / J1 pin17`；`scl=U2 PA9 pin17 / J1 pin18`；`direction=bidirectional`；`logic_rail=+3.3V` |
| GPIO 与控制信号 | 四路输入 MCU 映射 | `IN1=U2 PB1 pin14`；`IN2=U2 PA7 pin13`；`IN3=U2 PA6 pin12`；`IN4=U2 PA5 pin11`；`direction=inputs to U2` |
| 接口 | 四路无源接点输入 | `terminals=P1-P4`；`channels=PIN1-PIN4`；`common=GND`；`pullups=RP2 4.7KΩ each to +3.3V`；`series=RP1 4.7KΩ each`；`active_level=low when contact closes` |
| GPIO 与控制信号 | 八路输出 MCU 映射 | `OUT1=PA4 pin10`；`OUT2=PA3 pin9`；`OUT3=PA2 pin8`；`OUT4=PA1 pin7`；`OUT5=PA0 pin6`；`OUT6=PF1 pin3`；`OUT7=PF0 pin2`；`OUT8=PA13 pin19 SWDIO`；`series_resistors=RP3/RP4 4.7KΩ` |
| 接口 | 八路低侧输出 | `terminals=P7-P14`；`positive=+VIN`；`switched_nodes=POUT1-POUT8`；`fuses=F2-F9`；`mosfets=Q1-Q8 AO3400A`；`topology=low-side common-positive` |
| 保护电路 | 输出续流保护 | `diodes=D4-D11 1N4007W`；`channels=POUT1-POUT8`；`clamp_rail=+VIN` |
| 电源 | 9-24 V 输入路径 | `connector=P6`；`range_printed=DC 9-24V`；`rail=+VIN`；`fuse=F1 1.5A/24V`；`clamp=D2 SS54`；`input_caps=C2 10uF; C3 100nF` |
| 电源 | MP1584 5 V 降压 | `converter=U1 MP1584EN`；`inductor=L1 10uH`；`catch_diode=D1 SS54`；`feedback=R1 51KΩ; R2 10KΩ`；`output_caps=C4/C5/C6 22uF`；`output=+5V` |
| 接口 | M5-Bus 使用网络 | `reference=J1`；`sda=pin17`；`scl=pin18`；`3v3=pin12`；`5v=pin28`；`high_power=+VIN/HPWR on lower bus pins`；`ground=multiple GND pins` |
| 调试与烧录 | SWD 调试与 OUT8 复用 | `connector=P5 SWD_5p`；`swclk=U2 PA14 pin20`；`swdio=U2 PA13 pin19`；`reset=NRST`；`shared_function=OUT8 shares SWDIO` |
| GPIO 与控制信号 | BOOT0 开关 | `pin=U2 pin1 BOOT0`；`pullup=R5 10KΩ to +3.3V`；`switch=S1 SW-SPDT`；`low=connected to GND`；`high=released and pulled up` |
| 复位 | MCU 复位网络 | `pin=U2 pin4 NRST`；`pullup=R6 10KΩ`；`capacitor=C8 100nF`；`debug=P5 NRST` |
| 总线地址 | 模块 I2C 地址 | `claimed_default=0x45`；`claimed_changeable=true`；`schematic_address=not printed`；`address_straps=none shown` |
| 电源 | 5 V 输出能力 | `schematic_output=+5V`；`claimed_current=3A`；`rating_printed=false` |
| 保护电路 | 输出电流与保险丝额定值 | `claimed_per_channel=<=1A`；`claimed_total=<=8A`；`fuse_values=not printed` |
| 保护电路 | 无源输入限制 | `claimed_type=dry contact only`；`claimed_max_external=5V`；`schematic_pullup=3.3V through RP2 4.7KΩ`；`schematic_series=RP1 4.7KΩ` |

## 待确认事项

- `address.i2c`：产品正文给出默认地址 0x45 且可修改，但原理图未印出地址值、地址配置脚或寄存器。（证据：图 ecc34e3694e0 / 第 1 页 / U2 SDA/SCL 电路未标地址）
- `power.output-rating`：原理图确认输出网络为 +5V，但未直接标注产品正文所称 5V/3A 连续输出能力。（证据：图 ecc34e3694e0 / 第 1 页 / MP1584EN +5V 输出级未标 3A）
- `protection.channel-ratings`：产品正文称每路不超过 1 A、总电流不超过 8 A，但原理图中的 F2-F9 仅标 Fuse，未给出各保险丝额定值或总电流条件。（证据：图 ecc34e3694e0 / 第 1 页 / F2-F9 均仅标 Fuse）
- `protection.input-limit`：产品正文警告输入仅限无源触点且不得接入大于 5 V 的有源信号；原理图显示 3.3 V 上拉和 4.7 kΩ 串联电阻，但未标绝对输入电压限制。（证据：图 ecc34e3694e0 / 第 1 页 / P1-P4/RP1/RP2 输入网络未印绝对额定值）
- `review.i2c-address`：请用 STM32 固件或通信协议确认默认 7-bit I2C 地址 0x45 及修改机制。；原因：地址由固件决定，原理图未直接标注。
- `review.5v-rating`：请用 MP1584 热设计、BOM 和实测确认 5V/3A 输出能力。；原因：原理图只标 +5V，未标连续电流能力。
- `review.channel-ratings`：请用 F2-F9 BOM、MOSFET/端子/PCB 热设计确认每路 1 A 和总计 8 A 限值。；原因：原理图未给出通道保险丝额定值。
- `review.input-limit`：请用 MCU 绝对额定值和产品测试规范确认仅限无源触点及外部 5 V 上限。；原因：原理图没有印出输入绝对电压限制。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ecc34e3694e07d781516a6d46d990dcbc329d81285025bf133e267c247dd7a06` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/549/Sch_4IN8OUT_sch_01.png` |

---

源文档：`zh_CN/module/4in8out.md`

源文档 SHA-256：`d25a86920d2a4e757f8af9b4450e4bafa93990e3d307c427cd48fdc7ca77fce0`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
