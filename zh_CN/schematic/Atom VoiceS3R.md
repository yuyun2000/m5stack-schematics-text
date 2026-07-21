# Atom VoiceS3R 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atom VoiceS3R |
| SKU | C126-ECHO |
| 产品 ID | `atom-voices3r-a558a80fe93d` |
| 源文档 | `zh_CN/core/Atom_EchoS3R.md` |

## 概述

Atom VoiceS3R 由主板 U1 ESP32-S3-PICO-1-N8R8 与音频底板组成，主板提供 USB-C、2.4GHz PIFA 天线、JW5712 5V转3.3V电源、用户/复位按键、下载辅助控制、红外发射和扩展连接器。音频板以 U2 ES8311 为编解码核心，U1 MSM381A3729H9BPC 麦克风接其 ADC 输入，DAC 差分输出经 U3 NS4150B 驱动 H2 SPK+/SPK-；BTB1 传递 I2S、I2C、功放控制和 3.3V。ES8311 CE 接低，图面地址为 0x18；主控 GPIO45/0/48/4/3/17/11/18 分别承载 SDA/SCL/DOUT/DIN/WS/BCLK/MCLK/功放控制。

## 检索关键词

`Atom VoiceS3R`、`C126-ECHO`、`ESP32-S3-PICO-1-N8R8`、`ES8311`、`0x18`、`MSM381A3729H9BPC`、`NS4150B`、`JW5712`、`PMS150G-U6`、`USB Type-C`、`USB_D_P`、`USB_D_N`、`ESP-H0920-PIFA`、`I2S`、`MCLK`、`SCLK`、`LRCK`、`DSDIN`、`ASDOUT`、`SYS_SCL`、`SYS_SDA`、`4150_CTR`、`SPK+`、`SPK-`、`USER_BUT`、`ESP_EN`、`IR_LED_DRV`、`GPIO47`、`GPIO41`、`GPIO45`、`GPIO0`、`GPIO48`、`GPIO4`、`GPIO3`、`GPIO17`、`GPIO11`、`GPIO18`、`VIN_5V`、`VDD_3V3`、`GH2.0-4P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 [main] | ESP32-S3-PICO-1-N8R8 | 主控 SiP，连接 USB、Wi-Fi 天线、音频 I2S/I2C、按键、红外和扩展 GPIO | 图 0613b6a13ce3 / 第 1 页 / 网格 A2-B4，U1 ESP32-S3-PICO-1-N8R8 全部 GPIO/电源/RF/USB |
| U2 [main] | JW5712 | VIN_5V 至 VDD_3V3 的主降压转换器 | 图 0613b6a13ce3 / 第 1 页 / 网格 C1-C3，U2 JW5712、L1、VIN_5V、VDD_3V3 |
| J2 [main] | USB-TYPEC | 5V 电源与原生 USB D+/D- 接口，配置 CC 下拉、PPTC 与 ESD 防护 | 图 0613b6a13ce3 / 第 1 页 / 网格 A6-A8，J2 USB-TYPEC、F1、R4/R5/R19/R20、D3/D4 |
| ANT1 | ESP-H0920-PIFA | ESP32-S3 2.4GHz 板载 PIFA 天线 | 图 0613b6a13ce3 / 第 1 页 / 网格 A1-A2，ANT1 ESP-H0920-PIFA、R1/C1/C2 到 ESP_LNA |
| U7 [main] | PMS150G-U6 | 下载/复位辅助控制器，连接 GPIO0、GPO_LED、ESP_EN 与绿色 D1 | 图 0613b6a13ce3 / 第 1 页 / 网格 D1-D3，U7 PMS150G-U6、SYS_SCL GPIO0/GPO_LED/ESP_EN/D1 GREEN |
| S1,S2 | SMT_SW_PTS_820 / SMT_SW_TS_015 | 用户按键与 ESP_EN 复位按键 | 图 0613b6a13ce3 / 第 1 页 / 网格 C4-C5，S1 USER_BUT 与 S2 ESP_EN |
| D2,FET2 | MIEHUA/MHS153IRCT / CJ3134K KF | GPIO47 控制的红外发射 LED 与低端 MOSFET 驱动 | 图 0613b6a13ce3 / 第 1 页 / 网格 B7-C8，D2 红外 LED、R2/FET2/R3、IR_LED_DRV |
| J7 [main] | GH2.0-4P | 外部 GPIO1/GPIO2、VIN_5V、GND 四针接口，GPIO 旁有 ESD/串联保护 | 图 0613b6a13ce3 / 第 1 页 / 网格 B5-C6，J7 GH2.0-4P、GPIO1/GPIO2/VIN_5V/GND、D5/D6/R17/R18 |
| J4 [main] | XKB_X0400FVS-24 | 24针板间/扩展连接器，引出音频 GPIO、SYS I2C、电源与地 | 图 0613b6a13ce3 / 第 1 页 / 网格 A5-B6，J4 XKB_X0400FVS-24 pins1-24 |
| U2 [audio] | ES8311 | 单声道音频编解码器，连接 I2C、I2S、MEMS 麦克风与 NS4150B | 图 5300a63ff310 / 第 1 页 / 网格 A2-B3，U2 ES8311，SCL/SDA/I2S/MIC1P/MIC1N/OUTP/OUTN |
| U1 [audio] | MSM381A3729H9BPC | MEMS 麦克风，经 MIC_P/MIC_N 耦合到 ES8311 | 图 5300a63ff310 / 第 1 页 / 网格 A3-B4，U1 MSM381A3729H9BPC、MIC_P/MIC_N、L1/C1-C4 |
| U3 [audio] | NS4150B | 3.3V D类扬声器功放，差分输入来自 ES8311，输出 SPK-/SPK+ | 图 5300a63ff310 / 第 1 页 / 网格 C1-C3，U3 NS4150B，INN/INP/CTRL/VoN/VoP/VCC/GND |
| H2 [audio] | SpeakHeader | 两针扬声器接口，pin1 SPK+、pin2 SPK- | 图 5300a63ff310 / 第 1 页 / 网格 C2，H2 SpeakHeader SPK+/SPK- |
| BTB1 [audio] | X0400WVS-24-LPV01 | 主板到音频板的板间连接器，承载 I2S、I2C、4150_CTR、3.3V 与 GND | 图 5300a63ff310 / 第 1 页 / 网格 C4-D4，BTB1 X0400WVS-24-LPV01，DSDIN/LRCK/ASDOUT/SCLK/MCLK/4150_CTR/SCL/SDA/3.3V/GND |

## 系统结构

### Atom VoiceS3R 系统架构

系统由 ESP32-S3-PICO-1-N8R8 主板和 ES8311/MSM381A3729H9BPC/NS4150B 音频板组成，另有 USB-C、Wi-Fi PIFA、红外、按键和 GPIO 扩展。

- 参数与网络：`soc=U1 [main] ESP32-S3-PICO-1-N8R8`；`codec=U2 [audio] ES8311`；`microphone=U1 [audio] MSM381A3729H9BPC`；`amplifier=U3 [audio] NS4150B`；`usb=J2`；`antenna=ANT1`；`ir=D2/FET2`；`expansion=J4/J7`
- 证据：图 0613b6a13ce3 / 第 1 页 / 主板整页; 图 5300a63ff310 / 第 1 页 / 音频板整页

## 核心器件

### ESP32-S3-PICO-1-N8R8

主板 U1 明确标为 ESP32-S3-PICO-1-N8R8，集成 RF LNA 输入、原生 USB、GPIO0~48、SPI 电源域和 3.3V 电源引脚。

- 参数与网络：`reference=U1 [main]`；`part_number=ESP32-S3-PICO-1-N8R8`；`rf=ESP_LNA`；`usb=GPIO19 USB_D_N,GPIO20 USB_D_P`；`supply=VDD_3V3`；`flash_psram_capacity=null`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 A2-B4，U1 器件名与引脚

## 电源

### JW5712 3.3V 主电源

U2 JW5712 的 VIN/EN 接 VIN_5V，SW 经 L1 MWTC201608S2R2 输出 VDD_3V3；输入 C15 10uF/C16 100nF，输出含 C7 100nF 与 C13 10uF。

- 参数与网络：`converter=U2 [main] JW5712`；`input=VIN_5V`；`enable=VIN_5V`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`input_caps=C15 10uF,C16 100nF`；`output_caps=C7 100nF,C13 10uF`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 C1-C4，U2/L1/C12-C16/VIN_5V/VDD_3V3

### 麦克风滤波供电

3.3V 经 L1 120R@100MHz 给麦克风 VDD pin1 供电，C3 100nF/50V 与 C4 10uF/10V 去耦，C1 22pF/50V 从 OUT 接地。

- 参数与网络：`rail=3.3V`；`ferrite=L1 120R@100MHz`；`target=U1 pin1 VDD`；`decoupling=C3 100nF,C4 10uF`；`output_filter=C1 22pF`
- 证据：图 5300a63ff310 / 第 1 页 / 网格 A3-B4，L1/C1/C3/C4/U1

### 音频板 3.3V 供电

BTB1 多个电源脚把 3.3V/GND 引入音频板；ES8311、麦克风和 NS4150B 均在 3.3V 电源域，分别配置局部去耦。

- 参数与网络：`connector=BTB1`；`rail=3.3V`；`loads=ES8311,MSM381A3729H9BPC,NS4150B`；`ground=BTB1 GND pins`
- 证据：图 5300a63ff310 / 第 1 页 / 音频板 BTB1 3.3V/GND 与 U1/U2/U3 电源网络

## 接口

### USB-C 电源与数据

J2 USB-TYPEC VCC 经 F1 6V/2A/PPTC 形成 VIN_5V，CC1/CC2 各用 R4/R5 5.1K 下拉；DP1/DP2 与 DN1/DN2 分别合并为 USB_D_P/USB_D_N。

- 参数与网络：`connector=J2`；`vbus=VCC -> F1 6V/2A/PPTC -> VIN_5V`；`cc1=R4 5.1K to GND`；`cc2=R5 5.1K to GND`；`dp=DP1,DP2 -> USB_D_P`；`dn=DN1,DN2 -> USB_D_N`；`ground=GND/SHIELD`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 A6-A8，J2/F1/R4/R5/USB_D_P/N

### J7 GH2.0-4P 扩展接口

J7 pin1 经 R17 接 GPIO1、pin2 经 R18 接 GPIO2、pin3 VIN_5V、pin4 GND；D5/D6 ESDS5Z3V3 对 GPIO 网络提供 ESD 防护。

- 参数与网络：`connector=J7 GH2.0-4P`；`pin1=GPIO1 via R17 PRG15BC330MM1RC`；`pin2=GPIO2 via R18 PRG15BC330MM1RC`；`pin3=VIN_5V`；`pin4=GND`；`esd=D5,D6 ESDS5Z3V3`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 B5-C6，J7/R17/R18/D5/D6

## 总线

### ESP32-S3 原生 USB

USB_D_N 经 R20 22R/1% 连接 U1 GPIO19，USB_D_P 经 R19 22R/1% 连接 GPIO20；D3/D4 ESDS5Z3V3 分别对数据线提供 ESD 防护。

- 参数与网络：`dm=J2 USB_D_N -> R20 22R -> U1 GPIO19`；`dp=J2 USB_D_P -> R19 22R -> U1 GPIO20`；`dm_esd=D4 ESDS5Z3V3`；`dp_esd=D3 ESDS5Z3V3`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 A3/A7，U1 GPIO19/20 与 J2 R19/R20/D3/D4

### 主控到 ES8311 I2C

主板 GPIO45 形成 SYS_SDA，GPIO0 经 L2 33Ω@100MHz 形成 SYS_SCL；音频板 BTB1 SDA/SCL 接 ES8311 SDA/SCL，R1/R2 各 4.7K 上拉到 3.3V。

- 参数与网络：`sda_controller=U1 [main] GPIO45/SYS_SDA`；`scl_controller=U1 [main] GPIO0 -> L2 33Ω@100MHz -> SYS_SCL`；`device=U2 [audio] ES8311`；`pullups=R1 4.7K SCL,R2 4.7K SDA`；`level=3.3V`
- 证据：图 0613b6a13ce3 / 第 1 页 / 主板 U1 GPIO45/GPIO0、SYS_SDA/SYS_SCL、J4; 图 5300a63ff310 / 第 1 页 / 音频板 BTB1 SCL/SDA 到 ES8311 与 R1/R2

### 主控到 ES8311 I2S

主控 GPIO48/GPIO4/GPIO3/GPIO17/GPIO11 分别通过板间连接形成 ASDOUT/DSDIN/LRCK/SCLK/MCLK；音频板 BTB1 将这些网络连接 ES8311 对应引脚。

- 参数与网络：`dout=GPIO48 -> ASDOUT -> ES8311 pin7`；`din=GPIO4 -> DSDIN -> ES8311 pin9`；`ws=GPIO3 -> LRCK -> ES8311 pin8`；`bclk=GPIO17 -> SCLK -> ES8311 pin6`；`mclk=GPIO11 -> MCLK -> ES8311 pin2`
- 证据：图 0613b6a13ce3 / 第 1 页 / 主板 J4 GPIO48/4/3/17/11 音频映射; 图 5300a63ff310 / 第 1 页 / 音频板 BTB1/ES8311 I2S 网络

## 总线地址

### ES8311 I2C 地址

图面注记 CE low=0x18、CE high=0x19；U2 CE pin20 接 GND，因此装配地址为 0x18。

- 参数与网络：`device=U2 [audio] ES8311`；`ce=pin20 GND/low`；`address=0x18`；`alternate=0x19`
- 证据：图 5300a63ff310 / 第 1 页 / 网格 A2，地址注记与 CE pin20 接 GND

## GPIO 与控制信号

### NS4150B 功放控制

主控 GPIO18 通过板间网络 4150_CTR 连接 NS4150B CTRL pin1；R9 10K 将 4150_CTR 下拉至 GND。

- 参数与网络：`controller=U1 [main] GPIO18`；`net=4150_CTR`；`target=U3 [audio] pin1 CTRL`；`pulldown=R9 10K`
- 证据：图 0613b6a13ce3 / 第 1 页 / 主板 J4 GPIO18; 图 5300a63ff310 / 第 1 页 / 音频板 BTB1 4150_CTR、U3 CTRL、R9

### 用户按键

S1 SMT_SW_PTS_820 按下时将 USER_BUT/GPIO41 接地；R6 10K/1% 上拉至 VDD_3V3，C11 1nF/50V 对地滤波。

- 参数与网络：`button=S1`；`gpio=U1 GPIO41/USER_BUT`；`active_level=low`；`pullup=R6 10K/1%`；`filter=C11 1nF/50V`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 C4-C5，S1/R6/C11/USER_BUT

### 红外发射控制

U1 GPIO47 输出 IR_LED_DRV 到 FET2 栅极，R3 100K/1% 下拉；D2 红外 LED 从 VDD_3V3 经 R2 15R/1% 与 FET2 低端开关导通。

- 参数与网络：`gpio=U1 GPIO47`；`net=IR_LED_DRV`；`mosfet=FET2 CJ3134K KF`；`gate_pulldown=R3 100K/1%`；`led=D2 MIEHUA/MHS153IRCT`；`series=R2 15R/1%`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 B7-C8，GPIO47/IR_LED_DRV/FET2/D2/R2/R3

## 时钟

### 主控外部时钟

U1 XTAL_32K_P/N 与 XTAL_P/N 在本页均未连接，板上没有外部晶振；音频 MCLK/SCLK/LRCK 由 ESP32 GPIO 提供。

- 参数与网络：`xtal_32k=U1 pins21/22 NC`；`main_xtal=U1 pins52/53 NC`；`audio_clocks=GPIO11 MCLK,GPIO17 SCLK,GPIO3 LRCK`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 A3-B4，U1 XTAL 引脚红色 NC 与音频 GPIO

## 复位

### ESP_EN 复位按键

S2 SMT_SW_TS_015 按下时将 ESP_EN 接地，C17 1nF/50V 对地；ESP_EN 还通过 L4 33Ω@100MHz 接 U1 CHIP_PU，并由 R14 10K/C24 1uF 形成上电网络。

- 参数与网络：`button=S2`；`net=ESP_EN`；`target=U1 CHIP_PU via L4 33Ω@100MHz`；`pullup=R14 10K to VDD_3V3`；`caps=C17 1nF,C24 1uF`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 A2/C4-D5，ESP_EN/L4/S2/R14/C17/C24

## 保护电路

### USB 与扩展 GPIO 保护

USB VBUS 使用 F1 6V/2A/PPTC，USB D+/D- 使用 D3/D4 ESDS5Z3V3；J7 GPIO1/2 使用 D5/D6 ESDS5Z3V3 和串联 R17/R18。

- 参数与网络：`usb_power=F1 6V/2A/PPTC`；`usb_data=D3,D4 ESDS5Z3V3`；`gpio_esd=D5,D6 ESDS5Z3V3`；`gpio_series=R17,R18`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 A6-A8 与 B5-C6，USB/J7 保护

## 关键网络

### 语音采集、播放与控制路径

采集路径为麦克风 -> MIC_P/MIC_N -> ES8311 ADC -> ASDOUT/GPIO48；播放路径为 GPIO4 DSDIN -> ES8311 DAC -> OUTP/OUTN -> NS4150B -> H2；GPIO18 控制功放。

- 参数与网络：`capture=MSM381A3729H9BPC -> ES8311 -> ASDOUT -> GPIO48`；`playback=GPIO4 -> DSDIN -> ES8311 -> NS4150B -> SPK+/SPK-`；`clocks=GPIO11/GPIO17/GPIO3`；`amp_control=GPIO18/4150_CTR`
- 证据：图 0613b6a13ce3 / 第 1 页 / 主板 J4 音频 GPIO; 图 5300a63ff310 / 第 1 页 / 音频板 MIC/ES8311/NS4150B/H2

## 存储

### 外部存储

两张原理图未显示独立 Flash、EEPROM、eMMC 或存储卡；存储集成在 ESP32-S3-PICO-1-N8R8 SiP 内，容量未在图中明示。

- 参数与网络：`external_flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null`；`integrated_storage=inside U1 SiP`；`capacity=null`
- 证据：图 0613b6a13ce3 / 第 1 页 / 主板 U1 SiP，无外部存储; 图 5300a63ff310 / 第 1 页 / 音频板无存储

## 内存与 Flash

### 外部内存

原理图未显示外部 RAM/PSRAM/DDR；PSRAM 集成在 ESP32-S3-PICO-1-N8R8 SiP 内，容量未在图中明示。

- 参数与网络：`external_ram=null`；`ddr=null`；`integrated_psram=inside U1 SiP`；`capacity=null`
- 证据：图 0613b6a13ce3 / 第 1 页 / 主板 U1 SiP，无外部 RAM

## 音频

### ES8311 编解码器

音频板 U2 ES8311 的 MIC1P/MIC1N 接麦克风，OUTP/OUTN 接功放，数字侧使用 MCLK/SCLK/LRCK/DSDIN/ASDOUT，控制侧使用 SCL/SDA/CE。

- 参数与网络：`reference=U2 [audio]`；`part_number=ES8311`；`adc=MIC1P pin18,MIC1N pin17`；`dac=OUTP pin12,OUTN pin13`；`i2s=MCLK,SCLK,LRCK,DSDIN,ASDOUT`；`i2c=SCL,SDA`；`ce=pin20`
- 证据：图 5300a63ff310 / 第 1 页 / 网格 A2-B3，U2 ES8311 pins1-21

### MEMS 麦克风输入链

U1 MSM381A3729H9BPC OUT 经 C2 1uF/25V 形成 MIC_P 并接 ES8311 MIC1P；MIC_N 经 C5 1uF/25V 接 MIC1N，AGND 通过 R4 0R 接 GND。

- 参数与网络：`microphone=U1 [audio] MSM381A3729H9BPC`；`positive=OUT -> C2 -> MIC_P -> ES8311 MIC1P`；`negative=AGND/MIC_N -> C5 -> ES8311 MIC1N`；`ground_link=R4 0R`
- 证据：图 5300a63ff310 / 第 1 页 / 网格 A3-B4，U1/C2/C5/MIC_P/MIC_N 到 U2

### ES8311 DAC 到 NS4150B

ES8311 OUTN/OUTP 经 C11/C12 1uF 后，再经 C16/C17 100nF 与 R6/R8 150K 接 NS4150B INN/INP；NS4150B VoN/VoP 输出 SPK-/SPK+ 到 H2。

- 参数与网络：`negative_input=ES8311 OUTN -> C11 -> C16 -> R6 -> U3 INN`；`positive_input=ES8311 OUTP -> C12 -> C17 -> R8 -> U3 INP`；`negative_output=U3 VoN -> SPK- -> H2 pin2`；`positive_output=U3 VoP -> SPK+ -> H2 pin1`
- 证据：图 5300a63ff310 / 第 1 页 / 网格 B2-C3，ES8311 OUTN/P 到 U3/H2

## 传感器

### MEMS 麦克风传感器

音频板 U1 为 MSM381A3729H9BPC，pin4 OUT、pin1 VDD、pins2/3 GND，输出接 ES8311 模拟麦克风输入。

- 参数与网络：`reference=U1 [audio]`；`part_number=MSM381A3729H9BPC`；`output=pin4 OUT`；`supply=pin1 VDD`；`ground=pins2,3`；`codec=U2 ES8311`
- 证据：图 5300a63ff310 / 第 1 页 / 网格 A3-B4，U1 麦克风

## 射频

### ESP32-S3 PIFA 天线路径

U1 LNA_IN 通过 ESP_LNA 网络、R1 2.4nH 与 C1 2.7pF/C2 2.0pF 匹配连接 ANT1 ESP-H0920-PIFA。

- 参数与网络：`soc_pin=U1 LNA_IN`；`net=ESP_LNA`；`series=R1 2.4nH`；`shunt=C1 2.7pF,C2 2.0pF`；`antenna=ANT1 ESP-H0920-PIFA`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 A1-A3，ANT1/R1/C1/C2/ESP_LNA/U1

## 调试与烧录

### 下载模式辅助控制

U7 PMS150G-U6 连接 GPIO0/SYS_SCL、GPO_LED 与 ESP_EN，D1 GREEN 接 GPO_LED；该电路构成主板下载/状态辅助路径。

- 参数与网络：`controller=U7 PMS150G-U6`；`boot_signal=GPIO0/SYS_SCL`；`reset_signal=ESP_EN`；`indicator=D1 GREEN/GPO_LED`；`supply=VDD_3V3`
- 证据：图 0613b6a13ce3 / 第 1 页 / 网格 D1-D3，U7/D1/GPIO0/ESP_EN

## 模拟电路

### ES8311 模拟基准与耦合

ES8311 VMID/ADCVREF/DACVREF 分别用 C6/C7/C10 1uF 对地；AVDD 经 R5 0R 接 3.3V，OUTN/OUTP 经 C11/C12 1uF 交流耦合。

- 参数与网络：`vmid=C6 1uF`；`adcvref=C7 1uF`；`dacvref=C10 1uF`；`avdd=R5 0R,C13 1uF`；`dac_coupling=C11,C12 1uF`
- 证据：图 5300a63ff310 / 第 1 页 / 网格 B2-B3，ES8311 VMID/VREF/AVDD/OUTN/P 周边

## 其他事实

### 电池与充电路径

两张原理图未显示电池、充电器或电量监测器，系统由 USB-C VIN_5V 供电。

- 参数与网络：`battery=null`；`charger=null`；`fuel_gauge=null`；`input=USB-C VIN_5V`
- 证据：图 0613b6a13ce3 / 第 1 页 / 主板 USB-C/JW5712 电源路径，无 BAT/charger; 图 5300a63ff310 / 第 1 页 / 音频板仅 3.3V

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atom VoiceS3R 系统架构 | `soc=U1 [main] ESP32-S3-PICO-1-N8R8`；`codec=U2 [audio] ES8311`；`microphone=U1 [audio] MSM381A3729H9BPC`；`amplifier=U3 [audio] NS4150B`；`usb=J2`；`antenna=ANT1`；`ir=D2/FET2`；`expansion=J4/J7` |
| 核心器件 | ESP32-S3-PICO-1-N8R8 | `reference=U1 [main]`；`part_number=ESP32-S3-PICO-1-N8R8`；`rf=ESP_LNA`；`usb=GPIO19 USB_D_N,GPIO20 USB_D_P`；`supply=VDD_3V3`；`flash_psram_capacity=null` |
| 电源 | JW5712 3.3V 主电源 | `converter=U2 [main] JW5712`；`input=VIN_5V`；`enable=VIN_5V`；`inductor=L1 MWTC201608S2R2`；`output=VDD_3V3`；`input_caps=C15 10uF,C16 100nF`；`output_caps=C7 100nF,C13 10uF` |
| 接口 | USB-C 电源与数据 | `connector=J2`；`vbus=VCC -> F1 6V/2A/PPTC -> VIN_5V`；`cc1=R4 5.1K to GND`；`cc2=R5 5.1K to GND`；`dp=DP1,DP2 -> USB_D_P`；`dn=DN1,DN2 -> USB_D_N`；`ground=GND/SHIELD` |
| 总线 | ESP32-S3 原生 USB | `dm=J2 USB_D_N -> R20 22R -> U1 GPIO19`；`dp=J2 USB_D_P -> R19 22R -> U1 GPIO20`；`dm_esd=D4 ESDS5Z3V3`；`dp_esd=D3 ESDS5Z3V3` |
| 射频 | ESP32-S3 PIFA 天线路径 | `soc_pin=U1 LNA_IN`；`net=ESP_LNA`；`series=R1 2.4nH`；`shunt=C1 2.7pF,C2 2.0pF`；`antenna=ANT1 ESP-H0920-PIFA` |
| 音频 | ES8311 编解码器 | `reference=U2 [audio]`；`part_number=ES8311`；`adc=MIC1P pin18,MIC1N pin17`；`dac=OUTP pin12,OUTN pin13`；`i2s=MCLK,SCLK,LRCK,DSDIN,ASDOUT`；`i2c=SCL,SDA`；`ce=pin20` |
| 总线地址 | ES8311 I2C 地址 | `device=U2 [audio] ES8311`；`ce=pin20 GND/low`；`address=0x18`；`alternate=0x19` |
| 总线 | 主控到 ES8311 I2C | `sda_controller=U1 [main] GPIO45/SYS_SDA`；`scl_controller=U1 [main] GPIO0 -> L2 33Ω@100MHz -> SYS_SCL`；`device=U2 [audio] ES8311`；`pullups=R1 4.7K SCL,R2 4.7K SDA`；`level=3.3V` |
| 总线 | 主控到 ES8311 I2S | `dout=GPIO48 -> ASDOUT -> ES8311 pin7`；`din=GPIO4 -> DSDIN -> ES8311 pin9`；`ws=GPIO3 -> LRCK -> ES8311 pin8`；`bclk=GPIO17 -> SCLK -> ES8311 pin6`；`mclk=GPIO11 -> MCLK -> ES8311 pin2` |
| 音频 | MEMS 麦克风输入链 | `microphone=U1 [audio] MSM381A3729H9BPC`；`positive=OUT -> C2 -> MIC_P -> ES8311 MIC1P`；`negative=AGND/MIC_N -> C5 -> ES8311 MIC1N`；`ground_link=R4 0R` |
| 电源 | 麦克风滤波供电 | `rail=3.3V`；`ferrite=L1 120R@100MHz`；`target=U1 pin1 VDD`；`decoupling=C3 100nF,C4 10uF`；`output_filter=C1 22pF` |
| 音频 | ES8311 DAC 到 NS4150B | `negative_input=ES8311 OUTN -> C11 -> C16 -> R6 -> U3 INN`；`positive_input=ES8311 OUTP -> C12 -> C17 -> R8 -> U3 INP`；`negative_output=U3 VoN -> SPK- -> H2 pin2`；`positive_output=U3 VoP -> SPK+ -> H2 pin1` |
| GPIO 与控制信号 | NS4150B 功放控制 | `controller=U1 [main] GPIO18`；`net=4150_CTR`；`target=U3 [audio] pin1 CTRL`；`pulldown=R9 10K` |
| 电源 | 音频板 3.3V 供电 | `connector=BTB1`；`rail=3.3V`；`loads=ES8311,MSM381A3729H9BPC,NS4150B`；`ground=BTB1 GND pins` |
| GPIO 与控制信号 | 用户按键 | `button=S1`；`gpio=U1 GPIO41/USER_BUT`；`active_level=low`；`pullup=R6 10K/1%`；`filter=C11 1nF/50V` |
| 复位 | ESP_EN 复位按键 | `button=S2`；`net=ESP_EN`；`target=U1 CHIP_PU via L4 33Ω@100MHz`；`pullup=R14 10K to VDD_3V3`；`caps=C17 1nF,C24 1uF` |
| 调试与烧录 | 下载模式辅助控制 | `controller=U7 PMS150G-U6`；`boot_signal=GPIO0/SYS_SCL`；`reset_signal=ESP_EN`；`indicator=D1 GREEN/GPO_LED`；`supply=VDD_3V3` |
| GPIO 与控制信号 | 红外发射控制 | `gpio=U1 GPIO47`；`net=IR_LED_DRV`；`mosfet=FET2 CJ3134K KF`；`gate_pulldown=R3 100K/1%`；`led=D2 MIEHUA/MHS153IRCT`；`series=R2 15R/1%` |
| 接口 | J7 GH2.0-4P 扩展接口 | `connector=J7 GH2.0-4P`；`pin1=GPIO1 via R17 PRG15BC330MM1RC`；`pin2=GPIO2 via R18 PRG15BC330MM1RC`；`pin3=VIN_5V`；`pin4=GND`；`esd=D5,D6 ESDS5Z3V3` |
| 保护电路 | USB 与扩展 GPIO 保护 | `usb_power=F1 6V/2A/PPTC`；`usb_data=D3,D4 ESDS5Z3V3`；`gpio_esd=D5,D6 ESDS5Z3V3`；`gpio_series=R17,R18` |
| 时钟 | 主控外部时钟 | `xtal_32k=U1 pins21/22 NC`；`main_xtal=U1 pins52/53 NC`；`audio_clocks=GPIO11 MCLK,GPIO17 SCLK,GPIO3 LRCK` |
| 关键网络 | 语音采集、播放与控制路径 | `capture=MSM381A3729H9BPC -> ES8311 -> ASDOUT -> GPIO48`；`playback=GPIO4 -> DSDIN -> ES8311 -> NS4150B -> SPK+/SPK-`；`clocks=GPIO11/GPIO17/GPIO3`；`amp_control=GPIO18/4150_CTR` |
| 模拟电路 | ES8311 模拟基准与耦合 | `vmid=C6 1uF`；`adcvref=C7 1uF`；`dacvref=C10 1uF`；`avdd=R5 0R,C13 1uF`；`dac_coupling=C11,C12 1uF` |
| 存储 | 外部存储 | `external_flash=null`；`eeprom=null`；`emmc=null`；`storage_card=null`；`integrated_storage=inside U1 SiP`；`capacity=null` |
| 内存与 Flash | 外部内存 | `external_ram=null`；`ddr=null`；`integrated_psram=inside U1 SiP`；`capacity=null` |
| 传感器 | MEMS 麦克风传感器 | `reference=U1 [audio]`；`part_number=MSM381A3729H9BPC`；`output=pin4 OUT`；`supply=pin1 VDD`；`ground=pins2,3`；`codec=U2 ES8311` |
| 其他事实 | 电池与充电路径 | `battery=null`；`charger=null`；`fuel_gauge=null`；`input=USB-C VIN_5V` |
| 内存与 Flash | 集成 Flash 与 PSRAM 容量 | `device=ESP32-S3-PICO-1-N8R8`；`documented_flash=8MB`；`documented_psram=8MB Octal`；`schematic_flash_capacity=null`；`schematic_psram_capacity=null` |
| 音频 | 音频位宽与麦克风信噪比 | `documented_codec_resolution=24-bit`；`documented_mic_snr=65dB`；`codec=ES8311`；`microphone=MSM381A3729H9BPC`；`schematic_resolution=null`；`schematic_snr=null` |
| 音频 | 扬声器型号与额定值 | `documented_speaker=1318 cavity speaker`；`documented_rating=8Ω@1W`；`schematic_connector=H2 SpeakHeader`；`speaker_reference=null`；`schematic_rating=null` |
| 系统结构 | CPU 与 Wi-Fi 运行规格 | `documented_cpu=dual-core Xtensa LX7`；`documented_frequency=up to 240MHz`；`documented_wireless=2.4GHz Wi-Fi`；`schematic_soc=ESP32-S3-PICO-1-N8R8`；`schematic_antenna=ESP-H0920-PIFA`；`runtime_configuration=null` |

## 待确认事项

- `memory.documented-capacity`：正文称 ESP32-S3-PICO-1-N8R8 内含 8MB Flash 与 8MB PSRAM；原理图仅标完整 SiP 料号，没有直接给出容量数值或存储总线。（证据：图 0613b6a13ce3 / 第 1 页 / U1 ESP32-S3-PICO-1-N8R8，容量未展开）
- `audio.documented-format-mic`：正文称 ES8311 为 24位、MEMS 麦克风 SNR 65dB；原理图确认器件型号与音频路径，但没有位宽寄存器配置或 SNR 性能标注。（证据：图 5300a63ff310 / 第 1 页 / ES8311 与 MSM381A3729H9BPC 电路，无位宽/SNR 注记）
- `audio.documented-speaker`：正文称内置 1318 型腔体扬声器为 8Ω@1W；原理图只显示 H2 SpeakHeader 的 SPK+/SPK-，没有扬声器位号、型号、阻抗或功率。（证据：图 5300a63ff310 / 第 1 页 / 网格 C2，H2 SPK+/SPK-，无扬声器器件）
- `system.documented-performance`：正文称双核 Xtensa LX7 最高 240MHz并支持 2.4GHz Wi-Fi；原理图确认 ESP32-S3-PICO-1-N8R8 与 PIFA 天线，但不包含 CPU 频率配置或射频性能参数。（证据：图 0613b6a13ce3 / 第 1 页 / U1 与 ANT1 电路，无 CPU/Wi-Fi 性能表）
- `review.memory-capacity`：请依据 ESP32-S3-PICO-1-N8R8 datasheet、芯片检测或量产 BOM 确认 8MB Flash 与 8MB Octal PSRAM。；原因：原理图只给出 SiP 料号，没有容量数值。
- `review.audio-format-mic`：请用 ES8311 寄存器配置和 MSM381A3729H9BPC datasheet/测试确认 24位音频与 65dB SNR。；原因：原理图不包含运行位宽或麦克风性能参数。
- `review.speaker`：请用量产 BOM、扬声器标签或阻抗/功率测试确认 1318 型腔体扬声器为 8Ω@1W。；原因：原理图只显示 H2 扬声器接口。
- `review.system-performance`：请依据 ESP32-S3-PICO-1-N8R8 datasheet、时钟配置和无线测试确认 CPU 核心/240MHz 与 2.4GHz Wi-Fi 规格。；原因：原理图确认器件和天线，但不证明运行频率与射频性能。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `0613b6a13ce3fd85434c81a991425bd2824f7a1005b171b7dd7fc5228287c3e6` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/Sch_M5_AtomS3R_v0.4.1.png` |
| 2 | 1 | `5300a63ff310cbfa12fdbbc06adfb90ba0c18e9b63715bc7208e9c5f9bda7ced` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/Sch_M5_AtomEchoS3R_Audio_v1.0_20250716_page_01.png` |

---

源文档：`zh_CN/core/Atom_EchoS3R.md`

源文档 SHA-256：`4a90f34da221d1ebdf607611205241dc0a39e7aec31a6a383c47ff15a5fc45ed`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
