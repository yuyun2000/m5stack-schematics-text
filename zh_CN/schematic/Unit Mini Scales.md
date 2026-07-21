# Unit Mini Scales 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Mini Scales |
| SKU | U177 |
| 产品 ID | `unit-mini-scales-7a0edd9429d6` |
| 源文档 | `zh_CN/unit/Unit-Mini Scales.md` |

## 概述

Unit Mini Scales 以 U3 STM32F030F4P6 为协议控制器，通过 PA9/PA10 的 SCL/SDA 连接 J1 Grove，并以 PA5/PA6 的 HX711_SDA/HX711_SCK 连接 U2 HX711。P1 引出 E+、E−、S−、S+ 四线称重桥；Q1 S8550 与 HX711 BASE/VFB 网络生成桥路激励，S± 经 100Ω/100nF 滤波进入 INA±。BUS_5V 由 U1 HX6306P332MR 生成 3V3，PA7 读取低有效按键、PB1 驱动 SK6812-3535，J2 提供 SWD；I2C 地址、5kg 传感器身份、称重标定和固件行为未直接印在图纸上。

## 检索关键词

`Unit Mini Scales`、`U177`、`STM32F030F4P6`、`HX711`、`HX6306P332MR`、`SK6812-3535`、`S8550`、`I2C`、`0x26`、`SCL PA9`、`SDA PA10`、`HX711_SDA PA5`、`HX711_SCK PA6`、`KEY PA7`、`RGB PB1`、`E+`、`E-`、`S-`、`S+`、`P1 Header 4`、`J1 GROVE 4P`、`J2 SWD`、`SWDIO`、`SWCLK`、`NRST`、`BOOT0`、`BUS_5V`、`3V3`、`load cell`、`CZL928MC`、`5kg scale`、`tare`、`zero calibration`、`firmware v3`、`firmware v4`、`I2C protocol v3`、`weight bridge`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | STM32F030F4P6 | I2C 协议与称重控制 MCU，连接 HX711、按键、RGB、SWD 和复位/BOOT 网络 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 C1-C2，U3 STM32F030F4P6 pins1-20 |
| U2 | HX711 | 称重桥模拟前端与 ADC，连接 E+/E−/S−/S+、激励反馈和 MCU 两线接口 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 C3-C4，U2 HX711 pins1-16 |
| U1 | HX6306P332MR | 将 BUS_5V 稳压为 3V3 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 B1，U1 HX6306P332MR、VIN/VOUT/GND |
| U4 | SK6812-3535 | 由 PB1/RGB 驱动的单颗可编程 RGB LED | 图 dd620fdfce59 / 第 1 页 / 第1页网格 B3-B4，U4 SK6812-3535 DO/GND/DI/VDD |
| J1 | GROVE 4P | 外部 I2C 与 BUS_5V/GND 接口 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 B2，J1 GROVE 4P SCL/SDA/5V/GND |
| P1 | Header 4 | 四线称重桥接口，依次引出 E+、E−、S−、S+ | 图 dd620fdfce59 / 第 1 页 / 第1页网格 C3，P1 Header 4 pins4-1 E+/E-/S-/S+ |
| J2 | SWD | 五针 MCU 调试接口，引出 3V3、SWCLK、SWDIO、NRST、GND | 图 dd620fdfce59 / 第 1 页 / 第1页网格 D2，J2 SWD pins1-5 |
| Q1 | S8550 | 由 HX711 BASE 控制的称重桥 E+ 高边激励晶体管 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 C3，Q1 S8550、BUS_5V、E+ 与 U2 BASE |
| S1 | SW_TS_015 | 将 KEY/PA7 按下接 GND 的低有效功能按键 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 C2，S1 SW_TS_015、KEY、GND |
| R5/R6/C6 | 20KΩ / 8.2KΩ / 10uF | HX711 VFB 反馈分压与 E+ 激励电源滤波 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 C3-C4，E+/Q1/R5/R6/U2 VFB/C6 |
| R8/R4/C5 | 100Ω / 100Ω / 100nF | S−/S+ 到 HX711 INA−/INA+ 的对称输入滤波网络 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 C3-C4，P1 S-/S+、R8/R4、C5、U2 INA-/INA+ |
| R9/R10 | 4.7KΩ / 4.7KΩ | SCL/SDA 到 3V3 的 I2C 上拉电阻 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 B2，R9/R10 4.7K、3V3、SCL/SDA |
| R11/C7 | 10KΩ / 100nF | KEY 的 3V3 上拉与对地滤波/去抖网络 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 C2，KEY/R11 10K/C7 100nF/S1 |
| R1/C1/R7 | 10KΩ / 100nF / 10KΩ | NRST 的上拉/RC 与 BOOT0 的对地下拉网络 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 C1-D1，U3 BOOT0/NRST、R1/C1/R7 |
| FB1 | 330R/GZ1005D331TF | BUS_5V 到 HX711 DVDD pin16 的串联磁珠/滤波器件 | 图 dd620fdfce59 / 第 1 页 / 第1页网格 C4，FB1 330R/GZ1005D331TF、BUS_5V、U2 DVDD |

## 系统结构

### Unit Mini Scales 系统架构

U3 STM32F030F4P6 通过 Grove I2C 与外部主机通信，以 HX711_SDA/HX711_SCK 读取 U2 HX711，U2 接 P1 四线称重桥；板上另有按键、RGB、SWD 与 5V转3.3V电源。

- 参数与网络：`controller=U3 STM32F030F4P6`；`adc=U2 HX711`；`sensor_interface=P1 E+/E-/S-/S+`；`host=J1 GROVE I2C`；`button=S1 KEY`；`rgb=U4 SK6812-3535`；`debug=J2 SWD`；`power=U1 HX6306P332MR`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页完整单页 U1-U4/J1/J2/P1/Q1/S1

## 核心器件

### U3 关键 GPIO 映射

U3 PB1 pin14=RGB，PA5 pin11=HX711_SDA，PA6 pin12=HX711_SCK，PA7 pin13=KEY，PA9 pin17=SCL，PA10 pin18=SDA，PA13 pin19=SWDIO，PA14 pin20=SWCLK。

- 参数与网络：`PB1_pin14=RGB`；`PA5_pin11=HX711_SDA`；`PA6_pin12=HX711_SCK`；`PA7_pin13=KEY`；`PA9_pin17=SCL`；`PA10_pin18=SDA`；`PA13_pin19=SWDIO`；`PA14_pin20=SWCLK`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 C1-C2，U3 右侧 GPIO 与左上 PB1

### U2 HX711 关键针脚

U2 pins1-8 为 VSUP、BASE、AVDD、VFB、AGND、VBG、INA−、INA+；pins9/10 INB−/INB+ 接 GND，pin11 PD_SCK、pin12 DOUT，pin15 RATE 接 GND，pin16 DVDD 经 FB1 接 BUS_5V。

- 参数与网络：`pin1=VSUP / BUS_5V`；`pin2=BASE / Q1`；`pin3=AVDD / E+`；`pin4=VFB / R5-R6 node`；`pin5=AGND`；`pin6=VBG / C4`；`pin7=INA-`；`pin8=INA+`；`pins9_10=INB-/INB+ to GND`；`pin11=PD_SCK / HX711_SCK`；`pin12=DOUT / HX711_SDA`；`pin15=RATE to GND`；`pin16=DVDD via FB1 to BUS_5V`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 C3-C4，U2 HX711 pins1-16 与外部网络

## 电源

### BUS_5V 到 3V3

U1 HX6306P332MR VIN pin3 接 BUS_5V，VOUT pin2 输出 3V3，GND pin1 接地；输入 C2 100nF，输出 C8 100nF/C9 10uF。

- 参数与网络：`regulator=U1 HX6306P332MR`；`input=pin3 VIN / BUS_5V`；`output=pin2 VOUT / 3V3`；`ground=pin1`；`input_cap=C2 100nF`；`output_caps=C8 100nF; C9 10uF`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 B1，U1/C2/C8/C9/BUS_5V/3V3

### HX711 模拟与数字电源

U2 VSUP pin1 接 BUS_5V并配置 C10 10uF；DVDD pin16 经 FB1 330R/GZ1005D331TF 接 BUS_5V并配置 C11 10uF；AGND pin5 接地，VBG pin6 由 C4 100nF 旁路。

- 参数与网络：`vsup=pin1 BUS_5V / C10 10uF`；`dvdd=pin16 <- FB1 330R/GZ1005D331TF <- BUS_5V / C11 10uF`；`agnd=pin5 GND`；`vbg=pin6 / C4 100nF to GND`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 C3-C4，U2 VSUP/DVDD/AGND/VBG、FB1/C10/C11/C4

## 接口

### J1 Grove 针脚

J1 GROVE 4P 的 SCL 接 SCL，SDA 接 SDA，5V 接 BUS_5V，GND 接地。

- 参数与网络：`connector=J1 GROVE 4P`；`scl=SCL`；`sda=SDA`；`power=5V / BUS_5V`；`ground=GND`；`direction=SCL host output; SDA bidirectional`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 B2，J1 SCL/SDA/5V/GND 与网络名

### P1 四线称重桥

P1 pin4 为 E+、pin3 为 E−并接 GND、pin2 为 S−、pin1 为 S+。

- 参数与网络：`connector=P1 Header 4`；`pin4=E+ excitation positive`；`pin3=E- / GND`；`pin2=S- signal negative`；`pin1=S+ signal positive`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 C3，P1 pins4-1 E+/E-/S-/S+

## 总线

### 主机 I2C 路由

J1 SCL/SDA 分别连接 U3 PA9 pin17/PA10 pin18，并由 R9/R10 4.7KΩ上拉至 3V3。

- 参数与网络：`controller=external host via J1`；`device=U3 STM32F030F4P6 firmware`；`scl=J1 SCL -> U3 PA9 pin17`；`sda=J1 SDA -> U3 PA10 pin18`；`scl_pullup=R9 4.7KΩ`；`sda_pullup=R10 4.7KΩ`；`logic_rail=3V3`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 B2-C2，J1/R9/R10/U3 PA9/PA10

### MCU 与 HX711 两线接口

U2 DOUT pin12 形成 HX711_SDA 并连接 U3 PA5 pin11；U2 PD_SCK pin11 形成 HX711_SCK 并连接 U3 PA6 pin12。

- 参数与网络：`data=U2 pin12 DOUT / HX711_SDA -> U3 PA5 pin11`；`clock=U3 PA6 pin12 / HX711_SCK -> U2 pin11 PD_SCK`；`protocol=HX711 two-wire, not host I2C`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 C2-C4，U3 PA5/PA6 与 U2 DOUT/PD_SCK

## GPIO 与控制信号

### KEY 按键

U3 PA7 pin13 连接 KEY，R11 10KΩ将 KEY 上拉到 3V3，C7 100nF 对地，按下 S1 将 KEY 接 GND，形成低有效输入。

- 参数与网络：`mcu=U3 PA7 pin13`；`net=KEY`；`pullup=R11 10KΩ to 3V3`；`capacitor=C7 100nF to GND`；`switch=S1 SW_TS_015 to GND`；`active_level=low`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 C2，U3 PA7/KEY/R11/C7/S1

### SK6812 RGB

U3 PB1 pin14 的 RGB 网络连接 U4 DI pin3；U4 VDD pin4 接 3V3、GND pin2 接地、DO pin1 未连接。

- 参数与网络：`mcu=U3 PB1 pin14`；`net=RGB`；`led=U4 SK6812-3535`；`data_in=pin3`；`supply=pin4 3V3`；`ground=pin2`；`data_out=pin1 unconnected`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 C1 与 B3-B4，U3 PB1/RGB/U4

## 时钟

### 外部时钟

U3 PF0-OSC_IN/PF1-OSC_OUT 未连接，U2 XI/XO 周围也未显示晶振或外部时钟器件；U2 RATE pin15 接 GND。

- 参数与网络：`mcu_osc_in=U3 pin2 unconnected`；`mcu_osc_out=U3 pin3 unconnected`；`hx711_xi_xo=no external oscillator shown`；`hx711_rate=pin15 to GND`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页 U3 PF0/PF1 与 U2 XI/XO/RATE 周边

## 复位

### BOOT0 与 NRST

U3 BOOT0 pin1 经 R7 10KΩ下拉到 GND；NRST pin4 由 R1 10KΩ上拉至 3V3、C1 100nF 对地，并引至 J2 pin4。

- 参数与网络：`boot=U3 pin1 BOOT0 -> R7 10KΩ -> GND`；`reset=U3 pin4 NRST`；`reset_pullup=R1 10KΩ to 3V3`；`reset_cap=C1 100nF to GND`；`debug=J2 pin4 NRST`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 C1-D2，U3 BOOT0/NRST、R7/R1/C1/J2

## 保护电路

### Grove 与称重桥保护

J1 BUS_5V/SCL/SDA 与 P1 E+/E−/S−/S+ 路径未显示保险丝、TVS 或专用 ESD 器件；P1 信号端只有 100Ω/100nF 滤波。

- 参数与网络：`power_fuse=not shown`；`grove_esd=not shown`；`bridge_tvs=not shown`；`signal_filter=R8/R4 100Ω; C5 100nF`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页 J1/P1 至 U1/U2/U3 全部外部接口路径

## 调试与烧录

### J2 SWD 接口

J2 pins1-5 依次为 3V3、SWCLK、SWDIO、NRST、GND，对应 U3 PA14/PA13/NRST。

- 参数与网络：`pin1=3V3`；`pin2=SWCLK / U3 PA14 pin20`；`pin3=SWDIO / U3 PA13 pin19`；`pin4=NRST / U3 pin4`；`pin5=GND`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 D2，J2 pins1-5 与 U3 SWDIO/SWCLK/NRST

## 模拟电路

### 称重桥 E+ 激励

Q1 S8550 从 BUS_5V 向 E+ 提供高边激励，U2 BASE pin2 驱动 Q1，AVDD pin3 接 E+，VFB pin4 监测 R5 20KΩ/R6 8.2KΩ分压；C6 10uF 从 E+ 对地。

- 参数与网络：`source=BUS_5V`；`transistor=Q1 S8550`；`control=U2 pin2 BASE`；`excitation=E+ / U2 pin3 AVDD`；`feedback=U2 pin4 VFB / R5 20KΩ / R6 8.2KΩ`；`filter=C6 10uF`；`negative=E- / GND`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 C3-C4，BUS_5V/Q1/E+/R5/R6/U2 BASE/AVDD/VFB/C6

### S−/S+ 输入滤波

P1 S−/S+ 分别经 R8/R4 100Ω进入 U2 INA− pin7/INA+ pin8，C5 100nF 配置在输入线之间形成差分滤波。

- 参数与网络：`negative=P1 S- -> R8 100Ω -> U2 pin7 INA-`；`positive=P1 S+ -> R4 100Ω -> U2 pin8 INA+`；`differential_cap=C5 100nF`
- 证据：图 dd620fdfce59 / 第 1 页 / 第1页网格 C3-C4，P1 S-/S+、R8/R4/C5、U2 INA-/INA+

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Mini Scales 系统架构 | `controller=U3 STM32F030F4P6`；`adc=U2 HX711`；`sensor_interface=P1 E+/E-/S-/S+`；`host=J1 GROVE I2C`；`button=S1 KEY`；`rgb=U4 SK6812-3535`；`debug=J2 SWD`；`power=U1 HX6306P332MR` |
| 核心器件 | U3 关键 GPIO 映射 | `PB1_pin14=RGB`；`PA5_pin11=HX711_SDA`；`PA6_pin12=HX711_SCK`；`PA7_pin13=KEY`；`PA9_pin17=SCL`；`PA10_pin18=SDA`；`PA13_pin19=SWDIO`；`PA14_pin20=SWCLK` |
| 电源 | BUS_5V 到 3V3 | `regulator=U1 HX6306P332MR`；`input=pin3 VIN / BUS_5V`；`output=pin2 VOUT / 3V3`；`ground=pin1`；`input_cap=C2 100nF`；`output_caps=C8 100nF; C9 10uF` |
| 接口 | J1 Grove 针脚 | `connector=J1 GROVE 4P`；`scl=SCL`；`sda=SDA`；`power=5V / BUS_5V`；`ground=GND`；`direction=SCL host output; SDA bidirectional` |
| 总线 | 主机 I2C 路由 | `controller=external host via J1`；`device=U3 STM32F030F4P6 firmware`；`scl=J1 SCL -> U3 PA9 pin17`；`sda=J1 SDA -> U3 PA10 pin18`；`scl_pullup=R9 4.7KΩ`；`sda_pullup=R10 4.7KΩ`；`logic_rail=3V3` |
| 总线 | MCU 与 HX711 两线接口 | `data=U2 pin12 DOUT / HX711_SDA -> U3 PA5 pin11`；`clock=U3 PA6 pin12 / HX711_SCK -> U2 pin11 PD_SCK`；`protocol=HX711 two-wire, not host I2C` |
| 核心器件 | U2 HX711 关键针脚 | `pin1=VSUP / BUS_5V`；`pin2=BASE / Q1`；`pin3=AVDD / E+`；`pin4=VFB / R5-R6 node`；`pin5=AGND`；`pin6=VBG / C4`；`pin7=INA-`；`pin8=INA+`；`pins9_10=INB-/INB+ to GND`；`pin11=PD_SCK / HX711_SCK`；`pin12=DOUT / HX711_SDA`；`pin15=RATE to GND`；`pin16=DVDD via FB1 to BUS_5V` |
| 接口 | P1 四线称重桥 | `connector=P1 Header 4`；`pin4=E+ excitation positive`；`pin3=E- / GND`；`pin2=S- signal negative`；`pin1=S+ signal positive` |
| 模拟电路 | 称重桥 E+ 激励 | `source=BUS_5V`；`transistor=Q1 S8550`；`control=U2 pin2 BASE`；`excitation=E+ / U2 pin3 AVDD`；`feedback=U2 pin4 VFB / R5 20KΩ / R6 8.2KΩ`；`filter=C6 10uF`；`negative=E- / GND` |
| 模拟电路 | S−/S+ 输入滤波 | `negative=P1 S- -> R8 100Ω -> U2 pin7 INA-`；`positive=P1 S+ -> R4 100Ω -> U2 pin8 INA+`；`differential_cap=C5 100nF` |
| 电源 | HX711 模拟与数字电源 | `vsup=pin1 BUS_5V / C10 10uF`；`dvdd=pin16 <- FB1 330R/GZ1005D331TF <- BUS_5V / C11 10uF`；`agnd=pin5 GND`；`vbg=pin6 / C4 100nF to GND` |
| GPIO 与控制信号 | KEY 按键 | `mcu=U3 PA7 pin13`；`net=KEY`；`pullup=R11 10KΩ to 3V3`；`capacitor=C7 100nF to GND`；`switch=S1 SW_TS_015 to GND`；`active_level=low` |
| GPIO 与控制信号 | SK6812 RGB | `mcu=U3 PB1 pin14`；`net=RGB`；`led=U4 SK6812-3535`；`data_in=pin3`；`supply=pin4 3V3`；`ground=pin2`；`data_out=pin1 unconnected` |
| 调试与烧录 | J2 SWD 接口 | `pin1=3V3`；`pin2=SWCLK / U3 PA14 pin20`；`pin3=SWDIO / U3 PA13 pin19`；`pin4=NRST / U3 pin4`；`pin5=GND` |
| 复位 | BOOT0 与 NRST | `boot=U3 pin1 BOOT0 -> R7 10KΩ -> GND`；`reset=U3 pin4 NRST`；`reset_pullup=R1 10KΩ to 3V3`；`reset_cap=C1 100nF to GND`；`debug=J2 pin4 NRST` |
| 时钟 | 外部时钟 | `mcu_osc_in=U3 pin2 unconnected`；`mcu_osc_out=U3 pin3 unconnected`；`hx711_xi_xo=no external oscillator shown`；`hx711_rate=pin15 to GND` |
| 保护电路 | Grove 与称重桥保护 | `power_fuse=not shown`；`grove_esd=not shown`；`bridge_tvs=not shown`；`signal_filter=R8/R4 100Ω; C5 100nF` |
| 总线地址 | Unit Mini Scales I2C 地址 | `document_address=0x26`；`device=U3 firmware`；`schematic_address=not shown`；`address_straps=not shown` |
| 传感器 | 称重传感器型号与5kg量程 | `document_capacity=5kg`；`document_datasheet=CZL928MC`；`schematic_sensor=not shown`；`connector=P1 E+/E-/S-/S+`；`rated_load=not shown` |
| 传感器 | HX711 分辨率、增益、速率与标定 | `adc=U2 HX711`；`rate_pin=pin15 GND`；`resolution=not shown`；`gain=not shown`；`sample_rate=not shown`；`calibration=not shown`；`accuracy=not shown` |
| GPIO 与控制信号 | 按键清零与去皮行为 | `hardware=S1 -> KEY/PA7 active low`；`document_actions=zero calibration; tare`；`press_timing=not shown`；`firmware_state_machine=not shown` |
| 总线 | I2C 固件协议 v3/v4 | `document_firmware=v3; v4`；`document_protocol=I2C protocol v3`；`document_v4_change=negative weight allowed`；`registers=not shown`；`data_format=not shown`；`firmware_version_on_schematic=not shown` |
| 核心器件 | STM32 内核属性 | `schematic_mcu=STM32F030F4P6`；`document_architecture=32-bit ARM Cortex-M0`；`frequency=not shown`；`internal_memory=not shown` |
| GPIO 与控制信号 | RGB 状态语义 | `hardware=U3 PB1 -> U4 SK6812-3535 DI`；`colors=not shown`；`brightness=not shown`；`timing=not shown`；`status_mapping=not shown` |

## 待确认事项

- `address.i2c-0x26`：产品正文给出 0x26，但原理图没有地址文字或硬件地址选择网络；该地址由 U3 固件实现。（证据：图 dd620fdfce59 / 第 1 页 / 第1页 J1/U3 I2C 区，无地址注记）
- `sensor.load-cell-identity-capacity`：正文称集成 5kg 称重传感器并链接 CZL928MC 资料；原理图只画 P1 四线桥接口，没有传感器位号、型号或额定量程。（证据：图 dd620fdfce59 / 第 1 页 / 第1页 P1 Header 4，仅有桥路网络）
- `sensor.hx711-performance-calibration`：原理图确认 HX711 连接和 RATE 接地，但未标 ADC 分辨率、增益、采样速率、零点/满量程标定系数或称重误差。（证据：图 dd620fdfce59 / 第 1 页 / 第1页 U2 HX711 及 P1 模拟链，无性能/标定注记）
- `gpio.button-firmware-action`：正文称按键用于零点校准和去皮；图纸只确认 S1 使 PA7/KEY 变低，没有按压时长、状态机或固件动作。（证据：图 dd620fdfce59 / 第 1 页 / 第1页 U3 PA7/KEY/R11/C7/S1 电路）
- `bus.firmware-protocol`：正文列内置固件 v3/v4 并称通信协议沿用 v3，v4 可显示负重量；原理图不包含寄存器、数据格式、固件版本或负值处理逻辑。（证据：图 dd620fdfce59 / 第 1 页 / 第1页 U3/J1 I2C 电气连接，无固件协议）
- `component.mcu-architecture`：正文称 STM32F030F4P6 为 32位 ARM Cortex-M0；原理图只打印完整 MCU 型号和引脚，没有 CPU 内核或频率参数。（证据：图 dd620fdfce59 / 第 1 页 / 第1页 U3 型号与引脚符号）
- `gpio.rgb-firmware`：图纸确认 PB1 驱动 SK6812-3535，但未标颜色、亮度、数据时序或称重状态与灯效映射。（证据：图 dd620fdfce59 / 第 1 页 / 第1页 U3 PB1/RGB/U4 电路）
- `review.i2c-address`：请用 U177 固件或 I2C 实测确认默认 7 位地址为 0x26，并说明是否支持改址。；原因：地址由 MCU 固件实现，原理图没有地址字段或硬件选择。
- `review.load-cell-identity-capacity`：请用 U177 BOM、结构图和实装传感器丝印确认 CZL928MC 型号及 5kg 额定量程。；原因：原理图只给四线桥连接器，没有传感器型号或量程。
- `review.hx711-performance-calibration`：请用 HX711 资料、固件配置和校准流程确认分辨率、增益、采样率、标定系数与整机称重误差。；原因：原理图只显示连接与 RATE 硬件状态。
- `review.button-firmware-action`：请从固件确认短按/长按等条件分别如何触发清零、去皮与其他动作。；原因：原理图只确认低有效按键输入。
- `review.firmware-protocol`：请用发布固件和协议文档确认 v3/v4 固件、I2C v3 寄存器/数据格式及负重量表示。；原因：固件版本和协议语义不在原理图中。
- `review.mcu-architecture`：请用 STM32F030F4P6 对应 datasheet 确认 Cortex-M0 内核、频率与内部存储。；原因：原理图只打印型号，不含内部架构参数。
- `review.rgb-firmware`：请从固件确认 SK6812 数据时序、亮度限制和颜色/灯效与称重状态的映射。；原因：图纸只显示硬件连接。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `dd620fdfce59c1bdd237e48102542b799e95a26c76f4874a19be4daf7cda4b08` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/629/SCH_UNIT_MiniScales_V1.0_sch_01.png` |

---

源文档：`zh_CN/unit/Unit-Mini Scales.md`

源文档 SHA-256：`64747297d9c71456a207cefdf58ddfe3951013b6e753c18c6528e9b9c68663f3`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
