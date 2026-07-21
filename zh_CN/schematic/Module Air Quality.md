# Module Air Quality 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module Air Quality |
| SKU | M134 |
| 产品 ID | `module-air-quality-692ca7671c88` |
| 源文档 | `zh_CN/module/PM2.5 AIR QUALITY KIT (Excluding Core).md` |

## 概述

Module Air Quality 是由主机驱动的传感器扩展板，原理图没有本地主控：J2 M5Stack_BUS 直接连接 U1 PM2.5PORT 的 UART/RESET/SET，并通过 I2C 连接 U2 SHT20。J1 BUS_8P 同时引出 +5V、+3V3、GND、I2C 和 SPI，J3 USB-C 仅把 VBUS 接入 +5V 电源网。SHT20 的 MSDA/MSCL 各由 4.7K 上拉到 +3V3，颗粒物端口由 +5V 供电且信号直接连接 M5-Bus，图中未画电平转换或接口保护。正文所述 PMSA003 具体装配、SHT20 地址和 PM2.5PORT 信号电平未由本页明确标注，需结合 BOM、传感器资料或实板确认。

## 检索关键词

`Module Air Quality`、`M134`、`PM2.5PORT`、`PMSA003`、`SHT20`、`M5Stack_BUS`、`BUS_8P`、`USB-C`、`MSDA`、`MSCL`、`MMOSI`、`MMISO`、`MSCK`、`MRX`、`MTX`、`MRST`、`MSET`、`GPIO16`、`GPIO17`、`GPIO21`、`GPIO22`、`GPIO23`、`GPIO19`、`GPIO18`、`GPIO13`、`EN`、`I2C`、`SPI`、`UART`、`+5V`、`+3V3`、`R1 4.7K`、`R2 4.7K`、`C1 100nF`、`PM2.5`、`temperature humidity`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | PM2.5PORT | 十针颗粒物传感器接口，提供双 +5V、双 GND、RESET、RX、TX 和 SET | 图 d8b3f2036f8a / 第 1 页 / 第 1 页 A3-B3 U1 PM2.5PORT |
| U2 | SHT20 | 连接 MSDA/MSCL 的板载温湿度传感器 | 图 d8b3f2036f8a / 第 1 页 / 第 1 页 C1-C2 U2 SHT20 |
| J2 | M5Stack_BUS | 主机堆叠接口，连接颗粒物 UART/控制、SHT20 I2C、SPI 和电源 | 图 d8b3f2036f8a / 第 1 页 / 第 1 页 C3-C4 J2 M5Stack_BUS |
| J1 | BUS_8P | 八针扩展口，引出 +5V、+3V3、GND、I2C 和 SPI | 图 d8b3f2036f8a / 第 1 页 / 第 1 页 B1-B2 J1 BUS_8P |
| J3 | USB-C | 仅连接 VBUS 和 GND 的 +5V 电源输入连接器 | 图 d8b3f2036f8a / 第 1 页 / 第 1 页 A1-A2 J3 USB-C |
| R1/R2 | 4.7KΩ | MSDA/MSCL 到 +3V3 的 I2C 上拉电阻 | 图 d8b3f2036f8a / 第 1 页 / 第 1 页 C1-C2 R1/R2 4.7KΩ |
| C1 | 100nF | U2 SHT20 的 +3V3 电源去耦电容 | 图 d8b3f2036f8a / 第 1 页 / 第 1 页 C2 C1 100nF |

## 系统结构

### Module Air Quality

板上没有本地主控；J2 M5Stack_BUS 将主机 UART 和控制信号送到 U1 PM2.5PORT，将 I2C 送到 U2 SHT20，并把 I2C/SPI/电源透传到 J1 BUS_8P。

- 参数与网络：`local_mcu_shown=false`；`particle_interface=U1 PM2.5PORT`；`humidity_sensor=U2 SHT20`；`host=J2 M5Stack_BUS`；`extension=J1 BUS_8P`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页完整功能分区

## 电源

### +5V/+3V3 电源

+5V 网连接 J3 VBUS、J2.28、J1.1 和 U1.1/U1.2；+3V3 网连接 J2.12、J1.2、U2、R1/R2 与 C1。原理图未显示 DC/DC、LDO、负载开关、充电器或电池路径。

- 参数与网络：`5v_nodes=J3 VBUS,J2.28,J1.1,U1.1,U1.2`；`3v3_nodes=J2.12,J1.2,U2,R1,R2,C1`；`converter_shown=false`；`ldo_shown=false`；`load_switch_shown=false`；`charger_shown=false`；`battery_path_shown=false`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页全部 +5V/+3V3 网络

## 接口

### J1 BUS_8P

J1 针脚为 1=+5V、2=+3V3、3=GND、4=MSDA/SDA、5=MSCL/SCL、6=MMOSI/MOSI、7=MMISO/MISO、8=MSCK/SCK。

- 参数与网络：`pin_1=+5V`；`pin_2=+3V3`；`pin_3=GND`；`pin_4=MSDA SDA`；`pin_5=MSCL SCL`；`pin_6=MMOSI MOSI`；`pin_7=MMISO MISO`；`pin_8=MSCK SCK`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 B1-B2 J1 BUS_8P

### J2 M5Stack_BUS

本板使用 J2.1/.3/.5 GND、.6 EN/MRST、.7 GPIO23/MMOSI、.9 GPIO19/MMISO、.11 GPIO18/MSCK、.12 +3V3、.15 GPIO16/MRX、.16 GPIO17/MTX、.17 GPIO21/MSDA、.18 GPIO22/MSCL、.22 GPIO13/MSET、.28 +5V。

- 参数与网络：`ground=1,3,5`；`reset=6 EN/MRST`；`spi=7 GPIO23 MMOSI,9 GPIO19 MMISO,11 GPIO18 MSCK`；`3v3=12`；`uart=15 GPIO16 MRX,16 GPIO17 MTX`；`i2c=17 GPIO21 MSDA,18 GPIO22 MSCL`；`set=22 GPIO13 MSET`；`5v=28`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 C3-C4 J2 外部网络

### J3 USB-C

J3 只连接 VBUS 到 +5V、多个 GND 到 GND；原理图未画 D+/D-、CC1/CC2 或 USB 数据网络。

- 参数与网络：`role=power input`；`vbus=+5V`；`ground=GND`；`usb_data_shown=false`；`cc_resistors_shown=false`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 A1-A2 J3 USB-C

## 总线

### MSDA/MSCL I2C

J2.17 GPIO21 连接 MSDA，J2.18 GPIO22 连接 MSCL；两网同时连接 J1.4/J1.5 和 U2，R1/R2 各 4.7K 上拉至 +3V3。

- 参数与网络：`controller_sda=J2.17 GPIO21`；`controller_scl=J2.18 GPIO22`；`sensor=U2 SHT20`；`extension=J1.4 MSDA,J1.5 MSCL`；`pullups=R1/R2 4.7KΩ`；`rail=+3V3`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 B1-C4 MSDA/MSCL 全路径

### 颗粒物传感器 UART

J2.16 GPIO17 的 MTX 直接连接 U1.7 RX，J2.15 GPIO16 的 MRX 直接连接 U1.9 TX，构成主机与颗粒物传感器的交叉 UART。

- 参数与网络：`host_tx=J2.16 GPIO17 MTX -> U1.7 RX`；`sensor_tx=U1.9 TX MRX -> J2.15 GPIO16`；`series_resistors_shown=false`；`level_shifter_shown=false`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 A3-C4 MTX/MRX 网络

### MMOSI/MMISO/MSCK SPI

SPI 仅在 J2 与 J1 之间透传：J2.7 GPIO23/MMOSI 到 J1.6 MOSI，J2.9 GPIO19/MMISO 到 J1.7 MISO，J2.11 GPIO18/MSCK 到 J1.8 SCK；本页没有板载 SPI 设备或片选网络。

- 参数与网络：`mosi=J2.7 GPIO23 MMOSI -> J1.6`；`miso=J2.9 GPIO19 MMISO -> J1.7`；`sck=J2.11 GPIO18 MSCK -> J1.8`；`chip_select_shown=false`；`onboard_spi_device_shown=false`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 B1-C4 MMOSI/MMISO/MSCK

## GPIO 与控制信号

### MSET

J2.22 GPIO13 的 MSET 网络直接连接 U1.10 SET，原理图未画上拉、下拉或缓冲。

- 参数与网络：`host_pin=J2.22 GPIO13`；`net=MSET`；`device_pin=U1.10 SET`；`conditioning_shown=false`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 A3-C4 MSET

## 时钟

### 外部时钟

完整原理图页没有晶振、振荡器或时钟网络；板上器件不需要由本板提供可见的独立时钟源。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页完整图无时钟器件

## 复位

### MRST

J2.6 EN 网络标为 MRST，并直接连接 U1.5 RESET；原理图未画上拉、下拉、缓冲或 RC。

- 参数与网络：`host_pin=J2.6 EN`；`net=MRST`；`device_pin=U1.5 RESET`；`conditioning_shown=false`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 A3-C4 MRST

## 保护电路

### 外部接口保护

J3、J1 和 U1 外部接口周围未画 TVS/ESD 阵列、保险丝、反接保护或过流保护；PM UART/RESET/SET 也未画串联限流或钳位器件。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_protection_shown=false`；`overcurrent_protection_shown=false`；`pm_signal_series_resistors_shown=false`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 J1/J3/U1 外部接口完整网络

## 内存与 Flash

### 外部存储器

完整原理图页未展示 Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页完整图无存储器

## 传感器

### U2 SHT20

U2 在原理图中明确标为 SHT20，SDA 接 MSDA、SCL 接 MSCL，电源接 +3V3/GND。

- 参数与网络：`reference=U2`；`part_number=SHT20`；`sda=MSDA`；`scl=MSCL`；`supply=+3V3`；`ground=GND`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 C1-C2 U2 SHT20

### U1 PM2.5PORT

U1 是十针颗粒物传感器端口：1/2=+5V，3/4=GND，5=RESET/MRST，7=RX/MTX，9=TX/MRX，10=SET/MSET，6/8 标 NC。

- 参数与网络：`pin_1=+5V VCC`；`pin_2=+5V VCC`；`pin_3=GND`；`pin_4=GND`；`pin_5=RESET MRST`；`pin_6=NC`；`pin_7=RX MTX`；`pin_8=NC`；`pin_9=TX MRX`；`pin_10=SET MSET`
- 证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 A3-B3 U1 PM2.5PORT 针脚

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module Air Quality | `local_mcu_shown=false`；`particle_interface=U1 PM2.5PORT`；`humidity_sensor=U2 SHT20`；`host=J2 M5Stack_BUS`；`extension=J1 BUS_8P` |
| 传感器 | U2 SHT20 | `reference=U2`；`part_number=SHT20`；`sda=MSDA`；`scl=MSCL`；`supply=+3V3`；`ground=GND` |
| 总线 | MSDA/MSCL I2C | `controller_sda=J2.17 GPIO21`；`controller_scl=J2.18 GPIO22`；`sensor=U2 SHT20`；`extension=J1.4 MSDA,J1.5 MSCL`；`pullups=R1/R2 4.7KΩ`；`rail=+3V3` |
| 总线地址 | U2 I2C 地址 | `device=U2 SHT20`；`address_on_schematic=null`；`address_select_pins_shown=false` |
| 传感器 | U1 PM2.5PORT | `pin_1=+5V VCC`；`pin_2=+5V VCC`；`pin_3=GND`；`pin_4=GND`；`pin_5=RESET MRST`；`pin_6=NC`；`pin_7=RX MTX`；`pin_8=NC`；`pin_9=TX MRX`；`pin_10=SET MSET` |
| 总线 | 颗粒物传感器 UART | `host_tx=J2.16 GPIO17 MTX -> U1.7 RX`；`sensor_tx=U1.9 TX MRX -> J2.15 GPIO16`；`series_resistors_shown=false`；`level_shifter_shown=false` |
| 复位 | MRST | `host_pin=J2.6 EN`；`net=MRST`；`device_pin=U1.5 RESET`；`conditioning_shown=false` |
| GPIO 与控制信号 | MSET | `host_pin=J2.22 GPIO13`；`net=MSET`；`device_pin=U1.10 SET`；`conditioning_shown=false` |
| 总线 | MMOSI/MMISO/MSCK SPI | `mosi=J2.7 GPIO23 MMOSI -> J1.6`；`miso=J2.9 GPIO19 MMISO -> J1.7`；`sck=J2.11 GPIO18 MSCK -> J1.8`；`chip_select_shown=false`；`onboard_spi_device_shown=false` |
| 接口 | J1 BUS_8P | `pin_1=+5V`；`pin_2=+3V3`；`pin_3=GND`；`pin_4=MSDA SDA`；`pin_5=MSCL SCL`；`pin_6=MMOSI MOSI`；`pin_7=MMISO MISO`；`pin_8=MSCK SCK` |
| 接口 | J2 M5Stack_BUS | `ground=1,3,5`；`reset=6 EN/MRST`；`spi=7 GPIO23 MMOSI,9 GPIO19 MMISO,11 GPIO18 MSCK`；`3v3=12`；`uart=15 GPIO16 MRX,16 GPIO17 MTX`；`i2c=17 GPIO21 MSDA,18 GPIO22 MSCL`；`set=22 GPIO13 MSET`；`5v=28` |
| 接口 | J3 USB-C | `role=power input`；`vbus=+5V`；`ground=GND`；`usb_data_shown=false`；`cc_resistors_shown=false` |
| 电源 | +5V/+3V3 电源 | `5v_nodes=J3 VBUS,J2.28,J1.1,U1.1,U1.2`；`3v3_nodes=J2.12,J1.2,U2,R1,R2,C1`；`converter_shown=false`；`ldo_shown=false`；`load_switch_shown=false`；`charger_shown=false`；`battery_path_shown=false` |
| 保护电路 | 外部接口保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_protection_shown=false`；`overcurrent_protection_shown=false`；`pm_signal_series_resistors_shown=false` |
| 接口 | PM2.5PORT 逻辑电平 | `sensor_supply=+5V`；`signal_nets=MRX,MTX,MRST,MSET`；`level_shifter_shown=false`；`logic_level=null` |
| 传感器 | 正文中的 PMSA003 | `documented_sensor=PMSA003`；`schematic_designator=U1 PM2.5PORT`；`part_number_on_schematic=null` |
| 时钟 | 外部时钟 | `crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false` |
| 内存与 Flash | 外部存储器 | `flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_shown=false` |

## 待确认事项

- `address.sht20-not-shown`：原理图标出 U2 SHT20 和 MSDA/MSCL，但没有标注其 I2C 地址或地址配置网络。（证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 C1-C2 U2 I2C 网络无地址标注）
- `interface.pm-signal-level`：U1 由 +5V 供电且 MRX/MTX/MRST/MSET 直接连接 M5-Bus，但原理图未标这些信号的逻辑高电平范围，无法从该页确认与主机 GPIO 的电平兼容边界。（证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 U1 与 J2 直接连接且无电平标注）
- `sensor.documented-pmsa003`：产品正文指定 PMSA003 颗粒物传感器，但本页仅把 U1 标为通用 PM2.5PORT，未写出 PMSA003 料号，具体装配型号不能由该页独立确认。（证据：图 d8b3f2036f8a / 第 1 页 / 第 1 页 A3-B3 U1 仅标 PM2.5PORT）
- `review.sht20-address`：请依据 U2 实际器件资料或实板扫描确认 SHT20 的 I2C 地址。；原因：原理图未标地址或地址选择网络。
- `review.pm-signal-level`：请依据颗粒物传感器 datasheet 或实板测量确认 MRX/MTX/MRST/MSET 的逻辑电平范围。；原因：5V 供电的 PM2.5PORT 与 M5-Bus GPIO 直连，图中没有电平标注或转换器。
- `review.pmsa003-population`：请依据 M134 BOM、装配图或实物标签确认 U1 外接颗粒物传感器是否为 PMSA003。；原因：正文指定 PMSA003，但原理图仅显示 PM2.5PORT 接口名称。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d8b3f2036f8abc6dc36266db76123fba9adced368c2c120b674fe05d499ff62a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1030/M134_01.png` |

---

源文档：`zh_CN/module/PM2.5 AIR QUALITY KIT (Excluding Core).md`

源文档 SHA-256：`1f504e6455defdfed2397f11c4c0d13c20d41f09f1f33b91ed51a0d6bf35e951`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
