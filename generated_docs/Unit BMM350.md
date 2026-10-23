# Unit BMM350 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit BMM350 |
| SKU | U231 |
| 产品 ID | `unit-bmm350-88be2b4d449c` |
| 源文档 | `zh_CN/unit/Unit_BMM350.md` |

## 概述

Unit BMM350 以 BMM350 三轴磁力计为核心。GROVE_IO 提供 VCC_5V 与 I2C，ME6206A33M3G 将 5V 转为 3V3，SSP7615-18 将 3V3 转为 1V8；BMM350 的 SCL/SDA 经 R4/R5 0R 并入总线，ADSEL 接地。原理图还保留 BMI270 和 8 脚传感器位置，但这两个位置均标为 NC。

## 检索关键词

`Unit BMM350`、`U231`、`BMM350`、`ME6206A33M3G`、`SSP7615-18`、`GROVE_IO`、`I2C`、`SCL`、`SDA`、`BMM_SCL`、`BMM_SDA`、`VCC_5V`、`3V3`、`1V8`、`ADSEL`、`CRST`、`BYPASS`、`VDD`、`VDDIO`、`R1`、`R2`、`4.7K`、`R4`、`R5`、`0R`、`0x14`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ME6206A33M3G | 5V 转 3.3V LDO | 图 5597bc388a45 / 第 1 页 / B 区中部：U1 型号与 VIN/VOUT/GND |
| U2 | BMI270 | 可选 BMI270 六轴 IMU 位置，符号下方标注 NC | 图 5597bc388a45 / 第 1 页 / B 区右侧：U2 BMI270 与 NC 标注 |
| U4 | 未标注 | 可选 8 脚传感器位置，符号下方标注 NC 且未给出型号 | 图 5597bc388a45 / 第 1 页 / C 区左侧：U4 1~8 脚与 NC 标注 |
| U5 | SSP7615-18 | 3V3 转 1V8 LDO | 图 5597bc388a45 / 第 1 页 / D 区中部：U5 SSP7615-18 与 VIN/OUT/EN/GND_EP |
| BMM350 | BMM350 | 三轴磁力计核心器件；可见符号未单列 U 位号 | 图 5597bc388a45 / 第 1 页 / C 区右侧：绿色 BMM350 符号及 A1~C3 引脚 |
| J1 | GROVE_IO | I2C 接口：IO2=SCL、IO1=SDA、VCC=VCC_5V、GND | 图 5597bc388a45 / 第 1 页 / B 区左侧：J1 GROVE_IO 与网络名 |
| SW1 | SW-PWR | BMI270 SDO 地址选择开关，可将 SDO 接至 3V3 | 图 5597bc388a45 / 第 1 页 / B 区右侧：SW1 与 SDO/R3 |
| R1 / R2 | 4.7K | SCL 与 SDA 上拉到 3V3 | 图 5597bc388a45 / 第 1 页 / B 区左侧 J1 上方：R1、R2 4.7K |
| R3 | 10K | BMI270 SDO 下拉至 GND | 图 5597bc388a45 / 第 1 页 / B 区右侧：R3 10K 至 GND |
| R4 / R5 | 0R | BMM_SCL/BMM_SDA 到 SCL/SDA 的串联连接电阻 | 图 5597bc388a45 / 第 1 页 / C 区右侧：R4、R5 0R |
| C1 | 10uF | VCC_5V 输入滤波 | 图 5597bc388a45 / 第 1 页 / B 区中部：C1 10uF |
| C2 | 100nF | 3V3 输出高频滤波 | 图 5597bc388a45 / 第 1 页 / B 区中部：C2 100nF |
| C3 | 10uF | 3V3 输出储能滤波 | 图 5597bc388a45 / 第 1 页 / B 区中部：C3 10uF |
| C5 / C6 | 100nF | BMI270 VDD 与 VDDIO 去耦 | 图 5597bc388a45 / 第 1 页 / B 区右侧：C5、C6 各 100nF |
| C8 | 100nF | U4 VDDIO 去耦 | 图 5597bc388a45 / 第 1 页 / C 区左侧：C8 100nF |
| C4 | 100nF | BMM350 3V3/VDDIO 去耦 | 图 5597bc388a45 / 第 1 页 / C 区右侧 BMM350 左侧：C4 100nF |
| C7 | 100nF | BMM350 1V8/VDD 去耦 | 图 5597bc388a45 / 第 1 页 / C 区右侧 BMM350 左侧：C7 100nF |
| C9 | 2.2uF | BMM350 CRST 对地电容 | 图 5597bc388a45 / 第 1 页 / C 区右侧 BMM350 左侧：C9 2.2uF |
| C10 / C11 | 104 | 1V8 LDO 输入与输出滤波 | 图 5597bc388a45 / 第 1 页 / D 区中部：C10、C11 均标 104 |

## 系统结构

### Unit BMM350

当前产品的有效传感器路径为 BMM350；同一原理图中的 U2 BMI270 位置和 U4 八脚传感器位置均标注 NC。

- 参数与网络：`active_sensor=BMM350`；`u2_population=NC`；`u4_population=NC`
- 证据：图 5597bc388a45 / 第 1 页 / B/C 区：BMM350 符号、U2 NC、U4 NC

## 核心器件

### U2

U2 位置标注 BMI270，并在符号下方标注 NC；BMI270 的 VDD/VDDIO/CSB、SDO/SDX/SCX 与 GND 连接仍绘制在原理图中。

- 参数与网络：`part=BMI270`；`population=NC`
- 证据：图 5597bc388a45 / 第 1 页 / B 区右侧：U2 BMI270 与 NC

### U4

U4 为标有 NC 的八脚位置：SCK(4)=SCL、SDI(3)=SDA、CSB(2)=3V3、VDD(8)=VDDIO(6)=3V3、SDO(5)=GND、GND(1,7)=GND；该符号未给出型号。

- 参数与网络：`population=NC`；`sck_pin=4`；`sdi_pin=3`；`csb_pin=2`；`vdd_pin=8`；`vddio_pin=6`；`sdo_pin=5`
- 证据：图 5597bc388a45 / 第 1 页 / C 区左侧：U4 引脚与 NC

## 电源

### U1

VCC_5V 接 U1(ME6206A33M3G) 的 VIN(3)，VOUT(2) 输出 3V3，GND(1) 接地；输入 C1=10uF，输出 C2=100nF、C3=10uF。

- 参数与网络：`vin=VCC_5V`；`vout=3V3`；`vin_pin=3`；`vout_pin=2`；`gnd_pin=1`；`c1=10uF`；`c2=100nF`；`c3=10uF`
- 证据：图 5597bc388a45 / 第 1 页 / B 区中部：U1 与 C1-C3

### U5

U5(SSP7615-18) 的 VIN(4)=3V3、EN(3)=3V3、OUT(1)=1V8，GND(2) 与 GND_EP(5) 接地；输入 C10 与输出 C11 均标 104。

- 参数与网络：`part=SSP7615-18`；`vin=3V3`；`vout=1V8`；`enable=3V3`；`c10=104`；`c11=104`
- 证据：图 5597bc388a45 / 第 1 页 / D 区中部：U5 与 C10/C11

### BMM350

BMM350 的 VDDIO(B3) 接 3V3，VDD(C1) 接 1V8；CRST(C2) 经 C9(2.2uF) 到地，BYPASS(C3) 接地；C4 与 C7 均为 100nF。

- 参数与网络：`vddio=3V3`；`vdd=1V8`；`crst_cap=C9 2.2uF`；`bypass=GND`；`c4=100nF`；`c7=100nF`
- 证据：图 5597bc388a45 / 第 1 页 / C 区右侧 BMM350 左侧：VDDIO/VDD/CRST/BYPASS 与 C4/C7/C9

## 接口

### J1

J1(GROVE_IO)：IO2=SCL，IO1=SDA，VCC=VCC_5V，GND=GND。

- 参数与网络：`io2=SCL`；`io1=SDA`；`vcc=VCC_5V`；`gnd=GND`
- 证据：图 5597bc388a45 / 第 1 页 / B 区左侧：J1 GROVE_IO

## 总线

### R1/R2

SCL 与 SDA 分别经 R1、R2（4.7K）上拉到 3V3。

- 参数与网络：`scl_pullup=R1 4.7K`；`sda_pullup=R2 4.7K`；`pullup_rail=3V3`
- 证据：图 5597bc388a45 / 第 1 页 / B 区左侧 J1 上方：R1/R2

### BMM350

BMM350 的 SCK(A3) 为 BMM_SCL，经 R4(0R) 接 SCL；SDA(A2) 为 BMM_SDA，经 R5(0R) 接 SDA。

- 参数与网络：`sck_pin=A3`；`sda_pin=A2`；`r4=0R`；`r5=0R`
- 证据：图 5597bc388a45 / 第 1 页 / C 区右侧：BMM350 SCK/SDA 与 R4/R5

## 总线地址

### BMM350 ADSEL

BMM350 的 ADSEL(B2) 与 GND(B1) 接到同一 GND 网络，地址选择脚固定为低电平。

- 参数与网络：`adsel_pin=B2`；`gnd_pin=B1`；`adsel_level=low`
- 证据：图 5597bc388a45 / 第 1 页 / C 区右侧：BMM350 ADSEL(B2)/GND(B1) 与地网络

## GPIO 与控制信号

### BMM350 INT

BMM350 的 INT(A1) 引脚只绘出短引脚线，未连接命名网络、GROVE 接口或其他器件。

- 参数与网络：`pin=A1`；`net=null`
- 证据：图 5597bc388a45 / 第 1 页 / C 区右侧：BMM350 INT(A1)

## 关键网络

### I2C nets

外部 I2C 网络名称为 SCL/SDA；BMM350 侧网络名称为 BMM_SCL/BMM_SDA，两组网络分别通过 R4/R5 的 0R 电阻连接。

- 参数与网络：`external_scl=SCL`；`external_sda=SDA`；`sensor_scl=BMM_SCL`；`sensor_sda=BMM_SDA`；`series_resistors=R4/R5 0R`
- 证据：图 5597bc388a45 / 第 1 页 / B/C 区：SCL/SDA、BMM_SCL/BMM_SDA 与 R4/R5

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit BMM350 | `active_sensor=BMM350`；`u2_population=NC`；`u4_population=NC` |
| 电源 | U1 | `vin=VCC_5V`；`vout=3V3`；`vin_pin=3`；`vout_pin=2`；`gnd_pin=1`；`c1=10uF`；`c2=100nF`；`c3=10uF` |
| 电源 | U5 | `part=SSP7615-18`；`vin=3V3`；`vout=1V8`；`enable=3V3`；`c10=104`；`c11=104` |
| 接口 | J1 | `io2=SCL`；`io1=SDA`；`vcc=VCC_5V`；`gnd=GND` |
| 总线 | R1/R2 | `scl_pullup=R1 4.7K`；`sda_pullup=R2 4.7K`；`pullup_rail=3V3` |
| 总线 | BMM350 | `sck_pin=A3`；`sda_pin=A2`；`r4=0R`；`r5=0R` |
| 电源 | BMM350 | `vddio=3V3`；`vdd=1V8`；`crst_cap=C9 2.2uF`；`bypass=GND`；`c4=100nF`；`c7=100nF` |
| 总线地址 | BMM350 ADSEL | `adsel_pin=B2`；`gnd_pin=B1`；`adsel_level=low` |
| 总线地址 | BMM350 I2C address | `documented_address=0x14`；`adsel_level=low` |
| 核心器件 | U2 | `part=BMI270`；`population=NC` |
| 核心器件 | U4 | `population=NC`；`sck_pin=4`；`sdi_pin=3`；`csb_pin=2`；`vdd_pin=8`；`vddio_pin=6`；`sdo_pin=5` |
| GPIO 与控制信号 | BMM350 INT | `pin=A1`；`net=null` |
| 关键网络 | I2C nets | `external_scl=SCL`；`external_sda=SDA`；`sensor_scl=BMM_SCL`；`sensor_sda=BMM_SDA`；`series_resistors=R4/R5 0R` |

## 待确认事项

- `address.bmm350-value`：产品清单给出的 BMM350 I2C 地址为 0x14。原理图将 ADSEL(B2) 与 GND(B1) 接地，但页内没有打印地址值。（证据：图 5597bc388a45 / 第 1 页 / C 区右侧：BMM350 ADSEL(B2)/GND(B1)）
- `nr-bmm350-address`：请以 BMM350 数据手册确认 ADSEL 低电平时对应的 I2C 地址是否为 0x14。；原因：产品清单给出 0x14，原理图只明确 ADSEL(B2) 接地，未在页内打印地址值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5597bc388a459abe0070e3b551b41f9d554fa4dedaa1ea50443246602dfb9fcb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1293/U231_Unit_BMM350_sche_page_01.png` |

---

源文档：`zh_CN/unit/Unit_BMM350.md`

源文档 SHA-256：`ac12c0d461dfbe167e3f86508138e73be3ef1b648e3351cf714d3c10dbba4e34`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
