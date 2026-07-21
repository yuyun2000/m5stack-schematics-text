# Hat DAC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat DAC |
| SKU | U068 |
| 产品 ID | `hat-dac-b4c8fa71d070` |
| 源文档 | `zh_CN/hat/hat-dac.md` |

## 概述

Hat DAC 以 U2 MCP4725_DAC 为数模转换器，通过 P1 的 G26/SCL 与 G0/SDA 接入主机 I2C。U2 A0 接地，SCL/SDA 各由 4.7KΩ上拉到 VCC，DAC VOUT 经 U1 LM321MFX 电压跟随器缓冲后从 P2 pin1 输出。P1 的 5VOUT 为 VCC 电源，U1/U2 各配置 100nF 去耦。

## 检索关键词

`Hat DAC`、`U068`、`MCP4725_DAC`、`MCP4725`、`LM321MFX`、`I2C`、`0x60`、`A0 GND`、`G26 SCL`、`G0 SDA`、`VCC`、`5VOUT`、`DAC VOUT`、`P2 analog output`、`R1 4.7K`、`R2 4.7K`、`C1 100nF`、`C2 100nF`、`C3 100nF`、`voltage follower`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | MCP4725_DAC | I2C 单通道 DAC，输出送入缓冲放大器 | 图 5a42b8f2ff4b / 第 1 页 / 第1页左上：U2 MCP4725_DAC pins1-6 |
| U1 | LM321MFX | DAC 输出电压跟随缓冲器 | 图 5a42b8f2ff4b / 第 1 页 / 第1页中上：U1 LM321MFX pins1-5 |
| P1 | STICKIO | 主机电源与 I2C 接口 | 图 5a42b8f2ff4b / 第 1 页 / 第1页右下：P1 STICKIO pins1-8 |
| P2 | Header 2 | 缓冲模拟输出与 GND 的两针接口 | 图 5a42b8f2ff4b / 第 1 页 / 第1页右上：P2 Header 2 pins1-2 |
| R1,R2 | 4.7KΩ | SCL 与 SDA 上拉到 VCC | 图 5a42b8f2ff4b / 第 1 页 / 第1页左上：R1/R2 4.7KΩ |

## 系统结构

### Hat DAC 架构

P1 提供 VCC、GND、SCL 和 SDA；U2 MCP4725_DAC 完成数模转换，U1 LM321MFX 以电压跟随器方式缓冲 VOUT，P2 输出模拟电压。

- 参数与网络：`dac=U2 MCP4725_DAC`；`buffer=U1 LM321MFX`；`host=P1 STICKIO`；`output=P2 Header 2`
- 证据：图 5a42b8f2ff4b / 第 1 页 / 第1页完整单页

## 电源

### VCC 电源域

P1 pin2/5VOUT 连接 VCC，VCC 为 U2 Vdd pin3、U1 VCC pin5 以及 I2C 上拉电源；U2 Vss pin2 与 U1 VSS pin2 接 GND。

- 参数与网络：`input=P1 pin2 5VOUT`；`rail=VCC`；`loads=U2 Vdd pin3; U1 VCC pin5; R1/R2`；`grounds=U2 Vss pin2; U1 VSS pin2`
- 证据：图 5a42b8f2ff4b / 第 1 页 / 第1页 P1 pin2、U1/U2 VCC/Vdd/VSS

### 电源去耦

C1 100nF 从 VCC 对地，C2 100nF 位于 U2 Vdd，C3 100nF 位于 U1 VCC，三者均对地去耦。

- 参数与网络：`bulk=C1 100nF`；`dac=C2 100nF`；`op_amp=C3 100nF`；`rail=VCC`
- 证据：图 5a42b8f2ff4b / 第 1 页 / 第1页 C1/C2/C3 100nF

## 接口

### P2 模拟输出接口

P2 Header 2 pin1 为 U1 缓冲输出，pin2 为 GND。

- 参数与网络：`connector=P2 Header 2`；`pin1=buffered analog output`；`pin2=GND`；`direction=output`
- 证据：图 5a42b8f2ff4b / 第 1 页 / 第1页右上：P2 pins1-2

### P1 STICKIO 接口

P1 pin1 为 GND、pin2 为 5VOUT/VCC、pin3 G26 为 SCL、pin5 G0 为 SDA；pins4 G36、6 BAT、8 5VIN 标记未连接。

- 参数与网络：`pin1=GND`；`pin2=5VOUT / VCC`；`pin3=G26 / SCL`；`pin4=G36 NC`；`pin5=G0 / SDA`；`pin6=BAT NC`；`pin7=3V3 pin shown with +3.3V label`；`pin8=5VIN NC`
- 证据：图 5a42b8f2ff4b / 第 1 页 / 第1页右下：P1 pins1-8

## 总线

### MCP4725 I2C 连接

P1 pin3/G26 形成 SCL并连接 U2 pin5，P1 pin5/G0 形成 SDA并连接 U2 pin4；R1/R2 4.7KΩ分别将 SCL/SDA 上拉到 VCC。

- 参数与网络：`controller_connector=P1`；`scl=P1 pin3 G26 -> U2 pin5`；`sda=P1 pin5 G0 -> U2 pin4`；`pullup_scl=R1 4.7KΩ to VCC`；`pullup_sda=R2 4.7KΩ to VCC`；`direction=bidirectional`
- 证据：图 5a42b8f2ff4b / 第 1 页 / 第1页 P1 G26/G0、U2 SCL/SDA、R1/R2

## 时钟

### 时钟可见性

本页未画独立晶体、晶振或外部时钟输入。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`
- 证据：图 5a42b8f2ff4b / 第 1 页 / 第1页完整单页，无 X/Y 位号

## 保护电路

### 接口保护可见性

本页未画 P1、P2、I2C 或模拟输出上的 TVS、ESD、保险丝或串联保护器件。

- 参数与网络：`tvs_esd_shown=false`；`fuse_shown=false`；`protected_interfaces=none shown`
- 证据：图 5a42b8f2ff4b / 第 1 页 / 第1页完整单页保护器件范围

## 模拟电路

### MCP4725 模拟输出

U2 Vout pin1 直接连接 U1 +IN pin1，形成 DAC 原始模拟输出到缓冲器的输入路径。

- 参数与网络：`source=U2 Vout pin1`；`destination=U1 +IN pin1`；`net=DAC Vout`
- 证据：图 5a42b8f2ff4b / 第 1 页 / 第1页 U2 Vout pin1 至 U1 +IN pin1

### LM321 电压跟随器

U1 OUTPUT pin4 回接 -IN pin3，构成单位增益电压跟随器；OUTPUT 同时连接 P2 pin1，P2 pin2 接 GND。

- 参数与网络：`op_amp=U1 LM321MFX`；`feedback=OUTPUT pin4 -> -IN pin3`；`input=+IN pin1 from U2 Vout`；`output=U1 pin4 -> P2 pin1`；`return=P2 pin2 GND`；`gain=voltage follower`
- 证据：图 5a42b8f2ff4b / 第 1 页 / 第1页 U1 pins1/3/4 与 P2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat DAC 架构 | `dac=U2 MCP4725_DAC`；`buffer=U1 LM321MFX`；`host=P1 STICKIO`；`output=P2 Header 2` |
| 总线 | MCP4725 I2C 连接 | `controller_connector=P1`；`scl=P1 pin3 G26 -> U2 pin5`；`sda=P1 pin5 G0 -> U2 pin4`；`pullup_scl=R1 4.7KΩ to VCC`；`pullup_sda=R2 4.7KΩ to VCC`；`direction=bidirectional` |
| 总线地址 | MCP4725 地址配置 | `device=U2 MCP4725_DAC`；`a0=GND`；`documented_address=0x60`；`explicit_address_text_on_schematic=false` |
| 电源 | VCC 电源域 | `input=P1 pin2 5VOUT`；`rail=VCC`；`loads=U2 Vdd pin3; U1 VCC pin5; R1/R2`；`grounds=U2 Vss pin2; U1 VSS pin2` |
| 模拟电路 | MCP4725 模拟输出 | `source=U2 Vout pin1`；`destination=U1 +IN pin1`；`net=DAC Vout` |
| 模拟电路 | LM321 电压跟随器 | `op_amp=U1 LM321MFX`；`feedback=OUTPUT pin4 -> -IN pin3`；`input=+IN pin1 from U2 Vout`；`output=U1 pin4 -> P2 pin1`；`return=P2 pin2 GND`；`gain=voltage follower` |
| 接口 | P2 模拟输出接口 | `connector=P2 Header 2`；`pin1=buffered analog output`；`pin2=GND`；`direction=output` |
| 接口 | P1 STICKIO 接口 | `pin1=GND`；`pin2=5VOUT / VCC`；`pin3=G26 / SCL`；`pin4=G36 NC`；`pin5=G0 / SDA`；`pin6=BAT NC`；`pin7=3V3 pin shown with +3.3V label`；`pin8=5VIN NC` |
| 电源 | 电源去耦 | `bulk=C1 100nF`；`dac=C2 100nF`；`op_amp=C3 100nF`；`rail=VCC` |
| 模拟电路 | 标称输出电压范围 | `documented_range=0-3.3V`；`schematic_supply=VCC from P1 5VOUT`；`explicit_range_on_schematic=false`；`limiter_shown=false` |
| 保护电路 | 接口保护可见性 | `tvs_esd_shown=false`；`fuse_shown=false`；`protected_interfaces=none shown` |
| 时钟 | 时钟可见性 | `crystal_shown=false`；`oscillator_shown=false` |

## 待确认事项

- `address.mcp4725-config`：U2 A0 pin6 在原理图中接 GND；产品正文标称 I2C 地址为 0x60，但图中未打印地址数值。（证据：图 5a42b8f2ff4b / 第 1 页 / 第1页 U2 A0 pin6 接 GND）
- `analog.documented-output-range`：产品正文标称输出 0-3.3V；原理图显示 DAC 与缓冲器由 P1 5VOUT/VCC 供电，未打印 0-3.3V 限幅或范围标注。（证据：图 5a42b8f2ff4b / 第 1 页 / 第1页 P1 5VOUT/VCC、U2 Vdd、U1 VCC 与 P2 output）
- `review.i2c-address`：U068 在 A0 接地配置下的实际 I2C 地址是否固定为 0x60？；原因：0x60 来自产品正文；原理图显示 A0 接地，但未打印地址数值。
- `review.output-range`：U068 的实际缓冲输出范围为何标称 0-3.3V，而原理图 VCC 来自 P1 5VOUT？；原因：原理图未显示 3.3V 参考或输出限幅，需核对装配、电源或产品规格。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5a42b8f2ff4b6760aa2fb22bc01f0134d7474265079e43ee6e4cc40d500e42eb` | `https://static-cdn.m5stack.com/resource/docs/products/hat/hat-dac/hat-dac_sch_01.webp` |

---

源文档：`zh_CN/hat/hat-dac.md`

源文档 SHA-256：`db2c312321ec340788fbb47cea3d2419342201d330f7e545fb4cfb7b70ead2bc`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
