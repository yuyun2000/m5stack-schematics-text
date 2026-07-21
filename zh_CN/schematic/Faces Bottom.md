# Faces Bottom 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Faces Bottom |
| SKU | A009 |
| 产品 ID | `faces-bottom-0b69ecd4797d` |
| 源文档 | `zh_CN/module/faces.md` |

## 概述

Faces Bottom 原理图分为充电板与接口板两部分。充电板以 U1 IP5306 管理 +5V 输入、BAT 电池网络和 VOUT/SW 升压功率级，P1 连接电池，P2 引出 +5、GND、SDA、SCL；BUS1、BUS2 两组 24 针 M5_BUS 并联转接。接口板是无源总线展开电路，通过 30 针、24 针、8 针和两组 15 针连接器引出 M5-Bus 的电源、HPWR、BAT、I2C、SPI、UART、I2S、ADC/DAC 和 GPIO。

## 检索关键词

`Faces Bottom`、`A009`、`IP5306`、`BATTERY`、`BAT`、`600mAh`、`VOUT`、`SW`、`1uH`、`M5_BUS`、`M5_BUS 30 PIN`、`M5_BUS 24 PIN`、`M5_BUS 15 PIN`、`M5_BUS 8 PIN`、`SDA`、`SCL`、`MOSI`、`MISO`、`SCK`、`RXD0`、`TXD0`、`RXD2`、`TXD2`、`HPWR`、`HPR`、`+5`、`3.3V`、`Pogo Pin`、`BUS1`、`BUS2`、`P1`、`P2`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | IP5306 | 充电板的电池充放电与升压电源管理器 | 图 64fe8969ae3b / 第 1 页 / 页面左半充电板中央 U1，器件值 IP5306，标注 VIN、VOUT、SW、BAT、KEY、LED1-LED3、EP |
| P1 | BATTERY | 两针电池连接器，连接 BAT 与 GND | 图 64fe8969ae3b / 第 1 页 / 页面左半充电板下方 P1 BATTERY，两针分别连接 U1 BAT 网络和 GND |
| P2 | 4 PIN | 四针充电/扩展触点，引出 +5、GND、SDA 和 SCL | 图 64fe8969ae3b / 第 1 页 / 页面左半充电板下方 P2 4 PIN，pin 1 接 +5，pin 2 接 GND，pin 3/4 接 BUS1 SDA/SCL 线路 |
| BUS1,BUS2 | M5_BUS 24 PIN | 充电板上的两组并联 24 针 M5-Bus 连接器 | 图 64fe8969ae3b / 第 1 页 / 页面左侧 BUS1、BUS2 M5_BUS 24 针连接器及逐针蓝色并联连线 |
| L1,R1 | 1uH; 2R | IP5306 SW/VOUT 升压功率路径元件 | 图 64fe8969ae3b / 第 1 页 / 页面左半 U1 右侧 L1 1uH 与 R1 2R，位于 SW/VOUT 功率节点 |
| C1 (总线输入处) | 100uF/35V | 充电板总线电源到 GND 的极性储能电容 | 图 64fe8969ae3b / 第 1 页 / 页面左上 BUS1/BUS2 旁的极性电容，标注 +C1 100uF/35V |
| C1 (U1 输出处) | 106 | IP5306 VOUT 节点到 GND 的输出滤波电容之一 | 图 64fe8969ae3b / 第 1 页 / 页面左半 U1 右侧 VOUT 节点的电容，标注 C1 106，与 C2 并联 |
| C2-C5 | 106 | IP5306 输入、BAT 和 VOUT 电源滤波电容 | 图 64fe8969ae3b / 第 1 页 / 页面左半 U1 周围 C2、C3、C4、C5，均标注 106 并分别接 +5、BAT/VOUT 与 GND |
| BUS? 30 PIN | M5_BUS 30 PIN | 接口板 30 针 M5-Bus 主连接器 | 图 64fe8969ae3b / 第 1 页 / 页面右上接口板的 M5_BUS 30 PIN，pin 1-30 展开 BAT、5V、HPWR、GPIO、I2C、UART、I2S 和 GND |
| BUS? 24 PIN | M5_BUS 24 PIN | 接口板 24 针 FACES 总线连接器 | 图 64fe8969ae3b / 第 1 页 / 页面右中接口板的 M5_BUS 24 PIN，标注 GND、AD35/36、DA25/26、SPI、I2S、SDA/SCL、HPR、BAT |
| BUS? 8 PIN | M5_BUS 8 PIN | 接口板 8 针电源、I2C 和 SPI 扩展连接器 | 图 64fe8969ae3b / 第 1 页 / 页面右上 M5_BUS 8 PIN，pin 1-8 标注 5V、3.3V、GND、G21/IIS_SDA、G22/IIC_SCL、G23/MOSI、G19/MISO、G18/SCK |
| BUS? 15 PIN x2 | M5_BUS 15 PIN | 两组并列 GPIO、UART、ADC/DAC 和电源扩展连接器 | 图 64fe8969ae3b / 第 1 页 / 页面最右侧两组 M5_BUS 15 PIN，均标注 RXD0/TXD0、RXD2/TXD2、G2/G5、DAC、ADC、EN/RST、BAT、3.3V、5V、GND |

## 系统结构

### Faces Bottom 系统架构

充电板由 U1 IP5306、P1 电池连接器、P2 四针触点及 BUS1/BUS2 24 针连接器组成；接口板没有有源器件，通过 30/24/8/15 针连接器展开 M5-Bus 电源和信号。

- 参数与网络：`power_manager=U1 IP5306`；`battery_connector=P1 BATTERY`；`pogo_connector=P2 4 PIN`；`charging_board_bus=BUS1,BUS2 M5_BUS 24 PIN`；`interface_board_connectors=M5_BUS 30 PIN,24 PIN,8 PIN,15 PIN x2`；`interface_board_active_ic_visible=false`
- 证据：图 64fe8969ae3b / 第 1 页 / 完整单页：左侧充电板与右侧接口板两个大区

## 电源

### U1 +5V 输入

U1 VIN/pin 1 连接 +5，C3 106 从 +5 连接至 GND；U1 EP/pin 9 连接 GND。LED1、LED2、LED3 引脚在本页无外部连线。

- 参数与网络：`controller=U1 IP5306`；`input_pin=pin 1/VIN`；`input_rail=+5`；`input_capacitor=C3 106`；`exposed_pad=pin 9/EP to GND`；`unused_status_pins=LED1 pin 2,LED2 pin 3,LED3 pin 4`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面左半 U1 IP5306 左侧 VIN/LED1-3、上方 EP/GND 与 C3

### P1 BAT 电池网络

U1 BAT/pin 6 连接 P1 BATTERY 正端及 C4、C5 106 电容网络，P1 另一端和电容返回端连接 GND。

- 参数与网络：`battery_pin=U1 pin 6/BAT`；`connector=P1 BATTERY`；`battery_filter=C4 106,C5 106`；`return=GND`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面左半 U1 BAT pin 6、C4/C5 与下方 P1 BATTERY/GND 连线

### U1 SW/VOUT 功率级

U1 SW/pin 7 经 L1 1uH 和 R1 2R 连接 VOUT 功率节点，U1 VOUT/pin 8 连接该输出节点；C1、C2 均为 106，从输出节点连接至 GND。

- 参数与网络：`switch_pin=U1 pin 7/SW`；`output_pin=U1 pin 8/VOUT`；`inductor=L1 1uH`；`series_resistor=R1 2R`；`output_capacitors=C1 106,C2 106`；`return=GND`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面左半 U1 SW/VOUT、L1/R1 与 C1/C2 功率路径

## 接口

### P2 四针充电/扩展触点

P2 pin 1 连接 +5，pin 2 连接 GND，pin 3、pin 4 分别连接 BUS1 的 SDA、SCL 线路。

- 参数与网络：`reference=P2 4 PIN`；`pinout=1:+5,2:GND,3:SDA,4:SCL`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面左半下方 P2 pin 1-4 与 +5/GND、BUS1 pin 16 SDA、pin 18 SCL 连线

### BUS1/BUS2 24 针并联总线

BUS1 与 BUS2 的对应 24 针通过蓝色连线并联，信号包括 GND、5V、3V3、AD35、AD36、DA25、DA26、MOSI、MISO、SCK、R2/16、T2/17、SDA、SCL、I2S SK/WS/OUT/MK/IN、G2、G5、HPR、BAT 和 NC。

- 参数与网络：`connectors=BUS1,BUS2`；`type=M5_BUS 24 PIN`；`parallel=true`；`pinout=1:GND,2:5V,3:AD35,4:3V3,5:AD36,6:MOSI,7:DA25,8:MISO,9:DA26,10:SCK,11:SK,12:R2/16,13:WS,14:T2/17,15:OUT,16:SDA,17:MK,18:SCL,19:IN,20:G2,21:HPR,22:G5,23:BAT,24:NC`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面左侧 BUS1/BUS2 pin 1-24 的名称与逐针并联蓝线

### 接口板 M5_BUS 30 PIN

30 针连接器引出 BAT、5V、3.3V、HPWR/HPR、GND，以及 G34、G0、G13、G5、G22、G17、G1、G26、G25、EN/RST、G36、G35、G15、G12、G2、G21、G16、G3、G18、G19、G23 网络。

- 参数与网络：`pinout=1:BAT,2:HPR/HPWR,3:5V,4:HPR/HPWR,5:G34/IIS_IN,6:HPR/HPWR,7:G0/IIS_MK,8:G15/IIS_OUT,9:G13/IIS_WS,10:G12/IIS_SK,11:G5,12:G2,13:G22/IIC_SCL,14:G21/IIS_SDA,15:G17/TXD2,16:G16/RXD2,17:G1/TXD0,18:G3/RXD0,19:3.3V,20:G18/SCK,21:G26/DAC,22:G19/MISO,23:G25/DAC,24:G23/MOSI,25:EN/RST,26:GND,27:G36/ADC,28:GND,29:G35/ADC,30:GND`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面右上接口板 M5_BUS 30 PIN 的 pin 1-30 名称与 HPR 外部网络

### 接口板 M5_BUS 24 PIN

接口板 24 针连接器与充电板 24 针定义一致，并在 pin 21 将 HPR 引出；pin 23 为 BAT，pin 24 标为 *NC。

- 参数与网络：`pinout=1:GND,2:5V,3:AD35,4:3V3,5:AD36,6:MOSI,7:DA25,8:MISO,9:DA26,10:SCK,11:SK,12:R2/16,13:WS,14:T2/17,15:OUT,16:SDA,17:MK,18:SCL,19:IN,20:G2,21:HPR,22:G5,23:BAT,24:*NC`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面右中接口板 M5_BUS 24 PIN 的 pin 1-24 名称与 HPR 线

### 接口板 M5_BUS 8 PIN

8 针连接器依次引出 5V、3.3V、GND、G21/IIS_SDA、G22/IIC_SCL、G23/MOSI、G19/MISO、G18/SCK。

- 参数与网络：`pinout=1:5V,2:3.3V,3:GND,4:G21/IIS_SDA,5:G22/IIC_SCL,6:G23/MOSI,7:G19/MISO,8:G18/SCK`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面右上 M5_BUS 8 PIN 的 pin 1-8 标注

### 接口板两组 M5_BUS 15 PIN

两组 15 针连接器具有相同定义，依次引出 G3/RXD0、G1/TXD0、G16/RXD2、G17/TXD2、G2、G5、G25/DAC、G26/DAC、G35/ADC、G36/ADC、EN/RST、BAT、3.3V、5V、GND。

- 参数与网络：`count=2`；`pinout=1:G3/RXD0,2:G1/TXD0,3:G16/RXD2,4:G17/TXD2,5:G2,6:G5,7:G25/DAC,8:G26/DAC,9:G35/ADC,10:G36/ADC,11:EN/RST,12:BAT,13:3.3V,14:5V,15:GND`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面最右两组并列 M5_BUS 15 PIN 的相同 pin 1-15 标注

## 总线

### SDA/SCL 被动路由

SDA、SCL 在充电板 BUS1/BUS2 pin 16/18 与 P2 pin 3/4 间路由；接口板 30 针连接器使用 G21/IIS_SDA pin 14 和 G22/IIC_SCL pin 13，8 针连接器使用 pin 4/5，24 针连接器使用 pin 16/18。原理图未显示 I2C 从机或地址。

- 参数与网络：`charging_bus=BUS1/BUS2 pin 16:SDA,pin 18:SCL`；`pogo=P2 pin 3:SDA,pin 4:SCL`；`interface_30pin=pin 14:G21/IIS_SDA,pin 13:G22/IIC_SCL`；`interface_8pin=pin 4:G21/IIS_SDA,pin 5:G22/IIC_SCL`；`interface_24pin=pin 16:SDA,pin 18:SCL`；`i2c_device_visible=false`；`address_visible=false`
- 证据：图 64fe8969ae3b / 第 1 页 / 完整单页各连接器的 SDA/SCL、G21/G22 标注及 P2 路由

### MOSI/MISO/SCK 被动路由

24 针连接器在 pin 6、8、10 引出 MOSI、MISO、SCK；30 针连接器在 pin 24、22、20 引出 G23/MOSI、G19/MISO、G18/SCK；8 针连接器在 pin 6、7、8 引出同组三线。

- 参数与网络：`interface_24pin=6:MOSI,8:MISO,10:SCK`；`interface_30pin=24:G23/MOSI,22:G19/MISO,20:G18/SCK`；`interface_8pin=6:G23/MOSI,7:G19/MISO,8:G18/SCK`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面左右 24 针、右上 30 针和 8 针连接器的 MOSI/MISO/SCK 标注

### UART0/UART2 被动路由

30 针连接器 pin 17/18 引出 G1/TXD0、G3/RXD0，pin 15/16 引出 G17/TXD2、G16/RXD2；两组 15 针连接器分别在 pin 2/1 和 pin 4/3 引出相同 UART0/UART2 信号。

- 参数与网络：`interface_30pin=15:G17/TXD2,16:G16/RXD2,17:G1/TXD0,18:G3/RXD0`；`interface_15pin=1:G3/RXD0,2:G1/TXD0,3:G16/RXD2,4:G17/TXD2`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面右侧 30 针和两组 15 针连接器的 RXD0/TXD0/RXD2/TXD2 标注

## 保护电路

### 电池、电源和外部接口保护可见性

该页未绘出独立保险丝、TVS、ESD 或反接保护器件；电池保护是否集成在电芯或 IP5306 外部不可由本页确定。

- 参数与网络：`fuse_visible=false`；`tvs_visible=false`；`esd_visible=false`；`reverse_protection_visible=false`；`external_battery_protection_visible=false`
- 证据：图 64fe8969ae3b / 第 1 页 / 完整单页 U1/P1/P2/BUS1/BUS2 和接口板全部外围器件

## 关键网络

### HPWR/HPR 总线

接口板 30 针连接器 pin 2、4、6 的 HPWR 共同连接 HPR 网络，24 针连接器 pin 21 也连接 HPR。

- 参数与网络：`interface_30pin=pin 2,4,6 HPWR`；`interface_24pin=pin 21 HPR`；`net=HPR`
- 证据：图 64fe8969ae3b / 第 1 页 / 页面右侧 30 针 HPWR pin 2/4/6 与 24 针 pin 21 HPR 外部网络标注

## 其他事实

### 控制、时钟、复位、调试和存储可见性

该页未绘出主控制器、协处理器、晶体、复位电路、BOOT 电路、调试接口、独立存储器、音频、传感器或射频器件。

- 参数与网络：`controller_visible=false`；`clock_visible=false`；`reset_visible=false`；`boot_visible=false`；`debug_visible=false`；`storage_visible=false`；`audio_visible=false`；`sensor_visible=false`；`rf_visible=false`
- 证据：图 64fe8969ae3b / 第 1 页 / 完整单页器件清单仅含 IP5306、电池/电源无源件和被动连接器

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Faces Bottom 系统架构 | `power_manager=U1 IP5306`；`battery_connector=P1 BATTERY`；`pogo_connector=P2 4 PIN`；`charging_board_bus=BUS1,BUS2 M5_BUS 24 PIN`；`interface_board_connectors=M5_BUS 30 PIN,24 PIN,8 PIN,15 PIN x2`；`interface_board_active_ic_visible=false` |
| 电源 | U1 +5V 输入 | `controller=U1 IP5306`；`input_pin=pin 1/VIN`；`input_rail=+5`；`input_capacitor=C3 106`；`exposed_pad=pin 9/EP to GND`；`unused_status_pins=LED1 pin 2,LED2 pin 3,LED3 pin 4` |
| 电源 | P1 BAT 电池网络 | `battery_pin=U1 pin 6/BAT`；`connector=P1 BATTERY`；`battery_filter=C4 106,C5 106`；`return=GND` |
| 电源 | 内置电池容量 | `documented_capacity=600mAh`；`schematic_capacity_visible=false`；`cell_part_number_visible=false` |
| 电源 | U1 SW/VOUT 功率级 | `switch_pin=U1 pin 7/SW`；`output_pin=U1 pin 8/VOUT`；`inductor=L1 1uH`；`series_resistor=R1 2R`；`output_capacitors=C1 106,C2 106`；`return=GND` |
| 核心器件 | C1 位号重复 | `first_occurrence=C1 100uF/35V at bus input`；`second_occurrence=C1 106 at U1 VOUT`；`duplicate_reference=C1` |
| 接口 | P2 四针充电/扩展触点 | `reference=P2 4 PIN`；`pinout=1:+5,2:GND,3:SDA,4:SCL` |
| 接口 | BUS1/BUS2 24 针并联总线 | `connectors=BUS1,BUS2`；`type=M5_BUS 24 PIN`；`parallel=true`；`pinout=1:GND,2:5V,3:AD35,4:3V3,5:AD36,6:MOSI,7:DA25,8:MISO,9:DA26,10:SCK,11:SK,12:R2/16,13:WS,14:T2/17,15:OUT,16:SDA,17:MK,18:SCL,19:IN,20:G2,21:HPR,22:G5,23:BAT,24:NC` |
| 接口 | 接口板 M5_BUS 30 PIN | `pinout=1:BAT,2:HPR/HPWR,3:5V,4:HPR/HPWR,5:G34/IIS_IN,6:HPR/HPWR,7:G0/IIS_MK,8:G15/IIS_OUT,9:G13/IIS_WS,10:G12/IIS_SK,11:G5,12:G2,13:G22/IIC_SCL,14:G21/IIS_SDA,15:G17/TXD2,16:G16/RXD2,17:G1/TXD0,18:G3/RXD0,19:3.3V,20:G18/SCK,21:G26/DAC,22:G19/MISO,23:G25/DAC,24:G23/MOSI,25:EN/RST,26:GND,27:G36/ADC,28:GND,29:G35/ADC,30:GND` |
| 接口 | 接口板 M5_BUS 24 PIN | `pinout=1:GND,2:5V,3:AD35,4:3V3,5:AD36,6:MOSI,7:DA25,8:MISO,9:DA26,10:SCK,11:SK,12:R2/16,13:WS,14:T2/17,15:OUT,16:SDA,17:MK,18:SCL,19:IN,20:G2,21:HPR,22:G5,23:BAT,24:*NC` |
| 接口 | 接口板 M5_BUS 8 PIN | `pinout=1:5V,2:3.3V,3:GND,4:G21/IIS_SDA,5:G22/IIC_SCL,6:G23/MOSI,7:G19/MISO,8:G18/SCK` |
| 接口 | 接口板两组 M5_BUS 15 PIN | `count=2`；`pinout=1:G3/RXD0,2:G1/TXD0,3:G16/RXD2,4:G17/TXD2,5:G2,6:G5,7:G25/DAC,8:G26/DAC,9:G35/ADC,10:G36/ADC,11:EN/RST,12:BAT,13:3.3V,14:5V,15:GND` |
| 总线 | SDA/SCL 被动路由 | `charging_bus=BUS1/BUS2 pin 16:SDA,pin 18:SCL`；`pogo=P2 pin 3:SDA,pin 4:SCL`；`interface_30pin=pin 14:G21/IIS_SDA,pin 13:G22/IIC_SCL`；`interface_8pin=pin 4:G21/IIS_SDA,pin 5:G22/IIC_SCL`；`interface_24pin=pin 16:SDA,pin 18:SCL`；`i2c_device_visible=false`；`address_visible=false` |
| 总线 | MOSI/MISO/SCK 被动路由 | `interface_24pin=6:MOSI,8:MISO,10:SCK`；`interface_30pin=24:G23/MOSI,22:G19/MISO,20:G18/SCK`；`interface_8pin=6:G23/MOSI,7:G19/MISO,8:G18/SCK` |
| 总线 | UART0/UART2 被动路由 | `interface_30pin=15:G17/TXD2,16:G16/RXD2,17:G1/TXD0,18:G3/RXD0`；`interface_15pin=1:G3/RXD0,2:G1/TXD0,3:G16/RXD2,4:G17/TXD2` |
| 关键网络 | HPWR/HPR 总线 | `interface_30pin=pin 2,4,6 HPWR`；`interface_24pin=pin 21 HPR`；`net=HPR` |
| 保护电路 | 电池、电源和外部接口保护可见性 | `fuse_visible=false`；`tvs_visible=false`；`esd_visible=false`；`reverse_protection_visible=false`；`external_battery_protection_visible=false` |
| 其他事实 | 控制、时钟、复位、调试和存储可见性 | `controller_visible=false`；`clock_visible=false`；`reset_visible=false`；`boot_visible=false`；`debug_visible=false`；`storage_visible=false`；`audio_visible=false`；`sensor_visible=false`；`rf_visible=false` |

## 待确认事项

- `power.battery-capacity`：产品正文记载内置 600mAh 可充电锂电池，但原理图只画出 P1 BATTERY 与 BAT 网络，未打印容量或电芯型号。（证据：图 64fe8969ae3b / 第 1 页 / 页面左半 P1 BATTERY 与 U1 BAT 网络，未附容量或电芯型号）
- `component.duplicate-c1-reference`：同一页左上总线输入处标有 C1 100uF/35V，U1 输出处另有 C1 106；两处使用相同位号但数值和位置不同。（证据：图 64fe8969ae3b / 第 1 页 / 页面左上 BUS1/BUS2 旁 +C1 100uF/35V; 图 64fe8969ae3b / 第 1 页 / 页面左半 U1 右侧 VOUT 节点 C1 106）
- `review.battery-capacity`：Faces Bottom 内置电池容量是否确认为产品正文记载的 600mAh，电芯具体型号是什么？；原因：原理图只标出 BATTERY 连接器和 BAT 网络，没有容量或电芯料号。
- `review.duplicate-c1-reference`：BOM/PCB 中总线输入处 100uF/35V 电容与 U1 输出处 106 电容的正确独立位号分别是什么？；原因：原理图同一页将两个不同位置、不同数值的器件都标为 C1。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `64fe8969ae3bafbbb7e04d506522667176d5bb911594b977e1a6abc4bd465f9b` | `https://static-cdn.m5stack.com/resource/docs/products/module/faces/faces_sch_01.webp` |

---

源文档：`zh_CN/module/faces.md`

源文档 SHA-256：`fc110d86d0f2fb9dee2120ab30fe5bf7336722982f926000c83c78bf077614ea`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
