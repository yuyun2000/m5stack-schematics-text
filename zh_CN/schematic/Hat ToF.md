# Hat ToF 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat ToF |
| SKU | U072 |
| 产品 ID | `hat-tof-1a91e659606c` |
| 源文档 | `zh_CN/hat/hat-tof.md` |

## 概述

Hat ToF 以 VL53L0X 激光测距传感器为核心，通过主机连接器的 G26/SCL 与 G0/SDA 接入 I2C。R1、R2 均为 2KΩ，分别将 SCL、SDA 上拉到 +3.3V；主机 3V3 和 GND 为传感器供电。该简化原理图没有画 XSHUT、GPIO1、去耦、保护或其他功能器件。

## 检索关键词

`Hat ToF`、`U072`、`VL53L0X`、`I2C`、`0x29`、`G26 SCL`、`G0 SDA`、`+3.3V`、`R1 2K`、`R2 2K`、`laser ranging`、`time of flight`、`ToF sensor`、`3V3`、`GND`、`XSHUT not shown`、`GPIO1 not shown`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| SENSOR | VL53L0X | I2C 激光飞行时间测距传感器；图中未打印器件位号 | 图 166f1e2ac0d4 / 第 1 页 / 第1页左侧：VL53L0X 方框及 SCL/SDA |
| R1 | 2KΩ | SCL 上拉到 +3.3V | 图 166f1e2ac0d4 / 第 1 页 / 第1页上部：R1 2KΩ |
| R2 | 2KΩ | SDA 上拉到 +3.3V | 图 166f1e2ac0d4 / 第 1 页 / 第1页上部：R2 2KΩ |
| HOST | 未标注 | GND、3V3、G26、G0 等主机触点接口；图中未打印连接器位号 | 图 166f1e2ac0d4 / 第 1 页 / 第1页右侧：GND/5V0/G26/G36/G0/BAT/3V3/5V1 contacts |

## 系统结构

### Hat ToF 架构

VL53L0X 通过 G26/SCL 与 G0/SDA 连接主机 I2C，R1/R2 提供 3.3V 上拉，主机 3V3/GND 提供电源。

- 参数与网络：`sensor=VL53L0X`；`bus=I2C`；`scl=G26`；`sda=G0`；`rail=+3.3V`
- 证据：图 166f1e2ac0d4 / 第 1 页 / 第1页完整单页

## 电源

### VL53L0X 3.3V 供电

主机连接器 3V3 触点连接 +3.3V，GND 触点接地；+3.3V 同时供给 R1/R2 上拉。

- 参数与网络：`input=HOST 3V3`；`rail=+3.3V`；`ground=HOST GND`；`pullup_loads=R1,R2`；`sensor_power_pins=not expanded in simplified schematic`
- 证据：图 166f1e2ac0d4 / 第 1 页 / 第1页 HOST 3V3/GND 与 +3.3V rails

## 接口

### 主机触点映射

主机接口依次标出 GND、5V0、G26、G36、G0、BAT、3V3、5V1；本页功能连接使用 GND、G26/SCL、G0/SDA 与 3V3。

- 参数与网络：`contacts=GND,5V0,G26,G36,G0,BAT,3V3,5V1`；`used=GND,G26,G0,3V3`；`unused_in_function=5V0,G36,BAT,5V1`；`reference_designator_shown=false`
- 证据：图 166f1e2ac0d4 / 第 1 页 / 第1页右侧 host contacts

## 总线

### VL53L0X I2C 总线

主机 G26 接 VL53L0X SCL，G0 接 VL53L0X SDA；R1/R2 2KΩ分别将 SCL/SDA 上拉到 +3.3V。

- 参数与网络：`scl=G26 -> VL53L0X SCL`；`sda=G0 -> VL53L0X SDA`；`pullup_scl=R1 2KΩ to +3.3V`；`pullup_sda=R2 2KΩ to +3.3V`；`logic_level=+3.3V`；`direction=bidirectional`
- 证据：图 166f1e2ac0d4 / 第 1 页 / 第1页 R1/R2、SCL/SDA、G26/G0

## 时钟

### 外部时钟可见性

本页未画独立晶体、晶振或外部时钟输入器件。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`
- 证据：图 166f1e2ac0d4 / 第 1 页 / 第1页完整单页，无 X/Y 位号

## 保护电路

### 保护与去耦可见性

本页未画 TVS、ESD、保险丝、串联保护或电源去耦器件。

- 参数与网络：`tvs_esd_shown=false`；`fuse_shown=false`；`series_protection_shown=false`；`decoupling_shown=false`
- 证据：图 166f1e2ac0d4 / 第 1 页 / 第1页完整单页器件范围

## 传感器

### VL53L0X 连接

原理图中的 VL53L0X 方框仅画出 SCL 与 SDA 两条信号，分别连接 G26 与 G0；未画 XSHUT 或 GPIO1。

- 参数与网络：`device=VL53L0X`；`scl=G26`；`sda=G0`；`xshut_shown=false`；`gpio1_shown=false`；`reference_designator_shown=false`
- 证据：图 166f1e2ac0d4 / 第 1 页 / 第1页左侧 VL53L0X block

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat ToF 架构 | `sensor=VL53L0X`；`bus=I2C`；`scl=G26`；`sda=G0`；`rail=+3.3V` |
| 传感器 | VL53L0X 连接 | `device=VL53L0X`；`scl=G26`；`sda=G0`；`xshut_shown=false`；`gpio1_shown=false`；`reference_designator_shown=false` |
| 总线 | VL53L0X I2C 总线 | `scl=G26 -> VL53L0X SCL`；`sda=G0 -> VL53L0X SDA`；`pullup_scl=R1 2KΩ to +3.3V`；`pullup_sda=R2 2KΩ to +3.3V`；`logic_level=+3.3V`；`direction=bidirectional` |
| 总线地址 | VL53L0X I2C 地址 | `device=VL53L0X`；`documented_address=0x29`；`explicit_address_on_schematic=false` |
| 电源 | VL53L0X 3.3V 供电 | `input=HOST 3V3`；`rail=+3.3V`；`ground=HOST GND`；`pullup_loads=R1,R2`；`sensor_power_pins=not expanded in simplified schematic` |
| 接口 | 主机触点映射 | `contacts=GND,5V0,G26,G36,G0,BAT,3V3,5V1`；`used=GND,G26,G0,3V3`；`unused_in_function=5V0,G36,BAT,5V1`；`reference_designator_shown=false` |
| 保护电路 | 保护与去耦可见性 | `tvs_esd_shown=false`；`fuse_shown=false`；`series_protection_shown=false`；`decoupling_shown=false` |
| 时钟 | 外部时钟可见性 | `crystal_shown=false`；`oscillator_shown=false` |

## 待确认事项

- `address.vl53l0x`：产品正文标称 VL53L0X I2C 地址为 0x29；原理图显示 I2C 连接但未打印地址数值。（证据：图 166f1e2ac0d4 / 第 1 页 / 第1页 VL53L0X SCL/SDA）
- `review.i2c-address`：U072 当前 VL53L0X 的 I2C 地址是否固定为 0x29？；原因：地址来自产品正文，原理图未打印地址数值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `166f1e2ac0d4d4a6ccf955e95462ec35325d0ed68467b556d38d0389c0928368` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat-tof/hat-tof_sch_01.webp` |

---

源文档：`zh_CN/hat/hat-tof.md`

源文档 SHA-256：`241ec0219f0cda3cd1a82ab7ac924f74e17ee31f3068b87b42b7d063fc094e9b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
