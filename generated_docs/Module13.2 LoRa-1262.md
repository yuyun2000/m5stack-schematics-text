# Module13.2 LoRa-1262 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 LoRa-1262 |
| SKU | M149 |
| 产品 ID | `module13-2-lora-1262-b5bb939be918` |
| 源文档 | `zh_CN/module/Module13.2_LoRa-1262.md` |

## 概述

Module13.2 LoRa-1262 以 M1 Stamp LoRa-1262 为射频核心，M5Stack_BUS 提供 SPI、I2C、可选 GPIO 以及 BUS_3V3、BUS_5V、HPWR 和 VBAT 电源网络。HPWR 经 SY8303AIC 降压与 CH213K 串联电源级形成 BUS_5V，再由受 PY_IO5_PWR_EN 控制的 ME6211C33M5G-N 生成 VCC_3V3。U6 IO 扩展器通过 I2C 控制 LoRa 复位、SW、关断命名网络、本地 3.3 V 使能和可选 NeoPixel 电路，SW2 选择四档地址。SPI 信号通过 2N7002DW 双 MOS 通道跨接 BUS_3V3 与 VCC_3V3 域，SW1、SW3 分别为 BUSY/NSS 和 IRQ 选择 M5-Bus GPIO，射频端由 JP1 经可配置匹配位接入 M1 ANT。

## 检索关键词

`Module13.2 LoRa-1262`、`M149`、`Stamp LoRa-1262`、`SY8303AIC`、`CH213K`、`ME6211C33M5G-N`、`2N7002DW`、`M5Stack_BUS`、`SPI`、`I2C`、`BUS_3V3`、`BUS_5V`、`VCC_3V3`、`HPWR`、`VBAT`、`MOSI`、`MISO`、`SCK`、`ISO_MOSI`、`ISO_MISO`、`ISO_SCK`、`NSS`、`BUSY`、`IRQ`、`ADD_SEL`、`0x71`、`0x72`、`0x73`、`0x74`、`PY_IO2_LORA_RST`、`PY_IO3_BYPASS`、`PY_IO5_PWR_EN`、`PY_IO14_NEOPIXEL`、`JP1`、`SW1`、`SW2`、`SW3`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| P1 | 未标注 | HPWR 电源输入连接器，正端经 FU1 接入 HPWR，回路接 GND | 图 8d22c9d8533c / 第 1 页 / 网格 A1，P1 与 FU1/HPWR/GND |
| FU1 | 0805L050/30AR | P1 与 HPWR 之间的串联保险器件 | 图 8d22c9d8533c / 第 1 页 / 网格 A1，FU1 标注 0805L050/30AR |
| D1 | SMBJ30 | HPWR 到 GND 的并联瞬态抑制器件 | 图 8d22c9d8533c / 第 1 页 / 网格 A1-A2，D1 标注 SMBJ30，跨接 HPWR 与 GND |
| U1 | SY8303AIC | 以 HPWR 为输入的开关降压控制器 | 图 8d22c9d8533c / 第 1 页 / 网格 A2，U1 SY8303AIC，VIN/EN/LX/FB/BS/FS 引脚网络 |
| L1 | 10uH | U1 降压级的串联储能电感 | 图 8d22c9d8533c / 第 1 页 / 网格 A2-A3，L1 标注 10UH，连接 U1 LX 与输出节点 |
| U4 | CH213K | U1 降压输出与 BUS_5V 之间的串联电源器件 | 图 8d22c9d8533c / 第 1 页 / 网格 A3，U4 CH213K，IN+、VOUT 与 GND 引脚 |
| U7 | ME6211C33M5G-N | 由 BUS_5V 生成 VCC_3V3 的使能型 LDO | 图 8d22c9d8533c / 第 1 页 / 网格 B2-B3，U7 ME6211C33M5G-N，IN/EN/OUT/GND |
| U6 | IO_EXP | 连接 SDA/SCL、ADD_SEL 和多路板级控制信号的 I2C IO 扩展器 | 图 8d22c9d8533c / 第 1 页 / 网格 B1-B2，U6 符号值 IO_EXP 及 I2C/IO1-IO14 引脚 |
| J1 | M5Stack_BUS | 30 针 M5Stack 总线连接器，承载电源、SPI、I2C 和候选 GPIO | 图 8d22c9d8533c / 第 1 页 / 网格 C1-C2，J1 M5Stack_BUS 引脚 1-30 |
| JP2 | 未标注 | U6 的五针供电、SCLK、SWD 和 RST 调试连接器 | 图 8d22c9d8533c / 第 1 页 / 网格 B3，JP2 五针排针，BUS_3V3/SCLK/SWD/RST/GND |
| SW1 | SW DIP-8 | 为 BUSY 与 NSS 选择 M5-Bus GPIO 的八位拨码开关 | 图 8d22c9d8533c / 第 1 页 / 网格 B4-C5，SW1 SW DIP-8，端子 1-16 与 BUSY/NSS |
| SW2 | 未标注 | 通过 A、B 两路电阻支路改变 ADD_SEL 的两位地址选择开关 | 图 8d22c9d8533c / 第 1 页 / 网格 D2-D3，SW2、A/B、ADD_SEL 与地址表 |
| SW3 | 未标注 | 为 IRQ 选择三个 M5-Bus GPIO 之一的三位拨码开关 | 图 8d22c9d8533c / 第 1 页 / 网格 C4-C5，SW3 端子 1-6 与 GPIO35/GPIO34/GPIO26/IRQ |
| Q2A/Q2B | 2N7002DW | GPIO0 与 ISO_G0 之间的双 MOS 信号通道 | 图 8d22c9d8533c / 第 1 页 / 网格 B4-B5，Q2A/Q2B 2N7002DW，GPIO0/ISO_G0 |
| Q4A/Q4B | 2N7002DW | MISO 与 ISO_MISO 之间的双 MOS 信号通道 | 图 8d22c9d8533c / 第 1 页 / 网格 A4-A5，Q4A/Q4B 2N7002DW，MISO/ISO_MISO |
| Q5A/Q5B | 2N7002DW | MOSI 与 ISO_MOSI 之间的双 MOS 信号通道 | 图 8d22c9d8533c / 第 1 页 / 网格 B4-B5，Q5A/Q5B 2N7002DW，MOSI/ISO_MOSI |
| Q6A/Q6B | 2N7002DW | SCK 与 ISO_SCK 之间的双 MOS 信号通道 | 图 8d22c9d8533c / 第 1 页 / 网格 B4-B5，Q6A/Q6B 2N7002DW，SCK/ISO_SCK |
| M1 | Stamp LoRa-1262 | SPI 接口 LoRa 射频模组，带 ANT、NRST、BUSY、IRQ 和 SW 引脚 | 图 8d22c9d8533c / 第 1 页 / 网格 B7-B8，M1 Stamp LoRa-1262 引脚 1-13 |
| JP1 | 未标注 | 连接 RF 网络且外壳端接地的射频连接器 | 图 8d22c9d8533c / 第 1 页 / 网格 B5-B6，JP1 信号端 RF、接地端与 LB2 |
| LB2 | 0R(TBD) | JP1 与 M1 ANT 之间 RF 路径上的串联可配置器件 | 图 8d22c9d8533c / 第 1 页 / 网格 B6，LB2 标注 0R(TBD)，两侧均为 RF 网络 |
| Q3 | 未标注 | 由 PY_IO1_LED_EN 控制的可选 NeoPixel 电源通路器件 | 图 8d22c9d8533c / 第 1 页 / 网格 C5-C6，Q3 位于 VCC_3V3 与 D2-D4 VDD 总线之间 |
| D2/D3/D4 | 未标注 | 标注 NC 的三个串接 NeoPixel 兼容灯位 | 图 8d22c9d8533c / 第 1 页 / 网格 C6-D7，D2/D3/D4 的 DIN/VDD/DOUT/GND 引脚与 NC 标记 |
| P2 | 未标注 | 通过 Q1/Q7 接入 VBAT 与 GND 的两线连接器 | 图 8d22c9d8533c / 第 1 页 / 网格 D1-D2，P2 与 Q1/Q7、VBAT、GND |
| Q1 | CJ2301 | P2 到 VBAT 正向网络中的串联 MOS 器件 | 图 8d22c9d8533c / 第 1 页 / 网格 D1-D2，Q1 CJ2301，P2/VBAT 通路 |
| Q7 | CJ2302 | P2 回路与 GND 之间的 MOS 器件 | 图 8d22c9d8533c / 第 1 页 / 网格 D1-D2，Q7 CJ2302，P2/GND 通路 |
| TP1/TP3/TP4 | 未标注 | NSS、IRQ 和 BUSY 网络的测试点 | 图 8d22c9d8533c / 第 1 页 / 网格 C4-C5，TP1=NSS、TP3=IRQ、TP4=BUSY |

## 系统结构

### 模块总体结构

J1 M5Stack_BUS 连接 HPWR、BUS_5V、BUS_3V3、VBAT、SPI、I2C 和候选 GPIO；板上电源级产生 BUS_5V 与 VCC_3V3，U6 管理控制信号，M1 Stamp LoRa-1262 完成射频功能。

- 参数与网络：`bus_connector=J1 M5Stack_BUS`；`io_expander=U6`；`radio_module=M1 Stamp LoRa-1262`；`power_rails=HPWR, BUS_5V, BUS_3V3, VBAT, VCC_3V3`
- 证据：图 8d22c9d8533c / 第 1 页 / 全页，J1、P1/U1/U4/U7、U6、M1 功能分区

## 电源

### HPWR 降压级

U1 SY8303AIC 的 VIN pin 5 接 HPWR，EN pin 8 经 R2 100K 接 HPWR，LX pin 6 经 L1 10uH 到输出节点；C1 100nF 接在 BS pin 7 与 LX 节点之间。

- 参数与网络：`controller=U1 SY8303AIC`；`input=VIN pin 5 to HPWR`；`enable_bias=EN pin 8 through R2 100K to HPWR`；`inductor=L1 10uH`；`bootstrap_capacitor=C1 100nF between BS pin 7 and LX node`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 A2-A3，U1 VIN/EN/BS/LX、R2、C1 与 L1

### BUS_5V 输出

U1/L1 输出节点经 U4 CH213K 的 IN+ 到 VOUT 串联通路送至 BUS_5V，C12 22uF 从 BUS_5V 接地。

- 参数与网络：`series_device=U4 CH213K`；`input_pin=IN+ pin 3`；`output_pin=VOUT pin 2`；`output_net=BUS_5V`；`output_capacitor=C12 22uF`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 A3，U4 CH213K 与 C12/BUS_5V

### VCC_3V3 生成

BUS_5V 经 LB1 120R@100MHz 接入 U7 IN，U7 ME6211C33M5G-N 的 OUT 形成 VCC_3V3；C4、C9 与 C10 均标注 1uF。

- 参数与网络：`input_net=BUS_5V`；`filter=LB1 120R@100MHz`；`regulator=U7 ME6211C33M5G-N`；`output_net=VCC_3V3`；`capacitors=C4 1uF, C9 1uF, C10 1uF`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B1-B3，BUS_5V、LB1、U7 与 VCC_3V3

### VCC_3V3 去耦

VCC_3V3 在 M1 邻近位置并联 E1、C8、C26 到 GND，形成该本地电源域的去耦组。

- 参数与网络：`rail=VCC_3V3`；`capacitors=E1, C8, C26`；`connection=VCC_3V3 to GND`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B7，VCC_3V3 下方 E1/C8/C26 去耦组

### M1 供电

M1 3V3 pin 5 接 VCC_3V3，GND pins 1、11、13 接 GND。

- 参数与网络：`supply=M1 pin 5 VCC_3V3`；`ground=M1 pins 1, 11, 13 GND`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B7-B8，M1 pin 5 3V3 与 pins 1/11/13 GND

### 可选 NeoPixel 电源控制

Q3 串接在 VCC_3V3 与 D2-D4 VDD 总线之间，控制端连接 PY_IO1_LED_EN；R13 是该控制节点到 VCC_3V3 的 NC 预留位。

- 参数与网络：`input_rail=VCC_3V3`；`switch=Q3`；`control=PY_IO1_LED_EN`；`optional_bias=R13 NC`；`load=D2/D3/D4 VDD`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 C5-C6，VCC_3V3、Q3、R13、PY_IO1_LED_EN 与灯 VDD 总线

## 接口

### J1 电源引脚

J1 pin 12 接 BUS_3V3，pin 28 接 BUS_5V，pin 30 接 VBAT，pins 25/27/29 接 HPWR，pins 1/3/5 接 GND。

- 参数与网络：`BUS_3V3=J1 pin 12`；`BUS_5V=J1 pin 28`；`VBAT=J1 pin 30`；`HPWR=J1 pins 25, 27, 29`；`GND=J1 pins 1, 3, 5`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 C1-C2，J1 M5Stack_BUS 电源与接地引脚

### J1 I2C 引脚

J1 GPIO21 pin 17 接 SDA，J1 GPIO22 pin 18 接 SCL，并直接连接 U6 的 I2C 数据与时钟网络。

- 参数与网络：`sda=J1 pin 17 GPIO21`；`scl=J1 pin 18 GPIO22`；`device=U6`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B1-B2 与 C1-C2，U6 SDA/SCL 及 J1 pins 17/18

### J1 SPI 引脚

J1 GPIO23 pin 7 接 MOSI，GPIO19 pin 9 接 MISO，GPIO18 pin 11 经 R5 33R 接 SCK，GPIO0 pin 24 连接 GPIO0 域间通道。

- 参数与网络：`mosi=J1 pin 7 GPIO23`；`miso=J1 pin 9 GPIO19`；`sck=J1 pin 11 GPIO18 through R5 33R`；`gpio0=J1 pin 24 GPIO0`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 C1-C2，J1 MOSI/MISO/SCK/GPIO0 引脚与 R5

### P2 与 VBAT/GND

P2 的两条电气通路分别经 Q1 CJ2301 接到 VBAT、经 Q7 CJ2302 接到 GND；VBAT 同时连接 J1 pin 30。

- 参数与网络：`high_side_path=P2 through Q1 CJ2301 to VBAT`；`return_path=P2 through Q7 CJ2302 to GND`；`bus_connection=VBAT to J1 pin 30`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 D1-D2 与 C1-C2，P2/Q1/Q7/VBAT/GND 及 J1 pin 30

## 总线

### U6 I2C 接口

U6 I2C_SCL pin 9 接 SCL，I2C_SDA pin 8 接 SDA，VCC pin 6 接 BUS_3V3，VSS pins 4/21 接 GND。

- 参数与网络：`scl=U6 pin 9 SCL`；`sda=U6 pin 8 SDA`；`supply=U6 pin 6 BUS_3V3`；`ground=U6 pins 4 and 21 GND`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B1-B2，U6 左侧 VCC/VSS/I2C_SCL/I2C_SDA

### SDA/SCL 上拉

R9 2.2K/1% 将 SDA 上拉到 BUS_3V3，R14 2.2K/1% 将 SCL 上拉到 BUS_3V3。

- 参数与网络：`sda_pullup=R9 2.2K/1% to BUS_3V3`；`scl_pullup=R14 2.2K/1% to BUS_3V3`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 D2-D3，R9/R14 与 SDA/SCL/BUS_3V3

### SPI 与 GPIO0 域间通道

MISO/ISO_MISO、MOSI/ISO_MOSI、SCK/ISO_SCK 和 GPIO0/ISO_G0 四组网络分别通过 Q4A/Q4B、Q5B/Q5A、Q6A/Q6B 和 Q2B/Q2A 的 2N7002DW 双 MOS 通道连接。

- 参数与网络：`miso_channel=Q4A/Q4B: MISO to ISO_MISO`；`mosi_channel=Q5B/Q5A: MOSI to ISO_MOSI`；`sck_channel=Q6A/Q6B: SCK to ISO_SCK`；`gpio0_channel=Q2B/Q2A: GPIO0 to ISO_G0`；`bus_gate_domain=BUS_3V3`；`local_gate_domain=VCC_3V3`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 A4-B5，Q2/Q4/Q5/Q6 四组 2N7002DW 通道

### M1 SPI 连接

M1 NSS pin 9 接 NSS，MISO pin 8 接 ISO_MISO，MOSI pin 7 接 ISO_MOSI，CLK pin 6 接 ISO_SCK。

- 参数与网络：`nss=M1 pin 9 NSS`；`miso=M1 pin 8 ISO_MISO`；`mosi=M1 pin 7 ISO_MOSI`；`clock=M1 pin 6 ISO_SCK`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B7-B8，M1 pins 6-9 与 ISO_SCK/ISO_MOSI/ISO_MISO/NSS

## 总线地址

### U6 地址选择

原理图地址表给出 SW2 组合 A=0/B=0 对应 0x74，A=1/B=0 对应 0x73，A=0/B=1 对应 0x72，A=1/B=1 对应 0x71。

- 参数与网络：`A0_B0=0x74`；`A1_B0=0x73`；`A0_B1=0x72`；`A1_B1=0x71`；`select_net=ADD_SEL`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 D2-D3，SW2 下方 A/B/ADDR 地址表

## GPIO 与控制信号

### U7 使能

U7 EN pin 3 由 PY_IO5_PWR_EN 驱动；R11 10K/1% 将该网络下拉到 GND，R21 是连接 BUS_3V3 的 NC 选装位。

- 参数与网络：`enable_net=PY_IO5_PWR_EN`；`enable_pin=U7 pin 3`；`pulldown=R11 10K/1%`；`optional_pullup=R21 NC to BUS_3V3`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B1-B2，U7 EN 与 U6 下方 R21/R11 网络

### U6 控制信号映射

U6 IO1、IO2、IO3、IO4、IO5 与 IO14/NEOPIXEL 分别连接 PY_IO1_LED_EN、PY_IO2_LORA_RST、PY_IO3_BYPASS、PY_IO4_SHUT DOWN、PY_IO5_PWR_EN 与 PY_IO14_NEOPIXEL。

- 参数与网络：`IO1_pin7=PY_IO1_LED_EN`；`IO2_pin11=PY_IO2_LORA_RST`；`IO3_pin14=PY_IO3_BYPASS`；`IO4_pin16=PY_IO4_SHUT DOWN`；`IO5_pin17=PY_IO5_PWR_EN`；`IO14_pin3=PY_IO14_NEOPIXEL`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B2，U6 右侧 IO1-IO5 与 IO14/NEOPIXEL 网络

### M1 控制与状态引脚

M1 SW pin 10 接 PY_IO3_BYPASS，NRST pin 2 接 PY_IO2_LORA_RST，BUSY pin 3 接 BUSY，IRQ pin 4 接 IRQ。

- 参数与网络：`sw=M1 pin 10 PY_IO3_BYPASS`；`nrst=M1 pin 2 PY_IO2_LORA_RST`；`busy=M1 pin 3 BUSY`；`irq=M1 pin 4 IRQ`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B7-B8，M1 SW/NRST/BUSY/IRQ 引脚

### BUSY GPIO 选择

SW1 的四个 BUSY 选择位将 GPIO25、GPIO13、GPIO36 或 GPIO2 分别接到公共 BUSY 网络。

- 参数与网络：`switch_pairs=8-9 GPIO25, 7-10 GPIO13, 6-11 GPIO36, 5-12 GPIO2`；`bus_pins=GPIO25 J1 pin 8, GPIO13 J1 pin 22, GPIO36 J1 pin 4, GPIO2 J1 pin 19`；`target=M1 BUSY pin 3`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B4-C5，SW1 上半部 GPIO25/GPIO13/GPIO36/GPIO2 到 BUSY

### NSS GPIO 选择

SW1 的四个 NSS 选择位将 GPIO15、GPIO12、GPIO5 或 ISO_G0 分别接到公共 NSS 网络；ISO_G0 经 Q2A/Q2B 连接 M5-Bus GPIO0。

- 参数与网络：`switch_pairs=4-13 GPIO15, 3-14 GPIO12, 2-15 GPIO5, 1-16 ISO_G0`；`bus_pins=GPIO15 J1 pin 23, GPIO12 J1 pin 21, GPIO5 J1 pin 20, GPIO0 J1 pin 24 via Q2`；`target=M1 NSS pin 9`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B4-C5，SW1 下半部 GPIO15/GPIO12/GPIO5/ISO_G0 到 NSS

### IRQ GPIO 选择

SW3 的三个位将 GPIO35、GPIO34 或 GPIO26 分别接到公共 IRQ 网络。

- 参数与网络：`switch_pairs=1-6 GPIO35, 2-5 GPIO34, 3-4 GPIO26`；`bus_pins=GPIO35 J1 pin 2, GPIO34 J1 pin 26, GPIO26 J1 pin 10`；`target=M1 IRQ pin 4`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 C4-C5，SW3 GPIO35/GPIO34/GPIO26 到 IRQ

## 时钟

### M1 SPI 时钟

M5-Bus 的 SCK 经 Q6A/Q6B 域间通道成为 ISO_SCK，并连接 M1 CLK pin 6。

- 参数与网络：`source_net=SCK`；`bridge=Q6A/Q6B 2N7002DW`；`destination_net=ISO_SCK`；`destination_pin=M1 CLK pin 6`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B4-B5 与 B7-B8，SCK/Q6/ISO_SCK/M1 CLK

## 复位

### U6 复位

U6 NRST pin 1 接 RST，R7 将 RST 上拉到 BUS_3V3，C25 将 RST 接到 GND。

- 参数与网络：`reset_net=RST`；`reset_pin=U6 pin 1 NRST`；`pullup=R7 to BUS_3V3`；`capacitor=C25 to GND`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B1，U6 NRST、RST、R7 与 C25

### M1 复位

U6 IO2 pin 11 输出 PY_IO2_LORA_RST，并直接连接 M1 NRST pin 2。

- 参数与网络：`controller=U6 IO2 pin 11`；`net=PY_IO2_LORA_RST`；`target=M1 NRST pin 2`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B2 与 B8，U6 IO2/PY_IO2_LORA_RST/M1 NRST

## 保护电路

### HPWR 输入保护

P1 的电源端先串联 FU1 0805L050/30AR 后形成 HPWR；D1 SMBJ30 与多颗输入电容从 HPWR 并接到 GND。

- 参数与网络：`connector=P1`；`series_device=FU1 0805L050/30AR`；`shunt_device=D1 SMBJ30`；`input_net=HPWR`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 A1-A2，P1、FU1、D1、HPWR 输入网络

## 关键网络

### 域间通道上拉配置

ISO_MISO、ISO_MOSI、ISO_SCK 与 ISO_G0 分别通过 R16、R18、R20、R4 的 10K/1% 电阻上拉到 VCC_3V3；BUS_3V3 侧 R12、R17、R19、R3 均标注 NC。

- 参数与网络：`local_pullups=R16 ISO_MISO, R18 ISO_MOSI, R20 ISO_SCK, R4 ISO_G0; all 10K/1% to VCC_3V3`；`bus_optional_pulls=R12 MISO, R17 MOSI, R19 SCK, R3 GPIO0; all NC to BUS_3V3`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 A4-B5，R3/R4/R12/R16/R17/R18/R19/R20

### NSS/BUSY/IRQ 上拉配置

NSS 通过 R24 10K/1% 上拉到 VCC_3V3；BUSY 的 R23 与 IRQ 的 R25 均标注 NC，作为到 VCC_3V3 的未装上拉位。

- 参数与网络：`nss_pullup=R24 10K/1% to VCC_3V3`；`busy_optional_pullup=R23 NC to VCC_3V3`；`irq_optional_pullup=R25 NC to VCC_3V3`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B5-C5，R23/R24/R25 与 BUSY/NSS/IRQ/VCC_3V3

## 射频

### M1 射频路径

JP1 信号端经 RF 网络、LB2 0R(TBD) 和第二段 RF 网络连接 M1 ANT pin 12；JP1 接地端与 M1 GND pins 11/13 接 GND。

- 参数与网络：`connector=JP1`；`series_element=LB2 0R(TBD)`；`radio_pin=M1 ANT pin 12`；`net=RF`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B5-B8，JP1、RF、LB2 与 M1 ANT/GND

### 射频匹配预留

C16 与 C17 分别从 LB2 两侧 RF 节点接 GND，二者均标注 NC；LB2 标注 0R(TBD)。

- 参数与网络：`connector_side_shunt=C16 NC`；`module_side_shunt=C17 NC`；`series=LB2 0R(TBD)`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B5-B7，C16/LB2/C17 的 RF π 型预留位置

## 调试与烧录

### JP2 调试接口

JP2 pins 1-5 依次连接 BUS_3V3、SCLK、SWD、RST 与 GND；U6 IO13 pin 15 接 SCLK，IO12 pin 5 接 SWD。

- 参数与网络：`pin1=BUS_3V3`；`pin2=SCLK`；`pin3=SWD`；`pin4=RST`；`pin5=GND`；`u6_sclk=IO13 pin 15`；`u6_swd=IO12 pin 5`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 B2-B3，U6 SWD/SCLK 与 JP2 pins 1-5

### LoRa 控制测试点

TP1 接 NSS，TP3 接 IRQ，TP4 接 BUSY。

- 参数与网络：`TP1=NSS`；`TP3=IRQ`；`TP4=BUSY`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 C4-C5，NSS/IRQ/BUSY 三个 Test point

## 模拟电路

### ADD_SEL 电阻网络

ADD_SEL 由 R10 10K/1% 接 BUS_3V3、R15 24K/1% 接 GND；SW2 可将 A 支路 R22 24K/1% 或 B 支路 R27 9.1K/1% 接入 ADD_SEL。

- 参数与网络：`pullup=R10 10K/1% to BUS_3V3`；`base_pulldown=R15 24K/1% to GND`；`A_branch=R22 24K/1% to GND via SW2`；`B_branch=R27 9.1K/1% to GND via SW2`；`destination=U6 ADD_SEL pin 19`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 C2-D3，ADD_SEL、R10/R15、SW2、R22/R27

## 其他事实

### 可选 NeoPixel 链

D2、D3、D4 均标注 NC；PY_IO14_NEOPIXEL 接 D2 DIN，D2 DOUT 接 D3 DIN，D3 DOUT 接 D4 DIN，三个器件共用受控 VDD 与 GND。

- 参数与网络：`population=D2 NC, D3 NC, D4 NC`；`data_input=PY_IO14_NEOPIXEL to D2 DIN`；`chain=D2 DOUT to D3 DIN; D3 DOUT to D4 DIN`；`ground=D2/D3/D4 GND`
- 证据：图 8d22c9d8533c / 第 1 页 / 网格 C5-D7，PY_IO14_NEOPIXEL 与 D2/D3/D4 数据链

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 模块总体结构 | `bus_connector=J1 M5Stack_BUS`；`io_expander=U6`；`radio_module=M1 Stamp LoRa-1262`；`power_rails=HPWR, BUS_5V, BUS_3V3, VBAT, VCC_3V3` |
| 保护电路 | HPWR 输入保护 | `connector=P1`；`series_device=FU1 0805L050/30AR`；`shunt_device=D1 SMBJ30`；`input_net=HPWR` |
| 电源 | HPWR 降压级 | `controller=U1 SY8303AIC`；`input=VIN pin 5 to HPWR`；`enable_bias=EN pin 8 through R2 100K to HPWR`；`inductor=L1 10uH`；`bootstrap_capacitor=C1 100nF between BS pin 7 and LX node` |
| 电源 | BUS_5V 输出 | `series_device=U4 CH213K`；`input_pin=IN+ pin 3`；`output_pin=VOUT pin 2`；`output_net=BUS_5V`；`output_capacitor=C12 22uF` |
| 电源 | VCC_3V3 生成 | `input_net=BUS_5V`；`filter=LB1 120R@100MHz`；`regulator=U7 ME6211C33M5G-N`；`output_net=VCC_3V3`；`capacitors=C4 1uF, C9 1uF, C10 1uF` |
| GPIO 与控制信号 | U7 使能 | `enable_net=PY_IO5_PWR_EN`；`enable_pin=U7 pin 3`；`pulldown=R11 10K/1%`；`optional_pullup=R21 NC to BUS_3V3` |
| 接口 | J1 电源引脚 | `BUS_3V3=J1 pin 12`；`BUS_5V=J1 pin 28`；`VBAT=J1 pin 30`；`HPWR=J1 pins 25, 27, 29`；`GND=J1 pins 1, 3, 5` |
| 电源 | VCC_3V3 去耦 | `rail=VCC_3V3`；`capacitors=E1, C8, C26`；`connection=VCC_3V3 to GND` |
| 总线 | U6 I2C 接口 | `scl=U6 pin 9 SCL`；`sda=U6 pin 8 SDA`；`supply=U6 pin 6 BUS_3V3`；`ground=U6 pins 4 and 21 GND` |
| 总线 | SDA/SCL 上拉 | `sda_pullup=R9 2.2K/1% to BUS_3V3`；`scl_pullup=R14 2.2K/1% to BUS_3V3` |
| 接口 | J1 I2C 引脚 | `sda=J1 pin 17 GPIO21`；`scl=J1 pin 18 GPIO22`；`device=U6` |
| 复位 | U6 复位 | `reset_net=RST`；`reset_pin=U6 pin 1 NRST`；`pullup=R7 to BUS_3V3`；`capacitor=C25 to GND` |
| GPIO 与控制信号 | U6 控制信号映射 | `IO1_pin7=PY_IO1_LED_EN`；`IO2_pin11=PY_IO2_LORA_RST`；`IO3_pin14=PY_IO3_BYPASS`；`IO4_pin16=PY_IO4_SHUT DOWN`；`IO5_pin17=PY_IO5_PWR_EN`；`IO14_pin3=PY_IO14_NEOPIXEL` |
| 调试与烧录 | JP2 调试接口 | `pin1=BUS_3V3`；`pin2=SCLK`；`pin3=SWD`；`pin4=RST`；`pin5=GND`；`u6_sclk=IO13 pin 15`；`u6_swd=IO12 pin 5` |
| 总线地址 | U6 地址选择 | `A0_B0=0x74`；`A1_B0=0x73`；`A0_B1=0x72`；`A1_B1=0x71`；`select_net=ADD_SEL` |
| 模拟电路 | ADD_SEL 电阻网络 | `pullup=R10 10K/1% to BUS_3V3`；`base_pulldown=R15 24K/1% to GND`；`A_branch=R22 24K/1% to GND via SW2`；`B_branch=R27 9.1K/1% to GND via SW2`；`destination=U6 ADD_SEL pin 19` |
| 接口 | J1 SPI 引脚 | `mosi=J1 pin 7 GPIO23`；`miso=J1 pin 9 GPIO19`；`sck=J1 pin 11 GPIO18 through R5 33R`；`gpio0=J1 pin 24 GPIO0` |
| 总线 | SPI 与 GPIO0 域间通道 | `miso_channel=Q4A/Q4B: MISO to ISO_MISO`；`mosi_channel=Q5B/Q5A: MOSI to ISO_MOSI`；`sck_channel=Q6A/Q6B: SCK to ISO_SCK`；`gpio0_channel=Q2B/Q2A: GPIO0 to ISO_G0`；`bus_gate_domain=BUS_3V3`；`local_gate_domain=VCC_3V3` |
| 关键网络 | 域间通道上拉配置 | `local_pullups=R16 ISO_MISO, R18 ISO_MOSI, R20 ISO_SCK, R4 ISO_G0; all 10K/1% to VCC_3V3`；`bus_optional_pulls=R12 MISO, R17 MOSI, R19 SCK, R3 GPIO0; all NC to BUS_3V3` |
| 总线 | M1 SPI 连接 | `nss=M1 pin 9 NSS`；`miso=M1 pin 8 ISO_MISO`；`mosi=M1 pin 7 ISO_MOSI`；`clock=M1 pin 6 ISO_SCK` |
| 时钟 | M1 SPI 时钟 | `source_net=SCK`；`bridge=Q6A/Q6B 2N7002DW`；`destination_net=ISO_SCK`；`destination_pin=M1 CLK pin 6` |
| 复位 | M1 复位 | `controller=U6 IO2 pin 11`；`net=PY_IO2_LORA_RST`；`target=M1 NRST pin 2` |
| GPIO 与控制信号 | M1 控制与状态引脚 | `sw=M1 pin 10 PY_IO3_BYPASS`；`nrst=M1 pin 2 PY_IO2_LORA_RST`；`busy=M1 pin 3 BUSY`；`irq=M1 pin 4 IRQ` |
| 电源 | M1 供电 | `supply=M1 pin 5 VCC_3V3`；`ground=M1 pins 1, 11, 13 GND` |
| GPIO 与控制信号 | BUSY GPIO 选择 | `switch_pairs=8-9 GPIO25, 7-10 GPIO13, 6-11 GPIO36, 5-12 GPIO2`；`bus_pins=GPIO25 J1 pin 8, GPIO13 J1 pin 22, GPIO36 J1 pin 4, GPIO2 J1 pin 19`；`target=M1 BUSY pin 3` |
| GPIO 与控制信号 | NSS GPIO 选择 | `switch_pairs=4-13 GPIO15, 3-14 GPIO12, 2-15 GPIO5, 1-16 ISO_G0`；`bus_pins=GPIO15 J1 pin 23, GPIO12 J1 pin 21, GPIO5 J1 pin 20, GPIO0 J1 pin 24 via Q2`；`target=M1 NSS pin 9` |
| GPIO 与控制信号 | IRQ GPIO 选择 | `switch_pairs=1-6 GPIO35, 2-5 GPIO34, 3-4 GPIO26`；`bus_pins=GPIO35 J1 pin 2, GPIO34 J1 pin 26, GPIO26 J1 pin 10`；`target=M1 IRQ pin 4` |
| 关键网络 | NSS/BUSY/IRQ 上拉配置 | `nss_pullup=R24 10K/1% to VCC_3V3`；`busy_optional_pullup=R23 NC to VCC_3V3`；`irq_optional_pullup=R25 NC to VCC_3V3` |
| 调试与烧录 | LoRa 控制测试点 | `TP1=NSS`；`TP3=IRQ`；`TP4=BUSY` |
| 射频 | M1 射频路径 | `connector=JP1`；`series_element=LB2 0R(TBD)`；`radio_pin=M1 ANT pin 12`；`net=RF` |
| 射频 | 射频匹配预留 | `connector_side_shunt=C16 NC`；`module_side_shunt=C17 NC`；`series=LB2 0R(TBD)` |
| 其他事实 | 可选 NeoPixel 链 | `population=D2 NC, D3 NC, D4 NC`；`data_input=PY_IO14_NEOPIXEL to D2 DIN`；`chain=D2 DOUT to D3 DIN; D3 DOUT to D4 DIN`；`ground=D2/D3/D4 GND` |
| 电源 | 可选 NeoPixel 电源控制 | `input_rail=VCC_3V3`；`switch=Q3`；`control=PY_IO1_LED_EN`；`optional_bias=R13 NC`；`load=D2/D3/D4 VDD` |
| 接口 | P2 与 VBAT/GND | `high_side_path=P2 through Q1 CJ2301 to VBAT`；`return_path=P2 through Q7 CJ2302 to GND`；`bus_connection=VBAT to J1 pin 30` |
| 核心器件 | U6 精确型号 | `reference=U6`；`shown_value=IO_EXP`；`missing=manufacturer and exact part number` |
| 核心器件 | JP1 精确连接器类型 | `reference=JP1`；`shown_net=RF`；`missing=mechanical interface standard and part number` |
| 核心器件 | P2 精确接口定义 | `reference=P2`；`visible_nets=VBAT and GND through Q1/Q7`；`missing=connector series, pin names, external purpose` |
| 核心器件 | Q3 精确型号 | `reference=Q3`；`visible_control=PY_IO1_LED_EN`；`visible_path=VCC_3V3 to D2/D3/D4 VDD`；`missing=exact part number` |
| GPIO 与控制信号 | PY_IO4_SHUT DOWN 去向 | `source=U6 IO4 pin 16`；`net=PY_IO4_SHUT DOWN`；`missing=destination on this schematic page` |
| 核心器件 | D2-D4 精确灯珠型号 | `references=D2, D3, D4`；`population=NC`；`missing=exact LED part number` |

## 待确认事项

- `component.u6-exact-part`：U6 在该页只标注 IO_EXP，无法仅凭此原理图确认制造商和精确料号。（证据：图 8d22c9d8533c / 第 1 页 / 网格 B1-B2，U6 器件值仅显示 IO_EXP）
- `component.jp1-connector-type`：JP1 明确连接 RF 与 GND，但该页未给出其机械接口标准和精确料号。（证据：图 8d22c9d8533c / 第 1 页 / 网格 B5-B6，JP1 仅有位号、RF 与 GND 连接）
- `component.p2-connector-purpose`：P2 的 VBAT/GND 电气去向可见，但该页未标注连接器系列、针脚名称或外部用途。（证据：图 8d22c9d8533c / 第 1 页 / 网格 D1-D2，P2/Q1/Q7 电路未附接口名称）
- `component.q3-exact-part`：Q3 的开关位置与控制网络可见，但该页未标注 Q3 的精确器件型号。（证据：图 8d22c9d8533c / 第 1 页 / 网格 C5-C6，Q3 符号附近无器件值）
- `gpio.shutdown-net-destination`：U6 IO4 pin 16 输出 PY_IO4_SHUT DOWN，但该页未显示此命名网络的接收器或后续连接。（证据：图 8d22c9d8533c / 第 1 页 / 网格 B2，U6 IO4 的 PY_IO4_SHUT DOWN 网络标签）
- `component.optional-led-part`：D2、D3、D4 显示 DIN/VDD/DOUT/GND 引脚并标注 NC，但该页未提供灯珠型号。（证据：图 8d22c9d8533c / 第 1 页 / 网格 C6-D7，D2/D3/D4 均标注 NC，未显示型号）
- `review.u6-exact-part`：U6 IO_EXP 的制造商和精确料号是什么？；原因：当前原理图只给出功能名 IO_EXP，不能从页内证据唯一确定器件。
- `review.jp1-connector-type`：JP1 的机械接口标准和精确料号是什么？；原因：原理图只确认 RF/GND 电气连接，没有机械连接器标注。
- `review.p2-connector-purpose`：P2 的连接器系列、针脚定义和对外用途是什么？；原因：原理图显示其通过 Q1/Q7 接入 VBAT/GND，但没有接口名称或机械信息。
- `review.q3-exact-part`：Q3 的精确型号和额定参数是什么？；原因：页内只显示位号与开关连接，没有器件值。
- `review.shutdown-net-destination`：PY_IO4_SHUT DOWN 在本版硬件中是否连接到页外器件或预留测试点？；原因：当前唯一原理图页只显示 U6 端网络标签，没有接收端。
- `review.optional-led-part`：D2-D4 预留位设计对应的精确 NeoPixel 兼容灯珠型号是什么？；原因：三个器件均标注 NC，原理图未给出型号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8d22c9d8533c5258b190f80480375a502d76cf82120db86516cdf9648cb2b3a5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1277/SCH_Module13.2_LoRa1262_V1.0_2026_09_02_17_15_18_page_01.png` |

---

源文档：`zh_CN/module/Module13.2_LoRa-1262.md`

源文档 SHA-256：`9ddae3166e9a09ab5c196f777054071172bf45d1c2741193e98b399390b0c21a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
