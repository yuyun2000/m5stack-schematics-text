# Unit Joystick v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Joystick v1.1 |
| SKU | U024-C |
| 产品 ID | `unit-joystick-v1-1-a7c7ae16fa9a` |
| 源文档 | `zh_CN/unit/joystick_1.1.md` |

## 概述

Unit Joystick v1.1 的原理图以 U3 ATMEGA328 为主控，P1 将 ADIN0/ADIN1/ADIN2 三路输入连接到 PC0/ADC0、PC1/ADC1、PC2/ADC2。U3 PC4/PC5 作为 SDA/SCL，经 R8/R7 各 470Ω串联后并联到 J2、J3 两个 I2C 接口；两个接口同时承载 VCC/GND，图中没有 I2C 上拉。J1 ISP_Download 引出 VCC、RESET、SCK、MISO、MOSI、GND，PD2 的 LED1 网络驱动 D1 蓝灯，PB0-PB2 各由 10KΩ 下拉。正文写 MEGA8A、I2C 地址/寄存器 0x52 和 X/Y/按键数值映射，但这些与原理图型号或未标信号含义存在待复核项。

## 检索关键词

`Unit Joystick v1.1`、`U024-C`、`ATMEGA328`、`MEGA8A`、`I2C`、`0x52`、`ADIN0 PC0 ADC0`、`ADIN1 PC1 ADC1`、`ADIN2 PC2 ADC2`、`SDA PC4`、`SCL PC5`、`RESET PC6`、`MOSI PB3`、`MISO PB4`、`SCK PB5`、`PB0 PB1 PB2 pulldown`、`PD2 LED1`、`D1 blue LED 0603`、`J1 ISP_Download`、`J2 IIC_Socket_4P`、`J3 IIC_Socket_4P`、`P1 Header 3`、`R7 470Ω`、`R8 470Ω`、`R16 1KΩ`、`R17-R19 10KΩ`、`C8 100nF`、`VCC`、`X axis`、`Y axis`、`Z button`、`0-255`、`BTN STATUS`、`ISP`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ATMEGA328 | 采集三路模拟/数字输入、提供 I2C 从设备固件、驱动状态 LED，并支持 ISP 下载 | 图 d0e504b66d0f / 第 1 页 / 第 1 页网格 B2-C3，U3 ATMEGA328 pin1-pin32 |
| P1 | Header 3 | 连接 ADIN0、ADIN1、ADIN2 三路摇杆输入 | 图 d0e504b66d0f / 第 1 页 / 第 1 页网格 B2，P1 Header 3 pin1-pin3 |
| J1 | ISP_Download | ATMEGA328 ISP 下载与复位接口 | 图 d0e504b66d0f / 第 1 页 / 第 1 页网格 A4，J1 ISP_Download pin1-pin6 |
| J2/J3 | IIC_Socket_4P | 两组并联的 SCL、SDA、VCC、GND I2C 接口 | 图 d0e504b66d0f / 第 1 页 / 第 1 页网格 B4-C4，J2/J3 IIC_Socket_4P |
| D1 | 蓝灯 0603 | 由 U3 PD2/LED1 网络驱动的蓝色状态 LED | 图 d0e504b66d0f / 第 1 页 / 第 1 页网格 C2，D1 蓝灯 0603 与 LED1/R16 |
| R7/R8 | 470Ω | U3 SCL/SDA 到 J2/J3 的串联电阻 | 图 d0e504b66d0f / 第 1 页 / 第 1 页网格 B3-B4，R7 SCL、R8 SDA 470Ω |
| R16 | 1KΩ | D1 蓝色 LED 到 GND 的串联限流电阻 | 图 d0e504b66d0f / 第 1 页 / 第 1 页网格 C2，D1-R16 1KΩ-GND |
| R17/R18/R19 | 10KΩ | 分别将 U3 PB0、PB1、PB2 下拉到 GND | 图 d0e504b66d0f / 第 1 页 / 第 1 页网格 B1-B2，R17/R18/R19 10KΩ 至 PB0/PB1/PB2 |
| C8 | 100nF | VCC 到 GND 的电源去耦电容 | 图 d0e504b66d0f / 第 1 页 / 第 1 页网格 D2-D3，C8 100nF |

## 系统结构

### Unit Joystick v1.1 系统结构

U3 ATMEGA328 采集 P1 的 ADIN0-ADIN2，通过 J2/J3 I2C 与外部主机通信，J1 提供 ISP 下载，PD2 驱动 D1 蓝灯。

- 参数与网络：`controller=U3 ATMEGA328`；`inputs=P1 ADIN0,ADIN1,ADIN2`；`host_interfaces=J2,J3 I2C`；`programming=J1 ISP_Download`；`indicator=D1 blue LED via PD2`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页完整原理图全部功能区

## 核心器件

### U3 ATMEGA328 关键引脚

U3 PB0/PB1/PB2 为 pin12/pin13/pin14，PB3/MOSI pin15、PB4/MISO pin16、PB5/SCK pin17；PC0/ADC0 pin23=ADIN0、PC1/ADC1 pin24=ADIN1、PC2/ADC2 pin25=ADIN2、PC4/SDA pin27、PC5/SCL pin28、PC6/RESET pin29、PD2 pin32=LED1。

- 参数与网络：`PB0_pin12=R17 pulldown`；`PB1_pin13=R18 pulldown`；`PB2_pin14=R19 pulldown`；`PB3_pin15=MOSI`；`PB4_pin16=MISO`；`PB5_pin17=SCK`；`PC0_pin23=ADIN0`；`PC1_pin24=ADIN1`；`PC2_pin25=ADIN2`；`PC4_pin27=SDA`；`PC5_pin28=SCL`；`PC6_pin29=RESET`；`PD2_pin32=LED1`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页 U3 pin12-pin17/pin23-pin29/pin32 网络标注

## 电源

### VCC 电源轨

J2/J3 pin3 和 J1 ISP pin1 共用 VCC，U3 AVCC pin18 与 VCC pin4/pin6 接 VCC，GND pin3/pin5/pin21 接地；C8 100nF 跨接 VCC 与 GND，图中没有稳压器。

- 参数与网络：`sources=J2.3,J3.3`；`isp_power=J1.1`；`mcu_power=U3 AVCC pin18,VCC pin4,pin6`；`mcu_ground=U3 pin3,pin5,pin21`；`decoupling=C8 100nF`；`regulator_shown=false`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页 U3 VCC/AVCC/GND、J1/J2/J3 VCC 与 C8

## 接口

### J2/J3 IIC_Socket_4P

J2 与 J3 均为 pin1=IIC_SCL、pin2=IIC_SDA、pin3=VCC、pin4=GND，两接口的对应针脚同网并联。

- 参数与网络：`J2_pin_1=IIC_SCL`；`J2_pin_2=IIC_SDA`；`J2_pin_3=VCC`；`J2_pin_4=GND`；`J3_pin_1=IIC_SCL`；`J3_pin_2=IIC_SDA`；`J3_pin_3=VCC`；`J3_pin_4=GND`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页网格 B4-C4，J2/J3 pin1-pin4

## 总线

### U3 到 J2/J3 I2C 总线

U3 PC5/SCL pin28 经 R7 470Ω 到 J2/J3 pin1，PC4/SDA pin27 经 R8 470Ω 到 J2/J3 pin2；J2/J3 两组接口并联，图中未显示 SCL/SDA 上拉电阻。

- 参数与网络：`controller=external host via J2/J3`；`device=U3 ATMEGA328 firmware`；`scl=U3 PC5 pin28 -> R7 470Ω -> J2.1/J3.1`；`sda=U3 PC4 pin27 -> R8 470Ω -> J2.2/J3.2`；`connectors_parallel=true`；`pullups_shown=false`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页 U3 SCL/SDA、R7/R8 与 J2/J3 并联网络

## GPIO 与控制信号

### D1 蓝色状态 LED

U3 PD2 pin32 的 LED1 网络连接 D1 蓝色 0603 LED，再经 R16 1KΩ 到 GND；PD2 输出高电平时形成 LED 电流路径。

- 参数与网络：`controller_pin=U3 PD2 pin32`；`net=LED1`；`led=D1 blue 0603`；`resistor=R16 1KΩ`；`return=GND`；`active_level=high`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页网格 C2，U3 PD2/LED1/D1/R16/GND

### U3 PB0-PB2 配置输入

U3 PB0 pin12、PB1 pin13、PB2 pin14 分别由 R17、R18、R19 10KΩ 下拉到 GND，页面未标注这些引脚的功能名称。

- 参数与网络：`PB0=pin12 via R17 10KΩ to GND`；`PB1=pin13 via R18 10KΩ to GND`；`PB2=pin14 via R19 10KΩ to GND`；`function_labeled=false`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页网格 B1-B2，R17-R19 至 U3 PB0-PB2

## 时钟

### U3 时钟

U3 PB6/XTAL1 pin7 与 PB7/XTAL2 pin8 在页面未连接，完整原理图未显示晶振、谐振器或外部振荡器。

- 参数与网络：`xtal1=U3 pin7 no visible connection`；`xtal2=U3 pin8 no visible connection`；`crystal_shown=false`；`resonator_shown=false`；`external_oscillator_shown=false`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页 U3 pin7/pin8 与完整图无时钟器件

## 复位

### U3 RESET

U3 PC6/RESET pin29 直接连接 J1 ISP pin2；图中未显示复位按键、上拉电阻或复位电容。

- 参数与网络：`mcu_pin=U3 PC6/RESET pin29`；`connector=J1 pin2`；`reset_switch_shown=false`；`pullup_shown=false`；`reset_capacitor_shown=false`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页 U3 RESET pin29 与 J1 pin2

## 保护电路

### P1/J1/J2/J3 接口保护

完整原理图未显示 TVS、ESD 阵列、保险丝或反接保护；I2C 仅有 R7/R8 470Ω 串联电阻，ADIN0-2 与 ISP 信号没有可见保护器件。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`i2c_series=R7/R8 470Ω`；`analog_protection_shown=false`；`isp_protection_shown=false`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页 P1/J1/J2/J3 至 U3 的全部路径

## 关键网络

### 摇杆、I2C 与 ISP 关键路径

P1 ADIN0-2→U3 PC0-2；U3 PC4/PC5→R8/R7→J2/J3 SDA/SCL；J1 RESET/SCK/MISO/MOSI→U3 PC6/PB5/PB4/PB3。

- 参数与网络：`input_path=P1.1-3 ADIN0-2 -> U3 PC0-2`；`i2c_path=U3 PC4/PC5 -> R8/R7 -> J2/J3 SDA/SCL`；`isp_path=J1 RESET/SCK/MISO/MOSI -> U3 PC6/PB5/PB4/PB3`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页完整 P1/U3/J1/J2/J3 网络

## 内存与 Flash

### 外部存储器

完整原理图未显示外部 Flash、EEPROM、RAM、SD 卡或其他存储器，U3 内部存储容量未在页面标注。

- 参数与网络：`external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false`；`internal_capacity_printed=false`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页完整图无外部存储器件

## 调试与烧录

### J1 ISP_Download

J1 pin1=VCC、pin2=RESET、pin3=SCK、pin4=MISO、pin5=MOSI、pin6=GND；SCK/MISO/MOSI 分别连接 U3 PB5 pin17/PB4 pin16/PB3 pin15，RESET 连接 PC6 pin29。

- 参数与网络：`pin_1=VCC`；`pin_2=RESET/U3 PC6 pin29`；`pin_3=SCK/U3 PB5 pin17`；`pin_4=MISO/U3 PB4 pin16`；`pin_5=MOSI/U3 PB3 pin15`；`pin_6=GND`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页网格 A4 J1 与 U3 RESET/SCK/MISO/MOSI 网络

## 模拟电路

### P1 ADIN0-ADIN2

P1 pin1/pin2/pin3 分别连接 ADIN0/ADIN1/ADIN2，并一一进入 U3 PC0/ADC0 pin23、PC1/ADC1 pin24、PC2/ADC2 pin25；图中未画外部 RC 滤波、钳位或分压器。

- 参数与网络：`pin_1=ADIN0 -> U3 PC0/ADC0 pin23`；`pin_2=ADIN1 -> U3 PC1/ADC1 pin24`；`pin_3=ADIN2 -> U3 PC2/ADC2 pin25`；`filter_shown=false`；`clamp_shown=false`；`divider_shown=false`
- 证据：图 d0e504b66d0f / 第 1 页 / 第 1 页网格 B2，P1 ADIN0-ADIN2 至 U3 PC0-PC2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Joystick v1.1 系统结构 | `controller=U3 ATMEGA328`；`inputs=P1 ADIN0,ADIN1,ADIN2`；`host_interfaces=J2,J3 I2C`；`programming=J1 ISP_Download`；`indicator=D1 blue LED via PD2` |
| 核心器件 | U3 ATMEGA328 关键引脚 | `PB0_pin12=R17 pulldown`；`PB1_pin13=R18 pulldown`；`PB2_pin14=R19 pulldown`；`PB3_pin15=MOSI`；`PB4_pin16=MISO`；`PB5_pin17=SCK`；`PC0_pin23=ADIN0`；`PC1_pin24=ADIN1`；`PC2_pin25=ADIN2`；`PC4_pin27=SDA`；`PC5_pin28=SCL`；`PC6_pin29=RESET`；`PD2_pin32=LED1` |
| 模拟电路 | P1 ADIN0-ADIN2 | `pin_1=ADIN0 -> U3 PC0/ADC0 pin23`；`pin_2=ADIN1 -> U3 PC1/ADC1 pin24`；`pin_3=ADIN2 -> U3 PC2/ADC2 pin25`；`filter_shown=false`；`clamp_shown=false`；`divider_shown=false` |
| 模拟电路 | X/Y/Z 与 ADIN 通道映射 | `documented_controls=X analog,Y analog,Z button`；`schematic_channels=ADIN0,ADIN1,ADIN2`；`axis_mapping_printed=false`；`documented_xy_values=0-255`；`documented_z_values=0/1` |
| 总线 | U3 到 J2/J3 I2C 总线 | `controller=external host via J2/J3`；`device=U3 ATMEGA328 firmware`；`scl=U3 PC5 pin28 -> R7 470Ω -> J2.1/J3.1`；`sda=U3 PC4 pin27 -> R8 470Ω -> J2.2/J3.2`；`connectors_parallel=true`；`pullups_shown=false` |
| 接口 | J2/J3 IIC_Socket_4P | `J2_pin_1=IIC_SCL`；`J2_pin_2=IIC_SDA`；`J2_pin_3=VCC`；`J2_pin_4=GND`；`J3_pin_1=IIC_SCL`；`J3_pin_2=IIC_SDA`；`J3_pin_3=VCC`；`J3_pin_4=GND` |
| 总线地址 | Joystick I2C 地址 | `documented_address=0x52`；`address_width=7-bit`；`device=U3 firmware`；`address_printed_on_schematic=false`；`PB0_PB2_function_labeled=false` |
| 其他事实 | Joystick 读取协议 | `documented_register=0x52`；`documented_length=3`；`documented_byte_0=X VALUE`；`documented_byte_1=Y VALUE`；`documented_byte_2=BTN STATUS`；`firmware_protocol_visible_on_schematic=false` |
| 核心器件 | 主控型号版本 | `schematic_part=ATMEGA328`；`documented_part=MEGA8A`；`values_match=false`；`product_version=v1.1` |
| 调试与烧录 | J1 ISP_Download | `pin_1=VCC`；`pin_2=RESET/U3 PC6 pin29`；`pin_3=SCK/U3 PB5 pin17`；`pin_4=MISO/U3 PB4 pin16`；`pin_5=MOSI/U3 PB3 pin15`；`pin_6=GND` |
| 复位 | U3 RESET | `mcu_pin=U3 PC6/RESET pin29`；`connector=J1 pin2`；`reset_switch_shown=false`；`pullup_shown=false`；`reset_capacitor_shown=false` |
| GPIO 与控制信号 | D1 蓝色状态 LED | `controller_pin=U3 PD2 pin32`；`net=LED1`；`led=D1 blue 0603`；`resistor=R16 1KΩ`；`return=GND`；`active_level=high` |
| GPIO 与控制信号 | U3 PB0-PB2 配置输入 | `PB0=pin12 via R17 10KΩ to GND`；`PB1=pin13 via R18 10KΩ to GND`；`PB2=pin14 via R19 10KΩ to GND`；`function_labeled=false` |
| 电源 | VCC 电源轨 | `sources=J2.3,J3.3`；`isp_power=J1.1`；`mcu_power=U3 AVCC pin18,VCC pin4,pin6`；`mcu_ground=U3 pin3,pin5,pin21`；`decoupling=C8 100nF`；`regulator_shown=false` |
| 时钟 | U3 时钟 | `xtal1=U3 pin7 no visible connection`；`xtal2=U3 pin8 no visible connection`；`crystal_shown=false`；`resonator_shown=false`；`external_oscillator_shown=false` |
| 关键网络 | 摇杆、I2C 与 ISP 关键路径 | `input_path=P1.1-3 ADIN0-2 -> U3 PC0-2`；`i2c_path=U3 PC4/PC5 -> R8/R7 -> J2/J3 SDA/SCL`；`isp_path=J1 RESET/SCK/MISO/MOSI -> U3 PC6/PB5/PB4/PB3` |
| 保护电路 | P1/J1/J2/J3 接口保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`i2c_series=R7/R8 470Ω`；`analog_protection_shown=false`；`isp_protection_shown=false` |
| 内存与 Flash | 外部存储器 | `external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false`；`internal_capacity_printed=false` |

## 待确认事项

- `analog.documented-axis-map`：产品正文描述 X/Y 模拟轴和 Z 按键，但原理图仅将三路标为 ADIN0、ADIN1、ADIN2，没有打印哪一路对应 X、Y 或按键，也没有标注 0-255/0-1 的固件输出转换。（证据：图 d0e504b66d0f / 第 1 页 / 第 1 页 P1 ADIN0/ADIN1/ADIN2，无 X/Y/Z 标签）
- `address.documented-0x52`：产品正文列出 7 位 I2C 地址 0x52；原理图未打印地址或固件配置，PB0-PB2 虽各有 10KΩ 下拉但未标为地址脚，因此 0x52 需结合固件或总线扫描确认。（证据：图 d0e504b66d0f / 第 1 页 / 第 1 页 U3 SDA/SCL 与 PB0-PB2 下拉，页面无地址标注）
- `other.documented-register-protocol`：产品正文描述寄存器 0x52 返回 3 字节 X、Y、BTN 状态；原理图只显示硬件连接，无法确认寄存器号、返回长度、字节顺序或数值缩放。（证据：图 d0e504b66d0f / 第 1 页 / 第 1 页 U3/P1/J2/J3，页面无寄存器协议标注）
- `component.mcu-identity-conflict`：原理图 U3 明确标 ATMEGA328，而产品正文规格表写 MEGA8A；当前图纸与正文型号不一致，需确认 v1.1 实际装配和对应固件目标。（证据：图 d0e504b66d0f / 第 1 页 / 第 1 页中央 U3 标注 ATMEGA328）
- `review.axis-map`：请依据 PCB 网表、摇杆连接或固件确认 ADIN0/ADIN1/ADIN2 与 X/Y/Z 按键的逐路映射及输出缩放。；原因：原理图只标 ADIN0-2，未标 X/Y/Z 或 0-255/0-1 转换。
- `review.i2c-address`：请依据 Unit Joystick v1.1 固件或 I2C 扫描确认 7 位地址 0x52。；原因：原理图未打印固件地址或地址脚定义。
- `review.register-protocol`：请依据固件源码或协议实测确认寄存器 0x52、3 字节长度和 X/Y/BTN 字节顺序。；原因：寄存器协议不可由原理图确认。
- `review.mcu-version`：请依据 BOM、实物丝印或固件目标确认 v1.1 实际 MCU 是原理图的 ATMEGA328 还是正文的 MEGA8A。；原因：当前原理图和产品正文的主控型号不一致。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d0e504b66d0f12e38e9fe9a41fdffb1763d843b5c8358d0f3844f99a10126157` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/799/U024-C_UNIT_JOYSTICK_SCHE_page_01.png` |

---

源文档：`zh_CN/unit/joystick_1.1.md`

源文档 SHA-256：`d5f2acbcde2f4fbb4ca1cc3f7c7b81bab2a5e52ba5a52e6d03479f66bed0b0d8`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
