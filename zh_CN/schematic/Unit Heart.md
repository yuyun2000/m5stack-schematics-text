# Unit Heart 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Heart |
| SKU | U029 |
| 产品 ID | `unit-heart-641c5a874047` |
| 源文档 | `zh_CN/unit/heart.md` |

## 概述

Unit Heart 以 U1 MAX30100 为血氧/心率光学传感器，R_DRV 与 IR_DRV 驱动通道、INT 中断和 I2C 均引到板内测试/排针连接。J1 的 SCL/SDA 经 Q2/Q1 AO3400A 双向电平转换后成为 CHIP_SCL/CHIP_SDA，外侧分别上拉到 VCC，芯片侧上拉到 +3.3V。U3 HT7533-3.3V 从 VCC 生成 +3.3V，U2 RT9193-1.8V 再由 +3.3V 生成 +1.8V；MAX30100 的 LED 正端使用 +3.3V，VDD 使用 +1.8V。正文给出的 7 位 I2C 地址 0x57 和 Grove 5V 供电没有直接印在原理图上，需通过芯片资料、整板规格或总线扫描复核。

## 检索关键词

`Unit Heart`、`U029`、`MAX30100`、`RT9193-1.8V`、`HT7533-3.3V`、`AO3400A`、`pulse oximeter`、`heart rate`、`SpO2`、`I2C`、`0x57`、`SCL`、`SDA`、`CHIP_SCL`、`CHIP_SDA`、`INT`、`R_DRV`、`IR_DRV`、`R_LED+`、`IR_LED+`、`VCC`、`+3.3V`、`+1.8V`、`J1 IIC_Socket_4P`、`P1 Header 4`、`P2 Header 4`、`JP1 R_DRV`、`JP2 IR_DRV`、`JP3 INT`、`R1-R4 4.7KΩ`、`R5 4.7KΩ`、`C7 22nF`、`bidirectional level shifter`、`optical sensor`、`5V Grove`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | MAX30100 | 集成红光/红外驱动、光学采集、I2C 和中断接口的血氧/心率传感器 | 图 dfc9779beff7 / 第 1 页 / 第 1 页网格 B3，U1 MAX30100 pin1-pin14 |
| U2 | RT9193-1.8V | 将 +3.3V 稳压为 MAX30100 VDD 使用的 +1.8V | 图 dfc9779beff7 / 第 1 页 / 第 1 页网格 C1-C2，U2 RT9193-1.8V |
| U3 | HT7533-3.3V | 将 J1 VCC 稳压为 +3.3V | 图 dfc9779beff7 / 第 1 页 / 第 1 页网格 C3，U3 HT7533-3.3V |
| Q1/Q2 | AO3400A | SDA/SCL 在 VCC 侧与 +3.3V 芯片侧之间的双向 MOSFET 电平转换 | 图 dfc9779beff7 / 第 1 页 / 第 1 页网格 B2，Q1/Q2 AO3400A 与 SDA/SCL/CHIP_SDA/CHIP_SCL |
| J1 | IIC_Socket_4P | 外部 SCL、SDA、VCC、GND Grove I2C 接口 | 图 dfc9779beff7 / 第 1 页 / 第 1 页网格 C4，J1 IIC_Socket_4P pin1-pin4 |
| P1 | Header 4 | 引出 CHIP_SCL、CHIP_SDA、IR_DRV、R_DRV 的四针板内接口 | 图 dfc9779beff7 / 第 1 页 / 第 1 页网格 B3，P1 Header 4 |
| P2 | Header 4 | 引出 +3.3V、INT、+1.8V、GND 的四针板内接口 | 图 dfc9779beff7 / 第 1 页 / 第 1 页网格 B3，P2 Header 4 |
| JP1/JP2/JP3 | test | 分别连接 R_DRV、IR_DRV、INT 的测试点 | 图 dfc9779beff7 / 第 1 页 / 第 1 页 U1 周围 JP1 R_DRV、JP2 IR_DRV、JP3 INT test |
| R1/R2/R3/R4 | 4.7KΩ | I2C 芯片侧与外部侧的四个上拉电阻 | 图 dfc9779beff7 / 第 1 页 / 第 1 页网格 A1-B3，R1-R4 4.7KΩ 与 SCL/SDA 两侧 |
| R5 | 4.7KΩ | MAX30100 INT 到 +3.3V 的上拉电阻 | 图 dfc9779beff7 / 第 1 页 / 第 1 页网格 B3，R5 4.7KΩ 与 INT/+3.3V |
| C1/C4/C5/C6 | 100nF / 100nF / 10uF / 10uF | VCC 与 +3.3V 电源轨的输入输出去耦和滤波 | 图 dfc9779beff7 / 第 1 页 / 第 1 页网格 C3-C4，C1/C4/C5/C6 |
| C2/C3/C7 | 1uF / 1uF / 22nF | RT9193 输入、输出和 BP 旁路电容 | 图 dfc9779beff7 / 第 1 页 / 第 1 页网格 C1-C2，U2 与 C2/C3/C7 |

## 系统结构

### Unit Heart 系统结构

J1 接入 I2C 与 VCC，Q1/Q2 完成 I2C 电平转换，U3/U2 依次生成 +3.3V/+1.8V，U1 MAX30100 使用双电源并提供 R_DRV、IR_DRV 与 INT。

- 参数与网络：`sensor=U1 MAX30100`；`host_interface=J1 I2C`；`level_shift=Q1/Q2 AO3400A`；`power=VCC->U3 +3.3V->U2 +1.8V`；`led_drives=R_DRV,IR_DRV`；`interrupt=INT`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页完整原理图全部功能区

## 电源

### U3 HT7533-3.3V

U3 VIN pin2 接 J1 VCC，VOUT pin3 输出 +3.3V，GND pin1 接地；输入 C6 10uF，输出 C4 100nF 与 C5 10uF。

- 参数与网络：`input=VCC at U3 pin2`；`output=+3.3V at U3 pin3`；`ground=U3 pin1 GND`；`input_cap=C6 10uF`；`output_caps=C4 100nF,C5 10uF`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页网格 C3，U3/C4/C5/C6 与 VCC/+3.3V

### U2 RT9193-1.8V

U2 IN pin1 与 EN pin3 接 +3.3V，OUT pin5 输出 +1.8V，GND pin2 接地，BP pin4 经 C7 22nF 接地；C2/C3 各 1uF 位于输入/输出。

- 参数与网络：`input=+3.3V at pin1`；`enable=+3.3V at pin3`；`output=+1.8V at pin5`；`ground=pin2 GND`；`bypass=pin4 BP via C7 22nF to GND`；`input_cap=C2 1uF`；`output_cap=C3 1uF`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页网格 C1-C2，U2/C2/C3/C7 与 +3.3V/+1.8V

### MAX30100 双电源域

U1 R_LED+/IR_LED+ pin9/pin10 接 +3.3V，U1 VDD pin11 接 +1.8V，PGND pin4 与 GND pin12 接 GND；+3.3V/+1.8V/GND 同时引到 P2。

- 参数与网络：`led_supply=+3.3V at U1 pins9,10`；`core_supply=+1.8V at U1 pin11`；`grounds=U1 pin4 PGND,pin12 GND`；`header=P2 pin1 +3.3V,pin3 +1.8V,pin4 GND`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页 U1 pin4/pin9-pin12 与 P2

## 接口

### J1 IIC_Socket_4P

J1 pin1=IIC_SCL/SCL、pin2=IIC_SDA/SDA、pin3=VCC、pin4=GND；VCC 输入 U3，SCL/SDA 进入 Q2/Q1 电平转换。

- 参数与网络：`pin_1=SCL`；`pin_2=SDA`；`pin_3=VCC / power input`；`pin_4=GND`；`scl_destination=Q2`；`sda_destination=Q1`；`vcc_destination=U3 VIN`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页网格 C4，J1 pin1-pin4 与同名网络

### P1 Header 4

P1 pin1=CHIP_SCL、pin2=CHIP_SDA、pin3=IR_DRV、pin4=R_DRV。

- 参数与网络：`pin_1=CHIP_SCL`；`pin_2=CHIP_SDA`；`pin_3=IR_DRV`；`pin_4=R_DRV`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页网格 B3，P1 Header 4 pin1-pin4

### P2 Header 4

P2 pin1=+3.3V、pin2=INT、pin3=+1.8V、pin4=GND。

- 参数与网络：`pin_1=+3.3V`；`pin_2=INT`；`pin_3=+1.8V`；`pin_4=GND`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页网格 B3，P2 Header 4 pin1-pin4

## 总线

### SCL/SDA 双向电平转换

外部 SDA/SCL 分别经 Q1/Q2 AO3400A 连接 CHIP_SDA/CHIP_SCL；外部侧 R3/R4 各 4.7KΩ 上拉到 VCC，芯片侧 R2/R1 各 4.7KΩ 上拉到 +3.3V，Q1/Q2 栅极接 +3.3V。

- 参数与网络：`sda_path=SDA -> Q1 AO3400A -> CHIP_SDA`；`scl_path=SCL -> Q2 AO3400A -> CHIP_SCL`；`external_pullups=R3 SDA,R4 SCL 4.7KΩ to VCC`；`chip_pullups=R2 CHIP_SDA,R1 CHIP_SCL 4.7KΩ to +3.3V`；`mosfet_gates=+3.3V`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页网格 A1-B3，R1-R4/Q1/Q2 与 SDA/SCL/CHIP_SDA/CHIP_SCL

## GPIO 与控制信号

### MAX30100 INT

U1 INT pin13 连接 INT 网络，R5 4.7KΩ 将 INT 上拉到 +3.3V，INT 同时引到 JP3 test 和 P2 pin2；J1 Grove 未引出 INT。

- 参数与网络：`source=U1 pin13`；`net=INT`；`pullup=R5 4.7KΩ to +3.3V`；`testpoint=JP3`；`header=P2 pin2`；`grove_exported=false`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页 U1 pin13 INT、R5、JP3 与 P2 pin2

## 时钟

### 时钟电路

完整原理图未显示晶振、振荡器或外部时钟网络，MAX30100 没有外部时钟引脚连接。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false`；`external_clock_pin_connected=false`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页完整图无时钟器件或时钟网络

## 复位

### 复位、BOOT 与使能控制

完整原理图未显示 RESET、BOOT、主控或外部调试下载接口；U2 EN 固定接 +3.3V，U3 无独立使能引脚。

- 参数与网络：`reset_shown=false`；`boot_shown=false`；`mcu_shown=false`；`debug_download_shown=false`；`u2_enable=+3.3V`；`u3_enable_pin_shown=false`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页完整图及 U2 EN/U3 引脚

## 保护电路

### J1 I2C 与电源保护

完整原理图未在 J1 SCL、SDA、VCC 或 GND 路径画出 TVS、ESD 阵列、保险丝或反接保护；I2C 线上仅有上拉与 Q1/Q2 电平转换。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`i2c_components=pullups and AO3400A level shifters`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页 J1 至 Q1/Q2/U3 的全部路径

## 关键网络

### J1 到 MAX30100 关键路径

J1.1 SCL→Q2→CHIP_SCL→U1.2，J1.2 SDA→Q1→CHIP_SDA→U1.3，J1.3 VCC→U3→+3.3V→U2→+1.8V，U1.13 INT→P2.2/JP3。

- 参数与网络：`scl_path=J1.1->Q2->CHIP_SCL->U1.2`；`sda_path=J1.2->Q1->CHIP_SDA->U1.3`；`power_path=J1.3 VCC->U3 +3.3V->U2 +1.8V`；`interrupt_path=U1.13->INT->P2.2/JP3`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页完整 J1/Q1/Q2/U1/U2/U3/P2 信号与电源路径

## 内存与 Flash

### 主控与存储器

完整原理图未显示 MCU、协处理器、Flash、EEPROM、RAM、SD 卡或其他外部存储器。

- 参数与网络：`mcu_shown=false`；`coprocessor_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页完整图仅含传感器、电源、电平转换与连接器

## 传感器

### U1 MAX30100

U1 pin2=SCL/CHIP_SCL、pin3=SDA/CHIP_SDA、pin4=PGND、pin5=IR_DRV、pin6=R_DRV、pin9=R_LED+、pin10=IR_LED+、pin11=VDD/+1.8V、pin12=GND、pin13=INT；pin1/pin7/pin8/pin14 标 NC。

- 参数与网络：`pin_1=NC`；`pin_2=SCL / CHIP_SCL`；`pin_3=SDA / CHIP_SDA`；`pin_4=PGND / GND`；`pin_5=IR_DRV`；`pin_6=R_DRV`；`pin_7=NC`；`pin_8=NC`；`pin_9=R_LED+ / +3.3V`；`pin_10=IR_LED+ / +3.3V`；`pin_11=VDD / +1.8V`；`pin_12=GND`；`pin_13=INT`；`pin_14=NC`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页网格 B3，U1 MAX30100 全部引脚编号与网络名

### MAX30100 红光与红外驱动

U1 R_LED+ pin9 与 IR_LED+ pin10 均接 +3.3V；R_DRV pin6 与 IR_DRV pin5 分别引到 JP1/JP2 测试点和 P1 pin4/pin3。

- 参数与网络：`red_led_positive=U1 pin9 +3.3V`；`ir_led_positive=U1 pin10 +3.3V`；`red_drive=U1 pin6 R_DRV -> JP1,P1.4`；`ir_drive=U1 pin5 IR_DRV -> JP2,P1.3`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页 U1 pin5/pin6/pin9/pin10、JP1/JP2 与 P1

## 调试与烧录

### JP1-JP3 测试点

JP1 标 test 并连接 R_DRV，JP2 标 test 并连接 IR_DRV，JP3 标 test 并连接 INT；图中没有 MCU 下载、JTAG 或 SWD 接口。

- 参数与网络：`JP1=R_DRV`；`JP2=IR_DRV`；`JP3=INT`；`jtag_shown=false`；`swd_shown=false`；`download_connector_shown=false`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页 U1 周围 JP1/JP2/JP3 test 与完整图

## 模拟电路

### 光学模拟采样链

原理图未从 U1 引出独立光电模拟信号，也未显示外部运放、ADC 或跨阻放大器；可见外部连接仅为数字 I2C/INT、LED 驱动、电源和地。

- 参数与网络：`external_photodiode_signal_shown=false`；`external_opamp_shown=false`；`external_adc_shown=false`；`external_tia_shown=false`；`visible_interfaces=I2C,INT,R_DRV,IR_DRV,power`
- 证据：图 dfc9779beff7 / 第 1 页 / 第 1 页 U1 全部引脚与完整外部电路

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Heart 系统结构 | `sensor=U1 MAX30100`；`host_interface=J1 I2C`；`level_shift=Q1/Q2 AO3400A`；`power=VCC->U3 +3.3V->U2 +1.8V`；`led_drives=R_DRV,IR_DRV`；`interrupt=INT` |
| 传感器 | U1 MAX30100 | `pin_1=NC`；`pin_2=SCL / CHIP_SCL`；`pin_3=SDA / CHIP_SDA`；`pin_4=PGND / GND`；`pin_5=IR_DRV`；`pin_6=R_DRV`；`pin_7=NC`；`pin_8=NC`；`pin_9=R_LED+ / +3.3V`；`pin_10=IR_LED+ / +3.3V`；`pin_11=VDD / +1.8V`；`pin_12=GND`；`pin_13=INT`；`pin_14=NC` |
| 传感器 | MAX30100 红光与红外驱动 | `red_led_positive=U1 pin9 +3.3V`；`ir_led_positive=U1 pin10 +3.3V`；`red_drive=U1 pin6 R_DRV -> JP1,P1.4`；`ir_drive=U1 pin5 IR_DRV -> JP2,P1.3` |
| 总线 | SCL/SDA 双向电平转换 | `sda_path=SDA -> Q1 AO3400A -> CHIP_SDA`；`scl_path=SCL -> Q2 AO3400A -> CHIP_SCL`；`external_pullups=R3 SDA,R4 SCL 4.7KΩ to VCC`；`chip_pullups=R2 CHIP_SDA,R1 CHIP_SCL 4.7KΩ to +3.3V`；`mosfet_gates=+3.3V` |
| 接口 | J1 IIC_Socket_4P | `pin_1=SCL`；`pin_2=SDA`；`pin_3=VCC / power input`；`pin_4=GND`；`scl_destination=Q2`；`sda_destination=Q1`；`vcc_destination=U3 VIN` |
| 接口 | P1 Header 4 | `pin_1=CHIP_SCL`；`pin_2=CHIP_SDA`；`pin_3=IR_DRV`；`pin_4=R_DRV` |
| 接口 | P2 Header 4 | `pin_1=+3.3V`；`pin_2=INT`；`pin_3=+1.8V`；`pin_4=GND` |
| GPIO 与控制信号 | MAX30100 INT | `source=U1 pin13`；`net=INT`；`pullup=R5 4.7KΩ to +3.3V`；`testpoint=JP3`；`header=P2 pin2`；`grove_exported=false` |
| 调试与烧录 | JP1-JP3 测试点 | `JP1=R_DRV`；`JP2=IR_DRV`；`JP3=INT`；`jtag_shown=false`；`swd_shown=false`；`download_connector_shown=false` |
| 电源 | U3 HT7533-3.3V | `input=VCC at U3 pin2`；`output=+3.3V at U3 pin3`；`ground=U3 pin1 GND`；`input_cap=C6 10uF`；`output_caps=C4 100nF,C5 10uF` |
| 电源 | U2 RT9193-1.8V | `input=+3.3V at pin1`；`enable=+3.3V at pin3`；`output=+1.8V at pin5`；`ground=pin2 GND`；`bypass=pin4 BP via C7 22nF to GND`；`input_cap=C2 1uF`；`output_cap=C3 1uF` |
| 电源 | MAX30100 双电源域 | `led_supply=+3.3V at U1 pins9,10`；`core_supply=+1.8V at U1 pin11`；`grounds=U1 pin4 PGND,pin12 GND`；`header=P2 pin1 +3.3V,pin3 +1.8V,pin4 GND` |
| 电源 | J1 VCC 输入电压 | `documented_input=5V`；`schematic_net=VCC`；`regulator=U3 HT7533-3.3V`；`voltage_printed_on_schematic=false` |
| 总线地址 | MAX30100 I2C 地址 | `documented_address=0x57`；`address_width=7-bit`；`device=U1 MAX30100`；`address_printed_on_schematic=false`；`address_strap_shown=false` |
| 关键网络 | J1 到 MAX30100 关键路径 | `scl_path=J1.1->Q2->CHIP_SCL->U1.2`；`sda_path=J1.2->Q1->CHIP_SDA->U1.3`；`power_path=J1.3 VCC->U3 +3.3V->U2 +1.8V`；`interrupt_path=U1.13->INT->P2.2/JP3` |
| 保护电路 | J1 I2C 与电源保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`i2c_components=pullups and AO3400A level shifters` |
| 时钟 | 时钟电路 | `crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false`；`external_clock_pin_connected=false` |
| 复位 | 复位、BOOT 与使能控制 | `reset_shown=false`；`boot_shown=false`；`mcu_shown=false`；`debug_download_shown=false`；`u2_enable=+3.3V`；`u3_enable_pin_shown=false` |
| 内存与 Flash | 主控与存储器 | `mcu_shown=false`；`coprocessor_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false` |
| 模拟电路 | 光学模拟采样链 | `external_photodiode_signal_shown=false`；`external_opamp_shown=false`；`external_adc_shown=false`；`external_tia_shown=false`；`visible_interfaces=I2C,INT,R_DRV,IR_DRV,power` |

## 待确认事项

- `power.documented-5v-input`：产品正文 Grove 映射将 J1 VCC 标为 5V，但原理图仅标 VCC 并接 U3 VIN，没有直接打印 VCC 电压值。（证据：图 dfc9779beff7 / 第 1 页 / 第 1 页 J1 pin3 VCC 至 U3 VIN，页面无 5V 数值）
- `address.documented-0x57`：产品正文列出 7 位 I2C 地址 0x57；原理图确认总线设备为 U1 MAX30100，但页面未打印地址或地址表，因此需结合 MAX30100 资料或 I2C 扫描复核。（证据：图 dfc9779beff7 / 第 1 页 / 第 1 页 U1 SCL/SDA 与 J1 I2C 路径，页面无地址数值）
- `review.vcc-input`：请依据整板电气规格或实物确认 J1 VCC 的标称输入为 5V。；原因：5V 来自产品正文 Grove 映射，原理图仅标 VCC。
- `review.i2c-address`：请依据 MAX30100 数据手册或 I2C 扫描确认 7 位地址 0x57。；原因：原理图确认器件和总线连接，但没有打印地址值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `dfc9779beff72b6000b75322c81b2f0c9824ab51a4eb13f6f9092c9fbef4fbf0` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/716/Unit_Heart_page_01.png` |

---

源文档：`zh_CN/unit/heart.md`

源文档 SHA-256：`41437919a8b4822b17f1d27912fcad00fa9e7b7cebe5af8952d8d9f95467021d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
