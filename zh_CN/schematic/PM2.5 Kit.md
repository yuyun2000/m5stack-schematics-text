# PM2.5 Kit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | PM2.5 Kit |
| SKU | K023 |
| 产品 ID | `pm2-5-kit-752db3817213` |
| 源文档 | `zh_CN/base/pm2.5.md` |

## 概述

PM2.5 Kit 的本地单页原理图通过 J2 M5Stack_BUS 接入外部主机，并把 GPIO16/GPIO17 UART、GPIO21/GPIO22 I2C、GPIO23/GPIO19/GPIO18 SPI、+5V 和 +3V3 引到传感器及扩展接口。U1 PM2.5PORT 为颗粒物传感器提供双 5V、双 GND、RESET、RX、TX 和 SET，U2 SHT20 连接带 4.7KΩ 上拉的 I2C 总线。J3 USB-C 仅绘制 VBUS/GND 供电连接，J1 BUS_8P 引出电源、I2C 和 SPI；页面未展开 PMSA003 内部电路或传感器性能参数。

## 检索关键词

`PM2.5 Kit`、`K023`、`PM2.5PORT`、`PMSA003`、`SHT20`、`M5Stack_BUS`、`BUS_8P`、`USB-C`、`UART`、`I2C`、`SPI`、`GPIO13`、`GPIO16`、`GPIO17`、`GPIO18`、`GPIO19`、`GPIO21`、`GPIO22`、`GPIO23`、`MRX`、`MTX`、`MSDA`、`MSCL`、`MMOSI`、`MMISO`、`MSCK`、`MRST`、`MSET`、`+5V`、`+3V3`、`RESET`、`SET`、`R1 4.7KΩ`、`R2 4.7KΩ`、`C1 100nF`、`Air.SchDoc`、`power-only USB-C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | PM2.5PORT | PM2.5 传感器 10 Pin 电源、UART、RESET 与 SET 接口 | 图 40b7d4909e8b / 第 1 页 / 网格 B3：U1 PM2.5PORT，pins1-10 的 VCC/GND/RESET/NC/RX/NC/TX/SET |
| U2 | SHT20 | 3.3V I2C 温湿度传感器，连接 MSDA/MSCL 与去耦网络 | 图 40b7d4909e8b / 第 1 页 / 网格 C2-C3：U2 SHT20，SDA/SCL/VSS/VDD/NC 与 C1/R1/R2 |
| J1 | BUS_8P | 引出 +5V、+3V3、GND、I2C 与 SPI 信号的 8 Pin 扩展接口 | 图 40b7d4909e8b / 第 1 页 / 网格 B1：J1 BUS_8P，pins1-8 标注 5V/3V3/GND/SDA/SCL/MOSI/MISO/SCK |
| J2 | M5Stack_BUS | 连接外部 M5 主机的 30 Pin 堆叠总线 | 图 40b7d4909e8b / 第 1 页 / 网格 C4-D4：J2 M5Stack_BUS，pins1-30 及 MRST/MMOSI/MMISO/MSCK/MRX/MTX/MSDA/MSCL/MSET/+3V3/+5V |
| J3 | USB-C | +5V 电源输入连接器，图中只使用 VBUS 与 GND | 图 40b7d4909e8b / 第 1 页 / 网格 A1：J3 USB-C，VBUS 接 +5V，GND 与 pins11-14 接地 |
| R1,R2 | 4.7KΩ | MSDA 与 MSCL 到 +3V3 的 I2C 上拉电阻 | 图 40b7d4909e8b / 第 1 页 / 网格 C2-C3：R1 4.7KΩ 上拉 MSDA，R2 4.7KΩ 上拉 MSCL |
| C1 | 100nF | SHT20 +3V3 电源去耦电容 | 图 40b7d4909e8b / 第 1 页 / 网格 C3：C1 100nF 连接 +3V3 与 GND |

## 系统结构

### PM2.5 Kit 接口板架构

J2 M5Stack_BUS 连接外部 M5 主机，U1 PM2.5PORT 通过 UART/RESET/SET 连接颗粒物传感器，U2 SHT20 使用 I2C，J1 引出 I2C/SPI/电源，J3 提供 +5V USB-C 电源输入。

- 参数与网络：`host=external M5 host via J2`；`particle_port=U1 PM2.5PORT`；`temperature_humidity=U2 SHT20`；`expansion=J1 BUS_8P`；`power_input=J3 USB-C VBUS to +5V`
- 证据：图 40b7d4909e8b / 第 1 页 / 第 1 页完整 Air.SchDoc：J1/J2/J3、U1/U2 与全部网络

### 本页未集成的系统功能

当前完整单页未画出通用主控、协处理器、存储器、晶振、射频、音频或专用调试接口；处理和通信控制由 J2 外部 M5 主机承担。

- 参数与网络：`general_mcu_shown=false`；`coprocessor_shown=false`；`storage_shown=false`；`crystal_shown=false`；`rf_shown=false`；`audio_shown=false`；`debug_connector_shown=false`；`external_host=M5 host via J2`
- 证据：图 40b7d4909e8b / 第 1 页 / 第 1 页完整 Air.SchDoc 器件与接口范围

## 电源

### +5V 电源分配

+5V 网络同时连接 J3 USB-C VBUS、J2 M5Stack_BUS pin28、J1 BUS_8P pin1，以及 U1 PM2.5PORT 的 VCC pins1/2。

- 参数与网络：`rail=+5V`；`usb_c=J3 VBUS`；`m5_bus=J2 pin28`；`bus_8p=J1 pin1`；`pm25_port=U1 pins1,2`
- 证据：图 40b7d4909e8b / 第 1 页 / 网格 A1/B1/B3/D4：J3、J1、U1、J2 的同名 +5V 网络

### +3V3 电源分配

+3V3 网络连接 J2 pin12、J1 pin2、U2 SHT20 VDD pin5、R1/R2 上拉端和 C1 100nF。

- 参数与网络：`rail=+3V3`；`m5_bus=J2 pin12`；`bus_8p=J1 pin2`；`sensor=U2 pin5 VDD`；`pullups=R1/R2 4.7KΩ`；`decoupling=C1 100nF`
- 证据：图 40b7d4909e8b / 第 1 页 / 网格 B1-C3/D4：J1/U2/R1/R2/C1/J2 的 +3V3 网络

## 接口

### J3 USB-C 电源接口

J3 图中只连接 VBUS 与 GND：VBUS 接 +5V，左侧 pins11-14 和右侧 GND 引脚接地，页面未绘制 USB D+/D- 或 CC 网络。

- 参数与网络：`reference=J3`；`vbus=+5V`；`ground_pins=GND and pins11-14`；`usb_data_shown=false`；`cc_network_shown=false`；`protection_shown=false`
- 证据：图 40b7d4909e8b / 第 1 页 / 网格 A1：J3 USB-C 全部可见引脚和 +5V/GND 连线

### J1 BUS_8P

J1 pins1-8 依次为 +5V、+3V3、GND、MSDA、MSCL、MMOSI、MMISO、MSCK，对应符号内 5V、3V3、GND、SDA、SCL、MOSI、MISO、SCK。

- 参数与网络：`pin1=+5V`；`pin2=+3V3`；`pin3=GND`；`pin4=MSDA/SDA`；`pin5=MSCL/SCL`；`pin6=MMOSI/MOSI`；`pin7=MMISO/MISO`；`pin8=MSCK/SCK`
- 证据：图 40b7d4909e8b / 第 1 页 / 网格 B1：J1 BUS_8P pins1-8 与网络标签

### U1 PM2.5PORT

U1 pins1/2 VCC 接 +5V，pins3/4 GND 接地，pin5 RESET 接 MRST，pins6/8 标 NC，pin7 RX 接 MTX，pin9 TX 接 MRX，pin10 SET 接 MSET。

- 参数与网络：`pins1_2=VCC +5V`；`pins3_4=GND`；`pin5=RESET MRST`；`pins6_8=NC`；`pin7=RX MTX`；`pin9=TX MRX`；`pin10=SET MSET`；`logic_level=null`
- 证据：图 40b7d4909e8b / 第 1 页 / 网格 B3：U1 PM2.5PORT pins1-10 与左侧网络

### J2 M5Stack_BUS 已连接信号

J2 已连接 pins1/3/5 GND、pin6 EN/MRST、pin7 GPIO23/MMOSI、pin9 GPIO19/MMISO、pin11 GPIO18/MSCK、pin12 +3V3、pin15 GPIO16/MRX、pin16 GPIO17/MTX、pin17 GPIO21/MSDA、pin18 GPIO22/MSCL、pin22 GPIO13/MSET 和 pin28 +5V。

- 参数与网络：`ground=pins1,3,5`；`reset=pin6 EN/MRST`；`spi=pin7 GPIO23/MMOSI; pin9 GPIO19/MMISO; pin11 GPIO18/MSCK`；`power=pin12 +3V3; pin28 +5V`；`uart=pin15 GPIO16/MRX; pin16 GPIO17/MTX`；`i2c=pin17 GPIO21/MSDA; pin18 GPIO22/MSCL`；`set=pin22 GPIO13/MSET`
- 证据：图 40b7d4909e8b / 第 1 页 / 网格 C4-D4：J2 M5Stack_BUS pins1-30 与全部外接网络

## 总线

### PM2.5PORT UART 到 M5Stack_BUS

U1 RX pin7 经 MTX 连接 J2 pin16 GPIO17，U1 TX pin9 经 MRX 连接 J2 pin15 GPIO16；因此 GPIO17 为主机到传感器方向，GPIO16 为传感器到主机方向。

- 参数与网络：`sensor_rx=U1 pin7 RX <- MTX <- J2 pin16 GPIO17`；`sensor_tx=U1 pin9 TX -> MRX -> J2 pin15 GPIO16`；`host_tx_gpio=GPIO17`；`host_rx_gpio=GPIO16`；`baud_rate_shown=null`
- 证据：图 40b7d4909e8b / 第 1 页 / 网格 B3/D4：U1 MTX/MRX 与 J2 GPIO17/GPIO16 同名网络

### SPI 扩展引出

J2 GPIO23/GPIO19/GPIO18 分别通过 MMOSI/MMISO/MSCK 连接 J1 BUS_8P pins6/7/8；本页未显示板载 SPI 设备或片选信号。

- 参数与网络：`controller=external M5 host`；`mosi=J2 pin7 GPIO23-MMOSI-J1 pin6`；`miso=J2 pin9 GPIO19-MMISO-J1 pin7`；`sck=J2 pin11 GPIO18-MSCK-J1 pin8`；`chip_select_shown=false`；`onboard_spi_device_shown=false`
- 证据：图 40b7d4909e8b / 第 1 页 / 网格 B1/D4：J1 MMOSI/MMISO/MSCK 与 J2 GPIO23/GPIO19/GPIO18

### SHT20 I2C 总线

MSDA/MSCL 分别连接 U2 pins1/6、J1 pins4/5 和 J2 GPIO21/GPIO22，并通过 R1/R2 4.7KΩ 上拉到 +3V3。

- 参数与网络：`controller=external M5 host`；`device=U2 SHT20`；`sda=U2 pin1-MSDA-J1 pin4-J2 pin17 GPIO21`；`scl=U2 pin6-MSCL-J1 pin5-J2 pin18 GPIO22`；`sda_pullup=R1 4.7KΩ to +3V3`；`scl_pullup=R2 4.7KΩ to +3V3`
- 证据：图 40b7d4909e8b / 第 1 页 / 网格 B1-C3/D4：U2/R1/R2、J1、J2 的 MSDA/MSCL 网络

## 复位

### PM2.5PORT RESET 与 SET

U1 pin5 RESET 通过 MRST 连接 J2 pin6 EN；U1 pin10 SET 通过 MSET 连接 J2 pin22 GPIO13。

- 参数与网络：`reset=U1 pin5 RESET-MRST-J2 pin6 EN`；`set=U1 pin10 SET-MSET-J2 pin22 GPIO13`；`control_direction=host to sensor port`
- 证据：图 40b7d4909e8b / 第 1 页 / 网格 B3/D4：U1 RESET/SET 与 J2 EN/GPIO13 的 MRST/MSET 网络

## 传感器

### U2 SHT20 电气连接

U2 pin1 SDA 接 MSDA，pin6 SCL 接 MSCL，pin2 VSS 接 GND，pin5 VDD 接 +3V3，pins3/4 标 NC；C1 100nF 从 +3V3 接 GND。

- 参数与网络：`part=U2 SHT20`；`sda=pin1 MSDA`；`scl=pin6 MSCL`；`ground=pin2 VSS GND`；`supply=pin5 VDD +3V3`；`nc=pins3,4`；`decoupling=C1 100nF`
- 证据：图 40b7d4909e8b / 第 1 页 / 网格 C2-C3：U2 SHT20 全部引脚与 C1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | PM2.5 Kit 接口板架构 | `host=external M5 host via J2`；`particle_port=U1 PM2.5PORT`；`temperature_humidity=U2 SHT20`；`expansion=J1 BUS_8P`；`power_input=J3 USB-C VBUS to +5V` |
| 电源 | +5V 电源分配 | `rail=+5V`；`usb_c=J3 VBUS`；`m5_bus=J2 pin28`；`bus_8p=J1 pin1`；`pm25_port=U1 pins1,2` |
| 电源 | +3V3 电源分配 | `rail=+3V3`；`m5_bus=J2 pin12`；`bus_8p=J1 pin2`；`sensor=U2 pin5 VDD`；`pullups=R1/R2 4.7KΩ`；`decoupling=C1 100nF` |
| 接口 | J3 USB-C 电源接口 | `reference=J3`；`vbus=+5V`；`ground_pins=GND and pins11-14`；`usb_data_shown=false`；`cc_network_shown=false`；`protection_shown=false` |
| 接口 | J1 BUS_8P | `pin1=+5V`；`pin2=+3V3`；`pin3=GND`；`pin4=MSDA/SDA`；`pin5=MSCL/SCL`；`pin6=MMOSI/MOSI`；`pin7=MMISO/MISO`；`pin8=MSCK/SCK` |
| 接口 | U1 PM2.5PORT | `pins1_2=VCC +5V`；`pins3_4=GND`；`pin5=RESET MRST`；`pins6_8=NC`；`pin7=RX MTX`；`pin9=TX MRX`；`pin10=SET MSET`；`logic_level=null` |
| 总线 | PM2.5PORT UART 到 M5Stack_BUS | `sensor_rx=U1 pin7 RX <- MTX <- J2 pin16 GPIO17`；`sensor_tx=U1 pin9 TX -> MRX -> J2 pin15 GPIO16`；`host_tx_gpio=GPIO17`；`host_rx_gpio=GPIO16`；`baud_rate_shown=null` |
| 复位 | PM2.5PORT RESET 与 SET | `reset=U1 pin5 RESET-MRST-J2 pin6 EN`；`set=U1 pin10 SET-MSET-J2 pin22 GPIO13`；`control_direction=host to sensor port` |
| 接口 | J2 M5Stack_BUS 已连接信号 | `ground=pins1,3,5`；`reset=pin6 EN/MRST`；`spi=pin7 GPIO23/MMOSI; pin9 GPIO19/MMISO; pin11 GPIO18/MSCK`；`power=pin12 +3V3; pin28 +5V`；`uart=pin15 GPIO16/MRX; pin16 GPIO17/MTX`；`i2c=pin17 GPIO21/MSDA; pin18 GPIO22/MSCL`；`set=pin22 GPIO13/MSET` |
| 总线 | SPI 扩展引出 | `controller=external M5 host`；`mosi=J2 pin7 GPIO23-MMOSI-J1 pin6`；`miso=J2 pin9 GPIO19-MMISO-J1 pin7`；`sck=J2 pin11 GPIO18-MSCK-J1 pin8`；`chip_select_shown=false`；`onboard_spi_device_shown=false` |
| 传感器 | U2 SHT20 电气连接 | `part=U2 SHT20`；`sda=pin1 MSDA`；`scl=pin6 MSCL`；`ground=pin2 VSS GND`；`supply=pin5 VDD +3V3`；`nc=pins3,4`；`decoupling=C1 100nF` |
| 总线 | SHT20 I2C 总线 | `controller=external M5 host`；`device=U2 SHT20`；`sda=U2 pin1-MSDA-J1 pin4-J2 pin17 GPIO21`；`scl=U2 pin6-MSCL-J1 pin5-J2 pin18 GPIO22`；`sda_pullup=R1 4.7KΩ to +3V3`；`scl_pullup=R2 4.7KΩ to +3V3` |
| 总线地址 | SHT20 I2C 地址 | `device=U2 SHT20`；`seven_bit_address=null`；`address_text_shown=false`；`address_strap_shown=false` |
| 核心器件 | 颗粒物传感器实装型号 | `documented_model=PMSA003`；`schematic_component=U1 PM2.5PORT`；`sensor_part_number_shown=false`；`internal_circuit_shown=false` |
| 其他事实 | 正文中的颗粒物与温湿度性能 | `documented_particle_resolution=0.3um`；`documented_pm25_range=0-500ug/m3 effective; >=1000ug/m3 maximum`；`documented_temperature_range=-40 to 125C`；`documented_humidity_range=0-100%RH`；`schematic_particle_interface=U1 PM2.5PORT`；`schematic_temperature_humidity=U2 SHT20`；`calibration_shown=false` |
| 系统结构 | 本页未集成的系统功能 | `general_mcu_shown=false`；`coprocessor_shown=false`；`storage_shown=false`；`crystal_shown=false`；`rf_shown=false`；`audio_shown=false`；`debug_connector_shown=false`；`external_host=M5 host via J2` |

## 待确认事项

- `address.sht20-i2c`：页面明确显示 U2 使用 I2C，但未打印其 7-bit 地址值，也没有可见地址选择引脚。（证据：图 40b7d4909e8b / 第 1 页 / 网格 C2-C3：U2 SHT20 SDA/SCL 引脚，整页无 0x 地址标注）
- `component.particle-sensor-model`：产品正文指定 PMSA003，但当前原理图只画出 U1 PM2.5PORT 接口符号，没有传感器位号、PMSA003 型号文字或其内部电路，因此实装传感器型号无法由本页独立确认。（证据：图 40b7d4909e8b / 第 1 页 / 网格 B3：U1 仅标 PM2.5PORT，完整页无 PMSA003 型号文字）
- `other.documented-sensor-performance`：正文给出粒径、浓度范围、计数效率、温湿度范围和精度等参数；当前原理图只确认 PM2.5PORT 与 SHT20 电气连接，无法验证传感器批次、标定条件和整机测量性能。（证据：图 40b7d4909e8b / 第 1 页 / 第 1 页 U1 PM2.5PORT 与 U2 SHT20，图中无量程、精度、效率或标定参数）
- `review.sht20-i2c-address`：K023 当前 U2 SHT20 使用的正式 7-bit I2C 地址是多少？；原因：原理图只显示 SDA/SCL，没有地址数值或地址绑定位；需由对应 datasheet 或已确认软件定义闭环。
- `review.particle-sensor-bom`：K023 当前量产 BOM 中连接 U1 PM2.5PORT 的颗粒物传感器是否固定为 PMSA003？；原因：产品正文列出 PMSA003，但原理图只定义接口，需由 BOM、装配图或实物丝印确认。
- `review.sensor-performance`：K023 当前传感器批次和整机标定确认的颗粒物量程/效率及温湿度范围/精度分别是什么？；原因：这些是传感器和整机性能参数，接口原理图不能证明测试条件或量产一致性。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `40b7d4909e8b14aa7813a5559a29db3f78e5a9c8356ab0fa64771245630568f3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1065/UNIT_PM25_page_01.png` |

---

源文档：`zh_CN/base/pm2.5.md`

源文档 SHA-256：`6aa6d993ae3f4397a27396776a424bc2e8653335732ca04753f73fad9cd1cb18`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
