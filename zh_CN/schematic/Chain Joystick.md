# Chain Joystick 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain Joystick |
| SKU | U205 |
| 产品 ID | `chain-joystick-0496041983c4` |
| 源文档 | `zh_CN/chain/Chain_Joystick.md` |

## 概述

Chain Joystick 以 U1 STM32G031G8U6 为主控，通过 J1 入口 UART1（PB6/PB7）和 J2 出口 UART2（PA2/PA3）形成定向 Chain 级联。J1/J2 的 VCC_5V 经 U2 ME6206A33XG 转换为 VCC_3V3，为 MCU、FPC 摇杆和 U4 WS2812C-2020 RGB LED 供电。FPC1 引出 VR1_YOUT、VR2_XOUT 和 BTN1，分别连接 PA6、PA7、PB0；板上还提供 J4 五针 SWD 调试接口与 NRST RC 网络。

## 检索关键词

`Chain Joystick`、`U205`、`STM32G031G8U6`、`ME6206A33XG`、`WS2812C-2020`、`Chain direction`、`UART1`、`UART2`、`TXD1`、`RXD1`、`TXD2`、`RXD2`、`PB6`、`PB7`、`PA2`、`PA3`、`PA6`、`PA7`、`PB0`、`PA8`、`VR1_YOUT`、`VR2_XOUT`、`BTN1`、`RGB`、`GROVE_IO`、`VCC_5V`、`VCC_3V3`、`FPC-6P 0.5mm`、`SWD_5P`、`MCU_SWCLK`、`MCU_SWDIO`、`NRST`、`PESD3V3S1UB`、`115200bps 8N1`、`Hall joystick`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | 读取摇杆三轴输入、驱动 RGB，并以两个 UART 实现 Chain 入口/出口通信的主控 | 图 82f87022244f / 第 1 页 / 第 1 页 B2-B3 MCU 区 U1 STM32G031G8U6，28 脚及 UART、摇杆、RGB、SWD 网络 |
| U2 | ME6206A33XG | 将 VCC_5V 转换为 VCC_3V3 的 LDO | 图 82f87022244f / 第 1 页 / 第 1 页 A3 LDO 区 U2 ME6206A33XG，pin3 VIN/VCC_5V、pin2 VOUT/VCC_3V3、pin1 GND |
| J1 | GROVE_IO | Chain IN 四针接口，引出 TXD1、RXD1、VCC_5V 与 GND | 图 82f87022244f / 第 1 页 / 第 1 页 A1 Chain direction IN 下方 J1 GROVE_IO，IO2/TXD1、IO1/RXD1、VCC_5V、GND |
| J2 | GROVE_IO | Chain OUT 四针接口，引出 RXD2、TXD2、VCC_5V 与 GND | 图 82f87022244f / 第 1 页 / 第 1 页 A2 Chain direction OUT 下方 J2 GROVE_IO，IO2/RXD2、IO1/TXD2、VCC_5V、GND |
| FPC1 | FPC-6P 0.5mm, Thickness 0.2mm | 连接摇杆组件的 YOUT、XOUT、按键、3.3V、GND 与屏蔽焊盘 | 图 82f87022244f / 第 1 页 / 第 1 页 C2 Joystick 区 FPC1，pin1 VR1_YOUT、pin2 VCC_3V3、pin3 GND、pin4 BTN1、pin5 VR2_XOUT、pin6 NC，7/8 接 GND |
| U4 | WS2812C-2020 | 由 MCU PA8/RGB 驱动的单颗可编程 RGB LED | 图 82f87022244f / 第 1 页 / 第 1 页 C3 RGB 区 U4 WS2812C-2020，DI/RGB、VDD/VCC_3V3、GND、DO |
| J4 | SWD_5P | 引出 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST 与 GND 的调试接口 | 图 82f87022244f / 第 1 页 / 第 1 页 B3 MCU 区右侧 J4 SWD_5P，pin1-pin5 五个网络 |
| R1,C4,D1 | 10KΩ / 100nF / PESD3V3S1UB | BTN1 按键上拉、滤波和 ESD 钳位网络 | 图 82f87022244f / 第 1 页 / 第 1 页 C1 Joystick 区 BTN1 节点，R1 10KΩ 到 VCC_3V3、C4 100nF 与 D1 PESD3V3S1UB 到 GND |
| R2,C1 | 10KΩ / 1uF | MCU NRST 上拉与复位电容网络 | 图 82f87022244f / 第 1 页 / 第 1 页 B1 MCU 左侧 NRST，R2 10KΩ 到 VCC_3V3、C1 1uF 到 GND |
| C2,C3 | 100nF / 10uF | STM32G031 VDD/VDDA 的 3.3V 去耦电容 | 图 82f87022244f / 第 1 页 / 第 1 页 B1-B2 U1 VDD/VDDA 旁 C2 100nF、C3 10uF 接 GND |
| C5,C7,C8 | 10uF / 100nF / 10uF | ME6206A33XG 输入和输出旁路电容 | 图 82f87022244f / 第 1 页 / 第 1 页 A3 U2 周围 C5 10uF 位于 VCC_5V，C7 100nF/C8 10uF 位于 VCC_3V3 |
| C12 | 100nF | WS2812C-2020 的 VCC_3V3 去耦电容 | 图 82f87022244f / 第 1 页 / 第 1 页 C3 U4 VDD 旁 C12 100nF 接 GND |

## 系统结构

### Chain Joystick 系统架构

U1 STM32G031G8U6 通过两个 UART 分别连接 Chain IN/OUT，采集 FPC1 的 YOUT/XOUT/BTN1 并驱动 U4 RGB；U2 将接口 5V 转换为全板 3.3V。

- 参数与网络：`mcu=U1 STM32G031G8U6`；`input_connector=J1 GROVE_IO`；`output_connector=J2 GROVE_IO`；`joystick=FPC1`；`rgb=U4 WS2812C-2020`；`ldo=U2 ME6206A33XG`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页完整单页：Chain direction、LDO、MCU、Joystick、RGB 五个分区

## 电源

### 5V 到 3.3V 稳压

U2 ME6206A33XG pin3 VIN 接 VCC_5V，pin2 VOUT 输出 VCC_3V3，pin1 GND 接 GND；C5 10uF 为输入旁路，C7 100nF 与 C8 10uF为输出旁路。

- 参数与网络：`input=U2 pin3 VCC_5V`；`output=U2 pin2 VCC_3V3`；`ground=U2 pin1 GND`；`input_capacitor=C5 10uF`；`output_capacitors=C7 100nF; C8 10uF`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 A3 LDO 区 U2/C5/C7/C8

### 电源轨分配

J1/J2 均引出 VCC_5V；VCC_3V3 为 U1 VDD/VDDA、FPC1 pin2、U4 VDD 和 J4 pin1 供电。

- 参数与网络：`five_volt_sources=J1 VCC; J2 VCC`；`three_volt_source=U2 VOUT`；`three_volt_consumers=U1 VDD/VDDA; FPC1 pin2; U4 pin4 VDD; J4 pin1`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页所有 VCC_5V/VCC_3V3 全局网络

## 接口

### J1 Chain IN 接口

J1 GROVE_IO 的 IO2 接 TXD1、IO1 接 RXD1，并提供 VCC_5V 和 GND；页面箭头将 J1 侧标为 Chain direction IN。

- 参数与网络：`io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`ground=GND`；`direction_label=IN`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 A1 J1 GROVE_IO 与上方 IN 箭头

### J2 Chain OUT 接口

J2 GROVE_IO 的 IO2 接 RXD2、IO1 接 TXD2，并提供 VCC_5V 和 GND；页面箭头将 J2 侧标为 Chain direction OUT。

- 参数与网络：`io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`ground=GND`；`direction_label=OUT`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 A2 J2 GROVE_IO 与上方 OUT 箭头

### FPC1 摇杆接口

FPC1 pin1=VR1_YOUT、pin2=VCC_3V3、pin3=GND、pin4=BTN1、pin5=VR2_XOUT、pin6 未连接，机械/屏蔽 pin7/pin8 接 GND。

- 参数与网络：`pin1=VR1_YOUT`；`pin2=VCC_3V3`；`pin3=GND`；`pin4=BTN1`；`pin5=VR2_XOUT`；`pin6=NC`；`pin7_pin8=GND`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 C2 FPC1 1-8 脚及左侧网络

## 总线

### UART1 与 Chain IN

U1 PB6 pin26 连接 TXD1/J1 IO2，PB7 pin27 连接 RXD1/J1 IO1。

- 参数与网络：`controller=U1 USART on PB6/PB7`；`tx=PB6 pin26 -> TXD1 -> J1 IO2`；`rx=PB7 pin27 -> RXD1 -> J1 IO1`；`connector=J1 Chain IN`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 U1 右上 PB6/TXD1、PB7/RXD1 与 J1 同名网络

### UART2 与 Chain OUT

U1 PA2 pin8 连接 TXD2/J2 IO1，PA3 pin9 连接 RXD2/J2 IO2。

- 参数与网络：`controller=U1 USART on PA2/PA3`；`tx=PA2 pin8 -> TXD2 -> J2 IO1`；`rx=PA3 pin9 -> RXD2 -> J2 IO2`；`connector=J2 Chain OUT`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 U1 左侧 PA2/TXD2、PA3/RXD2 与 J2 同名网络

### MCU SDA/SCL 标注

U1 PA12[PA10] pin19 标注 SDA、PA11[PA9] pin18 标注 SCL，但两条短引线均带未连接标记，当前页面没有 I2C 设备或连接器。

- 参数与网络：`sda=U1 pin19 PA12[PA10], NC`；`scl=U1 pin18 PA11[PA9], NC`；`i2c_device_shown=false`；`address_shown=false`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 U1 右侧 pin18 SCL/pin19 SDA 末端红色未连接标记

## GPIO 与控制信号

### 摇杆 Z 轴按键输入

FPC1 pin4 BTN1 连接 U1 PB0 pin14；R1 10KΩ 将 BTN1 上拉到 VCC_3V3，C4 100nF 与 D1 PESD3V3S1UB 从 BTN1 接 GND。

- 参数与网络：`connector_pin=FPC1 pin4`；`mcu_pin=U1 PB0 pin14`；`pullup=R1 10KΩ to VCC_3V3`；`filter=C4 100nF to GND`；`protection=D1 PESD3V3S1UB to GND`；`direction=digital input`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 C1-C2 BTN1/R1/C4/D1/FPC1 与 B2 U1 PB0

### WS2812C RGB 控制

U1 PA8 pin16 的 RGB 网络连接 U4 DI pin3；U4 VDD pin4 接 VCC_3V3，GND pin2 接 GND，DO pin1 未连接，C12 100nF 为去耦。

- 参数与网络：`mcu_pin=U1 PA8 pin16`；`data_net=RGB`；`led_input=U4 pin3 DI`；`supply=U4 pin4 VCC_3V3`；`ground=U4 pin2 GND`；`data_out=U4 pin1 DO NC`；`decoupling=C12 100nF`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 B2 U1 PA8/RGB 与 C3 U4 WS2812C-2020/C12

## 时钟

### MCU 外部时钟

U1 PC14-OSC32IN pin1 与 PC15-OSC32OUT pin2 在当前页面未连接，完整原理图未画出晶振或外部振荡器。

- 参数与网络：`osc32in=U1 pin1 NC`；`osc32out=U1 pin2 NC`；`crystal_shown=false`；`oscillator_shown=false`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 U1 pin1/pin2 PC14/PC15 短引线无网络，完整页面无晶振

## 复位

### STM32G031 复位网络

U1 PF2-NRST pin5 接 NRST，R2 10KΩ 上拉至 VCC_3V3，C1 1uF 接 GND；NRST 另接 J4 pin4。

- 参数与网络：`mcu_pin=U1 pin5 PF2-NRST`；`pullup=R2 10KΩ to VCC_3V3`；`capacitor=C1 1uF to GND`；`debug_pin=J4 pin4 NRST`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 B1 U1 NRST/R2/C1 与 B3 J4 pin4

## 保护电路

### BTN1 ESD 防护

D1 PESD3V3S1UB 从 BTN1 接 GND，对摇杆按键信号提供钳位；C4 100nF 同节点接 GND。

- 参数与网络：`device=D1 PESD3V3S1UB`；`protected_net=BTN1`；`return=GND`；`parallel_capacitor=C4 100nF`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 C1 BTN1 节点的 D1 与 C4

## 内存与 Flash

### 外部存储器

当前完整单页原理图未画出外部 Flash、EEPROM、RAM 或存储卡接口。

- 参数与网络：`external_flash_shown=false`；`eeprom_shown=false`；`external_ram_shown=false`；`memory_card_shown=false`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页完整单页器件，仅 MCU/LDO/RGB/FPC/连接器，无外部存储

## 调试与烧录

### 五针 SWD 调试接口

J4 SWD_5P pin1=VCC_3V3、pin2=MCU_SWCLK、pin3=MCU_SWDIO、pin4=NRST、pin5=GND；SWCLK 接 U1 PA14-BOOT0 pin21，SWDIO 接 PA13 pin20。

- 参数与网络：`pin1=VCC_3V3`；`pin2=MCU_SWCLK / U1 PA14-BOOT0 pin21`；`pin3=MCU_SWDIO / U1 PA13 pin20`；`pin4=NRST`；`pin5=GND`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 B3 J4 SWD_5P 与 U1 PA14/PA13/NRST

## 模拟电路

### 摇杆 Y 轴输入

FPC1 pin1 的 VR1_YOUT 连接 U1 PA6 pin12。

- 参数与网络：`connector_pin=FPC1 pin1`；`net=VR1_YOUT`；`mcu_pin=U1 PA6 pin12`；`direction=analog input to MCU`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 C2 FPC1 pin1 VR1_YOUT 与 B2 U1 PA6 pin12

### 摇杆 X 轴输入

FPC1 pin5 的 VR2_XOUT 连接 U1 PA7 pin13。

- 参数与网络：`connector_pin=FPC1 pin5`；`net=VR2_XOUT`；`mcu_pin=U1 PA7 pin13`；`direction=analog input to MCU`
- 证据：图 82f87022244f / 第 1 页 / 第 1 页 C2 FPC1 pin5 VR2_XOUT 与 B2 U1 PA7 pin13

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain Joystick 系统架构 | `mcu=U1 STM32G031G8U6`；`input_connector=J1 GROVE_IO`；`output_connector=J2 GROVE_IO`；`joystick=FPC1`；`rgb=U4 WS2812C-2020`；`ldo=U2 ME6206A33XG` |
| 电源 | 5V 到 3.3V 稳压 | `input=U2 pin3 VCC_5V`；`output=U2 pin2 VCC_3V3`；`ground=U2 pin1 GND`；`input_capacitor=C5 10uF`；`output_capacitors=C7 100nF; C8 10uF` |
| 电源 | 电源轨分配 | `five_volt_sources=J1 VCC; J2 VCC`；`three_volt_source=U2 VOUT`；`three_volt_consumers=U1 VDD/VDDA; FPC1 pin2; U4 pin4 VDD; J4 pin1` |
| 接口 | J1 Chain IN 接口 | `io2=TXD1`；`io1=RXD1`；`vcc=VCC_5V`；`ground=GND`；`direction_label=IN` |
| 接口 | J2 Chain OUT 接口 | `io2=RXD2`；`io1=TXD2`；`vcc=VCC_5V`；`ground=GND`；`direction_label=OUT` |
| 总线 | UART1 与 Chain IN | `controller=U1 USART on PB6/PB7`；`tx=PB6 pin26 -> TXD1 -> J1 IO2`；`rx=PB7 pin27 -> RXD1 -> J1 IO1`；`connector=J1 Chain IN` |
| 总线 | UART2 与 Chain OUT | `controller=U1 USART on PA2/PA3`；`tx=PA2 pin8 -> TXD2 -> J2 IO1`；`rx=PA3 pin9 -> RXD2 -> J2 IO2`；`connector=J2 Chain OUT` |
| 总线 | Chain UART 波特率与帧格式 | `documented_baud=115200`；`documented_format=8N1`；`schematic_rate_shown=false`；`schematic_format_shown=false` |
| 模拟电路 | 摇杆 Y 轴输入 | `connector_pin=FPC1 pin1`；`net=VR1_YOUT`；`mcu_pin=U1 PA6 pin12`；`direction=analog input to MCU` |
| 模拟电路 | 摇杆 X 轴输入 | `connector_pin=FPC1 pin5`；`net=VR2_XOUT`；`mcu_pin=U1 PA7 pin13`；`direction=analog input to MCU` |
| GPIO 与控制信号 | 摇杆 Z 轴按键输入 | `connector_pin=FPC1 pin4`；`mcu_pin=U1 PB0 pin14`；`pullup=R1 10KΩ to VCC_3V3`；`filter=C4 100nF to GND`；`protection=D1 PESD3V3S1UB to GND`；`direction=digital input` |
| 保护电路 | BTN1 ESD 防护 | `device=D1 PESD3V3S1UB`；`protected_net=BTN1`；`return=GND`；`parallel_capacitor=C4 100nF` |
| 传感器 | 摇杆霍尔传感器与组件身份 | `interface=FPC1`；`signals=VR1_YOUT, VR2_XOUT, BTN1`；`joystick_part_number_shown=false`；`hall_sensor_model_shown=false`；`output_range_shown=false` |
| 接口 | FPC1 摇杆接口 | `pin1=VR1_YOUT`；`pin2=VCC_3V3`；`pin3=GND`；`pin4=BTN1`；`pin5=VR2_XOUT`；`pin6=NC`；`pin7_pin8=GND` |
| GPIO 与控制信号 | WS2812C RGB 控制 | `mcu_pin=U1 PA8 pin16`；`data_net=RGB`；`led_input=U4 pin3 DI`；`supply=U4 pin4 VCC_3V3`；`ground=U4 pin2 GND`；`data_out=U4 pin1 DO NC`；`decoupling=C12 100nF` |
| 复位 | STM32G031 复位网络 | `mcu_pin=U1 pin5 PF2-NRST`；`pullup=R2 10KΩ to VCC_3V3`；`capacitor=C1 1uF to GND`；`debug_pin=J4 pin4 NRST` |
| 调试与烧录 | 五针 SWD 调试接口 | `pin1=VCC_3V3`；`pin2=MCU_SWCLK / U1 PA14-BOOT0 pin21`；`pin3=MCU_SWDIO / U1 PA13 pin20`；`pin4=NRST`；`pin5=GND` |
| 总线 | MCU SDA/SCL 标注 | `sda=U1 pin19 PA12[PA10], NC`；`scl=U1 pin18 PA11[PA9], NC`；`i2c_device_shown=false`；`address_shown=false` |
| 时钟 | MCU 外部时钟 | `osc32in=U1 pin1 NC`；`osc32out=U1 pin2 NC`；`crystal_shown=false`；`oscillator_shown=false` |
| 内存与 Flash | 外部存储器 | `external_flash_shown=false`；`eeprom_shown=false`；`external_ram_shown=false`；`memory_card_shown=false` |

## 待确认事项

- `bus.documented-uart-format`：产品正文标注 Chain UART 为 115200bps@8N1，但当前原理图只显示 TXD/RXD 连接，没有波特率、数据位、校验或停止位标注。（证据：图 82f87022244f / 第 1 页 / 第 1 页 J1/J2 与 U1 TXD1/RXD1/TXD2/RXD2，未见速率或帧格式）
- `sensor.joystick-element-identity`：产品正文描述为霍尔电磁摇杆，但当前原理图仅显示 FPC1 与 VR1_YOUT/VR2_XOUT/BTN1，没有摇杆组件料号、霍尔传感器型号、量程或输出电压范围。（证据：图 82f87022244f / 第 1 页 / 第 1 页 Joystick 区仅有 FPC1 和 BTN1 外围，未见霍尔传感器器件）
- `review.uart-format`：Chain Joystick 当前内置固件是否固定使用 115200bps、8N1，两个 UART 的协议时序与转发行为是否一致？；原因：速率和帧格式来自产品正文，原理图只能确认 TXD/RXD 物理映射。
- `review.joystick-element`：FPC1 所连霍尔摇杆的具体料号、X/Y 输出范围、中心值、线性度和 BTN1 电气结构是什么？；原因：当前原理图只显示 FPC 接口信号和按键外围，没有摇杆内部传感器或规格。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `82f87022244f3d2df4ee500034f38a01b9fe92fbbc0bcd68fd22eff0d7740ef3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1191/U205-SCH_Chain-Joystick_SCH_Main_V1.0_2025_09_29_23_34_52_page_01.png` |

---

源文档：`zh_CN/chain/Chain_Joystick.md`

源文档 SHA-256：`dc7f386c9e0476c49c14c0d4df0439596e2268e073ffd3633a205f1bbe8f4d6c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
