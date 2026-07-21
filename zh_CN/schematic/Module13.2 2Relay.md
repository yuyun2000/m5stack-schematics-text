# Module13.2 2Relay 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 2Relay |
| SKU | M124 |
| 产品 ID | `module13-2-2relay-c332f9f68be2` |
| 源文档 | `zh_CN/module/2Relay.md` |

## 概述

Module13.2 2Relay 以 U1 STM32F030F4P6 为控制器，通过 J1 M5Stack_BUS 的 SDA/SCL 与主机通信。PA1、PA2 分别经 1 kΩ 电阻驱动两只 SS8050 低侧晶体管，控制 K1、K2 两组 5 V 继电器线圈，D1、D2 跨接在线圈回路上。P4、P5 分别引出两路 SPST 触点，控制电路由 M5-Bus 的 +3.3V 和 +5V 电源轨供电，并提供 P1 五针 SWD 调试接口。

## 检索关键词

`Module13.2 2Relay`、`M124`、`STM32F030F4P6`、`I2C`、`0x26`、`SDA`、`SCL`、`GPIO22`、`GPIO21`、`PA1`、`PA2`、`SS8050`、`1N4148WS T4`、`K1`、`K2`、`Relay-SPST`、`OUT1`、`OUT2`、`M5Stack_BUS`、`+3.3V`、`+5V`、`SWDIO`、`SWCLK`、`NRST`、`BOOT0`、`P4`、`P5`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | I2C 通信、双继电器控制和 SWD 调试的主控制器 | 图 957ed87dcd0e / 第 1 页 / 网格 B2 中央 U1 方框，器件值 STM32F030F4P6，周围标注 PA1、PA2、SDA、SCL、SWDIO、SWCLK、NRST、BOOT0 |
| K1,K2 | Relay-SPST | 两路单刀单掷继电器，线圈由 +5V 低侧驱动，触点分别引至 P4、P5 | 图 957ed87dcd0e / 第 1 页 / 网格 D2-D3 的 K1、K2，器件值均为 Relay-SPST，线圈与触点符号分离绘制 |
| VT1,VT2 | SS8050 | K1、K2 继电器线圈的两路低侧驱动晶体管 | 图 957ed87dcd0e / 第 1 页 / 网格 C2-C3 的 VT1、VT2，器件标注 SS8050 Y1，发射极接 GND，集电极接线圈返回路径 |
| D1,D2 | 1N4148WS T4 | 两路继电器线圈的反向钳位二极管 | 图 957ed87dcd0e / 第 1 页 / 网格 C2-C3 的 D1、D2，均标注 1N4148WS T4，跨接在 +5V 与 VT1/VT2 集电极节点之间 |
| R2,R3 | 1KΩ(1001)±1% | PA1、PA2 到 VT1、VT2 基极的串联电阻 | 图 957ed87dcd0e / 第 1 页 / 网格 C1-C3 的 R2、R3，值均为 1KΩ(1001)±1%，分别连接 PA1-VT1 与 PA2-VT2 |
| J1 | M5Stack_BUS | 30 针 M5-Bus 主机、电源和 I2C 接口 | 图 957ed87dcd0e / 第 1 页 / 网格 C4 的 J1 M5Stack_BUS，pin 1-30 标注 GND、GPIO、HPWR、+3.3V、+5V、BATTERY |
| P1 | SWD_5p | 五针 SWD 调试与复位接口 | 图 957ed87dcd0e / 第 1 页 / 网格 B4 的 P1 SWD_5p，pin 1-5 标注 VCC、SWCLK、SWDIO、RST、GND |
| P2,P3 | Header 3X2 | 控制板驱动回路与继电器板线圈回路之间的六针配对连接器 | 图 957ed87dcd0e / 第 1 页 / 网格 C2 与 D2 的 P2、P3 Header 3X2，二者之间以虚线表示配对关系，连接 +5V 和两路线圈返回节点 |
| P4,P5 | Header 2 | K1、K2 两路 SPST 继电器触点输出端子 | 图 957ed87dcd0e / 第 1 页 / 网格 D1 与 D3 的 P4、P5 Header 2，各自两针分别连接对应继电器的两个 SPST 触点 |
| R1,C1 | 10KΩ; 100nF | U1 NRST 的上拉和对地电容网络 | 图 957ed87dcd0e / 第 1 页 / 网格 B1 的 R1 10KΩ 从 NRST 到 +3.3V，C1 100nF 从 NRST 到 GND |
| C2 | 10uF | +3.3V 电源到 GND 的去耦/储能电容 | 图 957ed87dcd0e / 第 1 页 / 网格 B3 的 C2，值 10uF，连接 +3.3V 与 GND |

## 系统结构

### Module13.2 2Relay 系统架构

U1 STM32F030F4P6 通过 J1 的 SDA/SCL 与主机连接，以 PA1、PA2 控制 VT1、VT2 两路低侧驱动；两路驱动经 P2/P3 连接 K1、K2 的 +5V 线圈，P4、P5 引出两个 SPST 触点。

- 参数与网络：`controller=U1 STM32F030F4P6`；`host_connector=J1 M5Stack_BUS`；`relay_channels=K1,K2`；`drivers=VT1,VT2 SS8050`；`control_nets=PA1,PA2`；`contact_connectors=P4,P5`；`relay_supply=+5V`
- 证据：图 957ed87dcd0e / 第 1 页 / 完整单页网格 B1-D4：U1、J1、双晶体管驱动、P2/P3、K1/K2 与 P4/P5 功能区

## 核心器件

### U1 STM32F030F4P6 主要引脚

U1 PA1/pin 7 连接 PA1，PA2/pin 8 连接 PA2，PA9/pin 17 连接 SCL，PA10/pin 18 连接 SDA，PA13/pin 19 连接 SWDIO，PA14/pin 20 连接 SWCLK，NRST/pin 4 连接 NRST。

- 参数与网络：`relay1_control=PA1/pin 7`；`relay2_control=PA2/pin 8`；`scl=PA9/pin 17`；`sda=PA10/pin 18`；`swdio=PA13/pin 19`；`swclk=PA14/pin 20`；`reset=NRST/pin 4`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 B2 的 U1 左右两侧引脚号与 PA1、PA2、SCL、SDA、SWDIO、SWCLK、NRST 网络标注

## 电源

### 控制与继电器电源轨

J1 pin 12 提供 +3.3V，连接 U1 VDDA/pin 5、VDD/pin 16、NRST 上拉 R1 和 C2；J1 pin 28 提供 +5V，连接继电器线圈公共端及 D1、D2。

- 参数与网络：`logic_input=J1 pin 12/+3.3V`；`mcu_supply_pins=U1 VDDA pin 5,VDD pin 16`；`relay_input=J1 pin 28/+5V`；`relay_loads=K1,K2 coils`；`flyback_common=D1,D2 to +5V`；`ground_pins=J1 pin 1,3,5; U1 VSS pin 15`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 B1-B3 的 U1 +3.3V 供电、网格 C2-C3 的 +5V 线圈供电和网格 C4 的 J1 +3.3V/+5V/GND 针脚

### +3.3V 电源去耦

C2 为 10uF，连接在 +3.3V 与 GND 之间；本页未绘出 DC-DC、LDO、充电、电池或电源监测电路。

- 参数与网络：`capacitor=C2`；`capacitance=10uF`；`rail=+3.3V`；`return=GND`；`converter_visible=false`；`charger_visible=false`；`battery_path_visible=false`；`power_monitor_visible=false`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 B3 的 C2 10uF 与完整单页电源器件区域

## 接口

### P4、P5 继电器触点输出

P4 pin 1、pin 2 分别连接 K1 的两个 SPST 触点，P5 pin 1、pin 2 分别连接 K2 的两个 SPST 触点；原理图未把触点端子连接到控制侧电源或地。

- 参数与网络：`channel1=P4 pin 1,pin 2 <-> K1 SPST contacts`；`channel2=P5 pin 1,pin 2 <-> K2 SPST contacts`；`contact_side_control_rail_connection=false`；`contact_rating_visible=false`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 D1-D3 的 P4-K1 触点和 K2-P5 触点独立布线

### J1 M5Stack_BUS 已用针脚

J1 pin 1、3、5 连接 GND，pin 12 连接 +3.3V，pin 17 GPIO21 连接 SCL，pin 18 GPIO22 连接 SDA，pin 28 连接 +5V；其余针脚在本页无板内连线。

- 参数与网络：`reference=J1`；`used_pinout=1:GND,3:GND,5:GND,12:+3.3V,17:GPIO21/SCL,18:GPIO22/SDA,28:+5V`；`unused_pinout=2:GPIO35,4:GPIO36,6:EN,7:GPIO23,8:GPIO25,9:GPIO19,10:GPIO26,11:GPIO18,13:GPIO3,14:GPIO1,15:GPIO16,16:GPIO17,19:GPIO2,20:GPIO5,21:GPIO12,22:GPIO13,23:GPIO15,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,29:HPWR,30:BATTERY`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 C4 的 J1 M5Stack_BUS pin 1-30，外部蓝色网络仅出现在 GND、+3.3V、SCL、SDA、+5V 对应针脚

## 总线

### U1 与 J1 的 I2C 总线

U1 PA9/pin 17 的 SCL 连接 J1 pin 17 GPIO21，U1 PA10/pin 18 的 SDA 连接 J1 pin 18 GPIO22；本页未绘出 SDA/SCL 外部上拉电阻。

- 参数与网络：`controller=U1`；`scl_mcu_pin=PA9/pin 17`；`scl_bus_pin=J1 pin 17/GPIO21`；`sda_mcu_pin=PA10/pin 18`；`sda_bus_pin=J1 pin 18/GPIO22`；`pullups_visible=false`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 B2 的 U1 PA9/SCL、PA10/SDA 与网格 C4 的 J1 pin 17 SCL、pin 18 SDA

## GPIO 与控制信号

### 两路继电器 GPIO 控制

U1 PA1/pin 7 经 R2 1KΩ(1001)±1% 驱动 VT1 基极，U1 PA2/pin 8 经 R3 1KΩ(1001)±1% 驱动 VT2 基极；VT1、VT2 发射极均接 GND。

- 参数与网络：`channel1=U1 PA1/pin 7 -> R2 1KΩ -> VT1 base`；`channel2=U1 PA2/pin 8 -> R3 1KΩ -> VT2 base`；`transistors=VT1,VT2 SS8050`；`emitter_net=GND`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 C1-C3 的 PA1-R2-VT1 与 PA2-R3-VT2 两条驱动链

### U1 BOOT0 启动配置

U1 BOOT0/pin 1 在原理图中直接连接 GND。

- 参数与网络：`mcu_pin=U1 BOOT0/pin 1`；`net=GND`；`bias=direct connection`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 B2 的 U1 pin 1 BOOT0 左侧蓝色连线到 GND 符号

## 时钟

### U1 外部时钟可见性

U1 PF0/OSC_IN pin 2 与 PF1/OSC_OUT pin 3 在本页无外部连线，原理图未绘出晶体、谐振器或外部振荡器。

- 参数与网络：`osc_in=U1 PF0/OSC_IN pin 2 unconnected`；`osc_out=U1 PF1/OSC_OUT pin 3 unconnected`；`external_clock_component_visible=false`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 B2 的 U1 pin 2 PF0/OSC_IN、pin 3 PF1/OSC_OUT 无外部布线，完整单页无 Y/X 位号

## 复位

### U1 NRST 网络

U1 NRST/pin 4 连接 NRST；R1 10KΩ 将 NRST 上拉至 +3.3V，C1 100nF 将 NRST 连接至 GND，NRST 同时引至 P1 pin 4 RST。

- 参数与网络：`mcu_pin=U1 NRST/pin 4`；`net=NRST`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C1 100nF to GND`；`debug_pin=P1 pin 4/RST`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 B1-B2 的 R1/C1/NRST/U1 pin 4 与网格 B4 的 P1 RST

## 保护电路

### 继电器线圈反向钳位

D1、D2 均为 1N4148WS T4，分别跨接在 +5V 与 VT1、VT2 集电极节点之间，与两路线圈回路并联。

- 参数与网络：`channel1_diode=D1 1N4148WS T4`；`channel2_diode=D2 1N4148WS T4`；`common_rail=+5V`；`return_nodes=VT1 collector,VT2 collector`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 C2-C3 的 D1、D2 与 +5V、VT1/VT2 集电极连接

### M5-Bus 与触点端子保护可见性

除 D1、D2 线圈钳位外，本页未绘出 M5-Bus 或 P4/P5 触点端子的 TVS、ESD、保险丝或浪涌保护器件。

- 参数与网络：`relay_flyback_visible=true`；`bus_tvs_visible=false`；`bus_esd_visible=false`；`contact_fuse_visible=false`；`contact_surge_protection_visible=false`
- 证据：图 957ed87dcd0e / 第 1 页 / 完整单页网格 C2-D4 的 D1/D2、J1、P4/P5 及其全部外围器件

## 关键网络

### K1、K2 线圈回路

P2/P3 Header 3X2 在图中以虚线表示配对；pin 1 传递公共 +5V，pin 2 和 pin 6 分别传递 VT1、VT2 集电极的两路线圈低侧返回，P3 侧连接 K1、K2 线圈。

- 参数与网络：`connector_pair=P2,P3 Header 3X2`；`common_supply_pin=pin 1/+5V`；`channel1_return_pin=pin 2/VT1 collector`；`channel2_return_pin=pin 6/VT2 collector`；`unused_pins=3,4,5`；`coils=K1,K2`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 C2-D2 的 P2/P3 pin 1-6、虚线配对标记、+5V 与 VT1/VT2 集电极布线及 K1/K2 线圈

## 调试与烧录

### P1 SWD 调试接口

P1 pin 1 连接 VCC/+3.3V，pin 2 连接 SWCLK，pin 3 连接 SWDIO，pin 4 RST 连接 NRST，pin 5 连接 GND；SWCLK、SWDIO 分别连接 U1 PA14/pin 20、PA13/pin 19。

- 参数与网络：`connector=P1 SWD_5p`；`pinout=1:VCC/+3.3V,2:SWCLK,3:SWDIO,4:RST/NRST,5:GND`；`swclk_mcu_pin=U1 PA14/pin 20`；`swdio_mcu_pin=U1 PA13/pin 19`
- 证据：图 957ed87dcd0e / 第 1 页 / 网格 B2 的 U1 SWCLK/SWDIO/NRST 与网格 B4 的 P1 SWD_5p

## 其他事实

### 其他功能分区可见性

该单页原理图未绘出独立存储器、外部存储、音频器件、传感器、射频器件或模拟采样链路。

- 参数与网络：`storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`sensor_visible=false`；`rf_visible=false`；`analog_sampling_visible=false`；`schematic_pages_checked=1`
- 证据：图 957ed87dcd0e / 第 1 页 / 完整单页器件清单仅含 U1、双继电器、双晶体管驱动、接口、电阻、电容和二极管

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 2Relay 系统架构 | `controller=U1 STM32F030F4P6`；`host_connector=J1 M5Stack_BUS`；`relay_channels=K1,K2`；`drivers=VT1,VT2 SS8050`；`control_nets=PA1,PA2`；`contact_connectors=P4,P5`；`relay_supply=+5V` |
| 核心器件 | U1 STM32F030F4P6 主要引脚 | `relay1_control=PA1/pin 7`；`relay2_control=PA2/pin 8`；`scl=PA9/pin 17`；`sda=PA10/pin 18`；`swdio=PA13/pin 19`；`swclk=PA14/pin 20`；`reset=NRST/pin 4` |
| 总线 | U1 与 J1 的 I2C 总线 | `controller=U1`；`scl_mcu_pin=PA9/pin 17`；`scl_bus_pin=J1 pin 17/GPIO21`；`sda_mcu_pin=PA10/pin 18`；`sda_bus_pin=J1 pin 18/GPIO22`；`pullups_visible=false` |
| 总线地址 | I2C 从机地址 | `documented_address=0x26`；`schematic_address_visible=false` |
| GPIO 与控制信号 | 两路继电器 GPIO 控制 | `channel1=U1 PA1/pin 7 -> R2 1KΩ -> VT1 base`；`channel2=U1 PA2/pin 8 -> R3 1KΩ -> VT2 base`；`transistors=VT1,VT2 SS8050`；`emitter_net=GND` |
| 关键网络 | K1、K2 线圈回路 | `connector_pair=P2,P3 Header 3X2`；`common_supply_pin=pin 1/+5V`；`channel1_return_pin=pin 2/VT1 collector`；`channel2_return_pin=pin 6/VT2 collector`；`unused_pins=3,4,5`；`coils=K1,K2` |
| 保护电路 | 继电器线圈反向钳位 | `channel1_diode=D1 1N4148WS T4`；`channel2_diode=D2 1N4148WS T4`；`common_rail=+5V`；`return_nodes=VT1 collector,VT2 collector` |
| 接口 | P4、P5 继电器触点输出 | `channel1=P4 pin 1,pin 2 <-> K1 SPST contacts`；`channel2=P5 pin 1,pin 2 <-> K2 SPST contacts`；`contact_side_control_rail_connection=false`；`contact_rating_visible=false` |
| 接口 | J1 M5Stack_BUS 已用针脚 | `reference=J1`；`used_pinout=1:GND,3:GND,5:GND,12:+3.3V,17:GPIO21/SCL,18:GPIO22/SDA,28:+5V`；`unused_pinout=2:GPIO35,4:GPIO36,6:EN,7:GPIO23,8:GPIO25,9:GPIO19,10:GPIO26,11:GPIO18,13:GPIO3,14:GPIO1,15:GPIO16,16:GPIO17,19:GPIO2,20:GPIO5,21:GPIO12,22:GPIO13,23:GPIO15,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,29:HPWR,30:BATTERY` |
| 电源 | 控制与继电器电源轨 | `logic_input=J1 pin 12/+3.3V`；`mcu_supply_pins=U1 VDDA pin 5,VDD pin 16`；`relay_input=J1 pin 28/+5V`；`relay_loads=K1,K2 coils`；`flyback_common=D1,D2 to +5V`；`ground_pins=J1 pin 1,3,5; U1 VSS pin 15` |
| 电源 | +3.3V 电源去耦 | `capacitor=C2`；`capacitance=10uF`；`rail=+3.3V`；`return=GND`；`converter_visible=false`；`charger_visible=false`；`battery_path_visible=false`；`power_monitor_visible=false` |
| 复位 | U1 NRST 网络 | `mcu_pin=U1 NRST/pin 4`；`net=NRST`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C1 100nF to GND`；`debug_pin=P1 pin 4/RST` |
| GPIO 与控制信号 | U1 BOOT0 启动配置 | `mcu_pin=U1 BOOT0/pin 1`；`net=GND`；`bias=direct connection` |
| 调试与烧录 | P1 SWD 调试接口 | `connector=P1 SWD_5p`；`pinout=1:VCC/+3.3V,2:SWCLK,3:SWDIO,4:RST/NRST,5:GND`；`swclk_mcu_pin=U1 PA14/pin 20`；`swdio_mcu_pin=U1 PA13/pin 19` |
| 时钟 | U1 外部时钟可见性 | `osc_in=U1 PF0/OSC_IN pin 2 unconnected`；`osc_out=U1 PF1/OSC_OUT pin 3 unconnected`；`external_clock_component_visible=false` |
| 保护电路 | M5-Bus 与触点端子保护可见性 | `relay_flyback_visible=true`；`bus_tvs_visible=false`；`bus_esd_visible=false`；`contact_fuse_visible=false`；`contact_surge_protection_visible=false` |
| 其他事实 | 其他功能分区可见性 | `storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`sensor_visible=false`；`rf_visible=false`；`analog_sampling_visible=false`；`schematic_pages_checked=1` |

## 待确认事项

- `address.documented-i2c`：原理图未打印 I2C 从机地址；产品正文记载 0x26，但无法仅由本页电路图确认当前固件地址。（证据：图 957ed87dcd0e / 第 1 页 / 网格 B2-C4 的 U1 SDA/SCL 至 J1 连接区域，未见地址值或地址选择网络）
- `review.i2c-address`：当前 Module13.2 2Relay 固件的 I2C 从机地址是否确认为产品正文记载的 0x26？；原因：原理图只显示 SDA/SCL 物理连接，没有打印从机地址、地址选择网络或固件定义。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `957ed87dcd0e2163f36c5b33a1c32848e94dd9d686eb26cd4969b7b17c2cf5de` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/551/Sch_Module13.2_2Relay_sch_01.png` |

---

源文档：`zh_CN/module/2Relay.md`

源文档 SHA-256：`68075ce4fc1e93130a820b231cce0d76f4b08ab26fbb9db15bfc4f7bfbe5cc4d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
