# Faces Kit 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Faces Kit |
| SKU | K005 |
| 产品 ID | `faces-kit-86a5bcb22553` |
| 源文档 | `zh_CN/core/face_kit.md` |

## 概述

Faces Kit 的本地原理图由 IP5306 充电/接口板、QWERTY 面板、Calculator 面板和 GameBoy 面板四张单页组成。三个功能面板均以 ATmega328P-AU 为控制器，通过 M5 Bus 的 SDA/SCL 与主机通信，并分别扫描 30+5 键、4x5 键和八个游戏按键。充电板以 IP5306 管理 5V 与电池，并将 M5 Bus、24/30/15/8 针接口网络转接到各面板。

## 检索关键词

`Faces Kit`、`K005`、`ATmega328P-AU`、`IP5306`、`M5 Bus`、`SDA`、`SCL`、`I2C`、`0x08`、`QWERTY`、`Calculator`、`GameBoy`、`S1-S35`、`4x5 matrix`、`SPACE`、`BACK SPACE`、`ENTER`、`START`、`SELECT`、`UP`、`DOWN`、`LEFT`、`RIGHT`、`A`、`B`、`RESET`、`ISP Header 6`、`5V`、`3V3`、`BAT`、`HPR`、`GPIO21 SDA`、`GPIO22 SCL`、`G5`、`R2/16`、`T2/17`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 (charger) | IP5306 | 充电板电池充放电与 5V 电源管理 | 图 64fe8969ae3b / 第 1 页 / 第 1 资源页左中充电板 U1 IP5306、L1/R1/C1-C5 |
| P1 (charger) | BATTERY | IP5306 BAT/KEY 与电池连接器 | 图 64fe8969ae3b / 第 1 页 / 第 1 资源页充电板 P1 BATTERY |
| P2 (charger) | 4 PIN | 5V、GND 与充电板接口连接器 | 图 64fe8969ae3b / 第 1 页 / 第 1 资源页充电板 P2 4 PIN |
| BUS1/BUS2 | M5_BUS | 充电板和接口板的 M5 Bus 转接连接器 | 图 64fe8969ae3b / 第 1 页 / 第 1 资源页左侧 BUS1/BUS2 与右侧接口板 30/24/15/8 PIN |
| U1 (QWERTY) | ATmega328P-AU | QWERTY 面板 I2C 从控与键盘扫描控制器 | 图 0f5fa65390ea / 第 1 页 / 第 2 资源页左侧 U1 ATmega328P-AU |
| S1-S30 | SW-PB | QWERTY 主字符 10x3 键阵 | 图 0f5fa65390ea / 第 1 页 / 第 2 资源页右侧 S1-S30，列 O1-O3、行 A-J |
| S31-S35 | SW-PB | QWERTY SPACE/EN/alt/aA/ENTER 功能键 | 图 0f5fa65390ea / 第 1 页 / 第 2 资源页下方 S31-S35 与 P1 |
| P1 (QWERTY) | Header 6 | QWERTY 面板 ISP/复位连接器 | 图 0f5fa65390ea / 第 1 页 / 第 2 资源页下方 P1 Header 6、RESET |
| U1 (Calculator) | ATmega328P-AU | Calculator 面板 I2C 从控与 4x5 键阵扫描控制器 | 图 9698c28b8392 / 第 1 页 / 第 3 资源页左侧 U1 ATmega328P-AU |
| S1-S15 + five top switches | SW-PB | Calculator 的 4 行 x 5 列二十键矩阵 | 图 9698c28b8392 / 第 1 页 / 第 3 资源页右侧 O1-O4/A-E 矩阵，AC/0-9/运算键 |
| P1 (Calculator) | Header 6 | Calculator 面板 ISP/复位连接器 | 图 9698c28b8392 / 第 1 页 / 第 3 资源页下方 P1 Header 6 |
| U1 (GameBoy) | ATmega328P-AU | GameBoy 面板 I2C 从控与按键读取控制器 | 图 e3dbc484d0f5 / 第 1 页 / 第 4 资源页左侧 U1 ATmega328P-AU |
| S1-S8 | SW-PB | GameBoy UP/DOWN/LEFT/RIGHT/A/B/SELECT/START 八键输入 | 图 e3dbc484d0f5 / 第 1 页 / 第 4 资源页下方 S1-S8 |
| P1 (GameBoy) | Header 6 | GameBoy 面板 ISP/复位连接器 | 图 e3dbc484d0f5 / 第 1 页 / 第 4 资源页下方 P1 Header 6 |

## 系统结构

### Faces Kit 电路组成

本地四页原理图包含 IP5306 充电/接口板及 QWERTY、Calculator、GameBoy 三块 ATmega328P-AU 功能面板；三面板通过 M5 Bus SDA/SCL 与主机连接。

- 参数与网络：`power=IP5306 charging board`；`controllers=three ATmega328P-AU`；`panels=QWERTY, Calculator, GameBoy`；`host_bus=M5 Bus SDA/SCL`
- 证据：图 64fe8969ae3b / 第 1 页 / 第 1 资源页完整充电/接口板; 图 0f5fa65390ea / 第 1 页 / 第 2 资源页 QWERTY; 图 9698c28b8392 / 第 1 页 / 第 3 资源页 Calculator; 图 e3dbc484d0f5 / 第 1 页 / 第 4 资源页 GameBoy

## 电源

### IP5306 充放电电路

U1 IP5306 VIN 接 +5V，BAT 接 P1 电池，SW 经 L1 1uH 与 R1 2Ω/电容网络形成 VOUT；KEY 接电源按键网络，LED1-LED3 为状态输出。

- 参数与网络：`controller=U1 IP5306`；`input=+5V`；`battery=P1 BATTERY`；`inductor=L1 1uH`；`series=R1 2Ω`；`status=LED1/LED2/LED3`
- 证据：图 64fe8969ae3b / 第 1 页 / 第 1 资源页 U1/L1/R1/C1-C5/P1

## 接口

### M5 Bus 接口板

接口板提供 30 PIN、24 PIN、两组 15 PIN 和 8 PIN M5 Bus 映射，引出 5V、3.3V、GND、BAT、HPWR、GPIO、SPI、UART 与 I2C。

- 参数与网络：`connectors=30 PIN, 24 PIN, 15 PIN x2, 8 PIN`；`power=5V,3.3V,GND,BAT,HPWR`；`buses=SPI,UART,I2C`；`i2c=G21/IIS_SDA and G22/IIC_SCL on shown maps`
- 证据：图 64fe8969ae3b / 第 1 页 / 第 1 资源页右侧接口板全部 BUS 映射

## 总线

### 面板 I2C 连接

三块 ATmega328P-AU 的 PC4/SDA pin27 与 PC5/SCL pin28 分别接 M5 Bus SDA pin16 与 SCL pin18，面板由 3V3/GND 供电。

- 参数与网络：`controller=ATmega328P-AU`；`sda=PC4 pin27 -> BUS1 pin16 SDA`；`scl=PC5 pin28 -> BUS1 pin18 SCL`；`supply=3V3`；`role=I2C peripheral`
- 证据：图 0f5fa65390ea / 第 1 页 / 第 2 资源页 BUS1/U1 SDA/SCL; 图 9698c28b8392 / 第 1 页 / 第 3 资源页 BUS1/U1 SDA/SCL; 图 e3dbc484d0f5 / 第 1 页 / 第 4 资源页 BUS1/U1 SDA/SCL

## GPIO 与控制信号

### QWERTY 键盘扫描

QWERTY U1 以 PC1/PC2/PC3 形成 O1/O3/O2 三列选择，以 PD0-PD7、PB0/PB1 形成 A-J 十行，共扫描 S1-S30；PB3-PB7 另接 S31-S35 功能键。

- 参数与网络：`columns=O1,O2,O3`；`rows=A-J`；`main_keys=S1-S30`；`function_keys=S31 SPACE, S32 EN, S33 alt, S34 aA, S35 ENTER`
- 证据：图 0f5fa65390ea / 第 1 页 / 第 2 资源页 U1 与 S1-S35

### Calculator 4x5 键阵

Calculator U1 PC0-PC3 形成 O1-O4，PD2-PD6 形成 A-E，构成四行五列二十键矩阵，包含 AC、数字、运算、M、百分号与正负号键。

- 参数与网络：`outputs=O1-O4`；`inputs=A-E`；`matrix=4x5`；`keys=20`
- 证据：图 9698c28b8392 / 第 1 页 / 第 3 资源页 U1 与右侧 O1-O4/A-E 矩阵

### GameBoy 八键输入

GameBoy S1 UP、S2 DOWN、S3 LEFT、S4 RIGHT、S5 A、S6 B 分别连接 PB0-PB5，S7 SELECT 与 S8 START 连接 PB6/PB7，按下均接地。

- 参数与网络：`up=PB0`；`down=PB1`；`left=PB2`；`right=PB3`；`a=PB4`；`b=PB5`；`select=PB6`；`start=PB7`；`active=low`
- 证据：图 e3dbc484d0f5 / 第 1 页 / 第 4 资源页 U1 PB0-PB7 与 S1-S8

## 时钟

### 面板外部时钟器件

三块 ATmega328P-AU 面板完整单页均未画外部晶振或谐振器，PB6/PB7 仅在 GameBoy/QWERTY 中用于按键。

- 参数与网络：`qwerty_external_crystal=false`；`calculator_external_crystal=false`；`gameboy_external_crystal=false`
- 证据：图 0f5fa65390ea / 第 1 页 / 第 2 资源页 U1 PB6/PB7 与完整时钟范围; 图 9698c28b8392 / 第 1 页 / 第 3 资源页完整单页，无晶振; 图 e3dbc484d0f5 / 第 1 页 / 第 4 资源页 U1 PB6/PB7 与完整时钟范围

## 复位

### 面板复位网络

三块面板均以 ATmega PC6/RESET pin29 形成 RESET，并引到各自 P1 Header 6；QWERTY 另有板载复位/功能键连接。

- 参数与网络：`soc_pin=PC6/RESET pin29`；`connector=P1 pin5 RESET`
- 证据：图 0f5fa65390ea / 第 1 页 / 第 2 资源页 U1/P1 RESET; 图 9698c28b8392 / 第 1 页 / 第 3 资源页 U1/P1 RESET; 图 e3dbc484d0f5 / 第 1 页 / 第 4 资源页 U1/P1 RESET

## 内存与 Flash

### 面板外部存储可见性

三块功能面板仅画 ATmega328P-AU、按键、接口和少量阻容/LED，未画外部 Flash、EEPROM、PSRAM 或存储卡。

- 参数与网络：`external_flash=false`；`external_eeprom=false`；`psram=false`；`memory_card=false`
- 证据：图 0f5fa65390ea / 第 1 页 / 第 2 资源页完整单页; 图 9698c28b8392 / 第 1 页 / 第 3 资源页完整单页; 图 e3dbc484d0f5 / 第 1 页 / 第 4 资源页完整单页

## 调试与烧录

### QWERTY ISP 接口

QWERTY P1 Header 6 引出 ATmega PB3/PB4/PB5、RESET、3V3 和 GND，用于 ISP 下载；RESET 来自 PC6 pin29。

- 参数与网络：`connector=P1 Header 6`；`signals=PB3 MOSI, PB4 MISO, PB5 SCK, RESET, 3V3, GND`
- 证据：图 0f5fa65390ea / 第 1 页 / 第 2 资源页 P1 Header 6 与 U1 PB3-PB5/RESET

### Calculator ISP 接口

Calculator P1 Header 6 引出 PB3/PB4/PB5、RESET、3V3 和 GND。

- 参数与网络：`connector=P1 Header 6`；`signals=PB3,PB4,PB5,RESET,3V3,GND`
- 证据：图 9698c28b8392 / 第 1 页 / 第 3 资源页 P1 Header 6

### GameBoy ISP 接口

GameBoy P1 Header 6 引出 PB3/PB4/PB5、RESET、3V3 和 GND。

- 参数与网络：`connector=P1 Header 6`；`signals=PB3,PB4,PB5,RESET,3V3,GND`
- 证据：图 e3dbc484d0f5 / 第 1 页 / 第 4 资源页 P1 Header 6

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Faces Kit 电路组成 | `power=IP5306 charging board`；`controllers=three ATmega328P-AU`；`panels=QWERTY, Calculator, GameBoy`；`host_bus=M5 Bus SDA/SCL` |
| 电源 | IP5306 充放电电路 | `controller=U1 IP5306`；`input=+5V`；`battery=P1 BATTERY`；`inductor=L1 1uH`；`series=R1 2Ω`；`status=LED1/LED2/LED3` |
| 接口 | M5 Bus 接口板 | `connectors=30 PIN, 24 PIN, 15 PIN x2, 8 PIN`；`power=5V,3.3V,GND,BAT,HPWR`；`buses=SPI,UART,I2C`；`i2c=G21/IIS_SDA and G22/IIC_SCL on shown maps` |
| 总线 | 面板 I2C 连接 | `controller=ATmega328P-AU`；`sda=PC4 pin27 -> BUS1 pin16 SDA`；`scl=PC5 pin28 -> BUS1 pin18 SCL`；`supply=3V3`；`role=I2C peripheral` |
| 总线地址 | ATmega 面板 I2C 地址 | `documented_address=0x08`；`address_width=not shown`；`schematic_address_text=false` |
| GPIO 与控制信号 | QWERTY 键盘扫描 | `columns=O1,O2,O3`；`rows=A-J`；`main_keys=S1-S30`；`function_keys=S31 SPACE, S32 EN, S33 alt, S34 aA, S35 ENTER` |
| GPIO 与控制信号 | Calculator 4x5 键阵 | `outputs=O1-O4`；`inputs=A-E`；`matrix=4x5`；`keys=20` |
| GPIO 与控制信号 | GameBoy 八键输入 | `up=PB0`；`down=PB1`；`left=PB2`；`right=PB3`；`a=PB4`；`b=PB5`；`select=PB6`；`start=PB7`；`active=low` |
| 调试与烧录 | QWERTY ISP 接口 | `connector=P1 Header 6`；`signals=PB3 MOSI, PB4 MISO, PB5 SCK, RESET, 3V3, GND` |
| 调试与烧录 | Calculator ISP 接口 | `connector=P1 Header 6`；`signals=PB3,PB4,PB5,RESET,3V3,GND` |
| 调试与烧录 | GameBoy ISP 接口 | `connector=P1 Header 6`；`signals=PB3,PB4,PB5,RESET,3V3,GND` |
| 复位 | 面板复位网络 | `soc_pin=PC6/RESET pin29`；`connector=P1 pin5 RESET` |
| 时钟 | 面板外部时钟器件 | `qwerty_external_crystal=false`；`calculator_external_crystal=false`；`gameboy_external_crystal=false` |
| 内存与 Flash | 面板外部存储可见性 | `external_flash=false`；`external_eeprom=false`；`psram=false`；`memory_card=false` |

## 待确认事项

- `address.panel-i2c`：产品正文写面板 I2C 从机地址为 0x08，但四张原理图只画 SDA/SCL 网络，未打印数值地址。（证据：图 0f5fa65390ea / 第 1 页 / 第 2 资源页 QWERTY U1 SDA/SCL，无地址文字; 图 9698c28b8392 / 第 1 页 / 第 3 资源页 Calculator U1 SDA/SCL，无地址文字; 图 e3dbc484d0f5 / 第 1 页 / 第 4 资源页 GameBoy U1 SDA/SCL，无地址文字）
- `review.i2c-address`：K005 三种 Faces 面板固件的正式 7-bit I2C 从机地址是否均为 0x08？；原因：地址只出现在产品正文，四张原理图未打印数值地址。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `64fe8969ae3bafbbb7e04d506522667176d5bb911594b977e1a6abc4bd465f9b` | `https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_sch_01.webp` |
| 2 | 1 | `0f5fa65390ea8dac4fe4c11cfc56eef9f198b5773b147cbd4daa7368d421d716` | `https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_sch_02.webp` |
| 3 | 1 | `9698c28b8392f366835b47e6ee943835d02229ee7aa23d007464511885ff8915` | `https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_sch_03.webp` |
| 4 | 1 | `e3dbc484d0f5e689549aa58c2e59c8aaeffb51489be197ffd2d8bf68ec463743` | `https://static-cdn.m5stack.com/resource/docs/products/core/face_kit/face_kit_sch_04.webp` |

---

源文档：`zh_CN/core/face_kit.md`

源文档 SHA-256：`658b7b6155a00dd6bdf1f8d4d6ddee432a47ab426b417643c4d71e0330e14b5b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
