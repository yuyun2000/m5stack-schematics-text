# Unit ChainBus 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ChainBus |
| SKU | U212 |
| 产品 ID | `unit-chainbus-c02a3e614b6e` |
| 源文档 | `zh_CN/unit/Unit_ChainBus.md` |

## 概述

Unit ChainBus 以 U1 STM32G031G8U6 为主控，VCC_5V 经 U2 ME6211A33M3G 生成 VCC_3V3，并连接两路 Chain UART、一路多功能 Grove、SWD 和 WS2812C-2020 RGB LED。图面将左侧 IN/J1 接到 MCU UART2 的 TXD2/RXD2，将右侧 OUT/J2 接到 UART1 的 RXD1/TXD1；顶部 J3 的 SCL/IO、SDA/IO 分别接 MCU PA11[PA9]、PA12[PA10]，可选上拉 R3/R4 均标为 NC。源文档对 IN/OUT 的 UART1/UART2 编号与图面相反，而且级联协议、115200bps 8N1、扩展口 ADC/NVIC 能力、功耗和机械参数不在原理图内，均列为待确认。

## 检索关键词

`Unit ChainBus`、`U212`、`STM32G031G8U6`、`ME6211A33M3G`、`WS2812C-2020`、`Chain Bus`、`UART1`、`UART2`、`TXD1`、`RXD1`、`TXD2`、`RXD2`、`PA2`、`PA3`、`PB6`、`PB7`、`PA8`、`SCL/IO`、`SDA/IO`、`PA11`、`PA12`、`GROVE_IO`、`GROVE_4P`、`PORT.IN`、`PORT.OUT`、`Port.Ext`、`VCC_5V`、`VCC_3V3`、`MCU_SWCLK`、`MCU_SWDIO`、`NRST`、`SWD_5P`、`115200bps`、`8N1`、`RGB`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | Chain UART、扩展接口、SWD 与 RGB LED 的主控制器 | 图 710bb63a6494 / 第 1 页 / B2-C2 U1 STM32G031G8U6 pins1-28 |
| U2 | ME6211A33M3G | VCC_5V 到 VCC_3V3 的 LDO | 图 710bb63a6494 / 第 1 页 / A3 U2 ME6211A33M3G、VIN/VOUT/GND |
| U4 | WS2812C-2020 | 由 MCU RGB 网络驱动的 3.3V RGB LED | 图 710bb63a6494 / 第 1 页 / C3 U4 WS2812C-2020、DI RGB、VDD VCC_3V3 |
| J1 | GROVE_IO | 图面 Chain direction IN 一侧的 UART2 与 5V Grove 接口 | 图 710bb63a6494 / 第 1 页 / A1 J1 GROVE_IO，IO2 TXD2、IO1 RXD2、VCC_5V、GND |
| J2 | GROVE_IO | 图面 Chain direction OUT 一侧的 UART1 与 5V Grove 接口 | 图 710bb63a6494 / 第 1 页 / A2 J2 GROVE_IO，IO2 RXD1、IO1 TXD1、VCC_5V、GND |
| J3 | GROVE_4P | SCL/IO、SDA/IO、VCC_5V 与 GND 的顶部扩展接口 | 图 710bb63a6494 / 第 1 页 / B3 J3 GROVE_4P Port.Ext |
| J4 | SWD_5P | VCC_3V3、SWCLK、SWDIO、NRST 与 GND 调试接口 | 图 710bb63a6494 / 第 1 页 / C2 J4 SWD_5P pins1-5 |
| R2,C1 | 10K / 1uF | NRST 的 VCC_3V3 上拉与对地电容网络 | 图 710bb63a6494 / 第 1 页 / B1-C1 R2 10K、C1 1uF 与 NRST |
| R3,R4 | NC | SCL/IO 与 SDA/IO 到 VCC_3V3 的可选未装上拉位置 | 图 710bb63a6494 / 第 1 页 / B3 J3 上方 R3 NC、R4 NC 到 VCC_3V3 |

## 系统结构

### STM32G031G8U6 主控

U1 明确标为 STM32G031G8U6，VDD/VDDA 接 VCC_3V3、VSS/VSSA 接 GND，并引出两组 UART、扩展口、SWD、NRST 与 RGB 控制网络。

- 参数与网络：`mcu=STM32G031G8U6`；`supply=VCC_3V3`；`ground=VSS/VSSA`
- 证据：图 710bb63a6494 / 第 1 页 / B2-C2 U1 STM32G031G8U6

## 电源

### VCC_5V 到 VCC_3V3 LDO

U2 ME6211A33M3G 的 VIN pin3 接 VCC_5V，VOUT pin2 输出 VCC_3V3，GND pin1 接地。

- 参数与网络：`regulator=ME6211A33M3G`；`input=VCC_5V`；`output=VCC_3V3`
- 证据：图 710bb63a6494 / 第 1 页 / A3 U2 ME6211A33M3G pins1-3

### VCC_5V 与 VCC_3V3 对地电容

U2 输入侧 C5 10uF 跨接 VCC_5V 与 GND，输出侧 C7 100nF 和 C8 10uF 跨接 VCC_3V3 与 GND；U1 电源侧 C6 100nF、C3 10uF 跨接 VCC_3V3 与 GND。

- 参数与网络：`five_volt=C5=10uF`；`three_volt_ldo=C7=100nF,C8=10uF`；`three_volt_mcu=C6=100nF,C3=10uF`
- 证据：图 710bb63a6494 / 第 1 页 / A3 C5/C7/C8 与 B1 C6/C3

## 接口

### 左侧 IN 接口 J1

图面 Chain direction 的 IN 箭头位于左侧 J1 一侧；J1 IO2 接 TXD2、IO1 接 RXD2，VCC 接 VCC_5V，GND 接地。

- 参数与网络：`connector=J1 GROVE_IO`；`direction=IN`；`io2=TXD2`；`io1=RXD2`；`power=VCC_5V`；`ground=GND`
- 证据：图 710bb63a6494 / 第 1 页 / A1 IN 箭头与 J1 GROVE_IO

### 右侧 OUT 接口 J2

图面 Chain direction 的 OUT 箭头位于右侧 J2 一侧；J2 IO2 接 RXD1、IO1 接 TXD1，VCC 接 VCC_5V，GND 接地。

- 参数与网络：`connector=J2 GROVE_IO`；`direction=OUT`；`io2=RXD1`；`io1=TXD1`；`power=VCC_5V`；`ground=GND`
- 证据：图 710bb63a6494 / 第 1 页 / A2 OUT 箭头与 J2 GROVE_IO

### 顶部扩展接口 J3

J3 标为 GROVE_4P，四个网络依次标为 SCL、SDA、5V、GND；外部网络名分别为 SCL/IO、SDA/IO、VCC_5V 与 GND。

- 参数与网络：`connector=J3 GROVE_4P`；`signals=SCL/IO,SDA/IO`；`power=VCC_5V`；`ground=GND`
- 证据：图 710bb63a6494 / 第 1 页 / B3 J3 GROVE_4P Port.Ext

### WS2812C-2020 RGB LED

U4 标为 WS2812C-2020，VDD pin4 接 VCC_3V3、GND pin2 接地、DI pin3 接 RGB、DO pin1 未连接；RGB 网络连接 U1 PA8 pin16，C12 100nF 跨接 VCC_3V3 与 GND。

- 参数与网络：`led=WS2812C-2020`；`data_in=RGB -> U1 PA8 pin16`；`supply=VCC_3V3`；`capacitor=C12 100nF`；`data_out=not connected`
- 证据：图 710bb63a6494 / 第 1 页 / C3 U4 WS2812C-2020、C12 与 U1 PA8 RGB

## 总线

### MCU UART1 网络

U1 PB6 pin26 连接 TXD1，PB7 pin27 连接 RXD1；TXD1/RXD1 延伸到 J2 IO1/IO2。

- 参数与网络：`tx=PB6 pin26 -> TXD1 -> J2 IO1`；`rx=PB7 pin27 -> RXD1 -> J2 IO2`
- 证据：图 710bb63a6494 / 第 1 页 / U1 pins26-27 PB6/PB7 与 A2 J2 TXD1/RXD1

### MCU UART2 网络

U1 PA2 pin8 连接 TXD2，PA3 pin9 连接 RXD2；TXD2/RXD2 延伸到 J1 IO2/IO1。

- 参数与网络：`tx=PA2 pin8 -> TXD2 -> J1 IO2`；`rx=PA3 pin9 -> RXD2 -> J1 IO1`
- 证据：图 710bb63a6494 / 第 1 页 / U1 pins8-9 PA2/PA3 与 A1 J1 TXD2/RXD2

### 扩展接口可选上拉

SCL/IO 与 SDA/IO 上方各有到 VCC_3V3 的电阻位置 R3/R4，两者阻值均标为 NC。

- 参数与网络：`nets=SCL/IO,SDA/IO`；`pullups=R3=NC,R4=NC`；`rail=VCC_3V3`
- 证据：图 710bb63a6494 / 第 1 页 / B3 R3/R4 NC 与 VCC_3V3、SCL/IO、SDA/IO

## GPIO 与控制信号

### SCL/IO 与 SDA/IO 的 MCU 引脚

SCL/IO 连接 U1 PA11[PA9] pin18，SDA/IO 连接 U1 PA12[PA10] pin19。

- 参数与网络：`scl_io=U1 PA11[PA9] pin18`；`sda_io=U1 PA12[PA10] pin19`
- 证据：图 710bb63a6494 / 第 1 页 / U1 pins18-19 SCL/IO、SDA/IO 到 J3

## 时钟

### 外部 32kHz 振荡引脚

U1 PC14-OSC32IN pin1 与 PC15-OSC32OUT pin2 在本页没有绘制外部网络或晶体。

- 参数与网络：`osc_in=PC14-OSC32IN pin1`；`osc_out=PC15-OSC32OUT pin2`；`external_circuit=not drawn`
- 证据：图 710bb63a6494 / 第 1 页 / U1 pins1-2 PC14-OSC32IN/PC15-OSC32OUT 左侧无外部网络

## 复位

### MCU NRST 网络

U1 PF2-NRST pin5 连接 NRST；NRST 通过 R2 10K 接 VCC_3V3、通过 C1 1uF 接 GND，并引到 J4 pin4。

- 参数与网络：`mcu_pin=PF2-NRST pin5`；`pullup=R2 10K to VCC_3V3`；`capacitor=C1 1uF to GND`；`debug_pin=J4 pin4`
- 证据：图 710bb63a6494 / 第 1 页 / B1-C2 NRST、R2、C1、U1 pin5、J4 pin4

## 调试与烧录

### J4 五针 SWD 接口

J4 SWD_5P 的 pin1 接 VCC_3V3，pin2 接 MCU_SWCLK，pin3 接 MCU_SWDIO，pin4 接 NRST，pin5 接 GND；MCU_SWCLK 与 MCU_SWDIO 分别连接 U1 PA14-BOOT0 pin21 和 PA13 pin20。

- 参数与网络：`pin1=VCC_3V3`；`pin2=MCU_SWCLK`；`pin3=MCU_SWDIO`；`pin4=NRST`；`pin5=GND`；`mcu_debug=PA14-BOOT0 pin21,PA13 pin20`
- 证据：图 710bb63a6494 / 第 1 页 / C2 J4 SWD_5P 与 U1 pins20-21

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | STM32G031G8U6 主控 | `mcu=STM32G031G8U6`；`supply=VCC_3V3`；`ground=VSS/VSSA` |
| 电源 | VCC_5V 到 VCC_3V3 LDO | `regulator=ME6211A33M3G`；`input=VCC_5V`；`output=VCC_3V3` |
| 电源 | VCC_5V 与 VCC_3V3 对地电容 | `five_volt=C5=10uF`；`three_volt_ldo=C7=100nF,C8=10uF`；`three_volt_mcu=C6=100nF,C3=10uF` |
| 接口 | 左侧 IN 接口 J1 | `connector=J1 GROVE_IO`；`direction=IN`；`io2=TXD2`；`io1=RXD2`；`power=VCC_5V`；`ground=GND` |
| 接口 | 右侧 OUT 接口 J2 | `connector=J2 GROVE_IO`；`direction=OUT`；`io2=RXD1`；`io1=TXD1`；`power=VCC_5V`；`ground=GND` |
| 总线 | MCU UART1 网络 | `tx=PB6 pin26 -> TXD1 -> J2 IO1`；`rx=PB7 pin27 -> RXD1 -> J2 IO2` |
| 总线 | MCU UART2 网络 | `tx=PA2 pin8 -> TXD2 -> J1 IO2`；`rx=PA3 pin9 -> RXD2 -> J1 IO1` |
| 接口 | 顶部扩展接口 J3 | `connector=J3 GROVE_4P`；`signals=SCL/IO,SDA/IO`；`power=VCC_5V`；`ground=GND` |
| GPIO 与控制信号 | SCL/IO 与 SDA/IO 的 MCU 引脚 | `scl_io=U1 PA11[PA9] pin18`；`sda_io=U1 PA12[PA10] pin19` |
| 总线 | 扩展接口可选上拉 | `nets=SCL/IO,SDA/IO`；`pullups=R3=NC,R4=NC`；`rail=VCC_3V3` |
| 调试与烧录 | J4 五针 SWD 接口 | `pin1=VCC_3V3`；`pin2=MCU_SWCLK`；`pin3=MCU_SWDIO`；`pin4=NRST`；`pin5=GND`；`mcu_debug=PA14-BOOT0 pin21,PA13 pin20` |
| 复位 | MCU NRST 网络 | `mcu_pin=PF2-NRST pin5`；`pullup=R2 10K to VCC_3V3`；`capacitor=C1 1uF to GND`；`debug_pin=J4 pin4` |
| 时钟 | 外部 32kHz 振荡引脚 | `osc_in=PC14-OSC32IN pin1`；`osc_out=PC15-OSC32OUT pin2`；`external_circuit=not drawn` |
| 接口 | WS2812C-2020 RGB LED | `led=WS2812C-2020`；`data_in=RGB -> U1 PA8 pin16`；`supply=VCC_3V3`；`capacitor=C12 100nF`；`data_out=not connected` |
| 接口 | 源文档 PORT.IN/PORT.OUT 的 UART 编号 | `documented_in=UART1_RX,UART1_TX`；`documented_out=UART2_TX,UART2_RX`；`schematic_in=J1 TXD2,RXD2`；`schematic_out=J2 RXD1,TXD1` |
| 系统结构 | Chain Bus 级联协议与管理功能 | `documented_protocol=Chain Bus UART cascade`；`documented_functions=UID query,version query,device enumeration,heartbeat,peripheral control` |
| 接口 | 顶部扩展口 I2C/GPIO/ADC/NVIC 功能 | `documented_functions=I2C,GPIO input/output,ADC,NVIC interrupt`；`schematic_nets=SCL/IO,SDA/IO` |
| 总线 | UART 115200bps 8N1 参数 | `documented_baud=115200`；`documented_format=8N1` |
| 电源 | RGB 白光最大亮度功耗 | `documented_voltage_v=3.3`；`documented_current_ma=17.72`；`documented_condition=RGB white maximum brightness` |
| 系统结构 | 产品与包装机械参数 | `documented_product_size_mm=29.8x24.0x8.0`；`documented_product_weight_g=3.9`；`documented_package_size_mm=138.0x93.0x10.0`；`documented_gross_weight_g=8.7` |

## 待确认事项

- `interface.documented-chain-port-assignment`：源文档管脚表把 PORT.IN 标为 UART1_RX/UART1_TX、PORT.OUT 标为 UART2_TX/UART2_RX；原理图却把 IN/J1 接到 TXD2/RXD2，把 OUT/J2 接到 RXD1/TXD1，两者的 UART1/UART2 端口编号相反。（证据：图 710bb63a6494 / 第 1 页 / A1-A2 Chain direction IN/OUT、J1 TXD2/RXD2、J2 RXD1/TXD1）
- `system.documented-chain-protocol`：源文档称内置固件支持 UART 链式连接、UID 查询、版本查询、链路设备枚举、心跳包和多种外设统一控制；原理图只显示硬件网络，未包含协议帧、固件版本或这些运行行为。（证据：图 710bb63a6494 / 第 1 页 / U1 与 J1/J2 硬件图，无固件和协议帧）
- `interface.documented-extension-capabilities`：源文档称顶部接口支持 I2C 控制、GPIO 输入输出、ADC 采集以及 NVIC 中断配置和状态查询；原理图只能确认 SCL/IO、SDA/IO 到 U1 pin18/pin19 的连接，未给出固件配置、ADC 通道或中断行为。（证据：图 710bb63a6494 / 第 1 页 / B3 J3 与 U1 pins18-19，仅标 SCL/IO、SDA/IO）
- `bus.documented-uart-format`：源文档规格表将通信接口写为 UART 115200bps @ 8N1；原理图只确认 UART 网络与 MCU 引脚，不包含波特率、数据位、校验位或停止位设置。（证据：图 710bb63a6494 / 第 1 页 / U1 UART1/UART2 与 J1/J2 网络，无串口时序参数）
- `power.documented-rgb-consumption`：源文档称 RGB 白光最大亮度时工作功耗为 3.3V@17.72mA；原理图只显示 U4 的 VCC_3V3 供电和 C12，没有电流测量条件或亮度设置。（证据：图 710bb63a6494 / 第 1 页 / C3 U4 WS2812C-2020 与 VCC_3V3，无电流测量）
- `system.documented-mechanical`：源文档称产品尺寸 29.8x24.0x8.0mm、重量 3.9g，包装尺寸 138.0x93.0x10.0mm、毛重 8.7g；当前电气原理图没有板框、外壳、机械公差或质量信息。（证据：图 710bb63a6494 / 第 1 页 / 电气原理图无板框、外壳与机械尺寸）
- `review.chain-port-assignment`：确认当前 U212 硬件和固件中 PORT.IN/PORT.OUT 分别对应 UART1 还是 UART2；原因：源文档管脚表与正式原理图的 UART1/UART2 端口编号相反。
- `review.chain-protocol`：确认量产固件版本、Chain Bus 协议帧及 UID、版本、枚举、心跳功能；原因：这些功能由固件与协议定义，原理图不能确认。
- `review.extension-capabilities`：确认 J3 的 I2C、GPIO、ADC 通道和 NVIC 中断配置在当前固件中的完整映射；原因：图面只给出 SCL/IO、SDA/IO 网络，没有软件功能和 ADC/中断配置。
- `review.uart-format`：确认 Chain Bus UART 的默认 115200bps 8N1 设置及可配置范围；原因：原理图不包含串口时序参数。
- `review.rgb-consumption`：确认 RGB 白光最大亮度 3.3V@17.72mA 的测试条件和量产容差；原因：原理图没有电流测量和亮度设置。
- `review.mechanical`：确认 29.8x24.0x8.0mm 外形、3.9g 重量与当前量产配置；原因：当前电气原理图没有机械与质量信息。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `710bb63a6494423c15a1fc600013e8c753830812d5e3b92b95ba2c2ebd01b0b7` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1201/SCH_ChainBus_SCH_Main_V1.0_20250704_2025_11_28_11_09_00_page_01.png` |

---

源文档：`zh_CN/unit/Unit_ChainBus.md`

源文档 SHA-256：`e54e76b70903b210b1069438daa63b6177dcb6351461925b05963ebd6d1f8e6d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
