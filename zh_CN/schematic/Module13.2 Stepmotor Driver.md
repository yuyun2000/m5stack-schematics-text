# Module13.2 Stepmotor Driver 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 Stepmotor Driver |
| SKU | M039 |
| 产品 ID | `module13-2-stepmotor-driver-33d897af1a0b` |
| 源文档 | `zh_CN/module/stepmotor_driver.md` |

## 概述

Module13.2 Stepmotor Driver 原理图以 U3/U4/U5 三颗 DRV8825 分别驱动 X/Y/Z 三组双极步进电机，STEP_X/Y/Z 与 DIR_X/Y/Z 直接来自 M5-Bus，M0/M1/M2、DRV_EN 和四路 EXT_GP0-3 由 U6 TCA9554PWR 通过 I2C 控制或读取。VIN 可由 BUS1 HPWR 或 J1 DC5.5 输入，U1 SY8303 将 VIN 降压并经 FU2 0.5A 生成 SYS_P050。板上另有 U2 RS-485 收发电路与 J9 A/B/VIN/GND 端子，以及每轴独立电流调节电位器和四针电机输出。

## 检索关键词

`Module13.2 Stepmotor Driver`、`M039`、`DRV8825`、`HR8825`、`TCA9554PWR`、`SY8303`、`RS485`、`STEP_X`、`DIR_X`、`STEP_Y`、`DIR_Y`、`STEP_Z`、`DIR_Z`、`M0`、`M1`、`M2`、`DRV_EN`、`D_RST`、`EXT_GP0`、`EXT_GP1`、`EXT_GP2`、`EXT_GP3`、`I2C`、`0x27`、`SCL`、`SDA`、`VIN`、`SYS_P050`、`M5_BUS`、`RS_A`、`RS_B`、`J2`、`J3`、`J4`、`RW1`、`RW2`、`RW3`、`PWR485`、`1/32 microstep`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3,U4,U5 | DRV8825; DRV8825; DRV8825 | X/Y/Z 三轴双极步进电机驱动器 | 图 badcbc9b557f / 第 1 页 / 页面右侧三组 U3/U4/U5 DRV8825，分别连接 STP_X/DIR_X、STP_Y/DIR_Y、STP_Z/DIR_Z 与 J2/J3/J4 |
| U6 | TCA9554PWR | I2C 八位 GPIO 扩展器，管理四路输入、DRV_EN 与 M0-M2 | 图 badcbc9b557f / 第 1 页 / 页面中央下方 U6 TCA9554PWR，SCL/SDA/A0-A2/P0-P7 与 EXT_GP0-3/DRV_EN/M2/M1/M0 |
| U1 | SY8303 | VIN 至 SYS_P050 的降压转换器 | 图 badcbc9b557f / 第 1 页 / 页面上中 U1 SY8303、FU1、L1、FU2 与 SYS_P050 |
| U2 | 未标注 | TTL/UART 到 RS-485 A/B 的收发器，器件值在栅格图中未标出 | 图 badcbc9b557f / 第 1 页 / 页面中央 U2，pin 1 RO、2 /RE、3 DE、4 DI、5 GND、6 A、7 B、8 VCC，未见器件型号文字 |
| Q1 | S8050 | RS-485 /RE/DE 自动方向控制晶体管 | 图 badcbc9b557f / 第 1 页 / 页面 U2 左侧 Q1 S8050，连接 RS_RX 与 /RE/DE 控制节点 |
| J1 | DC5.5 | VIN 外部直流电源输入插座 | 图 badcbc9b557f / 第 1 页 / 页面左中 J1 DC5.5，PWR+ 接 VIN、PWR- 接 GND |
| FU1,FU2 | BSMD0805-050-24V; 0.5A | SY8303 输入自恢复保险丝与 SYS_P050 输出保险丝 | 图 badcbc9b557f / 第 1 页 / 页面上中 VIN-FU1-U1 与 L1-FU2 0.5A-SYS_P050 |
| J2,J3,J4 | CON4; CON4; CON4 | X/Y/Z 三轴四线双极步进电机输出连接器 | 图 badcbc9b557f / 第 1 页 / 页面右侧 J2/J3/J4 CON4，分别连接 U3/U4/U5 的 AOUT1/AOUT2/BOUT1/BOUT2 |
| RW1,RW2,RW3 | potentiometer; potentiometer; potentiometer | X/Y/Z 三轴 AVREF/BVREF 电流基准调节 | 图 badcbc9b557f / 第 1 页 / 页面右侧各 DRV8825 左下 RW1/RW2/RW3 与 R14/R15/R16、AVREF/BVREF |
| R17,R18,R19,R20,R21,R22 | RTT08R200FTP x6 | 三轴 ISENA/ISENB 电流检测电阻 | 图 badcbc9b557f / 第 1 页 / 页面 U3/U4/U5 右侧 R17-R22 RTT08R200FTP，分别连接 ISENA/ISENB 至功率地 |
| J5,J6,J7,J8 | CON2 x4 | EXT_GP0-EXT_GP3 四路外部输入连接器 | 图 badcbc9b557f / 第 1 页 / 页面左下 J5-J8 CON2，pin 1 为 EXT_GP0-3，pin 2 为 GND |
| J9 | CON4 | RS_B、RS_A、VIN、GND 的 PWR485 端子 | 图 badcbc9b557f / 第 1 页 / 页面左下 J9 CON4，pin 4 RS_B、3 RS_A、2 VIN、1 GND |
| BUS1 | M5_BUS | 30 针主机堆叠接口，提供三轴 STEP/DIR、I2C、RS485、VIN、5V、3.3V 与 GND | 图 badcbc9b557f / 第 1 页 / 页面左上 BUS1 M5_BUS pin 1-30 与外部网络 |

## 系统结构

### Module13.2 Stepmotor Driver 架构

三颗 DRV8825 直接接收 M5-Bus 的三轴 STEP/DIR，TCA9554PWR 通过 I2C 管理细分、驱动使能和四路输入，板载 SY8303 5V 电源与 RS-485/PWR485 接口。

- 参数与网络：`drivers=U3/U4/U5 DRV8825`；`io_expander=U6 TCA9554PWR`；`buck=U1 SY8303`；`rs485=U2 part number not printed`；`axes=X,Y,Z`
- 证据：图 badcbc9b557f / 第 1 页 / 完整单页 BUS1、电源、U2/U6 与三组 DRV8825 分区

## 核心器件

### 三轴 DRV8825 公共控制

U3/U4/U5 的 ENBL 均接 DRV_EN，MODE0/1/2 均接 M0/M1/M2，RESET 与 SLEEP 共接 D_RST；每轴 FAULT、HOME 未连接，AVREF/BVREF 由独立电位器设定。

- 参数与网络：`enable=DRV_EN`；`microstep=M0,M1,M2`；`reset_sleep=D_RST`；`unused=FAULT,HOME`；`current_reference=RW1/RW2/RW3 -> AVREF/BVREF`
- 证据：图 badcbc9b557f / 第 1 页 / 页面右侧三颗 DRV8825 左侧 ENBL/MODE/RESET/SLEEP/FAULT/HOME/AVREF/BVREF

## 电源

### VIN 输入来源

BUS1 pin 2、4、6 的 HPWR 并联连接 VIN；J1 DC5.5 PWR+ 也连接 VIN，PWR- 接 GND；J9 pin 2 同样引出 VIN、pin 1 接 GND。

- 参数与网络：`m5bus=BUS1 pins 2,4,6/HPWR -> VIN`；`dc_jack=J1 PWR+ -> VIN,PWR- -> GND`；`pwr485=J9 pin 2/VIN,pin 1/GND`
- 证据：图 badcbc9b557f / 第 1 页 / 页面 BUS1 HPWR/VIN、J1 DC5.5 与 J9 VIN/GND

### U1 SYS_P050 降压

VIN 经 FU1 BSMD0805-050-24V 进入 U1 SY8303，LX 经 L1 10uH 和 FU2 0.5A 输出 SYS_P050；R3 36K/R5 5.1K 构成 FB 分压，C4 22pF/25V 跨接上臂。

- 参数与网络：`input=VIN -> FU1`；`converter=U1 SY8303`；`inductor=L1 10uH`；`output_fuse=FU2 0.5A`；`output=SYS_P050`；`feedback=R3 36K,R5 5.1K,C4 22pF/25V`
- 证据：图 badcbc9b557f / 第 1 页 / 页面上中 VIN/FU1/U1/L1/FU2/R3/R5/C4/SYS_P050

## 接口

### 三轴电机输出

U3 的 AOUT1/AOUT2/BOUT1/BOUT2 接 J2 pin 1-4，U4 对应接 J3 pin 1-4，U5 对应接 J4 pin 1-4；每个连接器为一组四线双极步进电机输出。

- 参数与网络：`x=U3 -> J2 CON4`；`y=U4 -> J3 CON4`；`z=U5 -> J4 CON4`；`signals=AOUT1,AOUT2,BOUT1,BOUT2`
- 证据：图 badcbc9b557f / 第 1 页 / 页面右侧 U3/J2、U4/J3、U5/J4 输出连线

### BUS1 M5_BUS 已用针脚

BUS1 使用 pin 2/4/6 HPWR=VIN、pin 3 SYS_P050、pin 19 MCU_VDD、pin 13 SCL、pin 14 SDA、pin 16 STP_X、15 DIR_X、10 STP_Y、9 DIR_Y、8 STP_Z、7 DIR_Z、pin 5 RS_TX、pin 21 RS_RX，pin 26/28/30 为 GND。

- 参数与网络：`power=2,4,6:VIN;3:SYS_P050;19:MCU_VDD;26,28,30:GND`；`i2c=13:SCL,14:SDA`；`x_axis=16:STP_X,15:DIR_X`；`y_axis=10:STP_Y,9:DIR_Y`；`z_axis=8:STP_Z,7:DIR_Z`；`rs485=5:RS_TX,21:RS_RX`
- 证据：图 badcbc9b557f / 第 1 页 / 页面左上 BUS1 所有外部网络标注

## 总线

### 三轴 STEP/DIR 直连

BUS1 pin 16/G16/RXD2 连接 STP_X、pin 15/G17/TXD2 连接 DIR_X；pin 10/G12 连接 STP_Y、pin 9/G13 连接 DIR_Y；pin 8/G15 连接 STP_Z、pin 7/G0 连接 DIR_Z。

- 参数与网络：`x=STP_X BUS1 pin16 -> U3 STEP; DIR_X pin15 -> U3 DIR`；`y=STP_Y BUS1 pin10 -> U4 STEP; DIR_Y pin9 -> U4 DIR`；`z=STP_Z BUS1 pin8 -> U5 STEP; DIR_Z pin7 -> U5 DIR`
- 证据：图 badcbc9b557f / 第 1 页 / 页面左上 BUS1 STP_X/Y/Z、DIR_X/Y/Z 与右侧 U3/U4/U5 STEP/DIR

### TCA9554 I2C 总线

BUS1 pin 13/G22/IIC_SCL 连接 SCL 至 U6 pin 14，pin 14/G21/IIS_SDA 连接 SDA 至 U6 pin 15；R1/R9 各 10K/1% 将 SCL/SDA 上拉到 MCU_VDD。

- 参数与网络：`controller=M5 host`；`device=U6 TCA9554PWR`；`scl=BUS1 pin13 -> U6 pin14`；`sda=BUS1 pin14 -> U6 pin15`；`pullups=R1 10K,R9 10K to MCU_VDD`
- 证据：图 badcbc9b557f / 第 1 页 / 页面 BUS1 SCL/SDA 与 U6 R1/R9/SCL/SDA

### 板载 RS-485 物理层

U2 的 A/B 连接 RS_A/RS_B 至 J9；VCC 接 MCU_VDD、GND 接地，RO/DI 与 /RE/DE 连接 RS_TX/RS_RX 及 Q1 S8050 自动方向网络。原理图未标 U2 型号。

- 参数与网络：`transceiver=U2 part number not printed`；`a=pin 6 -> RS_A -> J9 pin3`；`b=pin 7 -> RS_B -> J9 pin4`；`supply=MCU_VDD`；`direction=Q1 S8050,/RE+DE`；`logic_nets=RS_TX,RS_RX`
- 证据：图 badcbc9b557f / 第 1 页 / 页面中央 U2/Q1/RS_A/RS_B 与左下 J9

## 总线地址

### TCA9554 地址脚

U6 A0、A1、A2 均直接连接 GND，硬件地址固定且没有拨码或焊盘选择；原理图未打印十六进制地址。

- 参数与网络：`a0=GND`；`a1=GND`；`a2=GND`；`selectable=false`；`numeric_address_visible=false`
- 证据：图 badcbc9b557f / 第 1 页 / 页面 U6 左下 A0/A1/A2 与 GND

## GPIO 与控制信号

### TCA9554 微步与使能映射

U6 P4 连接 DRV_EN，P5 连接 M2，P6 连接 M1，P7 连接 M0，统一控制三颗 DRV8825。

- 参数与网络：`p4=DRV_EN`；`p5=M2`；`p6=M1`；`p7=M0`；`targets=U3,U4,U5`
- 证据：图 badcbc9b557f / 第 1 页 / 页面 U6 右侧 P4-P7 与 DRV_EN/M2/M1/M0 网络

### 四路 EXT_GP 输入

J5-J8 pin 1 分别为 EXT_GP0-EXT_GP3、pin 2 接 GND；各信号经 R24-R27 5.1K/1% 串联至 U6 P0-P3，并由 R10/R11/R12/R23 36K/1% 上拉至 MCU_VDD。

- 参数与网络：`connectors=J5 EXT_GP0,J6 EXT_GP1,J7 EXT_GP2,J8 EXT_GP3`；`series=R24-R27 5.1K/1%`；`pullups=R10,R11,R12,R23 36K/1% to MCU_VDD`；`expander_pins=P0,P1,P2,P3`
- 证据：图 badcbc9b557f / 第 1 页 / 页面左下 J5-J8 与中央 U6 EXT_GP0-3 输入网络

## 时钟

### 时钟、MCU 与调试可见性

原理图没有板载 MCU、晶体、振荡器、SWD/JTAG 或专用调试连接器；STEP/DIR 由外部 M5 主机直接提供。

- 参数与网络：`mcu_visible=false`；`crystal_visible=false`；`oscillator_visible=false`；`swd_visible=false`；`jtag_visible=false`
- 证据：图 badcbc9b557f / 第 1 页 / 完整单页全部器件与接口

## 复位

### DRV8825 D_RST 网络

三颗 DRV8825 的 RESET 与 SLEEP 引脚连接公共 D_RST，R29 5.1K/1% 将 D_RST 上拉至 MCU_VDD。

- 参数与网络：`net=D_RST`；`loads=U3/U4/U5 RESET+SLEEP`；`pullup=R29 5.1K/1% to MCU_VDD`
- 证据：图 badcbc9b557f / 第 1 页 / 页面右上 R29/MCU_VDD/D_RST 与 U3/U4/U5 pin 16/17

## 保护电路

### RS-485 偏置、终端与保护

RS_A/RS_B 之间配置 R6（DNP）终端位置，R7/R8 5.1K/1% 提供偏置，A/B 各有 PSM712 类保护器件对地；具体保护器件位号/完整料号在栅格图中不清晰。

- 参数与网络：`termination=R6 DNP between A/B`；`bias=R7,R8 5.1K/1%`；`line_protection=PSM712-marked devices on RS_A/RS_B`；`isolation_visible=false`
- 证据：图 badcbc9b557f / 第 1 页 / 页面 U2 右侧 R6/R7/R8 与蓝色 PSM712 保护器件

## 内存与 Flash

### 存储器与内存可见性

原理图没有 Flash、EEPROM、RAM、SD 卡或其他存储器件。

- 参数与网络：`flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`
- 证据：图 badcbc9b557f / 第 1 页 / 完整单页全部器件，无存储位号

## 模拟电路

### 三轴驱动电流调节与采样

RW1/RW2/RW3 通过 R14/R15/R16 1.5K/1% 设定各轴 AVREF/BVREF；每轴 ISENA/ISENB 分别经两颗 RTT08R200FTP 电阻回到功率地。

- 参数与网络：`x_reference=RW1+R14`；`y_reference=RW2+R15`；`z_reference=RW3+R16`；`x_sense=R17,R18 RTT08R200FTP`；`y_sense=R19,R20 RTT08R200FTP`；`z_sense=R21,R22 RTT08R200FTP`
- 证据：图 badcbc9b557f / 第 1 页 / 页面右侧每轴 RW/AVREF/BVREF 与 ISENA/ISENB/R17-R22

## 其他事实

### 其他功能分区可见性

原理图未绘出 SPI、UART、CAN、USB、SDIO、MIPI、I2S、射频、音频或传感器；核心功能为步进驱动、I2C GPIO 扩展、RS-485 与电源。

- 参数与网络：`spi_visible=false`；`uart_visible=false`；`can_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`
- 证据：图 badcbc9b557f / 第 1 页 / 完整单页功能分区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 Stepmotor Driver 架构 | `drivers=U3/U4/U5 DRV8825`；`io_expander=U6 TCA9554PWR`；`buck=U1 SY8303`；`rs485=U2 part number not printed`；`axes=X,Y,Z` |
| 核心器件 | 步进驱动芯片型号一致性 | `schematic_part_number=DRV8825`；`documented_part_number=HR8825`；`references=U3,U4,U5`；`same_part_confirmed=false` |
| 电源 | VIN 输入来源 | `m5bus=BUS1 pins 2,4,6/HPWR -> VIN`；`dc_jack=J1 PWR+ -> VIN,PWR- -> GND`；`pwr485=J9 pin 2/VIN,pin 1/GND` |
| 电源 | U1 SYS_P050 降压 | `input=VIN -> FU1`；`converter=U1 SY8303`；`inductor=L1 10uH`；`output_fuse=FU2 0.5A`；`output=SYS_P050`；`feedback=R3 36K,R5 5.1K,C4 22pF/25V` |
| 电源 | 外部输入电压范围 | `documented_range=9-24V`；`schematic_range_visible=false`；`fuse_marking=BSMD0805-050-24V` |
| 总线 | 三轴 STEP/DIR 直连 | `x=STP_X BUS1 pin16 -> U3 STEP; DIR_X pin15 -> U3 DIR`；`y=STP_Y BUS1 pin10 -> U4 STEP; DIR_Y pin9 -> U4 DIR`；`z=STP_Z BUS1 pin8 -> U5 STEP; DIR_Z pin7 -> U5 DIR` |
| 核心器件 | 三轴 DRV8825 公共控制 | `enable=DRV_EN`；`microstep=M0,M1,M2`；`reset_sleep=D_RST`；`unused=FAULT,HOME`；`current_reference=RW1/RW2/RW3 -> AVREF/BVREF` |
| 复位 | DRV8825 D_RST 网络 | `net=D_RST`；`loads=U3/U4/U5 RESET+SLEEP`；`pullup=R29 5.1K/1% to MCU_VDD` |
| 模拟电路 | 三轴驱动电流调节与采样 | `x_reference=RW1+R14`；`y_reference=RW2+R15`；`z_reference=RW3+R16`；`x_sense=R17,R18 RTT08R200FTP`；`y_sense=R19,R20 RTT08R200FTP`；`z_sense=R21,R22 RTT08R200FTP` |
| 电源 | 单通道驱动电流 | `documented_max_current=1.5A per channel`；`schematic_current_rating_visible=false` |
| GPIO 与控制信号 | TCA9554 微步与使能映射 | `p4=DRV_EN`；`p5=M2`；`p6=M1`；`p7=M0`；`targets=U3,U4,U5` |
| GPIO 与控制信号 | 四路 EXT_GP 输入 | `connectors=J5 EXT_GP0,J6 EXT_GP1,J7 EXT_GP2,J8 EXT_GP3`；`series=R24-R27 5.1K/1%`；`pullups=R10,R11,R12,R23 36K/1% to MCU_VDD`；`expander_pins=P0,P1,P2,P3` |
| 总线 | TCA9554 I2C 总线 | `controller=M5 host`；`device=U6 TCA9554PWR`；`scl=BUS1 pin13 -> U6 pin14`；`sda=BUS1 pin14 -> U6 pin15`；`pullups=R1 10K,R9 10K to MCU_VDD` |
| 总线地址 | TCA9554 地址脚 | `a0=GND`；`a1=GND`；`a2=GND`；`selectable=false`；`numeric_address_visible=false` |
| 总线地址 | TCA9554 I2C 地址 | `documented_address=0x27`；`address_straps=A0=A1=A2=GND`；`schematic_numeric_address_visible=false` |
| GPIO 与控制信号 | 微步分辨率表 | `documented_modes=FULL,1/2,1/4,1/8,1/16,1/32`；`control_nets=M2,M1,M0`；`schematic_truth_table_visible=false` |
| 接口 | 三轴电机输出 | `x=U3 -> J2 CON4`；`y=U4 -> J3 CON4`；`z=U5 -> J4 CON4`；`signals=AOUT1,AOUT2,BOUT1,BOUT2` |
| 总线 | 板载 RS-485 物理层 | `transceiver=U2 part number not printed`；`a=pin 6 -> RS_A -> J9 pin3`；`b=pin 7 -> RS_B -> J9 pin4`；`supply=MCU_VDD`；`direction=Q1 S8050,/RE+DE`；`logic_nets=RS_TX,RS_RX` |
| 保护电路 | RS-485 偏置、终端与保护 | `termination=R6 DNP between A/B`；`bias=R7,R8 5.1K/1%`；`line_protection=PSM712-marked devices on RS_A/RS_B`；`isolation_visible=false` |
| 接口 | BUS1 M5_BUS 已用针脚 | `power=2,4,6:VIN;3:SYS_P050;19:MCU_VDD;26,28,30:GND`；`i2c=13:SCL,14:SDA`；`x_axis=16:STP_X,15:DIR_X`；`y_axis=10:STP_Y,9:DIR_Y`；`z_axis=8:STP_Z,7:DIR_Z`；`rs485=5:RS_TX,21:RS_RX` |
| 时钟 | 时钟、MCU 与调试可见性 | `mcu_visible=false`；`crystal_visible=false`；`oscillator_visible=false`；`swd_visible=false`；`jtag_visible=false` |
| 内存与 Flash | 存储器与内存可见性 | `flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false` |
| 其他事实 | 其他功能分区可见性 | `spi_visible=false`；`uart_visible=false`；`can_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false` |

## 待确认事项

- `component.driver-model-discrepancy`：正式原理图中 U3、U4、U5 均标 DRV8825，而产品正文和规格表写 HR8825；原理图未出现 HR8825 料号。（证据：图 badcbc9b557f / 第 1 页 / 页面右侧 U3/U4/U5 器件值 DRV8825）
- `power.documented-range`：产品正文记载 DC-JACK 与 PWR485 输入为 9-24V；原理图显示 VIN、电源器件和 FU1 24V 标记，但未打印 9-24V 工作范围。（证据：图 badcbc9b557f / 第 1 页 / 页面 VIN/J1/J9/U1 电源路径，无输入范围文字）
- `power.documented-current`：产品正文记载每路最大 1.5A；原理图显示电流调节与采样电阻，但未打印最大驱动电流。（证据：图 badcbc9b557f / 第 1 页 / 页面 U3/U4/U5 电流基准与 ISENA/ISENB 网络，无电流额定文字）
- `address.documented-i2c`：产品正文记载 I2C 地址为 0x27；原理图只显示 A0-A2 接地，没有打印 0x27。（证据：图 badcbc9b557f / 第 1 页 / 页面 U6 A0-A2 地址区，无十六进制数值）
- `gpio.documented-microstep`：产品正文给出 M2/M1/M0 对应 FULL 至 1/32 的真值表；原理图只显示 M0-M2 连接 DRV8825 MODE0-MODE2，没有打印分辨率。（证据：图 badcbc9b557f / 第 1 页 / 页面 U6 P5-P7 与 U3/U4/U5 MODE0-MODE2，无微步表）
- `review.driver-model`：Module13.2 Stepmotor Driver 当前正式驱动芯片是原理图标注的 DRV8825，还是产品正文所述 HR8825？；原因：当前原理图与产品正文的三轴驱动器型号不一致。
- `review.input-range`：DC-JACK 与 PWR485 的正式输入范围是否确认为 9-24V？；原因：原理图未打印工作范围，FU1 的 24V 标记不能单独确认输入上下限。
- `review.max-current`：当前三轴驱动器每路保证最大电流是否为 1.5A？；原因：原理图显示电流基准与采样网络，但未打印电流额定值，且驱动型号存在 DRV8825/HR8825 差异。
- `review.i2c-address`：U6 TCA9554PWR 在 A0-A2 接地时的正式 I2C 地址是否为产品正文记载的 0x27？；原因：原理图只显示地址脚接地，没有打印十六进制地址。
- `review.microstep-table`：当前驱动器 M2/M1/M0 的 FULL 至 1/32 微步真值表是否与产品正文一致？；原因：原理图仅显示 MODE0-MODE2 连接，且驱动器型号与正文不一致。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `badcbc9b557ffa048f02855f29cac4cbda74ffcec910d73d1f3487978067dd8b` | `https://static-cdn.m5stack.com/resource/docs/products/module/stepmotor_driver/stepmotor_driver_sch_01.webp` |

---

源文档：`zh_CN/module/stepmotor_driver.md`

源文档 SHA-256：`1fa74a4173bfeb3888299f01bff369db3776f5f8bf30e3e4b481d0d3995fad55`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
