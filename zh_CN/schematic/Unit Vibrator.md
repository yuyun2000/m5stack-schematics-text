# Unit Vibrator 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Vibrator |
| SKU | U059 |
| 产品 ID | `unit-vibrator-ee09b947945b` |
| 源文档 | `zh_CN/unit/vibrator.md` |

## 概述

Unit Vibrator 的资源页显示一组无主控的直流电机低侧开关电路。J1 pin2 MOSI 经 R1 1K 驱动 Q1 AO3400A 栅极，R2 51K 将控制节点下拉；Q1 导通时把 B1 Motor 下端拉向 GND，B1 上端接 VCC。D1 1N4148WS T4 与 C2 100nF 并接在电机两端，C1 100nF 从 VCC 接 GND；J1 pin1 MISO 未连接。页面未给 VCC 数值、电机具体型号、转速、PWM 频率或机械偏心轮，并且资源 URL 使用 unit_fan 路径名。

## 检索关键词

`Unit Vibrator`、`U059`、`AO3400A`、`B1 Motor`、`N20 motor`、`D1 1N4148WS T4`、`R1 1K`、`R2 51K`、`C1 100nF`、`C2 100nF`、`GROVE_IO`、`J1`、`MOSI`、`MISO`、`VCC`、`GND`、`low-side switch`、`PWM`、`10kHz`、`8800RPM`、`DIN`、`GPIO control`、`flyback diode`、`eccentric wheel`、`unit_fan_sch_01`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| B1 | Motor | VCC 与 Q1 漏极节点之间的直流电机负载 | 图 b008603cddfd / 第 1 页 / 第 1 页左上，B1 Motor，上端 VCC、下端 Q1 漏极节点 |
| Q1 | AO3400A | 由 J1 pin2 控制的 N 沟道低侧电机开关 | 图 b008603cddfd / 第 1 页 / 第 1 页左下，Q1 AO3400A，漏极接 B1、源极接 GND、栅极接 R1 |
| D1 | 1N4148WS T4 | 并接 B1 电机两端的续流/反向电压钳位二极管 | 图 b008603cddfd / 第 1 页 / 第 1 页左上，D1 1N4148WS T4 并接 VCC 与 Q1 漏极节点 |
| J1 | GROVE_IO | 四针控制与电源接口，pin2 MOSI 控制电机，pin3 VCC、pin4 GND，pin1 MISO 未连接 | 图 b008603cddfd / 第 1 页 / 第 1 页右侧，J1 GROVE_IO pins1-4 MISO/MOSI/VCC/GND |
| R1,R2 | 1K / 51K | R1 为 Q1 栅极串联电阻，R2 将控制节点下拉到 GND | 图 b008603cddfd / 第 1 页 / 第 1 页中央，J1 MOSI-R1 1K-Q1 gate 与 R2 51K-GND |
| C1,C2 | 100nF / 100nF | C1 为接口 VCC 对地去耦，C2 并接电机两端抑制噪声 | 图 b008603cddfd / 第 1 页 / 第 1 页，C1 VCC-GND 与 C2 VCC-Q1漏极节点 |

## 系统结构

### Unit Vibrator 驱动架构

J1 提供 VCC/GND 和单路 MOSI 控制，MOSI 经 R1/R2 驱动 Q1 AO3400A，Q1 低侧开关 B1 Motor；D1/C2 并接电机，C1 为 VCC 去耦。

- 参数与网络：`connector=J1 GROVE_IO`；`control=MOSI`；`switch=Q1 AO3400A`；`load=B1 Motor`；`flyback=D1 1N4148WS T4`；`motor_cap=C2 100nF`；`supply_cap=C1 100nF`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页完整电路

### 本页未包含的子系统

该页未显示 MCU、协处理器、存储、晶振、复位/BOOT、调试、I2C/UART/CAN/RS-485/USB、射频、音频、传感器、电池或充电电路；MISO 未连接。

- 参数与网络：`mcu=null`；`storage=null`；`clock=null`；`reset_debug=null`；`digital_buses=null`；`rf=null`；`audio=null`；`sensor=null`；`battery_charger=null`；`miso=NC`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页完整原理图，仅有电机、MOSFET、接口和无源保护

## 电源

### 电机低侧开关路径

B1 Motor 上端接 VCC，下端接 Q1 drain，Q1 source 接 GND；Q1 导通时形成 VCC-B1-Q1-GND 电流路径。

- 参数与网络：`path=VCC -> B1 Motor -> Q1 drain/source -> GND`；`switch=Q1 AO3400A`；`topology=low-side`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页左侧 B1/Q1/VCC/GND

### VCC 去耦

C1 100nF 从 J1 pin3 VCC 接到 GND，位于接口电源侧；图中未显示稳压器、负载开关、电流检测或电源使能。

- 参数与网络：`capacitor=C1 100nF`；`rail=VCC`；`ground=GND`；`regulator=null`；`load_switch=null`；`current_monitor=null`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页 J1 VCC/GND 与 C1

## 接口

### J1 Grove 针脚映射

J1 pin1 标 MISO 但未连接，pin2 标 MOSI 并连接控制网络，pin3 接 VCC，pin4 接 GND；该页未将 MOSI/MISO 标为完整 SPI 总线。

- 参数与网络：`reference=J1 GROVE_IO`；`pin1=MISO, NC`；`pin2=MOSI, control input`；`pin3=VCC power input`；`pin4=GND`；`complete_spi=false`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页右侧 J1 pins1-4

## GPIO 与控制信号

### MOSI 电机控制输入

J1 pin2 MOSI 经 R1 1K 接 Q1 gate，R2 51K 从同一控制节点接 GND；外部信号为高时可使 Q1 导通，低或悬空时 R2 把 gate 拉低。

- 参数与网络：`input=J1 pin2 MOSI`；`series=R1 1K`；`pulldown=R2 51K`；`gate=Q1 AO3400A`；`high=Q1 on`；`low_or_open=Q1 gate pulled to GND`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页 J1 MOSI/R1/R2/Q1 gate

## 保护电路

### 电机续流与噪声抑制

D1 1N4148WS T4 与 C2 100nF 均并接 VCC 与 B1 下端/Q1 drain 节点；D1 提供反向电压钳位路径，C2 为电机端并联滤波。

- 参数与网络：`diode=D1 1N4148WS T4`；`capacitor=C2 100nF`；`nodes=VCC and motor low/Q1 drain`；`tvs=null`；`fuse=null`
- 证据：图 b008603cddfd / 第 1 页 / 第 1 页 B1 并联 D1/C2 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Vibrator 驱动架构 | `connector=J1 GROVE_IO`；`control=MOSI`；`switch=Q1 AO3400A`；`load=B1 Motor`；`flyback=D1 1N4148WS T4`；`motor_cap=C2 100nF`；`supply_cap=C1 100nF` |
| 接口 | J1 Grove 针脚映射 | `reference=J1 GROVE_IO`；`pin1=MISO, NC`；`pin2=MOSI, control input`；`pin3=VCC power input`；`pin4=GND`；`complete_spi=false` |
| GPIO 与控制信号 | MOSI 电机控制输入 | `input=J1 pin2 MOSI`；`series=R1 1K`；`pulldown=R2 51K`；`gate=Q1 AO3400A`；`high=Q1 on`；`low_or_open=Q1 gate pulled to GND` |
| 电源 | 电机低侧开关路径 | `path=VCC -> B1 Motor -> Q1 drain/source -> GND`；`switch=Q1 AO3400A`；`topology=low-side` |
| 保护电路 | 电机续流与噪声抑制 | `diode=D1 1N4148WS T4`；`capacitor=C2 100nF`；`nodes=VCC and motor low/Q1 drain`；`tvs=null`；`fuse=null` |
| 电源 | VCC 去耦 | `capacitor=C1 100nF`；`rail=VCC`；`ground=GND`；`regulator=null`；`load_switch=null`；`current_monitor=null` |
| 系统结构 | 本页未包含的子系统 | `mcu=null`；`storage=null`；`clock=null`；`reset_debug=null`；`digital_buses=null`；`rf=null`；`audio=null`；`sensor=null`；`battery_charger=null`；`miso=NC` |
| 其他事实 | 原理图资源路径与产品身份 | `resource_path=products/unit/unit_fan/unit_fan_sch_01.webp`；`page_motor_label=B1 Motor`；`product_label_on_page=null`；`u059_label_on_page=null`；`confirmed_for_u059=false` |
| 核心器件 | 正文 N20 电机与偏心轮 | `documented_motor=N20 DC motor`；`documented_mass=metal eccentric wheel`；`documented_direction=one-way`；`documented_no_load_speed=8800RPM`；`schematic_motor=B1 Motor`；`stall_current=null` |
| GPIO 与控制信号 | 正文 PWM 频率与强度调节 | `documented_control=GPIO/PWM`；`documented_frequency=10kHz`；`documented_intensity=duty-cycle control`；`duty_range=null`；`minimum_pulse=null`；`response_time=null` |
| 电源 | 正文 5V 功耗 | `documented_test=PWM 10kHz,50% duty`；`documented_power=5V@424.35mA`；`schematic_rail=VCC`；`startup_current=null`；`stall_current=null`；`tolerance=null` |
| 接口 | 正文 DIN/NC 与页面 MOSI/MISO 命名 | `documented_yellow=DIN`；`documented_white=NC`；`schematic_pin2=MOSI control`；`schematic_pin1=MISO NC`；`naming_alignment=null` |

## 待确认事项

- `other.schematic-resource-identity`：资源 URL 路径名为 unit_fan/unit_fan_sch_01.webp，页面负载仅标 B1 Motor，没有 Unit Vibrator、U059、N20 或偏心轮文字；该图是否为 Unit Vibrator 正式量产图需确认。（证据：图 b008603cddfd / 第 1 页 / 第 1 页完整页面，无标题栏或 Unit Vibrator/U059/N20 标识）
- `component.documented-motor-mechanics`：正文称使用 N20 直流电机和金属偏心轮，单向旋转且空载 8800RPM；原理图只标 B1 Motor，没有电机料号、偏心轮、机械方向、转速或堵转参数。（证据：图 b008603cddfd / 第 1 页 / 第 1 页 B1 仅标 Motor）
- `gpio.documented-pwm-control`：正文称支持 GPIO/PWM 控制、推荐 PWM 频率 10kHz，并以占空比无级调节震动强度；原理图确认 MOSI 到 MOSFET gate 的开关路径，但未标频率、占空比范围、最小脉宽或电机响应。（证据：图 b008603cddfd / 第 1 页 / 第 1 页 J1 MOSI-R1-Q1-B1 路径，无 PWM 参数）
- `power.documented-voltage-consumption`：正文给出 10kHz、50% 占空比时 5V@424.35mA；原理图电源只标 VCC，未标电压、平均/峰值电流、启动/堵转电流、测试负载、温度或容差。（证据：图 b008603cddfd / 第 1 页 / 第 1 页 VCC/B1/Q1 电源路径，无额定值）
- `interface.documented-grove-labels`：正文管脚表将 PORT.B 黄色线称 DIN、白色线称 NC；原理图将相应控制针脚标 MOSI、未用针脚标 MISO。电气连接一致，但接口信号正式命名需统一。（证据：图 b008603cddfd / 第 1 页 / 第 1 页 J1 pins1/2 标 MISO/MOSI）
- `review.resource-identity`：unit_fan_sch_01.webp 是否确为 U059 Unit Vibrator 当前正式量产原理图？；原因：资源路径指向 unit_fan，页面没有产品名/SKU/N20 标识。
- `review.motor-mechanics`：请用 BOM、机械图和实测确认 N20 电机、偏心轮、单向特性、8800RPM、启动/堵转电流及寿命。；原因：原理图只显示通用 Motor 符号。
- `review.pwm-control`：请确认 10kHz 推荐值、允许 PWM 范围、占空比-震感关系、启动/停止响应和低占空比边界。；原因：原理图只确认开关拓扑。
- `review.voltage-consumption`：请确认 5V@424.35mA 的测试条件、平均/峰值、启动/堵转电流、温度和容差。；原因：页面只标 VCC，没有电气额定值。
- `review.grove-labels`：请确认外部 API 和丝印应使用 DIN/NC 还是 MOSI/MISO 命名，并固定 J1 针脚顺序。；原因：正文与原理图使用不同信号名。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `b008603cddfd4c1b55a4a2b8159c2e476e85a252484dfee1f800f1a72e389981` | `https://static-cdn.m5stack.com/resource/docs/products/unit/unit_fan/unit_fan_sch_01.webp` |

---

源文档：`zh_CN/unit/vibrator.md`

源文档 SHA-256：`c89f5ee20b64edb0c09bb499d4359440fcf07897aa59ec0d9c74819598fbc5af`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
