# Chain ToF 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Chain ToF |
| SKU | U209 |
| 产品 ID | `chain-tof-93d363be2dba` |
| 源文档 | `zh_CN/chain/Chain_ToF.md` |

## 概述

Chain ToF V1.0 以 U1 STM32G031G8U6 为主控，两组 GROVE_IO 分别连接 USART1 与 USART2，图面 IN/OUT 箭头定义链式方向。VCC_5V 经 U2 ME6206A33XG 生成 VCC_3V3，为 MCU、U3 VL53L0CXV0DH/1 ToF 模组和 U4 WS2812C-2020 RGB LED 供电。ToF 通过 PA11/PA12 I2C 连接 MCU，XSHUT 与 GPIO1 仅由 10K 上拉；PA8 的 RGB 网络驱动 WS2812C，另有 J4 五针 SWD/复位接口。

## 检索关键词

`Chain ToF`、`U209`、`STM32G031G8U6`、`VL53L0CXV0DH/1`、`VL53L0C`、`ME6206A33XG`、`WS2812C-2020`、`USART1`、`USART2`、`TXD1`、`RXD1`、`TXD2`、`RXD2`、`PB6`、`PB7`、`PA2`、`PA3`、`PA11`、`PA12`、`PA8`、`I2C_SCL`、`I2C_SDA`、`XSHUT`、`GPIO1`、`RGB`、`VCC_5V`、`VCC_3V3`、`SWDIO`、`SWCLK`、`NRST`、`GROVE_IO`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | 主控 MCU，处理双 UART Chain 通信、ToF I2C、RGB LED 与 SWD 调试 | 图 8a701e95b7c4 / 第 1 页 / 网格 B1-C3，U1 STM32G031G8U6 全部 PA/PB/SWD/RST/电源引脚 |
| U2 | ME6206A33XG | VCC_5V 至 VCC_3V3 的 LDO | 图 8a701e95b7c4 / 第 1 页 / 网格 A3-B3，U2 ME6206A33XG，VIN/VOUT/GND 与 C5-C8 |
| U3 | VL53L0CXV0DH/1 | 激光飞行时间测距传感器，通过 I2C_SCL/I2C_SDA 连接 MCU | 图 8a701e95b7c4 / 第 1 页 / 网格 C1-D3，U3 VL53L0CXV0DH/1，XSHUT/GPIO1/SDA/SCL/AVDD/GND |
| U4 | WS2812C-2020 | 单颗可编程 RGB LED，由 PA8/RGB 数据驱动 | 图 8a701e95b7c4 / 第 1 页 / 网格 C2-D3，U4 WS2812C-2020，DO/GND/DIN/VDD |
| J1 | GROVE_IO | Chain 输入四针接口，提供 TXD1、RXD1、VCC_5V、GND | 图 8a701e95b7c4 / 第 1 页 / 网格 A1-A2，J1 GROVE_IO 与 IN 箭头 |
| J2 | GROVE_IO | Chain 输出四针接口，提供 RXD2、TXD2、VCC_5V、GND | 图 8a701e95b7c4 / 第 1 页 / 网格 A2-A3，J2 GROVE_IO 与 OUT 箭头 |
| J4 | SWD_5P | 3.3V、SWCLK、SWDIO、NRST、GND 调试/烧录接口 | 图 8a701e95b7c4 / 第 1 页 / 网格 B3，J4 SWD_5P pins1-5 |
| R4,R5 | 4.7KΩ | ToF I2C_SCL/I2C_SDA 到 VCC_3V3 的上拉电阻 | 图 8a701e95b7c4 / 第 1 页 / 网格 C1-D2，R4/R5 4.7K 从 I2C 网络到 VCC_3V3 |
| R1,R3 | 10KΩ | VL53L0C XSHUT 与 GPIO1 的 3.3V 上拉电阻 | 图 8a701e95b7c4 / 第 1 页 / 网格 C1-D2，R1/R3 10K 上拉 U3 XSHUT/GPIO1 |

## 系统结构

### Chain ToF 系统架构

系统由 STM32G031G8U6、双 UART Chain 接口、ME6206A33XG LDO、VL53L0C ToF 传感器、WS2812C RGB 与 SWD 接口组成。

- 参数与网络：`mcu=U1 STM32G031G8U6`；`chain_ports=J1,J2`；`regulator=U2 ME6206A33XG`；`tof=U3 VL53L0CXV0DH/1`；`rgb=U4 WS2812C-2020`；`debug=J4 SWD_5P`
- 证据：图 8a701e95b7c4 / 第 1 页 / 整页 Chain ToF 各功能分区

### Chain 通信方向

图面 Chain direction 从 J1 IN 指向 J2 OUT；两端分别接 MCU 不同 USART，信号不直接贯通。

- 参数与网络：`input=J1 USART1`；`output=J2 USART2`；`direction=J1 -> J2`；`direct_pass_through=false`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 A1-A3，Chain direction IN/OUT 箭头与 J1/J2

## 核心器件

### STM32G031G8U6 主控

U1 明确标为 STM32G031G8U6，使用 PB6/PB7 与 PA2/PA3 两组 UART、PA11/PA12 I2C、PA8 RGB、PA13/PA14 SWD 和 PF2 NRST。

- 参数与网络：`reference=U1`；`part_number=STM32G031G8U6`；`uart1=PB6/PB7`；`uart2=PA2/PA3`；`i2c=PA11 SCL,PA12 SDA`；`rgb=PA8`；`swd=PA13/PA14`；`reset=PF2`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 B1-C3，U1 网络标注

### WS2812C-2020 RGB LED

U4 明确标为 WS2812C-2020，VDD pin4 接 VCC_3V3，DIN pin3 接 RGB，GND pin2 接地，DO pin1 未连接；C12 100nF 去耦。

- 参数与网络：`reference=U4`；`part_number=WS2812C-2020`；`vdd=pin4 VCC_3V3`；`din=pin3 RGB`；`gnd=pin2`；`dout=pin1 NC`；`decoupling=C12 100nF`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 C2-D3，RGB 分区 U4/C12

## 电源

### 5V 到 3.3V LDO

U2 ME6206A33XG 的 VIN pin3 接 VCC_5V，VOUT pin2 生成 VCC_3V3，GND pin1 接地；输入 C6 100nF/C5 10uF，输出 C7 100nF/C8 10uF。

- 参数与网络：`regulator=U2 ME6206A33XG`；`input=pin3 VCC_5V`；`output=pin2 VCC_3V3`；`ground=pin1`；`input_caps=C6 100nF,C5 10uF`；`output_caps=C7 100nF,C8 10uF`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 A3-B3，LDO 分区 U2/C5-C8

### VCC_5V 与 VCC_3V3 分配

VCC_5V 在 J1/J2 VCC 间直通并供 U2 输入；VCC_3V3 供给 U1、U3、U4、J4 与全部上拉/去耦。

- 参数与网络：`5v=J1/J2 VCC and U2 VIN`；`3v3=U2 VOUT`；`3v3_loads=U1,U3,U4,J4,R1,R3,R4,R5`
- 证据：图 8a701e95b7c4 / 第 1 页 / 整页 VCC_5V/VCC_3V3 网络

### ToF 电源去耦

U3 AVDD 接 VCC_3V3，C4 10uF 与 C9 100nF 从该电源节点对地去耦。

- 参数与网络：`rail=VCC_3V3`；`device=U3`；`bulk_cap=C4 10uF`；`hf_cap=C9 100nF`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 C1-D2，U3 AVDD 与 C4/C9

## 接口

### J1 Chain 输入接口

J1 GROVE_IO pin1 IO2=TXD1、pin2 IO1=RXD1、pin3 VCC=VCC_5V、pin4 GND；上方箭头标为 IN。

- 参数与网络：`reference=J1`；`pin1=IO2/TXD1`；`pin2=IO1/RXD1`；`pin3=VCC/VCC_5V`；`pin4=GND`；`role_mark=IN`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 A1-A2，J1 与 IN 箭头

### J2 Chain 输出接口

J2 GROVE_IO pin1 IO2=RXD2、pin2 IO1=TXD2、pin3 VCC=VCC_5V、pin4 GND；上方箭头标为 OUT。

- 参数与网络：`reference=J2`；`pin1=IO2/RXD2`；`pin2=IO1/TXD2`；`pin3=VCC/VCC_5V`；`pin4=GND`；`role_mark=OUT`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 A2-A3，J2 与 OUT 箭头

## 总线

### USART1 与 J1 输入接口

U1 PB6 pin26 输出 TXD1 到 J1 IO2，PB7 pin27 接收 RXD1 自 J1 IO1。

- 参数与网络：`controller=U1 STM32G031G8U6`；`tx=PB6 pin26/TXD1 -> J1 IO2`；`rx=J1 IO1/RXD1 -> PB7 pin27`；`connector=J1`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 A1-C3，J1 TXD1/RXD1 到 U1 PB6/PB7

### USART2 与 J2 输出接口

U1 PA2 pin8 输出 TXD2 到 J2 IO1，PA3 pin9 接收 RXD2 自 J2 IO2。

- 参数与网络：`controller=U1 STM32G031G8U6`；`tx=PA2 pin8/TXD2 -> J2 IO1`；`rx=J2 IO2/RXD2 -> PA3 pin9`；`connector=J2`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 A2-C2，J2 TXD2/RXD2 到 U1 PA2/PA3

### MCU 到 ToF I2C

U1 PA11 pin18 连接 I2C_SCL 到 U3 pin10，PA12 pin19 连接 I2C_SDA 到 U3 pin9；R4/R5 各 4.7K 将两线拉到 VCC_3V3。

- 参数与网络：`controller_scl=U1 PA11 pin18`；`device_scl=U3 pin10`；`controller_sda=U1 PA12 pin19`；`device_sda=U3 pin9`；`pullups=R4,R5 4.7K to VCC_3V3`；`level=3.3V`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 B2-D2，U1 PA11/PA12、R4/R5 与 U3 SCL/SDA

## GPIO 与控制信号

### ToF XSHUT 与 GPIO1

U3 XSHUT pin5 经 R1 10K 上拉至 VCC_3V3，GPIO1 pin7 经 R3 10K 上拉至 VCC_3V3；两脚均未连接 MCU GPIO，DNC pin8 未连接。

- 参数与网络：`xshut=U3 pin5,R1 10K pull-up`；`gpio1=U3 pin7,R3 10K pull-up`；`mcu_control=null`；`dnc=pin8 NC`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 C1-D2，U3 XSHUT/GPIO1/DNC 与 R1/R3

### RGB 数据 GPIO

U1 PA8 pin16 的 RGB 网络直接连接 U4 DIN pin3。

- 参数与网络：`controller=U1 PA8 pin16`；`net=RGB`；`target=U4 pin3 DIN`；`level=3.3V domain`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 B2-D3，U1 PA8/RGB 到 U4 DIN

## 时钟

### MCU 时钟

U1 PC14-OSC32IN pin1 与 PC15-OSC32OUT pin2 未连接，板上没有晶振或独立振荡器。

- 参数与网络：`pc14=pin1 NC`；`pc15=pin2 NC`；`crystal=null`；`oscillator=null`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 B2，U1 pins1/2 PC14/PC15 无外部网络

## 复位

### STM32 复位网络

U1 PF2-NRST pin5 连接 NRST 与 J4 pin4，R2 10K 上拉到 VCC_3V3，C1 1uF 对地。

- 参数与网络：`target=U1 pin5 PF2-NRST`；`debug_pin=J4 pin4`；`pullup=R2 10K`；`capacitor=C1 1uF`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 B1-B3，NRST/R2/C1/U1/J4

## 保护电路

### 外部接口保护

J1/J2 与 VCC_5V 输入在本页未显示 ESD/TVS、保险丝、反接或过压保护器件。

- 参数与网络：`esd_tvs=null`；`fuse=null`；`reverse_protection=null`；`ovp=null`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 A1-B3，J1/J2/VCC_5V/LDO 无保护器件

## 关键网络

### 通信、测距与指示关键路径

J1 -> USART1 -> MCU -> USART2 -> J2 构成 Chain 通信；MCU PA11/PA12 -> I2C -> U3 构成测距控制；MCU PA8 -> RGB -> U4 构成状态指示。

- 参数与网络：`chain=J1 USART1 -> U1 -> USART2 J2`；`tof=U1 PA11/PA12 -> U3 SCL/SDA`；`rgb=U1 PA8 -> U4 DIN`
- 证据：图 8a701e95b7c4 / 第 1 页 / 整页 J1/J2/U1/U3/U4 网络追踪

## 存储

### 外部存储

原理图没有外部 Flash、EEPROM、eMMC 或存储卡；STM32 内部 Flash 容量未在图中标注。

- 参数与网络：`external_flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null`；`internal_flash_capacity=null`
- 证据：图 8a701e95b7c4 / 第 1 页 / 整页无外部存储器件

## 内存与 Flash

### 外部内存

原理图没有外部 RAM、PSRAM 或 DDR；STM32 内部 RAM 容量未在图中标注。

- 参数与网络：`external_ram=null`；`psram=null`；`ddr=null`；`internal_ram_capacity=null`
- 证据：图 8a701e95b7c4 / 第 1 页 / 整页无外部内存器件

## 音频

### 音频电路

原理图没有音频编解码器、麦克风、扬声器或 I2S 网络。

- 参数与网络：`codec=null`；`microphone=null`；`speaker=null`；`i2s=null`
- 证据：图 8a701e95b7c4 / 第 1 页 / 整页无音频器件或网络

## 传感器

### VL53L0C ToF 传感器

U3 标为 VL53L0CXV0DH/1，AVDD pins1/11 接 VCC_3V3，SCL pin10 接 I2C_SCL，SDA pin9 接 I2C_SDA，多个 GND 引脚接地。

- 参数与网络：`reference=U3`；`part_number=VL53L0CXV0DH/1`；`supply=pins1,11 AVDD VCC_3V3`；`scl=pin10 I2C_SCL`；`sda=pin9 I2C_SDA`；`ground=pins2,3,4,6,12`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 C1-D3，U3 ToF 全部引脚

## 射频

### 射频通信电路

除 VL53L0C 内部光学测距功能外，原理图没有射频收发器、天线或射频匹配网络。

- 参数与网络：`rf_transceiver=null`；`antenna=null`；`matching=null`；`optical_sensor=U3 VL53L0C`
- 证据：图 8a701e95b7c4 / 第 1 页 / 整页无 RF/ANT 器件

## 调试与烧录

### J4 SWD 调试接口

J4 SWD_5P pin1 为 VCC_3V3、pin2 MCU_SWCLK、pin3 MCU_SWDIO、pin4 NRST、pin5 GND；SWCLK/SWDIO 分别连接 U1 PA14/PA13。

- 参数与网络：`reference=J4`；`pin1=VCC_3V3`；`pin2=MCU_SWCLK/U1 PA14`；`pin3=MCU_SWDIO/U1 PA13`；`pin4=NRST`；`pin5=GND`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 B3，J4 SWD_5P 与 U1 PA13/PA14

## 模拟电路

### ToF I2C 上拉网络

I2C_SCL 与 I2C_SDA 分别使用 R4/R5 4.7K 上拉到 VCC_3V3，没有额外电平转换器或滤波器。

- 参数与网络：`scl_pullup=R4/R5 one of pair 4.7K`；`sda_pullup=R4/R5 one of pair 4.7K`；`rail=VCC_3V3`；`level_shifter=null`；`filter=null`
- 证据：图 8a701e95b7c4 / 第 1 页 / 网格 C1-D2，R4/R5 与 I2C_SDA/I2C_SCL

## 其他事实

### 电池与充电路径

板上没有电池、充电器或电量监测器，电源来自 Chain 接口 VCC_5V。

- 参数与网络：`battery=null`；`charger=null`；`fuel_gauge=null`；`input=VCC_5V`
- 证据：图 8a701e95b7c4 / 第 1 页 / 整页电源路径仅 J1/J2 VCC_5V 与 U2 LDO

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Chain ToF 系统架构 | `mcu=U1 STM32G031G8U6`；`chain_ports=J1,J2`；`regulator=U2 ME6206A33XG`；`tof=U3 VL53L0CXV0DH/1`；`rgb=U4 WS2812C-2020`；`debug=J4 SWD_5P` |
| 核心器件 | STM32G031G8U6 主控 | `reference=U1`；`part_number=STM32G031G8U6`；`uart1=PB6/PB7`；`uart2=PA2/PA3`；`i2c=PA11 SCL,PA12 SDA`；`rgb=PA8`；`swd=PA13/PA14`；`reset=PF2` |
| 电源 | 5V 到 3.3V LDO | `regulator=U2 ME6206A33XG`；`input=pin3 VCC_5V`；`output=pin2 VCC_3V3`；`ground=pin1`；`input_caps=C6 100nF,C5 10uF`；`output_caps=C7 100nF,C8 10uF` |
| 电源 | VCC_5V 与 VCC_3V3 分配 | `5v=J1/J2 VCC and U2 VIN`；`3v3=U2 VOUT`；`3v3_loads=U1,U3,U4,J4,R1,R3,R4,R5` |
| 总线 | USART1 与 J1 输入接口 | `controller=U1 STM32G031G8U6`；`tx=PB6 pin26/TXD1 -> J1 IO2`；`rx=J1 IO1/RXD1 -> PB7 pin27`；`connector=J1` |
| 总线 | USART2 与 J2 输出接口 | `controller=U1 STM32G031G8U6`；`tx=PA2 pin8/TXD2 -> J2 IO1`；`rx=J2 IO2/RXD2 -> PA3 pin9`；`connector=J2` |
| 接口 | J1 Chain 输入接口 | `reference=J1`；`pin1=IO2/TXD1`；`pin2=IO1/RXD1`；`pin3=VCC/VCC_5V`；`pin4=GND`；`role_mark=IN` |
| 接口 | J2 Chain 输出接口 | `reference=J2`；`pin1=IO2/RXD2`；`pin2=IO1/TXD2`；`pin3=VCC/VCC_5V`；`pin4=GND`；`role_mark=OUT` |
| 系统结构 | Chain 通信方向 | `input=J1 USART1`；`output=J2 USART2`；`direction=J1 -> J2`；`direct_pass_through=false` |
| 传感器 | VL53L0C ToF 传感器 | `reference=U3`；`part_number=VL53L0CXV0DH/1`；`supply=pins1,11 AVDD VCC_3V3`；`scl=pin10 I2C_SCL`；`sda=pin9 I2C_SDA`；`ground=pins2,3,4,6,12` |
| 总线 | MCU 到 ToF I2C | `controller_scl=U1 PA11 pin18`；`device_scl=U3 pin10`；`controller_sda=U1 PA12 pin19`；`device_sda=U3 pin9`；`pullups=R4,R5 4.7K to VCC_3V3`；`level=3.3V` |
| GPIO 与控制信号 | ToF XSHUT 与 GPIO1 | `xshut=U3 pin5,R1 10K pull-up`；`gpio1=U3 pin7,R3 10K pull-up`；`mcu_control=null`；`dnc=pin8 NC` |
| 电源 | ToF 电源去耦 | `rail=VCC_3V3`；`device=U3`；`bulk_cap=C4 10uF`；`hf_cap=C9 100nF` |
| 核心器件 | WS2812C-2020 RGB LED | `reference=U4`；`part_number=WS2812C-2020`；`vdd=pin4 VCC_3V3`；`din=pin3 RGB`；`gnd=pin2`；`dout=pin1 NC`；`decoupling=C12 100nF` |
| GPIO 与控制信号 | RGB 数据 GPIO | `controller=U1 PA8 pin16`；`net=RGB`；`target=U4 pin3 DIN`；`level=3.3V domain` |
| 调试与烧录 | J4 SWD 调试接口 | `reference=J4`；`pin1=VCC_3V3`；`pin2=MCU_SWCLK/U1 PA14`；`pin3=MCU_SWDIO/U1 PA13`；`pin4=NRST`；`pin5=GND` |
| 复位 | STM32 复位网络 | `target=U1 pin5 PF2-NRST`；`debug_pin=J4 pin4`；`pullup=R2 10K`；`capacitor=C1 1uF` |
| 时钟 | MCU 时钟 | `pc14=pin1 NC`；`pc15=pin2 NC`；`crystal=null`；`oscillator=null` |
| 关键网络 | 通信、测距与指示关键路径 | `chain=J1 USART1 -> U1 -> USART2 J2`；`tof=U1 PA11/PA12 -> U3 SCL/SDA`；`rgb=U1 PA8 -> U4 DIN` |
| 模拟电路 | ToF I2C 上拉网络 | `scl_pullup=R4/R5 one of pair 4.7K`；`sda_pullup=R4/R5 one of pair 4.7K`；`rail=VCC_3V3`；`level_shifter=null`；`filter=null` |
| 保护电路 | 外部接口保护 | `esd_tvs=null`；`fuse=null`；`reverse_protection=null`；`ovp=null` |
| 存储 | 外部存储 | `external_flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null`；`internal_flash_capacity=null` |
| 内存与 Flash | 外部内存 | `external_ram=null`；`psram=null`；`ddr=null`；`internal_ram_capacity=null` |
| 音频 | 音频电路 | `codec=null`；`microphone=null`；`speaker=null`；`i2s=null` |
| 射频 | 射频通信电路 | `rf_transceiver=null`；`antenna=null`；`matching=null`；`optical_sensor=U3 VL53L0C` |
| 其他事实 | 电池与充电路径 | `battery=null`；`charger=null`；`fuel_gauge=null`；`input=VCC_5V` |
| 总线地址 | VL53L0C I2C 地址 | `device=U3 VL53L0CXV0DH/1`；`bus=I2C_SCL,I2C_SDA`；`address_7bit=null`；`address_strap=null` |
| 传感器 | ToF 测距范围与精度 | `documented_range=3~200cm`；`documented_accuracy=±3%`；`documented_normal_max=120cm`；`documented_long_range=200cm in dark/low IR`；`schematic_performance=null` |
| 电源 | 三种工作状态功耗 | `documented_stop_rgb=5V@21.27mA`；`documented_single=5V@20.26mA`；`documented_continuous=5V@24.75mA`；`schematic_current=null`；`measurement_conditions=null` |

## 待确认事项

- `address.tof`：原理图确认 U3 使用 I2C_SCL/I2C_SDA，但未标注数值 I2C 地址，也没有硬件地址选择脚配置。（证据：图 8a701e95b7c4 / 第 1 页 / 网格 C1-D3，U3 SCL/SDA/XSHUT/GPIO1，无地址注记）
- `sensor.documented-ranging`：正文称测距范围 3~200cm、精度 ±3%，并说明常规环境最大约 120cm、200cm 需 Long Range 暗环境；原理图只给出传感器型号与连接，不含这些性能与模式配置。（证据：图 8a701e95b7c4 / 第 1 页 / U3 VL53L0CXV0DH/1 电路，无范围/精度/模式注记）
- `power.documented-consumption`：正文列出停止模式白色 RGB 5V@21.27mA、单次测距 5V@20.26mA、连续测距 5V@24.75mA；原理图未给电流标注或测量条件。（证据：图 8a701e95b7c4 / 第 1 页 / VCC_5V/LDO/MCU/ToF/RGB 电路，无功耗数据）
- `review.tof-address`：请依据 VL53L0CXV0DH/1 datasheet 或 I2C 总线扫描确认默认 7-bit 地址。；原因：原理图只显示 I2C 连接，没有数值地址。
- `review.ranging-performance`：请用传感器配置、目标反射率/环境条件和实测确认 3~200cm、±3% 及 Long Range 模式表现。；原因：测距性能取决于运行配置与环境，原理图不包含这些参数。
- `review.power-consumption`：请按停止/单次/连续测距三种状态实测 5V 输入电流，确认 21.27mA、20.26mA、24.75mA。；原因：原理图不能证明系统动态功耗。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8a701e95b7c41a82098d85a20b8a181a5fed385778a97e4d5aaa7b65e0e33e1f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1199/U209_Chain-ToF_SCH_Main_V1.0_20250515_2025_10_30_22_09_27_page_01.png` |

---

源文档：`zh_CN/chain/Chain_ToF.md`

源文档 SHA-256：`2595e483b789eaeff524c4a24e290d42d4a1a04a1dea940f680ab2f451f516ba`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
