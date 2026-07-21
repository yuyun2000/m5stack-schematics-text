# Atomic ToChain Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic ToChain Base |
| SKU | A163 |
| 产品 ID | `atomic-tochain-base-30a3334c64cf` |
| 源文档 | `zh_CN/accessory/Atomic_ToChain_Base.md` |

## 概述

Atomic ToChain Base 是由 P1/P2 Atom 底部排针、J1 Grove 接口和两组 0R/NC 选择焊盘组成的无源信号转接电路。VCC_5V 与 GND 从 P1 直接连接 J1，IO1/IO2 则可分别从 GPIO22、GPIO19、GPIO23、GPIO33、GPIO21、GPIO25 六个物理信号中选择。默认装配 R7=0R 和 R2=0R，使 Atom Lite 的 GPIO22/GPIO19 分别连接 IO1/IO2；原理图同时标注这些位置在 Atom S3 上对应 GPIO5/GPIO6。

## 检索关键词

`Atomic ToChain Base`、`A163`、`Atom Lite`、`Atom S3`、`GROVE`、`HY2.0-4P`、`IO1`、`IO2`、`GPIO22`、`GPIO19`、`GPIO23`、`GPIO33`、`GPIO21`、`GPIO25`、`GPIO5`、`GPIO6`、`SCL`、`SDA`、`VCC_5V`、`GND`、`0R`、`NC`、`R1-R12`、`Header 4`、`Header 5`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| P1 | Header 4 | Atom 4 Pin 电源与 I2C/GPIO 排针 | 图 e862cef01a89 / 第 1 页 / B3 区域 P1 Header 4：4 脚 SCL/GPIO21、3 脚 SDA/GPIO25、2 脚 VCC_5V、1 脚 GND |
| P2 | Header 5 | Atom 5 Pin GPIO 与 3V3 排针 | 图 e862cef01a89 / 第 1 页 / B2 区域 P2 Header 5：5 脚 3V3 标记 NC，4/3/2/1 脚为 GPIO22/GPIO19/GPIO23/GPIO33 |
| J1 | GROVE 1x4P | Chain/Grove 输出接口，引出 IO2、IO1、VCC_5V、GND | 图 e862cef01a89 / 第 1 页 / B3-B4 区域 J1 GROVE 1x4P：1~4 脚对应 IO2、IO1、VCC、GND |
| R1 | NC | GPIO22 到 IO2 的可选连接位 | 图 e862cef01a89 / 第 1 页 / B2 区域左侧 IO2 选择组：GPIO22-R1(NC)-IO2 |
| R2 | 0R | GPIO19 到 IO2 的默认连接位 | 图 e862cef01a89 / 第 1 页 / B2 区域左侧 IO2 选择组：GPIO19-R2(0R)-IO2 |
| R3 | NC | GPIO23 到 IO2 的可选连接位 | 图 e862cef01a89 / 第 1 页 / B2 区域左侧 IO2 选择组：GPIO23-R3(NC)-IO2 |
| R4 | NC | GPIO33 到 IO2 的可选连接位 | 图 e862cef01a89 / 第 1 页 / B2 区域左侧 IO2 选择组：GPIO33-R4(NC)-IO2 |
| R5 | NC | GPIO21/SCL 到 IO2 的可选连接位 | 图 e862cef01a89 / 第 1 页 / B2 区域左侧 IO2 选择组：GPIO21-R5(NC)-IO2 |
| R6 | NC | GPIO25/SDA 到 IO2 的可选连接位 | 图 e862cef01a89 / 第 1 页 / B2 区域左侧 IO2 选择组：GPIO25-R6(NC)-IO2 |
| R7 | 0R | GPIO22 到 IO1 的默认连接位 | 图 e862cef01a89 / 第 1 页 / B2-B3 区域右侧 IO1 选择组：GPIO22-R7(0R)-IO1 |
| R8 | NC | GPIO19 到 IO1 的可选连接位 | 图 e862cef01a89 / 第 1 页 / B2-B3 区域右侧 IO1 选择组：GPIO19-R8(NC)-IO1 |
| R9 | NC | GPIO23 到 IO1 的可选连接位 | 图 e862cef01a89 / 第 1 页 / B2-B3 区域右侧 IO1 选择组：GPIO23-R9(NC)-IO1 |
| R10 | NC | GPIO33 到 IO1 的可选连接位 | 图 e862cef01a89 / 第 1 页 / B2-B3 区域右侧 IO1 选择组：GPIO33-R10(NC)-IO1 |
| R11 | NC | GPIO21/SCL 到 IO1 的可选连接位 | 图 e862cef01a89 / 第 1 页 / B2-B3 区域右侧 IO1 选择组：GPIO21-R11(NC)-IO1 |
| R12 | NC | GPIO25/SDA 到 IO1 的可选连接位 | 图 e862cef01a89 / 第 1 页 / B2-B3 区域右侧 IO1 选择组：GPIO25-R12(NC)-IO1 |

## 系统结构

### Atomic ToChain Base

该页只包含 P1、P2、J1 和 R1~R12 选择连接位；IO1/IO2 通过 0R 或 NC 焊盘从 Atom 底部信号中选择，VCC_5V/GND 直接转接到 J1。

- 参数与网络：`atom_headers=P1 Header 4,P2 Header 5`；`chain_connector=J1 GROVE 1x4P`；`selector_bank=R1-R12`；`active_ic=null`
- 证据：图 e862cef01a89 / 第 1 页 / 整页 B2-B4 区域：P1/P2、R1~R12、J1 及其全部连线

## 电源

### VCC_5V/GND

P1.2 的 VCC_5V 直接连接 J1.3，P1.1 的 GND 直接连接 J1.4；P2.5 的 3V3 未接入 J1。

- 参数与网络：`vcc_path=P1.2 VCC_5V to J1.3 VCC`；`ground_path=P1.1 GND to J1.4 GND`；`unused_power=P2.5 3V3 NC`
- 证据：图 e862cef01a89 / 第 1 页 / B2-B4 区域 P1/P2/J1：同名 VCC_5V/GND 网络及 P2.5 3V3 红色 NC

## 接口

### P1 Header 4

P1 的 4 脚连接 SCL/GPIO21，3 脚连接 SDA/GPIO25，2 脚连接 VCC_5V，1 脚连接 GND。

- 参数与网络：`pin_4=SCL GPIO21`；`pin_3=SDA GPIO25`；`pin_2=VCC_5V`；`pin_1=GND`
- 证据：图 e862cef01a89 / 第 1 页 / B3 区域 P1：4/3/2/1 脚与 SCL GPIO21、SDA GPIO25、VCC_5V、GND 标注

### P2 Header 5

P2 的 5 脚连接 3V3 但标记不接，4 脚连接 GPIO22，3 脚连接 GPIO19，2 脚连接 GPIO23，1 脚连接 GPIO33。

- 参数与网络：`pin_5=3V3 NC`；`pin_4=GPIO22`；`pin_3=GPIO19`；`pin_2=GPIO23`；`pin_1=GPIO33`
- 证据：图 e862cef01a89 / 第 1 页 / B2 区域 P2：5~1 脚、3V3 红色 NC 标记及 GPIO22/GPIO19/GPIO23/GPIO33

### J1 GROVE 1x4P

J1 的 1 脚连接 IO2，2 脚连接 IO1，3 脚连接 VCC_5V，4 脚连接 GND。

- 参数与网络：`pin_1=IO2`；`pin_2=IO1`；`pin_3=VCC_5V`；`pin_4=GND`
- 证据：图 e862cef01a89 / 第 1 页 / B3-B4 区域 J1：1/2/3/4 脚与 IO2/IO1/VCC/GND 字段和左侧网络

## 总线

### SCL/SDA 可选接入

P1.4 的 SCL/GPIO21 可通过 R5 接 IO2 或通过 R11 接 IO1；P1.3 的 SDA/GPIO25 可通过 R6 接 IO2 或通过 R12 接 IO1，但 R5/R6/R11/R12 当前均标注 NC。

- 参数与网络：`SCL_to_IO2=R5 NC`；`SCL_to_IO1=R11 NC`；`SDA_to_IO2=R6 NC`；`SDA_to_IO1=R12 NC`
- 证据：图 e862cef01a89 / 第 1 页 / B2-B3 区域：P1 SCL/GPIO21、SDA/GPIO25 与 R5/R6/R11/R12 选择路径

## GPIO 与控制信号

### IO2 选择组 R1~R6

IO2 可由 GPIO22、GPIO19、GPIO23、GPIO33、GPIO21 或 GPIO25 连接；当前仅 R2 为 0R，将 GPIO19 接入 IO2，R1/R3/R4/R5/R6 均标注 NC。

- 参数与网络：`GPIO22=R1 NC`；`GPIO19=R2 0R selected`；`GPIO23=R3 NC`；`GPIO33=R4 NC`；`GPIO21=R5 NC`；`GPIO25=R6 NC`；`output=IO2`
- 证据：图 e862cef01a89 / 第 1 页 / B2 区域左侧选择阵列：GPIO22/19/23/33/21/25 经 R1~R6 汇入 IO2，阻值状态为 NC/0R/NC/NC/NC/NC

### IO1 选择组 R7~R12

IO1 可由 GPIO22、GPIO19、GPIO23、GPIO33、GPIO21 或 GPIO25 连接；当前仅 R7 为 0R，将 GPIO22 接入 IO1，R8/R9/R10/R11/R12 均标注 NC。

- 参数与网络：`GPIO22=R7 0R selected`；`GPIO19=R8 NC`；`GPIO23=R9 NC`；`GPIO33=R10 NC`；`GPIO21=R11 NC`；`GPIO25=R12 NC`；`output=IO1`
- 证据：图 e862cef01a89 / 第 1 页 / B2-B3 区域右侧选择阵列：GPIO22/19/23/33/21/25 经 R7~R12 汇入 IO1，阻值状态为 0R/NC/NC/NC/NC/NC

### Atom Lite 默认 IO

原理图注释与 0R 装配共同标明 Atom Lite 默认 IO2=GPIO19、IO1=GPIO22。

- 参数与网络：`IO2=GPIO19 via R2 0R`；`IO1=GPIO22 via R7 0R`
- 证据：图 e862cef01a89 / 第 1 页 / B2-B3 区域：R2/R7 的 0R 标注及右侧 Atom Lite default Pin: GPIO19/GPIO22 注释

### Atom S3 默认 IO

原理图注释标明同一默认物理位置在 Atom S3 上对应 IO2=GPIO6、IO1=GPIO5。

- 参数与网络：`IO2=GPIO6`；`IO1=GPIO5`
- 证据：图 e862cef01a89 / 第 1 页 / B3 区域 J1 左侧注释：Atom S3 列的 GPIO6/GPIO5 分别与 IO2/IO1 行对齐

## 其他事实

### IO 选择焊盘改配

原理图注释说明默认只选择六个 IO 中的两个；更换 IO 时需移除默认 0R 电阻，并将对应 IO 的焊盘短接。

- 参数与网络：`default_selected_count=2`；`candidate_count_per_output=6`；`rework=remove 0R resistor and short-circuit corresponding IO pad`
- 证据：图 e862cef01a89 / 第 1 页 / C2 区域灰色英文注释：Two of the six IOs are selected by default... remove the 0R resistor and short-circuit the pad

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic ToChain Base | `atom_headers=P1 Header 4,P2 Header 5`；`chain_connector=J1 GROVE 1x4P`；`selector_bank=R1-R12`；`active_ic=null` |
| 接口 | P1 Header 4 | `pin_4=SCL GPIO21`；`pin_3=SDA GPIO25`；`pin_2=VCC_5V`；`pin_1=GND` |
| 接口 | P2 Header 5 | `pin_5=3V3 NC`；`pin_4=GPIO22`；`pin_3=GPIO19`；`pin_2=GPIO23`；`pin_1=GPIO33` |
| 接口 | J1 GROVE 1x4P | `pin_1=IO2`；`pin_2=IO1`；`pin_3=VCC_5V`；`pin_4=GND` |
| 电源 | VCC_5V/GND | `vcc_path=P1.2 VCC_5V to J1.3 VCC`；`ground_path=P1.1 GND to J1.4 GND`；`unused_power=P2.5 3V3 NC` |
| GPIO 与控制信号 | IO2 选择组 R1~R6 | `GPIO22=R1 NC`；`GPIO19=R2 0R selected`；`GPIO23=R3 NC`；`GPIO33=R4 NC`；`GPIO21=R5 NC`；`GPIO25=R6 NC`；`output=IO2` |
| GPIO 与控制信号 | IO1 选择组 R7~R12 | `GPIO22=R7 0R selected`；`GPIO19=R8 NC`；`GPIO23=R9 NC`；`GPIO33=R10 NC`；`GPIO21=R11 NC`；`GPIO25=R12 NC`；`output=IO1` |
| GPIO 与控制信号 | Atom Lite 默认 IO | `IO2=GPIO19 via R2 0R`；`IO1=GPIO22 via R7 0R` |
| GPIO 与控制信号 | Atom S3 默认 IO | `IO2=GPIO6`；`IO1=GPIO5` |
| 总线 | SCL/SDA 可选接入 | `SCL_to_IO2=R5 NC`；`SCL_to_IO1=R11 NC`；`SDA_to_IO2=R6 NC`；`SDA_to_IO1=R12 NC` |
| 其他事实 | IO 选择焊盘改配 | `default_selected_count=2`；`candidate_count_per_output=6`；`rework=remove 0R resistor and short-circuit corresponding IO pad` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e862cef01a89268ee0554adac2bbeac9c2e32f4849b3a72d348c248a162507dc` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1193/A163-Atom-Chain_SCH_Main_V1.0_20250902_page_01.png` |

---

源文档：`zh_CN/accessory/Atomic_ToChain_Base.md`

源文档 SHA-256：`ecc8a38b52850b2e90631b4179a2829ed100e56a0b07147d1a4700d65e8c9bca`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
