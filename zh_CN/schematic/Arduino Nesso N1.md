# Arduino Nesso N1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Arduino Nesso N1 |
| SKU | DK001 |
| 产品 ID | `arduino-nesso-n1-9bc6c4c0b02d` |
| 源文档 | `zh_CN/core/Arduino_Nesso_N1.md` |

## 概述

Arduino Nesso N1 以 ESP32-C6 为主控，集成 16 MB SPI Flash、SX1262 LoRa 射频链、ST7789 135×240 LCD、FT6336 触摸、BMI270 IMU、双 PI4IOE5V6408 IO 扩展器、250 mAh 电池与多路电源管理，并引出 USB-C、Qwiic、Grove 和 8 Pin 扩展接口。

## 检索关键词

`Arduino Nesso N1`、`DK001`、`TPX00227`、`ESP32-C6`、`SX1262`、`850-960 MHz`、`MMCX`、`ST7789`、`FT6336`、`BMI270`、`PI4IOE5V6408`、`BQ27220YZFR`、`AW32001ECSR`、`PMS150G`、`JW5712`、`SGM6603`、`GPIO21`、`GPIO20`、`GPIO10`、`GPIO8`、`I2C0`、`SPI2`、`Qwiic`、`Grove`、`Hat Bus`、`USB-C`、`LoRa`、`0x43`、`0x44`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4/U8 | ESP32-C6 | RISC-V 32 位主控制器 | 图 7bce7557076f / 第 1 页 / 系统框图中央黄色 ESP32-C6 RISC-V 32-bit 方框，标注 U4/U8 |
| U5 | GD25Q128/W25Q128 | 16 MB SPI Flash | 图 7bce7557076f / 第 1 页 / 系统框图左下 Flash 16 MB GD25Q128/W25Q128 (U5) 方框 |
| U1 | SX1262 | 850–960 MHz LoRa 收发器 | 图 7bce7557076f / 第 1 页 / 系统框图上方 LoRa Transceiver SX1262 (U1) 方框 |
| RF Switch SPDT | 0900FM15K0039 | LoRa 射频收发路径切换 | 图 7bce7557076f / 第 1 页 / 系统框图上方 SX1262 右侧 RF Switch SPDT 0900FM15K0039 方框 |
| U8 | SGM13005L4 | LoRa 接收低噪声放大器 | 图 7bce7557076f / 第 1 页 / 系统框图上方 Low Noise Amplifier SGM13005L4 (U8) 方框 |
| U3 | FM8625H | LoRa 射频开关/放大器 | 图 7bce7557076f / 第 1 页 / 系统框图右上 RF Switch/Amplifier FM8625H (U3) 方框 |
| I/O Expander #1/#2 | PI4IOE5V6408 | 按键、LoRa 控制、电源、LCD、Grove、VIN 检测和 LED 的 IO 扩展 | 图 343dbda5cdf7 / 第 1 页 / 页左下 I/O Expanders (PI4IOE5V6408) 注记，列出 E0 0x43 与 E1 0x44 的职责 |
| LCD | ST7789 | 1.14 英寸 135×240 IPS LCD 驱动器 | 图 343dbda5cdf7 / 第 1 页 / 页右侧 LCD TOUCHSCREEN DISPLAY 表，标注 ST7789、1.14 inch、135×240 |
| TP | FT6336 | 电容触摸控制器 | 图 343dbda5cdf7 / 第 1 页 / 页右侧 LCD TOUCHSCREEN DISPLAY 下半部 FT6336 接口表 |
| U7 (IMU) | BMI270 | 六轴 IMU | 图 343dbda5cdf7 / 第 1 页 / 页左侧 IMU BMI270 MODULE 接口表 |
| U2 | BQ27220YZFR | 电池电量计 | 图 7bce7557076f / 第 1 页 / 系统框图左下 Battery Fuel Gauge BQ27220YZFR (U2) 方框 |
| U1 (PMU) | AW32001ECSR | 电源管理单元 | 图 7bce7557076f / 第 1 页 / 系统框图左下 Power Management Unit AW32001ECSR (U1) 方框 |
| U5 (power) | PMS150G | 电源管理控制器 | 图 7bce7557076f / 第 1 页 / 系统框图下方 Power Management IC PMS150G (U5) 方框 |
| U6 | JW5712 | 降压转换器 | 图 7bce7557076f / 第 1 页 / 系统框图下方 Step-Down Converter JW5712 (U6) 方框 |
| U4 (power) | SGM6603 | 5V 输出升压转换器 | 图 7bce7557076f / 第 1 页 / 系统框图中下 Step-Up Converter SGM6603 (U4) 方框及 5VOUT_EN 连线 |
| BZ1 | 4 kHz Buzzer | 蜂鸣器 | 图 7bce7557076f / 第 1 页 / 系统框图左侧 4 KHz Buzzer BUZZER (BZ1) 方框 |
| LED4 | MHS153IRCT | 红外发射 LED | 图 7bce7557076f / 第 1 页 / 系统框图左侧 IR Transmitter LED MHS153IRCT (LED4) 方框 |

## 系统结构

### 主控制器

系统主控制器为 ESP32-C6，系统框图标注为 RISC-V 32-bit。

- 参数与网络：`part_number=ESP32-C6`；`architecture=RISC-V 32-bit`；`reference=U4/U8`
- 证据：图 7bce7557076f / 第 1 页 / 系统框图中央黄色 ESP32-C6 RISC-V 32-bit 方框

## 电源

### 8 Pin 扩展口电池脚

8 Pin 扩展口的 BATTERY OUT 为未稳压 3–4.2 V 电池轨，仅允许输出，不得反向供电。

- 参数与网络：`pin=6`；`voltage_v=3-4.2`；`regulated=false`；`direction=output-only`；`backfeed_allowed=false`
- 证据：图 1b2349863a66 / 第 1 页 / 8 PIN EXPANSION PORT 下方橙框：Unregulated ~3-4.2 V battery rail, output-only. Do not back-feed

### 内置锂电池

设备内置 250 mAh 锂聚合物电池；功能框图将电池电压范围标为 3.7–4.2 V。

- 参数与网络：`capacity_mah=250`；`voltage_range_v=3.7-4.2`；`chemistry=LiPo`
- 证据：图 c054f406cf7a / 第 1 页 / 功能框图左上 BATTERY 250mAh 方框及 3.7~4.2V 标注; 图 f27a232d9e2d / 第 1 页 / 页右侧 BUILT-IN 250mAh LIPO BATTERY 标注

### 电源管理链

电源链包含 BQ27220YZFR 电量计、AW32001ECSR 电源管理单元、PMS150G 电源管理控制器、JW5712 降压转换器和 SGM6603 升压转换器；SGM6603 的 5VOUT_EN 由 E1.P2 控制。

- 参数与网络：`fuel_gauge=BQ27220YZFR`；`pmu=AW32001ECSR`；`controller=PMS150G`；`step_down=JW5712`；`step_up=SGM6603`；`five_v_enable=E1.P2`
- 证据：图 7bce7557076f / 第 1 页 / 系统框图下方电源管理器件方框和 5VOUT_EN 连线; 图 c054f406cf7a / 第 1 页 / 功能框图左侧电池、BQ27220、AW32001、PMS150G、JW5712、SGM6603 与 VSYS_BUS/5V_OUT 电源链

### 电源按钮与关机控制

Power On/Reset/Power Off 按钮的 POWEROFF 信号连接 E1.P0；该按钮用于开机、复位、关机和进入 Bootloader 模式。

- 参数与网络：`poweroff=E1.P0`；`functions=power on,reset,power off,bootloader`
- 证据：图 e33c2a0b31f7 / 第 1 页 / 页右下 Power On / Reset / Power Off 表，标注 E1.P0 POWEROFF 及四种操作

## 接口

### ST7789 LCD

ST7789 1.14 英寸 IPS LCD 分辨率为 135×240；MOSI=GPIO21、SCK=GPIO20、CS=GPIO17、RS=GPIO16，RESET=E1.P1，BACKLIGHT=E1.P6。

- 参数与网络：`part_number=ST7789`；`resolution=135x240`；`mosi=GPIO21`；`sck=GPIO20`；`cs=GPIO17`；`rs=GPIO16`；`reset=E1.P1`；`backlight=E1.P6`
- 证据：图 343dbda5cdf7 / 第 1 页 / 页右侧 LCD TOUCHSCREEN DISPLAY 上半部 ST7789 引脚映射表和分辨率标注

### Qwiic 接口

Qwiic 4 针接口的 1 至 4 脚依次为 GND、3V3 OUT、SDA/GPIO10、SCL/GPIO8。

- 参数与网络：`pinout=1:GND,2:3V3_OUT,3:SDA/GPIO10,4:SCL/GPIO8`；`bus=I2C0`
- 证据：图 e33c2a0b31f7 / 第 1 页 / 页右侧 QWIIC CONNECTOR 1–4 脚表

### Grove 接口

Grove 4 针接口的 1 至 4 脚依次为 GND、5V OUT、GROVE_IO_0/GPIO5、GROVE_IO_1/GPIO4，GROVE_POWER_EN 由 E1.P2 控制。

- 参数与网络：`pinout=1:GND,2:5V_OUT,3:GPIO5,4:GPIO4`；`power_enable=E1.P2`
- 证据：图 27ab0be9cc30 / 第 1 页 / 页右侧 GROVE CONNECTOR 1–4 脚表及 GROVE_POWER_EN E1.P2; 图 f27a232d9e2d / 第 1 页 / 页左侧 Grove Connector 引脚表及 E1.P2 电源使能

### USB-C 接口

USB-C 接口用于编程与锂电池充电；USB D-=GPIO12、USB D+=GPIO13，VBUS 为输入，VIN_DETECT 连接 E1.P5。

- 参数与网络：`usb_d_minus=GPIO12`；`usb_d_plus=GPIO13`；`vbus_direction=input`；`vin_detect=E1.P5`；`uses=programming,battery charging`
- 证据：图 f27a232d9e2d / 第 1 页 / 页中下 USB-C PORT 表及 Program the board and recharge lipo battery 注记；右侧 VIN_DETECT=E1.P5

### 8 Pin Expansion Port

8 Pin 扩展口的 1 至 8 脚依次为 GND、5V OUT、GPIO7、GPIO2、GPIO6、BATTERY OUT、3V3 OUT、5V IN，并兼容 M5Stack HAT 系列。

- 参数与网络：`pinout=1:GND,2:5V_OUT,3:GPIO7,4:GPIO2,5:GPIO6,6:BATTERY_OUT,7:3V3_OUT,8:5V_IN`；`compatibility=M5Stack HAT series`
- 证据：图 1b2349863a66 / 第 1 页 / 页左上 8 PIN EXPANSION PORT 1–8 脚表及左下兼容性注记

## 总线

### LCD 与 LoRa 的 SPI2

LCD 与 LoRa 共用 SPI2：GPIO21 为 MOSI、GPIO20 为 SCK；LCD CS 为 GPIO17，LoRa CS 为 GPIO23，图面明确要求两者不得同时访问。

- 参数与网络：`mosi=GPIO21`；`sck=GPIO20`；`lcd_cs=GPIO17`；`lora_cs=GPIO23`；`simultaneous_access=false`
- 证据：图 7bce7557076f / 第 1 页 / 系统框图右下 ESP32-C6 Buses 注记，列出 SPI2 G20/G21/G22、LCD CS:G17、LoRa CS:G23 和 no simultaneous access

### 共享 I2C0

I2C0 使用 GPIO10(SDA) 和 GPIO8(SCL)，由触摸、IMU、电池电量计、电源管理、两颗 IO 扩展器、Qwiic 与 HAT 侧外设共享。

- 参数与网络：`sda=GPIO10`；`scl=GPIO8`；`bus=I2C0`；`shared=true`
- 证据：图 7bce7557076f / 第 1 页 / 系统框图蓝色 I2C0 连线及右下 ESP32-C6 Buses 注记; 图 c054f406cf7a / 第 1 页 / 功能框图右上 SDA:G10、SCL:G8 总线标注及各 I2C 外设连线

## 总线地址

### PI4IOE5V6408 地址

详细 Pinout 页将 E0 标为 0x43（buttons & LoRa control），E1 标为 0x44（power/UI、LCD reset/backlight、Grove power、VIN detect、LED）。

- 参数与网络：`e0_address=0x43`；`e1_address=0x44`；`part_number=PI4IOE5V6408`
- 证据：图 343dbda5cdf7 / 第 1 页 / 页左下 I/O Expanders (PI4IOE5V6408) 注记，明确 E0 @ 0x43、E1 @ 0x44; 图 82b6b1d8636e / 第 1 页 / 页左下重复的 I/O Expanders 地址与职责注记

## GPIO 与控制信号

### 用户按键

KEY1 连接 E0.P0，KEY2 连接 E0.P1。

- 参数与网络：`key1=E0.P0`；`key2=E0.P1`
- 证据：图 343dbda5cdf7 / 第 1 页 / 页下方 USER BUTTON 标注 E0.P0 KEY1; 图 82b6b1d8636e / 第 1 页 / 页下方 USER BUTTON 标注 E0.P1 KEY2

### 红外发射 LED

红外发射 LED4（MHS153IRCT）的 IR_TX_PIN 连接 ESP32-C6 GPIO9。

- 参数与网络：`reference=LED4`；`part_number=MHS153IRCT`；`gpio=GPIO9`；`signal=IR_TX_PIN`
- 证据：图 7bce7557076f / 第 1 页 / 系统框图左侧 IR Transmitter LED MHS153IRCT (LED4) 至 GPIO_9 连线; 图 1b2349863a66 / 第 1 页 / 页上方 IR EMITTER 标注 GPIO9 与 IR_TX_PIN

### 内置绿色 LED

内置绿色 LED 的 LED_BUILTIN 信号由 E1.P7 控制。

- 参数与网络：`color=green`；`control=E1.P7`；`signal=LED_BUILTIN`
- 证据：图 e33c2a0b31f7 / 第 1 页 / 页下方 BUILTIN LED (GREEN) 标注 E1.P7 与 LED_BUILTIN

## 时钟

### SX1262 参考时钟

SX1262 的 XTA 网络连接 32 MHz 参考振荡器。

- 参数与网络：`frequency_mhz=32`；`signal=XTA`
- 证据：图 7bce7557076f / 第 1 页 / 系统框图上方 SX1262 XTA 与 Crystal Osc. 32 MHz Ref. 方框

## 保护电路

### LoRa 天线使用限制

LoRa 无线模块使用时必须连接天线；图面警告未接天线使用会损坏 LoRa 模块。

- 参数与网络：`antenna_required=true`；`risk=module damage`
- 证据：图 82b6b1d8636e / 第 1 页 / 页右侧红色 WARNING：always use the LoRa radio module with its antenna connected

### GPIO 电平限制

所有 GPIO 仅支持 3.3 V 逻辑且不耐受 5 V。

- 参数与网络：`logic_voltage_v=3.3`；`five_v_tolerant=false`
- 证据：图 1b2349863a66 / 第 1 页 / 页右下 WARNING：All GPIO pins are 3.3 V logic only and are not 5V tolerant

### 锂电池操作安全

图面要求小心处理内置 LiPo 电池，不得穿刺、短路或暴露于高温。

- 参数与网络：`avoid_puncture=true`；`avoid_short_circuit=true`；`avoid_high_temperature=true`
- 证据：图 f27a232d9e2d / 第 1 页 / 页右下 LiPo battery WARNING，列出 puncture、short-circuit、high temperatures 风险

## 存储

### 外部 Flash

U5 为 GD25Q128 或 W25Q128，容量标注为 16 MB，并通过专用 SPI_Flash 总线连接 ESP32-C6。

- 参数与网络：`reference=U5`；`part_number=GD25Q128/W25Q128`；`capacity_mb=16`；`bus=SPI_Flash dedicated`
- 证据：图 7bce7557076f / 第 1 页 / 系统框图左下 Flash 16 MB 方框、SPI_Flash 连线及右下总线说明

## 音频

### 蜂鸣器

4 kHz 蜂鸣器 BZ1 的 BEEP_PIN 连接 ESP32-C6 GPIO11。

- 参数与网络：`reference=BZ1`；`frequency_hz=4000`；`gpio=GPIO11`；`signal=BEEP_PIN`
- 证据：图 7bce7557076f / 第 1 页 / 系统框图左侧 4 KHz Buzzer (BZ1) 至 GPIO_11 连线; 图 e33c2a0b31f7 / 第 1 页 / 页左侧 BUZZER 标注 GPIO11 与 BEEP_PIN

## 传感器

### FT6336 触摸控制器

FT6336 通过 I2C 连接，SDA=GPIO10、SCL=GPIO8、TOUCH_INT=GPIO3，7 位地址为 0x38。

- 参数与网络：`part_number=FT6336`；`sda=GPIO10`；`scl=GPIO8`；`interrupt=GPIO3`；`i2c_address=0x38`
- 证据：图 343dbda5cdf7 / 第 1 页 / 页右侧 FT6336 表，列出 GPIO10、GPIO8、GPIO3 以及 Capacitive Touch I2C addr: 0x38

### BMI270 IMU

BMI270 通过 I2C 连接，SCL=GPIO8、SDA=GPIO10、IMU_INT=GPIO3，7 位地址为 0x68。

- 参数与网络：`part_number=BMI270`；`scl=GPIO8`；`sda=GPIO10`；`interrupt=GPIO3`；`i2c_address=0x68`
- 证据：图 343dbda5cdf7 / 第 1 页 / 页左侧 IMU BMI270 MODULE 表及 BMI270 I2C addr: 0x68 注记

## 射频

### SX1262 数字接口

SX1262 的 MOSI=GPIO21、SCK=GPIO20、CS=GPIO23、MISO=GPIO22、BUSY=GPIO19、IRQ/DIO1=GPIO15；RESET=E0.P7、ANTENNA_SWITCH=E0.P6、LNA_ENABLE=E0.P5。

- 参数与网络：`mosi=GPIO21`；`sck=GPIO20`；`cs=GPIO23`；`miso=GPIO22`；`busy=GPIO19`；`irq_dio1=GPIO15`；`reset=E0.P7`；`antenna_switch=E0.P6`；`lna_enable=E0.P5`
- 证据：图 82b6b1d8636e / 第 1 页 / 页左侧 LoRa SX1262 MODULE 引脚映射表

### LoRa 射频链

SX1262 的 RFO/RFIP/RFIN 经 0900FM15K0039 SPDT、SGM13005L4 LNA 和 FM8625H 射频开关/放大器连接外置 LoRa MMCX 天线；工作频段标注为 850–960 MHz。

- 参数与网络：`transceiver=SX1262`；`spdt=0900FM15K0039`；`lna=SGM13005L4`；`rf_switch_amplifier=FM8625H`；`connector=MMCX`；`frequency_range_mhz=850-960`
- 证据：图 c054f406cf7a / 第 1 页 / 功能框图右下蓝色 LoRa 射频区域，含 SX1262、0900FM15K0039、SGM13005L4、FM8625H 与 MMCX; 图 82b6b1d8636e / 第 1 页 / 页中央外置 LoRa MMCX Connector 和 LoRa Antenna 850–960 MHz 标注

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 主控制器 | `part_number=ESP32-C6`；`architecture=RISC-V 32-bit`；`reference=U4/U8` |
| 存储 | 外部 Flash | `reference=U5`；`part_number=GD25Q128/W25Q128`；`capacity_mb=16`；`bus=SPI_Flash dedicated` |
| 总线 | LCD 与 LoRa 的 SPI2 | `mosi=GPIO21`；`sck=GPIO20`；`lcd_cs=GPIO17`；`lora_cs=GPIO23`；`simultaneous_access=false` |
| 总线 | 共享 I2C0 | `sda=GPIO10`；`scl=GPIO8`；`bus=I2C0`；`shared=true` |
| 接口 | ST7789 LCD | `part_number=ST7789`；`resolution=135x240`；`mosi=GPIO21`；`sck=GPIO20`；`cs=GPIO17`；`rs=GPIO16`；`reset=E1.P1`；`backlight=E1.P6` |
| 传感器 | FT6336 触摸控制器 | `part_number=FT6336`；`sda=GPIO10`；`scl=GPIO8`；`interrupt=GPIO3`；`i2c_address=0x38` |
| 传感器 | BMI270 IMU | `part_number=BMI270`；`scl=GPIO8`；`sda=GPIO10`；`interrupt=GPIO3`；`i2c_address=0x68` |
| 射频 | SX1262 数字接口 | `mosi=GPIO21`；`sck=GPIO20`；`cs=GPIO23`；`miso=GPIO22`；`busy=GPIO19`；`irq_dio1=GPIO15`；`reset=E0.P7`；`antenna_switch=E0.P6`；`lna_enable=E0.P5` |
| 射频 | LoRa 射频链 | `transceiver=SX1262`；`spdt=0900FM15K0039`；`lna=SGM13005L4`；`rf_switch_amplifier=FM8625H`；`connector=MMCX`；`frequency_range_mhz=850-960` |
| 时钟 | SX1262 参考时钟 | `frequency_mhz=32`；`signal=XTA` |
| 保护电路 | LoRa 天线使用限制 | `antenna_required=true`；`risk=module damage` |
| 总线地址 | PI4IOE5V6408 地址 | `e0_address=0x43`；`e1_address=0x44`；`part_number=PI4IOE5V6408` |
| 总线地址 | IO 扩展器地址记录冲突 | `system_diagram_addresses=0x20,0x21`；`pinout_addresses=0x43,0x44` |
| GPIO 与控制信号 | 用户按键 | `key1=E0.P0`；`key2=E0.P1` |
| 音频 | 蜂鸣器 | `reference=BZ1`；`frequency_hz=4000`；`gpio=GPIO11`；`signal=BEEP_PIN` |
| GPIO 与控制信号 | 红外发射 LED | `reference=LED4`；`part_number=MHS153IRCT`；`gpio=GPIO9`；`signal=IR_TX_PIN` |
| 接口 | Qwiic 接口 | `pinout=1:GND,2:3V3_OUT,3:SDA/GPIO10,4:SCL/GPIO8`；`bus=I2C0` |
| 接口 | Grove 接口 | `pinout=1:GND,2:5V_OUT,3:GPIO5,4:GPIO4`；`power_enable=E1.P2` |
| 接口 | USB-C 接口 | `usb_d_minus=GPIO12`；`usb_d_plus=GPIO13`；`vbus_direction=input`；`vin_detect=E1.P5`；`uses=programming,battery charging` |
| 接口 | 8 Pin Expansion Port | `pinout=1:GND,2:5V_OUT,3:GPIO7,4:GPIO2,5:GPIO6,6:BATTERY_OUT,7:3V3_OUT,8:5V_IN`；`compatibility=M5Stack HAT series` |
| 电源 | 8 Pin 扩展口电池脚 | `pin=6`；`voltage_v=3-4.2`；`regulated=false`；`direction=output-only`；`backfeed_allowed=false` |
| 电源 | 内置锂电池 | `capacity_mah=250`；`voltage_range_v=3.7-4.2`；`chemistry=LiPo` |
| 电源 | 电源管理链 | `fuel_gauge=BQ27220YZFR`；`pmu=AW32001ECSR`；`controller=PMS150G`；`step_down=JW5712`；`step_up=SGM6603`；`five_v_enable=E1.P2` |
| 电源 | 电源按钮与关机控制 | `poweroff=E1.P0`；`functions=power on,reset,power off,bootloader` |
| GPIO 与控制信号 | 内置绿色 LED | `color=green`；`control=E1.P7`；`signal=LED_BUILTIN` |
| 保护电路 | GPIO 电平限制 | `logic_voltage_v=3.3`；`five_v_tolerant=false` |
| 保护电路 | 锂电池操作安全 | `avoid_puncture=true`；`avoid_short_circuit=true`；`avoid_high_temperature=true` |

## 待确认事项

- `address.io_expander_conflict`：系统框图的 Reserved I2C addresses 列表包含 0x20 和 0x21，而详细 Pinout 页把两颗 PI4IOE5V6408 标为 0x43 和 0x44；两套图面记录不一致。（证据：图 7bce7557076f / 第 1 页 / 系统框图右下 Reserved I2C addresses 列表包含 0x20、0x21; 图 343dbda5cdf7 / 第 1 页 / 详细 Pinout 页左下明确标注 E0 @ 0x43、E1 @ 0x44）
- `review.io_expander_addresses`：系统框图中的 0x20/0x21 是否为旧版本或误写，当前 DK001 硬件上两颗 PI4IOE5V6408 是否应统一按详细 Pinout 的 0x43/0x44 使用？；原因：系统框图只在 Reserved I2C addresses 列表中出现 0x20/0x21，详细 Pinout 多页则明确写 E0=0x43、E1=0x44，图面记录冲突，不能仅凭现有资源消除。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c054f406cf7a710da56d74c38020171cf78741a29f07ea113aed4647146c987a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001-sche_02.png` |
| 2 | 1 | `7bce7557076fa017d2a7158af3df63e68c6f412c15baa0266b38a2de42d93e82` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/DK001-sche.png` |
| 3 | 1 | `343dbda5cdf7ebb88e917073bea90c929cda28dd647a94afd970c14b34a3674d` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_01.png` |
| 4 | 1 | `82b6b1d8636e0997ddc947a5f725f6011048d9d8c976f595dd8518805b091f9a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_02.png` |
| 5 | 1 | `e33c2a0b31f78a9dc0ae4f3cbb1984fa49ef4ab6692fba4414abc2a2126ff9bb` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_03.png` |
| 6 | 1 | `27ab0be9cc303b18ca582bd4d743aa6e602309b6edfa41ddc03a2caa4a9cb473` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_04.png` |
| 7 | 1 | `f27a232d9e2dcb7eefcc10c920d3081f818e7452e78d4263f56ba28233f2a669` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_05.png` |
| 8 | 1 | `1b2349863a66d260d8ff0ebaf00703787890dc680b8833e334f165b05fabcd7b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/TPX00227-full-pinout_page_06.png` |

---

源文档：`zh_CN/core/Arduino_Nesso_N1.md`

源文档 SHA-256：`2231c4e2a5f142bf2ceb7269047f33ab74ee574d5ff98a8288a3ff811163a902`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
