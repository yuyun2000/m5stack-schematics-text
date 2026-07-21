# AtomS3R-CAM AI Chatbot 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AtomS3R-CAM AI Chatbot |
| SKU | K147-CAM |
| 产品 ID | `atoms3r-cam-ai-chatbot-989c49375129` |
| 源文档 | `zh_CN/core/AtomS3R-CAM AI Chatbot.md` |

## 概述

AtomS3R-CAM AI Chatbot 由 AtomS3R-CAM 主控/摄像头两板和 Atomic Voice Base 组成。主板以 ESP32-S3-PICO-1-N8R8 为核心，集成 JW5712 3.3V 电源、BMI270/BMM150 九轴传感器、LP5562 RGB、USB、红外和扩展接口；摄像头子板提供 24P 并行图像接口、1.2V/2.8V 电源和复位/上电控制。语音底座使用 ES8311 编解码器、MSM381A3729H9BPC 麦克风、NS4150B 差分扬声器功放和 P14IOE5V6408ZTAEX 控制，ES8311 CE 接低时地址为 0x18。

## 检索关键词

`AtomS3R-CAM AI Chatbot`、`K147-CAM`、`ESP32-S3-PICO-1-N8R8`、`JW5712`、`BMI270`、`BMM150`、`LP5562`、`PMS150G-U6`、`GC0308`、`FPC-0.5-24P`、`LP3992-12B5F`、`WL2863E28-5/TR`、`CN809S`、`ES8311`、`0x18`、`MSM381A3729H9BPC`、`NS4150B`、`P14IOE5V6408ZTAEX`、`SYS_SCL`、`SYS_SDA`、`A_SCL`、`A_SDA`、`USB_D_P`、`USB_D_N`、`VIN_5V`、`VDD_3V3`、`DVDD 1.2V`、`AVDD 2.8V`、`CAM_RST`、`I2S`、`DSDIN`、`ASDOUT`、`LRCK`、`SCLK`、`SPK+`、`SPK-`、`IR_LED_DRV`、`8MB Flash`、`8MB PSRAM`、`Atomic Voice Base`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 (main) | ESP32-S3-PICO-1-N8R8 | 主控模组，连接 USB、摄像头、IMU、RGB、红外、按键和扩展接口 | 图 12d7e47ad6fa / 第 1 页 / 主板页网格 A2-B3：U1 ESP32-S3-PICO-1-N8R8 全部引脚 |
| U2 (main) | JW5712 | VIN_5V 到 VDD_3V3 的开关稳压器 | 图 12d7e47ad6fa / 第 1 页 / 主板页网格 C1-C3：U2 JW5712、L1、C12-C16 |
| U4 (main) | LP5562 | I2C RGB LED 驱动器，控制 U5 三色 LED 和背光驱动网络 | 图 12d7e47ad6fa / 第 1 页 / 主板页网格 C1-D3：U4 LP5562、SYS_SCL/SDA、LED_R/G/B |
| U5 | NH-B2020RGBA-HF | 由 LP5562 驱动的 RGB LED | 图 12d7e47ad6fa / 第 1 页 / 主板页网格 D3-D4：U5 NH-B2020RGBA-HF |
| U6 | BMI270 | 主 I2C 六轴惯性传感器，并通过辅助 I2C 连接 BMM150 | 图 12d7e47ad6fa / 第 1 页 / 主板页网格 C5-D6：U6 BMI270、SYS_SCL/SDA、A_SCL/A_SDA |
| U9 | BMM150 | 挂载在 BMI270 辅助 I2C 的三轴磁力计 | 图 12d7e47ad6fa / 第 1 页 / 主板页网格 C5：U9 BMM150，A_SCL/A_SDA 与 VDD_3V3 |
| U7 | PMS150G-U6 | 连接 ESP_EN、GPIO_LED 与 SYS_SCL/GPIO0 的辅助控制器 | 图 12d7e47ad6fa / 第 1 页 / 主板页网格 D1-D3：U7 PMS150G-U6 |
| J2 (main) | USB-TYPEC | 原生 USB 数据与 VIN_5V 输入 | 图 12d7e47ad6fa / 第 1 页 / 主板页网格 A6-A7：J2/F1/R4/R5/R19/R20/D3/D4 |
| FET2,D2 | CJ3134K KF / XMEH1UA/MHS153IRCT | GPIO47 IR_LED_DRV 控制的红外发射支路 | 图 12d7e47ad6fa / 第 1 页 / 主板页网格 B7-B8：FET2、D2、R2/R3、IR_LED_DRV |
| FPC1 | FPC-0.5-24P | 摄像头传感器并行数据、时钟、同步、控制与多路电源接口 | 图 2a02ef35734d / 第 1 页 / 摄像头页网格 A1-B2：FPC1 pins1-26 |
| U1 (camera) | LP3992-12B5F | VDD_3V3 到 DVDD 1.2V/300mA 的摄像头数字电源 LDO | 图 2a02ef35734d / 第 1 页 / 摄像头页网格 B3：U1 LP3992-12B5F 与 Vout 1.2V/Imax 300mA |
| U2 (camera) | WL2863E28-5/TR | VDD_3V3 到 AVDD 2.8V/250mA 的摄像头模拟电源 LDO | 图 2a02ef35734d / 第 1 页 / 摄像头页网格 C3：U2 WL2863E28-5/TR 与 Vout 2.8V/Imax 250mA |
| U3 (camera) | CN809S | VDD_3V3 摄像头复位监控器，输出 CAM_RST | 图 2a02ef35734d / 第 1 页 / 摄像头页网格 D3：U3 CN809S、CAM_RST、R2/C7/C8 |
| Q1 | CJ2301 | GPIO18 控制 VDD_3V3_IN 到 VDD_3V3 的摄像头电源开关 | 图 2a02ef35734d / 第 1 页 / 摄像头页网格 A3：Q1 CJ2301、GPIO18、R4 |
| BTB1 | X0400WVS-24-LPV01 | 主板与摄像头子板的 28 Pin 板对板接口 | 图 2a02ef35734d / 第 1 页 / 摄像头页网格 C1-D2：BTB1 pins1-28 |
| U2 (voice) | ES8311 | I2C 控制、全双工 I2S 音频编解码器 | 图 bd81161752dc / 第 1 页 / 语音页上部 U2 ES8311、SCL/SDA/MCLK/SCLK/LRCK/DSDIN/ASDOUT/MIC/OUT |
| U1 (voice) | MSM381A3729H9BPC | 连接 ES8311 MIC_P/MIC_N 的 MEMS 麦克风 | 图 bd81161752dc / 第 1 页 / 语音页右上 U1 MSM381A3729H9BPC、MIC_P/MIC_N |
| U3 (voice) | NS4150B | ES8311 OUTP/OUTN 到 SPK+/SPK- 的差分 D 类扬声器功放 | 图 bd81161752dc / 第 1 页 / 语音页中部 U3 NS4150B、OUTP/OUTN、CTRL、SPK+/SPK- |
| U4 (voice) | P14IOE5V6408ZTAEX | I2C GPIO 扩展器，P0 输出 CTRL 控制扬声器功放 | 图 bd81161752dc / 第 1 页 / 语音页左下 U4 P14IOE5V6408ZTAEX、P0 CTRL、ADDR/RESET |
| J1,J2 (voice) | Atom_5P@2.54 / Atom_4P@2.54 | I2S 音频与 I2C/5V 接口 | 图 bd81161752dc / 第 1 页 / 语音页右下 J1/J2，DSDIN/LRCK/ASDOUT/SCLK 与 SCL/SDA/5V/GND |

## 系统结构

### AtomS3R-CAM AI Chatbot 架构

套件由 ESP32-S3-PICO-1-N8R8 主板、24P 摄像头子板和 ES8311 Atomic Voice Base 组成；主板还集成 BMI270/BMM150、RGB、IR、USB 与扩展接口。

- 参数与网络：`controller=ESP32-S3-PICO-1-N8R8`；`camera=FPC1/BTB1 camera board`；`imu=BMI270 + BMM150`；`audio=ES8311 + MEMS + NS4150B`；`power=JW5712 main; LP3992/WL2863 camera`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板完整单页; 图 2a02ef35734d / 第 1 页 / 摄像头完整单页; 图 bd81161752dc / 第 1 页 / 语音底座完整单页

## 核心器件

### LP5562 RGB 驱动

U4 LP5562 通过 SYS_SCL/SYS_SDA 控制，R/G/B 输出形成 LED_R/LED_G/LED_B 并连接 U5 NH-B2020RGBA-HF；FET1 CJ1339 与 LED_BL_DRV 控制 LED_BL。

- 参数与网络：`driver=U4 LP5562`；`i2c=SYS_SCL/SYS_SDA`；`led=U5 NH-B2020RGBA-HF`；`outputs=LED_R/G/B`；`backlight=FET1 CJ1339, LED_BL_DRV -> LED_BL`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页网格 C1-D4：U4/U5/FET1

### Voice Base I2C GPIO 扩展

U4 P14IOE5V6408ZTAEX 的 SCL/SDA 接总线，ADDR pin9 接 GND，P0 pin12 输出 CTRL，RESET pin10 由 R12 4.7K 与 C24 100nF 配置。

- 参数与网络：`device=U4 P14IOE5V6408ZTAEX`；`i2c=SCL/SDA`；`address_strap=ADDR GND`；`output=P0 CTRL`；`reset=R12 4.7K; C24 100nF`
- 证据：图 bd81161752dc / 第 1 页 / 语音页左下 U4/R12/C24

## 电源

### 主板 VDD_3V3

U2 JW5712 以 VIN_5V 为输入，SW 经 L1 MWTC201608S2R2 输出 VDD_3V3，输入 C15 10uF/C16 100nF，输出 C7 100nF/C13 10uF。

- 参数与网络：`input=VIN_5V`；`converter=U2 JW5712`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`input_caps=C15 10uF; C16 100nF`；`output_caps=C7 100nF; C13 10uF`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页网格 C1-C3：U2/L1/C12-C16

### 摄像头 1.2V/2.8V/3.3V 电源

Q1 由 GPIO18 控制 VDD_3V3_IN 到 VDD_3V3；U1 LP3992-12B5F 生成 DVDD 1.2V/300mA，U2 WL2863E28-5/TR 生成 AVDD 2.8V/250mA。

- 参数与网络：`switch=Q1 CJ2301 controlled by GPIO18`；`digital=U1 LP3992-12B5F -> DVDD 1.2V 300mA`；`analog=U2 WL2863E28-5/TR -> AVDD 2.8V 250mA`；`io=VDD_3V3`
- 证据：图 2a02ef35734d / 第 1 页 / 摄像头页 Q1/U1/U2 电源区与红色电压注释

## 接口

### 摄像头 FPC 并行接口

FPC1 引出 SIO_D GPIO12、SIO_C GPIO9、RESET CAM_RST、VSYNC GPIO10、PWDN GPIO14、Y9/Y8/Y7/Y6/Y5/Y4/Y3/Y2、XCLK GPIO21、PCLK GPIO40、HREF 以及 AVDD/DVDD/DOVDD。

- 参数与网络：`sda=GPIO12`；`scl=GPIO9`；`reset=CAM_RST`；`vsync=GPIO10`；`pwdn=GPIO14`；`xclk=GPIO21`；`pclk=GPIO40`；`data=Y2-Y9 on GPIO3/42/46/4/48/17/11/13`；`power=AVDD,DVDD,DOVDD`
- 证据：图 2a02ef35734d / 第 1 页 / 摄像头页 FPC1 pins1-26

## 总线

### 原生 USB

J2 USB_D_P/USB_D_N 经 R19/R20 22R 连接 U1 GPIO20/GPIO19，CC1/CC2 经 R4/R5 5.1K 下拉，D3/D4 ESD5Z3V3 提供保护，VBUS 经 F1 6V/2A/PPTC 形成 VIN_5V。

- 参数与网络：`dp=GPIO20 via R19 22R`；`dm=GPIO19 via R20 22R`；`cc=R4/R5 5.1K`；`esd=D3/D4`；`vbus_fuse=F1 6V/2A/PPTC`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页网格 A6-A7：J2/F1/USB 网络

### SYS_SCL/SYS_SDA 总线

U1 GPIO0/GPIO45 形成 SYS_SCL/SYS_SDA，连接 BMI270、LP5562、Voice Base SCL/SDA 及主板扩展接口；主板 R10/R11 2.2K 上拉到 VDD_3V3。

- 参数与网络：`scl=SYS_SCL / GPIO0`；`sda=SYS_SDA / GPIO45`；`pullups=R10/R11 2.2K`；`devices=BMI270, LP5562, Voice Base ES8311/U4`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 U1/SYS_SCL/SYS_SDA/R10/R11/U4/U6; 图 bd81161752dc / 第 1 页 / 语音页 J2 SCL/SDA 与 U2/U4

## 总线地址

### ES8311 I2C 地址

语音页打印 ES8311 address: CE pin low - 0x18, CE pin high - 0x19；图中 CE pin20 接 GND，因此当前绑定位为 0x18。

- 参数与网络：`device=U2 ES8311`；`ce_low=0x18`；`ce_high=0x19`；`schematic_ce=GND`；`configured_address=0x18`
- 证据：图 bd81161752dc / 第 1 页 / 语音页顶部地址文字与 U2 CE pin20/GND

## GPIO 与控制信号

### 红外发射

U1 GPIO47 形成 IR_LED_DRV，经 R3 100K 驱动 FET2 CJ3134K KF，开关 D2 红外 LED 与 R2 15R 的 VDD_3V3 支路。

- 参数与网络：`gpio=GPIO47`；`gate_resistor=R3 100K`；`fet=FET2 CJ3134K KF`；`led=D2 XMEH1UA/MHS153IRCT`；`series=R2 15R`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页网格 B7-B8：IR_LED_DRV/FET2/D2

## 复位

### 用户键与复位键

S1 将 USER_BUT 拉低，R6 10K 上拉且 C11 1nF 滤波；S2 将 ESP_EN 拉低，C17 1nF 接地。

- 参数与网络：`user=S1 USER_BUT low; R6 10K; C11 1nF`；`reset=S2 ESP_EN low; C17 1nF`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页网格 C4-C5：S1/S2

### 摄像头复位监控

U3 CN809S 由 VDD_3V3 供电，/RST 输出 CAM_RST，R2 10K 上拉且 C8 1uF 接地。

- 参数与网络：`supervisor=U3 CN809S`；`supply=VDD_3V3`；`reset=CAM_RST`；`pullup=R2 10K`；`capacitor=C8 1uF`
- 证据：图 2a02ef35734d / 第 1 页 / 摄像头页网格 D3：U3/R2/C8/CAM_RST

## 内存与 Flash

### ESP32-S3-PICO-1-N8R8 存储料号

主板 U1 明确标 ESP32-S3-PICO-1-N8R8，VDD_SPI 与相关电源网络在图中可见，页面未画独立 Flash 或 PSRAM 器件。

- 参数与网络：`soc=ESP32-S3-PICO-1-N8R8`；`external_flash_shown=false`；`external_psram_shown=false`；`vdd_spi=U1 pin29`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页 U1 ESP32-S3-PICO-1-N8R8 与存储相关引脚

## 音频

### ES8311 I2S 音频

U2 ES8311 通过 SCLK、LRCK、DSDIN 和 ASDOUT 连接 J1 5 Pin 音频接口，MCLK 由 MCLK 网络输入；SCL/SDA 连接 J2 I2C 接口。

- 参数与网络：`codec=U2 ES8311`；`i2s=SCLK,LRCK,DSDIN,ASDOUT`；`clock=MCLK`；`control=SCL/SDA`；`connector=J1 Atom_5P@2.54`
- 证据：图 bd81161752dc / 第 1 页 / 语音页 U2 与 J1/J2

### MEMS 麦克风输入

U1 MSM381A3729H9BPC 由 3.3V 经 L1 供电，OUT 形成 MIC_P，GND 参考形成 MIC_N，MIC_P/MIC_N 经耦合网络进入 ES8311 MIC1P/MIC1N。

- 参数与网络：`microphone=U1 MSM381A3729H9BPC`；`supply=3.3V via L1`；`positive=MIC_P`；`negative=MIC_N`；`codec_inputs=ES8311 MIC1P/MIC1N`
- 证据：图 bd81161752dc / 第 1 页 / 语音页右上 U1 与 U2 MIC 网络

### NS4150B 扬声器功放

ES8311 OUTN/OUTP 经 C16/C17 100nF 与 R7/R8 150K 驱动 U3 NS4150B INN/INP，U3 输出 SPK-/SPK+；CTRL 由 U4 P0 控制。

- 参数与网络：`codec_outputs=OUTN/OUTP`；`amplifier=U3 NS4150B`；`inputs=C16/C17 100nF; R7/R8 150K`；`outputs=SPK-/SPK+`；`enable=CTRL from U4 P0`
- 证据：图 bd81161752dc / 第 1 页 / 语音页中部 U3 NS4150B 音频路径

## 传感器

### 九轴传感器连接

U6 BMI270 的 SCx/SDx 接 SYS_SCL/SYS_SDA，ASDx/ASCx 接 A_SDA/A_SCL 并连接 U9 BMM150；BMI270 INT1 经 R9 100K 上拉形成 IMU_INT。

- 参数与网络：`imu=U6 BMI270`；`host_i2c=SYS_SCL/SYS_SDA`；`magnetometer=U9 BMM150`；`aux_i2c=A_SCL/A_SDA`；`interrupt=INT1/IMU_INT with R9 100K`
- 证据：图 12d7e47ad6fa / 第 1 页 / 主板页网格 C5-D6：U6/U9 与 I2C 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | AtomS3R-CAM AI Chatbot 架构 | `controller=ESP32-S3-PICO-1-N8R8`；`camera=FPC1/BTB1 camera board`；`imu=BMI270 + BMM150`；`audio=ES8311 + MEMS + NS4150B`；`power=JW5712 main; LP3992/WL2863 camera` |
| 内存与 Flash | ESP32-S3-PICO-1-N8R8 存储料号 | `soc=ESP32-S3-PICO-1-N8R8`；`external_flash_shown=false`；`external_psram_shown=false`；`vdd_spi=U1 pin29` |
| 电源 | 主板 VDD_3V3 | `input=VIN_5V`；`converter=U2 JW5712`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`input_caps=C15 10uF; C16 100nF`；`output_caps=C7 100nF; C13 10uF` |
| 总线 | 原生 USB | `dp=GPIO20 via R19 22R`；`dm=GPIO19 via R20 22R`；`cc=R4/R5 5.1K`；`esd=D3/D4`；`vbus_fuse=F1 6V/2A/PPTC` |
| 传感器 | 九轴传感器连接 | `imu=U6 BMI270`；`host_i2c=SYS_SCL/SYS_SDA`；`magnetometer=U9 BMM150`；`aux_i2c=A_SCL/A_SDA`；`interrupt=INT1/IMU_INT with R9 100K` |
| 总线 | SYS_SCL/SYS_SDA 总线 | `scl=SYS_SCL / GPIO0`；`sda=SYS_SDA / GPIO45`；`pullups=R10/R11 2.2K`；`devices=BMI270, LP5562, Voice Base ES8311/U4` |
| GPIO 与控制信号 | 红外发射 | `gpio=GPIO47`；`gate_resistor=R3 100K`；`fet=FET2 CJ3134K KF`；`led=D2 XMEH1UA/MHS153IRCT`；`series=R2 15R` |
| 复位 | 用户键与复位键 | `user=S1 USER_BUT low; R6 10K; C11 1nF`；`reset=S2 ESP_EN low; C17 1nF` |
| 核心器件 | LP5562 RGB 驱动 | `driver=U4 LP5562`；`i2c=SYS_SCL/SYS_SDA`；`led=U5 NH-B2020RGBA-HF`；`outputs=LED_R/G/B`；`backlight=FET1 CJ1339, LED_BL_DRV -> LED_BL` |
| 接口 | 摄像头 FPC 并行接口 | `sda=GPIO12`；`scl=GPIO9`；`reset=CAM_RST`；`vsync=GPIO10`；`pwdn=GPIO14`；`xclk=GPIO21`；`pclk=GPIO40`；`data=Y2-Y9 on GPIO3/42/46/4/48/17/11/13`；`power=AVDD,DVDD,DOVDD` |
| 电源 | 摄像头 1.2V/2.8V/3.3V 电源 | `switch=Q1 CJ2301 controlled by GPIO18`；`digital=U1 LP3992-12B5F -> DVDD 1.2V 300mA`；`analog=U2 WL2863E28-5/TR -> AVDD 2.8V 250mA`；`io=VDD_3V3` |
| 复位 | 摄像头复位监控 | `supervisor=U3 CN809S`；`supply=VDD_3V3`；`reset=CAM_RST`；`pullup=R2 10K`；`capacitor=C8 1uF` |
| 音频 | ES8311 I2S 音频 | `codec=U2 ES8311`；`i2s=SCLK,LRCK,DSDIN,ASDOUT`；`clock=MCLK`；`control=SCL/SDA`；`connector=J1 Atom_5P@2.54` |
| 总线地址 | ES8311 I2C 地址 | `device=U2 ES8311`；`ce_low=0x18`；`ce_high=0x19`；`schematic_ce=GND`；`configured_address=0x18` |
| 音频 | MEMS 麦克风输入 | `microphone=U1 MSM381A3729H9BPC`；`supply=3.3V via L1`；`positive=MIC_P`；`negative=MIC_N`；`codec_inputs=ES8311 MIC1P/MIC1N` |
| 音频 | NS4150B 扬声器功放 | `codec_outputs=OUTN/OUTP`；`amplifier=U3 NS4150B`；`inputs=C16/C17 100nF; R7/R8 150K`；`outputs=SPK-/SPK+`；`enable=CTRL from U4 P0` |
| 核心器件 | Voice Base I2C GPIO 扩展 | `device=U4 P14IOE5V6408ZTAEX`；`i2c=SCL/SDA`；`address_strap=ADDR GND`；`output=P0 CTRL`；`reset=R12 4.7K; C24 100nF` |
| 核心器件 | 摄像头传感器型号 | `documented_model=GC0308`；`documented_resolution=0.3MP`；`schematic_component=FPC1 FPC-0.5-24P`；`sensor_model_shown=false` |
| 总线地址 | BMI270 I2C 地址 | `device=U6 BMI270`；`documented_address=0x68`；`schematic_address_text=null`；`sdo=U6 SDO pin11` |
| 内存与 Flash | 8MB Flash 与 8MB PSRAM | `soc=ESP32-S3-PICO-1-N8R8`；`documented_flash=8MB`；`documented_psram=8MB`；`external_memory_shown=false`；`capacity_text_shown=false` |

## 待确认事项

- `component.camera-model`：产品正文写 GC0308 0.3MP，但摄像头原理图只画 FPC1 通用引脚和电源，未在器件字段中标出 GC0308 或分辨率，实装型号需 BOM 确认。（证据：图 2a02ef35734d / 第 1 页 / 摄像头页 FPC1 与完整单页，未见 GC0308）
- `address.bmi270`：产品正文写 BMI270 地址 0x68，主板原理图显示 BMI270 的主 I2C 和 SDO/地址相关引脚，但未打印 0x68 地址文字。（证据：图 12d7e47ad6fa / 第 1 页 / 主板页 U6 BMI270，无数值地址标注）
- `memory.documented-capacity`：产品正文写 8MB Flash + 8MB PSRAM，原理图主控料号为 ESP32-S3-PICO-1-N8R8 且未画外部存储，但页面未单独打印容量字段。（证据：图 12d7e47ad6fa / 第 1 页 / 主板页 U1 ESP32-S3-PICO-1-N8R8 与完整存储器范围）
- `review.camera-model`：K147-CAM 当前摄像头 FPC 实装传感器是否固定为 GC0308 0.3MP？；原因：原理图只定义 FPC 电气接口，没有传感器型号或分辨率字段。
- `review.bmi270-address`：K147-CAM 当前 BMI270 的正式 7-bit I2C 地址是否为 0x68？；原因：地址来自正文，主板图没有直接打印数值。
- `review.memory-capacity`：ESP32-S3-PICO-1-N8R8 在 K147-CAM 当前 BOM 中的 Flash 与 PSRAM 容量是否均为 8MB？；原因：容量来自正文和料号解释，原理图未单独打印容量字段。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `12d7e47ad6faf5e5e5f3a4f75dfea67502822e394712651d8f514c5b27020abf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/C126_CAM_Sch_M5_AtomS3R_v0.4.1_page_01.png` |
| 2 | 1 | `2a02ef35734da25ddb4a874572c19f721f8da365dd4fb742f674c33d6c28f0aa` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/681/C126_CAM_Sch_M5_AtomS3R_page_01.png` |
| 3 | 1 | `bd81161752dc9459d869bd8b77462aa788e79245c4baec6645839ab9fe125604` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/schematic.png` |

---

源文档：`zh_CN/core/AtomS3R-CAM AI Chatbot.md`

源文档 SHA-256：`83072da48ab81450999f940dd54a98f88d0037534e442e86a327500b494c4e21`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
