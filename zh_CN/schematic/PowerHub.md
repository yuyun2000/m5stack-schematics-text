# PowerHub 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | PowerHub |
| SKU | C148 |
| 产品 ID | `powerhub-896e97cb79d5` |
| 源文档 | `zh_CN/core/PowerHub.md` |

## 概述

PowerHub 采用 U5 ESP32-S3-WROOM-1U-N16R8 主控和 U11 STM32G031G8U6 电源管理协处理器，系统管理总线连接 RX8130CE RTC，独立 PM I2C 总线连接 6 颗 INA226 与 SC8721。USB 数据通过两级 FSW7227 开关在底部 USB-C、前置 USB-C 和 USB-A 之间路由，另集成 SIT1044 CAN、SIT3088 RS-485、两组 HY2.0-4P、16P 扩展总线和 8 颗 WS2812C。电源支持 USB、DC 和 2S 电池路径，包含 TP/降压/升降压转换、2S 充电、负载开关、双向 PWR CAN/PWR485 控制及分路电流监测。

## 检索关键词

`PowerHub`、`C148`、`ESP32-S3-WROOM-1U-N16R8`、`STM32G031G8U6`、`RX8130CE`、`INA226`、`0x40`、`0x42`、`0x43`、`0x44`、`0x45`、`0x46`、`SC8721`、`SIT1044T(K)3`、`SIT3088EEUA`、`FSW7227YMS10G/TR`、`MP4560DN`、`IP2326`、`SY8113IABC`、`SY8089AAAC`、`MT9700`、`MAX40200AUK+`、`CAN`、`RS485`、`USB Type-C`、`USB Type-A`、`HY2.0-4P`、`EXT 2.54-16P`、`PM_SCL`、`PM_SDA`、`SYS_SCL`、`SYS_SDA`、`SYS_BAT_2S`、`SYS_5VBUS`、`SYS_INT5V`、`SOC_3V3`、`OEN_PWROUT`、`PDCDC_REFLOW`、`WS2812C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U5 | ESP32-S3-WROOM-1U-N16R8 | 主应用控制器，连接 USB、CAN、RS-485、Grove、扩展总线和 STM32 系统管理接口 | 图 2600e4e6e7fe / 第 1 页 / A1-B2，U5 ESP32-S3-WROOM-1U-N16R8 及 GPIO 网络 |
| U11 | STM32G031G8U6 | 电源、USB 路由、LED、充电、RTC 和分路监测管理协处理器 | 图 2600e4e6e7fe / 第 1 页 / B3-C4，U11 STM32G031G8U6 全部管理信号 |
| U12 | RX8130CE | 待机电源域 I2C RTC，nIRQ 输出为 nSTBY_WKUP | 图 2600e4e6e7fe / 第 1 页 / C4，U12 RX8130CE、PM_SCL/PM_SDA、nSTBY_WKUP、BATTERY_RTC |
| U10 | ME6239A33M3G | 由 SYS_5VBUS/SYS_BAT_2S 二极管汇合输入生成 VDD_STBY | 图 2600e4e6e7fe / 第 1 页 / A3-A4，D11/D14、U10 ME6239A33M3G、VDD_STBY |
| U1/U3/U6/U7/U8/U9 | WS2812C_2020 | 主板六颗串联可寻址 RGB LED | 图 2600e4e6e7fe / 第 1 页 / C1-D3，U1/U3/U6/U7/U8/U9 WS2812C_2020 LED_DAT 链 |
| U2/U4 (ext board) | WS2812C_4020 | 顶部小板两颗侧贴可寻址 RGB LED | 图 528d784dec96 / 第 1 页 / C1-C2，U2/U4 WS2812C_4020 侧贴，LED_TOP 链 |
| S2/S5/S1(ext board) | SW / YTS-C017-F | PMU_KEY2、USER KEY 和顶部 POWER KEY 三枚物理按键 | 图 2600e4e6e7fe / 第 1 页 / C1-C2，S2 PMU_KEY2、S5 USER KEY; 图 528d784dec96 / 第 1 页 / C2，S1 YTS-C017-F，PMU_SW_TOP |
| J1 | CON5 | STM32 SWD 调试与复位接口 | 图 2600e4e6e7fe / 第 1 页 / C2-C3，J1 CON5，VDD_STBY/SWCLK/SWDIO/PMU_RST/GND |
| J4 | USB_C_16P_Horizontal | 底部 USB-C 数据和输入供电连接器 | 图 b58c5653d925 / 第 1 页 / A1，J4 USB_C_16P_Horizontal，VUSBIN/USB_DEV_DP/DM |
| U14 | AW32901FCR | VUSBIN 到 USB_5VIN 的 USB 输入电源开关 | 图 b58c5653d925 / 第 1 页 / A2，U14 AW32901FCR，VUSBIN 输入与 USB_5VIN 输出 |
| U21/U22 | FSW7227YMS10G/TR | 两级 USB 2.0 高速数据选择开关 | 图 b58c5653d925 / 第 1 页 / A3-B3，U21/U22 FSW7227YMS10G/TR 与 USB_CON_LV1/LV2 |
| J6/J7 | USB_C_16PLT-H10.0 / USB-A | 前置 USB-C 与 USB-A 主机输出接口 | 图 b58c5653d925 / 第 1 页 / A4-B4，J6 USB-C、J7 USB-A、VDD_USB_OUT 与 USB_HOST_* |
| J2/J3 | HY2.0_4P_立插 | 红色与蓝色两组 HY2.0-4P 扩展连接器 | 图 b58c5653d925 / 第 1 页 / B1-C1，J2 GRV_RED、J3 GRV_BLUE、VOUT_GROVE_RED/BLUE |
| J5 | 2X8 | 电池、DC/5 V 电源、GPIO、复位与唤醒的 16P 扩展总线 | 图 b58c5653d925 / 第 1 页 / D1，J5 2X8，VBAT_2S_CONN/VIN_ADP/SYS_5VOUT/GPIO/nSTBY_WKUP |
| J10 | DC-C0330-5.5A-2.0 | VIN_ADP 直流电源输入插座 | 图 b58c5653d925 / 第 1 页 / C1，J10 DC-C0330-5.5A-2.0，VIN_ADP |
| U17/U19/U20/U35/U36/U28 | INA226 | USB、两路 Grove、PWR CAN、PWR485 和电池六路电压电流监测 | 图 b58c5653d925 / 第 1 页 / B2-C2，U17/U19/U20 INA226，ADDR:0x40/0x42/0x43; 图 01a3306426a0 / 第 1 页 / B2-D4，U35/U36/U28 INA226，ADDR:0x44/0x45/0x46 |
| U13/U15/U16/U30/U31 | MT9700 | USB、Grove 与内部/外部 5 V 分路负载开关 | 图 b58c5653d925 / 第 1 页 / B2-C2，U13/U15/U16 MT9700; 图 01a3306426a0 / 第 1 页 / B2-C2，U30/U31 MT9700 |
| U23 | SIT1044T(K)3 | CAN 收发器，带可切换 120 Ω 终端与浪涌保护 | 图 b58c5653d925 / 第 1 页 / B3-C4，U23 SIT1044T(K)3、D8 SM24CAN、R42 120R、S3 |
| U24 | SIT3088EEUA | 半双工 RS-485 收发器，带方向控制、可切换 120 Ω 终端与浪涌保护 | 图 b58c5653d925 / 第 1 页 / C3-D4，U24 SIT3088EEUA、SM712、R43 120R、S4 |
| J8/J9 | XT30(2+2)PW-M / HT3.96_4P | 带电源的 CAN 与 RS-485 外部连接器 | 图 b58c5653d925 / 第 1 页 / C4-D4，J8 EXCON_CANH/CANL/VOUT_PWCAN，J9 EXT_485_A/B/VOUT_RS485 |
| U27 | MP4560DN | VIN_ADP 降压生成 PRE_5V | 图 01a3306426a0 / 第 1 页 / A1-A2，D10/FU6/U27 MP4560DN/L3，VIN_ADP 到 PRE_5V |
| U25 | SY8113IABC | SYS_BAT_2S 降压并经 D11/D12 输出 SYS_INT5V | 图 01a3306426a0 / 第 1 页 / B1-B2，U25 SY8113IABC、L1、D11/D12、SYS_INT5V |
| U26 | IP2326（无后缀） | SYS_5VCHG 输入的 2S 电池充电控制器 | 图 01a3306426a0 / 第 1 页 / C1-D2，U26 IP2326（无后缀）、SYS_5VCHG、SYS_BAT_2S、CHG_EN/CHG_STAT |
| U29 | SY8089AAAC | SYS_INT5V 降压生成 SOC_3V3 | 图 01a3306426a0 / 第 1 页 / C2-C3，U29 SY8089AAAC、L4、SOC_3V3 |
| U32/U33 | MAX40200AUK+ | PRE_5V 与 USB_5VIN 到 SYS_5VBUS 的双路理想二极管汇合 | 图 01a3306426a0 / 第 1 页 / A2，U32/U33 MAX40200AUK+，PRE_5V/USB_5VIN 到 SYS_5VBUS |
| U34 | SC8721 | PM I2C 控制的 RS485/CAN 双向升降压电源转换器 | 图 01a3306426a0 / 第 1 页 / A3-A4，U34 SC8721、LX1、PM_SCL/PM_SDA、PDCDC_EN、VOUT |

## 系统结构

### 双控制器系统

U5 ESP32-S3-WROOM-1U-N16R8 负责应用与外部通信，U11 STM32G031G8U6 管理分路电源、监测、RTC、USB 选择、LED、按键和充电。

- 参数与网络：`application_controller=U5 ESP32-S3-WROOM-1U-N16R8`；`management_controller=U11 STM32G031G8U6`；`system_bus=SYS_SCL/SYS_SDA`；`pm_bus=PM_SCL/PM_SDA`
- 证据：图 2600e4e6e7fe / 第 1 页 / U5/U11 与 SYS_SCL/SYS_SDA、管理控制网络

## 核心器件

### RGB LED 链

主板 6 颗 WS2812C_2020 与顶部板 2 颗 WS2812C_4020 构成共 8 颗可寻址 LED，LED_DAT 从主板串行传递到 LED_TOP。

- 参数与网络：`main_board=U1/U3/U6/U7/U8/U9 WS2812C_2020`；`top_board=U2/U4 WS2812C_4020`；`count=8`；`data_in=LED_DAT`；`interboard_net=LED_DAT_FRONT2TOP/LED_TOP`；`supply=VDD_LED`
- 证据：图 2600e4e6e7fe / 第 1 页 / C1-D3，六颗 WS2812C_2020 链; 图 528d784dec96 / 第 1 页 / C1-C2，两颗 WS2812C_4020 链

## 电源

### 待机电源域

SYS_5VBUS 与 SYS_BAT_2S 经 D11/D14 1N4148WS 汇合后输入 U10 ME6239A33M3G，输出 VDD_STBY 供 STM32 与 RTC。

- 参数与网络：`inputs=SYS_5VBUS via D11; SYS_BAT_2S via D14`；`diodes=D11/D14 1N4148WS`；`regulator=U10 ME6239A33M3G`；`output=VDD_STBY`；`consumers=U11 STM32G031G8U6; U12 RX8130CE`
- 证据：图 2600e4e6e7fe / 第 1 页 / A3-A4，D11/D14/U10/VDD_STBY

### USB 输入电源

J4 VUSBIN 输入 U14 AW32901FCR，U14 输出 USB_5VIN；该电源随后进入理想二极管汇合和充电路径。

- 参数与网络：`connector=J4`；`input=VUSBIN`；`switch=U14 AW32901FCR`；`output=USB_5VIN`
- 证据：图 b58c5653d925 / 第 1 页 / J4/U14，VUSBIN 到 USB_5VIN; 图 01a3306426a0 / 第 1 页 / U33 USB_5VIN 与 D16 充电汇合

### DC 输入降压

J10 VIN_ADP 经 D10 DSK34 与 FU6 1.5A/24V 自恢复保险丝进入 U27 MP4560DN，U27 经 L3 8.2 µH 输出 PRE_5V。

- 参数与网络：`connector=J10 DC-C0330-5.5A-2.0`；`input=VIN_ADP`；`diode=D10 DSK34`；`fuse=FU6 1.5A/24V 自恢复`；`converter=U27 MP4560DN`；`inductor=L3 8.2uH/A_0630`；`output=PRE_5V`
- 证据：图 01a3306426a0 / 第 1 页 / A1-A2，D10/FU6/U27/L3/PRE_5V

### USB/DC 5 V 汇合

U32 与 U33 MAX40200AUK+ 分别将 PRE_5V 和 USB_5VIN 理想二极管汇合为 SYS_5VBUS；D15/D16 DSK34 还将两路汇合为 SYS_5VCHG。

- 参数与网络：`system_or=PRE_5V -> U32; USB_5VIN -> U33; output SYS_5VBUS`；`charge_or=PRE_5V -> D15; USB_5VIN -> D16; output SYS_5VCHG`
- 证据：图 01a3306426a0 / 第 1 页 / A2-B2，U32/U33 与 D15/D16 汇合网络

### 2S 电池到内部 5 V

U25 SY8113IABC 从 SYS_BAT_2S 降压，经 L1 和 D11/D12 DSK34 生成 SYS_INT5V。

- 参数与网络：`input=SYS_BAT_2S`；`converter=U25 SY8113IABC`；`enable=MPWR_EN`；`output=SYS_INT5V`；`rectifiers=D11/D12 DSK34`
- 证据：图 01a3306426a0 / 第 1 页 / B1-B2，U25/L1/D11/D12/SYS_INT5V

### 主控 3.3 V

U29 SY8089AAAC 将 SYS_INT5V 降压，经 L4 WPN3012H2R2MT 生成 SOC_3V3。

- 参数与网络：`input=SYS_INT5V`；`converter=U29 SY8089AAAC`；`inductor=L4 WPN3012H2R2MT`；`output=SOC_3V3`
- 证据：图 01a3306426a0 / 第 1 页 / C2-C3，U29/L4/SOC_3V3

### 2S 电池充电

U26 IP2326（无后缀）以 SYS_5VCHG 为输入，输出 SYS_BAT_2S，并接受 CHG_EN、输出 CHG_STAT；原理图注释给出 R55=91 kΩ 时 Imax 1 A，R55=110 kΩ 时 Imax 0.82 A。

- 参数与网络：`reference=U26`；`part_number=IP2326（无后缀）`；`input=SYS_5VCHG`；`output=SYS_BAT_2S`；`enable=CHG_EN`；`status=CHG_STAT`；`current_note=R55=91K Imax 1A; R55=110K Imax 0.82A`
- 证据：图 01a3306426a0 / 第 1 页 / C1-D2，U26 与 Charging current setting 注释

### USB/Grove 分路开关与监测

U13/U15/U16 MT9700 分别受 OEN_USB/OEN_GRV_R/OEN_GRV_B 控制，输出经 U17/U19/U20 INA226 监测后送往 USB、红色 Grove 和蓝色 Grove。

- 参数与网络：`usb=U13 MT9700 -> U17 INA226 0x40 -> VDD_USB_OUT`；`grove_red=U15 MT9700 -> U19 INA226 0x42 -> VOUT_GROVE_RED`；`grove_blue=U16 MT9700 -> U20 INA226 0x43 -> VOUT_GROVE_BLUE`
- 证据：图 b58c5653d925 / 第 1 页 / B2-C2，U13/U17、U15/U19、U16/U20 三路

### RS485/CAN 双向电源转换

U34 SC8721 的输入由 SYS_BAT_2S 和 VIN_ADP 经 D17/D18 SP1060L 汇合，转换节点为 VOUT；PDCDC_EN 控制使能，PM_SCL/PM_SDA 提供配置。

- 参数与网络：`converter=U34 SC8721`；`inputs=SYS_BAT_2S via D17; VIN_ADP via D18`；`input_diodes=D17/D18 SP1060L`；`inductor=LX1 2.2uH/10A`；`output=VOUT`；`enable=PDCDC_EN`；`control_bus=PM_SCL/PM_SDA`
- 证据：图 01a3306426a0 / 第 1 页 / A3-A4，D17/D18/U34/LX1/VOUT

### PWR CAN/PWR485 分配与反向路径

VOUT 经 Q3 高边开关形成 VDD_PSU_BUS，再分别经 U35/U36 INA226 输出 VOUT_PWCAN/VOUT_RS485；VIN_ADP 与 VDD_PSU_BUS 之间另有 Q6/Q8 与 PDCDC_REFLOW 控制的反向路径。

- 参数与网络：`forward_control=OEN_PWROUT`；`high_side=Q3 AP40P04Q`；`bus=VDD_PSU_BUS`；`can_monitor=U35 INA226 0x44 -> VOUT_PWCAN`；`rs485_monitor=U36 INA226 0x45 -> VOUT_RS485`；`reverse_control=PDCDC_REFLOW`；`reverse_fets=Q6/Q8 AP40P04Q; Q9 A2N7002W`
- 证据：图 01a3306426a0 / 第 1 页 / B3-D4，Q3/U35/U36 与 Q6/Q8/Q9 PDCDC_REFLOW 路径

## 接口

### 底部 USB-C

J4 接收 VUSBIN 并承载 USB_DEV_DP/DM，数据线经 D5 ESD0524P 后进入两级 USB 选择网络。

- 参数与网络：`reference=J4`；`power=VUSBIN`；`dp=USB_DEV_DP`；`dm=USB_DEV_DM`；`protection=D5 ESD0524P`
- 证据：图 b58c5653d925 / 第 1 页 / A1，J4/D5，VUSBIN/USB_DEV_DP/DM

### 前置 USB 主机接口

J7 USB-A 使用 USB_HOST_DP_A/DM_A，J6 USB-C 使用 USB_HOST_DP_C/DM_C；两者均由 VDD_USB_OUT 供电并分别经 D6/D7 ESD0524P 保护。

- 参数与网络：`usb_a=J7 USB-A`；`usb_c=J6 USB_C_16PLT-H10.0`；`power=VDD_USB_OUT`；`usb_a_esd=D6 ESD0524P`；`usb_c_esd=D7 ESD0524P`
- 证据：图 b58c5653d925 / 第 1 页 / A4-B4，D6/J7 与 D7/J6

### 红色 HY2.0-4P

J2 pins 4/3 为 GRV_RED_SCL/SDA，pin 2 为 VOUT_GROVE_RED，pin 1 为 GND；信号经 D3 ESD0524P 保护。

- 参数与网络：`pin4=GRV_RED_SCL/GPIO16`；`pin3=GRV_RED_SDA/GPIO15`；`pin2=VOUT_GROVE_RED`；`pin1=GND`；`protection=D3 ESD0524P`
- 证据：图 b58c5653d925 / 第 1 页 / B1，J2/D3

### 蓝色 HY2.0-4P

J3 pins 4/3 为 GRV_BLUE_RX/TX，pin 2 为 VOUT_GROVE_BLUE，pin 1 为 GND；信号经 D4 ESD0524P 保护。

- 参数与网络：`pin4=GRV_BLUE_RX/GPIO2`；`pin3=GRV_BLUE_TX/GPIO1`；`pin2=VOUT_GROVE_BLUE`；`pin1=GND`；`protection=D4 ESD0524P`
- 证据：图 b58c5653d925 / 第 1 页 / C1，J3/D4

### 16P 扩展总线

J5 提供双 BAT-2S、VIN_ADP、SYS_5VOUT、双 GND、GPIO43/44/42/41/40/7/6/5、PMU_RST 和 nSTBY_WKUP。

- 参数与网络：`pins1_2=VBAT_2S_CONN`；`pin3=VIN_ADP`；`pin4=SYS_5VOUT`；`pins5_6=GND`；`pin7=STD_GPIO43`；`pin8=PMU_RST`；`pin9=STD_GPIO44`；`pin10=nSTBY_WKUP`；`pin11=STD_GPIO42`；`pin12=STD_GPIO7`；`pin13=STD_GPIO41`；`pin14=STD_GPIO6`；`pin15=STD_GPIO4`；`pin16=STD_GPIO5`
- 证据：图 b58c5653d925 / 第 1 页 / D1，J5 2X8 pins 1-16

## 总线

### ESP32 与 STM32 管理链路

ESP32 GPIO45/SYS_SDA(PMU_RX) 与 GPIO48/SYS_SCL(PMU_TX) 连接 STM32 PB7/PB6，GPIO0/xGPIO_BOOT 连接 STM32 PA3。

- 参数与网络：`esp_sda_rx=GPIO45 SYS_SDA/PMU_RX`；`esp_scl_tx=GPIO48 SYS_SCL/PMU_TX`；`stm_rx=PB7 SYS_SDA/PMU_RX`；`stm_tx=PB6 SYS_SCL/PMU_TX`；`boot=ESP GPIO0 xGPIO_BOOT -> STM PA3`
- 证据：图 2600e4e6e7fe / 第 1 页 / U5 GPIO45/GPIO48/GPIO0 与 U11 PB7/PB6/PA3

### 电源管理 I2C

STM32 PA11/PM_SCL 与 PA12/PM_SDA 连接 RX8130CE、六颗 INA226 和 SC8721。

- 参数与网络：`controller=U11 STM32G031G8U6`；`scl=PA11/PM_SCL`；`sda=PA12/PM_SDA`；`devices=U12 RX8130CE; U17/U19/U20/U28/U35/U36 INA226; U34 SC8721`
- 证据：图 2600e4e6e7fe / 第 1 页 / U11 PA11/PA12 与 U12 PM_SCL/PM_SDA; 图 b58c5653d925 / 第 1 页 / U17/U19/U20 INA226 PM_SCL/PM_SDA; 图 01a3306426a0 / 第 1 页 / U28/U35/U36 INA226 与 U34 SC8721 PM_SCL/PM_SDA

### USB 两级数据切换

U22 在 MCU_USB_DP/DM 与 USB_DEV_DP/DM 间形成一级切换，U21 再将 USB_HOST_DP/DM 分配到前置 USB-A 或 USB-C。

- 参数与网络：`level1_switch=U22 FSW7227YMS10G/TR`；`level1_control=USB_CON_LV1`；`level2_switch=U21 FSW7227YMS10G/TR`；`level2_control=USB_CON_LV2`；`targets=J4 bottom USB-C; J6 front USB-C; J7 front USB-A`
- 证据：图 b58c5653d925 / 第 1 页 / U21/U22 HSD1/HSD2/D+/D- 网络

### CAN 总线

U23 SIT1044T(K)3 将 MCU_CAN_TXD/RXD 转换为 CANH/CANL，线路经 FU2/FU3 60V/200mA、D8 SM24CAN 保护，并可由 S3 接入 R42 120 Ω 终端。

- 参数与网络：`transceiver=U23 SIT1044T(K)3`；`tx=MCU_CAN_TXD`；`rx=MCU_CAN_RXD`；`bus=EXCON_CANH; EXCON_CANL`；`fuses=FU2/FU3 60V/200mA`；`tvs=D8 SM24CAN`；`termination=R42 120R via S3`；`connector=J8 XT30(2+2)PW-M`
- 证据：图 b58c5653d925 / 第 1 页 / B3-C4，U23/FU2/FU3/D8/R42/S3/J8

### RS-485 总线

U24 SIT3088EEUA 将 MCU_485_TXD/RXD/DIR 转换为 EXT_485_A/B，线路经 FU4/FU5 60V/200mA、SM712 保护，并可由 S4 接入 R43 120 Ω 终端。

- 参数与网络：`transceiver=U24 SIT3088EEUA`；`tx=MCU_485_TXD`；`rx=MCU_485_RXD`；`direction=MCU_485_DIR`；`bus=EXT_485_A; EXT_485_B`；`fuses=FU4/FU5 60V/200mA`；`tvs=SM712`；`termination=R43 120R via S4`；`connector=J9 HT3.96_4P`
- 证据：图 b58c5653d925 / 第 1 页 / C3-D4，U24/FU4/FU5/SM712/R43/S4/J9

## 总线地址

### INA226 地址映射

原理图明确标出六颗 INA226 的 7-bit 地址：USB 0x40、Grove Red 0x42、Grove Blue 0x43、PWR CAN 0x44、PWR485 0x45、电池 0x46。

- 参数与网络：`U17_USB=0x40`；`U19_GROVE_RED=0x42`；`U20_GROVE_BLUE=0x43`；`U35_PWR_CAN=0x44`；`U36_PWR485=0x45`；`U28_BATTERY=0x46`
- 证据：图 b58c5653d925 / 第 1 页 / U17 ADDR:0X40、U19 ADDR:0X42、U20 ADDR:0X43; 图 01a3306426a0 / 第 1 页 / U35 ADDR:0X44、U36 ADDR:0X45、U28 ADDR:0X46

## GPIO 与控制信号

### ESP32 通信 GPIO

RS-485 TX/DIR/RX 使用 GPIO8/GPIO18/GPIO17，CAN TX/RX 使用 GPIO39/GPIO40，USB DM/DP 使用 GPIO19/GPIO20。

- 参数与网络：`rs485_tx=GPIO8 MCU_485_TXD`；`rs485_dir=GPIO18 MCU_485_DIR`；`rs485_rx=GPIO17 MCU_485_RXD`；`can_tx=GPIO39 MCU_CAN_TXD`；`can_rx=GPIO40 MCU_CAN_RXD`；`usb_dm=GPIO19 MCU_USB_DM`；`usb_dp=GPIO20 MCU_USB_DP`
- 证据：图 2600e4e6e7fe / 第 1 页 / U5 GPIO8/17/18/19/20/39/40 网络映射

### Grove GPIO 映射

红色 Grove 使用 GPIO16/GRV_RED_SCL 与 GPIO15/GRV_RED_SDA；蓝色 Grove 使用 GPIO1/GRV_BLUE_TX 与 GPIO2/GRV_BLUE_RX。

- 参数与网络：`red_scl=GPIO16`；`red_sda=GPIO15`；`blue_tx=GPIO1`；`blue_rx=GPIO2`
- 证据：图 2600e4e6e7fe / 第 1 页 / U5 GRV_RED_SDA/SCL 与 GRV_BLUE_TX/RX; 图 b58c5653d925 / 第 1 页 / J2/J3 Grove 连接器

### STM32 电源控制映射

STM32 使用 PB8/OEN_USB、PC14/OEN_GRV_R、PC15/OEN_GRV_B、PB1/OEN_PWROUT、PA8/PDCDC_REFLOW、PC6/PDCDC_EN 控制各电源路径。

- 参数与网络：`usb=PB8 OEN_USB`；`grove_red=PC14 OEN_GRV_R`；`grove_blue=PC15 OEN_GRV_B`；`power_output=PB1 OEN_PWROUT`；`reflow=PA8 PDCDC_REFLOW`；`dc_dc_enable=PC6 PDCDC_EN`
- 证据：图 2600e4e6e7fe / 第 1 页 / U11 PB8/PC14/PC15/PB1/PA8/PC6 管脚网络

### USB 选择控制

STM32 PB3/USB_CON_LV1 控制 U22，PA15/USB_CON_LV2 控制 U21。

- 参数与网络：`level1=PB3 USB_CON_LV1 -> U22 OE#`；`level2=PA15 USB_CON_LV2 -> U21 OE#`
- 证据：图 2600e4e6e7fe / 第 1 页 / U11 PB3/PA15; 图 b58c5653d925 / 第 1 页 / U21/U22 OE# 与 USB_CON_LV2/LV1

## 保护电路

### 通信接口保护

USB 设备/主机口使用 ESD0524P，CAN 使用 SM24CAN 与 60V/200mA 保险丝，RS-485 使用 SM712 与 60V/200mA 保险丝。

- 参数与网络：`usb=D5/D6/D7 ESD0524P`；`can=D8 SM24CAN; FU2/FU3 60V/200mA`；`rs485=SM712; FU4/FU5 60V/200mA`
- 证据：图 b58c5653d925 / 第 1 页 / D5/D6/D7 USB ESD；D8/FU2/FU3 CAN；SM712/FU4/FU5 RS485

## 传感器

### RTC 唤醒

U12 RX8130CE 由 VDD_STBY 供电，nIRQ 输出网络 nSTBY_WKUP 连接 STM32 PB5 和 16P 扩展总线。

- 参数与网络：`reference=U12`；`part_number=RX8130CE`；`supply=VDD_STBY`；`interrupt=nSTBY_WKUP`；`stm32_pin=PB5`；`external_pin=J5 pin 10`
- 证据：图 2600e4e6e7fe / 第 1 页 / U12 nIRQ/nSTBY_WKUP 与 U11 PB5; 图 b58c5653d925 / 第 1 页 / J5 pin 10 nSTBY_WKUP

## 调试与烧录

### STM32 SWD

J1 五针接口依次提供 VDD_STBY、SWCLK、SWDIO、PMU_RST 和 GND，用于 STM32 调试与复位。

- 参数与网络：`reference=J1`；`pin1=VDD_STBY`；`pin2=SWCLK`；`pin3=SWDIO`；`pin4=PMU_RST`；`pin5=GND`
- 证据：图 2600e4e6e7fe / 第 1 页 / C2-C3，J1 CON5 pins 1-5

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 双控制器系统 | `application_controller=U5 ESP32-S3-WROOM-1U-N16R8`；`management_controller=U11 STM32G031G8U6`；`system_bus=SYS_SCL/SYS_SDA`；`pm_bus=PM_SCL/PM_SDA` |
| 总线 | ESP32 与 STM32 管理链路 | `esp_sda_rx=GPIO45 SYS_SDA/PMU_RX`；`esp_scl_tx=GPIO48 SYS_SCL/PMU_TX`；`stm_rx=PB7 SYS_SDA/PMU_RX`；`stm_tx=PB6 SYS_SCL/PMU_TX`；`boot=ESP GPIO0 xGPIO_BOOT -> STM PA3` |
| 总线 | 电源管理 I2C | `controller=U11 STM32G031G8U6`；`scl=PA11/PM_SCL`；`sda=PA12/PM_SDA`；`devices=U12 RX8130CE; U17/U19/U20/U28/U35/U36 INA226; U34 SC8721` |
| 总线地址 | INA226 地址映射 | `U17_USB=0x40`；`U19_GROVE_RED=0x42`；`U20_GROVE_BLUE=0x43`；`U35_PWR_CAN=0x44`；`U36_PWR485=0x45`；`U28_BATTERY=0x46` |
| GPIO 与控制信号 | ESP32 通信 GPIO | `rs485_tx=GPIO8 MCU_485_TXD`；`rs485_dir=GPIO18 MCU_485_DIR`；`rs485_rx=GPIO17 MCU_485_RXD`；`can_tx=GPIO39 MCU_CAN_TXD`；`can_rx=GPIO40 MCU_CAN_RXD`；`usb_dm=GPIO19 MCU_USB_DM`；`usb_dp=GPIO20 MCU_USB_DP` |
| GPIO 与控制信号 | Grove GPIO 映射 | `red_scl=GPIO16`；`red_sda=GPIO15`；`blue_tx=GPIO1`；`blue_rx=GPIO2` |
| GPIO 与控制信号 | STM32 电源控制映射 | `usb=PB8 OEN_USB`；`grove_red=PC14 OEN_GRV_R`；`grove_blue=PC15 OEN_GRV_B`；`power_output=PB1 OEN_PWROUT`；`reflow=PA8 PDCDC_REFLOW`；`dc_dc_enable=PC6 PDCDC_EN` |
| GPIO 与控制信号 | USB 选择控制 | `level1=PB3 USB_CON_LV1 -> U22 OE#`；`level2=PA15 USB_CON_LV2 -> U21 OE#` |
| 接口 | 底部 USB-C | `reference=J4`；`power=VUSBIN`；`dp=USB_DEV_DP`；`dm=USB_DEV_DM`；`protection=D5 ESD0524P` |
| 接口 | 前置 USB 主机接口 | `usb_a=J7 USB-A`；`usb_c=J6 USB_C_16PLT-H10.0`；`power=VDD_USB_OUT`；`usb_a_esd=D6 ESD0524P`；`usb_c_esd=D7 ESD0524P` |
| 总线 | USB 两级数据切换 | `level1_switch=U22 FSW7227YMS10G/TR`；`level1_control=USB_CON_LV1`；`level2_switch=U21 FSW7227YMS10G/TR`；`level2_control=USB_CON_LV2`；`targets=J4 bottom USB-C; J6 front USB-C; J7 front USB-A` |
| 总线 | CAN 总线 | `transceiver=U23 SIT1044T(K)3`；`tx=MCU_CAN_TXD`；`rx=MCU_CAN_RXD`；`bus=EXCON_CANH; EXCON_CANL`；`fuses=FU2/FU3 60V/200mA`；`tvs=D8 SM24CAN`；`termination=R42 120R via S3`；`connector=J8 XT30(2+2)PW-M` |
| 总线 | RS-485 总线 | `transceiver=U24 SIT3088EEUA`；`tx=MCU_485_TXD`；`rx=MCU_485_RXD`；`direction=MCU_485_DIR`；`bus=EXT_485_A; EXT_485_B`；`fuses=FU4/FU5 60V/200mA`；`tvs=SM712`；`termination=R43 120R via S4`；`connector=J9 HT3.96_4P` |
| 接口 | 红色 HY2.0-4P | `pin4=GRV_RED_SCL/GPIO16`；`pin3=GRV_RED_SDA/GPIO15`；`pin2=VOUT_GROVE_RED`；`pin1=GND`；`protection=D3 ESD0524P` |
| 接口 | 蓝色 HY2.0-4P | `pin4=GRV_BLUE_RX/GPIO2`；`pin3=GRV_BLUE_TX/GPIO1`；`pin2=VOUT_GROVE_BLUE`；`pin1=GND`；`protection=D4 ESD0524P` |
| 接口 | 16P 扩展总线 | `pins1_2=VBAT_2S_CONN`；`pin3=VIN_ADP`；`pin4=SYS_5VOUT`；`pins5_6=GND`；`pin7=STD_GPIO43`；`pin8=PMU_RST`；`pin9=STD_GPIO44`；`pin10=nSTBY_WKUP`；`pin11=STD_GPIO42`；`pin12=STD_GPIO7`；`pin13=STD_GPIO41`；`pin14=STD_GPIO6`；`pin15=STD_GPIO4`；`pin16=STD_GPIO5` |
| 电源 | 待机电源域 | `inputs=SYS_5VBUS via D11; SYS_BAT_2S via D14`；`diodes=D11/D14 1N4148WS`；`regulator=U10 ME6239A33M3G`；`output=VDD_STBY`；`consumers=U11 STM32G031G8U6; U12 RX8130CE` |
| 电源 | USB 输入电源 | `connector=J4`；`input=VUSBIN`；`switch=U14 AW32901FCR`；`output=USB_5VIN` |
| 电源 | DC 输入降压 | `connector=J10 DC-C0330-5.5A-2.0`；`input=VIN_ADP`；`diode=D10 DSK34`；`fuse=FU6 1.5A/24V 自恢复`；`converter=U27 MP4560DN`；`inductor=L3 8.2uH/A_0630`；`output=PRE_5V` |
| 电源 | USB/DC 5 V 汇合 | `system_or=PRE_5V -> U32; USB_5VIN -> U33; output SYS_5VBUS`；`charge_or=PRE_5V -> D15; USB_5VIN -> D16; output SYS_5VCHG` |
| 电源 | 2S 电池到内部 5 V | `input=SYS_BAT_2S`；`converter=U25 SY8113IABC`；`enable=MPWR_EN`；`output=SYS_INT5V`；`rectifiers=D11/D12 DSK34` |
| 电源 | 主控 3.3 V | `input=SYS_INT5V`；`converter=U29 SY8089AAAC`；`inductor=L4 WPN3012H2R2MT`；`output=SOC_3V3` |
| 电源 | 2S 电池充电 | `reference=U26`；`part_number=IP2326（无后缀）`；`input=SYS_5VCHG`；`output=SYS_BAT_2S`；`enable=CHG_EN`；`status=CHG_STAT`；`current_note=R55=91K Imax 1A; R55=110K Imax 0.82A` |
| 电源 | USB/Grove 分路开关与监测 | `usb=U13 MT9700 -> U17 INA226 0x40 -> VDD_USB_OUT`；`grove_red=U15 MT9700 -> U19 INA226 0x42 -> VOUT_GROVE_RED`；`grove_blue=U16 MT9700 -> U20 INA226 0x43 -> VOUT_GROVE_BLUE` |
| 电源 | RS485/CAN 双向电源转换 | `converter=U34 SC8721`；`inputs=SYS_BAT_2S via D17; VIN_ADP via D18`；`input_diodes=D17/D18 SP1060L`；`inductor=LX1 2.2uH/10A`；`output=VOUT`；`enable=PDCDC_EN`；`control_bus=PM_SCL/PM_SDA` |
| 电源 | PWR CAN/PWR485 分配与反向路径 | `forward_control=OEN_PWROUT`；`high_side=Q3 AP40P04Q`；`bus=VDD_PSU_BUS`；`can_monitor=U35 INA226 0x44 -> VOUT_PWCAN`；`rs485_monitor=U36 INA226 0x45 -> VOUT_RS485`；`reverse_control=PDCDC_REFLOW`；`reverse_fets=Q6/Q8 AP40P04Q; Q9 A2N7002W` |
| 传感器 | RTC 唤醒 | `reference=U12`；`part_number=RX8130CE`；`supply=VDD_STBY`；`interrupt=nSTBY_WKUP`；`stm32_pin=PB5`；`external_pin=J5 pin 10` |
| 调试与烧录 | STM32 SWD | `reference=J1`；`pin1=VDD_STBY`；`pin2=SWCLK`；`pin3=SWDIO`；`pin4=PMU_RST`；`pin5=GND` |
| 核心器件 | RGB LED 链 | `main_board=U1/U3/U6/U7/U8/U9 WS2812C_2020`；`top_board=U2/U4 WS2812C_4020`；`count=8`；`data_in=LED_DAT`；`interboard_net=LED_DAT_FRONT2TOP/LED_TOP`；`supply=VDD_LED` |
| 保护电路 | 通信接口保护 | `usb=D5/D6/D7 ESD0524P`；`can=D8 SM24CAN; FU2/FU3 60V/200mA`；`rs485=SM712; FU4/FU5 60V/200mA` |
| 存储 | ESP32 模组 Flash 容量 | `module=ESP32-S3-WROOM-1U-N16R8`；`claimed_flash=16MB`；`schematic_capacity_text=not separately printed` |
| 内存与 Flash | ESP32 模组 PSRAM 容量 | `module=ESP32-S3-WROOM-1U-N16R8`；`claimed_psram=8MB Octal`；`schematic_capacity_text=not separately printed` |
| 总线地址 | RTC 与 SC8721 I2C 地址 | `rtc=U12 RX8130CE`；`converter=U34 SC8721`；`addresses=not printed` |
| 电源 | RTC 后备电容规格 | `rtc=U12 RX8130CE`；`net=BATTERY_RTC`；`document_claim=70000uF/3.3V`；`status=requires BOM confirmation` |
| 电源 | 可拆卸电池型号与容量 | `confirmed_topology=2S battery`；`nets=VBAT_2S_CONN; SYS_BAT_2S`；`unverified_models=NP-F550/750/950`；`unverified_capacity=2000mAh kit battery` |
| 电源 | 外部输入范围与端口输出能力 | `inputs=VIN_ADP; VUSBIN; SYS_BAT_2S; VOUT_PWCAN; VOUT_RS485`；`unverified_dc_range=9-20V`；`unverified_output_table=per-port current capability` |

## 待确认事项

- `storage.module-capacity`：原理图确认模组完整料号 ESP32-S3-WROOM-1U-N16R8，但未单独以容量字段标注 16 MB Flash。（证据：图 2600e4e6e7fe / 第 1 页 / U5 仅以模组后缀 N16R8 表示变体）
- `memory.module-psram`：原理图确认模组完整料号 ESP32-S3-WROOM-1U-N16R8，但未单独以容量字段标注 8 MB PSRAM 或其总线模式。（证据：图 2600e4e6e7fe / 第 1 页 / U5 仅以模组后缀 N16R8 表示变体）
- `address.rtc-sc8721`：RX8130CE 和 SC8721 均连接 PM_SCL/PM_SDA，但原理图未直接印出其 7-bit I2C 地址。（证据：图 2600e4e6e7fe / 第 1 页 / U12 PM_SCL/PM_SDA，无地址文本; 图 01a3306426a0 / 第 1 页 / U34 PM_SCL/PM_SDA，无地址文本）
- `power.rtc-backup-capacitor`：原理图显示 BATTERY_RTC 储能网络，但其标注与产品正文所述 70000 µF/3.3 V 不能在当前页面上直接建立一致对应。（证据：图 2600e4e6e7fe / 第 1 页 / U12 VBAT/BATTERY_RTC 与 C16/C18 储能网络）
- `power.battery-model-capacity`：原理图以 VBAT_2S_CONN/SYS_BAT_2S 确认 2S 电池路径，但未标注 NP-F550/750/950 型号或 2000 mAh 容量。（证据：图 b58c5653d925 / 第 1 页 / J5 VBAT_2S_CONN; 图 01a3306426a0 / 第 1 页 / SYS_BAT_2S 电源与充电网络未标电池型号容量）
- `power.external-ratings`：原理图给出 DC、USB、2S、PWR CAN/PWR485 的拓扑与器件，但未直接列出 DC 9–20 V 输入范围或各端口完整电流能力表。（证据：图 b58c5653d925 / 第 1 页 / J10/J8/J9 连接器未标完整输入范围; 图 01a3306426a0 / 第 1 页 / 电源转换拓扑未列整机端口输出能力表）
- `review.module-flash`：请用 ESP32-S3-WROOM-1U-N16R8 datasheet/BOM 确认 16 MB Flash。；原因：原理图只给出模组后缀，未单列容量。
- `review.module-psram`：请用模组 datasheet/BOM 确认 8 MB Octal PSRAM。；原因：原理图未单列 PSRAM 容量和模式。
- `review.rtc-sc8721-address`：请用 RX8130CE 与 SC8721 datasheet 复核各自 7-bit I2C 地址。；原因：原理图未直接印出地址，不能按经验补全。
- `review.rtc-backup-capacitor`：请用 BOM 确认 RTC 后备储能器件是否为 70000 µF/3.3 V。；原因：当前原理图的 BATTERY_RTC 电容网络无法直接对应正文规格。
- `review.battery-model-capacity`：请用电池/BOM 确认兼容 NP-F550/750/950 及 Kit 电池 2000 mAh。；原因：原理图只确认 2S 电气路径。
- `review.external-ratings`：请用验证报告/BOM 复核 DC 9–20 V 与各供电方式下的端口输出能力。；原因：这些整机额定值不在原理图中直接列出。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `2600e4e6e7fea0a143b4d5a2e2958967617af0d6b30dcbabf8bfcb9b07432ae6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/PowerHub_SCH_Main_b0.3_20250704_Docs_2025_09_09_14_01_58_page_01.png` |
| 2 | 1 | `b58c5653d925ac84553af79010f8d11de940f194c9839ff74d452c6f229ee19c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/PowerHub_SCH_Main_b0.3_20250704_Docs_2025_09_09_14_01_58_page_02.png` |
| 3 | 1 | `01a3306426a03b49030d4e7e74154045c49e912bd41c1e0ed54a01d78e02c9d6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/PowerHub_SCH_Main_b0.3_20250704_Docs_2025_09_09_14_01_58_page_03.png` |
| 4 | 1 | `528d784dec965f2689cbf2674528ed3fd3ec463f05572c6b60d0e6aa792bb345` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/PowerHub_SCH_ext_b03_20250718_Docs_2025_09_09_14_01_53_page_01.png` |

---

源文档：`zh_CN/core/PowerHub.md`

源文档 SHA-256：`047e3cb292954c2b8e5f9eaf11503443e978fc36f072571041dd075c7fbe8751`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
