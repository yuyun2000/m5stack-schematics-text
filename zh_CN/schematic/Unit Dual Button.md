# Unit Dual Button 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Dual Button |
| SKU | U025 |
| 产品 ID | `unit-dual-button-276964214cf7` |
| 源文档 | `zh_CN/unit/dual_button.md` |

## 概述

Unit Dual Button 是一块无板载主控的双瞬时按键输入板，S1 与 S2 分别驱动 A、B 网络并在按下时接 GND。每路使用 10KΩ 上拉、20KΩ 下拉和 100nF 对地电容，释放时节点由电阻分压为约 2/3·VCC。J1 HY-2.0_IO 将 A、B、VCC 和 GND 直接引出，C2 100nF 对 VCC 去耦。

## 检索关键词

`Unit Dual Button`、`U025`、`Dual Button`、`S1`、`S2`、`SW-PB`、`A`、`B`、`J1`、`HY-2.0_IO`、`VCC`、`GND`、`R1 10KΩ(1002)±1%`、`R2 20KΩ(2002)±1%`、`R3 10KΩ(1002)±1%`、`R4 20KΩ(2002)±1%`、`C1 100nF`、`C2 100nF`、`C3 100nF`、`2/3 VCC`、`active low`、`button input`、`Red Btn`、`Blue Btn`、`Grove Port B`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| S1 | SW-PB | A 网络瞬时按键，按下时把 A 接到 GND。 | 图 4fe33f1fff95 / 第 1 页 / 网格 B2，S1 SW-PB 左端 GND、右端 A |
| S2 | SW-PB | B 网络瞬时按键，按下时把 B 接到 GND。 | 图 4fe33f1fff95 / 第 1 页 / 网格 C2，S2 SW-PB 左端 GND、右端 B |
| J1 | HY-2.0_IO | 四针 Grove IO 接口，引出 A、B、VCC 和 GND。 | 图 4fe33f1fff95 / 第 1 页 / 网格 B3，J1 HY-2.0_IO 1-4 脚 A/B/VCC/GND |
| R1,R3 | 10KΩ(1002)±1% | A 与 B 网络到 VCC 的上拉电阻。 | 图 4fe33f1fff95 / 第 1 页 / 网格 B2 R1 与 C2 R3，均标注 10KΩ(1002)±1% 并接 VCC |
| R2,R4 | 20KΩ(2002)±1% | A 与 B 网络到 GND 的下拉电阻，与 10K 上拉形成分压。 | 图 4fe33f1fff95 / 第 1 页 / 网格 B2 R2 与 C2 R4，均标注 20KΩ(2002)±1% 并接 GND |
| C1,C3 | 100nF(104) 10% 50V | A 与 B 网络的对地滤波电容。 | 图 4fe33f1fff95 / 第 1 页 / 网格 B2 C1 与 C2 C3，均标注 100nF(104) 10% 50V 并接 GND |
| C2 | 100nF(104) 10% 50V | J1 VCC 到 GND 的电源去耦电容。 | 图 4fe33f1fff95 / 第 1 页 / 网格 B3，C2 100nF(104) 10% 50V 跨接 VCC 与 GND |

## 系统结构

### 整板架构

整板由 S1、S2、J1、R1-R4 与 C1-C3 构成，两路按键网络直接输出；本页未显示 MCU、电源转换器、存储器、时钟、复位或通信 IC。

- 参数与网络：`buttons=S1,S2`；`outputs=A,B`；`connector=J1 HY-2.0_IO`；`resistors=R1-R4`；`capacitors=C1-C3`；`controller=原理图未显示`；`regulator=原理图未显示`
- 证据：图 4fe33f1fff95 / 第 1 页 / 第 1 页全图，S1/S2/J1/R1-R4/C1-C3

## 电源

### VCC 电源网络

J1.3 连接 VCC，C2 100nF(104) 10% 50V 从 VCC 接 GND；VCC 同时供给 R1/R3 上拉。

- 参数与网络：`connector_pin=J1.3`；`rail=VCC`；`decoupling=C2 100nF(104) 10% 50V`；`pullup_consumers=R1,R3`
- 证据：图 4fe33f1fff95 / 第 1 页 / J1.3 VCC、C2 VCC-GND 与 R1/R3 顶部 VCC

## 接口

### J1 HY-2.0_IO

J1.1-J1.4 分别连接 A、B、VCC、GND，符号内部也按 A、B、VCC、GND 标注。

- 参数与网络：`reference=J1`；`part_number=HY-2.0_IO`；`pin_1=A`；`pin_2=B`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 4fe33f1fff95 / 第 1 页 / 网格 B3，J1 1-4 脚左右网络与功能标注

## GPIO 与控制信号

### S1/A 按键输入

S1 是 A 与 GND 之间的 SW-PB 瞬时按键，闭合时将 J1.1 的 A 网络接到 GND。

- 参数与网络：`switch=S1 SW-PB`；`signal=A`；`connector_pin=J1.1`；`pressed_connection=GND`；`direction=output to host`
- 证据：图 4fe33f1fff95 / 第 1 页 / 网格 B2-B3，S1-GND/A 网络与 J1.1 A

### S2/B 按键输入

S2 是 B 与 GND 之间的 SW-PB 瞬时按键，闭合时将 J1.2 的 B 网络接到 GND。

- 参数与网络：`switch=S2 SW-PB`；`signal=B`；`connector_pin=J1.2`；`pressed_connection=GND`；`direction=output to host`
- 证据：图 4fe33f1fff95 / 第 1 页 / 网格 C2 与 B3，S2-GND/B 网络与 J1.2 B

## 保护电路

### J1 接口保护

J1 的 A、B、VCC、GND 直接进入按键与阻容网络，本页未显示 TVS、保险丝、反接保护或串联限流器件。

- 参数与网络：`connector=J1`；`signals=A,B,VCC,GND`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_protection=原理图未显示`
- 证据：图 4fe33f1fff95 / 第 1 页 / 第 1 页 J1 至 S1/S2/R1-R4/C1-C3 的直接路径

## 关键网络

### A/B 对称网络

A 与 B 两路使用相同的 10KΩ上拉、20KΩ下拉、100nF 对地电容和 SW-PB 接地按键拓扑。

- 参数与网络：`channel_a=S1,R1,R2,C1,A`；`channel_b=S2,R3,R4,C3,B`；`topology=identical`
- 证据：图 4fe33f1fff95 / 第 1 页 / 网格 B2 与 C2 上下两组对称按键电路

## 存储

### 主控与存储

本页未显示 MCU、Flash、EEPROM、SD 卡或其他存储器，A/B 按键状态由外部主机直接采样。

- 参数与网络：`mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`host_inputs=A,B`
- 证据：图 4fe33f1fff95 / 第 1 页 / 第 1 页全图，无主控或存储器位号

## 模拟电路

### A 网络偏置与滤波

A 由 R1 10KΩ上拉到 VCC、R2 20KΩ下拉到 GND，并由 C1 100nF 接 GND；S1 释放时理想直流分压为 VCC×20K/(10K+20K)，约 2/3·VCC。

- 参数与网络：`signal=A`；`pullup=R1 10KΩ(1002)±1%`；`pulldown=R2 20KΩ(2002)±1%`；`capacitor=C1 100nF(104) 10% 50V`；`released_ratio=2/3 VCC`；`pressed_level=GND`
- 证据：图 4fe33f1fff95 / 第 1 页 / 网格 B2，VCC-R1-A-R2/C1-GND 与 S1

### B 网络偏置与滤波

B 由 R3 10KΩ上拉到 VCC、R4 20KΩ下拉到 GND，并由 C3 100nF 接 GND；S2 释放时理想直流分压为 VCC×20K/(10K+20K)，约 2/3·VCC。

- 参数与网络：`signal=B`；`pullup=R3 10KΩ(1002)±1%`；`pulldown=R4 20KΩ(2002)±1%`；`capacitor=C3 100nF(104) 10% 50V`；`released_ratio=2/3 VCC`；`pressed_level=GND`
- 证据：图 4fe33f1fff95 / 第 1 页 / 网格 C2，VCC-R3-B-R4/C3-GND 与 S2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板架构 | `buttons=S1,S2`；`outputs=A,B`；`connector=J1 HY-2.0_IO`；`resistors=R1-R4`；`capacitors=C1-C3`；`controller=原理图未显示`；`regulator=原理图未显示` |
| 接口 | J1 HY-2.0_IO | `reference=J1`；`part_number=HY-2.0_IO`；`pin_1=A`；`pin_2=B`；`pin_3=VCC`；`pin_4=GND` |
| GPIO 与控制信号 | S1/A 按键输入 | `switch=S1 SW-PB`；`signal=A`；`connector_pin=J1.1`；`pressed_connection=GND`；`direction=output to host` |
| GPIO 与控制信号 | S2/B 按键输入 | `switch=S2 SW-PB`；`signal=B`；`connector_pin=J1.2`；`pressed_connection=GND`；`direction=output to host` |
| 模拟电路 | A 网络偏置与滤波 | `signal=A`；`pullup=R1 10KΩ(1002)±1%`；`pulldown=R2 20KΩ(2002)±1%`；`capacitor=C1 100nF(104) 10% 50V`；`released_ratio=2/3 VCC`；`pressed_level=GND` |
| 模拟电路 | B 网络偏置与滤波 | `signal=B`；`pullup=R3 10KΩ(1002)±1%`；`pulldown=R4 20KΩ(2002)±1%`；`capacitor=C3 100nF(104) 10% 50V`；`released_ratio=2/3 VCC`；`pressed_level=GND` |
| 关键网络 | A/B 对称网络 | `channel_a=S1,R1,R2,C1,A`；`channel_b=S2,R3,R4,C3,B`；`topology=identical` |
| 电源 | VCC 电源网络 | `connector_pin=J1.3`；`rail=VCC`；`decoupling=C2 100nF(104) 10% 50V`；`pullup_consumers=R1,R3` |
| 保护电路 | J1 接口保护 | `connector=J1`；`signals=A,B,VCC,GND`；`tvs=原理图未显示`；`fuse=原理图未显示`；`reverse_protection=原理图未显示` |
| 存储 | 主控与存储 | `mcu=原理图未显示`；`flash=原理图未显示`；`eeprom=原理图未显示`；`sd_card=原理图未显示`；`host_inputs=A,B` |
| 电源 | VCC 绝对电压与输出高电平 | `rail=VCC`；`documented_candidate=5V`；`schematic_voltage=未标注`；`released_ratio=2/3 VCC`；`absolute_output_high=需确认` |
| 其他事实 | 红/蓝按键与 A/B 对应 | `schematic_channels=S1/A,S2/B`；`physical_labels=Red Btn,Blue Btn`；`mapping=未标注` |

## 待确认事项

- `power.vcc-voltage-undetermined`：原理图仅标 VCC，没有打印其绝对电压；因此只能确认释放电平约为 2/3·VCC，不能仅由图纸确认正文所示 5V 供电下 A/B 的实际电压和主机逻辑裕量。（证据：图 4fe33f1fff95 / 第 1 页 / J1.3、R1/R3、C2 仅标 VCC，无电压数值）
- `other.button-color-map-undetermined`：原理图只使用 S1/A 与 S2/B 标识，没有红色或蓝色标注，无法由本页确定 Red Btn、Blue Btn 分别对应 A 还是 B。（证据：图 4fe33f1fff95 / 第 1 页 / S1/S2 与 A/B 网络区域，无颜色文字）
- `review.vcc-voltage`：J1 VCC 的额定电压是否固定为 5V，A/B 释放时的保证输出电压及兼容逻辑阈值是多少？；原因：原理图仅标 VCC；10K/20K 分压只能确定比例，不能确定绝对电压。
- `review.button-color-map`：PCB 上红色与蓝色按键分别对应 S1/A 还是 S2/B？；原因：原理图只有 S1/S2 与 A/B 标识，没有物理颜色标注。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `4fe33f1fff95f6addb819b54c5d8bf3337eac264d675a4cee8dea291b317561e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/578/Sch_UNIT_DualButton_v1.1_sch_01.png` |

---

源文档：`zh_CN/unit/dual_button.md`

源文档 SHA-256：`491e7e38172e8f1020001168f259d845fcaff84ae147abd8147ab850a1aabcfd`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
