# Unit Laser TX 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Laser TX |
| SKU | U066 |
| 产品 ID | `unit-laser-tx-9cc73b1c6bc0` |
| 源文档 | `zh_CN/unit/laser-tx.md` |

## 概述

Unit Laser TX 是由外部数字信号直接控制的激光发射单元：J1 pin2 MOSI 经 R1 1KΩ 驱动 Q1 AO3400A，Q1 作为低侧开关控制 VCC 至 D1 Laser 的电流通断。R2 51KΩ 将控制节点下拉，C1 100nF 跨接激光支路，C2 100nF 跨接 VCC 与 GND；J1 pin1 MISO 未接线。完整原理图没有本地主控、总线协议、稳压器或激光电流设定电路，正文所列 DIN/NC、5V 及光学/调制性能需结合 BOM、datasheet 或实测确认。

## 检索关键词

`Unit Laser TX`、`U066`、`Laser TX`、`D1 Laser`、`Q1 AO3400A`、`AO3400A`、`GROVE_IO`、`J1`、`MOSI`、`MISO`、`DIN`、`NC`、`VCC`、`GND`、`R1 1KΩ`、`R2 51KΩ`、`C1 100nF`、`C2 100nF`、`low-side switch`、`低侧开关`、`激光二极管`、`激光发射`、`PORT.B`、`5V`、`LASER.RX`、`gate pulldown`、`数字调制`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| D1 | Laser | 由 VCC 供电并经 Q1 低侧开关控制的激光发射器件 | 图 a2a1ef414145 / 第 1 页 / 第 1 页左上：D1 标注 Laser，连接 VCC 与 Q1 漏极节点 |
| Q1 | AO3400A | 控制 D1 Laser 回路的 N 沟道低侧 MOSFET 开关 | 图 a2a1ef414145 / 第 1 页 / 第 1 页左中：Q1 AO3400A，源极接 GND、漏极接 D1、栅极接 R1 |
| J1 | GROVE_IO | 四针外部供电与数字控制接口，标注 MISO、MOSI、VCC、GND | 图 a2a1ef414145 / 第 1 页 / 第 1 页右中：J1 GROVE_IO pin1-pin4 |
| R1,R2 | 1KΩ / 51KΩ | Q1 栅极串联电阻与控制节点下拉电阻 | 图 a2a1ef414145 / 第 1 页 / 第 1 页中央：J1 pin2-R1 1KΩ-Q1 gate，节点经 R2 51KΩ 接 GND |
| C1 | 100nF | 跨接 VCC 与 Q1 漏极节点、与 D1 Laser 并联的电容 | 图 a2a1ef414145 / 第 1 页 / 第 1 页左上：C1 100nF 与 D1 Laser 两端共节点 |
| C2 | 100nF | J1 附近 VCC 至 GND 的电源去耦电容 | 图 a2a1ef414145 / 第 1 页 / 第 1 页右侧：C2 100nF 跨接 VCC 与 GND |

## 系统结构

### Unit Laser TX 系统结构

J1 提供 VCC、GND 和 MOSI 控制输入；MOSI 经 R1 驱动 Q1 AO3400A，Q1 低侧开关控制 D1 Laser。完整单页没有本地主控、协处理器、存储器、通信收发器、电池、充电器或稳压器。

- 参数与网络：`controller=external via J1 pin2`；`emitter=D1 Laser`；`switch=Q1 AO3400A`；`control_path=J1 MOSI -> R1 -> Q1 gate`；`local_mcu=null`；`storage=null`；`transceiver=null`；`battery=null`；`regulator=null`
- 证据：图 a2a1ef414145 / 第 1 页 / 第 1 页完整原理图

## 核心器件

### Q1 AO3400A 低侧开关

Q1 AO3400A 的源极接 GND，漏极接 D1 Laser 下端与 C1 下端，栅极经 R1 接 MOSI 控制节点；Q1 导通时为激光支路提供到 GND 的回路。

- 参数与网络：`part=Q1 AO3400A`；`source=GND`；`drain=D1 lower/C1 lower`；`gate=R1 from MOSI`；`topology=N-channel low-side switch`
- 证据：图 a2a1ef414145 / 第 1 页 / 第 1 页左中 Q1 符号及源/漏/栅三条连接

## 电源

### 激光发射电流路径

D1 Laser 上端连接 VCC，下端连接 Q1 漏极；Q1 源极连接 GND，因此受控导通路径为 VCC -> D1 -> Q1 -> GND。原理图未在 D1 主电流路径中显示独立串联限流电阻或恒流驱动 IC。

- 参数与网络：`path=VCC -> D1 Laser -> Q1 AO3400A -> GND`；`series_current_resistor_shown=false`；`constant_current_driver_shown=false`
- 证据：图 a2a1ef414145 / 第 1 页 / 第 1 页左侧 VCC、D1、Q1 与 GND 竖直支路

### VCC 输入去耦

J1 pin3 引入 VCC、pin4 接 GND；C2 100nF 直接跨接 VCC 与 GND，作为接口附近的电源去耦。

- 参数与网络：`input=J1 pin3 VCC`；`return=J1 pin4 GND`；`decoupling=C2 100nF`
- 证据：图 a2a1ef414145 / 第 1 页 / 第 1 页右侧 J1 VCC/GND 与 C2 100nF

## 接口

### J1 GROVE_IO 引脚

J1 GROVE_IO 的 pin1=MISO、pin2=MOSI、pin3=VCC、pin4=GND；pin1 MISO 只有连接器侧短线且未连接其他器件，pin2 MOSI 连接控制网络。

- 参数与网络：`pin1=MISO, no external circuit connection`；`pin2=MOSI, digital control input`；`pin3=VCC, power input`；`pin4=GND`
- 证据：图 a2a1ef414145 / 第 1 页 / 第 1 页右中 J1 pin1-pin4 与各网络标注

## 总线

### 外部通信与调制接口

J1 仅有单向 MOSI 控制线进入 Q1，MISO pin1 未接；页面没有 I2C、SPI、UART、CAN、RS-485、USB 或其他协议控制器，也没有地址、寄存器、时钟或片选网络。

- 参数与网络：`control=single digital MOSI input`；`feedback=null`；`i2c=null`；`spi_controller=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`address=null`
- 证据：图 a2a1ef414145 / 第 1 页 / 第 1 页 J1 与全部线路，无总线控制器或协议网络

## GPIO 与控制信号

### MOSI 数字控制输入

J1 MOSI pin2 连接控制节点，该节点经 R2 51KΩ 下拉至 GND，并经 R1 1KΩ 串联到 Q1 gate；信号方向为外部主机到 Q1。

- 参数与网络：`input=J1 pin2 MOSI`；`series_resistor=R1 1KΩ`；`pulldown=R2 51KΩ`；`destination=Q1 gate`；`direction=external host -> Q1`
- 证据：图 a2a1ef414145 / 第 1 页 / 第 1 页中央 J1 pin2、R2、R1 与 Q1 gate 连线

## 保护电路

### 控制输入默认关断

R2 51KΩ 从 J1 MOSI/R1 输入节点接 GND；当外部控制端不驱动时，该电阻将控制节点保持为低电平侧，避免控制节点悬空。

- 参数与网络：`resistor=R2 51KΩ`；`node=J1 MOSI and R1 input`；`return=GND`；`purpose_from_topology=control-node pulldown`
- 证据：图 a2a1ef414145 / 第 1 页 / 第 1 页中央 R2 51KΩ 从 MOSI 控制节点至 GND

### 接口与激光支路保护器件

完整单页未显示保险丝、TVS/ESD 二极管、反接保护二极管、过流检测、温度检测或激光专用恒流/限流 IC；R1 位于 MOSFET 栅极路径，不在 D1 主电流路径中。

- 参数与网络：`fuse_shown=false`；`tvs_esd_shown=false`；`reverse_protection_shown=false`；`overcurrent_monitor_shown=false`；`temperature_monitor_shown=false`；`laser_current_driver_shown=false`；`r1_location=gate path`
- 证据：图 a2a1ef414145 / 第 1 页 / 第 1 页完整原理图，仅 D1/Q1/R1/R2/C1/C2/J1

## 关键网络

### C1 与 D1 并联网络

C1 100nF 的上端与 D1 上端同接 VCC，下端与 D1 下端同接 Q1 漏极，因此 C1 与 D1 Laser 电气并联。原理图未说明 C1 对脉冲边沿、EMI 或光输出的定量作用。

- 参数与网络：`capacitor=C1 100nF`；`parallel_component=D1 Laser`；`upper_node=VCC`；`lower_node=Q1 drain`
- 证据：图 a2a1ef414145 / 第 1 页 / 第 1 页左上 C1 与 D1 两端共节点

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Laser TX 系统结构 | `controller=external via J1 pin2`；`emitter=D1 Laser`；`switch=Q1 AO3400A`；`control_path=J1 MOSI -> R1 -> Q1 gate`；`local_mcu=null`；`storage=null`；`transceiver=null`；`battery=null`；`regulator=null` |
| 接口 | J1 GROVE_IO 引脚 | `pin1=MISO, no external circuit connection`；`pin2=MOSI, digital control input`；`pin3=VCC, power input`；`pin4=GND` |
| 接口 | 正文 DIN/NC 与原理图 MOSI/MISO 别名 | `documented_yellow=DIN`；`documented_white=NC`；`schematic_pin2=MOSI`；`schematic_pin1=MISO unconnected`；`din_alias_confirmed_in_schematic=false` |
| GPIO 与控制信号 | MOSI 数字控制输入 | `input=J1 pin2 MOSI`；`series_resistor=R1 1KΩ`；`pulldown=R2 51KΩ`；`destination=Q1 gate`；`direction=external host -> Q1` |
| 核心器件 | Q1 AO3400A 低侧开关 | `part=Q1 AO3400A`；`source=GND`；`drain=D1 lower/C1 lower`；`gate=R1 from MOSI`；`topology=N-channel low-side switch` |
| 电源 | 激光发射电流路径 | `path=VCC -> D1 Laser -> Q1 AO3400A -> GND`；`series_current_resistor_shown=false`；`constant_current_driver_shown=false` |
| 关键网络 | C1 与 D1 并联网络 | `capacitor=C1 100nF`；`parallel_component=D1 Laser`；`upper_node=VCC`；`lower_node=Q1 drain` |
| 电源 | VCC 输入去耦 | `input=J1 pin3 VCC`；`return=J1 pin4 GND`；`decoupling=C2 100nF` |
| 保护电路 | 控制输入默认关断 | `resistor=R2 51KΩ`；`node=J1 MOSI and R1 input`；`return=GND`；`purpose_from_topology=control-node pulldown` |
| 保护电路 | 接口与激光支路保护器件 | `fuse_shown=false`；`tvs_esd_shown=false`；`reverse_protection_shown=false`；`overcurrent_monitor_shown=false`；`temperature_monitor_shown=false`；`laser_current_driver_shown=false`；`r1_location=gate path` |
| 总线 | 外部通信与调制接口 | `control=single digital MOSI input`；`feedback=null`；`i2c=null`；`spi_controller=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`address=null` |
| 电源 | 正文 5V 工作电压 | `documented_voltage=5V`；`schematic_net=VCC`；`schematic_voltage=null`；`input_range=null`；`current=null`；`tolerance=null` |
| 其他事实 | 激光光学与数字调制边界 | `documented_application=free-space laser communication`；`documented_pair=LASER.RX`；`laser_part_number=null`；`wavelength=null`；`optical_power=null`；`laser_class=null`；`beam_divergence=null`；`max_duty_cycle=null`；`modulation_frequency=null`；`range=null` |

## 待确认事项

- `interface.documented-port-aliases`：正文 Grove 表将黄色触点称为 DIN、白色触点称为 NC；原理图则将 J1 pin2 标为 MOSI、pin1 标为 MISO 且未接。两组名称的对应关系可由触点顺序推对，但图中没有直接打印 DIN 或 NC。（证据：图 a2a1ef414145 / 第 1 页 / 第 1 页 J1 仅标 MISO/MOSI/VCC/GND，无 DIN/NC 文字）
- `power.documented-5v`：正文规格表与 Grove 管脚表将工作电压标为 5V；原理图只使用 VCC 网络名，没有打印 VCC 数值、允许输入范围、静态电流、峰值电流或容差。（证据：图 a2a1ef414145 / 第 1 页 / 第 1 页 J1/D1/C1/C2 均使用 VCC，整页无电压数字）
- `other.optical-and-modulation-specs`：正文称本产品用于自由空间激光通信并可与 LASER.RX 配对；原理图只将 D1 标为 Laser，没有激光器型号、波长、光功率、激光等级、光束发散角、最大占空比、调制频率、传输距离或接收器兼容条件。（证据：图 a2a1ef414145 / 第 1 页 / 第 1 页 D1 仅标 Laser，整页无光学或时序参数）
- `review.port-aliases`：请用 PCB 丝印、接口定义或实板确认正文 DIN/NC 是否分别对应 J1 pin2 MOSI 与 pin1 MISO 未接。；原因：原理图只打印 MOSI/MISO，未直接打印 DIN/NC 别名。
- `review.vcc-rating`：请用当前 U066 BOM、激光器 datasheet 或实板确认 VCC=5V、允许输入范围及工作/峰值电流。；原因：原理图仅标 VCC，且没有电源额定值或电流参数。
- `review.laser-safety-and-modulation`：请确认 D1 的量产型号、波长、光功率、激光等级、光束发散角、允许占空比/调制频率、传输距离及 LASER.RX 兼容条件。；原因：板级原理图不能证明光学性能、激光安全等级或数字调制边界。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a2a1ef4141450840929d166ca32d336be0b9995dce1df353c64d5e776320c2c6` | `https://static-cdn.m5stack.com/resource/docs/products/unit/laser-tx/laser-tx_sch_01.webp` |

---

源文档：`zh_CN/unit/laser-tx.md`

源文档 SHA-256：`fa45a05d1331cee08cbb8ec8aed33250c52289f4be672a88b0b861c5373cab9f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
