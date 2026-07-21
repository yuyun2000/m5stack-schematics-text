# Unit LoRaWAN-AS923 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit LoRaWAN-AS923 |
| SKU | U184-AS923 |
| 产品 ID | `unit-lorawan-as923-0a82795306a4` |
| 源文档 | `zh_CN/unit/Unit LoRaWAN-AS923.md` |

## 概述

Unit LoRaWAN-AS923 原理图以 M1 RAK3172 无线模组为核心，通过 U2_RX/U2_TX UART 与 J1 HY-2.0_UART 主机接口通信，并引出 SWD、RST、BOOT、辅助 UART、I2C 与 SPI 测试点。J1 的 VCC 经 F1 形成 +5V，U1 VRH3301NLX 再生成 +3.3V，为 RAK3172、复位网络和 UART 上拉供电。RF pin12 连接一组全部标 NC 的 E1/R8/C8/C9 射频支路，页面另列 R1-R4 对应 470/868/915/923 的装配表，但没有直接证明本件 AS923 的 R4 实装状态或正文所述射频、协议与性能参数。

## 检索关键词

`Unit LoRaWAN-AS923`、`U184-AS923`、`RAK3172`、`STM32WLE5`、`VRH3301NLX`、`HY-2.0_UART`、`AS923`、`923-925MHz`、`LoRaWAN 1.0.3`、`LoRa P2P`、`Class A`、`Class B`、`Class C`、`OTAA`、`ABP`、`AT command`、`UART 115200`、`U2_RX`、`U2_TX`、`U1_RX`、`U1_TX`、`SWDIO`、`SWCLK`、`RST`、`BOOT`、`SCL`、`SDA`、`MOSI`、`MISO`、`SCK`、`NSS`、`ANT`、`RF`、`+5V`、`+3.3V`、`F1 6V@1A`、`R4 0Ω 923`、`RLSD52A031V`、`LESD3Z5.0CMT1G`、`SMA antenna`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | RAK3172 | LoRa 无线通信模组，提供双 UART、SWD、I2C、SPI、RF、RST、BOOT、ADC/GPIO 与 3.3V 电源端 | 图 6def63d71dca / 第 1 页 / 第1页中央 M1 RAK3172 pins1-32 |
| U1 | VRH3301NLX | 将 +5V 稳压为 +3.3V 的五脚稳压器 | 图 6def63d71dca / 第 1 页 / 第1页左上 U1 VRH3301NLX pins1-5、+5V、+3.3V |
| J1 | HY-2.0_UART | 四针 Grove UART 和 5V 供电接口 | 图 6def63d71dca / 第 1 页 / 第1页右中 J1 HY-2.0_UART pins1-4 |
| E1/R8/C8/C9 | NC / NC / NC / NC | RAK3172 RF 到 ANT 的可选天线与 π 型匹配位置，页面全部标 NC | 图 6def63d71dca / 第 1 页 / 第1页中左 M1 RF pin12、C9 NC、R8 NC、C8 NC、ANT、E1 NC |
| F1 | 6V@1A | 串接 J1 VCC 与板上 +5V 的保险/限流器件 | 图 6def63d71dca / 第 1 页 / 第1页右中 F1 6V@1A、+5V、VCC 与 J1 pin3 |
| R9/R10 | 22Ω / 22Ω | U2_TX/U2_RX 与 Grove RX/TX 之间的 UART 串联电阻 | 图 6def63d71dca / 第 1 页 / 第1页右中 U2_TX/R9/RX 与 U2_RX/R10/TX |
| D2/R6/R7 | 1N4148WS T4 / 10KΩ / 10KΩ | 从 +3.3V 经二极管向 RX/TX 分别提供 10KΩ 上拉的 UART 偏置网络 | 图 6def63d71dca / 第 1 页 / 第1页右中 +3.3V、D2 1N4148WS T4、R6/R7 10KΩ、RX/TX |
| D1/D3/D4/D5 | RLSD52A031V / LESD3Z5.0CMT1G / RLSD52A031V / RLSD52A031V | +3.3V、VCC、RX 与 TX 的对地 ESD/瞬态保护 | 图 6def63d71dca / 第 1 页 / 第1页左上 D1；右中 D3/D4/D5 与 +3.3V/VCC/RX/TX |
| R5/C4 | 10KΩ / 1uF | M1 RST 的 +3.3V 上拉和对地 RC 网络 | 图 6def63d71dca / 第 1 页 / 第1页左中 R5 10KΩ、C4 1uF、RST |
| R1/R2/R3/R4 | 0Ω | 470/868/915/923 版本对应关系的装配选项电阻表 | 图 6def63d71dca / 第 1 页 / 第1页右上装配表：R1 470、R2 868、R3 915、R4 923，均标 0Ω |
| C1/C2/C3 | 22uF / 1uF / 1uF | U1 输入 +5V 与输出 +3.3V 的去耦/储能电容 | 图 6def63d71dca / 第 1 页 / 第1页左上 U1 周围 C1 22uF、C2 1uF、C3 1uF |
| C5/C6/C7 | 100nF / 22uF / 33pF | M1 VDD +3.3V 的对地去耦网络 | 图 6def63d71dca / 第 1 页 / 第1页中央偏右 M1 VDD pin24 与 C5/C6/C7 |
| JP1-JP14 | 未标注 | 引出电源、SWD、RST、BOOT、I2C、辅助 UART 与 SPI 的测试点组 | 图 6def63d71dca / 第 1 页 / 第1页左下 JP1-JP14 及 +3.3V/SWCLK/SWDIO/RST/GND/BOOT/SCL/SDA/U1_RX/U1_TX/MOSI/MISO/SCK/NSS |

## 系统结构

### Unit LoRaWAN-AS923 系统架构

单页电路由 M1 RAK3172、U1 3.3V 稳压器、J1 Grove UART、可选 RF/天线支路、复位/BOOT/SWD 和辅助串行总线测试点组成。

- 参数与网络：`radio_module=M1 RAK3172`；`power=U1 VRH3301NLX`；`host=J1 HY-2.0_UART`；`rf=M1 RF -> C9/R8/C8/E1, all NC`；`debug=JP1-JP14`
- 证据：图 6def63d71dca / 第 1 页 / 第1页完整单页各功能分区

## 核心器件

### RAK3172 模组边界

M1 明确标为 RAK3172，符号列出 32 脚，并引出 U2/U1 两组 UART、SWDIO/SWCLK、SCL/SDA、RF、MOSI/MISO/SCK/NSS、RST、BOOT、ADC 与 GPIO。

- 参数与网络：`reference=M1`；`part_number=RAK3172`；`pins=32`；`uart=U2_RX/U2_TX; U1_TX/U1_RX`；`debug=SWDIO/SWCLK`；`rf_pin=pin12 RF`；`reset_pin=pin22 RST`；`boot_pin=pin21 BOOT`
- 证据：图 6def63d71dca / 第 1 页 / 第1页中央 M1 RAK3172 全部引脚标签

## 电源

### +5V 到 +3.3V 稳压

U1 VRH3301NLX 的 VIN pin4 与 EN pin3 接 +5V，VOUT pin1 输出 +3.3V，VSS pins2/5 接 GND；C1 22uF/C2 1uF 位于输入，C3 1uF 位于输出。

- 参数与网络：`regulator=U1 VRH3301NLX`；`vin=pin4 / +5V`；`enable=pin3 / +5V`；`vout=pin1 / +3.3V`；`ground=pins2,5`；`input_caps=C1 22uF; C2 1uF`；`output_cap=C3 1uF`
- 证据：图 6def63d71dca / 第 1 页 / 第1页左上 U1/C1/C2/C3/+5V/+3.3V

### Grove 5V 输入路径

J1 pin3 VCC 经 F1 6V@1A 串联后形成板上 +5V；C10 100nF 从 VCC 对地，D3 LESD3Z5.0CMT1G 从 VCC 对地。

- 参数与网络：`connector=J1 pin3 VCC`；`series=F1 6V@1A`；`internal_rail=+5V`；`interface_cap=C10 100nF`；`protection=D3 LESD3Z5.0CMT1G to GND`
- 证据：图 6def63d71dca / 第 1 页 / 第1页右中 J1 pin3/VCC/F1/+5V/C10/D3

### RAK3172 VDD 去耦

M1 VDD pin24 接 +3.3V，C5 100nF、C6 22uF 和 C7 33pF 从同一电源节点对地；M1 多个 GND 脚接地。

- 参数与网络：`module_pin=M1 pin24 VDD`；`rail=+3.3V`；`decoupling=C5 100nF; C6 22uF; C7 33pF`；`grounds=M1 pins11,17,18,23,28`
- 证据：图 6def63d71dca / 第 1 页 / 第1页中央 M1 VDD/GND 与右侧 C5/C6/C7

## 接口

### J1 Grove UART 针脚

J1 HY-2.0_UART pin1 标 RX、pin2 标 TX、pin3 为 VCC、pin4 为 GND；RX 来自 M1 U2_TX，TX 送往 M1 U2_RX。

- 参数与网络：`connector=J1 HY-2.0_UART`；`pin1=RX <- U2_TX`；`pin2=TX -> U2_RX`；`pin3=VCC / 5V input`；`pin4=GND`；`logic_rail=+3.3V`
- 证据：图 6def63d71dca / 第 1 页 / 第1页右中 J1 pins1-4 与 RX/TX/VCC/GND

## 总线

### M1 U2 UART 主机路由

M1 pin2 U2_TX 经 R9 22Ω 到 J1 RX pin1；J1 TX pin2 经 R10 22Ω 到 M1 pin1 U2_RX。

- 参数与网络：`module_tx=M1 pin2 U2_TX -> R9 22Ω -> J1 pin1 RX`；`module_rx=J1 pin2 TX -> R10 22Ω -> M1 pin1 U2_RX`；`series_resistors=R9/R10 22Ω`；`direction=module-to-host TX; host-to-module RX`
- 证据：图 6def63d71dca / 第 1 页 / 第1页中央 M1 pins1/2 与右中 R9/R10/J1 RX/TX

### I2C 测试点

M1 pin9 SCL 和 pin10 SDA 分别引到 JP7 与 JP10；页面未显示外部 I2C 设备、地址或 SCL/SDA 上拉电阻。

- 参数与网络：`controller_scl=M1 pin9 SCL -> JP7`；`controller_sda=M1 pin10 SDA -> JP10`；`devices=not shown`；`address=not shown`；`pullups=not shown`
- 证据：图 6def63d71dca / 第 1 页 / 第1页中央 M1 SCL/SDA 与左下 JP7/JP10

### SPI 测试点

M1 pin13 MOSI、pin14 MISO、pin15 SCK、pin16 NSS 分别引到 JP9、JP12、JP13、JP14；页面未显示外部 SPI 设备。

- 参数与网络：`mosi=M1 pin13 -> JP9`；`miso=M1 pin14 -> JP12`；`clock=M1 pin15 -> JP13`；`chip_select=M1 pin16 NSS -> JP14`；`device=not shown`
- 证据：图 6def63d71dca / 第 1 页 / 第1页中央 M1 MOSI/MISO/SCK/NSS 与左下 JP9/JP12/JP13/JP14

## GPIO 与控制信号

### BOOT 网络

M1 BOOT pin21 连接 BOOT 网络和 JP6，并在模组右侧通过图中标注 0Ω 的支路接 GND。

- 参数与网络：`module_pin=M1 pin21 BOOT`；`testpoint=JP6`；`strap=0Ω to GND`；`default_level=low`
- 证据：图 6def63d71dca / 第 1 页 / 第1页中央 M1 BOOT pin21 右侧 0Ω/GND 与左下 JP6

## 时钟

### 外部时钟

该单页没有画 M1 外部晶振、振荡器或时钟输入网络；RAK3172 内部时钟电路未展开。

- 参数与网络：`external_crystal=not shown`；`oscillator=not shown`；`clock_net=not shown`；`module_internal_clock=not expanded`
- 证据：图 6def63d71dca / 第 1 页 / 第1页完整单页与 M1 模组边界

## 复位

### M1 复位网络

M1 RST pin22 接 RST 网络，R5 10KΩ 上拉到 +3.3V，C4 1uF 对地，并通过 JP4 引出。

- 参数与网络：`module_pin=M1 pin22 RST`；`pullup=R5 10KΩ to +3.3V`；`capacitor=C4 1uF to GND`；`testpoint=JP4`
- 证据：图 6def63d71dca / 第 1 页 / 第1页左中 R5/C4/RST、中央 M1 pin22、左下 JP4

## 保护电路

### +3.3V 保护

D1 RLSD52A031V 从 +3.3V 对地，位于 U1 输出电源域。

- 参数与网络：`device=D1 RLSD52A031V`；`protected_net=+3.3V`；`return=GND`
- 证据：图 6def63d71dca / 第 1 页 / 第1页左上 +3.3V 与 D1 RLSD52A031V

### Grove 电源与 UART 保护

D3 LESD3Z5.0CMT1G 保护 VCC，D4/D5 RLSD52A031V 分别从 RX/TX 对地，F1 串联在 VCC 与 +5V 之间。

- 参数与网络：`vcc=D3 LESD3Z5.0CMT1G to GND`；`rx=D4 RLSD52A031V to GND`；`tx=D5 RLSD52A031V to GND`；`fuse=F1 6V@1A`
- 证据：图 6def63d71dca / 第 1 页 / 第1页右中 F1/D3/D4/D5/VCC/RX/TX

## 关键网络

### RX/TX 上拉偏置

+3.3V 经 D2 1N4148WS T4 到公共节点，再分别经 R6/R7 10KΩ 接 RX/TX。

- 参数与网络：`source=+3.3V`；`diode=D2 1N4148WS T4`；`rx_pull=R6 10KΩ`；`tx_pull=R7 10KΩ`；`nets=RX; TX`
- 证据：图 6def63d71dca / 第 1 页 / 第1页右中 D2/R6/R7 与 RX/TX

## 存储

### 外部存储器

该单页未显示独立 Flash、RAM、EEPROM、SD 卡或其他外部存储器位号；RAK3172 内部存储未展开。

- 参数与网络：`external_flash=not shown`；`external_ram=not shown`；`eeprom=not shown`；`sd=not shown`；`module=M1 RAK3172`
- 证据：图 6def63d71dca / 第 1 页 / 第1页完整单页器件与 M1 模组边界

## 射频

### RF 与天线可选支路

M1 RF pin12 经 C9 对地位置、R8 串联位置、C8 对地位置到 ANT/E1；E1、R8、C8、C9 均在页面标 NC，因此该页不能证明这些位号已装配。

- 参数与网络：`module_pin=M1 pin12 RF`；`series=R8 NC`；`module_side_shunt=C9 NC`；`antenna_side_shunt=C8 NC`；`antenna_reference=E1 NC`；`net=ANT`
- 证据：图 6def63d71dca / 第 1 页 / 第1页中左 M1 RF/R8/C8/C9/ANT/E1，全部 NC 标记

### 470/868/915/923 版本表

页面右上表将 R1 0Ω 对应 470、R2 0Ω 对应 868、R3 0Ω 对应 915、R4 0Ω 对应 923。

- 参数与网络：`R1=0Ω -> 470`；`R2=0Ω -> 868`；`R3=0Ω -> 915`；`R4=0Ω -> 923`；`selection_location=not shown in circuit`
- 证据：图 6def63d71dca / 第 1 页 / 第1页右上 R1-R4 频段装配选项表

## 调试与烧录

### SWD 与基本调试测试点

JP1 引出 +3.3V，JP2 引出 SWCLK/M1 pin8，JP3 引出 SWDIO/M1 pin7，JP4 引出 RST，JP5 引出 GND，JP6 引出 BOOT。

- 参数与网络：`JP1=+3.3V`；`JP2=SWCLK / M1 pin8`；`JP3=SWDIO / M1 pin7`；`JP4=RST / M1 pin22`；`JP5=GND`；`JP6=BOOT / M1 pin21`
- 证据：图 6def63d71dca / 第 1 页 / 第1页左下 JP1-JP6 与中央 M1 SWCLK/SWDIO/RST/BOOT

### 辅助 U1 UART 测试点

JP8 的网络名 U1_RX 连接 M1 pin4（模组脚名 U1_TX），JP11 的网络名 U1_TX 连接 M1 pin5（模组脚名 U1_RX），形成交叉命名的辅助 UART 引出。

- 参数与网络：`JP8=net U1_RX -> M1 pin4 U1_TX`；`JP11=net U1_TX -> M1 pin5 U1_RX`；`connector=testpoints only`
- 证据：图 6def63d71dca / 第 1 页 / 第1页中央 M1 pins4/5 外部网络名与左下 JP8/JP11

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit LoRaWAN-AS923 系统架构 | `radio_module=M1 RAK3172`；`power=U1 VRH3301NLX`；`host=J1 HY-2.0_UART`；`rf=M1 RF -> C9/R8/C8/E1, all NC`；`debug=JP1-JP14` |
| 核心器件 | RAK3172 模组边界 | `reference=M1`；`part_number=RAK3172`；`pins=32`；`uart=U2_RX/U2_TX; U1_TX/U1_RX`；`debug=SWDIO/SWCLK`；`rf_pin=pin12 RF`；`reset_pin=pin22 RST`；`boot_pin=pin21 BOOT` |
| 电源 | +5V 到 +3.3V 稳压 | `regulator=U1 VRH3301NLX`；`vin=pin4 / +5V`；`enable=pin3 / +5V`；`vout=pin1 / +3.3V`；`ground=pins2,5`；`input_caps=C1 22uF; C2 1uF`；`output_cap=C3 1uF` |
| 电源 | Grove 5V 输入路径 | `connector=J1 pin3 VCC`；`series=F1 6V@1A`；`internal_rail=+5V`；`interface_cap=C10 100nF`；`protection=D3 LESD3Z5.0CMT1G to GND` |
| 电源 | RAK3172 VDD 去耦 | `module_pin=M1 pin24 VDD`；`rail=+3.3V`；`decoupling=C5 100nF; C6 22uF; C7 33pF`；`grounds=M1 pins11,17,18,23,28` |
| 保护电路 | +3.3V 保护 | `device=D1 RLSD52A031V`；`protected_net=+3.3V`；`return=GND` |
| 接口 | J1 Grove UART 针脚 | `connector=J1 HY-2.0_UART`；`pin1=RX <- U2_TX`；`pin2=TX -> U2_RX`；`pin3=VCC / 5V input`；`pin4=GND`；`logic_rail=+3.3V` |
| 总线 | M1 U2 UART 主机路由 | `module_tx=M1 pin2 U2_TX -> R9 22Ω -> J1 pin1 RX`；`module_rx=J1 pin2 TX -> R10 22Ω -> M1 pin1 U2_RX`；`series_resistors=R9/R10 22Ω`；`direction=module-to-host TX; host-to-module RX` |
| 关键网络 | RX/TX 上拉偏置 | `source=+3.3V`；`diode=D2 1N4148WS T4`；`rx_pull=R6 10KΩ`；`tx_pull=R7 10KΩ`；`nets=RX; TX` |
| 保护电路 | Grove 电源与 UART 保护 | `vcc=D3 LESD3Z5.0CMT1G to GND`；`rx=D4 RLSD52A031V to GND`；`tx=D5 RLSD52A031V to GND`；`fuse=F1 6V@1A` |
| 复位 | M1 复位网络 | `module_pin=M1 pin22 RST`；`pullup=R5 10KΩ to +3.3V`；`capacitor=C4 1uF to GND`；`testpoint=JP4` |
| 调试与烧录 | SWD 与基本调试测试点 | `JP1=+3.3V`；`JP2=SWCLK / M1 pin8`；`JP3=SWDIO / M1 pin7`；`JP4=RST / M1 pin22`；`JP5=GND`；`JP6=BOOT / M1 pin21` |
| GPIO 与控制信号 | BOOT 网络 | `module_pin=M1 pin21 BOOT`；`testpoint=JP6`；`strap=0Ω to GND`；`default_level=low` |
| 调试与烧录 | 辅助 U1 UART 测试点 | `JP8=net U1_RX -> M1 pin4 U1_TX`；`JP11=net U1_TX -> M1 pin5 U1_RX`；`connector=testpoints only` |
| 总线 | I2C 测试点 | `controller_scl=M1 pin9 SCL -> JP7`；`controller_sda=M1 pin10 SDA -> JP10`；`devices=not shown`；`address=not shown`；`pullups=not shown` |
| 总线 | SPI 测试点 | `mosi=M1 pin13 -> JP9`；`miso=M1 pin14 -> JP12`；`clock=M1 pin15 -> JP13`；`chip_select=M1 pin16 NSS -> JP14`；`device=not shown` |
| 射频 | RF 与天线可选支路 | `module_pin=M1 pin12 RF`；`series=R8 NC`；`module_side_shunt=C9 NC`；`antenna_side_shunt=C8 NC`；`antenna_reference=E1 NC`；`net=ANT` |
| 射频 | 470/868/915/923 版本表 | `R1=0Ω -> 470`；`R2=0Ω -> 868`；`R3=0Ω -> 915`；`R4=0Ω -> 923`；`selection_location=not shown in circuit` |
| 时钟 | 外部时钟 | `external_crystal=not shown`；`oscillator=not shown`；`clock_net=not shown`；`module_internal_clock=not expanded` |
| 存储 | 外部存储器 | `external_flash=not shown`；`external_ram=not shown`；`eeprom=not shown`；`sd=not shown`；`module=M1 RAK3172` |
| 射频 | AS923 版本实装选择 | `product_variant=AS923`；`sku=U184-AS923`；`table_selection=R4 0Ω -> 923`；`population_mark=not shown`；`asset_url_variant=Unit LoRaWAN-CN470` |
| 内存与 Flash | RAK3172 内部 MCU 与存储 | `schematic_module=RAK3172`；`document_mcu=STM32WLE5`；`document_flash=256KB`；`document_ram=64KB`；`internal_schematic=not shown` |
| 射频 | LoRaWAN 与 P2P 协议能力 | `document_protocol=LoRaWAN 1.0.3`；`document_classes=Class A; Class B; Class C`；`document_activation=OTAA; ABP`；`document_p2p=true`；`firmware=not shown` |
| 总线 | UART 与 AT 命令参数 | `document_baud=115200`；`document_protocol=AT command`；`baud_on_schematic=not shown`；`frame_format=not shown`；`flow_control=not shown`；`command_version=not shown` |
| 射频 | SMA 胶棒天线规格 | `document_impedance=50Ω`；`document_gain=2.3dBi`；`document_length=195mm`；`document_connector=SMA male pin`；`schematic_antenna=E1 NC`；`matching=R8/C8/C9 NC` |
| 射频 | 频段、灵敏度与通信距离 | `document_band=923-925MHz`；`document_sensitivity=-137dBm`；`document_125k_distance=2300m`；`document_500k_distance=1300m`；`schematic_test_data=not shown` |
| 电源 | 工作、空闲与休眠电流 | `document_idle=DC 5V/7.23mA`；`document_sleep=DC 5V/28.61uA`；`document_rx_500k=DC 5V/9.20mA`；`document_tx_500k=DC 5V/11.36mA`；`document_rx_125k=DC 5V/8.43mA`；`document_tx_125k=DC 5V/117.16mA`；`schematic_measurement=not shown` |
| 其他事实 | 工作温度与器件额定 | `document_temperature=0-40°C`；`schematic_temperature=not shown`；`regulator_load=not shown`；`uart_tolerance=not shown`；`esd_rating=not shown` |

## 待确认事项

- `rf.as923-population`：产品名和 SKU 指向 AS923，频段表将 R4 0Ω 对应 923，但图中没有在电路上标出 R1-R4 位置或明确哪一颗为本件实装；资源 URL 还位于 Unit LoRaWAN-CN470 路径。（证据：图 6def63d71dca / 第 1 页 / 第1页右上频段表仅列 R1-R4 对应关系，未标本件装配状态）
- `component.internal-mcu-memory`：产品正文称 STM32WLE5、256KB Flash、64KB RAM，但原理图只标外部模组 M1 RAK3172，没有展开内部 MCU 完整型号或存储容量。（证据：图 6def63d71dca / 第 1 页 / 第1页中央 M1 型号仅为 RAK3172）
- `rf.protocol-modes`：产品正文列出 LoRaWAN 1.0.3、Class A/B/C、OTAA、ABP 与 LoRa P2P；原理图没有协议栈、激活模式或固件版本信息。（证据：图 6def63d71dca / 第 1 页 / 第1页 M1 RAK3172 模组方框与 UART/RF 连接，无协议信息）
- `bus.uart-at-parameters`：产品正文称默认 115200 波特率并使用 AT 指令；原理图只确认 U2_RX/U2_TX 物理连线，未标波特率、帧格式、流控或命令集版本。（证据：图 6def63d71dca / 第 1 页 / 第1页 M1 U2_RX/U2_TX、R9/R10 与 J1，无串口参数注记）
- `rf.antenna-specification`：产品正文称 50Ω、2.3dBi、195mm、SMA 内针胶棒天线；本页 E1/R8/C8/C9 均标 NC，未标连接器型号、阻抗、增益或天线长度。（证据：图 6def63d71dca / 第 1 页 / 第1页中左 ANT/E1/R8/C8/C9 全部 NC）
- `rf.link-performance`：产品正文给出 AS923 923-925MHz、-137dBm，以及 P2P 125Kbps 2300m/500Kbps 1300m；原理图没有调制参数、测试环境、链路预算或射频测量数据。（证据：图 6def63d71dca / 第 1 页 / 第1页 RF/ANT 支路与频段选项表，无链路性能数据）
- `power.current-performance`：产品正文列出 5V 下空闲 7.23mA、休眠 28.61uA，以及不同速率的收发电流；原理图没有固件状态、射频功率、测量点或测试条件。（证据：图 6def63d71dca / 第 1 页 / 第1页 J1/F1/+5V/U1/+3.3V/M1 电源链路，无电流标注）
- `other.operating-limits`：产品正文给出 0-40°C；原理图未标整机工作温度、U1 最大负载、UART 电平容差或 ESD 等级。（证据：图 6def63d71dca / 第 1 页 / 第1页完整单页，无系统额定参数表）
- `review.as923-population`：请用 U184-AS923 BOM、实物和版本专用原理图确认 R4 0Ω/923 选项实际装配，并确认当前 CN470 路径资源是否为正确共用图。；原因：页面只列版本对应表，没有标本件实装，且资源 URL 指向 CN470 目录。
- `review.internal-mcu-memory`：请用实装 RAK3172 版本、模组 datasheet 或 BOM 确认内部 STM32WLE5 完整型号、256KB Flash 与 64KB RAM。；原因：原理图只有模组料号，没有展开内部 MCU 与存储。
- `review.protocol-modes`：请从 U184-AS923 发布固件和 RAK3172 固件版本确认 LoRaWAN 1.0.3、Class A/B/C、OTAA/ABP 与 P2P 支持。；原因：协议栈能力不在原理图电气连接中。
- `review.uart-at-parameters`：请用发布固件或实测确认默认 115200、帧格式、流控与 AT 命令集版本。；原因：原理图只给 UART 网络，没有通信参数。
- `review.antenna-specification`：请核对 AS923 实物的 SMA 连接器与胶棒天线料号、50Ω、2.3dBi、195mm 规格，并解释原理图 E1/R8/C8/C9 全部 NC 的装配状态。；原因：正文天线规格与本页 NC 射频支路无法仅凭图纸统一。
- `review.link-performance`：请按 AS923 法规配置、天线、发射功率和测试环境复核频段、-137dBm 灵敏度及两档 P2P 距离。；原因：原理图没有射频测试条件或链路预算。
- `review.current-performance`：请按明确固件状态、数据率、发射功率与 5V 供电路径复测空闲、休眠和收发电流。；原因：正文电流没有对应的图纸测试点或条件。
- `review.operating-limits`：请用整机规格、BOM 额定值和环境测试确认 0-40°C、LDO 带载、UART 容限及 ESD 等级。；原因：这些系统级额定参数未印在原理图。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6def63d71dca037aa67dff4bd11dd51418f453e8fa9a1cc794867509b3166570` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20LoRaWAN-CN470/schematic.png` |

---

源文档：`zh_CN/unit/Unit LoRaWAN-AS923.md`

源文档 SHA-256：`f77fed5ba25f165eaaa9fe1a4afa643fbeac4232be223776cdef0a5f99439f97`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
