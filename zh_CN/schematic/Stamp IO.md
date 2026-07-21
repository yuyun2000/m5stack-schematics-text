# Stamp IO 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp IO |
| SKU | S002 |
| 产品 ID | `stamp-io-bf4e37ffdb03` |
| 源文档 | `zh_CN/stamp/stamp_io.md` |

## 概述

Stamp IO 以 U1 STM32F030F4P6 为 I2C IO 协处理器，PA0~PA7 直接形成 IO0~IO7，PA9/PA10 分别连接 SCL/SDA。J3 StampIO_Pin 集中引出 8 路 IO、I2C、+5V、+3.3V 和 GND，J1 HY-2.0_IIC 另提供 SCL/SDA/+5V/GND。U2 HT7533 将 +5V 转换为 +3.3V，P1 提供 SWD，BOOT0 和 NRST 配置固定的下拉/上拉 RC 网络。原理图未显示 I2C 上拉、地址选择或 IO 保护，正文的 0x45 地址及数字/ADC/Servo/RGB/PWM 模式依赖固件确认。

## 检索关键词

`Stamp IO`、`S002`、`STM32F030F4P6`、`HT7533`、`I2C`、`0x45`、`IO0`、`IO1`、`IO2`、`IO3`、`IO4`、`IO5`、`IO6`、`IO7`、`PA0`、`PA1`、`PA2`、`PA3`、`PA4`、`PA5`、`PA6`、`PA7`、`SCL`、`SDA`、`PA9`、`PA10`、`StampIO_Pin`、`HY-2.0_IIC`、`SWD`、`SWCLK`、`SWDIO`、`RST`、`BOOT0`、`+5V`、`+3.3V`、`ADC`、`SERVO`、`RGB LED`、`PWM`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | I2C IO 扩展 MCU，连接 8 路 IO、复位、BOOT0 和 SWD | 图 68fd4bcfaddc / 第 1 页 / 第 1 页 B1-B2 U1 STM32F030F4P6 |
| U2 | HT7533 | +5V 到 +3.3V 的线性稳压器 | 图 68fd4bcfaddc / 第 1 页 / 第 1 页 C3 U2 HT7533 |
| J3 | StampIO_Pin | 14 针主连接器，引出 8 路 IO、I2C、+5V、+3.3V 和 GND | 图 68fd4bcfaddc / 第 1 页 / 第 1 页 C1-C2 J3 StampIO_Pin |
| J1 | HY-2.0_IIC | SCL、SDA、+5V、GND 四针 I2C 接口 | 图 68fd4bcfaddc / 第 1 页 / 第 1 页 B3 J1 HY-2.0_IIC |
| P1 | SWD_5p | +3.3V、SWCLK、SWDIO、RST、GND 调试/烧录接口 | 图 68fd4bcfaddc / 第 1 页 / 第 1 页 B4 P1 SWD_5p |
| R1/R2/C1 | 10KΩ/10KΩ/100nF | BOOT0 下拉与 NRST 上拉 RC 配置网络 | 图 68fd4bcfaddc / 第 1 页 / 第 1 页 B1 U1 左侧 R1/R2/C1 |
| C2/C3/C4 | 22uF/22uF/100nF | HT7533 输入和输出电源滤波/去耦 | 图 68fd4bcfaddc / 第 1 页 / 第 1 页 C2-C3 U2 周围 C2/C3/C4 |

## 系统结构

### Stamp IO

U1 STM32F030F4P6 通过 SCL/SDA 与外部主机通信，并把 PA0~PA7 作为 IO0~IO7 引出；U2 提供 +3.3V，J3/J1/P1 分别承担主连接、I2C 和 SWD。

- 参数与网络：`mcu=U1 STM32F030F4P6`；`channels=IO0-IO7`；`bus=I2C SCL/SDA`；`regulator=U2 HT7533`；`connectors=J3,J1,P1`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页完整功能分区

## 电源

### U2 HT7533

U2 VIN 接 +5V、VOUT 输出 +3.3V、GND 接地；C2/C3 均标 22uF(226) 20% 6.3V，C4 为 100nF。

- 参数与网络：`input=+5V`；`output=+3.3V`；`input_cap=C2 22uF(226) 20% 6.3V`；`output_caps=C3 22uF(226) 20% 6.3V,C4 100nF`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 C2-C3 U2

### +5V/+3.3V

+5V 从 J3.2 和 J1.3 进入同一网络并供 U2；+3.3V 供 U1 VDD/VDDA、J3.14 和 P1.1。图中没有充电器、电池、负载开关或电源使能。

- 参数与网络：`5v_nodes=J3.2,J1.3,U2 VIN`；`3v3_nodes=U1 VDD/VDDA,J3.14,P1.1`；`charger_shown=false`；`battery_shown=false`；`load_switch_shown=false`；`enable_shown=false`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页全部 +5V/+3.3V 网络

## 接口

### J3 StampIO_Pin

J3 针脚为 1=GND、2=5V、3=SDA、4=SCL、5=IO4、6=IO5、7=IO6、8=IO7、9=GND、10=IO3、11=IO2、12=IO1、13=IO0、14=3V3。

- 参数与网络：`pin_1=GND`；`pin_2=+5V`；`pin_3=SDA`；`pin_4=SCL`；`pin_5=IO4`；`pin_6=IO5`；`pin_7=IO6`；`pin_8=IO7`；`pin_9=GND`；`pin_10=IO3`；`pin_11=IO2`；`pin_12=IO1`；`pin_13=IO0`；`pin_14=+3.3V`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 C1-C2 J3

### J1 HY-2.0_IIC

J1.1=SCL、J1.2=SDA、J1.3=+5V、J1.4=GND；信号直接连接 3.3V 供电的 U1，图中没有电平转换。

- 参数与网络：`pin_1=SCL`；`pin_2=SDA`；`pin_3=+5V`；`pin_4=GND`；`level_shifter_shown=false`；`mcu_rail=+3.3V`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 B3 J1

## 总线

### U1 I2C

U1 PA9 pin17 连接 SCL，PA10 pin18 连接 SDA；两网同时进入 J1 和 J3，当前页未画 SCL/SDA 上拉电阻。

- 参数与网络：`scl=U1 PA9 pin17 -> J1.1/J3.4`；`sda=U1 PA10 pin18 -> J1.2/J3.3`；`pullups_shown=false`；`device=U1`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 U1 PA9/PA10 与 J1/J3

## GPIO 与控制信号

### IO0~IO7

U1 PA0/PA1/PA2/PA3/PA4/PA5/PA6/PA7 分别直接连接 IO0/IO1/IO2/IO3/IO4/IO5/IO6/IO7。

- 参数与网络：`IO0=U1 PA0 pin6`；`IO1=U1 PA1 pin7`；`IO2=U1 PA2 pin8`；`IO3=U1 PA3 pin9`；`IO4=U1 PA4 pin10`；`IO5=U1 PA5 pin11`；`IO6=U1 PA6 pin12`；`IO7=U1 PA7 pin13`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 B1-B2 U1 PA0-PA7

## 时钟

### U1 时钟

U1 PF0/OSC_IN 与 PF1/OSC_OUT 均标未连接，完整页面没有外部晶振或振荡器。

- 参数与网络：`PF0=NC`；`PF1=NC`；`crystal_shown=false`；`oscillator_shown=false`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 U1 PF0/PF1 未连接

## 复位

### U1 BOOT0/NRST

U1 BOOT0 pin1 经 R1 10K 下拉 GND；NRST pin4 连接 RST，由 R2 10K 上拉 +3.3V、C1 100nF 对地。

- 参数与网络：`boot0=U1.1 via R1 10K to GND`；`nrst=U1.4 RST`；`reset_pullup=R2 10K to +3.3V`；`reset_cap=C1 100nF to GND`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 B1 U1 左侧 reset/boot

## 保护电路

### 外部 IO/I2C 保护

J3 的 IO0~IO7 和 J1/J3 的 SCL/SDA 均直接连接 U1，当前页未画串联电阻、TVS/ESD 阵列、钳位器件或保险丝。

- 参数与网络：`series_resistors_shown=false`；`tvs_shown=false`；`esd_array_shown=false`；`clamps_shown=false`；`fuse_shown=false`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 J1/J3 外部信号网络

## 内存与 Flash

### 外部存储器

完整原理图未展示 U1 之外的 Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页完整图无外部存储器

## 调试与烧录

### P1 SWD_5p

P1.1=+3.3V、2=SWCLK、3=SWDIO、4=RST、5=GND；SWCLK/SWDIO 分别连接 U1 PA14/PA13。

- 参数与网络：`pin_1=+3.3V`；`pin_2=SWCLK U1 PA14`；`pin_3=SWDIO U1 PA13`；`pin_4=RST U1 NRST`；`pin_5=GND`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 B4 P1 与 U1 PA13/PA14

## 模拟电路

### IO0~IO7 模拟路径

IO0~IO7 均直接连接 U1 PA0~PA7，没有外部运放、分压、滤波或 ADC 参考网络；模拟采样范围和精度由 MCU/固件决定。

- 参数与网络：`channels=IO0-IO7`；`mcu_pins=PA0-PA7`；`external_amplifier_shown=false`；`divider_shown=false`；`filter_shown=false`；`external_reference_shown=false`
- 证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 U1 PA0-PA7 到 J3 直连

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp IO | `mcu=U1 STM32F030F4P6`；`channels=IO0-IO7`；`bus=I2C SCL/SDA`；`regulator=U2 HT7533`；`connectors=J3,J1,P1` |
| GPIO 与控制信号 | IO0~IO7 | `IO0=U1 PA0 pin6`；`IO1=U1 PA1 pin7`；`IO2=U1 PA2 pin8`；`IO3=U1 PA3 pin9`；`IO4=U1 PA4 pin10`；`IO5=U1 PA5 pin11`；`IO6=U1 PA6 pin12`；`IO7=U1 PA7 pin13` |
| 总线 | U1 I2C | `scl=U1 PA9 pin17 -> J1.1/J3.4`；`sda=U1 PA10 pin18 -> J1.2/J3.3`；`pullups_shown=false`；`device=U1` |
| 总线地址 | Stamp IO I2C 地址 | `documented_default=0x45`；`documented_configurable=true`；`address_hardware_shown=false`；`firmware_controlled=true` |
| 接口 | J3 StampIO_Pin | `pin_1=GND`；`pin_2=+5V`；`pin_3=SDA`；`pin_4=SCL`；`pin_5=IO4`；`pin_6=IO5`；`pin_7=IO6`；`pin_8=IO7`；`pin_9=GND`；`pin_10=IO3`；`pin_11=IO2`；`pin_12=IO1`；`pin_13=IO0`；`pin_14=+3.3V` |
| 接口 | J1 HY-2.0_IIC | `pin_1=SCL`；`pin_2=SDA`；`pin_3=+5V`；`pin_4=GND`；`level_shifter_shown=false`；`mcu_rail=+3.3V` |
| 电源 | U2 HT7533 | `input=+5V`；`output=+3.3V`；`input_cap=C2 22uF(226) 20% 6.3V`；`output_caps=C3 22uF(226) 20% 6.3V,C4 100nF` |
| 电源 | +5V/+3.3V | `5v_nodes=J3.2,J1.3,U2 VIN`；`3v3_nodes=U1 VDD/VDDA,J3.14,P1.1`；`charger_shown=false`；`battery_shown=false`；`load_switch_shown=false`；`enable_shown=false` |
| 复位 | U1 BOOT0/NRST | `boot0=U1.1 via R1 10K to GND`；`nrst=U1.4 RST`；`reset_pullup=R2 10K to +3.3V`；`reset_cap=C1 100nF to GND` |
| 调试与烧录 | P1 SWD_5p | `pin_1=+3.3V`；`pin_2=SWCLK U1 PA14`；`pin_3=SWDIO U1 PA13`；`pin_4=RST U1 NRST`；`pin_5=GND` |
| 模拟电路 | IO0~IO7 模拟路径 | `channels=IO0-IO7`；`mcu_pins=PA0-PA7`；`external_amplifier_shown=false`；`divider_shown=false`；`filter_shown=false`；`external_reference_shown=false` |
| 其他事实 | 正文中的 IO 模式 | `documented_modes=digital input, digital output, ADC, Servo PWM, RGB LED, PWM`；`firmware_parameters=null`；`timing_on_schematic=null`；`resolution_on_schematic=null` |
| 接口 | IO0~IO7 电气电平 | `documented_level=3.3V`；`mcu_supply=+3.3V`；`level_shifter_shown=false`；`absolute_max=null`；`drive_current=null` |
| 保护电路 | 外部 IO/I2C 保护 | `series_resistors_shown=false`；`tvs_shown=false`；`esd_array_shown=false`；`clamps_shown=false`；`fuse_shown=false` |
| 时钟 | U1 时钟 | `PF0=NC`；`PF1=NC`；`crystal_shown=false`；`oscillator_shown=false` |
| 内存与 Flash | 外部存储器 | `flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `address.documented-0x45`：正文列出默认 I2C 地址 0x45 并称支持配置地址；原理图没有地址选择引脚、拨码或焊盘，地址行为由 U1 固件决定。（证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 U1/J1/J3 I2C 网络无地址硬件）
- `other.documented-io-modes`：正文称每路支持数字输入/输出、ADC、Servo、RGB LED 和 PWM；原理图只确认 PA0~PA7 直连，未定义各模式的固件定时、分辨率、频率或并发限制。（证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 U1/J3 仅显示 IO 直连）
- `interface.io-electrical-level`：U1 与 IO0~IO7 由 +3.3V 域直接连接，图中没有电平转换；正文标称 3.3V IO，但绝对最大值、容限和驱动电流未在原理图标注。（证据：图 68fd4bcfaddc / 第 1 页 / 第 1 页 U1 PA0-PA7 与 J3 IO0-IO7）
- `review.i2c-address`：请通过 Stamp IO 固件或 I2C 扫描确认默认 0x45 及地址修改机制。；原因：原理图没有地址选择硬件。
- `review.io-modes`：请依据内置固件协议确认各 IO 模式的通道限制、PWM/Servo 频率、ADC 分辨率和 RGB 时序。；原因：这些行为属于固件，原理图只显示 PA0~PA7 直连。
- `review.io-electrical`：请依据 STM32F030F4P6 数据手册和板级测试确认 IO 电压容限、最大驱动电流与 ADC 输入范围。；原因：原理图只确认 3.3V 域直连，不含绝对最大值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `68fd4bcfaddc900a6a0b7821445a09ec69a7d0bcff5e4e6955a81e5272c0f14a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/568/Sch_StampIO_sch_01.png` |

---

源文档：`zh_CN/stamp/stamp_io.md`

源文档 SHA-256：`379aa98bc67c3abf212e4d0e64d72a7ace5e729e2c7d02b8c8a419ee0f40813b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
