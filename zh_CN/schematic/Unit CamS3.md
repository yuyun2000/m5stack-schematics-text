# Unit CamS3 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit CamS3 |
| SKU | U174 |
| 产品 ID | `unit-cams3-5a4131b60dd3` |
| 源文档 | `zh_CN/unit/Unit-CamS3.md` |

## 概述

Unit CamS3 以 U5 ESP32-S3-WROOM-1-N16R8 为核心，通过 8 位并行像素总线、PCLK/HREF/VSYNC/XCLK、SIO_C/SIO_D 和 RESET 连接 U2 24 针摄像头 FPC。U6 TF CARD 通过 GPIO9/38/39/40 的 SPI 总线连接主控，U7 MSM261DHP006 通过 GPIO47/48 的 MIC_CLK/MIC_DATA 提供 PDM 音频输入。J1 将 GPIO19/GPIO20 作为 RX/D- 与 TX/D+ 引出，P1/P2 提供串口、EN、GPIO0、SDA/SCL 下载/扩展接口。+5V 经 U1 SY8089AAAC 生成 +3V，再由 U3/U4 生成摄像头 +1.2V/+2.8V；原理图未直接标 OV2640、2MP/DFOV、Flash/PSRAM 容量或 WiFi 参数。

## 检索关键词

`Unit CamS3`、`U174`、`ESP32-S3-WROOM-1-N16R8`、`ESP32-S3`、`OV2640`、`FPC-0.5-24P`、`MSM261DHP006`、`MSM1261D4030HCPM`、`SY8089AAAC`、`HX6306P122MR`、`XC6206P282MR`、`TF CARD`、`microSD`、`SPI_CS GPIO9`、`SPI_MOSI GPIO38`、`SPI_CLK GPIO39`、`SPI_MISO GPIO40`、`SIO_C GPIO41`、`SIO_D GPIO17`、`XCLK GPIO11`、`PCLK GPIO12`、`VSYNC GPIO42`、`HREF GPIO18`、`RESET GPIO21`、`camera D2-D9`、`MIC_CLK GPIO47`、`MIC_DATA GPIO48`、`GPIO14 LED`、`GPIO19 D-`、`GPIO20 D+`、`RXD0`、`TXD0`、`GPIO0 boot`、`EN reset`、`+5V`、`+3V`、`+2.8V`、`+1.2V`、`USB`、`PDM microphone`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U5 | ESP32-S3-WROOM-1-N16R8 | 主控模组，连接摄像头、microSD、PDM 麦克风、USB/Grove、LED 和下载排针 | 图 61e511ccc274 / 第 1 页 / 第 1 页中央 U5 ESP32-S3-WROOM-1-N16R8，pins1-41 与全部 GPIO 网络 |
| U2 | FPC-0.5-24P | 摄像头 24 针 FPC 接口，承载并行像素、时序、SCCB、复位与三路电源 | 图 61e511ccc274 / 第 1 页 / 第 1 页右上 U2 FPC-0.5-24P pins1-24，Y0-Y9/PCLK/XCLK/HREF/PWDN/VSYNC/RESET/SIO_C/SIO_D/AVDD/DOVDD/DVDD |
| U6 | TF CARD | microSD 卡座，使用 SPI_CS/MOSI/CLK/MISO 与 +3V/GND | 图 61e511ccc274 / 第 1 页 / 第 1 页右中 U6 TF CARD pins1-10 与 SPI_CS/SPI_MOSI/SPI_CLK/SPI_MISO/+3V/GND |
| U7 | MSM261DHP006 | 3V 供电的 PDM 麦克风，输出 MIC_DATA 并接收 MIC_CLK | 图 61e511ccc274 / 第 1 页 / 第 1 页左下 U7 MSM261DHP006，VDD/L-R/CLK/DATA/GND pins1-8 |
| U1 | SY8089AAAC | 将 +5V 降压为 +3V 的开关稳压器 | 图 61e511ccc274 / 第 1 页 / 第 1 页左上 U1 SY8089AAAC，IN/EN/GND/LX/FB 与 L1/R1/R2/C1-C3/C12 |
| U3 | HX6306P122MR 1.2V 300mA SOT23-3 | 由 +3V 生成摄像头 DVDD +1.2V 的 LDO | 图 61e511ccc274 / 第 1 页 / 第 1 页左上 U3 LDO HX6306P122MR 1.2V 300mA，VDD/VOUT/GND 与 C4/C5 |
| U4 | XC6206P282MR 2.8V LDO 150mA | 由 +3V 生成摄像头 AVDD/DOVDD +2.8V 的 LDO | 图 61e511ccc274 / 第 1 页 / 第 1 页左上 U4 XC6206P282MR/2.8V LDO 150mA，VDD/VOUT/GND 与 C6-C8 |
| J1 | HY-2.0_UART | GPIO19/GPIO20 USB 或串行信号与 +5V/GND Grove 接口 | 图 61e511ccc274 / 第 1 页 / 第 1 页右下 J1 HY-2.0_UART，pin1 RX/D- GPIO19、pin2 TX/D+ GPIO20、pin3 +5V、pin4 GND |
| P1,P2 | Header 4 / Header 4 | 下载和扩展排针，提供 GPIO3/RXD0/TXD0/+5V 以及 GPIO8/EN/GPIO0/GND | 图 61e511ccc274 / 第 1 页 / 第 1 页右中 P1/P2 Header4，顶部标 SDA/SCL，pins1-4 的 GPIO3/RXD0/TXD0/+5V 与 GPIO8/EN/GPIO0/GND |
| D1,R7 | Blue 0603 / 1K | GPIO14 控制的蓝色可编程状态 LED | 图 61e511ccc274 / 第 1 页 / 第 1 页中央下方 GPIO14-R7 1K-D1 Blue 0603-+3V 支路 |
| R6,C11 | 10KΩ / 100nF | U5 EN 的 +3V 上拉与对地复位电容 | 图 61e511ccc274 / 第 1 页 / 第 1 页左中 R6 10KΩ 从 EN 到 +3V、C11 100nF 从 EN 到 GND |
| R8,R9,R10,R11 | 10KΩ | microSD DAT2、CS/DAT3、CMD/MOSI、DAT0/MISO 相关线路的 +3V 上拉网络 | 图 61e511ccc274 / 第 1 页 / 第 1 页右中 U6 左侧 R8-R11 四个 10KΩ 上拉到 +3V |

## 系统结构

### Unit CamS3 系统架构

U5 ESP32-S3-WROOM-1-N16R8 连接 U2 摄像头 FPC、U6 microSD、U7 PDM 麦克风、D1 蓝色 LED、J1 USB/Grove 和 P1/P2 下载排针。+5V 经 U1 形成 +3V，U3/U4 再生成摄像头 +1.2V/+2.8V。

- 参数与网络：`controller=U5 ESP32-S3-WROOM-1-N16R8`；`camera=U2 FPC-0.5-24P`；`storage=U6 TF CARD`；`audio=U7 MSM261DHP006`；`external_interface=J1 HY-2.0_UART`；`debug=P1,P2`；`power=+5V -> +3V -> +1.2V/+2.8V`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页完整单页，U1-U7/J1/P1/P2/D1 全部功能区

## 电源

### +5V 至 +3V 降压

+5V 连接 U1 SY8089AAAC IN pin4 与 EN pin1，LX pin3 经 L1 WPN252012H2R2MT 输出 +3V；R1 43KΩ/R2 10KΩ 连接 FB pin5，C12 22pF 跨 R1，输入 C1 22uF、输出 C2/C3 各 22uF 对地。

- 参数与网络：`converter=U1 SY8089AAAC`；`input=+5V -> IN pin4,EN pin1`；`inductor=L1 WPN252012H2R2MT`；`output=+3V`；`feedback=R1 43K,R2 10K,C12 22pF`；`input_cap=C1 22uF`；`output_caps=C2/C3 22uF`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页左上 U1/L1/R1/R2/C1-C3/C12 与 +5V/+3V

### 摄像头 +1.2V 与 +2.8V 电源

+3V 输入 U3 HX6306P122MR，输出 +1.2V 到 U2 DVDD pin10；+3V 输入 U4 XC6206P282MR，输出 +2.8V 到 U2 DOVDD pin11 与 AVDD pin4。U3 使用 C4 22uF/C5 47uF，U4 使用 C6 47uF/C7 100nF/C8 47uF。

- 参数与网络：`digital_core=U3 HX6306P122MR -> +1.2V -> U2 pin10 DVDD`；`io_analog=U4 XC6206P282MR -> +2.8V -> U2 pin11 DOVDD,pin4 AVDD`；`u3_caps=C4 22uF,C5 47uF`；`u4_caps=C6 47uF,C7 100nF,C8 47uF`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页左上 U3/U4 与右上 U2 DVDD/DOVDD/AVDD 同名电源

## 接口

### J1 Grove USB/UART 双命名接口

J1 HY-2.0_UART pin1 标 RX/D- 并连接 U5 GPIO19，pin2 标 TX/D+ 并连接 GPIO20，pin3 接 +5V，pin4 接 GND；原理图同时保留串行 RX/TX 与 USB D-/D+ 功能命名。

- 参数与网络：`connector=J1 HY-2.0_UART`；`pin1=RX/D- -> GPIO19`；`pin2=TX/D+ -> GPIO20`；`pin3=+5V`；`pin4=GND`；`usb_dm=GPIO19`；`usb_dp=GPIO20`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页右下 J1 pins1-4 与中央 U5 GPIO19/GPIO20

## 总线

### 摄像头 8 位并行像素总线

U2 Y2/Y3/Y4/Y5/Y6/Y7/Y8/Y9 分别连接 U5 GPIO6/GPIO15/GPIO16/GPIO7/GPIO5/GPIO10/GPIO4/GPIO13；U2 PCLK pin17 经 R3 47Ω 连接 GPIO12。Y0/Y1 在本页带未连接标记。

- 参数与网络：`bit0=U2 Y2 pin19 -> GPIO6`；`bit1=Y3 pin21 -> GPIO15`；`bit2=Y4 pin22 -> GPIO16`；`bit3=Y5 pin20 -> GPIO7`；`bit4=Y6 pin18 -> GPIO5`；`bit5=Y7 pin16 -> GPIO10`；`bit6=Y8 pin14 -> GPIO4`；`bit7=Y9 pin12 -> GPIO13`；`pixel_clock=PCLK pin17 -> R3 47R -> GPIO12`；`unused=Y0 pin24,Y1 pin23 NC`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页右上 U2 pins12-24 与中央 U5 GPIO4-7/10/12/13/15/16

### 摄像头 SCCB、时钟与同步控制

U2 XCLK pin13 经 R4 47Ω 接 GPIO11，HREF pin9 接 GPIO18，VSYNC pin7 接 GPIO42，RESET pin6 接 GPIO21，SIO_C pin5 接 GPIO41，SIO_D pin3 接 GPIO17；PWDN pin8 经 R5 10KΩ 接 GND。

- 参数与网络：`xclk=U2 pin13 -> R4 47R -> GPIO11`；`href=pin9 -> GPIO18`；`vsync=pin7 -> GPIO42`；`reset=pin6 -> GPIO21`；`sccb_clock=pin5 SIO_C -> GPIO41`；`sccb_data=pin3 SIO_D -> GPIO17`；`power_down=pin8 PWDN -> R5 10K -> GND`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页右上 U2 pins3-9/13 与 U5 GPIO11/17/18/21/41/42

## GPIO 与控制信号

### GPIO14 蓝色 LED

U5 GPIO14 通过 R7 1K 接到 D1 Blue 0603，D1 另一端接 +3V；该连接形成由 GPIO14 下拉点亮的蓝色指示支路。

- 参数与网络：`gpio=U5 GPIO14`；`resistor=R7 1K`；`led=D1 Blue 0603`；`rail=+3V`；`active_level=low`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页中央下方 U5 GPIO14/R7/D1/+3V

## 时钟

### 摄像头 XCLK/PCLK 时钟

U5 GPIO11 经 R4 47Ω 向 U2 XCLK pin13 提供系统时钟，U2 PCLK pin17 经 R3 47Ω 返回 U5 GPIO12；板级页面未显示独立摄像头晶振。

- 参数与网络：`camera_clock_out=GPIO11 -> R4 47R -> U2 pin13 XCLK`；`pixel_clock_in=U2 pin17 PCLK -> R3 47R -> GPIO12`；`external_camera_crystal=null`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页右上 U2 XCLK/PCLK、R3/R4 与 U5 GPIO11/GPIO12

## 复位

### U5 EN 复位网络

U5 EN pin3 连接 EN 网络，R6 10KΩ 将 EN 上拉到 +3V，C11 100nF 将 EN 接 GND，EN 同时引至 P2 pin2。

- 参数与网络：`module_pin=U5 pin3 EN`；`pullup=R6 10K to +3V`；`capacitor=C11 100nF to GND`；`header=P2 pin2 EN`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页左中 R6/C11/EN、U5 pin3 与右中 P2 pin2

## 保护电路

### J1 和外部接口保护边界

J1 GPIO19/GPIO20/+5V、P1/P2 和 U6 microSD 信号直接进入 U5 或电源/上拉网络；本页没有显示 USB ESD 二极管、5V 保险丝、反接保护或接口共模滤波器。

- 参数与网络：`interfaces=J1,P1,P2,U6`；`usb_esd=null`；`five_volt_fuse=null`；`reverse_protection=null`；`common_mode_filter=null`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页完整 J1/P1/P2/U6 至 U5 和电源路径，未见专用接口保护器件

## 存储

### microSD SPI 连接

U6 CD/DAT3 pin2 接 SPI_CS/GPIO9，CMD/MOSI pin3 接 SPI_MOSI/GPIO38，CLK pin5 接 SPI_CLK/GPIO39，DAT0/MISO pin7 接 SPI_MISO/GPIO40；VDD pin4 接 +3V、VSS pin6 与外壳 pins8-10 接 GND。

- 参数与网络：`card=U6 TF CARD`；`chip_select=pin2 CD/DAT3 -> SPI_CS -> GPIO9`；`mosi=pin3 CMD/MOSI -> GPIO38`；`clock=pin5 CLK -> GPIO39`；`miso=pin7 DAT0/MISO -> GPIO40`；`supply=pin4 +3V`；`ground=pin6,pins8-10 GND`；`pullups=R8-R11 10K to +3V`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页右中 U6/R8-R11 与中央 U5 GPIO9/38/39/40

## 音频

### U7 PDM 麦克风连接

U7 原理图型号标为 MSM261DHP006；VDD pin1 接 +3V 并由 C9 1uF 对地，L/R pin2 接 GND，CLK pin3 接 MIC_CLK/GPIO47，DATA pin4 接 MIC_DATA/GPIO48，pins5-8 接 GND。

- 参数与网络：`microphone=U7 MSM261DHP006`；`supply=pin1 VDD +3V`；`decoupling=C9 1uF`；`channel_select=pin2 L/R -> GND`；`clock=pin3 MIC_CLK -> GPIO47`；`data=pin4 MIC_DATA -> GPIO48`；`grounds=pins5-8 GND`；`interface=PDM`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页左下 U7 MSM261DHP006/C9 与中央 U5 MIC_CLK/MIC_DATA

## 调试与烧录

### P1/P2 下载与扩展排针

P1 pin1=GPIO3（上方标 SDA）、pin2=RXD0、pin3=TXD0、pin4=+5V；P2 pin1=GPIO8（上方标 SCL）、pin2=EN、pin3=GPIO0、pin4=GND。RXD0/TXD0 连接 U5 pins36/37，EN 和 GPIO0 可用于复位/下载控制。

- 参数与网络：`P1=pin1 GPIO3/SDA,pin2 RXD0,pin3 TXD0,pin4 +5V`；`P2=pin1 GPIO8/SCL,pin2 EN,pin3 GPIO0,pin4 GND`；`uart=U5 pin36 RXD0,pin37 TXD0`；`download_controls=EN,GPIO0`
- 证据：图 61e511ccc274 / 第 1 页 / 第 1 页右中 P1/P2 Header4 与中央 U5 GPIO3/GPIO8/RXD0/TXD0/EN/GPIO0

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit CamS3 系统架构 | `controller=U5 ESP32-S3-WROOM-1-N16R8`；`camera=U2 FPC-0.5-24P`；`storage=U6 TF CARD`；`audio=U7 MSM261DHP006`；`external_interface=J1 HY-2.0_UART`；`debug=P1,P2`；`power=+5V -> +3V -> +1.2V/+2.8V` |
| 电源 | +5V 至 +3V 降压 | `converter=U1 SY8089AAAC`；`input=+5V -> IN pin4,EN pin1`；`inductor=L1 WPN252012H2R2MT`；`output=+3V`；`feedback=R1 43K,R2 10K,C12 22pF`；`input_cap=C1 22uF`；`output_caps=C2/C3 22uF` |
| 电源 | 摄像头 +1.2V 与 +2.8V 电源 | `digital_core=U3 HX6306P122MR -> +1.2V -> U2 pin10 DVDD`；`io_analog=U4 XC6206P282MR -> +2.8V -> U2 pin11 DOVDD,pin4 AVDD`；`u3_caps=C4 22uF,C5 47uF`；`u4_caps=C6 47uF,C7 100nF,C8 47uF` |
| 总线 | 摄像头 8 位并行像素总线 | `bit0=U2 Y2 pin19 -> GPIO6`；`bit1=Y3 pin21 -> GPIO15`；`bit2=Y4 pin22 -> GPIO16`；`bit3=Y5 pin20 -> GPIO7`；`bit4=Y6 pin18 -> GPIO5`；`bit5=Y7 pin16 -> GPIO10`；`bit6=Y8 pin14 -> GPIO4`；`bit7=Y9 pin12 -> GPIO13`；`pixel_clock=PCLK pin17 -> R3 47R -> GPIO12`；`unused=Y0 pin24,Y1 pin23 NC` |
| 总线 | 摄像头 SCCB、时钟与同步控制 | `xclk=U2 pin13 -> R4 47R -> GPIO11`；`href=pin9 -> GPIO18`；`vsync=pin7 -> GPIO42`；`reset=pin6 -> GPIO21`；`sccb_clock=pin5 SIO_C -> GPIO41`；`sccb_data=pin3 SIO_D -> GPIO17`；`power_down=pin8 PWDN -> R5 10K -> GND` |
| 存储 | microSD SPI 连接 | `card=U6 TF CARD`；`chip_select=pin2 CD/DAT3 -> SPI_CS -> GPIO9`；`mosi=pin3 CMD/MOSI -> GPIO38`；`clock=pin5 CLK -> GPIO39`；`miso=pin7 DAT0/MISO -> GPIO40`；`supply=pin4 +3V`；`ground=pin6,pins8-10 GND`；`pullups=R8-R11 10K to +3V` |
| 音频 | U7 PDM 麦克风连接 | `microphone=U7 MSM261DHP006`；`supply=pin1 VDD +3V`；`decoupling=C9 1uF`；`channel_select=pin2 L/R -> GND`；`clock=pin3 MIC_CLK -> GPIO47`；`data=pin4 MIC_DATA -> GPIO48`；`grounds=pins5-8 GND`；`interface=PDM` |
| 接口 | J1 Grove USB/UART 双命名接口 | `connector=J1 HY-2.0_UART`；`pin1=RX/D- -> GPIO19`；`pin2=TX/D+ -> GPIO20`；`pin3=+5V`；`pin4=GND`；`usb_dm=GPIO19`；`usb_dp=GPIO20` |
| 调试与烧录 | P1/P2 下载与扩展排针 | `P1=pin1 GPIO3/SDA,pin2 RXD0,pin3 TXD0,pin4 +5V`；`P2=pin1 GPIO8/SCL,pin2 EN,pin3 GPIO0,pin4 GND`；`uart=U5 pin36 RXD0,pin37 TXD0`；`download_controls=EN,GPIO0` |
| 复位 | U5 EN 复位网络 | `module_pin=U5 pin3 EN`；`pullup=R6 10K to +3V`；`capacitor=C11 100nF to GND`；`header=P2 pin2 EN` |
| GPIO 与控制信号 | GPIO14 蓝色 LED | `gpio=U5 GPIO14`；`resistor=R7 1K`；`led=D1 Blue 0603`；`rail=+3V`；`active_level=low` |
| 时钟 | 摄像头 XCLK/PCLK 时钟 | `camera_clock_out=GPIO11 -> R4 47R -> U2 pin13 XCLK`；`pixel_clock_in=U2 pin17 PCLK -> R3 47R -> GPIO12`；`external_camera_crystal=null` |
| 保护电路 | J1 和外部接口保护边界 | `interfaces=J1,P1,P2,U6`；`usb_esd=null`；`five_volt_fuse=null`；`reverse_protection=null`；`common_mode_filter=null` |
| 传感器 | 正文中的 OV2640 摄像头规格 | `schematic_connector=U2 FPC-0.5-24P`；`documented_sensor=OV2640`；`documented_pixels=2MP`；`documented_resolution=1600x1200`；`documented_dfov=66.5 degrees`；`documented_formats=YUV422/420,YCbCr422,RGB565/555,Raw RGB`；`schematic_sensor_model=null` |
| 内存与 Flash | 正文中的 16MB Flash 与 8MB PSRAM | `module=U5 ESP32-S3-WROOM-1-N16R8`；`documented_flash=16MB`；`documented_psram=8MB`；`internal_flash_reference=null`；`internal_psram_reference=null`；`internal_bus=null` |
| 音频 | 麦克风型号冲突 | `schematic_model=MSM261DHP006`；`documented_model=MSM1261D4030HCPM`；`reference=U7`；`interface=PDM`；`clock=GPIO47`；`data=GPIO48` |
| 射频 | 正文中的 WiFi 与板载天线 | `module=U5 ESP32-S3-WROOM-1-N16R8`；`documented_radio=WiFi`；`documented_antenna=module onboard antenna`；`rf_pin=null`；`matching_network=null`；`frequency=null`；`tx_power=null` |

## 待确认事项

- `sensor.documented-camera-module`：产品正文称摄像头为 OV2640、2MP、最高 1600x1200、DFOV 66.5°并支持多种 YUV/RGB/Raw 格式；原理图只显示 U2 FPC-0.5-24P 的电气连接，没有摄像头料号、像素、镜头视场或输出格式文字。（证据：图 61e511ccc274 / 第 1 页 / 第 1 页右上 U2 仅标 FPC-0.5-24P 与引脚，无 OV2640/2MP/DFOV 文字）
- `memory.documented-module-capacity`：U5 料号明确为 ESP32-S3-WROOM-1-N16R8，产品正文将其解释为 16MB Flash 和 8MB PSRAM；板级原理图没有展开模组内部 Flash/PSRAM 芯片、总线、容量或料号。（证据：图 61e511ccc274 / 第 1 页 / 第 1 页中央 U5 仅显示 ESP32-S3-WROOM-1-N16R8 模组外部引脚）
- `audio.microphone-model-conflict`：原理图 U7 型号为 MSM261DHP006，而产品正文规格表写 MSM1261D4030HCPM；两者字符串不一致，当前量产 BOM 和实际器件型号需确认。（证据：图 61e511ccc274 / 第 1 页 / 第 1 页左下 U7 型号文字 MSM261DHP006）
- `rf.documented-wifi`：产品正文称 ESP32-S3-WROOM-1-N16R8 支持 WiFi 并使用模组板载天线；本页将 U5 作为封装模组，未展开内部射频芯片、匹配、天线结构、频段、协议版本或发射功率。（证据：图 61e511ccc274 / 第 1 页 / 第 1 页 U5 模组符号没有 RF/天线内部展开）
- `review.camera-module`：请用 U174 当前摄像头 BOM、丝印或模组规格确认 OV2640、2MP、1600x1200、66.5° DFOV 与输出格式。；原因：板级原理图只显示摄像头 FPC 电气接口，不能证明传感器和镜头规格。
- `review.module-memory`：请用 ESP32-S3-WROOM-1-N16R8 模组资料或实机确认 16MB Flash、8MB PSRAM 及其接口配置。；原因：当前板级原理图未展开模组内部存储器。
- `review.microphone-bom`：U174 当前量产麦克风是原理图的 MSM261DHP006，还是正文的 MSM1261D4030HCPM？；原因：原理图与产品正文的麦克风型号明确冲突。
- `review.wifi-radio`：请用模组资料或认证报告确认 U174 的 WiFi 频段、协议版本、板载天线实现与射频功率边界。；原因：板级原理图没有展开 U5 内部射频与天线。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `61e511ccc274935b99ae3795153e35fa350310e5d08796955d258f0e4eec884b` | `https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-CamS3/img-e3213db4-1167-4f95-b6b5-9ff7a42d0111.png` |

---

源文档：`zh_CN/unit/Unit-CamS3.md`

源文档 SHA-256：`bcecd5747be27a8bac04767aa64bf9e4919b9b149397dac9fb1df93a29b2f036`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
