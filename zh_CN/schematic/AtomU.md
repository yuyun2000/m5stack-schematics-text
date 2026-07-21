# AtomU 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | AtomU |
| SKU | K117 |
| 产品 ID | `atomu-83b61895ae06` |
| 源文档 | `zh_CN/core/ATOM U.md` |

## 概述

AtomU 以 U1 ESP32-PICO-D4 为主控，U2 CH552T 通过 USB-A 提供 USB-UART 下载调试，CH552_RXD/TXD 经 470Ω 电阻连接 ESP_TXD/ESP_RXD。USB 5V 经 U3 SY8089A 和 L2 转换为 VCC_3V3，为 ESP32、SPM1423 PDM 麦克风、SK6812 和按键供电。GPIO5/GPIO19 连接麦克风 CLK/DATA，GPIO12 驱动红外 LED，GPIO27 驱动 RGB，GPIO39读取用户按键；GPIO32/GPIO26 引到 Grove，GPIO21/22/33/25 引到六针扩展口。

## 检索关键词

`AtomU`、`K117`、`ESP32-PICO-D4`、`CH552T`、`SY8089A`、`SPM1423HM4H-B`、`SK6812`、`USB Type-A`、`USB-UART`、`CH552_RXD`、`CH552_TXD`、`ESP_TXD`、`ESP_RXD`、`GPIO0`、`ESP_EN`、`GPIO5 MIC_CLK`、`GPIO19 MIC_DATA`、`GPIO12 IR_LED`、`GPIO27 RGB`、`GPIO39 USER_SW`、`GPIO32`、`GPIO26`、`GPIO21`、`GPIO22`、`GPIO33`、`GPIO25`、`GROVE`、`JP1`、`SRV05-4`、`BAT54C`、`Proant 440`、`VCC_VUSB`、`VCC_3V3`、`VCC_VUSB_E`、`PDM microphone`、`IR LED`、`RST Button`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-PICO-D4 | AtomU 主控，连接 USB-UART、射频天线、PDM 麦克风、红外、RGB、按键与扩展 GPIO | 图 6f5407ad4740 / 第 1 页 / 第 1 页中央 ESP32_PICO 区 U1 ESP32-PICO-D4，49 脚方框及 IO/电源/LNA_IN |
| U2 | CH552T | USB 设备与 ESP32 UART 之间的 USB-UART/自动下载控制器 | 图 6f5407ad4740 / 第 1 页 / 第 1 页左上 CH552_USB2UART 区 U2 CH552T，USB_DP/DM、CH552_RXD/TXD、GPIO0_IN、ESP32_EN_IN |
| USB1 | USB Type-A | VCC_VUSB 电源与 USB_DP/USB_DM 数据输入连接器 | 图 6f5407ad4740 / 第 1 页 / 第 1 页左下 USB_TypeA 区 USB1，pin1 VCC_VUSB、pin2 USB_DM、pin3 USB_DP、pin4 GND |
| D3 | SRV05-4 | USB_DP、USB_DM 与 VCC_VUSB 的多路 ESD 保护器件 | 图 6f5407ad4740 / 第 1 页 / 第 1 页 USB1 右侧 D3 SRV05-4，IO1 USB_DM、IO2 USB_DP、VCC VCC_VUSB、GND |
| U3 | SY8089A | 将 VCC_VUSB 降压为 VCC_3V3 的开关转换器 | 图 6f5407ad4740 / 第 1 页 / 第 1 页下中 3V3_Power 区 U3 SY8089A、L2、R14/R15 与输入输出电容 |
| L2 | WPN3012H2R2MT | SY8089A 的输出电感，连接 SW 与 VCC_3V3 | 图 6f5407ad4740 / 第 1 页 / 第 1 页 3V3_Power 区 U3 SW 后 L2 WPN3012H2R2MT |
| MIC1 | SPM1423HM4H-B | 数字 PDM 麦克风，CLK 接 GPIO5、DATA 接 GPIO19 | 图 6f5407ad4740 / 第 1 页 / 第 1 页右中 Microphone 区 MIC1 SPM1423HM4H-B，CLK/DATA/SELECT/VCC/GND |
| LED1 | SK6812 | 由 ESP32 GPIO27 驱动的单颗可编程 RGB LED | 图 6f5407ad4740 / 第 1 页 / 第 1 页右上 RGB_LED 区 LED1 SK6812，DIN 接 ESP_GP27、VCC_3V3、GND，DOUT NC |
| LED2,R9 | IR LED / 22Ω | 由 ESP32 GPIO12 直接驱动的红外发射 LED 与串联限流电阻 | 图 6f5407ad4740 / 第 1 页 / 第 1 页中央 IR_LED 区 U1 IO12-IR_LED-R9 22Ω-LED2-GND |
| S1,DZ1,R8 | PTS_820 / 3v3 TVS / pull-up resistor | GPIO39 用户按键、上拉和 ESD 钳位网络 | 图 6f5407ad4740 / 第 1 页 / 第 1 页右中 USER_SW 区 ESP_GP39_SW、S1 PTS_820、DZ1、R8 到 VCC_3V3 |
| S2,D1,R12,R13,C16 | TS-045 / BAT54C / 12KΩ / 1KΩ / 470nF | ESP_EN 与 GPIO0 自动下载/复位及手动 RST 按键网络 | 图 6f5407ad4740 / 第 1 页 / 第 1 页中央 RST_Button 区 D1 BAT54C、S2 TS_045、R12/R13/C16、ESP_EN/GPIO0 |
| ANT1,L1,C1,C2 | Proant 440 / 2.7nH / 3.0pF / 1.5pF | ESP32-PICO-D4 LNA_IN 的 2.4GHz 板载天线匹配网络 | 图 6f5407ad4740 / 第 1 页 / 第 1 页右上 ANT 区 ANT1 Proant_440、L1 2.7nH、C1 3.0pF、C2 1.5pF 到 U1 LNA_IN |
| GROVE | HY2.0-4P | 引出 GPIO32、GPIO26、VCC_VUSB_E 与 GND 的 Grove 接口 | 图 6f5407ad4740 / 第 1 页 / 第 1 页右下 GROVE 区，IO2 ESP_GP32_E、IO1 ESP_GP26_E、5V VCC_VUSB_E、GND |
| JP1 | Header 6 | 引出 GPIO21、GPIO22、GPIO33、GPIO25、VCC_VUSB_E 与 GND 的六针扩展口 | 图 6f5407ad4740 / 第 1 页 / 第 1 页右下 EXT_IO 区 JP1 pin6-pin1 与 ESP_GP21_E/22_E/33_E/25_E/VCC_VUSB_E/GND |
| D2,D4 | SRV05-4 | Grove、扩展 GPIO 与 ESP_EN 的多路 ESD 保护阵列 | 图 6f5407ad4740 / 第 1 页 / 第 1 页右下 D2/D4 SRV05-4，连接 ESP_EN 与 ESP_GP21/22/25/26/32/33_E |
| F1,C14 | 6V/1A PPTC / 4.7uF | VCC_VUSB 到扩展 VCC_VUSB_E 的电源保护和旁路 | 图 6f5407ad4740 / 第 1 页 / 第 1 页 EXT_IO 下方 VCC_VUSB-F1 6V/1A-VCC_VUSB_E 与 C14 4.7uF |
| R1,R2,R4 | 4.7KΩ / 470Ω / 470Ω | CH552 自动下载 GPIO0 与 ESP32 UART 串联连接电阻 | 图 6f5407ad4740 / 第 1 页 / 第 1 页 U2/U1 之间 GPIO0_IN-R1 4.7K、CH552_RXD-R2 470R、CH552_TXD-R4 470R |
| R3,R5,R6,R7,R10,R11 | 22Ω | ESP32 GPIO25/26/32/33/22/21 到外部 E 后缀网络的串联电阻 | 图 6f5407ad4740 / 第 1 页 / 第 1 页 U1 右侧 GPIO25/26/32/33 及左下 GPIO21/22 的六个 22R 电阻 |

## 系统结构

### AtomU 系统架构

USB1 为板供电并连接 U2 CH552T，CH552T 以 UART 和自动下载信号控制 U1 ESP32-PICO-D4；U3 生成 3.3V，ESP32 连接麦克风、红外、RGB、按键、Grove 和扩展 GPIO。

- 参数与网络：`soc=U1 ESP32-PICO-D4`；`usb_uart=U2 CH552T`；`usb=USB1 Type-A`；`regulator=U3 SY8089A`；`microphone=MIC1 SPM1423HM4H-B`；`rgb=LED1 SK6812`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页完整单页各功能分区

## 电源

### USB-A 电源输入

USB1 pin1 提供 VCC_VUSB，pin4 接 GND；VCC_VUSB 同时为 U2 CH552T VCC 和 U3 SY8089A VIN/EN 供电。

- 参数与网络：`connector=USB1`；`vbus=pin1 VCC_VUSB`；`ground=pin4 GND`；`consumers=U2 VCC; U3 VIN/EN`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 USB1 VCC_VUSB、U2 VCC 与 U3 VIN/EN 同名网络

### VCC_VUSB 到 VCC_3V3

U3 SY8089A 的 VIN/EN 接 VCC_VUSB，SW 经 L2 WPN3012H2R2MT 输出 VCC_3V3，反馈为 R14 100KΩ 与 R15 22.1KΩ。

- 参数与网络：`input=VCC_VUSB`；`converter=U3 SY8089A`；`inductor=L2 WPN3012H2R2MT`；`feedback=R14 100KΩ; R15 22.1KΩ`；`output=VCC_3V3`；`output_capacitors=C10 22uF; C11 4.7uF`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 3V3_Power U3/L2/R14/R15/C10/C11

## 接口

### USB1 Type-A 接口

USB1 pin1=VCC_VUSB、pin2=USB_DM、pin3=USB_DP、pin4=GND；USB_DP/DM 连接 U2 CH552T P3.6/P3.7。

- 参数与网络：`pin1=VCC_VUSB`；`pin2=USB_DM -> U2 P3.7/UDM pin15`；`pin3=USB_DP -> U2 P3.6/UDP pin14`；`pin4=GND`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 USB1 与 U2 pins14/15 USB_DP/USB_DM

### HY2.0-4P Grove 接口

Grove IO2=ESP_GP32_E/GPIO32、IO1=ESP_GP26_E/GPIO26、5V=VCC_VUSB_E、GND=GND；GPIO32/26 各经 22Ω 电阻连接 U1。

- 参数与网络：`io2=GPIO32 via R6 22Ω`；`io1=GPIO26 via R5 22Ω`；`vcc=VCC_VUSB_E`；`ground=GND`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 U1 GPIO32/26、R6/R5 与 GROVE 连接器

### JP1 六针扩展接口

JP1 pin6=GPIO21、pin5=GPIO22、pin4=GPIO33、pin3=GPIO25、pin2=VCC_VUSB_E、pin1=GND；四个 GPIO 均经 22Ω 串联电阻。

- 参数与网络：`pin6=GPIO21 via R11 22Ω`；`pin5=GPIO22 via R10 22Ω`；`pin4=GPIO33 via R7 22Ω`；`pin3=GPIO25 via R3 22Ω`；`pin2=VCC_VUSB_E`；`pin1=GND`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 EXT_IO JP1 1-6 脚及 U1 对应 22R 电阻

## 总线

### CH552T 到 ESP32 UART

U2 CH552_RXD 经 R2 470Ω 连接 U1 ESP_TXD/U0TXD pin41，CH552_TXD 经 R4 470Ω 连接 U1 ESP_RXD/U0RXD pin40。

- 参数与网络：`usb_uart=U2 CH552T`；`host_tx=U1 U0TXD pin41 -> R2 470Ω -> CH552_RXD`；`host_rx=U1 U0RXD pin40 <- R4 470Ω <- CH552_TXD`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 U2 P3.0/P3.1 与 U1 IO1/U0TXD、IO3/U0RXD 之间网络

## GPIO 与控制信号

### 红外发射 GPIO

U1 GPIO12/IO12 通过 IR_LED 网络与 R9 22Ω 驱动 LED2，LED2 另一端接 GND。

- 参数与网络：`gpio=GPIO12`；`net=IR_LED`；`resistor=R9 22Ω`；`emitter=LED2`；`direction=output`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 U1 IO12 与 IR_LED 区 R9/LED2

### SK6812 RGB GPIO

U1 GPIO27 连接 LED1 SK6812 DIN，LED1 由 VCC_3V3/GND 供电，DOUT 标记未连接。

- 参数与网络：`gpio=GPIO27`；`destination=LED1 DIN`；`supply=VCC_3V3`；`ground=GND`；`dout_connected=false`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 U1 IO27/ESP_GP27 与 RGB_LED 区 LED1

### 用户按键 GPIO

U1 GPIO39 连接 ESP_GP39_SW，R8 将该网络上拉至 VCC_3V3，S1 按下接 GND，DZ1 从信号接 GND。

- 参数与网络：`gpio=GPIO39`；`pullup=R8 to VCC_3V3`；`switch=S1 PTS_820 to GND`；`protection=DZ1 3v3/TVS`；`direction=input`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 U1 GPIO39 与 USER_SW 区 R8/S1/DZ1

## 时钟

### 外部时钟器件

当前完整单页原理图未画出 ESP32-PICO-D4 或 CH552T 的外部晶振/振荡器。

- 参数与网络：`esp32_external_crystal_shown=false`；`ch552_external_crystal_shown=false`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 U1/U2 周围完整时钟相关引脚与器件，未见 Y/X 晶振位号

## 复位

### ESP32 自动下载与复位

U2 输出 GPIO0_IN 和 ESP32_EN_IN，通过 R1/D1/R12/R13 网络控制 ESP_GPIO0 与 ESP_EN；S2 将 ESP_EN 手动拉到 GND，C16 470nF 从 ESP_EN 接 GND。

- 参数与网络：`boot_control=GPIO0_IN -> R1 4.7KΩ -> ESP_GPIO0`；`enable_control=ESP32_EN_IN -> R13 1KΩ -> ESP_EN`；`steering=D1 BAT54C; R12 12KΩ`；`reset_button=S2 TS_045 to GND`；`enable_capacitor=C16 470nF`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 GPIO0_IN/ESP32_EN_IN 与中央 RST_Button 区

## 保护电路

### USB ESD 保护

D3 SRV05-4 的 IO1/IO2 分别连接 USB_DM/USB_DP，VCC 接 VCC_VUSB、GND 接 GND。

- 参数与网络：`device=D3 SRV05-4`；`io1=USB_DM`；`io2=USB_DP`；`vcc=VCC_VUSB`；`return=GND`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 USB_TypeA 区 D3 SRV05-4

### 外部 GPIO ESD 保护

D2 SRV05-4 保护 ESP_EN、GPIO21、GPIO32、GPIO26 外部网络；D4 SRV05-4 保护 GPIO25、GPIO33、GPIO22，阵列均接 VCC_3V3/GND。

- 参数与网络：`d2_nets=ESP_EN, ESP_GP21_E, ESP_GP32_E, ESP_GP26_E`；`d4_nets=ESP_GP25_E, ESP_GP33_E, ESP_GP22_E`；`devices=D2/D4 SRV05-4`；`rails=VCC_3V3/GND`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页右下 D2/D4 SRV05-4 与外部 E 后缀网络

### 扩展 5V 保护

VCC_VUSB 经 F1 6V/1A PPTC 成为 VCC_VUSB_E，C14 4.7uF 从 VCC_VUSB_E 接 GND，并为 Grove/JP1 供电。

- 参数与网络：`input=VCC_VUSB`；`protection=F1 6V/1A PPTC`；`output=VCC_VUSB_E`；`capacitor=C14 4.7uF`；`consumers=Grove and JP1`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 EXT_IO 底部 F1/C14/VCC_VUSB_E 与 Grove/JP1 电源

## 内存与 Flash

### ESP32-PICO-D4 存储可见性

原理图使用 ESP32-PICO-D4 封装且未画出外部 Flash、PSRAM 或存储卡连接。

- 参数与网络：`module=ESP32-PICO-D4`；`external_flash_shown=false`；`psram_shown=false`；`memory_card_shown=false`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页完整单页 ESP32_PICO 区及全部器件，无外部存储

## 音频

### SPM1423 PDM 音频连接

MIC1 CLK pin4 接 U1 GPIO5/MIC_CLK，DATA pin5 接 GPIO19/MIC_DATA；VCC pin1 经 FB1 接 VCC_3V3，GND pin6 接 GND。

- 参数与网络：`clock=U1 GPIO5 -> MIC_CLK -> MIC1 pin4`；`data=MIC1 pin5 -> MIC_DATA -> U1 GPIO19`；`supply=VCC_3V3 via FB1`；`ground=MIC1 pin6 GND`；`interface=PDM`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 U1 IO5/IO19 与 Microphone 区 MIC1 CLK/DATA/VCC/GND

## 射频

### 2.4GHz 天线连接

U1 LNA_IN pin2 通过匹配网络连接 ANT1 Proant 440，网络包含 L1 2.7nH、C1 3.0pF 和 C2 1.5pF。

- 参数与网络：`soc_pin=U1 pin2 LNA_IN`；`antenna=ANT1 Proant 440`；`inductor=L1 2.7nH`；`capacitors=C1 3.0pF; C2 1.5pF`
- 证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 U1 LNA_IN 到 ANT 区 ANT1/L1/C1/C2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | AtomU 系统架构 | `soc=U1 ESP32-PICO-D4`；`usb_uart=U2 CH552T`；`usb=USB1 Type-A`；`regulator=U3 SY8089A`；`microphone=MIC1 SPM1423HM4H-B`；`rgb=LED1 SK6812` |
| 电源 | USB-A 电源输入 | `connector=USB1`；`vbus=pin1 VCC_VUSB`；`ground=pin4 GND`；`consumers=U2 VCC; U3 VIN/EN` |
| 电源 | VCC_VUSB 到 VCC_3V3 | `input=VCC_VUSB`；`converter=U3 SY8089A`；`inductor=L2 WPN3012H2R2MT`；`feedback=R14 100KΩ; R15 22.1KΩ`；`output=VCC_3V3`；`output_capacitors=C10 22uF; C11 4.7uF` |
| 接口 | USB1 Type-A 接口 | `pin1=VCC_VUSB`；`pin2=USB_DM -> U2 P3.7/UDM pin15`；`pin3=USB_DP -> U2 P3.6/UDP pin14`；`pin4=GND` |
| 保护电路 | USB ESD 保护 | `device=D3 SRV05-4`；`io1=USB_DM`；`io2=USB_DP`；`vcc=VCC_VUSB`；`return=GND` |
| 总线 | CH552T 到 ESP32 UART | `usb_uart=U2 CH552T`；`host_tx=U1 U0TXD pin41 -> R2 470Ω -> CH552_RXD`；`host_rx=U1 U0RXD pin40 <- R4 470Ω <- CH552_TXD` |
| 复位 | ESP32 自动下载与复位 | `boot_control=GPIO0_IN -> R1 4.7KΩ -> ESP_GPIO0`；`enable_control=ESP32_EN_IN -> R13 1KΩ -> ESP_EN`；`steering=D1 BAT54C; R12 12KΩ`；`reset_button=S2 TS_045 to GND`；`enable_capacitor=C16 470nF` |
| 音频 | SPM1423 PDM 音频连接 | `clock=U1 GPIO5 -> MIC_CLK -> MIC1 pin4`；`data=MIC1 pin5 -> MIC_DATA -> U1 GPIO19`；`supply=VCC_3V3 via FB1`；`ground=MIC1 pin6 GND`；`interface=PDM` |
| 音频 | 麦克风性能参数 | `documented_sensitivity=-22dBFS at 94dB SPL/1KHz`；`documented_snr=61.4dB A-weighted`；`documented_audio_band=100Hz-10KHz`；`documented_pdm_clock=1.0-3.25MHz`；`schematic_specs_shown=false` |
| GPIO 与控制信号 | 红外发射 GPIO | `gpio=GPIO12`；`net=IR_LED`；`resistor=R9 22Ω`；`emitter=LED2`；`direction=output` |
| GPIO 与控制信号 | SK6812 RGB GPIO | `gpio=GPIO27`；`destination=LED1 DIN`；`supply=VCC_3V3`；`ground=GND`；`dout_connected=false` |
| GPIO 与控制信号 | 用户按键 GPIO | `gpio=GPIO39`；`pullup=R8 to VCC_3V3`；`switch=S1 PTS_820 to GND`；`protection=DZ1 3v3/TVS`；`direction=input` |
| 接口 | HY2.0-4P Grove 接口 | `io2=GPIO32 via R6 22Ω`；`io1=GPIO26 via R5 22Ω`；`vcc=VCC_VUSB_E`；`ground=GND` |
| 接口 | JP1 六针扩展接口 | `pin6=GPIO21 via R11 22Ω`；`pin5=GPIO22 via R10 22Ω`；`pin4=GPIO33 via R7 22Ω`；`pin3=GPIO25 via R3 22Ω`；`pin2=VCC_VUSB_E`；`pin1=GND` |
| 保护电路 | 外部 GPIO ESD 保护 | `d2_nets=ESP_EN, ESP_GP21_E, ESP_GP32_E, ESP_GP26_E`；`d4_nets=ESP_GP25_E, ESP_GP33_E, ESP_GP22_E`；`devices=D2/D4 SRV05-4`；`rails=VCC_3V3/GND` |
| 保护电路 | 扩展 5V 保护 | `input=VCC_VUSB`；`protection=F1 6V/1A PPTC`；`output=VCC_VUSB_E`；`capacitor=C14 4.7uF`；`consumers=Grove and JP1` |
| 射频 | 2.4GHz 天线连接 | `soc_pin=U1 pin2 LNA_IN`；`antenna=ANT1 Proant 440`；`inductor=L1 2.7nH`；`capacitors=C1 3.0pF; C2 1.5pF` |
| 内存与 Flash | ESP32-PICO-D4 存储可见性 | `module=ESP32-PICO-D4`；`external_flash_shown=false`；`psram_shown=false`；`memory_card_shown=false` |
| 时钟 | 外部时钟器件 | `esp32_external_crystal_shown=false`；`ch552_external_crystal_shown=false` |

## 待确认事项

- `audio.documented-microphone-performance`：产品正文给出 -22dBFS 灵敏度、61.4dB 信噪比、100Hz-10KHz 音频范围和 1.0-3.25MHz PDM 时钟范围，但原理图只显示 SPM1423HM4H-B 型号与连接。（证据：图 6f5407ad4740 / 第 1 页 / 第 1 页 MIC1 SPM1423HM4H-B，仅有引脚与外围，无性能数值）
- `review.microphone-performance`：AtomU 当前 SPM1423HM4H-B 批次是否满足正文列出的灵敏度、信噪比、音频带宽和 PDM 时钟范围？；原因：这些数值未标在原理图上，需由对应麦克风数据手册版本和整机测试确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6f5407ad47401787b16012ffa56fef40c645c22bdd08c803a0f9ac64e118ddbf` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/675/Sch_AtomU_01.jpg` |

---

源文档：`zh_CN/core/ATOM U.md`

源文档 SHA-256：`033ddf408cf8bb001d93b9104caf00ed4d453d33bd4e09662e935287ba65d566`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
