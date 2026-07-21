# Hat Mini JoyC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Hat Mini JoyC |
| SKU | U156 |
| 产品 ID | `hat-mini-joyc-2b282d3bc3f8` |
| 源文档 | `zh_CN/hat/MiniJoyC.md` |

## 概述

Hat Mini JoyC 以 STM32F030F4P6（U1）为主控，PA1/PA2 连接 RKJXV1224005 双轴摇杆，PA3 连接中心按键 BTN，PA6 驱动 SK6812-3535（U2）。PA9/PA10 的 SCL/SDA 同时连接 8 针 HAT 接口 P1 和 GROVE J1，J2 提供 SWD 调试。3V3 为 MCU、摇杆和 RGB LED 供电，5V 仅在 HAT 与 GROVE 间分配，BAT 连接 HAT 与 J3；原理图未显示充电器或电源转换器。

## 检索关键词

`Hat Mini JoyC`、`U156`、`STM32F030F4P6`、`RKJXV1224005`、`SK6812-3535`、`PA1`、`PA2`、`PA3`、`PA6`、`BTN`、`RGB`、`I2C`、`SCL`、`SDA`、`0x54`、`GROVE`、`SWD_5P`、`SWCLK`、`SWDIO`、`NRST`、`BOOT0`、`3V3`、`5V`、`BAT`、`200mAh`、`双轴摇杆`、`中心按键`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | 主控 MCU，采集摇杆 X/Y 与按键，驱动 RGB LED，并提供 I2C 与 SWD | 图 0fa4b2411eaf / 第 1 页 / B1-C2 区域 U1 STM32F030F4P6：PA1/PA2/BTN/RGB/SCL/SDA/SWDIO/SWCLK/BOOT0/NRST 与电源引脚 |
| SW1 | RKJXV1224005 | 双轴摇杆与中心按键组件，轴信号连接 PA1/PA2，按键信号连接 BTN | 图 0fa4b2411eaf / 第 1 页 / A2-B3 区域 SW1 RKJXV1224005：两组电位器端子与底部按钮触点 |
| U2 | SK6812-3535 | 单颗可编程 RGB LED，DI 接 RGB，VDD 接 3V3，GND 接地 | 图 0fa4b2411eaf / 第 1 页 / B3 区域 U2 SK6812-3535：1 DO、2 GND、3 DI/RGB、4 VDD/3V3 |
| P1 | Header 8H | 8 针 HAT 主机接口，引出 GND、5V、SCL、SDA、BAT、3V3 | 图 0fa4b2411eaf / 第 1 页 / D3 区域 P1 Header 8H：8 GND、7 5V、6 SCL、5 G36、4 SDA、3 BAT、2 3V3、1 5VIN |
| J1 | GROVE | 四针 I2C 与 5V 扩展接口，引出 SCL、SDA、5V 和 GND | 图 0fa4b2411eaf / 第 1 页 / D2 区域 J1 GROVE：IO2/SCL、IO1/SDA、5V、GND |
| J2 | SWD_5P | 五针 SWD 调试接口，引出 3V3、MCU_SWCLK、MCU_SWDIO、NRST 和 GND | 图 0fa4b2411eaf / 第 1 页 / D1 区域 J2 SWD_5P：VCC/SWCLK/SWDIO/NRST/GND |
| J3 | 未标注 | BAT/GND 电池连接器 | 图 0fa4b2411eaf / 第 1 页 / D4 区域 J3：左侧 BAT/GND 网络，符号内 +、-、3、4 标记 |
| R1/R4/R5 | 10K / 10K / 10K | BTN 上拉、BOOT0 下拉与 NRST 上拉电阻 | 图 0fa4b2411eaf / 第 1 页 / B2 R1 10K 从 BTN 至 3V3；C2 R4 10K 从 BOOT0 至 GND；C2 R5 10K 从 NRST 至 3V3 |
| C1/C2/C3/C4/C6 | 100nF / 100nF / 10uF / 1uF / 100nF | NRST、MCU、GROVE 5V 与 RGB LED 的去耦/滤波电容 | 图 0fa4b2411eaf / 第 1 页 / 页面 C1 NRST 100nF、C2/C3 MCU 100nF/10uF、C4 GROVE 1uF、C6 U2 100nF |

## 系统结构

### Hat Mini JoyC

U1 STM32F030F4P6 采集 SW1 的 PA1/PA2 双轴与 BTN 按键，使用 PA6/RGB 驱动 U2 SK6812-3535，并通过 PA9/SCL、PA10/SDA 连接 HAT 与 GROVE。

- 参数与网络：`controller=U1 STM32F030F4P6`；`joystick=SW1 RKJXV1224005`；`x_y=PA1, PA2`；`button=PA3 BTN`；`rgb=PA6 RGB to U2`；`i2c=PA9 SCL; PA10 SDA`
- 证据：图 0fa4b2411eaf / 第 1 页 / 全页 MCU、SW1、U2、P1、J1 的同名 GPIO、总线和电源网络

## 核心器件

### U1 STM32F030F4P6

U1.7 PA1 接 PA1 摇杆轴，U1.8 PA2 接 PA2 摇杆轴，U1.9 PA3 接 BTN，U1.12 PA6 接 RGB；U1.17 PA9 接 SCL，U1.18 PA10 接 SDA，U1.19 PA13 接 MCU_SWDIO，U1.20 PA14 接 MCU_SWCLK。

- 参数与网络：`pin_7=PA1 joystick`；`pin_8=PA2 joystick`；`pin_9=PA3 BTN`；`pin_12=PA6 RGB`；`pin_17=PA9 SCL`；`pin_18=PA10 SDA`；`pin_19=PA13 MCU_SWDIO`；`pin_20=PA14 MCU_SWCLK`
- 证据：图 0fa4b2411eaf / 第 1 页 / B1-C2 区域 U1 左右侧引脚编号、GPIO 名称和网络标签

## 电源

### 3V3 电源轨

P1.2 的 3V3 连接 U1 VDD/VDDA、SW1 两轴端点、U2 VDD、BTN 上拉和 J2 VCC；C2 100nF、C3 10uF 与 C6 100nF 对地去耦。

- 参数与网络：`source=P1.2 3V3`；`mcu=U1.16 VDD; U1.5 VDDA`；`joystick=SW1 axis endpoints`；`rgb=U2.4 VDD`；`debug=J2 VCC`；`capacitors=C2 100nF; C3 10uF; C6 100nF`
- 证据：图 0fa4b2411eaf / 第 1 页 / 全页 3V3 同名网络在 P1/U1/SW1/U2/J2 与电容上的连接

### 5V 电源轨

P1.7 的 5V 直接连接 J1 GROVE 的 5V，并由 C4 1uF 对地；页面未显示 5V 到 3V3 的板载转换器。

- 参数与网络：`source=P1.7 5V`；`load=J1 5V`；`capacitor=C4 1uF`；`3v3_converter=not shown`
- 证据：图 0fa4b2411eaf / 第 1 页 / D2-D3 区域 P1.7 与 J1/C4 的 5V 同名网络

### BAT 电池路径

P1.3 BAT 连接 J3 的 BAT，J3 同时引出 GND；页面未显示充电器、保护 IC、负载开关或 BAT 到 3V3/5V 的转换路径。

- 参数与网络：`host_battery=P1.3 BAT`；`battery_connector=J3 BAT/GND`；`charger=not shown`；`protection_ic=not shown`；`converter=not shown`
- 证据：图 0fa4b2411eaf / 第 1 页 / D3-D4 区域 P1.3 BAT 与 J3 BAT/GND，同页无充电或转换器件

## 接口

### P1 Header 8H

P1.8~P1.1 依次为 GND、5V、SCL、G36/未连接、SDA、BAT、3V3、5VIN/未连接。

- 参数与网络：`pin_8=GND`；`pin_7=5V`；`pin_6=SCL`；`pin_5=G36 NC`；`pin_4=SDA`；`pin_3=BAT`；`pin_2=3V3`；`pin_1=5VIN NC`
- 证据：图 0fa4b2411eaf / 第 1 页 / D3 区域 P1 Header 8H 的 8~1 脚编号、左侧网络与 G36/5VIN 未连接标记

### J1 GROVE

J1 IO2 接 SCL，IO1 接 SDA，5V 接 5V，GND 接 GND；C4 1uF 跨接 5V 与 GND。

- 参数与网络：`IO2=SCL`；`IO1=SDA`；`5V=5V`；`GND=GND`；`port_capacitor=C4 1uF`
- 证据：图 0fa4b2411eaf / 第 1 页 / D2 区域 J1 GROVE 与右侧 SCL/SDA/5V/C4/GND 网络

## 总线

### SCL/SDA

SCL 连接 U1.17 PA9、P1.6 与 J1 IO2；SDA 连接 U1.18 PA10、P1.4 与 J1 IO1。该页未显示 I2C 上拉或电平转换器。

- 参数与网络：`scl=U1.17 PA9; P1.6; J1 IO2`；`sda=U1.18 PA10; P1.4; J1 IO1`；`pullups=not shown`；`level_shifter=not shown`
- 证据：图 0fa4b2411eaf / 第 1 页 / 页面 U1、P1、J1 的 SCL/SDA 同名网络

## GPIO 与控制信号

### SW1 中心按键

BTN 通过 R1 10K 上拉至 3V3，SW1 按钮触点动作时将 BTN 接 GND；BTN 连接 U1.9 PA3。

- 参数与网络：`signal=BTN`；`mcu_pin=U1.9 PA3`；`pullup=R1 10K to 3V3`；`active_level=low`；`switch_return=GND`
- 证据：图 0fa4b2411eaf / 第 1 页 / B2-B3 区域 SW1 底部按钮、BTN 网络、R1 10K/3V3 与 GND 触点

### U2 SK6812-3535

U1.12 PA6 的 RGB 网络连接 U2.3 DI；U2.4 VDD 接 3V3、U2.2 GND 接地，U2.1 DO 未连接，C6 100nF 跨接 3V3 与 GND。

- 参数与网络：`data_input=U2.3 DI RGB from U1.12 PA6`；`supply=U2.4 VDD 3V3`；`ground=U2.2 GND`；`data_output=U2.1 DO NC`；`decoupling=C6 100nF`
- 证据：图 0fa4b2411eaf / 第 1 页 / B3 区域 U2 SK6812-3535 的 DO/GND/DI/VDD 与 RGB/3V3/C6 网络

## 时钟

### U1 时钟

U1.2 PF0-OSC_IN 与 U1.3 PF1-OSC_OUT 未连接，页面未显示外部晶振或谐振器。

- 参数与网络：`osc_in=U1.2 PF0-OSC_IN NC`；`osc_out=U1.3 PF1-OSC_OUT NC`；`external_crystal=not shown`
- 证据：图 0fa4b2411eaf / 第 1 页 / B2 区域 U1 右上 PF0-OSC_IN/PF1-OSC_OUT 短线无连接

## 复位

### BOOT0 与 NRST

U1.1 BOOT0 通过 R4 10K 下拉至 GND；U1.4 NRST 通过 R5 10K 上拉至 3V3，并由 C1 100nF 对地。

- 参数与网络：`boot0=U1.1 via R4 10K to GND`；`nrst=U1.4 via R5 10K to 3V3`；`reset_capacitor=C1 100nF to GND`
- 证据：图 0fa4b2411eaf / 第 1 页 / C2 区域 U1 BOOT0/R4 与 NRST/R5/C1 网络

## 保护电路

### 接口保护

HAT、GROVE、SWD 和电池接口路径上未显示 TVS、保险丝或专用反接保护器件。

- 参数与网络：`tvs=not shown`；`fuse=not shown`；`reverse_polarity=not shown`
- 证据：图 0fa4b2411eaf / 第 1 页 / 全页 P1/J1/J2/J3 的完整可见连接路径

## 调试与烧录

### J2 SWD_5P

J2 依次引出 3V3/VCC、MCU_SWCLK、MCU_SWDIO、NRST 和 GND，分别连接 U1 PA14、PA13 与复位网络。

- 参数与网络：`VCC=3V3`；`SWCLK=U1.20 PA14 MCU_SWCLK`；`SWDIO=U1.19 PA13 MCU_SWDIO`；`NRST=U1.4 NRST`；`GND=GND`
- 证据：图 0fa4b2411eaf / 第 1 页 / D1 区域 J2 与 C1-C2 区域 U1 SWDIO/SWCLK/NRST 同名网络

## 模拟电路

### SW1 双轴电位器

SW1 一轴两端接 3V3/GND、滑动端接 PA1；另一轴两端接 3V3/GND、滑动端接 PA2。

- 参数与网络：`axis_1_wiper=PA1`；`axis_1_ends=3V3, GND`；`axis_2_wiper=PA2`；`axis_2_ends=3V3, GND`
- 证据：图 0fa4b2411eaf / 第 1 页 / A2-B3 区域 SW1 的水平与垂直两组电位器端子及 PA1/PA2/3V3/GND 标签

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Hat Mini JoyC | `controller=U1 STM32F030F4P6`；`joystick=SW1 RKJXV1224005`；`x_y=PA1, PA2`；`button=PA3 BTN`；`rgb=PA6 RGB to U2`；`i2c=PA9 SCL; PA10 SDA` |
| 核心器件 | U1 STM32F030F4P6 | `pin_7=PA1 joystick`；`pin_8=PA2 joystick`；`pin_9=PA3 BTN`；`pin_12=PA6 RGB`；`pin_17=PA9 SCL`；`pin_18=PA10 SDA`；`pin_19=PA13 MCU_SWDIO`；`pin_20=PA14 MCU_SWCLK` |
| 模拟电路 | SW1 双轴电位器 | `axis_1_wiper=PA1`；`axis_1_ends=3V3, GND`；`axis_2_wiper=PA2`；`axis_2_ends=3V3, GND` |
| GPIO 与控制信号 | SW1 中心按键 | `signal=BTN`；`mcu_pin=U1.9 PA3`；`pullup=R1 10K to 3V3`；`active_level=low`；`switch_return=GND` |
| GPIO 与控制信号 | U2 SK6812-3535 | `data_input=U2.3 DI RGB from U1.12 PA6`；`supply=U2.4 VDD 3V3`；`ground=U2.2 GND`；`data_output=U2.1 DO NC`；`decoupling=C6 100nF` |
| 接口 | P1 Header 8H | `pin_8=GND`；`pin_7=5V`；`pin_6=SCL`；`pin_5=G36 NC`；`pin_4=SDA`；`pin_3=BAT`；`pin_2=3V3`；`pin_1=5VIN NC` |
| 接口 | J1 GROVE | `IO2=SCL`；`IO1=SDA`；`5V=5V`；`GND=GND`；`port_capacitor=C4 1uF` |
| 总线 | SCL/SDA | `scl=U1.17 PA9; P1.6; J1 IO2`；`sda=U1.18 PA10; P1.4; J1 IO1`；`pullups=not shown`；`level_shifter=not shown` |
| 总线地址 | Hat Mini JoyC I2C 地址 | `documented_address=0x54`；`schematic_address_label=not shown`；`address_straps=not shown`；`firmware_evidence=not shown` |
| 调试与烧录 | J2 SWD_5P | `VCC=3V3`；`SWCLK=U1.20 PA14 MCU_SWCLK`；`SWDIO=U1.19 PA13 MCU_SWDIO`；`NRST=U1.4 NRST`；`GND=GND` |
| 复位 | BOOT0 与 NRST | `boot0=U1.1 via R4 10K to GND`；`nrst=U1.4 via R5 10K to 3V3`；`reset_capacitor=C1 100nF to GND` |
| 时钟 | U1 时钟 | `osc_in=U1.2 PF0-OSC_IN NC`；`osc_out=U1.3 PF1-OSC_OUT NC`；`external_crystal=not shown` |
| 电源 | 3V3 电源轨 | `source=P1.2 3V3`；`mcu=U1.16 VDD; U1.5 VDDA`；`joystick=SW1 axis endpoints`；`rgb=U2.4 VDD`；`debug=J2 VCC`；`capacitors=C2 100nF; C3 10uF; C6 100nF` |
| 电源 | 5V 电源轨 | `source=P1.7 5V`；`load=J1 5V`；`capacitor=C4 1uF`；`3v3_converter=not shown` |
| 电源 | BAT 电池路径 | `host_battery=P1.3 BAT`；`battery_connector=J3 BAT/GND`；`charger=not shown`；`protection_ic=not shown`；`converter=not shown` |
| 电源 | 内置电池容量 | `documented_capacity=200mAh`；`schematic_capacity=not shown`；`chemistry=not shown`；`voltage=not shown` |
| 保护电路 | 接口保护 | `tvs=not shown`；`fuse=not shown`；`reverse_polarity=not shown` |

## 待确认事项

- `address.i2c-0x54`：产品正文标注 I2C 地址为 0x54，但原理图未标注 0x54、地址选择网络或固件版本，无法仅由该页确认地址。（证据：图 0fa4b2411eaf / 第 1 页 / 全页 U1 与 SCL/SDA 网络，未见 0x54 或地址配置）
- `power.battery-capacity-200mah`：产品正文声明内置 200mAh 聚合物锂电池，但原理图仅显示 J3 BAT/GND 接口，未标注电池容量、化学体系或额定电压。（证据：图 0fa4b2411eaf / 第 1 页 / D4 区域 J3 仅标注 BAT/GND，无容量或电池参数）
- `review.i2c-address-0x54`：Hat Mini JoyC 的 I2C 从设备地址 0x54 是否由 STM32 固件固定实现？；原因：产品正文给出 0x54，但原理图没有地址标注、地址选择或固件版本信息。
- `review.battery-capacity`：J3 所接内置电池的额定容量、化学体系和电压是否为正文所述 200mAh 聚合物锂电池？；原因：原理图仅显示 BAT/GND 接口，没有电池规格或充电/保护信息。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `0fa4b2411eafc14741fd7b06503dfb1c87d15e23c7361c6cad60baa4eed94b37` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/610/SCH_HAT_MiniJoyC_V1.0_sch_01.png` |

---

源文档：`zh_CN/hat/MiniJoyC.md`

源文档 SHA-256：`71bbb3a2d61f7c4e5c7475567797647f4015a4de79c3624e25fa17b1906cf386`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
