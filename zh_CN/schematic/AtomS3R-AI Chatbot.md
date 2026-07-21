# AtomS3R-AI Chatbot 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AtomS3R-AI Chatbot |
| SKU | K147 |
| 产品 ID | `atoms3r-ai-chatbot-54b324f77e29` |
| 源文档 | `zh_CN/core/AtomS3R-AI Chatbot.md` |

## 概述

AtomS3R-AI Chatbot 由 AtomS3R 主板和 Atomic Voice Base 组成。主板以 ESP32-S3-PICO-1-N8R8 为核心，JW5712 生成 3.3V，集成 PIFA 天线、原生 USB、LP5562 RGB 控制、BMI270/BMM150、IR 发射、IPS 显示接口、按键、Grove 与底部 GPIO。语音底座以 ES8311 为音频编解码器，CE 接低使其地址为 0x18，通过 SCLK/LRCK/DSDIN/ASDOUT 全双工 I2S 和 SCL/SDA I2C 连接主机；MSM381A3729H9BPC 提供麦克风，NS4150B 驱动 SPK+/SPK-，PI4IOE5V6408ZTAEX P0 控制功放 CTRL。音频位深、SNR、扬声器功率、内存容量及 AI 助手软件能力需由 datasheet/BOM/固件确认。

## 检索关键词

`AtomS3R-AI Chatbot`、`K147`、`ESP32-S3-PICO-1-N8R8`、`JW5712`、`LP5562`、`BMI270`、`BMM150`、`ES8311`、`ES8311 0x18`、`MSM381A3729H9BPC`、`NS4150B`、`PI4IOE5V6408ZTAEX`、`SCLK`、`LRCK`、`DSDIN`、`ASDOUT`、`MCLK`、`SCL`、`SDA`、`SPK+`、`SPK-`、`MIC_P`、`MIC_N`、`IR_LED_DRV`、`GPIO47`、`USER_BUT`、`GPIO42`、`SYS_SCL`、`SYS_SDA`、`A_SCL`、`A_SDA`、`USB_D_P`、`USB_D_N`、`LCD_BL`、`DISP_RST`、`SPI_MOSI`、`SPI_SCK`、`DISP_CS`、`8MB Flash`、`8MB PSRAM`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 (AtomS3R) | ESP32-S3-PICO-1-N8R8 | 主控 SiP，连接显示、IMU、USB、IR、RGB、按键、GPIO 和射频 | 图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 A3-B4，U1 ESP32-S3-PICO-1-N8R8 |
| U2 (AtomS3R) | JW5712 | VIN_5V 到 VDD_3V3 的开关稳压器 | 图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 C1-C3，U2 JW5712 与 L1 |
| U4 (AtomS3R) | LP5562 | I2C RGB LED 控制器，输出 LED_R/G/B 与 LED_BL_DRV | 图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 C1-D3，U4 LP5562 |
| U6 (AtomS3R) | BMI270 | SYS I2C 六轴 IMU，并通过 A_SCL/A_SDA 连接 BMM150 | 图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 C6-D6，U6 BMI270 |
| U9 | BMM150 | 挂接 BMI270 辅助 I2C 的磁力计 | 图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 C5，U9 BMM150 |
| ANT1 | ESP-H0920-PIFA | ESP_LNA 射频端的 PIFA 天线 | 图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 A1-A2，ANT1/R1/C1/C2 |
| J2 | USB-TYPEC | VIN_5V 与 USB_D_P/USB_D_N 接口 | 图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 A6-A7 J2 USB Type-C |
| J1 | HDGC/0.5K-HX-8PWB | IPS 显示接口，连接背光、复位、命令/数据和 SPI | 图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 A5，J1 8P DISPLAY 接口 |
| FET2,D2 | CJ3134K KF / XMEIHUA/MHS153IRCT | GPIO47 控制的红外发射驱动 | 图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 B7-C8 IR_LED_DRV/FET2/D2 |
| U2 (Voice Base) | ES8311 | I2S/I2C 音频编解码器，连接 MEMS 麦克风和功放 | 图 bd81161752dc / 第 1 页 / 第 2 张第 1 页左上 U2 ES8311，SCL/SDA/MCLK/I2S/MIC/OUT 引脚 |
| U1 (Voice Base) | MSM381A3729H9BPC | 3.3V 供电的 MEMS 麦克风，差分输出 MIC_P/MIC_N | 图 bd81161752dc / 第 1 页 / 第 2 张第 1 页右上 U1 MSM381A3729H9BPC 与 MIC_P/MIC_N |
| U3 (Voice Base) | NS4150B | 由 OUTP/OUTN 驱动 SPK+/SPK- 的 D 类功放 | 图 bd81161752dc / 第 1 页 / 第 2 张第 1 页左中 U3 NS4150B，INP/INN/CTRL/VoP/VoN |
| U4 (Voice Base) | PI4IOE5V6408ZTAEX | I2C GPIO 扩展器，P0 输出 CTRL 控制 NS4150B | 图 bd81161752dc / 第 1 页 / 第 2 张第 1 页左下 U4 PI4IOE5V6408ZTAEX，SCL/SDA/P0/RESET/ADDR |
| J1,J2 (Voice Base) | Atom_5P@2.54 / Atom_4P@2.54 | I2S 音频和 I2C/电源主机接口 | 图 bd81161752dc / 第 1 页 / 第 2 张第 1 页右下 J1/J2 Atom_5P/4P |
| S1,S2 | SMT_SW_PTS_820 / SMT_SW_TS_015 | USER_BUT 用户按键和 ESP_EN 复位按键 | 图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 C4 S1 USER_BUT 与 S2 ESP_EN |

## 系统结构

### AtomS3R-AI Chatbot 系统架构

AtomS3R 主板以 ESP32-S3-PICO-1-N8R8 为核心，集成显示、BMI270/BMM150、LP5562 RGB、IR、USB、Grove 和 GPIO；Atomic Voice Base 以 ES8311 连接 MEMS 麦克风、NS4150B 功放和 PI4IOE5V6408ZTAEX，并通过 I2S/I2C 接口连接 AtomS3R。

- 参数与网络：`controller=ESP32-S3-PICO-1-N8R8`；`display=J1 IPS interface`；`imu=BMI270+BMM150`；`codec=ES8311`；`microphone=MSM381A3729H9BPC`；`amplifier=NS4150B`；`io_expander=PI4IOE5V6408ZTAEX`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页完整 AtomS3R 主板; 图 bd81161752dc / 第 1 页 / 第 2 张第 1 页完整 Voice Base

## 电源

### AtomS3R VIN_5V 到 VDD_3V3

U2 JW5712 的 VIN 接 VIN_5V，SW 经 L1 MWTC201608S2R2 输出 VDD_3V3，输入 C15/C16、输出 C7/C13 去耦。

- 参数与网络：`input=VIN_5V`；`converter=JW5712`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`input_caps=C15 10uF,C16 100nF`；`output_caps=C7 100nF,C13 10uF`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 C1-C3 U2/L1

## 接口

### Grove 与底部 GPIO

J7 GH2.0-4P 引出 GPIO1、GPIO2、VIN_5V、GND，GPIO1/2 带 D5/D6 ESD 和 R17/R18 串联器件；J5 引出 3.3V/GPIO6/GPIO5/GPIO7/GPIO8，J6 引出 GPIO39/GPIO38/VIN_5V/GND。

- 参数与网络：`grove=GPIO1,GPIO2,VIN_5V,GND`；`J5=VDD_3V3,G6,G5,G7,G8`；`J6=G39,G38,VIN_5V,GND`；`protection=D5/D6 ESD5Z3V3`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 B5-C6 J5/J6/J7

## 总线

### 原生 USB-C

J2 DP1/DN1 经 R19/R20 各 22Ω 形成 USB_D_P/USB_D_N，连接 U1 GPIO20/GPIO19；D3/D4 ESD5Z3V3 对地保护，CC1/CC2 经 R4/R5 5.1KΩ 接 GND，VIN_5V 串 F1 6V/2A PPTC。

- 参数与网络：`dp=GPIO20`；`dn=GPIO19`；`series=R19/R20 22Ω`；`esd=D3/D4 ESD5Z3V3`；`cc=R4/R5 5.1KΩ`；`fuse=F1 6V/2A`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 A6-A7 J2 USB

### AtomS3R SYS I2C

U1 GPIO0 形成 SYS_SCL，GPIO45 形成 SYS_SDA；R10/R11 各 2.2KΩ 上拉到 VDD_3V3，连接 BMI270 与 LP5562。

- 参数与网络：`scl=GPIO0 SYS_SCL`；`sda=GPIO45 SYS_SDA`；`pullups=R10/R11 2.2KΩ`；`devices=BMI270,LP5562`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页 U1/U4/U6 SYS_SCL/SYS_SDA

### BMI270 Sensor Hub 与 BMM150

BMI270 ASDx/ASCx 形成 A_SDA/A_SCL 并连接 BMM150 SDx/SCK；R12 2.2KΩ 将 A_SDA 上拉到 VDD_3V3，BMM150 CSB 接 GND。

- 参数与网络：`hub=BMI270`；`device=BMM150`；`sda=A_SDA`；`scl=A_SCL`；`pullup=R12 2.2KΩ`；`csb=GND`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 C5-D6 U6/U9

### IPS 显示 SPI/控制

J1 pin1 LED_BL、pin3 DISP_RST/GPIO48、pin4 DISP_RS/GPIO42、pin5 SPI_MOSI/GPIO21、pin6 SPI_SCK/GPIO15、pin8 DISP_CS/GPIO14；pin2 GND、pin7 VDD_3V3。LED_BL 由 LP5562 LED_BL_DRV 经 FET1 控制。

- 参数与网络：`backlight=LED_BL via LP5562/FET1`；`reset=GPIO48`；`dc=GPIO42`；`mosi=GPIO21`；`sck=GPIO15`；`cs=GPIO14`；`supply=VDD_3V3`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 A5 J1 与 C2-D3 LP5562/FET1

### Atomic Voice Base I2S

J1 Atom_5P pin2=DSDIN、pin3=LRCK、pin4=ASDOUT、pin5=SCLK，pin1=3.3V；这些网络连接 ES8311 DSDIN pin9、LRCK pin8、ASDOUT pin7、SCLK pin6，MCLK 单独进入 pin2。

- 参数与网络：`codec=ES8311`；`host_map=G5 DSDIN,G6 LRCK,G7 ASDOUT,G8 SCLK`；`connector=J1 Atom_5P`；`signals=DSDIN,LRCK,ASDOUT,SCLK,MCLK`
- 证据：图 bd81161752dc / 第 1 页 / 第 2 张第 1 页 ES8311 左侧 I2S 与右下 J1

### Atomic Voice Base I2C

J2 Atom_4P 的 pin1=SCL、pin2=SDA、pin3=5V、pin4=GND；SCL/SDA 连接 ES8311 与 PI4IOE5V6408ZTAEX，并分别由 R1/R2 4.7KΩ 上拉到 3.3V。

- 参数与网络：`host_map=G39 SCL,G38 SDA`；`codec=ES8311`；`expander=PI4IOE5V6408ZTAEX`；`pullups=R1/R2 4.7KΩ`；`power=5V,GND`
- 证据：图 bd81161752dc / 第 1 页 / 第 2 张第 1 页 SCL/SDA、R1/R2、U2/U4 与 J2

## 总线地址

### ES8311 I2C 地址

图中说明 ES8311 address: CE pin low -> 0x18, CE pin high -> 0x19；U2 CE pin20 在本页连接 GND，因此本板 ES8311 地址配置为 0x18。

- 参数与网络：`device=U2 ES8311`；`ce_low=0x18`；`ce_high=0x19`；`ce_connection=GND`；`configured_address=0x18`
- 证据：图 bd81161752dc / 第 1 页 / 第 2 张第 1 页顶部地址说明与 U2 CE pin20 到 GND

## GPIO 与控制信号

### 用户与复位按键

U1 GPIO42 的 USER_BUT 由 R6 10KΩ 上拉到 VDD_3V3，并由 S1 按下接 GND，C11 1nF 对地；S2 将 ESP_EN 按下接 GND，ESP_EN 由 R14 10KΩ 上拉和 C24 1uF 延时。

- 参数与网络：`user=GPIO42 USER_BUT,S1,R6 10KΩ,C11 1nF`；`reset=ESP_EN,S2,R14 10KΩ,C24 1uF`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 C4-D4 S1/S2

### 红外 LED 驱动

U1 GPIO47 输出 IR_LED_DRV，经 R3 100KΩ 控制 FET2 CJ3134K KF，低侧驱动 D2 红外 LED；D2 经 R2 15Ω 接 VDD_3V3。

- 参数与网络：`gpio=GPIO47`；`fet=CJ3134K KF`；`led=XMEIHUA/MHS153IRCT`；`series=R2 15Ω`；`gate=R3 100KΩ`
- 证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页网格 B7-C8 IR_LED_DRV

## 音频

### MEMS 麦克风输入

U1 MSM381A3729H9BPC 由 3.3V 供电，OUT/GND 差分侧通过 MIC_P/MIC_N 与 C2/C5 1uF 连接 ES8311 MIC1P/MIC1N；C1 22pF、R4 0Ω 和 C3/C4 构成外围网络。

- 参数与网络：`microphone=MSM381A3729H9BPC`；`supply=3.3V`；`signals=MIC_P,MIC_N`；`codec_inputs=MIC1P,MIC1N`；`coupling=C2/C5 1uF`
- 证据：图 bd81161752dc / 第 1 页 / 第 2 张第 1 页右上 U1 与 ES8311 MIC 输入

### ES8311 到 NS4150B 扬声器路径

ES8311 OUTN/OUTP 经 C16/C17 100nF 与 R7/R8 150KΩ 连接 NS4150B INN/INP；U3 VoN/VoP 经 R6/R11 0Ω 输出 SPK-/SPK+，CTRL 由 U4 P0 控制。

- 参数与网络：`codec_outputs=OUTN,OUTP`；`coupling=C16/C17 100nF,R7/R8 150KΩ`；`amplifier=NS4150B`；`speaker=SPK-,SPK+`；`enable=PI4IOE5V6408ZTAEX P0 -> CTRL`
- 证据：图 bd81161752dc / 第 1 页 / 第 2 张第 1 页中部 ES8311 OUTP/OUTN、U3 NS4150B 与 SPK+/SPK-

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | AtomS3R-AI Chatbot 系统架构 | `controller=ESP32-S3-PICO-1-N8R8`；`display=J1 IPS interface`；`imu=BMI270+BMM150`；`codec=ES8311`；`microphone=MSM381A3729H9BPC`；`amplifier=NS4150B`；`io_expander=PI4IOE5V6408ZTAEX` |
| 电源 | AtomS3R VIN_5V 到 VDD_3V3 | `input=VIN_5V`；`converter=JW5712`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`input_caps=C15 10uF,C16 100nF`；`output_caps=C7 100nF,C13 10uF` |
| 总线 | 原生 USB-C | `dp=GPIO20`；`dn=GPIO19`；`series=R19/R20 22Ω`；`esd=D3/D4 ESD5Z3V3`；`cc=R4/R5 5.1KΩ`；`fuse=F1 6V/2A` |
| 总线 | AtomS3R SYS I2C | `scl=GPIO0 SYS_SCL`；`sda=GPIO45 SYS_SDA`；`pullups=R10/R11 2.2KΩ`；`devices=BMI270,LP5562` |
| 总线 | BMI270 Sensor Hub 与 BMM150 | `hub=BMI270`；`device=BMM150`；`sda=A_SDA`；`scl=A_SCL`；`pullup=R12 2.2KΩ`；`csb=GND` |
| GPIO 与控制信号 | 用户与复位按键 | `user=GPIO42 USER_BUT,S1,R6 10KΩ,C11 1nF`；`reset=ESP_EN,S2,R14 10KΩ,C24 1uF` |
| GPIO 与控制信号 | 红外 LED 驱动 | `gpio=GPIO47`；`fet=CJ3134K KF`；`led=XMEIHUA/MHS153IRCT`；`series=R2 15Ω`；`gate=R3 100KΩ` |
| 总线 | IPS 显示 SPI/控制 | `backlight=LED_BL via LP5562/FET1`；`reset=GPIO48`；`dc=GPIO42`；`mosi=GPIO21`；`sck=GPIO15`；`cs=GPIO14`；`supply=VDD_3V3` |
| 接口 | Grove 与底部 GPIO | `grove=GPIO1,GPIO2,VIN_5V,GND`；`J5=VDD_3V3,G6,G5,G7,G8`；`J6=G39,G38,VIN_5V,GND`；`protection=D5/D6 ESD5Z3V3` |
| 总线 | Atomic Voice Base I2S | `codec=ES8311`；`host_map=G5 DSDIN,G6 LRCK,G7 ASDOUT,G8 SCLK`；`connector=J1 Atom_5P`；`signals=DSDIN,LRCK,ASDOUT,SCLK,MCLK` |
| 总线 | Atomic Voice Base I2C | `host_map=G39 SCL,G38 SDA`；`codec=ES8311`；`expander=PI4IOE5V6408ZTAEX`；`pullups=R1/R2 4.7KΩ`；`power=5V,GND` |
| 总线地址 | ES8311 I2C 地址 | `device=U2 ES8311`；`ce_low=0x18`；`ce_high=0x19`；`ce_connection=GND`；`configured_address=0x18` |
| 音频 | MEMS 麦克风输入 | `microphone=MSM381A3729H9BPC`；`supply=3.3V`；`signals=MIC_P,MIC_N`；`codec_inputs=MIC1P,MIC1N`；`coupling=C2/C5 1uF` |
| 音频 | ES8311 到 NS4150B 扬声器路径 | `codec_outputs=OUTN,OUTP`；`coupling=C16/C17 100nF,R7/R8 150KΩ`；`amplifier=NS4150B`；`speaker=SPK-,SPK+`；`enable=PI4IOE5V6408ZTAEX P0 -> CTRL` |
| 总线地址 | PI4IOE5V6408 I2C 地址 | `device=PI4IOE5V6408ZTAEX`；`address_pin=ADDR GND`；`address=null`；`reset=R12 4.7KΩ,C24 100nF` |
| 总线地址 | BMI270/BMM150 地址 | `documented_bmi270=0x68`；`bmm150=null`；`schematic_addresses=null` |
| 内存与 Flash | 8MB Flash 与 8MB PSRAM | `part_number=ESP32-S3-PICO-1-N8R8`；`documented_flash=8MB`；`documented_psram=8MB`；`external_memory=null` |
| 音频 | 音频位深、SNR 与扬声器功率 | `documented_codec=24-bit`；`documented_mic_snr=>=65dB`；`documented_speaker=1W@8Ω`；`sample_rate=null`；`thd=null`；`measured_power=null` |
| 其他事实 | AI 语音助手软件能力 | `documented_services=XiaoZhi,OpenAI,Volcengine`；`firmware_version=null`；`model=null`；`latency=null`；`privacy=null` |

## 待确认事项

- `address.voice-io-expander`：U4 PI4IOE5V6408ZTAEX 的 ADDR pin9 接 GND，RESET pin10 由 R12 4.7KΩ 上拉并由 C24 100nF 对地；本页未直接写出该地址数值。（证据：图 bd81161752dc / 第 1 页 / 第 2 张第 1 页左下 U4 ADDR/RESET 网络，无地址文字）
- `address.imu-addresses`：正文给出 BMI270 地址 0x68，并说明 BMM150 通过 Sensor Hub 获取；原理图确认拓扑但未标 BMI270/BMM150 地址或 BMI270 地址选择状态。（证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页 U6/U9 无地址文字）
- `memory.documented-n8r8`：原理图标 U1 ESP32-S3-PICO-1-N8R8，正文写 8MB Flash + 8MB PSRAM；板级图未单列存储容量字段，需由 SiP datasheet 或实机确认。（证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页 U1 型号，无容量字段）
- `audio.documented-performance`：正文称 ES8311 24-bit、麦克风 SNR≥65dB、NS4150B 驱动 1W@8Ω 扬声器；原理图只确认型号和连接，未标采样参数、SNR、扬声器阻抗/额定功率或整机失真。（证据：图 bd81161752dc / 第 1 页 / 第 2 张第 1 页 ES8311/MIC/NS4150B 电路，无性能表）
- `other.ai-assistant-software`：正文描述小智、OpenAI、火山引擎、唤醒词和低时延交互；原理图只能确认音频与网络硬件，无法验证固件版本、云服务、模型、延迟或隐私行为。（证据：图 f6814e0cd0e8 / 第 1 页 / 第 1 张第 1 页主控/USB/天线硬件; 图 bd81161752dc / 第 1 页 / 第 2 张第 1 页音频硬件）
- `review.io-expander-address`：PI4IOE5V6408ZTAEX 在 ADDR=GND 时的正式 7 位 I2C 地址是什么？；原因：原理图只给出地址脚电平。
- `review.imu-addresses`：请确认 BMI270=0x68 以及 BMM150 辅助总线地址/初始化方式。；原因：原理图未标地址。
- `review.memory-capacity`：请用 SiP datasheet 或实机确认 8MB Flash 和 8MB PSRAM。；原因：板级图未写容量。
- `review.audio-performance`：请以 datasheet/BOM/实测确认 24-bit、麦克风 SNR、1W@8Ω、采样率和失真。；原因：连接图不能证明整机音频性能。
- `review.ai-software`：当前固件实际支持哪些语音助手、模型、唤醒词、延迟和隐私策略？；原因：软件与云服务能力不在原理图中。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f6814e0cd0e897a09992bb89ebb5592d44b28aa2e3fd2391db43300349894ede` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/680/Sch_M5_AtomS3R_v0.4.1_page_01.png` |
| 2 | 1 | `bd81161752dc9459d869bd8b77462aa788e79245c4baec6645839ab9fe125604` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/schematic.png` |

---

源文档：`zh_CN/core/AtomS3R-AI Chatbot.md`

源文档 SHA-256：`16592dfa648e2b72e1913286f1dc4f2717a9465446b4e0b13b1bba4c43acc53e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
