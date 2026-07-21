# Atom SPK 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom SPK |
| SKU | K054 |
| 产品 ID | `atom-spk-9b8445334331` |
| 源文档 | `zh_CN/atom/atom_spk.md` |

## 概述

Atom SPK 通过 P1/P2 接收 Atom 主机的 +3.3V、+5VIN、I2S 音频信号和 TF 卡 SPI 信号。U2 NS4168 接收 LRCLK、BCLK 和 DATA，将音频转换为 VON/VOP 差分输出，并同时连接 P5 扬声器接口与 J1 3.5 mm 插座。U1 TF-015 由 +3.3V 供电，使用 CS、MOSI、CLK、MISO 四线 SPI；Rp1 为三路上拉和一路 CS 下拉提供 4.7KΩ 偏置。P3/P4 并联引出 DATA、BCLK、LRCLK 和 +3.3V。

## 检索关键词

`Atom SPK`、`K054`、`NS4168`、`TF-015`、`TF card`、`microSD`、`I2S`、`SPI`、`LRCLK`、`BCLK`、`DATA`、`SDATA`、`MOSI`、`MISO`、`CLK`、`CS`、`VON`、`VOP`、`+3.3V`、`+5VIN`、`P1 Header 5`、`P2 Header 4`、`P3 Header 2X2`、`P4 Header 2X2`、`P5 Header 2`、`3.5mm jack`、`4.7KΩ`、`differential speaker output`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | TF-015 | 使用 CS、MOSI、CLK、MISO 的 TF 卡插座 | 图 6350bd8032e5 / 第 1 页 / 第 1 页左上 U1 TF-015，pin2 CS、pin3 MOSI、pin4 VCC、pin5 CLK、pin6 GND、pin7 MISO |
| Rp1 | 4.7KΩ (472) ±5% | TF 卡 SPI 网络的三路上拉和一路 CS 下拉电阻阵列 | 图 6350bd8032e5 / 第 1 页 / 第 1 页左上 Rp1，pin8/7/6 接 +3.3V、pin5 接 GND，pin1/2/3/4 分别接 MISO/MOSI/CLK/CS |
| U2 | NS4168 | 接收 I2S LRCLK/BCLK/DATA 并输出 VON/VOP 差分音频的功放 | 图 6350bd8032e5 / 第 1 页 / 第 1 页右上 U2 NS4168，CTRL/LRCLK/BCLK/SDATA、VDD/GND 与 VON/VOP |
| P1 | Header 5 | Atom 侧 +3.3V、BCLK 与 TF 卡 SPI 信号接口 | 图 6350bd8032e5 / 第 1 页 / 第 1 页左下 P1 Header 5，pin1 +3.3V、pin2 BCLK、pin3 MOSI、pin4 CLK、pin5 MISO |
| P2 | Header 4 | Atom 侧 LRCLK、DATA、+5VIN 和 GND 接口 | 图 6350bd8032e5 / 第 1 页 / 第 1 页左下 P2 Header 4，pin1 LRCLK、pin2 DATA、pin3 +5VIN、pin4 GND |
| P3,P4 | Header 2X2 | 并联引出 DATA、BCLK、LRCLK 和 +3.3V 的板间接口 | 图 6350bd8032e5 / 第 1 页 / 第 1 页中左 P3 与右下 P4，均为 pin1 DATA、pin2 BCLK、pin3 LRCLK、pin4 +3.3V |
| P5 | Header 2 | 引出 NS4168 VON/VOP 差分扬声器输出 | 图 6350bd8032e5 / 第 1 页 / 第 1 页右上 P5 Header 2，pin2 接 U2 VON、pin1 接 U2 VOP |
| J1 | 3.5mm jack | 接收 VON/VOP 差分音频的 3.5 mm 插座 | 图 6350bd8032e5 / 第 1 页 / 第 1 页右上 J1 3.5mm jack，pin2 接 VON、pin3 接 VOP，pin1/pin4 未画外部网络连接 |
| C1,C2 | 100nF (104) 10% 50V | +3.3V 与 +5VIN 电源轨的对地去耦电容 | 图 6350bd8032e5 / 第 1 页 / 第 1 页左下 C1 从 +3.3V 到 GND、C2 从 +5VIN 到 GND，均标注 100nF (104) 10% 50V |
| C3 | 10uF (106) 10% 10V | NS4168 +3.3V VDD 电源轨的对地去耦电容 | 图 6350bd8032e5 / 第 1 页 / 第 1 页右上 C3 10uF (106) 10% 10V，连接 U2 VDD 的 +3.3V 电源轨与 GND |

## 系统结构

### Atom SPK 音频与存储架构

P1/P2 从 Atom 主机引入 +3.3V、+5VIN、I2S 和 SPI 网络；U2 NS4168 将 I2S 音频转换为 VON/VOP 差分输出，U1 TF-015 通过 SPI 网络连接主机，P3/P4 另行并联引出 I2S 和 +3.3V。

- 参数与网络：`audio_amplifier=U2 NS4168`；`storage_connector=U1 TF-015`；`host_connectors=P1 Header 5, P2 Header 4`；`expansion_connectors=P3/P4 Header 2X2`；`audio_outputs=P5 Header 2, J1 3.5mm jack`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页完整单页原理图，U1/Rp1、P1-P4、U2/P5/J1 与 C1-C3

## 电源

### NS4168 供电与控制

U2 NS4168 的 CTRL pin1 和 VDD pin6 均接 +3.3V，GND pin7 接 GND；C3 10uF 从该 +3.3V VDD 电源轨连接至 GND。

- 参数与网络：`CTRL=pin1 +3.3V`；`VDD=pin6 +3.3V`；`GND=pin7 GND`；`decoupling=C3 10uF (106) 10% 10V`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页右上 U2 CTRL/VDD/GND 与 C3 的 +3.3V-GND 连接

### +3.3V 与 +5VIN 去耦

C1 100nF (104) 10% 50V 连接 +3.3V 与 GND，C2 同规格电容连接 +5VIN 与 GND。

- 参数与网络：`+3.3V=C1 100nF (104) 10% 50V to GND`；`+5VIN=C2 100nF (104) 10% 50V to GND`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页左下 C1 的 +3.3V-GND 与 C2 的 +5VIN-GND 连接

## 接口

### Atom 主机连接器映射

P1 Header 5 的 pin1=+3.3V、pin2=BCLK、pin3=MOSI、pin4=CLK、pin5=MISO；P2 Header 4 的 pin1=LRCLK、pin2=DATA、pin3=+5VIN、pin4=GND。

- 参数与网络：`P1=pin1 +3.3V, pin2 BCLK, pin3 MOSI, pin4 CLK, pin5 MISO`；`P2=pin1 LRCLK, pin2 DATA, pin3 +5VIN, pin4 GND`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页左下 P1 Header 5 与 P2 Header 4 的针脚和网络名

### P3/P4 I2S 扩展接口

P3 与 P4 具有相同映射：pin1=DATA、pin2=BCLK、pin3=LRCLK、pin4=+3.3V。

- 参数与网络：`P3=pin1 DATA, pin2 BCLK, pin3 LRCLK, pin4 +3.3V`；`P4=pin1 DATA, pin2 BCLK, pin3 LRCLK, pin4 +3.3V`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页中左 P3 与右下 P4 Header 2X2 的 DATA/BCLK/LRCLK/+3.3V

## 总线

### TF 卡 SPI 总线

U1 使用 CS、MOSI、CLK、MISO 四个网络构成 SPI 连接，其中 MOSI、CLK、MISO 经 P1 接至 Atom 主机。

- 参数与网络：`chip_select=CS`；`controller_to_card=MOSI`；`card_to_controller=MISO`；`clock=CLK`；`host_connector=P1 pins 3-5 for MOSI/CLK/MISO`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页左侧 U1 TF-015 与 P1 的同名 MOSI/CLK/MISO 网络，以及 U1 CS 网络

### NS4168 I2S 输入

U2 NS4168 的 LRCLK pin2、BCLK pin3 和 SDATA pin4 分别连接 LRCLK、BCLK 和 DATA 网络。

- 参数与网络：`LRCLK=U2 pin2 LRCLK`；`BCLK=U2 pin3 BCLK`；`SDATA=U2 pin4 DATA`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页右上 U2 NS4168 左侧 pin2 LRCLK、pin3 BCLK、pin4 SDATA/DATA

## 关键网络

### TF 卡 SPI 偏置电阻

Rp1 的 4.7KΩ 电阻分别将 MISO、MOSI、CLK 上拉至 +3.3V，并将 CS 下拉至 GND。

- 参数与网络：`value=4.7KΩ (472) ±5%`；`MISO=Rp1 pin1 to pin8 +3.3V`；`MOSI=Rp1 pin2 to pin7 +3.3V`；`CLK=Rp1 pin3 to pin6 +3.3V`；`CS=Rp1 pin4 to pin5 GND`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页左上 Rp1 的 pin1-8、+3.3V/GND 端和 MISO/MOSI/CLK/CS 连接

## 存储

### TF-015 TF 卡针脚映射

U1 TF-015 的 pin2=CS、pin3=MOSI、pin4=VCC/+3.3V、pin5=CLK、pin6=GND、pin7=MISO。

- 参数与网络：`pin2=CS`；`pin3=MOSI`；`pin4=VCC +3.3V`；`pin5=CLK`；`pin6=GND`；`pin7=MISO`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页左上 U1 TF-015 的 pin2 至 pin7 与 CS/MOSI/VCC/CLK/GND/MISO

## 音频

### NS4168 差分音频输出

U2 NS4168 从 VON pin5 和 VOP pin8 输出差分音频，两个网络同时进入 P5 和 J1。

- 参数与网络：`negative_output=VON pin5`；`positive_output=VOP pin8`；`destinations=P5 Header 2, J1 3.5mm jack`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页右上 U2 VON pin5、VOP pin8 到 P5 与 J1 的两条网络

### P5 扬声器输出接口

P5 Header 2 的 pin2 接 VON，pin1 接 VOP，直接引出 NS4168 的差分输出。

- 参数与网络：`pin2=VON / U2 pin5`；`pin1=VOP / U2 pin8`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页右上 P5 Header 2 与 U2 VON/VOP 直连

### J1 3.5 mm 插座音频连接

J1 pin2 接 VON、pin3 接 VOP；原理图没有给 J1 pin1 和 pin4 画出外部网络连接。

- 参数与网络：`pin2=VON / U2 pin5`；`pin3=VOP / U2 pin8`；`pin1_external_net=null`；`pin4_external_net=null`
- 证据：图 6350bd8032e5 / 第 1 页 / 第 1 页右上 J1 3.5mm jack，pin2/pin3 左侧分别连接 VON/VOP，pin1/pin4 左侧无外部网络线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom SPK 音频与存储架构 | `audio_amplifier=U2 NS4168`；`storage_connector=U1 TF-015`；`host_connectors=P1 Header 5, P2 Header 4`；`expansion_connectors=P3/P4 Header 2X2`；`audio_outputs=P5 Header 2, J1 3.5mm jack` |
| 接口 | Atom 主机连接器映射 | `P1=pin1 +3.3V, pin2 BCLK, pin3 MOSI, pin4 CLK, pin5 MISO`；`P2=pin1 LRCLK, pin2 DATA, pin3 +5VIN, pin4 GND` |
| 存储 | TF-015 TF 卡针脚映射 | `pin2=CS`；`pin3=MOSI`；`pin4=VCC +3.3V`；`pin5=CLK`；`pin6=GND`；`pin7=MISO` |
| 总线 | TF 卡 SPI 总线 | `chip_select=CS`；`controller_to_card=MOSI`；`card_to_controller=MISO`；`clock=CLK`；`host_connector=P1 pins 3-5 for MOSI/CLK/MISO` |
| 关键网络 | TF 卡 SPI 偏置电阻 | `value=4.7KΩ (472) ±5%`；`MISO=Rp1 pin1 to pin8 +3.3V`；`MOSI=Rp1 pin2 to pin7 +3.3V`；`CLK=Rp1 pin3 to pin6 +3.3V`；`CS=Rp1 pin4 to pin5 GND` |
| 接口 | P3/P4 I2S 扩展接口 | `P3=pin1 DATA, pin2 BCLK, pin3 LRCLK, pin4 +3.3V`；`P4=pin1 DATA, pin2 BCLK, pin3 LRCLK, pin4 +3.3V` |
| 总线 | NS4168 I2S 输入 | `LRCLK=U2 pin2 LRCLK`；`BCLK=U2 pin3 BCLK`；`SDATA=U2 pin4 DATA` |
| 电源 | NS4168 供电与控制 | `CTRL=pin1 +3.3V`；`VDD=pin6 +3.3V`；`GND=pin7 GND`；`decoupling=C3 10uF (106) 10% 10V` |
| 音频 | NS4168 差分音频输出 | `negative_output=VON pin5`；`positive_output=VOP pin8`；`destinations=P5 Header 2, J1 3.5mm jack` |
| 音频 | P5 扬声器输出接口 | `pin2=VON / U2 pin5`；`pin1=VOP / U2 pin8` |
| 音频 | J1 3.5 mm 插座音频连接 | `pin2=VON / U2 pin5`；`pin3=VOP / U2 pin8`；`pin1_external_net=null`；`pin4_external_net=null` |
| 电源 | +3.3V 与 +5VIN 去耦 | `+3.3V=C1 100nF (104) 10% 50V to GND`；`+5VIN=C2 100nF (104) 10% 50V to GND` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6350bd8032e5d535e15fc3d932e6d4f4358a99329bec122f73380497fed9f133` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_spk/atom_spk_sch_01.webp` |

---

源文档：`zh_CN/atom/atom_spk.md`

源文档 SHA-256：`7b692926efc3dd50b13a646295cf830b88eb37756810429660d399ee8f2faf7c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
