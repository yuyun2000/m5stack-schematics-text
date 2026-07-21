# Stamp-Pico 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-Pico |
| SKU | C050-B |
| 产品 ID | `stamp-pico-2def1461ad81` |
| 源文档 | `zh_CN/core/stamp_pico.md` |

## 概述

Stamp-Pico 以 U2 PICO_D4 为主控，连接五金 3D 天线、GPIO27 控制的 SK6812_3535、GPIO39 用户按键以及 J1/J2 外部接口。SYS_P050 由 J1/J2 的 5V 引脚输入，经 U1 SY80079AAAC 降压形成 MCU_P033，并由 J2 提供 3.3V 引出。J2 还引出 EN、UART0 和 12 路 GPIO，图中未配置板载 USB-UART 下载电路。

## 检索关键词

`Stamp-Pico`、`C050-B`、`ESP32-PICO-D4`、`PICO_D4`、`SY80079AAAC`、`SK6812_3535`、`五金3D天线`、`SYS_P050`、`MCU_P033`、`GPIO27 RGB`、`GPIO39 Button`、`GPIO0 Boot`、`GPIO1 U0TXD`、`GPIO3 U0RXD`、`GPIO18`、`GPIO19`、`GPIO21`、`GPIO22`、`GPIO25`、`GPIO26`、`GPIO32`、`GPIO33`、`GPIO36`、`EN`、`J1 GROVE`、`J2 DNP`、`R1 22K/1%`、`R2 5.1K/1%`、`L1 2.20H`、`L2 0R`、`C5 TBD`、`C6 TBD`、`U0TXD`、`U0RXD`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | PICO_D4 | 主控模块，连接射频、GPIO、UART0、RGB、按键和外部接口 | 图 81479376963d / 第 1 页 / 第1页右上主控区：U2 PICO_D4，pins0-46 |
| U1 | SY80079AAAC | SYS_P050 到 MCU_P033 的降压转换器 | 图 81479376963d / 第 1 页 / 第1页左下电源区：U1 SY80079AAAC |
| LED1 | SK6812_3535 | 由 GPIO27 控制的可编程 RGB LED | 图 81479376963d / 第 1 页 / 第1页下部中央：LED1 SK6812_3535 |
| ANT1 | 五金3D天线 | 经 L2/C5/C6 匹配网络连接 U2 LNA_IN 的板载天线 | 图 81479376963d / 第 1 页 / 第1页顶部：ANT1 五金3D天线、L2/C5/C6 |
| S1 | SW | 按下将 GPIO39 拉到 GND 的用户按键 | 图 81479376963d / 第 1 页 / 第1页右下：S1 SW、GPIO39、R3 |
| J1 | GROVE | GPIO32/GPIO33、5V 和 GND 的 4 针外部接口 | 图 81479376963d / 第 1 页 / 第1页左上：J1 GROVE pins1-4 |
| J2 | DNP | EN、UART0、GPIO、电源和 GND 的主引出接口 | 图 81479376963d / 第 1 页 / 第1页左中：J2，底部标注 DNP |
| L1 | 2.20H | U1 SW 到 MCU_P033 的降压储能电感 | 图 81479376963d / 第 1 页 / 第1页左下：L1，图中标注 2.20H |

## 系统结构

### Stamp-Pico 架构

U2 PICO_D4 连接板载 3D 天线、LED1 SK6812_3535、GPIO39 按键和 J1/J2；U1 SY80079AAAC 将 SYS_P050 转换为 MCU_P033。

- 参数与网络：`soc=U2 PICO_D4`；`power=U1 SY80079AAAC`；`antenna=ANT1 五金3D天线`；`rgb=LED1 SK6812_3535`；`button=S1 GPIO39`；`connectors=J1 GROVE; J2 DNP`
- 证据：图 81479376963d / 第 1 页 / 第1页完整单页：U1/U2、ANT1、LED1、S1、J1/J2

## 电源

### SYS_P050 到 MCU_P033

U1 SY80079AAAC 的 IN pin1 与 EN pin4 接 SYS_P050，SW pin3 经 L1 输出 MCU_P033；FB pin5 由 R1 22KΩ/1% 与 R2 5.1KΩ/1% 分压。

- 参数与网络：`converter=U1 SY80079AAAC`；`input=SYS_P050`；`enable=SYS_P050`；`switch_pin=U1 SW pin3`；`inductor=L1 2.20H`；`output=MCU_P033`；`feedback_top=R1 22KΩ/1%`；`feedback_bottom=R2 5.1KΩ/1%`；`input_cap=C1 226/10V`；`output_cap=C3 226/10V`
- 证据：图 81479376963d / 第 1 页 / 第1页左下：U1 pins1-5、L1、R1/R2、C1/C3

### 外部 5V/3.3V 电源接口

J1 pin2 与 J2 5V 引脚连接 SYS_P050；J2 3V3 引脚连接 MCU_P033；J1 pin1 与 J2 GND 引脚接地。

- 参数与网络：`five_volt_inputs=J1 pin2 5V; J2 5V -> SYS_P050`；`three_volt_output=J2 3V3 -> MCU_P033`；`grounds=J1 pin1; J2 GND`；`logic_rail=MCU_P033`
- 证据：图 81479376963d / 第 1 页 / 第1页左侧 J1/J2 的 5V/3V3/GND 与 SYS_P050/MCU_P033

### PICO_D4 电源域与去耦

U2 VDDA、VDDA3P3、VDD3P3、VDD3P3_RTC、VDD3P3_CPU 和 VDD_SDIO 接 MCU_P033，并配置 C7-C12、C14 对地去耦。

- 参数与网络：`rail=MCU_P033`；`domains=VDDA,VDDA3P3,VDD3P3,VDD3P3_RTC,VDD3P3_CPU,VDD_SDIO`；`bulk_cap=C7 226/6.3V`；`decoupling=C8/C9/C10/C11/C12/C14 105/6.3V`；`pad=U2 PAD pin0 -> GND`
- 证据：图 81479376963d / 第 1 页 / 第1页 U2 右下 power pins1/3/4/19/37/43/46/26、C7-C12/C14

## 接口

### J1 GROVE 接口

J1 pins1-4 依次为 GND、5V/SYS_P050、IO1/GPIO32、IO2/GPIO33；GPIO32/33 为 MCU_P033 逻辑域的可配置 GPIO。

- 参数与网络：`connector=J1 GROVE`；`pin1=GND`；`pin2=5V / SYS_P050`；`pin3=IO1 / GPIO32`；`pin4=IO2 / GPIO33`；`logic_level=MCU_P033`；`direction=GPIO32/GPIO33 configurable`
- 证据：图 81479376963d / 第 1 页 / 第1页左上：J1 GROVE pins1-4

### J2 主引出接口

J2 依次引出 EN、GPIO0、GPIO1、GPIO3、GPIO18、GPIO19、GPIO21、GPIO22、GPIO26、GPIO25、GPIO36、GPIO32、GPIO33、SYS_P050、MCU_P033 和 GND，器件标注 DNP。

- 参数与网络：`connector=J2 DNP`；`signals=EN,GPIO0,GPIO1,GPIO3,GPIO18,GPIO19,GPIO21,GPIO22,GPIO26,GPIO25,GPIO36,GPIO32,GPIO33`；`power=5V/SYS_P050; 3V3/MCU_P033; GND`；`logic_level=MCU_P033`；`direction=GPIO configurable; EN input`
- 证据：图 81479376963d / 第 1 页 / 第1页左中：J2 EN/G0/G1/G3/G18/G19/G21/G22/G26/G25/G36/G32/G33/5V/3V3/GND

## GPIO 与控制信号

### GPIO27 RGB LED

U2 IO27 pin16 形成 GPIO27并连接 LED1 SK6812_3535 DI；LED1 VDD 接 MCU_P033，GND 接地，DO 未连接。

- 参数与网络：`controller=U2 IO27 pin16 / GPIO27`；`data=GPIO27 -> LED1 DI`；`supply=LED1 VDD -> MCU_P033`；`ground=LED1 GND`；`data_out=LED1 DO NC`；`decoupling=C4 105/6.3V`
- 证据：图 81479376963d / 第 1 页 / 第1页 U2 IO27/GPIO27 与下部 LED1/C4

### GPIO39 用户按键

U2 IO39 pin8 形成 GPIO39；R3 5.1KΩ将 GPIO39 上拉到 MCU_P033，S1 按下时将 GPIO39 接地。

- 参数与网络：`gpio=U2 IO39 pin8 / GPIO39`；`switch=S1 SW`；`active_level=low`；`pullup=R3 5.1KΩ to MCU_P033`；`connection=GPIO39 -> S1 -> GND`
- 证据：图 81479376963d / 第 1 页 / 第1页 U2 IO39/GPIO39 与右下 R3/S1

### IO2 与 IO12 固定连接

U2 IO2 pin22 与 IO12 pin18 在图中连接同一接地网络。

- 参数与网络：`io2=U2 pin22 -> GND`；`io12=U2 pin18 -> GND`
- 证据：图 81479376963d / 第 1 页 / 第1页 U2 左侧 IO2 pin22、IO12 pin18 与外侧 GND 连线

### 外部 GPIO 映射

J1/J2 对外提供 GPIO0、GPIO1、GPIO3、GPIO18、GPIO19、GPIO21、GPIO22、GPIO25、GPIO26、GPIO32、GPIO33、GPIO36；GPIO27 与 GPIO39 分别在板上连接 RGB LED 和按键。

- 参数与网络：`external=GPIO0,GPIO1,GPIO3,GPIO18,GPIO19,GPIO21,GPIO22,GPIO25,GPIO26,GPIO32,GPIO33,GPIO36`；`onboard_rgb=GPIO27`；`onboard_button=GPIO39`；`connectors=J1,J2`
- 证据：图 81479376963d / 第 1 页 / 第1页 U2 GPIO labels、左侧 J1/J2、下部 LED1 与右下 S1

## 时钟

### 离散时钟可见性

本页原理图未画独立晶振、晶体或外部时钟输入器件，时钟连接未作为板级独立网络引出。

- 参数与网络：`discrete_crystal_shown=false`；`external_clock_connector_shown=false`；`soc_module=U2 PICO_D4`
- 证据：图 81479376963d / 第 1 页 / 第1页完整单页：仅 U2 PICO_D4，无 X/Y 晶体位号

## 复位

### EN 复位网络

U2 EN pin9 连接 EN 并引到 J2；R4 5.1KΩ从 MCU_P033 上拉 EN，C13 105/6.3V 从 EN 对地。

- 参数与网络：`soc_pin=U2 EN pin9`；`external_pin=J2 EN`；`pullup=R4 5.1KΩ to MCU_P033`；`capacitor=C13 105/6.3V to GND`
- 证据：图 81479376963d / 第 1 页 / 第1页 U2 EN/J2 EN 与右下 R4/C13

## 关键网络

### GPIO0 启动网络

U2 IO0 pin23 形成 GPIO0并引到 J2 G0；R5 5.1KΩ将 GPIO0 上拉到 MCU_P033。

- 参数与网络：`soc_pin=U2 IO0 pin23`；`net=GPIO0`；`external_pin=J2 G0`；`pullup=R5 5.1KΩ to MCU_P033`
- 证据：图 81479376963d / 第 1 页 / 第1页 U2 IO0/GPIO0、J2 G0 与右下 R5

## 内存与 Flash

### PICO_D4 集成存储可见性

U2 标为 PICO_D4，IO6/CLK、IO7/SD0、IO8/SD1、IO9/SD2、IO10/SD3、IO11/CMD pins28-33 未引到外部器件，原理图没有画独立 Flash 或 PSRAM。

- 参数与网络：`soc=U2 PICO_D4`；`memory_bus_pins=IO6/CLK,IO7/SD0,IO8/SD1,IO9/SD2,IO10/SD3,IO11/CMD`；`external_flash_shown=false`；`external_psram_shown=false`
- 证据：图 81479376963d / 第 1 页 / 第1页 U2 pins28-33 IO6/CLK 至 IO11/CMD

## 射频

### 3D 天线射频路径

U2 LNA_IN pin2 经 L2 0Ω串联连接 ANT1 五金3D天线；C5、C6 为匹配支路且图中值均标为 TBD。

- 参数与网络：`soc_pin=U2 LNA_IN pin2`；`series=L2 0Ω`；`antenna=ANT1 五金3D天线`；`matching_caps=C5 TBD; C6 TBD`
- 证据：图 81479376963d / 第 1 页 / 第1页顶部：U2 LNA_IN、L2/C5/C6、ANT1

## 调试与烧录

### UART0 引出

U2 IO1/U0TXD pin41 形成 GPIO1 并引到 J2 G1；U2 IO3/U0RXD pin40 形成 GPIO3 并引到 J2 G3。

- 参数与网络：`tx=U2 IO1/U0TXD pin41 -> GPIO1 -> J2 G1`；`rx=U2 IO3/U0RXD pin40 -> GPIO3 -> J2 G3`；`logic_level=MCU_P033`；`direction=U0TXD output; U0RXD input`
- 证据：图 81479376963d / 第 1 页 / 第1页 U2 IO1/U0TXD、IO3/U0RXD 与左侧 J2 G1/G3

### 外部下载所需网络

J2 同时引出 EN、GPIO0、GPIO1/U0TXD、GPIO3/U0RXD、5V、3.3V 和 GND；图中未画板载 USB-UART 桥或 USB 连接器。

- 参数与网络：`reset=J2 EN`；`boot=J2 G0/GPIO0`；`uart_tx=J2 G1/GPIO1/U0TXD`；`uart_rx=J2 G3/GPIO3/U0RXD`；`power=J2 5V/3V3/GND`；`usb_uart_bridge_shown=false`；`usb_connector_shown=false`
- 证据：图 81479376963d / 第 1 页 / 第1页左中 J2 与完整单页器件范围

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-Pico 架构 | `soc=U2 PICO_D4`；`power=U1 SY80079AAAC`；`antenna=ANT1 五金3D天线`；`rgb=LED1 SK6812_3535`；`button=S1 GPIO39`；`connectors=J1 GROVE; J2 DNP` |
| 电源 | SYS_P050 到 MCU_P033 | `converter=U1 SY80079AAAC`；`input=SYS_P050`；`enable=SYS_P050`；`switch_pin=U1 SW pin3`；`inductor=L1 2.20H`；`output=MCU_P033`；`feedback_top=R1 22KΩ/1%`；`feedback_bottom=R2 5.1KΩ/1%`；`input_cap=C1 226/10V`；`output_cap=C3 226/10V` |
| 电源 | 外部 5V/3.3V 电源接口 | `five_volt_inputs=J1 pin2 5V; J2 5V -> SYS_P050`；`three_volt_output=J2 3V3 -> MCU_P033`；`grounds=J1 pin1; J2 GND`；`logic_rail=MCU_P033` |
| 接口 | J1 GROVE 接口 | `connector=J1 GROVE`；`pin1=GND`；`pin2=5V / SYS_P050`；`pin3=IO1 / GPIO32`；`pin4=IO2 / GPIO33`；`logic_level=MCU_P033`；`direction=GPIO32/GPIO33 configurable` |
| 接口 | J2 主引出接口 | `connector=J2 DNP`；`signals=EN,GPIO0,GPIO1,GPIO3,GPIO18,GPIO19,GPIO21,GPIO22,GPIO26,GPIO25,GPIO36,GPIO32,GPIO33`；`power=5V/SYS_P050; 3V3/MCU_P033; GND`；`logic_level=MCU_P033`；`direction=GPIO configurable; EN input` |
| 调试与烧录 | UART0 引出 | `tx=U2 IO1/U0TXD pin41 -> GPIO1 -> J2 G1`；`rx=U2 IO3/U0RXD pin40 -> GPIO3 -> J2 G3`；`logic_level=MCU_P033`；`direction=U0TXD output; U0RXD input` |
| GPIO 与控制信号 | GPIO27 RGB LED | `controller=U2 IO27 pin16 / GPIO27`；`data=GPIO27 -> LED1 DI`；`supply=LED1 VDD -> MCU_P033`；`ground=LED1 GND`；`data_out=LED1 DO NC`；`decoupling=C4 105/6.3V` |
| GPIO 与控制信号 | GPIO39 用户按键 | `gpio=U2 IO39 pin8 / GPIO39`；`switch=S1 SW`；`active_level=low`；`pullup=R3 5.1KΩ to MCU_P033`；`connection=GPIO39 -> S1 -> GND` |
| 复位 | EN 复位网络 | `soc_pin=U2 EN pin9`；`external_pin=J2 EN`；`pullup=R4 5.1KΩ to MCU_P033`；`capacitor=C13 105/6.3V to GND` |
| 关键网络 | GPIO0 启动网络 | `soc_pin=U2 IO0 pin23`；`net=GPIO0`；`external_pin=J2 G0`；`pullup=R5 5.1KΩ to MCU_P033` |
| GPIO 与控制信号 | IO2 与 IO12 固定连接 | `io2=U2 pin22 -> GND`；`io12=U2 pin18 -> GND` |
| GPIO 与控制信号 | 外部 GPIO 映射 | `external=GPIO0,GPIO1,GPIO3,GPIO18,GPIO19,GPIO21,GPIO22,GPIO25,GPIO26,GPIO32,GPIO33,GPIO36`；`onboard_rgb=GPIO27`；`onboard_button=GPIO39`；`connectors=J1,J2` |
| 射频 | 3D 天线射频路径 | `soc_pin=U2 LNA_IN pin2`；`series=L2 0Ω`；`antenna=ANT1 五金3D天线`；`matching_caps=C5 TBD; C6 TBD` |
| 电源 | PICO_D4 电源域与去耦 | `rail=MCU_P033`；`domains=VDDA,VDDA3P3,VDD3P3,VDD3P3_RTC,VDD3P3_CPU,VDD_SDIO`；`bulk_cap=C7 226/6.3V`；`decoupling=C8/C9/C10/C11/C12/C14 105/6.3V`；`pad=U2 PAD pin0 -> GND` |
| 内存与 Flash | PICO_D4 集成存储可见性 | `soc=U2 PICO_D4`；`memory_bus_pins=IO6/CLK,IO7/SD0,IO8/SD1,IO9/SD2,IO10/SD3,IO11/CMD`；`external_flash_shown=false`；`external_psram_shown=false` |
| 内存与 Flash | 集成 Flash 容量 | `documented_capacity=4MB`；`schematic_part_number=PICO_D4`；`explicit_capacity_field_on_schematic=false` |
| 时钟 | 离散时钟可见性 | `discrete_crystal_shown=false`；`external_clock_connector_shown=false`；`soc_module=U2 PICO_D4` |
| 调试与烧录 | 外部下载所需网络 | `reset=J2 EN`；`boot=J2 G0/GPIO0`；`uart_tx=J2 G1/GPIO1/U0TXD`；`uart_rx=J2 G3/GPIO3/U0RXD`；`power=J2 5V/3V3/GND`；`usb_uart_bridge_shown=false`；`usb_connector_shown=false` |

## 待确认事项

- `memory.flash-capacity`：产品正文标称 4MB Flash；原理图只打印 U2 PICO_D4，没有独立容量字段。（证据：图 81479376963d / 第 1 页 / 第1页主控区：U2 PICO_D4 与 IO6/CLK-IO11/CMD）
- `review.flash-capacity`：C050-B 的 U2 PICO_D4 集成 Flash 容量是否应确认为 4MB？；原因：4MB 来自产品正文，原理图仅打印 PICO_D4 型号，没有独立容量字段。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `81479376963d1b7ac69231f718bbe2287d47d6a373437cba92c073bfa11365c5` | `https://static-cdn.m5stack.com/resource/docs/products/core/stamp_pico/stamp_pico_sch_01.webp` |

---

源文档：`zh_CN/core/stamp_pico.md`

源文档 SHA-256：`39046b557bca06d02609e5bf889ca33ced1239952edd4f502d89655b3cad85a6`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
