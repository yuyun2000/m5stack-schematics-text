# Unit ENV-II 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ENV-II |
| SKU | U001-B |
| 产品 ID | `unit-env-ii-87836fb3befd` |
| 源文档 | `zh_CN/unit/envII.md` |

## 概述

Unit ENV-II 由 SHT30-DIS-B（U1）和 BMP280（U2）两颗环境传感器组成，两者共享 J1 的 SCL/SDA 总线。SHT30 ADDR pin 2 接 GND；BMP280 CSB pin 2 接 +3.3V、SDO pin 5 接 GND，形成固定硬件配置。HT7533（U3）将 J1 输入的 VCC 稳压为 +3.3V，为两颗传感器供电；SCL/SDA 的 4.7KΩ 上拉则连接 VCC。原理图未打印 VCC 数值、SHT30/BMP280 的十六进制地址或测量量程和精度。

## 检索关键词

`Unit ENV-II`、`U001-B`、`SHT30-DIS-B`、`SHT30`、`BMP280`、`HT7533`、`IIC_Socket_4P`、`I2C`、`SCL`、`SDA`、`ADDR`、`CSB`、`SDO`、`0x44`、`0x76`、`VCC`、`+3.3V`、`R1 4.7KΩ`、`R2 4.7KΩ`、`temperature`、`humidity`、`pressure`、`C1 100nF`、`C2 100nF`、`C3 100nF`、`C4 10uF`、`C5 10uF`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | SHT30-DIS-B | 共享 I2C 总线的环境传感器，ADDR 硬件接地 | 图 13cfdf5a43da / 第 1 页 / 页 1 左上 U1 SHT30-DIS-B：ALERT/nRESET/ADDR/R/VSS/dpad/VDD/SDA/SCL pins 1~9 |
| U2 | BMP280 | 共享 I2C 总线的环境传感器，CSB 上拉且 SDO 接地 | 图 13cfdf5a43da / 第 1 页 / 页 1 左下 U2 BMP280：SCK/SDI/CSB/SDO/Vdd/Vddio/GND pins 1~8 |
| U3 | HT7533 | 将 J1 VCC 稳压为 +3.3V | 图 13cfdf5a43da / 第 1 页 / 页 1 下部 U3 HT7533，VIN pin 2 接 VCC、VOUT pin 3 接 +3.3V、GND pin 1 接地 |
| J1 | IIC_Socket_4P | 外部 I2C、VCC 与 GND 接口 | 图 13cfdf5a43da / 第 1 页 / 页 1 右上 J1 IIC_Socket_4P：pin 1 IIC_SCL、pin 2 IIC_SDA、pin 3 VCC、pin 4 GND |
| R1/R2 | 4.7KΩ | SCL 与 SDA 到 VCC 的 I2C 上拉电阻 | 图 13cfdf5a43da / 第 1 页 / 页 1 上中：R1/R2 均 4.7KΩ，上端 VCC，下端分别 SCL/SDA |
| C1/C3/C4 | 100nF / 100nF / 10uF | +3.3V 传感器电源去耦电容 | 图 13cfdf5a43da / 第 1 页 / 页 1 左侧 C1 100nF 与下部 C3 100nF/C4 10uF，均跨接 +3.3V-GND |
| C2/C5 | 100nF / 10uF | VCC 输入去耦与 HT7533 输入滤波电容 | 图 13cfdf5a43da / 第 1 页 / 页 1 右侧 C2 100nF 与下右 C5 10uF，均跨接 VCC-GND |

## 系统结构

### Unit ENV-II

U1 SHT30-DIS-B 与 U2 BMP280 共享 SCL/SDA，总线通过 J1 对外；U3 HT7533 从 VCC 产生 +3.3V，为两颗传感器供电。

- 参数与网络：`sensor_1=U1 SHT30-DIS-B`；`sensor_2=U2 BMP280`；`bus=SCL,SDA`；`connector=J1 IIC_Socket_4P`；`power=VCC->U3 HT7533->+3.3V`
- 证据：图 13cfdf5a43da / 第 1 页 / 整页：U1/U2/U3/J1 与 SCL/SDA/VCC/+3.3V/GND 网络

## 电源

### SCL/SDA 上拉

R1 与 R2 均为 4.7KΩ，分别将 SCL 与 SDA 上拉到 VCC；上拉轨在原理图中不是标为 +3.3V。

- 参数与网络：`scl_pullup=R1 4.7KΩ`；`sda_pullup=R2 4.7KΩ`；`pullup_rail=VCC`；`sensor_supply_rail=+3.3V`
- 证据：图 13cfdf5a43da / 第 1 页 / 页 1 上中：R1/R2 上端均标 VCC，下端 SCL/SDA

### U3 HT7533

U3 VIN pin 2 接 VCC，VOUT pin 3 输出 +3.3V，GND pin 1 接地；C5 10uF 位于输入侧，C3 100nF 与 C4 10uF 位于输出侧。

- 参数与网络：`input=VIN pin 2,VCC`；`output=VOUT pin 3,+3.3V`；`ground=pin 1 GND`；`input_capacitor=C5 10uF`；`output_capacitors=C3 100nF,C4 10uF`
- 证据：图 13cfdf5a43da / 第 1 页 / 页 1 下部 U3/C3/C4/C5 与 VCC/+3.3V/GND

### U1/U2 +3.3V 供电

U1 VDD pin 5 与 U2 Vdd pin 8、Vddio pin 6 接 +3.3V；U1 VSS/dpad/R pins 8/9/7 与 U2 GND pins 1/7 接 GND。

- 参数与网络：`sht30_supply=U1 VDD pin5,+3.3V`；`sht30_ground=U1 pins7/8/9,GND`；`bmp280_supply=U2 pins8/6,+3.3V`；`bmp280_ground=U2 pins1/7,GND`；`decoupling=C1 100nF,C3 100nF,C4 10uF`
- 证据：图 13cfdf5a43da / 第 1 页 / 页 1 U1/U2 电源引脚与 C1/C3/C4 +3.3V 网络

## 接口

### J1 IIC_Socket_4P

J1 pin 1 标 IIC_SCL 并接 SCL，pin 2 标 IIC_SDA 并接 SDA，pin 3 接 VCC，pin 4 接 GND。

- 参数与网络：`pin_1=IIC_SCL,SCL`；`pin_2=IIC_SDA,SDA`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 13cfdf5a43da / 第 1 页 / 页 1 右上 J1 pins 1~4 与 SCL/SDA/VCC/GND

## 总线

### SHT30/BMP280 共享 I2C

J1 SCL 同时连接 U1 SCL pin 4 与 U2 SCK pin 4，J1 SDA 同时连接 U1 SDA pin 1 与 U2 SDI pin 3。

- 参数与网络：`controller=external I2C host`；`scl_devices=U1 pin4,U2 pin4`；`sda_devices=U1 pin1,U2 pin3`；`connector=J1 pins 1/2`
- 证据：图 13cfdf5a43da / 第 1 页 / 页 1 U1/U2/J1 的 SCL/SDA 同名网络

## GPIO 与控制信号

### U1 ADDR

U1 ADDR pin 2 与 R/VSS/dpad 地网连接 GND，页面未绘出跳线或可变地址选择器。

- 参数与网络：`device=SHT30-DIS-B`；`pin=ADDR pin 2`；`strap=GND`；`selector=null`
- 证据：图 13cfdf5a43da / 第 1 页 / 页 1 左上 U1 ADDR pin 2 与 pins 7/8/9 公共 GND 竖线

### U2 CSB/SDO

U2 CSB pin 2 接 +3.3V，SDO pin 5 接 GND，页面未绘出跳线或外部可变选择器。

- 参数与网络：`device=BMP280`；`csb=pin 2,+3.3V`；`sdo=pin 5,GND`；`selector=null`
- 证据：图 13cfdf5a43da / 第 1 页 / 页 1 左下 U2 CSB pin 2 的 +3.3V 连线及 SDO pin 5 的 GND 汇线

### U1 ALERT

U1 ALERT pin 3 在原理图中未连接，未引至 J1 或其他器件。

- 参数与网络：`device=SHT30-DIS-B`；`pin=ALERT pin 3`；`connection=null`
- 证据：图 13cfdf5a43da / 第 1 页 / 页 1 左上 U1 ALERT pin 3 左侧未连接端点

## 时钟

### 外部时钟

本页没有绘出晶振、振荡器或独立时钟网络；U2 SCK pin 4 在当前连接中使用 SCL 总线网络。

- 参数与网络：`external_crystal=null`；`external_oscillator=null`；`bmp280_sck=pin 4,SCL`
- 证据：图 13cfdf5a43da / 第 1 页 / 整页无晶振/振荡器位号；U2 SCK pin 4 连接 SCL

## 复位

### U1 nRESET

U1 nRESET pin 6 在原理图中未连接，页面未提供外部复位控制网络。

- 参数与网络：`device=SHT30-DIS-B`；`reset_pin=nRESET pin 6`；`connection=null`；`external_control=null`
- 证据：图 13cfdf5a43da / 第 1 页 / 页 1 左上 U1 nRESET pin 6 左侧未连接端点

## 保护电路

### Grove 与传感器保护

本页没有绘出 TVS、ESD 阵列、保险丝或反接保护器件。

- 参数与网络：`i2c_esd=null`；`power_tvs=null`；`fuse=null`；`reverse_polarity=null`
- 证据：图 13cfdf5a43da / 第 1 页 / 整页所有位号 U1/U2/U3/J1/R1/R2/C1-C5，无保护器件

## 关键网络

### Unit ENV-II 关键网络索引

关键路径为 J1 pin 3 VCC→U3→+3.3V→U1/U2，J1 pin 1 SCL→U1 pin 4/U2 pin 4，J1 pin 2 SDA→U1 pin 1/U2 pin 3；U1 ADDR 与 U2 SDO 接 GND。

- 参数与网络：`power_path=J1.3-U3-+3.3V-U1/U2`；`scl_path=J1.1-U1.4-U2.4`；`sda_path=J1.2-U1.1-U2.3`；`sht30_strap=U1.2-GND`；`bmp280_straps=U2.2-+3.3V,U2.5-GND`
- 证据：图 13cfdf5a43da / 第 1 页 / 整页 VCC/+3.3V/SCL/SDA/GND 同名网络与配置脚

## 传感器

### U1 SHT30-DIS-B

U1 SDA pin 1 接 SDA，ADDR pin 2 接 GND，ALERT pin 3 未接，SCL pin 4 接 SCL，VDD pin 5 接 +3.3V，nRESET pin 6 未接，R pin 7、VSS pin 8 与 dpad pin 9 接 GND。

- 参数与网络：`pin_1=SDA`；`pin_2=ADDR,GND`；`pin_3=ALERT no-connect`；`pin_4=SCL`；`pin_5=VDD,+3.3V`；`pin_6=nRESET no-connect`；`pin_7=R,GND`；`pin_8=VSS,GND`；`pin_9=dpad,GND`
- 证据：图 13cfdf5a43da / 第 1 页 / 页 1 左上 U1 pins 1~9、功能名、未连接端点和网络

### U2 BMP280

U2 GND pins 1/7 接 GND，CSB pin 2 接 +3.3V，SDI pin 3 接 SDA，SCK pin 4 接 SCL，SDO pin 5 接 GND，Vddio pin 6 与 Vdd pin 8 接 +3.3V。

- 参数与网络：`pin_1=GND`；`pin_2=CSB,+3.3V`；`pin_3=SDI,SDA`；`pin_4=SCK,SCL`；`pin_5=SDO,GND`；`pin_6=Vddio,+3.3V`；`pin_7=GND`；`pin_8=Vdd,+3.3V`
- 证据：图 13cfdf5a43da / 第 1 页 / 页 1 左下 U2 pins 1~8、SCK/SDI/CSB/SDO/Vdd/Vddio/GND 与网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit ENV-II | `sensor_1=U1 SHT30-DIS-B`；`sensor_2=U2 BMP280`；`bus=SCL,SDA`；`connector=J1 IIC_Socket_4P`；`power=VCC->U3 HT7533->+3.3V` |
| 传感器 | U1 SHT30-DIS-B | `pin_1=SDA`；`pin_2=ADDR,GND`；`pin_3=ALERT no-connect`；`pin_4=SCL`；`pin_5=VDD,+3.3V`；`pin_6=nRESET no-connect`；`pin_7=R,GND`；`pin_8=VSS,GND`；`pin_9=dpad,GND` |
| 传感器 | U2 BMP280 | `pin_1=GND`；`pin_2=CSB,+3.3V`；`pin_3=SDI,SDA`；`pin_4=SCK,SCL`；`pin_5=SDO,GND`；`pin_6=Vddio,+3.3V`；`pin_7=GND`；`pin_8=Vdd,+3.3V` |
| 接口 | J1 IIC_Socket_4P | `pin_1=IIC_SCL,SCL`；`pin_2=IIC_SDA,SDA`；`pin_3=VCC`；`pin_4=GND` |
| 总线 | SHT30/BMP280 共享 I2C | `controller=external I2C host`；`scl_devices=U1 pin4,U2 pin4`；`sda_devices=U1 pin1,U2 pin3`；`connector=J1 pins 1/2` |
| 电源 | SCL/SDA 上拉 | `scl_pullup=R1 4.7KΩ`；`sda_pullup=R2 4.7KΩ`；`pullup_rail=VCC`；`sensor_supply_rail=+3.3V` |
| GPIO 与控制信号 | U1 ADDR | `device=SHT30-DIS-B`；`pin=ADDR pin 2`；`strap=GND`；`selector=null` |
| GPIO 与控制信号 | U2 CSB/SDO | `device=BMP280`；`csb=pin 2,+3.3V`；`sdo=pin 5,GND`；`selector=null` |
| 总线地址 | SHT30 I2C 地址 | `device=SHT30-DIS-B`；`addr_pin=GND`；`schematic_address=null`；`address_source_needed=SHT30 datasheet` |
| 总线地址 | BMP280 I2C 地址 | `device=BMP280`；`sdo_pin=GND`；`csb_pin=+3.3V`；`schematic_address=null`；`address_source_needed=BMP280 datasheet` |
| 电源 | U3 HT7533 | `input=VIN pin 2,VCC`；`output=VOUT pin 3,+3.3V`；`ground=pin 1 GND`；`input_capacitor=C5 10uF`；`output_capacitors=C3 100nF,C4 10uF` |
| 电源 | U1/U2 +3.3V 供电 | `sht30_supply=U1 VDD pin5,+3.3V`；`sht30_ground=U1 pins7/8/9,GND`；`bmp280_supply=U2 pins8/6,+3.3V`；`bmp280_ground=U2 pins1/7,GND`；`decoupling=C1 100nF,C3 100nF,C4 10uF` |
| 电源 | VCC 与 I2C 上拉电平 | `connector_pin=J1 pin 3`；`net=VCC`；`loads=U3 VIN,R1,R2,C2,C5`；`schematic_voltage=null`；`sensor_supply=+3.3V`；`i2c_pullup_voltage=null` |
| 传感器 | ENV-II 测量参数 | `sensors=SHT30-DIS-B,BMP280`；`schematic_temperature_range=null`；`schematic_humidity_range=null`；`schematic_pressure_range=null`；`schematic_accuracy=null`；`schematic_sampling_rate=null` |
| 复位 | U1 nRESET | `device=SHT30-DIS-B`；`reset_pin=nRESET pin 6`；`connection=null`；`external_control=null` |
| GPIO 与控制信号 | U1 ALERT | `device=SHT30-DIS-B`；`pin=ALERT pin 3`；`connection=null` |
| 时钟 | 外部时钟 | `external_crystal=null`；`external_oscillator=null`；`bmp280_sck=pin 4,SCL` |
| 保护电路 | Grove 与传感器保护 | `i2c_esd=null`；`power_tvs=null`；`fuse=null`；`reverse_polarity=null` |
| 关键网络 | Unit ENV-II 关键网络索引 | `power_path=J1.3-U3-+3.3V-U1/U2`；`scl_path=J1.1-U1.4-U2.4`；`sda_path=J1.2-U1.1-U2.3`；`sht30_strap=U1.2-GND`；`bmp280_straps=U2.2-+3.3V,U2.5-GND` |

## 待确认事项

- `address.sht30-not-printed`：原理图明确显示 U1 ADDR 接 GND，但没有打印十六进制 I2C 地址，数字地址需结合 SHT30 地址规则确认。（证据：图 13cfdf5a43da / 第 1 页 / U1 ADDR/SCL/SDA 区域，页面无 0x 地址）
- `address.bmp280-not-printed`：原理图明确显示 U2 SDO 接 GND 且 CSB 接 +3.3V，但没有打印十六进制 I2C 地址，数字地址需结合 BMP280 地址规则确认。（证据：图 13cfdf5a43da / 第 1 页 / U2 SDO/CSB/SCK/SDI 区域，页面无 0x 地址）
- `power.vcc-rating-and-i2c-level-not-shown`：J1 pin 3、U3 VIN、R1/R2 和 C2/C5 使用 VCC 网络，但页面未打印 VCC 数值，因此无法仅凭原理图确认接口供电值及 SCL/SDA 上拉的绝对高电平。（证据：图 13cfdf5a43da / 第 1 页 / 页 1 J1/U3/R1/R2/C2/C5 的 VCC 网络，未见数值标注）
- `sensor.measurement-specs-not-shown`：原理图只给出 SHT30-DIS-B 与 BMP280 型号及电气连接，没有打印温度、湿度、气压量程、精度、采样速率或工作温度。（证据：图 13cfdf5a43da / 第 1 页 / U1/U2 器件符号仅含型号和引脚，整页无测量参数）
- `review.sht30-address`：ADDR 接 GND 时，SHT30-DIS-B 的 I2C 地址是否为 0x44？；原因：原理图未打印数字地址，需要 SHT30 数据手册的地址规则确认。
- `review.bmp280-address`：CSB 接 +3.3V、SDO 接 GND 时，BMP280 的 I2C 地址是否为 0x76？；原因：原理图未打印数字地址，需要 BMP280 数据手册的接口与地址规则确认。
- `review.vcc-i2c-level`：J1 VCC 的额定值以及 SCL/SDA 实际上拉高电平是多少？；原因：R1/R2 直接上拉到未标数值的 VCC，而两颗传感器供电为 +3.3V；需要硬件版本和额定接口定义确认。
- `review.measurement-specs`：当前整机的温度、湿度、气压量程、精度和工作温度分别是多少？；原因：这些参数未印在原理图，需结合 SHT30/BMP280 数据手册、外壳与整机测试条件确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `13cfdf5a43da111e5e08be9024ea0461c76eced298c28f7974c3684517d501e5` | `https://static-cdn.m5stack.com/resource/docs/products/unit/envII/envII_sch_01.webp` |

---

源文档：`zh_CN/unit/envII.md`

源文档 SHA-256：`566cdd26e9b4f32a21733f1536f42cc175a83d5f0d65cbc71c8090e7a290df8d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
