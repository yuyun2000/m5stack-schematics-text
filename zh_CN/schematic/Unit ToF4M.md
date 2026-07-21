# Unit ToF4M 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ToF4M |
| SKU | U172 |
| 产品 ID | `unit-tof4m-f7f755230293` |
| 源文档 | `zh_CN/unit/Unit-ToF4M.md` |

## 概述

Unit ToF4M 以 VL53L1CXV0FY/1（U1）ToF 测距传感器为核心，通过 J1 IIC_Socket_4P 的 SCL/SDA 直接连接外部 I2C 主机，图面明确标注 7-bit 地址为 0x29。U1 的 XSHUT、GPIO1、SDA、SCL 均由 4.7KΩ 电阻上拉到 +3.3V，XSHUT 与 GPIO1 另引至 jp1/jp2 测试点。HT7533（U2）将 J1 输入的 VCC 转换为 +3.3V，为传感器和四组上拉供电；原理图未标明 VCC 数值、测距范围或 I2C 速率。

## 检索关键词

`Unit ToF4M`、`U172`、`VL53L1CXV0FY/1`、`VL53L1CX`、`U1`、`HT7533`、`U2`、`IIC_Socket_4P`、`J1`、`I2C`、`7-bit Addr: 0x29`、`0x29`、`SCL`、`SDA`、`XSHUT`、`GPIO1`、`jp1`、`jp2`、`R1 4.7KΩ`、`R2 4.7KΩ`、`R3 4.7KΩ`、`R4 4.7KΩ`、`+3.3V`、`VCC`、`AVDD`、`AVSS`、`DNC`、`C1 100nF`、`C2 100nF`、`C3 10uF`、`C4 10uF`、`Time-of-Flight`、`ToF sensor`、`4m ranging`、`Grove I2C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | VL53L1CXV0FY/1 | ToF 测距传感器，提供 I2C、XSHUT 与 GPIO1 接口 | 图 52cb492af62a / 第 1 页 / 页 1 网格 B2-B3，U1 VL53L1CXV0FY/1，pins 1~12 与 7-bit Addr: 0x29 标注 |
| U2 | HT7533 | 将 J1 输入的 VCC 转换为 +3.3V | 图 52cb492af62a / 第 1 页 / 页 1 网格 C2，U2 HT7533：VIN pin 2 接 VCC、VOUT pin 3 接 +3.3V、GND pin 1 接地 |
| J1 | IIC_Socket_4P | 外部 I2C、VCC 与 GND 的四针 Grove 接口 | 图 52cb492af62a / 第 1 页 / 页 1 网格 C3，J1 IIC_Socket_4P pins 1~4 为 IIC_SCL、IIC_SDA、VCC、GND |
| R1/R2 | 4.7KΩ | U1 SCL/SDA 到 +3.3V 的 I2C 上拉电阻 | 图 52cb492af62a / 第 1 页 / 页 1 网格 A2-B2，R1 4.7KΩ 接 SCL，R2 4.7KΩ 接 SDA，二者上端均为 +3.3V |
| R3/R4 | 4.7KΩ | U1 GPIO1/XSHUT 到 +3.3V 的上拉电阻 | 图 52cb492af62a / 第 1 页 / 页 1 网格 A2-B2，R3 4.7KΩ 接 GPIO1，R4 4.7KΩ 接 XSHUT，二者上端均为 +3.3V |
| jp1/jp2 | 未标注 | 分别引出 XSHUT 与 GPIO1 的测试点 | 图 52cb492af62a / 第 1 页 / 页 1 网格 B1-B2，jp1 test 接 U1 XSHUT pin 5 网络，jp2 test 接 U1 GPIO1 pin 7 网络 |
| C1/C4 | 100nF / 10uF | VCC 输入侧的高频去耦与储能电容 | 图 52cb492af62a / 第 1 页 / 页 1 网格 C2-C3，C1 100nF 与 C4 10uF 分别跨接 VCC 和 GND |
| C2/C3 | 100nF / 10uF | HT7533 +3.3V 输出侧的高频去耦与储能电容 | 图 52cb492af62a / 第 1 页 / 页 1 网格 C1-C2，C2 100nF 与 C3 10uF 跨接 +3.3V 和 GND |

## 系统结构

### Unit ToF4M 系统架构

U1 VL53L1CXV0FY/1 通过 J1 SCL/SDA 直接连接外部 I2C 主机，U2 HT7533 从 J1 VCC 生成 +3.3V，jp1/jp2 分别引出 XSHUT/GPIO1。

- 参数与网络：`sensor=U1 VL53L1CXV0FY/1`；`interface=J1 IIC_Socket_4P`；`bus=SCL,SDA`；`regulator=U2 HT7533`；`control_test=jp1 XSHUT,jp2 GPIO1`；`onboard_controller=null`
- 证据：图 52cb492af62a / 第 1 页 / 整页：U1/U2/J1/jp1/jp2 与 SCL/SDA/XSHUT/GPIO1/VCC/+3.3V 网络

## 电源

### J1 VCC 输入

J1 pin 3 VCC 连接 U2 VIN pin 2；C1 100nF 与 C4 10uF 从 VCC 接至 GND。

- 参数与网络：`input_connector=J1 pin 3 VCC`；`regulator_input=U2 VIN pin 2`；`input_decoupling=C1 100nF,C4 10uF`；`ground=J1 pin 4 GND`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 网格 C2-C3，J1 VCC/U2 VIN/C1/C4 同名网络

### U2 HT7533

U2 VIN pin 2 接 VCC，VOUT pin 3 输出 +3.3V，GND pin 1 接地；输出侧由 C2 100nF 与 C3 10uF 去耦。

- 参数与网络：`input=VIN pin 2,VCC`；`output=VOUT pin 3,+3.3V`；`ground=pin 1,GND`；`output_decoupling=C2 100nF,C3 10uF`；`enable=null`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 网格 C1-C2，U2 HT7533 pins 1/2/3 与 C2/C3/VCC/+3.3V/GND

### U1 电源

U1 AVDD pins 1/11 接 +3.3V；AVSS pin 2、GND pin 3、GND2 pin 4、GND3 pin 6 和 GND4 pin 12 接 GND。

- 参数与网络：`positive_supply=AVDD pins 1,11 +3.3V`；`avss=pin 2 GND`；`ground_pins=pins 3,4,6,12 GND`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 网格 B2-B3，U1 AVDD/AVSS/GND/GND2/GND3/GND4 pins 1/2/3/4/6/11/12

### 电源控制、充电与监测

本页未绘出稳压使能、负载开关、充电器、电池、电量计或电源监测器。

- 参数与网络：`regulator_enable=null`；`load_switch=null`；`charger=null`；`battery=null`；`fuel_gauge=null`；`power_monitor=null`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 整页，电源链仅 J1 VCC、U2 HT7533、C1~C4 与 +3.3V

## 接口

### J1 IIC_Socket_4P

J1 pin 1 为 IIC_SCL 并接 SCL，pin 2 为 IIC_SDA 并接 SDA，pin 3 为 VCC，pin 4 为 GND；原理图未标注 I2C 信号方向或 VCC 数值。

- 参数与网络：`pin_1=IIC_SCL,SCL`；`pin_2=IIC_SDA,SDA`；`pin_3=VCC`；`pin_4=GND`；`direction_marking=not shown`；`vcc_value=not shown`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 网格 C3，J1 pins 1~4、IIC_SCL/IIC_SDA/VCC/GND 与左侧 SCL/SDA 网络

## 总线

### J1 到 U1 的 I2C 连接

J1 pin 1 SCL 直接连接 U1 SCL pin 10，J1 pin 2 SDA 直接连接 U1 SDA pin 9；两条线上没有串联电平转换器。

- 参数与网络：`controller_side=external host at J1`；`device=U1 VL53L1CXV0FY/1`；`scl=J1 pin 1->U1 pin 10`；`sda=J1 pin 2->U1 pin 9`；`level_shifter=null`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 网格 B1-C3，SCL/SDA 同名网络从 U1 pins 10/9 直达 J1 pins 1/2

### SCL/SDA 上拉

U1 SCL pin 10 经 R1 4.7KΩ 上拉到 +3.3V，SDA pin 9 经 R2 4.7KΩ 上拉到 +3.3V。

- 参数与网络：`scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`；`sensor_scl=U1 pin 10`；`sensor_sda=U1 pin 9`；`pullup_rail=+3.3V`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 网格 A2-B2，R1/R2 4.7KΩ 从 +3.3V 分别连接 SCL/SDA

### 其他外部总线

本页外部通信只显示 I2C SCL/SDA，未显示 SPI、UART、CAN、RS-485、USB、SDIO、MIPI 或 I2S。

- 参数与网络：`i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 J1 仅 IIC_SCL/IIC_SDA/VCC/GND，整页无其他总线网络

## 总线地址

### U1 I2C 地址

原理图在 U1 上方明确标注 7-bit Addr: 0x29。

- 参数与网络：`device=U1 VL53L1CXV0FY/1`；`address_format=7-bit`；`address=0x29`；`address_selector=null`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 网格 B2，U1 上方文字 7-bit Addr: 0x29

## GPIO 与控制信号

### U1 XSHUT

U1 XSHUT pin 5 经 R4 4.7KΩ 上拉到 +3.3V，并连接 jp1 test 测试点；该网络未引至 J1。

- 参数与网络：`pin=U1 pin 5 XSHUT`；`pullup=R4 4.7KΩ to +3.3V`；`test_point=jp1`；`grove_connection=null`；`direction_marking=not shown`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 网格 B1-B2，jp1/R4/U1 XSHUT pin 5 顶部网络

### U1 GPIO1

U1 GPIO1 pin 7 经 R3 4.7KΩ 上拉到 +3.3V，并连接 jp2 test 测试点；该网络未引至 J1。

- 参数与网络：`pin=U1 pin 7 GPIO1`；`pullup=R3 4.7KΩ to +3.3V`；`test_point=jp2`；`grove_connection=null`；`direction_marking=not shown`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 网格 B1-B2，jp2/R3/U1 GPIO1 pin 7 第二条网络

## 时钟

### 时钟网络

本页未绘出外部晶振、谐振器、振荡器或专用时钟网络；SCL 是唯一带时钟名称的 I2C 总线信号。

- 参数与网络：`crystal=null`；`resonator=null`；`oscillator=null`；`dedicated_clock_net=null`；`bus_clock=SCL`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 整页，器件仅 U1/U2/J1、测试点与阻容，无时钟器件

## 复位

### 复位与关断控制

本页未绘出独立 RESET/NRST 引脚或 RC 复位网络；U1 只显示 XSHUT pin 5 控制网络，并由 R4 上拉后引至 jp1。

- 参数与网络：`reset_pin=null`；`reset_rc=null`；`xshut=U1 pin 5,R4 4.7KΩ,jp1`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 U1 pins 1~12 与外围网络，只有 XSHUT，无 RESET/NRST 或 RC 网络

## 保护电路

### J1 与电源保护

J1 SCL/SDA/VCC 路径未绘出 TVS、ESD 阵列、保险丝、反接保护、过压保护或浪涌限制器。

- 参数与网络：`tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`surge_limiter=null`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 整页，J1 到 U1/U2 的 SCL/SDA/VCC 路径无专用保护位号

## 关键网络

### Unit ToF4M 关键网络索引

关键路径为 J1 pin1 SCL→U1 pin10、J1 pin2 SDA→U1 pin9、J1 pin3 VCC→U2 pin2→U2 pin3/+3.3V→U1 AVDD，以及 jp1→XSHUT、jp2→GPIO1。

- 参数与网络：`scl=J1.1-U1.10`；`sda=J1.2-U1.9`；`power=J1.3 VCC-U2.2/U2.3-+3.3V-U1.1/U1.11`；`xshut=jp1-U1.5`；`gpio1=jp2-U1.7`；`ground=J1.4-U1.2/3/4/6/12-U2.1`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 整页，SCL/SDA/VCC/+3.3V/XSHUT/GPIO1/GND 同名网络

## 存储

### 存储连接

本页未绘出存储器件、存储卡连接器或 SDIO/SPI 存储连接。

- 参数与网络：`storage_device=null`；`card_connector=null`；`sdio=null`；`spi_storage=null`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 整页，仅传感器、稳压器、I2C 插座、测试点与阻容

## 内存与 Flash

### 外部存储器

U1 周边未绘出独立 Flash、EEPROM、SRAM 或 PSRAM。

- 参数与网络：`flash=null`；`eeprom=null`；`sram=null`；`psram=null`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 U1 全部引脚与整页器件清单中无外部存储器

## 音频

### 音频链路

本页未绘出麦克风、扬声器、音频编解码器、放大器或 I2S 音频网络。

- 参数与网络：`microphone=null`；`speaker=null`；`codec=null`；`amplifier=null`；`i2s=null`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 整页，无音频器件或音频网络

## 传感器

### U1 VL53L1CXV0FY/1 引脚

U1 XSHUT pin 5、GPIO1 pin 7、SDA pin 9、SCL pin 10；AVDD pins 1/11 接 +3.3V，AVSS/GND/GND2/GND3/GND4 pins 2/3/4/6/12 接 GND，DNC pin 8 未连接。

- 参数与网络：`xshut=pin 5`；`gpio1=pin 7`；`sda=pin 9`；`scl=pin 10`；`avdd=pins 1,11 +3.3V`；`grounds=pins 2,3,4,6,12 GND`；`dnc=pin 8 no-connect`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 网格 B2-B3，U1 pins 1~12 的引脚名、编号与连线

## 射频

### 射频链路

本页未绘出天线、射频收发器、匹配网络或射频连接器。

- 参数与网络：`antenna=null`；`transceiver=null`；`matching_network=null`；`rf_connector=null`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 整页，无 RF/ANT 网络或射频器件

## 调试与烧录

### jp1/jp2 测试点

jp1 test 连接 XSHUT，jp2 test 连接 GPIO1；本页未绘出 JTAG、SWD、UART 调试头或其他调试连接器。

- 参数与网络：`jp1=U1 XSHUT pin 5`；`jp2=U1 GPIO1 pin 7`；`jtag=null`；`swd=null`；`uart_debug=null`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 网格 B1-B2 jp1/jp2 test 与整页连接器 J1

## 模拟电路

### 外部模拟链路

本页未绘出运算放大器、独立 ADC/DAC、分压采样或模拟前端；测距功能集成在 U1 内。

- 参数与网络：`op_amp=null`；`external_adc=null`；`external_dac=null`；`voltage_divider=null`；`sensor=U1 VL53L1CXV0FY/1`
- 证据：图 52cb492af62a / 第 1 页 / 页 1 整页，U1 外围仅数字控制/I2C、电源与上拉网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit ToF4M 系统架构 | `sensor=U1 VL53L1CXV0FY/1`；`interface=J1 IIC_Socket_4P`；`bus=SCL,SDA`；`regulator=U2 HT7533`；`control_test=jp1 XSHUT,jp2 GPIO1`；`onboard_controller=null` |
| 传感器 | U1 VL53L1CXV0FY/1 引脚 | `xshut=pin 5`；`gpio1=pin 7`；`sda=pin 9`；`scl=pin 10`；`avdd=pins 1,11 +3.3V`；`grounds=pins 2,3,4,6,12 GND`；`dnc=pin 8 no-connect` |
| 总线地址 | U1 I2C 地址 | `device=U1 VL53L1CXV0FY/1`；`address_format=7-bit`；`address=0x29`；`address_selector=null` |
| 接口 | J1 IIC_Socket_4P | `pin_1=IIC_SCL,SCL`；`pin_2=IIC_SDA,SDA`；`pin_3=VCC`；`pin_4=GND`；`direction_marking=not shown`；`vcc_value=not shown` |
| 总线 | J1 到 U1 的 I2C 连接 | `controller_side=external host at J1`；`device=U1 VL53L1CXV0FY/1`；`scl=J1 pin 1->U1 pin 10`；`sda=J1 pin 2->U1 pin 9`；`level_shifter=null` |
| 总线 | SCL/SDA 上拉 | `scl_pullup=R1 4.7KΩ to +3.3V`；`sda_pullup=R2 4.7KΩ to +3.3V`；`sensor_scl=U1 pin 10`；`sensor_sda=U1 pin 9`；`pullup_rail=+3.3V` |
| GPIO 与控制信号 | U1 XSHUT | `pin=U1 pin 5 XSHUT`；`pullup=R4 4.7KΩ to +3.3V`；`test_point=jp1`；`grove_connection=null`；`direction_marking=not shown` |
| GPIO 与控制信号 | U1 GPIO1 | `pin=U1 pin 7 GPIO1`；`pullup=R3 4.7KΩ to +3.3V`；`test_point=jp2`；`grove_connection=null`；`direction_marking=not shown` |
| 电源 | J1 VCC 输入 | `input_connector=J1 pin 3 VCC`；`regulator_input=U2 VIN pin 2`；`input_decoupling=C1 100nF,C4 10uF`；`ground=J1 pin 4 GND` |
| 电源 | U2 HT7533 | `input=VIN pin 2,VCC`；`output=VOUT pin 3,+3.3V`；`ground=pin 1,GND`；`output_decoupling=C2 100nF,C3 10uF`；`enable=null` |
| 电源 | U1 电源 | `positive_supply=AVDD pins 1,11 +3.3V`；`avss=pin 2 GND`；`ground_pins=pins 3,4,6,12 GND` |
| 电源 | 电源控制、充电与监测 | `regulator_enable=null`；`load_switch=null`；`charger=null`；`battery=null`；`fuel_gauge=null`；`power_monitor=null` |
| 电源 | J1 VCC 电压 | `schematic_rail=VCC`；`schematic_voltage=null`；`product_document_value=5V`；`verification_source_needed=HT7533 input design requirement or board electrical specification` |
| 传感器 | ToF 测距性能 | `sensor=VL53L1CXV0FY/1`；`range=null`；`accuracy=null`；`resolution=null`；`response_time=null`；`field_of_view=null`；`wavelength=null`；`product_document_range=4 to 400 cm` |
| 总线 | I2C 工作速率 | `pullups=R1/R2 4.7KΩ to +3.3V`；`frequency=null`；`bus_capacitance=null`；`timing=null` |
| 复位 | 复位与关断控制 | `reset_pin=null`；`reset_rc=null`；`xshut=U1 pin 5,R4 4.7KΩ,jp1` |
| 调试与烧录 | jp1/jp2 测试点 | `jp1=U1 XSHUT pin 5`；`jp2=U1 GPIO1 pin 7`；`jtag=null`；`swd=null`；`uart_debug=null` |
| 时钟 | 时钟网络 | `crystal=null`；`resonator=null`；`oscillator=null`；`dedicated_clock_net=null`；`bus_clock=SCL` |
| 保护电路 | J1 与电源保护 | `tvs_esd=null`；`fuse=null`；`reverse_polarity=null`；`overvoltage=null`；`surge_limiter=null` |
| 总线 | 其他外部总线 | `i2c=SCL,SDA`；`spi=null`；`uart=null`；`can=null`；`rs485=null`；`usb=null`；`sdio=null`；`mipi=null`；`i2s=null` |
| 存储 | 存储连接 | `storage_device=null`；`card_connector=null`；`sdio=null`；`spi_storage=null` |
| 内存与 Flash | 外部存储器 | `flash=null`；`eeprom=null`；`sram=null`；`psram=null` |
| 音频 | 音频链路 | `microphone=null`；`speaker=null`；`codec=null`；`amplifier=null`；`i2s=null` |
| 射频 | 射频链路 | `antenna=null`；`transceiver=null`；`matching_network=null`；`rf_connector=null` |
| 模拟电路 | 外部模拟链路 | `op_amp=null`；`external_adc=null`；`external_dac=null`；`voltage_divider=null`；`sensor=U1 VL53L1CXV0FY/1` |
| 关键网络 | Unit ToF4M 关键网络索引 | `scl=J1.1-U1.10`；`sda=J1.2-U1.9`；`power=J1.3 VCC-U2.2/U2.3-+3.3V-U1.1/U1.11`；`xshut=jp1-U1.5`；`gpio1=jp2-U1.7`；`ground=J1.4-U1.2/3/4/6/12-U2.1` |

## 待确认事项

- `power.vcc-voltage-not-shown`：原理图只将 J1 pin 3 和 U2 VIN 标为 VCC，没有打印输入电压数值或允许范围。（证据：图 52cb492af62a / 第 1 页 / 页 1 网格 C2-C3，J1 pin 3/U2 VIN/C1/C4 仅标 VCC，无数字电压）
- `sensor.ranging-performance-not-shown`：原理图确认 U1 型号，但未打印测距范围、精度、分辨率、响应时间、视场角或光源波长。（证据：图 52cb492af62a / 第 1 页 / 页 1 U1 VL53L1CXV0FY/1 与整页标注，无测距性能参数）
- `bus.i2c-speed-not-shown`：原理图给出 R1/R2 4.7KΩ 上拉，但未标注 I2C 频率、总线电容或时序要求。（证据：图 52cb492af62a / 第 1 页 / 页 1 SCL/SDA 与 R1/R2 区域，无 Hz、kHz、电容或时序标注）
- `review.vcc-voltage`：J1 VCC 的额定输入电压和允许范围是否为产品正文所示的 5V？；原因：原理图只标 VCC，未打印数字电压或输入范围。
- `review.ranging-performance`：该硬件版本在指定条件下的有效测距范围、精度、分辨率、响应时间、FoV 和光源参数是什么？；原因：原理图只确认传感器型号与电气连接，未记录光学和测量性能。
- `review.i2c-speed`：该板推荐和允许的 I2C 频率、总线电容与时序范围是什么？；原因：图面仅给出 4.7KΩ 上拉，未给总线速率与时序条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `52cb492af62acb384dd81d515477339c44e9f39922f7c1e9ee269e7ff6911938` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/626/UNIT-ToF4M_sch_01.png` |

---

源文档：`zh_CN/unit/Unit-ToF4M.md`

源文档 SHA-256：`5646d9eb1cb69ae4731dc7f9d9b03ae6a9afe71796e931a10d561ec9fd6ba39c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
