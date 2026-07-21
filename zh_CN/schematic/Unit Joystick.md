# Unit Joystick 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Joystick |
| SKU | U024 |
| 产品 ID | `unit-joystick-3a33915b6406` |
| 源文档 | `zh_CN/unit/joystick.md` |

## 概述

Unit Joystick 以 U3 ATMEGA328 为本地主控，P1 的 ADIN0/ADIN1/ADIN2 分别进入 ADC0/ADC1/ADC2，用于采集摇杆三路输入。U3 的 PC4/PC5 通过 R8/R7 470Ω 串联连接 J2 Grove 的 IIC_SDA/IIC_SCL，J3 是同网络但标记 Not Mount 的备用接口；J1 提供六针 ISP 下载。VCC 由 Grove 直接输入并为 MCU 供电，原理图没有稳压器或专用保护器件；正文所列 0x52 地址、X/Y/Z 数据语义和 5V 电气边界未直接印在图中。

## 检索关键词

`Unit Joystick`、`U024`、`ATMEGA328`、`ATmega328`、`P1 Rocker`、`ADIN0`、`ADIN1`、`ADIN2`、`ADC0`、`ADC1`、`ADC2`、`I2C`、`0x52`、`IIC_SCL`、`IIC_SDA`、`SCL`、`SDA`、`J2 IIC_Socket_4P`、`J3 Not Mount`、`J1 ISP_Download`、`MOSI`、`MISO`、`SCK`、`RESET`、`VCC`、`GND`、`R7 470R`、`R8 470R`、`R16 1K`、`R17 10K`、`R18 10K`、`R19 10K`、`LED1`、`D1 红灯 0603`、`PC4`、`PC5`、`PB0`、`PB1`、`PB2`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ATMEGA328 | 采集三路摇杆输入、提供 I2C 从接口并驱动状态 LED 的本地主控 | 图 14dbfb9d33ff / 第 1 页 / 第 1 页中央：U3 ATMEGA328，PB0-PB7、PC0-PC6、PD0-PD7、电源与地引脚 |
| P1 | Header 3 | Rocker 三针输入接口，引出 ADIN0、ADIN1、ADIN2 | 图 14dbfb9d33ff / 第 1 页 / 第 1 页左中 Rocker 区：P1 Header3 pin1-pin3 与 ADIN0/ADIN1/ADIN2 |
| J2 | IIC_Socket_4P | 标注 Connected to Core 的主 Grove I2C/VCC/GND 接口 | 图 14dbfb9d33ff / 第 1 页 / 第 1 页右中：J2 IIC_Socket_4P，Connected to Core，pin1-pin4 |
| J3 | IIC_Socket_4P | 与 J2 同网络但标记 Not Mount 的备用 I2C/VCC/GND 接口 | 图 14dbfb9d33ff / 第 1 页 / 第 1 页右下：J3 IIC_Socket_4P，Not Mount，pin1-pin4 |
| J1 | ISP_Download | ATMEGA328 的 VCC、RESET、SCK、MISO、MOSI、GND 六针 ISP 下载接口 | 图 14dbfb9d33ff / 第 1 页 / 第 1 页右上：J1 ISP_Download pin1-pin6 |
| R7,R8 | 470R | SCL 与 SDA 到 J2/J3 的串联电阻 | 图 14dbfb9d33ff / 第 1 页 / 第 1 页中右：SCL-R7(470Ω)-IIC_SCL 与 SDA-R8(470Ω)-IIC_SDA |
| R17,R18,R19 | 10KΩ | 分别将 U3 PB0、PB1、PB2 下拉到 GND | 图 14dbfb9d33ff / 第 1 页 / 第 1 页左上：R17/R18/R19 10KΩ 从 U3 pins12/13/14 接 GND |
| D1,R16 | 红灯 0603 / 1KΩ | 由 U3 LED1/PD2 驱动的红色 LED 与限流电阻支路 | 图 14dbfb9d33ff / 第 1 页 / 第 1 页左下：U3 LED1 至 D1 红灯 0603、R16 1KΩ、GND |
| C8 | 100nF | VCC 至 GND 的电源去耦电容 | 图 14dbfb9d33ff / 第 1 页 / 第 1 页下中：C8 100nF 跨接 VCC 与 GND |
| Rocker | 未标注 | 经 P1 提供三路信号的摇杆组件；本页未给出具体型号与内部电阻结构 | 图 14dbfb9d33ff / 第 1 页 / 第 1 页左中 Rocker 文字、P1 Header3 与 ADIN0/ADIN1/ADIN2 |

## 系统结构

### Unit Joystick 系统架构

U3 ATMEGA328 通过 ADC0/ADC1/ADC2 采集 P1 的 ADIN0/ADIN1/ADIN2，通过 PC4/PC5 提供 SDA/SCL I2C，从 J2 连接外部主机；J1 为 ISP 下载，PD2 驱动 D1 红色 LED。完整单页没有独立稳压器、外部存储器、射频、音频或电池电路。

- 参数与网络：`controller=U3 ATMEGA328`；`analog_inputs=P1 ADIN0/ADIN1/ADIN2 -> ADC0/ADC1/ADC2`；`host_bus=PC4 SDA,PC5 SCL -> J2`；`debug=J1 ISP_Download`；`indicator=PD2 LED1 -> D1/R16`；`storage=null`；`rf=null`；`battery=null`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页完整原理图

## 电源

### VCC 供电路径

J2/J3 pin3、J1 pin1、U3 AVCC pin18、VCC pin4 与 VCC pin6 均连接同名 VCC；U3 GND pins3/5/21、J1 pin6、J2/J3 pin4 接 GND。C8 100nF 跨接 VCC 与 GND，本页没有稳压器或电源开关。

- 参数与网络：`input=J2 pin3 VCC`；`mcu_supply=AVCC pin18,VCC pins4/6`；`mcu_ground=pins3/5/21`；`isp_supply=J1 pin1 VCC,pin6 GND`；`decoupling=C8 100nF`；`regulator=null`；`power_switch=null`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页 J2/J3/J1/U3/C8 的全部 VCC 与 GND 同名网络

## 接口

### J2 主 Grove 接口

J2 IIC_Socket_4P 标注 Connected to Core，pin1=IIC_SCL、pin2=IIC_SDA、pin3=VCC、pin4=GND；IIC_SCL/IIC_SDA 分别经 R7/R8 接 U3。

- 参数与网络：`connector=J2 IIC_Socket_4P`；`pin1=IIC_SCL`；`pin2=IIC_SDA`；`pin3=VCC`；`pin4=GND`；`assembly=Connected to Core`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页右中 J2 pin1-pin4 与 Connected to Core 标注

### J3 备用未装接口

J3 IIC_Socket_4P 的 pin1=IIC_SCL、pin2=IIC_SDA、pin3=VCC、pin4=GND，与 J2 相同网络并联，但原理图在 J3 下方明确标注 Not Mount。

- 参数与网络：`connector=J3 IIC_Socket_4P`；`pin1=IIC_SCL`；`pin2=IIC_SDA`；`pin3=VCC`；`pin4=GND`；`assembly=Not Mount`；`parallel_with=J2`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页右下 J3 pin1-pin4、与 J2 共线及 Not Mount 标注

### P1 Rocker 三针接口

P1 Header3 的 pin1=ADIN0、pin2=ADIN1、pin3=ADIN2，三条网络均直接进入 U3 的模拟输入。原理图未在 P1 上标电源或 GND 引脚。

- 参数与网络：`pin1=ADIN0`；`pin2=ADIN1`；`pin3=ADIN2`；`power_pin=null`；`ground_pin=null`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页左中 P1 Header3 pin1-pin3 与 ADIN0/ADIN1/ADIN2

## 总线

### ATMEGA328 至 Grove I2C

U3 PC4/ADC4/SDA pin27 连接 SDA，经过 R8 470Ω 后形成 IIC_SDA；PC5/ADC5/SCL pin28 连接 SCL，经过 R7 470Ω 后形成 IIC_SCL。IIC_SDA/IIC_SCL 同时连接 J2 与未装配的 J3，本页未显示 I2C 上拉电阻。

- 参数与网络：`controller=U3 ATMEGA328`；`sda=PC4 pin27 -> SDA -> R8 470R -> IIC_SDA`；`scl=PC5 pin28 -> SCL -> R7 470R -> IIC_SCL`；`connectors=J2,J3`；`pullups_shown=false`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页 U3 PC4/PC5 至 R8/R7、J2/J3 的完整信号路径

## GPIO 与控制信号

### PB0/PB1/PB2 固定下拉

U3 PB0 pin12、PB1 pin13、PB2 pin14 分别经 R17、R18、R19 10KΩ 接 GND；这些节点未标功能网络名，也未引至外部连接器。

- 参数与网络：`pb0=pin12 via R17 10K to GND`；`pb1=pin13 via R18 10K to GND`；`pb2=pin14 via R19 10K to GND`；`external_connector=null`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页左上 R17/R18/R19 与 U3 PB0/PB1/PB2

### 红色 LED 驱动

U3 PD2/PCINT18/INT0 pin32 的 LED1 网络串联 D1（红灯 0603）与 R16 1KΩ 后接 GND。

- 参数与网络：`mcu_pin=U3 PD2 pin32`；`net=LED1`；`led=D1 红灯 0603`；`resistor=R16 1KΩ`；`return=GND`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页左下 U3 pin32 LED1-D1-R16-GND 支路

## 时钟

### ATMEGA328 时钟连接

U3 PB6/XTAL1/TOSC1 pin7 与 PB7/XTAL2/TOSC2 pin8 没有外接晶振、谐振器、负载电容或时钟网络；原理图未标 MCU 工作频率。

- 参数与网络：`xtal1=PB6 pin7 no external connection`；`xtal2=PB7 pin8 no external connection`；`external_crystal=false`；`frequency=null`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页 U3 PB6/XTAL1 pin7 与 PB7/XTAL2 pin8 无外接连线

## 复位

### ATMEGA328 RESET

U3 PC6/RESET pin29 连接 RESET 网络并引至 J1 pin2；本页未显示 RESET 的外部上拉电阻、复位电容或按键。

- 参数与网络：`mcu_pin=U3 PC6/RESET pin29`；`debug_pin=J1 pin2`；`external_pullup_shown=false`；`reset_cap_shown=false`；`reset_button_shown=false`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页 U3 PC6/RESET pin29 与 J1 RESET pin2

## 保护电路

### Grove 与 VCC 保护拓扑

J2 的 VCC 直接连接 U3 与 J1，SCL/SDA 仅经过 R7/R8 470Ω 串联电阻；本页未显示保险丝、TVS/ESD 二极管、反接保护、稳压器或专用电平转换器。

- 参数与网络：`vcc_path=J2 pin3 VCC -> U3/J1`；`signal_series=R7/R8 470R`；`fuse_shown=false`；`tvs_esd_shown=false`；`reverse_protection_shown=false`；`regulator_shown=false`；`level_shifter_shown=false`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页完整 J2/J3 至 U3 的电源与 I2C 路径

## 内存与 Flash

### 程序与数据存储

原理图只标 U3 为 ATMEGA328，没有显示外部 EEPROM、Flash、SD 卡或其他存储器，也未注明 U3 内部程序存储和 SRAM 容量。

- 参数与网络：`controller=U3 ATMEGA328`；`external_eeprom=null`；`external_flash=null`；`sd_card=null`；`internal_flash_capacity=null`；`sram_capacity=null`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页完整原理图，仅 U3 主控，无独立存储器件

## 调试与烧录

### J1 ISP 下载接口

J1 ISP_Download 的 pin1=VCC、pin2=RESET、pin3=SCK、pin4=MISO、pin5=MOSI、pin6=GND；SCK/MISO/MOSI 分别连接 U3 PB5 pin17、PB4 pin16、PB3 pin15。

- 参数与网络：`pin1=VCC`；`pin2=RESET`；`pin3=SCK -> U3 PB5 pin17`；`pin4=MISO -> U3 PB4 pin16`；`pin5=MOSI -> U3 PB3 pin15`；`pin6=GND`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页右上 J1 pin1-pin6 与 U3 PB3/PB4/PB5 同名网络

## 模拟电路

### 三路摇杆 ADC 映射

ADIN0 连接 U3 PC0/ADC0 pin23，ADIN1 连接 PC1/ADC1 pin24，ADIN2 连接 PC2/ADC2 pin25；PC3/ADC3 pin26、ADC6 pin19 与 ADC7 pin22 在本页未连接。

- 参数与网络：`adin0=P1 pin1 -> U3 PC0/ADC0 pin23`；`adin1=P1 pin2 -> U3 PC1/ADC1 pin24`；`adin2=P1 pin3 -> U3 PC2/ADC2 pin25`；`unused_adc=PC3/ADC3 pin26,ADC6 pin19,ADC7 pin22`
- 证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页 P1 ADIN0-2 到 U3 PC0/ADC0、PC1/ADC1、PC2/ADC2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Joystick 系统架构 | `controller=U3 ATMEGA328`；`analog_inputs=P1 ADIN0/ADIN1/ADIN2 -> ADC0/ADC1/ADC2`；`host_bus=PC4 SDA,PC5 SCL -> J2`；`debug=J1 ISP_Download`；`indicator=PD2 LED1 -> D1/R16`；`storage=null`；`rf=null`；`battery=null` |
| 接口 | J2 主 Grove 接口 | `connector=J2 IIC_Socket_4P`；`pin1=IIC_SCL`；`pin2=IIC_SDA`；`pin3=VCC`；`pin4=GND`；`assembly=Connected to Core` |
| 接口 | J3 备用未装接口 | `connector=J3 IIC_Socket_4P`；`pin1=IIC_SCL`；`pin2=IIC_SDA`；`pin3=VCC`；`pin4=GND`；`assembly=Not Mount`；`parallel_with=J2` |
| 总线 | ATMEGA328 至 Grove I2C | `controller=U3 ATMEGA328`；`sda=PC4 pin27 -> SDA -> R8 470R -> IIC_SDA`；`scl=PC5 pin28 -> SCL -> R7 470R -> IIC_SCL`；`connectors=J2,J3`；`pullups_shown=false` |
| 接口 | P1 Rocker 三针接口 | `pin1=ADIN0`；`pin2=ADIN1`；`pin3=ADIN2`；`power_pin=null`；`ground_pin=null` |
| 模拟电路 | 三路摇杆 ADC 映射 | `adin0=P1 pin1 -> U3 PC0/ADC0 pin23`；`adin1=P1 pin2 -> U3 PC1/ADC1 pin24`；`adin2=P1 pin3 -> U3 PC2/ADC2 pin25`；`unused_adc=PC3/ADC3 pin26,ADC6 pin19,ADC7 pin22` |
| 模拟电路 | X/Y/Z 与 ADIN0/ADIN1/ADIN2 对应关系 | `documented_axes=X analog,Y analog,Z button`；`adin0_semantic=null`；`adin1_semantic=null`；`adin2_semantic=null`；`rocker_internal_schematic=null` |
| 总线地址 | I2C 地址与寄存器协议 | `documented_i2c_address=0x52`；`documented_register=0x52`；`documented_length=3`；`documented_payload=X,Y,BTN`；`schematic_address=null`；`address_selector=null`；`firmware_version=null` |
| 其他事实 | 正文摇杆数据范围 | `documented_xy_range=0-255`；`documented_z_range=0/1`；`adc_scaling=null`；`center_value=null`；`dead_zone=null`；`axis_direction=null`；`button_active_level=null` |
| 电源 | VCC 供电路径 | `input=J2 pin3 VCC`；`mcu_supply=AVCC pin18,VCC pins4/6`；`mcu_ground=pins3/5/21`；`isp_supply=J1 pin1 VCC,pin6 GND`；`decoupling=C8 100nF`；`regulator=null`；`power_switch=null` |
| 电源 | Grove VCC 电压 | `documented_grove_supply=5V`；`schematic_net=VCC`；`schematic_voltage=null`；`input_range=null`；`tolerance=null` |
| 调试与烧录 | J1 ISP 下载接口 | `pin1=VCC`；`pin2=RESET`；`pin3=SCK -> U3 PB5 pin17`；`pin4=MISO -> U3 PB4 pin16`；`pin5=MOSI -> U3 PB3 pin15`；`pin6=GND` |
| 复位 | ATMEGA328 RESET | `mcu_pin=U3 PC6/RESET pin29`；`debug_pin=J1 pin2`；`external_pullup_shown=false`；`reset_cap_shown=false`；`reset_button_shown=false` |
| 时钟 | ATMEGA328 时钟连接 | `xtal1=PB6 pin7 no external connection`；`xtal2=PB7 pin8 no external connection`；`external_crystal=false`；`frequency=null` |
| GPIO 与控制信号 | PB0/PB1/PB2 固定下拉 | `pb0=pin12 via R17 10K to GND`；`pb1=pin13 via R18 10K to GND`；`pb2=pin14 via R19 10K to GND`；`external_connector=null` |
| GPIO 与控制信号 | 红色 LED 驱动 | `mcu_pin=U3 PD2 pin32`；`net=LED1`；`led=D1 红灯 0603`；`resistor=R16 1KΩ`；`return=GND` |
| 保护电路 | Grove 与 VCC 保护拓扑 | `vcc_path=J2 pin3 VCC -> U3/J1`；`signal_series=R7/R8 470R`；`fuse_shown=false`；`tvs_esd_shown=false`；`reverse_protection_shown=false`；`regulator_shown=false`；`level_shifter_shown=false` |
| 内存与 Flash | 程序与数据存储 | `controller=U3 ATMEGA328`；`external_eeprom=null`；`external_flash=null`；`sd_card=null`；`internal_flash_capacity=null`；`sram_capacity=null` |

## 待确认事项

- `analog.xyz-semantic-map`：正文称摇杆提供 X/Y 轴模拟偏移和 Z 轴按键数字输入；原理图只将 P1 三路标为 ADIN0、ADIN1、ADIN2，没有标出哪一路对应 X、Y 或 Z，也没有显示 Rocker 内部电位器与按键接法。（证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页左中仅显示 Rocker/P1/ADIN0-2，无 X/Y/Z 文字）
- `address.documented-0x52`：正文将设备地址列为 0x52，并以 JOYSTICK REG 0x52 描述一次读取 3 字节 X、Y、BTN；原理图没有打印 I2C 地址、寄存器地址、地址选择绑带或固件版本。（证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页 U3/J2 I2C 电路，整页无 0x52 或寄存器文字）
- `other.documented-output-values`：正文称 X/Y 偏移输出为 0-255、Z 按键输出为 0/1；原理图只确认 ATMEGA328 的三路 ADC 连接，不能确认 ADC 采样位宽、缩放、中心值、死区、方向、按键有效电平或输出字节编码。（证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页 P1 ADIN0-2 与 U3 ADC0-2；图中无数据格式或缩放参数）
- `power.documented-5v`：正文 Grove 管脚表将电源触点标为 5V；原理图仅使用 VCC 网络名并直接供给 ATMEGA328，没有标出 VCC 数值、允许范围、输入保护或电源容差。（证据：图 14dbfb9d33ff / 第 1 页 / 第 1 页 J2/J3 pin3 与 U3 电源脚均标 VCC，无电压数字）
- `review.xyz-map`：请通过摇杆 BOM、PCB 网表或固件确认 ADIN0/ADIN1/ADIN2 分别对应 X、Y、Z 的哪一路，以及 Z 按键有效电平。；原因：本页只给出 P1 三路 ADIN 编号，没有摇杆内部接法或轴名称。
- `review.i2c-protocol`：请用当前 ATMEGA328 固件或实机总线记录确认 7 位地址 0x52、寄存器 0x52、3 字节读取顺序及协议版本。；原因：原理图没有地址、寄存器或固件版本信息。
- `review.output-scaling`：请从固件确认 X/Y 的 0-255 缩放、中心值、死区、方向和 Z 按键 0/1 的有效电平。；原因：ADC 接线不能证明固件输出编码与机械方向。
- `review.vcc-voltage`：请以当前 U024 接口规范、BOM 或实板确认 J2 VCC 是否固定为 5V，以及允许输入范围和容差。；原因：原理图只标 VCC，且 VCC 直接供给 ATMEGA328，没有电压数字或稳压器。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `14dbfb9d33ff1332b9a92dc2a33aa4109bde9af9591947b66c367a7a640d79ca` | `https://static-cdn.m5stack.com/resource/docs/products/unit/joystick/joystick_sch_01.webp` |

---

源文档：`zh_CN/unit/joystick.md`

源文档 SHA-256：`b72b8452bd7d7a60fa7dafab7df15b9344963c7ba8459df71d48de334d7987ff`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
