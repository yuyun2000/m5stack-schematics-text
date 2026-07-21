# Unit Joystick2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Joystick2 |
| SKU | U024-V2 |
| 产品 ID | `unit-joystick2-df80d35d1bae` |
| 源文档 | `zh_CN/unit/Unit-JoyStick2.md` |

## 概述

Unit Joystick2 以 U1 STM32G030F6P6 为主控，采集 J1 JH16 的 LEFT-SW-X、LEFT-SW-Y 模拟信号和 LEFT-SW-B 按键信号，并通过 RGB 网络驱动一颗 WS2812C。J2 HY-2.0_IIC 提供 SCL、SDA、5V 和 GND，PB8/PB9 分别连接 SCL/SDA，两线均以 10KΩ 上拉到 3V3。U2 HT7533 将 5V 转换为 3V3，为 MCU、摇杆和 LED 供电。P1 SWD_5p 引出 SWCLK、SWDIO、NRST、3V3 和 GND，板上还配置轴输入滤波、按钮上拉/滤波和 MCU 复位 RC。

## 检索关键词

`Unit Joystick2`、`U024-V2`、`STM32G030F6P6`、`JH16`、`HT7533`、`WS2812C`、`HY-2.0_IIC`、`SWD_5p`、`I2C`、`0x63`、`PB8_SCL`、`PB9_SDA`、`SCL`、`SDA`、`LEFT-SW-X`、`LEFT-SW-Y`、`LEFT-SW-B`、`PA0`、`PA1`、`PA2`、`PA4`、`RGB`、`SWCLK`、`SWDIO`、`NRST`、`3V3`、`5V`、`Hall joystick`、`16-bit ADC`、`64MHz`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G030F6P6 | 主控制器，采集摇杆三路输入、实现 I2C 通信并驱动 RGB LED | 图 eab10eb6fff0 / 第 1 页 / 第 1 页上中 U1，器件值 STM32G030F6P6 与 pins 1-20 |
| J1 | JH16 | X/Y 两轴输出与按键输出的摇杆组件 | 图 eab10eb6fff0 / 第 1 页 / 第 1 页左下 J1 JH16，VCC/X/Y/SW/GND/NC pins 1-8 |
| U2 | HT7533 | 5V 至 3V3 线性稳压器 | 图 eab10eb6fff0 / 第 1 页 / 第 1 页下中 U2 HT7533，VIN/VOUT/GND 与 5V/3V3 |
| J2 | HY-2.0_IIC | I2C 与 5V 电源 Grove 接口 | 图 eab10eb6fff0 / 第 1 页 / 第 1 页右下 J2 HY-2.0_IIC，pins 1-4 IIC_SCL/IIC_SDA/VCC/GND |
| LED1 | WS2812C | 由 RGB 网络控制的单颗串行 RGB LED | 图 eab10eb6fff0 / 第 1 页 / 第 1 页右上 LED1 WS2812C，DI/DO/VDD/GND pins 1-4 |
| P1 | SWD_5p | STM32 的五针 SWD 调试和复位接口 | 图 eab10eb6fff0 / 第 1 页 / 第 1 页右中 P1 SWD_5p，VCC/SWCLK/SWDIO/RST/GND |
| R2,C2 | 10KΩ / 1.0uF | NRST 的 3V3 上拉和对地复位电容 | 图 eab10eb6fff0 / 第 1 页 / 第 1 页左上 R2 10KΩ、NRST、C2 1.0uF、3V3/GND |
| R3,R4 | 10KΩ / 10KΩ | SCL 与 SDA 到 3V3 的 I2C 上拉电阻 | 图 eab10eb6fff0 / 第 1 页 / 第 1 页右下 R3/R4 10KΩ 分别连接 SCL/SDA 与 3V3 |
| R5,C6,C7,C8,C9 | 10KΩ / 100nF | 摇杆按键上拉和 X/Y/按键输入滤波网络 | 图 eab10eb6fff0 / 第 1 页 / 第 1 页左下 R5 10KΩ、C6-C9 100nF 与 LEFT-SW-X/Y/B |
| C1,C3,C4,C10,C11,C12,C13 | 100nF / 10uF / 100nF / 10uF / 100nF / 10uF / 100nF | RGB、MCU 和 HT7533 输入输出的去耦与储能电容 | 图 eab10eb6fff0 / 第 1 页 / 第 1 页 LED1 旁 C1、U1 旁 C3/C4、U2/J2 旁 C10-C13 |

## 系统结构

### Unit Joystick2 系统架构

U1 STM32G030F6P6 采集 J1 JH16 的 X/Y/按键三路，驱动 LED1 WS2812C，并通过 J2 I2C 与外部主机通信；U2 HT7533 从 5V 生成 3V3，P1 提供 SWD 调试。

- 参数与网络：`controller=U1 STM32G030F6P6`；`joystick=J1 JH16`；`host_bus=I2C via J2`；`rgb=LED1 WS2812C`；`regulator=U2 HT7533`；`debug=P1 SWD_5p`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页完整原理图，U1/J1/U2/J2/LED1/P1 功能分区

### 其他功能分区

本页未绘制独立协处理器、外部存储器、存储卡、音频、射频、额外传感器、电池或充电器；模拟采样由 U1 内部 ADC 对 LEFT-SW-X/Y 实现。

- 参数与网络：`coprocessor=false`；`external_memory=false`；`storage=false`；`audio=false`；`rf=false`；`additional_sensor=false`；`battery=false`；`charger=false`；`analog_frontend=J1 X/Y directly to U1 PA2/PA1 with capacitors`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页全部器件与功能分区

## 核心器件

### U1 外部引脚映射

U1 pin 1 PB7/PB8 接 PB8_SCL，pin 2 PB9/PC14-OSC32_IN 接 PB9_SDA，pin 4 VDD/VDDA 接 3V3，pin 5 VSS/VSSA 接 GND，pin 6 NRST，pins 7/8/9 PA0/PA1/PA2 分别接 LEFT-SW-B/Y/X，pin 11 PA4 接 RGB，pin 18 PA13 接 SWDIO，pin 19 PA15/PA14-BOOT0 接 SWCLK。

- 参数与网络：`i2c=pin 1 PB8_SCL,pin 2 PB9_SDA`；`power=pin 4 VDD/VDDA 3V3,pin 5 VSS/VSSA GND`；`reset=pin 6 NRST`；`joystick=pin 7 PA0 LEFT-SW-B,pin 8 PA1 LEFT-SW-Y,pin 9 PA2 LEFT-SW-X`；`rgb=pin 11 PA4 RGB`；`debug=pin 18 PA13 SWDIO,pin 19 PA14-BOOT0 SWCLK`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页上中 U1 pins 1-20 与周围网络名

## 电源

### 5V 至 3V3 稳压

J2 VCC pin 3 的 5V 网络连接 U2 HT7533 VIN pin 2，VOUT pin 3 输出 3V3，GND pin 1 接地。

- 参数与网络：`input=J2 pin 3 VCC/5V -> U2 pin 2 VIN`；`output=U2 pin 3 VOUT -> 3V3`；`ground=U2 pin 1`；`enable=null`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页下中 U2 HT7533 与右下 J2 5V/VCC 网络

### HT7533 输入输出滤波

U2 输出 3V3 侧由 C10 10uF 与 C11 100nF 对地，输入 5V 侧由 C12 10uF 与 C13 100nF 对地。

- 参数与网络：`output_caps=C10 10uF,C11 100nF`；`output_rail=3V3`；`input_caps=C12 10uF,C13 100nF`；`input_rail=5V`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页下中/右下 U2 两侧 C10-C13 与 3V3/5V/GND

### U1 供电与去耦

U1 VDD/VDDA pin 4 接 3V3，VSS/VSSA pin 5 接 GND；C3 10uF 和 C4 100nF 跨接 3V3 与 GND。

- 参数与网络：`supply_pin=U1 pin 4 VDD/VDDA`；`ground_pin=U1 pin 5 VSS/VSSA`；`rail=3V3`；`decoupling=C3 10uF,C4 100nF`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页左上/上中 U1 pins 4/5 与 C3/C4

### J1 摇杆供电

J1 VCC pin 1 接 3V3，GND pin 5 接地；J1 右侧标 NC 的 pins 6、7、8 连接公共 GND 节点。

- 参数与网络：`supply=J1 pin 1 VCC -> 3V3`；`ground=J1 pin 5 GND`；`nc_pads=J1 pins 6,7,8 marked NC and tied to GND`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页左下 J1 VCC/GND/NC pins 1,5-8 与 3V3/GND

## 接口

### J2 Grove I2C 接口

J2 pin 1 IIC_SCL 连接 SCL，pin 2 IIC_SDA 连接 SDA，pin 3 VCC 连接 5V，pin 4 GND 接地。

- 参数与网络：`connector=J2 HY-2.0_IIC`；`pinout=1:IIC_SCL/SCL,2:IIC_SDA/SDA,3:VCC/5V,4:GND`；`bus_level=3V3 pullups`；`direction=SCL/SDA bidirectional bus`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页右下 J2 HY-2.0_IIC pins 1-4 与 SCL/SDA/5V/GND

## 总线

### U1 与 J2 I2C

U1 PB8_SCL pin 1 连接 J2 SCL，PB9_SDA pin 2 连接 J2 SDA；SCL 通过 R3 10KΩ 上拉到 3V3，SDA 通过 R4 10KΩ 上拉到 3V3。

- 参数与网络：`device=U1`；`scl=U1 pin 1 PB8_SCL -> J2 pin 1`；`sda=U1 pin 2 PB9_SDA -> J2 pin 2`；`scl_pullup=R3 10K to 3V3`；`sda_pullup=R4 10K to 3V3`；`bus_voltage_v=3.3`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页 U1 pins 1/2 PB8_SCL/PB9_SDA 与右下 R3/R4/J2

## GPIO 与控制信号

### J1 按键信号

J1 SW pin 4 输出 LEFT-SW-B 并连接 U1 PA0 pin 7；R5 10KΩ 将该信号上拉到 3V3，C6 与 C9 均为 100nF 并接地滤波。

- 参数与网络：`path=J1 pin 4 SW/LEFT-SW-B -> U1 pin 7 PA0`；`pullup=R5 10K to 3V3`；`filter_capacitors=C6 100nF,C9 100nF to GND`；`direction=input`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页左下 J1 SW/LEFT-SW-B、R5/C6/C9 与上中 U1 PA0

### LED1 WS2812C

U1 PA4 pin 11 通过 RGB 网络连接 LED1 DI pin 3；LED1 VDD pin 4 接 3.3V，GND pin 2 接地，DO pin 1 未画后续连接，C1 100nF 跨接 3.3V/GND。

- 参数与网络：`controller_pin=U1 pin 11 PA4`；`data_net=RGB -> LED1 pin 3 DI`；`supply=LED1 pin 4 VDD -> 3.3V`；`ground=LED1 pin 2`；`data_output=pin 1 DO unconnected`；`decoupling=C1 100nF`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页 U1 PA4/RGB 与右上 LED1/C1

## 时钟

### U1 外部时钟

U1 PC15-OSC32_OUT pin 3 未连接，本页未绘制外部晶振或振荡器。

- 参数与网络：`oscillator_pin=U1 pin 3 PC15-OSC32_OUT unconnected`；`external_crystal=null`；`frequency=null`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页 U1 pin 3 PC15-OSC32_OUT 与整页无晶振器件

## 复位

### U1 NRST

U1 NRST pin 6 连接 NRST 网络，R2 10KΩ 将其上拉到 3.3V，C2 1.0uF 将其接地，P1 pin 4 也引出 NRST/RST。

- 参数与网络：`module_pin=U1 pin 6 NRST`；`pullup=R2 10K to 3.3V`；`capacitor=C2 1.0uF to GND`；`debug_pin=P1 pin 4 RST`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页左上 R2/C2/NRST、U1 pin 6 与右中 P1 pin 4

## 保护电路

### 接口与电源保护

本页未显示 J2、摇杆输入或电源路径的 TVS/ESD、保险丝、反接保护、过压保护或负载开关。

- 参数与网络：`tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`overvoltage_protection_visible=false`；`load_switch_visible=false`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页完整电源、J1/J2 和信号输入路径

## 调试与烧录

### P1 SWD 调试接口

P1 pin 1=VCC/3.3V、pin 2=SWCLK、pin 3=SWDIO、pin 4=RST/NRST、pin 5=GND；SWDIO 连接 U1 PA13 pin 18，SWCLK 连接 U1 PA14-BOOT0 pin 19。

- 参数与网络：`connector=P1 SWD_5p`；`pinout=1:3.3V,2:SWCLK,3:SWDIO,4:NRST,5:GND`；`swdio=U1 pin 18 PA13`；`swclk=U1 pin 19 PA14-BOOT0`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页上中 U1 PA13/PA14-BOOT0 与右中 P1 SWD_5p

## 模拟电路

### J1 X/Y 轴信号

J1 X pin 2 输出 LEFT-SW-X 并连接 U1 PA2 pin 9，J1 Y pin 3 输出 LEFT-SW-Y 并连接 U1 PA1 pin 8；LEFT-SW-X、LEFT-SW-Y 分别由 C7、C8 100nF 对地滤波。

- 参数与网络：`x_path=J1 pin 2 X/LEFT-SW-X -> U1 pin 9 PA2`；`y_path=J1 pin 3 Y/LEFT-SW-Y -> U1 pin 8 PA1`；`x_filter=C7 100nF to GND`；`y_filter=C8 100nF to GND`；`adc_resolution=null`
- 证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页左下 J1 X/Y、C7/C8 与上中 U1 PA2/PA1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Joystick2 系统架构 | `controller=U1 STM32G030F6P6`；`joystick=J1 JH16`；`host_bus=I2C via J2`；`rgb=LED1 WS2812C`；`regulator=U2 HT7533`；`debug=P1 SWD_5p` |
| 核心器件 | U1 外部引脚映射 | `i2c=pin 1 PB8_SCL,pin 2 PB9_SDA`；`power=pin 4 VDD/VDDA 3V3,pin 5 VSS/VSSA GND`；`reset=pin 6 NRST`；`joystick=pin 7 PA0 LEFT-SW-B,pin 8 PA1 LEFT-SW-Y,pin 9 PA2 LEFT-SW-X`；`rgb=pin 11 PA4 RGB`；`debug=pin 18 PA13 SWDIO,pin 19 PA14-BOOT0 SWCLK` |
| 电源 | 5V 至 3V3 稳压 | `input=J2 pin 3 VCC/5V -> U2 pin 2 VIN`；`output=U2 pin 3 VOUT -> 3V3`；`ground=U2 pin 1`；`enable=null` |
| 电源 | HT7533 输入输出滤波 | `output_caps=C10 10uF,C11 100nF`；`output_rail=3V3`；`input_caps=C12 10uF,C13 100nF`；`input_rail=5V` |
| 电源 | U1 供电与去耦 | `supply_pin=U1 pin 4 VDD/VDDA`；`ground_pin=U1 pin 5 VSS/VSSA`；`rail=3V3`；`decoupling=C3 10uF,C4 100nF` |
| 接口 | J2 Grove I2C 接口 | `connector=J2 HY-2.0_IIC`；`pinout=1:IIC_SCL/SCL,2:IIC_SDA/SDA,3:VCC/5V,4:GND`；`bus_level=3V3 pullups`；`direction=SCL/SDA bidirectional bus` |
| 总线 | U1 与 J2 I2C | `device=U1`；`scl=U1 pin 1 PB8_SCL -> J2 pin 1`；`sda=U1 pin 2 PB9_SDA -> J2 pin 2`；`scl_pullup=R3 10K to 3V3`；`sda_pullup=R4 10K to 3V3`；`bus_voltage_v=3.3` |
| 模拟电路 | J1 X/Y 轴信号 | `x_path=J1 pin 2 X/LEFT-SW-X -> U1 pin 9 PA2`；`y_path=J1 pin 3 Y/LEFT-SW-Y -> U1 pin 8 PA1`；`x_filter=C7 100nF to GND`；`y_filter=C8 100nF to GND`；`adc_resolution=null` |
| GPIO 与控制信号 | J1 按键信号 | `path=J1 pin 4 SW/LEFT-SW-B -> U1 pin 7 PA0`；`pullup=R5 10K to 3V3`；`filter_capacitors=C6 100nF,C9 100nF to GND`；`direction=input` |
| 电源 | J1 摇杆供电 | `supply=J1 pin 1 VCC -> 3V3`；`ground=J1 pin 5 GND`；`nc_pads=J1 pins 6,7,8 marked NC and tied to GND` |
| GPIO 与控制信号 | LED1 WS2812C | `controller_pin=U1 pin 11 PA4`；`data_net=RGB -> LED1 pin 3 DI`；`supply=LED1 pin 4 VDD -> 3.3V`；`ground=LED1 pin 2`；`data_output=pin 1 DO unconnected`；`decoupling=C1 100nF` |
| 复位 | U1 NRST | `module_pin=U1 pin 6 NRST`；`pullup=R2 10K to 3.3V`；`capacitor=C2 1.0uF to GND`；`debug_pin=P1 pin 4 RST` |
| 调试与烧录 | P1 SWD 调试接口 | `connector=P1 SWD_5p`；`pinout=1:3.3V,2:SWCLK,3:SWDIO,4:NRST,5:GND`；`swdio=U1 pin 18 PA13`；`swclk=U1 pin 19 PA14-BOOT0` |
| 时钟 | U1 外部时钟 | `oscillator_pin=U1 pin 3 PC15-OSC32_OUT unconnected`；`external_crystal=null`；`frequency=null` |
| 保护电路 | 接口与电源保护 | `tvs_esd_visible=false`；`fuse_visible=false`；`reverse_protection_visible=false`；`overvoltage_protection_visible=false`；`load_switch_visible=false` |
| 系统结构 | 其他功能分区 | `coprocessor=false`；`external_memory=false`；`storage=false`；`audio=false`；`rf=false`；`additional_sensor=false`；`battery=false`；`charger=false`；`analog_frontend=J1 X/Y directly to U1 PA2/PA1 with capacitors` |
| 总线地址 | I2C 从机地址 | `documented_address=0x63`；`schematic_address=null`；`address_straps=null` |
| 内存与 Flash | MCU 主频与存储容量 | `schematic_part_number=STM32G030F6P6`；`documented_frequency_mhz=64`；`documented_flash_kb=32`；`documented_sram_kb=8`；`external_clock=null` |
| 模拟电路 | X/Y 轴 16 位输出值 | `documented_output_bits=16`；`documented_min=0`；`documented_max=65535`；`schematic_adc_resolution=null`；`firmware_scaling=null` |
| 传感器 | 摇杆霍尔技术 | `schematic_part_number=JH16`；`documented_technology=Hall effect electromagnetic joystick`；`internal_sensor_model=null` |
| GPIO 与控制信号 | 正文与原理图 GPIO 映射差异 | `schematic_mapping=PA0:B,PA1:Y,PA2:X,PA4:RGB`；`documented_mapping=PA1:X,PA2:Y,PA3:B,PA4:RGB`；`confirmed_for_board=null` |

## 待确认事项

- `address.documented-i2c-address`：产品正文称 I2C 地址为 0x63，但原理图只显示 SCL/SDA 与 MCU，没有地址绑带或固件地址常量。（证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页 U1 PB8_SCL/PB9_SDA、R3/R4 与 J2 I2C 区域，无地址值）
- `memory.documented-controller-specs`：产品正文称 STM32G030F6P6 主频 64MHz、Flash 32KB、SRAM 8KB；原理图只确认芯片型号，没有频率或内部存储容量标注。（证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页 U1 型号标注与未展开内部存储/时钟）
- `analog.documented-output-range`：产品正文称 X/Y 轴通过 I2C 输出 0-65535 的 16 位 ADC 数值；原理图只确认模拟信号进入 PA2/PA1，没有 ADC 分辨率、缩放算法或输出寄存器定义。（证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页 J1 LEFT-SW-X/Y 至 U1 PA2/PA1 模拟路径，无位宽或寄存器文字）
- `sensor.documented-hall-joystick`：产品正文称 J1 为霍尔电磁摇杆；原理图只将器件值标为 JH16 并给出 VCC/X/Y/SW/GND 引脚，没有内部霍尔元件、磁体或传感器型号。（证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页左下 J1 JH16 外部引脚符号，未展开内部结构）
- `gpio.documented-map-conflict`：当前原理图明确为 PA0=LEFT-SW-B、PA1=LEFT-SW-Y、PA2=LEFT-SW-X、PA4=RGB；产品正文表格写 PA1=LEFT-SW-X、PA2=LEFT-SW-Y、PA3=LEFT-SW-B、PA4=RGB，两者对 X/Y/按键映射不一致。（证据：图 eab10eb6fff0 / 第 1 页 / 第 1 页 U1 pins 7-11 明确标注 PA0 LEFT-SW-B、PA1 LEFT-SW-Y、PA2 LEFT-SW-X、PA4 RGB）
- `review.i2c-address`：当前量产固件的 I2C 从机地址是否为 0x63？；原因：原理图没有地址绑带或固件常量。
- `review.controller-specs`：请用 STM32G030F6P6 当前订货型号和固件时钟配置确认 64MHz、32KB Flash、8KB SRAM。；原因：原理图只提供 MCU 型号，不包含内部存储和运行时钟配置。
- `review.axis-output-range`：0-65535 是否为固件缩放后的 16 位寄存器值，原始 ADC 位宽与校准方式是什么？；原因：原理图只能确认模拟输入脚，不能确认固件输出格式。
- `review.hall-joystick`：J1 JH16 的当前量产版本是否为霍尔电磁摇杆，内部传感器型号是什么？；原因：原理图没有展开 JH16 内部传感结构。
- `review.gpio-map-conflict`：量产 PCB 与固件应采用原理图 PA0/PA1/PA2 映射，还是正文 PA1/PA2/PA3 映射？；原因：当前原理图和产品正文对 X/Y/按键 GPIO 的直接标注冲突。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `eab10eb6fff047986983b4cb89cc73da1df5e1eb5a1df0bdced32c7deb2db26c` | `https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-JoyStick2/img-c9e7fc3b-846d-48c6-9813-7c834cbf1e61.png` |

---

源文档：`zh_CN/unit/Unit-JoyStick2.md`

源文档 SHA-256：`06243d6b21cb2cc95a14f8af448150ae51a0468be48ea578b0b96615934fa426`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
