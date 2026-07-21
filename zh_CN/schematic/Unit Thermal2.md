# Unit Thermal2 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Thermal2 |
| SKU | U149 |
| 产品 ID | `unit-thermal2-332816353c42` |
| 源文档 | `zh_CN/unit/Thermal2.md` |

## 概述

Unit Thermal2 以 ESP32-PICO-D4（U2）为处理核心：外部 J2 Grove I2C 使用 GPIO32/GPIO33，内部 MLX90640（U3）使用 GPIO22/GPIO21 的独立 I2C 总线。SY8089（U1）将 +5V 降压为 +3.3V，为 MCU、传感器、SK6812 RGB 和蜂鸣器驱动供电。板上还提供 GPIO39 功能按键、EN 复位按键、六针下载口、四针 GPIO32/GPIO33 扩展口，以及 GPIO25 驱动的低边蜂鸣器电路。

## 检索关键词

`Unit Thermal2`、`U149`、`ESP32-PICO-D4`、`MLX90640`、`SY8089`、`SK6812`、`GPIO32`、`GPIO33`、`GPIO22`、`GPIO21`、`GPIO39`、`GPIO27`、`GPIO25`、`IIC_SCL`、`IIC_SDA`、`0x33`、`HY-2.0_IIC`、`DownloadSocket`、`UTX`、`URX`、`EN`、`GPIO0`、`+5V`、`+3.3V`、`L1 C3015 4.7uH`、`SS8050 Y1`、`Buzzer`、`1N4007WS`、`RLSD52A031V`、`LESD3Z5.0CMT1G`、`32x24`、`110x75`、`-40~300C`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ESP32-PICO-D4 | 主控与数据处理 MCU，连接外部/内部 I2C、按键、RGB、蜂鸣器、下载口和扩展口 | 图 3fe925cd9795 / 第 1 页 / B2-C3：U2 ESP32-PICO-D4 的电源、GPIO、UART、EN、SDIO 与 GND 引脚 |
| U3 | MLX90640 | 通过 GPIO22/GPIO21 I2C 总线连接 MCU 的热阵列传感器 | 图 3fe925cd9795 / 第 1 页 / C1-C2：U3 MLX90640，VDD/GND/SCL/SDA 四脚及 GPIO22/GPIO21 网络 |
| U1 | SY8089 | 将 +5V 降压为 +3.3V 的开关稳压器 | 图 3fe925cd9795 / 第 1 页 / A1-B2：U1 SY8089 与 L1、R1/R2、C2~C5 组成的 +5V 到 +3.3V 电路 |
| J2 | HY-2.0_IIC | 外部 I2C、+5V、GND Grove 接口 | 图 3fe925cd9795 / 第 1 页 / B3-B4：J2 HY-2.0_IIC 的 IIC_SCL/IIC_SDA/VCC/GND 与保护/上拉网络 |
| J1 | DownloadSocket | ESP32 下载调试接口，引出 +3.3V、UTX、URX、EN、GPIO0、GND | 图 3fe925cd9795 / 第 1 页 / A3-A4：J1 DownloadSocket 六脚及 +3.3V/UTX/URX/EN/GPIO0/GND |
| P1 | Header 4 | GPIO32、GPIO33、+5V、GND 扩展接口 | 图 3fe925cd9795 / 第 1 页 / A3：P1 Header4 的 GPIO32/GPIO33/+5V/GND 四脚 |
| LED1 | SK6812 | GPIO27 控制的可编程 RGB LED | 图 3fe925cd9795 / 第 1 页 / D1-D2：LED1 SK6812，DIN 接 GPIO27、VDD 接 +3.3V、VSS 接 GND、DOUT 未连接 |
| LS1 | Buzzer | 由 Q1 低边驱动的蜂鸣器 | 图 3fe925cd9795 / 第 1 页 / C4-D4：LS1 Buzzer、Q1、D7、R9/R11/R13 与 GPIO25 |
| Q1 | SS8050 Y1 | GPIO25 控制的蜂鸣器低边驱动晶体管 | 图 3fe925cd9795 / 第 1 页 / D3-D4：Q1 SS8050 Y1，基极经 R11 接 GPIO25，集电极接 LS1，发射极接 GND |
| S1 | SW-PB | 将 EN 拉低的复位按键 | 图 3fe925cd9795 / 第 1 页 / B1-B2：S1 SW-PB 从 EN 节点连接 GND，旁有 R3/C6/D2 |
| S2 | SMT_SW_PTS_820 | 将 GPIO39 拉低的功能按键 | 图 3fe925cd9795 / 第 1 页 / B1：S2 SMT_SW_PTS_820 从 GPIO39 接 GND，旁有 R4/D1 |
| D3 | LESD3Z5.0CMT1G | J2 +5V 到 GND 的浪涌/ESD 保护器件 | 图 3fe925cd9795 / 第 1 页 / B4：D3 LESD3Z5.0CMT1G 跨接 J2 +5V 与 GND |
| D1, D2, D4, D5, D6 | RLSD52A031V | 功能键、复位、外部 I2C 与传感器电源网络的对地保护器件 | 图 3fe925cd9795 / 第 1 页 / B1 的 D1/D2、B3-B4 的 D4/D5、C1 的 D6，均标 RLSD52A031V 并接 GND |
| D7 | 1N4007WS | 跨接蜂鸣器支路的续流/钳位二极管 | 图 3fe925cd9795 / 第 1 页 / C4-D4：D7 1N4007WS 跨接 LS1 上下端驱动节点 |

## 系统结构

### Unit Thermal2

U2 ESP32-PICO-D4 通过 GPIO22/GPIO21 读取 U3 MLX90640，并通过 GPIO32/GPIO33 的独立 I2C 接口连接 J2；同时控制 RGB、蜂鸣器和按键。

- 参数与网络：`controller=U2 ESP32-PICO-D4`；`sensor=U3 MLX90640`；`sensor_bus=GPIO22 SCL / GPIO21 SDA`；`external_bus=GPIO32 SCL / GPIO33 SDA`；`rgb=LED1 GPIO27`；`buzzer=LS1/Q1 GPIO25`；`button=S2 GPIO39`
- 证据：图 3fe925cd9795 / 第 1 页 / 全页：U2 与 U3/J2/LED1/LS1/S1/S2 的同名 GPIO 网络

## 电源

### U1 SY8089

U1.VIN.4 与 EN.1 接 +5V，GND.2 接地，SW.3 经 L1（C3015 4.7uH）输出 +3.3V；R1 68KΩ 与 R2 15KΩ连接 FB.5。

- 参数与网络：`input=+5V to VIN.4 and EN.1`；`output=+3.3V`；`inductor=L1 C3015 4.7uH`；`feedback=R1 68KΩ, R2 15KΩ`；`input_caps=C4 22uF, C5 100nF`；`output_caps=C2 100nF, C3 22uF`
- 证据：图 3fe925cd9795 / 第 1 页 / A1-B2：+5V-U1-L1-+3.3V、R1/R2、C2~C5 完整降压电路

### +3.3V 与 VDD_SDIO

+3.3V 供给 U2、U3、LED1、J1 和各上拉；C9/C10 为 22uF，C11/C12/C14/C1/C7/C8 为 100nF，VDD_SDIO 由 C13（1uF）去耦。

- 参数与网络：`main_rail=+3.3V`；`bulk_caps=C9 22uF, C10 22uF`；`logic_decoupling=C11/C12/C14/C1/C7/C8 100nF`；`sdio_rail=VDD_SDIO with C13 1uF`
- 证据：图 3fe925cd9795 / 第 1 页 / A4、C1、D1-D3 的 +3.3V/VDD_SDIO 电容与 U2/U3/LED1/J1 电源网络

## 接口

### J2

J2.1 IIC_SCL 接 GPIO32，J2.2 IIC_SDA 接 GPIO33，J2.3 VCC 接 +5V，J2.4 GND 接地。

- 参数与网络：`connector=HY-2.0_IIC`；`pin_1=IIC_SCL / GPIO32`；`pin_2=IIC_SDA / GPIO33`；`pin_3=VCC / +5V`；`pin_4=GND`；`power_direction=+5V input to board`
- 证据：图 3fe925cd9795 / 第 1 页 / B3-B4：J2.1~J2.4 与 GPIO32/GPIO33/+5V/GND 网络

### P1

P1.1 接 GPIO32，P1.2 接 GPIO33，P1.3 接 +5V，P1.4 接 GND。

- 参数与网络：`connector=Header 4`；`pin_1=GPIO32`；`pin_2=GPIO33`；`pin_3=+5V`；`pin_4=GND`
- 证据：图 3fe925cd9795 / 第 1 页 / A3：P1 Header4 的 GPIO32/GPIO33/+5V/GND 标注

## 总线

### J2 与 U2

J2 的 SCL/SDA 分别连接 U2.IO32.12 与 U2.IO33.13；R5/R6（均 4.7KΩ）分别将两条网络上拉至 +3.3V。

- 参数与网络：`SCL=J2.1 -> GPIO32 / U2.12; R5 4.7KΩ to +3.3V`；`SDA=J2.2 -> GPIO33 / U2.13; R6 4.7KΩ to +3.3V`；`controller_role=U2 firmware-facing external I2C`
- 证据：图 3fe925cd9795 / 第 1 页 / B2-B4：U2 GPIO32/GPIO33、J2 IIC_SCL/IIC_SDA 与 R5/R6 +3.3V 上拉

### U2 与 U3 MLX90640

MLX90640 的 SCL/GPIO22 经 R8（4.7KΩ）上拉至 +3.3V，SDA/GPIO21 经 R10（4.7KΩ）上拉至 +3.3V；该总线与 GPIO32/GPIO33 外部 I2C 分离。

- 参数与网络：`SCL=U3.4 GPIO22; R8 4.7KΩ to +3.3V`；`SDA=U3.1 GPIO21; R10 4.7KΩ to +3.3V`；`separate_from_external=external bus uses GPIO32/GPIO33`
- 证据：图 3fe925cd9795 / 第 1 页 / C1-C2：U3 GPIO22/GPIO21 与 R8/R10；B3-B4 外部总线为 GPIO32/GPIO33

## GPIO 与控制信号

### S2 / GPIO39

GPIO39 由 R4（10KΩ）上拉至 +3.3V，S2 按下时接 GND，D1（RLSD52A031V）对地保护。

- 参数与网络：`gpio=GPIO39`；`pullup=R4 10KΩ`；`button=S2 SMT_SW_PTS_820 to GND`；`protection=D1 RLSD52A031V`
- 证据：图 3fe925cd9795 / 第 1 页 / B1-B2：R4/S2/D1 与 GPIO39/U2 SENSOR_VN 网络

### LED1 SK6812

LED1.VDD.4 接 +3.3V、VSS.2 接 GND、DIN.3 接 GPIO27，DOUT.1 未连接；R12（4.7KΩ）从 GPIO27/DIN 节点连接 +3.3V。

- 参数与网络：`data=GPIO27 -> DIN.3`；`supply=+3.3V`；`ground=VSS.2`；`dout=pin 1 NC`；`pullup=R12 4.7KΩ to +3.3V`；`decoupling=C14 100nF`
- 证据：图 3fe925cd9795 / 第 1 页 / D1-D2：LED1 SK6812、GPIO27、R12、C14 与 DOUT 未连接标记

## 时钟

### U2 ESP32-PICO-D4

本页未显示连接 U2 的外部晶体、谐振器或有源时钟器件。

- 参数与网络：`external_crystal=none shown`；`external_oscillator=none shown`；`controller_module=ESP32-PICO-D4`
- 证据：图 3fe925cd9795 / 第 1 页 / 全页 U2 及外围，无晶体/时钟源符号

## 复位

### U2 EN / S1

EN 节点由 R3（10KΩ）上拉至 +3.3V、C6（100nF）接 GND，S1 按下时将 EN 接地，D2（RLSD52A031V）对地保护。

- 参数与网络：`reset_net=EN / U2.9`；`pullup=R3 10KΩ`；`capacitor=C6 100nF`；`button=S1 SW-PB to GND`；`protection=D2 RLSD52A031V`
- 证据：图 3fe925cd9795 / 第 1 页 / B1-B2：S1/R3/C6/D2 与 U2 EN.9

## 保护电路

### J2、U3、S1、S2

J2 的 GPIO32/GPIO33 分别由 D4/D5（RLSD52A031V）对地保护，+5V 由 D3（LESD3Z5.0CMT1G）保护；S1/S2 使用 D2/D1，U3 +3.3V 使用 D6（RLSD52A031V）。

- 参数与网络：`external_scl_sda=D4/D5 RLSD52A031V`；`external_5v=D3 LESD3Z5.0CMT1G`；`reset_button=D2 RLSD52A031V`；`function_button=D1 RLSD52A031V`；`sensor_supply=D6 RLSD52A031V`
- 证据：图 3fe925cd9795 / 第 1 页 / B1、B3-B4、C1：D1~D6 与各受保护网络和 GND

## 内存与 Flash

### U2 存储连接

本页未显示外接 Flash、PSRAM、EEPROM 或存储卡器件；VDD_SDIO 仅显示 C13（1uF）去耦。

- 参数与网络：`external_flash=none shown`；`external_psram=none shown`；`eeprom=none shown`；`memory_card=none shown`；`vdd_sdio=C13 1uF`
- 证据：图 3fe925cd9795 / 第 1 页 / B2-D3：U2 SDIO 脚未连接外部存储，VDD_SDIO 仅接 C13

## 音频

### LS1 蜂鸣器

GPIO25 经 R11（1KΩ）驱动 Q1 基极，R13（4.7KΩ）下拉；Q1 发射极接 GND、集电极低边驱动 LS1，LS1 高端经 R9（10Ω）接 +3.3V，D7（1N4007WS）跨接负载。

- 参数与网络：`gpio=GPIO25`；`base_resistor=R11 1KΩ`；`base_pulldown=R13 4.7KΩ`；`transistor=Q1 SS8050 Y1`；`series_supply=+3.3V via R9 10Ω`；`load=LS1 Buzzer`；`flyback=D7 1N4007WS`
- 证据：图 3fe925cd9795 / 第 1 页 / C4-D4：+3.3V/R9/LS1/D7/Q1/R11/R13/GPIO25 完整支路

## 传感器

### U3 MLX90640

U3.VDD.2 接 +3.3V，GND.3 接地，SCL.4 接 GPIO22，SDA.1 接 GPIO21。

- 参数与网络：`VDD=pin 2 +3.3V`；`GND=pin 3`；`SCL=pin 4 GPIO22`；`SDA=pin 1 GPIO21`
- 证据：图 3fe925cd9795 / 第 1 页 / C1-C2：U3 MLX90640 四脚与 +3.3V/GND/GPIO22/GPIO21

## 调试与烧录

### J1 DownloadSocket

J1.1 接 +3.3V，J1.2 TXD 接 UTX/U2.U0TXD.41，J1.3 RXD 接 URX/U2.U0RXD.40，J1.4 接 EN，J1.5 G0 接 GPIO0，J1.6 接 GND。

- 参数与网络：`pin_1=+3.3V`；`pin_2=TXD / UTX / U2.41`；`pin_3=RXD / URX / U2.40`；`pin_4=EN`；`pin_5=G0 / GPIO0`；`pin_6=GND`
- 证据：图 3fe925cd9795 / 第 1 页 / A3-A4 J1 六脚与 B2-C3 U2 UTX/URX/EN/GPIO0 同名网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Thermal2 | `controller=U2 ESP32-PICO-D4`；`sensor=U3 MLX90640`；`sensor_bus=GPIO22 SCL / GPIO21 SDA`；`external_bus=GPIO32 SCL / GPIO33 SDA`；`rgb=LED1 GPIO27`；`buzzer=LS1/Q1 GPIO25`；`button=S2 GPIO39` |
| 接口 | J2 | `connector=HY-2.0_IIC`；`pin_1=IIC_SCL / GPIO32`；`pin_2=IIC_SDA / GPIO33`；`pin_3=VCC / +5V`；`pin_4=GND`；`power_direction=+5V input to board` |
| 总线 | J2 与 U2 | `SCL=J2.1 -> GPIO32 / U2.12; R5 4.7KΩ to +3.3V`；`SDA=J2.2 -> GPIO33 / U2.13; R6 4.7KΩ to +3.3V`；`controller_role=U2 firmware-facing external I2C` |
| 传感器 | U3 MLX90640 | `VDD=pin 2 +3.3V`；`GND=pin 3`；`SCL=pin 4 GPIO22`；`SDA=pin 1 GPIO21` |
| 总线 | U2 与 U3 MLX90640 | `SCL=U3.4 GPIO22; R8 4.7KΩ to +3.3V`；`SDA=U3.1 GPIO21; R10 4.7KΩ to +3.3V`；`separate_from_external=external bus uses GPIO32/GPIO33` |
| 总线地址 | Unit Thermal2 / MLX90640 地址 | `documented_address=0x33`；`external_bus=GPIO32/GPIO33`；`sensor_bus=GPIO22/GPIO21`；`schematic_address=未标注` |
| 传感器 | MLX90640 热成像性能 | `documented_resolution=32x24`；`documented_fov=110°x75°`；`documented_measurement_range=-40~300°C`；`documented_refresh_rate=0.5~64Hz`；`schematic_values=未标注` |
| 电源 | U1 SY8089 | `input=+5V to VIN.4 and EN.1`；`output=+3.3V`；`inductor=L1 C3015 4.7uH`；`feedback=R1 68KΩ, R2 15KΩ`；`input_caps=C4 22uF, C5 100nF`；`output_caps=C2 100nF, C3 22uF` |
| 电源 | +3.3V 与 VDD_SDIO | `main_rail=+3.3V`；`bulk_caps=C9 22uF, C10 22uF`；`logic_decoupling=C11/C12/C14/C1/C7/C8 100nF`；`sdio_rail=VDD_SDIO with C13 1uF` |
| 电源 | +5V 输入能力 | `voltage=+5V`；`documented_current=0.5A`；`schematic_current=未标注`；`input_protection=D3 ESD only` |
| 调试与烧录 | J1 DownloadSocket | `pin_1=+3.3V`；`pin_2=TXD / UTX / U2.41`；`pin_3=RXD / URX / U2.40`；`pin_4=EN`；`pin_5=G0 / GPIO0`；`pin_6=GND` |
| 接口 | P1 | `connector=Header 4`；`pin_1=GPIO32`；`pin_2=GPIO33`；`pin_3=+5V`；`pin_4=GND` |
| 复位 | U2 EN / S1 | `reset_net=EN / U2.9`；`pullup=R3 10KΩ`；`capacitor=C6 100nF`；`button=S1 SW-PB to GND`；`protection=D2 RLSD52A031V` |
| GPIO 与控制信号 | S2 / GPIO39 | `gpio=GPIO39`；`pullup=R4 10KΩ`；`button=S2 SMT_SW_PTS_820 to GND`；`protection=D1 RLSD52A031V` |
| GPIO 与控制信号 | LED1 SK6812 | `data=GPIO27 -> DIN.3`；`supply=+3.3V`；`ground=VSS.2`；`dout=pin 1 NC`；`pullup=R12 4.7KΩ to +3.3V`；`decoupling=C14 100nF` |
| 音频 | LS1 蜂鸣器 | `gpio=GPIO25`；`base_resistor=R11 1KΩ`；`base_pulldown=R13 4.7KΩ`；`transistor=Q1 SS8050 Y1`；`series_supply=+3.3V via R9 10Ω`；`load=LS1 Buzzer`；`flyback=D7 1N4007WS` |
| 保护电路 | J2、U3、S1、S2 | `external_scl_sda=D4/D5 RLSD52A031V`；`external_5v=D3 LESD3Z5.0CMT1G`；`reset_button=D2 RLSD52A031V`；`function_button=D1 RLSD52A031V`；`sensor_supply=D6 RLSD52A031V` |
| 时钟 | U2 ESP32-PICO-D4 | `external_crystal=none shown`；`external_oscillator=none shown`；`controller_module=ESP32-PICO-D4` |
| 内存与 Flash | U2 存储连接 | `external_flash=none shown`；`external_psram=none shown`；`eeprom=none shown`；`memory_card=none shown`；`vdd_sdio=C13 1uF` |

## 待确认事项

- `address.i2c-0x33-unconfirmed`：产品正文标注 I2C 地址 0x33，但原理图未在外部 GPIO32/33 总线或内部 MLX90640 GPIO22/21 总线上标注地址，不能由本页确定该地址属于固件从机、传感器或两者。（证据：图 3fe925cd9795 / 第 1 页 / B2-B4 与 C1-C2：两组 I2C 网络及器件引脚，均无地址文字或绑带）
- `sensor.performance-unconfirmed`：正文列出的 32x24 分辨率、110°x75° FOV、-40~300°C 测量范围和 0.5~64Hz 刷新率未在原理图中标注。（证据：图 3fe925cd9795 / 第 1 页 / C1-C2：U3 仅标 MLX90640 和四个电气引脚，无光学/测温参数）
- `power.input-current-unconfirmed`：原理图确认 J2/P1 的 +5V 供电网络，但没有标注正文所列 5V@0.5A 电源要求或电流保护。（证据：图 3fe925cd9795 / 第 1 页 / A3 P1、B3-B4 J2 与 A1 U1 的 +5V 网络，无 0.5A 或保险丝标注）
- `review.i2c-address`：正文所列 0x33 是外部 Unit Thermal2 固件从机地址、内部 MLX90640 地址，还是二者均使用该值？；原因：原理图显示两条分离的 I2C 总线但没有地址文字或固件协议，需用通信协议、固件或总线扫描确认。
- `review.sensor-performance`：量产 MLX90640 模组的分辨率、FOV、测温范围和刷新率是否为正文所列值？；原因：原理图只确认 MLX90640 型号及四线电气连接，光学版本和性能需以具体传感器订货号/数据手册或实测确认。
- `review.input-current`：Unit Thermal2 的外部 +5V 供电是否要求或限制为 0.5A？；原因：原理图没有电流标注、保险丝或功耗边界，需由 BOM、热设计或负载实测确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3fe925cd9795eb9759a2bbb0e9469bb56750d7c3c7ab766c5751bc364b91ed6f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/603/SCH_UNIT-THERMAL2_sch_01.png` |

---

源文档：`zh_CN/unit/Thermal2.md`

源文档 SHA-256：`77b9e04d9691b6419fb384c76901711bee0942656d49f692e1059dbf15c133bd`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
