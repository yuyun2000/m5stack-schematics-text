# Stamp-S3Bat DIP 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-S3Bat DIP |
| SKU | S015-DIP |
| 产品 ID | `stamp-s3bat-dip-36a8afc15a95` |
| 源文档 | `zh_CN/core/Stamp-S3Bat_DIP.md` |

## 概述

Stamp-S3Bat DIP 原理图以 ESP32-S3-PICO-1 为主控，USB-C 与 5VIN、电池通过 AW32901FCR、LGS4056HDA 和四路 CH213K 构成多源供电；JW5712 生成 3V3_L2，TPAP7343D-33FS4 生成 3V3_L1，SY7088 生成 EXT_5V_OUT。板上含 IPEX-4 天线、24P BTB、11 路焊盘 GPIO、PY32_PMIC 电源管理控制、ADC 检测和 NeoPixel。DIP 源文档说明默认焊接排针，但原理图没有装配属性。

## 检索关键词

`Stamp-S3Bat DIP`、`S015-DIP`、`Stamp-S3Bat`、`ESP32-S3-PICO-1-N8R8`、`ESP32-S3-PICO-1`、`8MB Flash`、`8MB PSRAM`、`M5PM1`、`M5MP1`、`PY32_PMIC`、`0x6E`、`LGS4056HDA`、`CH213K`、`AW32901FCR`、`JW5712`、`TPAP7343D-33FS4`、`SY7088`、`USB Type-C`、`VBAT`、`SYS_VIN`、`SYS_VBUS`、`3V3_L1`、`3V3_L2`、`EXT_5V_OUT`、`BTB 24P`、`BTB0.408-24PLBDR-M41`、`IPEX-4`、`G47_SCL`、`G48_SDA`、`PY_G4_WAKE`、`G0_BOOT_OUT`、`NeoPixel`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-S3-PICO-1 | Stamp-S3Bat DIP 主控制器 | 图 941fad0422cf / 第 1 页 / A3-D4 ESP32_S3_PICO 区域 U1 ESP32_S3_PICO_1 |
| U2 | PY32_PMIC | 电源、充电、ADC、唤醒、Boot 与 NeoPixel 管理控制器 | 图 941fad0422cf / 第 1 页 / C3-D4 U2 PY32_PMIC 全部控制、ADC 与 I2C 网络 |
| U3 | LGS4056HDA | SYS_VIN 至 VBAT 锂电池充电器 | 图 941fad0422cf / 第 1 页 / A2 Charge 区域 U3 LGS4056HDA、SYS_VIN 与 VBAT |
| U5/U7/U8/U9 | CH213K | USB、5VIN、电池与系统电源路径 OR 控制 | 图 941fad0422cf / 第 1 页 / A2-B2 四个 PowerPath 区域 U5/U7/U8/U9 CH213K |
| U12 | AW32901FCR | USB VBUS 输入过压保护 | 图 941fad0422cf / 第 1 页 / A1-B1 USB_IN 区域 U12 AW32901FCR |
| U4 | JW5712 | SYS_VBUS 至 3V3_L2 降压转换器 | 图 941fad0422cf / 第 1 页 / B1-B2 DCDC 区域 U4 JW5712 与 3V3_L2 |
| U11 | TPAP7343D-33FS4 | SYS_VBUS 至 3V3_L1 低压差稳压器 | 图 941fad0422cf / 第 1 页 / C2 U11 TPAP7343D-33FS4、SYS_VBUS 与 3V3_L1 |
| U6 | SY7088 | SYS_VBUS 至 EXT_5V_OUT 升压转换器 | 图 941fad0422cf / 第 1 页 / D1-D2 U6 SY7088、5VOUT_EN 与 EXT_5V_OUT |
| J1 | USB_C_16P_Horizontal | USB Type-C 供电与原生 USB 数据接口 | 图 941fad0422cf / 第 1 页 / A1 USB-C 区域 J1 USB_C_16P_Horizontal |
| J4 | IPEX_4 | ESP32-S3 外部 FPC 天线接口 | 图 941fad0422cf / 第 1 页 / A2-A3 J4 IPEX_4 与 ESP32-S3 LNA_IN 匹配网络 |
| H1 | 24-pin BTB | DVP/GPIO、UART、I2C 与电源扩展连接器 | 图 941fad0422cf / 第 1 页 / B1-C1 BTB 区域 H1 1-24 脚 |
| J3/J5 | 2 x 9-pin castellated headers | 11 路 GPIO、唤醒 IO 与电源焊盘引出 | 图 941fad0422cf / 第 1 页 / D1 Hole 区域 J3/J5 1-9 脚 |
| LED1 | NeoPixel | 由 PY32_PMIC 控制供电与数据的 RGB LED | 图 941fad0422cf / 第 1 页 / B4-C4 LED1 NeoPixel、PY_LED_EN 与 NeoPixel 网络 |
| TVS3 | LXES15AAA1-153 | PWR_BTN 按键节点保护 | 图 941fad0422cf / 第 1 页 / B2-C2 KEY 区域按钮与 TVS3 LXES15AAA1-153 |

## 系统结构

### Stamp-S3Bat DIP 主控制器

U1 原理图器件值为 ESP32_S3_PICO_1，GPIO0-21、GPIO38-48、原生 USB GPIO19/20 和 LNA_IN 射频端均在页面中连接。

- 参数与网络：`reference=U1`；`part_number=ESP32_S3_PICO_1`；`native_usb=GPIO19 USB_D-,GPIO20 USB_D+`；`rf=LNA_IN`；`gpio=GPIO0-21,GPIO38-48`
- 证据：图 941fad0422cf / 第 1 页 / A3-D4 U1 ESP32_S3_PICO_1 全部 GPIO、USB、射频与电源引脚

## 电源

### LGS4056HDA 充电电路

U3 LGS4056HDA 的 VCC 接 SYS_VIN、BAT 接 VBAT，DONE/CHRG/PROG/CE 分别进入 PY_G2_CHG_STAT、PY_G3_CHG_PROG 周边电阻网络和 CHG_EN 控制，VBAT 由 C10 10 µF 去耦。

- 参数与网络：`charger=U3 LGS4056HDA`；`input=SYS_VIN`；`battery=VBAT`；`status=PY_G2_CHG_STAT`；`program_control=PY_G3_CHG_PROG`；`enable=CHG_EN`；`battery_capacitor=C10 10uF`
- 证据：图 941fad0422cf / 第 1 页 / A2 U3 LGS4056HDA、SYS_VIN/VBAT、PY_G2/PY_G3 与 CHG_EN

### 四路 CH213K 电源路径

U5 将 USB_VIN 送入 SYS_VIN，U7 将 5VIN 送入 SYS_VIN，U8 将 VBAT 送入 SYS_VBUS，U9 将 SYS_VIN 送入 SYS_VBUS；四路器件均标为 CH213K。

- 参数与网络：`u5=USB_VIN->SYS_VIN`；`u7=5VIN->SYS_VIN`；`u8=VBAT->SYS_VBUS`；`u9=SYS_VIN->SYS_VBUS`；`part_number=CH213K`
- 证据：图 941fad0422cf / 第 1 页 / A2-B2 四个 PowerPath 区域 U5/U7/U8/U9 与源/目标网络

### 3V3_L2 主控电源

U4 JW5712 以 SYS_VBUS 为 VIN，EN 接 3V3_L2_EN，SW 经 L4 FTC121065S2R2MBCA 生成 3V3_L2，C11/C12/C18 提供输出滤波。

- 参数与网络：`converter=U4 JW5712`；`input=SYS_VBUS`；`enable=3V3_L2_EN`；`inductor=L4 FTC121065S2R2MBCA`；`output=3V3_L2`；`output_capacitors=C11,C12,C18`
- 证据：图 941fad0422cf / 第 1 页 / B1-B2 DCDC 区域 U4、L4、SYS_VBUS、3V3_L2_EN 与 3V3_L2

### 3V3_L1 管理电源

U11 TPAP7343D-33FS4 以 SYS_VBUS 为 VIN，EN 接输入电源，OUT 输出 3V3_L1，输入与输出各配置 4.7 µF 电容。

- 参数与网络：`regulator=U11 TPAP7343D-33FS4`；`input=SYS_VBUS`；`output=3V3_L1`；`input_capacitor=4.7uF/6.3V`；`output_capacitor=4.7uF/6.3V`
- 证据：图 941fad0422cf / 第 1 页 / C2 U11、SYS_VBUS、3V3_L1 与两侧 4.7uF 电容

### EXT_5V_OUT 升压

U6 SY7088 以 SYS_VBUS 为输入，EN 由 5VOUT_EN 控制，经电感 FTC201610S2R2MBCA 和 R22 147 kΩ/R27 46.4 kΩ 反馈生成 EXT_5V_OUT。

- 参数与网络：`converter=U6 SY7088`；`input=SYS_VBUS`；`enable=5VOUT_EN`；`inductor=FTC201610S2R2MBCA`；`feedback=R22=147k,R27=46.4k`；`output=EXT_5V_OUT`
- 证据：图 941fad0422cf / 第 1 页 / D1-D2 U6 SY7088、反馈分压、5VOUT_EN 与 EXT_5V_OUT

## 接口

### USB Type-C 输入

J1 USB_C_16P_Horizontal 的 VBUS 输出 VUSBIN，A6/B6 并接 USB_DP，A7/B7 并接 USB_DM，CC1/CC2 分别经 R1/R2 5.1 kΩ 下拉至 GND；USB_DP/DM 分别由 TVS1/TVS2 ESDS311 保护。

- 参数与网络：`connector=J1 USB_C_16P_Horizontal`；`power=VUSBIN`；`d_plus=A6,B6 USB_DP`；`d_minus=A7,B7 USB_DM`；`cc_pulldowns=R1=5.1k,R2=5.1k`；`esd=TVS1,TVS2 ESDS311`
- 证据：图 941fad0422cf / 第 1 页 / A1 J1、R1/R2、TVS1/TVS2 与 USB_DP/DM

### ESP32-S3 原生 USB

USB_DM/USB_DP 经 R36/R35 两只 33 Ω 电阻和 FT1 SDMM0806H-2-900T 共模器件形成 G19/G20，并连接 U1 GPIO19/USB_D- 与 GPIO20/USB_D+。

- 参数与网络：`d_minus=USB_DM-R36 33R-FT1-G19/U1 USB_D-`；`d_plus=USB_DP-R35 33R-FT1-G20/U1 USB_D+`；`filter=FT1 SDMM0806H-2-900T`
- 证据：图 941fad0422cf / 第 1 页 / B3 USB_DM/DP、R35/R36、FT1 与 U1 GPIO19/20

### 24P BTB 接口

H1 的 1-24 脚依次为 G40、G46、G38、G45、G12、G41、G13、U0TX/G43、G14、G42、G15、G39、G16、GND、G18、G17、G21、U0RX/G44、3V3_L2、G47_SCL、SYS_VBUS、GND、SYS_VBUS、G48_SDA。

- 参数与网络：`pinout=1:G40,2:G46,3:G38,4:G45,5:G12,6:G41,7:G13,8:U0TX/G43,9:G14,10:G42,11:G15,12:G39,13:G16,14:GND,15:G18,16:G17,17:G21,18:U0RX/G44,19:3V3_L2,20:G47_SCL,21:SYS_VBUS,22:GND,23:SYS_VBUS,24:G48_SDA`
- 证据：图 941fad0422cf / 第 1 页 / B1-C1 BTB 区域 H1 1-24 脚网络

### DIP 两侧焊盘引出

J3 的 1-9 脚为 G1、G2、G3、G4、G5、GND、EXT_5V_OUT、G6、G7；J5 的 1-9 脚为 5VIN、3V3_L2、VBAT、G8、G9、G10、G11、PY_G4_WAKE、GND。

- 参数与网络：`j3=1:G1,2:G2,3:G3,4:G4,5:G5,6:GND,7:EXT_5V_OUT,8:G6,9:G7`；`j5=1:5VIN,2:3V3_L2,3:VBAT,4:G8,5:G9,6:G10,7:G11,8:PY_G4_WAKE,9:GND`；`gpio_count=11`；`wake_io=PY_G4_WAKE`
- 证据：图 941fad0422cf / 第 1 页 / D1 Hole 区域 J3/J5 全部引脚

### PWR_BTN 按键

按键将 PWR_BTN 接地，TVS3 LXES15AAA1-153 跨接按键节点与 GND；PWR_BTN 同时连接 U2 BTN_PU。

- 参数与网络：`signal=PWR_BTN`；`action=switch to GND`；`protection=TVS3 LXES15AAA1-153`；`controller=U2 BTN_PU`
- 证据：图 941fad0422cf / 第 1 页 / B2-C2 KEY 区域按钮、PWR_BTN、TVS3 与 U2 BTN_PU

## GPIO 与控制信号

### PY32_PMIC 控制映射

U2 以 G47_SCL/G48_SDA 接 I2C，输出 3V3_L2_EN、CHG_EN、BAT_ADC_EN、5VOUT_EN、PY_LED_EN 与 G0_BOOT_OUT，并采集 VUSB_ADC、5VIN_ADC、BAT_ADC、PY_G2_CHG_STAT、PY_G3_CHG_PROG、PY_G4_WAKE 和 PWR_BTN。

- 参数与网络：`i2c=G47_SCL,G48_SDA`；`outputs=3V3_L2_EN,CHG_EN,BAT_ADC_EN,5VOUT_EN,PY_LED_EN,G0_BOOT_OUT`；`inputs=VUSB_ADC,5VIN_ADC,BAT_ADC,PY_G2_CHG_STAT,PY_G3_CHG_PROG,PY_G4_WAKE,PWR_BTN`；`reference=U2 PY32_PMIC`
- 证据：图 941fad0422cf / 第 1 页 / C3-D4 U2 PY32_PMIC 全部 I2C、控制、ADC、唤醒与按键网络

### NeoPixel RGB LED

LED1 NeoPixel 的 VDD 接 PY_LED_EN、DIN 接 NeoPixel 数据网络，二者分别连接 U2 LED_EN_PP 与 G0_WAKEin/IRQout_NEOPIXEL。

- 参数与网络：`reference=LED1`；`power=PY_LED_EN from U2 LED_EN_PP`；`data=NeoPixel from U2 G0_WAKEin/IRQout_NEOPIXEL`；`output=DOUT unconnected`
- 证据：图 941fad0422cf / 第 1 页 / B4-C4 LED1 与 U2 的 PY_LED_EN/NeoPixel 网络

## 复位

### SOC_RESET 网络

U1 CHIP_PU 接 SOC_RESET，SOC_RESET 由 R12 100 kΩ 上拉至 3V3_L2、C1 1 µF 对地。

- 参数与网络：`signal=SOC_RESET`；`destination=U1 CHIP_PU`；`pullup=R12 100k to 3V3_L2`；`capacitor=C1 1uF`
- 证据：图 941fad0422cf / 第 1 页 / B3 SOC_RESET、R12/C1 与 U1 CHIP_PU

### GPIO0 Boot 控制

U1 GPIO0(strap) 接 G0_BOOT_OUT，G0_BOOT_OUT 同时引至 JP1 pin4、TP2 和 U2 BOOT_OUT_OD。

- 参数与网络：`gpio=U1 GPIO0`；`signal=G0_BOOT_OUT`；`connector=JP1 pin4`；`testpoint=TP2`；`controller=U2 BOOT_OUT_OD`
- 证据：图 941fad0422cf / 第 1 页 / B3-C4 G0_BOOT_OUT 在 U1 GPIO0、JP1、TP2 与 U2 pin15 间连接

## 保护电路

### USB 输入过压保护

U12 AW32901FCR 的三路 IN 接 VUSBIN、三路 OUT 输出 USB_VIN，输入端 C17 1 µF、输出端 C25 1 µF 去耦。

- 参数与网络：`reference=U12`；`part_number=AW32901FCR`；`input=VUSBIN`；`output=USB_VIN`；`capacitors=C17=1uF,C25=1uF`
- 证据：图 941fad0422cf / 第 1 页 / A1-B1 U12 AW32901FCR、VUSBIN/USB_VIN 与 C17/C25

## 射频

### IPEX-4 外部天线匹配

J4 IPEX_4 通过 C12 GRM0335C1H1R5BA01D、L1 LQP03TN3N3B02D、L2 LQP03TN1N5B02D 与 C20/C24 匹配位连接 U1 LNA_IN；图面注记天线端和芯片端各放置一组匹配。

- 参数与网络：`connector=J4 IPEX_4`；`series_capacitor=C12 GRM0335C1H1R5BA01D`；`shunt_inductor=L1 LQP03TN3N3B02D`；`series_inductor=L2 LQP03TN1N5B02D`；`matching_caps=C20,C24`；`destination=U1 LNA_IN`
- 证据：图 941fad0422cf / 第 1 页 / A2-A4 J4、C12/L1/L2/C20/C24 与 U1 LNA_IN

## 调试与烧录

### 控制与电源测试点

TP1=PY_LED_EN、TP3=BAT_ADC_EN、TP2=G0_BOOT_OUT、TP5=U0RX/G44、TP6=U0TX/G43、TP7=SYS_VBUS、TP8=SYS_VIN。

- 参数与网络：`mapping=TP1:PY_LED_EN,TP2:G0_BOOT_OUT,TP3:BAT_ADC_EN,TP5:U0RX/G44,TP6:U0TX/G43,TP7:SYS_VBUS,TP8:SYS_VIN`
- 证据：图 941fad0422cf / 第 1 页 / B3-C3 TP1/TP2/TP3/TP5/TP6/TP7/TP8 网络标签

## 模拟电路

### VBAT、5VIN 与 USB 电压检测

VBAT_ADC 通过 Q1/Q2 与 BAT_ADC_EN 受控接入 BAT_ADC 分压滤波；5VIN 经 R19/R20 分压和 C31 滤波形成 5VIN_ADC，USB_VIN 经 R5/R6 分压和 C5 滤波形成 VUSB_ADC。

- 参数与网络：`battery=VBAT_ADC gated by Q1/Q2 and BAT_ADC_EN to BAT_ADC`；`five_volt=R19/R20 divider,C31 filter to 5VIN_ADC`；`usb=R5/R6 divider,C5 filter to VUSB_ADC`
- 证据：图 941fad0422cf / 第 1 页 / C2-D3 Q1/Q2 BAT_ADC 与 5VIN_ADC/VUSB_ADC 分压滤波网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 接口 | USB Type-C 输入 | `connector=J1 USB_C_16P_Horizontal`；`power=VUSBIN`；`d_plus=A6,B6 USB_DP`；`d_minus=A7,B7 USB_DM`；`cc_pulldowns=R1=5.1k,R2=5.1k`；`esd=TVS1,TVS2 ESDS311` |
| 保护电路 | USB 输入过压保护 | `reference=U12`；`part_number=AW32901FCR`；`input=VUSBIN`；`output=USB_VIN`；`capacitors=C17=1uF,C25=1uF` |
| 电源 | LGS4056HDA 充电电路 | `charger=U3 LGS4056HDA`；`input=SYS_VIN`；`battery=VBAT`；`status=PY_G2_CHG_STAT`；`program_control=PY_G3_CHG_PROG`；`enable=CHG_EN`；`battery_capacitor=C10 10uF` |
| 电源 | 四路 CH213K 电源路径 | `u5=USB_VIN->SYS_VIN`；`u7=5VIN->SYS_VIN`；`u8=VBAT->SYS_VBUS`；`u9=SYS_VIN->SYS_VBUS`；`part_number=CH213K` |
| 电源 | 3V3_L2 主控电源 | `converter=U4 JW5712`；`input=SYS_VBUS`；`enable=3V3_L2_EN`；`inductor=L4 FTC121065S2R2MBCA`；`output=3V3_L2`；`output_capacitors=C11,C12,C18` |
| 电源 | 3V3_L1 管理电源 | `regulator=U11 TPAP7343D-33FS4`；`input=SYS_VBUS`；`output=3V3_L1`；`input_capacitor=4.7uF/6.3V`；`output_capacitor=4.7uF/6.3V` |
| 电源 | EXT_5V_OUT 升压 | `converter=U6 SY7088`；`input=SYS_VBUS`；`enable=5VOUT_EN`；`inductor=FTC201610S2R2MBCA`；`feedback=R22=147k,R27=46.4k`；`output=EXT_5V_OUT` |
| 系统结构 | Stamp-S3Bat DIP 主控制器 | `reference=U1`；`part_number=ESP32_S3_PICO_1`；`native_usb=GPIO19 USB_D-,GPIO20 USB_D+`；`rf=LNA_IN`；`gpio=GPIO0-21,GPIO38-48` |
| 接口 | ESP32-S3 原生 USB | `d_minus=USB_DM-R36 33R-FT1-G19/U1 USB_D-`；`d_plus=USB_DP-R35 33R-FT1-G20/U1 USB_D+`；`filter=FT1 SDMM0806H-2-900T` |
| 射频 | IPEX-4 外部天线匹配 | `connector=J4 IPEX_4`；`series_capacitor=C12 GRM0335C1H1R5BA01D`；`shunt_inductor=L1 LQP03TN3N3B02D`；`series_inductor=L2 LQP03TN1N5B02D`；`matching_caps=C20,C24`；`destination=U1 LNA_IN` |
| 复位 | SOC_RESET 网络 | `signal=SOC_RESET`；`destination=U1 CHIP_PU`；`pullup=R12 100k to 3V3_L2`；`capacitor=C1 1uF` |
| 复位 | GPIO0 Boot 控制 | `gpio=U1 GPIO0`；`signal=G0_BOOT_OUT`；`connector=JP1 pin4`；`testpoint=TP2`；`controller=U2 BOOT_OUT_OD` |
| 接口 | 24P BTB 接口 | `pinout=1:G40,2:G46,3:G38,4:G45,5:G12,6:G41,7:G13,8:U0TX/G43,9:G14,10:G42,11:G15,12:G39,13:G16,14:GND,15:G18,16:G17,17:G21,18:U0RX/G44,19:3V3_L2,20:G47_SCL,21:SYS_VBUS,22:GND,23:SYS_VBUS,24:G48_SDA` |
| 接口 | DIP 两侧焊盘引出 | `j3=1:G1,2:G2,3:G3,4:G4,5:G5,6:GND,7:EXT_5V_OUT,8:G6,9:G7`；`j5=1:5VIN,2:3V3_L2,3:VBAT,4:G8,5:G9,6:G10,7:G11,8:PY_G4_WAKE,9:GND`；`gpio_count=11`；`wake_io=PY_G4_WAKE` |
| 接口 | PWR_BTN 按键 | `signal=PWR_BTN`；`action=switch to GND`；`protection=TVS3 LXES15AAA1-153`；`controller=U2 BTN_PU` |
| GPIO 与控制信号 | PY32_PMIC 控制映射 | `i2c=G47_SCL,G48_SDA`；`outputs=3V3_L2_EN,CHG_EN,BAT_ADC_EN,5VOUT_EN,PY_LED_EN,G0_BOOT_OUT`；`inputs=VUSB_ADC,5VIN_ADC,BAT_ADC,PY_G2_CHG_STAT,PY_G3_CHG_PROG,PY_G4_WAKE,PWR_BTN`；`reference=U2 PY32_PMIC` |
| 模拟电路 | VBAT、5VIN 与 USB 电压检测 | `battery=VBAT_ADC gated by Q1/Q2 and BAT_ADC_EN to BAT_ADC`；`five_volt=R19/R20 divider,C31 filter to 5VIN_ADC`；`usb=R5/R6 divider,C5 filter to VUSB_ADC` |
| GPIO 与控制信号 | NeoPixel RGB LED | `reference=LED1`；`power=PY_LED_EN from U2 LED_EN_PP`；`data=NeoPixel from U2 G0_WAKEin/IRQout_NEOPIXEL`；`output=DOUT unconnected` |
| 调试与烧录 | 控制与电源测试点 | `mapping=TP1:PY_LED_EN,TP2:G0_BOOT_OUT,TP3:BAT_ADC_EN,TP5:U0RX/G44,TP6:U0TX/G43,TP7:SYS_VBUS,TP8:SYS_VIN` |
| 核心器件 | M5PM1 电源管理器身份与地址 | `source_primary_name=M5PM1`；`source_typo_or_alias=M5MP1`；`schematic_value=PY32_PMIC`；`source_i2c_address=0x6E` |
| 存储 | ESP32-S3-PICO N8R8 容量 | `source_document=ESP32-S3-PICO-1-N8R8`；`source_flash=8MB`；`source_psram=8MB`；`schematic_value=ESP32_S3_PICO_1` |
| 电源 | 充电电流两档控制 | `source_low=650mA`；`source_floating=200mA`；`control=PY_G3_CHG_PROG`；`drawing_resistors=R3,R14` |
| 接口 | BTB 连接器具体料号 | `source_document=BTB0.408-24PLBDR-M41`；`pitch_mm=0.4`；`pins=24`；`schematic_reference=H1` |
| 接口 | DIP 排针装配状态 | `source_document_dip=2.54mm headers soldered by default`；`schematic=J3/J5 9-pin electrical interfaces`；`header_part_number=not specified` |
| 电源 | 电池工作电流指标 | `sleep=4.2V@13.43uA`；`standby=4.2V@955.36uA`；`light_load=4.2V@26.83mA`；`full_load=4.2V@27.49mA`；`test_conditions=not specified` |

## 待确认事项

- `component.pmic-identity`：源文档主体称 M5PM1、描述首段出现 M5MP1，原理图 U2 器件值为 PY32_PMIC；源文档给出 I2C 地址 0x6E，但原理图页面未标该地址，需确认三种名称的对应关系和正式料号。（证据：图 941fad0422cf / 第 1 页 / C3-D4 U2 仅标 PY32_PMIC，I2C 网络为 G47_SCL/G48_SDA，未标地址）
- `storage.pico-variant`：源文档标注 ESP32-S3-PICO-1-N8R8、8MB Flash 和 8MB PSRAM，原理图 U1 只标 ESP32_S3_PICO_1，未显示 N8R8 后缀或外部存储器；当前封装容量需由 BOM 或器件标识确认。（证据：图 941fad0422cf / 第 1 页 / A3-D4 U1 仅标 ESP32_S3_PICO_1，页面无外部 Flash/PSRAM）
- `power.charge-current-modes`：源文档说明 PY_G3_CHG_PROG 低电平选择 650mA、浮空选择 200mA；原理图显示 PY_G3_CHG_PROG 与 U3 PROG 周边 R3/R14 网络，但未直接标两档电流，需结合 LGS4056HDA 规格确认。（证据：图 941fad0422cf / 第 1 页 / A2 U3 PROG、PY_G3_CHG_PROG 与 R3/R14 周边网络）
- `interface.btb-part-number`：源文档标注 BTB0.408-24PLBDR-M41、0.4mm 间距 24P，原理图 H1 只给出 24 针电气符号和网络，没有连接器料号与装配方向。（证据：图 941fad0422cf / 第 1 页 / B1-C1 H1 24 针 BTB 符号未标料号或方向）
- `interface.dip-header-assembly`：Stamp-S3Bat DIP 源文档说明默认焊接 2.54mm 标准间距排针，原理图只显示 J3/J5 九针电气符号，没有排针料号、针长或装配属性；DIP 与裸 Stamp-S3Bat 的装配差异需由 BOM 或实物确认。（证据：图 941fad0422cf / 第 1 页 / D1 J3/J5 电气符号无排针料号或装配属性）
- `power.operating-current`：源文档给出 4.2V 下休眠 13.43µA、待机 955.36µA、轻载 26.83mA、满载 27.49mA；原理图显示多级电源路径、PMIC、ADC 与 LED，但没有测试固件、射频状态、负载或温度条件，无法从图面复核。（证据：图 941fad0422cf / 第 1 页 / A1-D4 多源 PowerPath、3V3_L1/L2、5VOUT、PMIC、ADC 与 LED 电路）
- `review.pmic-identity`：M5PM1、M5MP1 与原理图 PY32_PMIC 是否指同一器件，正式料号和 0x6E 地址如何确认？；原因：源文档名称不一致，原理图也未标 M5PM1 或 I2C 地址。
- `review.pico-variant`：S015-DIP 实装是否确认为 ESP32-S3-PICO-1-N8R8，Flash 和 PSRAM 是否各为 8MB？；原因：原理图未显示 N8R8 后缀或外部存储器。
- `review.charge-current-modes`：PY_G3_CHG_PROG 的 650mA/200mA 两档电流如何由 R3/R14 和 LGS4056HDA PROG 规格计算？；原因：图面未直接标两档电流。
- `review.btb-part-number`：H1 是否实装 BTB0.408-24PLBDR-M41，连接器方向与 Pin 1 标识是什么？；原因：原理图只给出 24 针网络，未标料号和装配方向。
- `review.dip-header-assembly`：Stamp-S3Bat DIP 默认焊接排针的具体料号、针长和装配方向是什么？；原因：源文档确认 DIP 焊接排针，原理图只显示 J3/J5 电气符号。
- `review.operating-current`：四档 4.2V 功耗指标的固件、射频、外设、LED、负载与温度条件是什么？；原因：性能测试边界未出现在原理图。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `941fad0422cfd8c2d78b20c7ce9a11036dd887596524ce8c3577f7dc2796e0e7` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1222/S015-SCH_Stamp-S3BAT_page_01.png` |

---

源文档：`zh_CN/core/Stamp-S3Bat_DIP.md`

源文档 SHA-256：`0f782efc919fedcd49c5153f29ddc24e3b5f56971d68231a8adf097ff840329a`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
