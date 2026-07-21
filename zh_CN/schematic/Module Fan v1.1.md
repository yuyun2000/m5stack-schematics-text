# Module Fan v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module Fan v1.1 |
| SKU | M013-V11 |
| 产品 ID | `module-fan-v1-1-fb76038d1490` |
| 源文档 | `zh_CN/module/Module Fan v1.1.md` |

## 概述

Module Fan v1.1 以 U1 STM32F030F4P6 通过 I2C 接入 M5-Bus，并以 PA6 FanCtr 控制风扇 PWM、PA7 FG_OUT 读取转速反馈。Q1 BSS138 与 R5/R6 将 3.3V FanCtr 侧和 5V PWM 侧连接，P1 FAN 3004 的 5V 电源经过 F1 6V/0.5A，FG_OUT 经过 R3 100R 并由 R1 10K 上拉。MCU 直接使用总线 VCC_3V3，风扇使用总线 VCC_5V；I2C 地址 0x18、堵转保护和转速/功耗/噪声参数未在原理图中直接给出。

## 检索关键词

`Module Fan v1.1`、`M013-V11`、`STM32F030F4P6`、`FAN 3004`、`BSS138`、`FanCtr`、`FG_OUT`、`PWM`、`I2C`、`0x18`、`SDA`、`SCL`、`PA6`、`PA7`、`PA9`、`PA10`、`VCC_3V3`、`VCC_5V`、`F1 6V/0.5A`、`R3 100R`、`R1 10K`、`SWD_5P`、`MCU_SWDIO`、`MCU_SWCLK`、`NRST`、`BOOT0`、`M5_BUS`、`11500RPM`、`stall protection`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | I2C 从设备 MCU，输出风扇控制并采集转速反馈 | 图 d30e669ef7c0 / 第 1 页 / 第 1 页 B2-C3 U1 STM32F030F4P6，FanCtr/FG_OUT/SCL/SDA/SWD/复位与电源引脚 |
| BUS1 | M5_BUS | 30 针堆叠接口，向 MCU/风扇提供 3.3V、5V、I2C 和 GND | 图 d30e669ef7c0 / 第 1 页 / 第 1 页 A2-B2 BUS1 M5_BUS，1~30 脚及 SDA/SCL/VCC_3V3/VCC_5V/GND |
| P1 | FAN 3004 | 四针风扇接口，引出 FG_OUT、PWM、VCC_5V 和 GND | 图 d30e669ef7c0 / 第 1 页 / 第 1 页 D2 P1 FAN 3004，1~4 脚 |
| Q1 | BSS138 | 连接 3.3V FanCtr 与 5V PWM 的 MOSFET 电平转换器 | 图 d30e669ef7c0 / 第 1 页 / 第 1 页 D2-D3 Q1 BSS138，左接 PWM/R6，右接 FanCtr/R5 |
| F1 | 6V/0.5A | 串联在 VCC_5V 与 P1.2 风扇电源之间的保护器件 | 图 d30e669ef7c0 / 第 1 页 / 第 1 页 D2 P1.2 与 VCC_5V 之间 F1 6V/0.5A |
| J1 | SWD_5P | MCU 调试与复位接口，提供 VCC、SWCLK、SWDIO、NRST 和 GND | 图 d30e669ef7c0 / 第 1 页 / 第 1 页 C1-C2 J1 SWD_5P 五路标签 |

## 系统结构

### Module Fan v1.1

U1 STM32F030F4P6 通过 SDA/SCL 接 BUS1，以 FanCtr 经 Q1 控制 P1 PWM，并从 P1 FG_OUT 经 R3 读取风扇反馈。

- 参数与网络：`mcu=U1 STM32F030F4P6`；`host_bus=I2C`；`control_path=U1 PA6 FanCtr -> Q1 BSS138 -> PWM -> P1.3`；`feedback_path=P1.4 FG_OUT -> R3 100R -> U1 PA7`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 BUS1、U1、Q1 与 P1 同名网络

## 核心器件

### U1

控制器位号 U1，型号标为 STM32F030F4P6。

- 参数与网络：`reference=U1`；`part_number=STM32F030F4P6`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 U1 底部 STM32F030F4P6

## 电源

### U1 3.3V 电源

U1.16 VDD 与 U1.5 VDDA 接 VCC_3V3，U1.15 VSS 接 GND；C3 100nF 与 C4 10uF 跨接 VCC_3V3 和 GND。

- 参数与网络：`VDD=U1.16 VCC_3V3`；`VDDA=U1.5 VCC_3V3`；`VSS=U1.15 GND`；`decoupling=C3 100nF,C4 10uF`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 C2-C3 U1 电源引脚与 C3/C4

## 接口

### FanCtr 到 PWM

Q1 BSS138 位于 FanCtr 与 PWM 之间；PWM 侧由 R6 10K 上拉到 VCC_5V，FanCtr 侧由 R5 10K 上拉到 VCC_3V3。

- 参数与网络：`low_voltage_net=FanCtr`；`low_voltage_pullup=R5 10K to VCC_3V3`；`high_voltage_net=PWM`；`high_voltage_pullup=R6 10K to VCC_5V`；`translator=Q1 BSS138`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 D2-D3 Q1、R5、R6、FanCtr/PWM

### P1 FAN 3004

P1.1 接 GND，P1.2 经 F1 接 VCC_5V，P1.3 接 PWM，P1.4 经 R3 接 FG_OUT。

- 参数与网络：`pin_1=GND`；`pin_2=VCC_5V via F1`；`pin_3=PWM`；`pin_4=FG_OUT via R3 100R`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 D2 P1 1~4 脚与相邻网络

### BUS1 M5_BUS 已用针脚

BUS1.2/.4/.6 接 GND，BUS1.11 接 VCC_3V3，BUS1.17 接 SCL，BUS1.18 接 SDA，BUS1.27 接 VCC_5V，BUS1.26/.28/.30 为 HPWR。

- 参数与网络：`pins_2_4_6=GND`；`pin_11=VCC_3V3`；`pin_17=SCL`；`pin_18=SDA`；`pin_27=VCC_5V`；`pins_26_28_30=HPWR`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 A2 BUS1 外部网络标注

## 总线

### U1 I2C

U1.17 PA9 接 SCL，U1.18 PA10 接 SDA；SCL/SDA 分别连接 BUS1.17/BUS1.18，并由 R8/R7 各 10K 上拉到 VCC_3V3。

- 参数与网络：`scl=U1.17 PA9 -> SCL -> BUS1.17`；`sda=U1.18 PA10 -> SDA -> BUS1.18`；`scl_pullup=R8 10K to VCC_3V3`；`sda_pullup=R7 10K to VCC_3V3`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 A2 BUS1 与 B2-C2 U1 SDA/SCL/R7/R8

## GPIO 与控制信号

### FanCtr

U1.12 PA6 输出 FanCtr；FanCtr 侧由 R5 10K 上拉到 VCC_3V3，并连接 Q1 BSS138。

- 参数与网络：`mcu_pin=U1.12 PA6`；`net=FanCtr`；`pullup=R5 10K to VCC_3V3`；`level_shifter=Q1 BSS138`；`direction=MCU to fan`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 U1 PA6 FanCtr 与 D3 Q1/R5

### FG_OUT

U1.13 PA7 接 FG_OUT，FG_OUT 由 R1 10K 上拉到 VCC_3V3，并经 R3 100R 连接 P1.4。

- 参数与网络：`mcu_pin=U1.13 PA7`；`net=FG_OUT`；`pullup=R1 10K to VCC_3V3`；`series_resistor=R3 100R`；`fan_pin=P1.4`；`direction=fan to MCU`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 U1 PA7/R1 与 D2 P1.4/R3

## 复位

### U1 BOOT0/NRST

U1.1 BOOT0 通过 R2 10K 接 GND；U1.4 NRST 由 R4 10K 上拉到 VCC_3V3，并由 C2 100nF 接 GND。

- 参数与网络：`boot0=U1.1 via R2 10K to GND`；`reset=U1.4 NRST`；`reset_pullup=R4 10K`；`reset_cap=C2 100nF`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 B3 U1 BOOT0/R2 与 NRST/R4/C2

## 保护电路

### 风扇 5V 电源保护

F1 标注 6V/0.5A，串联在 VCC_5V 与 P1.2 之间；C1 标注 106/10V，从风扇 5V 节点接 GND。

- 参数与网络：`fuse=F1 6V/0.5A`；`protected_load=P1.2 fan VCC`；`rail=VCC_5V`；`capacitor=C1 106/10V to GND`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 D2 P1.2-F1-VCC_5V 与 C1

## 内存与 Flash

### 外部存储器

页面未显示 U1 之外的 Flash、EEPROM、RAM、SD 卡或其他外部存储器件。

- 参数与网络：`external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_shown=false`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页完整原理图无独立存储器

## 调试与烧录

### J1 SWD_5P

J1 依次引出 VCC_3V3、MCU_SWCLK、MCU_SWDIO、NRST 和 GND；SWCLK/SWDIO 分别连接 U1 PA14/PA13。

- 参数与网络：`signals=VCC_3V3,MCU_SWCLK,MCU_SWDIO,NRST,GND`；`swclk=U1.20 PA14`；`swdio=U1.19 PA13`
- 证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 C1-C2 J1 与 U1 PA13/PA14 同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module Fan v1.1 | `mcu=U1 STM32F030F4P6`；`host_bus=I2C`；`control_path=U1 PA6 FanCtr -> Q1 BSS138 -> PWM -> P1.3`；`feedback_path=P1.4 FG_OUT -> R3 100R -> U1 PA7` |
| 核心器件 | U1 | `reference=U1`；`part_number=STM32F030F4P6` |
| 总线 | U1 I2C | `scl=U1.17 PA9 -> SCL -> BUS1.17`；`sda=U1.18 PA10 -> SDA -> BUS1.18`；`scl_pullup=R8 10K to VCC_3V3`；`sda_pullup=R7 10K to VCC_3V3` |
| 总线地址 | 正文中的 I2C 地址 | `documented_address=0x18`；`address_on_schematic=null`；`address_straps_shown=false` |
| GPIO 与控制信号 | FanCtr | `mcu_pin=U1.12 PA6`；`net=FanCtr`；`pullup=R5 10K to VCC_3V3`；`level_shifter=Q1 BSS138`；`direction=MCU to fan` |
| 接口 | FanCtr 到 PWM | `low_voltage_net=FanCtr`；`low_voltage_pullup=R5 10K to VCC_3V3`；`high_voltage_net=PWM`；`high_voltage_pullup=R6 10K to VCC_5V`；`translator=Q1 BSS138` |
| GPIO 与控制信号 | FG_OUT | `mcu_pin=U1.13 PA7`；`net=FG_OUT`；`pullup=R1 10K to VCC_3V3`；`series_resistor=R3 100R`；`fan_pin=P1.4`；`direction=fan to MCU` |
| 接口 | P1 FAN 3004 | `pin_1=GND`；`pin_2=VCC_5V via F1`；`pin_3=PWM`；`pin_4=FG_OUT via R3 100R` |
| 保护电路 | 风扇 5V 电源保护 | `fuse=F1 6V/0.5A`；`protected_load=P1.2 fan VCC`；`rail=VCC_5V`；`capacitor=C1 106/10V to GND` |
| 电源 | U1 3.3V 电源 | `VDD=U1.16 VCC_3V3`；`VDDA=U1.5 VCC_3V3`；`VSS=U1.15 GND`；`decoupling=C3 100nF,C4 10uF` |
| 复位 | U1 BOOT0/NRST | `boot0=U1.1 via R2 10K to GND`；`reset=U1.4 NRST`；`reset_pullup=R4 10K`；`reset_cap=C2 100nF` |
| 调试与烧录 | J1 SWD_5P | `signals=VCC_3V3,MCU_SWCLK,MCU_SWDIO,NRST,GND`；`swclk=U1.20 PA14`；`swdio=U1.19 PA13` |
| 接口 | BUS1 M5_BUS 已用针脚 | `pins_2_4_6=GND`；`pin_11=VCC_3V3`；`pin_17=SCL`；`pin_18=SDA`；`pin_27=VCC_5V`；`pins_26_28_30=HPWR` |
| 时钟 | U1 时钟 | `PF0_OSC_IN=not connected`；`PF1_OSC_OUT=not connected`；`external_crystal_shown=false`；`frequency=null` |
| 保护电路 | 正文中的堵转保护 | `documented_stall_protection=true`；`current_sensor_shown=false`；`dedicated_protection_ic_shown=false`；`visible_feedback=FG_OUT`；`visible_fuse=F1 6V/0.5A` |
| 其他事实 | 正文中的风扇性能参数 | `documented_speed=11500RPM±10%`；`documented_airflow=1.23CFM`；`documented_test_points=PWM20%,PWM60%,PWM100%`；`parameters_on_schematic=null` |
| 内存与 Flash | 外部存储器 | `external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `address.documented-0x18`：产品正文给出 I2C 地址 0x18，但原理图未显示 0x18 或地址配置硬件，需由内部固件/协议确认。（证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 U1 与 BUS1 SDA/SCL 区，无地址标注）
- `clock.mcu-clock-not-shown`：U1 PF0-OSC_IN 与 PF1-OSC_OUT 未连接，页面未显示外部晶振或时钟频率，实际时钟配置需由固件确认。（证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 B3 U1.2/U1.3 PF0/PF1 无连线）
- `protection.documented-stall`：产品正文声称支持堵转保护，但原理图只显示 PWM、FG_OUT、F1 与 MCU，未显示电流检测、专用堵转保护 IC 或保护阈值；堵转恢复逻辑需由风扇规格/固件确认。（证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 P1/Q1/U1/F1 范围，无堵转检测专用电路）
- `other.documented-fan-performance`：产品正文列出 11500RPM±10%、1.23CFM 及 PWM 20/60/100% 的噪声和功耗数据；这些参数未标在原理图上，需由实际风扇规格书和测试条件确认。（证据：图 d30e669ef7c0 / 第 1 页 / 第 1 页 P1 仅标 FAN 3004，无转速、风量、噪声或功耗参数）
- `review.i2c-address`：请通过 M013-V11 当前内部固件或协议确认 7-bit I2C 地址是否固定为 0x18。；原因：原理图未显示地址配置。
- `review.mcu-clock`：请确认 STM32F030F4P6 使用的内部时钟源、频率和固件配置。；原因：PF0/PF1 未连接，原理图未标时钟。
- `review.stall-protection`：请确认堵转检测依据、保护/恢复算法、阈值、超时，以及由风扇内部还是 MCU 固件实现。；原因：当前图只有 FG_OUT、PWM 和保险器件，没有专用堵转检测电路。
- `review.fan-performance`：请以当前装配风扇规格书和测试报告确认转速、风量、噪声、工作/待机功耗。；原因：性能数据不属于本页电路标注。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d30e669ef7c003a963d01d47ad4667ef4545e5988d38e0bb95c2806b1ca85c12` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/M013_v11_Schematic_sch_01.png` |

---

源文档：`zh_CN/module/Module Fan v1.1.md`

源文档 SHA-256：`428e07a8738ac8babe090a8d36e98108f4b5b29e0d66a1e257760564cc323243`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
