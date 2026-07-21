# Module13.2 QRCode 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 QRCode |
| SKU | M145 |
| 产品 ID | `module13-2-qrcode-4a6d94edd708` |
| 源文档 | `zh_CN/module/Module13.2_QRCode.md` |

## 概述

Module13.2 QRCode 从 J4 DC005 的 DC 9–24 V 输入经保护、保险丝和 U1 SY8303AIC 降压产生 BUS_5V，再由 U2 ME6206A33XG 生成 MCU_3V3。U3 PI4IOE5V6408 通过 I2C 控制 QR_5V_EN 和 TRIG，U4 MT9700 为 FPC1 扫码引擎切换 QR_5V；FPC1 同时提供 UART、USB、BEEP 和触发信号。SW1/SW2 为 BUS_RX/BUS_TX 选择主机 GPIO，S2 在 Port C 的 DM-/DP+ USB 路径和 GPIO16/GPIO17 UART 路径间切换，另有 Port A I2C、Port B GPIO 与晶体管蜂鸣器驱动。

## 检索关键词

`Module13.2 QRCode`、`M145`、`PI4IOE5V6408ZTAEX`、`0x43`、`0x44`、`SY8303AIC`、`ME6206A33XG`、`MT9700`、`DC005`、`DC9-24V`、`BUS_5V`、`MCU_3V3`、`QR_5V`、`QR_5V_EN`、`TRIG`、`QR_RX`、`QR_TX`、`BUS_RX`、`BUS_TX`、`DM-`、`DP+`、`UART`、`USB`、`SW1`、`SW2`、`S2`、`GPIO34`、`GPIO13`、`GPIO16`、`GPIO3`、`GPIO12`、`GPIO15`、`GPIO17`、`GPIO1`、`I2C_SDA`、`I2C_SCL`、`GROVE_A`、`GROVE_B`、`GROVE_C`、`FPC-12P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | PI4IOE5V6408ZTAEX | I2C GPIO 扩展器，P0 控制 QR_5V_EN，P4 输出 TRIG，并提供可选地址 0x43/0x44 | 图 3b0385802260 / 第 1 页 / B1-C2 U3 PI4IOE5V6408ZTAEX pins1-16 and address note |
| U1 | SY8303AIC | 将 VIN 降压为 BUS_5V 的开关转换器 | 图 3b0385802260 / 第 1 页 / A1-A2 DCDC 分区 U1 SY8303AIC/L1/R5-R8/C2-C7 |
| U2 | ME6206A33XG | 从 BUS_5V 产生 MCU_3V3 的 3.3 V LDO | 图 3b0385802260 / 第 1 页 / A3 LDO 3.3V 分区 U2 ME6206A33XG/C9-C12 |
| U4 | MT9700 | 由 QR_5V_EN 控制的扫码引擎 5 V 负载开关 | 图 3b0385802260 / 第 1 页 / D1-D2 U4 MT9700、BUS_5V/QR_5V/QR_5V_EN |
| FPC1 | FPC-12P | 扫码引擎连接器，承载 QR_5V、UART、USB、BEEP 与 TRIG | 图 3b0385802260 / 第 1 页 / D2 FPC1 FPC-12P pins1-12 |
| SW1/SW2 | 未标注 | BUS_RX 和 BUS_TX 到多组 M5-Bus GPIO 的四路选择开关 | 图 3b0385802260 / 第 1 页 / B3-C3 SW1 BUS_RX/GPIO34/13/16/3 与 SW2 BUS_TX/GPIO12/15/17/1 |
| S2 | 未标注 | Port C 在 QR USB DM-/DP+ 与主机 UART GPIO16/GPIO17 之间的双刀切换开关 | 图 3b0385802260 / 第 1 页 / C4 S2 USB/UART switch pins1-6 |
| J1/J2/J3 | GROVE_A / GROVE_B / GROVE_C | Port A I2C、Port B GPIO 与 Port C USB/UART 三组 HY2.0-4P 接口 | 图 3b0385802260 / 第 1 页 / B4-C4 J1 GROVE_A、J2 GROVE_B、J3 GROVE_C |
| BUS1 | M5Stack_BUS | 30 针主机接口，承载 BUS_5V、HPWR、I2C、Port B GPIO 与 UART 候选 GPIO | 图 3b0385802260 / 第 1 页 / A4-B4 BUS1 M5Stack_BUS pins1-30 |
| J4 | DC005 | 标注 DC 9–24 V 的直流电源输入插座，输入进入 HPWR | 图 3b0385802260 / 第 1 页 / A1 J4 DC005、INPUT: DC9-24V、HPWR |
| D1/FU1/D2 | SMAJ30CA / 0805L050/30AR / TVS 5V | DC 输入浪涌保护、可恢复保险丝和 BUS_5V 钳位保护 | 图 3b0385802260 / 第 1 页 / A1-A2 D1 SMAJ30CA/FU1 0805L050/30AR/D2 TVS 5V |
| P1/Q1/D3 | Buzzer / SS8050 Y1 / 1N4148WS | BEEP 控制的低侧晶体管蜂鸣器驱动及反向电压钳位 | 图 3b0385802260 / 第 1 页 / D3 P1 Buzzer/Q1 SS8050 Y1/D3/R1-R3 |

## 系统结构

### Module13.2 QRCode 系统架构

DC 输入经保护和 U1 产生 BUS_5V，U2 再产生 MCU_3V3；U3 I2C GPIO 扩展器控制 U4 扫码引擎电源与 TRIG，FPC1 提供 UART/USB/BEEP，三组 Grove 与 M5-Bus 完成外部连接。

- 参数与网络：`dc_input=J4 DC005`；`buck=U1 SY8303AIC`；`5v_rail=BUS_5V`；`ldo=U2 ME6206A33XG`；`logic_rail=MCU_3V3`；`io_expander=U3 PI4IOE5V6408ZTAEX`；`load_switch=U4 MT9700`；`scanner=FPC1 FPC-12P`；`host=BUS1 M5Stack_BUS`
- 证据：图 3b0385802260 / 第 1 页 / 整页 DCDC/LDO/MBUS/U3/PortC/FPC1/Buzzer 分区

## 电源

### DC 9–24 V 输入

J4 DC005 旁明确标注 INPUT: DC9-24V，正输入连接 HPWR，负端连接 GND；HPWR 同时连接 BUS1 pins25/27/29。

- 参数与网络：`connector=J4 DC005`；`range=DC9-24V`；`positive=HPWR`；`negative=GND`；`m5bus=BUS1 pins25/27/29 HPWR`
- 证据：图 3b0385802260 / 第 1 页 / A1 J4/INPUT DC9-24V/HPWR；A4 BUS1 HPWR

### VIN 至 BUS_5V 降压

U1 SY8303AIC 从 VIN 经 LX 与 L1 10 uH 输出 BUS_5V，反馈/补偿网络由 R5-R8 与 C3 构成，输出配置两颗 22 uF/6.3 V 电容。

- 参数与网络：`converter=U1 SY8303AIC`；`input=VIN`；`inductor=L1 10uH`；`output=BUS_5V`；`feedback=R5 220K; R7 30K; R6 220K; R8 10K`；`compensation=C3 22pF/50V`；`output_caps=C6/C7 22uF/6.3V`
- 证据：图 3b0385802260 / 第 1 页 / A2 U1/L1/R5-R8/C2/C3/C6/C7/BUS_5V

### BUS_5V 至 MCU_3V3

U2 ME6206A33XG Vin pin3 接 BUS_5V、Vout pin2 输出 MCU_3V3、GND pin1 接地；输入 C9 10 uF/C10 100 nF，输出 C11 100 nF/C12 10 uF。

- 参数与网络：`ldo=U2 ME6206A33XG`；`input=BUS_5V pin3`；`output=MCU_3V3 pin2`；`ground=pin1`；`input_caps=C9 10uF; C10 100nF`；`output_caps=C11 100nF; C12 10uF`
- 证据：图 3b0385802260 / 第 1 页 / A3 U2 ME6206A33XG/C9-C12

### 扫码引擎 5 V 负载开关

U4 MT9700 VIN pin5 接 BUS_5V、VOUT pin1 输出 QR_5V、EN pin4 接 QR_5V_EN；R17 100 kΩ 下拉 EN，R18 标 NC，R16 10 kΩ 接 SET，C16/C15 各 10 uF。

- 参数与网络：`switch=U4 MT9700`；`input=BUS_5V`；`output=QR_5V`；`enable=QR_5V_EN`；`enable_pulldown=R17 100K`；`optional_pullup=R18 NC`；`set=R16 10K`；`caps=C16 input 10uF; C15 output 10uF`
- 证据：图 3b0385802260 / 第 1 页 / D1-D2 U4/R16-R18/C15/C16

## 接口

### 扫码引擎 FPC 引脚

FPC1 pin2 为 QR_5V、pin3 GND、pin4 RX/QR_RX、pin5 TX/QR_TX、pin6 DM-、pin7 DP+、pin9 BUZ/BEEP、pin12 TRIG；pins1/8/10/11 未连接。

- 参数与网络：`connector=FPC1 FPC-12P`；`power=pin2 QR_5V; pin3 GND`；`uart=pin4 RX QR_RX; pin5 TX QR_TX`；`usb=pin6 DM-; pin7 DP+`；`buzzer=pin9 BUZ BEEP`；`trigger=pin12 TRIG`；`unused=pins1/8/10/11`
- 证据：图 3b0385802260 / 第 1 页 / D2 FPC1 pins1-12

### Port A I2C Grove

J1 GROVE_A 的 IO2 为 I2C_SCL、IO1 为 I2C_SDA、5V 为 BUS_5V、GND 接地。

- 参数与网络：`connector=J1 GROVE_A`；`io2=I2C_SCL`；`io1=I2C_SDA`；`vcc=BUS_5V`；`ground=GND`
- 证据：图 3b0385802260 / 第 1 页 / B4 J1 GROVE_A

### Port B GPIO Grove

J2 GROVE_B 的 IO2 为 GPIO36、IO1 为 GPIO26、5V 为 BUS_5V、GND 接地；GPIO36/GPIO26 同时来自 BUS1 pins4/10。

- 参数与网络：`connector=J2 GROVE_B`；`io2=GPIO36 / BUS1 pin4`；`io1=GPIO26 / BUS1 pin10`；`vcc=BUS_5V`；`ground=GND`
- 证据：图 3b0385802260 / 第 1 页 / B4 J2 GROVE_B；A4 BUS1 GPIO36/GPIO26

### Port C USB/UART 切换

J3 IO2 经 R13 22 Ω 连接 S2 公共端 pin2，IO1 经 R14 22 Ω 连接公共端 pin5；USB 位置连接 DM-/DP+，UART 位置连接 GPIO16/GPIO17。

- 参数与网络：`connector=J3 GROVE_C`；`io2=R13 22R -> S2 pin2 -> DM- pin3 or GPIO16 pin1`；`io1=R14 22R -> S2 pin5 -> DP+ pin6 or GPIO17 pin4`；`vcc=BUS_5V`；`ground=GND`；`modes=USB or UART`
- 证据：图 3b0385802260 / 第 1 页 / C4 J3/R13/R14/S2/DM-/DP+/GPIO16/GPIO17

### M5-Bus 使用网络

BUS1 使用 pins1/3/5 GND、pin4 GPIO36、pin10 GPIO26、pin17 I2C_SDA、pin18 I2C_SCL、pins25/27/29 HPWR、pin28 BUS_5V；UART 候选为 pin26 GPIO34、pin22 GPIO13、pin15 GPIO16、pin13 GPIO3、pin21 GPIO12、pin23 GPIO15、pin16 GPIO17、pin14 GPIO1，pin30 BAT 未连接。

- 参数与网络：`ground=pins1/3/5`；`port_b=pin4 GPIO36; pin10 GPIO26`；`i2c=pin17 SDA; pin18 SCL`；`hpwr=pins25/27/29`；`5v=pin28 BUS_5V`；`bus_rx_candidates=pin26 GPIO34; pin22 GPIO13; pin15 GPIO16; pin13 GPIO3`；`bus_tx_candidates=pin21 GPIO12; pin23 GPIO15; pin16 GPIO17; pin14 GPIO1`；`battery=pin30 NC`
- 证据：图 3b0385802260 / 第 1 页 / A4-B4 BUS1 M5Stack_BUS pins1-30

## 总线

### PI4IOE5V6408 I2C 总线

BUS1 pin17/GPIO21 的 I2C_SDA 与 pin18/GPIO22 的 I2C_SCL 连接 U3 SDA pin14/SCL pin13，并由 R20/R19 各 4.7 kΩ 上拉到 MCU_3V3；Port A 同步引出该总线。

- 参数与网络：`controller=host via BUS1`；`device=U3 PI4IOE5V6408ZTAEX`；`sda=BUS1 pin17 GPIO21 -> U3 pin14 -> J1 IO1`；`scl=BUS1 pin18 GPIO22 -> U3 pin13 -> J1 IO2`；`pullups=R20 SDA 4.7K; R19 SCL 4.7K to MCU_3V3`；`level=MCU_3V3`
- 证据：图 3b0385802260 / 第 1 页 / B1-B2 U3/R19/R20/I2C；A4 BUS1 pins17/18；B4 J1

### 扫码引擎 UART

FPC1 RX/QR_RX 经 R11 0 Ω 连接 BUS_TX，FPC1 TX/QR_TX 经 R12 0 Ω 连接 BUS_RX；BUS_RX 与 BUS_TX 再由 SW1/SW2 选择主机 GPIO。

- 参数与网络：`scanner_rx=FPC1 pin4 QR_RX <- R11 0R <- BUS_TX`；`scanner_tx=FPC1 pin5 QR_TX -> R12 0R -> BUS_RX`；`direction=BUS_TX host-to-scanner; BUS_RX scanner-to-host`；`routing=SW1 BUS_RX; SW2 BUS_TX`
- 证据：图 3b0385802260 / 第 1 页 / D2 FPC1/R11/R12/BUS_TX/BUS_RX；B3-C3 SW1/SW2

## 总线地址

### PI4IOE5V6408 地址选择

原理图地址注记为 ADDR=L 0x43（Default）、ADDR=H 0x44；U3 ADDR pin9 由 R21 10 kΩ 下拉，并可通过 JP1 接 MCU_3V3。

- 参数与网络：`device=U3 PI4IOE5V6408ZTAEX`；`default=0x43`；`high=0x44`；`address_pin=pin9 ADDR`；`pulldown=R21 10K to GND`；`high_option=JP1 to MCU_3V3`
- 证据：图 3b0385802260 / 第 1 页 / B1-C2 U3 ADDR/JP1/R21 and I2C Addr Select note

## GPIO 与控制信号

### QR 电源与触发 GPIO

U3 P0 pin12 输出 QR_5V_EN，P4 pin6 输出 TRIG；P1/P2/P3/P5/P6/P7 在页面未连接。

- 参数与网络：`power_enable=U3 P0 pin12 QR_5V_EN`；`trigger=U3 P4 pin6 TRIG`；`unused=P1 pin11; P2 pin8; P3 pin7; P5 pin5; P6 pin4; P7 pin3`
- 证据：图 3b0385802260 / 第 1 页 / B2-C2 U3 P0-P7 labels

### 扫码 UART GPIO 选择

SW1 将 BUS_RX 选择连接 GPIO34、GPIO13、GPIO16 或 GPIO3；SW2 将 BUS_TX 选择连接 GPIO12、GPIO15、GPIO17 或 GPIO1。

- 参数与网络：`scanner_to_host=BUS_RX -> GPIO34/GPIO13/GPIO16/GPIO3 via SW1`；`host_to_scanner=BUS_TX -> GPIO12/GPIO15/GPIO17/GPIO1 via SW2`；`selection=one or more mechanical switch channels`
- 证据：图 3b0385802260 / 第 1 页 / B3-C3 SW1/SW2 labels

## 复位

### IO 扩展器复位

U3 RESET pin10 由 R15 10 kΩ 上拉到 MCU_3V3，并由 C13 100 nF 对地；INT pin1 未连接。

- 参数与网络：`target=U3 RESET pin10`；`pullup=R15 10K to MCU_3V3`；`capacitor=C13 100nF to GND`；`interrupt=U3 INT pin1 unconnected`
- 证据：图 3b0385802260 / 第 1 页 / B1-C2 U3 RESET/INT/R15/C13

## 保护电路

### DC 输入保护

HPWR 对地配置 D1 SMAJ30CA，随后经 FU1 0805L050/30AR 进入 VIN；VIN 配置 C5 100 uF/35 V 与 C4 100 nF 对地。

- 参数与网络：`tvs=D1 SMAJ30CA`；`fuse=FU1 0805L050/30AR`；`after_fuse=VIN`；`bulk=C5 100uF/35V`；`decoupling=C4 100nF`
- 证据：图 3b0385802260 / 第 1 页 / A1 HPWR/D1/FU1/VIN/C5/C4

### BUS_5V 钳位

BUS_5V 输出对地配置 D2 TVS 5V，用于 5 V 轨钳位保护。

- 参数与网络：`rail=BUS_5V`；`device=D2 TVS 5V`；`connection=BUS_5V to GND`
- 证据：图 3b0385802260 / 第 1 页 / A2 BUS_5V/D2 TVS 5V

## 音频

### 扫码蜂鸣器驱动

FPC1 BEEP 经 R2 1 kΩ 驱动 Q1 SS8050 Y1，R3 10 kΩ 下拉基极；P1 蜂鸣器由 BUS_5V 经 R1 4.7 Ω 供电，D3 1N4148WS 跨接钳位。

- 参数与网络：`control=FPC1 pin9 BEEP`；`base_resistor=R2 1K`；`pulldown=R3 10K`；`transistor=Q1 SS8050 Y1`；`buzzer=P1`；`supply=BUS_5V via R1 4.7R`；`diode=D3 1N4148WS`
- 证据：图 3b0385802260 / 第 1 页 / D2-D3 FPC1 BEEP and P1/Q1/D3/R1-R3

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 QRCode 系统架构 | `dc_input=J4 DC005`；`buck=U1 SY8303AIC`；`5v_rail=BUS_5V`；`ldo=U2 ME6206A33XG`；`logic_rail=MCU_3V3`；`io_expander=U3 PI4IOE5V6408ZTAEX`；`load_switch=U4 MT9700`；`scanner=FPC1 FPC-12P`；`host=BUS1 M5Stack_BUS` |
| 电源 | DC 9–24 V 输入 | `connector=J4 DC005`；`range=DC9-24V`；`positive=HPWR`；`negative=GND`；`m5bus=BUS1 pins25/27/29 HPWR` |
| 保护电路 | DC 输入保护 | `tvs=D1 SMAJ30CA`；`fuse=FU1 0805L050/30AR`；`after_fuse=VIN`；`bulk=C5 100uF/35V`；`decoupling=C4 100nF` |
| 电源 | VIN 至 BUS_5V 降压 | `converter=U1 SY8303AIC`；`input=VIN`；`inductor=L1 10uH`；`output=BUS_5V`；`feedback=R5 220K; R7 30K; R6 220K; R8 10K`；`compensation=C3 22pF/50V`；`output_caps=C6/C7 22uF/6.3V` |
| 保护电路 | BUS_5V 钳位 | `rail=BUS_5V`；`device=D2 TVS 5V`；`connection=BUS_5V to GND` |
| 电源 | BUS_5V 至 MCU_3V3 | `ldo=U2 ME6206A33XG`；`input=BUS_5V pin3`；`output=MCU_3V3 pin2`；`ground=pin1`；`input_caps=C9 10uF; C10 100nF`；`output_caps=C11 100nF; C12 10uF` |
| 总线 | PI4IOE5V6408 I2C 总线 | `controller=host via BUS1`；`device=U3 PI4IOE5V6408ZTAEX`；`sda=BUS1 pin17 GPIO21 -> U3 pin14 -> J1 IO1`；`scl=BUS1 pin18 GPIO22 -> U3 pin13 -> J1 IO2`；`pullups=R20 SDA 4.7K; R19 SCL 4.7K to MCU_3V3`；`level=MCU_3V3` |
| 总线地址 | PI4IOE5V6408 地址选择 | `device=U3 PI4IOE5V6408ZTAEX`；`default=0x43`；`high=0x44`；`address_pin=pin9 ADDR`；`pulldown=R21 10K to GND`；`high_option=JP1 to MCU_3V3` |
| 复位 | IO 扩展器复位 | `target=U3 RESET pin10`；`pullup=R15 10K to MCU_3V3`；`capacitor=C13 100nF to GND`；`interrupt=U3 INT pin1 unconnected` |
| GPIO 与控制信号 | QR 电源与触发 GPIO | `power_enable=U3 P0 pin12 QR_5V_EN`；`trigger=U3 P4 pin6 TRIG`；`unused=P1 pin11; P2 pin8; P3 pin7; P5 pin5; P6 pin4; P7 pin3` |
| 电源 | 扫码引擎 5 V 负载开关 | `switch=U4 MT9700`；`input=BUS_5V`；`output=QR_5V`；`enable=QR_5V_EN`；`enable_pulldown=R17 100K`；`optional_pullup=R18 NC`；`set=R16 10K`；`caps=C16 input 10uF; C15 output 10uF` |
| 接口 | 扫码引擎 FPC 引脚 | `connector=FPC1 FPC-12P`；`power=pin2 QR_5V; pin3 GND`；`uart=pin4 RX QR_RX; pin5 TX QR_TX`；`usb=pin6 DM-; pin7 DP+`；`buzzer=pin9 BUZ BEEP`；`trigger=pin12 TRIG`；`unused=pins1/8/10/11` |
| 总线 | 扫码引擎 UART | `scanner_rx=FPC1 pin4 QR_RX <- R11 0R <- BUS_TX`；`scanner_tx=FPC1 pin5 QR_TX -> R12 0R -> BUS_RX`；`direction=BUS_TX host-to-scanner; BUS_RX scanner-to-host`；`routing=SW1 BUS_RX; SW2 BUS_TX` |
| GPIO 与控制信号 | 扫码 UART GPIO 选择 | `scanner_to_host=BUS_RX -> GPIO34/GPIO13/GPIO16/GPIO3 via SW1`；`host_to_scanner=BUS_TX -> GPIO12/GPIO15/GPIO17/GPIO1 via SW2`；`selection=one or more mechanical switch channels` |
| 接口 | Port A I2C Grove | `connector=J1 GROVE_A`；`io2=I2C_SCL`；`io1=I2C_SDA`；`vcc=BUS_5V`；`ground=GND` |
| 接口 | Port B GPIO Grove | `connector=J2 GROVE_B`；`io2=GPIO36 / BUS1 pin4`；`io1=GPIO26 / BUS1 pin10`；`vcc=BUS_5V`；`ground=GND` |
| 接口 | Port C USB/UART 切换 | `connector=J3 GROVE_C`；`io2=R13 22R -> S2 pin2 -> DM- pin3 or GPIO16 pin1`；`io1=R14 22R -> S2 pin5 -> DP+ pin6 or GPIO17 pin4`；`vcc=BUS_5V`；`ground=GND`；`modes=USB or UART` |
| 音频 | 扫码蜂鸣器驱动 | `control=FPC1 pin9 BEEP`；`base_resistor=R2 1K`；`pulldown=R3 10K`；`transistor=Q1 SS8050 Y1`；`buzzer=P1`；`supply=BUS_5V via R1 4.7R`；`diode=D3 1N4148WS` |
| 接口 | M5-Bus 使用网络 | `ground=pins1/3/5`；`port_b=pin4 GPIO36; pin10 GPIO26`；`i2c=pin17 SDA; pin18 SCL`；`hpwr=pins25/27/29`；`5v=pin28 BUS_5V`；`bus_rx_candidates=pin26 GPIO34; pin22 GPIO13; pin15 GPIO16; pin13 GPIO3`；`bus_tx_candidates=pin21 GPIO12; pin23 GPIO15; pin16 GPIO17; pin14 GPIO1`；`battery=pin30 NC` |
| 传感器 | 640×480 CMOS 与码制能力 | `document_sensor=640x480 CMOS`；`document_2d=PDF417, QR Code, Data Matrix`；`document_1d_count=14`；`schematic_engine=FPC1 only`；`sensor_part_number=null` |
| 接口 | USB 虚拟串口、HID 键盘与 HID-POS | `document_modes=USB virtual serial; USB HID keyboard; USB HID-POS`；`schematic_usb=FPC1 DM-/DP+ via S2 to Port C`；`firmware_mode=not shown` |
| 传感器 | 照明与瞄准 LED | `document_illumination=white LED`；`document_targeting=red LED`；`schematic_led=not shown`；`fpc_led_pin=pin10 NC` |
| 电源 | 主机组合工作电流 | `document_5v=off 5.04V@74.42mA; on 5.09V@255.84mA`；`document_9v=off 9.09V@98.93mA; on 9.10V@153.44mA`；`document_10v=off 10.49V@79.96mA; on 10.38V@124.54mA`；`schematic_measurement=not shown` |

## 待确认事项

- `sensor.scan-engine`：产品正文声明扫码引擎为 640×480 CMOS，并支持 3 类二维码和 14 类一维码；原理图仅显示 FPC1 接口，没有传感器型号或码制表。（证据：图 3b0385802260 / 第 1 页 / FPC1 FPC-12P lacks sensor/decoder identity）
- `interface.usb-modes`：产品正文称 QR 引擎 USB 可配置为虚拟串口、HID 键盘和 HID-POS，原理图只显示 DM-/DP+ 电气路径，没有 USB 描述符或固件模式。（证据：图 3b0385802260 / 第 1 页 / FPC1 pins6/7 and S2 USB path）
- `sensor.illumination-targeting`：产品正文称扫码引擎内含白光照明和红光瞄准 LED，但原理图未画这些 LED；FPC1 LED pin10 还标为未连接。（证据：图 3b0385802260 / 第 1 页 / FPC1 pin10 LED marked no-connect）
- `power.operating-current`：产品正文列出 Core2 组合在 5 V、9 V、约 10 V 下的开关机电流，但原理图没有测试条件、负载状态或电流测量点。（证据：图 3b0385802260 / 第 1 页 / J4/U1/BUS_5V/FPC1 power path lacks current annotations）
- `review.scan-engine`：请用扫码引擎铭牌、BOM 或用户手册确认 CMOS 型号、640×480 分辨率及支持码制。；原因：原理图仅显示 12 针接口，没有展开传感器和解码器。
- `review.usb-modes`：请用扫码引擎固件配置或 USB 枚举结果确认虚拟串口、HID 键盘和 HID-POS 模式。；原因：USB 工作模式不由 DM-/DP+ 原理图连线决定。
- `review.illumination-targeting`：请用扫码引擎模组资料或实物确认白光照明、红光瞄准 LED 及其控制方式。；原因：这些 LED 未在板级原理图中显示。
- `review.operating-current`：请按明确输入电压、Core2 状态、扫码引擎开关和触发模式复测工作电流。；原因：原理图没有电流测试条件或测量数据。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `3b03858022600b4da4b208084e2109505e30b5e725e7126044365be1c8fba553` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1163/SCH_Module13.2_QRCODE_V1.0_docs_page_01.png` |

---

源文档：`zh_CN/module/Module13.2_QRCode.md`

源文档 SHA-256：`e65eed42c72f9ae123db5338b2a44da46fe57d5cd17c0d6a607b054f153ef68c`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
