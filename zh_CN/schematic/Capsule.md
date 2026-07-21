# Capsule 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Capsule |
| SKU | K129 |
| 产品 ID | `capsule-a356fc943d88` |
| 源文档 | `zh_CN/core/M5Capsule.md` |

## 概述

Capsule 以 M1 Stamp-S3-MID 为控制器，主板连接 BMI270、SPM1423HM4H-B、RTC8563、SPI microSD、红外、蜂鸣器、Grove 和双排扩展接口。TP4057 负责电池充电，SY7088 从 VBAT_OUT 生成 +5VOUT，SY8089 生成 +3.3V，CN809J 与 WAKE/HOLD MOSFET 网络实现按键/RTC 唤醒和电源保持。BMI270 与 RTC 共用 G8/G10 I2C，总线上的 BMI270 绑定位在原理图中明确对应 0x69。

## 检索关键词

`Capsule`、`K129`、`Stamp-S3-MID`、`ESP32-S3FN8`、`TP4057`、`CN809J`、`SY7088`、`SY8089`、`RTC8563`、`BM8563`、`BMI270`、`0x69`、`SPM1423HM4H-B`、`microSD`、`TF-015`、`G8 SDA`、`G10 SCL`、`G40 MIC_CLK`、`G41 MIC_DAT`、`G4 IR`、`G2 Buzzer`、`G42 WAKE`、`G46 HOLD`、`VBAT_IN`、`VBAT_OUT`、`+5VIN`、`+5VOUT`、`+3.3V`、`WAKE`、`HOLD`、`32.768KHz`、`G11 SD_CS`、`G12 SD_MOSI`、`G14 SD_CLK`、`G39 SD_MISO`、`HY-2.0_IIC`、`PESDNC2FD3V3B`、`LP3218DT1G`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | STAMP-S3-MID | Capsule 主控模组，通过双排连接器接入全部外设与电源控制 | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 D2-D3：M1 STAMP-S3-MID 与 P1/P2 |
| U2 | TP4057 | +5VIN 到 VBAT_IN 的锂电池充电器 | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 A1：U2 TP4057、R11/R17、C15/C21 |
| U1 | CN809J | +5VIN 电压监控与电源路径复位控制 | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 A2-B2：U1 CN809J、INT、Q2/Q3 |
| Q2,Q3 | LP3218DT1G | VBAT_IN 到 VBAT_OUT 的受控电源路径 MOSFET | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 A1-A3：Q2/Q3、D1、VBAT_IN/OUT |
| Q4 | LN2324DT2AG | HOLD 控制的电源保持 MOSFET | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 B2-B3：Q4、HOLD、WAKE、D3/D4 |
| U3 | SY7088 | VBAT_OUT 到 +5VOUT 的升压转换器 | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 A3-A4：U3 SY7088、L4、R16/R18、D8 |
| U4 | SY8089 | VBAT_OUT 到 +3.3V 的降压转换器 | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 B3-B4：U4 SY8089、L5、R27/R28 |
| U5 | RTC8563 | G8/G10 I2C 实时时钟与 INT 唤醒源 | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 B1-B2：U5 RTC8563、Y2、SDA/SCL/INT |
| Y2 | 32.768KHz +/-20ppm 12.5pF | RTC8563 低速时钟晶体 | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 C1-C2：Y2、C28/C29 |
| U7 | BMI270 | G8/G10 I2C 六轴 IMU，地址绑定位 0x69 | 图 203c49dde3fb / 第 1 页 / 外设页网格 B3：U7 BMI270 与 SDO=VDDIO 0x69 注释 |
| U9 | SPM1423HM4H-B | G41 数据、G40 时钟的 PDM 麦克风 | 图 203c49dde3fb / 第 1 页 / 外设页网格 B1-B2：U9 SPM1423HM4H-B |
| J1 | TF-015 | G11/G12/G14/G39 SPI microSD 卡座 | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 D4：J1 TF-015、R10/R20-R22、D9-D14 |
| J3 | HY-2.0_IIC | G15/G13、可选 5V 电源与 GND 的 Grove 接口 | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 C4：J3/R1/R2/D12/D13/D16 |
| LS1,Q5 | Buzzer / SS8050 Y1 | G2 控制的蜂鸣器驱动 | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 D1：LS1/Q5/R24/R25/C27/D6/D7 |
| IR1,R3 | IR LED / 22R/1% | G4 驱动的红外发射支路 | 图 ac6e57f217e9 / 第 1 页 / 主板页网格 C2：G4-IR1-R3-GND |
| S1,S4 | SW-PB | WAKE 唤醒按键与 EN 复位按键 | 图 ac6e57f217e9 / 第 1 页 / 主板页 S1 WAKE 与 S4 EN |

## 系统结构

### Capsule 系统架构

M1 Stamp-S3-MID 连接电池充放电、RTC8563、BMI270、SPM1423、SPI microSD、红外、蜂鸣器、Grove 和双排扩展接口；WAKE/HOLD 网络控制电池供电保持。

- 参数与网络：`controller=M1 Stamp-S3-MID`；`power=TP4057 + SY7088 + SY8089`；`sensors=BMI270 + SPM1423`；`rtc=RTC8563`；`storage=J1 TF-015`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板完整单页; 图 203c49dde3fb / 第 1 页 / 外设完整单页

## 电源

### TP4057 电池充电

U2 TP4057 VCC 经 R11 0.8Ω 接 +5VIN，BAT pin3 接 VBAT_IN，PROG 经 R17 3.3KΩ 接地；J2 Header 2 引出 VBAT_IN 与 GND。

- 参数与网络：`charger=U2 TP4057`；`input=+5VIN via R11 0.8Ω`；`battery=VBAT_IN`；`program=R17 3.3KΩ`；`connector=J2 Header 2`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 A1-B1 U2/J2/R11/R17

### WAKE/HOLD 电源保持

Q2/Q3 LP3218DT1G 构成 VBAT_IN 到 VBAT_OUT 路径；U1 CN809J INT、S1 WAKE、D3/D4 B5819WT 与 Q4 LN2324DT2AG 组合控制保持，M1 G46 形成 HOLD。

- 参数与网络：`path=VBAT_IN -> Q2/Q3 -> VBAT_OUT`；`supervisor=U1 CN809J`；`wake=S1 WAKE / G42`；`hold=M1 G46 -> HOLD -> Q4`；`diodes=D3/D4 B5819WT`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 A1-B3 Q2/Q3/U1/S1/Q4

### +5VOUT 升压

U3 SY7088 由 VBAT_OUT 供电，L4 3015 1.5uH、R16 52.3KΩ/R18 15KΩ 和 D8 SS34 生成 +5VOUT。

- 参数与网络：`converter=U3 SY7088`；`input=VBAT_OUT`；`inductor=L4 3015 1.5uH`；`feedback=R16 52.3KΩ; R18 15KΩ`；`output=+5VOUT`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 A3-A4 U3/L4/R16/R18/D8

### +3.3V 降压

U4 SY8089 从 VBAT_OUT 降压，LX 经 L5 3015 4.7uH 输出 +3.3V，反馈为 R27 68KΩ 与 R28 15KΩ。

- 参数与网络：`converter=U4 SY8089`；`input=VBAT_OUT`；`output=+3.3V`；`inductor=L5 3015 4.7uH`；`feedback=R27 68KΩ; R28 15KΩ`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 B3-B4 U4/L5/R27/R28

## 接口

### J3 Grove 接口

J3 pin1=G15/IIC_SCL、pin2=G13/IIC_SDA、pin3=VCC、pin4=GND；R1 0Ω 默认从 +5VOUT 供电，R2 0Ω/NC 为 +5VIN 备选。

- 参数与网络：`pin1=G15 / IIC_SCL`；`pin2=G13 / IIC_SDA`；`pin3=VCC`；`pin4=GND`；`default_power=+5VOUT via R1 0Ω`；`option=+5VIN via R2 0Ω/NC`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 C4 J3/R1/R2

### 双排 Capsule Bus

P2/P1 Header 9 与 M1 两侧引出 G1/G3/G5/G7/G9/G13/G15、G43/G44、5VIN、5VOUT、VBAT_IN、WAKE、EN、G0、+3.3V 和 GND。

- 参数与网络：`left=P2 G1,G3,G5,G7,G9,GND,5VIN,G13,G15`；`right=P1 5VOUT,VBAT_IN,WAKE,+3.3V,G43,G44,EN,G0,GND`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 D1-D3 P2/M1/P1

## 总线

### RTC 与 IMU I2C

M1 G8 形成 SDA、G10 形成 SCL，连接 U5 RTC8563 和 U7 BMI270；BMI270 SDA/SDX pin14 与 SCL/SCX pin13 各由 15KΩ 上拉至 VDDIO。

- 参数与网络：`controller=Stamp-S3-MID`；`sda=G8`；`scl=G10`；`devices=RTC8563, BMI270`；`pullups=R7/R8 15KΩ to VDDIO`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 U5/M1 SDA/SCL; 图 203c49dde3fb / 第 1 页 / 外设页 U7 SDA/SCL/R7/R8

## 总线地址

### BMI270 I2C 地址

外设页直接标注 SDO=GND 0x68、SDO=VDDIO 0x69；U7 SDO/SA0 由 R9 15KΩ 上拉至 VDDIO，因此绑定位对应 0x69。

- 参数与网络：`device=U7 BMI270`；`sdo_low=0x68`；`sdo_high=0x69`；`strap=R9 15KΩ to VDDIO`；`configured=0x69`
- 证据：图 203c49dde3fb / 第 1 页 / 外设页 U7 上方 SDO 地址注释与 R9/SA0

## GPIO 与控制信号

### 红外与蜂鸣器输出

G4 经 IR1 与 R3 22Ω/1% 驱动红外；G2 经 R25 470Ω/C27 控制 Q5 SS8050 Y1，驱动 LS1 Buzzer。

- 参数与网络：`ir=G4 -> IR1 -> R3 22Ω -> GND`；`buzzer=G2 -> R25 470Ω/C27 -> Q5 -> LS1`；`direction=output`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 C2 IR1 与 D1 LS1/Q5

## 时钟

### RTC 32.768KHz 晶体

Y2 32.768KHz +/-20ppm 12.5pF 连接 U5 OSCI/OSCO，C28/C29 各 6.0pF 对地。

- 参数与网络：`crystal=Y2 32.768KHz +/-20ppm 12.5pF`；`pins=U5 OSCI/OSCO`；`loads=C28/C29 6.0pF`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 B1-C2 U5/Y2/C28/C29

## 复位

### WAKE 与 EN 按键

S1 按下将 WAKE 拉低并由 D5 PESDNC2FD3V3B 保护，WAKE 连接 M1 G42；S4 按下将 EN 拉低。

- 参数与网络：`wake=S1 -> WAKE -> G42`；`wake_protection=D5 PESDNC2FD3V3B`；`reset=S4 -> EN low`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 S1 WAKE/D5 与 S4 EN

## 保护电路

### microSD 与 Grove ESD

microSD G11/G12/G14/G39 使用 D9-D11/D14 PESDNC2FD3V3B；Grove G15/G13/VCC 使用 D12/D13/D16 PESDNC2FD3V3B。

- 参数与网络：`microsd=D9,D10,D11,D14`；`grove=D12,D13,D16`；`device=PESDNC2FD3V3B`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 C4-D4 ESD 支路

## 存储

### microSD SPI

J1 TF-015 使用 G11=CS、G12=MOSI、G14=CLK、G39=MISO，各信号串 R10/R20/R21/R22 33Ω，并由 +3.3V 供电。

- 参数与网络：`cs=G11 via R10 33Ω`；`mosi=G12 via R20 33Ω`；`clk=G14 via R21 33Ω`；`miso=G39 via R22 33Ω`；`supply=+3.3V`
- 证据：图 ac6e57f217e9 / 第 1 页 / 主板页 D4 J1/R10/R20-R22

## 音频

### SPM1423 PDM 麦克风

U9 SPM1423HM4H-B DAT pin5 接 G41，CLK pin4 接 G40，3V3 pin6 接 +3.3V，SELECT 与 GND 接地。

- 参数与网络：`data=G41`；`clock=G40`；`supply=+3.3V`；`interface=PDM`
- 证据：图 203c49dde3fb / 第 1 页 / 外设页 U9 SPM1423HM4H-B

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Capsule 系统架构 | `controller=M1 Stamp-S3-MID`；`power=TP4057 + SY7088 + SY8089`；`sensors=BMI270 + SPM1423`；`rtc=RTC8563`；`storage=J1 TF-015` |
| 电源 | TP4057 电池充电 | `charger=U2 TP4057`；`input=+5VIN via R11 0.8Ω`；`battery=VBAT_IN`；`program=R17 3.3KΩ`；`connector=J2 Header 2` |
| 电源 | WAKE/HOLD 电源保持 | `path=VBAT_IN -> Q2/Q3 -> VBAT_OUT`；`supervisor=U1 CN809J`；`wake=S1 WAKE / G42`；`hold=M1 G46 -> HOLD -> Q4`；`diodes=D3/D4 B5819WT` |
| 电源 | +5VOUT 升压 | `converter=U3 SY7088`；`input=VBAT_OUT`；`inductor=L4 3015 1.5uH`；`feedback=R16 52.3KΩ; R18 15KΩ`；`output=+5VOUT` |
| 电源 | +3.3V 降压 | `converter=U4 SY8089`；`input=VBAT_OUT`；`output=+3.3V`；`inductor=L5 3015 4.7uH`；`feedback=R27 68KΩ; R28 15KΩ` |
| 总线 | RTC 与 IMU I2C | `controller=Stamp-S3-MID`；`sda=G8`；`scl=G10`；`devices=RTC8563, BMI270`；`pullups=R7/R8 15KΩ to VDDIO` |
| 总线地址 | BMI270 I2C 地址 | `device=U7 BMI270`；`sdo_low=0x68`；`sdo_high=0x69`；`strap=R9 15KΩ to VDDIO`；`configured=0x69` |
| 总线地址 | RTC8563 I2C 地址 | `device=U5 RTC8563`；`documented_address=0x51`；`schematic_address_text=false` |
| 时钟 | RTC 32.768KHz 晶体 | `crystal=Y2 32.768KHz +/-20ppm 12.5pF`；`pins=U5 OSCI/OSCO`；`loads=C28/C29 6.0pF` |
| 音频 | SPM1423 PDM 麦克风 | `data=G41`；`clock=G40`；`supply=+3.3V`；`interface=PDM` |
| 存储 | microSD SPI | `cs=G11 via R10 33Ω`；`mosi=G12 via R20 33Ω`；`clk=G14 via R21 33Ω`；`miso=G39 via R22 33Ω`；`supply=+3.3V` |
| GPIO 与控制信号 | 红外与蜂鸣器输出 | `ir=G4 -> IR1 -> R3 22Ω -> GND`；`buzzer=G2 -> R25 470Ω/C27 -> Q5 -> LS1`；`direction=output` |
| 接口 | J3 Grove 接口 | `pin1=G15 / IIC_SCL`；`pin2=G13 / IIC_SDA`；`pin3=VCC`；`pin4=GND`；`default_power=+5VOUT via R1 0Ω`；`option=+5VIN via R2 0Ω/NC` |
| 接口 | 双排 Capsule Bus | `left=P2 G1,G3,G5,G7,G9,GND,5VIN,G13,G15`；`right=P1 5VOUT,VBAT_IN,WAKE,+3.3V,G43,G44,EN,G0,GND` |
| 复位 | WAKE 与 EN 按键 | `wake=S1 -> WAKE -> G42`；`wake_protection=D5 PESDNC2FD3V3B`；`reset=S4 -> EN low` |
| 内存与 Flash | Stamp-S3 8MB Flash | `documented_soc=ESP32-S3FN8`；`documented_flash=8MB`；`module=STAMP-S3-MID`；`internal_memory_shown=false` |
| 电源 | 250mAh 电池容量 | `documented_capacity=250mAh`；`schematic_capacity_text=false` |
| 保护电路 | microSD 与 Grove ESD | `microsd=D9,D10,D11,D14`；`grove=D12,D13,D16`；`device=PESDNC2FD3V3B` |

## 待确认事项

- `address.rtc8563`：产品正文写 RTC/BM8563 地址 0x51，但主板原理图 U5 只显示 SDA/SCL/INT/OSCI/OSCO，未打印数值地址。（证据：图 ac6e57f217e9 / 第 1 页 / 主板页 U5 RTC8563，无地址文字）
- `memory.documented-flash`：产品正文写 ESP32-S3FN8 与 8MB Flash，主板原理图只画 M1 STAMP-S3-MID 模组接口，没有模组内部 Flash 器件或容量字段。（证据：图 ac6e57f217e9 / 第 1 页 / 主板页 M1 STAMP-S3-MID，仅显示模组引脚）
- `power.documented-battery-capacity`：产品正文写内置 250mAh 电池，主板图只显示 J2 VBAT_IN 接口与充电/电源路径，未打印容量。（证据：图 ac6e57f217e9 / 第 1 页 / 主板页 J2 VBAT_IN 与 U2 TP4057，无容量文字）
- `review.rtc-address`：K129 当前 RTC8563/BM8563 的正式 7-bit I2C 地址是否为 0x51？；原因：地址来自正文，原理图未打印数值。
- `review.flash-capacity`：K129 当前 Stamp-S3-MID 内部 Flash 是否固定为 8MB？；原因：主板图未展示模组内部存储器或容量字段。
- `review.battery-capacity`：K129 当前内置电池容量是否固定为 250mAh？；原因：容量只出现在正文，原理图未打印。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `ac6e57f217e95acd75ddb1dff39ab71ed9158a2a2bb9c953514d14b7499a8f11` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/496/Sch_M5Capsule_sch_01.png` |
| 2 | 1 | `203c49dde3fb6a1b938b43d2ce59fb2be4469ce919856555056e48c1e7afb471` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/496/Sch_M5Capsule_sch_02.png` |

---

源文档：`zh_CN/core/M5Capsule.md`

源文档 SHA-256：`b979cab017eea4c9aa38d505b3032061d6a1c3d8b5821b30b45147d57fd50cfd`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
