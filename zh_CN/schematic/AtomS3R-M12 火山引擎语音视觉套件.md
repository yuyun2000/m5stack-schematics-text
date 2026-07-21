# AtomS3R-M12 火山引擎语音视觉套件 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AtomS3R-M12 火山引擎语音视觉套件 |
| SKU | D062-M12 |
| 产品 ID | `atoms3r-m12-864fa7e586d0` |
| 源文档 | `zh_CN/core/AtomS3R-M12 Volcengine Kit.md` |

## 概述

AtomS3R-M12 主板以 U1 ESP32-S3-PICO-1-N8R8 为核心，集成 BMI270/BMM150、USB-C、PIFA 天线、红外驱动、LP5562 RGB 驱动和多组扩展接口，并由 U2 JW5712 将 VIN_5V 转换为 VDD_3V3。摄像头小板通过 J4/BTB1 传递并行像素、SCCB 和控制信号，使用 LP3992-12B5F、WL2863E28-5/TR 生成 1.2V/2.8V 摄像头电源。Atomic Voice Base 通过 GPIO39/38 I2C 与 GPIO5-8 I2S 接入，板上包含 ES8311 编解码器、MSM381A3729H9PBC MEMS 麦克风、NS4150B 功放和 PI4IOE5V6408 I/O 扩展器。

## 检索关键词

`AtomS3R-M12`、`D062-M12`、`ESP32-S3-PICO-1-N8R8`、`OV3660`、`BMI270`、`BMM150`、`ES8311`、`NS4150B`、`MSM381A3729H9PBC`、`PI4IOE5V6408`、`JW5712`、`LP3992-12B5F`、`WL2863E28-5/TR`、`SYS_SCL`、`SYS_SDA`、`A_SCL`、`A_SDA`、`CAM_RST`、`GPIO18 POWER_N`、`GPIO47 IR_LED_DRV`、`GPIO41 USER_BUT`、`GPIO39 SCL`、`GPIO38 SDA`、`GPIO5 DSDIN`、`GPIO6 LRCK`、`GPIO7 ASDOUT`、`GPIO8 SCLK`、`USB_D_P`、`USB_D_N`、`FPC-0.5-24P`、`X0400VVS-24-LPV01`、`VDD_3V3`、`AVDD 2.8V`、`VDDD 1.2V`、`I2S full duplex`、`ES8311 0x18`、`ESP-H0920-PIFA`、`IR LED`、`Atomic Voice Base`、`M12 camera`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-S3-PICO-1-N8R8 | 主控 SoC/模组，连接摄像头、IMU、USB、射频、红外、RGB、按键与 Voice Base | 图 12d7e47ad6fa / 第 1 页 / 主板页 A3-B3 U1 ESP32-S3-PICO-1-N8R8，GPIO0-48、USB、LNA_IN 与电源引脚 |
| U2 | JW5712 | 将 VIN_5V 转换为 VDD_3V3 的主板 DC/DC | 图 12d7e47ad6fa / 第 1 页 / 主板页 C1-C3 U2 JW5712、L1 MWT201608S2R2 与 VDD_3V3 |
| U6 | BMI270 | 通过 SYS_SCL/SYS_SDA 接主控的六轴 IMU，并通过辅助 I2C 接 BMM150 | 图 12d7e47ad6fa / 第 1 页 / 主板页 C5-D6 U6 BMI270，SCx/SDx、ASCL/ASDx、IMU_INT |
| U9 | BMM150 | 连接 BMI270 A_SCL/A_SDA 辅助总线的三轴地磁传感器 | 图 12d7e47ad6fa / 第 1 页 / 主板页 C5 小型 U9 BMM150，SCK/SDI 接 A_SCL/A_SDA |
| U4,U5 | LP5562 / NH-B2020RGBA-HF | I2C RGB LED 驱动器和三色 LED | 图 12d7e47ad6fa / 第 1 页 / 主板页 C1-D3 U4 LP5562 连接 SYS_SCL/SYS_SDA 与 LED_R/G/B，U5 NH-B2020RGBA-HF |
| U7,D1 | PMS150G-U6 / GREEN LED | 辅助控制器，监测/驱动 SYS_SCL_GPIO0、GPIO_LED、ESP_EN 与绿色状态 LED | 图 12d7e47ad6fa / 第 1 页 / 主板页 D1-D3 U7 PMS150G-U6、D1 GREEN、SYS_SCL_GPIO0/GPIO_LED/ESP_EN |
| J2,F1,D3,D4 | USB-TYPEC / 6V 2A PPTC / ESD5Z3V3 | USB-C 电源与 USB_D_P/N 数据连接及过流/ESD 保护 | 图 12d7e47ad6fa / 第 1 页 / 主板页 A6-A7 J2 USB-TYPEC、F1、D3/D4、R19/R20 与 CC 电阻 |
| ANT1,R1,C1,C2 | ESP-H0920-PIFA / 2.4nH / 2.7pF / 2.0pF | ESP32-S3 LNA_IN 的板载 PIFA 天线匹配网络 | 图 12d7e47ad6fa / 第 1 页 / 主板页 A1-A3 ANT1 ESP-H0920-PIFA、R1、C1/C2 与 ESP_LNA |
| D2,FET2 | XMEIHUA/MHS153IRCT / CJ3134K_KF | 由 GPIO47/IR_LED_DRV 控制的红外发射级 | 图 12d7e47ad6fa / 第 1 页 / 主板页 B7 D2 红外 LED、R2 15R、FET2、R3 100K 与 IR_LED_DRV |
| S1,S2 | PTS_820 / SMT_SW_TS_015 | GPIO41 用户按键与 ESP_EN 复位/下载按键 | 图 12d7e47ad6fa / 第 1 页 / 主板页 C4 S1 USER_BUT 与 S2 ESP_EN 到 GND |
| J1 | HDGC/0.5K-HX-8PWB | 主板 8 针显示接口，承载背光、SPI 和复位/命令信号 | 图 12d7e47ad6fa / 第 1 页 / 主板页 A5 J1 8P，LED_BL、DISP_RST、DISP_RS、SPI_MOSI、SPI_SCK、DISP_CS |
| J4 | XKB_X0400FVS-24 | 主板到摄像头小板的 24 针板对板接口 | 图 12d7e47ad6fa / 第 1 页 / 主板页 A5-B5 J4 24 针，摄像头 GPIO、SYS_SCL/SDA、电源和地 |
| J5,J6,J7 | THT headers / GPIO-4P | Voice Base I2S/I2C、电源和 Grove GPIO 扩展接口 | 图 12d7e47ad6fa / 第 1 页 / 主板页 B5-C6 J5 GPIO5-8、J6 GPIO39/38/VIN_5V/GND、J7 GPIO1/2/VIN_5V/GND |
| FPC1 | FPC-0.5-24P | 摄像头小板并行像素、SCCB、时钟、同步、复位和多电源接口 | 图 2a02ef35734d / 第 1 页 / 摄像头小板页 A1-B2 FPC1 FPC-0.5-24P，SIO_D/SIO_C、VSYNC/HREF/PCLK/XCLK、Y2-Y9、电源 |
| BTB1 | X0400VVS-24-LPV01 | 摄像头小板到主板的 24 针板对板连接器 | 图 2a02ef35734d / 第 1 页 / 摄像头小板页 C1-D2 BTB1，GPIO42/46/48/40/3/21/4/14/17/10/11/9/13/12/18、SYS_SCL/SDA、电源与地 |
| U1,U2 | LP3992-12B5F / WL2863E28-5/TR | 摄像头小板的 1.2V VDDD 与 2.8V AVDD LDO | 图 2a02ef35734d / 第 1 页 / 摄像头小板页 B3/C3 U1 1.2V 300mA、U2 2.8V 250mA |
| U3,Q1 | CN809S / CJ2301 | 摄像头 CAM_RST 监控与 GPIO18 控制的 3.3V 高边开关 | 图 2a02ef35734d / 第 1 页 / 摄像头小板页 A3 Q1 CJ2301/GPIO18 与 D3 U3 CN809S/CAM_RST |
| U2 | ES8311 | Atomic Voice Base 的 I2C 控制、全双工 I2S 音频编解码器 | 图 bd81161752dc / 第 1 页 / Voice Base 页左上 U2 ES8311，SCL/SDA/MCLK/SCLK/LRCK/ASDOUT/DSDIN/MIC/OUT 引脚 |
| U1,L1 | MSM381A3729H9PBC / HZ1005U102TFB01 | Atomic Voice Base 的 MEMS 麦克风与 3.3V 电源滤波磁珠 | 图 bd81161752dc / 第 1 页 / Voice Base 页右上 U1 MSM381A3729H9PBC，MIC_P/MIC_N、L1 与去耦 |
| U3 | NS4150B | 由 ES8311 OUTP/OUTN 差分输出驱动的 D 类扬声器功放 | 图 bd81161752dc / 第 1 页 / Voice Base 页中部 U3 NS4150B，INP/INN、CTRL、SPK+/SPK- |
| U4 | PI4IOE5V6408ZTAEX | I2C 八位 GPIO 扩展器，P0 输出 CTRL 控制 NS4150B | 图 bd81161752dc / 第 1 页 / Voice Base 页左下 U4 PI4IOE5V6408ZTAEX，SCL/SDA、P0 CTRL、RESET/ADDR |
| J1,J2 | Atom_5P@2.54 / Atom_4P@2.54 | Voice Base 与 AtomS3R-M12 的 I2S、I2C 和电源堆叠接口 | 图 bd81161752dc / 第 1 页 / Voice Base 页右下 J1 3.3V/DSDIN/LRCK/ASDOUT/SCLK 与 J2 SCL/SDA/5V/GND |

## 系统结构

### 语音视觉套件总体架构

ESP32-S3-PICO-1-N8R8 主板通过 24 针小板采集并行摄像头数据，通过 J5/J6 的 I2S/I2C 连接 Atomic Voice Base，并同时管理 BMI270/BMM150、USB、红外和扩展接口。

- 参数与网络：`controller=U1 ESP32-S3-PICO-1-N8R8`；`camera_link=J4/BTB1/FPC1`；`voice_link=J5 I2S + J6 I2C`；`imu=BMI270 + BMM150`；`voice_codec=ES8311`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板完整页; 图 2a02ef35734d / 第 1 页 / 摄像头小板完整页; 图 bd81161752dc / 第 1 页 / Atomic Voice Base 完整页

## 电源

### 主板 5V 到 3.3V

U2 JW5712 VIN/EN 接 VIN_5V，SW 经 L1 MWT201608S2R2 输出 VDD_3V3，R14 100KΩ/R15 22.1KΩ 构成反馈。

- 参数与网络：`input=VIN_5V`；`converter=U2 JW5712`；`inductor=L1 MWT201608S2R2`；`feedback=R14 100KΩ; R15 22.1KΩ`；`output=VDD_3V3`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 C1-C3 U2/L1/R14/R15

### 摄像头 1.2V/2.8V 电源

U1 LP3992-12B5F 从 VDD_3V3 生成 VDDD 1.2V/300mA；U2 WL2863E28-5/TR 生成 AVDD 2.8V/250mA。

- 参数与网络：`digital=VDDD 1.2V 300mA`；`analog=AVDD 2.8V 250mA`
- 证据：图 2a02ef35734d / 第 1 页 / 摄像头小板页 B3/C3 U1/U2 与 Vout/Imax

## 接口

### USB-C 电源与数据

J2 DP/DN 经 R19/R20 22Ω 接 USB_D_P/N，CC1/CC2 各由 R4/R5 5.1KΩ 下拉，VBUS 经 F1 6V/2A PPTC 形成 VIN_5V；D3/D4 为数据 ESD。

- 参数与网络：`data=USB_D_P/N via R19/R20 22Ω`；`cc=R4/R5 5.1KΩ`；`vbus=F1 6V/2A PPTC -> VIN_5V`；`esd=D3/D4 ESD5Z3V3`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 A6-A7 J2/F1/R4/R5/R19/R20/D3/D4

### 主板到摄像头小板

J4/BTB1 传递 GPIO46/42/40/48/21/3/14/4/10/17/9/11/12/13/18、SYS_SCL/SYS_SDA、VDD_3V3 和 GND。

- 参数与网络：`main=J4 XKB_X0400FVS-24`；`daughter=BTB1 X0400VVS-24-LPV01`；`power_control=GPIO18`；`i2c=SYS_SCL/SYS_SDA`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 J4 1-24; 图 2a02ef35734d / 第 1 页 / 摄像头小板页 BTB1

### HY2.0-4P 扩展接口

主板 J7 pin1=GPIO1、pin2=GPIO2、pin3=VIN_5V、pin4=GND，两条 GPIO 由 D5/D6 ESD5Z3V3 保护。

- 参数与网络：`pin1=GPIO1`；`pin2=GPIO2`；`pin3=VIN_5V`；`pin4=GND`；`protection=D5/D6 ESD5Z3V3`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 C5-C6 J7 GPIO-4P 与 D5/D6

## 总线

### BMI270 主 I2C

ESP32 GPIO0 经 L2 33Ω 连接 SYS_SCL，GPIO45 连接 SYS_SDA；R10/R11 各 2.2KΩ 上拉 VDD_3V3，U6 BMI270 SCx/SDx 接入。

- 参数与网络：`scl=GPIO0 -> L2 33Ω -> SYS_SCL`；`sda=GPIO45 -> SYS_SDA`；`pullups=R10/R11 2.2KΩ`；`device=U6 BMI270`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 U1 GPIO0/GPIO45 与 U6 SYS_SCL/SYS_SDA/R10/R11

### BMM150 辅助 I2C

BMM150 的 A_SCL/A_SDA 连接 BMI270 ASCx/ASDx，构成由 BMI270 管理的传感器辅助总线。

- 参数与网络：`controller=U6 BMI270 sensor hub`；`scl=A_SCL`；`sda=A_SDA`；`device=U9 BMM150`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 C5-D6 U9 BMM150 与 U6 ASDx/ASCx

### 主板显示 SPI

J1 pin3 DISP_RST=GPIO48、pin4 DISP_RS=GPIO42、pin5 SPI_MOSI=GPIO21、pin6 SPI_SCK=GPIO15、pin8 DISP_CS=GPIO14，pin1 为 LED_BL。

- 参数与网络：`reset=GPIO48`；`dc=GPIO42`；`mosi=GPIO21`；`sck=GPIO15`；`cs=GPIO14`；`backlight=LED_BL`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 A5 J1 8P 网络

### LP5562 RGB 驱动总线

U4 LP5562 SDA/SCL 连接 SYS_SDA/SYS_SCL，R/G/B 输出连接 U5 三色 LED，EN 接 VDD_3V3。

- 参数与网络：`controller=ESP32 SYS_SCL/SYS_SDA`；`device=U4 LP5562`；`outputs=LED_R, LED_G, LED_B`；`led=U5 NH-B2020RGBA-HF`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 C1-D3 U4/U5 与 SYS_SCL/SYS_SDA

### 摄像头并行数据映射

FPC1 的 Y9/Y8/Y7/Y6/Y5/Y4/Y3/Y2 分别连接 GPIO13/11/17/4/48/46/42/3；XCLK=GPIO21、PCLK=GPIO40、VSYNC=GPIO10、HREF=GPIO14。

- 参数与网络：`data=Y9 GPIO13; Y8 GPIO11; Y7 GPIO17; Y6 GPIO4; Y5 GPIO48; Y4 GPIO46; Y3 GPIO42; Y2 GPIO3`；`xclk=GPIO21`；`pclk=GPIO40`；`vsync=GPIO10`；`href=GPIO14`
- 证据：图 2a02ef35734d / 第 1 页 / 摄像头小板页 FPC1 pin7-22 的 VSYNC/HREF/PCLK/XCLK/Y2-Y9

### 摄像头 SCCB 控制

FPC1 SIO_D 连接 GPIO12，SIO_C 连接 GPIO9，R1/R3 各 2.2KΩ 上拉 VDD_3V3；CAM_RST 由 U3 CN809S 输出。

- 参数与网络：`sio_d=GPIO12`；`sio_c=GPIO9`；`pullups=R1/R3 2.2KΩ`；`reset=CAM_RST from U3 CN809S`
- 证据：图 2a02ef35734d / 第 1 页 / 摄像头小板页 FPC1 SIO_D/SIO_C/CAM_RST 与 R1/R3/U3

### Voice Base I2C

主板 GPIO39/GPIO38 分别通过 J6 连接 Voice Base J2 的 SCL/SDA；ES8311 与 PI4IOE5V6408 共用该总线，R1/R2 4.7KΩ 上拉 3.3V。

- 参数与网络：`scl=GPIO39 -> J6 -> J2 SCL`；`sda=GPIO38 -> J6 -> J2 SDA`；`devices=U2 ES8311; U4 PI4IOE5V6408ZTAEX`；`pullups=R1/R2 4.7KΩ`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 J6 GPIO39/GPIO38; 图 bd81161752dc / 第 1 页 / Voice Base 页 J2 SCL/SDA、U2/U4 与 R1/R2

### Voice Base 全双工 I2S

主板 J5 GPIO5/6/7/8 分别映射到 Voice Base J1 的 DSDIN、LRCK、ASDOUT、SCLK，另由 J1 pin1 提供 3.3V。

- 参数与网络：`dsdin=GPIO5`；`lrck=GPIO6`；`asdout=GPIO7`；`sclk=GPIO8`；`connector=J5 main / J1 Voice Base`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 J5 VDD_3V3/GPIO5/6/7/8; 图 bd81161752dc / 第 1 页 / Voice Base 页 J1 3.3V/DSDIN/LRCK/ASDOUT/SCLK

## 总线地址

### ES8311 I2C 地址

Voice Base 图注明 CE 低电平地址为 0x18、CE 高电平为 0x19；当前 U2 CE pin20 接 GND，因此可见配置地址为 0x18。

- 参数与网络：`device=U2 ES8311`；`ce_low=0x18`；`ce_high=0x19`；`ce_connection=GND`；`configured_address=0x18`
- 证据：图 bd81161752dc / 第 1 页 / Voice Base 页顶部地址注释与 U2 CE pin20/GND

## GPIO 与控制信号

### BMI270 中断

U6 INT1 连接 IMU_INT 并对应 ESP32 GPIO15；INT2 未连接。

- 参数与网络：`interrupt=U6 INT1 -> IMU_INT -> GPIO15`；`int2_connected=false`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 U6 INT1/INT2 与 U1 GPIO15 IMU_INT

### 红外发射控制

ESP32 GPIO47 连接 IR_LED_DRV，经 R3 100KΩ 控制 FET2；VDD_3V3 经 D2 与 R2 15Ω 到 FET2。

- 参数与网络：`gpio=GPIO47`；`mosfet=FET2 CJ3134K_KF`；`emitter=D2 XMEIHUA/MHS153IRCT`；`series=R2 15Ω`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 B7 IR LED 驱动与 U1 GPIO47

### 用户按键

ESP32 GPIO41 连接 USER_BUT，R6 10KΩ 上拉到 VDD_3V3，C11 1nF 接 GND，S1 按下接 GND。

- 参数与网络：`gpio=GPIO41`；`pullup=R6 10KΩ`；`capacitor=C11 1nF`；`switch=S1 PTS_820`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 C4 U1 GPIO41 USER_BUT、R6/C11/S1

### 摄像头电源开关

GPIO18 通过 R4 10KΩ 控制 Q1 CJ2301，将 VDD_3V3_IN 切换到摄像头小板 VDD_3V3。

- 参数与网络：`gpio=GPIO18`；`switch=Q1 CJ2301`；`input=VDD_3V3_IN`；`output=VDD_3V3`
- 证据：图 2a02ef35734d / 第 1 页 / 摄像头小板页 A3 Q1/R4/GPIO18

## 时钟

### 外部主晶振

ESP32-S3-PICO-1-N8R8 的 XTAL_P/XTAL_N 在当前主板页标记未连接，未画出外部主晶振。

- 参数与网络：`xtal_p=NC`；`xtal_n=NC`；`external_crystal_shown=false`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 U1 XTAL_P pin54、XTAL_N pin53 未连接标记

## 复位

### ESP32 复位

ESP_EN 由 R14 10KΩ 上拉与 C24 1uF 下拉形成 RC，S2 按下将 ESP_EN 接 GND。

- 参数与网络：`net=ESP_EN`；`pullup=R14 10KΩ`；`capacitor=C24 1uF`；`switch=S2`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 C4/D4 ESP_EN/R14/C24/S2

## 内存与 Flash

### 主控集成存储

主控型号明确为 ESP32-S3-PICO-1-N8R8，主板未画出外部 Flash/PSRAM，SPI 存储引脚标为未连接。

- 参数与网络：`soc=ESP32-S3-PICO-1-N8R8`；`integrated_marking=N8R8`；`external_flash_shown=false`；`external_psram_shown=false`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 U1 型号与 SPIHD/SPIWP/SPICS0/SPICLK/SPIQ/SPID 未连接

## 音频

### MEMS 麦克风输入链路

U1 MSM381A3729H9PBC 的差分 MIC_P/MIC_N 经 C2/C5 各 1uF 连接 ES8311 MIC1P/MIC1N，麦克风 3.3V 经 L1 滤波并使用 C3/C4 去耦。

- 参数与网络：`microphone=U1 MSM381A3729H9PBC`；`codec=U2 ES8311`；`positive=MIC_P via C2 1uF`；`negative=MIC_N via C5 1uF`；`supply_filter=L1 HZ1005U102TFB01`
- 证据：图 bd81161752dc / 第 1 页 / Voice Base 页右上 U1/C2/C5/L1 与 U2 MIC1P/MIC1N

### 扬声器功放链路

ES8311 OUTN/OUTP 经 C16/C17 100nF 与 R7/R8 150KΩ 进入 U3 NS4150B INN/INP，差分输出经 R6/R11 0Ω 形成 SPK-/SPK+；CTRL 由 U4 P0 控制。

- 参数与网络：`codec_outputs=OUTN/OUTP`；`input_network=C16/C17 100nF; R7/R8 150KΩ`；`amplifier=U3 NS4150B`；`speaker=SPK-/SPK+`；`enable=U4 P0 CTRL`
- 证据：图 bd81161752dc / 第 1 页 / Voice Base 页中部 ES8311 OUTN/OUTP 到 U3 NS4150B 与 SPK+/SPK-

## 射频

### 板载 PIFA 天线

U1 LNA_IN 通过 ESP_LNA 匹配网络连接 ANT1 ESP-H0920-PIFA，器件为 R1 2.4nH、C1 2.7pF、C2 2.0pF。

- 参数与网络：`antenna=ANT1 ESP-H0920-PIFA`；`matching=R1 2.4nH; C1 2.7pF; C2 2.0pF`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 A1-A3 ANT1/ESP_LNA/U1 LNA_IN

## 调试与烧录

### USB 下载调试

ESP32 GPIO19/GPIO20 分别连接 USB_D_N/USB_D_P 到 J2，GPIO0 与 ESP_EN 提供下载和复位控制。

- 参数与网络：`usb_dn=GPIO19`；`usb_dp=GPIO20`；`boot=GPIO0`；`reset=ESP_EN`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 U1 GPIO19/20 USB_D_N/P、GPIO0 与 ESP_EN/S2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 语音视觉套件总体架构 | `controller=U1 ESP32-S3-PICO-1-N8R8`；`camera_link=J4/BTB1/FPC1`；`voice_link=J5 I2S + J6 I2C`；`imu=BMI270 + BMM150`；`voice_codec=ES8311` |
| 内存与 Flash | 主控集成存储 | `soc=ESP32-S3-PICO-1-N8R8`；`integrated_marking=N8R8`；`external_flash_shown=false`；`external_psram_shown=false` |
| 电源 | 主板 5V 到 3.3V | `input=VIN_5V`；`converter=U2 JW5712`；`inductor=L1 MWT201608S2R2`；`feedback=R14 100KΩ; R15 22.1KΩ`；`output=VDD_3V3` |
| 接口 | USB-C 电源与数据 | `data=USB_D_P/N via R19/R20 22Ω`；`cc=R4/R5 5.1KΩ`；`vbus=F1 6V/2A PPTC -> VIN_5V`；`esd=D3/D4 ESD5Z3V3` |
| 总线 | BMI270 主 I2C | `scl=GPIO0 -> L2 33Ω -> SYS_SCL`；`sda=GPIO45 -> SYS_SDA`；`pullups=R10/R11 2.2KΩ`；`device=U6 BMI270` |
| 总线 | BMM150 辅助 I2C | `controller=U6 BMI270 sensor hub`；`scl=A_SCL`；`sda=A_SDA`；`device=U9 BMM150` |
| 总线地址 | BMI270 I2C 地址 | `documented_address=0x68`；`schematic_address_shown=false`；`address_pin=U6 SDO visible` |
| GPIO 与控制信号 | BMI270 中断 | `interrupt=U6 INT1 -> IMU_INT -> GPIO15`；`int2_connected=false` |
| GPIO 与控制信号 | 红外发射控制 | `gpio=GPIO47`；`mosfet=FET2 CJ3134K_KF`；`emitter=D2 XMEIHUA/MHS153IRCT`；`series=R2 15Ω` |
| GPIO 与控制信号 | 用户按键 | `gpio=GPIO41`；`pullup=R6 10KΩ`；`capacitor=C11 1nF`；`switch=S1 PTS_820` |
| 复位 | ESP32 复位 | `net=ESP_EN`；`pullup=R14 10KΩ`；`capacitor=C24 1uF`；`switch=S2` |
| 射频 | 板载 PIFA 天线 | `antenna=ANT1 ESP-H0920-PIFA`；`matching=R1 2.4nH; C1 2.7pF; C2 2.0pF` |
| 总线 | 主板显示 SPI | `reset=GPIO48`；`dc=GPIO42`；`mosi=GPIO21`；`sck=GPIO15`；`cs=GPIO14`；`backlight=LED_BL` |
| 总线 | LP5562 RGB 驱动总线 | `controller=ESP32 SYS_SCL/SYS_SDA`；`device=U4 LP5562`；`outputs=LED_R, LED_G, LED_B`；`led=U5 NH-B2020RGBA-HF` |
| 接口 | 主板到摄像头小板 | `main=J4 XKB_X0400FVS-24`；`daughter=BTB1 X0400VVS-24-LPV01`；`power_control=GPIO18`；`i2c=SYS_SCL/SYS_SDA` |
| 总线 | 摄像头并行数据映射 | `data=Y9 GPIO13; Y8 GPIO11; Y7 GPIO17; Y6 GPIO4; Y5 GPIO48; Y4 GPIO46; Y3 GPIO42; Y2 GPIO3`；`xclk=GPIO21`；`pclk=GPIO40`；`vsync=GPIO10`；`href=GPIO14` |
| 总线 | 摄像头 SCCB 控制 | `sio_d=GPIO12`；`sio_c=GPIO9`；`pullups=R1/R3 2.2KΩ`；`reset=CAM_RST from U3 CN809S` |
| GPIO 与控制信号 | 摄像头电源开关 | `gpio=GPIO18`；`switch=Q1 CJ2301`；`input=VDD_3V3_IN`；`output=VDD_3V3` |
| 电源 | 摄像头 1.2V/2.8V 电源 | `digital=VDDD 1.2V 300mA`；`analog=AVDD 2.8V 250mA` |
| 传感器 | 摄像头型号与光学规格 | `documented_model=OV3660`；`documented_resolution=3MP`；`documented_aperture=F2.4`；`documented_fov=120 degrees`；`documented_fps=30`；`schematic_model_shown=false` |
| 总线 | Voice Base I2C | `scl=GPIO39 -> J6 -> J2 SCL`；`sda=GPIO38 -> J6 -> J2 SDA`；`devices=U2 ES8311; U4 PI4IOE5V6408ZTAEX`；`pullups=R1/R2 4.7KΩ` |
| 总线地址 | ES8311 I2C 地址 | `device=U2 ES8311`；`ce_low=0x18`；`ce_high=0x19`；`ce_connection=GND`；`configured_address=0x18` |
| 总线 | Voice Base 全双工 I2S | `dsdin=GPIO5`；`lrck=GPIO6`；`asdout=GPIO7`；`sclk=GPIO8`；`connector=J5 main / J1 Voice Base` |
| 音频 | MEMS 麦克风输入链路 | `microphone=U1 MSM381A3729H9PBC`；`codec=U2 ES8311`；`positive=MIC_P via C2 1uF`；`negative=MIC_N via C5 1uF`；`supply_filter=L1 HZ1005U102TFB01` |
| 音频 | 扬声器功放链路 | `codec_outputs=OUTN/OUTP`；`input_network=C16/C17 100nF; R7/R8 150KΩ`；`amplifier=U3 NS4150B`；`speaker=SPK-/SPK+`；`enable=U4 P0 CTRL` |
| 音频 | Voice Base 音频额定参数 | `documented_codec=24-bit, 16-64kHz`；`documented_mic_snr=>=65dB`；`documented_amp_max=3W`；`documented_speaker=8Ω 1W`；`schematic_ratings_shown=false` |
| 接口 | HY2.0-4P 扩展接口 | `pin1=GPIO1`；`pin2=GPIO2`；`pin3=VIN_5V`；`pin4=GND`；`protection=D5/D6 ESD5Z3V3` |
| 时钟 | 外部主晶振 | `xtal_p=NC`；`xtal_n=NC`；`external_crystal_shown=false` |
| 调试与烧录 | USB 下载调试 | `usb_dn=GPIO19`；`usb_dp=GPIO20`；`boot=GPIO0`；`reset=ESP_EN` |

## 待确认事项

- `address.documented-bmi270`：产品正文给出 BMI270 地址 0x68，但当前原理图未直接标注地址值或明确 SDO 地址绑带状态。（证据：图 12d7e47ad6fa / 第 1 页 / 主板页 U6 BMI270，SDO/CSB/SYS_SCL/SYS_SDA 可见但无 0x68 文本）
- `sensor.documented-camera`：产品正文称摄像头为 OV3660、3MP、F2.4、120° FOV、30FPS，但小板原理图仅显示 FPC1 信号和电源，未标摄像头料号或光学参数。（证据：图 2a02ef35734d / 第 1 页 / 摄像头小板完整页，仅见 FPC1/电源/复位，无 OV3660 或光学标注）
- `audio.documented-ratings`：产品正文给出 ES8311 24-bit/16-64kHz、麦克风 SNR≥65dB、NS4150B 最大 3W 和配套 8Ω/1W 扬声器，但当前原理图仅确认器件与连接，未标这些系统额定值。（证据：图 bd81161752dc / 第 1 页 / Voice Base 完整页 ES8311/麦克风/NS4150B/SPK 网络，无位深、采样率、SNR 或功率标注）
- `review.bmi270-address`：AtomS3R-M12 当前 BMI270 的 SDO/地址绑带是否确保 I2C 地址固定为 0x68？；原因：0x68 来自产品正文，原理图没有直接标注地址数值。
- `review.camera-identity`：FPC1 所接当前摄像头是否确认为 OV3660，且 3MP/F2.4/120°/30FPS 参数适用于本硬件批次？；原因：摄像头小板原理图没有摄像头料号或光学参数。
- `review.audio-ratings`：Atomic Voice Base 的 24-bit/16-64kHz、麦克风 SNR≥65dB、3W 功放和 8Ω/1W 扬声器额定条件是否均由当前料号与整机测试确认？；原因：当前原理图只显示器件型号和连接，没有这些额定参数及测试条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `12d7e47ad6faf5e5e5f3a4f75dfea67502822e394712651d8f514c5b27020abf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/C126_CAM_Sch_M5_AtomS3R_v0.4.1_page_01.png` |
| 2 | 1 | `2a02ef35734da25ddb4a874572c19f721f8da365dd4fb742f674c33d6c28f0aa` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/C126_CAM_Sch_M5_AtomS3R_page_01.png` |
| 3 | 1 | `bd81161752dc9459d869bd8b77462aa788e79245c4baec6645839ab9fe125604` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/schematic.png` |

---

源文档：`zh_CN/core/AtomS3R-M12 Volcengine Kit.md`

源文档 SHA-256：`abb933c1c208c612dd3584d524ab9843e77b8efba9288840d6b5674e669b4100`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
