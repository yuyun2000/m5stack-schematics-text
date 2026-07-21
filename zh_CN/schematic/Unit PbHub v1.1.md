# Unit PbHub v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit PbHub v1.1 |
| SKU | U041-B |
| 产品 ID | `unit-pbhub-v1-1-b2aa06be0a47` |
| 源文档 | `zh_CN/unit/pbhub_1.1.md` |

## 概述

Unit PbHub v1.1 以 STM32F030F4P6（U2）通过 J7 接收 I2C SCL/SDA，并控制 J1~J6 六组 GROVE_IO 接口的 IN0~IN5 与 OUT0~OUT5。J7 输入的 +5V 直接供给六个输出口，并经 HT7533（U1）转换为 +3.3V 供 MCU、I2C 上拉和调试接口使用。板上提供五针 SWD 接口、BOOT0 下拉和 NRST RC；OUT5 与 PA13/SWDIO 共网，PF0/OSC_IN 与 PF1/OSC_OUT 则分别复用为 OUT3、OUT4。

## 检索关键词

`Unit PbHub v1.1`、`U041-B`、`PbHub`、`STM32F030F4P6`、`U2`、`HT7533`、`U1`、`GROVE_I2C`、`GROVE_IO`、`J1`、`J2`、`J3`、`J4`、`J5`、`J6`、`J7`、`P1`、`SWD_5p`、`SWCLK`、`SWDIO`、`NRST`、`BOOT0`、`SCL`、`SDA`、`IN0`、`IN1`、`IN2`、`IN3`、`IN4`、`IN5`、`OUT0`、`OUT1`、`OUT2`、`OUT3`、`OUT4`、`OUT5`、`+5V`、`+3.3V`、`0x61`、`PA13/SWDIO`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | STM32F030F4P6 | I2C 从设备主控，采集六路 IN0~IN5 并驱动六路 OUT0~OUT5，同时提供 SWD 调试 | 图 e25b0b50de83 / 第 1 页 / D1-D3：U2 标注 STM32F030F4P6，20 个引脚及 IN0~IN5、OUT0~OUT5、SCL/SDA、SWD、BOOT0、NRST 网络 |
| U1 | HT7533 | 将 +5V 转换为 +3.3V 的三端稳压器 | 图 e25b0b50de83 / 第 1 页 / B1-B2：U1 HT7533，VIN.2 接 +5V、VOUT.3 接 +3.3V、GND.1 接地 |
| J7 | GROVE_I2C | 上游 I2C、+5V 和 GND 输入接口 | 图 e25b0b50de83 / 第 1 页 / A1-B2：J7 GROVE_I2C 的 IIC_SCL、IIC_SDA、VCC、GND 四脚连接 |
| J1 | GROVE_IO | 通道 0 的 IN0、OUT0、+5V、GND 接口 | 图 e25b0b50de83 / 第 1 页 / A2-A3：J1 GROVE_IO，IN0/OUT0 网络接 1/2 脚，3/4 脚接 +5V/GND |
| J2 | GROVE_IO | 通道 1 的 IN1、OUT1、+5V、GND 接口 | 图 e25b0b50de83 / 第 1 页 / A3-A4：J2 GROVE_IO，IN1/OUT1 网络接 1/2 脚，3/4 脚接 +5V/GND |
| J3 | GROVE_IO | 通道 2 的 IN2、OUT2、+5V、GND 接口 | 图 e25b0b50de83 / 第 1 页 / B2-B3：J3 GROVE_IO，IN2/OUT2 网络接 1/2 脚，3/4 脚接 +5V/GND |
| J4 | GROVE_IO | 通道 3 的 IN3、OUT3、+5V、GND 接口 | 图 e25b0b50de83 / 第 1 页 / B3-B4：J4 GROVE_IO，IN3/OUT3 网络接 1/2 脚，3/4 脚接 +5V/GND |
| J5 | GROVE_IO | 通道 4 的 IN4、OUT4、+5V、GND 接口 | 图 e25b0b50de83 / 第 1 页 / B2-C3：J5 GROVE_IO，IN4/OUT4 网络接 1/2 脚，3/4 脚接 +5V/GND |
| J6 | GROVE_IO | 通道 5 的 IN5、OUT5、+5V、GND 接口 | 图 e25b0b50de83 / 第 1 页 / B3-C4：J6 GROVE_IO，IN5/OUT5 网络接 1/2 脚，3/4 脚接 +5V/GND |
| P1 | SWD_5p | MCU 的 +3.3V、SWCLK、SWDIO、NRST、GND 调试与下载接口 | 图 e25b0b50de83 / 第 1 页 / D3：P1 SWD_5p 的 VCC、SWCLK、SWDIO、RST、GND 五脚 |
| R5, R6 | 10KΩ | SCL 和 SDA 到 +3.3V 的 I2C 上拉电阻 | 图 e25b0b50de83 / 第 1 页 / A1-A2：R5/R6 均标注 10KΩ，分别从 +3.3V 接至 SCL/SDA |
| R1, C7 | 10KΩ / 100nF | NRST 的 +3.3V 上拉与对地电容复位网络 | 图 e25b0b50de83 / 第 1 页 / D1-D2：+3.3V-R1(10KΩ)-NRST 节点与 C7(100nF)-GND 支路 |
| R2 | 10KΩ | U2 BOOT0 到 GND 的下拉电阻 | 图 e25b0b50de83 / 第 1 页 / D1-D2：U2.1 BOOT0 经 R2 10KΩ 接 GND |
| C1, C2, C3, C4, C5, C6 | 100nF | J1~J6 的 +5V 到 GND 本地去耦电容 | 图 e25b0b50de83 / 第 1 页 / A3-C4：C1~C6 均标注 100nF，分别邻近 J1~J6 并跨接 +5V/GND |
| C8, C9, C11 | 100nF / 22uF / 22uF | HT7533 输出与输入电源去耦 | 图 e25b0b50de83 / 第 1 页 / B1-B2：C8 100nF、C9 22uF 接 +3.3V/GND，C11 22uF 接 +5V/GND |

## 系统结构

### Unit PbHub v1.1

U2 STM32F030F4P6 通过 J7 的 I2C SCL/SDA 与上游通信，并将六组 IN0~IN5、OUT0~OUT5 连接到 J1~J6。

- 参数与网络：`controller=U2 STM32F030F4P6`；`upstream=J7 GROVE_I2C`；`downstream=J1~J6 GROVE_IO`；`inputs=IN0~IN5`；`outputs=OUT0~OUT5`
- 证据：图 e25b0b50de83 / 第 1 页 / 全页：A1-B2 的 J7，A3-C4 的 J1~J6，D1-D3 的 U2 及同名网络

## 核心器件

### U2 STM32F030F4P6

U2 的 VDDA.5 与 VDD.16 接 +3.3V，VSS.15 接 GND。

- 参数与网络：`VDDA=pin 5 +3.3V`；`VDD=pin 16 +3.3V`；`VSS=pin 15 GND`
- 证据：图 e25b0b50de83 / 第 1 页 / D2-D3：U2.5 VDDA、U2.16 VDD 的 +3.3V 网络与 U2.15 VSS 的 GND 网络

## 电源

### +5V

J7.3 输入的 +5V 直接连接 U1.VIN.2，并分配到 J1~J6 的 VCC.3。

- 参数与网络：`source=J7.3 VCC`；`rail=+5V`；`regulator_input=U1.2 VIN`；`port_power=J1.3, J2.3, J3.3, J4.3, J5.3, J6.3`
- 证据：图 e25b0b50de83 / 第 1 页 / A1-C4：J7.3、U1.2 和 J1.3~J6.3 的 +5V 同名网络

### U1 HT7533

U1.VIN.2 接 +5V，U1.GND.1 接 GND，U1.VOUT.3 输出 +3.3V；C11（22uF）位于输入端，C8（100nF）和 C9（22uF）位于输出端。

- 参数与网络：`input=U1.2 VIN / +5V`；`ground=U1.1 GND`；`output=U1.3 VOUT / +3.3V`；`input_capacitor=C11 22uF`；`output_capacitors=C8 100nF, C9 22uF`
- 证据：图 e25b0b50de83 / 第 1 页 / B1-B2：U1 HT7533 的 VIN/VOUT/GND 与 C8/C9/C11、+5V/+3.3V/GND 完整连接

### J1~J6

J1~J6 的 +5V 电源分别由 C1~C6（每只 100nF）对地去耦。

- 参数与网络：`J1=C1 100nF`；`J2=C2 100nF`；`J3=C3 100nF`；`J4=C4 100nF`；`J5=C5 100nF`；`J6=C6 100nF`
- 证据：图 e25b0b50de83 / 第 1 页 / A3-C4：J1~J6 邻近的 C1~C6 100nF +5V-GND 支路

## 接口

### J7

J7.1 IIC_SCL 接 SCL，J7.2 IIC_SDA 接 SDA，J7.3 VCC 接 +5V，J7.4 GND 接地。

- 参数与网络：`connector=GROVE_I2C`；`pin_1=IIC_SCL / SCL`；`pin_2=IIC_SDA / SDA`；`pin_3=VCC / +5V`；`pin_4=GND`；`power_direction=+5V input to board`
- 证据：图 e25b0b50de83 / 第 1 页 / A1-B2：J7.1~J7.4 的 IIC_SCL、IIC_SDA、VCC、GND 标注及 SCL/SDA/+5V/GND 网络

### J1

J1.1（符号名 MISO）接 IN0，J1.2（符号名 IO）接 OUT0，J1.3 VCC 接 +5V，J1.4 GND 接地。

- 参数与网络：`channel=0`；`pin_1=IN0 / MISO`；`pin_2=OUT0 / IO`；`pin_3=+5V`；`pin_4=GND`
- 证据：图 e25b0b50de83 / 第 1 页 / A2-A3：J1.1~J1.4 的 IN0、OUT0、+5V、GND 连线及 MISO/IO/VCC/GND 符号名

### J2

J2.1（符号名 MISO）接 IN1，J2.2（符号名 IO）接 OUT1，J2.3 VCC 接 +5V，J2.4 GND 接地。

- 参数与网络：`channel=1`；`pin_1=IN1 / MISO`；`pin_2=OUT1 / IO`；`pin_3=+5V`；`pin_4=GND`
- 证据：图 e25b0b50de83 / 第 1 页 / A3-A4：J2.1~J2.4 的 IN1、OUT1、+5V、GND 连线及 MISO/IO/VCC/GND 符号名

### J3

J3.1（符号名 MISO）接 IN2，J3.2（符号名 IO）接 OUT2，J3.3 VCC 接 +5V，J3.4 GND 接地。

- 参数与网络：`channel=2`；`pin_1=IN2 / MISO`；`pin_2=OUT2 / IO`；`pin_3=+5V`；`pin_4=GND`
- 证据：图 e25b0b50de83 / 第 1 页 / B2-B3：J3.1~J3.4 的 IN2、OUT2、+5V、GND 连线及 MISO/IO/VCC/GND 符号名

### J4

J4.1（符号名 MISO）接 IN3，J4.2（符号名 IO）接 OUT3，J4.3 VCC 接 +5V，J4.4 GND 接地。

- 参数与网络：`channel=3`；`pin_1=IN3 / MISO`；`pin_2=OUT3 / IO`；`pin_3=+5V`；`pin_4=GND`
- 证据：图 e25b0b50de83 / 第 1 页 / B3-B4：J4.1~J4.4 的 IN3、OUT3、+5V、GND 连线及 MISO/IO/VCC/GND 符号名

### J5

J5.1（符号名 MISO）接 IN4，J5.2（符号名 IO）接 OUT4，J5.3 VCC 接 +5V，J5.4 GND 接地。

- 参数与网络：`channel=4`；`pin_1=IN4 / MISO`；`pin_2=OUT4 / IO`；`pin_3=+5V`；`pin_4=GND`
- 证据：图 e25b0b50de83 / 第 1 页 / B2-C3：J5.1~J5.4 的 IN4、OUT4、+5V、GND 连线及 MISO/IO/VCC/GND 符号名

### J6

J6.1（符号名 MISO）接 IN5，J6.2（符号名 IO）接 OUT5，J6.3 VCC 接 +5V，J6.4 GND 接地。

- 参数与网络：`channel=5`；`pin_1=IN5 / MISO`；`pin_2=OUT5 / IO`；`pin_3=+5V`；`pin_4=GND`
- 证据：图 e25b0b50de83 / 第 1 页 / B3-C4：J6.1~J6.4 的 IN5、OUT5、+5V、GND 连线及 MISO/IO/VCC/GND 符号名

## 总线

### J7 与 U2

J7 的 SCL 网络连接 U2.PA9.17，SDA 网络连接 U2.PA10.18。

- 参数与网络：`scl_net=SCL`；`scl_mcu_pin=U2.17 PA9`；`sda_net=SDA`；`sda_mcu_pin=U2.18 PA10`；`upstream_connector=J7`
- 证据：图 e25b0b50de83 / 第 1 页 / A1-A2 的 J7 SCL/SDA 与 D2-D3 的 U2.17 PA9/SCL、U2.18 PA10/SDA 同名网络

### SCL 与 SDA

SCL 经 R5（10KΩ）上拉至 +3.3V，SDA 经 R6（10KΩ）上拉至 +3.3V。

- 参数与网络：`SCL=R5 10KΩ to +3.3V`；`SDA=R6 10KΩ to +3.3V`；`logic_rail=+3.3V`
- 证据：图 e25b0b50de83 / 第 1 页 / A1-A2：+3.3V-R5-SCL 与 +3.3V-R6-SDA 两条上拉支路

## GPIO 与控制信号

### U2 IN0~IN5

IN0~IN5 分别连接 U2 的 PA0.6、PA1.7、PA2.8、PA3.9、PA4.10、PA5.11。

- 参数与网络：`IN0=PA0 pin 6`；`IN1=PA1 pin 7`；`IN2=PA2 pin 8`；`IN3=PA3 pin 9`；`IN4=PA4 pin 10`；`IN5=PA5 pin 11`
- 证据：图 e25b0b50de83 / 第 1 页 / D2：U2 左侧 PA0.6~PA5.11 与 IN0~IN5 网络标注

### U2 OUT0~OUT5

OUT0、OUT1、OUT2、OUT3、OUT4、OUT5 分别连接 U2 的 PA6.12、PA7.13、PB1.14、PF0/OSC_IN.2、PF1/OSC_OUT.3、PA13/SWDIO.19。

- 参数与网络：`OUT0=PA6 pin 12`；`OUT1=PA7 pin 13`；`OUT2=PB1 pin 14`；`OUT3=PF0/OSC_IN pin 2`；`OUT4=PF1/OSC_OUT pin 3`；`OUT5=PA13/SWDIO pin 19`
- 证据：图 e25b0b50de83 / 第 1 页 / D2-D3：U2 的 PA6.12/PA7.13/PB1.14、PF0.2/PF1.3、PA13.19 与 OUT0~OUT5 网络

### U2 BOOT0

U2.BOOT0.1 经 R2（10KΩ）下拉到 GND，原理图未将 BOOT0 引出到连接器。

- 参数与网络：`boot_pin=U2.1 BOOT0`；`pulldown=R2 10KΩ to GND`；`external_connector=none shown`
- 证据：图 e25b0b50de83 / 第 1 页 / D1-D2：GND-R2(10KΩ)-U2.1 BOOT0 支路及全部接口网络

## 时钟

### U2 PF0/OSC_IN 与 PF1/OSC_OUT

U2.PF0/OSC_IN.2 接 OUT3，U2.PF1/OSC_OUT.3 接 OUT4；本页未显示外部晶体、谐振器或有源时钟器件。

- 参数与网络：`PF0_OSC_IN=pin 2 / OUT3`；`PF1_OSC_OUT=pin 3 / OUT4`；`external_crystal=none shown`；`external_clock=none shown`
- 证据：图 e25b0b50de83 / 第 1 页 / D2：U2.2 PF0/OSC_IN 标注 OUT3、U2.3 PF1/OSC_OUT 标注 OUT4；全页无晶体或时钟源符号

## 复位

### U2 NRST

U2.NRST.4 由 R1（10KΩ）上拉至 +3.3V，并由 C7（100nF）连接到 GND；NRST 同时引到 P1.4。

- 参数与网络：`reset_pin=U2.4 NRST`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C7 100nF to GND`；`debug_pin=P1.4 RST`
- 证据：图 e25b0b50de83 / 第 1 页 / D1-D3：R1/C7 的 NRST RC 网络、U2.4 NRST 与 P1.4 RST

## 保护电路

### J1~J7

本页未显示 J1~J7 外部接口上的 TVS、保险丝、反接保护或串联限流器件。

- 参数与网络：`tvs=none shown`；`fuse=none shown`；`reverse_polarity=none shown`；`series_current_limit=none shown`
- 证据：图 e25b0b50de83 / 第 1 页 / 全页：J1~J7 的信号和电源完整连接中未出现离散保护器件位号或符号

## 内存与 Flash

### U2 存储连接

本页未显示与 U2 相连的外部 Flash、EEPROM、SD 卡或其他存储器件。

- 参数与网络：`external_flash=none shown`；`eeprom=none shown`；`sd_card=none shown`
- 证据：图 e25b0b50de83 / 第 1 页 / 全页：U2 的全部 20 脚均可见，外围仅连接电源、I2C、六路 IO、复位/启动与 SWD

## 调试与烧录

### OUT5 / SWDIO

OUT5 与 SWDIO 为同一网络，连接 U2.PA13.19，并同时接到 J6.2 和 P1.3。

- 参数与网络：`mcu_pin=U2.19 PA13`；`signal_aliases=OUT5, SWDIO`；`io_connector=J6.2`；`debug_connector=P1.3`
- 证据：图 e25b0b50de83 / 第 1 页 / D2-D3：U2.19 PA13 线上同时标注 SWDIO 与 OUT5；D3 P1.3 为 SWDIO；B3-C4 J6.2 为 OUT5

### P1

P1.1 VCC 接 +3.3V，P1.2 接 SWCLK，P1.3 接 SWDIO，P1.4 RST 接 NRST，P1.5 接 GND。

- 参数与网络：`connector=SWD_5p`；`pin_1=+3.3V`；`pin_2=SWCLK / U2.20 PA14`；`pin_3=SWDIO / U2.19 PA13 / OUT5`；`pin_4=NRST / U2.4`；`pin_5=GND`
- 证据：图 e25b0b50de83 / 第 1 页 / D3：P1 SWD_5p 的 1~5 脚及 +3.3V、SWCLK、SWDIO、NRST、GND 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit PbHub v1.1 | `controller=U2 STM32F030F4P6`；`upstream=J7 GROVE_I2C`；`downstream=J1~J6 GROVE_IO`；`inputs=IN0~IN5`；`outputs=OUT0~OUT5` |
| 核心器件 | U2 STM32F030F4P6 | `VDDA=pin 5 +3.3V`；`VDD=pin 16 +3.3V`；`VSS=pin 15 GND` |
| 接口 | J7 | `connector=GROVE_I2C`；`pin_1=IIC_SCL / SCL`；`pin_2=IIC_SDA / SDA`；`pin_3=VCC / +5V`；`pin_4=GND`；`power_direction=+5V input to board` |
| 总线 | J7 与 U2 | `scl_net=SCL`；`scl_mcu_pin=U2.17 PA9`；`sda_net=SDA`；`sda_mcu_pin=U2.18 PA10`；`upstream_connector=J7` |
| 总线 | SCL 与 SDA | `SCL=R5 10KΩ to +3.3V`；`SDA=R6 10KΩ to +3.3V`；`logic_rail=+3.3V` |
| 总线地址 | Unit PbHub v1.1 I2C 地址 | `documented_address=0x61`；`address_implementation=firmware/register; not shown in schematic`；`hardware_address_straps=none shown` |
| 接口 | J1 | `channel=0`；`pin_1=IN0 / MISO`；`pin_2=OUT0 / IO`；`pin_3=+5V`；`pin_4=GND` |
| 接口 | J2 | `channel=1`；`pin_1=IN1 / MISO`；`pin_2=OUT1 / IO`；`pin_3=+5V`；`pin_4=GND` |
| 接口 | J3 | `channel=2`；`pin_1=IN2 / MISO`；`pin_2=OUT2 / IO`；`pin_3=+5V`；`pin_4=GND` |
| 接口 | J4 | `channel=3`；`pin_1=IN3 / MISO`；`pin_2=OUT3 / IO`；`pin_3=+5V`；`pin_4=GND` |
| 接口 | J5 | `channel=4`；`pin_1=IN4 / MISO`；`pin_2=OUT4 / IO`；`pin_3=+5V`；`pin_4=GND` |
| 接口 | J6 | `channel=5`；`pin_1=IN5 / MISO`；`pin_2=OUT5 / IO`；`pin_3=+5V`；`pin_4=GND` |
| GPIO 与控制信号 | U2 IN0~IN5 | `IN0=PA0 pin 6`；`IN1=PA1 pin 7`；`IN2=PA2 pin 8`；`IN3=PA3 pin 9`；`IN4=PA4 pin 10`；`IN5=PA5 pin 11` |
| GPIO 与控制信号 | U2 OUT0~OUT5 | `OUT0=PA6 pin 12`；`OUT1=PA7 pin 13`；`OUT2=PB1 pin 14`；`OUT3=PF0/OSC_IN pin 2`；`OUT4=PF1/OSC_OUT pin 3`；`OUT5=PA13/SWDIO pin 19` |
| 调试与烧录 | OUT5 / SWDIO | `mcu_pin=U2.19 PA13`；`signal_aliases=OUT5, SWDIO`；`io_connector=J6.2`；`debug_connector=P1.3` |
| 调试与烧录 | P1 | `connector=SWD_5p`；`pin_1=+3.3V`；`pin_2=SWCLK / U2.20 PA14`；`pin_3=SWDIO / U2.19 PA13 / OUT5`；`pin_4=NRST / U2.4`；`pin_5=GND` |
| 复位 | U2 NRST | `reset_pin=U2.4 NRST`；`pullup=R1 10KΩ to +3.3V`；`capacitor=C7 100nF to GND`；`debug_pin=P1.4 RST` |
| GPIO 与控制信号 | U2 BOOT0 | `boot_pin=U2.1 BOOT0`；`pulldown=R2 10KΩ to GND`；`external_connector=none shown` |
| 时钟 | U2 PF0/OSC_IN 与 PF1/OSC_OUT | `PF0_OSC_IN=pin 2 / OUT3`；`PF1_OSC_OUT=pin 3 / OUT4`；`external_crystal=none shown`；`external_clock=none shown` |
| 电源 | +5V | `source=J7.3 VCC`；`rail=+5V`；`regulator_input=U1.2 VIN`；`port_power=J1.3, J2.3, J3.3, J4.3, J5.3, J6.3` |
| 电源 | U1 HT7533 | `input=U1.2 VIN / +5V`；`ground=U1.1 GND`；`output=U1.3 VOUT / +3.3V`；`input_capacitor=C11 22uF`；`output_capacitors=C8 100nF, C9 22uF` |
| 电源 | J1~J6 | `J1=C1 100nF`；`J2=C2 100nF`；`J3=C3 100nF`；`J4=C4 100nF`；`J5=C5 100nF`；`J6=C6 100nF` |
| 保护电路 | J1~J7 | `tvs=none shown`；`fuse=none shown`；`reverse_polarity=none shown`；`series_current_limit=none shown` |
| 内存与 Flash | U2 存储连接 | `external_flash=none shown`；`eeprom=none shown`；`sd_card=none shown` |

## 待确认事项

- `address.firmware-0x61-unconfirmed`：产品正文标注 I2C 地址为 0x61 且可通过写寄存器修改；原理图只显示 SCL/SDA 到 MCU，没有硬件地址绑带或地址数值，因此不能仅由本页确认该固件地址。（证据：图 e25b0b50de83 / 第 1 页 / A1-A2 与 D2-D3：J7 SCL/SDA 到 U2 PA9/PA10 的连接，未见地址脚、绑带或地址标注）
- `review.i2c-address-0x61`：该硬件随附固件的默认 7 位 I2C 地址是否为正文所列 0x61，且地址修改是否按所述寄存器机制实现？；原因：地址由 MCU 固件决定，原理图没有地址绑带、寄存器定义或固件版本信息，需以对应固件/协议文档或实板扫描复核。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `e25b0b50de830de93a3ede8af841a36be7c03c23dd4b8b051fc899392596672d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/579/SHC_UNIT_PBHUB_v1.1_sch_01.png` |

---

源文档：`zh_CN/unit/pbhub_1.1.md`

源文档 SHA-256：`62e7a0bfd906d2776e30e10c27348b9c1713422087d838e83ccd5394e9ad1b2e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
