# Unit Scales 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Scales |
| SKU | U108 |
| 产品 ID | `unit-scales-b8e4bdd6bf8a` |
| 源文档 | `zh_CN/unit/UNIT Scales.md` |

## 概述

Unit Scales 以 U1 STM32F030F4P6（原理图备注 XM1008F6P6）为主控，通过 J1 Grove 的 I2C_CLK/I2C_DATA 与外部主机通信。U2 HX711 连接 J3 四线称重桥，DOUT/PD_SCK 分别形成 HX711_SDA/HX711_CLK 并接到 U1 PA3/PA4，Q1 S8550 Y2 与 R1/R4 构成 HX711 模拟供电反馈。+5V 经 VR1 HT7333 生成 +3.3V，板上另有 SK6812 RGB、key 按键以及 J2 SWD 下载口。原理图没有标注 I2C 地址、称重量程、ADC 位数/增益/采样率或称重误差，这些正文参数需另行确认。

## 检索关键词

`Unit Scales`、`U108`、`STM32F030F4P6`、`XM1008F6P6`、`HX711`、`HT7333`、`S8550 Y2`、`SK6812`、`I2C`、`0x26`、`I2C_CLK`、`I2C_DATA`、`PA9`、`PA10`、`HX711_SDA`、`HX711_CLK`、`PA3`、`PA4`、`PA7 LED`、`PA2 key`、`SWCLK`、`SWDIO`、`NRST`、`BOOT0`、`Grove-4P(RED)`、`J1`、`J2 SIP-5`、`J3 SIP-4`、`RED WHITE BLUE GREEN`、`+5V`、`+3.3V`、`R6 R7 4.7K`、`R2 R3 4.7K`、`R1 20K`、`R4 8.2K`、`20kg load cell`、`24bit ADC`、`10SPS`、`tare button`、`weighing bridge`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6（备注 XM1008F6P6） | 主控 MCU，连接主机 I2C、HX711、RGB、按键、SWD、复位和 BOOT0 | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A3，U1 STM32F030F4P6（备注 XM1008F6P6），pins1-20 |
| U2 | HX711 | 称重桥模拟前端与 ADC，连接 J3、模拟电源反馈和 HX711_SDA/HX711_CLK | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 B3-C3，U2 HX711 pins1-16，VSUP/BASE/AVDD/VFB/AGND/VBG/INNA/INPA/INPB/INNB/PD_SCK/DOUT/XO/XI/RATE/DVDD |
| VR1 | HT7333 | 将 +5V 转换为 +3.3V 的稳压器 | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A2，VR1 HT7333，Vin/Vout/GND 与 C1/C3 |
| Q1 | S8550 Y2 | 由 HX711 BASE 控制、参与 AVDD/称重桥激励供电的 PNP 晶体管 | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 B3，Q1 S8550 Y2 位于 +3.3V、U2 BASE/AVDD 与 R1/R4 反馈网络 |
| J1 | Grove-4P(RED) | 主机 I2C 与电源接口，pin1 I2C_CLK、pin2 I2C_DATA、pin3 +5V、pin4 GND | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A1，J1 Grove-4P(RED) pins1-4 与 I2C_CLK/I2C_DATA/+5/GND |
| J2 | SIP-5 | +3.3V、SWCLK、SWDIO、NRST、GND 调试/下载接口 | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A4，J2 SIP-5 pins1-5 与 +3.3/SWCLK/SWDIO/NRST/GND |
| J3 | SIP-4 | 四线称重传感器接口，pin4 RED、pin3 WHITE、pin2 BLUE、pin1 GREEN | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 C2，J3 SIP-4 pins4/3/2/1 标注 RED/WHITE/BLUE/GREEN，并连接 U2 模拟前端网络 |
| LED1 | sk6812 | +5V 供电、由 U1 PA7/LED 网络驱动的可编程 RGB LED | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 B1，LED1 sk6812，VDD pin1、DOUT pin2、VSS pin3、DIN pin4 |
| SW1 | 未标注 | 按下将 key/PA2 接到 GND 的按键 | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 C1，SW1 位于 key 与 GND 之间 |
| R6,R7 | 4.7KΩ | I2C_DATA 与 I2C_CLK 到 +3.3V 的上拉电阻 | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A1，R6/R7 4.7KΩ 从 I2C_DATA/I2C_CLK 接 +3.3V |
| R2,R3 | 4.7KΩ | HX711_SDA 与 HX711_CLK 到 +3.3V 的上拉电阻 | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 C4，R2/R3 4.7KΩ 从 HX711_SDA/HX711_CLK 接 +3.3V |
| R1,R4,C5,C6 | 20KΩ / 8.2KΩ / 1uF / 1uF | HX711 AVDD/VFB/VBG 模拟电源反馈与旁路网络 | 图 ad6ae5355bea / 第 1 页 / 第 1 页网格 B3-C3，U2 左侧 Q1、R1 20KΩ、R4 8.2KΩ、C5/C6 1uF |

## 系统结构

### Unit Scales 系统架构

U1 STM32F030F4P6 作为主控，以 I2C 对外通信，以两线 HX711_SDA/HX711_CLK 连接 U2 HX711；U2 接 J3 四线称重桥并配有 Q1 模拟供电网络。VR1 生成 3.3V，LED1、SW1 和 J2 分别提供 RGB 状态、按键与 SWD 调试。

- 参数与网络：`controller=U1 STM32F030F4P6（备注 XM1008F6P6）`；`adc=U2 HX711`；`load_cell=J3 SIP-4`；`host_bus=I2C via J1`；`indicator=LED1 sk6812`；`button=SW1 key`；`debug=J2 SIP-5 SWD`；`power=+5V -> VR1 HT7333 -> +3.3V`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页完整 A1-C4，J1/VR1/U1/LED1/SW1/J3/U2/J2

## 核心器件

### STM32F030F4P6 关键引脚映射

U1 pin1 BOOT0 接 GND，pin4 NRST 接复位网络，pin5 VDDA 与 pin16 VDD 接 +3.3V，pin15 VSS 接 GND；PA2 pin8=key、PA3 pin9=HX711_SDA、PA4 pin10=HX711_CLK、PA7 pin13=LED、PA9 pin17=I2C_CLK、PA10 pin18=I2C_DATA、PA13 pin19=SWDIO、PA14 pin20=SWCLK。

- 参数与网络：`boot=pin1 BOOT0 -> GND`；`reset=pin4 NRST`；`analog_supply=pin5 VDDA -> +3.3V`；`digital_supply=pin16 VDD -> +3.3V`；`ground=pin15 VSS`；`key=pin8 PA2`；`hx711=pin9 PA3/HX711_SDA; pin10 PA4/HX711_CLK`；`led=pin13 PA7/LED`；`i2c=pin17 PA9/I2C_CLK; pin18 PA10/I2C_DATA`；`swd=pin19 PA13/SWDIO; pin20 PA14/SWCLK`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A3，U1 pins1-20 及左右网络标签

## 电源

### +5V 至 +3.3V 电源

J1 pin3 引入 +5V，连接 VR1 HT7333 Vin；VR1 Vout 输出 +3.3V，GND 端接地。C1 22uF 位于 +5V 输入侧，C3 22uF 位于 +3.3V 输出侧。

- 参数与网络：`input=J1 pin3 +5V`；`regulator=VR1 HT7333`；`output=+3.3V`；`input_cap=C1 22uF`；`output_cap=C3 22uF`；`ground=GND`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A1-A2，J1 +5、VR1 HT7333、C1/C3 与 +3.3

## 接口

### J1 Grove I2C 接口

J1 Grove-4P(RED) pin1=I2C_CLK、pin2=I2C_DATA、pin3=+5V、pin4=GND；R7 4.7KΩ 将 I2C_CLK 上拉到 +3.3V，R6 4.7KΩ 将 I2C_DATA 上拉到 +3.3V。

- 参数与网络：`connector=J1 Grove-4P(RED)`；`pin1=I2C_CLK -> U1 PA9 pin17`；`pin2=I2C_DATA -> U1 PA10 pin18`；`pin3=+5V`；`pin4=GND`；`clock_pullup=R7 4.7K to +3.3V`；`data_pullup=R6 4.7K to +3.3V`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A1 J1/R6/R7 与网格 A3 U1 PA9/PA10 同名网络

## 总线

### U1 与 HX711 两线接口

U2 DOUT pin12 形成 HX711_SDA 并连接 U1 PA3 pin9；U2 PD_SCK pin11 形成 HX711_CLK 并连接 U1 PA4 pin10。R2/R3 各 4.7KΩ 将两路网络上拉到 +3.3V。

- 参数与网络：`data=U2 pin12 DOUT/HX711_SDA -> U1 pin9 PA3`；`clock=U2 pin11 PD_SCK/HX711_CLK -> U1 pin10 PA4`；`data_pullup=R2 4.7K to +3.3V`；`clock_pullup=R3 4.7K to +3.3V`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 C3-C4 U2 DOUT/PD_SCK、R2/R3 与网格 A3 U1 PA3/PA4

## GPIO 与控制信号

### SW1 key 按键

U1 PA2 pin8 连接 key 网络，SW1 按下时将 key 接到 GND；原理图没有画出 key 的外部上拉、滤波或 ESD 器件。

- 参数与网络：`mcu_pin=U1 pin8 PA2`；`net=key`；`switch=SW1 to GND`；`external_pullup=null`；`filter=null`；`esd=null`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 C1 SW1/key/GND 与网格 A3 U1 PA2/key

### SK6812 状态灯

LED1 sk6812 VDD pin1 接 +5V、VSS pin3 接 GND、DIN pin4 接 LED 网络和 U1 PA7 pin13；DOUT pin2 标为 OUT 并带未连接标记。

- 参数与网络：`reference=LED1 sk6812`；`supply=pin1 VDD -> +5V`；`ground=pin3 VSS -> GND`；`data_in=pin4 DIN/LED <- U1 pin13 PA7`；`data_out=pin2 DOUT/OUT -> NC`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 B1 LED1 sk6812 pins1-4 与网格 A3 U1 PA7/LED

## 时钟

### U1 时钟器件

U1 PF0/OSC_IN pin2 与 PF1/OSC_OUT pin3 在本页没有连接外部晶振、谐振器或负载电容，原理图未显示独立时钟器件。

- 参数与网络：`osc_in=U1 pin2 PF0/OSC_IN unconnected`；`osc_out=U1 pin3 PF1/OSC_OUT unconnected`；`external_crystal=null`；`load_capacitors=null`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A3，U1 pins2/3 PF0/OSC_IN 与 PF1/OSC_OUT 无外接线路

## 复位

### U1 复位与启动配置

U1 NRST pin4 通过 R8 10KΩ 上拉到 +3.3V，并由 C2 1uF 接 GND，同时引至 J2 pin4；BOOT0 pin1 直接接 GND。

- 参数与网络：`reset_pin=U1 pin4 NRST`；`pullup=R8 10K to +3.3V`；`capacitor=C2 1uF to GND`；`debug_pin=J2 pin4`；`boot0=U1 pin1 -> GND`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A3-A4，U1 BOOT0/NRST、C2、R8、J2 pin4 与 GND/+3.3V

## 保护电路

### Grove 与称重接口保护边界

J1 的 +5V、I2C_CLK、I2C_DATA 以及 J3 的四线称重桥均直接进入电源、上拉或模拟网络；本页没有显示保险丝、反接保护、TVS/ESD 二极管或共模滤波器。

- 参数与网络：`interfaces=J1,J3`；`fuse=null`；`reverse_protection=null`；`tvs_esd=null`；`common_mode_filter=null`；`i2c_series_resistors=null`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页完整 J1 与 J3 外部接口路径，未见专用保护符号

## 调试与烧录

### J2 SWD 下载接口

J2 SIP-5 pin1=+3.3V、pin2=SWCLK、pin3=SWDIO、pin4=NRST、pin5=GND；SWCLK/SWDIO/NRST 分别连接 U1 PA14 pin20、PA13 pin19、NRST pin4。

- 参数与网络：`pin1=+3.3V`；`pin2=SWCLK -> U1 PA14 pin20`；`pin3=SWDIO -> U1 PA13 pin19`；`pin4=NRST -> U1 pin4`；`pin5=GND`；`interface=SWD`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A4 J2 SIP-5、R8 与网格 A3 U1 SWCLK/SWDIO/NRST

## 模拟电路

### HX711 模拟与数字电源

U2 VSUP pin1 与 DVDD pin16 接 +3.3V；BASE pin2 驱动 Q1 S8550 Y2，Q1 参与 AVDD pin3 输出。R1 20KΩ 与 R4 8.2KΩ 构成 AVDD 至 GND 的反馈分压并接 VFB pin4，C5 1uF 位于模拟供电节点，C6 1uF 连接 VBG pin6 的旁路网络。

- 参数与网络：`adc=U2 HX711`；`supply=VSUP pin1,DVDD pin16 -> +3.3V`；`pass_transistor=Q1 S8550 Y2 via BASE pin2`；`analog_output=AVDD pin3`；`feedback=R1 20K,R4 8.2K -> VFB pin4`；`bypass=C5 1uF,C6 1uF/VBG pin6`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 B3-C3，Q1/U2 pins1-6/R1/R4/C5/C6

### J3 四线称重桥输入

J3 SIP-4 依次将 pin4 RED、pin3 WHITE、pin2 BLUE、pin1 GREEN 引入 HX711 模拟网络；图中可见这些线路连接 AVDD/AGND 与 INNA/INPA 输入支路，GREEN 路包含 R5 1KΩ，输入网络另配置 C7 100nF。

- 参数与网络：`connector=J3 SIP-4`；`pin4=RED`；`pin3=WHITE`；`pin2=BLUE`；`pin1=GREEN`；`adc_inputs=U2 INNA pin7,INPA pin8`；`series_resistor=R5 1K on GREEN path`；`filter=C7 100nF`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 C2-C3，J3 RED/WHITE/BLUE/GREEN 至 U2 AVDD/AGND/INNA/INPA，R5/C7

### HX711 B 通道连接

U2 INPB pin9 与 INNB pin10 在原理图右侧汇接到 GND，因此板级称重输入使用 A 通道 INPA/INNA，B 通道没有引到 J3。

- 参数与网络：`channel_a=INNA pin7,INPA pin8 -> J3 network`；`channel_b_positive=INPB pin9 -> GND`；`channel_b_negative=INNB pin10 -> GND`；`external_channel_b=false`
- 证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 C3，U2 pins9/10 INPB/INNB 右侧公共节点与 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Scales 系统架构 | `controller=U1 STM32F030F4P6（备注 XM1008F6P6）`；`adc=U2 HX711`；`load_cell=J3 SIP-4`；`host_bus=I2C via J1`；`indicator=LED1 sk6812`；`button=SW1 key`；`debug=J2 SIP-5 SWD`；`power=+5V -> VR1 HT7333 -> +3.3V` |
| 电源 | +5V 至 +3.3V 电源 | `input=J1 pin3 +5V`；`regulator=VR1 HT7333`；`output=+3.3V`；`input_cap=C1 22uF`；`output_cap=C3 22uF`；`ground=GND` |
| 核心器件 | STM32F030F4P6 关键引脚映射 | `boot=pin1 BOOT0 -> GND`；`reset=pin4 NRST`；`analog_supply=pin5 VDDA -> +3.3V`；`digital_supply=pin16 VDD -> +3.3V`；`ground=pin15 VSS`；`key=pin8 PA2`；`hx711=pin9 PA3/HX711_SDA; pin10 PA4/HX711_CLK`；`led=pin13 PA7/LED`；`i2c=pin17 PA9/I2C_CLK; pin18 PA10/I2C_DATA`；`swd=pin19 PA13/SWDIO; pin20 PA14/SWCLK` |
| 接口 | J1 Grove I2C 接口 | `connector=J1 Grove-4P(RED)`；`pin1=I2C_CLK -> U1 PA9 pin17`；`pin2=I2C_DATA -> U1 PA10 pin18`；`pin3=+5V`；`pin4=GND`；`clock_pullup=R7 4.7K to +3.3V`；`data_pullup=R6 4.7K to +3.3V` |
| 总线 | U1 与 HX711 两线接口 | `data=U2 pin12 DOUT/HX711_SDA -> U1 pin9 PA3`；`clock=U2 pin11 PD_SCK/HX711_CLK -> U1 pin10 PA4`；`data_pullup=R2 4.7K to +3.3V`；`clock_pullup=R3 4.7K to +3.3V` |
| 模拟电路 | HX711 模拟与数字电源 | `adc=U2 HX711`；`supply=VSUP pin1,DVDD pin16 -> +3.3V`；`pass_transistor=Q1 S8550 Y2 via BASE pin2`；`analog_output=AVDD pin3`；`feedback=R1 20K,R4 8.2K -> VFB pin4`；`bypass=C5 1uF,C6 1uF/VBG pin6` |
| 模拟电路 | J3 四线称重桥输入 | `connector=J3 SIP-4`；`pin4=RED`；`pin3=WHITE`；`pin2=BLUE`；`pin1=GREEN`；`adc_inputs=U2 INNA pin7,INPA pin8`；`series_resistor=R5 1K on GREEN path`；`filter=C7 100nF` |
| 模拟电路 | HX711 B 通道连接 | `channel_a=INNA pin7,INPA pin8 -> J3 network`；`channel_b_positive=INPB pin9 -> GND`；`channel_b_negative=INNB pin10 -> GND`；`external_channel_b=false` |
| GPIO 与控制信号 | SW1 key 按键 | `mcu_pin=U1 pin8 PA2`；`net=key`；`switch=SW1 to GND`；`external_pullup=null`；`filter=null`；`esd=null` |
| GPIO 与控制信号 | SK6812 状态灯 | `reference=LED1 sk6812`；`supply=pin1 VDD -> +5V`；`ground=pin3 VSS -> GND`；`data_in=pin4 DIN/LED <- U1 pin13 PA7`；`data_out=pin2 DOUT/OUT -> NC` |
| 调试与烧录 | J2 SWD 下载接口 | `pin1=+3.3V`；`pin2=SWCLK -> U1 PA14 pin20`；`pin3=SWDIO -> U1 PA13 pin19`；`pin4=NRST -> U1 pin4`；`pin5=GND`；`interface=SWD` |
| 复位 | U1 复位与启动配置 | `reset_pin=U1 pin4 NRST`；`pullup=R8 10K to +3.3V`；`capacitor=C2 1uF to GND`；`debug_pin=J2 pin4`；`boot0=U1 pin1 -> GND` |
| 时钟 | U1 时钟器件 | `osc_in=U1 pin2 PF0/OSC_IN unconnected`；`osc_out=U1 pin3 PF1/OSC_OUT unconnected`；`external_crystal=null`；`load_capacitors=null` |
| 保护电路 | Grove 与称重接口保护边界 | `interfaces=J1,J3`；`fuse=null`；`reverse_protection=null`；`tvs_esd=null`；`common_mode_filter=null`；`i2c_series_resistors=null` |
| 总线地址 | 正文中的 I2C 地址 0x26 | `documented_address=0x26`；`controller=U1 STM32F030F4P6`；`scl=PA9/I2C_CLK`；`sda=PA10/I2C_DATA`；`schematic_address=null`；`address_selector=null` |
| 模拟电路 | 正文中的 HX711 采集参数 | `adc=U2 HX711`；`documented_resolution=24bit`；`documented_gain=32,64,128`；`documented_rate=10SPS`；`schematic_resolution=null`；`schematic_gain=null`；`rate_setting_text=null` |
| 传感器 | 正文中的 20kg 量程与误差 | `documented_range=0-20kg`；`documented_error_points=50g,100g,250g,500g,1000g`；`connector=J3 RED/WHITE/BLUE/GREEN`；`sensor_model=null`；`rated_output=null`；`calibration=null`；`test_conditions=null` |

## 待确认事项

- `address.documented-i2c-address`：产品正文标称 Unit Scales 的 I2C 地址为 0x26；本页原理图只显示 U1 PA9/PA10 与 J1 的 I2C_CLK/I2C_DATA 连接，没有地址电阻、拨码配置、地址文字或固件寄存器信息。（证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 A1/A3 J1、R6/R7、U1 PA9/PA10，图中无 0x26 或地址配置）
- `analog.documented-hx711-performance`：产品正文称 HX711 为 24bit ADC，支持 32/64/128 增益并以 10SPS 输出；原理图确认 U2 型号与 RATE/XI/XO/输入连接，但没有打印位数、增益、采样率或固件配置。（证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 B3-C3 U2 HX711，图中无 24bit/增益/SPS 文字）
- `sensor.documented-load-range-error`：产品正文称集成 0-20kg 称重传感器，并给出 50g 至 1000g 的绝对/相对误差表；本页原理图只显示 J3 四线桥接线，没有传感器型号、额定量程、灵敏度、激励电压、校准系数或误差条件。（证据：图 ad6ae5355bea / 第 1 页 / 第 1 页网格 C2-C3 J3 与 HX711 模拟网络，图中无传感器规格或误差表）
- `review.i2c-address`：请用 U108 当前内置固件、通信协议或 I2C 扫描确认默认地址 0x26 及地址修改/持久化规则。；原因：板级原理图没有地址文字或硬件地址配置。
- `review.hx711-performance`：请用 HX711 料号资料和当前固件配置确认 ADC 位数、实际增益、RATE 状态与输出采样率。；原因：原理图未打印 24bit、32/64/128 增益或 10SPS 配置结果。
- `review.load-cell-rating`：请用量产称重传感器规格书和校准/测试记录确认 0-20kg 量程、灵敏度、激励条件与正文误差数据。；原因：原理图只显示四线桥连接，不能证明机械量程和整机测量误差。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ad6ae5355bea90eed10b704b0877f2a79d7fd914ad34fd9358d758c8b8976c15` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/592/Sch_UNIT-Scales_sch_01.png` |

---

源文档：`zh_CN/unit/UNIT Scales.md`

源文档 SHA-256：`584ce86717ba8017c28a1b02edced4a510fcca6372928ea91502ab1096a65129`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
