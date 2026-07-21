# Unit Fingerprint2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Fingerprint2 |
| SKU | U203 |
| 产品 ID | `unit-fingerprint2-df1b9c951b4d` |
| 源文档 | `zh_CN/unit/Unit_Fingerprint2.md` |

## 概述

Unit Fingerprint2 以 U1 STM32G031G8U6 为板上控制器，USART2 的 USER_TX/USER_RX 连接 J1 Grove，USART1 的 SENSOR_TX/SENSOR_RX 连接 J2 FingerPrinter 接口。5V 经 U3 TPAP7343D-33FS4 生成常开的 3V3_SEN，U1 的 Sensor_EN 控制 U4 同型号稳压器生成 3V3_MCU；J2 同时引出 GND、INT、3V3_MCU 和 3V3_SEN。RST 由 R1/C4 构成上拉延时网络，CN1 提供 SWDIO/SWCLK/RST 调试接口，LED1 为 3V3_SEN 蓝色电源指示。原理图未展开指纹模组内部传感器、存储、算法与 RGB 灯环。

## 检索关键词

`Unit Fingerprint2`、`U203`、`STM32G031G8U6`、`A-K323CP`、`TPAP7343D-33FS4`、`Fingerprint`、`USART1`、`USART2`、`USER_TX`、`USER_RX`、`SENSOR_TX`、`SENSOR_RX`、`Sensor_EN`、`INT`、`RST`、`SWDIO`、`SWCLK`、`CN1`、`J1 4P-UART`、`J2 FingerPrinter`、`5V`、`3V3_SEN`、`3V3_MCU`、`UART 115200`、`8N1`、`100 fingerprints`、`508 dpi`、`80x208`、`7262 Bytes`、`RGB ring`、`BLUE LED`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | STM32G031G8U6 | 板上控制 MCU，桥接外部 UART 与指纹模组 UART，并控制模组电源、处理中断、复位和 SWD 调试 | 图 28edccee3ce8 / 第 1 页 / 第 1 页网格 A2-B3，U1 STM32G031G8U6 pins1-28，USART1/USART2/INT/Sensor_EN/RST/SWD |
| U3,U4 | TPAP7343D-33FS4 | 分别由 5V 生成 3V3_SEN 与 3V3_MCU；U3 常开，U4 受 Sensor_EN 控制 | 图 28edccee3ce8 / 第 1 页 / 第 1 页网格 A1-B1，U3/U4 TPAP7343D-33FS4、5V、3V3_SEN、3V3_MCU、Sensor_EN |
| J1 | 4P-UART | Grove UART 与 5V/GND 外部接口 | 图 28edccee3ce8 / 第 1 页 / 第 1 页网格 C1，J1 4P-UART pin1 USER_TX、pin2 USER_RX、pin3 5V、pin4 GND |
| J2 | FingerPrinter 6P | 指纹识别模组接口，提供 SENSOR_RX/TX、INT、3V3_MCU、3V3_SEN 与 GND | 图 28edccee3ce8 / 第 1 页 / 第 1 页网格 C2，J2 FingerPrinter pins1-6 |
| CN1 | 1.25-5A | 五针 SWD 调试与复位接口，提供 3V3_SEN、SWCLK、SWDIO、RST、GND | 图 28edccee3ce8 / 第 1 页 / 第 1 页网格 C2-D2，CN1 1.25-5A pins1-5 |
| D1 | 未标注 | INT 网络到 GND 的保护二极管 | 图 28edccee3ce8 / 第 1 页 / 第 1 页网格 B2，INT 与 D1 到 GND |
| LED1 | BLUE | 3V3_SEN 电源指示 LED，经 R4 1K/1% 接地 | 图 28edccee3ce8 / 第 1 页 / 第 1 页网格 C3，3V3_SEN-R4 1K/1%-LED1 BLUE-GND |
| R1,C4 | 10K / 4.7uF/16V | STM32 RST 上拉与对地电容网络 | 图 28edccee3ce8 / 第 1 页 / 第 1 页网格 A1-A2，3V3_SEN/R1/RST/C4/GND |

## 系统结构

### Unit Fingerprint2 系统架构

U1 STM32G031G8U6 通过 USART2 连接 J1 外部主机，通过 USART1、INT 和 Sensor_EN 连接 J2 指纹模组；U3/U4 从 5V 生成 3V3_SEN/3V3_MCU，CN1 提供 SWD 调试，LED1 指示 3V3_SEN。

- 参数与网络：`controller=U1 STM32G031G8U6`；`host_interface=J1 USART2 USER_TX/USER_RX`；`sensor_interface=J2 USART1 SENSOR_TX/SENSOR_RX/INT`；`power=5V -> U3/U4 -> 3V3_SEN/3V3_MCU`；`enable=Sensor_EN`；`debug=CN1 SWD`；`indicator=LED1 BLUE`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页完整 A1-D4 原理图

### 本页未包含的子系统

该页未显示外部 Flash/EEPROM、I2C/SPI/CAN/RS-485/USB/SDIO/I2S、射频、音频、电池、充电器或独立用户开关；指纹模组内部电路未展开。

- 参数与网络：`external_storage=null`；`other_buses=null`；`rf=null`；`audio=null`；`battery_charger=null`；`user_switch=null`；`fingerprint_module_internal=null`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页完整原理图，仅含 STM32、电源、UART、J2、SWD、LED 与保护网络

## 核心器件

### 蓝色电源指示 LED

3V3_SEN 经 R4 1K/1% 与 LED1 BLUE 串联到 GND，构成常接电源指示支路。

- 参数与网络：`path=3V3_SEN -> R4 1K/1% -> LED1 BLUE -> GND`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页网格 C3 LED1/R4

## 电源

### 3V3_SEN 常开电源

U3 TPAP7343D-33FS4 VIN pin4 与 EN pin3 同接 5V，VOUT pin1 输出 3V3_SEN，GND pin2/EP 接 GND；C2/C3 各 4.7uF/16V 位于输入/输出侧。3V3_SEN 供 U1 VDD/VDDA、J2 pin6、CN1 pin1 与 LED1。

- 参数与网络：`regulator=U3 TPAP7343D-33FS4`；`input=5V`；`enable=EN=5V`；`output=3V3_SEN`；`caps=C2/C3 4.7uF/16V`；`loads=U1 VDD/VDDA,J2 pin6,CN1 pin1,LED1`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页网格 A1-C3，U3/3V3_SEN 全路径

### 3V3_MCU 可控电源

U4 TPAP7343D-33FS4 VIN pin4 接 5V、EN pin3 接 Sensor_EN、VOUT pin1 输出 3V3_MCU，GND pin2/EP 接 GND；C5/C6 各 4.7uF/16V 位于输入/输出侧，3V3_MCU 引至 J2 pin4。

- 参数与网络：`regulator=U4 TPAP7343D-33FS4`；`input=5V`；`enable=Sensor_EN`；`output=3V3_MCU`；`caps=C5/C6 4.7uF/16V`；`destination=J2 pin4`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页网格 B1-C2，U4/Sensor_EN/3V3_MCU/J2 pin4

## 接口

### J1 Grove UART 针脚映射

J1 pin1=USER_TX、pin2=USER_RX、pin3=5V、pin4=GND；USER_TX 由 U1 PA2 pin8 输出，USER_RX 进入 U1 PA3 pin9。

- 参数与网络：`connector=J1 4P-UART`；`pin1=USER_TX, unit output`；`pin2=USER_RX, unit input`；`pin3=5V power input`；`pin4=GND`；`mcu_tx=U1 PA2 pin8`；`mcu_rx=U1 PA3 pin9`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页 J1 与 U1 PA2/PA3 USER_TX/USER_RX 同名网络

### J2 指纹模组针脚映射

J2 pin1=GND、pin2=SENSOR_RX、pin3=SENSOR_TX、pin4=3V3_MCU、pin5=INT、pin6=3V3_SEN；R2/R3 各 10K 分别将 SENSOR_RX/SENSOR_TX 下拉到 GND。

- 参数与网络：`connector=J2 FingerPrinter`；`pin1=GND`；`pin2=SENSOR_RX`；`pin3=SENSOR_TX`；`pin4=3V3_MCU`；`pin5=INT`；`pin6=3V3_SEN`；`pulldowns=R2/R3 10K to GND`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页网格 C2，J2 pins1-6 与 R2/R3

## 总线

### 外部主机 USART2

U1 PA2 pin8 标为 USER_TX、PA3 pin9 标为 USER_RX，构成 USART2 双线 UART 并通过 J1 引出；原理图未打印波特率或帧格式。

- 参数与网络：`controller=U1 STM32G031G8U6 USART2`；`tx=PA2 pin8 USER_TX -> J1 pin1`；`rx=J1 pin2 USER_RX -> PA3 pin9`；`baud_printed=null`；`frame_printed=null`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页网格 B2-C1，U1 USART2 与 J1

### STM32 到指纹模组 USART1

U1 PB6 pin26 连接 SENSOR_RX，PB7 pin27 连接 SENSOR_TX，构成 USART1 与 J2 pins2/3 的双线 UART；本页只确认网络连接，不定义信号名采用 STM32 侧还是指纹模组侧视角。

- 参数与网络：`controller=U1 USART1`；`pb6=pin26 SENSOR_RX -> J2 pin2`；`pb7=pin27 SENSOR_TX -> J2 pin3`；`network_naming=sensor-side RX/TX`；`baud_printed=null`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页 U1 PB6/PB7 USART1 与 J2 SENSOR_RX/SENSOR_TX

## GPIO 与控制信号

### Sensor_EN 电源控制

U1 PC15-OSC32_OUT pin2 连接 Sensor_EN，Sensor_EN 驱动 U4 EN pin3，从而控制 J2 pin4 的 3V3_MCU 电源。

- 参数与网络：`controller_pin=U1 PC15-OSC32_OUT pin2`；`net=Sensor_EN`；`target=U4 EN pin3`；`controlled_rail=3V3_MCU -> J2 pin4`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页 U1 pin2 Sensor_EN 与 U4 EN

### 指纹模组 INT

J2 pin5 的 INT 连接 U1 PA8 pin18，D1 从 INT 接 GND 提供保护；原理图未标中断有效电平、输出类型或时序。

- 参数与网络：`source_connector=J2 pin5 INT`；`controller_pin=U1 PA8 pin18`；`protection=D1 to GND`；`active_level_printed=null`；`output_type_printed=null`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页网格 B2-C2，J2 INT、D1 与 U1 PA8

## 时钟

### 外部时钟连接

U1 PC14-OSC32_IN pin1 未连接外部晶振；PC15-OSC32_OUT pin2 被复用为 Sensor_EN，本页未显示任何晶振、谐振器或时钟输入器件。

- 参数与网络：`pc14=pin1 unconnected`；`pc15=pin2 Sensor_EN`；`external_crystal=null`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页 U1 PC14/PC15 OSC32 pins1/2

## 复位

### STM32 RST 网络

U1 PF2 RST pin5 连接 RST，R1 10K 将 RST 上拉到 3V3_SEN，C4 4.7uF/16V 从 RST 接 GND，RST 同时引至 CN1 pin4。

- 参数与网络：`controller_pin=U1 PF2 RST pin5`；`pullup=R1 10K to 3V3_SEN`；`capacitor=C4 4.7uF/16V to GND`；`debug_connector=CN1 pin4`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页网格 A1-B3，R1/C4/RST/U1 pin5/CN1

## 调试与烧录

### CN1 SWD 调试接口

CN1 pin1=3V3_SEN、pin2=SWCLK、pin3=SWDIO、pin4=RST、pin5=GND；SWDIO 连接 U1 PA13 pin20，SWCLK 连接 U1 PA14-BOOT0 pin21。

- 参数与网络：`connector=CN1 1.25-5A`；`pin1=3V3_SEN`；`pin2=SWCLK -> U1 PA14-BOOT0 pin21`；`pin3=SWDIO -> U1 PA13 pin20`；`pin4=RST`；`pin5=GND`
- 证据：图 28edccee3ce8 / 第 1 页 / 第 1 页网格 B2-D2，U1 SWDIO/SWCLK 与 CN1 pins1-5

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Fingerprint2 系统架构 | `controller=U1 STM32G031G8U6`；`host_interface=J1 USART2 USER_TX/USER_RX`；`sensor_interface=J2 USART1 SENSOR_TX/SENSOR_RX/INT`；`power=5V -> U3/U4 -> 3V3_SEN/3V3_MCU`；`enable=Sensor_EN`；`debug=CN1 SWD`；`indicator=LED1 BLUE` |
| 接口 | J1 Grove UART 针脚映射 | `connector=J1 4P-UART`；`pin1=USER_TX, unit output`；`pin2=USER_RX, unit input`；`pin3=5V power input`；`pin4=GND`；`mcu_tx=U1 PA2 pin8`；`mcu_rx=U1 PA3 pin9` |
| 总线 | 外部主机 USART2 | `controller=U1 STM32G031G8U6 USART2`；`tx=PA2 pin8 USER_TX -> J1 pin1`；`rx=J1 pin2 USER_RX -> PA3 pin9`；`baud_printed=null`；`frame_printed=null` |
| 接口 | J2 指纹模组针脚映射 | `connector=J2 FingerPrinter`；`pin1=GND`；`pin2=SENSOR_RX`；`pin3=SENSOR_TX`；`pin4=3V3_MCU`；`pin5=INT`；`pin6=3V3_SEN`；`pulldowns=R2/R3 10K to GND` |
| 总线 | STM32 到指纹模组 USART1 | `controller=U1 USART1`；`pb6=pin26 SENSOR_RX -> J2 pin2`；`pb7=pin27 SENSOR_TX -> J2 pin3`；`network_naming=sensor-side RX/TX`；`baud_printed=null` |
| 电源 | 3V3_SEN 常开电源 | `regulator=U3 TPAP7343D-33FS4`；`input=5V`；`enable=EN=5V`；`output=3V3_SEN`；`caps=C2/C3 4.7uF/16V`；`loads=U1 VDD/VDDA,J2 pin6,CN1 pin1,LED1` |
| 电源 | 3V3_MCU 可控电源 | `regulator=U4 TPAP7343D-33FS4`；`input=5V`；`enable=Sensor_EN`；`output=3V3_MCU`；`caps=C5/C6 4.7uF/16V`；`destination=J2 pin4` |
| GPIO 与控制信号 | Sensor_EN 电源控制 | `controller_pin=U1 PC15-OSC32_OUT pin2`；`net=Sensor_EN`；`target=U4 EN pin3`；`controlled_rail=3V3_MCU -> J2 pin4` |
| GPIO 与控制信号 | 指纹模组 INT | `source_connector=J2 pin5 INT`；`controller_pin=U1 PA8 pin18`；`protection=D1 to GND`；`active_level_printed=null`；`output_type_printed=null` |
| 复位 | STM32 RST 网络 | `controller_pin=U1 PF2 RST pin5`；`pullup=R1 10K to 3V3_SEN`；`capacitor=C4 4.7uF/16V to GND`；`debug_connector=CN1 pin4` |
| 调试与烧录 | CN1 SWD 调试接口 | `connector=CN1 1.25-5A`；`pin1=3V3_SEN`；`pin2=SWCLK -> U1 PA14-BOOT0 pin21`；`pin3=SWDIO -> U1 PA13 pin20`；`pin4=RST`；`pin5=GND` |
| 时钟 | 外部时钟连接 | `pc14=pin1 unconnected`；`pc15=pin2 Sensor_EN`；`external_crystal=null` |
| 核心器件 | 蓝色电源指示 LED | `path=3V3_SEN -> R4 1K/1% -> LED1 BLUE -> GND` |
| 系统结构 | 本页未包含的子系统 | `external_storage=null`；`other_buses=null`；`rf=null`；`audio=null`；`battery_charger=null`；`user_switch=null`；`fingerprint_module_internal=null` |
| 核心器件 | 正文 A-K323CP 模组身份 | `documented_module=A-K323CP`；`documented_sensor_type=capacitive semiconductor`；`schematic_connector=J2 FingerPrinter`；`schematic_module_reference=null`；`internal_sensor_part=null` |
| 总线 | 正文 UART 设置 | `documented_baud=115200bps`；`documented_frame=8N1`；`bus=USART2 USER_TX/USER_RX`；`logic_thresholds=null`；`protocol_frames=null` |
| 传感器 | 正文指纹容量与算法功能 | `documented_capacity=100`；`documented_functions=capture,feature extraction,enroll,match,store,search,dry/wet adaptation`；`algorithm_version=null`；`storage_device=null`；`far=null`；`frr=null`；`search_time=null`；`security=null` |
| 传感器 | 正文分辨率、像素与图像大小 | `documented_resolution=508dpi`；`documented_pixels=80x208`；`documented_bits_per_pixel=4`；`documented_size_text=8230 Bytes`；`calculated_size_text=8320 Bytes`；`conflict=true` |
| 存储 | 正文单枚指纹数据大小 | `documented_template_size=7262 Bytes`；`storage_location=null`；`format=null`；`checksum=null`；`encryption=null` |
| GPIO 与控制信号 | 正文七彩 RGB 灯环 | `documented_indicator=seven-color RGB ring`；`documented_colors=7`；`schematic_led=LED1 BLUE only`；`rgb_reference=null`；`control_net=null`；`color_mapping=null` |
| 电源 | 正文工作与休眠功耗 | `documented_active_led_on=40mA`；`documented_active_led_off=37.25mA`；`documented_sleep=14.11mA`；`input_voltage=null`；`test_conditions=null`；`tolerance=null` |

## 待确认事项

- `component.documented-fingerprint-module`：正文称指纹模组为 A-K323CP 且采用半导体电容式传感器；原理图只将 J2 标为 FingerPrinter，没有 A-K323CP 位号、传感器型号或模组内部电路。（证据：图 28edccee3ce8 / 第 1 页 / 第 1 页 J2 仅标 FingerPrinter）
- `bus.documented-uart-settings`：正文称外部通信使用 115200bps@8N1；原理图确认 USER_TX/USER_RX UART 拓扑，但未打印波特率、数据位、校验、停止位、逻辑门限、指令帧或超时。（证据：图 28edccee3ce8 / 第 1 页 / 第 1 页 U1 USART2 与 J1，无 UART 参数）
- `sensor.documented-capacity-algorithms`：正文称可存储 100 枚指纹，支持采集、特征提取、注册、比对、存储、检索以及干湿手指自适应；原理图只显示 J2 电气接口，未显示存储器容量、算法版本、误识率、拒真率、搜索时间或安全机制。（证据：图 28edccee3ce8 / 第 1 页 / 第 1 页 J2 FingerPrinter，无算法或存储参数）
- `sensor.documented-image-spec`：正文称分辨率 508dpi、图像 80×208、每像素4bit，并同时写“8230 Bytes”与括号计算“80×208/2=8320”；两处字节数互相冲突，原理图没有图像规格可裁决。（证据：图 28edccee3ce8 / 第 1 页 / 第 1 页 J2 FingerPrinter 接口，无分辨率/像素/图像大小文字）
- `storage.documented-template-size`：正文称每枚指纹数据为 7262 Bytes；原理图未显示指纹模板存储器、数据格式、校验、加密、导入导出或容量分配。（证据：图 28edccee3ce8 / 第 1 页 / 第 1 页无指纹存储器或模板格式）
- `gpio.documented-rgb-ring`：正文称指纹模组自带七彩灯圈并支持七种状态灯光；原理图只显示 LED1 BLUE 电源指示，没有 RGB 灯环位号、控制网络、LED 数量、颜色映射或时序。（证据：图 28edccee3ce8 / 第 1 页 / 第 1 页仅有 LED1 BLUE，无 RGB 环）
- `power.documented-consumption`：正文称工作呼吸灯开 40mA、关 37.25mA，休眠 14.11mA；原理图确认双 3.3V 电源与 Sensor_EN，但未给输入电压、指纹模组状态、LED 模式、测试温度、采样方法或容差。（证据：图 28edccee3ce8 / 第 1 页 / 第 1 页 5V/U3/U4/J2 电源路径，无功耗数据）
- `review.fingerprint-module`：请用 BOM、模组丝印或规格确认 J2 连接的量产模组是否为 A-K323CP及内部电容传感器型号。；原因：原理图只显示通用 FingerPrinter 接口。
- `review.uart-settings`：请用当前固件和通信协议确认 115200bps@8N1、UART 电平、命令帧、响应、超时和错误码。；原因：原理图只确认 UART 连线。
- `review.capacity-algorithms`：请确认 100枚容量、算法版本、注册/检索流程、干湿手指适应、FAR/FRR、搜索时间和安全机制。；原因：这些属于模组内部存储与算法，板级原理图未展开。
- `review.image-spec`：请确认 508dpi、80×208、4bit 像素，并裁决图像大小应为 8230 还是 8320 Bytes。；原因：正文数值内部冲突，原理图无图像规格。
- `review.template-size`：请确认每枚 7262 Bytes 的数据类型、存储位置、格式、校验、加密和导入导出规则。；原因：原理图没有模板存储器或格式。
- `review.rgb-ring`：请用指纹模组规格或实物确认 RGB 灯环的 LED 数量、控制方式、七种颜色及状态映射。；原因：板级原理图仅显示蓝色电源 LED。
- `review.power-consumption`：请确认工作/休眠电流的输入电压、模组状态、呼吸灯配置、采样周期、温度和容差。；原因：原理图不能证明整机动态功耗。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `28edccee3ce8d0fcdf434b63e5d0a029ff0390885bd19a504ac45e9dc6e6a0ae` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/SCH_Unit_Fingerprint2_SCH_MAIN_V1.0_20250822_2025_09_22_14_45_23_page_01.png` |

---

源文档：`zh_CN/unit/Unit_Fingerprint2.md`

源文档 SHA-256：`4235d62d7483ea4d5b999a76b0877d80a09e15af23093959183417ea8917ee1b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
