# Module GNSS 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module GNSS |
| SKU | M135 |
| 产品 ID | `module-gnss-409f80dbfd81` |
| 源文档 | `zh_CN/module/GNSS Module.md` |

## 概述

Module GNSS 以 U1 NEO-M9N-00B 提供定位、UART 和 PPS，SW1/SW2/SW3 分别选择 TXD、RXD 和 PPS 的 M5-Bus GPIO。主 I2C 总线连接 U2 M24C32 EEPROM、U3 BMI270 与 U5 BMP280，U4 BMM150 则连接 BMI270 的 ASDX/ASCX 辅助总线。GNSS 使用 J1 IPEX 射频接口，V_BCKP 由 3.3 V 经 D1 和 0.22 F 备份电容供电；模块还预留 Stamp.COMX UART 焊盘。

## 检索关键词

`Module GNSS`、`M135`、`NEO-M9N-00B`、`BMI270`、`BMM150`、`BMP280`、`M24C32`、`I2C`、`UART`、`PPS`、`TIMEPULSE`、`M5-TXD`、`M5-RXD`、`GPIO17`、`GPIO15`、`GPIO12`、`GPIO0`、`GPIO16`、`GPIO13`、`GPIO34`、`GPIO35`、`SDA`、`SCL`、`BMM_SDA`、`BMM_SCL`、`ASDX`、`ASCX`、`V_BCKP`、`0.22F`、`ANT_IPEX`、`SW1`、`SW2`、`SW3`、`SW4`、`0x69`、`0x10`、`0x76`、`38400bps`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | NEO-M9N-00B | GNSS 接收模组，提供 UART、TIMEPULSE/PPS、I2C/SPI 与射频接口 | 图 49901c901f34 / 第 1 页 / A2-B3，U1 NEO-M9N-00B pins1-24 |
| U2 | M24C32 | 主 I2C 总线 EEPROM，地址脚与 WP 固定接地 | 图 49901c901f34 / 第 1 页 / A1，U2 M24C32 与 R1/R2/C1 |
| U3 | BMI270 | 主 I2C 六轴 IMU，并作为 BMM150 辅助 I2C 控制器 | 图 49901c901f34 / 第 1 页 / B1-C2，U3 BMI270，SDA/SCL、ASDX/ASCX、SDO/CSB |
| U4 | BMM150 | 连接 BMI270 BMM_SDA/BMM_SCL 辅助总线的三轴磁传感器 | 图 49901c901f34 / 第 1 页 / B2-C3，U4 BMM150 与 BMM_SDA/BMM_SCL |
| U5 | BMP280 | 主 I2C 气压传感器，CSB 上拉、SDO 接地 | 图 49901c901f34 / 第 1 页 / D1-D2，U5 BMP280 |
| J1 | IPEX | NEO-M9N RF_IN 的有源天线接口 | 图 49901c901f34 / 第 1 页 / A3，J1 IPEX、RF_IN/VCC_RF/R3/C2 |
| J2 | M5Stack_BUS | 30 针主机总线，提供电源、I2C 与可切换 UART/PPS GPIO | 图 49901c901f34 / 第 1 页 / B3-C4，J2 M5Stack_BUS pins1-30 |
| SW1/SW2/SW3 | multi-position switch | 分别选择 NEO TXD、NEO RXD 与 PPS 的主机 GPIO | 图 49901c901f34 / 第 1 页 / A4，SW1 M5-TXD、SW2 M5-RXD、SW3 PPS |
| SW4 | SW-PWR | BMI270 SDO 地址选择，连接 3.3 V 或 R4 4.7 kΩ 下拉 | 图 49901c901f34 / 第 1 页 / B1，SW4/R4 与 U3 SDO |
| D1/C6 | 1N4148WS T4 / 0.22F 3.3V | GNSS V_BCKP 备份供电隔离与储能 | 图 49901c901f34 / 第 1 页 / A1-B2，+3.3V-D1-V_BCKP 与 C6 0.22F/3.3V |
| JP1-JP4 | DEBUG PAD | 可选 Stamp.COMX TXD/RXD GPIO16/13/17/15 焊盘 | 图 49901c901f34 / 第 1 页 / D4，OPTIONAL STAMP.COMX JP1-JP4 |

## 系统结构

### GNSS 多传感器架构

U1 NEO-M9N-00B 通过可切换 UART/PPS 连接 M5-Bus；主 I2C 总线连接 U1、M24C32、BMI270 和 BMP280，BMM150 挂在 BMI270 辅助总线上。

- 参数与网络：`gnss=U1 NEO-M9N-00B`；`main_i2c=U1/U2 M24C32/U3 BMI270/U5 BMP280`；`aux_i2c=U3 ASDX/ASCX -> U4 BMM150`；`host=J2 M5Stack_BUS`；`uart_switches=SW1/SW2`；`pps_switch=SW3`
- 证据：图 49901c901f34 / 第 1 页 / 整页 GNSS、传感器、开关与 M5-Bus

## 电源

### GNSS 备份电源

U1 V_BCKP pin22 由 +3.3 V 经 D1 1N4148WS T4 隔离供电，并配置 C3 100 nF 与 C6 0.22 F/3.3 V 储能。

- 参数与网络：`pin=U1 pin22 V_BCKP`；`source=+3.3V`；`diode=D1 1N4148WS T4`；`capacitors=C3 100nF; C6 0.22F/3.3V`
- 证据：图 49901c901f34 / 第 1 页 / A1-B2 D1/C3/C6/V_BCKP

## 总线

### NEO-M9N UART

U1 TXD pin20 连接 M5-RXD，U1 RXD pin21 连接 M5-TXD；SW1 将 M5-TXD 选择到 GPIO17/GPIO15/GPIO12/GPIO0，SW2 将 M5-RXD 选择到 GPIO16/GPIO13/GPIO34/GPIO35。

- 参数与网络：`module_tx=U1 pin20 TXD -> M5-RXD`；`module_rx=U1 pin21 RXD <- M5-TXD`；`host_tx_options=GPIO17/GPIO15/GPIO12/GPIO0`；`host_rx_options=GPIO16/GPIO13/GPIO34/GPIO35`；`switch_tx=SW1`；`switch_rx=SW2`
- 证据：图 49901c901f34 / 第 1 页 / U1 pins20/21 与 SW1/SW2

### 主 I2C 总线

SDA/SCL 由 R2/R1 各 4.7 kΩ 上拉到 3.3 V，连接 U1 pins18/19、U2 pins5/6、U3 pins14/13、U5 pins3/4，并接 J2 pins17/18。

- 参数与网络：`controller=external M5Stack host`；`sda=J2 pin17`；`scl=J2 pin18`；`pullups=R2 SDA 4.7KΩ; R1 SCL 4.7KΩ`；`devices=U1/U2/U3/U5`；`level=3.3V`
- 证据：图 49901c901f34 / 第 1 页 / SDA/SCL horizontal bus、R1/R2、U1/U2/U3/U5/J2

### BMM150 辅助 I2C

BMI270 ASDX pin2 与 ASCX pin3 分别连接 BMM_SDA/BMM_SCL，再连接 BMM150 SDI B4/SCK A3；该总线未直接接 J2 主机 I2C。

- 参数与网络：`controller=U3 BMI270`；`device=U4 BMM150`；`sda=U3 ASDX pin2 -> BMM_SDA -> U4 B4 SDI`；`scl=U3 ASCX pin3 -> BMM_SCL -> U4 A3 SCK`；`host_direct=false`
- 证据：图 49901c901f34 / 第 1 页 / U3 ASDX/ASCX 与 U4 BMM_SDA/BMM_SCL

## GPIO 与控制信号

### PPS/TIMEPULSE 路由

U1 TIMEPULSE pin3 标为 PPS，SW3 可将 PPS 选择连接 GPIO0、GPIO35 或 GPIO34。

- 参数与网络：`source=U1 pin3 TIMEPULSE`；`net=PPS`；`switch=SW3`；`options=GPIO0/GPIO35/GPIO34`；`direction=output from GNSS`
- 证据：图 49901c901f34 / 第 1 页 / U1 TIMEPULSE/PPS 与 SW3

## 存储

### M24C32 EEPROM

U2 M24C32 的 A0/A1/A2 与 GND 接地，WP 接地，VCC 接 3.3 V，SDA/SCL 接主 I2C，总线旁有 C1 100 nF 去耦。

- 参数与网络：`reference=U2`；`part_number=M24C32`；`address_pins=A0/A1/A2 GND`；`write_protect=WP GND`；`supply=3.3V`；`decoupling=C1 100nF`
- 证据：图 49901c901f34 / 第 1 页 / A1 U2 M24C32

## 传感器

### BMI270 配置

U3 BMI270 的 VDD/VDDIO/CSB 接 3.3 V，GNDIO/GND 接地，SDA/SCL 接主 I2C；SW4 选择 SDO 高电平或由 R4 4.7 kΩ 下拉。

- 参数与网络：`reference=U3`；`part_number=BMI270`；`supply=3.3V`；`interface=I2C`；`csb=3.3V`；`sdo_select=SW4 3.3V or R4 4.7KΩ to GND`；`decoupling=C7/C8 100nF`
- 证据：图 49901c901f34 / 第 1 页 / B1-C2 U3 BMI270/SW4/R4/C7/C8

### BMM150 配置

U4 BMM150 的 PS/VDDIO/VDD 接 3.3 V，CSB 与 SDO 接 GND，SDI/SCK 接 BMI270 辅助总线；INT/DRDY 未连接。

- 参数与网络：`reference=U4`；`part_number=BMM150`；`supply=3.3V`；`csb=GND`；`sdo=GND`；`bus=BMM_SDA/BMM_SCL`；`interrupt=INT/DRDY NC`；`decoupling=C9/C10 100nF`
- 证据：图 49901c901f34 / 第 1 页 / B2-C3 U4 BMM150

### BMP280 配置

U5 BMP280 的 VDD/VDDIO/CSB 接 3.3 V，SDO 与 GND pins1/7 接地，SCK/SDI 接主 SCL/SDA，C11 100 nF 去耦。

- 参数与网络：`reference=U5`；`part_number=BMP280`；`supply=3.3V`；`csb=3.3V`；`sdo=GND`；`scl=pin4`；`sda=pin3`；`decoupling=C11 100nF`
- 证据：图 49901c901f34 / 第 1 页 / D1-D2 U5 BMP280

## 射频

### GNSS 天线接口

U1 RF_IN pin11 连接 J1 IPEX；VCC_RF pin9 经 R3 10 Ω 注入天线节点，C2 10 nF 对地，J1 外壳/回路接 GND。

- 参数与网络：`rf_pin=U1 pin11 RF_IN`；`connector=J1 IPEX`；`active_bias=U1 pin9 VCC_RF via R3 10Ω`；`filter=C2 10nF`；`external_marker=J3 Ex-ANT/ANT`
- 证据：图 49901c901f34 / 第 1 页 / A3-B3 U1 RF_IN/VCC_RF/R3/C2/J1/J3

## 调试与烧录

### Stamp.COMX 可选 UART 焊盘

OPTIONAL STAMP.COMX 区将 TXD 引到 JP1 GPIO16 或 JP2 GPIO13，将 RXD 引到 JP3 GPIO17 或 JP4 GPIO15。

- 参数与网络：`tx_options=JP1 GPIO16; JP2 GPIO13`；`rx_options=JP3 GPIO17; JP4 GPIO15`；`population=optional debug pads`
- 证据：图 49901c901f34 / 第 1 页 / D4 OPTIONAL STAMP.COMX

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | GNSS 多传感器架构 | `gnss=U1 NEO-M9N-00B`；`main_i2c=U1/U2 M24C32/U3 BMI270/U5 BMP280`；`aux_i2c=U3 ASDX/ASCX -> U4 BMM150`；`host=J2 M5Stack_BUS`；`uart_switches=SW1/SW2`；`pps_switch=SW3` |
| 总线 | NEO-M9N UART | `module_tx=U1 pin20 TXD -> M5-RXD`；`module_rx=U1 pin21 RXD <- M5-TXD`；`host_tx_options=GPIO17/GPIO15/GPIO12/GPIO0`；`host_rx_options=GPIO16/GPIO13/GPIO34/GPIO35`；`switch_tx=SW1`；`switch_rx=SW2` |
| GPIO 与控制信号 | PPS/TIMEPULSE 路由 | `source=U1 pin3 TIMEPULSE`；`net=PPS`；`switch=SW3`；`options=GPIO0/GPIO35/GPIO34`；`direction=output from GNSS` |
| 总线 | 主 I2C 总线 | `controller=external M5Stack host`；`sda=J2 pin17`；`scl=J2 pin18`；`pullups=R2 SDA 4.7KΩ; R1 SCL 4.7KΩ`；`devices=U1/U2/U3/U5`；`level=3.3V` |
| 总线 | BMM150 辅助 I2C | `controller=U3 BMI270`；`device=U4 BMM150`；`sda=U3 ASDX pin2 -> BMM_SDA -> U4 B4 SDI`；`scl=U3 ASCX pin3 -> BMM_SCL -> U4 A3 SCK`；`host_direct=false` |
| 存储 | M24C32 EEPROM | `reference=U2`；`part_number=M24C32`；`address_pins=A0/A1/A2 GND`；`write_protect=WP GND`；`supply=3.3V`；`decoupling=C1 100nF` |
| 传感器 | BMI270 配置 | `reference=U3`；`part_number=BMI270`；`supply=3.3V`；`interface=I2C`；`csb=3.3V`；`sdo_select=SW4 3.3V or R4 4.7KΩ to GND`；`decoupling=C7/C8 100nF` |
| 传感器 | BMM150 配置 | `reference=U4`；`part_number=BMM150`；`supply=3.3V`；`csb=GND`；`sdo=GND`；`bus=BMM_SDA/BMM_SCL`；`interrupt=INT/DRDY NC`；`decoupling=C9/C10 100nF` |
| 传感器 | BMP280 配置 | `reference=U5`；`part_number=BMP280`；`supply=3.3V`；`csb=3.3V`；`sdo=GND`；`scl=pin4`；`sda=pin3`；`decoupling=C11 100nF` |
| 射频 | GNSS 天线接口 | `rf_pin=U1 pin11 RF_IN`；`connector=J1 IPEX`；`active_bias=U1 pin9 VCC_RF via R3 10Ω`；`filter=C2 10nF`；`external_marker=J3 Ex-ANT/ANT` |
| 电源 | GNSS 备份电源 | `pin=U1 pin22 V_BCKP`；`source=+3.3V`；`diode=D1 1N4148WS T4`；`capacitors=C3 100nF; C6 0.22F/3.3V` |
| 调试与烧录 | Stamp.COMX 可选 UART 焊盘 | `tx_options=JP1 GPIO16; JP2 GPIO13`；`rx_options=JP3 GPIO17; JP4 GPIO15`；`population=optional debug pads` |
| 总线地址 | 传感器与 EEPROM I2C 地址 | `claimed_bmi270=0x69`；`claimed_bmm150=0x10`；`claimed_bmp280=0x76`；`m24c32=not printed`；`schematic=strap levels only` |
| 总线 | GNSS UART 默认参数 | `claimed_baud=38400bps`；`claimed_frame=8N1`；`schematic=TXD/RXD only` |
| 射频 | GNSS 系统与定位性能 | `claimed_systems=GPS/QZSS/GLONASS/Galileo/BeiDou`；`claimed_accuracy=1.5m`；`claimed_channels=92`；`claimed_update_rate=25Hz`；`claimed_heading_accuracy=0.3deg` |
| 传感器 | IMU、磁场和气压量程 | `claimed_accel=±2g/±4g/±8g/±16g`；`claimed_gyro=±125/250/500/1000/2000dps`；`claimed_magnetic_resolution=0.3uT`；`claimed_pressure=300-1100hPa` |

## 待确认事项

- `address.i2c-devices`：产品正文给出 BMI270 0x69、BMM150 0x10、BMP280 0x76，但原理图只显示地址选择电平/开关，未印地址表；M24C32 地址也未直接标注。（证据：图 49901c901f34 / 第 1 页 / U2/U3/SW4/U4/U5 address strap circuits）
- `bus.uart-settings`：产品正文称默认 38400 bps 8N1，但原理图仅显示 TXD/RXD 路由，没有印出波特率和帧格式。（证据：图 49901c901f34 / 第 1 页 / U1 TXD/RXD 与 SW1/SW2）
- `rf.gnss-performance`：产品正文列出 GPS/QZSS、GLONASS、Galileo、BeiDou、1.5 m、92 通道和 25 Hz 等性能，但这些指标未印在原理图。（证据：图 49901c901f34 / 第 1 页 / U1 NEO-M9N-00B block lacks performance table）
- `sensor.performance`：产品正文列出 BMI270 加速度/陀螺量程、BMM150 0.3 µT 分辨率及 BMP280 300-1100 hPa 范围，但原理图未标这些性能参数。（证据：图 49901c901f34 / 第 1 页 / U3/U4/U5 circuits lack performance values）
- `review.i2c-addresses`：请用各器件 datasheet 和 SW4 默认档位复核 BMI270/BMM150/BMP280/M24C32 地址。；原因：原理图未印地址表，BMI270 地址还可切换。
- `review.uart-settings`：请用 NEO-M9N 配置或固件确认默认 UART 为 38400 bps 8N1。；原因：串口参数未印在原理图。
- `review.gnss-performance`：请用 NEO-M9N-00B datasheet 与模块配置复核支持星座、精度、通道数和更新率。；原因：这些性能指标不在原理图中。
- `review.sensor-performance`：请用 BMI270/BMM150/BMP280 datasheet 复核量程、分辨率和压力范围。；原因：性能参数未印在原理图中。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `49901c901f347dc1691a126d20cd2543d6aa135e7df333ef29f1bbe63b719008` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/561/SCH_Module_GNSS_V1.0_sch_01.png` |

---

源文档：`zh_CN/module/GNSS Module.md`

源文档 SHA-256：`df3c0bf77e38207c65575b19b8fea0e1498d92a0d0d9ac4bdf79a2090fefa82a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
