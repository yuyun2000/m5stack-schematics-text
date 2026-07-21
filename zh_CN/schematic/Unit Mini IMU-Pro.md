# Unit Mini IMU-Pro 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Mini IMU-Pro |
| SKU | U171 |
| 产品 ID | `unit-mini-imu-pro-d28db2be8dfa` |
| 源文档 | `zh_CN/unit/IMU Pro Mini Unit.md` |

## 概述

Unit Mini IMU-Pro 由 U2 BMI270、U3 BMM150 和 U4 BMP280 三颗传感器组成，没有本地主控；外部主机通过 J1 Grove 的 SCL/SDA 访问 BMI270 与 BMP280。BMM150 不直接挂在主 SCL/SDA 上，而是通过 BMM_SDA/BMM_SCL 连接 BMI270 的 ASDX/ASCX 辅助接口。J1 的 VCC_5V 经 U1 HX6306P332MR 生成 3V3，SW1 配合 R3 选择 BMI270 的 0x68 默认地址或 0x69 地址；BMM150/BMP280 地址与正文性能参数未在原理图中直接标注。

## 检索关键词

`Unit Mini IMU-Pro`、`U171`、`BMI270`、`BMM150`、`BMP280`、`HX6306P332MR`、`Grove I2C`、`J1 GROVE 4P`、`SCL`、`SDA`、`BMM_SCL`、`BMM_SDA`、`ASDX`、`ASCX`、`SDO`、`SW1`、`0x68`、`0x69`、`0x10`、`0x76`、`VCC_5V`、`3V3`、`R1 10K`、`R2 10K`、`R3 10K`、`INT1`、`INT2`、`DRDY`、`CSB`、`SDI`、`SCK`、`六轴 IMU`、`三轴磁力计`、`气压传感器`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | BMI270 | 主 I2C 六轴惯性传感器，并通过 ASDX/ASCX 辅助接口连接 BMM150 | 图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B3：U2 BMI270、SDX/SCX、ASDX/ASCX、SDO、INT1/INT2 与电源引脚 |
| U3 | BMM150 | 连接 BMI270 辅助 I2C 的三轴磁力传感器 | 图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 C3：U3 BMM150、BMM_SDA/BMM_SCL、电源与绑带引脚 |
| U4 | BMP280 | 直接连接主 SCL/SDA 总线的气压/温度传感器 | 图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 C2：U4 BMP280、SCK/SDI/CSB/SDO/VDD/VDDIO/GND |
| U1 | HX6306P332MR | 将 J1 输入的 VCC_5V 稳压为传感器使用的 3V3 | 图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B2：U1 HX6306P332MR，VIN/VOUT/GND 与 VCC_5V/3V3 |
| J1 | GROVE 4P | 外部主机的 SCL、SDA、VCC_5V、GND 接口 | 图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B1：J1 GROVE 4P 的 SCL/SDA/5V/GND 标注 |
| SW1 | SW-PWR | 选择 BMI270 SDO 电平，从而切换图中标注的 I2C 地址 0x68/0x69 | 图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B2-B3：SW1、3V3、R3 与 BMI270 I2C Address 注释 |
| R1,R2 | 10K | 分别将 SCL 与 SDA 上拉到 3V3 | 图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B1-B2：R1/R2 10K 从 3V3 到 SCL/SDA |
| R3 | 10K | BMI270 SDO 地址选择节点下拉电阻 | 图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B3：U2 SDO/SW1 公共节点经 R3 10K 接 GND |
| C1,C2,C3,C4,C5,C6,C7,C8 | 100nF / 10uF | LDO 输入输出以及 BMI270、BMM150、BMP280 的电源去耦 | 图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B2-C3：C1-C8；C3=10uF，其余均标注 100nF |

## 系统结构

### Unit Mini IMU-Pro 系统架构

外部主机经 J1 SCL/SDA 直接连接 U2 BMI270 与 U4 BMP280；U2 再以 ASDX/ASCX 形成 BMM_SDA/BMM_SCL，连接 U3 BMM150。U1 从 VCC_5V 生成全板 3V3，完整单页没有本地主控、协处理器、存储器、电池或充电电路。

- 参数与网络：`external_controller=via J1 SCL/SDA`；`direct_i2c_devices=U2 BMI270,U4 BMP280`；`aux_i2c_device=U3 BMM150 via U2`；`power=VCC_5V -> U1 HX6306P332MR -> 3V3`；`local_controller=null`；`storage=null`；`battery=null`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页完整 A1-D4 原理图

## 电源

### VCC_5V 至 3V3 稳压

VCC_5V 接 U1 HX6306P332MR VIN，U1 VOUT pin2 输出 3V3，GND pin1 接地；C1 100nF 位于输入侧，C2 100nF 与 C3 10uF 位于 3V3 输出侧。

- 参数与网络：`input=VCC_5V`；`regulator=U1 HX6306P332MR`；`output=VOUT pin2 3V3`；`ground=pin1 GND`；`input_cap=C1 100nF`；`output_caps=C2 100nF,C3 10uF`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B2：U1、C1/C2/C3 与 VCC_5V/3V3/GND

## 接口

### J1 Grove 接口

J1 GROVE 4P 的四个触点从上到下标注 SCL、SDA、5V、GND；5V 触点连接 VCC_5V，SCL/SDA 进入 3V3 上拉的主 I2C 总线。

- 参数与网络：`connector=J1 GROVE 4P`；`order_top_to_bottom=SCL,SDA,5V,GND`；`power_net=VCC_5V`；`ground=GND`；`signal_rail=3V3 via R1/R2`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B1：J1 与 SCL/SDA/VCC_5V/GND 网络

## 总线

### 主 SCL/SDA I2C 总线

J1 SCL 同名网络连接 U2 BMI270 SCX pin13 和 U4 BMP280 SCK pin4；J1 SDA 连接 U2 SDX pin14 和 U4 SDI pin3。R1/R2 各 10K，分别将 SCL/SDA 上拉到 3V3。

- 参数与网络：`controller=external via J1`；`scl=J1 SCL -> U2 SCX pin13,U4 SCK pin4`；`sda=J1 SDA -> U2 SDX pin14,U4 SDI pin3`；`pullups=R1 10K SCL,R2 10K SDA to 3V3`；`devices=BMI270,BMP280`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B1-C2：J1、R1/R2、U2 SDX/SCX 与 U4 SDI/SCK

### BMI270 辅助 I2C 与 BMM150

U2 BMI270 ASDX pin2 输出/接收 BMM_SDA，ASCX pin3 输出 BMM_SCL；BMM_SDA 连接 U3 BMM150 SDI B4，BMM_SCL 连接 U3 SCK A3。该辅助总线未直接连接 J1 SCL/SDA，页面也未显示外部上拉电阻。

- 参数与网络：`hub=U2 BMI270`；`device=U3 BMM150`；`sda=U2 ASDX pin2 BMM_SDA -> U3 SDI B4`；`scl=U2 ASCX pin3 BMM_SCL -> U3 SCK A3`；`host_direct_connection=false`；`external_pullups_shown=false`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B3-C3：U2 ASDX/ASCX、BMM_SDA/BMM_SCL 与 U3 SDI/SCK

## 总线地址

### BMI270 I2C 地址选择

原理图注释明确给出 BMI270：SDO=1 时地址 0x69，SDO=0 时地址 0x68（Default）。U2 SDO pin1 接 SW1 pin2 公共端并由 R3 10K 下拉至 GND，SW1 pin3 接 3V3，pin1 未外接。

- 参数与网络：`device=U2 BMI270`；`selector_pin=SDO pin1`；`sd0_high=0x69`；`sd0_low=0x68`；`default=0x68`；`switch=SW1 pin2 common,pin3 3V3,pin1 NC`；`pulldown=R3 10K to GND`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B2-B3：BMI270 I2C Address 注释、SW1、R3 与 U2 SDO

## GPIO 与控制信号

### 传感器中断与数据就绪引脚

U2 BMI270 INT1 pin4 与 INT2 pin9 未接线，OSDO pin11 与 OCSB pin10 标为不连接；U3 BMM150 DRDY D4 与 INT D2 也标为不连接。J1 只引出 SCL/SDA，没有中断线。

- 参数与网络：`bmi270=INT1 pin4 NC,INT2 pin9 NC,OSDO pin11 NC,OCSB pin10 NC`；`bmm150=DRDY D4 NC,INT D2 NC`；`external_interrupt=null`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B3-C3：U2 INT1/INT2/OSDO/OCSB 与 U3 DRDY/INT 的无连接标记

## 时钟

### 时钟、复位与调试电路

完整单页没有外部晶振、振荡器、RESET/BOOT 网络或调试连接器；板上仅包含 LDO、三颗传感器、地址开关、Grove 接口及其阻容网络。

- 参数与网络：`external_crystal=false`；`oscillator=false`；`reset_net=null`；`boot_net=null`；`debug_connector=null`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页完整 A1-D4 原理图，无晶振、复位、启动或调试器件

## 保护电路

### Grove 输入与信号保护拓扑

J1 VCC_5V 直接进入 U1 输入，SCL/SDA 直接连接 R1/R2 与传感器；本页未显示保险丝、TVS/ESD 二极管、反接二极管、串联限流电阻或电平转换器。

- 参数与网络：`power_path=J1 VCC_5V -> U1 VIN`；`signal_path=J1 SCL/SDA -> R1/R2,U2,U4`；`fuse_shown=false`；`tvs_esd_shown=false`；`reverse_protection_shown=false`；`level_shifter_shown=false`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B1-C3：J1 至 U1/U2/U4 的完整电源和信号路径

## 关键网络

### 3V3 传感器电源网络

3V3 同名网络为 U2 BMI270、U3 BMM150、U4 BMP280 供电，并连接 R1/R2 I2C 上拉和 SW1 地址选择；C2-C8 构成输出与各传感器去耦，其中 C3 为 10uF，其余为 100nF。

- 参数与网络：`rail=3V3`；`loads=U2 BMI270,U3 BMM150,U4 BMP280,R1,R2,SW1`；`bulk_cap=C3 10uF`；`decoupling=C2,C4,C5,C6,C7,C8 100nF`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页完整 3V3 同名电源网络及 C2-C8

## 传感器

### U2 BMI270 主机接口与供电

U2 BMI270 的 SDX pin14 接 SDA、SCX pin13 接 SCL；VDD pin8、VDDIO pin5 与 CSB pin12 接 3V3，GNDIO pin6/GND pin7 接地，C5/C6 各 100nF 对 3V3 去耦。

- 参数与网络：`sda=SDX pin14 SDA`；`scl=SCX pin13 SCL`；`vdd=pin8 3V3`；`vddio=pin5 3V3`；`csb=pin12 3V3`；`ground=pins6/7 GND`；`decoupling=C5,C6 100nF`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 B3：U2 BMI270 主 I2C、电源、CSB 与 C5/C6

### U3 BMM150 电源与模式绑带

U3 BMM150 的 VDD E5 与 VDDIO B2 接 3V3，GND C5/GND E3/GNDIO E1 接地；PS A1、SDO C1 与 CSB A5 接 GND。C4/C7 各 100nF，分别位于 3V3 电源去耦支路。

- 参数与网络：`vdd=E5 3V3`；`vddio=B2 3V3`；`grounds=C5,E3,E1 GND`；`ps=A1 GND`；`sdo=C1 GND`；`csb=A5 GND`；`decoupling=C4,C7 100nF`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 C3：U3 BMM150 的 A1/B2/C1/C5/D2/D4/E1/E3/E5/A3/A5/B4 引脚与 C4/C7

### U4 BMP280 电源与 I2C 连接

U4 BMP280 的 SCK pin4 接 SCL、SDI pin3 接 SDA；VDD pin8、VDDIO pin6 与 CSB pin2 接 3V3，SDO pin5 与 GND pin1/pin7 接 GND，C8 100nF 跨接 3V3 与 GND。

- 参数与网络：`scl=SCK pin4 SCL`；`sda=SDI pin3 SDA`；`vdd=pin8 3V3`；`vddio=pin6 3V3`；`csb=pin2 3V3`；`sdo=pin5 GND`；`ground=pins1/7 GND`；`decoupling=C8 100nF`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页网格 C2：U4 BMP280 全部 pin1-pin8 与 C8

## 其他事实

### 本地处理与其他功能分区

本页未包含本地主控、存储器、射频、音频、显示、用户按键或执行器；测量数据只能通过 J1 I2C 路径由外部控制器读取，SW1 仅连接 BMI270 SDO 地址选择节点。

- 参数与网络：`local_mcu=null`；`memory=null`；`storage=null`；`rf=null`；`audio=null`；`display=null`；`actuator=null`；`data_interface=J1 I2C`；`local_switch=SW1 BMI270 address`
- 证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页完整 A1-D4 原理图

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Mini IMU-Pro 系统架构 | `external_controller=via J1 SCL/SDA`；`direct_i2c_devices=U2 BMI270,U4 BMP280`；`aux_i2c_device=U3 BMM150 via U2`；`power=VCC_5V -> U1 HX6306P332MR -> 3V3`；`local_controller=null`；`storage=null`；`battery=null` |
| 接口 | J1 Grove 接口 | `connector=J1 GROVE 4P`；`order_top_to_bottom=SCL,SDA,5V,GND`；`power_net=VCC_5V`；`ground=GND`；`signal_rail=3V3 via R1/R2` |
| 电源 | VCC_5V 至 3V3 稳压 | `input=VCC_5V`；`regulator=U1 HX6306P332MR`；`output=VOUT pin2 3V3`；`ground=pin1 GND`；`input_cap=C1 100nF`；`output_caps=C2 100nF,C3 10uF` |
| 总线 | 主 SCL/SDA I2C 总线 | `controller=external via J1`；`scl=J1 SCL -> U2 SCX pin13,U4 SCK pin4`；`sda=J1 SDA -> U2 SDX pin14,U4 SDI pin3`；`pullups=R1 10K SCL,R2 10K SDA to 3V3`；`devices=BMI270,BMP280` |
| 传感器 | U2 BMI270 主机接口与供电 | `sda=SDX pin14 SDA`；`scl=SCX pin13 SCL`；`vdd=pin8 3V3`；`vddio=pin5 3V3`；`csb=pin12 3V3`；`ground=pins6/7 GND`；`decoupling=C5,C6 100nF` |
| 总线地址 | BMI270 I2C 地址选择 | `device=U2 BMI270`；`selector_pin=SDO pin1`；`sd0_high=0x69`；`sd0_low=0x68`；`default=0x68`；`switch=SW1 pin2 common,pin3 3V3,pin1 NC`；`pulldown=R3 10K to GND` |
| 总线 | BMI270 辅助 I2C 与 BMM150 | `hub=U2 BMI270`；`device=U3 BMM150`；`sda=U2 ASDX pin2 BMM_SDA -> U3 SDI B4`；`scl=U2 ASCX pin3 BMM_SCL -> U3 SCK A3`；`host_direct_connection=false`；`external_pullups_shown=false` |
| 传感器 | U3 BMM150 电源与模式绑带 | `vdd=E5 3V3`；`vddio=B2 3V3`；`grounds=C5,E3,E1 GND`；`ps=A1 GND`；`sdo=C1 GND`；`csb=A5 GND`；`decoupling=C4,C7 100nF` |
| 传感器 | U4 BMP280 电源与 I2C 连接 | `scl=SCK pin4 SCL`；`sda=SDI pin3 SDA`；`vdd=pin8 3V3`；`vddio=pin6 3V3`；`csb=pin2 3V3`；`sdo=pin5 GND`；`ground=pins1/7 GND`；`decoupling=C8 100nF` |
| 总线地址 | BMM150 与 BMP280 I2C 地址 | `documented_bmm150=0x10`；`documented_bmp280=0x76`；`bmm150_straps=SDO GND,CSB GND`；`bmp280_straps=SDO GND,CSB 3V3`；`schematic_numeric_addresses=null` |
| GPIO 与控制信号 | 传感器中断与数据就绪引脚 | `bmi270=INT1 pin4 NC,INT2 pin9 NC,OSDO pin11 NC,OCSB pin10 NC`；`bmm150=DRDY D4 NC,INT D2 NC`；`external_interrupt=null` |
| 关键网络 | 3V3 传感器电源网络 | `rail=3V3`；`loads=U2 BMI270,U3 BMM150,U4 BMP280,R1,R2,SW1`；`bulk_cap=C3 10uF`；`decoupling=C2,C4,C5,C6,C7,C8 100nF` |
| 保护电路 | Grove 输入与信号保护拓扑 | `power_path=J1 VCC_5V -> U1 VIN`；`signal_path=J1 SCL/SDA -> R1/R2,U2,U4`；`fuse_shown=false`；`tvs_esd_shown=false`；`reverse_protection_shown=false`；`level_shifter_shown=false` |
| 时钟 | 时钟、复位与调试电路 | `external_crystal=false`；`oscillator=false`；`reset_net=null`；`boot_net=null`；`debug_connector=null` |
| 传感器 | 正文传感器自由度与精度 | `documented_dof=10`；`documented_bmi270_acceleration_accuracy=0.05%`；`documented_bmi270_angular_accuracy=0.05deg/s`；`documented_bmm150_accuracy=0.3uT`；`documented_bmp280_temperature_accuracy=+/-1degC`；`documented_bmp280_pressure_accuracy=+/-1Pa`；`schematic_performance_values=null` |
| 其他事实 | 本地处理与其他功能分区 | `local_mcu=null`；`memory=null`；`storage=null`；`rf=null`；`audio=null`；`display=null`；`actuator=null`；`data_interface=J1 I2C`；`local_switch=SW1 BMI270 address` |

## 待确认事项

- `address.bmm150-bmp280`：正文列出 BMM150 地址 0x10、BMP280 地址 0x76；原理图确认 BMM150 的 SDO/CSB 接 GND、BMP280 的 SDO 接 GND且 CSB 接 3V3，但图中没有打印这两个十六进制地址，也没有总线扫描结果。（证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页 U3/U4 绑带连接；仅 BMI270 区域印有地址文字）
- `sensor.documented-performance`：正文称本单元为 10 自由度，并列出 BMI270 加速度精度 0.05%、角速度精度 0.05°/s、BMM150 精度 0.3uT、BMP280 温度精度 ±1°C 和气压精度 ±1Pa；原理图只确认器件型号与电气连接，没有量程、精度、采样率、噪声、校准或温度条件。（证据：图 87d11a92a8d3 / 第 1 页 / 第 1 页 U2 BMI270、U3 BMM150、U4 BMP280；整页无性能参数）
- `review.bmm150-bmp280-addresses`：请用当前器件 datasheet 或实机总线访问记录确认 BMM150=0x10、BMP280=0x76，以及 BMM150 经 BMI270 辅助总线的初始化方式。；原因：原理图显示绑带和总线拓扑，但没有打印 BMM150/BMP280 的数字地址。
- `review.sensor-performance`：请按当前 BMI270、BMM150、BMP280 datasheet 与整机测试条件复核 10 自由度定义、各项精度、量程、采样率、噪声和校准要求。；原因：器件连接原理图不能证明正文中的测量性能及适用条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `87d11a92a8d3e5fe9ad1a8563ed45ab55017906e2ecf38f2c042092d2f87d4e4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/625/SCH_UNIT_IMU_ProV1.0_sch_01.png` |

---

源文档：`zh_CN/unit/IMU Pro Mini Unit.md`

源文档 SHA-256：`2224319728cd01f5faa05121823a06a3b3bc00dd0206e19f22ea243ffb2f25a3`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
