# Unit Scroll 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Scroll |
| SKU | U186 |
| 产品 ID | `unit-scroll-ed7a75d33f1d` |
| 源文档 | `zh_CN/unit/UNIT-Scroll.md` |

## 概述

Unit Scroll 以 STM32F030F4P6（U1）为控制器，通过 Grove J1 的 SCL/SDA 与外部主机通信，并采集 J3 旋转触点 A1/B1 和 SW1 按键。U1 PA0 的 RGB 网络驱动一颗 3V3 供电的 WS2812C-2020（U4），板上另提供 BOOT0 下拉、NRST RC 和 5 针 SWD 调试接口。Grove 输入的 VCC_5V 经 ME6206A33XG（U2）稳压为 3V3，供 MCU、I2C 上拉、编码器输入上拉和 RGB LED 使用。原理图未打印 I2C 地址，也未给出旋转编码器型号与每圈脉冲数。

## 检索关键词

`Unit Scroll`、`U186`、`STM32F030F4P6`、`ME6206A33XG`、`WS2812C-2020`、`GROVE 4P`、`Header 5`、`SWD_5P`、`I2C`、`0x40`、`EC10E`、`12 pulses`、`SCL`、`SDA`、`A1`、`B1`、`BTN1`、`RGB`、`VCC_5V`、`3V3`、`PA0`、`PA5`、`PA6`、`PA7`、`PA9`、`PA10`、`MCU_SWDIO`、`MCU_SWCLK`、`NRST`、`BOOT0`、`R15 10K`、`R16 10K`、`R1 10K`、`R2 10K`、`C1 47pF`、`C2 47pF`、`C3 10nF`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32F030F4P6 | 采集旋转触点与按键、驱动 RGB LED，并实现 I2C 从设备及 SWD 调试连接 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B1-C2，U1 STM32F030F4P6，pins 1~20 及 RGB/BTN1/A1/B1/SCL/SDA/MCU_SWDIO/MCU_SWCLK/NRST 网络 |
| U2 | ME6206A33XG | 将 Grove 输入的 VCC_5V 稳压为 3V3 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B2，U2 ME6206A33XG：VIN pin 3 接 VCC_5V、VOUT pin 2 接 3V3、GND pin 1 接地 |
| U4 | WS2812C-2020 | 由 U1 PA0 控制的单颗可寻址 RGB LED | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B3，U4 WS2812C-2020：DO pin 1、GND pin 2、DI pin 3/RGB、VDD pin 4/3V3 |
| J1 | GROVE 4P | 外部 SCL、SDA、5V 和 GND 接口 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B1，J1 GROVE 4P，从上到下标注 SCL、SDA、5V、GND |
| J2 | SWD_5P | U1 的 3V3 参考、SWCLK、SWDIO、NRST 和 GND 调试/烧录接口 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 D1，J2 SWD_5P，自上而下为 VCC、SWCLK、SWDIO、NRST、GND |
| J3 | Header 5 | 旋转机构的 A、B、公共端 C 与两个外壳接点接口 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C3，J3 Header 5，引脚标注 A、B、C、SHELL、SHELL；A/B 接 A1/B1，C 与两个 SHELL 接 GND |
| SW1 | 未标注 | 低有效用户按键，COM 接 BTN1、NO 接 GND、NC 未连接 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C3，SW1 COM/NO/NC：COM 接 BTN1，NO 接 GND，NC 悬空 |
| R15/R16 | 10K | SCL 与 SDA 到 3V3 的 I2C 上拉电阻 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B1，R15/R16 均标 10K，上端接 3V3，下端分别接 SCL/SDA |
| R1/R2/C1/C2/C3 | 10K / 10K / 47pF / 47pF / 10nF | A1/B1 上拉与对地滤波网络 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C1/C3，A1 经 R1 10K 上拉、C2 47pF 与 C3 10nF 对地；B1 经 R2 10K 上拉、C1 47pF 对地 |
| R3 | 10K | BTN1 到 3V3 的上拉电阻 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C3，R3 10K 位于 3V3 与 BTN1/SW1 COM 之间 |
| R6 | 10K | U1 BOOT0 到 GND 的下拉电阻 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C2，U1 BOOT0 pin 1 经 R6 10K 接 GND |
| R7/C9 | 10K / 100nF | U1 NRST 的 3V3 上拉与对地复位电容 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C2，NRST 节点经 R7 10K 接 3V3、经 C9 100nF 接 GND |
| C5/C7/C8 | 10uF / 100nF / 10uF | U2 的 VCC_5V 输入滤波与 3V3 输出滤波 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B2，C5 10uF 跨 VCC_5V/GND，C7 100nF 与 C8 10uF 跨 3V3/GND |
| C10/C11 | 100nF / 10uF | U1 VDD/VDDA 的 3V3 去耦与储能电容 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C1，U1 VDD pin 16/VDDA pin 5 的 3V3 节点经 C10 100nF、C11 10uF 接 GND |
| C12 | 100nF | U4 3V3 电源去耦 | 图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B3，C12 100nF 跨 U4 VDD 所在 3V3 与 GND |

## 系统结构

### Unit Scroll

U1 STM32F030F4P6 通过 J1 的 SCL/SDA 对外通信，采集 J3 的 A1/B1 与 SW1 的 BTN1，并以 PA0/RGB 驱动 U4 WS2812C-2020；U2 将 VCC_5V 转换为 3V3。

- 参数与网络：`controller=U1 STM32F030F4P6`；`communication=J1 SCL,SDA`；`rotation_inputs=J3 A1,B1`；`button=SW1 BTN1`；`rgb=U4 WS2812C-2020`；`power=J1 VCC_5V->U2 ME6206A33XG->3V3`
- 证据：图 a3cef0e2d48f / 第 1 页 / 整页：U1/U2/U4/J1/J2/J3/SW1 与 SCL/SDA/A1/B1/BTN1/RGB/VCC_5V/3V3 同名网络

## 核心器件

### U1 STM32F030F4P6

U1 使用 PA0 pin 6 驱动 RGB，PA5 pin 11 采集 BTN1，PA6 pin 12 采集 A1，PA7 pin 13 采集 B1，PA9 pin 17 接 SCL，PA10 pin 18 接 SDA，PA13 pin 19 接 MCU_SWDIO，PA14 pin 20 接 MCU_SWCLK。

- 参数与网络：`PA0_pin6=RGB`；`PA5_pin11=BTN1`；`PA6_pin12=A1`；`PA7_pin13=B1`；`PA9_pin17=SCL`；`PA10_pin18=SDA`；`PA13_pin19=MCU_SWDIO`；`PA14_pin20=MCU_SWCLK`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B1-C2，U1 左侧 PA0/PA5/PA6/PA7/PA9/PA10/PA13/PA14 的 pin 编号与网络名

### J3 Header 5

J3 A 接 A1，B 接 B1，C 接 GND，两个 SHELL 端也接 GND。

- 参数与网络：`A=A1`；`B=B1`；`C=GND`；`SHELL_1=GND`；`SHELL_2=GND`；`reference=J3`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C3，J3 A/B/C/SHELL/SHELL 五条引线与 A1/B1/GND 连线

## 电源

### U2 ME6206A33XG

U2 VIN pin 3 接 VCC_5V，VOUT pin 2 输出 3V3，GND pin 1 接地；C5 10uF 位于输入侧，C7 100nF 与 C8 10uF 位于输出侧。

- 参数与网络：`input=VIN pin 3,VCC_5V`；`output=VOUT pin 2,3V3`；`ground=pin 1,GND`；`input_capacitor=C5 10uF`；`output_capacitors=C7 100nF,C8 10uF`；`enable=null`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B2，U2/C5/C7/C8/VCC_5V/3V3/GND

### U1 电源

U1 VDD pin 16 与 VDDA pin 5 接 3V3，VSS pin 15 接 GND；C10 100nF 与 C11 10uF 跨接 3V3 和 GND。

- 参数与网络：`vdd=pin 16,3V3`；`vdda=pin 5,3V3`；`vss=pin 15,GND`；`decoupling=C10 100nF,C11 10uF`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C1-C2，U1 VDD/VDDA/VSS pins 16/5/15 与 C10/C11

### U4 电源

U4 VDD pin 4 接 3V3、GND pin 2 接地，C12 100nF 跨接 3V3 与 GND。

- 参数与网络：`vdd=pin 4,3V3`；`ground=pin 2,GND`；`decoupling=C12 100nF`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B3，U4 VDD/GND pins 4/2 与 C12 100nF

## 接口

### J1 GROVE 4P

J1 从上到下的四个位置标为 SCL、SDA、5V、GND；SCL/SDA 接 U1，5V 进入 VCC_5V 电源网，GND 接地。原理图未标注连接器数字针脚号或信号方向。

- 参数与网络：`position_1_top=SCL`；`position_2=SDA`；`position_3=5V,VCC_5V`；`position_4_bottom=GND`；`signal_voltage=3V3 pull-up via R15/R16`；`direction_marking=not shown`；`pin_numbers=not shown`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B1，J1 GROVE 4P 四条引线标签与 R15/R16/VCC_5V/GND

### 未使用的 U1 引脚

U1 PA1 pin 7、PA2 pin 8、PA3 pin 9、PA4 pin 10 与 PB1 pin 14 在页面无网络连接；PF0/PF1 的未连接情况另见时钟事实。

- 参数与网络：`unused_gpio=PA1.7,PA2.8,PA3.9,PA4.10,PB1.14`；`unused_clock_pins=PF0.2,PF1.3`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B1-B2，U1 PA1/PA2/PA3/PA4/PB1 与 PF0/PF1 的未连接端点

## 总线

### U1 I2C

SCL 在 J1 与 U1 PA9 pin 17 之间同名连接，SDA 在 J1 与 U1 PA10 pin 18 之间同名连接；R15/R16 各 10K 将 SCL/SDA 上拉到 3V3。

- 参数与网络：`controller_device=U1 STM32F030F4P6`；`scl=J1 SCL->U1 PA9 pin 17`；`sda=J1 SDA->U1 PA10 pin 18`；`pullups=R15/R16 10K to 3V3`；`bus_level=3V3 pull-up`；`external_connector=J1 GROVE 4P`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B1-C2，J1/R15/R16 与 U1 PA9/PA10 的 SCL/SDA 同名网络

### U4 WS2812C-2020 数据链

U1 PA0 pin 6 的 RGB 网络连接 U4 DI pin 3；U4 DO pin 1 在页面未继续连接。

- 参数与网络：`controller=U1 STM32F030F4P6`；`controller_pin=PA0 pin 6`；`data_net=RGB`；`led_input=U4 DI pin 3`；`led_output=U4 DO pin 1 no-connect`；`device_count=1`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B1/B3，U1 PA0/RGB 与 U4 DI pin 3 同名网络，U4 DO pin 1 无后续连线

## GPIO 与控制信号

### A1/B1 旋转输入

J3 A/A1 连接 U1 PA6 pin 12，由 R1 10K 上拉到 3V3，并由 C2 47pF 与 C3 10nF 对地；J3 B/B1 连接 U1 PA7 pin 13，由 R2 10K 上拉到 3V3，并由 C1 47pF 对地。

- 参数与网络：`phase_a=J3 A/A1->U1 PA6 pin 12`；`phase_a_pullup=R1 10K to 3V3`；`phase_a_filter=C2 47pF,C3 10nF to GND`；`phase_b=J3 B/B1->U1 PA7 pin 13`；`phase_b_pullup=R2 10K to 3V3`；`phase_b_filter=C1 47pF to GND`；`common=J3 C,GND`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C1-C3，U1 PA6/PA7、A1/B1、R1/R2、C1/C2/C3 与 J3 A/B/C

### SW1 BTN1

BTN1 连接 U1 PA5 pin 11，并由 R3 10K 上拉到 3V3；SW1 COM 接 BTN1、NO 接 GND、NC 未连接，闭合 COM-NO 时 BTN1 被拉低。

- 参数与网络：`mcu_pin=U1 PA5 pin 11`；`pullup=R3 10K to 3V3`；`switch_common=SW1 COM,BTN1`；`switch_no=SW1 NO,GND`；`switch_nc=no-connect`；`active_level=low`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C1/C3，U1 PA5/BTN1 同名网络与 R3/SW1 COM-NO-NC

## 时钟

### U1 PF0/PF1 时钟引脚

U1 PF0-OSC_IN pin 2 与 PF1-OSC_OUT pin 3 在页面未连接，整页没有外部晶振、谐振器或有源振荡器。

- 参数与网络：`osc_in=PF0 pin 2 no-connect`；`osc_out=PF1 pin 3 no-connect`；`external_clock_component=null`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 B2，U1 PF0-OSC_IN/PF1-OSC_OUT pins 2/3 未连接；整页无晶振位号

## 复位

### U1 NRST

U1 NRST pin 4 由 R7 10K 上拉到 3V3，并由 C9 100nF 接 GND；NRST 同名网络还引至 J2。

- 参数与网络：`mcu_pin=NRST pin 4`；`pullup=R7 10K to 3V3`；`capacitor=C9 100nF to GND`；`debug_connector=J2 NRST`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C2/D1，U1 NRST pin 4、R7/C9 与 J2 NRST 同名网络

### U1 BOOT0

U1 BOOT0 pin 1 通过 R6 10K 下拉到 GND。

- 参数与网络：`mcu_pin=BOOT0 pin 1`；`resistor=R6 10K`；`strap=GND`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C2，U1 BOOT0 pin 1-R6 10K-GND

## 保护电路

### 外部接口与电源保护

本页未绘出 TVS、ESD 阵列、保险丝、反接保护或浪涌限制器件。

- 参数与网络：`tv_suppressor=null`；`esd_array=null`；`fuse=null`；`reverse_polarity=null`；`surge_limiter=null`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 整页，J1/U2/J3/SW1 周边及全部位号中无 TVS/ESD/FUSE/反接保护器件

## 关键网络

### Unit Scroll 关键网络索引

关键信号路径为 J3 A/B→A1/B1→U1 PA6/PA7，SW1→BTN1→U1 PA5，U1 PA0→RGB→U4 DI，J1 SCL/SDA→U1 PA9/PA10，以及 J1 5V→VCC_5V→U2→3V3。

- 参数与网络：`rotation=J3 A/B-A1/B1-U1 PA6/PA7`；`button=SW1 COM-BTN1-U1 PA5`；`rgb=U1 PA0-RGB-U4 DI`；`i2c=J1 SCL/SDA-U1 PA9/PA10`；`power=J1 5V-VCC_5V-U2-3V3`；`debug=J2-MCU_SWCLK/MCU_SWDIO/NRST`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 整页，A1/B1/BTN1/RGB/SCL/SDA/VCC_5V/3V3/MCU_SWCLK/MCU_SWDIO/NRST 同名网络

## 存储

### 外部存储连接

本页未绘出存储器件、存储卡连接器或 SDIO/SPI 存储连接。

- 参数与网络：`storage_device=null`；`card_connector=null`；`sdio=null`；`spi_storage=null`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 整页，器件仅含 U1/U2/U4、J1/J2/J3、SW1 及阻容，无存储器或存储接口

## 内存与 Flash

### 外部存储器

U1 周边未绘出独立 Flash、EEPROM、SRAM 或 PSRAM。

- 参数与网络：`flash=null`；`eeprom=null`；`sram=null`；`psram=null`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 整页，U1 所有外连网络及器件清单中无外部存储器

## 音频

### 音频链路

本页未绘出麦克风、扬声器、编解码器、放大器或 I2S 音频网络。

- 参数与网络：`microphone=null`；`speaker=null`；`codec=null`；`amplifier=null`；`i2s=null`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 整页，全部器件与网络中无音频器件或 I2S 信号

## 传感器

### 传感器连接

本页未绘出独立传感器 IC 或传感器连接器；J3 与 SW1 为机械输入触点。

- 参数与网络：`sensor_ic=null`；`sensor_connector=null`；`mechanical_inputs=J3,SW1`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 整页，功能输入仅见 J3 A/B/C/SHELL 与 SW1 COM/NO/NC

## 射频

### 射频链路

本页未绘出天线、射频收发器、匹配网络或射频连接器。

- 参数与网络：`antenna=null`；`transceiver=null`；`matching_network=null`；`rf_connector=null`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 整页，全部器件与连接器中无 RF/ANT 网络或射频器件

## 调试与烧录

### J2 SWD_5P

J2 自上而下标为 VCC、SWCLK、SWDIO、NRST、GND，分别连接 3V3、U1 PA14 pin 20、U1 PA13 pin 19、U1 NRST pin 4 和 GND；原理图未打印 J2 数字针脚号。

- 参数与网络：`position_1_top=VCC,3V3`；`position_2=SWCLK,MCU_SWCLK,U1 PA14 pin 20`；`position_3=SWDIO,MCU_SWDIO,U1 PA13 pin 19`；`position_4=NRST,U1 pin 4`；`position_5_bottom=GND`；`pin_numbers=not shown`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 D1 与 C1-C2，J2 五条信号及 U1 MCU_SWCLK/MCU_SWDIO/NRST 同名网络

## 模拟电路

### 模拟采样链路

本页未绘出运算放大器、ADC 前端、分压采样或模拟传感器；A1/B1/BTN1 均作为数字触点网络连接 U1 GPIO。

- 参数与网络：`op_amp=null`；`adc_front_end=null`；`voltage_divider=null`；`analog_sensor=null`；`digital_contact_nets=A1,B1,BTN1`
- 证据：图 a3cef0e2d48f / 第 1 页 / 页 1 整页，A1/B1/BTN1 直接连接 U1 PA6/PA7/PA5，未见模拟前端器件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Scroll | `controller=U1 STM32F030F4P6`；`communication=J1 SCL,SDA`；`rotation_inputs=J3 A1,B1`；`button=SW1 BTN1`；`rgb=U4 WS2812C-2020`；`power=J1 VCC_5V->U2 ME6206A33XG->3V3` |
| 核心器件 | U1 STM32F030F4P6 | `PA0_pin6=RGB`；`PA5_pin11=BTN1`；`PA6_pin12=A1`；`PA7_pin13=B1`；`PA9_pin17=SCL`；`PA10_pin18=SDA`；`PA13_pin19=MCU_SWDIO`；`PA14_pin20=MCU_SWCLK` |
| 电源 | U2 ME6206A33XG | `input=VIN pin 3,VCC_5V`；`output=VOUT pin 2,3V3`；`ground=pin 1,GND`；`input_capacitor=C5 10uF`；`output_capacitors=C7 100nF,C8 10uF`；`enable=null` |
| 电源 | U1 电源 | `vdd=pin 16,3V3`；`vdda=pin 5,3V3`；`vss=pin 15,GND`；`decoupling=C10 100nF,C11 10uF` |
| 电源 | U4 电源 | `vdd=pin 4,3V3`；`ground=pin 2,GND`；`decoupling=C12 100nF` |
| 接口 | J1 GROVE 4P | `position_1_top=SCL`；`position_2=SDA`；`position_3=5V,VCC_5V`；`position_4_bottom=GND`；`signal_voltage=3V3 pull-up via R15/R16`；`direction_marking=not shown`；`pin_numbers=not shown` |
| 总线 | U1 I2C | `controller_device=U1 STM32F030F4P6`；`scl=J1 SCL->U1 PA9 pin 17`；`sda=J1 SDA->U1 PA10 pin 18`；`pullups=R15/R16 10K to 3V3`；`bus_level=3V3 pull-up`；`external_connector=J1 GROVE 4P` |
| 总线地址 | Unit Scroll I2C 地址 | `device=U1 STM32F030F4P6`；`schematic_address=null`；`address_selector=null`；`product_document_value=0x40`；`verification_source_needed=firmware or communication protocol` |
| 核心器件 | J3 Header 5 | `A=A1`；`B=B1`；`C=GND`；`SHELL_1=GND`；`SHELL_2=GND`；`reference=J3` |
| GPIO 与控制信号 | A1/B1 旋转输入 | `phase_a=J3 A/A1->U1 PA6 pin 12`；`phase_a_pullup=R1 10K to 3V3`；`phase_a_filter=C2 47pF,C3 10nF to GND`；`phase_b=J3 B/B1->U1 PA7 pin 13`；`phase_b_pullup=R2 10K to 3V3`；`phase_b_filter=C1 47pF to GND`；`common=J3 C,GND` |
| 核心器件 | 旋转编码器型号与分辨率 | `schematic_part_number=null`；`schematic_pulses_per_revolution=null`；`schematic_detents=null`；`product_document_part_number=EC10E`；`product_document_resolution=12 pulses per rotation`；`verification_source_needed=BOM or encoder datasheet tied to this schematic revision` |
| GPIO 与控制信号 | SW1 BTN1 | `mcu_pin=U1 PA5 pin 11`；`pullup=R3 10K to 3V3`；`switch_common=SW1 COM,BTN1`；`switch_no=SW1 NO,GND`；`switch_nc=no-connect`；`active_level=low` |
| 总线 | U4 WS2812C-2020 数据链 | `controller=U1 STM32F030F4P6`；`controller_pin=PA0 pin 6`；`data_net=RGB`；`led_input=U4 DI pin 3`；`led_output=U4 DO pin 1 no-connect`；`device_count=1` |
| 复位 | U1 NRST | `mcu_pin=NRST pin 4`；`pullup=R7 10K to 3V3`；`capacitor=C9 100nF to GND`；`debug_connector=J2 NRST` |
| 复位 | U1 BOOT0 | `mcu_pin=BOOT0 pin 1`；`resistor=R6 10K`；`strap=GND` |
| 调试与烧录 | J2 SWD_5P | `position_1_top=VCC,3V3`；`position_2=SWCLK,MCU_SWCLK,U1 PA14 pin 20`；`position_3=SWDIO,MCU_SWDIO,U1 PA13 pin 19`；`position_4=NRST,U1 pin 4`；`position_5_bottom=GND`；`pin_numbers=not shown` |
| 时钟 | U1 PF0/PF1 时钟引脚 | `osc_in=PF0 pin 2 no-connect`；`osc_out=PF1 pin 3 no-connect`；`external_clock_component=null` |
| 接口 | 未使用的 U1 引脚 | `unused_gpio=PA1.7,PA2.8,PA3.9,PA4.10,PB1.14`；`unused_clock_pins=PF0.2,PF1.3` |
| 保护电路 | 外部接口与电源保护 | `tv_suppressor=null`；`esd_array=null`；`fuse=null`；`reverse_polarity=null`；`surge_limiter=null` |
| 关键网络 | Unit Scroll 关键网络索引 | `rotation=J3 A/B-A1/B1-U1 PA6/PA7`；`button=SW1 COM-BTN1-U1 PA5`；`rgb=U1 PA0-RGB-U4 DI`；`i2c=J1 SCL/SDA-U1 PA9/PA10`；`power=J1 5V-VCC_5V-U2-3V3`；`debug=J2-MCU_SWCLK/MCU_SWDIO/NRST` |
| 存储 | 外部存储连接 | `storage_device=null`；`card_connector=null`；`sdio=null`；`spi_storage=null` |
| 内存与 Flash | 外部存储器 | `flash=null`；`eeprom=null`；`sram=null`；`psram=null` |
| 音频 | 音频链路 | `microphone=null`；`speaker=null`；`codec=null`；`amplifier=null`；`i2s=null` |
| 传感器 | 传感器连接 | `sensor_ic=null`；`sensor_connector=null`；`mechanical_inputs=J3,SW1` |
| 射频 | 射频链路 | `antenna=null`；`transceiver=null`；`matching_network=null`；`rf_connector=null` |
| 模拟电路 | 模拟采样链路 | `op_amp=null`；`adc_front_end=null`；`voltage_divider=null`；`analog_sensor=null`；`digital_contact_nets=A1,B1,BTN1` |

## 待确认事项

- `address.i2c-not-shown`：原理图显示 U1 的 SCL/SDA 连接，但本页未打印 I2C 从机地址，也没有硬件地址选择网络。（证据：图 a3cef0e2d48f / 第 1 页 / 页 1 整页，U1/J1 SCL/SDA 区域无 0x 地址、ADDR 引脚或地址拨码）
- `component.encoder-spec-not-shown`：原理图仅以 J3 Header 5 表示 A/B/C 与两个 SHELL 接点，没有打印旋转编码器型号、每圈脉冲数、机械定位数或 A/B 相时序。（证据：图 a3cef0e2d48f / 第 1 页 / 页 1 网格 C3，J3 仅标 Header 5 与 A/B/C/SHELL/SHELL，无 EC10E 或脉冲参数）
- `review.i2c-address`：Unit Scroll 当前固件使用的 I2C 从机地址是否为产品正文所列的 0x40？；原因：I2C 地址由 STM32 固件实现，原理图未打印地址值或硬件地址选择电路。
- `review.encoder-spec`：J3 所接旋转编码器是否为 EC10E，且分辨率是否为每圈 12 脉冲？；原因：产品正文给出 EC10E 和 12 脉冲/转，但本版本原理图只标 J3 Header 5，无法从原理图独立确认机械型号与分辨率。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a3cef0e2d48f46f17165bcb9fd705dd4f81594c1e2054dae06782256c391c868` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/773/U186_SCH_SCH_UNIT_Scroll_V1.0_2024_07_01_18_29_10_page_01.png` |

---

源文档：`zh_CN/unit/UNIT-Scroll.md`

源文档 SHA-256：`ff699f22ea5e4763d4f377ad17fc885e25fe10d15362a25d1ee98719adcb2b48`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
