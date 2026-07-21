# Hat PIR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat PIR |
| SKU | U054 |
| 产品 ID | `hat-pir-629e63ebfbd6` |
| 源文档 | `zh_CN/hat/hat-pir.md` |

## 概述

Hat PIR 以 U1 PIR_AS312 被动红外传感器为核心，由 P1 STICKIO pin7 的 +3.3V 供电。传感器 OUT pin2 经 R1 1KΩ串联到 P1 pin4/G36，供主机读取数字检测信号；C1 100nF 对电源去耦。其余 STICKIO 信号未接入本页电路。

## 检索关键词

`Hat PIR`、`U054`、`PIR_AS312`、`PIR sensor`、`G36 OUT`、`+3.3V`、`STICKIO`、`R1 1K`、`C1 100nF`、`P1 pin4`、`P1 pin7`、`digital output`、`L=12M /3.3V`、`passive infrared`、`motion detection`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | PIR_AS312 | 被动红外检测传感器，输出数字检测信号 | 图 d3d39d138016 / 第 1 页 / 第1页网格 B2：U1 PIR_AS312 pins1-3 |
| P1 | STICKIO | 主机 3.3V、GND 与 G36 输出接口 | 图 d3d39d138016 / 第 1 页 / 第1页网格 B3：P1 STICKIO pins1-8 |
| R1 | 1KΩ | PIR OUT 到 G36 的串联电阻 | 图 d3d39d138016 / 第 1 页 / 第1页网格 B2：R1 1KΩ |
| C1 | 100nF | PIR_AS312 3.3V 电源去耦 | 图 d3d39d138016 / 第 1 页 / 第1页网格 B2：C1 100nF |

## 系统结构

### Hat PIR 架构

P1 提供 +3.3V 和 GND，U1 PIR_AS312 产生检测输出，R1 将 OUT 串联连接到主机 G36，C1 提供电源去耦。

- 参数与网络：`sensor=U1 PIR_AS312`；`host=P1 STICKIO`；`output=G36`；`rail=+3.3V`
- 证据：图 d3d39d138016 / 第 1 页 / 第1页完整单页

## 电源

### PIR 3.3V 供电

P1 pin7/3V3 连接 +3.3V并供给 U1 VCC pin1；C1 100nF 从 +3.3V 对地去耦。

- 参数与网络：`input=P1 pin7 3V3`；`rail=+3.3V`；`load=U1 VCC pin1`；`decoupling=C1 100nF`
- 证据：图 d3d39d138016 / 第 1 页 / 第1页 P1 pin7、U1 VCC、C1

## 接口

### P1 STICKIO 接口

P1 pin1 为 GND、pin4 G36 为 PIR OUT、pin7 3V3 接 +3.3V；pins2 5VOUT、3 G26、5 G0、6 BAT、8 5VIN 未接入本页功能网络。

- 参数与网络：`pin1=GND`；`pin2=5VOUT unused`；`pin3=G26 unused`；`pin4=G36 / PIR OUT`；`pin5=G0 unused`；`pin6=BAT unused`；`pin7=3V3 / +3.3V`；`pin8=5VIN unused`
- 证据：图 d3d39d138016 / 第 1 页 / 第1页 B3：P1 pins1-8

## GPIO 与控制信号

### PIR 数字输出

U1 OUT pin2 经 R1 1KΩ串联连接 P1 pin4/G36，信号方向为传感器到主机输入。

- 参数与网络：`source=U1 OUT pin2`；`series=R1 1KΩ`；`destination=P1 pin4 / G36`；`direction=sensor output to host input`；`logic_rail=+3.3V`
- 证据：图 d3d39d138016 / 第 1 页 / 第1页 U1 OUT、R1 与 P1 G36

## 时钟

### 外部时钟可见性

本页未画独立晶体、晶振或外部时钟输入器件。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`
- 证据：图 d3d39d138016 / 第 1 页 / 第1页完整单页，无 X/Y 位号

## 保护电路

### 接口保护可见性

本页未画 P1、G36 OUT 或 +3.3V 上的 TVS、ESD、保险丝；OUT 路径仅有 R1 1KΩ串联。

- 参数与网络：`tvs_esd_shown=false`；`fuse_shown=false`；`output_series=R1 1KΩ`
- 证据：图 d3d39d138016 / 第 1 页 / 第1页完整单页保护器件范围

## 传感器

### PIR_AS312 连接

U1 PIR_AS312 VCC pin1 接 +3.3V，OUT pin2 连接 R1，GND pin3 接地。

- 参数与网络：`device=U1 PIR_AS312`；`pin1=VCC / +3.3V`；`pin2=OUT`；`pin3=GND`
- 证据：图 d3d39d138016 / 第 1 页 / 第1页 B2：U1 pins1-3

## 其他事实

### 原理图传感器注记

U1 上方原理图注记原文为 L=12M /3.3V。

- 参数与网络：`note=L=12M /3.3V`
- 证据：图 d3d39d138016 / 第 1 页 / 第1页 B2：U1 上方蓝色 L=12M /3.3V 注记

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat PIR 架构 | `sensor=U1 PIR_AS312`；`host=P1 STICKIO`；`output=G36`；`rail=+3.3V` |
| 传感器 | PIR_AS312 连接 | `device=U1 PIR_AS312`；`pin1=VCC / +3.3V`；`pin2=OUT`；`pin3=GND` |
| GPIO 与控制信号 | PIR 数字输出 | `source=U1 OUT pin2`；`series=R1 1KΩ`；`destination=P1 pin4 / G36`；`direction=sensor output to host input`；`logic_rail=+3.3V` |
| 电源 | PIR 3.3V 供电 | `input=P1 pin7 3V3`；`rail=+3.3V`；`load=U1 VCC pin1`；`decoupling=C1 100nF` |
| 接口 | P1 STICKIO 接口 | `pin1=GND`；`pin2=5VOUT unused`；`pin3=G26 unused`；`pin4=G36 / PIR OUT`；`pin5=G0 unused`；`pin6=BAT unused`；`pin7=3V3 / +3.3V`；`pin8=5VIN unused` |
| 其他事实 | 原理图传感器注记 | `note=L=12M /3.3V` |
| 保护电路 | 接口保护可见性 | `tvs_esd_shown=false`；`fuse_shown=false`；`output_series=R1 1KΩ` |
| 时钟 | 外部时钟可见性 | `crystal_shown=false`；`oscillator_shown=false` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d3d39d138016fbde223e7644c4ffb305d16301db7ae2d44f2664fc86a616acdb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/853/StickHat_PIR_page_01.png` |

---

源文档：`zh_CN/hat/hat-pir.md`

源文档 SHA-256：`9e8cdaa1aa565eadb740a6a9da8989b358ff5a125500b4aa618483363842d03c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
