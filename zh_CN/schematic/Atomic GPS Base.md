# Atomic GPS Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic GPS Base |
| SKU | A134 |
| 产品 ID | `atomic-gps-base-5a9b55b80f7b` |
| 源文档 | `zh_CN/atom/Atomic GPS Base.md` |

## 概述

当前本地原理图只覆盖 Atomic GPS Base 的 microSD 与排针子电路。U1 TF-015 由 +3.3V 供电，通过 CS、MOSI、CLK、MISO 四条 SPI 网络连接；Rp1 为 4.7KΩ 四联电阻，其中 MISO/CLK/MOSI 上拉到 +3.3V，CS 下拉到 GND。P1 引出 +3.3V、GPS_T、MOSI、CLK、MISO，P2/P3 引出 +5VIN、GND 和 GPS_T；页面没有显示 GPS 芯片、天线、PPS、备份电池、状态指示或电源转换电路。

## 检索关键词

`Atomic GPS Base`、`A134`、`TF-015`、`microSD`、`SPI`、`CS`、`MOSI`、`CLK`、`MISO`、`GPS_T`、`+3.3V`、`+5VIN`、`Rp1`、`4.7KΩ`、`P1 Header 5`、`P2 Header 4`、`P3 Header 4`、`C1 100nF`、`C2 100nF`、`GPS circuit not shown`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | TF-015 | 由 +3.3V 供电并通过四线 SPI 连接的 microSD 卡座 | 图 8484b4e774d1 / 第 1 页 / 页面左侧黄色 U1 TF-015，CS/MOSI/VCC/CLK/GND/MISO 引脚 |
| Rp1 | 4.7KΩ (472) ±5% | 为 MISO、CLK、MOSI 提供 +3.3V 上拉，并为 CS 提供 GND 下拉的四联电阻阵列 | 图 8484b4e774d1 / 第 1 页 / U1 左上 Rp1 四联阵列，8/7/6 接 +3.3V，5 接 GND，1/2/3/4 分别接 MISO/CLK/MOSI/CS |
| P1 | Header 5 | 引出 +3.3V、GPS_T 和 microSD SPI 的 MOSI/CLK/MISO | 图 8484b4e774d1 / 第 1 页 / 页面右上 P1 Header 5，1-5 脚为 +3.3V/GPS_T/MOSI/CLK/MISO |
| P2 | Header 4 | 引出 +5VIN 与 GND，1/2 脚在当前页面未连接 | 图 8484b4e774d1 / 第 1 页 / 页面右上 P2 Header 4，1/2 脚 no-connect，3 +5VIN，4 GND |
| P3 | Header 4 | 引出 +5VIN、GPS_T 与 GND，2 脚在当前页面未连接 | 图 8484b4e774d1 / 第 1 页 / 页面右下 P3 Header 4，1 +5VIN，2 no-connect，3 GPS_T，4 GND |
| C1/C2 | 100nF (104) 10% 50V | 分别对 +3.3V 与 +5VIN 进行对地去耦 | 图 8484b4e774d1 / 第 1 页 / 页面右侧 C1 从 +3.3V 到 GND，C2 从 +5VIN 到 GND |

## 系统结构

### 当前原理图覆盖范围

当前唯一页面包含 U1 TF-015 microSD 卡座、Rp1 偏置阵列、P1/P2/P3 排针和 C1/C2 去耦，没有出现 GPS 接收器或射频电路。

- 参数与网络：`storage_shown=true`；`headers_shown=true`；`gps_receiver_shown=false`；`rf_path_shown=false`
- 证据：图 8484b4e774d1 / 第 1 页 / 整页仅有 TF-015、Rp1、P1/P2/P3 和 C1/C2

## 核心器件

### GPS 主电路可见性

当前页面没有显示 GPS 接收器型号、天线与射频匹配、PPS、备份电池、Flash、UART 接收端、状态指示或 GPS 电源转换。

- 参数与网络：`gps_receiver_shown=false`；`antenna_shown=false`；`pps_shown=false`；`backup_battery_shown=false`；`flash_shown=false`；`uart_rx_shown=false`；`indicators_shown=false`；`gps_power_conversion_shown=false`
- 证据：图 8484b4e774d1 / 第 1 页 / 整页只出现 TF-015、Rp1、P1/P2/P3 和 C1/C2

### 排针用途可见性

P1/P2/P3 仅标为 Header 5/Header 4，没有在当前页面标明各排针对应的 Atom 主机型号、板间连接对象或连接器方向。

- 参数与网络：`p1_role_shown=false`；`p2_role_shown=false`；`p3_role_shown=false`；`mating_orientation_shown=false`
- 证据：图 8484b4e774d1 / 第 1 页 / 页面右侧 P1/P2/P3 下方仅标 Header 5/Header 4

## 电源

### microSD 供电

U1 VCC 4 脚连接 +3.3V，GND 6 脚连接 GND。

- 参数与网络：`component=U1 TF-015`；`supply=+3.3V on pin 4`；`ground=GND on pin 6`
- 证据：图 8484b4e774d1 / 第 1 页 / U1 4 脚 +3.3V 与 6 脚 GND

### 排针电源去耦

C1 100nF (104) 10% 50V 从 +3.3V 接 GND，C2 同规格从 +5VIN 接 GND。

- 参数与网络：`c1=100nF (104) 10% 50V, +3.3V to GND`；`c2=100nF (104) 10% 50V, +5VIN to GND`
- 证据：图 8484b4e774d1 / 第 1 页 / 页面右侧 C1 +3.3V-GND 与 C2 +5VIN-GND

## 接口

### P1 五针排针

P1 Header 5 的 1-5 脚依次为 +3.3V、GPS_T、MOSI、CLK、MISO。

- 参数与网络：`pin1=+3.3V`；`pin2=GPS_T`；`pin3=MOSI`；`pin4=CLK`；`pin5=MISO`
- 证据：图 8484b4e774d1 / 第 1 页 / 页面右上 P1 Header 5 与 1-5 脚网络

### P2 四针排针

P2 Header 4 的 1/2 脚标为未连接，3 脚接 +5VIN，4 脚接 GND。

- 参数与网络：`pin1=not connected`；`pin2=not connected`；`pin3=+5VIN`；`pin4=GND`
- 证据：图 8484b4e774d1 / 第 1 页 / 页面右上 P2 Header 4 与 no-connect/+5VIN/GND

### P3 四针排针

P3 Header 4 的 1 脚接 +5VIN，2 脚标为未连接，3 脚接 GPS_T，4 脚接 GND。

- 参数与网络：`pin1=+5VIN`；`pin2=not connected`；`pin3=GPS_T`；`pin4=GND`
- 证据：图 8484b4e774d1 / 第 1 页 / 页面右下 P3 Header 4 与 +5VIN/no-connect/GPS_T/GND

## 总线

### microSD SPI 网络

U1 使用 CS、MOSI、CLK、MISO 四条 SPI 网络；P1 引出 MOSI、CLK、MISO，但当前页面没有在 P1 上引出 CS。

- 参数与网络：`chip_select=CS -> U1 pin 2`；`controller_to_card=MOSI -> U1 pin 3`；`clock=CLK -> U1 pin 5`；`card_to_controller=MISO -> U1 pin 7`；`p1_cs_shown=false`
- 证据：图 8484b4e774d1 / 第 1 页 / U1 左侧 CS/MOSI/CLK/MISO 与右上 P1 MOSI/CLK/MISO

## GPIO 与控制信号

### SPI 偏置网络

Rp1 的 1/2/3 路分别把 MISO、CLK、MOSI 经 4.7KΩ 上拉到 +3.3V，第 4 路把 CS 经 4.7KΩ 下拉到 GND。

- 参数与网络：`miso=Rp1 pins 1-8, 4.7KΩ pull-up to +3.3V`；`clk=Rp1 pins 2-7, 4.7KΩ pull-up to +3.3V`；`mosi=Rp1 pins 3-6, 4.7KΩ pull-up to +3.3V`；`cs=Rp1 pins 4-5, 4.7KΩ pull-down to GND`
- 证据：图 8484b4e774d1 / 第 1 页 / U1 左上 Rp1：8/7/6 接 +3.3V、5 接 GND，1/2/3/4 接 MISO/CLK/MOSI/CS

## 关键网络

### GPS_T 排针网络

GPS_T 同时连接 P1 2 脚与 P3 3 脚；当前页面没有显示 GPS_T 的源器件。

- 参数与网络：`p1=pin 2`；`p3=pin 3`；`source_component_shown=false`
- 证据：图 8484b4e774d1 / 第 1 页 / 页面右侧 P1 pin 2 与 P3 pin 3 的 GPS_T 标签

## 存储

### TF-015 microSD 引脚

U1 TF-015 的 2 脚为 CS，3 脚为 MOSI，4 脚为 VCC，5 脚为 CLK，6 脚为 GND，7 脚为 MISO。

- 参数与网络：`pin2=CS`；`pin3=MOSI`；`pin4=VCC`；`pin5=CLK`；`pin6=GND`；`pin7=MISO`
- 证据：图 8484b4e774d1 / 第 1 页 / 页面左侧 U1 TF-015 方框内 2-7 脚标签

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 当前原理图覆盖范围 | `storage_shown=true`；`headers_shown=true`；`gps_receiver_shown=false`；`rf_path_shown=false` |
| 存储 | TF-015 microSD 引脚 | `pin2=CS`；`pin3=MOSI`；`pin4=VCC`；`pin5=CLK`；`pin6=GND`；`pin7=MISO` |
| 电源 | microSD 供电 | `component=U1 TF-015`；`supply=+3.3V on pin 4`；`ground=GND on pin 6` |
| 总线 | microSD SPI 网络 | `chip_select=CS -> U1 pin 2`；`controller_to_card=MOSI -> U1 pin 3`；`clock=CLK -> U1 pin 5`；`card_to_controller=MISO -> U1 pin 7`；`p1_cs_shown=false` |
| GPIO 与控制信号 | SPI 偏置网络 | `miso=Rp1 pins 1-8, 4.7KΩ pull-up to +3.3V`；`clk=Rp1 pins 2-7, 4.7KΩ pull-up to +3.3V`；`mosi=Rp1 pins 3-6, 4.7KΩ pull-up to +3.3V`；`cs=Rp1 pins 4-5, 4.7KΩ pull-down to GND` |
| 接口 | P1 五针排针 | `pin1=+3.3V`；`pin2=GPS_T`；`pin3=MOSI`；`pin4=CLK`；`pin5=MISO` |
| 接口 | P2 四针排针 | `pin1=not connected`；`pin2=not connected`；`pin3=+5VIN`；`pin4=GND` |
| 接口 | P3 四针排针 | `pin1=+5VIN`；`pin2=not connected`；`pin3=GPS_T`；`pin4=GND` |
| 关键网络 | GPS_T 排针网络 | `p1=pin 2`；`p3=pin 3`；`source_component_shown=false` |
| 电源 | 排针电源去耦 | `c1=100nF (104) 10% 50V, +3.3V to GND`；`c2=100nF (104) 10% 50V, +5VIN to GND` |
| 核心器件 | GPS 主电路可见性 | `gps_receiver_shown=false`；`antenna_shown=false`；`pps_shown=false`；`backup_battery_shown=false`；`flash_shown=false`；`uart_rx_shown=false`；`indicators_shown=false`；`gps_power_conversion_shown=false` |
| 核心器件 | 排针用途可见性 | `p1_role_shown=false`；`p2_role_shown=false`；`p3_role_shown=false`；`mating_orientation_shown=false` |

## 待确认事项

- `review.full_gps_schematic`：是否有 A134 当前硬件版本的完整 GPS 主电路原理图，可确认接收器型号、UART/PPS、天线、备份电池、Flash、指示灯与电源？；原因：当前唯一资源只覆盖 microSD 和排针子电路，无法完成 GPS 功能链的器件级核对。
- `review.header_roles`：P1、P2、P3 分别连接哪种 Atom 主机或哪块子板，实际插接方向与完整针脚定义是什么？；原因：页面只给出本地针号和网络，没有连接器用途或配对关系。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8484b4e774d1e545bf2222560052662d903c68f5f2d50ba71d36fc8fcaf011f8` | `https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic GPS Base/img-c6106d8c-5518-4355-a565-69c615bef0c8.webp` |

---

源文档：`zh_CN/atom/Atomic GPS Base.md`

源文档 SHA-256：`7ed666e072a2cdb7e44b8bac716e07b5e106c185bf13dcb84992a548e6388cbe`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
