# Atom Motion 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom Motion |
| SKU | K053 |
| 产品 ID | `atom-motion-3e67d876f82b` |
| 源文档 | `zh_CN/atom/atom_motion.md` |

## 概述

Atom Motion 以 U3 STM32F030F4P6 为控制器，经 Atom G21/G25 的 I2C 连接主控，PA0-PA3 直接引出四路舵机控制信号。U4/U2 两颗 RZ7899 分别以 M1F/M1R、M2F/M2R 驱动 JP2/JP1 两路直流电机，电机和舵机使用 BAT+，U1 ETA9740 将电池电源转换为 5V 供 Atom 与两组 Grove。电路还包含 16340 电池、5A 保险、滑动开关、SWD 接口和两组 Grove；I2C 地址、固件寄存器、额定电流及 18350/700mAh 参数未在原理图中确认。

## 检索关键词

`Atom Motion`、`K053`、`STM32F030F4P6`、`ETA9740`、`RZ7899`、`I2C`、`0x38`、`SCL`、`SDA`、`G21`、`G25`、`M1F`、`M1R`、`M2F`、`M2R`、`PA0`、`PA1`、`PA2`、`PA3`、`PA4`、`PA6`、`PA7`、`PB1`、`BAT+`、`5V`、`3V3`、`16340`、`18350`、`SWDIO`、`SWCLK`、`NRST`、`Grove`、`G23`、`G33`、`G22`、`G19`、`DC motor`、`servo`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030F4P6 | I2C 控制器，生成四路舵机和两路电机方向控制信号，并连接 SWD/复位 | 图 cacac3d1e29e / 第 1 页 / 第 1 页中央 U3 STM32F030F4P6，PA/PB、SCL/SDA、SWDIO/SWCLK、NRST、BOOT0 和电源地 |
| U1 | ETA9740 | 从 BAT+ 通过 L1 生成 5V 的开关电源转换器，并带 LED1/LED2/LED3 引脚 | 图 cacac3d1e29e / 第 1 页 / 第 1 页左上 U1 ETA9740，BAT/SW/OUT/ISET/LED1-3、L1 与 BAT+/5V |
| U2,U4 | RZ7899 | 两路独立直流电机驱动器，分别连接 M2F/M2R 与 M1F/M1R | 图 cacac3d1e29e / 第 1 页 / 第 1 页左中 U2/U4 RZ7899，OUTF/OUTR、INF/INR、BAT+/GND 与 JP1/JP2 |
| BT1 | 16340 | 板载可拆卸电池位，正端经 5A 保险形成 BAT+，负端接 GND | 图 cacac3d1e29e / 第 1 页 / 第 1 页上中 BT1 16340、FUSE 5A、BAT+ 与 GND |
| JP1,JP2 | 未标注 | U2/U4 两路 RZ7899 的两针直流电机输出接口 | 图 cacac3d1e29e / 第 1 页 / 第 1 页左中 JP1/JP2 两针接口与 U2/U4 OUTF/OUTR |
| JP3-JP6 | 未标注 | 四组三针舵机接口，每组包含 MCU 控制信号、BAT+ 和 GND | 图 cacac3d1e29e / 第 1 页 / 第 1 页左下 JP3-JP6 三针接口与 PA0-PA3/BAT+/GND |
| ATOM | ATOM | 连接 Atom 主控的 3V3、I2C、5V、GND 和 G22/G19/G23/G33 信号 | 图 cacac3d1e29e / 第 1 页 / 第 1 页中下 ATOM 9 针连接器，G21/G25/5V/GND/3V3/G22/G19/G23/G33 |
| J1,J2 | GROVE | 两组 5V Grove 扩展接口，分别引出 G23/G33 与 G22/G19 | 图 cacac3d1e29e / 第 1 页 / 第 1 页右下 J1/J2 GROVE，IO2/IO1/5V/GND 与 ATOM 网络 |
| J3 | SWD | STM32 的 NRST、SWCLK、SWDIO、3V3 和 GND 调试接口 | 图 cacac3d1e29e / 第 1 页 / 第 1 页中右 J3 SWD，RST/CLK/DIO/VCC/GND 与 NRST/SWCLK/SWDIO/3V3 |
| S(未编号) | SS-12F23 | 电源区域的三针滑动开关 | 图 cacac3d1e29e / 第 1 页 / 第 1 页上中未编号开关 SS-12F23，pin1/pin2/pin3 与电源/GND 网络 |
| D1,Fuse | DSS34P / 5A | BAT+ 电池电源的对地二极管和串联保险保护 | 图 cacac3d1e29e / 第 1 页 / 第 1 页上中 BT1/FUSE 5A/BAT+ 与 D1 DSS34P 到 GND |

## 系统结构

### Atom Motion 系统架构

Atom Motion 使用 STM32F030F4P6 通过 I2C 接收 Atom 命令，直接输出四路舵机控制并驱动两颗 RZ7899 完成两路直流电机控制；电池 BAT+ 为电机/舵机供电，ETA9740 生成 5V 给 Atom 和 Grove。

- 参数与网络：`controller=U3 STM32F030F4P6`；`host_bus=I2C SCL/SDA`；`motor_drivers=U2/U4 RZ7899`；`motor_channels=2`；`servo_channels=4`；`battery_rail=BAT+`；`five_volt_converter=U1 ETA9740`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页完整单页原理图，电源、U2/U4 电机、U3 MCU、JP3-JP6 舵机、ATOM/Grove/SWD

## 核心器件

### STM32F030F4P6 运动控制器

U3 STM32F030F4P6 由 3V3 供电，连接 PA0-PA3 舵机信号、M1F/M1R/M2F/M2R 电机控制、SCL/SDA、SWDIO/SWCLK 和 NRST，BOOT0 接 GND。

- 参数与网络：`reference=U3`；`part_number=STM32F030F4P6`；`power=VDDA/VDD 3V3, VSS GND`；`servo_gpio=PA0, PA1, PA2, PA3`；`motor_nets=M1F, M1R, M2F, M2R`；`i2c=SCL, SDA`；`debug=SWDIO, SWCLK, NRST`；`boot0=GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页中央 U3 STM32F030F4P6 全部已连接网络

## 电源

### 16340 电池到 BAT+ 电源轨

BT1 正端经 5A 保险连接 BAT+，负端接 GND；BAT+ 连接 ETA9740 BAT、两颗 RZ7899 VCC 和四组舵机接口电源，D1 DSS34P 从 BAT+ 接到 GND。

- 参数与网络：`cell=BT1 16340`；`positive_path=BT1 -> Fuse 5A -> BAT+`；`negative=GND`；`consumers=U1 BAT, U2/U4 VCC, JP3-JP6 power`；`shunt_diode=D1 DSS34P`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页上中 BT1/Fuse/D1/BAT+ 与 U1、U2/U4、JP3-JP6 同名网络

### BAT+ 到 5V 转换

U1 ETA9740 的 BAT/SW 侧连接 BAT+ 和 L1 3.3uH，OUT pin7 形成 5V 输出；输入使用 C1 10uF/C2 4.7uF，输出使用 C3/C4/C5 10uF 和 C11 100nF。

- 参数与网络：`converter=U1 ETA9740`；`input=BAT+`；`output=5V`；`inductor=L1 3.3uH/4012`；`input_caps=C1 10uF, C2 4.7uF`；`output_caps=C3/C4/C5 10uF, C11 100nF`；`iset=R2 150K`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页左上 U1 ETA9740、L1、R2、C1-C5/C11 与 BAT+/5V

### 5V、3V3 和 BAT+ 负载分配

5V 连接 ATOM pin3、J1/J2 Grove pin2 及 C7；3V3 从 ATOM pin9 连接 U3 VDDA/VDD、J3 VCC 和 C8/C9/C10；BAT+ 连接电机与舵机负载。

- 参数与网络：`5V=ATOM, J1/J2 Grove`；`3V3=U3 VDDA/VDD, J3 SWD`；`BAT+=U2/U4 motor drivers, JP3-JP6 servos`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页 ATOM/Grove/MCU/SWD/电机/舵机区的 5V、3V3、BAT+ 网络

## 接口

### JP1/JP2 直流电机输出

U2 RZ7899 的并联 OUTF/OUTR 输出连接 JP1 两针接口，U4 RZ7899 的并联 OUTF/OUTR 输出连接 JP2 两针接口；两颗驱动器 VCC 均接 BAT+、GND 接地。

- 参数与网络：`motor_1=U4 -> JP2`；`motor_2=U2 -> JP1`；`supply=BAT+`；`ground=GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页左中 U2/U4 RZ7899 与 JP1/JP2、BAT+/GND

### J1 Grove 扩展接口

J1 IO2 连接 ATOM G23，IO1 连接 G33，5V 与 GND 分别接系统 5V/GND。

- 参数与网络：`connector=J1`；`io2=G23`；`io1=G33`；`power=5V`；`ground=GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页右下 J1 GROVE 与 ATOM G23/G33/5V/GND

### J2 Grove 扩展接口

J2 IO2 连接 ATOM G22，IO1 连接 G19，5V 与 GND 分别接系统 5V/GND。

- 参数与网络：`connector=J2`；`io2=G22`；`io1=G19`；`power=5V`；`ground=GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页右下 J2 GROVE 与 ATOM G22/G19/5V/GND

## 总线

### Atom 到 STM32 的 I2C 链路

ATOM pin7 G21 连接 SCL，并接 U3 PA9 pin17；ATOM pin5 G25 连接 SDA，并接 U3 PA10 pin18。

- 参数与网络：`host_scl=ATOM pin7 G21`；`mcu_scl=U3 PA9 pin17`；`host_sda=ATOM pin5 G25`；`mcu_sda=U3 PA10 pin18`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页 U3 PA9/PA10 SCL/SDA 与 ATOM G21/G25

## GPIO 与控制信号

### 四路舵机 GPIO 映射

U3 PA0/PA1/PA2/PA3 分别连接 JP3/JP4/JP5/JP6 的控制信号脚；每个接口另外连接 BAT+ 和 GND。

- 参数与网络：`PA0=JP3 signal`；`PA1=JP4 signal`；`PA2=JP5 signal`；`PA3=JP6 signal`；`servo_power=BAT+`；`servo_ground=GND`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页中央 U3 PA0-PA3 到左下 JP3-JP6 长连线

### 两路电机 GPIO 映射

U3 PA4 连接 M1F，PB1 连接 M1R；PA6 连接 M2F，PA7 连接 M2R，分别驱动 U4 和 U2 的 INF/INR。

- 参数与网络：`PA4=M1F -> U4 INF`；`PB1=M1R -> U4 INR`；`PA6=M2F -> U2 INF`；`PA7=M2R -> U2 INR`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页中央 U3 PA4/PB1/PA6/PA7 与左中 U4/U2 M1F/M1R/M2F/M2R

## 调试与烧录

### STM32 SWD 与复位

J3 引出 NRST、SWCLK、SWDIO、3V3 和 GND；U3 PA13/SWDIO、PA14/SWCLK 和 NRST 分别连接这些网络，C6 100nF 从 NRST 节点接地。

- 参数与网络：`connector=J3 SWD`；`signals=NRST, SWCLK, SWDIO, 3V3, GND`；`debug_pins=PA13/SWDIO, PA14/SWCLK`；`reset_pin=NRST`；`reset_capacitor=C6 100nF`
- 证据：图 cacac3d1e29e / 第 1 页 / 第 1 页中央 U3 SWDIO/SWCLK/NRST 与中右 J3/C6

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom Motion 系统架构 | `controller=U3 STM32F030F4P6`；`host_bus=I2C SCL/SDA`；`motor_drivers=U2/U4 RZ7899`；`motor_channels=2`；`servo_channels=4`；`battery_rail=BAT+`；`five_volt_converter=U1 ETA9740` |
| 电源 | 16340 电池到 BAT+ 电源轨 | `cell=BT1 16340`；`positive_path=BT1 -> Fuse 5A -> BAT+`；`negative=GND`；`consumers=U1 BAT, U2/U4 VCC, JP3-JP6 power`；`shunt_diode=D1 DSS34P` |
| 电源 | BAT+ 到 5V 转换 | `converter=U1 ETA9740`；`input=BAT+`；`output=5V`；`inductor=L1 3.3uH/4012`；`input_caps=C1 10uF, C2 4.7uF`；`output_caps=C3/C4/C5 10uF, C11 100nF`；`iset=R2 150K` |
| 电源 | 5V、3V3 和 BAT+ 负载分配 | `5V=ATOM, J1/J2 Grove`；`3V3=U3 VDDA/VDD, J3 SWD`；`BAT+=U2/U4 motor drivers, JP3-JP6 servos` |
| 核心器件 | STM32F030F4P6 运动控制器 | `reference=U3`；`part_number=STM32F030F4P6`；`power=VDDA/VDD 3V3, VSS GND`；`servo_gpio=PA0, PA1, PA2, PA3`；`motor_nets=M1F, M1R, M2F, M2R`；`i2c=SCL, SDA`；`debug=SWDIO, SWCLK, NRST`；`boot0=GND` |
| 总线 | Atom 到 STM32 的 I2C 链路 | `host_scl=ATOM pin7 G21`；`mcu_scl=U3 PA9 pin17`；`host_sda=ATOM pin5 G25`；`mcu_sda=U3 PA10 pin18` |
| 总线 | 产品正文中的 I2C 地址和寄存器 | `documented_address=0x38`；`servo_angle_registers=0x00-0x03`；`servo_pulse_registers=0x10,0x12,0x14,0x16`；`motor_registers=0x20-0x21`；`schematic_setting=null` |
| GPIO 与控制信号 | 四路舵机 GPIO 映射 | `PA0=JP3 signal`；`PA1=JP4 signal`；`PA2=JP5 signal`；`PA3=JP6 signal`；`servo_power=BAT+`；`servo_ground=GND` |
| GPIO 与控制信号 | 两路电机 GPIO 映射 | `PA4=M1F -> U4 INF`；`PB1=M1R -> U4 INR`；`PA6=M2F -> U2 INF`；`PA7=M2R -> U2 INR` |
| 接口 | JP1/JP2 直流电机输出 | `motor_1=U4 -> JP2`；`motor_2=U2 -> JP1`；`supply=BAT+`；`ground=GND` |
| 接口 | J1 Grove 扩展接口 | `connector=J1`；`io2=G23`；`io1=G33`；`power=5V`；`ground=GND` |
| 接口 | J2 Grove 扩展接口 | `connector=J2`；`io2=G22`；`io1=G19`；`power=5V`；`ground=GND` |
| 调试与烧录 | STM32 SWD 与复位 | `connector=J3 SWD`；`signals=NRST, SWCLK, SWDIO, 3V3, GND`；`debug_pins=PA13/SWDIO, PA14/SWCLK`；`reset_pin=NRST`；`reset_capacitor=C6 100nF` |
| 电源 | 产品正文中的电池规格 | `schematic_cell=16340`；`documented_cells=16340/18350`；`documented_capacity=700mAh` |
| 电源 | 产品正文中的负载电流额定值 | `documented_full_load=3A`；`documented_motor_peak=1A per channel`；`documented_servo_peak=0.4A per channel`；`schematic_fuse=5A` |

## 待确认事项

- `bus.documented-i2c-protocol`：产品正文给出 I2C 地址 0x38，以及舵机 0x00-0x03/0x10-0x16 和电机 0x20-0x21 寄存器，但当前原理图只显示 SCL/SDA 物理连接，无法验证固件地址与寄存器语义。（证据：图 cacac3d1e29e / 第 1 页 / 第 1 页 U3 SCL/SDA 与 ATOM G21/G25，图中无地址或寄存器设定）
- `power.documented-battery-options`：产品正文称支持 16340/18350 且容量 700mAh，但当前原理图 BT1 只标 16340，没有 18350 或容量标注，因此扩展规格无法由原理图确认。（证据：图 cacac3d1e29e / 第 1 页 / 第 1 页上中 BT1 仅标 16340，未标容量）
- `power.documented-current-ratings`：产品正文给出满负荷转向 3A、单电机峰值 1A、单舵机峰值 0.4A，但原理图仅标 BAT+、5A 保险和器件连接，无法验证这些系统级额定值和测试条件。（证据：图 cacac3d1e29e / 第 1 页 / 第 1 页 BAT+/5A Fuse、U2/U4 RZ7899 与 JP3-JP6，图中无通道电流额定值）
- `review.i2c-firmware-protocol`：K053 当前 STM32 固件是否确认为 I2C 地址 0x38，并实现正文所列舵机和电机寄存器映射？；原因：地址和寄存器由固件决定，原理图只有 SCL/SDA 物理连接。
- `review.battery-options`：当前结构是否同时兼容 16340 和 18350，且配套电池容量是否固定为 700mAh？；原因：原理图 BT1 只标 16340，机械兼容性和容量需要结构图、BOM 或实物确认。
- `review.current-ratings`：3A 满负荷、1A 单电机和 0.4A 单舵机额定值的电池、散热和测试条件是什么？；原因：原理图无法单独证明系统级持续或峰值电流能力，需要器件规格和整机测试记录。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `cacac3d1e29ea7035c746de97a331103b07bb0ab32a5b1c7d70c35724b57b915` | `https://static-cdn.m5stack.com/resource/docs/products/atom/atom_motion/atom_motion_sch_01.webp` |

---

源文档：`zh_CN/atom/atom_motion.md`

源文档 SHA-256：`aa37f41926d678a3eb6ef15c0a885aad74898fb569be248466c49d1859b2100b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
