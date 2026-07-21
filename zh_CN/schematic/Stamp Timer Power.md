# Stamp Timer Power 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp Timer Power |
| SKU | S005 |
| 产品 ID | `stamp-timer-power-e1b11c744436` |
| 源文档 | `zh_CN/module/StampTimerPower.md` |

## 概述

Stamp Timer Power 以 U1 TP4057 为单节电池充电器，Q1/Q3/Q2 与 WAKE/HOLD/INT 网络构成手动和 RTC 定时唤醒后的电源保持路径，VBAT_OUT 再分别送入 U2 SY7088 生成 +5VOUT、U3 SY8089 生成 +3V3OUT。U4 RTC8563 使用 32.768kHz 晶体，通过 SCL/SDA 与主机通信，并以 INT 参与唤醒控制。J1 StampTimerPWR_Pin 集中引出输入、输出、控制和 I2C，J3 HY-2.0_IIC 另提供 SCL/SDA/+5VOUT/GND。

## 检索关键词

`Stamp Timer Power`、`S005`、`TP4057`、`RTC8563`、`BM8563`、`SY7088`、`SY8089`、`LP3218DT1G`、`LN2324DT2AG`、`32.768kHz`、`I2C`、`0x51`、`0xA2`、`0xA3`、`+5VIN`、`VBAT_IN`、`+VIN`、`VBAT_OUT`、`+5VOUT`、`+3V3OUT`、`HOLD`、`WAKE`、`INT`、`3V3EN`、`SCL`、`SDA`、`StampTimerPWR_Pin`、`HY-2.0_IIC`、`SW-PB`、`B5819WT`、`PESDNC2FD3V3B`、`battery charger`、`RTC wake`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | TP4057 | +5VIN 至 VBAT_IN 的锂电池线性充电控制器 | 图 b478d31c117e / 第 1 页 / 页面 A1-B1 U1 TP4057，VCC/BAT/PROG/CHRG/STDBY/GND 引脚与 R13/R7/C1/C7 |
| U2 | SY7088 | VBAT_OUT 至 +5VOUT 的升压转换器 | 图 b478d31c117e / 第 1 页 / 页面 A3-B4 虚线框 U2 SY7088、L1 1.5uH、R1/R2 与 +5VOUT |
| U3 | SY8089 | VBAT_OUT 至 +3V3OUT 的降压转换器 | 图 b478d31c117e / 第 1 页 / 页面 B3-C4 虚线框 U3 SY8089、L2 4.7uH、R9/R10 与 +3V3OUT |
| U4 | RTC8563 | 带 INT 输出的 I2C 实时时钟与定时唤醒源 | 图 b478d31c117e / 第 1 页 / 页面 D1-D2 U4 RTC8563，OSCI/OSCO/INT/VSS/SDA/SCL/CLKOUT/VDD 引脚 |
| Y1,C12,C13 | 32.768KHz ±20ppm 12.5pF; 6.0pF; 6.0pF | RTC8563 的 32.768kHz 晶体时钟网络 | 图 b478d31c117e / 第 1 页 / 页面 D1 Y1 32.768KHz ±20ppm 12.5pF 与 OSCI/OSCO 两侧 C12/C13 6.0pF |
| Q1,Q3 | LP3218DT1G; LP3218DT1G | VBAT_IN 至 +VIN 与 +VIN 至 VBAT_OUT 的高侧电源开关 | 图 b478d31c117e / 第 1 页 / 页面 A1-A3 Q1/Q3 LP3218DT1G 串联在 VBAT_IN-+VIN-VBAT_OUT 电源路径 |
| Q2 | LN2324DT2AG | HOLD 控制的低侧晶体管，用于维持或释放 Q3 电源开关 | 图 b478d31c117e / 第 1 页 / 页面 B2-C2 Q2 LN2324DT2AG，栅极接 HOLD、R11 100K 下拉、漏极接 Q3 控制节点 |
| S1 | SW-PB | WAKE 手动唤醒按键 | 图 b478d31c117e / 第 1 页 / 页面 B2 S1 SW-PB，将 WAKE 节点按下接 GND |
| D4 | PESDNC2FD3V3B | WAKE 按键节点的 ESD 保护器件 | 图 b478d31c117e / 第 1 页 / 页面 B2 WAKE 节点 D4 PESDNC2FD3V3B 对 GND |
| D5,D6 | B5819WT; B5819WT | RTC INT 与手动 WAKE 到 Q3 控制节点的二极管或逻辑 | 图 b478d31c117e / 第 1 页 / 页面 B2 D5 从 INT、D6 从 WAKE 汇入 Q3/Q2 控制节点 |
| D2 | SS34 | +5VIN 与 +VIN 电源路径的肖特基二极管 | 图 b478d31c117e / 第 1 页 / 页面 A2 Q1 下方 D2 SS34，连接 +5VIN 与 +VIN 节点 |
| D1,R4 | LED; 1KΩ | VBAT_OUT 电源存在指示 | 图 b478d31c117e / 第 1 页 / 页面 A3-B3 VBAT_OUT 经 R4 1KΩ 与 D1 LED 接 GND |
| J1 | StampTimerPWR_Pin | 14 针 Stamp 封装主接口，提供输入输出电源、唤醒保持和 I2C | 图 b478d31c117e / 第 1 页 / 页面 D3 J1 StampTimerPWR_Pin，pin 1-14 网络名完整可见 |
| J3 | HY-2.0_IIC | SCL/SDA/+5VOUT/GND 的四针 I2C 扩展接口 | 图 b478d31c117e / 第 1 页 / 页面 D4 J3 HY-2.0_IIC，pin 1 SCL、2 SDA、3 +5VOUT、4 GND |

## 系统结构

### Stamp Timer Power 系统架构

TP4057 负责电池充电，Q1/Q3/Q2 与 WAKE/HOLD/RTC INT 负责电源门控和唤醒保持，SY7088 与 SY8089 分别提供 5V 和 3.3V 输出，RTC8563 提供定时与 I2C 接口。

- 参数与网络：`charger=U1 TP4057`；`rtc=U4 RTC8563`；`power_switches=Q1,Q3 LP3218DT1G,Q2 LN2324DT2AG`；`boost=U2 SY7088`；`buck=U3 SY8089`；`manual_wake=S1 SW-PB`
- 证据：图 b478d31c117e / 第 1 页 / 完整单页 A1-D4 充电、门控、RTC、输出转换与接口分区

## 核心器件

### U4 RTC8563 引脚

U4 pin 1 OSCI、2 OSCO、3 INT、4 VSS、5 SDA、6 SCL、7 CLKOUT、8 VDD；VDD 接 VBAT_IN，VSS 接 GND，INT 接唤醒网络，SCL/SDA 引出，CLKOUT 未连接。

- 参数与网络：`pinout=1:OSCI,2:OSCO,3:INT,4:VSS,5:SDA,6:SCL,7:CLKOUT,8:VDD`；`supply=VBAT_IN`；`ground=GND`；`clkout=unconnected`
- 证据：图 b478d31c117e / 第 1 页 / 页面 D2 U4 RTC8563 全部 pin 1-8 与网络

## 电源

### TP4057 电池充电路径

+5VIN 经 R13 0.8Ω 进入 U1 pin 4/VCC，U1 pin 3/BAT 输出 VBAT_IN，pin 6/PROG 经 R7 3.3KΩ 接 GND；C1 10uF 滤波 +5VIN，C7 10uF 滤波 VBAT_IN，CHRG/STDBY 未外接。

- 参数与网络：`input=+5VIN -> R13 0.8Ω -> U1 pin 4/VCC`；`battery=U1 pin 3/BAT -> VBAT_IN`；`program=pin 6/PROG -> R7 3.3KΩ -> GND`；`input_cap=C1 10uF`；`battery_cap=C7 10uF`；`status_pins=CHRG/STDBY unconnected`
- 证据：图 b478d31c117e / 第 1 页 / 页面 A1-B1 U1/R13/R7/C1/C7/+5VIN/VBAT_IN

### +5VIN 与电池到 +VIN 的电源路径

Q1 LP3218DT1G 串联在 VBAT_IN 与 +VIN 之间；D2 SS34 连接 +5VIN 与 +VIN，Q1 控制网络含 R12 100KΩ。该网络在外部 5V 与电池之间形成图示电源路径。

- 参数与网络：`battery_path=VBAT_IN -> Q1 LP3218DT1G -> +VIN`；`external_path=+5VIN -> D2 SS34 -> +VIN`；`gate_bias=R12 100KΩ`
- 证据：图 b478d31c117e / 第 1 页 / 页面 A1-A2 Q1/D2/R12/VBAT_IN/+5VIN/+VIN

### VBAT_OUT 唤醒与保持门控

Q3 LP3218DT1G 串联在 +VIN 与 VBAT_OUT；R6 100KΩ偏置其控制节点，RTC INT 经 D5、手动 WAKE 经 D6 汇入该节点，Q2 LN2324DT2AG 由 HOLD 控制并可拉低控制节点，R11 100KΩ将 HOLD 下拉。

- 参数与网络：`high_side_switch=Q3 LP3218DT1G`；`input=+VIN`；`output=VBAT_OUT`；`rtc_wake=INT -> D5 B5819WT`；`manual_wake=WAKE -> D6 B5819WT`；`hold_switch=HOLD -> Q2 LN2324DT2AG`；`hold_pulldown=R11 100KΩ`
- 证据：图 b478d31c117e / 第 1 页 / 页面 A2-C2 Q3/R6/D5/D6/Q2/R11 与 INT/WAKE/HOLD/VBAT_OUT

### U2 +5VOUT 升压

VBAT_OUT 经 R3 0Ω 进入 U2 SY7088，L1 3015 1.5uH 连接 LX，输出形成 +5VOUT；R1 150KΩ/R2 47KΩ 构成反馈，图中给出公式 Vout=1.2V×(R1/R2+1)。

- 参数与网络：`input=VBAT_OUT -> R3 0Ω`；`converter=U2 SY7088`；`inductor=L1 3015 1.5uH`；`output=+5VOUT`；`feedback=R1 150KΩ,R2 47KΩ`；`printed_formula=Vout=1.2V*(R1/R2+1)`
- 证据：图 b478d31c117e / 第 1 页 / 页面 A3-B4 上方虚线框 U2/R3/L1/R1/R2/+5VOUT 与公式

### U3 +3V3OUT 降压

VBAT_OUT 进入 U3 SY8089，EN 接 3V3EN，LX 经 L2 3015 4.7uH 输出 +3V3OUT；R9 68KΩ/R10 15KΩ 构成反馈，C10 22uF 与 C11 100nF 滤波输出。

- 参数与网络：`input=VBAT_OUT`；`converter=U3 SY8089`；`enable=3V3EN`；`inductor=L2 3015 4.7uH`；`output=+3V3OUT`；`feedback=R9 68KΩ,R10 15KΩ`；`output_caps=C10 22uF,C11 100nF`
- 证据：图 b478d31c117e / 第 1 页 / 页面 B3-C4 下方虚线框 U3/L2/R9/R10/C10/C11/+3V3OUT

## 接口

### J1 StampTimerPWR_Pin 针脚

J1 pin 1 +5VIN、2 GND、3 HOLD、4 WAKE、5 3V3EN、6 VBAT_IN、7 GND、8 GND、9 VBAT_OUT、10 +3V3OUT、11 GND、12 +5VOUT、13 SDA、14 SCL。

- 参数与网络：`pinout=1:+5VIN,2:GND,3:HOLD,4:WAKE,5:3V3EN,6:VBAT_IN,7:GND,8:GND,9:VBAT_OUT,10:+3V3OUT,11:GND,12:+5VOUT,13:SDA,14:SCL`
- 证据：图 b478d31c117e / 第 1 页 / 页面 D3 J1 StampTimerPWR_Pin pin 1-14

### J3 HY-2.0 I2C 接口

J3 HY-2.0_IIC pin 1 SCL、pin 2 SDA、pin 3 +5VOUT、pin 4 GND。

- 参数与网络：`pinout=1:IIC_SCL/SCL,2:IIC_SDA/SDA,3:VCC/+5VOUT,4:GND`
- 证据：图 b478d31c117e / 第 1 页 / 页面 D4 J3 HY-2.0_IIC pin 1-4

## 总线

### RTC I2C 总线

U4 pin 6/SCL 与 pin 5/SDA 连接 J1 pin 14/13，并同时连接 J3 pin 1/IIC_SCL 与 pin 2/IIC_SDA；原理图未绘出本板 I2C 上拉电阻。

- 参数与网络：`device=U4 RTC8563`；`scl=U4 pin 6 -> SCL -> J1 pin 14,J3 pin 1`；`sda=U4 pin 5 -> SDA -> J1 pin 13,J3 pin 2`；`pullups_visible=false`
- 证据：图 b478d31c117e / 第 1 页 / 页面 D2-D4 U4 SCL/SDA、J1 pin 13/14 与 J3 pin 1/2

## GPIO 与控制信号

### 手动 WAKE 按键

S1 SW-PB 将 WAKE 按下接 GND；D4 PESDNC2FD3V3B 将 WAKE 对 GND 提供 ESD 保护，WAKE 经 D6 B5819WT 连接电源门控节点。

- 参数与网络：`switch=S1 SW-PB`；`active_connection=WAKE -> GND`；`esd=D4 PESDNC2FD3V3B`；`gate_diode=D6 B5819WT`
- 证据：图 b478d31c117e / 第 1 页 / 页面 B2 S1/D4/D6/WAKE

### WAKE、HOLD 与 3V3EN 控制

WAKE 触发 Q3 唤醒门控，HOLD 驱动 Q2 维持 VBAT_OUT，3V3EN 连接 U3 EN 控制 +3V3OUT；三者均由 J1 引出。

- 参数与网络：`wake=J1 pin 4 -> WAKE -> D6/Q3 control`；`hold=J1 pin 3 -> HOLD -> Q2 gate`；`three3_enable=J1 pin 5 -> 3V3EN -> U3 EN`
- 证据：图 b478d31c117e / 第 1 页 / 页面 B2-C3 WAKE/HOLD/3V3EN 与 D3 J1 对应针脚

### VBAT_OUT 指示灯

VBAT_OUT 经 R4 1KΩ 与 D1 LED 串联到 GND，指示受控电池输出存在。

- 参数与网络：`path=VBAT_OUT -> R4 1KΩ -> D1 LED -> GND`
- 证据：图 b478d31c117e / 第 1 页 / 页面 A3-B3 R4/D1/VBAT_OUT

## 时钟

### RTC 32.768kHz 时钟

Y1 32.768KHz ±20ppm 12.5pF 连接 U4 pin 1/OSCI 与 pin 2/OSCO，C12、C13 各 6.0pF 分别从两端接 GND。

- 参数与网络：`rtc=U4 RTC8563`；`crystal=Y1 32.768KHz ±20ppm 12.5pF`；`osci=pin 1`；`osco=pin 2`；`load_caps=C12 6.0pF,C13 6.0pF`
- 证据：图 b478d31c117e / 第 1 页 / 页面 D1 Y1/C12/C13/OSCI/OSCO

## 保护电路

### 保护器件可见性

WAKE 配置 D4 PESDNC2FD3V3B ESD 保护，电源路径包含 D2 SS34 与 D5/D6 B5819WT；原理图未绘出输入保险丝、主电源 TVS、反接专用保护或电池温度监测。

- 参数与网络：`wake_esd=D4 PESDNC2FD3V3B`；`power_diode=D2 SS34`；`logic_diodes=D5,D6 B5819WT`；`fuse_visible=false`；`power_tvs_visible=false`；`battery_temperature_visible=false`
- 证据：图 b478d31c117e / 第 1 页 / 完整单页输入、充电、WAKE 与电池路径

## 内存与 Flash

### 存储器与内存可见性

原理图没有独立 Flash、EEPROM、RAM、SD 卡或其他存储器件；RTC 内部寄存器未展开。

- 参数与网络：`external_flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`；`rtc_registers_expanded=false`
- 证据：图 b478d31c117e / 第 1 页 / 完整单页全部器件，无存储位号

## 调试与烧录

### 复位、BOOT 与调试可见性

原理图没有 MCU、复位、BOOT、SWD/JTAG、UART 调试或专用调试连接器；控制由外部主机通过 GPIO 与 I2C 完成。

- 参数与网络：`mcu_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false`；`debug_uart_visible=false`
- 证据：图 b478d31c117e / 第 1 页 / 完整单页所有器件与接口

## 其他事实

### 其他功能分区可见性

原理图未绘出 SPI、UART、CAN、RS-485、USB、SDIO、MIPI、I2S、射频、音频、传感器或模拟采样链；核心功能为充电、电源门控、RTC 与 DC-DC。

- 参数与网络：`spi_visible=false`；`uart_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false`
- 证据：图 b478d31c117e / 第 1 页 / 完整单页功能分区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp Timer Power 系统架构 | `charger=U1 TP4057`；`rtc=U4 RTC8563`；`power_switches=Q1,Q3 LP3218DT1G,Q2 LN2324DT2AG`；`boost=U2 SY7088`；`buck=U3 SY8089`；`manual_wake=S1 SW-PB` |
| 电源 | TP4057 电池充电路径 | `input=+5VIN -> R13 0.8Ω -> U1 pin 4/VCC`；`battery=U1 pin 3/BAT -> VBAT_IN`；`program=pin 6/PROG -> R7 3.3KΩ -> GND`；`input_cap=C1 10uF`；`battery_cap=C7 10uF`；`status_pins=CHRG/STDBY unconnected` |
| 电源 | +5VIN 与电池到 +VIN 的电源路径 | `battery_path=VBAT_IN -> Q1 LP3218DT1G -> +VIN`；`external_path=+5VIN -> D2 SS34 -> +VIN`；`gate_bias=R12 100KΩ` |
| 电源 | VBAT_OUT 唤醒与保持门控 | `high_side_switch=Q3 LP3218DT1G`；`input=+VIN`；`output=VBAT_OUT`；`rtc_wake=INT -> D5 B5819WT`；`manual_wake=WAKE -> D6 B5819WT`；`hold_switch=HOLD -> Q2 LN2324DT2AG`；`hold_pulldown=R11 100KΩ` |
| GPIO 与控制信号 | 手动 WAKE 按键 | `switch=S1 SW-PB`；`active_connection=WAKE -> GND`；`esd=D4 PESDNC2FD3V3B`；`gate_diode=D6 B5819WT` |
| 电源 | U2 +5VOUT 升压 | `input=VBAT_OUT -> R3 0Ω`；`converter=U2 SY7088`；`inductor=L1 3015 1.5uH`；`output=+5VOUT`；`feedback=R1 150KΩ,R2 47KΩ`；`printed_formula=Vout=1.2V*(R1/R2+1)` |
| 电源 | U3 +3V3OUT 降压 | `input=VBAT_OUT`；`converter=U3 SY8089`；`enable=3V3EN`；`inductor=L2 3015 4.7uH`；`output=+3V3OUT`；`feedback=R9 68KΩ,R10 15KΩ`；`output_caps=C10 22uF,C11 100nF` |
| 时钟 | RTC 32.768kHz 时钟 | `rtc=U4 RTC8563`；`crystal=Y1 32.768KHz ±20ppm 12.5pF`；`osci=pin 1`；`osco=pin 2`；`load_caps=C12 6.0pF,C13 6.0pF` |
| 核心器件 | U4 RTC8563 引脚 | `pinout=1:OSCI,2:OSCO,3:INT,4:VSS,5:SDA,6:SCL,7:CLKOUT,8:VDD`；`supply=VBAT_IN`；`ground=GND`；`clkout=unconnected` |
| 核心器件 | RTC 型号一致性 | `schematic_part_number=RTC8563`；`documented_part_number=BM8563`；`same_part_confirmed=false` |
| 总线 | RTC I2C 总线 | `device=U4 RTC8563`；`scl=U4 pin 6 -> SCL -> J1 pin 14,J3 pin 1`；`sda=U4 pin 5 -> SDA -> J1 pin 13,J3 pin 2`；`pullups_visible=false` |
| 总线地址 | RTC I2C 地址 | `documented_7bit=0x51`；`documented_write=0xA2`；`documented_read=0xA3`；`schematic_address_visible=false` |
| 接口 | J1 StampTimerPWR_Pin 针脚 | `pinout=1:+5VIN,2:GND,3:HOLD,4:WAKE,5:3V3EN,6:VBAT_IN,7:GND,8:GND,9:VBAT_OUT,10:+3V3OUT,11:GND,12:+5VOUT,13:SDA,14:SCL` |
| 接口 | J3 HY-2.0 I2C 接口 | `pinout=1:IIC_SCL/SCL,2:IIC_SDA/SDA,3:VCC/+5VOUT,4:GND` |
| GPIO 与控制信号 | WAKE、HOLD 与 3V3EN 控制 | `wake=J1 pin 4 -> WAKE -> D6/Q3 control`；`hold=J1 pin 3 -> HOLD -> Q2 gate`；`three3_enable=J1 pin 5 -> 3V3EN -> U3 EN` |
| GPIO 与控制信号 | VBAT_OUT 指示灯 | `path=VBAT_OUT -> R4 1KΩ -> D1 LED -> GND` |
| 保护电路 | 保护器件可见性 | `wake_esd=D4 PESDNC2FD3V3B`；`power_diode=D2 SS34`；`logic_diodes=D5,D6 B5819WT`；`fuse_visible=false`；`power_tvs_visible=false`；`battery_temperature_visible=false` |
| 调试与烧录 | 复位、BOOT 与调试可见性 | `mcu_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false`；`debug_uart_visible=false` |
| 内存与 Flash | 存储器与内存可见性 | `external_flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`；`rtc_registers_expanded=false` |
| 其他事实 | 其他功能分区可见性 | `spi_visible=false`；`uart_visible=false`；`can_visible=false`；`rs485_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false` |

## 待确认事项

- `component.rtc-model-discrepancy`：正式原理图将 U4 标为 RTC8563，而产品正文将 RTC 写为 BM8563；本页没有 BM8563 料号。（证据：图 b478d31c117e / 第 1 页 / 页面 D2 U4 器件值 RTC8563）
- `address.documented-rtc`：产品正文记载默认 7 位地址 0x51，并列出 0xA2 写、0xA3 读；原理图没有打印这些地址或地址配置。（证据：图 b478d31c117e / 第 1 页 / 页面 U4 RTC8563 与 SCL/SDA 网络，无十六进制地址）
- `review.rtc-model`：Stamp Timer Power v1.2 的 RTC 正式物料是原理图标注的 RTC8563，还是产品正文所述 BM8563？；原因：当前正式原理图与产品正文的芯片型号不同，不能在无 BOM 证据下视为同一料号。
- `review.rtc-address`：当前 RTC 物料的 I2C 地址是否确认为 0x51（7 位）/0xA2 写/0xA3 读？；原因：地址来自产品正文，原理图未打印地址，且 RTC 型号存在 RTC8563/BM8563 差异。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `b478d31c117e3510ddaa1c489623d9daffcbabd63fe62c17d89b5b44998abaed` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/571/Sch_StampTimerPower_v1.2_sch_01.png` |

---

源文档：`zh_CN/module/StampTimerPower.md`

源文档 SHA-256：`e7e3f67d4b28bb5b6c747048e7aaf5e54c1aaa3b3a74b8c2aa2ac4b4d9113bc2`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
