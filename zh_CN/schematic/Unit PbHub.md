# Unit PbHub 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit PbHub |
| SKU | U041 |
| 产品 ID | `unit-pbhub-3ebe0981c7ee` |
| 源文档 | `zh_CN/unit/pbhub.md` |

## 概述

Unit PbHub（U041）原理图以 U1 ATMEGA328 为主控，通过 J7 GROVE_I2C 接收 SCL/SDA，并扩展为 J1~J6 六组 IN0~IN5 与 OUT0~OUT5 GPIO/模拟通道。全部接口和 MCU 直接使用 +5V，SCL/SDA 各由 10KΩ 上拉；U1 使用 Y1 8MHz 晶振、RESET 上拉/电容网络和 J8 六针 ISP。R2/R3/R4 0Ω 与 R7 10KΩ 构成 PB0~PB2 三位配置网络，但原理图未写出 I2C 地址映射；源产品文字还对 ATMEGA328 与 STM32F030F4P6 存在型号冲突，需以 BOM/实物确认装配版本。

## 检索关键词

`Unit PbHub`、`U041`、`PbHub`、`ATMEGA328`、`U1`、`GROVE_I2C`、`J7`、`J1-J6 GROVE_IO`、`IN0`、`IN1`、`IN2`、`IN3`、`IN4`、`IN5`、`OUT0`、`OUT1`、`OUT2`、`OUT3`、`OUT4`、`OUT5`、`SCL`、`SDA`、`I2C`、`0x61`、`0x68`、`PB0`、`PB1`、`PB2`、`R2 R3 R4 0Ω`、`R7 10KΩ`、`8MHz`、`Y1`、`RESET`、`J8 ISP_Download`、`MOSI`、`MISO`、`SCK`、`+5V`、`ADC6`、`ADC7`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ATMEGA328 | I2C 到六路 GPIO/模拟端口扩展主控，连接地址配置、8MHz 时钟、RESET 与 ISP | 图 7bd7bcb18379 / 第 1 页 / 页面中央 U1 ATMEGA328，PB0~PB7、PC0~PC6、PD0~PD7、ADC6/ADC7、AVCC/VCC/GND 引脚 |
| J7 | GROVE_I2C | 上游四针 I2C 与 +5V 电源接口 | 图 7bd7bcb18379 / 第 1 页 / 页面左上 J7 GROVE_I2C，pins 1~4 为 IIC_SCL/IIC_SDA/VCC/GND |
| J1-J6 | GROVE_IO | 六组扩展端口，每组包含一路 INn、一路 OUTn、+5V 与 GND | 图 7bd7bcb18379 / 第 1 页 / 页面右半 J1~J6 GROVE_IO，分别连接 IN0/OUT0 至 IN5/OUT5，pins 3/4 为 +5V/GND |
| J8 | ISP_Download | ATMEGA328 六针 ISP 编程/调试接口 | 图 7bd7bcb18379 / 第 1 页 / 页面右下 J8 ISP_Download，pins 1~6 为 VCC/RST/SCK/MISO/MOSI/GND |
| Y1 | 8MHz | ATMEGA328 PB6/XTAL1 与 PB7/XTAL2 的外部晶振 | 图 7bd7bcb18379 / 第 1 页 / 页面 U1 左侧 Y1 8MHz 连接 U1 pins 7/8，C8/C9 各 20pF 到 GND |
| R5/R6 | 10KΩ | SCL 与 SDA 到 +5V 的 I2C 上拉电阻 | 图 7bd7bcb18379 / 第 1 页 / 页面左上 R5 10KΩ 从 SCL 到 +5V，R6 10KΩ 从 SDA 到 +5V |
| R1/C7 | 10KΩ/100nF | RESET 网络的 +5V 上拉和对地电容 | 图 7bd7bcb18379 / 第 1 页 / 页面左中 +5V-R1 10KΩ-RESET-C7 100nF-GND |
| R2/R3/R4 | 0Ω | PB2/PB1/PB0 到 +5V 的三位地址/配置跳线 | 图 7bd7bcb18379 / 第 1 页 / 页面 U1 左上 R2/R3/R4 0Ω 从 +5V 分别连接 U1 PB2 pin14、PB1 pin13、PB0 pin12 |
| R7 | 10KΩ (103) ±5% | PB0~PB2 配置网络的多联下拉电阻阵列 | 图 7bd7bcb18379 / 第 1 页 / 页面 U1 左侧 R7 八针电阻阵列，标 10KΩ (103) ±5%，一侧接 PB0~PB2 配置线、另一侧接 GND |
| C8/C9 | 20pF | Y1 两端到 GND 的晶振负载电容 | 图 7bd7bcb18379 / 第 1 页 / 页面 Y1 两侧 C8/C9 20pF 到 GND |
| C1-C6 | 100nF | J1~J6 各 +5V 端口的本地去耦电容 | 图 7bd7bcb18379 / 第 1 页 / 页面右半 C1~C6 各 100nF，从对应 J1~J6 +5V 旁接 GND |
| C10 | 100nF | J7 上游 +5V 输入的本地去耦电容 | 图 7bd7bcb18379 / 第 1 页 / 页面左上 J7 旁 +5V-C10 100nF-GND |

## 系统结构

### Unit PbHub 系统架构

U1 ATMEGA328 作为 I2C 从设备控制六组 J1~J6 GROVE_IO；J7 提供上游 I2C/+5V，Y1 提供 8MHz 时钟，J8 提供 ISP 下载，R2~R4/R7 提供三位配置。

- 参数与网络：`controller=U1 ATMEGA328`；`upstream=J7 GROVE_I2C`；`ports=J1-J6 GROVE_IO`；`clock=Y1 8MHz`；`debug=J8 ISP_Download`；`configuration=PB0-PB2 via R2-R4/R7`
- 证据：图 7bd7bcb18379 / 第 1 页 / 整页 U1/J1~J8/Y1/R1~R7/C1~C10 与同名网络

## 核心器件

### U1 电源引脚

U1 AVCC pin 18、VCC pins 4/6 接 +5V，GND pins 3/5/21 接地；AREF pin 20 未显示外接网络。

- 参数与网络：`avcc=pin 18 +5V`；`vcc=pins 4,6 +5V`；`ground=pins 3,5,21 GND`；`aref=pin 20 no visible connection`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面 U1 右侧 AREF/AVCC/VCC/GND pins 20/18/4/6/3/5/21

## 电源

### +5V 电源分配

J7 pin 3 输入 +5V，并直接供给 U1 AVCC/VCC、J1~J6 pin 3、I2C 上拉、RESET 上拉、配置电阻和去耦电容；本页没有稳压器、DC/DC 或负载开关。

- 参数与网络：`input=J7 pin 3 +5V`；`mcu=U1 AVCC/VCC`；`ports=J1-J6 pin 3`；`pullups=R1,R2-R6`；`regulator=null`；`dc_dc=null`；`load_switch=null`
- 证据：图 7bd7bcb18379 / 第 1 页 / 整页 +5V 同名网络，从 J7 到 U1/J1~J6/阻容；无电源转换器件

### 接口去耦电容

C1~C6 各 100nF，分别位于 J1~J6 的 +5V 端口旁并接地；C10 100nF 位于 J7 +5V 输入旁并接地。

- 参数与网络：`output_ports=C1-C6 100nF for J1-J6`；`upstream=C10 100nF for J7`；`rail=+5V`；`return=GND`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面 J1~J7 旁 C1~C6/C10 100nF 到 GND

## 接口

### J7 GROVE_I2C 针脚

J7 pins 1~4 依次为 IIC_SCL、IIC_SDA、VCC、GND，对应网络 SCL、SDA、+5V、GND。

- 参数与网络：`pin_1=IIC_SCL-SCL`；`pin_2=IIC_SDA-SDA`；`pin_3=VCC +5V`；`pin_4=GND`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面左上 J7 pins 1~4 与 SCL/SDA/+5V/GND

### J1~J6 公共针脚定义

J1~J6 每组 pin 1 标注 MISO 并连接 INn，pin 2 标注 IO 并连接 OUTn，pin 3 为 +5V，pin 4 为 GND。

- 参数与网络：`pin_1=MISO-INn，端口到 MCU 输入`；`pin_2=IO-OUTn，MCU 到端口输出`；`pin_3=+5V`；`pin_4=GND`；`ports=n=0..5`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面右半 J1~J6 GROVE_IO 重复 pin 1 MISO/INn、pin 2 IO/OUTn、pin 3 +5V、pin 4 GND

## 总线

### 上游 I2C 总线

J7 SCL 连接 U1 PC5/SCL pin 28，J7 SDA 连接 U1 PC4/SDA pin 27；两线分别经 R5/R6 10KΩ 上拉到 +5V。

- 参数与网络：`controller_connector=J7`；`device=U1 ATMEGA328`；`scl=J7 pin 1 -> U1 pin 28 PC5/SCL`；`sda=J7 pin 2 -> U1 pin 27 PC4/SDA`；`scl_pullup=R5 10KΩ to +5V`；`sda_pullup=R6 10KΩ to +5V`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面 J7 SCL/SDA、R5/R6 与 U1 pins 28/27

### ISP SPI 信号

MOSI、MISO、SCK 仅用于图中 J8 ISP 下载路径，页面未显示其他 SPI 外设或片选网络。

- 参数与网络：`controller=U1 ATMEGA328`；`connector=J8`；`mosi=PB3 pin15`；`miso=PB4 pin16`；`sck=PB5 pin17`；`external_spi_device=null`；`chip_select=null`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面 U1 PB3/PB4/PB5 到 J8 MOSI/MISO/SCK，同页无其他 SPI 器件

## GPIO 与控制信号

### J1 Port 0

J1 IN0 连接 U1 PC0/ADC0 pin 23，OUT0 连接 U1 PD2/INT0 pin 32。

- 参数与网络：`connector=J1`；`input=pin 1 IN0 -> U1 pin 23 PC0/ADC0`；`output=pin 2 OUT0 -> U1 pin 32 PD2/INT0`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面右上 J1 IN0/OUT0 与中央 U1 IN0 pin23/OUT0 pin32

### J2 Port 1

J2 IN1 连接 U1 PC1/ADC1 pin 24，OUT1 连接 U1 PD3/PCINT19/OC2B/INT1 pin 1。

- 参数与网络：`connector=J2`；`input=pin 1 IN1 -> U1 pin 24 PC1/ADC1`；`output=pin 2 OUT1 -> U1 pin 1 PD3/PCINT19/OC2B/INT1`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面右上 J2 IN1/OUT1 与中央 U1 IN1 pin24/OUT1 pin1

### J3 Port 2

J3 IN2 连接 U1 PC2/ADC2 pin 25，OUT2 连接 U1 PD4/PCINT20/XCK/T0 pin 2。

- 参数与网络：`connector=J3`；`input=pin 1 IN2 -> U1 pin 25 PC2/ADC2`；`output=pin 2 OUT2 -> U1 pin 2 PD4/PCINT20/XCK/T0`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面右中 J3 IN2/OUT2 与中央 U1 IN2 pin25/OUT2 pin2

### J4 Port 3

J4 IN3 连接 U1 PC3/ADC3 pin 26，OUT3 连接 U1 PD5/PCINT21/OC0B/T1 pin 9。

- 参数与网络：`connector=J4`；`input=pin 1 IN3 -> U1 pin 26 PC3/ADC3`；`output=pin 2 OUT3 -> U1 pin 9 PD5/PCINT21/OC0B/T1`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面右中 J4 IN3/OUT3 与中央 U1 IN3 pin26/OUT3 pin9

### J5 Port 4

J5 IN4 连接 U1 ADC6 pin 19，OUT4 连接 U1 PD6/PCINT22/OC0A/AIN0 pin 10。

- 参数与网络：`connector=J5`；`input=pin 1 IN4 -> U1 pin 19 ADC6`；`output=pin 2 OUT4 -> U1 pin 10 PD6/PCINT22/OC0A/AIN0`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面右下 J5 IN4/OUT4 与中央 U1 ADC6 pin19 IN4、PD6 pin10 OUT4

### J6 Port 5

J6 IN5 连接 U1 ADC7 pin 22，OUT5 连接 U1 PD7/PCINT23/AIN1 pin 11。

- 参数与网络：`connector=J6`；`input=pin 1 IN5 -> U1 pin 22 ADC7`；`output=pin 2 OUT5 -> U1 pin 11 PD7/PCINT23/AIN1`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面右下 J6 IN5/OUT5 与中央 U1 ADC7 pin22 IN5、PD7 pin11 OUT5

### PB0~PB2 配置网络

U1 PB0 pin12、PB1 pin13、PB2 pin14 各连接一只 0Ω 电阻 R4/R3/R2 到 +5V，并连接 R7 10KΩ 多联电阻到 GND，形成三位硬件配置输入。

- 参数与网络：`bit_0=PB0 pin12,R4 0Ω to +5V,R7 10KΩ to GND`；`bit_1=PB1 pin13,R3 0Ω to +5V,R7 10KΩ to GND`；`bit_2=PB2 pin14,R2 0Ω to +5V,R7 10KΩ to GND`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面 U1 左上 PB0~PB2、R2~R4 0Ω、R7 10KΩ 与 +5V/GND

## 时钟

### U1 外部时钟

Y1 8MHz 连接 U1 PB6/XTAL1 pin 7 与 PB7/XTAL2 pin 8，两端分别通过 C8/C9 20pF 接地。

- 参数与网络：`crystal=Y1 8MHz`；`xtal1=U1 pin 7 PB6/XTAL1`；`xtal2=U1 pin 8 PB7/XTAL2`；`load_caps=C8 20pF,C9 20pF`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面 U1 左侧 Y1 8MHz、pins 7/8 与 C8/C9 20pF

## 复位

### ATMEGA328 RESET

U1 PC6/RESET pin 29 连接 RESET 网络；R1 10KΩ 将 RESET 上拉到 +5V，C7 100nF 将 RESET 接地，J8 pin 2 也连接 RESET。

- 参数与网络：`mcu_pin=U1 pin 29 PC6/RESET`；`pullup=R1 10KΩ to +5V`；`capacitor=C7 100nF to GND`；`debug_pin=J8 pin 2 RST`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面左中 R1/C7 RESET、U1 pin29 与右下 J8 pin2

## 保护电路

### 端口与电源保护

J7 与 J1~J6 的信号/+5V 路径未显示 TVS/ESD、保险丝、反接、过压、串联限流或端口隔离器件。

- 参数与网络：`tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`series_limit=null`；`isolation=null`
- 证据：图 7bd7bcb18379 / 第 1 页 / 整页 J7/J1~J6 到 U1 的直接信号和 +5V 路径，无保护器件

## 存储

### 外部存储器

本页未显示独立 Flash、EEPROM、RAM、SD 卡或其他外部存储器；U1 内部存储容量未在原理图标注。

- 参数与网络：`external_flash=null`；`external_eeprom=null`；`external_ram=null`；`sd=null`；`internal_capacity=null`
- 证据：图 7bd7bcb18379 / 第 1 页 / 整页器件无独立存储芯片，U1 符号未给存储容量

## 调试与烧录

### J8 ISP 下载接口

J8 pins 1~6 依次为 VCC(+5V)、RST、SCK、MISO、MOSI、GND；SCK/MISO/MOSI 分别连接 U1 PB5 pin17、PB4 pin16、PB3 pin15。

- 参数与网络：`pin_1=VCC +5V`；`pin_2=RST RESET`；`pin_3=SCK U1 pin17 PB5`；`pin_4=MISO U1 pin16 PB4`；`pin_5=MOSI U1 pin15 PB3`；`pin_6=GND`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面右下 J8 ISP_Download pins 1~6 与中央 U1 MOSI/MISO/SCK/RESET

## 模拟电路

### 六路输入 ADC 映射

IN0~IN3 分别映射 U1 ADC0~ADC3，IN4/IN5 分别映射独立 ADC6/ADC7；原理图未显示输入分压、缓冲、滤波或过压钳位。

- 参数与网络：`IN0=ADC0 pin23`；`IN1=ADC1 pin24`；`IN2=ADC2 pin25`；`IN3=ADC3 pin26`；`IN4=ADC6 pin19`；`IN5=ADC7 pin22`；`divider=null`；`buffer=null`；`filter=null`；`clamp=null`
- 证据：图 7bd7bcb18379 / 第 1 页 / 页面 U1 IN0~IN5 对应 ADC 引脚与 J1~J6 直连网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit PbHub 系统架构 | `controller=U1 ATMEGA328`；`upstream=J7 GROVE_I2C`；`ports=J1-J6 GROVE_IO`；`clock=Y1 8MHz`；`debug=J8 ISP_Download`；`configuration=PB0-PB2 via R2-R4/R7` |
| 核心器件 | U1 电源引脚 | `avcc=pin 18 +5V`；`vcc=pins 4,6 +5V`；`ground=pins 3,5,21 GND`；`aref=pin 20 no visible connection` |
| 接口 | J7 GROVE_I2C 针脚 | `pin_1=IIC_SCL-SCL`；`pin_2=IIC_SDA-SDA`；`pin_3=VCC +5V`；`pin_4=GND` |
| 总线 | 上游 I2C 总线 | `controller_connector=J7`；`device=U1 ATMEGA328`；`scl=J7 pin 1 -> U1 pin 28 PC5/SCL`；`sda=J7 pin 2 -> U1 pin 27 PC4/SDA`；`scl_pullup=R5 10KΩ to +5V`；`sda_pullup=R6 10KΩ to +5V` |
| 接口 | J1~J6 公共针脚定义 | `pin_1=MISO-INn，端口到 MCU 输入`；`pin_2=IO-OUTn，MCU 到端口输出`；`pin_3=+5V`；`pin_4=GND`；`ports=n=0..5` |
| GPIO 与控制信号 | J1 Port 0 | `connector=J1`；`input=pin 1 IN0 -> U1 pin 23 PC0/ADC0`；`output=pin 2 OUT0 -> U1 pin 32 PD2/INT0` |
| GPIO 与控制信号 | J2 Port 1 | `connector=J2`；`input=pin 1 IN1 -> U1 pin 24 PC1/ADC1`；`output=pin 2 OUT1 -> U1 pin 1 PD3/PCINT19/OC2B/INT1` |
| GPIO 与控制信号 | J3 Port 2 | `connector=J3`；`input=pin 1 IN2 -> U1 pin 25 PC2/ADC2`；`output=pin 2 OUT2 -> U1 pin 2 PD4/PCINT20/XCK/T0` |
| GPIO 与控制信号 | J4 Port 3 | `connector=J4`；`input=pin 1 IN3 -> U1 pin 26 PC3/ADC3`；`output=pin 2 OUT3 -> U1 pin 9 PD5/PCINT21/OC0B/T1` |
| GPIO 与控制信号 | J5 Port 4 | `connector=J5`；`input=pin 1 IN4 -> U1 pin 19 ADC6`；`output=pin 2 OUT4 -> U1 pin 10 PD6/PCINT22/OC0A/AIN0` |
| GPIO 与控制信号 | J6 Port 5 | `connector=J6`；`input=pin 1 IN5 -> U1 pin 22 ADC7`；`output=pin 2 OUT5 -> U1 pin 11 PD7/PCINT23/AIN1` |
| 模拟电路 | 六路输入 ADC 映射 | `IN0=ADC0 pin23`；`IN1=ADC1 pin24`；`IN2=ADC2 pin25`；`IN3=ADC3 pin26`；`IN4=ADC6 pin19`；`IN5=ADC7 pin22`；`divider=null`；`buffer=null`；`filter=null`；`clamp=null` |
| 时钟 | U1 外部时钟 | `crystal=Y1 8MHz`；`xtal1=U1 pin 7 PB6/XTAL1`；`xtal2=U1 pin 8 PB7/XTAL2`；`load_caps=C8 20pF,C9 20pF` |
| 复位 | ATMEGA328 RESET | `mcu_pin=U1 pin 29 PC6/RESET`；`pullup=R1 10KΩ to +5V`；`capacitor=C7 100nF to GND`；`debug_pin=J8 pin 2 RST` |
| 调试与烧录 | J8 ISP 下载接口 | `pin_1=VCC +5V`；`pin_2=RST RESET`；`pin_3=SCK U1 pin17 PB5`；`pin_4=MISO U1 pin16 PB4`；`pin_5=MOSI U1 pin15 PB3`；`pin_6=GND` |
| 总线 | ISP SPI 信号 | `controller=U1 ATMEGA328`；`connector=J8`；`mosi=PB3 pin15`；`miso=PB4 pin16`；`sck=PB5 pin17`；`external_spi_device=null`；`chip_select=null` |
| GPIO 与控制信号 | PB0~PB2 配置网络 | `bit_0=PB0 pin12,R4 0Ω to +5V,R7 10KΩ to GND`；`bit_1=PB1 pin13,R3 0Ω to +5V,R7 10KΩ to GND`；`bit_2=PB2 pin14,R2 0Ω to +5V,R7 10KΩ to GND` |
| 电源 | +5V 电源分配 | `input=J7 pin 3 +5V`；`mcu=U1 AVCC/VCC`；`ports=J1-J6 pin 3`；`pullups=R1,R2-R6`；`regulator=null`；`dc_dc=null`；`load_switch=null` |
| 电源 | 接口去耦电容 | `output_ports=C1-C6 100nF for J1-J6`；`upstream=C10 100nF for J7`；`rail=+5V`；`return=GND` |
| 保护电路 | 端口与电源保护 | `tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`series_limit=null`；`isolation=null` |
| 存储 | 外部存储器 | `external_flash=null`；`external_eeprom=null`；`external_ram=null`；`sd=null`；`internal_capacity=null` |
| 总线地址 | I2C 地址配置 | `bits=PB0,PB1,PB2`；`default_address=null`；`address_map=null`；`candidate_from_product_doc=0x61-0x68` |
| 核心器件 | 实装 MCU 型号 | `schematic=ATMEGA328`；`full_suffix=null`；`conflicting_product_spec=STM32F030F4P6`；`assembled_part=null` |
| 其他事实 | 固件与 ADC/PWM 能力 | `firmware_commands=null`；`adc_resolution=null`；`adc_reference=null`；`pwm_frequency=null`；`port_mode_limits=null`；`nested_hub_support=null` |

## 待确认事项

- `address.i2c-strap-map`：原理图确认 PB0~PB2 三位硬件配置网络，但没有列出各组合对应的 I2C 地址，因此不能仅凭本页确认默认 0x61 或 0x61~0x68 映射。（证据：图 7bd7bcb18379 / 第 1 页 / 页面 PB0~PB2/R2~R4/R7 配置电路，无十六进制地址或映射表）
- `component.assembled-mcu`：原理图明确将 U1 标为 ATMEGA328，但未给完整封装/速度后缀；源产品文字的规格表另列 STM32F030F4P6，与图纸冲突，实际装配型号需 BOM 或实物确认。（证据：图 7bd7bcb18379 / 第 1 页 / 页面中央 U1 型号文字 ATMEGA328 与 32-pin 引脚符号）
- `other.firmware-capabilities`：原理图给出 ADC、定时器/PWM 复用引脚，但未标注固件命令、ADC 分辨率/参考电压、PWM 频率、端口模式限制或是否支持嵌套。（证据：图 7bd7bcb18379 / 第 1 页 / 页面 U1 ADC/OC 引脚复用文字及六路端口，整页无固件/性能参数）
- `review.i2c-address-map`：PB0~PB2 各焊接组合对应的 I2C 地址是什么，默认地址是否为 0x61？；原因：原理图只显示三位电阻配置网络，没有地址真值表。
- `review.assembled-mcu`：当前 U041 硬件版本实际装配 ATMEGA328 的哪个完整型号，还是 STM32F030F4P6？；原因：原理图标 ATMEGA328，源产品规格表列 STM32F030F4P6，需按硬件优先级用 BOM/实物消除冲突。
- `review.firmware-capabilities`：该固件版本的命令集、ADC 分辨率/参考、PWM 参数和端口功能限制是什么？；原因：这些行为由 MCU 固件和器件参数决定，原理图只给硬件引脚映射。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7bd7bcb1837980d1e5812935dc8f929b2a6ded1208b0e3faa4cc1fb4c1ca21fb` | `https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub/pbhub_sch_01.webp` |

---

源文档：`zh_CN/unit/pbhub.md`

源文档 SHA-256：`ee9dcbc79d765713c19b5ed6c4feb1b0e7aab511063c40a1327f26b8c804c536`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
