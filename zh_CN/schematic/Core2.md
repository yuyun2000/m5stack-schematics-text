# Core2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Core2 |
| SKU | K010 |
| 产品 ID | `core2-51bd4e3e1bdb` |
| 源文档 | `zh_CN/core/core2.md` |

## 概述

Core2 V1.0 核心板以 ESP32-D0WDQ6 为主控，搭配 XM25QH128B Flash、ESPPSRAM64H PSRAM、AXP192 PMU、BM8563 RTC、CP2104 USB-UART、NS4168 I2S 功放、SY7088 5V升压、LCD/触摸和 microSD。AXP192 从 USB_5V/SYS_VBAT 供电并生成 MCU_VDD、IPS_BUS、RTC_VDD、PERI_VDD 与 VIB_MOTOR，GPIO1/2/4 分别控制系统LED、扬声器使能和LCD/触摸复位。扩展底板通过 M5_BUS 的 G21/G22、G0/G34 连接 MPU-6886 I2C 与 SPM1423 PDM 麦克风；当前正式资源仍是 V1.0，后续 USB 芯片、电池容量和 RTC 备份电池变更需按实际硬件确认。

## 检索关键词

`Core2`、`K010`、`CORE2_V1.0`、`ESP32-D0WDQ6`、`AXP192`、`XM25QH128B`、`ESPPSRAM64H`、`CP2104-F03-GMR`、`BM8563`、`MPU-6886`、`SPM1423HM4H-B`、`NS4168`、`SY7088`、`ILI9342C`、`FT6336U`、`M5_BUS`、`G21 SYS_SDA`、`G22 SYS_SCL`、`G39 TOUCH_INT`、`G23 MOSI`、`G38 MISO`、`G18 SCK`、`G5 LCD_CS`、`G15 LCD_DC`、`G4 SD_CS`、`G2 I2S_DOUT`、`G0 I2S_LRCK MIC_CLK`、`G12 I2S_BCLK`、`G34 MIC_DATA`、`RTC_VDD`、`PERI_VDD`、`VIB_MOTOR`、`IPS_BUS`、`SYS_VBAT`、`USB Type-C`、`microSD`、`PORT-A`、`M5Stack BUS`、`RTC_BAT`、`PWR_KEY`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | AXP192 | 系统PMU，管理USB/电池输入、充电、DCDC/LDO、电源键、LED、扬声器和马达电源 | 图 6c305db1571c / 第 1 页 / 核心板页 A1-B1 PMU区 U4 AXP192，ACIN/VBUS/BAT、DCDC1-3、LDO1-3、GPIO0-4 |
| MCU | ESP32-D0WDQ6 | Core2主控，连接存储、显示、I2C、I2S、UART、microSD和M5-Bus | 图 6c305db1571c / 第 1 页 / 核心板页 A2-B3 MCU区 ESP32-D0WDQ6，GPIO0-39、晶振、射频和电源 |
| U1 | XM25QH128B | ESP32外部SPI Flash | 图 6c305db1571c / 第 1 页 / 核心板页 D1 FLASH区 U1 XM25QH128B |
| U2 | ESPPSRAM64H | ESP32外部SPI PSRAM | 图 6c305db1571c / 第 1 页 / 核心板页 D1 PSRAM区 U2 ESPPSRAM64H |
| U3 | CP2104-F03-GMR | USB转UART下载芯片，连接ESP32 UART0与自动复位/下载网络 | 图 6c305db1571c / 第 1 页 / 核心板页 C1 USB2UART区 U3 CP2104-F03-GMR |
| J3,FU1,D8 | TYPEC_16P / 1A 6V fuse / SRV05-4 | USB-C数据/供电输入及过流、ESD保护 | 图 6c305db1571c / 第 1 页 / 核心板页 B3 USB区 J3 TYPEC_16P、FU1、USB_DP/DM、D8 |
| RTC | BM8563 | 连接G21/G22 I2C与PWR_KEY中断的RTC | 图 6c305db1571c / 第 1 页 / 核心板页 D1-D2 RTC区 BM8563、32.768K晶振、SDA/SCL/INT |
| U6 | NS4168 | 由ESP32 I2S驱动的扬声器功放 | 图 6c305db1571c / 第 1 页 / 核心板页 C2 SPEAKER区 U6 NS4168，LRCK/BCLK/SADATA/CTRL与PAD1 |
| U8 | SY7088 | IPS_BUS到BUS_5V的升压转换器 | 图 6c305db1571c / 第 1 页 / 核心板页 C2-C3 5V_BOOST区 U8 SY7088、L4 2.2uH与反馈 |
| LCD1 | M5_CORE2_LCD_10P | LCD SPI、电源、背光和复位接口 | 图 6c305db1571c / 第 1 页 / 核心板页 B4-C4 LCD区 LCD1 M5_CORE2_LCD_10P |
| CTP1 | CTP_2.0inch | 电容触摸屏I2C、INT和RST接口 | 图 6c305db1571c / 第 1 页 / 核心板页 C4 C-TP区 CTP1，SDA/SCL/INT/RST/VDD/GND |
| TF_CARD_SOCKET | TF_CARD_SOCKET | G4/G23/G18/G38 SPI microSD卡槽 | 图 6c305db1571c / 第 1 页 / 核心板页 D2-D3 TF_CARD区，DAT0/MISO、CMD/MOSI、CLK、DAT3/CS |
| BUS1 | M5_BUS | 30针M5Stack堆叠总线，承载GPIO、I2C、I2S、UART与电源 | 图 6c305db1571c / 第 1 页 / 核心板页 A3-B3 BUS1 M5_BUS 1-30脚 |
| J4 | PORT-A | G33/G32、BUS_5V、GND四针外部接口 | 图 6c305db1571c / 第 1 页 / 核心板页 C3 EXT.PORTA J4，IO2 G33、IO1 G32、5V、GND |
| J5 | M1250V-02P | SYS_VBAT与GND外部电池接口 | 图 6c305db1571c / 第 1 页 / 核心板页 C3 EXT.BATT J5，SYS_VBAT/GND |
| PAD2,D2 | VIB_MOTOR_PAD / 4148 | AXP192 LDO3供电的震动马达连接和反向钳位 | 图 6c305db1571c / 第 1 页 / 核心板页 C2 VIB_MOTOR区 PAD2、D2 4148、VIB_MOTOR |
| LED1 | GREEN LED | 由AXP192 SYS_LED/GPIO1驱动的绿色系统电源LED | 图 6c305db1571c / 第 1 页 / 核心板页 C2 LED区 LED1 GREEN、SYS_LED |
| S1,S2 | TS-015 | MCU_RST与PWR_KEY按键 | 图 6c305db1571c / 第 1 页 / 核心板页 D2 BUTTON区 S1 MCU_RST、S2 PWR_KEY |
| ANT1,X1 | 2.4GHz antenna / X2520-40MMB4SC | ESP32 2.4GHz射频匹配和40MHz晶振 | 图 6c305db1571c / 第 1 页 / 核心板页 A2 ANT1射频网络与B2 X1 40MHz/C3/C4 |
| U1 | MPU-6886 | 扩展底板六轴IMU，连接IMU_SDA/IMU_SCL | 图 112373303e35 / 第 1 页 / 扩展板页 C2 U1 MPU-6886，SDA/SCL/INT/供电 |
| U2 | SPM1423HM4H-B | 扩展底板PDM麦克风，连接MIC_CLK/MIC_DAT | 图 112373303e35 / 第 1 页 / 扩展板页 C2 U2 SPM1423HM4H-B，CLK/DATA/VCC/GND |
| D3-D8 | SRV05-4 | M5_BUS外部GPIO、USB与复位网络的多路ESD保护阵列 | 图 6c305db1571c / 第 1 页 / 核心板页 A4-B4 ESD区 D3-D8 SRV05-4 |
| BT1 | BATTERY_RTC | V1.0图中BM8563 RTC_BAT备份电池 | 图 6c305db1571c / 第 1 页 / 核心板页 D1 RTC区 BT1 BATTERY_RTC/RTC_BAT |

## 系统结构

### Core2 V1.0系统架构

ESP32-D0WDQ6连接16MB Flash、8MB PSRAM、LCD/触摸、microSD、RTC、USB-UART、I2S功放和M5_BUS；AXP192负责多路电源，扩展底板提供MPU-6886与SPM1423。

- 参数与网络：`mcu=ESP32-D0WDQ6`；`pmu=U4 AXP192`；`flash=XM25QH128B`；`psram=ESPPSRAM64H`；`rtc=BM8563`；`usb_uart=CP2104-F03-GMR`；`bottom=MPU-6886 + SPM1423HM4H-B`
- 证据：图 6c305db1571c / 第 1 页 / 核心板完整页; 图 112373303e35 / 第 1 页 / 扩展底板完整页

## 电源

### AXP192输入与电池

AXP192 ACIN/VBUS接USB_5V/BUS_5V，BAT pins34/35接SYS_VBAT，TS经电容接GND；J5与M5_BUS pin30引出SYS_VBAT。

- 参数与网络：`usb_input=USB_5V`；`bus_input=BUS_5V`；`battery=SYS_VBAT`；`external_battery=J5`；`bus_battery=BUS1 pin30`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 A1 U4 ACIN/VBUS/BAT/TS与BUS1/J5

### AXP192电源轨

DCDC1经L3生成MCU_VDD，DCDC3经L2形成IPS_BUS/LCD背光路径，LDO1=RTC_VDD，LDO2=PERI_VDD，LDO3=VIB_MOTOR。

- 参数与网络：`dcdc1=MCU_VDD`；`dcdc3=IPS_BUS/LCD_BL`；`ldo1=RTC_VDD`；`ldo2=PERI_VDD`；`ldo3=VIB_MOTOR`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 A1-B1 AXP192 DCDC1-3/LDO1-3输出

### IPS_BUS到BUS_5V升压

U8 SY7088由IPS_BUS供电，LX经L4 2.2uH产生BUS_5V，反馈为R31 15KΩ与R32/R33 47KΩ网络。

- 参数与网络：`input=IPS_BUS`；`converter=U8 SY7088`；`inductor=L4 2.2uH`；`output=BUS_5V`；`feedback=R31 15KΩ; R32/R33 47KΩ`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 C2-C3 5V_BOOST U8/L4/反馈

## 接口

### 电容触摸接口

CTP1 SDA=G21、SCL=G22、INT=G39、RST=LCD_RST，VDD经R65 47Ω来自MCU_VDD。

- 参数与网络：`sda=G21`；`scl=G22`；`interrupt=G39`；`reset=LCD_RST`；`power=MCU_VDD via R65 47Ω`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 C4 C-TP CTP1

### USB-C接口

J3 DP/DM经FU1与ESD网络连接USB_DP/USB_DM和CP2104，CC1/CC2各由5.1KΩ下拉，VBUS形成USB_5V。

- 参数与网络：`connector=J3 TYPEC_16P`；`data=USB_DP/USB_DM`；`cc=5.1KΩ pull-downs`；`protection=FU1 1A/6V; D8 SRV05-4`；`power=USB_5V`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 B3 USB J3/FU1/D8

### M5_BUS主要映射

BUS1 pin7/9/11为G23 MOSI/G38 MISO/G18 SCK，pin13/14为G3 RXD0/G1 TXD0，pin17/18为G21/G22内部I2C，pin19/20为G32/G33外部I2C，pin23/24/26为G2/G0/G34音频。

- 参数与网络：`spi=pin7 G23; pin9 G38; pin11 G18`；`uart0=pin13 G3; pin14 G1`；`internal_i2c=pin17 G21; pin18 G22`；`external_i2c=pin19 G32; pin20 G33`；`audio=pin23 G2; pin24 G0; pin26 G34`；`power=pin12 3V3; pin28 5V; pin30 BAT`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 A3-B3 BUS1 M5_BUS

### PORT-A接口

J4 PORT-A pin4=G33/IO2、pin3=G32/IO1、pin2=BUS_5V、pin1=GND，外部I2C由R59/R60各5.1KΩ上拉MCU_VDD。

- 参数与网络：`pin4=G33`；`pin3=G32`；`pin2=BUS_5V`；`pin1=GND`；`pullups=R59/R60 5.1KΩ`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 C3 J4 PORT-A与D4 EXT.I2C PULLUP

## 总线

### 内部I2C总线

ESP32 G21=SYS_SDA、G22=SYS_SCL，连接AXP192、BM8563和触摸接口，并经R57/R58各2.2KΩ上拉MCU_VDD；扩展底板MPU-6886同样接入。

- 参数与网络：`sda=G21 SYS_SDA`；`scl=G22 SYS_SCL`；`devices=AXP192, BM8563, CTP1, MPU-6886`；`pullups=R57/R58 2.2KΩ`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页U4/RTC/CTP/BUS1与INTERNAL I2C PULLUP; 图 112373303e35 / 第 1 页 / 扩展板页U1 IMU_SDA/IMU_SCL到BUS1 G21/G22

### LCD SPI映射

LCD1 MOSI=G23、MISO=G38、SCK=G18、CS=G5、D/C=G15；RST=LCD_RST，背光=LCD_BL，VDD=PERI_VDD。

- 参数与网络：`mosi=G23`；`miso=G38`；`sck=G18`；`cs=G5`；`dc=G15`；`reset=LCD_RST`；`backlight=LCD_BL`；`power=PERI_VDD`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 B4-C4 LCD1引脚

### NS4168 I2S映射

ESP32 G12连接U6 BCLK，G0连接LRCK，G2连接SADATA，AXP192 SPK_EN连接CTRL。

- 参数与网络：`bclk=G12`；`lrck=G0`；`data=G2`；`enable=SPK_EN from AXP192 GPIO2`；`amplifier=NS4168`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 C2 SPEAKER U6网络

### CP2104 UART下载

CP2104 TXD经CP_TX/R8连接ESP32 G3/U0RXD，RXD经CP_RX/R7连接G1/U0TXD，Q1/Q2与D1形成自动下载/复位控制。

- 参数与网络：`tx=CP_TX -> G3 U0RXD`；`rx=CP_RX <- G1 U0TXD`；`series=R7/R8 47Ω`；`auto_reset=Q1/Q2 + D1 4148`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 C1 USB2UART U3/Q1/Q2/D1与MCU G1/G3

## GPIO 与控制信号

### AXP192外设控制

AXP192 GPIO1连接SYS_LED，GPIO2连接SPK_EN，GPIO4连接LCD_RST；LDO3直接形成VIB_MOTOR电源。

- 参数与网络：`gpio1=SYS_LED`；`gpio2=SPK_EN`；`gpio4=LCD_RST`；`ldo3=VIB_MOTOR`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 B1 U4 GPIO1/2/4与LED/SPEAKER/LCD网络

### 马达与系统LED

AXP192 LDO3形成VIB_MOTOR并驱动PAD2，D2 4148反向钳位；AXP GPIO1的SYS_LED经R18/R19驱动LED1 GREEN。

- 参数与网络：`motor=LDO3 VIB_MOTOR -> PAD2; D2 4148`；`led=GPIO1 SYS_LED -> LED1 GREEN`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 C2 VIB_MOTOR与LED区

## 时钟

### ESP32主时钟

ESP32 XTAL_P/N连接X1 X2520-40MMB4SC，C3/C4各12pF接GND，R3 51Ω串联。

- 参数与网络：`crystal=X1 X2520-40MMB4SC`；`frequency=40MHz marking`；`capacitors=C3/C4 12pF`；`series=R3 51Ω`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 B2 X1/R3/C3/C4/XTAL_P/N

### BM8563 RTC时钟

BM8563 OSCI/OSCO连接32.768K晶振及C30/C29各6.8pF，INT连接PWR_KEY网络。

- 参数与网络：`rtc=BM8563`；`crystal=32.768K`；`capacitors=C30/C29 6.8pF`；`interrupt=PWR_KEY`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 D1-D2 RTC BM8563/晶振/PWR_KEY

## 复位

### 复位与电源按键

S1将MCU_RST拉到GND，S2将PWR_KEY拉到GND；MCU_RST由R5 10KΩ上拉，PWR_KEY连接AXP192 PWRON和RTC INT网络。

- 参数与网络：`reset=S1 MCU_RST`；`reset_pullup=R5 10KΩ`；`power=S2 PWR_KEY`；`pmu=AXP192 PWRON`；`rtc_interrupt=BM8563 INT`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 B1/D2 AXP PWRON、RTC INT与BUTTON S1/S2

## 保护电路

### 外部总线ESD

D3-D7 SRV05-4保护多个EXT GPIO，D8保护USB_DP/DM与MCU_RST，所有阵列参考MCU_VDD/GND。

- 参数与网络：`gpio_arrays=D3-D7 SRV05-4`；`usb_reset_array=D8 SRV05-4`；`rails=MCU_VDD/GND`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 A4-B4 ESD D3-D8

## 存储

### microSD SPI映射

TF卡DAT0/MISO=G38、CMD/MOSI=G23、CLK=G18、DAT3/CS=G4，R25-R28各10KΩ上拉PERI_VDD。

- 参数与网络：`miso=G38`；`mosi=G23`；`clk=G18`；`cs=G4`；`pullups=R25-R28 10KΩ`；`power=PERI_VDD`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 D2-D3 TF_CARD_SOCKET

## 内存与 Flash

### 16MB SPI Flash

U1 XM25QH128B通过GPIO11/7/6/8连接CS#/HOLD#/SCLK/SI，并使用MCU_VDD。

- 参数与网络：`device=XM25QH128B`；`cs=GPIO11`；`hold=GPIO7`；`sclk=GPIO6`；`si=GPIO8`；`supply=MCU_VDD`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 D1 FLASH U1网络

### 8MB PSRAM

U2 ESPPSRAM64H通过GPIO8/7/10/9连接SIO0/SIO1/SIO2/SIO3，SCLK=GPIO17、CS#=GPIO16。

- 参数与网络：`device=ESPPSRAM64H`；`sio=GPIO8,GPIO7,GPIO10,GPIO9`；`sclk=GPIO17`；`cs=GPIO16`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 D1 PSRAM U2网络

## 音频

### 底板PDM麦克风

SPM1423 CLK连接M5_BUS pin24/G0 MIC_CLK，DATA连接pin26/G34 MIC_DAT，VCC使用SYS_P033，SELECT接GND。

- 参数与网络：`clock=BUS1 pin24 G0 MIC_CLK`；`data=BUS1 pin26 G34 MIC_DAT`；`supply=SYS_P033`；`select=GND`
- 证据：图 112373303e35 / 第 1 页 / 扩展板页 BUS1与U2 SPM1423 MIC_CLK/MIC_DAT

## 传感器

### 底板MPU-6886

MPU-6886 SCL/SDA连接M5_BUS pin18/G22与pin17/G21，VDD/VDDIO接SYS_P033；INT未连接。

- 参数与网络：`scl=G22 IMU_SCL`；`sda=G21 IMU_SDA`；`supply=SYS_P033`；`interrupt_connected=false`
- 证据：图 112373303e35 / 第 1 页 / 扩展板页 BUS1与U1 MPU-6886

## 射频

### 2.4GHz天线

ESP32 LNA_IN通过L1/C1/C2/R1/R2匹配网络连接ANT1。

- 参数与网络：`soc_pin=LNA_IN`；`antenna=ANT1`；`matching=L1,C1,C2,R1,R2`
- 证据：图 6c305db1571c / 第 1 页 / 核心板页 A2 RF网络与ANT1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Core2 V1.0系统架构 | `mcu=ESP32-D0WDQ6`；`pmu=U4 AXP192`；`flash=XM25QH128B`；`psram=ESPPSRAM64H`；`rtc=BM8563`；`usb_uart=CP2104-F03-GMR`；`bottom=MPU-6886 + SPM1423HM4H-B` |
| 电源 | AXP192输入与电池 | `usb_input=USB_5V`；`bus_input=BUS_5V`；`battery=SYS_VBAT`；`external_battery=J5`；`bus_battery=BUS1 pin30` |
| 电源 | AXP192电源轨 | `dcdc1=MCU_VDD`；`dcdc3=IPS_BUS/LCD_BL`；`ldo1=RTC_VDD`；`ldo2=PERI_VDD`；`ldo3=VIB_MOTOR` |
| GPIO 与控制信号 | AXP192外设控制 | `gpio1=SYS_LED`；`gpio2=SPK_EN`；`gpio4=LCD_RST`；`ldo3=VIB_MOTOR` |
| 电源 | IPS_BUS到BUS_5V升压 | `input=IPS_BUS`；`converter=U8 SY7088`；`inductor=L4 2.2uH`；`output=BUS_5V`；`feedback=R31 15KΩ; R32/R33 47KΩ` |
| 内存与 Flash | 16MB SPI Flash | `device=XM25QH128B`；`cs=GPIO11`；`hold=GPIO7`；`sclk=GPIO6`；`si=GPIO8`；`supply=MCU_VDD` |
| 内存与 Flash | 8MB PSRAM | `device=ESPPSRAM64H`；`sio=GPIO8,GPIO7,GPIO10,GPIO9`；`sclk=GPIO17`；`cs=GPIO16` |
| 时钟 | ESP32主时钟 | `crystal=X1 X2520-40MMB4SC`；`frequency=40MHz marking`；`capacitors=C3/C4 12pF`；`series=R3 51Ω` |
| 射频 | 2.4GHz天线 | `soc_pin=LNA_IN`；`antenna=ANT1`；`matching=L1,C1,C2,R1,R2` |
| 总线 | 内部I2C总线 | `sda=G21 SYS_SDA`；`scl=G22 SYS_SCL`；`devices=AXP192, BM8563, CTP1, MPU-6886`；`pullups=R57/R58 2.2KΩ` |
| 总线地址 | 内部I2C地址 | `axp192=0x34`；`bm8563=0x51`；`ft6336u=0x38`；`mpu6886=0x68`；`schematic_addresses_shown=false` |
| 时钟 | BM8563 RTC时钟 | `rtc=BM8563`；`crystal=32.768K`；`capacitors=C30/C29 6.8pF`；`interrupt=PWR_KEY` |
| 总线 | LCD SPI映射 | `mosi=G23`；`miso=G38`；`sck=G18`；`cs=G5`；`dc=G15`；`reset=LCD_RST`；`backlight=LCD_BL`；`power=PERI_VDD` |
| 接口 | 电容触摸接口 | `sda=G21`；`scl=G22`；`interrupt=G39`；`reset=LCD_RST`；`power=MCU_VDD via R65 47Ω` |
| 其他事实 | LCD面板规格 | `documented_controller=ILI9342C`；`documented_size=2.0 inch`；`documented_resolution=320x240`；`schematic_model_shown=false` |
| 存储 | microSD SPI映射 | `miso=G38`；`mosi=G23`；`clk=G18`；`cs=G4`；`pullups=R25-R28 10KΩ`；`power=PERI_VDD` |
| 总线 | NS4168 I2S映射 | `bclk=G12`；`lrck=G0`；`data=G2`；`enable=SPK_EN from AXP192 GPIO2`；`amplifier=NS4168` |
| 音频 | 底板PDM麦克风 | `clock=BUS1 pin24 G0 MIC_CLK`；`data=BUS1 pin26 G34 MIC_DAT`；`supply=SYS_P033`；`select=GND` |
| 传感器 | 底板MPU-6886 | `scl=G22 IMU_SCL`；`sda=G21 IMU_SDA`；`supply=SYS_P033`；`interrupt_connected=false` |
| 总线 | CP2104 UART下载 | `tx=CP_TX -> G3 U0RXD`；`rx=CP_RX <- G1 U0TXD`；`series=R7/R8 47Ω`；`auto_reset=Q1/Q2 + D1 4148` |
| 接口 | USB-C接口 | `connector=J3 TYPEC_16P`；`data=USB_DP/USB_DM`；`cc=5.1KΩ pull-downs`；`protection=FU1 1A/6V; D8 SRV05-4`；`power=USB_5V` |
| 接口 | M5_BUS主要映射 | `spi=pin7 G23; pin9 G38; pin11 G18`；`uart0=pin13 G3; pin14 G1`；`internal_i2c=pin17 G21; pin18 G22`；`external_i2c=pin19 G32; pin20 G33`；`audio=pin23 G2; pin24 G0; pin26 G34`；`power=pin12 3V3; pin28 5V; pin30 BAT` |
| 接口 | PORT-A接口 | `pin4=G33`；`pin3=G32`；`pin2=BUS_5V`；`pin1=GND`；`pullups=R59/R60 5.1KΩ` |
| GPIO 与控制信号 | 马达与系统LED | `motor=LDO3 VIB_MOTOR -> PAD2; D2 4148`；`led=GPIO1 SYS_LED -> LED1 GREEN` |
| 复位 | 复位与电源按键 | `reset=S1 MCU_RST`；`reset_pullup=R5 10KΩ`；`power=S2 PWR_KEY`；`pmu=AXP192 PWRON`；`rtc_interrupt=BM8563 INT` |
| 保护电路 | 外部总线ESD | `gpio_arrays=D3-D7 SRV05-4`；`usb_reset_array=D8 SRV05-4`；`rails=MCU_VDD/GND` |
| 核心器件 | USB-UART版本 | `schematic_device=CP2104-F03-GMR`；`documented_alternate=CH9102F`；`schematic_revision=CORE2_V1.0` |
| 其他事实 | 电池容量与RTC备份电池版本 | `schematic_rtc_battery=BT1 BATTERY_RTC`；`documented_old_capacity=390mAh`；`documented_new_capacity=500mAh`；`documented_rtc_battery_removed=true` |

## 待确认事项

- `address.documented-i2c`：产品正文给出AXP192=0x34、BM8563=0x51、FT6336U=0x38、MPU6886=0x68，但两张原理图只显示器件与I2C连接，没有地址文本。（证据：图 6c305db1571c / 第 1 页 / 核心板页AXP192/BM8563/CTP I2C连接，无地址标注; 图 112373303e35 / 第 1 页 / 扩展板页MPU-6886 I2C连接，无地址标注）
- `other.documented-display`：产品正文称LCD为ILI9342C、2.0英寸、320×240，但原理图只将连接器标为M5_CORE2_LCD_10P，没有控制器料号或分辨率。（证据：图 6c305db1571c / 第 1 页 / 核心板页LCD1 M5_CORE2_LCD_10P，无ILI9342C/分辨率文本）
- `component.usb-variant`：当前CORE2_V1.0原理图明确使用CP2104-F03-GMR；产品正文说明后续实物还存在CH9102F版本，因此不能由本图确认任一当前出货批次的芯片。（证据：图 6c305db1571c / 第 1 页 / 核心板页 C1 U3 CP2104-F03-GMR）
- `other.battery-rtc-revisions`：V1.0图画出BT1 BATTERY_RTC和SYS_VBAT接口但未标主电池容量；产品正文说明主电池后续由390mAh改为500mAh并取消RTC纽扣电池，当前图无法代表所有批次。（证据：图 6c305db1571c / 第 1 页 / 核心板页 D1 BT1 RTC_BAT与A1 SYS_VBAT电源路径，无容量文本）
- `review.i2c-addresses`：Core2当前硬件批次的AXP192、BM8563、FT6336U、MPU6886地址是否分别固定为0x34、0x51、0x38、0x68？；原因：地址来自产品正文，两张原理图未直接标注地址或所有地址绑带。
- `review.display-model`：Core2当前LCD组件是否确认为ILI9342C、2.0英寸、320×240，并与LCD1连接器物料一致？；原因：型号和分辨率来自产品正文，原理图只显示LCD连接器和信号。
- `review.usb-variant`：待描述的Core2实物批次使用CP2104还是CH9102F，是否有对应修订原理图？；原因：当前资源是CP2104的V1.0图，产品正文确认存在CH9102F版本。
- `review.battery-rtc-revisions`：当前Core2批次的主电池容量和RTC备份电池装配状态是什么？；原因：V1.0图显示BT1且无主电池容量，产品版本记录说明容量和RTC电池均曾变更。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6c305db1571c5d0b2bf6bf88a747719ac07a7be236002d15e44fc5974aa50204` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_V1.0_SCH_page_01.png` |
| 2 | 1 | `112373303e35fe1e47a55b650c144d0319d258fdbed06e33d7151f563a581ad3` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/CORE2_EXT_Board_page_01.png` |

---

源文档：`zh_CN/core/core2.md`

源文档 SHA-256：`c6026c8950a98c42eeb0565e8d4c38189ab878cc0404745d35ab251865e14373`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
