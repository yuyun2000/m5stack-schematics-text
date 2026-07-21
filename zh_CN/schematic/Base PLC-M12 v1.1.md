# Base PLC-M12 v1.1 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base PLC-M12 v1.1 |
| SKU | K011-B-V11 |
| 产品 ID | `base-plc-m12-v1-1-a0933a0b5bdd` |
| 源文档 | `zh_CN/module/PLC-M12 Base v1.1.md` |

## 概述

Base PLC-M12 v1.1 主板从 J2 PWR3.5 经 F1 PPTC-1812 接收 IN+，U6 TPS54360 配合 L1 8.2uH 与 D6 B290B 生成 +5V，并向 J1 M5Stack_BUS、J3 IIC_Socket_4P 和扩展连接器供电。主板 P1 HDR_4P 引出 B-/A+/12V+/12V-，P2 HDR_6P 引出 I/O_01 至 I/O_06。RS-485 子板以 U1 SP485EEN-L/TR 为收发器，A/B 接 4 针端子，R1/R5 提供总线偏置，Q1 SS8050 Y1 由 TX 驱动并控制 /RE/DE。

## 检索关键词

`Base PLC-M12 v1.1`、`K011-B-V11`、`PLC-M12`、`TPS54360`、`SP485EEN-L/TR`、`SS8050 Y1`、`RS-485`、`RS485_A`、`RS485_B`、`RX`、`TX`、`DE`、`RE`、`DI`、`RO`、`IN+`、`IN12/24V`、`+5V`、`12V+`、`12V-`、`PPTC-1812`、`B290B`、`L1 8.2uH`、`M5Stack_BUS`、`GPIO16`、`GPIO17`、`SDA`、`SCL`、`IIC_Socket_4P`、`I/O_01`、`I/O_02`、`I/O_03`、`I/O_04`、`I/O_05`、`I/O_06`、`HDR_4P`、`HDR_6P`、`HPWR`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U6 | TPS54360 | IN+ 至 +5V 的降压转换器 | 图 acb19df9e443 / 第 1 页 / 主板页左上 U6 TPS54360，VIN/BOOT/SW/FB/COMP/RT-CLK/GND-PWRPD 引脚与 L1/D6 周边 |
| J2,F1 | PWR3.5; PPTC-1812 | 外部电源输入连接器与自恢复保险丝 | 图 acb19df9e443 / 第 1 页 / 主板页左上 J2 PWR3.5，正端经 F1 PPTC-1812 到 IN+，其余端接 GND |
| L1,D6 | 8.2uH; B290B | TPS54360 输出电感与续流肖特基二极管 | 图 acb19df9e443 / 第 1 页 / 主板页 U6 右侧 D6 B290B 从 SW 节点到 GND，L1 8.2uH 串联至 +5V |
| J1 | M5Stack_BUS | 30 针主机堆叠总线，承载 RS485 UART、I2C、IN+/HPWR 与 +5V | 图 acb19df9e443 / 第 1 页 / 主板页右下 J1 M5Stack_BUS，pin 1-30 与外部网络名 |
| P1 | HDR_4P | RS-485 A/B 与 12V 电源板间接口 | 图 acb19df9e443 / 第 1 页 / 主板页中下 P1 HDR_4P，pin 1-4 为 B-、A+、12V+、12V- |
| P2 | HDR_6P | 六路通用扩展 I/O 排针 | 图 acb19df9e443 / 第 1 页 / 主板页中下 P2 HDR_6P，pin 1-6 为 I/O_01 至 I/O_06 |
| J3 | IIC_Socket_4P | SCL/SDA/+5V/GND 的四针 I2C 扩展接口 | 图 acb19df9e443 / 第 1 页 / 主板页右中 J3 IIC_Socket_4P，pin 1 SCL、2 SDA、3 +5V、4 GND |
| D5,R20 | EXT 0603; 4.7KΩ | +5V 电源状态指示支路 | 图 acb19df9e443 / 第 1 页 / 主板页右中 +5V 经 D5 EXT 0603 与 R20 4.7KΩ 串联到 GND |
| U1 | SP485EEN-L/TR | TTL/UART 到半双工 RS-485 的收发器 | 图 8d2356549ea4 / 第 1 页 / RS485 页中央 U1 SP485EEN-L/TR，RO,/RE,DE,DI,A,B,VCC,GND 引脚 |
| Q1 | SS8050 Y1 | 由 TX 经 R4 驱动的 /RE 与 DE 方向控制晶体管 | 图 8d2356549ea4 / 第 1 页 / RS485 页左侧 Q1 SS8050 Y1，基极经 R4 1KΩ 接 TX，集电极接 /RE+DE，发射极接 GND |
| R1,R5 | 4.7KΩ; 4.7KΩ | RS485_B 下拉与 RS485_A 上拉偏置 | 图 8d2356549ea4 / 第 1 页 / RS485 页 U1 右侧 R1 4.7KΩ 从 B 到 GND，R5 4.7KΩ 从 A 到 +5V |
| J1 | HDR_4P_3.96 | RS485_B、RS485_A、12V+、12V- 外部端子 | 图 8d2356549ea4 / 第 1 页 / RS485 页右侧 J1 HDR_4P_3.96，pin 1-4 标 B、A、12V+、12V-，12V- 接 GND |

## 系统结构

### Base PLC-M12 v1.1 架构

主板将外部 IN+ 降压为 +5V，并提供 M5-Bus、I2C、六路 I/O 与 RS485/12V 板间接口；独立转接板使用 SP485EEN-L/TR 和 SS8050 实现 TTL 控制及 A/B 差分接口。

- 参数与网络：`main_converter=U6 TPS54360`；`host_bus=J1 M5Stack_BUS`；`i2c=J3 IIC_Socket_4P`；`io_header=P2 HDR_6P`；`rs485=U1 SP485EEN-L/TR`；`direction_control=Q1 SS8050 Y1`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页完整电源与连接器电路; 图 8d2356549ea4 / 第 1 页 / RS485 页完整收发器、方向控制和端子电路

## 电源

### IN+ 输入与保护

J2 PWR3.5 pin 1 经 F1 PPTC-1812 进入 IN+，J2 pin 2、3 接 GND；C5、C6 各 2.2uF 并联在 IN+ 与 GND 之间。

- 参数与网络：`connector=J2 PWR3.5`；`positive=pin 1 -> F1 PPTC-1812 -> IN+`；`ground=pins 2,3`；`input_caps=C5 2.2uF,C6 2.2uF`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页左上 J2/F1/C5/C6/IN+

### U6 +5V 降压转换

U6 TPS54360 的 VIN 接 IN+，SW 经 L1 8.2uH 输出 +5V，D6 B290B 从开关节点接 GND；R28 51KΩ 与 R30 10KΩ 构成 FB 分压，R27 12KΩ/C4 6.8nF 连接 COMP，R29 160KΩ 连接 RT/CLK。

- 参数与网络：`input=IN+`；`converter=U6 TPS54360`；`switch=pin 8/SW`；`inductor=L1 8.2uH`；`diode=D6 B290B`；`output=+5V`；`feedback=R28 51KΩ,R30 10KΩ`；`compensation=R27 12KΩ,C4 6.8nF`；`frequency_resistor=R29 160KΩ`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页左上 U6、L1、D6、R27-R30、C1-C4 与 +5V

### M5-Bus 电源分配

IN+ 连接 J1 pin 25、27、29 的 HPWR；+5V 连接 J1 pin 28，并在图中也标到 pin 30 外部网络；J1 pin 12 标 +3.3V，pin 1、3、5 接 GND。

- 参数与网络：`hpwr=IN+ -> J1 pins 25,27,29`；`five_volt=J1 pin 28 and shown external +5V at pin 30`；`three3=J1 pin 12/+3.3V`；`ground=J1 pins 1,3,5`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页右下 J1 HPWR/IN+、+5V、+3.3V 与 GND 针脚

### RS-485 收发器供电

U1 SP485EEN-L/TR 的 VCC 接 +5V、GND 接地，C1 100nF 并联在 +5V 与 GND 之间；J1 的 12V+ 仅引出到端子，12V- 接 GND，未为 U1 供电。

- 参数与网络：`transceiver_supply=+5V`；`decoupling=C1 100nF`；`terminal_supply=J1 pin 3/12V+ passthrough`；`terminal_return=J1 pin 4/12V- -> GND`
- 证据：图 8d2356549ea4 / 第 1 页 / RS485 页 U1 VCC/GND/C1 与 J1 12V+/12V-

## 接口

### J1 M5Stack_BUS 完整针脚

J1 奇数针为 1 GND、3 GND、5 GND、7 GPIO23、9 GPIO19、11 GPIO18、13 GPIO3、15 GPIO16、17 GPIO21、19 GPIO2、21 GPIO12、23 GPIO15、25 HPWR、27 HPWR、29 HPWR；偶数针为 2 GPIO35、4 GPIO36、6 EN、8 GPIO25、10 GPIO26、12 +3.3V、14 GPIO1、16 GPIO17、18 GPIO22、20 GPIO5、22 GPIO13、24 GPIO0、26 GPIO34、28 +5V、30 BATTERY。

- 参数与网络：`odd_pins=1:GND,3:GND,5:GND,7:GPIO23,9:GPIO19,11:GPIO18,13:GPIO3,15:GPIO16,17:GPIO21,19:GPIO2,21:GPIO12,23:GPIO15,25:HPWR,27:HPWR,29:HPWR`；`even_pins=2:GPIO35,4:GPIO36,6:EN,8:GPIO25,10:GPIO26,12:+3.3V,14:GPIO1,16:GPIO17,18:GPIO22,20:GPIO5,22:GPIO13,24:GPIO0,26:GPIO34,28:+5V,30:BATTERY`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页右下 J1 M5Stack_BUS pin 1-30

### P1 RS485 与 12V 板间接口

P1 HDR_4P pin 1 为 B-、pin 2 为 A+、pin 3 为 12V+、pin 4 为 12V-；RS485 子板 J1 使用相同顺序 B、A、12V+、12V-，其中 12V- 接 GND。

- 参数与网络：`main_header=P1 HDR_4P`；`pinout=1:B-/RS485_B,2:A+/RS485_A,3:12V+,4:12V-/GND`；`daughter_header=J1 HDR_4P_3.96`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页中下 P1 B-/A+/12V+/12V-; 图 8d2356549ea4 / 第 1 页 / RS485 页右侧 J1 B/A/12V+/12V-

### P2 六路 I/O 排针

P2 HDR_6P pin 1-6 依次连接 I/O_01、I/O_02、I/O_03、I/O_04、I/O_05、I/O_06；本页未画这些网络到 M5-Bus GPIO 或外部保护/驱动电路。

- 参数与网络：`pinout=1:I/O_01,2:I/O_02,3:I/O_03,4:I/O_04,5:I/O_05,6:I/O_06`；`m5bus_mapping_visible=false`；`protection_visible=false`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页中下 P2 HDR_6P 与六个 I/O 网络

## 总线

### M5-Bus I2C 与 J3 扩展

J1 pin 17/GPIO21 连接 SDA，pin 18/GPIO22 连接 SCL；SDA/SCL 分别进入 J3 pin 2/IIC_SDA 与 pin 1/IIC_SCL，J3 pin 3 为 +5V、pin 4 为 GND。图中未显示 I2C 上拉电阻或设备地址。

- 参数与网络：`controller_sda=J1 pin 17/GPIO21 -> SDA -> J3 pin 2`；`controller_scl=J1 pin 18/GPIO22 -> SCL -> J3 pin 1`；`supply=J3 pin 3/+5V`；`ground=J3 pin 4/GND`；`pullups_visible=false`；`address_visible=false`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页右中 J3 与右下 J1 SDA/SCL 网络

### RS-485 接收路径

U1 pin 6/A 与 pin 7/B 连接 RS485_A/RS485_B；pin 1/RO 经 R2 1KΩ 输出 RX。R1 4.7KΩ 将 B 下拉到 GND，R5 4.7KΩ 将 A 上拉到 +5V。

- 参数与网络：`transceiver=U1 SP485EEN-L/TR`；`a=pin 6 -> RS485_A`；`b=pin 7 -> RS485_B`；`receiver_output=pin 1/RO -> R2 1KΩ -> RX`；`bias_b=R1 4.7KΩ to GND`；`bias_a=R5 4.7KΩ to +5V`
- 证据：图 8d2356549ea4 / 第 1 页 / RS485 页 U1 RO/A/B、R2、R1、R5 与 RX/RS485_A/RS485_B

## 总线地址

### 总线地址可见性

两张原理图没有 I2C 设备地址、UART 地址或其他数值总线地址；J3 仅为 I2C 直通接口，RS-485 子板为物理层收发器。

- 参数与网络：`i2c_address_visible=false`；`uart_address_visible=false`；`rs485_node_address_visible=false`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页 J3 SDA/SCL 与所有接口，无地址; 图 8d2356549ea4 / 第 1 页 / RS485 页 U1 收发器，无节点地址

## GPIO 与控制信号

### RS-485 /RE 与 DE 方向控制

U1 pin 2 /RE 与 pin 3 DE 连接同一控制节点；R3 4.7KΩ 将该节点上拉到 +5V，Q1 SS8050 Y1 可将其拉到 GND，Q1 基极由 TX 经 R4 1KΩ 驱动。

- 参数与网络：`control_pins=U1 pin 2 /RE + pin 3 DE`；`pullup=R3 4.7KΩ to +5V`；`transistor=Q1 SS8050 Y1`；`base_drive=TX -> R4 1KΩ -> Q1 base`；`emitter=GND`
- 证据：图 8d2356549ea4 / 第 1 页 / RS485 页左中 TX-R4-Q1-R3-/RE-DE 控制网络

### +5V 指示灯

+5V 经 D5 EXT 0603 和 R20 4.7KΩ 串联到 GND，形成电源存在指示支路。

- 参数与网络：`path=+5V -> D5 EXT 0603 -> R20 4.7KΩ -> GND`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页右中 D5/R20/+5V/GND

## 时钟

### 时钟、复位与调试可见性

两张原理图未绘出 MCU、晶体、振荡器、复位电路、BOOT 开关、SWD/JTAG 或专用调试接口；该底座主要由电源与接口电路构成。

- 参数与网络：`mcu_visible=false`；`crystal_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页完整器件与接口; 图 8d2356549ea4 / 第 1 页 / RS485 页完整器件

## 保护电路

### 主板输入保护可见性

IN+ 输入串联 F1 PPTC-1812 自恢复保险丝；主板未绘出 TVS、反接 MOSFET 或浪涌抑制器。

- 参数与网络：`fuse=F1 PPTC-1812`；`tvs_visible=false`；`reverse_protection_visible=false`；`surge_protection_visible=false`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页 J2 至 IN+ 输入路径及完整电源区

### RS-485 总线保护与终端可见性

RS485_A/RS485_B 配置 R5/R1 偏置，但未绘出 120Ω 终端电阻、TVS、共模电感、保险丝或隔离器。

- 参数与网络：`bias=R5 4.7KΩ to +5V,R1 4.7KΩ to GND`；`termination_visible=false`；`tvs_visible=false`；`common_mode_choke_visible=false`；`galvanic_isolation_visible=false`
- 证据：图 8d2356549ea4 / 第 1 页 / RS485 页 U1 A/B 至 J1 全部外部线路

## 内存与 Flash

### 存储器与内存可见性

两张原理图没有 Flash、EEPROM、RAM、SD 卡或其他存储器件。

- 参数与网络：`flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页完整器件，无存储位号; 图 8d2356549ea4 / 第 1 页 / RS485 页完整器件，无存储位号

## 其他事实

### 其他功能分区可见性

原理图未绘出 SPI、CAN、USB、SDIO、MIPI、I2S、射频、音频、传感器或模拟采样链；主要功能为 DC-DC、I2C 扩展和 RS-485 物理层。

- 参数与网络：`spi_visible=false`；`can_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false`
- 证据：图 acb19df9e443 / 第 1 页 / 主板页完整功能分区; 图 8d2356549ea4 / 第 1 页 / RS485 页完整功能分区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base PLC-M12 v1.1 架构 | `main_converter=U6 TPS54360`；`host_bus=J1 M5Stack_BUS`；`i2c=J3 IIC_Socket_4P`；`io_header=P2 HDR_6P`；`rs485=U1 SP485EEN-L/TR`；`direction_control=Q1 SS8050 Y1` |
| 电源 | IN+ 输入与保护 | `connector=J2 PWR3.5`；`positive=pin 1 -> F1 PPTC-1812 -> IN+`；`ground=pins 2,3`；`input_caps=C5 2.2uF,C6 2.2uF` |
| 电源 | U6 +5V 降压转换 | `input=IN+`；`converter=U6 TPS54360`；`switch=pin 8/SW`；`inductor=L1 8.2uH`；`diode=D6 B290B`；`output=+5V`；`feedback=R28 51KΩ,R30 10KΩ`；`compensation=R27 12KΩ,C4 6.8nF`；`frequency_resistor=R29 160KΩ` |
| 电源 | M5-Bus 电源分配 | `hpwr=IN+ -> J1 pins 25,27,29`；`five_volt=J1 pin 28 and shown external +5V at pin 30`；`three3=J1 pin 12/+3.3V`；`ground=J1 pins 1,3,5` |
| 电源 | 外部输入电压范围 | `documented_range=DC 9-24V`；`schematic_label=IN12/24V`；`confirmed_range=null` |
| 接口 | J1 M5Stack_BUS 完整针脚 | `odd_pins=1:GND,3:GND,5:GND,7:GPIO23,9:GPIO19,11:GPIO18,13:GPIO3,15:GPIO16,17:GPIO21,19:GPIO2,21:GPIO12,23:GPIO15,25:HPWR,27:HPWR,29:HPWR`；`even_pins=2:GPIO35,4:GPIO36,6:EN,8:GPIO25,10:GPIO26,12:+3.3V,14:GPIO1,16:GPIO17,18:GPIO22,20:GPIO5,22:GPIO13,24:GPIO0,26:GPIO34,28:+5V,30:BATTERY` |
| 总线 | M5-Bus I2C 与 J3 扩展 | `controller_sda=J1 pin 17/GPIO21 -> SDA -> J3 pin 2`；`controller_scl=J1 pin 18/GPIO22 -> SCL -> J3 pin 1`；`supply=J3 pin 3/+5V`；`ground=J3 pin 4/GND`；`pullups_visible=false`；`address_visible=false` |
| 接口 | P1 RS485 与 12V 板间接口 | `main_header=P1 HDR_4P`；`pinout=1:B-/RS485_B,2:A+/RS485_A,3:12V+,4:12V-/GND`；`daughter_header=J1 HDR_4P_3.96` |
| 接口 | P2 六路 I/O 排针 | `pinout=1:I/O_01,2:I/O_02,3:I/O_03,4:I/O_04,5:I/O_05,6:I/O_06`；`m5bus_mapping_visible=false`；`protection_visible=false` |
| 总线 | RS-485 接收路径 | `transceiver=U1 SP485EEN-L/TR`；`a=pin 6 -> RS485_A`；`b=pin 7 -> RS485_B`；`receiver_output=pin 1/RO -> R2 1KΩ -> RX`；`bias_b=R1 4.7KΩ to GND`；`bias_a=R5 4.7KΩ to +5V` |
| GPIO 与控制信号 | RS-485 /RE 与 DE 方向控制 | `control_pins=U1 pin 2 /RE + pin 3 DE`；`pullup=R3 4.7KΩ to +5V`；`transistor=Q1 SS8050 Y1`；`base_drive=TX -> R4 1KΩ -> Q1 base`；`emitter=GND` |
| 总线 | RS-485 发送数据路径 | `documented_host_tx=GPIO17/TXD`；`visible_tx_path=TX -> R4 -> Q1 direction control`；`visible_di=U1 pin 4/DI -> GND`；`tx_to_di_visible=false` |
| 总线 | 主机 UART 映射 | `documented_rx=M5Core GPIO16/RXD -> RS485 RXD`；`documented_tx=M5Core GPIO17/TXD -> RS485 TXD`；`main_schematic_cross_connection_visible=false` |
| 电源 | RS-485 收发器供电 | `transceiver_supply=+5V`；`decoupling=C1 100nF`；`terminal_supply=J1 pin 3/12V+ passthrough`；`terminal_return=J1 pin 4/12V- -> GND` |
| 保护电路 | 主板输入保护可见性 | `fuse=F1 PPTC-1812`；`tvs_visible=false`；`reverse_protection_visible=false`；`surge_protection_visible=false` |
| 保护电路 | RS-485 总线保护与终端可见性 | `bias=R5 4.7KΩ to +5V,R1 4.7KΩ to GND`；`termination_visible=false`；`tvs_visible=false`；`common_mode_choke_visible=false`；`galvanic_isolation_visible=false` |
| GPIO 与控制信号 | +5V 指示灯 | `path=+5V -> D5 EXT 0603 -> R20 4.7KΩ -> GND` |
| 总线地址 | 总线地址可见性 | `i2c_address_visible=false`；`uart_address_visible=false`；`rs485_node_address_visible=false` |
| 时钟 | 时钟、复位与调试可见性 | `mcu_visible=false`；`crystal_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false` |
| 内存与 Flash | 存储器与内存可见性 | `flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false` |
| 其他事实 | 其他功能分区可见性 | `spi_visible=false`；`can_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false` |

## 待确认事项

- `power.documented-input-range`：产品正文记载输入范围为 DC 9-24V，主板原理图仅在输入附近标 IN12/24V，没有打印 9V 下限或精确允许范围。（证据：图 acb19df9e443 / 第 1 页 / 主板页左上 J2 输入区域的 IN12/24V 文字）
- `bus.rs485-transmit-path`：产品正文将主机 TXD/GPIO17 映射为 RS485 TXD，但 RS485 栅格原理图中 TX 只清晰连接 R4/Q1 方向控制，U1 pin 4/DI 显示为独立对地连接，未见 TX 到 DI 的数据连线。（证据：图 8d2356549ea4 / 第 1 页 / RS485 页 U1 pin 4/DI、TX/R4/Q1 区域，未见 TX 与 DI 连线）
- `bus.documented-uart-map`：产品正文记载 M5Core RXD/GPIO16 对应 RS485 RXD、TXD/GPIO17 对应 RS485 TXD；主板原理图显示 J1 pin 15/GPIO16 与 pin 16/GPIO17，但未以 RX/TX 网络跨接到 RS485 子板。（证据：图 acb19df9e443 / 第 1 页 / 主板页 J1 pin 15/GPIO16 与 pin 16/GPIO17，无 RX/TX 外部网络; 图 8d2356549ea4 / 第 1 页 / RS485 页独立 RX/TX 网络，未显示 M5-Bus）
- `review.input-range`：Base PLC-M12 v1.1 的正式输入范围是否确认为 DC 9-24V？；原因：主板原理图只标 IN12/24V，没有打印 9V 下限或允许范围。
- `review.rs485-transmit`：RS485 子板的 TX 数据如何连接 U1 pin 4/DI，当前图中 DI 对地连接是否为栅格或版本错误？；原因：TX 只清晰连接 Q1 方向控制，而 U1 DI 未显示 TX 数据连线，无法闭合发送路径。
- `review.uart-map`：M5-Bus GPIO16/GPIO17 到 RS485 子板 RX/TX 的实际板间连接如何实现？；原因：产品正文给出映射，但两张原理图之间没有 RX/TX 板间连接器或同名跨页网络。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `acb19df9e44355fa0186560215bdde2ea7ffd7e7676619f8d9abc61b1febf848` | `https://static-cdn.m5stack.com/resource/docs/products/module/PLC-M12 Base v1.1/img-ebfb57a0-ba41-414a-a0b7-231f89daae07.webp` |
| 2 | 1 | `8d2356549ea4b5ef3b2d5f1672346ea3b1d7ef50fbb9fa185c214df8508326fd` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/PLC-M12%20Base%20v1.1/rs485%E5%8E%9F%E7%90%86%E5%9B%BE.png` |

---

源文档：`zh_CN/module/PLC-M12 Base v1.1.md`

源文档 SHA-256：`4dd5e7a3c0bcf5ea41be5631f79ea67db31bfef634ee9c565aa38d1e943b2885`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
