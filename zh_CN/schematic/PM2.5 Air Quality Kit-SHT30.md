# PM2.5 Air Quality Kit-SHT30 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | PM2.5 Air Quality Kit-SHT30 |
| SKU | K023-B |
| 产品 ID | `pm2-5-air-quality-kit-sht30-f8c045ee6b54` |
| 源文档 | `zh_CN/app/PM2.5_Air_Quality_Kit-SHT30.md` |

## 概述

套件的 Module Air Quality 页面通过 30 Pin M5Stack_BUS 接入主机，并把 GPIO16/GPIO17 UART、GPIO21/GPIO22 I2C、GPIO23/GPIO19/GPIO18 SPI 和电源引到 PM2.5PORT 与 BUS_8P。该页还绘制了一个灰显的 U2 SHT20 I2C 支路，实际装配状态需要确认。Base BTC 页面以 U1 SHT30-DIS-B 连接 G21/G22，USB-C 的 VIN 经 F1 保险丝形成 +5V，并通过 P1 引出 +5V、+3.3V、GND 和五路 GPIO；SHT30 的 ADDR 接地，但页面未给出数值地址。

## 检索关键词

`PM2.5 Air Quality Kit-SHT30`、`K023-B`、`Module Air Quality`、`Base BTC`、`PMSA003`、`PM2.5PORT`、`SHT20`、`SHT30-DIS-B`、`M5Stack_BUS`、`BUS_8P`、`USB-C`、`UART`、`I2C`、`SPI`、`GPIO13`、`GPIO16`、`GPIO17`、`GPIO18`、`GPIO19`、`GPIO21`、`GPIO22`、`GPIO23`、`MRX`、`MTX`、`MSDA`、`MSCL`、`MMOSI`、`MMISO`、`MSCK`、`MRST`、`MSET`、`G21`、`G22`、`+5V`、`+3.3V`、`VIN`、`Rp1 5.1KΩ`、`R1/R2 4.7KΩ`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J3 (Module Air) | USB-C | Module Air Quality 的 5V 电源输入连接器，图中只使用 VBUS 与 GND | 图 995a138ac041 / 第 1 页 / 网格 1A：J3 USB-C，VBUS 接 +5V，GND 引脚接地 |
| J1 (Module Air) | BUS_8P | 引出 5V、3.3V、GND、I2C 与 SPI 信号的 8 Pin 扩展接口 | 图 995a138ac041 / 第 1 页 / 网格 1B：J1 BUS_8P，1~8 脚标注 5V/3V3/GND/SDA/SCL/MOSI/MISO/SCK |
| U2 (Module Air) | SHT20 | 原理图中灰显的 I2C 温湿度传感器位，绘制连接明确但装配状态待确认 | 图 995a138ac041 / 第 1 页 / 网格 1C~2C：灰显 U2 SHT20，MSDA/MSCL、+3V3、GND 与 C1/R1/R2 |
| U1 (Module Air) | PM2.5PORT | PM2.5 传感器 10 Pin 电源、UART、RESET 与 SET 接口 | 图 995a138ac041 / 第 1 页 / 网格 3A：U1 PM2.5PORT，1~10 脚的 VCC/GND/RESET/NC/RX/NC/TX/SET |
| J2 (Module Air) | M5Stack_BUS | 连接 M5Stack 主机的 30 Pin 堆叠总线 | 图 995a138ac041 / 第 1 页 / 网格 3C：J2 M5Stack_BUS，1~30 脚及 MRST/MMOSI/MMISO/MSCK/MRX/MTX/MSDA/MSCL/MSET/+3V3/+5V |
| R1/R2 (Module Air) | 4.7KΩ | MSDA 与 MSCL 到 +3V3 的 I2C 上拉电阻 | 图 995a138ac041 / 第 1 页 / 网格 1C~2C：R1 4.7KΩ 从 MSDA 到 +3V3，R2 4.7KΩ 从 MSCL 到 +3V3 |
| C1 (Module Air) | 100nF | SHT20 绘制电源支路的 +3V3 去耦电容 | 图 995a138ac041 / 第 1 页 / 网格 2C：C1 100nF 连接 +3V3 与 GND |
| J1 (Base BTC) | USB-C | Base BTC 的 VIN 电源输入与 CC1/CC2 配置连接器 | 图 a7b0c57b0c94 / 第 1 页 / 网格 1B：J1 USB-C，VBUS 引脚 2/5 接 VIN，CC1/CC2 为引脚 3/4，其他引脚接 GND |
| F1 (Base BTC) | Fuse | VIN 到 +5V 电源轨的串联保险丝 | 图 a7b0c57b0c94 / 第 1 页 / 网格 3B：VIN-F1 Fuse-+5V 串联路径 |
| Rp1 (Base BTC) | 5.1KΩ(512)±5% | USB-C CC 下拉与 G21/G22 I2C 上拉共用的四联电阻网络 | 图 a7b0c57b0c94 / 第 1 页 / 网格 2B：Rp1 四联 5.1KΩ，CC2/CC1 到 GND，G21/G22 到 +3.3V |
| P1 (Base BTC) | Header 8 | Base BTC 的电源与 G21/G22/G23/G19/G18 信号接口 | 图 a7b0c57b0c94 / 第 1 页 / 网格 4B：P1 Header 8，1~8 脚标注 +5V/+3.3V/GND/G21/G22/G23/G19/G18 |
| U1 (Base BTC) | SHT30-DIS-B | 3.3V I2C 温湿度传感器，SDA/SCL 接 G21/G22，ADDR 接地 | 图 a7b0c57b0c94 / 第 1 页 / 网格 1C~2C：U1 SHT30-DIS-B，VDD/VSS/ADDR/SDA/SCL/ALERT/nRESET/R/dpad 引脚 |
| C1 (Base BTC) | 100nF | SHT30 +3.3V 电源去耦电容 | 图 a7b0c57b0c94 / 第 1 页 / 网格 1C：C1 100nF 连接 +3.3V 与 GND |

## 系统结构

### PM2.5 Air Quality Kit-SHT30

资源包含 Module Air Quality 与 Base BTC 两张独立电路页：前者通过 M5Stack_BUS 连接 PM2.5PORT、BUS_8P 和 SHT20 绘制支路，后者包含 SHT30-DIS-B、USB-C 电源输入与 8 Pin Header。

- 参数与网络：`module_air_asset=K023-B-Sch_Air_page_01`；`base_btc_asset=A011-Sch_BTC_v2.1_page_01`；`module_bus=J2 M5Stack_BUS`；`base_sensor=U1 SHT30-DIS-B`
- 证据：图 995a138ac041 / 第 1 页 / Module Air Quality 全页：J1/J2/J3、U1/U2 与各总线网络; 图 a7b0c57b0c94 / 第 1 页 / Base BTC 全页：J1、F1、Rp1、P1、U1 与 C1

## 电源

### Module Air +5V 电源轨

Module Air 的 +5V 网络同时连接 J3 USB-C VBUS、J2 M5Stack_BUS 引脚 28、J1 BUS_8P 引脚 1，以及 U1 PM2.5PORT 的 VCC 引脚 1/2。

- 参数与网络：`rail=+5V`；`usb_c=J3 VBUS`；`m5_bus=J2 pin 28`；`bus_8p=J1 pin 1`；`pm25_port=U1 pins 1,2`
- 证据：图 995a138ac041 / 第 1 页 / J3 网格 1A、J1 网格 1B、U1 网格 3A、J2 网格 3C 的同名 +5V 网络

### Base BTC USB-C 到 +5V

Base BTC 的 J1 USB-C VBUS 引脚 2/5 连接 VIN，VIN 经 F1 Fuse 串联后形成 +5V，+5V 再连接 P1 引脚 1。

- 参数与网络：`input=J1 VBUS pins 2,5`；`intermediate=VIN`；`protection=F1 Fuse`；`output=+5V`；`header=P1 pin 1`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 1B J1 VBUS/VIN、网格 3B F1 VIN-+5V、网格 4B P1 pin 1

### Base BTC +3.3V 电源域

+3.3V 连接 P1 引脚 2、U1 SHT30-DIS-B 的 VDD 引脚 5、C1 100nF，以及 Rp1 中 G21/G22 两路 5.1KΩ 上拉电阻。

- 参数与网络：`rail=+3.3V`；`header=P1 pin 2`；`sensor=U1 pin 5 VDD`；`decoupling=C1 100nF`；`pullups=Rp1 pins 6 and 5`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 4B P1、网格 2B Rp1、网格 1C C1 与网格 2C U1 的 +3.3V 网络

## 接口

### Module Air J3 USB-C

J3 图中只连接 VBUS 与 GND：VBUS 接 +5V，左侧 11~14 脚和右侧 GND 引脚接地，页面未绘制数据线或 CC 网络。

- 参数与网络：`reference=J3`；`vbus=+5V`；`ground_pins=GND and pins 11-14`；`data_lines=not drawn`；`cc_lines=not drawn`
- 证据：图 995a138ac041 / 第 1 页 / 网格 1A：J3 USB-C 的全部可见引脚与 +5V/GND 网络

### Module Air J1 BUS_8P

J1 的 1~8 脚依次为 +5V、+3V3、GND、MSDA、MSCL、MMOSI、MMISO、MSCK，对应符号内的 5V、3V3、GND、SDA、SCL、MOSI、MISO、SCK。

- 参数与网络：`pin_1=+5V`；`pin_2=+3V3`；`pin_3=GND`；`pin_4=MSDA`；`pin_5=MSCL`；`pin_6=MMOSI`；`pin_7=MMISO`；`pin_8=MSCK`
- 证据：图 995a138ac041 / 第 1 页 / 网格 1B：J1 BUS_8P 引脚 1~8 与左侧同名网络

### Module Air U1 PM2.5PORT

U1 的 1/2 脚 VCC 接 +5V，3/4 脚 GND 接地，5 脚 RESET 接 MRST，6/8 脚标为 NC，7 脚 RX 接 MTX，9 脚 TX 接 MRX，10 脚 SET 接 MSET。

- 参数与网络：`pins_1_2=VCC +5V`；`pins_3_4=GND`；`pin_5=RESET MRST`；`pins_6_8=NC`；`pin_7=RX MTX`；`pin_9=TX MRX`；`pin_10=SET MSET`
- 证据：图 995a138ac041 / 第 1 页 / 网格 3A：U1 PM2.5PORT 引脚 1~10 与左侧网络

### Module Air J2 M5Stack_BUS 已用信号

J2 已连接的信号包括 GPIO23/MMOSI、GPIO19/MMISO、GPIO18/MSCK、GPIO16/MRX、GPIO17/MTX、GPIO21/MSDA、GPIO22/MSCL、GPIO13/MSET、EN/MRST、+3V3、+5V 与 GND。

- 参数与网络：`pin_6=EN MRST`；`pin_7=GPIO23 MMOSI`；`pin_9=GPIO19 MMISO`；`pin_11=GPIO18 MSCK`；`pin_12=+3V3`；`pin_15=GPIO16 MRX`；`pin_16=GPIO17 MTX`；`pin_17=GPIO21 MSDA`；`pin_18=GPIO22 MSCL`；`pin_22=GPIO13 MSET`；`pin_28=+5V`；`ground_pins=1,3,5`
- 证据：图 995a138ac041 / 第 1 页 / 网格 3C：J2 M5Stack_BUS 的 1~30 脚及所有外接网络

### Base BTC P1 Header 8

P1 的 1~8 脚依次引出 +5V、+3.3V、GND、G21、G22、G23、G19、G18。

- 参数与网络：`pin_1=+5V`；`pin_2=+3.3V`；`pin_3=GND`；`pin_4=G21`；`pin_5=G22`；`pin_6=G23`；`pin_7=G19`；`pin_8=G18`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 4B：P1 Header 8 的 1~8 脚与左侧网络标签

## 总线

### PM2.5PORT UART 到 M5Stack_BUS

PM2.5PORT 的 RX 引脚 7 经 MTX 连接 J2 引脚 16 GPIO17，TX 引脚 9 经 MRX 连接 J2 引脚 15 GPIO16。

- 参数与网络：`sensor_rx=U1 pin 7 RX-MTX-J2 pin 16 GPIO17`；`sensor_tx=U1 pin 9 TX-MRX-J2 pin 15 GPIO16`；`host_tx_gpio=GPIO17`；`host_rx_gpio=GPIO16`
- 证据：图 995a138ac041 / 第 1 页 / 网格 3A U1 的 MTX/MRX 与网格 3C J2 GPIO17/GPIO16 的同名网络

### Module Air SPI 引出

J2 GPIO23/GPIO19/GPIO18 分别通过 MMOSI/MMISO/MSCK 连接 J1 BUS_8P 的 MOSI/MISO/SCK 引脚 6/7/8。

- 参数与网络：`mosi=J2 pin 7 GPIO23-MMOSI-J1 pin 6`；`miso=J2 pin 9 GPIO19-MMISO-J1 pin 7`；`sck=J2 pin 11 GPIO18-MSCK-J1 pin 8`
- 证据：图 995a138ac041 / 第 1 页 / 网格 1B J1 MMOSI/MMISO/MSCK 与网格 3C J2 GPIO23/GPIO19/GPIO18

### Module Air SHT20 绘制 I2C 支路

图中 U2 引脚 1 接 MSDA、引脚 6 接 MSCL，MSDA/MSCL 分别通过 R1/R2 4.7KΩ 上拉到 +3V3；MSDA/MSCL 同时到 J1 引脚 4/5 和 J2 GPIO21/GPIO22。

- 参数与网络：`sda=U2 pin 1-MSDA-J1 pin 4-J2 pin 17 GPIO21`；`scl=U2 pin 6-MSCL-J1 pin 5-J2 pin 18 GPIO22`；`sda_pullup=R1 4.7KΩ to +3V3`；`scl_pullup=R2 4.7KΩ to +3V3`；`decoupling=C1 100nF`
- 证据：图 995a138ac041 / 第 1 页 / 网格 1C~2C U2/R1/R2/C1、网格 1B J1、网格 3C J2 的 MSDA/MSCL 网络

### Base BTC SHT30 I2C

U1 SDA 引脚 1 通过 G21 连接 P1 引脚 4，并经 Rp1 pins 3-6 的 5.1KΩ 电阻上拉到 +3.3V；SCL 引脚 4 通过 G22 连接 P1 引脚 5，并经 Rp1 pins 4-5 的 5.1KΩ 电阻上拉到 +3.3V。

- 参数与网络：`sda=U1 pin 1-G21-P1 pin 4`；`scl=U1 pin 4-G22-P1 pin 5`；`sda_pullup=Rp1 pins 3-6 5.1KΩ to +3.3V`；`scl_pullup=Rp1 pins 4-5 5.1KΩ to +3.3V`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 2C U1 SDA/SCL、网格 2B Rp1 G21/G22 上拉、网格 4B P1 pins 4/5

## 复位

### PM2.5PORT RESET 与 SET

PM2.5PORT 引脚 5 RESET 通过 MRST 连接 J2 引脚 6 EN；引脚 10 SET 通过 MSET 连接 J2 引脚 22 GPIO13。

- 参数与网络：`reset=U1 pin 5 RESET-MRST-J2 pin 6 EN`；`set=U1 pin 10 SET-MSET-J2 pin 22 GPIO13`
- 证据：图 995a138ac041 / 第 1 页 / 网格 3A U1 RESET/SET 与网格 3C J2 EN/GPIO13 的 MRST/MSET 网络

## 保护电路

### Base BTC USB-C CC1/CC2

J1 引脚 3 CC1 经 Rp1 的 7-2 电阻接 GND，J1 引脚 4 CC2 经 Rp1 的 8-1 电阻接 GND；Rp1 标值为 5.1KΩ(512)±5%。

- 参数与网络：`cc1=J1 pin 3-Rp1 pins 7-2-GND`；`cc2=J1 pin 4-Rp1 pins 8-1-GND`；`resistance=5.1KΩ`；`tolerance=±5%`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 1B J1 CC1/CC2 与网格 2B Rp1 pins 7/8 到 pins 2/1/GND

## 传感器

### Base BTC U1 SHT30-DIS-B

U1 的 VDD 引脚 5 接 +3.3V，VSS 引脚 8、R 引脚 7、dpad 引脚 9 与 ADDR 引脚 2 接 GND，SDA 引脚 1 接 G21，SCL 引脚 4 接 G22；ALERT 引脚 3 与 nRESET 引脚 6 在图中没有外接网络。

- 参数与网络：`vdd=pin 5 +3.3V`；`vss=pin 8 GND`；`reserved=pin 7 R to GND`；`dpad=pin 9 GND`；`addr=pin 2 GND`；`sda=pin 1 G21`；`scl=pin 4 G22`；`alert=pin 3 no external net`；`nreset=pin 6 no external net`
- 证据：图 a7b0c57b0c94 / 第 1 页 / 网格 1C~2C：U1 SHT30-DIS-B 全部引脚及 GND/+3.3V/G21/G22 连接

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | PM2.5 Air Quality Kit-SHT30 | `module_air_asset=K023-B-Sch_Air_page_01`；`base_btc_asset=A011-Sch_BTC_v2.1_page_01`；`module_bus=J2 M5Stack_BUS`；`base_sensor=U1 SHT30-DIS-B` |
| 电源 | Module Air +5V 电源轨 | `rail=+5V`；`usb_c=J3 VBUS`；`m5_bus=J2 pin 28`；`bus_8p=J1 pin 1`；`pm25_port=U1 pins 1,2` |
| 接口 | Module Air J3 USB-C | `reference=J3`；`vbus=+5V`；`ground_pins=GND and pins 11-14`；`data_lines=not drawn`；`cc_lines=not drawn` |
| 接口 | Module Air J1 BUS_8P | `pin_1=+5V`；`pin_2=+3V3`；`pin_3=GND`；`pin_4=MSDA`；`pin_5=MSCL`；`pin_6=MMOSI`；`pin_7=MMISO`；`pin_8=MSCK` |
| 接口 | Module Air U1 PM2.5PORT | `pins_1_2=VCC +5V`；`pins_3_4=GND`；`pin_5=RESET MRST`；`pins_6_8=NC`；`pin_7=RX MTX`；`pin_9=TX MRX`；`pin_10=SET MSET` |
| 总线 | PM2.5PORT UART 到 M5Stack_BUS | `sensor_rx=U1 pin 7 RX-MTX-J2 pin 16 GPIO17`；`sensor_tx=U1 pin 9 TX-MRX-J2 pin 15 GPIO16`；`host_tx_gpio=GPIO17`；`host_rx_gpio=GPIO16` |
| 复位 | PM2.5PORT RESET 与 SET | `reset=U1 pin 5 RESET-MRST-J2 pin 6 EN`；`set=U1 pin 10 SET-MSET-J2 pin 22 GPIO13` |
| 接口 | Module Air J2 M5Stack_BUS 已用信号 | `pin_6=EN MRST`；`pin_7=GPIO23 MMOSI`；`pin_9=GPIO19 MMISO`；`pin_11=GPIO18 MSCK`；`pin_12=+3V3`；`pin_15=GPIO16 MRX`；`pin_16=GPIO17 MTX`；`pin_17=GPIO21 MSDA`；`pin_18=GPIO22 MSCL`；`pin_22=GPIO13 MSET`；`pin_28=+5V`；`ground_pins=1,3,5` |
| 总线 | Module Air SPI 引出 | `mosi=J2 pin 7 GPIO23-MMOSI-J1 pin 6`；`miso=J2 pin 9 GPIO19-MMISO-J1 pin 7`；`sck=J2 pin 11 GPIO18-MSCK-J1 pin 8` |
| 总线 | Module Air SHT20 绘制 I2C 支路 | `sda=U2 pin 1-MSDA-J1 pin 4-J2 pin 17 GPIO21`；`scl=U2 pin 6-MSCL-J1 pin 5-J2 pin 18 GPIO22`；`sda_pullup=R1 4.7KΩ to +3V3`；`scl_pullup=R2 4.7KΩ to +3V3`；`decoupling=C1 100nF` |
| 传感器 | Module Air U2 SHT20 装配状态 | `reference=U2`；`part_number=SHT20`；`rendering=greyed`；`explicit_dnp=false`；`population=null` |
| 电源 | Base BTC USB-C 到 +5V | `input=J1 VBUS pins 2,5`；`intermediate=VIN`；`protection=F1 Fuse`；`output=+5V`；`header=P1 pin 1` |
| 保护电路 | Base BTC USB-C CC1/CC2 | `cc1=J1 pin 3-Rp1 pins 7-2-GND`；`cc2=J1 pin 4-Rp1 pins 8-1-GND`；`resistance=5.1KΩ`；`tolerance=±5%` |
| 接口 | Base BTC P1 Header 8 | `pin_1=+5V`；`pin_2=+3.3V`；`pin_3=GND`；`pin_4=G21`；`pin_5=G22`；`pin_6=G23`；`pin_7=G19`；`pin_8=G18` |
| 电源 | Base BTC +3.3V 电源域 | `rail=+3.3V`；`header=P1 pin 2`；`sensor=U1 pin 5 VDD`；`decoupling=C1 100nF`；`pullups=Rp1 pins 6 and 5` |
| 传感器 | Base BTC U1 SHT30-DIS-B | `vdd=pin 5 +3.3V`；`vss=pin 8 GND`；`reserved=pin 7 R to GND`；`dpad=pin 9 GND`；`addr=pin 2 GND`；`sda=pin 1 G21`；`scl=pin 4 G22`；`alert=pin 3 no external net`；`nreset=pin 6 no external net` |
| 总线 | Base BTC SHT30 I2C | `sda=U1 pin 1-G21-P1 pin 4`；`scl=U1 pin 4-G22-P1 pin 5`；`sda_pullup=Rp1 pins 3-6 5.1KΩ to +3.3V`；`scl_pullup=Rp1 pins 4-5 5.1KΩ to +3.3V` |
| 总线地址 | Base BTC SHT30 I2C 地址 | `device=U1 SHT30-DIS-B`；`address_pin=pin 2 ADDR`；`strap=GND`；`schematic_address_label=null` |

## 待确认事项

- `sensor.air-sht20-population`：U2 SHT20 的符号、位号、型号与引脚在原理图中呈灰色，页面没有明确的 DNP 或装配说明，无法仅凭此页确认 U2 是否实装。（证据：图 995a138ac041 / 第 1 页 / 网格 1C~2C：U2 SHT20 整个器件符号灰显，但邻近 R1/R2/C1 为正常颜色且无 DNP 文本）
- `address.btc-sht30`：原理图明确将 U1 SHT30-DIS-B 的 ADDR 引脚 2 接地，但页面未标注由该绑定位对应的数值 I2C 地址，需要依据 SHT30 datasheet 或软件配置确认。（证据：图 a7b0c57b0c94 / 第 1 页 / 网格 1C~2C：U1 pin 2 ADDR 接 GND，整页无十六进制地址标注）
- `review.air-sht20-population`：请用 Module Air Quality K023-B 的 BOM、装配图或实物确认灰显 U2 SHT20 是否实装。；原因：原理图绘制了完整 SHT20 支路，但 U2 灰显且没有明确 DNP 文本，颜色本身不足以判定装配状态。
- `review.btc-sht30-address`：请依据 SHT30 官方 datasheet 或产品软件确认 ADDR 接地时使用的数值 I2C 地址。；原因：页面只显示 ADDR 接地，没有打印 I2C 地址值，不能只凭原理图确定十六进制地址。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `995a138ac0416a3f76de5844147d6a77be96d56ee9a5db4ee8f4dbdf8d021c2d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1067/K023-B-Sch_Air_page_01.png` |
| 2 | 1 | `a7b0c57b0c9411ae8a60e8f0b359b1f784805d2e1ceef453ea9729bb7f968b24` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1000/A011-Sch_BTC_v2.1_page_01.png` |

---

源文档：`zh_CN/app/PM2.5_Air_Quality_Kit-SHT30.md`

源文档 SHA-256：`49677df42d8d2bfc33f3049993bdc176e2e1372a2703b965b288f390a00e8086`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
