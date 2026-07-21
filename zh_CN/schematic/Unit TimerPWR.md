# Unit TimerPWR 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit TimerPWR |
| SKU | U189 |
| 产品 ID | `unit-timerpwr-2ec0fb97a5f8` |
| 源文档 | `zh_CN/unit/Unit-TimerPWR.md` |

## 概述

Unit TimerPWR 以 U6 STM32G031G8U6 为主控，分别通过 PA_SCL/PA_SDA 对外提供 Grove I2C，通过 SCL2/SDA2 连接 U2 INA3221，并以 SPI 和控制线驱动 FPC1 OLED。USB1 的 VUSB 经 U8 LGS4056H 接入 VBAT_OUT 充电节点，P1 外接电池经 Q1 和 R4 进入同一节点；U5 MT9700 形成受 PWR_HOLD 控制的 VBAT，再由 U4 SY7088 升压到 5V_OUT。U7 ME6206A33XG 产生 RTC_3V3，U3 AW35122FDR 受 SYS_3V3_EN 控制产生 SYS_3V3，U9 与 U1 形成 OLED 的 BL_VBAT 和 9V 电源路径。板上还包括 32.768kHz 晶振、两枚按键、SWD 接口、三路电流采样和 Grove 5V 输出监测。

## 检索关键词

`Unit TimerPWR`、`U189`、`STM32G031G8U6`、`LGS4056H`、`INA3221`、`MT9700`、`SY7088`、`ME6206A33XG`、`AW35122FDR`、`TPS61040DBVR`、`TYPE-C 6P`、`GROVE`、`PA_SCL`、`PA_SDA`、`SCL2`、`SDA2`、`0x56`、`VBAT_OUT`、`VBAT`、`RTC_3V3`、`SYS_3V3`、`SYS_3V3_EN`、`5V_OUT`、`GROVE_5V`、`PWR_HOLD`、`BAT_CHRG`、`BL_EN`、`BL_VBAT`、`32.768KHz`、`MCU_SWCLK`、`MCU_SWDIO`、`BTN_A`、`BTN_B`、`CH1P`、`CH1N`、`CH2P`、`CH2N`、`CH3P`、`CH3N`、`OLED SPI`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U6 | STM32G031G8U6 | 主控 MCU，连接 Grove I2C、INA3221 I2C、OLED、按键、电源保持、充电状态与 SWD | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C2-D2，U6 STM32G031G8U6 pin1-pin28 |
| USB1 | TYPE-C 6P | 5V USB-C 电源输入连接器，VBUS 经 FUSE1 输出 VUSB，CC1/CC2 各有 5.1KΩ 下拉 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A1，USB1 TYPE-C 6P 的 VBUS/CC1/CC2/GND/SHELL |
| FUSE1 | 6V/2A | USB1 VBUS 至 VUSB 的串联输入保险丝 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A1，USB1 VBUS 与 VUSB 之间的 FUSE1 6V/2A |
| U8 | LGS4056H | VUSB 至 VBAT_OUT 的单节电池充电器，提供 BAT_CHRG 状态 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A2，U8 LGS4056H，TEMP/PROG/VCC/CE/CHRG/DONE/BAT |
| P1 | 未标注 | 外接电池连接器，正极经 Q1/R4 接入 VBAT_OUT，负极接 GND | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B1，P1 pin1 至 Q1，pin2 至 GND，另有机械焊盘 3/4 |
| Q1 | LP3218DT1G | P1 电池正极至 CH3P/R4/VBAT_OUT 路径的串联 MOSFET | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B1，Q1 LP3218DT1G 与 P1、CH3P、R4 |
| U5 | MT9700 | 受 PWR_HOLD 控制的 VBAT_OUT 至 VBAT 负载开关/限流器件 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B2，U5 MT9700 的 VIN/EN/OUT/SET/GND |
| U4 | SY7088 | 将 VBAT 升压为 5V_OUT 的 DC-DC 转换器 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B3，U4 SY7088、L2、R5/R13 与 5V_OUT |
| U2 | INA3221 | 监测 Grove 5V、USB 充电输入和外接电池三路分流电阻压差的 I2C 电流/电压监测器 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A3，U2 INA3221 的 IN1±/IN2±/IN3±、SCL/SDA/A0/VS/VPU |
| U7 | ME6206A33XG | 由 VBAT_OUT 生成 RTC_3V3 的 3.3V LDO | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A4，U7 ME6206A33XG，VIN=VBAT_OUT、VOUT=RTC_3V3 |
| U3 | AW35122FDR | 由 SYS_3V3_EN 控制、将 RTC_3V3 切换为 SYS_3V3 的负载开关 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A4，U3 AW35122FDR 的 IN/OUT/EN/GND |
| U9 | AW35122FDR | 由 BL_EN 控制、将 VBAT_OUT 切换为 BL_VBAT 的 OLED 电源负载开关 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C3，U9 AW35122FDR 的 IN=VBAT_OUT、OUT=BL_VBAT、EN=BL_EN |
| U1 | TPS61040DBVR | 由 BL_VBAT 升压生成 OLED 使用的 9V 电源 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C3-D3，U1 TPS61040DBVR、L1、D1、R1/R2 与 9V |
| FPC1 | 未标注 | OLED 显示屏 FPC，连接 9V、SYS_3V3、SPI/控制线和内部电荷泵电容 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C4-D4，FPC1 的 VLSS/VCC/VCOM/IREF/SDIN/SCLK/D-C#/RES#/CS#/VDD/VBAT/C1P-C2N |
| J1 | GROVE | 四线 Grove 接口，提供 PA_SCL、PA_SDA、GROVE_5V 和 GND | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B4，J1 GROVE，IO2/IO1/5V/GND |
| J4 | SWD_5P | MCU 调试接口，提供 RTC_3V3、MCU_SWCLK、MCU_SWDIO、NRST 和 GND | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 D1，J4 SWD_5P 五针网络 |
| S1,S2 | 未标注 | BTN_A 和 BTN_B 两枚低有效用户按键 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C1，S1 BTN_A、S2 BTN_B 与 R8/R24 |
| Y1 | 32.768KHz | STM32G031 PC14/PC15 的低速外部晶振 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C1-C2，Y1 32.768KHz 与 C24/C15 10pF |
| D3 | 未标注 | 5V_OUT 对地的钳位/浪涌保护器件，原理图未标具体型号 | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B3，5V_OUT 至 GND 的 D3 瞬态抑制符号 |
| D4 | 未标注 | 5V_OUT 电源指示 LED，串联 R6 3.4KΩ | 图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B3-B4，5V_OUT、R6 3.4KΩ、D4、GND |

## 系统结构

### Unit TimerPWR 系统架构

U6 STM32G031G8U6 控制 Grove I2C、U2 INA3221、FPC1 OLED、两枚按键和电源使能；USB1/U8 与 P1/Q1 汇入 VBAT_OUT，U5 产生受控 VBAT，U4 产生 5V_OUT，U7/U3 形成 RTC_3V3 与 SYS_3V3，U9/U1 形成 OLED 的 BL_VBAT 与 9V 电源。

- 参数与网络：`controller=U6 STM32G031G8U6`；`monitor=U2 INA3221`；`charger=U8 LGS4056H`；`power_path=VBAT_OUT -> U5 MT9700 -> VBAT -> U4 SY7088 -> 5V_OUT`；`logic_rails=RTC_3V3,SYS_3V3`；`display=FPC1 OLED`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页完整 A1-D4 原理图

### 独立协处理器、存储、射频和音频

本页除 U6 MCU、U2 监测器及电源器件外，未画出独立协处理器、外部存储器、射频电路、音频器件或其他传感器。

- 参数与网络：`coprocessor=null`；`external_storage=null`；`rf=null`；`audio=null`；`other_sensor=null`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页完整 A1-D4 原理图，唯一原理图页面

## 电源

### VUSB 至 VBAT_OUT 充电路径

VUSB 经 R25 0.05Ω 的 CH2P/CH2N 分流节点进入 U8 LGS4056H VCC，U8 BAT pin5 连接 VBAT_OUT，CHRG pin7 输出 BAT_CHRG；R21 3KΩ 接在 PROG 路径，C14/C19 各 10uF 分别位于输入和 VBAT_OUT 侧。

- 参数与网络：`input=VUSB`；`shunt=R25 0.05Ω, CH2P/CH2N`；`charger=U8 LGS4056H`；`battery_node=BAT pin5 -> VBAT_OUT`；`status=CHRG pin7 -> BAT_CHRG`；`program_resistor=R21 3KΩ`；`caps=C14/C19 10uF`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A2，R25/CH2P/CH2N、U8、R21、C14/C19

### P1 外接电池输入

P1 pin1 经 Q1 LP3218DT1G 形成 CH3P，再经 R4 0.05Ω 形成 CH3N/VBAT_OUT；P1 pin2 接 GND。该路径同时为 INA3221 第 3 通道提供分流压差。

- 参数与网络：`connector=P1`；`positive=pin1 -> Q1 -> CH3P -> R4 0.05Ω -> CH3N/VBAT_OUT`；`negative=pin2 GND`；`mosfet=Q1 LP3218DT1G`；`monitor_channel=INA3221 channel 3`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B1，P1、Q1、CH3P、R4、CH3N、VBAT_OUT

### PWR_HOLD 受控 VBAT 电源

VBAT_OUT 接 U5 MT9700 VIN pin5，PWR_HOLD 接 EN pin4 并由 R11 10KΩ 下拉；OUT pin1 输出 VBAT，SET pin3 经 R10 3.4KΩ 接 GND，输入和输出分别由 C11/C12 10uF 去耦。

- 参数与网络：`input=VBAT_OUT`；`switch=U5 MT9700`；`enable=PWR_HOLD -> EN pin4`；`enable_pulldown=R11 10KΩ`；`output=VBAT`；`set=R10 3.4KΩ`；`caps=C11/C12 10uF`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B2，U5、R10/R11、C11/C12

### VBAT 至 5V_OUT 升压

VBAT 同时接 U4 SY7088 IN pin6 并经 L2 2.2uH 接 LX pins1/2；EN pin3 由 R9 100KΩ 上拉到 VBAT。OUT pins7/8 输出 5V_OUT，R5 15KΩ 与 R13 4.7KΩ构成反馈分压，C16/C27 各 22uF/10V 对地，D3 从 5V_OUT 接 GND。

- 参数与网络：`input=VBAT`；`converter=U4 SY7088`；`inductor=L2 2.2uH/301`；`enable=EN via R9 100KΩ to VBAT`；`output=5V_OUT`；`feedback=R5 15KΩ,R13 4.7KΩ`；`output_caps=C16/C27 22uF/10V`；`protection=D3 to GND`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B3，L2、U4、R5/R9/R13、C16/C27、D3

### RTC_3V3 常供电轨

VBAT_OUT 接 U7 ME6206A33XG VIN pin3，VOUT pin2 输出 RTC_3V3，GND pin1 接地；C23/C25 各 10uF，C26 100nF。RTC_3V3 为 U6 VDD/VDDA、按键上拉、NRST 上拉和 J4 VCC 供电。

- 参数与网络：`input=VBAT_OUT`；`ldo=U7 ME6206A33XG`；`output=RTC_3V3`；`caps=C23/C25 10uF,C26 100nF`；`loads=U6 VDD/VDDA,R8/R24,R12,J4 VCC`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A4 的 U7；网格 C1-D2 的 RTC_3V3 同名网络

### SYS_3V3 受控电源轨

U3 AW35122FDR 的 IN A2 接 RTC_3V3，EN B2 接 SYS_3V3_EN，OUT A1 输出 SYS_3V3，GND B1 接地；C10 10uF 与 C6 100nF 位于输出端。SYS_3V3 为 U2 INA3221、Grove I2C 上拉和 FPC1 逻辑电源供电。

- 参数与网络：`input=RTC_3V3`；`switch=U3 AW35122FDR`；`enable=SYS_3V3_EN`；`output=SYS_3V3`；`caps=C10 10uF,C6 100nF`；`loads=U2 VS,R16/R17,FPC1 VDD/VBAT`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A4，U3/C10/C6；SYS_3V3 同名网络连接 U2、J1 上拉与 FPC1

### OLED BL_VBAT 与 9V 电源

U9 AW35122FDR 由 BL_EN 控制，将 VBAT_OUT 切换为 BL_VBAT；BL_VBAT 同时接 U1 TPS61040DBVR IN/EN，并经 L1 10uH 接 SW。SW 经 D1 1N4148WS T4 输出 9V，FB 使用 R2 1MΩ 与 R1 160KΩ，C1 22pF 跨接反馈上臂，C2 4.7uF/16V 对地。

- 参数与网络：`switch=U9 AW35122FDR`；`switch_input=VBAT_OUT`；`enable=BL_EN`；`intermediate=BL_VBAT`；`boost=U1 TPS61040DBVR`；`inductor=L1 10uH`；`diode=D1 1N4148WS T4`；`output=9V`；`feedback=R2 1MΩ,R1 160KΩ,C1 22pF`；`output_cap=C2 4.7uF/16V`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C3-D3，U9、U1、L1、D1、R1/R2、C1/C2

### FPC1 OLED 电源与电荷泵连接

FPC1 VCC 接 9V，VDD 与 VBAT 接 SYS_3V3，VLSS/VSS/BS1/BS2 接 GND；IREF 经 R3 390KΩ 接 GND，VCOM 由 C3 4.7uF/16V 对地，C1P/C1N 与 C2P/C2N 分别跨接 C5/C4 1uF。

- 参数与网络：`panel_high_voltage=VCC 9V`；`logic_supply=VDD/VBAT SYS_3V3`；`grounds=VLSS,VSS,BS1,BS2 GND`；`iref=R3 390KΩ to GND`；`vcom_cap=C3 4.7uF/16V`；`charge_pump_caps=C5 1uF across C1P/C1N; C4 1uF across C2P/C2N`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C4-D4，FPC1 电源、偏置与 C3/C4/C5/R3

## 接口

### USB1 Type-C 电源输入

USB1 的 A9/B9 VBUS 并联后经 FUSE1 6V/2A 输出 VUSB；A5 CC2 经 R15 5.1KΩ、B5 CC1 经 R14 5.1KΩ 下拉到 GND，A12/B12 GND 与 SHELL 接 GND。图中未画 USB 数据引脚或数据网络。

- 参数与网络：`connector=USB1 TYPE-C 6P`；`power_pins=A9/B9 VBUS`；`output=VUSB via FUSE1 6V/2A`；`cc1=B5 via R14 5.1KΩ to GND`；`cc2=A5 via R15 5.1KΩ to GND`；`data=null`；`direction=5V power input`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A1，USB1、FUSE1、R14、R15

### J1 Grove 接口

J1 GROVE 的 IO2 接 PA_SCL、IO1 接 PA_SDA、5V 接 GROVE_5V、GND 接 GND。PA_SCL/PA_SDA 是 3.3V 上拉的双向 I2C 信号，GROVE_5V 是经 R23 0.05Ω 监测后的 5V_OUT 输出。

- 参数与网络：`connector=J1 GROVE`；`io2=PA_SCL, bidirectional I2C clock`；`io1=PA_SDA, bidirectional I2C data`；`power=GROVE_5V from 5V_OUT via R23 0.05Ω`；`ground=GND`；`logic_level=SYS_3V3 pull-up`；`power_direction=output`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B4，J1、R16/R17、R23、PA_SCL/PA_SDA/GROVE_5V

## 总线

### U6 至 INA3221 的 I2C2 总线

U6 PA11 pin18 接 SCL2，PA12 pin19 接 SDA2；U2 SCL pin6/SDA pin7 接同名网络，R7/R19 各 10KΩ 将 SDA2/SCL2 上拉至 SYS_3V3。U2 VS pin4 接 SYS_3V3，A0 pin5 接 GND。

- 参数与网络：`controller=U6 STM32G031G8U6`；`scl=PA11 pin18 -> SCL2 -> U2 pin6`；`sda=PA12 pin19 -> SDA2 -> U2 pin7`；`pullups=R19/R7 10KΩ to SYS_3V3`；`device=U2 INA3221`；`address_strap=A0 pin5 GND`；`logic_level=SYS_3V3`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A3 的 U2/SCL2/SDA2/R7/R19 与网格 C2-D2 的 U6 PA11/PA12

### U6 至 Grove 的 I2C 总线

U6 PB6 pin26 接 PA_SCL，PB7 pin27 接 PA_SDA；R16/R17 各 10KΩ 将两线拉至 SYS_3V3，随后接 J1 IO2/IO1。

- 参数与网络：`controller=U6 STM32G031G8U6`；`scl=PB6 pin26 -> PA_SCL -> J1 IO2`；`sda=PB7 pin27 -> PA_SDA -> J1 IO1`；`pullups=R16/R17 10KΩ to SYS_3V3`；`logic_level=SYS_3V3`；`direction=bidirectional`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 B4 的 J1/R16/R17 与网格 C2-D2 的 U6 PB6/PB7

### FPC1 OLED SPI 与控制连接

U6 PA2 pin8 的 MOSI 接 FPC1 SDIN pin15，PA1 pin7 的 SCK 接 SCLK pin14，PA6 pin12 的 DC 接 D/C# pin13，PA7 pin13 的 RES 接 RES# pin12，PB0 pin14 的 CS 接 CS# pin11。

- 参数与网络：`controller=U6 STM32G031G8U6`；`mosi=PA2 pin8 -> MOSI -> FPC1 SDIN pin15`；`clock=PA1 pin7 -> SCK -> FPC1 SCLK pin14`；`data_command=PA6 pin12 -> DC -> FPC1 D/C# pin13`；`reset=PA7 pin13 -> RES -> FPC1 RES# pin12`；`chip_select=PB0 pin14 -> CS -> FPC1 CS# pin11`；`miso=null`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 D2 的 U6 PA1/PA2/PA6/PA7/PB0 与网格 C4-D4 的 FPC1 pins11-15

## GPIO 与控制信号

### STM32G031 控制与状态网络映射

U6 PA3 pin9 驱动 SYS_3V3_EN，PB5 pin25 驱动 PWR_HOLD，PB4 pin24 接 BAT_CHRG，PB1 pin15 驱动 BL_EN；PA0 pin6 接 BTN_A，PA4 pin10 接 BTN_B。

- 参数与网络：`PA3_pin9=SYS_3V3_EN output`；`PB5_pin25=PWR_HOLD output`；`PB4_pin24=BAT_CHRG input`；`PB1_pin15=BL_EN output`；`PA0_pin6=BTN_A input`；`PA4_pin10=BTN_B input`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C2-D2，U6 pins6/9/10/15/24/25 网络标注

### BTN_A 与 BTN_B 按键

BTN_A 由 R8 10KΩ 上拉至 RTC_3V3，按下 S1 接 GND并连接 U6 PA0；BTN_B 由 R24 10KΩ 上拉至 RTC_3V3，按下 S2 接 GND并连接 U6 PA4。两路均为低有效输入。

- 参数与网络：`button_a=S1 BTN_A -> U6 PA0 pin6`；`button_b=S2 BTN_B -> U6 PA4 pin10`；`pullups=R8/R24 10KΩ to RTC_3V3`；`active_level=low`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C1 的 S1/S2/R8/R24 与 U6 PA0/PA4

## 时钟

### STM32 32.768kHz 外部时钟

U6 PC14-OSC32IN pin1 与 PC15-OSC32OUT pin2 连接 Y1 32.768KHz 晶振，两端分别经 C24/C15 10pF 接 GND。原理图未画出其他外部 MCU 晶振。

- 参数与网络：`controller=U6 STM32G031G8U6`；`pins=PC14-OSC32IN pin1,PC15-OSC32OUT pin2`；`crystal=Y1 32.768KHz`；`load_caps=C24/C15 10pF`；`other_external_clock=null`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C1-C2，Y1/C24/C15 与 U6 pins1/2

## 复位

### STM32 NRST 网络

U6 PF2-NRST pin5 接 NRST；R12 10KΩ 将 NRST 上拉到 RTC_3V3，C20 100nF 将 NRST 接 GND，J4 同时引出 NRST。

- 参数与网络：`controller_pin=U6 PF2-NRST pin5`；`network=NRST`；`pullup=R12 10KΩ to RTC_3V3`；`capacitor=C20 100nF to GND`；`debug_header=J4 NRST`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 D1-D2，R12/C20/NRST、U6 pin5 与 J4

## 保护电路

### 输入与 5V 输出保护

USB1 VBUS 串联 FUSE1 6V/2A；5V_OUT 通过 D3 对地钳位。USB Type-C 的 CC1/CC2 具有 5.1KΩ 下拉，但图中未画专用 USB ESD 阵列、反接保护 IC 或电池保护 IC。

- 参数与网络：`input_fuse=FUSE1 6V/2A`；`output_clamp=D3 from 5V_OUT to GND`；`cc_resistors=R14/R15 5.1KΩ`；`usb_esd=null`；`battery_protection_ic=null`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A1 的 USB1/FUSE1/R14/R15 与网格 B3 的 D3

## 关键网络

### BAT_CHRG 充电状态

U8 LGS4056H CHRG pin7 输出 BAT_CHRG，连接 U6 PB4 pin24；因此 BAT_CHRG 是从充电器到 MCU 的状态输入网络。D4 则是由 5V_OUT 经 R6 3.4KΩ 单独驱动的电源指示 LED。

- 参数与网络：`charger_output=U8 CHRG pin7`；`network=BAT_CHRG`；`mcu_input=U6 PB4 pin24`；`power_led=5V_OUT -> R6 3.4KΩ -> D4 -> GND`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A2 的 U8 BAT_CHRG、网格 C2-D2 的 U6 PB4、网格 B3-B4 的 D4

## 调试与烧录

### J4 SWD 调试接口

J4 SWD_5P 依次引出 RTC_3V3、MCU_SWCLK、MCU_SWDIO、NRST 和 GND；MCU_SWCLK 连接 U6 PA14-BOOT0 pin21，MCU_SWDIO 连接 U6 PA13 pin20。

- 参数与网络：`header=J4 SWD_5P`；`vcc=RTC_3V3`；`swclk=MCU_SWCLK -> U6 PA14-BOOT0 pin21`；`swdio=MCU_SWDIO -> U6 PA13 pin20`；`reset=NRST`；`ground=GND`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 D1 的 J4 与网格 C2-D2 的 U6 PA13/PA14

## 模拟电路

### INA3221 三路分流采样

U2 INA3221 的 IN1+ pin12/IN1- pin11 接 CH1P/CH1N，跨 R23 0.05Ω 监测 5V_OUT 至 GROVE_5V；IN2+ pin15/IN2- pin14 接 CH2P/CH2N，跨 R25 0.05Ω 监测 VUSB 至充电器输入；IN3+ pin2/IN3- pin1 接 CH3P/CH3N，跨 R4 0.05Ω 监测 P1 电池路径。

- 参数与网络：`channel1=IN1+ CH1P, IN1- CH1N, R23 0.05Ω, 5V_OUT/GROVE_5V`；`channel2=IN2+ CH2P, IN2- CH2N, R25 0.05Ω, VUSB/charger`；`channel3=IN3+ CH3P, IN3- CH3N, R4 0.05Ω, P1/VBAT_OUT`；`device=U2 INA3221`
- 证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页 U2 IN1±/IN2±/IN3± 与网格 A2/B1/B4 的 R25/R4/R23 同名 CH1-CH3 网络

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit TimerPWR 系统架构 | `controller=U6 STM32G031G8U6`；`monitor=U2 INA3221`；`charger=U8 LGS4056H`；`power_path=VBAT_OUT -> U5 MT9700 -> VBAT -> U4 SY7088 -> 5V_OUT`；`logic_rails=RTC_3V3,SYS_3V3`；`display=FPC1 OLED` |
| 系统结构 | 独立协处理器、存储、射频和音频 | `coprocessor=null`；`external_storage=null`；`rf=null`；`audio=null`；`other_sensor=null` |
| 接口 | USB1 Type-C 电源输入 | `connector=USB1 TYPE-C 6P`；`power_pins=A9/B9 VBUS`；`output=VUSB via FUSE1 6V/2A`；`cc1=B5 via R14 5.1KΩ to GND`；`cc2=A5 via R15 5.1KΩ to GND`；`data=null`；`direction=5V power input` |
| 电源 | VUSB 至 VBAT_OUT 充电路径 | `input=VUSB`；`shunt=R25 0.05Ω, CH2P/CH2N`；`charger=U8 LGS4056H`；`battery_node=BAT pin5 -> VBAT_OUT`；`status=CHRG pin7 -> BAT_CHRG`；`program_resistor=R21 3KΩ`；`caps=C14/C19 10uF` |
| 电源 | P1 外接电池输入 | `connector=P1`；`positive=pin1 -> Q1 -> CH3P -> R4 0.05Ω -> CH3N/VBAT_OUT`；`negative=pin2 GND`；`mosfet=Q1 LP3218DT1G`；`monitor_channel=INA3221 channel 3` |
| 电源 | PWR_HOLD 受控 VBAT 电源 | `input=VBAT_OUT`；`switch=U5 MT9700`；`enable=PWR_HOLD -> EN pin4`；`enable_pulldown=R11 10KΩ`；`output=VBAT`；`set=R10 3.4KΩ`；`caps=C11/C12 10uF` |
| 电源 | VBAT 至 5V_OUT 升压 | `input=VBAT`；`converter=U4 SY7088`；`inductor=L2 2.2uH/301`；`enable=EN via R9 100KΩ to VBAT`；`output=5V_OUT`；`feedback=R5 15KΩ,R13 4.7KΩ`；`output_caps=C16/C27 22uF/10V`；`protection=D3 to GND` |
| 电源 | RTC_3V3 常供电轨 | `input=VBAT_OUT`；`ldo=U7 ME6206A33XG`；`output=RTC_3V3`；`caps=C23/C25 10uF,C26 100nF`；`loads=U6 VDD/VDDA,R8/R24,R12,J4 VCC` |
| 电源 | SYS_3V3 受控电源轨 | `input=RTC_3V3`；`switch=U3 AW35122FDR`；`enable=SYS_3V3_EN`；`output=SYS_3V3`；`caps=C10 10uF,C6 100nF`；`loads=U2 VS,R16/R17,FPC1 VDD/VBAT` |
| 电源 | OLED BL_VBAT 与 9V 电源 | `switch=U9 AW35122FDR`；`switch_input=VBAT_OUT`；`enable=BL_EN`；`intermediate=BL_VBAT`；`boost=U1 TPS61040DBVR`；`inductor=L1 10uH`；`diode=D1 1N4148WS T4`；`output=9V`；`feedback=R2 1MΩ,R1 160KΩ,C1 22pF`；`output_cap=C2 4.7uF/16V` |
| 模拟电路 | INA3221 三路分流采样 | `channel1=IN1+ CH1P, IN1- CH1N, R23 0.05Ω, 5V_OUT/GROVE_5V`；`channel2=IN2+ CH2P, IN2- CH2N, R25 0.05Ω, VUSB/charger`；`channel3=IN3+ CH3P, IN3- CH3N, R4 0.05Ω, P1/VBAT_OUT`；`device=U2 INA3221` |
| 总线 | U6 至 INA3221 的 I2C2 总线 | `controller=U6 STM32G031G8U6`；`scl=PA11 pin18 -> SCL2 -> U2 pin6`；`sda=PA12 pin19 -> SDA2 -> U2 pin7`；`pullups=R19/R7 10KΩ to SYS_3V3`；`device=U2 INA3221`；`address_strap=A0 pin5 GND`；`logic_level=SYS_3V3` |
| 接口 | J1 Grove 接口 | `connector=J1 GROVE`；`io2=PA_SCL, bidirectional I2C clock`；`io1=PA_SDA, bidirectional I2C data`；`power=GROVE_5V from 5V_OUT via R23 0.05Ω`；`ground=GND`；`logic_level=SYS_3V3 pull-up`；`power_direction=output` |
| 总线 | U6 至 Grove 的 I2C 总线 | `controller=U6 STM32G031G8U6`；`scl=PB6 pin26 -> PA_SCL -> J1 IO2`；`sda=PB7 pin27 -> PA_SDA -> J1 IO1`；`pullups=R16/R17 10KΩ to SYS_3V3`；`logic_level=SYS_3V3`；`direction=bidirectional` |
| GPIO 与控制信号 | STM32G031 控制与状态网络映射 | `PA3_pin9=SYS_3V3_EN output`；`PB5_pin25=PWR_HOLD output`；`PB4_pin24=BAT_CHRG input`；`PB1_pin15=BL_EN output`；`PA0_pin6=BTN_A input`；`PA4_pin10=BTN_B input` |
| GPIO 与控制信号 | BTN_A 与 BTN_B 按键 | `button_a=S1 BTN_A -> U6 PA0 pin6`；`button_b=S2 BTN_B -> U6 PA4 pin10`；`pullups=R8/R24 10KΩ to RTC_3V3`；`active_level=low` |
| 总线 | FPC1 OLED SPI 与控制连接 | `controller=U6 STM32G031G8U6`；`mosi=PA2 pin8 -> MOSI -> FPC1 SDIN pin15`；`clock=PA1 pin7 -> SCK -> FPC1 SCLK pin14`；`data_command=PA6 pin12 -> DC -> FPC1 D/C# pin13`；`reset=PA7 pin13 -> RES -> FPC1 RES# pin12`；`chip_select=PB0 pin14 -> CS -> FPC1 CS# pin11`；`miso=null` |
| 电源 | FPC1 OLED 电源与电荷泵连接 | `panel_high_voltage=VCC 9V`；`logic_supply=VDD/VBAT SYS_3V3`；`grounds=VLSS,VSS,BS1,BS2 GND`；`iref=R3 390KΩ to GND`；`vcom_cap=C3 4.7uF/16V`；`charge_pump_caps=C5 1uF across C1P/C1N; C4 1uF across C2P/C2N` |
| 时钟 | STM32 32.768kHz 外部时钟 | `controller=U6 STM32G031G8U6`；`pins=PC14-OSC32IN pin1,PC15-OSC32OUT pin2`；`crystal=Y1 32.768KHz`；`load_caps=C24/C15 10pF`；`other_external_clock=null` |
| 复位 | STM32 NRST 网络 | `controller_pin=U6 PF2-NRST pin5`；`network=NRST`；`pullup=R12 10KΩ to RTC_3V3`；`capacitor=C20 100nF to GND`；`debug_header=J4 NRST` |
| 调试与烧录 | J4 SWD 调试接口 | `header=J4 SWD_5P`；`vcc=RTC_3V3`；`swclk=MCU_SWCLK -> U6 PA14-BOOT0 pin21`；`swdio=MCU_SWDIO -> U6 PA13 pin20`；`reset=NRST`；`ground=GND` |
| 保护电路 | 输入与 5V 输出保护 | `input_fuse=FUSE1 6V/2A`；`output_clamp=D3 from 5V_OUT to GND`；`cc_resistors=R14/R15 5.1KΩ`；`usb_esd=null`；`battery_protection_ic=null` |
| 关键网络 | BAT_CHRG 充电状态 | `charger_output=U8 CHRG pin7`；`network=BAT_CHRG`；`mcu_input=U6 PB4 pin24`；`power_led=5V_OUT -> R6 3.4KΩ -> D4 -> GND` |
| 总线地址 | Unit TimerPWR 对外 I2C 地址 | `documented_address=0x56`；`controller=U6 STM32G031G8U6`；`interface=J1 PA_SCL/PA_SDA`；`schematic_address=null` |
| 总线地址 | INA3221 I2C 地址 | `device=U2 INA3221`；`address_pin=A0 pin5 GND`；`numeric_address=null` |
| 接口 | OLED 尺寸与分辨率 | `documented_size=0.66 inch`；`documented_resolution=64x48`；`documented_bus=SPI`；`connector=FPC1`；`schematic_model=null` |
| 电源 | 充电电流、电池规格和 Grove 输出能力 | `documented_battery=3.7V lithium battery`；`documented_charge_current=330mA`；`documented_grove_example=approximately 5V/800mA with 1400mAh@1C battery`；`charger_program=U8 LGS4056H,R21 3KΩ`；`output_path=U4 SY7088 -> 5V_OUT -> R23 -> GROVE_5V`；`schematic_current_ratings=null` |

## 待确认事项

- `address.documented-unit-i2c`：产品正文给出 Grove I2C 通讯地址 0x56；原理图只确认 U6 通过 PB6/PB7 的 PA_SCL/PA_SDA 连接 J1，图中没有 0x56 地址文字、地址选择引脚或协议寄存器。（证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页 U6 PB6/PB7 至 J1 PA_SCL/PA_SDA，图中无数字地址）
- `address.ina3221`：原理图显示 U2 INA3221 的 A0 pin5 接 GND，但未在页内标出该配置对应的数字 I2C 地址。（证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 A3，U2 A0 pin5 接 GND，图中无地址文字）
- `interface.documented-oled`：产品正文称 OLED 为 0.66 英寸、64x48、SPI；原理图仅确认 FPC1 的 SPI/控制、电源和电荷泵连接，没有显示屏型号、尺寸或分辨率文字。（证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页网格 C4-D4，FPC1 仅标引脚和网络，无面板型号/尺寸/分辨率）
- `power.documented-ratings`：产品正文称外接 3.7V 锂电池、充电电流 330mA，并给出与电池能力相关的 Grove 5V 输出示例；原理图只确认 P1、U8/R21、U4 和 J1 电路，未直接标注电池化学体系、连接器间距、充电电流数值或最大输出电流。（证据：图 c03d86b36fe8 / 第 1 页 / 第 1 页 P1/U8/R21/U4/J1，图中无 330mA、3.7V 或最大输出电流标注）
- `review.unit-i2c-address`：请用固件协议或总线扫描确认 Unit TimerPWR 对外 I2C 从地址为 0x56。；原因：0x56 只出现在产品正文，原理图未标数字地址或地址选择逻辑。
- `review.ina3221-address`：请依据 INA3221 datasheet 或总线扫描确认 A0 接 GND 时的数字 I2C 地址。；原因：原理图只显示 A0 接地，没有地址对照表。
- `review.oled-spec`：请用 OLED BOM、面板 datasheet 或实物确认 FPC1 对应 0.66 英寸 64x48 OLED 的具体型号。；原因：原理图未标面板型号、尺寸和分辨率。
- `review.power-ratings`：请依据 LGS4056H/SY7088 datasheet、BOM 与整机测试确认 330mA 充电电流、电池要求及 Grove 最大持续输出能力。；原因：原理图给出 R21、反馈网络和分流电阻，但没有直接标注这些整机额定值。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `c03d86b36fe8e7841a39f0069e3bc5312a697a9035d13f6dbf32978fb2a0ef4b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/780/U189_SCH_UNIT_TimerPwr_V1.0_page_01.png` |

---

源文档：`zh_CN/unit/Unit-TimerPWR.md`

源文档 SHA-256：`8d5242194d529149cad70f4adc0713dd4eb19bcb5c494dc775c288847232488d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
