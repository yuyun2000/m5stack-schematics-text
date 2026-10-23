# Unit DoF10 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit DoF10 |
| SKU | U230 |
| 产品 ID | `unit-dof10-6864dc726831` |
| 源文档 | `zh_CN/unit/Unit_DoF10.md` |

## 概述

Unit DoF10 集成 BMI270、BMM350 与 SPA06-003，三者共用 GROVE_IO 的 I2C 总线。ME6206A33M3G 将 5V 转为 3V3，SSP7615-18DFR 将 3V3 转为 1V8 供 BMM350；BMI270 的 SDO 由 SW1/R3 选择 0x68 或 0x69。SCL/SDA 由 R1/R2 上拉，BMM350 经 R4/R5 0R 接入，SPA06-003 与 BMI270 由 3V3 供电。

## 检索关键词

`Unit DoF10`、`U230`、`BMI270`、`BMM350`、`SPA06-003`、`ME6206A33M3G`、`SSP7615-18DFR`、`GROVE_IO`、`I2C`、`SCL`、`SDA`、`BMM_SCL`、`BMM_SDA`、`0x68`、`0x69`、`0x14`、`0x76`、`SDO`、`SW1`、`R3`、`ADSEL`、`CRST`、`BYPASS`、`VDD`、`VDDIO`、`VCC_5V`、`3V3`、`1V8`、`INT1`、`INT2`、`CSB`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ME6206A33M3G | 5V 转 3.3V LDO | 图 ff9fd127d707 / 第 1 页 / B 区中部：U1 型号与 VIN/VOUT/GND |
| U2 | BMI270 | 六轴 IMU，I2C 从机 | 图 ff9fd127d707 / 第 1 页 / B 区右侧：U2 BMI270 与 1~14 脚 |
| U4 | SPA06-003 | 气压/温度传感器，I2C 从机 | 图 ff9fd127d707 / 第 1 页 / C 区左侧：U4 SPA06-003 与 1~8 脚 |
| U5 | SSP7615-18DFR | 3V3 转 1V8 LDO | 图 ff9fd127d707 / 第 1 页 / D 区中部：U5 SSP7615-18DFR 与 VIN/OUT/EN/GND_EP |
| BMM350 | BMM350 | 三轴磁力计；可见符号未单列 U 位号 | 图 ff9fd127d707 / 第 1 页 / C 区右侧：绿色 BMM350 符号及 A1~C3 引脚 |
| J1 | GROVE_IO | I2C 接口：IO2=SCL、IO1=SDA、VCC=VCC_5V、GND | 图 ff9fd127d707 / 第 1 页 / B 区左侧：J1 GROVE_IO 与网络名 |
| SW1 | SW-PWR | BMI270 SDO 地址选择开关，可将 SDO 接至 3V3 | 图 ff9fd127d707 / 第 1 页 / B 区右侧：SW1 与 SDO/R3 |
| R1 / R2 | 4.7K | SCL 与 SDA 上拉到 3V3 | 图 ff9fd127d707 / 第 1 页 / B 区左侧 J1 上方：R1、R2 4.7K |
| R3 | 10K | BMI270 SDO 下拉至 GND | 图 ff9fd127d707 / 第 1 页 / B 区右侧：R3 10K 至 GND |
| R4 / R5 | 0R | BMM_SCL/BMM_SDA 到 SCL/SDA 的串联连接电阻 | 图 ff9fd127d707 / 第 1 页 / C 区右侧：R4、R5 0R |
| C1 | 10uF | VCC_5V 输入滤波 | 图 ff9fd127d707 / 第 1 页 / B 区中部：C1 10uF |
| C2 | 100nF | 3V3 输出高频滤波 | 图 ff9fd127d707 / 第 1 页 / B 区中部：C2 100nF |
| C3 | 10uF | 3V3 输出储能滤波 | 图 ff9fd127d707 / 第 1 页 / B 区中部：C3 10uF |
| C5 / C6 | 100nF | BMI270 VDD 与 VDDIO 去耦 | 图 ff9fd127d707 / 第 1 页 / B 区右侧：C5、C6 各 100nF |
| C8 | 100nF | SPA06-003 VDDIO 去耦 | 图 ff9fd127d707 / 第 1 页 / C 区左侧：C8 100nF |
| C4 | 100nF | BMM350 3V3/VDDIO 去耦 | 图 ff9fd127d707 / 第 1 页 / C 区右侧 BMM350 左侧：C4 100nF |
| C7 | 100nF | BMM350 1V8/VDD 去耦 | 图 ff9fd127d707 / 第 1 页 / C 区右侧 BMM350 左侧：C7 100nF |
| C9 | 2.2uF | BMM350 CRST 对地电容 | 图 ff9fd127d707 / 第 1 页 / C 区右侧 BMM350 左侧：C9 2.2uF |
| C10 / C11 | 104 | 1V8 LDO 输入与输出滤波 | 图 ff9fd127d707 / 第 1 页 / D 区中部：C10、C11 均标 104 |

## 系统结构

### Unit DoF10

Unit DoF10 的传感器组合为 BMI270、BMM350 与 SPA06-003，三个器件均接入 SCL/SDA I2C 总线并由同一 GROVE_IO 对外连接。

- 参数与网络：`imu=BMI270`；`magnetometer=BMM350`；`pressure_sensor=SPA06-003`；`external_connector=J1 GROVE_IO`
- 证据：图 ff9fd127d707 / 第 1 页 / B/C 区：U2 BMI270、BMM350、U4 SPA06-003 与 J1

## 核心器件

### U2

BMI270 的 VDD(8) 与 VDDIO(5) 均接 3V3，CSB(12) 接 VDDIO 所在 3V3 网络，GNDIO(6) 与 GND(7) 接地；C5、C6 各 100nF。

- 参数与网络：`vdd=3V3`；`vddio=3V3`；`csb=3V3`；`c5=100nF`；`c6=100nF`
- 证据：图 ff9fd127d707 / 第 1 页 / B 区右侧：U2 电源脚、CSB 与 C5/C6

### U4

SPA06-003 的 SCK(4)=SCL、SDI(3)=SDA、CSB(2)=3V3、VDD(8)=VDDIO(6)=3V3、SDO(5)=GND、GND(1,7)=GND，C8 为 100nF。

- 参数与网络：`sck_pin=4`；`sdi_pin=3`；`csb_pin=2`；`vdd_pin=8`；`vddio_pin=6`；`sdo_pin=5`；`c8=100nF`
- 证据：图 ff9fd127d707 / 第 1 页 / C 区左侧：U4 SPA06-003、1~8 脚与 C8

## 电源

### U1

VCC_5V 接 U1(ME6206A33M3G) 的 VIN(3)，VOUT(2) 输出 3V3，GND(1) 接地；输入 C1=10uF，输出 C2=100nF、C3=10uF。

- 参数与网络：`vin=VCC_5V`；`vout=3V3`；`vin_pin=3`；`vout_pin=2`；`gnd_pin=1`；`c1=10uF`；`c2=100nF`；`c3=10uF`
- 证据：图 ff9fd127d707 / 第 1 页 / B 区中部：U1 与 C1-C3

### U5

U5(SSP7615-18DFR) 的 VIN(4)=3V3、EN(3)=3V3、OUT(1)=1V8，GND(2) 与 GND_EP(5) 接地；输入 C10 与输出 C11 均标 104。

- 参数与网络：`part=SSP7615-18DFR`；`vin=3V3`；`vout=1V8`；`enable=3V3`；`c10=104`；`c11=104`
- 证据：图 ff9fd127d707 / 第 1 页 / D 区中部：U5 与 C10/C11

### BMM350

BMM350 的 VDDIO(B3) 接 3V3，VDD(C1) 接 1V8；CRST(C2) 经 C9(2.2uF) 到地，BYPASS(C3) 接地；C4 与 C7 均为 100nF。

- 参数与网络：`vddio=3V3`；`vdd=1V8`；`crst_cap=C9 2.2uF`；`bypass=GND`；`c4=100nF`；`c7=100nF`
- 证据：图 ff9fd127d707 / 第 1 页 / C 区右侧 BMM350 左侧：VDDIO/VDD/CRST/BYPASS 与 C4/C7/C9

## 接口

### J1

J1(GROVE_IO)：IO2=SCL，IO1=SDA，VCC=VCC_5V，GND=GND。

- 参数与网络：`io2=SCL`；`io1=SDA`；`vcc=VCC_5V`；`gnd=GND`
- 证据：图 ff9fd127d707 / 第 1 页 / B 区左侧：J1 GROVE_IO

## 总线

### R1/R2

SCL 与 SDA 分别经 R1、R2（4.7K）上拉到 3V3。

- 参数与网络：`scl_pullup=R1 4.7K`；`sda_pullup=R2 4.7K`；`pullup_rail=3V3`
- 证据：图 ff9fd127d707 / 第 1 页 / B 区左侧 J1 上方：R1/R2

### U2

BMI270 的 SDA(14) 接 SDA，SCX(13) 接 SCL；SDO(1) 接地址选择网络。

- 参数与网络：`sda_pin=14`；`scl_pin=13`；`sdo_pin=1`
- 证据：图 ff9fd127d707 / 第 1 页 / B 区右侧：U2 SDX/SCX/SDO 与网络名

### BMM350

BMM350 的 SCK(A3) 为 BMM_SCL，经 R4(0R) 接 SCL；SDA(A2) 为 BMM_SDA，经 R5(0R) 接 SDA；ADSEL(B2) 与 GND(B1) 接地。

- 参数与网络：`sck_pin=A3`；`sda_pin=A2`；`r4=0R`；`r5=0R`；`adsel=GND`
- 证据：图 ff9fd127d707 / 第 1 页 / C 区右侧：BMM350 SCK/SDA/ADSEL/GND 与 R4/R5

## 总线地址

### U2

BMI270 地址由 SDO(1) 决定：SDO=1 为 0x69，SDO=0 为 0x68（默认）；R3(10K) 下拉 SDO，SW1 可将 SDO 接到 3V3。

- 参数与网络：`sdo0=0x68`；`sdo1=0x69`；`default=0x68`；`pulldown=R3 10K`；`switch=SW1`
- 证据：图 ff9fd127d707 / 第 1 页 / B 区右侧：BMI270 I2C Address 注释与 SW1/R3

## GPIO 与控制信号

### BMI270 INT

BMI270 的 INT1(4) 与 INT2(9) 仅绘出短引脚线，未连接命名网络、GROVE 接口或其他器件。

- 参数与网络：`int1_pin=4`；`int2_pin=9`；`net=null`
- 证据：图 ff9fd127d707 / 第 1 页 / B 区右侧：U2 INT1/INT2

### BMM350 INT

BMM350 的 INT(A1) 引脚只绘出短引脚线，未连接命名网络、GROVE 接口或其他器件。

- 参数与网络：`pin=A1`；`net=null`
- 证据：图 ff9fd127d707 / 第 1 页 / C 区右侧：BMM350 INT(A1)

## 关键网络

### I2C nets

外部 I2C 网络名称为 SCL/SDA；BMM350 侧网络名称为 BMM_SCL/BMM_SDA，两组网络分别通过 R4/R5 的 0R 电阻连接。

- 参数与网络：`external_scl=SCL`；`external_sda=SDA`；`sensor_scl=BMM_SCL`；`sensor_sda=BMM_SDA`；`series_resistors=R4/R5 0R`
- 证据：图 ff9fd127d707 / 第 1 页 / B/C 区：SCL/SDA、BMM_SCL/BMM_SDA 与 R4/R5

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit DoF10 | `imu=BMI270`；`magnetometer=BMM350`；`pressure_sensor=SPA06-003`；`external_connector=J1 GROVE_IO` |
| 电源 | U1 | `vin=VCC_5V`；`vout=3V3`；`vin_pin=3`；`vout_pin=2`；`gnd_pin=1`；`c1=10uF`；`c2=100nF`；`c3=10uF` |
| 电源 | U5 | `part=SSP7615-18DFR`；`vin=3V3`；`vout=1V8`；`enable=3V3`；`c10=104`；`c11=104` |
| 接口 | J1 | `io2=SCL`；`io1=SDA`；`vcc=VCC_5V`；`gnd=GND` |
| 总线 | R1/R2 | `scl_pullup=R1 4.7K`；`sda_pullup=R2 4.7K`；`pullup_rail=3V3` |
| 核心器件 | U2 | `vdd=3V3`；`vddio=3V3`；`csb=3V3`；`c5=100nF`；`c6=100nF` |
| 总线 | U2 | `sda_pin=14`；`scl_pin=13`；`sdo_pin=1` |
| 总线地址 | U2 | `sdo0=0x68`；`sdo1=0x69`；`default=0x68`；`pulldown=R3 10K`；`switch=SW1` |
| 电源 | BMM350 | `vddio=3V3`；`vdd=1V8`；`crst_cap=C9 2.2uF`；`bypass=GND`；`c4=100nF`；`c7=100nF` |
| 总线 | BMM350 | `sck_pin=A3`；`sda_pin=A2`；`r4=0R`；`r5=0R`；`adsel=GND` |
| 总线地址 | BMM350 I2C address | `documented_address=0x14`；`adsel_level=low` |
| 核心器件 | U4 | `sck_pin=4`；`sdi_pin=3`；`csb_pin=2`；`vdd_pin=8`；`vddio_pin=6`；`sdo_pin=5`；`c8=100nF` |
| 总线地址 | SPA06-003 I2C address | `documented_address=0x76`；`sdo=GND`；`csb=3V3` |
| GPIO 与控制信号 | BMI270 INT | `int1_pin=4`；`int2_pin=9`；`net=null` |
| GPIO 与控制信号 | BMM350 INT | `pin=A1`；`net=null` |
| 关键网络 | I2C nets | `external_scl=SCL`；`external_sda=SDA`；`sensor_scl=BMM_SCL`；`sensor_sda=BMM_SDA`；`series_resistors=R4/R5 0R` |

## 待确认事项

- `address.bmm350-value`：产品清单给出的 BMM350 I2C 地址为 0x14。原理图将 ADSEL(B2) 与 GND(B1) 接地，但页内没有打印地址值。（证据：图 ff9fd127d707 / 第 1 页 / C 区右侧：BMM350 ADSEL(B2)/GND(B1)）
- `address.spa06-value`：产品清单给出的 SPA06-003 I2C 地址为 0x76。原理图将 SDO(5) 接地且 CSB(2) 接 3V3，但页内没有打印地址值。（证据：图 ff9fd127d707 / 第 1 页 / C 区左侧：U4 SDO(5) 与 CSB(2)）
- `nr-bmm350-address`：请以 BMM350 数据手册确认 ADSEL 低电平时对应的 I2C 地址是否为 0x14。；原因：产品清单给出 0x14，原理图只明确 ADSEL(B2) 接地，未在页内打印地址值。
- `nr-spa06-address`：请以 SPA06-003 数据手册确认 SDO 接地时对应的 I2C 地址是否为 0x76。；原因：产品清单给出 0x76，原理图只明确 SDO(5) 接地且 CSB(2) 接 3V3，未在页内打印地址值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ff9fd127d707d3ce01ad78cbcbc040e18f75a89a4fa10ae43985894918a0f459` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1291/U230_Unit_DoF10_sche_page_01.png` |

---

源文档：`zh_CN/unit/Unit_DoF10.md`

源文档 SHA-256：`ce87690f434ff765d96112715f9212375874d3db3dac5ea9d02a02f100b79a6a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
