# Unit DoF9 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit DoF9 |
| SKU | U229 |
| 产品 ID | `unit-dof9-a231857e2581` |
| 源文档 | `zh_CN/unit/Unit_DoF9.md` |

## 概述

Unit DoF9 与 DoF6 采用相同的 BMI270 六轴 IMU + BMM350 三轴磁力计架构：GROVE 提供 5V 与 I2C，ME6206A33M3G 将 5V 转为 3V3；BMI270 通过 SDO 选择 0x68/0x69，BMM350 经 0R 电阻并入同一 I2C 总线；板上 SSP7615-18DFR 将 3V3 转为 1V8 供 BMM350 VDD/CRST 使用。

## 检索关键词

`Unit DoF9`、`U229`、`BMI270`、`BMM350`、`ME6206A33M3G`、`SSP7615-18DFR`、`I2C`、`0x68`、`0x69`、`SDO`、`SCL`、`SDA`、`3V3`、`1V8`、`VCC_5V`、`GROVE_IO`、`CRST`、`BYPASS`、`ADSEL`、`INT1`、`INT2`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ME6206A33M3G | 5V 转 3.3V LDO | 图 c20f5e56a031 / 第 1 页 / A/B 区：U1 型号与 VIN/VOUT/GND |
| U2 | BMI270 | 六轴 IMU（加速度计+陀螺仪），I2C 从机 | 图 c20f5e56a031 / 第 1 页 / B 区：U2 BMI270 及 1/13/14/5/8/12 脚 |
| U3 | BMM350 | 三轴磁力计 | 图 c20f5e56a031 / 第 1 页 / C 区：BMM350 及 VDDIO/VDD/SCK/SDA/ADSEL/GND |
| U5 | SSP7615-18DFR | 3V3 转 1V8 LDO，为 BMM350 供电 | 图 c20f5e56a031 / 第 1 页 / D 区：U5 SSP7615-18DFR 与 VIN/OUT/EN/GND_EP |
| U4 | 未标注 | 8 脚 SPI 器件位置（SCK/SDI/CSB/SDO/VDD/VDDIO/GND），未标注具体型号 | 图 c20f5e56a031 / 第 1 页 / C 区：U4 与 1~8 脚 |
| J1 | GROVE_IO | I2C 接口：IO2=SCL、IO1=SDA、VCC=VCC_5V、GND | 图 c20f5e56a031 / 第 1 页 / B 区左侧：J1 GROVE_IO |
| SW1 | SW-PWR | BMI270 SDO 地址选择开关，接 3V3 时 SDO=1 | 图 c20f5e56a031 / 第 1 页 / B 区：SW1 与 SDO/R3 |
| R1 / R2 | 2.2K | I2C SCL/SDA 上拉到 3V3 | 图 c20f5e56a031 / 第 1 页 / B 区 J1 右侧：R1、R2 2.2K |
| R3 | 10K | BMI270 SDO 下拉，默认地址 0x68 | 图 c20f5e56a031 / 第 1 页 / B 区：R3 10K 对地 |
| R4 / R5 | 0R | BMM350 的 BMM_SCL/BMM_SDA 并入主 I2C 总线 | 图 c20f5e56a031 / 第 1 页 / C 区：R4、R5 0R |

## 电源

### U1

VCC_5V 接 U1(ME6206A33M3G) 的 VIN(3)，VOUT(2) 输出 3V3，GND(1) 接地；输入 C1=1uF，输出 C2=100nF、C3=10uF。

- 参数与网络：`vin=VCC_5V`；`vout=3V3`
- 证据：图 c20f5e56a031 / 第 1 页 / B 区 U1 与 C1-C3

### U2

BMI270 的 VDD(8) 与 VDDIO(5) 均接 3V3，CSB(12) 接 VDDIO（I2C 模式），GND(6,7) 接地；C5、C6 各 100nF。

- 参数与网络：`vdd=3V3`；`vddio=3V3`；`csb=VDDIO`
- 证据：图 c20f5e56a031 / 第 1 页 / B 区 U2 右侧

### U3

BMM350 的 VDDIO(B3) 接 3V3，VDD(C1) 与 CRST(C2) 接 1V8；BYPASS(C3) 经 C7(100nF) 到地，3V3 侧 C4=100nF，1V8 侧 C9=2.2uF。

- 参数与网络：`vddio=3V3`；`vdd=1V8`；`crst=1V8`；`c7=100nF`；`c9=2.2uF`
- 证据：图 c20f5e56a031 / 第 1 页 / C 区 BMM350 左侧

### U5

U5(SSP7615-18DFR)：VIN(4)=3V3、EN(3)=3V3、OUT(1)=1V8、GND(2)/GND_EP(5) 接地，C10/C11 为 104。

- 参数与网络：`vin=3V3`；`vout=1V8`；`part=SSP7615-18DFR`
- 证据：图 c20f5e56a031 / 第 1 页 / D 区 U5

## 接口

### J1

J1(GROVE_IO)：IO2=SCL，IO1=SDA，VCC=VCC_5V，GND=GND。

- 参数与网络：`io2=SCL`；`io1=SDA`；`vcc=VCC_5V`
- 证据：图 c20f5e56a031 / 第 1 页 / B 区左侧 J1

## 总线

### R1/R2

SCL 与 SDA 分别经 R1、R2（2.2K）上拉到 3V3。

- 参数与网络：`scl_pullup=R1 2.2K`；`sda_pullup=R2 2.2K`
- 证据：图 c20f5e56a031 / 第 1 页 / B 区 R1/R2

### U2

BMI270 使用 SDA(14) 与 SCX(13，网络 SCL) 作为 I2C 数据/时钟；INT1(4)、INT2(9) 引出中断网络。

- 参数与网络：`sda_pin=14`；`scl_pin=13`
- 证据：图 c20f5e56a031 / 第 1 页 / B 区 U2 引脚

### U3

BMM350 的 SCK(A3)=BMM_SCL 经 R4(0R) 接 SCL；SDA(A2)=BMM_SDA 经 R5(0R) 接 SDA；ADSEL(B2) 与 GND(B1) 接地。

- 参数与网络：`scl=A3 via R4 0R`；`sda=A2 via R5 0R`；`adsel=GND`
- 证据：图 c20f5e56a031 / 第 1 页 / C 区 BMM350 右侧

## 总线地址

### U2

BMI270 地址由 SDO(1) 决定：SDO=1 为 0x69，SDO=0 为 0x68（默认）；R3(10K) 下拉 SDO，SW1 可将 SDO 接到 3V3。

- 参数与网络：`sdo0=0x68`；`sdo1=0x69`；`pulldown=R3 10K`；`switch=SW1`
- 证据：图 c20f5e56a031 / 第 1 页 / B 区地址注释与 SW1/R3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 电源 | U1 | `vin=VCC_5V`；`vout=3V3` |
| 接口 | J1 | `io2=SCL`；`io1=SDA`；`vcc=VCC_5V` |
| 总线 | R1/R2 | `scl_pullup=R1 2.2K`；`sda_pullup=R2 2.2K` |
| 电源 | U2 | `vdd=3V3`；`vddio=3V3`；`csb=VDDIO` |
| 总线地址 | U2 | `sdo0=0x68`；`sdo1=0x69`；`pulldown=R3 10K`；`switch=SW1` |
| 总线 | U2 | `sda_pin=14`；`scl_pin=13` |
| 电源 | U3 | `vddio=3V3`；`vdd=1V8`；`crst=1V8`；`c7=100nF`；`c9=2.2uF` |
| 总线 | U3 | `scl=A3 via R4 0R`；`sda=A2 via R5 0R`；`adsel=GND` |
| 电源 | U5 | `vin=3V3`；`vout=1V8`；`part=SSP7615-18DFR` |
| 核心器件 | U4 | `sck=SCL`；`sdi=SDA` |

## 待确认事项

- `component.spi-footprint`：U4 为 8 脚 SPI 器件位置：SCK(4)=SCL、SDI(3)=SDA、CSB(2)=3V3、VDD(8)=VDDIO(6)=3V3、SDO(5)=GND；未标注具体型号。（证据：图 c20f5e56a031 / 第 1 页 / C 区 U4）
- `nr-1`：U4 的具体型号与是否贴装？；原因：U4 仅画引脚，未标注 part number；附近 C8 标注 NC。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c20f5e56a031392805ceb05a8be23d3e5e9046a1fc992dd1e7e9a173935417b4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1292/U229_Unit_DoF9_sche_page_01.png` |

---

源文档：`zh_CN/unit/Unit_DoF9.md`

源文档 SHA-256：`fd3f8245cbcf281431e5597fc0e7d032929fd5e33196a982832d02ad1bedf30d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
