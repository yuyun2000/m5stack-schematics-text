# StackChan Core 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StackChan Core |
| SKU | C156 |
| 产品 ID | `stackchan-core-cbbf2e7748c5` |
| 源文档 | `zh_CN/core/StackChan_Core.md` |

## 概述

StackChan Core 清单绑定的七页 CoreS3 v1.0 电路以 ESP32-S3 为主控，集成 AXP2101 电源、128Mbit SPI Flash、外部 PSRAM、USB Type-C/OTG、BM8563 RTC、AW88298 功放、ES7210 双麦克风编码、AW9523B IO 扩展、LCD/触摸/摄像头连接器、microSD，以及 BMI270 通过辅助 I2C 挂载 BMM150。图中明确标注 AXP2101=0x34、AW88298=0x36、ES7210=0x40、AW9523B=0x58、BMI270=0x69。产品源文档声明 StackChan Core 与 CoreS3/CoreS3-Lite 硬件功能相同并预置 StackChan 固件，但七页资源没有 StackChan Core/C156 标识；8MB PSRAM、ILI9342C、GC0308、LTR-553ALS-WA、1W 扬声器和无线性能也未在当前主板图中完整标注，因此这些产品级信息保留待确认。

## 检索关键词

`StackChan Core`、`C156`、`StackChan`、`CoreS3 v1.0`、`ESP32-S3`、`GD25Q128`、`W25Q128`、`128Mbit Flash`、`16MB Flash`、`EPSRAM`、`8MB PSRAM`、`AXP2101`、`AXP2101 0x34`、`SY7088`、`BM8563`、`AW88298`、`AW88298 0x36`、`ES7210`、`ES7210 0x40`、`AW9523B`、`AW9523B 0x58`、`BMI270`、`BMI270 0x69`、`BMM150`、`GC0308`、`LTR-553ALS-WA`、`ILI9342C`、`MicroSD-SPI`、`USB Type-C`、`USB OTG`、`StackChan firmware`、`BUS_OUT_EN`、`USB_OTG_EN`、`I2C_SYS_SDA`、`I2C_SYS_SCL`、`I2S_BCK`、`I2S_WCK`、`I2S_DATO`、`I2S_DATI`、`M5.BUS`、`BUS_5V`、`BUS_OUT`、`VUSB`、`VBUS`、`VDD_3V3`、`VCC_3V3`、`VDD_1V8`、`VDDCAM_3V3`、`VDD_3V3_SD`、`VCC_BL`、`PROANT440`、`IPEX`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | AXP2101 | 0x34 电源管理器，管理 VBUS/VBAT 并生成数字、模拟、摄像头、SD、RTC 与背光电源轨 | 图 de85c198f634 / 第 1 页 / 网格 B1-D3，U1 AXP2101 全部电源输出和 0x34 标注 |
| U5 | ESP32-S3 | 主控，连接 Flash/PSRAM、USB、I2C、I2S、摄像头、LCD、microSD、总线和射频 | 图 8f2f5466da03 / 第 1 页 / 网格 A1-C2，U5 ESP32-S3 全部引脚 |
| U6 | GD25Q128/W25Q128/128Mbit/3.3V | ESP32-S3 外部 128Mbit QSPI Flash | 图 8f2f5466da03 / 第 1 页 / 网格 A3-B4，U6 与 FLASH_CS0/CLK/D/Q/WP/HD |
| U7 | EPSRAM | ESP32-S3 外部 SPI PSRAM，复用 FLASH_CLK/D/Q/WP/HD 并使用 FLASH_CS1 | 图 8f2f5466da03 / 第 1 页 / 网格 B3，U7 EPSRAM |
| U3 | SY7088 | AXP_PS 到 BUS_5V 的升压转换器 | 图 674d725f5dc6 / 第 1 页 / 网格 B1-C2，U3 SY7088、L5 与 BOOST_EN |
| U4 | BM8563 | RTC_VDD 供电的 I2C 实时时钟，INT 接 AXP_WAKEUP | 图 674d725f5dc6 / 第 1 页 / 网格 C1-D3，U4 BM8563 与 Y1 |
| U8 | AW88298 | 0x36 I2C/I2S 扬声器功放，输出 SPK_VOP/SPK_VON | 图 f7f0dc3f29b1 / 第 1 页 / 网格 A1-B2，U8 AW88298 与 0x36 标注 |
| U9 | ES7210 | 0x40 四通道音频 ADC，连接双模拟麦克风、I2S 和 AEC 回采 | 图 f7f0dc3f29b1 / 第 1 页 / 网格 C1-D3，U9 ES7210 与 0x40 标注 |
| U12,U13 | MSM381A3729H9BPC | 两颗模拟麦克风，经隔直电容连接 ES7210 MIC1/MIC2 差分输入 | 图 f7f0dc3f29b1 / 第 1 页 / 网格 C3-D4，U12/U13 麦克风与 VBIAS_MIC |
| U10 | AW9523B | 0x58 I2C IO 扩展器，控制触摸、LCD、摄像头、音频、TF、OTG 和 Boost 信号 | 图 12e215412fd9 / 第 1 页 / 网格 A3-B4，U10 AW9523B 与 0x58 标注 |
| U15 | BMI270 | 0x69 I2C 六轴 IMU，并以 ASDX/ASCX 连接 BMM150 | 图 95d654aa1d79 / 第 1 页 / 网格 B1-C3，U15 BMI270 与地址配置 |
| U20 | BMM150 | 挂载在 BMI270 辅助 I2C 总线上的三轴磁力计 | 图 95d654aa1d79 / 第 1 页 / 网格 B3-C4，U20 BMM150 |
| J1 | USB-TYPEC | USB-C 电源与 USB D+/D- 接口，CC1/CC2 各有 5.1K 下拉 | 图 674d725f5dc6 / 第 1 页 / 网格 A3-B4，J1 USB-TYPEC 与 R6/R9/D4/D6 |
| U11 | MicroSD-SPI | 3.3V microSD 卡槽，连接 TF_CS 与 SPI_MOSI/SCK/MISO | 图 12e215412fd9 / 第 1 页 / 网格 C2-D3，U11 MicroSD-SPI |
| LCD1,CTP1 | M5_LCD_10P / M5_TOUCH_8P | LCD 与电容触摸子板连接器 | 图 12e215412fd9 / 第 1 页 / 网格 C4-D4，LCD1 与 CTP1 |
| J2 | AFC34-S24FIA-00 | 24 针摄像头/传感子板连接器，承载并行像素、I2C、时钟、复位、掉电和多路电源 | 图 12e215412fd9 / 第 1 页 / 网格 A1-B2，J2 24-pin camera connector |
| BUS1,J3 | M5.BUS / GH2.0-4P | 30 针 M5-BUS 与 BUS_PA_SCL/SDA/BUS_OUT Grove 接口 | 图 12e215412fd9 / 第 1 页 / 网格 C1-D2，BUS1 与 J3 |
| U14,U17 | ME1502AM5G | 高电平使能的 BUS_5V->BUS_OUT 与 BUS_OUT->VUSB 电源开关 | 图 97e9cd876f18 / 第 1 页 / 网格 A1-B4，U14/U17 Boost 与 OTG 路径 |
| U18,U19 | ME1502CM5G | 低电平使能的 VUSB->VBUS 与 BUS_OUT->VBUS 电源开关 | 图 97e9cd876f18 / 第 1 页 / 网格 B2-C4，U18/U19 USB 与 PMU 路径 |

## 系统结构

### 七页 CoreS3 v1.0 主板架构

七页资源以 U5 ESP32-S3 为主控，连接 AXP2101 电源、128Mbit Flash、外部 PSRAM、USB-C/OTG、BM8563、AW88298/ES7210 双麦克风音频、AW9523B、LCD/触摸/摄像头连接器、microSD、M5-BUS 以及 BMI270+BMM150。

- 参数与网络：`controller=U5 ESP32-S3`；`power=U1 AXP2101`；`memory=U6 128Mbit Flash,U7 EPSRAM`；`audio=U8 AW88298,U9 ES7210,U12/U13`；`sensors=U15 BMI270,U20 BMM150`；`expander=U10 AW9523B`；`interfaces=USB-C,LCD,Touch,Camera,microSD,M5.BUS`
- 证据：图 de85c198f634 / 第 1 页 / AXP2101 电源页; 图 8f2f5466da03 / 第 1 页 / ESP32-S3/Flash/PSRAM 页; 图 f7f0dc3f29b1 / 第 1 页 / 音频页; 图 12e215412fd9 / 第 1 页 / 扩展接口页; 图 95d654aa1d79 / 第 1 页 / BMI270/BMM150 页

## 电源

### AXP2101 电源轨

U1 AXP2101 从 VBUS/VBAT 供电：LX1 经 L1 产生 VDD_3V3，LX3 经 L3 产生 VCC_3V3；BLDO1/2 输出 AVDD/DVDD，DLDO1/DC1SW 输出 VCC_BL，VBackup/VRTC 连接 RTC_VDD，ALDO1-4 分别输出 VDD_1V8、VDDA_3V3、VDDCAM_3V3、VDD_3V3_SD。

- 参数与网络：`dcdc1=VDD_3V3`；`dcdc3=VCC_3V3`；`bldo1=AVDD`；`bldo2=DVDD`；`dldo1=VCC_BL`；`rtc=RTC_VDD`；`aldo1=VDD_1V8`；`aldo2=VDDA_3V3`；`aldo3=VDDCAM_3V3`；`aldo4=VDD_3V3_SD`
- 证据：图 de85c198f634 / 第 1 页 / U1 AXP2101 的 LX/BLDO/DLDO/ALDO/VRTC 输出

### AXP2101 按键、充电灯与唤醒

U1 PWROK 输出 AXP_PG、PWRON 接 PWR_KEY、IRQ 输出 AXP_WAKEUP；S1/S2 分别经 R38/R39 510Ω把 AXP_PG/PWR_KEY 按下接地，CHGLED 驱动 AXP_CHG_LED 与红色 LED1，AXP_WAKEUP 由 R15 10K 上拉到 RTC_VDD。

- 参数与网络：`power_good=AXP_PG`；`power_key=PWR_KEY`；`irq=AXP_WAKEUP`；`button_s1=AXP_PG via R38 510R`；`button_s2=PWR_KEY via R39 510R`；`charge_led=AXP_CHG_LED -> LED1 red`；`irq_pullup=R15 10K to RTC_VDD`
- 证据：图 de85c198f634 / 第 1 页 / 网格 C1-D4，PWROK/PWRON/IRQ/CHGLED 与 S1/S2/LED1

### SY7088 BUS_5V 升压

U3 SY7088 从 AXP_PS 取电，经 L5 WPN3012H2R2MT 产生 BUS_5V，反馈分压为 R11 15K/R12 4.7K；BOOST_EN 经 R13 47Ω接 EN，R14 10K 下拉并配 C29 1uF。

- 参数与网络：`converter=U3 SY7088`；`input=AXP_PS`；`inductor=L5 WPN3012H2R2MT`；`output=BUS_5V`；`feedback=R11 15K,R12 4.7K`；`enable=BOOST_EN via R13 47R`；`enable_rc=R14 10K,C29 1uF`
- 证据：图 674d725f5dc6 / 第 1 页 / 网格 B1-C2，U3 SY7088 Boost 区

### BUS_OUT、VUSB 与 VBUS 双向控制

U14 ME1502AM5G 在 BUS_OUT_EN 高时把 BUS_5V 送到 BUS_OUT，U17 在 USB_OTG_EN 高时把 BUS_OUT 送到 VUSB；U19 ME1502CM5G 在 BUS_OUT_EN 低时把 BUS_OUT 送到 VBUS，U18 在 USB_OTG_EN 低时把 VUSB 送到 VBUS。

- 参数与网络：`boost_path=BUS_5V -> U14 -> BUS_OUT, BUS_OUT_EN high`；`otg_path=BUS_OUT -> U17 -> VUSB, USB_OTG_EN high`；`pmu_path=BUS_OUT -> U19 -> VBUS, BUS_OUT_EN low`；`usb_input_path=VUSB -> U18 -> VBUS, USB_OTG_EN low`；`high_enable_switch=ME1502AM5G`；`low_enable_switch=ME1502CM5G`
- 证据：图 97e9cd876f18 / 第 1 页 / Boost/OTG/USB/PMU 四个箭头与 U14/U17/U18/U19

## 接口

### USB Type-C 与 USB 2.0 信号

J1 USB-TYPEC 的 CC1/CC2 各经 R6/R9 5.1K 接地，USB_D_P/USB_D_N 由 D4/D6 ESD5Z3V3 对地保护，并经 R47/R25 各 22Ω接 USB_DU_P/USB_DU_N；VCC 接 VUSB。

- 参数与网络：`connector=J1 USB-TYPEC`；`vbus=VUSB`；`cc1=R6 5.1K to GND`；`cc2=R9 5.1K to GND`；`d_plus=USB_D_P via R47 22R to USB_DU_P`；`d_minus=USB_D_N via R25 22R to USB_DU_N`；`esd=D4/D6 ESD5Z3V3`
- 证据：图 674d725f5dc6 / 第 1 页 / 网格 A3-B4，J1 USB-TYPEC

### 摄像头/传感子板接口

J2 24-pin 接口承载 CAM_D2-D9、CAM_PCLK、CAM_VSYNC、CAM_HREF、CAM_RST、CAM_PWDN、CAM_MCLK、I2C_SYS_SDA/SCL，以及 AVDD、DVDD、VDDCAM_3V3 和 GND；CAM_MCLK 经 R31 51Ω连接 X2 20MHz 输出。

- 参数与网络：`connector=J2 AFC34-S24FIA-00`；`pixel_data=CAM_D2-D9`；`sync=CAM_PCLK,CAM_VSYNC,CAM_HREF`；`control=CAM_RST,CAM_PWDN`；`bus=I2C_SYS_SDA/SCL`；`clock=CAM_MCLK via R31 51R from X2`；`supplies=AVDD,DVDD,VDDCAM_3V3`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 A1-B2，J2 与 X2

### LCD 与触摸连接器

LCD1 连接 SPI_MOSI、SPI_SCK、LCD_CS、LCD_RST、SPI_MISO、VDD_3V3、VCC_BL 与 GND；CTP1 pins1-6 依次为 VDD_3V3、GND、I2C_SYS_SDA、I2C_SYS_SCL、TOUCH_INT、TOUCH_RST，pins7/8 未连接。

- 参数与网络：`lcd=LCD1 M5_LCD_10P`；`lcd_signals=SPI_MOSI,SPI_SCK,LCD_CS,LCD_RST,SPI_MISO`；`lcd_power=VDD_3V3,VCC_BL,GND`；`touch=CTP1 M5_TOUCH_8P`；`touch_bus=I2C_SYS_SDA/SCL`；`touch_control=TOUCH_INT,TOUCH_RST`；`touch_nc=pins7/8`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 C4-D4，LCD1/CTP1

### 30 针 M5-BUS

BUS1 pins1-10 为 GND/BUS_ADC1、GND/BUS_PB_IN、GND/AXP_PG、SPI_MOSI/BUS_G5、SPI_MISO/BUS_PB_OUT；pins11-20 为 SPI_SCK/VCC_3V3、BUS_U0RXD/BUS_U0TXD、BUS_PC_RX/BUS_PC_TX、I2C_SYS_SDA/SCL、BUS_PA_SDA/SCL；pins21-30 为 BUS_G6/G7、I2S_DATO/ESP_BOOT、NC/I2S_DATI、NC/BUS_OUT、NC/VBAT。

- 参数与网络：`pins_1_10=1 GND,2 BUS_ADC1,3 GND,4 BUS_PB_IN,5 GND,6 AXP_PG,7 SPI_MOSI,8 BUS_G5,9 SPI_MISO,10 BUS_PB_OUT`；`pins_11_20=11 SPI_SCK,12 VCC_3V3,13 BUS_U0RXD,14 BUS_U0TXD,15 BUS_PC_RX,16 BUS_PC_TX,17 I2C_SYS_SDA,18 I2C_SYS_SCL,19 BUS_PA_SDA,20 BUS_PA_SCL`；`pins_21_30=21 BUS_G6,22 BUS_G7,23 I2S_DATO,24 ESP_BOOT,25 NC,26 I2S_DATI,27 NC,28 BUS_OUT,29 NC,30 VBAT`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 C1-D2，BUS1 M5.BUS

### Grove Port.A

J3 GH2.0-4P pins1-4 依次连接 BUS_PA_SCL、BUS_PA_SDA、BUS_OUT、GND；U5 将 BUS_PA_SCL/SDA 映射到 GPIO1/GPIO2。

- 参数与网络：`connector=J3 GH2.0-4P`；`pin1=BUS_PA_SCL/GPIO1`；`pin2=BUS_PA_SDA/GPIO2`；`pin3=BUS_OUT`；`pin4=GND`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 D1-D2，J3; 图 8f2f5466da03 / 第 1 页 / U5 GPIO1/GPIO2 BUS_PA_SCL/SDA

## 总线

### 内部 I2C 总线

U5 GPIO12/GPIO11 分别连接 I2C_SYS_SDA/I2C_SYS_SCL，R20/R32 各 2.2K 上拉到 VDD_3V3；AXP2101、BM8563、AW88298、ES7210、AW9523B 和 BMI270 均接入这组网络。

- 参数与网络：`sda=GPIO12/I2C_SYS_SDA`；`scl=GPIO11/I2C_SYS_SCL`；`pullups=R20/R32 2.2K to VDD_3V3`；`devices=AXP2101,BM8563,AW88298,ES7210,AW9523B,BMI270`
- 证据：图 8f2f5466da03 / 第 1 页 / U5 GPIO11/12 与 R20/R32; 图 de85c198f634 / 第 1 页 / AXP2101 SDA/SCL; 图 f7f0dc3f29b1 / 第 1 页 / AW88298/ES7210 SDA/SCL; 图 12e215412fd9 / 第 1 页 / AW9523B SDA/SCL; 图 95d654aa1d79 / 第 1 页 / BMI270 SDA/SCL

## 总线地址

### 原理图明确标注的 I2C 地址

页面明确标注 U1 AXP2101=0x34、U8 AW88298=0x36、U9 ES7210=0x40、U10 AW9523B=0x58、U15 BMI270=0x69，均为 7-bit 地址。

- 参数与网络：`AXP2101=0x34`；`AW88298=0x36`；`ES7210=0x40`；`AW9523B=0x58`；`BMI270=0x69`
- 证据：图 de85c198f634 / 第 1 页 / U1 上方 I2C ADDR(7bit):0x34; 图 f7f0dc3f29b1 / 第 1 页 / U8/U9 上方 0x36/0x40; 图 12e215412fd9 / 第 1 页 / U10 上方 0x58; 图 95d654aa1d79 / 第 1 页 / U15 SA0 上拉和 SDO=VDDIO 0x69 注释

## GPIO 与控制信号

### AW9523B 控制信号映射

U10 P0_0-P0_5 依次连接 TOUCH_RST、BUS_OUT_EN、AW_RST、ES_INT、TF_SW、USB_OTG_EN；P1_0-P1_3 依次连接 CAM_RST、LCD_RST、TOUCH_INT、AW_INT，P1_7 连接 BOOST_EN，RSTN 接 AXP_PG，INTN 输出 I2C_INT。

- 参数与网络：`p0_0=TOUCH_RST`；`p0_1=BUS_OUT_EN`；`p0_2=AW_RST`；`p0_3=ES_INT`；`p0_4=TF_SW`；`p0_5=USB_OTG_EN`；`p1_0=CAM_RST`；`p1_1=LCD_RST`；`p1_2=TOUCH_INT`；`p1_3=AW_INT`；`p1_7=BOOST_EN`；`reset=AXP_PG`；`interrupt=I2C_INT`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 A3-B4，U10 AW9523B 全部已用 IO

## 时钟

### ESP32-S3 40MHz 晶振

X1 标注 40MHz/10ppm/20pF/2520，连接 XTAL_40M_P/N；R33 22nH 位于 P 端，C44/C51 各 12pF 接地。

- 参数与网络：`reference=X1`；`frequency=40MHz`；`tolerance=10ppm`；`load_annotation=20pF`；`package=2520`；`series=R33 22nH`；`capacitors=C44/C51 12pF`
- 证据：图 8f2f5466da03 / 第 1 页 / 网格 C1-D2，X1/R33/C44/C51

### BM8563 RTC 与唤醒

U4 BM8563 的 SCL/SDA 接 I2C_SYS_SCL/SDA，INT 接 AXP_WAKEUP，VDD 接 RTC_VDD；Y1 接 OSCI/OSCO，C30/C32 各 6pF，BAT1 标 NC。

- 参数与网络：`rtc=U4 BM8563`；`bus=I2C_SYS`；`interrupt=AXP_WAKEUP`；`supply=RTC_VDD`；`crystal=Y1 TXC/9H0320`；`load_capacitors=C30/C32 6pF`；`backup=BAT1/NC`
- 证据：图 674d725f5dc6 / 第 1 页 / 网格 C1-D3，U4 BM8563

### 摄像头 20MHz 时钟

X2 标注 20MHz ±25ppm 3.3V，输出 CAM_MCLK，并经 R31 51Ω送到 J2 pin12。

- 参数与网络：`reference=X2`；`frequency=20MHz`；`tolerance=±25ppm`；`supply=VDDCAM_3V3`；`output=CAM_MCLK`；`series=R31 51R`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 A2-B2，X2 与 CAM_MCLK

## 复位

### LMV331 ESP_BOOT 控制

U2 LMV331 由 VDD_3V3 供电，输出 ESP_BOOT 并由 R4 10K 上拉；AXP_PG 经 D3/R5 和 RC/二极管网络进入比较器输入，LED2 GREEN 与 R10 2K 连接 ESP_BOOT。

- 参数与网络：`comparator=U2 LMV331`；`output=ESP_BOOT`；`pullup=R4 10K to VDD_3V3`；`source=AXP_PG via D3/R5`；`indicator=LED2 GREEN,R10 2K`
- 证据：图 674d725f5dc6 / 第 1 页 / 网格 A1-B3，AXP_PG/LMV331/ESP_BOOT 区

## 存储

### 128Mbit 外部 Flash

U6 标注 GD25Q128/W25Q128/128Mbit/3.3V，nCS/CLK/DI/DO/nWP/nHOLD 分别连接 FLASH_CS0、FLASH_CLK、FLASH_D、FLASH_Q、FLASH_WP、FLASH_HD。

- 参数与网络：`reference=U6`；`part_number=GD25Q128/W25Q128`；`capacity_bits=128Mbit`；`supply=FLASH_VCC 3.3V`；`cs=FLASH_CS0`；`clock=FLASH_CLK`；`io=FLASH_D/Q/WP/HD`
- 证据：图 8f2f5466da03 / 第 1 页 / 网格 A3-B4，U6 Flash

### microSD SPI 接口

U11 MicroSD-SPI 的 CS、DI、SCLK、DO 分别接 TF_CS、SPI_MOSI、SPI_SCK、SPI_MISO，VDD 接 VDD_3V3_SD；卡检测 SW 输出 TF_SW 并由 R28 10K 上拉到 VDD_3V3。

- 参数与网络：`slot=U11 MicroSD-SPI`；`cs=TF_CS/GPIO4`；`mosi=SPI_MOSI/GPIO37`；`clock=SPI_SCK/GPIO36`；`miso=SPI_MISO/GPIO35`；`supply=VDD_3V3_SD`；`card_detect=TF_SW,R28 10K pullup`
- 证据：图 12e215412fd9 / 第 1 页 / 网格 C2-D3，U11 MicroSD-SPI; 图 8f2f5466da03 / 第 1 页 / U5 GPIO4/35/36/37 映射

## 内存与 Flash

### 外部 PSRAM 连接

U7 EPSRAM 使用 FLASH_CS1 片选、FLASH_CLK 时钟和 FLASH_D/Q/WP/HD 四条数据网络，VDD 接 FLASH_VCC。

- 参数与网络：`reference=U7`；`label=EPSRAM`；`cs=FLASH_CS1`；`clock=FLASH_CLK`；`io0=FLASH_D`；`io1=FLASH_Q`；`io2=FLASH_WP`；`io3=FLASH_HD`；`supply=FLASH_VCC`
- 证据：图 8f2f5466da03 / 第 1 页 / 网格 B3，U7 EPSRAM

## 音频

### AW88298 I2S 功放

U8 AW88298 的 SDA/SCL 接内部 I2C，BCK/WCK/DATAI 接 I2S_BCK/I2S_WCK/I2S_DATO，AW_RST/AW_INT 为复位和中断；VOP/VON 经 FB2/FB1 输出 SPK_VOP/SPK_VON。

- 参数与网络：`device=U8 AW88298`；`address=0x36`；`i2s_bck=I2S_BCK`；`i2s_wck=I2S_WCK`；`i2s_data=I2S_DATO`；`reset=AW_RST`；`interrupt=AW_INT`；`outputs=SPK_VOP,SPK_VON`
- 证据：图 f7f0dc3f29b1 / 第 1 页 / 网格 A1-B2，U8 AW88298

### ES7210 双麦克风采集

U9 ES7210 MCLK 经 R34 51Ω接 ESP_BOOT，SCLK/LRCK/SDOUT1 接 I2S_BCK/I2S_WCK/I2S_DATI；U12/U13 麦克风由 VBIAS_MIC 供电，分别经 C88/C91 和 C93/C96 接 MIC1_P/N、MIC2_P/N。

- 参数与网络：`codec=U9 ES7210`；`address=0x40`；`mclk=ESP_BOOT via R34 51R`；`bck=I2S_BCK`；`word_clock=I2S_WCK`；`data_out=I2S_DATI`；`microphones=U12/U13 MSM381A3729H9BPC`；`inputs=MIC1_P/N,MIC2_P/N`
- 证据：图 f7f0dc3f29b1 / 第 1 页 / 网格 C1-D4，U9/U12/U13

### 扬声器 AEC 回采

SPK_VOP/SPK_VON 分别经 R40/R42 150K 和 C102/C104 耦合到 AEC_P/AEC_N，AEC_P/N 接 ES7210 MIC3P/MIC3N；C103/C105 各 22pF 对地，R41/R43 标 NC。

- 参数与网络：`positive=SPK_VOP -> R40 150K/C102 -> AEC_P`；`negative=SPK_VON -> R42 150K/C104 -> AEC_N`；`codec_inputs=ES7210 MIC3P/MIC3N`；`shunt_caps=C103/C105 22pF`；`optional=R41/R43 NC`
- 证据：图 f7f0dc3f29b1 / 第 1 页 / 网格 B2-C3，AEC_P/N 回采网络

## 传感器

### BMI270 与 BMM150 传感器 Hub

U15 BMI270 通过 I2C_SYS_SDA/SCL 接主控，SDO/SA0 由 R50 2.2K 上拉到 VDD_3V3，配置地址 0x69；ASDX/ASCX 输出 BMM_SDA/BMM_SCL 到 U20 BMM150，BMM150 的 CSB 与 SDO 接地并由 3.3V 供电。

- 参数与网络：`imu=U15 BMI270 0x69`；`primary_bus=I2C_SYS_SDA/SCL`；`sa0=R50 2.2K to VDD_3V3`；`aux_sda=ASDX/BMM_SDA`；`aux_scl=ASCX/BMM_SCL`；`magnetometer=U20 BMM150`；`bmm_csb=GND`；`bmm_sdo=GND`；`supply=VDD_3V3`
- 证据：图 95d654aa1d79 / 第 1 页 / U15 BMI270 与 U20 BMM150 完整连接

## 射频

### ESP32-S3 天线与 IPEX 选路

ESP_LNA 经 C68、C69/C86 匹配网络和 R35 0Ω连接 ANT1 PROANT440；R36、L9、C121 标 NC，J4 IPEX 为未装配备用路径。

- 参数与网络：`source=ESP_LNA`；`series=C68 1.8nH`；`shunt=C69 2.7pF,C86 2.4pF`；`installed_path=R35 0R -> ANT1 PROANT440`；`alternate=R36/L9/C121 NC -> J4 IPEX`
- 证据：图 8f2f5466da03 / 第 1 页 / 网格 D1-D3，ESP_LNA/ANT1/J4 匹配网络

## 调试与烧录

### ESP32-S3 原生 USB

U5 GPIO19/GPIO20 分别连接 USB_DU_N/USB_DU_P，再经 22Ω串联电阻到 J1 USB D-/D+，形成 ESP32-S3 原生 USB 数据路径。

- 参数与网络：`usb_dm_gpio=GPIO19/USB_DU_N`；`usb_dp_gpio=GPIO20/USB_DU_P`；`connector_dm=J1 USB_D_N`；`connector_dp=J1 USB_D_P`；`series=R25/R47 22R`
- 证据：图 8f2f5466da03 / 第 1 页 / U5 GPIO19/GPIO20 USB_DU_N/P; 图 674d725f5dc6 / 第 1 页 / R25/R47 到 J1 USB D-/D+

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 七页 CoreS3 v1.0 主板架构 | `controller=U5 ESP32-S3`；`power=U1 AXP2101`；`memory=U6 128Mbit Flash,U7 EPSRAM`；`audio=U8 AW88298,U9 ES7210,U12/U13`；`sensors=U15 BMI270,U20 BMM150`；`expander=U10 AW9523B`；`interfaces=USB-C,LCD,Touch,Camera,microSD,M5.BUS` |
| 总线地址 | 原理图明确标注的 I2C 地址 | `AXP2101=0x34`；`AW88298=0x36`；`ES7210=0x40`；`AW9523B=0x58`；`BMI270=0x69` |
| 电源 | AXP2101 电源轨 | `dcdc1=VDD_3V3`；`dcdc3=VCC_3V3`；`bldo1=AVDD`；`bldo2=DVDD`；`dldo1=VCC_BL`；`rtc=RTC_VDD`；`aldo1=VDD_1V8`；`aldo2=VDDA_3V3`；`aldo3=VDDCAM_3V3`；`aldo4=VDD_3V3_SD` |
| 电源 | AXP2101 按键、充电灯与唤醒 | `power_good=AXP_PG`；`power_key=PWR_KEY`；`irq=AXP_WAKEUP`；`button_s1=AXP_PG via R38 510R`；`button_s2=PWR_KEY via R39 510R`；`charge_led=AXP_CHG_LED -> LED1 red`；`irq_pullup=R15 10K to RTC_VDD` |
| 电源 | SY7088 BUS_5V 升压 | `converter=U3 SY7088`；`input=AXP_PS`；`inductor=L5 WPN3012H2R2MT`；`output=BUS_5V`；`feedback=R11 15K,R12 4.7K`；`enable=BOOST_EN via R13 47R`；`enable_rc=R14 10K,C29 1uF` |
| 电源 | BUS_OUT、VUSB 与 VBUS 双向控制 | `boost_path=BUS_5V -> U14 -> BUS_OUT, BUS_OUT_EN high`；`otg_path=BUS_OUT -> U17 -> VUSB, USB_OTG_EN high`；`pmu_path=BUS_OUT -> U19 -> VBUS, BUS_OUT_EN low`；`usb_input_path=VUSB -> U18 -> VBUS, USB_OTG_EN low`；`high_enable_switch=ME1502AM5G`；`low_enable_switch=ME1502CM5G` |
| 接口 | USB Type-C 与 USB 2.0 信号 | `connector=J1 USB-TYPEC`；`vbus=VUSB`；`cc1=R6 5.1K to GND`；`cc2=R9 5.1K to GND`；`d_plus=USB_D_P via R47 22R to USB_DU_P`；`d_minus=USB_D_N via R25 22R to USB_DU_N`；`esd=D4/D6 ESD5Z3V3` |
| 调试与烧录 | ESP32-S3 原生 USB | `usb_dm_gpio=GPIO19/USB_DU_N`；`usb_dp_gpio=GPIO20/USB_DU_P`；`connector_dm=J1 USB_D_N`；`connector_dp=J1 USB_D_P`；`series=R25/R47 22R` |
| 复位 | LMV331 ESP_BOOT 控制 | `comparator=U2 LMV331`；`output=ESP_BOOT`；`pullup=R4 10K to VDD_3V3`；`source=AXP_PG via D3/R5`；`indicator=LED2 GREEN,R10 2K` |
| 存储 | 128Mbit 外部 Flash | `reference=U6`；`part_number=GD25Q128/W25Q128`；`capacity_bits=128Mbit`；`supply=FLASH_VCC 3.3V`；`cs=FLASH_CS0`；`clock=FLASH_CLK`；`io=FLASH_D/Q/WP/HD` |
| 内存与 Flash | 外部 PSRAM 连接 | `reference=U7`；`label=EPSRAM`；`cs=FLASH_CS1`；`clock=FLASH_CLK`；`io0=FLASH_D`；`io1=FLASH_Q`；`io2=FLASH_WP`；`io3=FLASH_HD`；`supply=FLASH_VCC` |
| 时钟 | ESP32-S3 40MHz 晶振 | `reference=X1`；`frequency=40MHz`；`tolerance=10ppm`；`load_annotation=20pF`；`package=2520`；`series=R33 22nH`；`capacitors=C44/C51 12pF` |
| 射频 | ESP32-S3 天线与 IPEX 选路 | `source=ESP_LNA`；`series=C68 1.8nH`；`shunt=C69 2.7pF,C86 2.4pF`；`installed_path=R35 0R -> ANT1 PROANT440`；`alternate=R36/L9/C121 NC -> J4 IPEX` |
| 总线 | 内部 I2C 总线 | `sda=GPIO12/I2C_SYS_SDA`；`scl=GPIO11/I2C_SYS_SCL`；`pullups=R20/R32 2.2K to VDD_3V3`；`devices=AXP2101,BM8563,AW88298,ES7210,AW9523B,BMI270` |
| 时钟 | BM8563 RTC 与唤醒 | `rtc=U4 BM8563`；`bus=I2C_SYS`；`interrupt=AXP_WAKEUP`；`supply=RTC_VDD`；`crystal=Y1 TXC/9H0320`；`load_capacitors=C30/C32 6pF`；`backup=BAT1/NC` |
| 音频 | AW88298 I2S 功放 | `device=U8 AW88298`；`address=0x36`；`i2s_bck=I2S_BCK`；`i2s_wck=I2S_WCK`；`i2s_data=I2S_DATO`；`reset=AW_RST`；`interrupt=AW_INT`；`outputs=SPK_VOP,SPK_VON` |
| 音频 | ES7210 双麦克风采集 | `codec=U9 ES7210`；`address=0x40`；`mclk=ESP_BOOT via R34 51R`；`bck=I2S_BCK`；`word_clock=I2S_WCK`；`data_out=I2S_DATI`；`microphones=U12/U13 MSM381A3729H9BPC`；`inputs=MIC1_P/N,MIC2_P/N` |
| 音频 | 扬声器 AEC 回采 | `positive=SPK_VOP -> R40 150K/C102 -> AEC_P`；`negative=SPK_VON -> R42 150K/C104 -> AEC_N`；`codec_inputs=ES7210 MIC3P/MIC3N`；`shunt_caps=C103/C105 22pF`；`optional=R41/R43 NC` |
| GPIO 与控制信号 | AW9523B 控制信号映射 | `p0_0=TOUCH_RST`；`p0_1=BUS_OUT_EN`；`p0_2=AW_RST`；`p0_3=ES_INT`；`p0_4=TF_SW`；`p0_5=USB_OTG_EN`；`p1_0=CAM_RST`；`p1_1=LCD_RST`；`p1_2=TOUCH_INT`；`p1_3=AW_INT`；`p1_7=BOOST_EN`；`reset=AXP_PG`；`interrupt=I2C_INT` |
| 接口 | 摄像头/传感子板接口 | `connector=J2 AFC34-S24FIA-00`；`pixel_data=CAM_D2-D9`；`sync=CAM_PCLK,CAM_VSYNC,CAM_HREF`；`control=CAM_RST,CAM_PWDN`；`bus=I2C_SYS_SDA/SCL`；`clock=CAM_MCLK via R31 51R from X2`；`supplies=AVDD,DVDD,VDDCAM_3V3` |
| 时钟 | 摄像头 20MHz 时钟 | `reference=X2`；`frequency=20MHz`；`tolerance=±25ppm`；`supply=VDDCAM_3V3`；`output=CAM_MCLK`；`series=R31 51R` |
| 接口 | LCD 与触摸连接器 | `lcd=LCD1 M5_LCD_10P`；`lcd_signals=SPI_MOSI,SPI_SCK,LCD_CS,LCD_RST,SPI_MISO`；`lcd_power=VDD_3V3,VCC_BL,GND`；`touch=CTP1 M5_TOUCH_8P`；`touch_bus=I2C_SYS_SDA/SCL`；`touch_control=TOUCH_INT,TOUCH_RST`；`touch_nc=pins7/8` |
| 存储 | microSD SPI 接口 | `slot=U11 MicroSD-SPI`；`cs=TF_CS/GPIO4`；`mosi=SPI_MOSI/GPIO37`；`clock=SPI_SCK/GPIO36`；`miso=SPI_MISO/GPIO35`；`supply=VDD_3V3_SD`；`card_detect=TF_SW,R28 10K pullup` |
| 接口 | 30 针 M5-BUS | `pins_1_10=1 GND,2 BUS_ADC1,3 GND,4 BUS_PB_IN,5 GND,6 AXP_PG,7 SPI_MOSI,8 BUS_G5,9 SPI_MISO,10 BUS_PB_OUT`；`pins_11_20=11 SPI_SCK,12 VCC_3V3,13 BUS_U0RXD,14 BUS_U0TXD,15 BUS_PC_RX,16 BUS_PC_TX,17 I2C_SYS_SDA,18 I2C_SYS_SCL,19 BUS_PA_SDA,20 BUS_PA_SCL`；`pins_21_30=21 BUS_G6,22 BUS_G7,23 I2S_DATO,24 ESP_BOOT,25 NC,26 I2S_DATI,27 NC,28 BUS_OUT,29 NC,30 VBAT` |
| 接口 | Grove Port.A | `connector=J3 GH2.0-4P`；`pin1=BUS_PA_SCL/GPIO1`；`pin2=BUS_PA_SDA/GPIO2`；`pin3=BUS_OUT`；`pin4=GND` |
| 传感器 | BMI270 与 BMM150 传感器 Hub | `imu=U15 BMI270 0x69`；`primary_bus=I2C_SYS_SDA/SCL`；`sa0=R50 2.2K to VDD_3V3`；`aux_sda=ASDX/BMM_SDA`；`aux_scl=ASCX/BMM_SCL`；`magnetometer=U20 BMM150`；`bmm_csb=GND`；`bmm_sdo=GND`；`supply=VDD_3V3` |
| 系统结构 | CoreS3 v1.0 图与 StackChan Core 对应关系 | `product=StackChan Core`；`sku=C156`；`resource_name=Sch_M5_CoreS3_v1.0`；`documented_equivalence=CoreS3/CoreS3-Lite hardware function identical`；`documented_firmware=StackChan preinstalled`；`stackchan_bom=null` |
| 总线 | AXP2101 I2C 反接注记 | `device=U1 AXP2101`；`sda=I2C_SYS_SDA`；`scl=I2C_SYS_SCL`；`annotation=I2C NEED REVERSED`；`resolution=null` |
| 内存与 Flash | StackChan Core 8MB PSRAM | `documented_capacity=8MB`；`schematic_label=U7 EPSRAM`；`part_number=null`；`capacity=null`；`frequency=null`；`package=null` |
| 核心器件 | ILI9342C 显示与电容触摸子板 | `documented_lcd=ILI9342C 2.0 inch 320x240`；`documented_touch=capacitive touch`；`documented_glass=high-strength glass`；`schematic_lcd=LCD1 connector`；`schematic_touch=CTP1 connector`；`subboard_bom=null` |
| 传感器 | GC0308 与 LTR-553ALS-WA 子板器件 | `documented_camera=GC0308 0.3MP`；`documented_proximity=LTR-553ALS-WA`；`schematic=J2 connector only`；`subboard_bom=null` |
| 音频 | AW88298 配套 1W 扬声器 | `documented_power=1W`；`documented_format=16-bit I2S`；`amplifier=U8 AW88298`；`output=SPK_VOP/SPK_VON`；`speaker_part=null`；`impedance=null`；`connector=null` |
| 系统结构 | ESP32-S3 性能与无线规格 | `documented_cpu=dual-core Xtensa LX7 240MHz`；`documented_radio=2.4GHz Wi-Fi and BLE`；`schematic_soc=U5 ESP32-S3`；`schematic_rf=ANT1 PROANT440 path` |

## 待确认事项

- `system.stackchan-resource-applicability`：产品源文档声明 StackChan Core、CoreS3 与 CoreS3-Lite 仅外观不同且硬件功能相同，并说明 StackChan Core 预置 StackChan 固件；七页资源均名为 Sch_M5_CoreS3_v1.0，页面没有 StackChan Core、C156、外观版本或固件标识，量产 BOM 与固件对应关系需确认。（证据：图 de85c198f634 / 第 1 页 / AXP2101 页无 StackChan Core/C156 标识; 图 12e215412fd9 / 第 1 页 / 接口页无 StackChan Core/C156 或固件标识）
- `bus.axp-i2c-reversed-note`：AXP2101 SDA/SCL 分别连接 I2C_SYS_SDA/I2C_SYS_SCL，但两脚旁保留红字 I2C NEED REVERSED，无法仅据页面判断该注记是已处理说明还是当前连线待修订项。（证据：图 de85c198f634 / 第 1 页 / U1 pins39/40 SDA/SCL 旁红字 I2C NEED REVERSED）
- `memory.documented-8mb-psram`：产品源文档标注 8MB PSRAM；原理图 U7 只标 EPSRAM 并显示共享 SPI 网络，没有器件型号、容量、工作频率或封装，C156 量产 PSRAM 需确认。（证据：图 8f2f5466da03 / 第 1 页 / U7 EPSRAM，无型号/容量）
- `component.documented-display-touch`：产品源文档标注 2.0 英寸 320x240 ILI9342C 高强度玻璃电容触摸屏；主板图只给 LCD1 与 CTP1 连接器和网络，没有显示控制器、触摸芯片、分辨率或玻璃参数。（证据：图 12e215412fd9 / 第 1 页 / LCD1/CTP1 仅为连接器，无控制芯片）
- `sensor.documented-camera-proximity`：产品源文档标注 GC0308 0.3MP 摄像头和 LTR-553ALS-WA 接近/环境光传感器；主板图仅给 J2 摄像头/传感子板接口，没有这两个器件、地址选择、像素或光学参数。（证据：图 12e215412fd9 / 第 1 页 / J2 24-pin 接口，无 GC0308/LTR-553ALS-WA 器件）
- `audio.documented-1w-speaker`：产品源文档标注 AW88298 16-bit I2S 功放和 1W 扬声器；音频页只显示功放与 SPK_VOP/SPK_VON 网络，没有扬声器器件、连接器、阻抗或额定功率。（证据：图 f7f0dc3f29b1 / 第 1 页 / U8 输出终止于 SPK_VOP/VON 网络，无扬声器器件）
- `system.documented-performance-radio`：产品源文档标注双核 Xtensa LX7 240MHz、2.4GHz Wi-Fi 与 BLE；原理图确认 U5 ESP32-S3 和板载天线链路，但未直接标注 CPU 主频、协议、频段或射频性能。（证据：图 8f2f5466da03 / 第 1 页 / U5 ESP32-S3 与 ESP_LNA/ANT1 射频链路）
- `review.stackchan-resource`：请提供 StackChan Core/C156 的正式 BOM、外观差异记录和固件版本，确认 CoreS3 v1.0 七页资源的完整适用范围。；原因：资源没有 StackChan Core/C156 或固件标识，硬件等价与预置固件来自产品源文档。
- `review.axp-i2c-reversed`：AXP2101 页面的 I2C NEED REVERSED 是已处理的历史注记，还是表示当前 SDA/SCL 网络仍需交换？；原因：红字注记与当前 I2C_SYS_SDA/SCL 连线同时存在。
- `review.psram`：请确认 StackChan Core 8MB PSRAM 的料号、容量、频率和封装。；原因：U7 只标 EPSRAM。
- `review.display-touch`：请提供 StackChan Core LCD/触摸子板原理图或 BOM，确认 ILI9342C、面板分辨率、触摸芯片与玻璃参数。；原因：主板页只有 LCD1/CTP1 连接器。
- `review.camera-proximity`：请提供 StackChan Core 摄像头/接近传感子板原理图或 BOM，确认 GC0308、LTR-553ALS-WA 与 0.3MP 参数。；原因：主板页只有 J2 接口。
- `review.speaker`：请确认 StackChan Core 1W 扬声器料号、阻抗、连接器及 AW88298 输出匹配参数。；原因：音频页没有扬声器器件。
- `review.performance-radio`：StackChan Core 量产配置是否确认为双核 LX7 240MHz、2.4GHz Wi-Fi 与 BLE，射频认证参数是什么？；原因：原理图只显示 ESP32-S3 与天线链路，未直接标性能和无线协议参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `de85c198f6340569fcb9880840cb6d621959f85ca828bac072b6027148c6dbc7` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_01.png` |
| 2 | 1 | `674d725f5dc6e794929e90b12382509383d1288daa1c072076dfb5dfcc3880b3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_02.png` |
| 3 | 1 | `8f2f5466da03500bf49e2ad964b43197786bf9dc5c6df50fb5163b31587e67eb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_03.png` |
| 4 | 1 | `f7f0dc3f29b13b37133d50f1f10161c4279e0d32cccd48127e770ab59d006060` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_04.png` |
| 5 | 1 | `12e215412fd96b2d51e3979a012840b5eab11d88da6427b3e85411d98d05908c` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_05.png` |
| 6 | 1 | `97e9cd876f18a199c947ff69bb91418d59d48a2f508fc54ccfd1c053bc60ecb4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_06.png` |
| 7 | 1 | `95d654aa1d7999f926432f23a42b5414b0f342edfeb1a8a7dfec078025224d5a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/Sch_M5_CoreS3_v1.0_page_07.png` |

---

源文档：`zh_CN/core/StackChan_Core.md`

源文档 SHA-256：`4219bf660ed0a7474c4d5c7e45fedf437a19ecc18bcfe8953d47c6b0dee52f0f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
