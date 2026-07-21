# Demo Board-SHT30 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Demo Board-SHT30 |
| SKU | K024-B |
| 产品 ID | `demo-board-sht30-57672aae1d3e` |
| 源文档 | `zh_CN/app/demo-board_sht30.md` |

## 概述

Demo Board-SHT30 是通过 M5Stack 30 Pin 总线接入主机的多功能演示底板，板上分为 ADC、DAC、电机、继电器、键盘、RGB 矩阵、传感器、RFID、RS-232 和 RS-485 等独立功能区。主电源由 J5 输入 +12V，经 F1 和 TPS54360 降压为 +5V，各功能区再用独立 SPST 开关形成局部 5V 或 3.3V 电源轨。主要芯片包括 ADS1115、DAC6574、两颗 LV8548MC、MAX232ESE、SP485EEN-L/TR、MAX4466 与 LM393DR2G；资源中的传感器页实际标注 DHT12 和 BMP280，而非产品名对应的 SHT30/QMP6988，需核对原理图版本。

## 检索关键词

`Demo Board-SHT30`、`K024-B`、`ADS1115`、`DAC6574`、`TPS54360`、`LV8548MC`、`MAX232ESE`、`SP485EEN-L/TR`、`SK6812`、`DHT12`、`BMP280`、`MAX4466`、`LM393DR2G`、`MODULE_RC522_1`、`M5Stack_BUS`、`M5_BUS`、`I2C`、`UART`、`RS-232`、`RS-485`、`ADC`、`DAC`、`RFID`、`8x8 RGB`、`4x4 KEYBOARD`、`ROTARY ENCODER`、`JOYSTICK`、`RELAY-SPDT`、`+12V`、`+5V`、`+3.3V`、`+5V_RELAY`、`+3.3V_SENSOR`、`GPIO16`、`GPIO17`、`RS485_A`、`RS485_B`、`ROUT0`、`AIN0`、`DACIN0`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| J5 | PWR3.5 | +12V 直流电源输入插座 | 图 4d11daaedea5 / 第 1 页 / B1 区域：J5 PWR3.5、F1 与 +12V 网络 |
| F1 | PPTC-1812 | J5 +12V 输入串联的自恢复保护器件 | 图 4d11daaedea5 / 第 1 页 / B1 区域：J5.1-F1-+12V 串联路径 |
| U4 | TPS54360 | 将 +12V 转换为 +5V 的降压转换器 | 图 4d11daaedea5 / 第 1 页 / B2 区域：U4 TPS54360、L1、D5 与反馈网络 |
| J6 | M5Stack_BUS | 30 Pin 主 M5Stack 总线连接器 | 图 4d11daaedea5 / 第 1 页 / C3 区域：J6 M5Stack_BUS 1~30 脚网络标注 |
| J3/J4 | Grove_UART / Grove_IO | 5V Grove UART 与通用 GPIO 接口 | 图 4d11daaedea5 / 第 1 页 / A4-B4 区域：J3、J4 及 GPIO16/GPIO17/GPIO36/GPIO26 |
| U1 | ADS1115 | 四通道 I2C 模数转换器 | 图 b052aef3b337 / 第 1 页 / B2-C3 区域：U1 ADS1115、AIN0~AIN3、SCL/SDA、ADDR |
| U2 | DAC6574 | 四通道 I2C 数模转换器 | 图 39e3fb354667 / 第 1 页 / B2-B3 区域：U2 DAC6574、VoutA~VoutD、SDA/SCL、A0/A1 |
| U3/U12 | LV8548MC | 直流电机与步进电机双 H 桥驱动器 | 图 559fe27f1888 / 第 1 页 / C2 区域：U3 LV8548MC 与 MOTOR+/MOTOR-; 图 757ad4529870 / 第 1 页 / B2-C3 区域：U12 LV8548MC、IN1~IN4、OUT1~OUT4 |
| J1 | Rotary encode | A/B 相与按压开关旋转编码器 | 图 f5063462f633 / 第 1 页 / B2-C3 区域：J1 Rotary encode、IN_A、IN_B、BUTTON、GND |
| J2 | Rocker | 双轴电位器加按键摇杆 | 图 ad7be59e087e / 第 1 页 / B3 区域：J2 Rocker 1~8 脚、ADC_X、ADC_Y、BTN1 |
| S5~S20 | SW-PB | 4x4 矩阵键盘的 16 个按键 | 图 3923693a1280 / 第 1 页 / B2-C3 区域：S5~S20 与 COL0~COL3、ROW0~ROW3 矩阵 |
| LED1~LED64 | SK6812 | 8x8 级联可寻址 RGB LED 矩阵 | 图 65f152e7500e / 第 1 页 / A1-D4：LED1~LED64 SK6812、NP1~NP7 串行级联与 +5V_MATRIX |
| K1~K8 | Relay-SPDT | 八路 SPDT 继电器输出 | 图 c357d2a482c6 / 第 1 页 / B1-C4 区域：K1~K8、P19~P26 三触点输出 |
| Q1~Q8 | SS8050 Y1 | ROUT0~ROUT7 控制的继电器低边驱动晶体管 | 图 c357d2a482c6 / 第 1 页 / B1-C4 区域：Q1~Q8、R5~R12 与继电器线圈 |
| M1 | MODULE_RC522_1 | 以 SCL/SDA 接出的 RFID 模块 | 图 510cceb0bd26 / 第 1 页 / B2-C3 区域：M1 RFID MODULE_RC522_1、SCL/SDA/3.3V/GND |
| U5 | MAX232ESE | TTL UART 与 RS-232 电平转换器 | 图 e90f09397cbd / 第 1 页 / B2-C3 区域：U5 MAX232ESE、TXD/RXD、RS232_R/RS232_T |
| J9 | D Connector 9 | RS-232 DB9 外部接口 | 图 e90f09397cbd / 第 1 页 / B3-C4 区域：J9 的 2、3、5 脚网络 |
| U6 | SP485EEN-L/TR | RS-485 差分收发器 | 图 f826de6918aa / 第 1 页 / B2-C3 区域：U6 SP485EEN-L/TR、RO、RE、DE、DI、A、B |
| D14~D16 | P6SMB6.8CA | RS485_A/RS485_B 差分线的双向 TVS 保护链 | 图 f826de6918aa / 第 1 页 / B3-C3 区域：D14~D16 P6SMB6.8CA 位于 GND、RS485_B、RS485_A 之间 |
| U8 | DHT12 | 资源中实际绘制的温湿度传感器 | 图 44c05699ad81 / 第 1 页 / B1-B2 区域：U8 标注 DHT12，连接 SCL/SDA/+3.3V_SENSOR/GND |
| U11 | BMP280 | 资源中实际绘制的气压传感器 | 图 44c05699ad81 / 第 1 页 / C1-D2 区域：U11 标注 BMP280、SCK/SDI/CSB/SDO |
| U7A/U10A | LM393DR2G | 光敏模拟量与麦克风模拟量的阈值比较器 | 图 44c05699ad81 / 第 1 页 / A3-A4 与 C3-C4 区域：U7A/U10A LM393DR2G、Ain/Din 与 AinA/Din1 |
| U9 | max4466 | 驻极体麦克风前置放大器 | 图 44c05699ad81 / 第 1 页 / C2-D3 区域：MK1、U9 max4466、反馈网络与 AinA |
| P34/P35 | Header 2 / Header 3 | 舵机 SIGNAL 输入和三线舵机接口 | 图 da46320e275d / 第 1 页 / B2-C2 区域：P34、P35、SIGNAL、+5V_SERVO、GND |
| S1~S4/S21~S28 | SW-SPST | ADC、DAC、电机、摇杆、RFID、矩阵、继电器、串口、传感器和舵机等功能区电源开关 | 图 a19c9a08c0aa / 第 1 页 / 顶层页列出各独立功能子页; 图 44c05699ad81 / 第 1 页 / A1 区域：S26 将 +3.3V 接到 +3.3V_SENSOR |

## 系统结构

### 整板功能分区

顶层原理图将整板分为 ADC、DAC、DCMOTOR、ENCODER、JOYSTICK、KEYBOARD、MAIN、PROTO、MATRIX、RELAY、RFID、RS232、RS485、SENSOR、SERVO 和 STEPMOTOR 共 16 个子页。

- 参数与网络：`partition_count=16`；`top_sheet=M5IoT.SchDoc`
- 证据：图 a19c9a08c0aa / 第 1 页 / A1-D3：16 个绿色层次化子页块及子页名称

## 核心器件

### U3 LV8548MC

U3 的 IN1~IN4 接 MTR+/MTR- 控制网络，OUT1~OUT4 组合为 MOTOR+ 与 MOTOR-，D1~D4（M7）对输出提供到电源与地的续流路径。

- 参数与网络：`supply=+5V_DCMOTOR`；`inputs=MTR+,MTR-`；`outputs=MOTOR+,MOTOR-`；`flyback=D1~D4 M7`；`control_connector=P11`；`motor_connector=P12`
- 证据：图 559fe27f1888 / 第 1 页 / B2-C3：U3、D1~D4、P11、P12

### U12 LV8548MC

U12 的 IN1~IN4 分别由 A、B、C、D 控制，OUT1~OUT4 逐路送至 P36，D17~D24（M7）构成四输出的续流保护。

- 参数与网络：`supply=+5V_STEPMOTOR`；`inputs=P37.1=A,P37.2=B,P37.3=C,P37.4=D,P37.5=GND`；`outputs=P36.1=OUT1,P36.2=OUT2,P36.3=OUT3,P36.4=OUT4,P36.5=+5V_STEPMOTOR`；`flyback=D17~D24 M7`
- 证据：图 757ad4529870 / 第 1 页 / B2-C3：P37-U12-D17~D24-P36

### K1~K8 继电器组

ROUT0~ROUT7 各经 1KΩ 基极电阻驱动一颗 SS8050 Y1 低边晶体管，控制 +5V_RELAY 线圈；每路线圈并联 M7 二极管和 100nF 电容。

- 参数与网络：`controls=ROUT0~ROUT7`；`base_resistors=R5~R12 1KΩ`；`transistors=Q1~Q8 SS8050 Y1`；`relays=K1~K8 Relay-SPDT`；`flyback=D6~D13 M7`；`coil_capacitors=C38~C45 100nF`
- 证据：图 c357d2a482c6 / 第 1 页 / B1-C4：八路相同的 ROUT-电阻-Q-线圈-D/C 电路

## 电源

### 主电源路径

J5.1 经 F1 接到 +12V；U4 TPS54360 通过 L1 8.2uH、D5 B290B 和输出电容网络产生 +5V。

- 参数与网络：`input_connector=J5 PWR3.5`；`input_net=+12V`；`protection=F1 PPTC-1812`；`converter=U4 TPS54360`；`inductor=L1 8.2uH`；`diode=D5 B290B`；`output_net=+5V`
- 证据：图 4d11daaedea5 / 第 1 页 / B1-B3：J5-F1-+12V-U4-SW-L1-+5V 完整路径

### TPS54360 调节与补偿

U4 的 FB 网络包含 R2 51KΩ 和 R4 10KΩ；COMP 支路为 R1 12KΩ 与 C15 6.8nF，RT/CLK 由 R3 标注 160KΩ 且旁注 162K。

- 参数与网络：`fb_upper=R2 51KΩ`；`fb_lower=R4 10KΩ`；`comp=R1 12KΩ + C15 6.8nF`；`rt_clk=R3 160KΩ, red note 162K`
- 证据：图 4d11daaedea5 / 第 1 页 / B2-C2：U4 FB/COMP/RT-CLK 引脚及 R1~R4、C15

### 独立功能电源轨

各功能页以 SPST 开关从 +5V 或 +3.3V 生成局部电源轨，并普遍配置 100uF 储能电容。

- 参数与网络：`5v_rails=+5V_ADC,+5V_DAC,+5V_DCMOTOR,+5V_MATRIX,+5V_RELAY,+5V_RS232,+5V_RS485,+5V_SERVO,+5V_STEPMOTOR`；`3v3_rails=+3.3V_JOYSTICK,+3.3V_RFID,+3.3V_SENSOR`；`switches=S1,S2,S3,S4,S21,S22,S23,S24,S25,S26,S27,S28`
- 证据：图 b052aef3b337 / 第 1 页 / A1：S1、C1 与 +5V_ADC; 图 c357d2a482c6 / 第 1 页 / A1：S23、C37 与 +5V_RELAY; 图 44c05699ad81 / 第 1 页 / A1：S26、C54 与 +3.3V_SENSOR

### U5 MAX232ESE 电荷泵

U5 使用 C47~C51 五颗 470nF 电容形成 VDD/VEE 与 C1/C2 电荷泵网络。

- 参数与网络：`capacitors=C47,C48,C49,C50,C51`；`value=470nF`；`supply=+5V_RS232`
- 证据：图 e90f09397cbd / 第 1 页 / B2-C3：U5 周围 C47~C51 470nF

## 接口

### J6 M5Stack_BUS

J6 为 30 Pin 主总线，提供 GND、HPWR、+12V、+5V、+3.3V、BAT、EN 和多路 GPIO。

- 参数与网络：`pins_1_10=1:GND,2:GPIO35,3:GND,4:GPIO36,5:GND,6:EN,7:GPIO23,8:GPIO25,9:GPIO19,10:GPIO26`；`pins_11_20=11:GPIO18,12:+3.3V,13:GPIO3,14:GPIO1,15:GPIO16,16:GPIO17,17:GPIO21,18:GPIO22,19:GPIO2,20:GPIO5`；`pins_21_30=21:GPIO12,22:GPIO13,23:GPIO15,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,28:+5V,29:+12V,30:BAT`
- 证据：图 4d11daaedea5 / 第 1 页 / C3：J6 M5Stack_BUS 1~30 脚逐脚网络标注

### J3 Grove_UART

J3.1=GPIO16/RX，J3.2=GPIO17/TX，J3.3=+5V，J3.4=GND。

- 参数与网络：`pin_1=GPIO16 / RX`；`pin_2=GPIO17 / TX`；`pin_3=+5V`；`pin_4=GND`；`logic_supply=5V connector supply`
- 证据：图 4d11daaedea5 / 第 1 页 / A4：J3 Grove_UART 1~4 脚

### J4 Grove_IO

J4.1=GPIO36，J4.2=GPIO26，J4.3=+5V，J4.4=GND。

- 参数与网络：`pin_1=GPIO36`；`pin_2=GPIO26`；`pin_3=+5V`；`pin_4=GND`
- 证据：图 4d11daaedea5 / 第 1 页 / B4：J4 Grove_IO 1~4 脚

### P11/P12

P11.1~5=MTR+、MTR-、MTRA、MTRB、GND；P12.1~6=GND、MOTOR+、MTRA、MTRB、+5V_DCMOTOR、MOTOR-。

- 参数与网络：`p11=1:MTR+,2:MTR-,3:MTRA,4:MTRB,5:GND`；`p12=1:GND,2:MOTOR+,3:MTRA,4:MTRB,5:+5V_DCMOTOR,6:MOTOR-`
- 证据：图 559fe27f1888 / 第 1 页 / B3-C3：P11 与 P12 逐脚网络

### LED1~LED64 SK6812

64 颗 SK6812 以 DOUT→DIN 串接，行间以 NP1~NP7 延续数据链；全部由 +5V_MATRIX 供电并接 GND。

- 参数与网络：`count=64`；`layout=8x8`；`data_chain=LED1 DIN through LED64 DOUT`；`row_links=NP1~NP7`；`supply=+5V_MATRIX`；`input_header=P17 data and GND`
- 证据：图 65f152e7500e / 第 1 页 / A1-D4：LED1~LED64、NP1~NP7、P17、+5V_MATRIX/GND

### 继电器接口

P18.1~8=ROUT0~ROUT7、P18.9=GND；K1~K8 的三组 SPDT 触点分别由 P19~P26 三针连接器引出。

- 参数与网络：`control_header=P18.1=ROUT0,...,P18.8=ROUT7,P18.9=GND`；`contact_headers=K1:P19,K2:P20,K3:P21,K4:P22,K5:P23,K6:P24,K7:P25,K8:P26`
- 证据：图 c357d2a482c6 / 第 1 页 / A2：P18；B1-C4：K1~K8 与 P19~P26

### P29 RS-485 接口

P29.1=RS485_B，P29.2=RS485_A，P29.3=+12V，P29.4=GND。

- 参数与网络：`pin_1=RS485_B`；`pin_2=RS485_A`；`pin_3=+12V`；`pin_4=GND`
- 证据：图 f826de6918aa / 第 1 页 / B4-C4：P29 1~4 脚

### P34/P35 舵机接口

P34.1=SIGNAL、P34.2=GND；P35.1=SIGNAL、P35.2=+5V_SERVO、P35.3=GND。

- 参数与网络：`control_header=P34.1=SIGNAL,P34.2=GND`；`servo_header=P35.1=SIGNAL,P35.2=+5V_SERVO,P35.3=GND`；`power_switch=S27`；`bulk_capacitor=C62 100uF`
- 证据：图 da46320e275d / 第 1 页 / A2-C2：S27/C62、P34/P35 及 SIGNAL/+5V_SERVO/GND

### J8 M5_BUS 原型区

J8 将两路 3V3、两路 5V、BAT、EN、GPIO0/1/2/3/5/12/13/15/16/17/18/19/21/22/23/25/26/34/35/36 和四路 GND 引到原型区 J7。

- 参数与网络：`odd_pins=1:3V3,3:3V3,5:GPIO17,7:GPIO16,9:GPIO21,11:GPIO22,13:GPIO23,15:GPIO19,17:GPIO18,19:GPIO2,21:GPIO5,23:GPIO12,25:GPIO13,27:GPIO15,29:BAT`；`even_pins=2:5V,4:5V,6:GPIO1,8:GPIO3,10:EN,12:GPIO0,14:GPIO34,16:GPIO35,18:GPIO36,20:GPIO25,22:GPIO26,24:GND,26:GND,28:GND,30:GND`；`proto_grid=J7`
- 证据：图 85e20e8ae9c7 / 第 1 页 / B1-C3：J7 原型网格与 J8 M5_BUS 1~30 脚

## 总线

### I2C 功能接口

ADC 页 P3、DAC 页 P8、RFID 页 P38 和传感器页 P31/P33 均以 SCL/SDA 或等价的 SCK/SDI 两线信号引出；这些子页未在顶层画出彼此的板内并联关系。

- 参数与网络：`adc=P3:SCL,SDA,GND`；`dac=P8:U2.SDA,U2.SCL,GND`；`rfid=P38:SCL,SDA,GND`；`dht12=P31:SCL,SDA,GND`；`bmp280=P33:SCK,SDI,GND`
- 证据：图 b052aef3b337 / 第 1 页 / B3：P3 SCL/SDA/GND; 图 39e3fb354667 / 第 1 页 / B3：U2 到 P8 三线接口; 图 510cceb0bd26 / 第 1 页 / B2-C3：M1 到 P38; 图 44c05699ad81 / 第 1 页 / B1 与 C1：P31、P33

### U5 MAX232ESE

P27.1 TXD 接 U5 T1IN，T1OUT 形成 RS232_R 并到 J9.2；J9.3 的 RS232_T 接 R1IN，R1OUT 输出到 P27.2 RXD；P27.3 和 J9.5 接 GND。

- 参数与网络：`ttl_header=P27.1=TXD,P27.2=RXD,P27.3=GND`；`tx_path=TXD-U5.11 T1IN-U5.14 T1OUT-RS232_R-J9.2`；`rx_path=J9.3-RS232_T-U5.13 R1IN-U5.12 R1OUT-RXD`；`db9_ground=J9.5`；`supply=+5V_RS232`
- 证据：图 e90f09397cbd / 第 1 页 / B1-C4：P27-U5-J9 完整 TX/RX 路径

### U6 SP485EEN-L/TR

U6 的 RO 经 R14 1KΩ 输出 R0；RE 与 DE 并联，由 R15 4.7KΩ 上拉并由 Q9 拉低，Q9 基极由 T0 经 R16 1KΩ 控制；DI 在图中接 GND。

- 参数与网络：`receive_output=U6.1 RO-R14 1KΩ-R0/P28.2`；`direction_control=U6.2 RE + U6.3 DE`；`pullup=R15 4.7KΩ to +5V_RS485`；`transistor=Q9 SS8050 Y1`；`control_input=P28.1 T0 through R16 1KΩ`；`di=U6.4 to GND`；`p28=1:T0,2:R0,3:GND`
- 证据：图 f826de6918aa / 第 1 页 / B1-C3：P28、Q9、R14~R16、U6 RE/DE/DI/RO

## GPIO 与控制信号

### J1/P13 旋转编码器

J1 的 A、B 和按键分别形成 IN_A、IN_B、BUTTON，公共端和按键另一端接 GND；P13.1~4=IN_A、IN_B、BUTTON、GND。

- 参数与网络：`a=IN_A`；`b=IN_B`；`button=BUTTON`；`common=GND`；`header=P13.1=IN_A,P13.2=IN_B,P13.3=BUTTON,P13.4=GND`
- 证据：图 f5063462f633 / 第 1 页 / B2-C3：P13、J1 A/COM/B 与 b1/b2

### 4x4 键盘

S5~S20 构成 4 列 4 行无二极管矩阵；P15.1~4=COL0~COL3，P16.1~4=ROW0~ROW3。

- 参数与网络：`columns=P15.1=COL0,P15.2=COL1,P15.3=COL2,P15.4=COL3`；`rows=P16.1=ROW0,P16.2=ROW1,P16.3=ROW2,P16.4=ROW3`；`switches=S5~S20`；`diodes=none shown`
- 证据：图 3923693a1280 / 第 1 页 / B2-C3：16 键矩阵及 P15/P16

## 时钟

### 整板时钟

17 张资源中未绘制独立晶振或有源时钟器件；串行与传感器时钟均作为外部 SCL、SCK 或 UART 信号引入。

- 参数与网络：`crystal=none shown`；`clock_nets=SCL,SCK`
- 证据：图 a19c9a08c0aa / 第 1 页 / 顶层 16 子页索引，无时钟功能页; 图 44c05699ad81 / 第 1 页 / 传感器页仅见 SCL/SCK 外部信号，无晶振

## 复位

### EN

主总线 J6.6 和原型总线 J8.10 均引出 EN 网络。

- 参数与网络：`main_bus=J6.6`；`proto_bus=J8.10`；`net=EN`
- 证据：图 4d11daaedea5 / 第 1 页 / C3：J6.6=EN; 图 85e20e8ae9c7 / 第 1 页 / B2：J8.10=EN

## 保护电路

### RS485_A/RS485_B

D14~D16 均为 P6SMB6.8CA，依次跨接 GND-RS485_B、RS485_B-RS485_A、RS485_A-GND；R13 和 R17 均为 4.7KΩ 偏置电阻。

- 参数与网络：`tvs_top=D14 GND-RS485_B`；`tvs_middle=D15 RS485_B-RS485_A`；`tvs_bottom=D16 RS485_A-GND`；`bias_b=R13 4.7KΩ to GND`；`bias_a=R17 4.7KΩ to +5V_RS485`
- 证据：图 f826de6918aa / 第 1 页 / B3-C3：R13/R17 与 D14~D16 保护/偏置网络

## 存储

### 存储器

17 张原理图资源中未绘制独立 Flash、EEPROM、SD 卡或其他存储器件。

- 参数与网络：`flash=none shown`；`eeprom=none shown`；`sd=none shown`
- 证据：图 a19c9a08c0aa / 第 1 页 / 顶层 16 个功能分区中无存储分区; 图 85e20e8ae9c7 / 第 1 页 / PROTO 页仅为总线与原型网格，无存储器件

## 音频

### MK1/U9 麦克风前端

MK1 经 R22/R23 偏置和 C58 10nF 耦合到 U9 max4466；U9 输出 AinA，反馈支路为 R28 100KΩ 与 C59 100pF，并经 U10A 比较得到 Din1。

- 参数与网络：`microphone=MK1 Mic2`；`amplifier=U9 max4466`；`coupling=C58 10nF`；`feedback=R28 100KΩ parallel C59 100pF`；`analog_output=AinA / P32.1`；`digital_output=Din1 / P32.2`；`ground=P32.3`；`comparator=U10A LM393DR2G`；`digital_pullup=R26 10KΩ`
- 证据：图 44c05699ad81 / 第 1 页 / B2-D4：MK1、R22~R29、C57~C61、U9、U10A、P32

## 传感器

### U8 DHT12

U8 由 +3.3V_SENSOR 供电并接 GND，SCL/SDA 由 P31 引出；图面未标数字 I2C 地址。

- 参数与网络：`supply=+3.3V_SENSOR`；`header=P31.1=SCL,P31.2=SDA,P31.3=GND`；`address=not printed`
- 证据：图 44c05699ad81 / 第 1 页 / B1-B2：U8 DHT12、C56、P31

### U11 BMP280

U11 的 Vdd/Vddio 和 CSB 接 +3.3V_SENSOR，SDO 接 GND；SCK、SDI 和 GND 由 P33 引出，构成图面所示两线接口配置。

- 参数与网络：`supply=U11.8 Vdd + U11.6 Vddio = +3.3V_SENSOR`；`csb=U11.2 to +3.3V_SENSOR`；`sdo=U11.5 to GND`；`header=P33.1=SCK,P33.2=SDI,P33.3=GND`；`address=not printed`
- 证据：图 44c05699ad81 / 第 1 页 / C1-D2：U11 BMP280 引脚与 P33

## 射频

### M1 RFID

M1 标注 MODULE_RC522_1，由 +3.3V_RFID 供电，信号端标为 SCL 和 SDA；P38.1=SCL、P38.2=SDA、P38.3=GND。

- 参数与网络：`module=MODULE_RC522_1`；`supply=+3.3V_RFID`；`interface=SCL/SDA`；`header=P38.1=SCL,P38.2=SDA,P38.3=GND`
- 证据：图 510cceb0bd26 / 第 1 页 / B2-C3：M1 与 P38

## 调试与烧录

### 调试接口

图中未见独立 JTAG、SWD 或专用下载调试连接器；可用信号来自 M5Stack 总线、Grove UART 和原型总线引出。

- 参数与网络：`jtag=none shown`；`swd=none shown`；`available_uart=J3 GPIO16/GPIO17`；`breakout=J6/J8`
- 证据：图 4d11daaedea5 / 第 1 页 / A4-C4：J3/J4/J6 接口，无专用调试连接器; 图 85e20e8ae9c7 / 第 1 页 / B2：J8 原型总线引出

## 模拟电路

### U1 ADS1115

U1 由 +5V_ADC 供电，AIN0~AIN3 分别接 P1、P2、P4、P5 的 1 脚，各连接器 2 脚接 GND；SCL/SDA 从 P3 引出。

- 参数与网络：`supply=+5V_ADC`；`ain0=P1.1`；`ain1=P2.1`；`ain2=P4.1`；`ain3=P5.1`；`returns=P1.2,P2.2,P4.2,P5.2=GND`；`i2c=P3.1=SCL,P3.2=SDA,P3.3=GND`
- 证据：图 b052aef3b337 / 第 1 页 / B2-C3：P1/P2/P4/P5、U1、P3 及网络标注

### U2 DAC6574

U2 由 +5V_DAC 供电，VoutA~VoutD 对应 DACIN0~DACIN3 并分别由 P6、P7、P9、P10 引出，各输出连接器另一脚为 GND。

- 参数与网络：`supply=+5V_DAC`；`vouta=DACIN0 / P6.1`；`voutb=DACIN1 / P7.1`；`voutc=DACIN2 / P9.1`；`voutd=DACIN3 / P10.1`；`returns=P6.2,P7.2,P9.2,P10.2=GND`
- 证据：图 39e3fb354667 / 第 1 页 / B2-C3：U2、DACIN0~3、P6/P7/P9/P10

### J2/P14 摇杆

J2 的 X/Y 电位器分别在 +3.3V_JOYSTICK 与 GND 之间，滑臂输出 ADC_X 和 ADC_Y；按键输出 BTN1 并按下接 GND。

- 参数与网络：`x=J2.2 ADC_X`；`y=J2.7 ADC_Y`；`x_ends=J2.1 GND,J2.3 +3.3V_JOYSTICK`；`y_ends=J2.6 GND,J2.8 +3.3V_JOYSTICK`；`button=J2.4 BTN1,J2.5 GND`；`header=P14.1=ADC_X,P14.2=ADC_Y,P14.3=BTN1,P14.4=GND`
- 证据：图 ad7be59e087e / 第 1 页 / B2-C3：P14 与 J2 1~8 脚

### 光敏采样与比较器

R18 10KΩ 与 R21 LightRes 形成 Ain 光敏采样节点，C55 100nF 对地滤波；U7A LM393DR2G 比较 Ain 与 R20 10K 电位器阈值，Din 由 R19 10KΩ 上拉。

- 参数与网络：`analog=Ain / P30.1`；`digital=Din / P30.2`；`ground=P30.3`；`divider=R18 10KΩ + R21 LightRes`；`filter=C55 100nF`；`threshold=R20 RPot 10K`；`pullup=R19 10KΩ to +3.3V_SENSOR`
- 证据：图 44c05699ad81 / 第 1 页 / A2-A4：R18/R20/R21/C55、U7A、R19、P30

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 整板功能分区 | `partition_count=16`；`top_sheet=M5IoT.SchDoc` |
| 电源 | 主电源路径 | `input_connector=J5 PWR3.5`；`input_net=+12V`；`protection=F1 PPTC-1812`；`converter=U4 TPS54360`；`inductor=L1 8.2uH`；`diode=D5 B290B`；`output_net=+5V` |
| 电源 | TPS54360 调节与补偿 | `fb_upper=R2 51KΩ`；`fb_lower=R4 10KΩ`；`comp=R1 12KΩ + C15 6.8nF`；`rt_clk=R3 160KΩ, red note 162K` |
| 电源 | 独立功能电源轨 | `5v_rails=+5V_ADC,+5V_DAC,+5V_DCMOTOR,+5V_MATRIX,+5V_RELAY,+5V_RS232,+5V_RS485,+5V_SERVO,+5V_STEPMOTOR`；`3v3_rails=+3.3V_JOYSTICK,+3.3V_RFID,+3.3V_SENSOR`；`switches=S1,S2,S3,S4,S21,S22,S23,S24,S25,S26,S27,S28` |
| 接口 | J6 M5Stack_BUS | `pins_1_10=1:GND,2:GPIO35,3:GND,4:GPIO36,5:GND,6:EN,7:GPIO23,8:GPIO25,9:GPIO19,10:GPIO26`；`pins_11_20=11:GPIO18,12:+3.3V,13:GPIO3,14:GPIO1,15:GPIO16,16:GPIO17,17:GPIO21,18:GPIO22,19:GPIO2,20:GPIO5`；`pins_21_30=21:GPIO12,22:GPIO13,23:GPIO15,24:GPIO0,25:HPWR,26:GPIO34,27:HPWR,28:+5V,29:+12V,30:BAT` |
| 接口 | J3 Grove_UART | `pin_1=GPIO16 / RX`；`pin_2=GPIO17 / TX`；`pin_3=+5V`；`pin_4=GND`；`logic_supply=5V connector supply` |
| 接口 | J4 Grove_IO | `pin_1=GPIO36`；`pin_2=GPIO26`；`pin_3=+5V`；`pin_4=GND` |
| 模拟电路 | U1 ADS1115 | `supply=+5V_ADC`；`ain0=P1.1`；`ain1=P2.1`；`ain2=P4.1`；`ain3=P5.1`；`returns=P1.2,P2.2,P4.2,P5.2=GND`；`i2c=P3.1=SCL,P3.2=SDA,P3.3=GND` |
| 总线地址 | U1 ADS1115 | `address_pin=U1.1 ADDR`；`strap=GND`；`address=not printed on schematic` |
| 模拟电路 | U2 DAC6574 | `supply=+5V_DAC`；`vouta=DACIN0 / P6.1`；`voutb=DACIN1 / P7.1`；`voutc=DACIN2 / P9.1`；`voutd=DACIN3 / P10.1`；`returns=P6.2,P7.2,P9.2,P10.2=GND` |
| 总线地址 | U2 DAC6574 | `a0=GND`；`a1=GND`；`address=not printed on schematic`；`conflict_with_ads1115=not established by schematic alone` |
| 总线 | I2C 功能接口 | `adc=P3:SCL,SDA,GND`；`dac=P8:U2.SDA,U2.SCL,GND`；`rfid=P38:SCL,SDA,GND`；`dht12=P31:SCL,SDA,GND`；`bmp280=P33:SCK,SDI,GND` |
| 核心器件 | U3 LV8548MC | `supply=+5V_DCMOTOR`；`inputs=MTR+,MTR-`；`outputs=MOTOR+,MOTOR-`；`flyback=D1~D4 M7`；`control_connector=P11`；`motor_connector=P12` |
| 接口 | P11/P12 | `p11=1:MTR+,2:MTR-,3:MTRA,4:MTRB,5:GND`；`p12=1:GND,2:MOTOR+,3:MTRA,4:MTRB,5:+5V_DCMOTOR,6:MOTOR-` |
| 核心器件 | U12 LV8548MC | `supply=+5V_STEPMOTOR`；`inputs=P37.1=A,P37.2=B,P37.3=C,P37.4=D,P37.5=GND`；`outputs=P36.1=OUT1,P36.2=OUT2,P36.3=OUT3,P36.4=OUT4,P36.5=+5V_STEPMOTOR`；`flyback=D17~D24 M7` |
| GPIO 与控制信号 | J1/P13 旋转编码器 | `a=IN_A`；`b=IN_B`；`button=BUTTON`；`common=GND`；`header=P13.1=IN_A,P13.2=IN_B,P13.3=BUTTON,P13.4=GND` |
| 模拟电路 | J2/P14 摇杆 | `x=J2.2 ADC_X`；`y=J2.7 ADC_Y`；`x_ends=J2.1 GND,J2.3 +3.3V_JOYSTICK`；`y_ends=J2.6 GND,J2.8 +3.3V_JOYSTICK`；`button=J2.4 BTN1,J2.5 GND`；`header=P14.1=ADC_X,P14.2=ADC_Y,P14.3=BTN1,P14.4=GND` |
| GPIO 与控制信号 | 4x4 键盘 | `columns=P15.1=COL0,P15.2=COL1,P15.3=COL2,P15.4=COL3`；`rows=P16.1=ROW0,P16.2=ROW1,P16.3=ROW2,P16.4=ROW3`；`switches=S5~S20`；`diodes=none shown` |
| 接口 | LED1~LED64 SK6812 | `count=64`；`layout=8x8`；`data_chain=LED1 DIN through LED64 DOUT`；`row_links=NP1~NP7`；`supply=+5V_MATRIX`；`input_header=P17 data and GND` |
| 核心器件 | K1~K8 继电器组 | `controls=ROUT0~ROUT7`；`base_resistors=R5~R12 1KΩ`；`transistors=Q1~Q8 SS8050 Y1`；`relays=K1~K8 Relay-SPDT`；`flyback=D6~D13 M7`；`coil_capacitors=C38~C45 100nF` |
| 接口 | 继电器接口 | `control_header=P18.1=ROUT0,...,P18.8=ROUT7,P18.9=GND`；`contact_headers=K1:P19,K2:P20,K3:P21,K4:P22,K5:P23,K6:P24,K7:P25,K8:P26` |
| 射频 | M1 RFID | `module=MODULE_RC522_1`；`supply=+3.3V_RFID`；`interface=SCL/SDA`；`header=P38.1=SCL,P38.2=SDA,P38.3=GND` |
| 总线 | U5 MAX232ESE | `ttl_header=P27.1=TXD,P27.2=RXD,P27.3=GND`；`tx_path=TXD-U5.11 T1IN-U5.14 T1OUT-RS232_R-J9.2`；`rx_path=J9.3-RS232_T-U5.13 R1IN-U5.12 R1OUT-RXD`；`db9_ground=J9.5`；`supply=+5V_RS232` |
| 电源 | U5 MAX232ESE 电荷泵 | `capacitors=C47,C48,C49,C50,C51`；`value=470nF`；`supply=+5V_RS232` |
| 总线 | U6 SP485EEN-L/TR | `receive_output=U6.1 RO-R14 1KΩ-R0/P28.2`；`direction_control=U6.2 RE + U6.3 DE`；`pullup=R15 4.7KΩ to +5V_RS485`；`transistor=Q9 SS8050 Y1`；`control_input=P28.1 T0 through R16 1KΩ`；`di=U6.4 to GND`；`p28=1:T0,2:R0,3:GND` |
| 接口 | P29 RS-485 接口 | `pin_1=RS485_B`；`pin_2=RS485_A`；`pin_3=+12V`；`pin_4=GND` |
| 保护电路 | RS485_A/RS485_B | `tvs_top=D14 GND-RS485_B`；`tvs_middle=D15 RS485_B-RS485_A`；`tvs_bottom=D16 RS485_A-GND`；`bias_b=R13 4.7KΩ to GND`；`bias_a=R17 4.7KΩ to +5V_RS485` |
| 传感器 | Demo Board-SHT30 传感器版本 | `product_name=Demo Board-SHT30`；`schematic_temperature_humidity=U8 DHT12`；`schematic_pressure=U11 BMP280`；`sht30=not found in supplied sheets`；`qmp6988=not found in supplied sheets` |
| 传感器 | U8 DHT12 | `supply=+3.3V_SENSOR`；`header=P31.1=SCL,P31.2=SDA,P31.3=GND`；`address=not printed` |
| 传感器 | U11 BMP280 | `supply=U11.8 Vdd + U11.6 Vddio = +3.3V_SENSOR`；`csb=U11.2 to +3.3V_SENSOR`；`sdo=U11.5 to GND`；`header=P33.1=SCK,P33.2=SDI,P33.3=GND`；`address=not printed` |
| 模拟电路 | 光敏采样与比较器 | `analog=Ain / P30.1`；`digital=Din / P30.2`；`ground=P30.3`；`divider=R18 10KΩ + R21 LightRes`；`filter=C55 100nF`；`threshold=R20 RPot 10K`；`pullup=R19 10KΩ to +3.3V_SENSOR` |
| 音频 | MK1/U9 麦克风前端 | `microphone=MK1 Mic2`；`amplifier=U9 max4466`；`coupling=C58 10nF`；`feedback=R28 100KΩ parallel C59 100pF`；`analog_output=AinA / P32.1`；`digital_output=Din1 / P32.2`；`ground=P32.3`；`comparator=U10A LM393DR2G`；`digital_pullup=R26 10KΩ` |
| 接口 | P34/P35 舵机接口 | `control_header=P34.1=SIGNAL,P34.2=GND`；`servo_header=P35.1=SIGNAL,P35.2=+5V_SERVO,P35.3=GND`；`power_switch=S27`；`bulk_capacitor=C62 100uF` |
| 接口 | J8 M5_BUS 原型区 | `odd_pins=1:3V3,3:3V3,5:GPIO17,7:GPIO16,9:GPIO21,11:GPIO22,13:GPIO23,15:GPIO19,17:GPIO18,19:GPIO2,21:GPIO5,23:GPIO12,25:GPIO13,27:GPIO15,29:BAT`；`even_pins=2:5V,4:5V,6:GPIO1,8:GPIO3,10:EN,12:GPIO0,14:GPIO34,16:GPIO35,18:GPIO36,20:GPIO25,22:GPIO26,24:GND,26:GND,28:GND,30:GND`；`proto_grid=J7` |
| 复位 | EN | `main_bus=J6.6`；`proto_bus=J8.10`；`net=EN` |
| 时钟 | 整板时钟 | `crystal=none shown`；`clock_nets=SCL,SCK` |
| 存储 | 存储器 | `flash=none shown`；`eeprom=none shown`；`sd=none shown` |
| 调试与烧录 | 调试接口 | `jtag=none shown`；`swd=none shown`；`available_uart=J3 GPIO16/GPIO17`；`breakout=J6/J8` |

## 待确认事项

- `address.ads1115-strap`：原理图明确将 ADDR 脚接 GND，但图面没有标注对应的十六进制 I2C 地址。（证据：图 b052aef3b337 / 第 1 页 / B2-C3：U1.1 ADDR 到 GND 的连线）
- `address.dac6574-strap`：原理图明确将 A0 和 A1 地址脚接 GND，但未在图面标出十六进制 I2C 地址，也无法仅凭图面确认与 ADS1115 的数字地址冲突。（证据：图 39e3fb354667 / 第 1 页 / B3：U2.9 A0、U2.10 A1 接 GND; 图 b052aef3b337 / 第 1 页 / B2-C3：U1 ADDR 接 GND，图面无数字地址）
- `sensor.schematic-version-mismatch`：产品清单名称为 Demo Board-SHT30，但资源传感器页明确标注 U8=DHT12、U11=BMP280，17 张资源中未见 SHT30 或 QMP6988 器件标注，因此无法确认资源是否属于 K024-B 的当前传感器版本。（证据：图 44c05699ad81 / 第 1 页 / B1：U8 DHT12；C1-D2：U11 BMP280；本页无 SHT30/QMP6988; 图 a19c9a08c0aa / 第 1 页 / A3：顶层 SENSOR 子页仅指向 M5IoT_SENSOR.SchDoc，不含器件型号）
- `review.ads1115-address`：请用 ADS1115 对应数据手册确认 ADDR=GND 的 7-bit I2C 地址。；原因：原理图只给出 ADDR 接地，未打印数字地址。
- `review.dac6574-address`：请用 DAC6574 数据手册确认 A1=A0=GND 的 7-bit I2C 地址，并复核是否与 ADS1115 冲突。；原因：原理图仅显示地址脚电平，正文所述数字地址与冲突无法由图面独立验证。
- `review.sensor-version`：请确认这 17 张原理图是否为 SKU K024-B 的 SHT30/QMP6988 版本，并提供匹配版本资源。；原因：产品名和正文定位到 SHT30/QMP6988，但资源传感器页实际标注 DHT12/BMP280。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `a19c9a08c0aa2e853d77d1d70024bbecd44ef88e52f78a0510fa6b8beea61986` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_01.png` |
| 2 | 1 | `b052aef3b337ad6ebcec969e487cba072b66383088457fb8c85bb45b9cc13528` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_02.png` |
| 3 | 1 | `39e3fb3546676aebcdceadd47ee47b1bb92e4b7b81b27f3401b27939d1d0a1d1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_03.png` |
| 4 | 1 | `559fe27f188887d71392a01bd8d7a0324a27ce1d4326841515ab12641278ee92` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_04.png` |
| 5 | 1 | `f5063462f633dbfdfc0eda9c3f913b551cd6b093e8735f3a0c091f59b7bcb46f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_05.png` |
| 6 | 1 | `ad7be59e087e2bd57a1fd62f285837747ef0637ab0cfe20c082b03366ec4b92f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_06.png` |
| 7 | 1 | `3923693a128075895202a053ea9be17fc9b01733df741aa1bd62099ab87dc78f` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_07.png` |
| 8 | 1 | `4d11daaedea56c379e8952fcdde16c4a8b50dc9392e803076922a9a84f0cdbd4` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_08.png` |
| 9 | 1 | `65f152e7500ea7684a989d9dfd15009e4ec1a6f021607a91eb348478c4b0cfc5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_09.png` |
| 10 | 1 | `85e20e8ae9c7e85b0969b5a26b1a8eb6b22676fb7fe97339c428009caa99af7b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_10.png` |
| 11 | 1 | `c357d2a482c69250cda0f08fd344f81edc738cc85685e734e2ef681b6d904b17` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_11.png` |
| 12 | 1 | `510cceb0bd261e91e59eb4c601469fa1c5b3bbcfa3bb03d1623e44f08bfb0faa` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_12.png` |
| 13 | 1 | `e90f09397cbdc279d420d729b5118af4b30eb0c473de75e3c06c2810064a2495` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_13.png` |
| 14 | 1 | `f826de6918aa209e0548166874fa753a14356aee04db0c2e9385561e9298111b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_14.png` |
| 15 | 1 | `44c05699ad81b2ad368bd93bd0e81d520af67b695c04fcbbae817e2cc0bf0151` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_15.png` |
| 16 | 1 | `da46320e275dc42ceb5f612967b10fd94225b0da72b15ba4df20d728099d25c1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_16.png` |
| 17 | 1 | `757ad45298704fd78a49631f05e057994fbaa835b2817c3a6927a4bff9e4cdd5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/634/Sch_Demo_Board_sch_17.png` |

---

源文档：`zh_CN/app/demo-board_sht30.md`

源文档 SHA-256：`3f021a389c7fe486402c30c42d7ab407a201ea0c8bdf6744e0b9cae0216248d0`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
