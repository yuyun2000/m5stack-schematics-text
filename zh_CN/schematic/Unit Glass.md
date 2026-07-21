# Unit Glass 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Glass |
| SKU | U158 |
| 产品 ID | `unit-glass-135ab40c2570` |
| 源文档 | `zh_CN/unit/Glass Unit.md` |

## 概述

Unit Glass 以 U3 STM32F030F4P6 为控制核心，通过 J2 的 SCL/SDA 接入外部 I2C 主机，并以 CS、RES、DC、SCK、MOSI 控制 J1 AFCO5-S24FIA-00 / SSD1309 OLED。+5V 输入分别经 U2 BL8075CB5TR33 生成 +3.3V，并经 U1 SGM6601YTNSG/TR 升压生成 +12.5V，两个电源域共同为 MCU 和 OLED 供电。板上包含 S1/S2 两个低有效按键、Q1 SS8050 Y1 低边驱动的 LS1 蜂鸣器、BOOT0 下拉、NRST RC 网络和 P1 SWD_5p 调试口。正文给出的 I2C 地址 0x3D、128x64 总分辨率和 128x56 透明区域未直接印在原理图上，需结合固件协议、显示模组资料或实测确认。

## 检索关键词

`Unit Glass`、`U158`、`STM32F030F4P6`、`AFCO5-S24FIA-00`、`SSD1309`、`SGM6601YTNSG/TR`、`BL8075CB5TR33`、`I2C`、`0x3D`、`SCL PA9`、`SDA PA10`、`CS PA2`、`RES PA3`、`DC PA6`、`SCK PA5`、`MOSI PA7`、`KEY_A PA0`、`KEY_B PA1`、`BEEP PB1`、`SWCLK PA14`、`SWDIO PA13`、`NRST`、`BOOT0`、`+5V`、`+3.3V`、`+12.5V`、`HY-2.0_IIC`、`SWD_5p`、`LS1 Buzzer`、`SS8050 Y1`、`128x64 OLED`、`128x56 transparent`、`R1 1.1MΩ`、`R2 120KΩ`、`R5 910KΩ`、`L1 10uH`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030F4P6 | I2C 从设备主控，读取按键、驱动蜂鸣器和 SSD1309，并提供 SWD/BOOT/复位连接 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 C2-C3，U3 STM32F030F4P6 pin1-pin20 |
| J1 | AFCO5-S24FIA-00 / SSD1309 | 透明 OLED 显示模组，接收 CS/RES/DC/SCK/MOSI 并使用 +3.3V 与 +12.5V 电源 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 A3-B3，J1 AFCO5-S24FIA-00、SSD1309、pin1-pin24 |
| U1 | SGM6601YTNSG/TR | +5V 输入、+12.5V 输出的 OLED 升压转换器 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 A1-A2，U1 SGM6601YTNSG/TR 与 +5V/+12.5V |
| U2 | BL8075CB5TR33 | 将 +5V 稳压为 +3.3V，供 MCU、OLED 逻辑和外围电路使用 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 B1-B2，U2 BL8075CB5TR33 |
| J2 | HY-2.0_IIC | 外部 I2C 与 +5V 电源 Grove 接口 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 B4，J2 HY-2.0_IIC pin1-pin4 |
| P1 | SWD_5p | 引出 +3.3V、SWCLK、SWDIO、NRST 和 GND 的调试/下载接口 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 A4，P1 SWD_5p |
| S1/S2 | SMT_SW_TS_015 | 分别将 KEY_A、KEY_B 按下接地的两个用户按键 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 C1-D1，S1/S2 SMT_SW_TS_015 |
| LS1 | Buzzer | 由 Q1 低边开关驱动的蜂鸣器 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 C4，LS1 Buzzer |
| Q1 | SS8050 Y1 | BEEP 控制的蜂鸣器 NPN 低边驱动晶体管 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 C4-D4，Q1 SS8050 Y1 |
| L1/D1 | 10uH / 1N4148WST4 | U1 升压级的储能电感和从 SW 节点到 +12.5V 的整流二极管 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 A1-A2，L1 10uH、D1 1N4148WST4 |
| R1/R2/C1 | 1.1MΩ / 120KΩ / 22pF | U1 +12.5V 输出到 FB 的反馈分压和前馈补偿网络 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 A2，R1 1.1MΩ、R2 120KΩ、C1 22pF 与 FB |
| C2/C3/C6/C7 | 1uF / 22uF / 1uF / 1uF | 两路电源转换器的输入输出滤波电容 | 图 0df8640150fa / 第 1 页 / 第 1 页 A1-A2/B1-B2，C2/C3/C6/C7 |
| R3/R4 | 10KΩ | SDA/SCL 到 +3.3V 的 I2C 上拉电阻 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 B4，R3/R4 10KΩ 与 SDA/SCL |
| R5/C8/C9/C10 | 910KΩ / 4.7uF / 10uF / 100nF | SSD1309 IREF、VCOMH 和 +12.5V VCC 偏置/去耦网络 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 B3，J1 pin21-pin23 与 R5/C8/C9/C10 |
| R7/R11 | 10KΩ | KEY_A 与 KEY_B 到 +3.3V 的按键上拉电阻 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 C1-D1，R7/R11 10KΩ |
| R8/R10/C12 | 10KΩ / 10KΩ / 100nF | BOOT0 下拉和 NRST 上拉/电容复位网络 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 C2，R8 BOOT0、R10/C12 NRST |
| R6/R9/C11/D2/D3 | 10Ω / 470Ω / 10uF / 1N4148WT / 1N4148WT | 蜂鸣器供电限流、基极耦合及感性/基极节点钳位保护网络 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 C4-D4，R6/R9/C11/D2/D3、LS1/Q1 |
| C4/C5/C13/C14 | 4.7uF / 100nF / 100nF / 100nF | OLED +3.3V 与 STM32 VDDA/VDD 的去耦电容 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 A3/C2-C3，C4/C5/C13/C14 |
| J3/J4/J5/J6 | 未标注 | 四个并联到 GND 的单点焊盘/测试连接 | 图 0df8640150fa / 第 1 页 / 第 1 页网格 D3，J3-J6 共接 GND |

## 系统结构

### Unit Glass 系统结构

U3 STM32F030F4P6 通过 J2 与外部 I2C 主机通信，控制 J1 SSD1309 OLED、读取 S1/S2，并经 Q1 驱动 LS1；U1/U2 分别提供 +12.5V 与 +3.3V，P1 提供 SWD。

- 参数与网络：`controller=U3 STM32F030F4P6`；`display=J1 AFCO5-S24FIA-00 / SSD1309`；`host_bus=J2 I2C`；`power=U1 +12.5V,U2 +3.3V`；`inputs=S1 KEY_A,S2 KEY_B`；`audio=LS1 via Q1`；`debug=P1 SWD_5p`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页完整原理图全部功能区

## 核心器件

### U3 STM32F030F4P6 关键引脚

U3 PA0 pin6=KEY_A、PA1 pin7=KEY_B、PA2 pin8=CS、PA3 pin9=RES、PA5 pin11=SCK、PA6 pin12=DC、PA7 pin13=MOSI、PB1 pin14=BEEP、PA9 pin17=SCL、PA10 pin18=SDA、PA13 pin19=SWDIO、PA14 pin20=SWCLK。

- 参数与网络：`PA0_pin6=KEY_A`；`PA1_pin7=KEY_B`；`PA2_pin8=CS`；`PA3_pin9=RES`；`PA5_pin11=SCK`；`PA6_pin12=DC`；`PA7_pin13=MOSI`；`PB1_pin14=BEEP`；`PA9_pin17=SCL`；`PA10_pin18=SDA`；`PA13_pin19=SWDIO`；`PA14_pin20=SWCLK`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 C2-C3，U3 pin6-pin20 网络标注

## 电源

### +5V 输入电源

J2 pin3 的 VCC 网络为 +5V，直接进入 U1 VIN/EN、U2 VIN/EN，并由 C3 22uF 与 C6 1uF 对地滤波。

- 参数与网络：`source=J2 pin3`；`net=+5V`；`loads=U1 VIN pin5/EN pin4; U2 VIN pin1/EN pin3`；`caps=C3 22uF,C6 1uF`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页 J2 +5V 与网格 A1/B1 U1/U2 输入

### U2 BL8075CB5TR33

U2 VIN pin1 与 EN pin3 接 +5V，GND pin2 接地，VOUT pin5 输出 +3.3V，NC pin4 未连接；C6/C7 各 1uF 位于输入/输出。

- 参数与网络：`input=+5V at pin1`；`enable=+5V at pin3`；`ground=pin2 GND`；`output=+3.3V at pin5`；`nc=pin4`；`input_cap=C6 1uF`；`output_cap=C7 1uF`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 B1-B2，U2/C6/C7

### U1 SGM6601YTNSG/TR 升压

U1 VIN pin5 与 EN pin4 接 +5V，SW pin1 接 L1/D1 开关节点，FB pin3 接反馈分压，GND pin2 接地；D1 后形成标注 +12.5V 的输出。

- 参数与网络：`input=+5V at VIN pin5`；`enable=+5V at EN pin4`；`switch=pin1 SW with L1 10uH/D1`；`feedback=pin3 FB`；`ground=pin2 GND`；`output=+12.5V`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 A1-A2，U1/L1/D1/+12.5V

### +12.5V 反馈与滤波

R1 1.1MΩ 从 +12.5V 接到 FB，R2 120KΩ 从 FB 接 GND，C1 22pF 跨接输出与 FB；C2 1uF 从 +12.5V 接 GND。

- 参数与网络：`upper_feedback=R1 1.1MΩ`；`lower_feedback=R2 120KΩ`；`feedforward=C1 22pF`；`output_cap=C2 1uF`；`rail=+12.5V`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 A2，R1/R2/C1/C2 与 FB/+12.5V

### J1 OLED 电源与偏置

J1 VDD pin5 接 +3.3V，并由 C4 4.7uF/C5 100nF 去耦；VCC pin23 接 +12.5V，并由 C9 10uF/C10 100nF 去耦；IREF pin21 经 R5 910KΩ 接 GND，VCOMH pin22 经 C8 4.7uF 接 GND。

- 参数与网络：`logic_supply=J1 pin5 VDD +3.3V`；`logic_caps=C4 4.7uF,C5 100nF`；`panel_supply=J1 pin23 VCC +12.5V`；`panel_caps=C9 10uF,C10 100nF`；`iref=J1 pin21 via R5 910KΩ to GND`；`vcomh=J1 pin22 via C8 4.7uF to GND`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 A3-B3，J1 pin5/pin21-pin23 与 C4/C5/R5/C8-C10

## 接口

### J2 HY-2.0_IIC

J2 pin1=IIC_SCL、pin2=IIC_SDA、pin3=VCC/+5V、pin4=GND；SCL/SDA 连接 U3 PA9/PA10，+5V 为板上电源输入。

- 参数与网络：`pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC / +5V`；`pin_4=GND`；`controller_scl=U3 PA9 pin17`；`controller_sda=U3 PA10 pin18`；`power_direction=input`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 B4 J2 与 U3 PA9/PA10 同名 SCL/SDA 网络

## 总线

### STM32 到 SSD1309 控制总线

U3 PA2/PA3/PA6/PA5/PA7 分别通过 CS、RES、DC、SCK、MOSI 连接 J1 pin8/pin9/pin10/pin13/pin14；图中没有从 OLED 返回 MCU 的 MISO 数据线。

- 参数与网络：`chip_select=U3 PA2 pin8 -> CS -> J1 pin8`；`reset=U3 PA3 pin9 -> RES -> J1 pin9`；`data_command=U3 PA6 pin12 -> DC -> J1 pin10`；`clock=U3 PA5 pin11 -> SCK -> J1 D0 pin13`；`data=U3 PA7 pin13 -> MOSI -> J1 D1 pin14`；`miso_shown=false`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页 U3 CS/RES/DC/SCK/MOSI 与 J1 pin8-pin14

### 外部主机 I2C 总线

J2 SCL/SDA 分别连接 U3 PA9 pin17/PA10 pin18，R4/R3 各 10KΩ 将 SCL/SDA 上拉到 +3.3V；外部主机为控制器，U3 为板上设备。

- 参数与网络：`controller=external host via J2`；`device=U3 STM32F030F4P6 firmware`；`scl=J2.1/U3 PA9 pin17/R4 10KΩ to +3.3V`；`sda=J2.2/U3 PA10 pin18/R3 10KΩ to +3.3V`；`logic_rail=+3.3V`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 B4 R3/R4/J2 与网格 C3 U3 SCL/SDA

## GPIO 与控制信号

### S1/S2 用户按键

S1 按下将 KEY_A/U3 PA0 pin6 接 GND，R7 10KΩ 上拉到 +3.3V；S2 按下将 KEY_B/U3 PA1 pin7 接 GND，R11 10KΩ 上拉到 +3.3V。

- 参数与网络：`key_a=S1 to GND,R7 10KΩ to +3.3V,U3 PA0 pin6`；`key_b=S2 to GND,R11 10KΩ to +3.3V,U3 PA1 pin7`；`active_level=low`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 C1-D1 S1/R7 KEY_A、S2/R11 KEY_B 与 U3 PA0/PA1

### U3 BOOT0

U3 BOOT0 pin1 经 R8 10KΩ 下拉到 GND，原理图未显示 BOOT 按键或可选跳线。

- 参数与网络：`mcu_pin=U3 BOOT0 pin1`；`pulldown=R8 10KΩ to GND`；`boot_switch_shown=false`；`boot_jumper_shown=false`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 C2，R8/BOOT0/U3 pin1

## 时钟

### U3 时钟

U3 PF0/OSC_IN pin2 与 PF1/OSC_OUT pin3 在页面未连接，完整原理图未显示晶振、谐振器或外部振荡器。

- 参数与网络：`osc_in=U3 pin2 no visible connection`；`osc_out=U3 pin3 no visible connection`；`crystal_shown=false`；`external_oscillator_shown=false`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 C2 U3 PF0/OSC_IN、PF1/OSC_OUT 与完整图

## 复位

### U3 NRST

U3 NRST pin4、P1 pin4 和 NRST 网络相连，R10 10KΩ 上拉到 +3.3V，C12 100nF 对地；P1 可外部拉动复位。

- 参数与网络：`mcu_pin=U3 NRST pin4`；`pullup=R10 10KΩ to +3.3V`；`capacitor=C12 100nF to GND`；`debug_pin=P1 pin4 NRST`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 C2 U3 NRST/R10/C12 与网格 A4 P1 NRST

## 保护电路

### 蜂鸣器驱动保护

D2 1N4148WT 跨接蜂鸣器高端与 Q1 集电极节点，D3 1N4148WT 从 Q1 基极耦合节点接 GND，形成负载与基极节点的二极管钳位。

- 参数与网络：`flyback_diode=D2 1N4148WT across LS1 path`；`base_clamp=D3 1N4148WT to GND`；`protected_stage=Q1/LS1`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 C4-D4，D2/D3 与 LS1/Q1

### J2 外部接口保护

J2 的 SCL、SDA、+5V 和 GND 路径未画 TVS、ESD 阵列、保险丝或反接保护；SCL/SDA 仅配置 R4/R3 上拉。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`signal_components=R4 SCL pullup,R3 SDA pullup`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 B4 J2 至 U3/U1/U2 的完整路径

## 关键网络

### +5V、+3.3V 与 +12.5V

+5V 来自 J2 并进入 U1/U2；+3.3V 由 U2 输出，供 U3、OLED VDD、I2C/按键/复位上拉和蜂鸣器；+12.5V 由 U1 输出，供 OLED VCC。

- 参数与网络：`5v_nodes=J2.3,U1 VIN/EN,U2 VIN/EN,C3,C6`；`3v3_nodes=U2 VOUT,U3 VDDA/VDD,J1 VDD,R3/R4/R7/R10/R11,R6,P1.1`；`12v5_nodes=U1 boost output,J1 VCC pin23,C2,C9,C10`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页完整 +5V/+3.3V/+12.5V 网络

## 内存与 Flash

### 存储器

完整原理图未显示外部 Flash、EEPROM、RAM、SD 卡或其他存储器；U3 芯片内部存储容量未在页面标注。

- 参数与网络：`external_flash_shown=false`；`eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false`；`internal_capacity_printed=false`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页完整图无存储器件，U3 仅标 STM32F030F4P6

## 音频

### LS1 蜂鸣器驱动

U3 PB1 pin14 的 BEEP 经 R9 470Ω 和 C11 10uF 串联耦合到 Q1 基极，Q1 SS8050 Y1 发射极接 GND、集电极低边驱动 LS1；LS1 高端经 R6 10Ω 接 +3.3V。

- 参数与网络：`controller=U3 PB1 pin14`；`net=BEEP`；`base_path=R9 470Ω -> C11 10uF -> Q1 base`；`transistor=Q1 SS8050 Y1`；`load=LS1 Buzzer`；`supply=+3.3V via R6 10Ω`；`switching=low-side`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 C3-D4，U3 BEEP/R9/C11/Q1/LS1/R6

## 调试与烧录

### P1 SWD_5p

P1 pin1=VCC/+3.3V、pin2=SWCLK、pin3=SWDIO、pin4=RST/NRST、pin5=GND；SWCLK/SWDIO 分别连接 U3 PA14 pin20/PA13 pin19。

- 参数与网络：`pin_1=+3.3V`；`pin_2=SWCLK/U3 PA14 pin20`；`pin_3=SWDIO/U3 PA13 pin19`；`pin_4=NRST/U3 pin4`；`pin_5=GND`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 A4 P1 SWD_5p 与网格 C3 U3 SWCLK/SWDIO

### J3-J6 GND 焊盘

J3、J4、J5、J6 四个单点连接在页面底部并联到 GND，未标注其他信号。

- 参数与网络：`references=J3,J4,J5,J6`；`net=GND`；`signal_labels=null`
- 证据：图 0df8640150fa / 第 1 页 / 第 1 页网格 D3，J3-J6 与 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Glass 系统结构 | `controller=U3 STM32F030F4P6`；`display=J1 AFCO5-S24FIA-00 / SSD1309`；`host_bus=J2 I2C`；`power=U1 +12.5V,U2 +3.3V`；`inputs=S1 KEY_A,S2 KEY_B`；`audio=LS1 via Q1`；`debug=P1 SWD_5p` |
| 核心器件 | U3 STM32F030F4P6 关键引脚 | `PA0_pin6=KEY_A`；`PA1_pin7=KEY_B`；`PA2_pin8=CS`；`PA3_pin9=RES`；`PA5_pin11=SCK`；`PA6_pin12=DC`；`PA7_pin13=MOSI`；`PB1_pin14=BEEP`；`PA9_pin17=SCL`；`PA10_pin18=SDA`；`PA13_pin19=SWDIO`；`PA14_pin20=SWCLK` |
| 电源 | +5V 输入电源 | `source=J2 pin3`；`net=+5V`；`loads=U1 VIN pin5/EN pin4; U2 VIN pin1/EN pin3`；`caps=C3 22uF,C6 1uF` |
| 电源 | U2 BL8075CB5TR33 | `input=+5V at pin1`；`enable=+5V at pin3`；`ground=pin2 GND`；`output=+3.3V at pin5`；`nc=pin4`；`input_cap=C6 1uF`；`output_cap=C7 1uF` |
| 电源 | U1 SGM6601YTNSG/TR 升压 | `input=+5V at VIN pin5`；`enable=+5V at EN pin4`；`switch=pin1 SW with L1 10uH/D1`；`feedback=pin3 FB`；`ground=pin2 GND`；`output=+12.5V` |
| 电源 | +12.5V 反馈与滤波 | `upper_feedback=R1 1.1MΩ`；`lower_feedback=R2 120KΩ`；`feedforward=C1 22pF`；`output_cap=C2 1uF`；`rail=+12.5V` |
| 电源 | J1 OLED 电源与偏置 | `logic_supply=J1 pin5 VDD +3.3V`；`logic_caps=C4 4.7uF,C5 100nF`；`panel_supply=J1 pin23 VCC +12.5V`；`panel_caps=C9 10uF,C10 100nF`；`iref=J1 pin21 via R5 910KΩ to GND`；`vcomh=J1 pin22 via C8 4.7uF to GND` |
| 总线 | STM32 到 SSD1309 控制总线 | `chip_select=U3 PA2 pin8 -> CS -> J1 pin8`；`reset=U3 PA3 pin9 -> RES -> J1 pin9`；`data_command=U3 PA6 pin12 -> DC -> J1 pin10`；`clock=U3 PA5 pin11 -> SCK -> J1 D0 pin13`；`data=U3 PA7 pin13 -> MOSI -> J1 D1 pin14`；`miso_shown=false` |
| 接口 | J2 HY-2.0_IIC | `pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC / +5V`；`pin_4=GND`；`controller_scl=U3 PA9 pin17`；`controller_sda=U3 PA10 pin18`；`power_direction=input` |
| 总线 | 外部主机 I2C 总线 | `controller=external host via J2`；`device=U3 STM32F030F4P6 firmware`；`scl=J2.1/U3 PA9 pin17/R4 10KΩ to +3.3V`；`sda=J2.2/U3 PA10 pin18/R3 10KΩ to +3.3V`；`logic_rail=+3.3V` |
| 总线地址 | Unit Glass I2C 地址 | `documented_address=0x3D`；`address_width=7-bit`；`i2c_endpoint=U3 firmware`；`address_printed_on_schematic=false`；`address_strap_shown=false` |
| GPIO 与控制信号 | S1/S2 用户按键 | `key_a=S1 to GND,R7 10KΩ to +3.3V,U3 PA0 pin6`；`key_b=S2 to GND,R11 10KΩ to +3.3V,U3 PA1 pin7`；`active_level=low` |
| 音频 | LS1 蜂鸣器驱动 | `controller=U3 PB1 pin14`；`net=BEEP`；`base_path=R9 470Ω -> C11 10uF -> Q1 base`；`transistor=Q1 SS8050 Y1`；`load=LS1 Buzzer`；`supply=+3.3V via R6 10Ω`；`switching=low-side` |
| 保护电路 | 蜂鸣器驱动保护 | `flyback_diode=D2 1N4148WT across LS1 path`；`base_clamp=D3 1N4148WT to GND`；`protected_stage=Q1/LS1` |
| 复位 | U3 NRST | `mcu_pin=U3 NRST pin4`；`pullup=R10 10KΩ to +3.3V`；`capacitor=C12 100nF to GND`；`debug_pin=P1 pin4 NRST` |
| GPIO 与控制信号 | U3 BOOT0 | `mcu_pin=U3 BOOT0 pin1`；`pulldown=R8 10KΩ to GND`；`boot_switch_shown=false`；`boot_jumper_shown=false` |
| 调试与烧录 | P1 SWD_5p | `pin_1=+3.3V`；`pin_2=SWCLK/U3 PA14 pin20`；`pin_3=SWDIO/U3 PA13 pin19`；`pin_4=NRST/U3 pin4`；`pin_5=GND` |
| 时钟 | U3 时钟 | `osc_in=U3 pin2 no visible connection`；`osc_out=U3 pin3 no visible connection`；`crystal_shown=false`；`external_oscillator_shown=false` |
| 内存与 Flash | 存储器 | `external_flash_shown=false`；`eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false`；`internal_capacity_printed=false` |
| 保护电路 | J2 外部接口保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`signal_components=R4 SCL pullup,R3 SDA pullup` |
| 关键网络 | +5V、+3.3V 与 +12.5V | `5v_nodes=J2.3,U1 VIN/EN,U2 VIN/EN,C3,C6`；`3v3_nodes=U2 VOUT,U3 VDDA/VDD,J1 VDD,R3/R4/R7/R10/R11,R6,P1.1`；`12v5_nodes=U1 boost output,J1 VCC pin23,C2,C9,C10` |
| 调试与烧录 | J3-J6 GND 焊盘 | `references=J3,J4,J5,J6`；`net=GND`；`signal_labels=null` |
| 其他事实 | OLED 分辨率与透明区域 | `documented_resolution=128x64`；`documented_transparent_pixels=128x56`；`documented_size=1.51 inch`；`module=AFCO5-S24FIA-00`；`parameters_printed_on_schematic=false` |

## 待确认事项

- `address.documented-0x3d`：产品正文列出 7 位 I2C 地址 0x3D；原理图只显示 SCL/SDA 进入 U3，未打印地址、地址脚或固件配置，因此该值需依据内置固件协议或总线扫描确认。（证据：图 0df8640150fa / 第 1 页 / 第 1 页 J2 SCL/SDA 至 U3 PA9/PA10，页面无地址标注）
- `other.documented-display-geometry`：产品正文描述 128x64 总分辨率、128x56 透明区域和 1.51 英寸透明 OLED；原理图仅标出 AFCO5-S24FIA-00 与 SSD1309，未打印这些光学和像素参数。（证据：图 0df8640150fa / 第 1 页 / 第 1 页 J1 AFCO5-S24FIA-00/SSD1309，页面无分辨率或尺寸标注）
- `review.i2c-address`：请依据 Unit Glass 内置固件通信协议或 I2C 扫描确认 7 位地址 0x3D。；原因：原理图只显示 I2C 连接到 STM32，未打印固件地址或硬件地址绑带。
- `review.display-geometry`：请依据 AFCO5-S24FIA-00 模组资料确认 128x64 总分辨率、128x56 透明区域与 1.51 英寸规格。；原因：这些参数来自产品正文，原理图仅显示模组型号和控制器型号。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `0df8640150fa5a7b7f80843f40303959db9ace05ae9e8286bc0069f39e4de398` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/612/Sch_UNIT-GLASS_sch_01.png` |

---

源文档：`zh_CN/unit/Glass Unit.md`

源文档 SHA-256：`1dfd89254c421731af9125e68f3ca03476d3c3af630290f2f83af2b989323965`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
