# StackChan 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | StackChan |
| SKU | K151 |
| 产品 ID | `stackchan-4ab98aca5f72` |
| 源文档 | `zh_CN/StackChan.md` |

## 概述

StackChan/K151 的 11 个原理图资源覆盖完整整机：前 7 页为 CoreS3 v1.0 主机，以 ESP32-S3、AXP2101、128Mbit Flash、外部 PSRAM、USB、音频、显示/触摸/摄像头、microSD 和 BMI270+BMM150 为核心；后 4 页为 Adapter、Power、Ring、Touch 身体板，包含电池保护、TPS61088 舵机 5V、电池监测、半双工舵机总线、双 USB-C、红外、12 颗 RGB、三点触摸和 ST25R3916 NFC。原理图明确多组 I2C 地址和主机到身体的信号映射；容量、舵机机械性能、部分子板器件、无线/声学性能、固件功能及量产版本仍需 BOM、子板图或测试确认。

## 检索关键词

`StackChan`、`K151`、`K151-R`、`CoreS3`、`ESP32-S3`、`AXP2101`、`0x34`、`GD25Q128`、`W25Q128`、`128Mbit Flash`、`EPSRAM`、`AW88298`、`0x36`、`ES7210`、`0x40`、`AW9523B`、`0x58`、`BMI270`、`0x69`、`BMM150`、`BM8563`、`USB Type-C`、`microSD`、`M5_BUS`、`Adapter`、`Power`、`Ring`、`Touch`、`FH9261-G3JZ`、`TPS61088`、`Servo_SIG`、`Servo_TX`、`Servo_RX`、`INA226AIDGSR`、`0x41`、`PY32IO_EXP`、`0x6F`、`0x71`、`IRM-56384`、`IR_SEND`、`IR_REC`、`WS2812C`、`RGB`、`Si12T`、`0x68`、`ST25R3916`、`0x50`、`ANT_NFC`、`550mAh`、`SCS0009`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 (Core p1) | AXP2101 | 主机电源管理器，地址 0x34，管理 VBUS/VBAT 与多路系统电源 | 图 de85c198f634 / 第 1 页 / CoreS3 第1资源页 U1 AXP2101 |
| U5 | ESP32-S3 | StackChan 主机主控，连接存储、USB、摄像头、音频、总线和射频 | 图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 U5 ESP32-S3 |
| U6/U7 | GD25Q128/W25Q128 128Mbit / EPSRAM | ESP32-S3 外部 QSPI Flash 与 PSRAM | 图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 U6 Flash 与 U7 EPSRAM |
| U3 (Core p2) | SY7088 | AXP_PS 至 BUS_5V 升压转换器 | 图 674d725f5dc6 / 第 1 页 / CoreS3 第2资源页 U3 SY7088 |
| U4 | BM8563 | RTC_VDD 供电的 I2C 实时时钟 | 图 674d725f5dc6 / 第 1 页 / CoreS3 第2资源页 U4 BM8563 |
| U8 | AW88298 | 地址 0x36 的 I2C/I2S 扬声器功放 | 图 f7f0dc3f29b1 / 第 1 页 / CoreS3 第4资源页 U8 AW88298 |
| U9,U12,U13 | ES7210 / MSM381A3729H9BPC | 地址 0x40 的音频 ADC、双模拟麦克风和 AEC 回采链 | 图 f7f0dc3f29b1 / 第 1 页 / CoreS3 第4资源页 U9/U12/U13 |
| U10 | AW9523B | 地址 0x58 的 IO 扩展器，控制触摸、显示、摄像头、音频、TF、OTG 与 Boost | 图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 U10 AW9523B |
| U15/U20 | BMI270 / BMM150 | 地址 0x69 的六轴 IMU 与辅助总线三轴磁力计 | 图 95d654aa1d79 / 第 1 页 / CoreS3 第7资源页 U15 BMI270、U20 BMM150 |
| J1 (Core) | USB-TYPEC | CoreS3 主机 USB-C 电源与原生 USB 数据接口 | 图 674d725f5dc6 / 第 1 页 / CoreS3 第2资源页 J1 USB-TYPEC |
| U11 | MicroSD-SPI | 3.3V SPI microSD 卡槽 | 图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 U11 MicroSD-SPI |
| LCD1/CTP1/J2 | M5_LCD_10P / M5_TOUCH_8P / AFC34-S24FIA-00 | LCD、触摸与摄像头/传感子板连接器 | 图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 LCD1/CTP1/J2 |
| BUS1/J3 | M5.BUS / GH2.0-4P | 主机 30 针扩展总线与 Grove PORT.A | 图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 BUS1/J3 |
| U1/Q1/Q2 (Adapter) | FH9261-G3JZ / NMOS | Adapter 板单节电池保护链 | 图 9db48f62a793 / 第 1 页 / Adapter 第8资源页 Battery protection |
| S1/S2 | HC-5264-3A | 两路 Servo_SIG/VM/GND 舵机接口 | 图 9db48f62a793 / 第 1 页 / Adapter 第8资源页 S1/S2 Servo Interface |
| U1/Q3/Q4 (Power) | TPS61088 / AH20P30Q / S8050 Y1 | BAT+ 至 5V VM 舵机电源升压与 VM_EN 高边控制 | 图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 DCDC 与 VM Voltage:5V |
| U5/U4/Q2 | SN74LVC1G126DC / SN74LVC1G125DC / SS8550 Y2 | 舵机单线半双工串口收发与方向控制 | 图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 Servo Serial port signal conversion |
| U2 (Power) | INA226AIDGSR | 地址 0x41 的电池电流与电压监测器 | 图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 U2 INA226AIDGSR |
| U3 (Power) | PY32IO_EXP | 默认地址 0x6F 的身体 IO 扩展器，控制 VM_EN 与 RGB | 图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 U3 PY32IO_EXP |
| Q1/D1 (Power) | S8050 Y1 / IR LED | IR_SEND 控制的红外发射器 | 图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 Infrared Transmitter |
| USB1/F1 | TYPE-C 16P / Fuse 0603 2A/6V | Ring 板 USB Type-C 和旋转供电/数据触点入口 | 图 856c1ae467b5 / 第 1 页 / Ring 第10资源页 USB1/F1 与 TP1-TP4 |
| D1 (Touch) | IRM-56384 | 3.3V 红外接收器，输出 IR_REC | 图 4599f61bb443 / 第 1 页 / Touch 第11资源页 D1 IRM-56384 |
| U1-U12 (Touch) | WS2812C_4020 | BUS_5V 供电的 12 颗串联 RGB LED | 图 4599f61bb443 / 第 1 页 / Touch 第11资源页 RGB U1-U12 |
| U14 | Si12T | 地址 0x68 的三通道电容触摸控制器 | 图 4599f61bb443 / 第 1 页 / Touch 第11资源页 U14 Si12T |
| U13/Y1/ANT1 | ST25R3916-AQWT / 27.12MHz / ANT_NFC | 地址 0x50 的 NFC 读写器、外部晶体与差分线圈 | 图 4599f61bb443 / 第 1 页 / Touch 第11资源页 NFC U13/Y1/ANT1 |

## 系统结构

### StackChan/K151 整机硬件架构

StackChan/K151 由 CoreS3 主机和 Adapter、Power、Ring、Touch 四块身体板组成；主机负责 ESP32-S3 计算、显示/触摸/摄像头、音频、存储、无线与系统电源，身体板负责电池、舵机、底座 USB、红外、RGB、三点触摸和 NFC。

- 参数与网络：`host_assets=CoreS3 resources 1-7`；`body_assets=Adapter/Power/Ring/Touch resources 8-11`；`host_controller=ESP32-S3`；`body_boards=Adapter; Power; Ring; Touch`
- 证据：图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 ESP32-S3 与主机数字核心; 图 9db48f62a793 / 第 1 页 / Adapter 第8资源页; 图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页; 图 856c1ae467b5 / 第 1 页 / Ring 第10资源页; 图 4599f61bb443 / 第 1 页 / Touch 第11资源页

### 当前产品资源范围

当前 product_id 的清单明确包含 CoreS3 v1.0 七页、SCH_Adapter、SCH_Power、SCH_Ring、SCH_Touch 共 11 个资源；这些资源共同描述 StackChan 整机，而不是只描述独立销售的 StackChan Core/C156 或 StackChan Body/A180。

- 参数与网络：`product_id=stackchan-4ab98aca5f72`；`sku=K151`；`resource_count=11`；`core_pages=7`；`body_boards=4`
- 证据：图 de85c198f634 / 第 1 页 / 当前清单第1资源 CoreS3 page_01; 图 4599f61bb443 / 第 1 页 / 当前清单第11资源 SCH_Touch

### 机器人身体四板架构

Adapter 汇聚电池、USB 和两路舵机；Power 提供 TPS61088 VM 5V、半双工舵机、INA226、PY32 与红外发射；Ring 提供底座 USB-C 与四个旋转触点；Touch 集成红外接收、12颗 RGB、Si12T 与 ST25R3916 NFC。

- 参数与网络：`adapter=battery/USB/servos`；`power=VM/I2C/servo/IR`；`ring=USB-C rotating contacts`；`touch=IR receiver/RGB/touch/NFC`
- 证据：图 9db48f62a793 / 第 1 页 / Adapter 第8资源页; 图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页; 图 856c1ae467b5 / 第 1 页 / Ring 第10资源页; 图 4599f61bb443 / 第 1 页 / Touch 第11资源页

## 电源

### AXP2101 主机电源轨

U1 AXP2101 从 VBUS/VBAT 供电：LX1 产生 VDD_3V3，LX3 产生 VCC_3V3，BLDO1/2 输出 AVDD/DVDD，DLDO1/DC1SW 输出 VCC_BL，VBackup/VRTC 连接 RTC_VDD，ALDO1-4 输出 VDD_1V8、VDDA_3V3、VDDCAM_3V3、VDD_3V3_SD。

- 参数与网络：`pmu=AXP2101`；`inputs=VBUS; VBAT`；`buck_rails=VDD_3V3; VCC_3V3`；`ldo_rails=AVDD; DVDD; VCC_BL; VDD_1V8; VDDA_3V3; VDDCAM_3V3; VDD_3V3_SD`；`rtc=RTC_VDD`
- 证据：图 de85c198f634 / 第 1 页 / CoreS3 第1资源页 U1 AXP2101 全部电源输出

### 主机按键、BUS_5V 与 USB/OTG 电源方向

AXP2101 PWROK/PWRON/IRQ 分别连接 AXP_PG/PWR_KEY/AXP_WAKEUP；S1/S2 为复位/电源按键。U3 SY7088 从 AXP_PS 升压生成 BUS_5V，U14/U17/U18/U19 在 BUS_OUT_EN 与 USB_OTG_EN 控制下建立 BUS_5V、BUS_OUT、VUSB、VBUS 的双向受控路径。

- 参数与网络：`reset_power_keys=S1 AXP_PG; S2 PWR_KEY`；`boost=U3 SY7088 AXP_PS -> BUS_5V`；`switches=U14/U17 ME1502AM5G; U18/U19 ME1502CM5G`；`control=BUS_OUT_EN; USB_OTG_EN`
- 证据：图 de85c198f634 / 第 1 页 / CoreS3 第1资源页 AXP2101 控制与 S1/S2; 图 674d725f5dc6 / 第 1 页 / CoreS3 第2资源页 U3 SY7088; 图 97e9cd876f18 / 第 1 页 / CoreS3 第6资源页 Boost/OTG/USB/PMU 电源开关

### TPS61088 舵机 VM 5V

Power U1 TPS61088 以 BAT+ 为输入、L1 2.2uH 接 SW、R3 110KΩ/R4 33KΩ反馈；输出经 Q3 AH20P30Q 高边开关形成标注 VM Voltage:5V 的 VM。PY32 IO1 输出 VM_EN，经 Q4 S8050 控制 Q3。

- 参数与网络：`converter=U1 TPS61088`；`input=BAT+`；`inductor=L1 2.2uH`；`feedback=R3 110KΩ; R4 33KΩ`；`output=VM 5V`；`enable=PY32 IO1 VM_EN -> Q4 -> Q3`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 DCDC 与 IO Expansion VM_EN

## 接口

### CoreS3 原生 USB-C

主机 J1 USB-TYPEC 的 CC1/CC2 各经 5.1KΩ 接地，USB_D_P/USB_D_N 由 ESD5Z3V3 对地保护并各经 22Ω接 ESP32-S3 GPIO20/GPIO19，形成原生 USB 数据路径；VCC 连接 VUSB。

- 参数与网络：`connector=J1 USB-TYPEC`；`usb_dp=GPIO20 via 22Ω`；`usb_dn=GPIO19 via 22Ω`；`cc=2 x 5.1KΩ to GND`；`esd=D4/D6 ESD5Z3V3`；`power=VUSB`
- 证据：图 674d725f5dc6 / 第 1 页 / CoreS3 第2资源页 J1 USB-TYPEC 与保护/串阻; 图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 ESP32-S3 GPIO19/20 USB_DU_N/P

### 显示、触摸、摄像头与 microSD 接口

LCD1 引出 SPI_MOSI/SCK/MISO、LCD_CS/RST、VDD_3V3、VCC_BL；CTP1 引出 I2C_SYS_SDA/SCL、TOUCH_INT/RST。J2 24针承载 CAM_D2-D9、PCLK/VSYNC/HREF、RST/PWDN/MCLK、I2C 与 AVDD/DVDD/VDDCAM_3V3。U11 microSD 使用 TF_CS 与 SPI_MOSI/SCK/MISO，并由 TF_SW 检测插卡。

- 参数与网络：`lcd=LCD1 M5_LCD_10P SPI`；`touch=CTP1 M5_TOUCH_8P I2C`；`camera=J2 24-pin parallel camera/sensor`；`sd=U11 MicroSD-SPI`
- 证据：图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 J2/LCD1/CTP1/U11

### CoreS3 M5-Bus 与 PORT.A

CoreS3 BUS1 30针引出 GND、VCC_3V3、VBAT、BUS_OUT、SPI、UART、I2C、I2S、GPIO 与 AXP_PG；J3 GH2.0-4P pins1-4 为 BUS_PA_SCL、BUS_PA_SDA、BUS_OUT、GND，BUS_PA_SCL/SDA 对应 ESP32-S3 GPIO1/GPIO2。

- 参数与网络：`bus=BUS1 M5.BUS 30-pin`；`grove_port_a=J3 pin1 SCL; pin2 SDA; pin3 BUS_OUT; pin4 GND`；`esp_gpio=SCL GPIO1; SDA GPIO2`
- 证据：图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 BUS1/J3; 图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 GPIO1/2 BUS_PA_SCL/SDA

### Adapter 主连接器与双舵机

Adapter CON4 pins1-7 为 USB_5V、USB_DM、USB_DP、GND、Servo_SIG、VM、BAT+；S1/S2 两路舵机接口均为 pin1 Servo_SIG、pin2 VM、pin3 GND。CON1/CON2 转接 USB/5V/GND，CON3 引入 B-/BAT+。

- 参数与网络：`main_header=CON4 7-pin`；`servo_1=S1 Servo_SIG/VM/GND`；`servo_2=S2 Servo_SIG/VM/GND`；`battery_header=CON3 B-/BAT+`
- 证据：图 9db48f62a793 / 第 1 页 / Adapter 第8资源页 CON1-CON4 与 S1/S2

### 身体 Grove、主连接器与 Touch FPC

Power J1 GROVE_C 为 UART_RX/UART_TX/BUS_5V/GND，J2 GROVE_B 为 GPIO8/GPIO9/BUS_5V/GND；CON1 为 USB_DP/USB_DM/GND/USB_5V。Touch FPC1 pins1-8 为 BUS_5V、VCC_3V3、GND、RGB、I2C_SCL、I2C_SDA、Touch_IRQ、IR_REC。

- 参数与网络：`grove_c=UART_RX; UART_TX; BUS_5V; GND`；`grove_b=GPIO8; GPIO9; BUS_5V; GND`；`usb_header=USB_DP; USB_DM; GND; USB_5V`；`touch_fpc=BUS_5V; VCC_3V3; GND; RGB; I2C_SCL; I2C_SDA; Touch_IRQ; IR_REC`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 Grove/Onboard Interface; 图 4599f61bb443 / 第 1 页 / Touch 第11资源页 FPC1

### 底座 Ring USB-C

Ring USB1 VCC 经 F1 2A/6V 保险丝连接 USB_5V，DP1/DP2 合并为 USB_DP，DN1/DN2 合并为 USB_DM，CC1/CC2 各由 5.1KΩ下拉；四个同心触点依次为 TP1=GND、TP2=USB_DP、TP3=USB_5V、TP4=USB_DM。

- 参数与网络：`connector=USB1 TYPE-C 16P`；`fuse=F1 2A/6V`；`cc=2 x 5.1KΩ`；`contacts=TP1 GND; TP2 USB_DP; TP3 USB_5V; TP4 USB_DM`
- 证据：图 856c1ae467b5 / 第 1 页 / Ring 第10资源页 USB1/F1 与四圈 TP1-TP4

### ESP32-S3 到身体功能信号

跨 CoreS3 M5-Bus 与 Power 页可确认：ESP32-S3 GPIO6/GPIO7 对应 Servo_TX/Servo_RX，GPIO5 对应 IR_SEND，GPIO10/BUS_ADC1 对应 IR_REC，GPIO12/GPIO11 对应身体 I2C_SDA/I2C_SCL。

- 参数与网络：`GPIO6=Servo_TX`；`GPIO7=Servo_RX`；`GPIO5=IR_SEND`；`GPIO10=IR_REC via BUS_ADC1`；`GPIO12=I2C_SDA`；`GPIO11=I2C_SCL`
- 证据：图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 ESP32-S3 GPIO5/6/7/10/11/12 网络; 图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 M5-BUS 对应针脚; 图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 M5Stack_BUS Servo/IR/I2C 信号

## 总线

### CoreS3 内部 I2C

ESP32-S3 GPIO12/GPIO11 分别连接 I2C_SYS_SDA/I2C_SYS_SCL，并由 R20/R32 各 2.2KΩ上拉到 VDD_3V3；AXP2101、BM8563、AW88298、ES7210、AW9523B 与 BMI270 接入该总线。

- 参数与网络：`sda=ESP32-S3 GPIO12`；`scl=ESP32-S3 GPIO11`；`pullups=R20/R32 2.2KΩ`；`devices=AXP2101; BM8563; AW88298; ES7210; AW9523B; BMI270`
- 证据：图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 GPIO11/12 与 I2C 上拉; 图 f7f0dc3f29b1 / 第 1 页 / CoreS3 第4资源页音频 I2C; 图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 AW9523B I2C

### 舵机单线半双工串口

Servo_TX 经 U5 SN74LVC1G126DC 驱动 Servo_SIG，Servo_SIG 经 U4 SN74LVC1G125DC 返回 Servo_RX；Q2 SS8550 由 Servo_TX 经 R9 控制并生成 TX_EN，控制发送/接收三态方向。

- 参数与网络：`tx=Servo_TX -> U5 -> Servo_SIG`；`rx=Servo_SIG -> U4 -> Servo_RX`；`direction=Q2 SS8550 -> TX_EN`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 Servo Serial port signal conversion

### 身体系统 I2C

I2C_SCL/I2C_SDA 经身体 M5Stack_BUS 与 Touch FPC 连接 PY32IO_EXP、INA226、Si12T、ST25R3916；Power 板 R19/R20 4.7KΩ 和 Touch 板 R4/R5 4.7KΩ均提供 3.3V 上拉。

- 参数与网络：`devices=PY32IO_EXP; INA226; Si12T; ST25R3916`；`power_pullups=R19/R20 4.7KΩ`；`touch_pullups=R4/R5 4.7KΩ`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 I2C_SCL/SDA、PY32、INA226 与 R19/R20; 图 4599f61bb443 / 第 1 页 / Touch 第11资源页 Si12T/ST25R3916 与 R4/R5

## 总线地址

### CoreS3 主机 I2C 地址

CoreS3 页面明确标注 AXP2101=0x34、AW88298=0x36、ES7210=0x40、AW9523B=0x58、BMI270=0x69，均为 7-bit 地址。

- 参数与网络：`AXP2101=0x34`；`AW88298=0x36`；`ES7210=0x40`；`AW9523B=0x58`；`BMI270=0x69`
- 证据：图 de85c198f634 / 第 1 页 / CoreS3 第1资源页 AXP2101 0x34; 图 f7f0dc3f29b1 / 第 1 页 / CoreS3 第4资源页 AW88298 0x36 与 ES7210 0x40; 图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 AW9523B 0x58; 图 95d654aa1d79 / 第 1 页 / CoreS3 第7资源页 BMI270 地址注记 0x69

### 身体 I2C 地址

Power/Touch 页面明确标注 INA226=0x41、PY32IO_EXP 默认=0x6F（ADD_SEL=1 时 0x71）、Si12T=0x68、ST25R3916=0x50。PY32 R27 标 NC、R26 10KΩ下拉，使默认地址为 0x6F。

- 参数与网络：`INA226=0x41`；`PY32_default=0x6F`；`PY32_alt=0x71`；`Si12T=0x68`；`ST25R3916=0x50`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 PY32 与 INA226 地址注记; 图 4599f61bb443 / 第 1 页 / Touch 第11资源页 Si12T 0x68 与 ST25R3916 0x50

## GPIO 与控制信号

### AW9523B 控制映射

AW9523B P0_0-P0_5 依次连接 TOUCH_RST、BUS_OUT_EN、AW_RST、ES_INT、TF_SW、USB_OTG_EN；P1_0-P1_3 连接 CAM_RST、LCD_RST、TOUCH_INT、AW_INT，P1_7 连接 BOOST_EN，RSTN 接 AXP_PG，INTN 输出 I2C_INT。

- 参数与网络：`P0=TOUCH_RST; BUS_OUT_EN; AW_RST; ES_INT; TF_SW; USB_OTG_EN`；`P1=CAM_RST; LCD_RST; TOUCH_INT; AW_INT; BOOST_EN`；`reset=AXP_PG`；`interrupt=I2C_INT`
- 证据：图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 U10 AW9523B pin map

### 红外发射与接收

IR_SEND 经 R6 4.7KΩ驱动 Q1 S8050，下拉由 BUS_5V 经 R1 51Ω供电的红外 LED；Touch D1 IRM-56384 由 VCC_3V3 供电并输出 IR_REC，经 FPC1 pin8 返回主板。

- 参数与网络：`transmitter=IR_SEND -> R6/Q1 -> IR LED; R1 51Ω to BUS_5V`；`receiver=D1 IRM-56384 VCC_3V3 -> IR_REC`；`return=FPC1 pin8`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 Infrared Transmitter; 图 4599f61bb443 / 第 1 页 / Touch 第11资源页 Infrared Receiver

### 12 颗 WS2812C RGB 链

RGB 数据进入 U1 DIN，U1-U12 WS2812C_4020 逐级 DOUT 到下一颗 DIN；12颗 LED 全部由 BUS_5V 供电并接 GND。Power 页 PY32IO_EXP IO14 输出 RGB 网络。

- 参数与网络：`count=12`；`part_number=WS2812C_4020`；`data_source=PY32IO_EXP IO14/RGB`；`supply=BUS_5V`；`topology=serial DIN/DOUT chain`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 PY32 IO14/RGB; 图 4599f61bb443 / 第 1 页 / Touch 第11资源页 RGB U1-U12

## 时钟

### ESP32-S3、RTC 与摄像头时钟

ESP32-S3 使用 X1 40MHz/10ppm/20pF/2520 晶体；BM8563 使用 Y1 与 C30/C32 6pF；摄像头连接器的 CAM_MCLK 由 X2 20MHz ±25ppm 3.3V 振荡器经 R31 51Ω提供。

- 参数与网络：`esp32=X1 40MHz 10ppm 20pF 2520`；`rtc=BM8563 Y1; C30/C32 6pF`；`camera=X2 20MHz ±25ppm 3.3V; R31 51Ω`
- 证据：图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 X1 40MHz; 图 674d725f5dc6 / 第 1 页 / CoreS3 第2资源页 BM8563/Y1; 图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 X2 20MHz/CAM_MCLK

## 复位

### ESP_BOOT 比较器电路

U2 LMV331 由 VDD_3V3 供电，输出 ESP_BOOT 并由 R4 10KΩ 上拉；AXP_PG 经二极管、电阻和 RC 网络进入比较器，LED2 GREEN 与 R10 2KΩ连接 ESP_BOOT。

- 参数与网络：`comparator=U2 LMV331`；`input=AXP_PG RC/diode network`；`output=ESP_BOOT`；`pullup=R4 10KΩ`；`indicator=LED2 GREEN`
- 证据：图 674d725f5dc6 / 第 1 页 / CoreS3 第2资源页 U2 LMV331/ESP_BOOT

## 保护电路

### 身体电池保护

Adapter U1 FH9261-G3JZ 配合 Q1/Q2 背靠背 NMOS 控制 BAT+/B-/GND/VM 保护路径，外围包含 R2 330Ω、R3 2.2KΩ 与 C1 100nF。

- 参数与网络：`controller=FH9261-G3JZ`；`switches=Q1/Q2 NMOS`；`nets=BAT+; B-; GND; VM`；`passives=R2 330Ω; R3 2.2KΩ; C1 100nF`
- 证据：图 9db48f62a793 / 第 1 页 / Adapter 第8资源页 Battery protection

## 存储

### ESP32-S3 外部 Flash 与 PSRAM 接线

U6 标注 GD25Q128/W25Q128/128Mbit/3.3V，并通过 FLASH_CS0/CLK/D/Q/WP/HD 接 ESP32-S3；U7 EPSRAM 使用 FLASH_CS1，复用 FLASH_CLK 与 FLASH_D/Q/WP/HD。

- 参数与网络：`flash=U6 GD25Q128/W25Q128 128Mbit`；`flash_cs=FLASH_CS0`；`psram=U7 EPSRAM`；`psram_cs=FLASH_CS1`；`shared_bus=FLASH_CLK/D/Q/WP/HD`
- 证据：图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 U5/U6/U7 存储网络

## 音频

### 双麦克风、AEC 与扬声器功放

U9 ES7210 通过 I2S_BCK/WCK/DATI 接 ESP32-S3并采集 U12/U13 双麦克风；AW88298 通过 I2S_BCK/WCK/DATO 接收播放数据并输出 SPK_VOP/SPK_VON。两路扬声器输出经 150KΩ与耦合电容回采到 ES7210 MIC3P/MIC3N，形成 AEC_P/AEC_N。

- 参数与网络：`adc=U9 ES7210 0x40`；`microphones=U12/U13 MSM381A3729H9BPC`；`amplifier=U8 AW88298 0x36`；`record_i2s=I2S_BCK/WCK/DATI`；`play_i2s=I2S_BCK/WCK/DATO`；`aec=SPK_VOP/VON -> AEC_P/N -> MIC3P/N`
- 证据：图 f7f0dc3f29b1 / 第 1 页 / CoreS3 第4资源页 AW88298、ES7210、U12/U13 与 AEC 回采

## 传感器

### BMI270 与 BMM150 九轴链

BMI270 通过 I2C_SYS_SDA/SCL 接主控，SDO/SA0 上拉到 3.3V形成地址 0x69；BMI270 ASDX/ASCX 输出 BMM_SDA/BMM_SCL 到 BMM150，BMM150 的 CSB 与 SDO 接地并由 3.3V 供电。

- 参数与网络：`imu=U15 BMI270 0x69`；`magnetometer=U20 BMM150`；`host_bus=I2C_SYS_SDA/SCL`；`aux_bus=BMM_SDA/BMM_SCL`
- 证据：图 95d654aa1d79 / 第 1 页 / CoreS3 第7资源页 BMI270/BMM150

### Si12T 三点触摸

U14 Si12T 连接 TP1、TP2、TP3 三个经 680Ω串联的触摸通道，IRQ 输出 Touch_IRQ 并由 R10 10KΩ上拉到 VCC_3V3；器件地址标为 0x68。

- 参数与网络：`controller=U14 Si12T`；`address=0x68`；`channels=TP1; TP2; TP3`；`series_resistors=3 x 680Ω`；`interrupt=Touch_IRQ; R10 10KΩ pullup`
- 证据：图 4599f61bb443 / 第 1 页 / Touch 第11资源页 U14 Si12T TOUCH 区

## 射频

### ESP32-S3 射频天线路径

ESP_LNA 经 C68、C69/C86 匹配网络和 R35 0Ω连接 ANT1 PROANT440；R36、L9、C121 标为 NC，J4 IPEX 为未装配备用路径。

- 参数与网络：`source=ESP_LNA`；`antenna=ANT1 PROANT440`；`series=C68 1.8nH; R35 0Ω`；`shunt=C69 2.7pF; C86 2.4pF`；`alternate=J4 IPEX via NC parts`
- 证据：图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 ESP_LNA/ANT1/J4

### ST25R3916 NFC 与差分天线

U13 ST25R3916-AQWT 使用地址 0x50，Y1 27.12MHz 晶体连接 XTO/XTI；RFO1/RFO2 经 L1/L2 270nH 5%、C1-C15 和 R1/R3 2.4Ω形成差分匹配并驱动 ANT1/ANT_NFC 线圈。

- 参数与网络：`controller=U13 ST25R3916-AQWT`；`address=0x50`；`clock=Y1 27.12MHz; C16/C17 10pF`；`inductors=L1/L2 270nH 5%`；`antenna=ANT1 ANT_NFC`
- 证据：图 4599f61bb443 / 第 1 页 / Touch 第11资源页 NFC 区 U13/Y1/ANT1

## 模拟电路

### INA226 电池电流与电压监测

BAT+ 与 BAT_IN 之间串联 R18 10mΩ/0805 分流器；INA226 IN+/IN- 经 R22/R21 各 10Ω接 BAT+/BAT_IN，VBUS 经 R23 4.7KΩ接 BUS_3V3 监测网络，ALERT 引出。

- 参数与网络：`shunt=R18 10mΩ/0805`；`in_plus=R22 10Ω -> BAT+`；`in_minus=R21 10Ω -> BAT_IN`；`vbus=R23 4.7KΩ -> BUS_3V3`；`alert=ALERT`
- 证据：图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 Battery Current and Voltage Monitor

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | StackChan/K151 整机硬件架构 | `host_assets=CoreS3 resources 1-7`；`body_assets=Adapter/Power/Ring/Touch resources 8-11`；`host_controller=ESP32-S3`；`body_boards=Adapter; Power; Ring; Touch` |
| 系统结构 | 当前产品资源范围 | `product_id=stackchan-4ab98aca5f72`；`sku=K151`；`resource_count=11`；`core_pages=7`；`body_boards=4` |
| 总线地址 | CoreS3 主机 I2C 地址 | `AXP2101=0x34`；`AW88298=0x36`；`ES7210=0x40`；`AW9523B=0x58`；`BMI270=0x69` |
| 电源 | AXP2101 主机电源轨 | `pmu=AXP2101`；`inputs=VBUS; VBAT`；`buck_rails=VDD_3V3; VCC_3V3`；`ldo_rails=AVDD; DVDD; VCC_BL; VDD_1V8; VDDA_3V3; VDDCAM_3V3; VDD_3V3_SD`；`rtc=RTC_VDD` |
| 电源 | 主机按键、BUS_5V 与 USB/OTG 电源方向 | `reset_power_keys=S1 AXP_PG; S2 PWR_KEY`；`boost=U3 SY7088 AXP_PS -> BUS_5V`；`switches=U14/U17 ME1502AM5G; U18/U19 ME1502CM5G`；`control=BUS_OUT_EN; USB_OTG_EN` |
| 接口 | CoreS3 原生 USB-C | `connector=J1 USB-TYPEC`；`usb_dp=GPIO20 via 22Ω`；`usb_dn=GPIO19 via 22Ω`；`cc=2 x 5.1KΩ to GND`；`esd=D4/D6 ESD5Z3V3`；`power=VUSB` |
| 复位 | ESP_BOOT 比较器电路 | `comparator=U2 LMV331`；`input=AXP_PG RC/diode network`；`output=ESP_BOOT`；`pullup=R4 10KΩ`；`indicator=LED2 GREEN` |
| 存储 | ESP32-S3 外部 Flash 与 PSRAM 接线 | `flash=U6 GD25Q128/W25Q128 128Mbit`；`flash_cs=FLASH_CS0`；`psram=U7 EPSRAM`；`psram_cs=FLASH_CS1`；`shared_bus=FLASH_CLK/D/Q/WP/HD` |
| 时钟 | ESP32-S3、RTC 与摄像头时钟 | `esp32=X1 40MHz 10ppm 20pF 2520`；`rtc=BM8563 Y1; C30/C32 6pF`；`camera=X2 20MHz ±25ppm 3.3V; R31 51Ω` |
| 射频 | ESP32-S3 射频天线路径 | `source=ESP_LNA`；`antenna=ANT1 PROANT440`；`series=C68 1.8nH; R35 0Ω`；`shunt=C69 2.7pF; C86 2.4pF`；`alternate=J4 IPEX via NC parts` |
| 总线 | CoreS3 内部 I2C | `sda=ESP32-S3 GPIO12`；`scl=ESP32-S3 GPIO11`；`pullups=R20/R32 2.2KΩ`；`devices=AXP2101; BM8563; AW88298; ES7210; AW9523B; BMI270` |
| 音频 | 双麦克风、AEC 与扬声器功放 | `adc=U9 ES7210 0x40`；`microphones=U12/U13 MSM381A3729H9BPC`；`amplifier=U8 AW88298 0x36`；`record_i2s=I2S_BCK/WCK/DATI`；`play_i2s=I2S_BCK/WCK/DATO`；`aec=SPK_VOP/VON -> AEC_P/N -> MIC3P/N` |
| GPIO 与控制信号 | AW9523B 控制映射 | `P0=TOUCH_RST; BUS_OUT_EN; AW_RST; ES_INT; TF_SW; USB_OTG_EN`；`P1=CAM_RST; LCD_RST; TOUCH_INT; AW_INT; BOOST_EN`；`reset=AXP_PG`；`interrupt=I2C_INT` |
| 接口 | 显示、触摸、摄像头与 microSD 接口 | `lcd=LCD1 M5_LCD_10P SPI`；`touch=CTP1 M5_TOUCH_8P I2C`；`camera=J2 24-pin parallel camera/sensor`；`sd=U11 MicroSD-SPI` |
| 接口 | CoreS3 M5-Bus 与 PORT.A | `bus=BUS1 M5.BUS 30-pin`；`grove_port_a=J3 pin1 SCL; pin2 SDA; pin3 BUS_OUT; pin4 GND`；`esp_gpio=SCL GPIO1; SDA GPIO2` |
| 传感器 | BMI270 与 BMM150 九轴链 | `imu=U15 BMI270 0x69`；`magnetometer=U20 BMM150`；`host_bus=I2C_SYS_SDA/SCL`；`aux_bus=BMM_SDA/BMM_SCL` |
| 系统结构 | 机器人身体四板架构 | `adapter=battery/USB/servos`；`power=VM/I2C/servo/IR`；`ring=USB-C rotating contacts`；`touch=IR receiver/RGB/touch/NFC` |
| 接口 | Adapter 主连接器与双舵机 | `main_header=CON4 7-pin`；`servo_1=S1 Servo_SIG/VM/GND`；`servo_2=S2 Servo_SIG/VM/GND`；`battery_header=CON3 B-/BAT+` |
| 保护电路 | 身体电池保护 | `controller=FH9261-G3JZ`；`switches=Q1/Q2 NMOS`；`nets=BAT+; B-; GND; VM`；`passives=R2 330Ω; R3 2.2KΩ; C1 100nF` |
| 电源 | TPS61088 舵机 VM 5V | `converter=U1 TPS61088`；`input=BAT+`；`inductor=L1 2.2uH`；`feedback=R3 110KΩ; R4 33KΩ`；`output=VM 5V`；`enable=PY32 IO1 VM_EN -> Q4 -> Q3` |
| 总线 | 舵机单线半双工串口 | `tx=Servo_TX -> U5 -> Servo_SIG`；`rx=Servo_SIG -> U4 -> Servo_RX`；`direction=Q2 SS8550 -> TX_EN` |
| 接口 | 身体 Grove、主连接器与 Touch FPC | `grove_c=UART_RX; UART_TX; BUS_5V; GND`；`grove_b=GPIO8; GPIO9; BUS_5V; GND`；`usb_header=USB_DP; USB_DM; GND; USB_5V`；`touch_fpc=BUS_5V; VCC_3V3; GND; RGB; I2C_SCL; I2C_SDA; Touch_IRQ; IR_REC` |
| 总线 | 身体系统 I2C | `devices=PY32IO_EXP; INA226; Si12T; ST25R3916`；`power_pullups=R19/R20 4.7KΩ`；`touch_pullups=R4/R5 4.7KΩ` |
| 总线地址 | 身体 I2C 地址 | `INA226=0x41`；`PY32_default=0x6F`；`PY32_alt=0x71`；`Si12T=0x68`；`ST25R3916=0x50` |
| 模拟电路 | INA226 电池电流与电压监测 | `shunt=R18 10mΩ/0805`；`in_plus=R22 10Ω -> BAT+`；`in_minus=R21 10Ω -> BAT_IN`；`vbus=R23 4.7KΩ -> BUS_3V3`；`alert=ALERT` |
| GPIO 与控制信号 | 红外发射与接收 | `transmitter=IR_SEND -> R6/Q1 -> IR LED; R1 51Ω to BUS_5V`；`receiver=D1 IRM-56384 VCC_3V3 -> IR_REC`；`return=FPC1 pin8` |
| GPIO 与控制信号 | 12 颗 WS2812C RGB 链 | `count=12`；`part_number=WS2812C_4020`；`data_source=PY32IO_EXP IO14/RGB`；`supply=BUS_5V`；`topology=serial DIN/DOUT chain` |
| 传感器 | Si12T 三点触摸 | `controller=U14 Si12T`；`address=0x68`；`channels=TP1; TP2; TP3`；`series_resistors=3 x 680Ω`；`interrupt=Touch_IRQ; R10 10KΩ pullup` |
| 射频 | ST25R3916 NFC 与差分天线 | `controller=U13 ST25R3916-AQWT`；`address=0x50`；`clock=Y1 27.12MHz; C16/C17 10pF`；`inductors=L1/L2 270nH 5%`；`antenna=ANT1 ANT_NFC` |
| 接口 | 底座 Ring USB-C | `connector=USB1 TYPE-C 16P`；`fuse=F1 2A/6V`；`cc=2 x 5.1KΩ`；`contacts=TP1 GND; TP2 USB_DP; TP3 USB_5V; TP4 USB_DM` |
| 接口 | ESP32-S3 到身体功能信号 | `GPIO6=Servo_TX`；`GPIO7=Servo_RX`；`GPIO5=IR_SEND`；`GPIO10=IR_REC via BUS_ADC1`；`GPIO12=I2C_SDA`；`GPIO11=I2C_SCL` |
| 系统结构 | K151 整机资源版本适用范围 | `product=StackChan K151`；`core_schematic=CoreS3 v1.0`；`body_schematics=Adapter; Power; Ring; Touch`；`bom_mapping=null`；`production_batch=null` |
| 总线 | AXP2101 I2C NEED REVERSED 注记 | `device=AXP2101`；`visible_sda=I2C_SYS_SDA`；`visible_scl=I2C_SYS_SCL`；`note=I2C NEED REVERSED` |
| 内存与 Flash | 8MB PSRAM | `documented_capacity=8MB`；`schematic_label=U7 EPSRAM`；`part_number=null`；`frequency=null` |
| 核心器件 | 显示与触摸具体规格 | `documented_lcd=2.0 inch 320x240 ILI9342C IPS 65536 colors`；`documented_touch=FT6336U capacitive multi-touch`；`schematic_scope=connectors only` |
| 传感器 | 摄像头与接近/环境光器件 | `documented_camera=GC0308 640x480 0.3MP`；`documented_proximity_als=LTR-553ALS-WA`；`schematic_scope=J2 connector only` |
| 音频 | 1W 扬声器规格 | `documented_power=1W`；`amplifier=AW88298`；`speaker_part_number=null`；`impedance=null` |
| 系统结构 | ESP32-S3 主频与无线能力 | `documented_cpu=dual-core Xtensa LX7 240MHz`；`documented_wifi=2.4GHz 802.11b/g/n`；`documented_bluetooth=Bluetooth 5 LE`；`schematic_device=ESP32-S3` |
| 电源 | 550mAh 电池 | `documented_capacity=550mAh`；`cell_part_number=null`；`nominal_voltage=null`；`charger_visible_in_body_pages=false`；`temperature_sensor_visible=false` |
| 核心器件 | SCS0009 舵机与机械角度 | `documented_model=SCS0009`；`documented_horizontal=360 degree continuous`；`documented_vertical=90 degree`；`documented_feedback=true`；`schematic_scope=two electrical interfaces` |
| 核心器件 | PY32L020 IO 扩展器型号 | `documented_family=PY32L020`；`schematic_label=PY32IO_EXP`；`part_number=null`；`firmware_version=null` |
| 射频 | NFC 协议与性能 | `controller=ST25R3916`；`address=0x50`；`protocol_modes=null`；`read_distance=null`；`supported_tags=null`；`certification=null` |
| 其他事实 | 整机与包装尺寸重量 | `documented_product_size=54.0 x 70.5 x 61.5mm`；`documented_product_weight=187.2g`；`documented_package_size=142.0 x 101.0 x 58.0mm`；`documented_gross_weight=272.4g` |
| 其他事实 | K151 与 K151-R 套装范围 | `current_manifest_sku=K151`；`documented_variant=K151-R`；`remote_components=StickC-Plus; Hat Mini JoyC`；`remote_schematics_in_assets=false` |
| 其他事实 | 出厂固件与联网功能 | `documented_features=AI agent; animations; ESP-NOW remote; phone video; app download; OTA`；`firmware_version=null`；`service_version=null` |

## 待确认事项

- `system.resource-version-applicability`：当前主机七页均命名为 Sch_M5_CoreS3_v1.0，身体四板页未打印 K151 SKU、整机版本、PCB/BOM 组合版本或量产批次；这 11 页与当前 K151 整机量产版本的精确对应关系仍需版本化设计资料确认。（证据：图 de85c198f634 / 第 1 页 / CoreS3 第1资源页无 K151 标识; 图 9db48f62a793 / 第 1 页 / Adapter 第8资源页无 K151/整机 BOM 标识）
- `bus.axp-i2c-reversed-note`：AXP2101 SDA/SCL 连接 I2C_SYS_SDA/I2C_SYS_SCL，但两脚旁保留红字 I2C NEED REVERSED；仅凭页面不能判断该注记是已处理的历史说明还是当前连线待修订项。（证据：图 de85c198f634 / 第 1 页 / CoreS3 第1资源页 U1 pins39/40 红字注记）
- `memory.documented-8mb-psram`：产品正文称主机具有 8MB PSRAM；原理图 U7 只标 EPSRAM 并给出总线连接，没有料号、容量、频率或封装。（证据：图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 U7 仅标 EPSRAM）
- `component.documented-display-touch`：产品正文称 2.0英寸 320x240 ILI9342C IPS LCD 和 FT6336U 电容多点触摸；主板图只给 LCD1/CTP1 连接器，没有显示控制器、尺寸、分辨率、色深或玻璃参数。（证据：图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 LCD1/CTP1 仅为连接器）
- `sensor.documented-camera-proximity`：产品正文称使用 GC0308 640x480 0.3MP 摄像头和 LTR-553ALS-WA 接近/环境光传感器；主板图只给 J2 摄像头/传感子板连接器，没有这两个器件或其光学参数。（证据：图 12e215412fd9 / 第 1 页 / CoreS3 第5资源页 J2 24针摄像头/传感子板接口）
- `audio.documented-speaker`：产品正文称主机包含 1W 扬声器；音频页只显示 AW88298 与 SPK_VOP/SPK_VON 网络，没有扬声器器件、连接器、阻抗或额定功率。（证据：图 f7f0dc3f29b1 / 第 1 页 / CoreS3 第4资源页 AW88298/SPK_VOP/SPK_VON，无扬声器）
- `system.documented-performance-wireless`：产品正文称双核 Xtensa LX7 240MHz、2.4GHz Wi-Fi 802.11b/g/n 和 Bluetooth 5 LE；原理图确认 ESP32-S3 与天线链，但未直接标注 CPU 主频、无线协议、频段、发射功率或认证参数。（证据：图 8f2f5466da03 / 第 1 页 / CoreS3 第3资源页 U5 ESP32-S3 与射频天线链）
- `power.documented-battery-capacity`：产品正文称机器人身体包含 550mAh 电池；原理图只显示 BAT+/B-/BAT_IN、电池保护、分流器和升压路径，没有电芯型号、容量、标称/满充电压、充电器或温度检测。（证据：图 9db48f62a793 / 第 1 页 / Adapter 第8资源页 BAT+/B- 保护; 图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 BAT+/BAT_IN 监测与升压）
- `component.documented-servos`：产品正文称两路舵机为带反馈 SCS0009，水平轴 360度无限旋转、竖直轴 90度；原理图只确认两路 Servo_SIG/VM/GND 和半双工串口，没有舵机型号、角度、机械限位、反馈帧或电流。（证据：图 9db48f62a793 / 第 1 页 / Adapter 第8资源页 S1/S2 Servo Interface; 图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页半双工舵机串口）
- `component.documented-py32l020`：产品正文数据手册指向 PY32L020，原理图器件仅标 U3 PY32IO_EXP，没有完整 MCU 型号、Flash/RAM、时钟、固件版本或启动配置。（证据：图 a3c6b35ef1aa / 第 1 页 / Power 第9资源页 U3 仅标 PY32IO_EXP）
- `rf.documented-nfc-performance`：原理图确认 ST25R3916、0x50 地址、27.12MHz 晶体和差分天线匹配，但没有协议模式、载波功率、读写距离、支持卡型、天线调谐验证或认证信息。（证据：图 4599f61bb443 / 第 1 页 / Touch 第11资源页 NFC 电路与天线匹配）
- `other.documented-mechanics`：产品正文列出 StackChan 54.0 x 70.5 x 61.5mm、187.2g，包装 142.0 x 101.0 x 58.0mm、272.4g；11 个电气原理图没有整机结构、尺寸、重量或舵机安全角度证据。（证据：图 9db48f62a793 / 第 1 页 / 电气原理图资源不含整机机械尺寸）
- `other.documented-kit-scope`：源文档同时描述 K151 与带 StickC-Plus/Hat Mini JoyC 遥控器的 K151-R，但当前产品清单 SKU 为 K151，11 个原理图资源不包含遥控器电路；K151-R 的遥控器规格和重量不属于当前 confirmed 硬件范围。（证据：图 de85c198f634 / 第 1 页 / 当前 11 页资源从 CoreS3 开始，未包含遥控器原理图）
- `other.documented-firmware-features`：产品正文宣称 AI 智能体、表情动作、ESP-NOW 遥控、手机视频、应用下载和 OTA；这些属于固件、服务器或 App 行为，11 个原理图只能确认相应硬件能力，不能证明具体功能版本与在线服务可用性。（证据：图 8f2f5466da03 / 第 1 页 / CoreS3 硬件主控页无固件或在线服务版本）
- `review.resource-version`：请提供 K151 的版本化主机/身体 PCB、BOM 和工程变更记录，确认 CoreS3 v1.0 与四块身体板图适用的量产批次。；原因：页面没有 K151 整机版本与 11 份图纸组合版本的对应表。
- `review.axp-i2c-reversed`：AXP2101 页面的 I2C NEED REVERSED 是已处理历史注记，还是表示当前 SDA/SCL 仍需交换？；原因：红字注记与当前同名网络并存，语义不明确。
- `review.psram`：请确认 K151 主机 8MB PSRAM 的料号、容量、频率和封装。；原因：原理图只标 EPSRAM，不含容量或料号。
- `review.display-touch`：请用 K151 主机 LCD/触摸子板原理图或 BOM 确认 ILI9342C、FT6336U、分辨率、色深与玻璃参数。；原因：主板图只提供 LCD1/CTP1 连接器。
- `review.camera-proximity`：请用摄像头/传感子板原理图或 BOM 确认 GC0308、LTR-553ALS-WA 与 0.3MP 参数。；原因：当前页只提供 J2 接口。
- `review.speaker`：请确认 K151 1W 扬声器料号、阻抗、连接器及 AW88298 输出匹配参数。；原因：音频页没有扬声器器件或额定参数。
- `review.performance-wireless`：请用 ESP32-S3 量产配置和认证资料确认 240MHz、Wi-Fi/BLE 协议、频段与射频性能。；原因：原理图只确认芯片和天线链。
- `review.battery`：请确认 550mAh 电芯型号、额定/满充电压、持续/峰值放电、保护阈值、充电器与温度保护。；原因：身体原理图没有容量、电芯或完整充电规格。
- `review.servos`：请用 SCS0009 BOM/datasheet 与实机确认两路舵机型号、角度、反馈帧、波特率、电流和机械限位。；原因：原理图只确认电气接口和半双工串口。
- `review.py32`：请确认 U3 的完整 PY32L020 料号、内部存储、时钟、固件版本、复位/升级方式和 GPIO 默认状态。；原因：图中器件值仅为 PY32IO_EXP。
- `review.nfc-performance`：请用 ST25R3916 配置、天线调谐与实测确认 NFC 协议、卡型、读写距离、场强、功耗和认证。；原因：原理图没有系统级 NFC 性能或认证数据。
- `review.mechanics`：请用 K151 正式结构图、称重记录与包装规范复核整机尺寸、重量和舵机安全角度。；原因：电气原理图不包含整机机械参数。
- `review.kit-scope`：是否需要为 K151-R 的 StickC-Plus/Hat Mini JoyC 遥控器建立独立产品事实与原理图描述？；原因：当前 product_id/SKU 为 K151，资源不含遥控器电路。
- `review.firmware-features`：请用 K151 出厂固件版本、App/服务版本与发布记录确认 AI、ESP-NOW、视频、应用下载和 OTA 功能边界。；原因：这些功能不能由静态电气原理图确认。

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
| 8 | 1 | `9db48f62a793a225399111d25f773c77e1d816ec6c0fea3205ec0c05c3c4617f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/SCH_Adapter.png` |
| 9 | 1 | `a3c6b35ef1aadbec775fdc0a0241130b374efa8b2d59cb5dd2b48eb063b4ebf6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/SCH_Power.png` |
| 10 | 1 | `856c1ae467b59541b366e109c831b1d1054103d5ef5431e6986eb6fce4ee452f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/SCH_Ring.png` |
| 11 | 1 | `4599f61bb443685aa5844104a12c968188342db6a6f71fe4b4da9c428890638f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/SCH_Touch.png` |

---

源文档：`zh_CN/StackChan.md`

源文档 SHA-256：`8dab8ac7c818457e5d8b3f3528692defff8a0bdbb73bf655360a1a2a0e1863c3`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
