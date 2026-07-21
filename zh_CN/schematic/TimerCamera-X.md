# TimerCamera-X 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | TimerCamera-X |
| SKU | U082-X |
| 产品 ID | `timercamera-x-eba094edbdc4` |
| 源文档 | `zh_CN/unit/timercam_x.md` |

## 概述

TimerCamera-X 主控页以 U1 ESP32 连接 U2 OV-Camera、U3 ESPPSRAM64H、U4 W25Q32、40MHz 晶体、双天线选择网络、蓝色 LED 和 HY2.0-4P 接口。电源/控制页使用 U5 SY8089AAC 将 VSYS_VIN 转为 VCC_3V3，U8/U9 分别生成 1.5V/2.8V 相机电源，U11 TP4057 从 USB-C VBUS 为 VBAT_IN 充电。U6 BM8563 通过 GPIO14/GPIO12 连接 RTC 总线并以 RTC_ALM 参与 PMOS/NMOS 电源保持与唤醒；CH552T（U7）桥接 USB D+/D- 与 ESP32 UART，并控制 GPIO0/EN 下载时序。电池和 USB 经 D6/D8 肖特基二极管汇合到 VSYS_VIN，GPIO38 采样 VBAT，GPIO33 参与 PWR_EN 保持。

## 检索关键词

`TimerCamera-X`、`U082-X`、`ESP32`、`ESP32-D0WDQ6-V3`、`OV-Camera`、`OV3660`、`ESPPSRAM64H`、`W25Q32`、`BM8563`、`CH552T`、`TP4057`、`SY8089AAC`、`HX6306P152`、`HX6306P282`、`GPIO13`、`GPIO4`、`GPIO14`、`GPIO12`、`GPIO38`、`GPIO33`、`GPIO2`、`PWR_EN`、`RTC_ALM`、`VBAT_IN`、`VSYS_VIN`、`VUSB_VCC`、`VCC_3V3`、`VCC_1V5`、`VCC_2V8`、`VDD_SDIO`、`USB_DP`、`USB_DM`、`U0TXD`、`U0RXD`、`IPEX`、`PROANT_440`、`40MHz`、`HY2.0-4P`、`SK6812`、`140mAh`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32 | 相机主控，连接相机并口、外部存储、RTC、Grove、USB-UART、电源保持与状态 LED | 图 d59e37772926 / 第 1 页 / A1-C2：U1 ESP32 的 GPIO、晶振、SDIO、电源与 GND 引脚 |
| U2 | OV-Camera | 24 Pin 摄像头模组接口，连接 8 位像素数据、同步、时钟、SCCB 和三路电源 | 图 d59e37772926 / 第 1 页 / A4-C4：U2 OV-Camera，Y0~Y9/PCLK/XCLK/HREF/VSYNC/RESET/SIO_C/SIO_D 与电源脚 |
| U3 | ESPPSRAM64H | 连接 ESP32 SDIO 总线的外部 PSRAM | 图 d59e37772926 / 第 1 页 / C2-C3：U3 ESPPSRAM64H，nCS/SI/SO/SIO2/SIO3/SCLK/VDD/VSS |
| U4 | W25Q32 | 连接 ESP32 SDIO 总线的外部串行 Flash | 图 d59e37772926 / 第 1 页 / D2-D3：U4 W25Q32，nCS/CLK/DI/DO/WP/HOLD/VCC/GND 与 SDIO 网络 |
| ANT1 | PROANT_440 | ESP_LNA 射频路径的板载天线 | 图 d59e37772926 / 第 1 页 / A2-A3：ANT1 PROANT_440 经 R2 0R 和 TBD 匹配网络连接 ESP_LNA |
| J1 | IPEX | 可选外部射频天线座，路径由 R3 DNP 控制 | 图 d59e37772926 / 第 1 页 / A3-B3：J1 IPEX，信号端经 R3 DNP 接 ESP_LNA 匹配节点，外壳接 GND |
| X1 | TXC/8Z40000017 | ESP32 40MHz 主晶体及负载网络 | 图 d59e37772926 / 第 1 页 / C1-C2：X1 TXC/8Z40000017 连接 ESP_XTAL_N/P，R35 100R、C17/C18 12pF |
| LED1 | XBLUE | GPIO2 控制的蓝色状态 LED | 图 d59e37772926 / 第 1 页 / A4：GPIO2-LED1 XBLUE-R31 470R-GND 支路 |
| J2 | PH2.0_4P_SMT | GPIO13/GPIO4、VSYS_VIN、GND 的 HY2.0-4P 扩展接口 | 图 d59e37772926 / 第 1 页 / C3-D4：J2 PH2.0_4P_SMT 四脚与 R7/R8、D1/D2、GPIO13/GPIO4/VSYS_VIN/GND |
| U5 | SY8089AAC | 将 VSYS_VIN 降压生成 VCC_3V3 | 图 6f41535b5573 / 第 1 页 / A1-A2：U5 SY8089AAC、L2、R14/R15、C24/C25 的 VSYS_VIN 到 VCC_3V3 电路 |
| U6 | BM8563 | VBAT_IN 供电的 RTC，通过 GPIO14/GPIO12 通信并输出 RTC_ALM | 图 6f41535b5573 / 第 1 页 / A3-A4：U6 BM8563，OSCI/OSCO/INT/SCL/SDA/VDD/VSS 与 Y1、RTC_ALM、GPIO14/GPIO12、VBAT_IN |
| U7 | CH552T | USB D+/D- 到 ESP32 UART 的下载桥，并配合 FET1/FET2 控制 GPIO0/EN | 图 6f41535b5573 / 第 1 页 / A2-B3：U7 CH552T 的 USB_DP/DM、CH552_TXD/RXD、GPIO0_IN/ESP32_EN_IN 与电源 |
| J3 | USB-TYPEC | USB VBUS、电源与 D+/D- 接口，CC1/CC2 各 5.1KΩ 下拉 | 图 6f41535b5573 / 第 1 页 / B3：J3 USB-TYPEC，VCC/DP/DM/CC1/CC2/GND 与 R22/R23 |
| U8 | HX6306P152/1.5V LDO 300mA | 由 VCC_3V3 生成 VCC_1V5 相机电源 | 图 6f41535b5573 / 第 1 页 / C3-C4：U8 HX6306P152/1.5V LDO 300mA 与 C33/C34/C41 |
| U9 | HX6306P282/2.8V LDO 300mA | 由 VCC_3V3 生成 VCC_2V8 相机电源 | 图 6f41535b5573 / 第 1 页 / D3-D4：U9 HX6306P282/2.8V LDO 300mA 与 C37/C38/C42 |
| U11 | TP4057 | 从 VUSB_VCC 为 VBAT_IN 充电的单节电池充电器 | 图 6f41535b5573 / 第 1 页 / D2-D3：U11 TP4057，VCC/BAT/PROG/CHRG/STDBY/GND 与 VUSB_VCC/VBAT_IN/R30 |
| J4 | SMT_HDR_2x1.25mm | VBAT_IN 与 GND 电池接口 | 图 6f41535b5573 / 第 1 页 / B2-C3：J4 SMT_HDR_2x1.25mm，pin2 VBAT_IN、pin1 GND |
| FET3, FET4 | CJ2301/PMOS / CJ2302-NMOS | RTC/按键/GPIO33 控制的 VBAT 电源保持开关 | 图 6f41535b5573 / 第 1 页 / B1-C2：FET3/FET4、PWR_EN、GPIO33、RTC_ALM、USER_SWC、D3/D4/D5、R24~R26 |
| U10 | 未标注 | DNP 复位监控器位，RESET 接 ESP32_EN；实际按键 S2 也可拉低 ESP32_EN | 图 6f41535b5573 / 第 1 页 / D1-D2：U10 VCC/RESET/GND 符号及 C39 DNP、R27、S2、D9，U10 无型号 |

## 系统结构

### TimerCamera-X

U1 ESP32 连接相机 U2、PSRAM U3、Flash U4、天线、Grove 和 LED；第二页由 BM8563、CH552T、TP4057、SY8089AAC、双 LDO 与电源保持电路提供 RTC 唤醒、USB 下载、充电和多路供电。

- 参数与网络：`controller=U1 ESP32`；`camera=U2 OV-Camera`；`psram=U3 ESPPSRAM64H`；`flash=U4 W25Q32`；`rtc=U6 BM8563`；`usb_bridge=U7 CH552T`；`charger=U11 TP4057`；`main_regulator=U5 SY8089AAC`
- 证据：图 d59e37772926 / 第 1 页 / 主控页全部功能区; 图 6f41535b5573 / 第 1 页 / 电源/RTC/USB 页全部功能区

## 电源

### U2 相机电源

U2.DOVDD.11 接 VCC_3V3、DVDD.10 接 VCC_1V5、AVDD.4 接 VCC_2V8，AGND.2 与 DGND.15 接 GND；PWDN.8 经 R4 10K 接 GND。

- 参数与网络：`DOVDD=pin11 VCC_3V3`；`DVDD=pin10 VCC_1V5`；`AVDD=pin4 VCC_2V8`；`AGND=pin2 GND`；`DGND=pin15 GND`；`PWDN=pin8 via R4 10K to GND`
- 证据：图 d59e37772926 / 第 1 页 / B4-C4：U2 DOVDD/DVDD/AVDD/AGND/DGND/PWDN 与对应电源和 R4

### U5 SY8089AAC

VSYS_VIN 接 U5.IN.4 与 EN.1，LX.3 经 L2（WPN3012H2R2MT）输出 VCC_3V3；R14 11.5K/1% 与 R15 2.55K/1% 连接 FB.5，C24/C25 均为 22uF/6.3V。

- 参数与网络：`input=VSYS_VIN`；`output=VCC_3V3`；`inductor=L2 WPN3012H2R2MT`；`feedback=R14 11.5K/1%, R15 2.55K/1%`；`output_caps=C24/C25 22uF/6.3V`
- 证据：图 6f41535b5573 / 第 1 页 / A1-A2：U5/L2/R14/R15/C24/C25 与 VSYS_VIN/VCC_3V3

### U8/U9

U8 从 VCC_3V3 生成 VCC_1V5，U9 从 VCC_3V3 生成 VCC_2V8；两者均标 LDO 300mA 并带输入/输出电容。

- 参数与网络：`U8=HX6306P152 / 1.5V LDO 300mA -> VCC_1V5`；`U9=HX6306P282 / 2.8V LDO 300mA -> VCC_2V8`；`U8_caps=C33 4.7uF, C34 4.7uF, C41 22uF`；`U9_caps=C37 4.7uF, C38 4.7uF, C42 22uF`
- 证据：图 6f41535b5573 / 第 1 页 / C3-D4：U8/U9 与 VCC_3V3/VCC_1V5/VCC_2V8 和电容

### U11 TP4057

VUSB_VCC 接 U11.VCC.4，BAT.3 输出 VBAT_IN，PROG.6 经 R30 5.1K 接 GND；C36 4.7uF 位于输入端，C40 10uF 位于 VBAT_IN，CHRG/STDBY 未连接。

- 参数与网络：`input=VUSB_VCC`；`charger=U11 TP4057`；`battery_net=VBAT_IN`；`program_resistor=R30 5.1K`；`input_cap=C36 4.7uF`；`battery_cap=C40 10uF`；`status_pins=CHRG/STDBY NC`
- 证据：图 6f41535b5573 / 第 1 页 / D2-D3：U11/R30/C36/C40 与 VUSB_VCC/VBAT_IN/GND

### VSYS_VIN

VBAT 经 D6（1N5819）连接 VSYS_VIN，VUSB_VCC 经 D8（1N5819）连接同一 VSYS_VIN；C43/C44 均为 10uF/6.3V 对地。

- 参数与网络：`battery_path=VBAT -> D6 1N5819 -> VSYS_VIN`；`usb_path=VUSB_VCC -> D8 1N5819 -> VSYS_VIN`；`decoupling=C43/C44 10uF/6.3V`
- 证据：图 6f41535b5573 / 第 1 页 / C2-D3：D6/D8、VBAT/VUSB_VCC/VSYS_VIN、C43/C44

### PWR_EN 电源保持

FET3（CJ2301/PMOS）控制 VBAT_IN 到 VBAT；其门极 PWR_EN 由 RTC_ALM 经 D3、USER_SWC 经 D5 汇入，并由 FET4（CJ2302-NMOS）受 GPIO33 控制，S1 将 USER_SWC 拉地。

- 参数与网络：`high_side=FET3 CJ2301/PMOS VBAT_IN -> VBAT`；`hold_gate=PWR_EN`；`rtc_wake=RTC_ALM via D3 1N4148`；`button_wake=USER_SWC/S1 via D5 1N4148`；`mcu_hold=GPIO33 -> FET4 CJ2302-NMOS`；`bias=R24/R25/R26 100K`
- 证据：图 6f41535b5573 / 第 1 页 / B1-C2：VBAT_IN/FET3/PWR_EN/FET4/GPIO33/RTC_ALM/USER_SWC/S1/D3-D5/R24-R26

## 接口

### J2 PH2.0_4P_SMT

J2.1 经 R7 22R 接 GPIO13，J2.2 经 R8 22R 接 GPIO4，J2.3 接 VSYS_VIN，J2.4 接 GND；D1/D2 为两条信号的 3.3V ESD 保护。

- 参数与网络：`pin_1=GPIO13 via R7 22R`；`pin_2=GPIO4 via R8 22R`；`pin_3=VSYS_VIN`；`pin_4=GND`；`protection=D1/D2 3.3V/ESD`
- 证据：图 d59e37772926 / 第 1 页 / C3-D4：J2、R7/R8、D1/D2 与 GPIO13/GPIO4/VSYS_VIN/GND

### J3 USB-TYPEC

J3.A6/B6 连接 USB_DP，A7/B7 连接 USB_DM，VCC 接 VUSB_VCC，CC1/CC2 分别经 R22/R23（5.1K）接 GND，外壳与地脚接 GND。

- 参数与网络：`VBUS=VUSB_VCC`；`DP=A6/B6 USB_DP`；`DM=A7/B7 USB_DM`；`CC1=R22 5.1K to GND`；`CC2=R23 5.1K to GND`
- 证据：图 6f41535b5573 / 第 1 页 / B3：J3 USB-TYPEC 与 R22/R23、VUSB_VCC、USB_DP/DM、GND

### J4

J4.2 接 VBAT_IN，J4.1 接 GND。

- 参数与网络：`connector=SMT_HDR_2x1.25mm`；`pin_1=GND`；`pin_2=VBAT_IN`
- 证据：图 6f41535b5573 / 第 1 页 / B2-C3：J4 两脚与 VBAT_IN/GND

## 总线

### U2 摄像头像素数据

U2.Y2.19、Y1.23、Y0.24、Y3.21、Y4.22、Y5.20、Y6.18、Y7.16 分别连接 GPIO32、GPIO35、GPIO34、GPIO5、GPIO39、GPIO18、GPIO36、GPIO19。

- 参数与网络：`D0_Y2=GPIO32`；`D1_Y1=GPIO35`；`D2_Y0=GPIO34`；`D3_Y3=GPIO5`；`D4_Y4=GPIO39`；`D5_Y5=GPIO18`；`D6_Y6=GPIO36`；`D7_Y7=GPIO19`
- 证据：图 d59e37772926 / 第 1 页 / A4-B4：U2 Y0~Y7 与 GPIO34/35/39/5/18/32/36/19 网络

### U1 与 U6 BM8563

U6.SCL.6 接 GPIO14，SDA.5 接 GPIO12，INT.3 输出 RTC_ALM；U6.VDD.8 接 VBAT_IN、VSS.4 接 GND。

- 参数与网络：`SCL=GPIO14`；`SDA=GPIO12`；`alarm=RTC_ALM`；`supply=VBAT_IN`；`ground=GND`
- 证据：图 6f41535b5573 / 第 1 页 / A3-A4：U6 SCL/SDA/INT/VDD/VSS 与 GPIO14/GPIO12/RTC_ALM/VBAT_IN/GND

## GPIO 与控制信号

### U2 相机控制与同步

PCLK.17 经 R36 47R 接 GPIO21，XCLK.13 经 R37 47R 接 GPIO27，HREF.9 接 GPIO26，VSYNC.7 接 GPIO22，RESET.6 接 GPIO15，SIO_C.5 接 GPIO23，SIO_D.3 接 GPIO25。

- 参数与网络：`PCLK=GPIO21 via R36 47R`；`XCLK=GPIO27 via R37 47R`；`HREF=GPIO26`；`VSYNC=GPIO22`；`RESET=GPIO15`；`SIO_C=GPIO23`；`SIO_D=GPIO25`
- 证据：图 d59e37772926 / 第 1 页 / B3-C4：U2 PCLK/XCLK/HREF/VSYNC/RESET/SIO_C/SIO_D 与 R36/R37/GPIO 网络

### LED1

GPIO2 连接 LED1（XBLUE），LED1 经 R31（470R）接 GND。

- 参数与网络：`gpio=GPIO2`；`led=LED1 XBLUE`；`resistor=R31 470R to GND`
- 证据：图 d59e37772926 / 第 1 页 / A4：GPIO2-LED1-R31-GND

## 时钟

### U1 ESP32

U1.XTAL_N.44 与 XTAL_P.45 连接 X1；R35 100R 串接 XTAL_P，C17/C18 均为 12pF 对地。

- 参数与网络：`crystal=X1 TXC/8Z40000017`；`XTAL_N=U1.44`；`XTAL_P=U1.45 via R35 100R`；`load_caps=C17 12pF, C18 12pF`
- 证据：图 d59e37772926 / 第 1 页 / B1-C2：U1 ESP_XTAL_N/P 与 X1/R35/C17/C18

### U6 BM8563

U6.OSCI.1 与 OSCO.2 连接 Y1（TCX/QH0320），C23/C28 均为 7pF 对地；CLKOUT.7 未连接。

- 参数与网络：`rtc=U6 BM8563`；`crystal=Y1 TCX/QH0320`；`load_caps=C23/C28 7pF`；`clkout=pin7 NC`
- 证据：图 6f41535b5573 / 第 1 页 / A3-A4：U6 OSCI/OSCO、Y1、C23/C28 与 CLKOUT 未连接

## 复位

### ESP32_EN / S2

ESP32_EN 由 R27（10K）上拉至 VCC_3V3，S2 按下时接 GND，D9 提供 3.3V ESD 保护；U10/C39 标 DNP。

- 参数与网络：`reset_net=ESP32_EN`；`pullup=R27 10K`；`button=S2 SMT_SW_PTS_820 to GND`；`protection=D9 3.3V/ESD`；`monitor_footprint=U10/C39 DNP`
- 证据：图 6f41535b5573 / 第 1 页 / D1-D2：U10/C39/R27/S2/D9 与 ESP32_EN

## 保护电路

### J2 与复位接口

J2 的 GPIO13/GPIO4 分别由 D1/D2（3.3V/ESD）钳位到 GND，ESP32_EN 由 D9（3.3V/ESD）钳位；USB-C VBUS 路径未显示保险丝或独立 TVS。

- 参数与网络：`grove_gpio13=D1 3.3V/ESD`；`grove_gpio4=D2 3.3V/ESD`；`reset=D9 3.3V/ESD`；`usb_fuse=none shown`；`usb_tvs=none shown`
- 证据：图 d59e37772926 / 第 1 页 / C3-D4：J2/D1/D2; 图 6f41535b5573 / 第 1 页 / D1-D2：D9/ESP32_EN；B3 J3 USB-C 电源路径

## 存储

### U4 W25Q32

U4.nCS 接 SD_CMD 并由 R9 10K 上拉至 VDD_SDIO，CLK 经 R10 200R 接 SD_CLK，DI/DO/WP/HOLD 接 SD_DATA1/0/3/2。

- 参数与网络：`nCS=SD_CMD, R9 10K to VDD_SDIO`；`CLK=SD_CLK via R10 200R`；`DI=SD_DATA1`；`DO=SD_DATA0`；`nWP=SD_DATA3`；`nHOLD=SD_DATA2`；`supply=VDD_SDIO`
- 证据：图 d59e37772926 / 第 1 页 / D2-D3：U4 W25Q32、R9/R10 与 SD_CMD/CLK/DATA0~3

## 内存与 Flash

### U3 ESPPSRAM64H

U3.nCS 接 GPIO16 并由 R5 10K 上拉至 VDD_SDIO，SCLK 经 R6 200R 接 GPIO17，SI/SO/SIO2/SIO3 接 SD_DATA1/0/3/2。

- 参数与网络：`nCS=GPIO16, R5 10K to VDD_SDIO`；`SCLK=GPIO17 via R6 200R`；`SI_SIO0=SD_DATA1`；`SO_SIO1=SD_DATA0`；`SIO2=SD_DATA3`；`SIO3=SD_DATA2`；`supply=VDD_SDIO`
- 证据：图 d59e37772926 / 第 1 页 / C2-C3：U3 ESPPSRAM64H、R5/R6、GPIO16/17 与 SD_DATA0~3

## 射频

### ESP_LNA 天线网络

ESP_LNA 经 C1/L1/C3（均 TBD）到选择节点，R2 0R 接 ANT1 PROANT_440，R3 DNP 接 J1 IPEX；因此当前原理图装配标记选择板载天线路径。

- 参数与网络：`rf_net=ESP_LNA`；`matching=C1/L1/C3 TBD`；`onboard_path=R2 0R -> ANT1 PROANT_440`；`external_path=R3 DNP -> J1 IPEX`
- 证据：图 d59e37772926 / 第 1 页 / A2-B3：ESP_LNA、TBD 匹配、R2 0R/ANT1、R3 DNP/J1 IPEX

## 调试与烧录

### U7 CH552T

U7.P3.6/UDP.14 与 P3.7/UDM.15 接 USB_DP/DM；CH552_TXD 经 R19 1K 接 U0RXD，CH552_RXD 经 R20 1K 接 U0TXD，R34 10K 将 CH552_RXD 节点上拉至 VCC_3V3。

- 参数与网络：`USB_DP=U7.14`；`USB_DM=U7.15`；`to_esp_rx=CH552_TXD -> R19 1K -> U0RXD`；`to_esp_tx=U0TXD -> R20 1K -> CH552_RXD`；`pullup=R34 10K to VCC_3V3`
- 证据：图 6f41535b5573 / 第 1 页 / A2-B3：U7 USB_DP/DM、CH552_TXD/RXD、R19/R20/R34 与 U0RXD/U0TXD

### GPIO0/ESP32_EN 自动下载

FET1/FET2（CJ2302）分别把 GPIO0_IN、ESP32_EN_IN 转换到 GPIO0、ESP32_EN；R12/R17 均为 2.2K，VUSB_VCC 侧分压使用 R13/R16 和 R18/R21（均 1K）。

- 参数与网络：`gpio0=U7 GPIO0_IN -> FET1 CJ2302 -> GPIO0 via R12 2.2K`；`enable=U7 ESP32_EN_IN -> FET2 CJ2302 -> ESP32_EN via R17 2.2K`；`bias=R13/R16/R18/R21 1K`
- 证据：图 6f41535b5573 / 第 1 页 / A1-B2：FET1/FET2、R12/R13/R16/R17/R18/R21 与 U7 GPIO0_IN/ESP32_EN_IN

## 模拟电路

### GPIO38 电池采样

VBAT 经 R28（1.37K）与 R29（2.67K）分压，分压中点连接 GPIO38。

- 参数与网络：`source=VBAT`；`upper_resistor=R28 1.37K`；`lower_resistor=R29 2.67K`；`adc_gpio=GPIO38`
- 证据：图 6f41535b5573 / 第 1 页 / C2-D2：VBAT-R28-GPIO38-R29-GND 分压支路

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | TimerCamera-X | `controller=U1 ESP32`；`camera=U2 OV-Camera`；`psram=U3 ESPPSRAM64H`；`flash=U4 W25Q32`；`rtc=U6 BM8563`；`usb_bridge=U7 CH552T`；`charger=U11 TP4057`；`main_regulator=U5 SY8089AAC` |
| 核心器件 | U1 ESP32 具体型号 | `documented_model=ESP32-D0WDQ6-V3`；`schematic_model=ESP32`；`reference=U1` |
| 总线 | U2 摄像头像素数据 | `D0_Y2=GPIO32`；`D1_Y1=GPIO35`；`D2_Y0=GPIO34`；`D3_Y3=GPIO5`；`D4_Y4=GPIO39`；`D5_Y5=GPIO18`；`D6_Y6=GPIO36`；`D7_Y7=GPIO19` |
| GPIO 与控制信号 | U2 相机控制与同步 | `PCLK=GPIO21 via R36 47R`；`XCLK=GPIO27 via R37 47R`；`HREF=GPIO26`；`VSYNC=GPIO22`；`RESET=GPIO15`；`SIO_C=GPIO23`；`SIO_D=GPIO25` |
| 电源 | U2 相机电源 | `DOVDD=pin11 VCC_3V3`；`DVDD=pin10 VCC_1V5`；`AVDD=pin4 VCC_2V8`；`AGND=pin2 GND`；`DGND=pin15 GND`；`PWDN=pin8 via R4 10K to GND` |
| 传感器 | U2 摄像头模组 | `documented_sensor=OV3660`；`documented_resolution=3MP / 2048x1536`；`documented_dfov=66.5°`；`schematic_designation=OV-Camera` |
| 内存与 Flash | U3 ESPPSRAM64H | `nCS=GPIO16, R5 10K to VDD_SDIO`；`SCLK=GPIO17 via R6 200R`；`SI_SIO0=SD_DATA1`；`SO_SIO1=SD_DATA0`；`SIO2=SD_DATA3`；`SIO3=SD_DATA2`；`supply=VDD_SDIO` |
| 存储 | U4 W25Q32 | `nCS=SD_CMD, R9 10K to VDD_SDIO`；`CLK=SD_CLK via R10 200R`；`DI=SD_DATA1`；`DO=SD_DATA0`；`nWP=SD_DATA3`；`nHOLD=SD_DATA2`；`supply=VDD_SDIO` |
| 内存与 Flash | U3/U4 容量 | `documented_psram=8MB Quad`；`documented_flash=4M`；`psram_part=ESPPSRAM64H`；`flash_part=W25Q32` |
| 射频 | ESP_LNA 天线网络 | `rf_net=ESP_LNA`；`matching=C1/L1/C3 TBD`；`onboard_path=R2 0R -> ANT1 PROANT_440`；`external_path=R3 DNP -> J1 IPEX` |
| 时钟 | U1 ESP32 | `crystal=X1 TXC/8Z40000017`；`XTAL_N=U1.44`；`XTAL_P=U1.45 via R35 100R`；`load_caps=C17 12pF, C18 12pF` |
| 接口 | J2 PH2.0_4P_SMT | `pin_1=GPIO13 via R7 22R`；`pin_2=GPIO4 via R8 22R`；`pin_3=VSYS_VIN`；`pin_4=GND`；`protection=D1/D2 3.3V/ESD` |
| GPIO 与控制信号 | LED1 | `gpio=GPIO2`；`led=LED1 XBLUE`；`resistor=R31 470R to GND` |
| 电源 | U5 SY8089AAC | `input=VSYS_VIN`；`output=VCC_3V3`；`inductor=L2 WPN3012H2R2MT`；`feedback=R14 11.5K/1%, R15 2.55K/1%`；`output_caps=C24/C25 22uF/6.3V` |
| 电源 | U8/U9 | `U8=HX6306P152 / 1.5V LDO 300mA -> VCC_1V5`；`U9=HX6306P282 / 2.8V LDO 300mA -> VCC_2V8`；`U8_caps=C33 4.7uF, C34 4.7uF, C41 22uF`；`U9_caps=C37 4.7uF, C38 4.7uF, C42 22uF` |
| 接口 | J3 USB-TYPEC | `VBUS=VUSB_VCC`；`DP=A6/B6 USB_DP`；`DM=A7/B7 USB_DM`；`CC1=R22 5.1K to GND`；`CC2=R23 5.1K to GND` |
| 调试与烧录 | U7 CH552T | `USB_DP=U7.14`；`USB_DM=U7.15`；`to_esp_rx=CH552_TXD -> R19 1K -> U0RXD`；`to_esp_tx=U0TXD -> R20 1K -> CH552_RXD`；`pullup=R34 10K to VCC_3V3` |
| 调试与烧录 | GPIO0/ESP32_EN 自动下载 | `gpio0=U7 GPIO0_IN -> FET1 CJ2302 -> GPIO0 via R12 2.2K`；`enable=U7 ESP32_EN_IN -> FET2 CJ2302 -> ESP32_EN via R17 2.2K`；`bias=R13/R16/R18/R21 1K` |
| 时钟 | U6 BM8563 | `rtc=U6 BM8563`；`crystal=Y1 TCX/QH0320`；`load_caps=C23/C28 7pF`；`clkout=pin7 NC` |
| 总线 | U1 与 U6 BM8563 | `SCL=GPIO14`；`SDA=GPIO12`；`alarm=RTC_ALM`；`supply=VBAT_IN`；`ground=GND` |
| 电源 | U11 TP4057 | `input=VUSB_VCC`；`charger=U11 TP4057`；`battery_net=VBAT_IN`；`program_resistor=R30 5.1K`；`input_cap=C36 4.7uF`；`battery_cap=C40 10uF`；`status_pins=CHRG/STDBY NC` |
| 接口 | J4 | `connector=SMT_HDR_2x1.25mm`；`pin_1=GND`；`pin_2=VBAT_IN` |
| 电源 | VSYS_VIN | `battery_path=VBAT -> D6 1N5819 -> VSYS_VIN`；`usb_path=VUSB_VCC -> D8 1N5819 -> VSYS_VIN`；`decoupling=C43/C44 10uF/6.3V` |
| 电源 | PWR_EN 电源保持 | `high_side=FET3 CJ2301/PMOS VBAT_IN -> VBAT`；`hold_gate=PWR_EN`；`rtc_wake=RTC_ALM via D3 1N4148`；`button_wake=USER_SWC/S1 via D5 1N4148`；`mcu_hold=GPIO33 -> FET4 CJ2302-NMOS`；`bias=R24/R25/R26 100K` |
| 模拟电路 | GPIO38 电池采样 | `source=VBAT`；`upper_resistor=R28 1.37K`；`lower_resistor=R29 2.67K`；`adc_gpio=GPIO38` |
| 复位 | ESP32_EN / S2 | `reset_net=ESP32_EN`；`pullup=R27 10K`；`button=S2 SMT_SW_PTS_820 to GND`；`protection=D9 3.3V/ESD`；`monitor_footprint=U10/C39 DNP` |
| 电源 | 内置电池与低功耗性能 | `documented_battery=140mAh`；`documented_sleep_current=2uA`；`documented_runtime=over one month at one photo/hour`；`schematic_capacity=未标注` |
| 保护电路 | J2 与复位接口 | `grove_gpio13=D1 3.3V/ESD`；`grove_gpio4=D2 3.3V/ESD`；`reset=D9 3.3V/ESD`；`usb_fuse=none shown`；`usb_tvs=none shown` |

## 待确认事项

- `component.esp32-exact-model-unconfirmed`：产品正文称主控为 ESP32-D0WDQ6-V3，但原理图 U1 仅标 ESP32，没有显示完整订货型号。（证据：图 d59e37772926 / 第 1 页 / A1-C2：U1 器件下方仅标 ESP32）
- `sensor.camera-model-performance-unconfirmed`：正文称传感器为 OV3660、3MP、最大 2048x1536、DFOV 66.5°；原理图只标 U2 为 OV-Camera，没有型号、分辨率或视场角。（证据：图 d59e37772926 / 第 1 页 / A4-C4：U2 仅标 OV-Camera 与接口引脚）
- `memory.documented-capacities-unconfirmed`：正文称 PSRAM 为 8MB Quad、Flash 为 4M；原理图只标 ESPPSRAM64H 与 W25Q32 型号，没有直接写 MB 容量。（证据：图 d59e37772926 / 第 1 页 / C2-D3：U3/U4 器件型号与引脚，无容量单位标注）
- `power.battery-performance-unconfirmed`：正文称内置 140mAh 电池、休眠电流低至 2uA 且每小时拍照可工作一个月；原理图仅显示 J4/VBAT_IN、TP4057、RTC 与保持电路，没有容量、电流或续航标注。（证据：图 6f41535b5573 / 第 1 页 / B1-D3：J4、VBAT_IN、U11、U6 与 FET3/FET4 电源保持区域，无容量/电流/续航数据）
- `review.esp32-model`：U1 的量产主控是否确为 ESP32-D0WDQ6-V3？；原因：原理图只标 ESP32，需由 BOM、芯片丝印或原始设计属性确认完整订货型号。
- `review.camera-model`：U2 所装摄像头是否为 OV3660 3MP、2048x1536、DFOV 66.5° 版本？；原因：原理图只有 OV-Camera 通用符号和电气映射，没有模组型号与光学参数。
- `review.memory-capacity`：U3/U4 的量产容量是否分别为 8MB Quad PSRAM 与 4M Flash？；原因：原理图提供 ESPPSRAM64H/W25Q32 型号但未直接标 MB 容量，需数据手册或 BOM 复核单位与容量。
- `review.battery-low-power`：量产电池容量、保护配置、2uA 休眠电流和每小时拍照续航是否符合正文声明？；原因：这些参数依赖电池、固件、RTC 唤醒和整机漏电，原理图没有容量/实测数据。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d59e377729269ff9861c98e94ea64c868010a7c625075e734628b2cae40d4c33` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/Sch_M5TimerCAM_page_01.png` |
| 2 | 1 | `6f41535b5573e4bb7000ff81b2558046dbfdc208c6f3b55c810658823d28749b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1040/Sch_M5TimerCAM_page_02.png` |

---

源文档：`zh_CN/unit/timercam_x.md`

源文档 SHA-256：`6e1d04d0435d80d3591c15e1cc9c1eb0f4d4f699a788f4a99d4252d5bac49796`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
