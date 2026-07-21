# Module DCMotor 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module DCMotor |
| SKU | M021 |
| 产品 ID | `module-dcmotor-fbc738802491` |
| 源文档 | `zh_CN/module/lego_plus.md` |

## 概述

Module DCMotor 以 U2 ATMEGA328 为控制器，通过 U3、U4 两颗 L293DD 提供四路直流电机 H 桥输出，并从 P2 至 P5 六针接口同时连接电机电源线、编码器 A/B、+5V 和 GND。P1 外部 VCC 经 U1 LM2596SX-5.0/NOPB、L1 和滤波电容生成 +5V，+5V 为 MCU 逻辑、L293DD 逻辑与编码器接口供电，VCC 直接供给 L293DD 电机功率级。J4 M5Stack_BUS 通过 470Ω 电阻连接 SDA、SCL 和 RESET/EN，J2、J3 另外提供两组四针 I2C 扩展接口。

## 检索关键词

`Module DCMotor`、`M021`、`ATMEGA328`、`L293DD`、`LM2596SX-5.0/NOPB`、`I2C`、`0x56`、`VCC`、`+5V`、`M1+`、`M1-`、`M2+`、`M2-`、`M3+`、`M3-`、`M4+`、`M4-`、`M1A`、`M1B`、`M2A`、`M2B`、`M3A`、`M3B`、`M4A`、`M4B`、`GPIO21`、`GPIO22`、`M5Stack_BUS`、`IIC_Socket_4P`、`16MHz`、`ISP_Download`、`ZH1.5-6P`、`XT30`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ATMEGA328 | I2C 从机、四路电机方向控制和四组编码器输入控制器 | 图 89e80d158f09 / 第 1 页 / 页面中央 U2 ATMEGA328，标注 M1-M4 控制/编码器网络、SDA/SCL、RESET、ISP 与晶振引脚 |
| U3,U4 | L293DD | 四路直流电机 H 桥驱动器，U3 驱动 Motor 1/2，U4 驱动 Motor 3/4 | 图 89e80d158f09 / 第 1 页 / 页面下中 U3/U4 L293DD，分别连接 M1/M2 与 M3/M4 的输入、输出、VCC、+5V 和 GND |
| U1 | LM2596SX-5.0/NOPB | VCC 至 +5V 的固定输出降压稳压器 | 图 89e80d158f09 / 第 1 页 / 页面左上 U1 LM2596SX-5.0/NOPB，VIN/ON-OFF 接 VCC，OUT 经 L1 到 +5V，FB 接 +5V |
| P1 | Header 2 | 外部 VCC/GND 电机电源输入接口 | 图 89e80d158f09 / 第 1 页 / 页面左上 P1 Header 2，pin 1 连接 VCC，pin 2 连接 GND |
| P2-P5 | Header 6 | 四路电机与编码器六针接口 | 图 89e80d158f09 / 第 1 页 / 页面左下 P2 Motor1、P4 Motor2、P3 Motor3、P5 Motor4 Header 6，分别标注 Mx+/GND/MxA/MxB/+5V/Mx- |
| J2,J3 | IIC_Socket_4P | 两组并联的 GPIO22/SCL、GPIO21/SDA、+5V、GND I2C 扩展接口 | 图 89e80d158f09 / 第 1 页 / 页面右上 J2/J3 IIC_Socket_4P，pin 1 IIC_SCL/GPIO22、pin 2 IIC_SDA/GPIO21、pin 3 +5V、pin 4 GND |
| J4 | M5Stack_BUS | 30 针主机、电源、I2C、UART、GPIO 与 HPWR 接口 | 图 89e80d158f09 / 第 1 页 / 页面右下 J4 M5Stack_BUS，pin 1-30 标注 GND、GPIO、EN、3.3V、HPWR、+5V、BATTERY |
| J1 | ISP_Download | ATMEGA328 六针 ISP 下载接口 | 图 89e80d158f09 / 第 1 页 / 页面右上 J1 ISP_Download，pin 1-6 标注 VCC、RESET、SCK、MISO、MOSI、GND |
| Y1,C5,C6 | 16MHZ; 22pF; 22pF | ATMEGA328 16MHz 主时钟晶体与负载电容 | 图 89e80d158f09 / 第 1 页 / 页面中左 Y1 16MHZ 与 C5/C6 22pF，连接 U2 XTAL1/XTAL2 |
| R1,R2,R3 | 470Ω; 470Ω; 470Ω | SDA、SCL 和 RESET 到 M5-Bus GPIO21、GPIO22、EN 的串联电阻 | 图 89e80d158f09 / 第 1 页 / 页面中右 R1/R2/R3 470Ω，分别连接 SDA-GPIO21、SCL-GPIO22、RESET-EN |
| L1,C1-C4 | 0630/330; 100uF; 100uF; 100nF; 100nF | LM2596 输入和 +5V 输出滤波网络 | 图 89e80d158f09 / 第 1 页 / 页面左上 U1 周围 L1 0630/330、输入 C1 100uF/C3 100nF 与输出 C2 100uF/C4 100nF |

## 系统结构

### Module DCMotor 系统架构

U2 ATMEGA328 通过 U3/U4 两颗 L293DD 控制四路直流电机，并直接采集四组 A/B 编码器信号；P2-P5 各提供一组电机、编码器和 +5V/GND 接口。J4 通过 I2C 与主机通信，J2/J3扩展同一 I2C 总线，U1 从外部 VCC 生成 +5V 逻辑电源。

- 参数与网络：`controller=U2 ATMEGA328`；`motor_drivers=U3,U4 L293DD`；`motor_ports=P2-P5`；`host=J4 M5Stack_BUS`；`i2c_expansion=J2,J3`；`power_converter=U1 LM2596SX-5.0/NOPB`
- 证据：图 89e80d158f09 / 第 1 页 / 完整单页 P1/U1 电源、U2 MCU、U3/U4 驱动、P2-P5 电机接口与 J1-J4 主机接口

## 电源

### U1 VCC 至 +5V 转换

U1 VIN/pin 1 与 ON/OFF/pin 5 连接 VCC，GND/pin 3 接 GND，OUT/pin 2 经 L1 0630/330 输出 +5V，FB/pin 4 接 +5V；输入与输出各配置 100uF 和 100nF 电容。

- 参数与网络：`converter=U1 LM2596SX-5.0/NOPB`；`input=VCC`；`enable=ON/OFF pin 5 to VCC`；`inductor=L1 0630/330`；`output=+5V`；`input_filter=C1 100uF,C3 100nF`；`output_filter=C2 100uF,C4 100nF`
- 证据：图 89e80d158f09 / 第 1 页 / 页面左上 P1、U1、L1、C1-C4 与 VCC/+5V/GND 路径

### L293DD 电机与逻辑电源

U3/U4 Vs/pin 8 连接 VCC 电机功率轨，Vss/pin 20 与 EN_1/pin 1、EN_2/pin 9 连接 +5V，所有 GND 引脚接 GND；U2 AVCC/pin 18 与 VCC pin 4、pin 6 也连接 +5V。

- 参数与网络：`motor_rail=VCC -> U3/U4 Vs pin 8`；`logic_rail=+5V -> U3/U4 Vss pin 20 and EN pins 1,9`；`mcu_rail=+5V -> U2 AVCC pin 18,VCC pin 4,6`；`ground=U2/U3/U4 GND pins`
- 证据：图 89e80d158f09 / 第 1 页 / 页面下方 U3/U4 Vss/Vs/EN/GND 与页面中央 U2 AVCC/VCC/GND

## 接口

### J2/J3 I2C 扩展口

J2、J3 均为 IIC_Socket_4P，pin 1 连接 GPIO22/IIC_SCL，pin 2 连接 GPIO21/IIC_SDA，pin 3 连接 +5V/VCC，pin 4 连接 GND。

- 参数与网络：`J2=1:GPIO22/IIC_SCL,2:GPIO21/IIC_SDA,3:+5V/VCC,4:GND`；`J3=1:GPIO22/IIC_SCL,2:GPIO21/IIC_SDA,3:+5V/VCC,4:GND`
- 证据：图 89e80d158f09 / 第 1 页 / 页面右上 J2/J3 的 pin 1-4 与 IIC_SCL/IIC_SDA/VCC/GND 标注

### P2-P5 电机编码器接口

P2 Motor1 的 pin 1-6 为 M1+、GND、M1A、M1B、+5V、M1-；P4 Motor2 为 M2+、GND、M2A、M2B、+5V、M2-；P3 Motor3 为 M3+、GND、M3A、M3B、+5V、M3-；P5 Motor4 为 M4+、GND、M4A、M4B、+5V、M4-。

- 参数与网络：`P2=1:M1+,2:GND,3:M1A,4:M1B,5:+5V,6:M1-`；`P4=1:M2+,2:GND,3:M2A,4:M2B,5:+5V,6:M2-`；`P3=1:M3+,2:GND,3:M3A,4:M3B,5:+5V,6:M3-`；`P5=1:M4+,2:GND,3:M4A,4:M4B,5:+5V,6:M4-`
- 证据：图 89e80d158f09 / 第 1 页 / 页面左下 P2/P4 Motor1/2 与 P3/P5 Motor3/4 的 pin 1-6 标注

### J4 M5Stack_BUS 已用/标注针脚

J4 pin 1、3、5 连接 GND，pin 6 连接 EN/RESET，pin 12 连接 +3.3V，pin 17 连接 GPIO21/SDA，pin 18 连接 GPIO22/SCL，pin 28 连接 +5V；图中另标出 GPIO36、GPIO23、GPIO25、GPIO26、GPIO18、GPIO3、GPIO1、GPIO16、GPIO17、GPIO2、GPIO5、GPIO13、GPIO0、GPIO34、HPWR 与 BATTERY 针脚。

- 参数与网络：`used_pinout=1:GND,3:GND,5:GND,6:EN/RESET,12:+3.3V,17:GPIO21/SDA,18:GPIO22/SCL,28:+5V`；`connector=J4 M5Stack_BUS`
- 证据：图 89e80d158f09 / 第 1 页 / 页面右下 J4 M5Stack_BUS pin 1-30 与外部网络标注

## 总线

### U2、J4、J2/J3 I2C

U2 PC4/SDA/pin 27 经 R1 470Ω连接 GPIO21，并到 J4 pin 17 与 J2/J3 pin 2；U2 PC5/SCL/pin 28 经 R2 470Ω连接 GPIO22，并到 J4 pin 18 与 J2/J3 pin 1。

- 参数与网络：`sda=U2 PC4/pin 27 -> R1 470Ω -> GPIO21 -> J4 pin 17,J2/J3 pin 2`；`scl=U2 PC5/pin 28 -> R2 470Ω -> GPIO22 -> J4 pin 18,J2/J3 pin 1`；`logic_rail=+5V`；`pullups_visible=false`
- 证据：图 89e80d158f09 / 第 1 页 / U2 SDA/SCL、R1/R2、J4 GPIO21/22 与 J2/J3 IIC_SDA/IIC_SCL

## GPIO 与控制信号

### 四路 L293DD 控制映射

U3 的 INPUT1/INPUT2 控制 Motor1，INPUT3/INPUT4 控制 Motor2；U4 的 INPUT1/INPUT2 控制 Motor3，INPUT3/INPUT4 控制 Motor4。对应输出分别为 M1+/M1-、M2-/M2+、M3+/M3-、M4-/M4+。

- 参数与网络：`motor1=U3 INPUT1 M1_H,INPUT2 M1_L -> OUT1 M1+,OUT2 M1-`；`motor2=U3 INPUT3 M2_L,INPUT4 M2_H -> OUT3 M2-,OUT4 M2+`；`motor3=U4 INPUT1 M3_H,INPUT2 M3_L -> OUT1 M3+,OUT2 M3-`；`motor4=U4 INPUT3 M4_L,INPUT4 M4_H -> OUT3 M4-,OUT4 M4+`
- 证据：图 89e80d158f09 / 第 1 页 / 页面下中 U3/U4 INPUT1-4、OUTPUT1-4 与 M1-M4 H/L、+/− 网络标注

### 四组编码器输入映射

U2 PC0/pin 23、PC1/pin 24 接 M1A/M1B，PC2/pin 25、PC3/pin 26 接 M2A/M2B，PD1/pin 31 与 PD6/pin 10 接 M3A/M3B，PB4/pin 16 与 PB5/pin 17 接 M4A/M4B。

- 参数与网络：`motor1_encoder=M1A:PC0 pin 23,M1B:PC1 pin 24`；`motor2_encoder=M2A:PC2 pin 25,M2B:PC3 pin 26`；`motor3_encoder=M3A:PD1 pin 31,M3B:PD6 pin 10`；`motor4_encoder=M4A:PB4 pin 16,M4B:PB5 pin 17`
- 证据：图 89e80d158f09 / 第 1 页 / U2 左侧 PC0-PC3/PD1/PD6/PB4/PB5 与 M1A/B-M4A/B 外部网络标注

## 时钟

### U2 16MHz 时钟

Y1 标注 16MHZ，连接 U2 PB6/XTAL1 pin 7 与 PB7/XTAL2 pin 8；C5、C6 均为 22pF，并分别从两条晶振网络接至 GND。

- 参数与网络：`crystal=Y1 16MHZ`；`mcu_pins=PB6/XTAL1 pin 7,PB7/XTAL2 pin 8`；`load_capacitors=C5 22pF,C6 22pF`
- 证据：图 89e80d158f09 / 第 1 页 / 页面中左 Y1/C5/C6 与 U2 XTAL1/XTAL2

## 复位

### RESET 网络

U2 PC6/RESET pin 29 与 J1 pin 2 连接 RESET；RESET 经 R3 470Ω连接 J4 pin 6 EN。原理图未绘出 RESET 上拉电阻或对地电容。

- 参数与网络：`mcu_pin=U2 PC6/RESET pin 29`；`isp_pin=J1 pin 2`；`bus_path=RESET -> R3 470Ω -> J4 pin 6/EN`；`pullup_visible=false`；`capacitor_visible=false`
- 证据：图 89e80d158f09 / 第 1 页 / U2 RESET、J1 RESET 与中右 R3 470Ω/J4 EN

## 保护电路

### 电源与电机端口保护可见性

该页未绘出 P1 输入保险丝、TVS、反接保护或 P2-P5 电机端口的外部钳位器件。

- 参数与网络：`input_fuse_visible=false`；`input_tvs_visible=false`；`reverse_protection_visible=false`；`motor_external_clamps_visible=false`
- 证据：图 89e80d158f09 / 第 1 页 / 完整单页 P1/U1 输入及 U3/U4/P2-P5 电机输出外围

## 调试与烧录

### J1 ISP 下载接口

J1 pin 1 连接 VCC/+5V，pin 2 连接 RESET，pin 3 连接 SCK，pin 4 连接 MISO，pin 5 连接 MOSI，pin 6 连接 GND；对应 U2 RESET、PB5/SCK、PB4/MISO、PB3/MOSI。

- 参数与网络：`pinout=1:VCC/+5V,2:RESET,3:SCK,4:MISO,5:MOSI,6:GND`；`mcu_mapping=RESET:PC6 pin 29,SCK:PB5 pin 17,MISO:PB4 pin 16,MOSI:PB3 pin 15`
- 证据：图 89e80d158f09 / 第 1 页 / 页面右上 J1 ISP_Download 与 U2 RESET/SCK/MISO/MOSI 网络

## 其他事实

### 其他功能分区可见性

该页未绘出独立存储器、外部存储、音频器件、离散传感器或射频器件；编码器 A/B 信号直接由电机端口进入 U2 GPIO。

- 参数与网络：`external_storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`sensor_ic_visible=false`；`rf_visible=false`；`encoder_inputs=M1A/B,M2A/B,M3A/B,M4A/B`
- 证据：图 89e80d158f09 / 第 1 页 / 完整单页全部功能区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module DCMotor 系统架构 | `controller=U2 ATMEGA328`；`motor_drivers=U3,U4 L293DD`；`motor_ports=P2-P5`；`host=J4 M5Stack_BUS`；`i2c_expansion=J2,J3`；`power_converter=U1 LM2596SX-5.0/NOPB` |
| 电源 | VCC 输入电压范围 | `documented_range=6-12V`；`schematic_range_visible=false`；`confirmed_range=null`；`documented_connector=XT30 female`；`schematic_connector=P1 Header 2` |
| 电源 | U1 VCC 至 +5V 转换 | `converter=U1 LM2596SX-5.0/NOPB`；`input=VCC`；`enable=ON/OFF pin 5 to VCC`；`inductor=L1 0630/330`；`output=+5V`；`input_filter=C1 100uF,C3 100nF`；`output_filter=C2 100uF,C4 100nF` |
| 电源 | L293DD 电机与逻辑电源 | `motor_rail=VCC -> U3/U4 Vs pin 8`；`logic_rail=+5V -> U3/U4 Vss pin 20 and EN pins 1,9`；`mcu_rail=+5V -> U2 AVCC pin 18,VCC pin 4,6`；`ground=U2/U3/U4 GND pins` |
| 总线 | U2、J4、J2/J3 I2C | `sda=U2 PC4/pin 27 -> R1 470Ω -> GPIO21 -> J4 pin 17,J2/J3 pin 2`；`scl=U2 PC5/pin 28 -> R2 470Ω -> GPIO22 -> J4 pin 18,J2/J3 pin 1`；`logic_rail=+5V`；`pullups_visible=false` |
| 总线地址 | I2C 从机地址 | `documented_address=0x56`；`schematic_address_visible=false` |
| 接口 | J2/J3 I2C 扩展口 | `J2=1:GPIO22/IIC_SCL,2:GPIO21/IIC_SDA,3:+5V/VCC,4:GND`；`J3=1:GPIO22/IIC_SCL,2:GPIO21/IIC_SDA,3:+5V/VCC,4:GND` |
| 接口 | P2-P5 电机编码器接口 | `P2=1:M1+,2:GND,3:M1A,4:M1B,5:+5V,6:M1-`；`P4=1:M2+,2:GND,3:M2A,4:M2B,5:+5V,6:M2-`；`P3=1:M3+,2:GND,3:M3A,4:M3B,5:+5V,6:M3-`；`P5=1:M4+,2:GND,3:M4A,4:M4B,5:+5V,6:M4-` |
| GPIO 与控制信号 | 四路 L293DD 控制映射 | `motor1=U3 INPUT1 M1_H,INPUT2 M1_L -> OUT1 M1+,OUT2 M1-`；`motor2=U3 INPUT3 M2_L,INPUT4 M2_H -> OUT3 M2-,OUT4 M2+`；`motor3=U4 INPUT1 M3_H,INPUT2 M3_L -> OUT1 M3+,OUT2 M3-`；`motor4=U4 INPUT3 M4_L,INPUT4 M4_H -> OUT3 M4-,OUT4 M4+` |
| GPIO 与控制信号 | 四组编码器输入映射 | `motor1_encoder=M1A:PC0 pin 23,M1B:PC1 pin 24`；`motor2_encoder=M2A:PC2 pin 25,M2B:PC3 pin 26`；`motor3_encoder=M3A:PD1 pin 31,M3B:PD6 pin 10`；`motor4_encoder=M4A:PB4 pin 16,M4B:PB5 pin 17` |
| 调试与烧录 | J1 ISP 下载接口 | `pinout=1:VCC/+5V,2:RESET,3:SCK,4:MISO,5:MOSI,6:GND`；`mcu_mapping=RESET:PC6 pin 29,SCK:PB5 pin 17,MISO:PB4 pin 16,MOSI:PB3 pin 15` |
| 时钟 | U2 16MHz 时钟 | `crystal=Y1 16MHZ`；`mcu_pins=PB6/XTAL1 pin 7,PB7/XTAL2 pin 8`；`load_capacitors=C5 22pF,C6 22pF` |
| 复位 | RESET 网络 | `mcu_pin=U2 PC6/RESET pin 29`；`isp_pin=J1 pin 2`；`bus_path=RESET -> R3 470Ω -> J4 pin 6/EN`；`pullup_visible=false`；`capacitor_visible=false` |
| 接口 | J4 M5Stack_BUS 已用/标注针脚 | `used_pinout=1:GND,3:GND,5:GND,6:EN/RESET,12:+3.3V,17:GPIO21/SDA,18:GPIO22/SCL,28:+5V`；`connector=J4 M5Stack_BUS` |
| 保护电路 | 电源与电机端口保护可见性 | `input_fuse_visible=false`；`input_tvs_visible=false`；`reverse_protection_visible=false`；`motor_external_clamps_visible=false` |
| 其他事实 | 其他功能分区可见性 | `external_storage_visible=false`；`memory_visible=false`；`audio_visible=false`；`sensor_ic_visible=false`；`rf_visible=false`；`encoder_inputs=M1A/B,M2A/B,M3A/B,M4A/B` |

## 待确认事项

- `power.input-range`：原理图只标出 P1 VCC/GND 和 LM2596 输入网络，未打印输入电压范围；产品正文记载 6-12V，但无法仅据本页确认端点和容差。（证据：图 89e80d158f09 / 第 1 页 / 页面左上 P1 VCC/GND 与 U1 VIN 电源输入区域）
- `address.documented-i2c`：原理图未打印 I2C 从机地址；产品正文记载 0x56，但无法仅由本页硬件图确认固件地址。（证据：图 89e80d158f09 / 第 1 页 / U2 PC4/PC5 与 I2C 接口区域未见地址值或地址配置器件）
- `review.input-range`：Module DCMotor 的正式 VCC 输入范围是否确认为产品正文记载的 6-12V，P1 实际装配是否为 XT30 female？；原因：原理图仅将 P1 画为 Header 2 并标 VCC/GND，没有输入范围或 XT30 料号。
- `review.i2c-address`：Module DCMotor 当前固件的 I2C 从机地址是否确认为产品正文记载的 0x56？；原因：原理图只显示 SDA/SCL 物理连接，没有地址值、地址配置网络或固件定义。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `89e80d158f093423fb5f33e71e0418faa453fa06db07cce95b5b0514a690edb9` | `https://static-cdn.m5stack.com/resource/docs/products/module/lego_plus/lego_plus_sch_01.webp` |

---

源文档：`zh_CN/module/lego_plus.md`

源文档 SHA-256：`6fa381466900978aa88583bd9365230a3ccc7f4aa5dca9e629ccd68f6d4cf8f7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
