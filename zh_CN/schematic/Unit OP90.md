# Unit OP90 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit OP90 |
| SKU | U057 |
| 产品 ID | `unit-op90-38e94bce5a10` |
| 源文档 | `zh_CN/unit/OP.90.md` |

## 概述

Unit OP90 以 U1 ITR9606 槽型光电开关完成红外发射与遮挡检测，不含 MCU、存储器或时钟电路。发射二极管由 VCC 经 R1 1KΩ 限流，光敏晶体管集电极输出经 R3 10KΩ 上拉、R2 20KΩ 下拉和 C4 100nF 滤波后形成 MISO。J1 GROVE_IO 引出 MISO、VCC 和 GND，pin 2 在原理图中明确未连接，C5 100nF 为电源去耦。

## 检索关键词

`Unit OP90`、`U057`、`OP.90`、`ITR9606`、`U1`、`GROVE_IO`、`J1`、`MISO`、`VCC`、`GND`、`NC`、`R1 1KΩ`、`R2 20KΩ`、`R3 10KΩ`、`C4 100nF`、`C5 100nF`、`infrared emitter`、`phototransistor`、`photo interrupter`、`optical limit switch`、`digital output`、`active low`、`HY2.0-4P`、`PORT.B`、`90 degree`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ITR9606 | 集成红外发射二极管与光敏晶体管的槽型光电开关，产生遮挡检测信号 | 图 dc417b1afd7c / 第 1 页 / 页面中央 U1，器件值 ITR9606，左侧红外 LED、右侧受光晶体管符号 |
| J1 | GROVE_IO | 4 针外部接口，引出 MISO 检测输出、VCC 和 GND | 图 dc417b1afd7c / 第 1 页 / 页面右侧 J1 GROVE_IO：pin 1 MISO、pin 2 NC 标记、pin 3 VCC、pin 4 GND |
| R1 | 1KΩ | U1 红外发射二极管的 VCC 侧串联限流电阻 | 图 dc417b1afd7c / 第 1 页 / 页面左中 R1 1KΩ，连接 VCC 与 U1 红外 LED 上端 |
| R2/R3 | 20KΩ / 10KΩ | MISO 节点的下拉/上拉偏置分压网络 | 图 dc417b1afd7c / 第 1 页 / 页面中右 MISO 节点：R3 10KΩ 接 VCC，R2 20KΩ 接 GND |
| C4/C5 | 100nF | C4 对 MISO 滤波，C5 对 VCC 电源去耦 | 图 dc417b1afd7c / 第 1 页 / 页面左侧 C5 100nF 跨接 VCC-GND；页面中右 C4 100nF 跨接 MISO-GND |

## 系统结构

### Unit OP90

U1 ITR9606 同时提供红外发射和光敏晶体管接收，外围仅包含发射限流、输出偏置滤波、电源去耦和一个 Grove 接口；本页未显示 MCU、协处理器、存储器、晶振、复位或调试电路。

- 参数与网络：`sensor=U1 ITR9606`；`emitter_limit=R1 1KΩ`；`output_bias=R3 10KΩ to VCC,R2 20KΩ to GND`；`output_filter=C4 100nF to GND`；`connector=J1 GROVE_IO`；`controller=null`；`storage=null`；`clock=null`
- 证据：图 dc417b1afd7c / 第 1 页 / 整页：C5、R1、U1、R2/R3/C4 和 J1 构成全部可见电路

## 电源

### U1 红外发射侧

VCC 经 R1 1KΩ 串联到 U1 红外发射二极管，二极管另一端接 GND，发射支路在上电时持续获得偏置。

- 参数与网络：`supply=VCC`；`series_resistor=R1 1KΩ`；`load=U1 infrared LED`；`return=GND`；`enable_control=null`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面左中 VCC-R1 1KΩ-U1 发射 LED-GND 串联路径

### VCC 电源轨

J1 pin 3 输入 VCC，VCC 直接供给 R1 发射支路、R3 输出上拉和 C5 去耦；本页未显示电源转换器、LDO、负载开关、充电器或电池。

- 参数与网络：`input=J1 pin 3`；`rail=VCC`；`loads=R1 infrared emitter branch,R3 MISO pullup,C5 decoupling`；`converter=null`；`ldo=null`；`load_switch=null`；`charger=null`；`battery=null`
- 证据：图 dc417b1afd7c / 第 1 页 / 整页 VCC 标记位于 J1 pin 3、R1 上端、R3 上端和 C5 上端；无电源 IC

### C5 电源去耦

C5 100nF 跨接在 VCC 与 GND 之间，为光电开关电路提供本地电源去耦。

- 参数与网络：`reference=C5`；`capacitance=100nF`；`positive_node=VCC`；`return=GND`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面左侧 C5 100nF，上端接 VCC、下端接 GND

## 接口

### J1 GROVE_IO

J1 pin 1 标注 MISO，pin 2 带未连接标记，pin 3 标注 VCC，pin 4 标注 GND。

- 参数与网络：`reference=J1`；`part_number=GROVE_IO`；`pin_1=MISO output`；`pin_2=NC`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面右侧 J1 GROVE_IO 的 1=MISO、2=NC 红色叉号、3=VCC、4=GND

## GPIO 与控制信号

### MISO 检测输出

MISO 是由 U1 光敏晶体管下拉的板到主机输出；受光使晶体管导通时输出趋向低电平，光路被遮挡使晶体管截止时输出由 R3/R2 偏置网络抬高。

- 参数与网络：`net=MISO`；`direction=output from Unit OP90 to host`；`light_received=low tendency`；`beam_blocked=biased high tendency`；`driver=U1 phototransistor collector`；`connector_pin=J1 pin 1`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面中央 U1 光敏晶体管接 MISO/GND，页面右侧 R3/R2 偏置及 J1 pin 1 MISO

## 保护电路

### J1 外部接口保护

本页未显示 J1 的 VCC、MISO 或 GND 路径上有保险丝、反接保护、TVS/ESD 阵列或串联输出保护电阻；J1 直接连接内部网络。

- 参数与网络：`fuse=null`；`reverse_polarity_protection=null`；`tv_esd=null`；`output_series_resistor=null`；`visible_protection=none`
- 证据：图 dc417b1afd7c / 第 1 页 / 整页 J1 到 VCC/MISO/GND 的直接连接，未见保护器件位号

## 关键网络

### MISO

MISO 同时连接 U1 光敏晶体管集电极、R3 下端、R2 上端、C4 上端和 J1 pin 1，是整板唯一的功能输出网络。

- 参数与网络：`net=MISO`；`sensor_node=U1 phototransistor collector`；`pullup_node=R3 10KΩ lower terminal`；`pulldown_node=R2 20KΩ upper terminal`；`filter_node=C4 100nF upper terminal`；`external_pin=J1 pin 1`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面中央至右侧连续横线：U1 集电极、R3、R2、C4 与 J1 pin 1 MISO 共节点

## 传感器

### U1 ITR9606

U1 符号左侧为红外发射二极管，右侧为受其光照控制的光敏晶体管；二者构成非接触遮挡检测光路。

- 参数与网络：`reference=U1`；`part_number=ITR9606`；`emitter=infrared LED`；`receiver=phototransistor`；`sensing_method=beam interruption`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面中央 U1 ITR9606，LED 与光敏晶体管之间有光箭头

## 模拟电路

### U1 光敏晶体管输出

U1 光敏晶体管的发射极接 GND，集电极直接连接 MISO 节点；光敏晶体管导通时对 MISO 形成下拉。

- 参数与网络：`collector=MISO`；`emitter=GND`；`effect_when_conducting=pull MISO toward GND`；`output_stage=phototransistor collector`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面中央 U1 右侧晶体管：集电极接输出横线，发射极向下接 GND

### MISO 偏置网络

MISO 由 R3 10KΩ 上拉至 VCC，并由 R2 20KΩ 下拉至 GND；在忽略光敏晶体管与外部负载时，电阻分压给出的静态电压为约 2/3 VCC。

- 参数与网络：`pullup=R3 10KΩ to VCC`；`pulldown=R2 20KΩ to GND`；`unloaded_divider_ratio=2/3 VCC`；`thevenin_resistance=6.67KΩ`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面中右 MISO 节点的 R3 10KΩ-VCC 与 R2 20KΩ-GND 分压支路

### C4 输出滤波

C4 100nF 从 MISO 接至 GND，与 R3/R2 的等效电阻构成输出低通滤波；按标称值计算的无外部负载 RC 时间常数约为 0.667 ms。

- 参数与网络：`capacitor=C4 100nF`；`connection=MISO to GND`；`bias_thevenin_resistance=6.67KΩ`；`nominal_rc_time_constant=0.667ms`
- 证据：图 dc417b1afd7c / 第 1 页 / 页面中右 C4 100nF 从 MISO 节点接 GND，并与 R3 10KΩ/R2 20KΩ 同节点

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit OP90 | `sensor=U1 ITR9606`；`emitter_limit=R1 1KΩ`；`output_bias=R3 10KΩ to VCC,R2 20KΩ to GND`；`output_filter=C4 100nF to GND`；`connector=J1 GROVE_IO`；`controller=null`；`storage=null`；`clock=null` |
| 传感器 | U1 ITR9606 | `reference=U1`；`part_number=ITR9606`；`emitter=infrared LED`；`receiver=phototransistor`；`sensing_method=beam interruption` |
| 电源 | U1 红外发射侧 | `supply=VCC`；`series_resistor=R1 1KΩ`；`load=U1 infrared LED`；`return=GND`；`enable_control=null` |
| 模拟电路 | U1 光敏晶体管输出 | `collector=MISO`；`emitter=GND`；`effect_when_conducting=pull MISO toward GND`；`output_stage=phototransistor collector` |
| 模拟电路 | MISO 偏置网络 | `pullup=R3 10KΩ to VCC`；`pulldown=R2 20KΩ to GND`；`unloaded_divider_ratio=2/3 VCC`；`thevenin_resistance=6.67KΩ` |
| 模拟电路 | C4 输出滤波 | `capacitor=C4 100nF`；`connection=MISO to GND`；`bias_thevenin_resistance=6.67KΩ`；`nominal_rc_time_constant=0.667ms` |
| GPIO 与控制信号 | MISO 检测输出 | `net=MISO`；`direction=output from Unit OP90 to host`；`light_received=low tendency`；`beam_blocked=biased high tendency`；`driver=U1 phototransistor collector`；`connector_pin=J1 pin 1` |
| 接口 | J1 GROVE_IO | `reference=J1`；`part_number=GROVE_IO`；`pin_1=MISO output`；`pin_2=NC`；`pin_3=VCC`；`pin_4=GND` |
| 关键网络 | MISO | `net=MISO`；`sensor_node=U1 phototransistor collector`；`pullup_node=R3 10KΩ lower terminal`；`pulldown_node=R2 20KΩ upper terminal`；`filter_node=C4 100nF upper terminal`；`external_pin=J1 pin 1` |
| 电源 | VCC 电源轨 | `input=J1 pin 3`；`rail=VCC`；`loads=R1 infrared emitter branch,R3 MISO pullup,C5 decoupling`；`converter=null`；`ldo=null`；`load_switch=null`；`charger=null`；`battery=null` |
| 电源 | C5 电源去耦 | `reference=C5`；`capacitance=100nF`；`positive_node=VCC`；`return=GND` |
| 保护电路 | J1 外部接口保护 | `fuse=null`；`reverse_polarity_protection=null`；`tv_esd=null`；`output_series_resistor=null`；`visible_protection=none` |
| 电源 | VCC 标称电压 | `schematic_rail=VCC`；`schematic_voltage=null`；`document_voltage=5V`；`connector_pin=J1 pin 3` |
| 接口 | J1 Grove 线色映射 | `electrical_pinout=pin1 MISO,pin2 NC,pin3 VCC,pin4 GND`；`color_labels_on_schematic=null`；`document_colors=Black,Red,Yellow,White` |
| 传感器 | OP90 机械光路角度 | `product_claim=90 degree`；`schematic_mechanical_angle=null`；`sensor=U1 ITR9606` |
| GPIO 与控制信号 | MISO 主机数字电平兼容性 | `output_net=MISO`；`nominal_unloaded_high=2/3 VCC`；`host_input_threshold=null`；`guaranteed_voh=null`；`guaranteed_vol=null` |

## 待确认事项

- `power.vcc-voltage`：产品正文将 Grove 电源写为 5V，但原理图电源轨只标注 VCC，没有电压数值，因此无法仅凭本页确认 VCC 必须为 5 V。（证据：图 dc417b1afd7c / 第 1 页 / 页面 J1 pin 3、R1/R3/C5 电源节点均仅标 VCC，无 5V 数字标注）
- `interface.grove-color-mapping`：原理图给出 J1 pin 1-4 的电气网络，但未标注 Black/Red/Yellow/White 线色，不能仅凭本页验证产品正文中的线色映射。（证据：图 dc417b1afd7c / 第 1 页 / 页面右侧 J1 仅显示 MISO/NC/VCC/GND 与 pin 编号，无线色文字）
- `sensor.mechanical-angle`：产品名与正文描述为 90° 光电限位结构，但电气原理图仅显示 ITR9606 内部光耦符号，没有机械尺寸或发射/接收器空间夹角，90°结构不能由本页复核。（证据：图 dc417b1afd7c / 第 1 页 / 整页为电气连接图，仅 U1 ITR9606 符号，无机械角度或尺寸标注）
- `gpio.host-logic-thresholds`：原理图显示 MISO 的模拟偏置和下拉结构，但未标注主机输入阈值、允许电压范围或保证的 VOH/VOL，因此无法仅凭本页确认特定主控的数字电平裕量。（证据：图 dc417b1afd7c / 第 1 页 / 页面中右 R3/R2/C4-MISO-J1 pin 1；整页无 VIH/VIL/VOH/VOL 或主控型号标注）
- `review.vcc-voltage`：请用当前版本 BOM、设计说明或实板电源定义确认 J1 pin 3 的 VCC 标称值是否固定为 5 V。；原因：原理图只写 VCC，未给出数值；正文的 5V 不能替代原理图证据。
- `review.grove-color-mapping`：请结合连接器方向、线缆规范或 PCB 确认 Black/Red/Yellow/White 与 J1 pin 1-4 的对应关系。；原因：原理图没有 Grove 线色标签，只有电气 pinout。
- `review.mechanical-angle`：请用结构图或 PCB/外壳机械资料复核 OP90 的 90°发射接收结构。；原因：电气原理图没有机械夹角或尺寸，无法证明 90°结构。
- `review.host-logic-thresholds`：请结合实际 VCC、ITR9606 参数和目标主控 VIH/VIL 复核 MISO 的高低电平裕量。；原因：原理图可算出无负载偏置比，但没有主机阈值与器件最差参数，不能确认数字接口裕量。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `dc417b1afd7c43d6a5ab8846c96ad7d9edee711617c034f23e2d103ad748dc2a` | `https://static-cdn.m5stack.com/resource/docs/products/unit/OP.90/img-2e3ce6f3-673a-4a87-9d0f-e355656ec33f.webp` |

---

源文档：`zh_CN/unit/OP.90.md`

源文档 SHA-256：`bc342312ace2b1b4ff1dde276536402b5d7722d3c74cc1cd81d5efcee5ecec2d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
