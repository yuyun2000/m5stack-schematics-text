# Unit KMeter 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit KMeter |
| SKU | U133 |
| 产品 ID | `unit-kmeter-21cc0cf305f9` |
| 源文档 | `zh_CN/unit/kmeter.md` |

## 概述

Unit KMeter 以 U3 ESP32-C3 为主控，通过 TC_CS、TC_SCK、TC_MISO 三线接口连接 U4（原理图标 MAX6675/31855）热电偶转换器，并由 Grove 的 ESP_SCL/ESP_SDA 向外提供 I2C。TC1 PCC-SMP-K-100-CE 的 T-/T+ 经过 FB1/FB2、R6/R5 1KΩ 和 47nF 差分滤波后进入 U4，屏蔽端 SH 接 GND。U1 MD5333 从 VCC_5V 生成 VCC_3V3；U2 HX6306P332 生成模拟 3.3V 并经 FB3 分隔为 VCC_A3V3，分别为 MCU 与热电偶转换器供电。板上还包含 40MHz 晶体、ESP_EN/ESP_BOOT 上拉、DL_ESPC3 下载口、白/红 LED、SRV05-4 保护和 LNA_IN 50Ω 接地终端；正文指定 MAX31855KASA+T、I2C 0x66/4 字节协议及量程精度，需结合 BOM、数据手册与固件确认。

## 检索关键词

`Unit KMeter`、`U133`、`ESP32-C3`、`MAX6675/31855`、`MAX31855KASA+T`、`MD5333`、`HX6306P332`、`PCC-SMP-K-100-CE`、`K-type thermocouple`、`I2C`、`0x66`、`ESP_SCL`、`ESP_SDA`、`TC_CS GPIO7`、`TC_SCK GPIO6`、`TC_MISO GPIO5`、`TEMP_Read`、`ESP_BOOT GPIO9`、`ESP_EN CHIP_EN`、`ESP_RXD GPIO20`、`ESP_TXD GPIO21`、`VCC_5V`、`VCC_3V3`、`VCC_A3V3`、`X1 40M`、`SRV05-4`、`FB1 FB2 FB3`、`R5 R6 1KΩ`、`C11 47nF`、`LED1 white`、`LED2 red`、`DL_ESPC3`、`14-bit ADC`、`0.25C resolution`、`-200 to 1350C`、`thermocouple_H`、`internal_H`、`LNA_IN 50R GND`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | ESP32-C3 | 读取热电偶转换器、提供 I2C 固件接口、状态 LED 与 UART 下载控制的主控 | 图 73aee450ef05 / 第 1 页 / 第 1 页中部 MCU 区 U3 ESP32-C3 pin1-pin33 |
| U4 | MAX6675/31855 | K 型热电偶 T-/T+ 到 TC_MISO 数字数据的转换器，受 TC_CS/TC_SCK 控制 | 图 73aee450ef05 / 第 1 页 / 第 1 页右中 Thermocouple Converter 区 U4 MAX6675/31855 |
| U1 | MD5333 | 将 VCC_5V 稳压为 MCU 使用的 VCC_3V3 | 图 73aee450ef05 / 第 1 页 / 第 1 页左上 MCU LDO 区 U1 MD5333 |
| U2 | HX6306P332 | 将 VCC_5V 稳压为热电偶 ADC 使用的模拟 3.3V 电源 | 图 73aee450ef05 / 第 1 页 / 第 1 页上部 ADC LDO 区 U2 HX6306P332 |
| TC1 | PCC-SMP-K-100-CE | 引出 T-、T+ 和接地屏蔽 SH 的 K 型热电偶插座 | 图 73aee450ef05 / 第 1 页 / 第 1 页最右 Thermocouple Connector 区 TC1 PCC-SMP-K-100-CE |
| GROVE | 未标注 | ESP_SCL、ESP_SDA、VCC_5V、GND 外部接口 | 图 73aee450ef05 / 第 1 页 / 第 1 页左中 Grove I2C 区 GROVE IO2/IO1/5V/GND |
| J2 | DL_ESPC3 | ESP32-C3 的 3V3、UART、EN、BOOT、GND 下载接口 | 图 73aee450ef05 / 第 1 页 / 第 1 页左下 MCU DL CON 区 J2 DL_ESPC3 pin1-pin6 |
| D1 | SRV05-4 | TC_SCK、TC_MISO、ESP_SCL、ESP_SDA 四路信号的多通道瞬态保护阵列 | 图 73aee450ef05 / 第 1 页 / 第 1 页左中 D1 SRV05-4，IO1-IO4/VCC/GND |
| X1/C9/C10/R4 | 40M / 12pF / 12pF / 22Ω | ESP32-C3 XTAL_P/XTAL_N 的 40MHz 晶体与负载/串联网络 | 图 73aee450ef05 / 第 1 页 / 第 1 页 MCU 区左侧 X1 40M、C9/C10 12pF、R4 22Ω |
| R5/R6/C11/FB1/FB2 | 1KΩ / 1KΩ / 47nF / 330R GZ1005D331TF / 330R GZ1005D331TF | 热电偶 T+/T- 的串联限流、差分滤波与铁氧体抑制网络 | 图 73aee450ef05 / 第 1 页 / 第 1 页右侧 U4 T-/T+ 至 TC1 的 R5/R6/C11/FB1/FB2 |
| FB3 | 330R/GZ1005D331TF | U2 输出与 VCC_A3V3 之间的模拟电源铁氧体隔离 | 图 73aee450ef05 / 第 1 页 / 第 1 页上部 ADC LDO 区 FB3 与 VCC_A3V3 |
| LED1/R1 | white / 22KΩ | VCC_3V3 电源白色指示灯及串联电阻 | 图 73aee450ef05 / 第 1 页 / 第 1 页左上 MCU LDO 区 LED1 white 与 R1 22KΩ |
| LED2/R9 | red / 10KΩ | TEMP_Read 网络控制的红色温度状态 LED 及串联电阻 | 图 73aee450ef05 / 第 1 页 / 第 1 页 MCU 左下 Temp LED 区 LED2 red 与 R9 10KΩ |
| R3/R7/R8/R10/R11/R2 | 10KΩ / 10KΩ / 10KΩ / 10KΩ / 10KΩ / 50Ω | ESP_SCL/SDA、ESP_EN、ESP_BOOT 的上拉及 LNA_IN 的 50Ω 接地终端 | 图 73aee450ef05 / 第 1 页 / 第 1 页 R7/R8 I2C、R10 EN、R11 BOOT、R2 LNA_IN 与 R3 GPIO 网络 |

## 系统结构

### Unit KMeter 系统结构

U3 ESP32-C3 通过 TC_CS/TC_SCK/TC_MISO 控制 U4 热电偶转换器，通过 ESP_SCL/ESP_SDA 向 Grove 主机提供 I2C；U1/U2 分别供 MCU 与 ADC 电源，TC1 接入热电偶。

- 参数与网络：`controller=U3 ESP32-C3`；`converter=U4 MAX6675/31855`；`thermocouple_connector=TC1 PCC-SMP-K-100-CE`；`host_bus=GROVE I2C`；`mcu_power=U1 MD5333`；`adc_power=U2 HX6306P332`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页完整原理图全部功能分区

## 核心器件

### U3 ESP32-C3 关键引脚

U3 GPIO1 pin5=TEMP_Read、GPIO3 pin8=ESP_SCL、GPIO4 pin9=ESP_SDA、GPIO5 pin10=TC_MISO、GPIO6 pin12=TC_SCK、GPIO7 pin13=TC_CS、GPIO9 pin15=ESP_BOOT、CHIP_EN pin7=ESP_EN、GPIO20 pin27=ESP_RXD、GPIO21 pin28=ESP_TXD。

- 参数与网络：`GPIO1_pin5=TEMP_Read`；`GPIO3_pin8=ESP_SCL`；`GPIO4_pin9=ESP_SDA`；`GPIO5_pin10=TC_MISO`；`GPIO6_pin12=TC_SCK`；`GPIO7_pin13=TC_CS`；`GPIO9_pin15=ESP_BOOT`；`CHIP_EN_pin7=ESP_EN`；`GPIO20_pin27=ESP_RXD`；`GPIO21_pin28=ESP_TXD`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页 U3 右侧 pin5-pin15 与 pin27-pin28 网络标注

### U4 MAX6675/31855

U4 pin1=GND、pin2=T-、pin3=T+、pin4=VCC/VCC_A3V3、pin5=SCK/TC_SCK、pin6=CS/TC_CS、pin7=MISO/TC_MISO、pin8 标 NC 并在页面旁标 TC_N。

- 参数与网络：`pin_1=GND`；`pin_2=T-`；`pin_3=T+`；`pin_4=VCC_A3V3`；`pin_5=TC_SCK`；`pin_6=TC_CS`；`pin_7=TC_MISO`；`pin_8=NC / page label TC_N`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页 Thermocouple Converter 区 U4 pin1-pin8

## 电源

### U1 MD5333 MCU 电源

U1 VIN pin3 接 VCC_5V、VOUT pin2 输出 VCC_3V3、GND pin1 接地；C1 4.7uF/C2 100nF 位于输入，C3 4.7uF 位于输出。

- 参数与网络：`input=VCC_5V at pin3`；`output=VCC_3V3 at pin2`；`ground=pin1 GND`；`input_caps=C1 4.7uF,C2 100nF`；`output_cap=C3 4.7uF`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页左上 MCU LDO 区 U1/C1-C3

### U2 HX6306P332 ADC 电源

U2 VIN pin3 接 VCC_5V、VOUT pin2 经 FB3 输出 VCC_A3V3、GND pin1 接地；C4 4.7uF/C5 100nF 输入去耦，C6 4.7uF/C8 100nF 位于 FB3 前，C7 4.7uF 位于 VCC_A3V3 侧。

- 参数与网络：`input=VCC_5V at pin3`；`raw_output=U2 pin2`；`filtered_output=VCC_A3V3 via FB3`；`ground=pin1 GND`；`input_caps=C4 4.7uF,C5 100nF`；`pre_bead_caps=C6 4.7uF,C8 100nF`；`post_bead_cap=C7 4.7uF`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页上部 ADC LDO 区 U2/C4-C8/FB3

### U4 VCC_A3V3 电源

U4 VCC pin4 接 VCC_A3V3、GND pin1 接地，旁路配置 100nF 与 4.7uF 电容到 GND；模拟电源由 FB3 与 MCU VCC_3V3 分区。

- 参数与网络：`vcc=U4 pin4 VCC_A3V3`；`ground=U4 pin1 GND`；`decoupling=100nF and 4.7uF`；`power_partition=U2/FB3 separate from U1 VCC_3V3`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页 U4 pin1/pin4 及旁路电容、上部 FB3/VCC_A3V3

## 接口

### GROVE I2C 接口

GROVE IO2 连接 ESP_SCL、IO1 连接 ESP_SDA、5V 连接 VCC_5V、GND 接地；SCL/SDA 分别由 R7/R8 10KΩ 上拉到 VCC_3V3。

- 参数与网络：`IO2=ESP_SCL`；`IO1=ESP_SDA`；`power=VCC_5V`；`ground=GND`；`scl_pullup=R7 10KΩ to VCC_3V3`；`sda_pullup=R8 10KΩ to VCC_3V3`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页左中 Grove I2C 区 GROVE/R7/R8

## 总线

### ESP32-C3 到 U4 串行接口

U3 GPIO7/TC_CS 连接 U4 CS pin6，GPIO6/TC_SCK 连接 U4 SCK pin5，GPIO5/TC_MISO 连接 U4 MISO pin7；图中没有 MOSI 连接，数据方向为 U4 到 U3。

- 参数与网络：`controller=U3 ESP32-C3`；`device=U4 MAX6675/31855`；`chip_select=GPIO7 pin13 -> TC_CS -> U4 pin6`；`clock=GPIO6 pin12 -> TC_SCK -> U4 pin5`；`data=U4 pin7 TC_MISO -> GPIO5 pin10`；`mosi_shown=false`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页 U3 TC_CS/TC_SCK/TC_MISO 与 U4 pin5-pin7

### 外部主机 I2C

外部主机通过 GROVE ESP_SCL/ESP_SDA 连接 U3 GPIO3 pin8/GPIO4 pin9，主机为 I2C 控制器，U3 固件为设备端；总线逻辑上拉轨为 VCC_3V3。

- 参数与网络：`controller=external host`；`device=U3 ESP32-C3 firmware`；`scl=GROVE IO2 ESP_SCL -> U3 GPIO3 pin8`；`sda=GROVE IO1 ESP_SDA -> U3 GPIO4 pin9`；`pullup_rail=VCC_3V3`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页 GROVE ESP_SCL/ESP_SDA 至 U3 GPIO3/GPIO4

## GPIO 与控制信号

### LED1/LED2 指示灯

LED1 white 与 R1 22KΩ 串接在 VCC_3V3 和 GND 之间作为电源指示；TEMP_Read 网络经 LED2 red 与 R9 10KΩ 到 GND，TEMP_Read 高电平时形成红灯电流路径。

- 参数与网络：`power_led=VCC_3V3 -> LED1 white -> R1 22KΩ -> GND`；`temp_led=TEMP_Read -> LED2 red -> R9 10KΩ -> GND`；`temp_net=U3 GPIO1 pin5`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页 MCU LDO LED1 区与 Temp LED LED2/R9 区

## 时钟

### ESP32-C3 40MHz 晶体

U3 XTAL_P pin30 经 R4 22Ω 连接 X1，XTAL_N pin29 连接 X1 另一端；C9/C10 各 12pF 从晶体两端接 GND，X1 标 40M。

- 参数与网络：`frequency=40M`；`crystal=X1 TXC/8Z400001`；`xtal_p=U3 pin30 via R4 22Ω`；`xtal_n=U3 pin29`；`load_caps=C9 12pF,C10 12pF`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页 MCU 区 X1/C9/C10/R4 与 U3 XTAL_P/XTAL_N

## 复位

### ESP_EN 与 ESP_BOOT

U3 CHIP_EN pin7 的 ESP_EN 由 R10 10KΩ 上拉到 VCC_3V3，并由 C14 100nF 对地；GPIO9 pin15 的 ESP_BOOT 由 R11 10KΩ 上拉到 VCC_3V3，两网均引到 J2。

- 参数与网络：`enable=U3 pin7 ESP_EN,R10 10KΩ to VCC_3V3,C14 100nF to GND,J2 pin4`；`boot=U3 GPIO9 pin15 ESP_BOOT,R11 10KΩ to VCC_3V3,J2 pin5`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页 U3 ESP_EN/ESP_BOOT、R10/R11/C14 与 J2

## 保护电路

### D1 SRV05-4 信号保护

D1 SRV05-4 由 VCC_3V3/GND 供电，其四个 IO 通道连接 TC_SCK、TC_MISO、ESP_SCL、ESP_SDA，为热电偶串行与 Grove I2C 信号提供钳位路径。

- 参数与网络：`part=SRV05-4`；`supply=VCC_3V3`；`ground=GND`；`protected_nets=TC_SCK,TC_MISO,ESP_SCL,ESP_SDA`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页左中 D1 SRV05-4 IO1-IO4 与四路网络

### 热电偶输入抑制网络

T-/T+ 各串联 330R/GZ1005D331TF 铁氧体和 1KΩ 电阻，并以 C11 47nF 跨线滤波；TC1 SH 直接接 GND，图中未显示热电偶端 TVS。

- 参数与网络：`negative_series=FB1 330R + R6 1KΩ`；`positive_series=FB2 330R + R5 1KΩ`；`differential_filter=C11 47nF`；`shield=SH to GND`；`tvs_at_connector_shown=false`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页 U4 至 TC1 输入网络

## 关键网络

### 热电偶到 I2C 主机路径

TC1 T-/T+→FB1/FB2→R6/R5/C11→U4→TC_MISO/TC_SCK/TC_CS→U3→ESP_SDA/ESP_SCL→GROVE，电源路径为 VCC_5V→U1/U2→VCC_3V3/VCC_A3V3。

- 参数与网络：`sensor_path=TC1->input filter->U4`；`converter_bus=U4 TC_MISO/TC_SCK/TC_CS->U3`；`host_path=U3 ESP_SDA/ESP_SCL->GROVE`；`power_path=VCC_5V->U1 VCC_3V3 and U2/FB3 VCC_A3V3`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页完整 TC1/U4/U3/GROVE 与双电源路径

## 内存与 Flash

### 外部存储器

完整原理图未显示外部 Flash、EEPROM、RAM、SD 卡或其他存储器，ESP32-C3 的具体内部存储配置未在页面标注。

- 参数与网络：`external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false`；`internal_capacity_printed=false`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页完整图无外部存储器件

## 射频

### ESP32-C3 LNA_IN

U3 LNA_IN pin1 经 R2 50Ω 接 GND，完整原理图未显示天线、匹配网络或射频连接器。

- 参数与网络：`mcu_pin=U3 LNA_IN pin1`；`termination=R2 50Ω to GND`；`antenna_shown=false`；`matching_network_shown=false`；`rf_connector_shown=false`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页 MCU 区左上 U3 LNA_IN/R2/GND 与完整图

## 调试与烧录

### J2 DL_ESPC3

J2 pin1=VCC_3V3、pin2=ESP_TXD、pin3=ESP_RXD、pin4=ESP_EN、pin5=ESP_BOOT、pin6=GND；ESP_RXD/TXD 连接 U3 GPIO20 pin27/GPIO21 pin28。

- 参数与网络：`pin_1=VCC_3V3`；`pin_2=ESP_TXD`；`pin_3=ESP_RXD`；`pin_4=ESP_EN`；`pin_5=ESP_BOOT`；`pin_6=GND`；`mcu_uart=GPIO20 U0RXD pin27,GPIO21 U0TXD pin28`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页左下 J2 DL_ESPC3 与 U3 ESP_RXD/ESP_TXD

## 模拟电路

### TC1 到 U4 热电偶差分输入

TC1 T- 与 T+ 分别经 FB1/FB2、R6/R5 1KΩ 连接 U4 T- pin2/T+ pin3，C11 47nF 跨接两路形成差分滤波；TC1 SH 接 GND。

- 参数与网络：`negative_path=TC1 T- -> FB1 -> R6 1KΩ -> U4 pin2 T-`；`positive_path=TC1 T+ -> FB2 -> R5 1KΩ -> U4 pin3 T+`；`differential_cap=C11 47nF`；`shield=TC1 SH -> GND`
- 证据：图 73aee450ef05 / 第 1 页 / 第 1 页右侧 U4 T-/T+、R5/R6/C11/FB1/FB2 与 TC1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit KMeter 系统结构 | `controller=U3 ESP32-C3`；`converter=U4 MAX6675/31855`；`thermocouple_connector=TC1 PCC-SMP-K-100-CE`；`host_bus=GROVE I2C`；`mcu_power=U1 MD5333`；`adc_power=U2 HX6306P332` |
| 核心器件 | U3 ESP32-C3 关键引脚 | `GPIO1_pin5=TEMP_Read`；`GPIO3_pin8=ESP_SCL`；`GPIO4_pin9=ESP_SDA`；`GPIO5_pin10=TC_MISO`；`GPIO6_pin12=TC_SCK`；`GPIO7_pin13=TC_CS`；`GPIO9_pin15=ESP_BOOT`；`CHIP_EN_pin7=ESP_EN`；`GPIO20_pin27=ESP_RXD`；`GPIO21_pin28=ESP_TXD` |
| 总线 | ESP32-C3 到 U4 串行接口 | `controller=U3 ESP32-C3`；`device=U4 MAX6675/31855`；`chip_select=GPIO7 pin13 -> TC_CS -> U4 pin6`；`clock=GPIO6 pin12 -> TC_SCK -> U4 pin5`；`data=U4 pin7 TC_MISO -> GPIO5 pin10`；`mosi_shown=false` |
| 模拟电路 | TC1 到 U4 热电偶差分输入 | `negative_path=TC1 T- -> FB1 -> R6 1KΩ -> U4 pin2 T-`；`positive_path=TC1 T+ -> FB2 -> R5 1KΩ -> U4 pin3 T+`；`differential_cap=C11 47nF`；`shield=TC1 SH -> GND` |
| 核心器件 | U4 MAX6675/31855 | `pin_1=GND`；`pin_2=T-`；`pin_3=T+`；`pin_4=VCC_A3V3`；`pin_5=TC_SCK`；`pin_6=TC_CS`；`pin_7=TC_MISO`；`pin_8=NC / page label TC_N` |
| 核心器件 | 热电偶转换器实际型号 | `schematic_label=MAX6675/31855`；`documented_part=MAX31855KASA+T`；`exact_assembly_confirmed=false` |
| 接口 | GROVE I2C 接口 | `IO2=ESP_SCL`；`IO1=ESP_SDA`；`power=VCC_5V`；`ground=GND`；`scl_pullup=R7 10KΩ to VCC_3V3`；`sda_pullup=R8 10KΩ to VCC_3V3` |
| 总线 | 外部主机 I2C | `controller=external host`；`device=U3 ESP32-C3 firmware`；`scl=GROVE IO2 ESP_SCL -> U3 GPIO3 pin8`；`sda=GROVE IO1 ESP_SDA -> U3 GPIO4 pin9`；`pullup_rail=VCC_3V3` |
| 总线地址 | Unit KMeter I2C 地址 | `documented_address=0x66`；`address_width=7-bit`；`endpoint=U3 firmware`；`address_printed_on_schematic=false`；`address_strap_shown=false` |
| 其他事实 | I2C 温度数据协议 | `documented_register=0x66`；`documented_length=4`；`documented_bytes=thermocouple_H,thermocouple_L,internal_H,internal_L`；`thermocouple_scale=0.25C`；`internal_scale=0.0625C`；`protocol_visible_on_schematic=false` |
| 传感器 | K 型热电偶测量规格 | `documented_adc_bits=14`；`documented_resolution=0.25C`；`documented_accuracy=+/-2%`；`documented_range=-200 to 1350C`；`probe_type=K`；`specs_printed_on_schematic=false` |
| 电源 | U1 MD5333 MCU 电源 | `input=VCC_5V at pin3`；`output=VCC_3V3 at pin2`；`ground=pin1 GND`；`input_caps=C1 4.7uF,C2 100nF`；`output_cap=C3 4.7uF` |
| 电源 | U2 HX6306P332 ADC 电源 | `input=VCC_5V at pin3`；`raw_output=U2 pin2`；`filtered_output=VCC_A3V3 via FB3`；`ground=pin1 GND`；`input_caps=C4 4.7uF,C5 100nF`；`pre_bead_caps=C6 4.7uF,C8 100nF`；`post_bead_cap=C7 4.7uF` |
| 电源 | U4 VCC_A3V3 电源 | `vcc=U4 pin4 VCC_A3V3`；`ground=U4 pin1 GND`；`decoupling=100nF and 4.7uF`；`power_partition=U2/FB3 separate from U1 VCC_3V3` |
| 时钟 | ESP32-C3 40MHz 晶体 | `frequency=40M`；`crystal=X1 TXC/8Z400001`；`xtal_p=U3 pin30 via R4 22Ω`；`xtal_n=U3 pin29`；`load_caps=C9 12pF,C10 12pF` |
| 复位 | ESP_EN 与 ESP_BOOT | `enable=U3 pin7 ESP_EN,R10 10KΩ to VCC_3V3,C14 100nF to GND,J2 pin4`；`boot=U3 GPIO9 pin15 ESP_BOOT,R11 10KΩ to VCC_3V3,J2 pin5` |
| 调试与烧录 | J2 DL_ESPC3 | `pin_1=VCC_3V3`；`pin_2=ESP_TXD`；`pin_3=ESP_RXD`；`pin_4=ESP_EN`；`pin_5=ESP_BOOT`；`pin_6=GND`；`mcu_uart=GPIO20 U0RXD pin27,GPIO21 U0TXD pin28` |
| GPIO 与控制信号 | LED1/LED2 指示灯 | `power_led=VCC_3V3 -> LED1 white -> R1 22KΩ -> GND`；`temp_led=TEMP_Read -> LED2 red -> R9 10KΩ -> GND`；`temp_net=U3 GPIO1 pin5` |
| 保护电路 | D1 SRV05-4 信号保护 | `part=SRV05-4`；`supply=VCC_3V3`；`ground=GND`；`protected_nets=TC_SCK,TC_MISO,ESP_SCL,ESP_SDA` |
| 保护电路 | 热电偶输入抑制网络 | `negative_series=FB1 330R + R6 1KΩ`；`positive_series=FB2 330R + R5 1KΩ`；`differential_filter=C11 47nF`；`shield=SH to GND`；`tvs_at_connector_shown=false` |
| 射频 | ESP32-C3 LNA_IN | `mcu_pin=U3 LNA_IN pin1`；`termination=R2 50Ω to GND`；`antenna_shown=false`；`matching_network_shown=false`；`rf_connector_shown=false` |
| 关键网络 | 热电偶到 I2C 主机路径 | `sensor_path=TC1->input filter->U4`；`converter_bus=U4 TC_MISO/TC_SCK/TC_CS->U3`；`host_path=U3 ESP_SDA/ESP_SCL->GROVE`；`power_path=VCC_5V->U1 VCC_3V3 and U2/FB3 VCC_A3V3` |
| 内存与 Flash | 外部存储器 | `external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false`；`internal_capacity_printed=false` |

## 待确认事项

- `component.converter-identity`：原理图 U4 标为通用 MAX6675/31855，而产品正文指定 MAX31855KASA+T；需由 BOM 或实物丝印确认 v1.0/v当前装配型号。（证据：图 73aee450ef05 / 第 1 页 / 第 1 页 U4 标注 MAX6675/31855）
- `address.documented-0x66`：产品正文列出 7 位 I2C 地址 0x66；原理图只显示 I2C 进入 U3 ESP32-C3，没有打印固件地址或地址绑带，因此需通过固件或总线扫描确认。（证据：图 73aee450ef05 / 第 1 页 / 第 1 页 GROVE I2C 至 U3，页面无地址标注）
- `other.documented-i2c-protocol`：产品正文描述寄存器 0x66 返回 thermocouple_H/L 与 internal_H/L 四字节并使用 0.25/0.0625 缩放；原理图无法确认寄存器、字节顺序或固件换算。（证据：图 73aee450ef05 / 第 1 页 / 第 1 页 U3/U4/GROVE 硬件路径，无寄存器协议标注）
- `sensor.documented-measurement-specs`：产品正文列出 14-bit、0.25°C 分辨率、±2% 精度和 -200~1350°C 支持范围；原理图只显示转换器兼容标签与 K 型插座，未打印这些性能参数。（证据：图 73aee450ef05 / 第 1 页 / 第 1 页 U4 MAX6675/31855 与 TC1 PCC-SMP-K-100-CE）
- `review.converter-identity`：请依据 BOM 或实物丝印确认 U4 实际装配为 MAX31855KASA+T，而不是通用图纸中的其他 MAX6675/31855 兼容项。；原因：原理图使用 MAX6675/31855 通用标签，正文指定具体 MAX31855KASA+T。
- `review.i2c-address`：请依据 Unit KMeter 固件或 I2C 扫描确认 7 位地址 0x66。；原因：原理图未打印 ESP32-C3 固件地址。
- `review.i2c-protocol`：请依据固件源码或协议实测确认寄存器 0x66、四字节顺序及 0.25/0.0625 温度缩放。；原因：固件寄存器协议无法由原理图确认。
- `review.measurement-specs`：请依据实际 U4 数据手册和探头规格确认 14-bit、0.25°C、±2% 与 -200~1350°C 参数。；原因：这些性能参数未打印在原理图，且取决于 U4 实际型号和探头。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `73aee450ef059b68b8d67048f63097b6a6c902ea49db5fa0ff50b3ccb6d8691f` | `https://static-cdn.m5stack.com/resource/docs/products/unit/kmeter/kmeter_sch_01.webp` |

---

源文档：`zh_CN/unit/kmeter.md`

源文档 SHA-256：`69e25ce2adce32008ebd10b214a593e45dd060b51258b2d56c0293a196a960a0`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
