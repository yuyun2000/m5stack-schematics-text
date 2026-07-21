# Cardputer-Adv 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Cardputer-Adv |
| SKU | K132-Adv |
| 产品 ID | `cardputer-adv-b4ebce93d617` |
| 源文档 | `zh_CN/core/Cardputer-Adv.md` |

## 概述

Cardputer-Adv 以 M1 STAMP-S3-DIP-1.27/ESP32-S3FN8 为主控，板上集成 TCA8418RTWR 56 键矩阵、BMI270、ES8311 音频编解码、MEMS 麦克风、NS4150B 扬声器功放、microSD、红外和 Grove/14P 扩展接口。U1 TP4057 管理电池充电，Q1-Q3 与 SW1 形成电池/电源开关路径，U2 SY7088 生成 +5VOUT，U4 SY8089 生成 +3.3V。TCA8418 与 BMI270 共用 G8/G9 I2C，页内地址分别明确为 0x34 和 0x69；ES8311 使用 G8/G9 控制并以 G41/G46/G43/G42 形成 I2S 音频链路。

## 检索关键词

`Cardputer-Adv`、`K132-Adv`、`STAMP-S3-DIP-1.27`、`ESP32-S3FN8`、`TCA8418RTWR`、`TCA8418 0x34`、`BMI270`、`BMI270 0x69`、`ES8311`、`NS4150B`、`MSM381A3729H9PBC`、`TP4057`、`SY7088`、`SY8089`、`CN809J`、`LP3218DT1G`、`microSD`、`TF-015`、`G8 SDA`、`G9 SCL`、`G11 keyboard INT`、`G41 SCLK`、`G46 ASDOUT`、`G43 LRCK`、`G42 DSDIN`、`G12 SD_CS`、`G14 SD_MOSI`、`G40 SD_CLK`、`G39 SD_MISO`、`G44 IR`、`G10 battery ADC`、`PJ-342`、`HP_DET`、`EXT 14P`、`HY2.0_IIC`、`56-key matrix`、`+5VOUT`、`+3.3V`、`VBAT_IN`、`USB Type-C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| M1 | STAMP-S3-DIP-1.27 | Cardputer 主控模组接口，连接显示、键盘、音频、IMU、存储、电源控制与扩展 GPIO | 图 b721dfa2ce19 / 第 1 页 / 主板第1页 D2-D3 M1 STAMP-S3-DIP-1.27 与 P1/P2 引脚 |
| U1 | TP4057 | 从 +5VIN 为 VBAT_IN 充电的单节锂电池充电器 | 图 b721dfa2ce19 / 第 1 页 / 主板第1页 A1 U1 TP4057，VCC/BAT/PROG/CHRG/STDBY |
| U3 | CN809J | VBAT_IN 高边路径的复位监控器 | 图 b721dfa2ce19 / 第 1 页 / 主板第1页 A2 U3 CN809J，VCC/RESET/GND 与 Q1 |
| Q1,Q2,Q3 | LP3218DT1G | VBAT_IN/VBAT_OUT 与 BAT 电源开关路径中的三个高边开关器件 | 图 b721dfa2ce19 / 第 1 页 / 主板第1页 A2-B2 Q1/Q2/Q3 LP3218DT1G 与 SW1/BAT/VBAT 网络 |
| U2 | SY7088 | 由 VBAT_OUT 生成 +5VOUT 的开关电源 | 图 b721dfa2ce19 / 第 1 页 / 主板第1页 A3-A4 虚线框 U2 SY7088、L1、D2 与反馈 |
| U4 | SY8089 | 由 VBAT_OUT 生成 +3.3V 的降压转换器 | 图 b721dfa2ce19 / 第 1 页 / 主板第1页 B3-B4 U4 SY8089、L2、R11/R13 |
| U9 | TCA8418RTWR | I2C 键盘矩阵扫描器，连接 7 行8列共56键 | 图 cf469cc225c4 / 第 1 页 / 主板第2页 B1 U9 TCA8418RTWR，ROW0-ROW6、COL0-COL7、INT/SCL/SDA 与 7-bit Address 34H |
| S1-S56 | SW-PB | 由 ROW0-ROW6 与 COL0-COL7 组成的 7×8、56 键矩阵 | 图 cf469cc225c4 / 第 1 页 / 主板第2页 B2-D4 S1-S56 全部按键矩阵 |
| U7 | BMI270 | 连接 G8/G9 I2C 的六轴惯性传感器 | 图 3162cda432ca / 第 1 页 / 主板第3页 A1-B1 U7 BMI270，SDX/SCX、SDO、地址 69H |
| U6 | ES8311 | I2C 控制、全双工 I2S 音频编解码器 | 图 3162cda432ca / 第 1 页 / 主板第3页 C2 U6 ES8311，CCLK/C_DATA/SCLK/ASDOUT/LRCK/DSDIN/MIC/OUT |
| U8 | MSM381A3729H9PBC | 连接 ES8311 MIC_P/MIC_N 的 MEMS 麦克风 | 图 3162cda432ca / 第 1 页 / 主板第3页 D1 U8 MSM381A3729H9PBC，MIC_P/MIC_N/VDD/GND |
| U5 | NS4150B | 由 ES8311 DAC 输出驱动扬声器的 D 类功放 | 图 3162cda432ca / 第 1 页 / 主板第3页 B2-B3 U5 NS4150B，INP/INN/CTRL/VoP/VoN 与 J4 |
| J4 | Header 2 | NS4150B 差分扬声器输出接口 | 图 3162cda432ca / 第 1 页 / 主板第3页 B3 J4 Header 2，连接 U5 VoP/VoN 经 FB1/FB2 |
| J7 | PJ-342 | 3.5mm 音频输出和耳机插入检测接口 | 图 3162cda432ca / 第 1 页 / 主板第3页 C3-D3 J7 PJ-342，DAC_P、HP_DET 与插拔触点 |
| J3 | TF-015 | microSD 卡槽，连接 SPI CS/MOSI/CLK/MISO 与 3.3V/GND | 图 b721dfa2ce19 / 第 1 页 / 主板第1页 D1-D2 J3 TF-015 与 G12/G14/G40/G39、D9-D12 |
| J2,SW2 | HY-2.0_IIC / SW-SPDT | Grove I2C 接口，SW2 选择 +5VOUT 或 +5VIN 作为 VCC | 图 b721dfa2ce19 / 第 1 页 / 主板第1页 C4 J2 HY-2.0_IIC、SW2 与 SCL/SDA/VCC/GND |
| P3 | HDR-SMD_14P-P2.54 | 14针 EXT 总线，承载 RESET/INT/BUSY/SPI/I2C/UART 与 5VIN/5VOUT/GND | 图 6f970d99f036 / 第 1 页 / 主板第4页中央 P3 HDR-SMD_14P-P2.54，1-14脚 |
| IR1,R14 | IR LED / 22Ω | 由 G44 驱动的红外发射 LED 与限流电阻 | 图 b721dfa2ce19 / 第 1 页 / 主板第1页 D4 G44-IR1-R14 22Ω-GND |
| M1 | STAMP-S3M | Stamp-S3A 模组针脚载体，内部连接 ESP32-S3、RGB、Boot、USB与电源 | 图 1156e645de35 / 第 1 页 / Stamp页 C4 M1 STAMP-S3M 1-28脚 |
| U1 | ESP32-S3FN8 | Stamp-S3A 内部主 SoC，连接 GPIO、USB、射频、40MHz 与集成 Flash 电源 | 图 1156e645de35 / 第 1 页 / Stamp页 A2-C2 U1 ESP32-S3FN8 |
| ANT1,X1 | PCB antenna / 40MHz crystal | Stamp-S3A 的2.4GHz天线匹配与40MHz主时钟 | 图 1156e645de35 / 第 1 页 / Stamp页 A1 ANT1 匹配网络与 B1 X1 40MHz/L3/C9/C14 |
| U4 | JW5712 | Stamp-S3A 内部 VIN_5V 到 VDD_3V3 的 DC/DC | 图 1156e645de35 / 第 1 页 / Stamp页 D1-D2 U4 JW5712 与 L4 |
| J2,F1,D3,D4,D14 | USB-TYPEC / PPTC / PESD | Stamp-S3A 模组 USB-C 数据、电源与保护电路 | 图 1156e645de35 / 第 1 页 / Stamp页 D3-D4 USB-TYPEC、USB_D_P/N、F1与ESD器件 |
| U3,S1 | WS2812 / SMT_SW_1TS026A | Stamp-S3A 板载 RGB LED 与 GPIO0 Boot/用户按键 | 图 1156e645de35 / 第 1 页 / Stamp页 B3 RGB LED U3 与 C3 BTN-USER S1 |

## 系统结构

### Cardputer-Adv 总体架构

Stamp-S3A 控制 TCA8418 键盘、BMI270、ES8311音频、microSD、红外与扩展接口；TP4057/Q1-Q3/SW1管理电池路径，SY7088/SY8089分别生成5V和3.3V。

- 参数与网络：`controller=M1 STAMP-S3-DIP-1.27`；`keyboard=U9 TCA8418RTWR`；`imu=U7 BMI270`；`audio=U6 ES8311 + U5 NS4150B`；`storage=J3 microSD`；`power=TP4057 + SY7088 + SY8089`
- 证据：图 b721dfa2ce19 / 第 1 页 / 主板第1页电源/主控/接口; 图 cf469cc225c4 / 第 1 页 / 主板第2页键盘; 图 3162cda432ca / 第 1 页 / 主板第3页IMU/音频

## 电源

### TP4057充电路径

+5VIN经R1 0.8Ω进入U1 TP4057，BAT pin3输出VBAT_IN，PROG pin6经R5 3.3KΩ接GND。

- 参数与网络：`input=+5VIN`；`charger=U1 TP4057`；`series=R1 0.8Ω`；`battery_net=VBAT_IN`；`program=R5 3.3KΩ`
- 证据：图 b721dfa2ce19 / 第 1 页 / 主板第1页 A1 U1/R1/R5/VBAT_IN

### 电池与电源开关路径

J1 BAT+/BAT-连接Q2/Q3 LP3218DT1G与SW1，形成BAT到VBAT_IN的机械开关路径；Q1与U3 CN809J控制VBAT_IN到VBAT_OUT。

- 参数与网络：`battery_connector=J1 BAT+/BAT-`；`switch=SW1 SPDT`；`battery_fets=Q2/Q3 LP3218DT1G`；`output_fet=Q1 LP3218DT1G`；`supervisor=U3 CN809J`
- 证据：图 b721dfa2ce19 / 第 1 页 / 主板第1页 A2-B2 J1/Q1-Q3/SW1/U3

### VBAT_OUT到+5VOUT

VBAT_OUT经R2 0Ω进入U2 SY7088/L1 1.5uH，反馈R4 75KΩ/R6 22KΩ，输出经D2 SS34形成+5VOUT。

- 参数与网络：`input=VBAT_OUT`；`converter=U2 SY7088`；`inductor=L1 1.5uH`；`feedback=R4 75KΩ; R6 22KΩ`；`output=+5VOUT`
- 证据：图 b721dfa2ce19 / 第 1 页 / 主板第1页 A3-A4 SY7088虚线框

### VBAT_OUT到+3.3V

U4 SY8089由VBAT_OUT供电，LX经L2 4.7uH输出+3.3V，反馈为R11 68KΩ/R13 15KΩ。

- 参数与网络：`input=VBAT_OUT`；`converter=U4 SY8089`；`inductor=L2 4.7uH`；`feedback=R11 68KΩ; R13 15KΩ`；`output=+3.3V`
- 证据：图 b721dfa2ce19 / 第 1 页 / 主板第1页 B3-B4 U4/L2/R11/R13

## 接口

### HY2.0-4P Grove接口

J2 pin1=IIC_SCL、pin2=IIC_SDA、pin3=VCC、pin4=GND；SW2选择+5VOUT或+5VIN作为VCC，R3/R10各10KΩ上拉信号。

- 参数与网络：`pin1=IIC_SCL`；`pin2=IIC_SDA`；`pin3=selected +5V`；`pin4=GND`；`power_select=SW2 +5VOUT/+5VIN`；`pullups=R3/R10 10KΩ`
- 证据：图 b721dfa2ce19 / 第 1 页 / 主板第1页 C4 J2/SW2/R3/R10

### 14针EXT精确映射

P3 pin1 G3 RESET、2 +5VIN、3 G4 INT、4 GND、5 G6 BUSY、6 +5VOUT、7 G40 SCK、8 G8 SDA、9 G14 MOSI、10 G9 SCL、11 G39 MISO、12 G13 GPS-RX、13 G5 CS、14 G15 GPS-TX。

- 参数与网络：`pins1_7=1 G3 RESET; 2 +5VIN; 3 G4 INT; 4 GND; 5 G6 BUSY; 6 +5VOUT; 7 G40 SCK`；`pins8_14=8 G8 SDA; 9 G14 MOSI; 10 G9 SCL; 11 G39 MISO; 12 G13 GPS-RX; 13 G5 CS; 14 G15 GPS-TX`
- 证据：图 6f970d99f036 / 第 1 页 / 主板第4页 P3 HDR-SMD_14P-P2.54

### Stamp-S3A原生USB

Stamp内部GPIO19/GPIO20分别连接USB_D_N/USB_D_P，经共模器件与ESD到USB-C；VBUS经F1 6V/1A PPTC形成VIN_5V。

- 参数与网络：`dn=GPIO19 USB_D_N`；`dp=GPIO20 USB_D_P`；`connector=J2 USB-TYPEC`；`protection=D3/D4/D14 PESD; F1 PPTC`
- 证据：图 1156e645de35 / 第 1 页 / Stamp页 U1 GPIO19/20与D3-D4 USB区

## 总线

### TCA8418键盘I2C

U9 SDA=G8、SCL=G9、INT=G11；R35/R36/R37各3.3KΩ上拉到+3.3V。

- 参数与网络：`device=U9 TCA8418RTWR`；`sda=G8`；`scl=G9`；`interrupt=G11`；`pullups=R35/R36/R37 3.3KΩ`
- 证据：图 cf469cc225c4 / 第 1 页 / 主板第2页 U9 SDA/SCL/INT与R35-R37

### BMI270 I2C

U7 SDX连接G8、SCX连接G9，SDO由R43 3.3KΩ上拉+3.3V；INT1/INT2与辅助I2C引脚未连接。

- 参数与网络：`device=U7 BMI270`；`sda=G8`；`scl=G9`；`sdo_pullup=R43 3.3KΩ`；`interrupts_connected=false`
- 证据：图 3162cda432ca / 第 1 页 / 主板第3页 U7 G8/G9/SDO/INT1/INT2/ASDx/ASCx

### ES8311控制与I2S映射

ES8311 C_DATA=G8、CCLK=G9；SCLK=G41、ASDOUT=G46、LRCK=G43、DSDIN=G42，形成全双工数字音频链路。

- 参数与网络：`codec=U6 ES8311`；`sda=G8`；`scl=G9`；`sclk=G41`；`asdout=G46`；`lrck=G43`；`dsdin=G42`
- 证据：图 3162cda432ca / 第 1 页 / 主板第3页 U6 ES8311左侧数字接口网络

## 总线地址

### TCA8418 I2C地址

键盘页明确标注TCA8418 7-bit Address 34H，即0x34。

- 参数与网络：`device=U9 TCA8418RTWR`；`address=0x34`；`format=7-bit`
- 证据：图 cf469cc225c4 / 第 1 页 / 主板第2页 U9下方文字 7-bit Address 34H

### BMI270 I2C地址

IMU页明确标注BMI270 7-bit Address 69H，即0x69。

- 参数与网络：`device=U7 BMI270`；`address=0x69`；`format=7-bit`
- 证据：图 3162cda432ca / 第 1 页 / 主板第3页 U7上方文字 7-bit Address 69H

## GPIO 与控制信号

### 56键矩阵

U9使用ROW0-ROW6和COL0-COL7扫描S1-S56的7×8矩阵；COL0-COL7分别经R27-R34 22Ω串联，ROW7/COL8/COL9未连接。

- 参数与网络：`rows=ROW0-ROW6`；`columns=COL0-COL7`；`keys=56`；`series=R27-R34 22Ω`；`unused=ROW7, COL8, COL9`
- 证据：图 cf469cc225c4 / 第 1 页 / 主板第2页U9与S1-S56完整矩阵

### 红外发射GPIO

G44直接连接IR1红外LED，再经R14 22Ω接GND。

- 参数与网络：`gpio=G44`；`emitter=IR1`；`resistor=R14 22Ω`；`direction=output`
- 证据：图 b721dfa2ce19 / 第 1 页 / 主板第1页 D4 G44/IR1/R14

### EN与G0按键

BTN1将EN拉到GND并由R15 10KΩ上拉+3.3V；BTN2将G0拉到GND并由R18 10KΩ上拉，D4/D5提供ESD保护。

- 参数与网络：`reset=BTN1 EN; R15 10KΩ`；`boot=BTN2 G0; R18 10KΩ`；`protection=D4/D5 PESDNC2FD3V3B`
- 证据：图 b721dfa2ce19 / 第 1 页 / 主板第1页 C1 BTN1/BTN2/EN/G0/D4/D5

## 时钟

### Stamp-S3A 40MHz时钟

ESP32-S3 XTAL_P/N连接X1 40MHz晶振，L3 10nH位于正端，C9/C14各12pF接GND。

- 参数与网络：`crystal=X1 40MHz`；`inductor=L3 10nH`；`capacitors=C9/C14 12pF`
- 证据：图 1156e645de35 / 第 1 页 / Stamp页 B1 X1/L3/C9/C14/XTAL_40M_P/N

## 存储

### microSD SPI映射

J3 TF-015 CS=G12、MOSI=G14、CLK=G40、MISO=G39，四线各经R19-R22 33Ω并由D9-D12保护，卡槽供电为+3.3V。

- 参数与网络：`cs=G12`；`mosi=G14`；`clk=G40`；`miso=G39`；`series=R19-R22 33Ω`；`esd=D9-D12`；`supply=+3.3V`
- 证据：图 b721dfa2ce19 / 第 1 页 / 主板第1页 D1-D2 J3/R19-R22/D9-D12

## 内存与 Flash

### Stamp-S3A集成Flash

Stamp原理图使用ESP32-S3FN8，VDD_SPI接FLASH_VCC，SPI Flash外部引脚标记未连接，页面未画外部Flash或PSRAM。

- 参数与网络：`soc=ESP32-S3FN8`；`flash_supply=FLASH_VCC`；`external_flash_shown=false`；`external_psram_shown=false`
- 证据：图 1156e645de35 / 第 1 页 / Stamp页U1 VDD_SPI/FLASH_VCC与SPIHD-SPIQ未连接

## 音频

### MEMS麦克风输入

U8 MSM381A3729H9PBC OUT/GND形成MIC_P/MIC_N差分网络，经C22/C23各1uF连接ES8311 MIC1P/MIC1N。

- 参数与网络：`microphone=U8 MSM381A3729H9PBC`；`positive=MIC_P via C22 1uF`；`negative=MIC_N via C23 1uF`；`codec=U6 ES8311`
- 证据：图 3162cda432ca / 第 1 页 / 主板第3页 D1 U8与C22/C23/U6 MIC1P/MIC1N

### NS4150B扬声器输出

DAC_P经R16/R17与C13/C15进入U5 NS4150B INP/INN，AMP_EN控制CTRL，VoP/VoN经FB1/FB2输出到J4。

- 参数与网络：`amplifier=U5 NS4150B`；`input=DAC_P via R16/R17 and C13/C15`；`enable=AMP_EN`；`output=VoP/VoN -> FB1/FB2 -> J4`
- 证据：图 3162cda432ca / 第 1 页 / 主板第3页 B2-B3 U5输入/控制/输出

### 3.5mm耳机输出与功放关闭

ES8311 OUTP经C30 22uF形成DAC_P并进入PJ-342；插拔触点生成HP_DET，经2N7002T相关网络影响AMP_EN。

- 参数与网络：`codec_output=OUTP -> C30 22uF -> DAC_P`；`jack=J7 PJ-342`；`detect=HP_DET`；`amplifier_control=AMP_EN`
- 证据：图 3162cda432ca / 第 1 页 / 主板第3页 C2-D3 ES8311 OUTP/C30与PJ-342/HP_DET/AMP_EN

## 射频

### Stamp-S3A射频天线

ESP32-S3 LNA_IN经ESP_LNA匹配网络连接ANT1，器件包含L6 0R、L1 2.7nH、C19、C2 2.2pF、C1 1.8pF。

- 参数与网络：`antenna=ANT1`；`soc_pin=LNA_IN`；`matching=L6 0R; L1 2.7nH; C19; C2 2.2pF; C1 1.8pF`
- 证据：图 1156e645de35 / 第 1 页 / Stamp页 A1 ANT1与ESP_LNA/LNA_IN

## 模拟电路

### 电池电压检测

VBAT_IN经R8/R12各100KΩ分压至G10，C10 100nF从G10接GND。

- 参数与网络：`source=VBAT_IN`；`upper=R8 100KΩ`；`lower=R12 100KΩ`；`adc=G10`；`filter=C10 100nF`
- 证据：图 b721dfa2ce19 / 第 1 页 / 主板第1页 B2 VBAT_IN/R8/R12/G10/C10

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Cardputer-Adv 总体架构 | `controller=M1 STAMP-S3-DIP-1.27`；`keyboard=U9 TCA8418RTWR`；`imu=U7 BMI270`；`audio=U6 ES8311 + U5 NS4150B`；`storage=J3 microSD`；`power=TP4057 + SY7088 + SY8089` |
| 电源 | TP4057充电路径 | `input=+5VIN`；`charger=U1 TP4057`；`series=R1 0.8Ω`；`battery_net=VBAT_IN`；`program=R5 3.3KΩ` |
| 电源 | 电池与电源开关路径 | `battery_connector=J1 BAT+/BAT-`；`switch=SW1 SPDT`；`battery_fets=Q2/Q3 LP3218DT1G`；`output_fet=Q1 LP3218DT1G`；`supervisor=U3 CN809J` |
| 模拟电路 | 电池电压检测 | `source=VBAT_IN`；`upper=R8 100KΩ`；`lower=R12 100KΩ`；`adc=G10`；`filter=C10 100nF` |
| 电源 | VBAT_OUT到+5VOUT | `input=VBAT_OUT`；`converter=U2 SY7088`；`inductor=L1 1.5uH`；`feedback=R4 75KΩ; R6 22KΩ`；`output=+5VOUT` |
| 电源 | VBAT_OUT到+3.3V | `input=VBAT_OUT`；`converter=U4 SY8089`；`inductor=L2 4.7uH`；`feedback=R11 68KΩ; R13 15KΩ`；`output=+3.3V` |
| 其他事实 | 电池容量 | `documented_capacity=1750mAh`；`battery_nets=BAT, VBAT_IN`；`capacity_shown=false` |
| 总线 | TCA8418键盘I2C | `device=U9 TCA8418RTWR`；`sda=G8`；`scl=G9`；`interrupt=G11`；`pullups=R35/R36/R37 3.3KΩ` |
| 总线地址 | TCA8418 I2C地址 | `device=U9 TCA8418RTWR`；`address=0x34`；`format=7-bit` |
| GPIO 与控制信号 | 56键矩阵 | `rows=ROW0-ROW6`；`columns=COL0-COL7`；`keys=56`；`series=R27-R34 22Ω`；`unused=ROW7, COL8, COL9` |
| 总线 | BMI270 I2C | `device=U7 BMI270`；`sda=G8`；`scl=G9`；`sdo_pullup=R43 3.3KΩ`；`interrupts_connected=false` |
| 总线地址 | BMI270 I2C地址 | `device=U7 BMI270`；`address=0x69`；`format=7-bit` |
| 总线 | ES8311控制与I2S映射 | `codec=U6 ES8311`；`sda=G8`；`scl=G9`；`sclk=G41`；`asdout=G46`；`lrck=G43`；`dsdin=G42` |
| 音频 | MEMS麦克风输入 | `microphone=U8 MSM381A3729H9PBC`；`positive=MIC_P via C22 1uF`；`negative=MIC_N via C23 1uF`；`codec=U6 ES8311` |
| 音频 | NS4150B扬声器输出 | `amplifier=U5 NS4150B`；`input=DAC_P via R16/R17 and C13/C15`；`enable=AMP_EN`；`output=VoP/VoN -> FB1/FB2 -> J4` |
| 音频 | 3.5mm耳机输出与功放关闭 | `codec_output=OUTP -> C30 22uF -> DAC_P`；`jack=J7 PJ-342`；`detect=HP_DET`；`amplifier_control=AMP_EN` |
| 音频 | 音频额定参数 | `documented_mic_snr=65dB`；`documented_speaker=8Ω 1W`；`schematic_ratings_shown=false` |
| 存储 | microSD SPI映射 | `cs=G12`；`mosi=G14`；`clk=G40`；`miso=G39`；`series=R19-R22 33Ω`；`esd=D9-D12`；`supply=+3.3V` |
| 接口 | HY2.0-4P Grove接口 | `pin1=IIC_SCL`；`pin2=IIC_SDA`；`pin3=selected +5V`；`pin4=GND`；`power_select=SW2 +5VOUT/+5VIN`；`pullups=R3/R10 10KΩ` |
| 接口 | 14针EXT精确映射 | `pins1_7=1 G3 RESET; 2 +5VIN; 3 G4 INT; 4 GND; 5 G6 BUSY; 6 +5VOUT; 7 G40 SCK`；`pins8_14=8 G8 SDA; 9 G14 MOSI; 10 G9 SCL; 11 G39 MISO; 12 G13 GPS-RX; 13 G5 CS; 14 G15 GPS-TX` |
| GPIO 与控制信号 | 红外发射GPIO | `gpio=G44`；`emitter=IR1`；`resistor=R14 22Ω`；`direction=output` |
| GPIO 与控制信号 | EN与G0按键 | `reset=BTN1 EN; R15 10KΩ`；`boot=BTN2 G0; R18 10KΩ`；`protection=D4/D5 PESDNC2FD3V3B` |
| 内存与 Flash | Stamp-S3A集成Flash | `soc=ESP32-S3FN8`；`flash_supply=FLASH_VCC`；`external_flash_shown=false`；`external_psram_shown=false` |
| 时钟 | Stamp-S3A 40MHz时钟 | `crystal=X1 40MHz`；`inductor=L3 10nH`；`capacitors=C9/C14 12pF` |
| 射频 | Stamp-S3A射频天线 | `antenna=ANT1`；`soc_pin=LNA_IN`；`matching=L6 0R; L1 2.7nH; C19; C2 2.2pF; C1 1.8pF` |
| 接口 | Stamp-S3A原生USB | `dn=GPIO19 USB_D_N`；`dp=GPIO20 USB_D_P`；`connector=J2 USB-TYPEC`；`protection=D3/D4/D14 PESD; F1 PPTC` |
| 其他事实 | LCD型号与分辨率 | `documented_controller=ST7789V2`；`documented_size=1.14 inch`；`documented_resolution=240x135`；`schematic_model_shown=false` |

## 待确认事项

- `other.documented-battery-capacity`：产品正文标注内置电池1750mAh，但原理图只显示BAT/VBAT_IN连接与充电电路，没有电池料号或容量。（证据：图 b721dfa2ce19 / 第 1 页 / 主板第1页 J1/J8与TP4057电池路径，无容量文本）
- `audio.documented-ratings`：产品正文称MEMS麦克风SNR 65dB、扬声器8Ω/1W，但原理图只确认器件型号和连接，未标整机SNR或扬声器额定值。（证据：图 3162cda432ca / 第 1 页 / 主板第3页完整音频链路，无SNR和扬声器功率文本）
- `other.documented-display`：产品正文标注ST7789V2、1.14英寸、240×135，但所收录主板页仅给显示接口/控制信号，未在当前页面标出面板型号和分辨率。（证据：图 1156e645de35 / 第 1 页 / Stamp页LCD区仅见DISP_RST/RS/MOSI/SCK/CS与连接器，无ST7789V2/分辨率文本）
- `review.battery-capacity`：K132-Adv当前电池料号和额定容量是否确认为1750mAh，保护板规格是什么？；原因：容量来自产品正文，原理图只显示电池连接和充电/开关路径。
- `review.audio-ratings`：Cardputer-Adv当前麦克风与扬声器是否满足65dB SNR和8Ω/1W额定参数？；原因：当前原理图只给出音频器件型号与连接，没有整机SNR和扬声器额定值。
- `review.display-model`：K132-Adv当前LCD面板是否确认为ST7789V2、1.14英寸、240×135，接口连接器具体对应哪一物料？；原因：型号、尺寸和分辨率来自产品正文，当前原理图只显示显示控制网络。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `b721dfa2ce1979194d19c425fe1a2ac842b7e0b1846722fde165fcf0dca7a3d9` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_01.png` |
| 2 | 1 | `cf469cc225c427da5cc46f197ddbd728e3c5b1ebad65a0d1749150d89757bacf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_02.png` |
| 3 | 1 | `3162cda432ca2cb9e6a3f732d063942dcdbb152f79a64f1f9eaae487e1cd009b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_03.png` |
| 4 | 1 | `6f970d99f03603ac21277e9305132a80d16424d6656ab3cf62a1f743e79a7923` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Sch_M5CardputerAdv_v1.0_2025_06_20_17_19_58_page_04.png` |
| 5 | 1 | `1156e645de35fe68e6458e9131657c8f02045bbcd14f97ab190bb1486ee7a1c5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1150/Sch_StampS3_v0.3.3_page_01.png` |

---

源文档：`zh_CN/core/Cardputer-Adv.md`

源文档 SHA-256：`1e32412e43b7e951fa7ca68e8b6e2922ea11aa22216fe06db559cdd463fb9e65`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
