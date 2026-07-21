# Dial 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Dial |
| SKU | K130 |
| 产品 ID | `dial-aff7d730eff4` |
| 源文档 | `zh_CN/core/M5Dial.md` |

## 概述

Dial 以 M1 Stamp-S3-DIP-1.27 为主控，连接 WS1850S RFID、圆形 LCD/触摸模组、RTC8563、EC30-16bit 编码器、蜂鸣器和两组 HY2.0 扩展口。P5 宽压输入经 ME3116AM6G 生成 +5VIN，TP4057 管理电池充电，SY7088 生成 +5VOUT，SY8089 生成 +3.3V，并以 WAKE/HOLD MOSFET 网络实现电源保持。RFID 使用 27.12MHz 晶体和差分天线匹配网络，LCD 使用 SPI，触摸与 RFID/RTC 使用 I2C。

## 检索关键词

`Dial`、`K130`、`Stamp-S3-DIP-1.27`、`WS1850S`、`ME3116AM6G`、`TP4057`、`SY7088`、`SY8089`、`RTC8563`、`EC30-16bit`、`27.12MHz`、`32.768KHz`、`RFID`、`RC522_SDA`、`RC522_SCL`、`RC522_IRQ`、`LCD_MOSI`、`LCD_SCK`、`LCD_CS`、`LCD_RS`、`LCD_RESET`、`LCD_BL`、`TP_SDA`、`TP_SCL`、`TP_INT`、`G41 Encoder A`、`G40 Encoder B`、`G46 HOLD`、`G42 WAKE`、`+VIN`、`+5VIN`、`+5VOUT`、`+3.3V`、`VBAT_IN`、`VBAT_OUT`、`HY-2.0_IIC`、`HY-2.0_IO`、`Buzzer`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 (RFID) | WS1850S | I2C RFID 前端，连接 27.12MHz 晶体与差分天线 | 图 1d8705f9d82d / 第 1 页 / 显示/RFID 页网格 A1-B2：U1 WS1850S |
| Y1 | 27.12MHz | WS1850S 主时钟晶体 | 图 1d8705f9d82d / 第 1 页 / 显示/RFID 页 U1 OSCIN/OSCOUT、Y1、C6/C9 |
| L2 | ANT_Hole | WS1850S TX1/TX2 差分 RFID 天线线圈 | 图 1d8705f9d82d / 第 1 页 / 显示/RFID 页网格 B2：L2 ANT_Hole 与 L1/L3/C8-C14/R4/R5 |
| BTB1 | OK-24M024-04 | 24P LCD、背光与电容触摸连接器 | 图 1d8705f9d82d / 第 1 页 / 显示/RFID 页网格 C3-D4：BTB1 pins1-24 |
| U7 | ME3116AM6G | P5 宽压输入到 +5VIN 的前级转换器 | 图 0528f589274c / 第 1 页 / 主板页网格 A1-A3：P5/U7/L6/R32-R34/D9/D11 |
| U2 | TP4057 | +5VIN 到 VBAT_IN 的锂电池充电器 | 图 0528f589274c / 第 1 页 / 主板页网格 A1-B1：U2 TP4057、P6、R11/R17 |
| U6 | CN809J | +5VIN 监控与电池路径复位控制 | 图 0528f589274c / 第 1 页 / 主板页网格 B1-B2：U6 CN809J |
| Q2,Q3 | LP3218DT1G | VBAT_IN 到 VBAT_OUT 的电源路径 MOSFET | 图 0528f589274c / 第 1 页 / 主板页网格 A1-B3：Q2/Q3、VBAT_IN/OUT |
| Q4 | LN2324DT2AG | HOLD 控制的电源保持 MOSFET | 图 0528f589274c / 第 1 页 / 主板页网格 B2-B3：Q4 HOLD/WAKE |
| U3 | SY7088 | VBAT_OUT 到 +5VOUT 的升压转换器 | 图 0528f589274c / 第 1 页 / 主板页网格 A3-B4：U3 SY7088/L4/D8 |
| U4 | SY8089 | VBAT_OUT 到 +3.3V 的降压转换器 | 图 0528f589274c / 第 1 页 / 主板页网格 B3-B4：U4 SY8089/L5 |
| U5 | RTC8563 | I2C RTC 与 INT 唤醒源 | 图 0528f589274c / 第 1 页 / 主板页网格 C2-C3：U5 RTC8563/Y2 |
| J5 | EC30-16bit | G41/G40 双相旋转编码器 | 图 0528f589274c / 第 1 页 / 主板页网格 C3：J5 EC30-16bit、A/B、R21/R22 |
| M1 | STAMP-S3-DIP-1.27 | Dial 主控模组与外设/电源控制接口 | 图 0528f589274c / 第 1 页 / 主板页网格 D2-D3：M1 STAMP-S3-DIP-1.27 |
| LS1,Q5 | Buzzer / SS8050 Y1 | beep 网络控制的蜂鸣器驱动 | 图 0528f589274c / 第 1 页 / 主板页网格 D1：LS1/Q5/R24/R25 |
| J3,J2 | HY-2.0_IIC / HY-2.0_IO | I2C Port A 与 GPIO Port B 扩展接口 | 图 0528f589274c / 第 1 页 / 主板页网格 D4：J3/J2 |

## 系统结构

### Dial 系统架构

M1 Stamp-S3-DIP-1.27 连接 WS1850S RFID、LCD/触摸、RTC8563、旋转编码器、蜂鸣器、双扩展口和多路电源；WAKE/HOLD 网络控制电池供电保持。

- 参数与网络：`controller=M1 Stamp-S3-DIP-1.27`；`rfid=WS1850S`；`display=BTB1 24P LCD/touch`；`rtc=RTC8563`；`encoder=EC30-16bit`；`power=ME3116AM6G + TP4057 + SY7088 + SY8089`
- 证据：图 1d8705f9d82d / 第 1 页 / 显示/RFID 完整单页; 图 0528f589274c / 第 1 页 / 主板完整单页

## 电源

### P5 宽压输入到 +5VIN

P5 pin1 经 D13 B5819W SL 与 D12 SD36 保护后进入 U7 ME3116AM6G；L6 3015 10uH、D9/D11 B5819W SL 与反馈网络生成 +5VIN。

- 参数与网络：`connector=P5 Header 2`；`protection=D13 B5819W SL; D12 SD36`；`converter=U7 ME3116AM6G`；`inductor=L6 3015 10uH`；`output=+5VIN`
- 证据：图 0528f589274c / 第 1 页 / 主板页 A1-A3 P5/U7/L6/D9/D11

### TP4057 电池充电

U2 TP4057 VCC 经 R11 0.8Ω 接 +5VIN，BAT 接 VBAT_IN/P6，PROG 经 R17 10KΩ 接地。

- 参数与网络：`charger=U2 TP4057`；`input=+5VIN via R11 0.8Ω`；`battery=VBAT_IN / P6`；`program=R17 10KΩ`
- 证据：图 0528f589274c / 第 1 页 / 主板页 A1-B1 U2/P6/R11/R17

### WAKE/HOLD 电源保持

Q2/Q3 LP3218DT1G 连接 VBAT_IN/VBAT_OUT；U6 CN809J、S1、D3/D4/D10 与 Q4 LN2324DT2AG 形成 WAKE/HOLD 控制，HOLD 由 M1 G46 驱动。

- 参数与网络：`path=VBAT_IN -> Q2/Q3 -> VBAT_OUT`；`wake=S1 / WAKE / G42`；`hold=G46 -> HOLD -> Q4`；`supervisor=U6 CN809J`
- 证据：图 0528f589274c / 第 1 页 / 主板页 A1-B3 Q2/Q3/U6/S1/Q4

### +5VOUT 与 +3.3V

U3 SY7088 从 VBAT_OUT 经 L4 1.5uH/D8 SS34 生成 +5VOUT；U4 SY8089 经 L5 4.7uH 生成 +3.3V。

- 参数与网络：`boost=U3 SY7088 -> +5VOUT`；`buck=U4 SY8089 -> +3.3V`；`boost_inductor=L4 3015 1.5uH`；`buck_inductor=L5 3015 4.7uH`
- 证据：图 0528f589274c / 第 1 页 / 主板页 A3-B4 U3/U4

## 接口

### LCD 与触摸连接

BTB1 引出 LCD_RS、LCD_MOSI、LCD_SCK、LCD_CS、LCD_RESET、LCD_BL，以及 TP_INT、TP_SCL、TP_SDA、TP_RST；Q1 LN2324DT2AG 由 LCD_BL 控制背光阴极。

- 参数与网络：`lcd=RS,MOSI,SCK,CS,RESET,BL`；`touch=INT,SCL,SDA,RST`；`connector=BTB1 OK-24M024-04`；`backlight=Q1 LN2324DT2AG`
- 证据：图 1d8705f9d82d / 第 1 页 / 显示/RFID 页 C3-D4 BTB1/Q1/P1

### Port A 与 Port B

J3 HY-2.0_IIC 引出 SCL、SDA、+5VOUT、GND；J2 HY-2.0_IO 引出 G1、G0、+5VOUT、GND。

- 参数与网络：`port_a=SCL,SDA,+5VOUT,GND`；`port_b=G1,G0,+5VOUT,GND`
- 证据：图 0528f589274c / 第 1 页 / 主板页 D4 J3/J2

## 总线

### WS1850S I2C

WS1850S SDA/NSS/RX pin24 形成 RC522_SDA，SCL/MISO/TX pin31 形成 RC522_SCL，IRQ pin23 形成 RC522_IRQ；经 R9/R8/R29 0Ω 接 TP_SDA/TP_SCL/RC522_INT。

- 参数与网络：`device=U1 WS1850S`；`sda=RC522_SDA -> TP_SDA`；`scl=RC522_SCL -> TP_SCL`；`irq=RC522_IRQ -> RC522_INT`；`reset=NRSTPD -> LCD_RESET via R7 0Ω`
- 证据：图 1d8705f9d82d / 第 1 页 / 显示/RFID 页 U1 与 R7-R9/R29

### RTC8563 I2C

U5 RTC8563 SCL/SDA 连接 TP_SCL/TP_SDA，INT 输出连接 WAKE 网络；Y2 32.768KHz 晶体连接 OSCI/OSCO。

- 参数与网络：`scl=TP_SCL / G12`；`sda=TP_SDA / G11`；`interrupt=INT -> WAKE`；`crystal=Y2 32.768KHz +/-20ppm 12.5pF`
- 证据：图 0528f589274c / 第 1 页 / 主板页 C2-C3 U5/Y2

## GPIO 与控制信号

### 显示与触摸 GPIO 映射

M1 引出 LCD_RS=G4、LCD_MOSI=G5、LCD_SCK=G6、LCD_CS=G7、LCD_RESET=G8、LCD_BL=G9；TP_SDA=G11、TP_SCL=G12、TP_INT=G14。

- 参数与网络：`lcd_rs=G4`；`lcd_mosi=G5`；`lcd_sck=G6`；`lcd_cs=G7`；`lcd_reset=G8`；`lcd_bl=G9`；`tp_sda=G11`；`tp_scl=G12`；`tp_int=G14`
- 证据：图 0528f589274c / 第 1 页 / 主板页 D2-D4 M1/P2/P3 显示网络

### EC30 旋转编码器

J5 EC30-16bit A 相接 M1 G41、B 相接 G40，A/B 各由 R21/R22 10KΩ 上拉到 +3.3V，并由 C22/C23 100nF 滤波；公共端接 GND。

- 参数与网络：`encoder=J5 EC30-16bit`；`a=G41`；`b=G40`；`pullups=R21/R22 10KΩ`；`filters=C22/C23 100nF`；`common=GND`
- 证据：图 0528f589274c / 第 1 页 / 主板页 C3 J5/R21/R22/C22/C23

### 蜂鸣器输出

M1 G3 形成 beep，经 R25 470Ω/C27 控制 Q5 SS8050 Y1，驱动 LS1 Buzzer。

- 参数与网络：`gpio=G3`；`net=beep`；`driver=Q5 SS8050 Y1`；`load=LS1 Buzzer`
- 证据：图 0528f589274c / 第 1 页 / 主板页 D1-D2 LS1/Q5/M1 beep

## 时钟

### RFID 27.12MHz 时钟

Y1 27.12MHz 连接 WS1850S OSCIN/OSCOUT，C6/C9 各 15pF 对地。

- 参数与网络：`crystal=Y1 27.12MHz`；`pins=U1 OSCIN/OSCOUT`；`loads=C6/C9 15pF`
- 证据：图 1d8705f9d82d / 第 1 页 / 显示/RFID 页 U1/Y1/C6/C9

## 保护电路

### 宽压与接口保护

P5 输入由 D13 B5819W SL 反向路径和 D12 SD36 瞬态器件保护；WAKE 使用 D5 PESDNC2FD3V3B，LCD/RFID 接口通过串联 0Ω和上拉网络隔离。

- 参数与网络：`input_diode=D13 B5819W SL`；`input_tvs=D12 SD36`；`wake_esd=D5 PESDNC2FD3V3B`；`signal_links=R7/R8/R9/R29 0Ω`
- 证据：图 0528f589274c / 第 1 页 / 主板页 P5/D13/D12 与 WAKE/D5; 图 1d8705f9d82d / 第 1 页 / 显示/RFID 页 R7-R9/R29

## 射频

### 13.56MHz RFID 天线链路

WS1850S TX1/TX2 经 L1/L3 1uH、C8/C14 47pF、C10/C12 120pF、C11/C13 390pF 与 R4/R5 1.2Ω 驱动 L2 ANT_Hole；RX 经 R2/C7/R3 返回。

- 参数与网络：`frontend=WS1850S`；`tx=TX1/TX2 differential`；`antenna=L2 ANT_Hole`；`series_inductors=L1/L3 1uH`；`rx=R2 1KΩ; C7 1nF; R3 1.5KΩ`
- 证据：图 1d8705f9d82d / 第 1 页 / 显示/RFID 页 B1-B3 U1/L1-L3/C7-C14/R2-R5

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Dial 系统架构 | `controller=M1 Stamp-S3-DIP-1.27`；`rfid=WS1850S`；`display=BTB1 24P LCD/touch`；`rtc=RTC8563`；`encoder=EC30-16bit`；`power=ME3116AM6G + TP4057 + SY7088 + SY8089` |
| 电源 | P5 宽压输入到 +5VIN | `connector=P5 Header 2`；`protection=D13 B5819W SL; D12 SD36`；`converter=U7 ME3116AM6G`；`inductor=L6 3015 10uH`；`output=+5VIN` |
| 电源 | TP4057 电池充电 | `charger=U2 TP4057`；`input=+5VIN via R11 0.8Ω`；`battery=VBAT_IN / P6`；`program=R17 10KΩ` |
| 电源 | WAKE/HOLD 电源保持 | `path=VBAT_IN -> Q2/Q3 -> VBAT_OUT`；`wake=S1 / WAKE / G42`；`hold=G46 -> HOLD -> Q4`；`supervisor=U6 CN809J` |
| 电源 | +5VOUT 与 +3.3V | `boost=U3 SY7088 -> +5VOUT`；`buck=U4 SY8089 -> +3.3V`；`boost_inductor=L4 3015 1.5uH`；`buck_inductor=L5 3015 4.7uH` |
| 总线 | WS1850S I2C | `device=U1 WS1850S`；`sda=RC522_SDA -> TP_SDA`；`scl=RC522_SCL -> TP_SCL`；`irq=RC522_IRQ -> RC522_INT`；`reset=NRSTPD -> LCD_RESET via R7 0Ω` |
| 射频 | 13.56MHz RFID 天线链路 | `frontend=WS1850S`；`tx=TX1/TX2 differential`；`antenna=L2 ANT_Hole`；`series_inductors=L1/L3 1uH`；`rx=R2 1KΩ; C7 1nF; R3 1.5KΩ` |
| 时钟 | RFID 27.12MHz 时钟 | `crystal=Y1 27.12MHz`；`pins=U1 OSCIN/OSCOUT`；`loads=C6/C9 15pF` |
| 接口 | LCD 与触摸连接 | `lcd=RS,MOSI,SCK,CS,RESET,BL`；`touch=INT,SCL,SDA,RST`；`connector=BTB1 OK-24M024-04`；`backlight=Q1 LN2324DT2AG` |
| GPIO 与控制信号 | 显示与触摸 GPIO 映射 | `lcd_rs=G4`；`lcd_mosi=G5`；`lcd_sck=G6`；`lcd_cs=G7`；`lcd_reset=G8`；`lcd_bl=G9`；`tp_sda=G11`；`tp_scl=G12`；`tp_int=G14` |
| GPIO 与控制信号 | EC30 旋转编码器 | `encoder=J5 EC30-16bit`；`a=G41`；`b=G40`；`pullups=R21/R22 10KΩ`；`filters=C22/C23 100nF`；`common=GND` |
| 总线 | RTC8563 I2C | `scl=TP_SCL / G12`；`sda=TP_SDA / G11`；`interrupt=INT -> WAKE`；`crystal=Y2 32.768KHz +/-20ppm 12.5pF` |
| GPIO 与控制信号 | 蜂鸣器输出 | `gpio=G3`；`net=beep`；`driver=Q5 SS8050 Y1`；`load=LS1 Buzzer` |
| 接口 | Port A 与 Port B | `port_a=SCL,SDA,+5VOUT,GND`；`port_b=G1,G0,+5VOUT,GND` |
| 总线地址 | RFID、RTC 与触摸地址 | `WS1850S=0x28`；`RTC8563=0x51`；`FT3267=0x38`；`schematic_address_text=false` |
| 核心器件 | GC9A01/FT3267 与 240x240 | `lcd_driver=GC9A01`；`touch_driver=FT3267`；`size=1.28 inch`；`resolution=240x240`；`schematic_model_shown=false` |
| 内存与 Flash | Stamp-S3 8MB Flash | `documented_soc=ESP32-S3FN8`；`documented_flash=8MB`；`internal_memory_shown=false` |
| 保护电路 | 宽压与接口保护 | `input_diode=D13 B5819W SL`；`input_tvs=D12 SD36`；`wake_esd=D5 PESDNC2FD3V3B`；`signal_links=R7/R8/R9/R29 0Ω` |

## 待确认事项

- `address.documented-i2c`：正文给出 WS1850S=0x28、RTC8563=0x51、FT3267=0x38，但两张原理图未直接打印这些数值地址。（证据：图 1d8705f9d82d / 第 1 页 / 显示/RFID 页 U1/BTB1，无地址文字; 图 0528f589274c / 第 1 页 / 主板页 U5，无地址文字）
- `component.documented-display`：正文写 GC9A01、FT3267、1.28 inch 240x240；原理图仅显示 BTB1/P1 显示触摸接口，未打印面板驱动型号或分辨率。（证据：图 1d8705f9d82d / 第 1 页 / 显示/RFID 页 BTB1/P1，无 GC9A01/FT3267/240x240 文字）
- `memory.documented-flash`：正文写 ESP32-S3FN8 与 8MB Flash，主板原理图只画 M1 Stamp-S3 接口，未展示模组内部存储器或容量字段。（证据：图 0528f589274c / 第 1 页 / 主板页 M1 STAMP-S3-DIP-1.27）
- `review.i2c-addresses`：K130 当前 WS1850S、RTC8563 与 FT3267 的正式 7-bit 地址是否分别为 0x28、0x51、0x38？；原因：地址来自正文，原理图未直接打印。
- `review.display-spec`：K130 当前圆屏是否固定为 GC9A01+FT3267、1.28 inch、240x240？；原因：面板内部型号与分辨率未在原理图打印。
- `review.flash-capacity`：K130 当前 Stamp-S3 内部 Flash 是否固定为 8MB？；原因：主板图未展示模组内部存储器。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1d8705f9d82d57055876ab9d3a01eb0ae8e4b1610880c99568b4b360f5b47c1f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/499/Sch_M5Dial_sch_01.png` |
| 2 | 1 | `0528f589274c10708c0eb75b8f10f0cc9f0d02a4adef8b0e2d31747cd6252a88` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/499/Sch_M5Dial_sch_02.png` |

---

源文档：`zh_CN/core/M5Dial.md`

源文档 SHA-256：`89202780d7b2108558ae1bd10eb257874a8c7a5a6789174edd21bdde834cddee`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
