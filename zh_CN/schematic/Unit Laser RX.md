# Unit Laser RX 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Laser RX |
| SKU | U065 |
| 产品 ID | `unit-laser-rx-d2bc4b24c5c2` |
| 源文档 | `zh_CN/unit/laser-rx.md` |

## 概述

Unit Laser RX 的原理图由 P1 Header 3、J1 GROVE_IO、R1/R2 偏置分压和 C2 去耦组成，没有显示独立放大器、比较器或主控。P1 pin3 接 VCC、pin1 接 GND、pin2 直接连接 J1 pin1 MISO/DOUT；该信号节点由 R1 10KΩ 上拉到 VCC、R2 20KΩ 下拉到 GND，空载静态分压为 VCC 的 2/3。J1 pin2 MOSI 未连接，pin3/pin4 分别为 VCC/GND，C2 100nF 跨接电源。产品正文所述激光晶体管、5V 供电与 140KHz~205KHz 接收频率未直接标在图纸上，需通过实物、BOM 或测试确认。

## 检索关键词

`Unit Laser RX`、`U065`、`laser receiver`、`laser transistor`、`phototransistor`、`P1 Header 3`、`J1 GROVE_IO`、`MISO`、`DOUT`、`MOSI NC`、`VCC`、`5V`、`GND`、`R1 10KΩ`、`R2 20KΩ`、`C2 100nF`、`2/3 VCC divider`、`140KHz`、`205KHz`、`LASER.TX`、`PORT.B`、`digital output`、`free-space optical communication`、`line of sight`、`HY2.0-4P`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| P1 | Header 3 | 连接 VCC、接收信号和 GND 的三针激光接收元件接口 | 图 35fefbbab46a / 第 1 页 / 第 1 页左侧 P1 Header 3 pin1-pin3 |
| J1 | GROVE_IO | 引出 MISO/DOUT、VCC 和 GND 的四针 Grove 接口，MOSI 针脚未连接 | 图 35fefbbab46a / 第 1 页 / 第 1 页右侧 J1 GROVE_IO pin1-pin4 |
| R1 | 10KΩ | P1 pin2/J1 MISO 信号节点到 VCC 的上拉电阻 | 图 35fefbbab46a / 第 1 页 / 第 1 页中央 R1 10KΩ，VCC 到信号节点 |
| R2 | 20KΩ | P1 pin2/J1 MISO 信号节点到 GND 的下拉电阻 | 图 35fefbbab46a / 第 1 页 / 第 1 页中央 R2 20KΩ，信号节点到 GND |
| C2 | 100nF | VCC 到 GND 的电源去耦电容 | 图 35fefbbab46a / 第 1 页 / 第 1 页最右 C2 100nF，VCC 到 GND |

## 系统结构

### Unit Laser RX 系统结构

P1 三针接收元件接口的信号直接连接 J1 MISO/DOUT，并由 R1/R2 偏置；板上仅另有 VCC 去耦，未显示有源放大、比较或数字处理 IC。

- 参数与网络：`sensor_connector=P1 Header 3`；`host_connector=J1 GROVE_IO`；`signal=P1.2 -> J1.1 MISO/DOUT`；`bias=R1 10KΩ to VCC,R2 20KΩ to GND`；`active_signal_ic_shown=false`
- 证据：图 35fefbbab46a / 第 1 页 / 第 1 页完整原理图 P1/R1/R2/J1/C2

## 电源

### VCC 电源轨

J1 pin3 输入 VCC，VCC 连接 P1 pin3、R1 上端和 C2 100nF；J1 pin4/P1 pin1/R2 下端/C2 下端共接 GND，图中没有稳压器、使能或电源开关。

- 参数与网络：`source=J1 pin3`；`vcc_nodes=P1.3,R1,C2`；`ground_nodes=J1.4,P1.1,R2,C2`；`decoupling=C2 100nF`；`regulator_shown=false`；`enable_shown=false`；`power_switch_shown=false`
- 证据：图 35fefbbab46a / 第 1 页 / 第 1 页完整 VCC/GND 网络

## 接口

### P1 Header 3

P1 pin3=VCC、pin2=接收信号节点、pin1=GND；pin2 与 J1 pin1、R1/R2 汇合点同网。

- 参数与网络：`pin_1=GND`；`pin_2=receiver signal / J1 pin1`；`pin_3=VCC`
- 证据：图 35fefbbab46a / 第 1 页 / 第 1 页左侧 P1 pin1-pin3 与信号连线

### J1 GROVE_IO

J1 pin1=MISO 并连接接收输出，pin2=MOSI 但无外部连线，pin3=VCC，pin4=GND；相对外部主机，pin1 为本板到主机的数字/波形输出。

- 参数与网络：`pin_1=MISO / DOUT / unit-to-host`；`pin_2=MOSI / no visible connection`；`pin_3=VCC / power input`；`pin_4=GND`
- 证据：图 35fefbbab46a / 第 1 页 / 第 1 页右侧 J1 pin1-pin4

## 总线地址

### 通信总线与地址

原理图未显示 I2C、SPI、UART、CAN、RS-485、USB 或设备地址；MISO 只是 J1 pin1 的信号标签，图中没有时钟或片选组成 SPI 总线。

- 参数与网络：`i2c_shown=false`；`spi_complete_bus_shown=false`；`uart_shown=false`；`can_shown=false`；`rs485_shown=false`；`usb_shown=false`；`device_address=null`
- 证据：图 35fefbbab46a / 第 1 页 / 第 1 页完整图仅 J1 MISO/MOSI/VCC/GND，其中 MOSI 未连接

## GPIO 与控制信号

### DOUT/MISO 输出

P1 pin2 的接收信号未经缓冲或电平转换直接到 J1 pin1 MISO；J1 pin2 MOSI 不参与本页电路。

- 参数与网络：`source=P1 pin2`；`destination=J1 pin1 MISO/DOUT`；`buffer_shown=false`；`level_shifter_shown=false`；`input_pin_used=false`；`unused_pin=J1 pin2 MOSI`
- 证据：图 35fefbbab46a / 第 1 页 / 第 1 页 P1.2 到 J1.1 直连及 J1.2 无连线

## 时钟

### 时钟、复位与调试

完整原理图未显示晶振、振荡器、时钟网络、RESET、BOOT、调试、下载或测试点。

- 参数与网络：`clock_shown=false`；`crystal_shown=false`；`reset_shown=false`；`boot_shown=false`；`debug_connector_shown=false`；`testpoint_shown=false`
- 证据：图 35fefbbab46a / 第 1 页 / 第 1 页完整图无时钟、复位或调试电路

## 保护电路

### Grove 与接收输入保护

完整原理图未显示 TVS、ESD 阵列、保险丝、反接保护、串联限流或过压钳位；信号节点仅有 R1/R2 偏置。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`series_limiter_shown=false`；`overvoltage_clamp_shown=false`
- 证据：图 35fefbbab46a / 第 1 页 / 第 1 页 P1/J1 全部信号与电源路径

## 关键网络

### 接收输出关键路径

关键路径为 P1 pin2→R1/R2 偏置节点→J1 pin1 MISO/DOUT；供电路径为 J1 pin3 VCC→P1 pin3/C2/R1，回流为 P1 pin1/J1 pin4 GND。

- 参数与网络：`signal_path=P1.2->R1/R2 node->J1.1`；`power_path=J1.3 VCC->P1.3,C2,R1`；`ground_path=P1.1,J1.4,R2,C2`
- 证据：图 35fefbbab46a / 第 1 页 / 第 1 页完整 P1/R1/R2/J1/C2 网络

## 内存与 Flash

### 主控与存储器

完整原理图未显示 MCU、协处理器、Flash、EEPROM、RAM、SD 卡或其他存储器。

- 参数与网络：`mcu_shown=false`；`coprocessor_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false`
- 证据：图 35fefbbab46a / 第 1 页 / 第 1 页完整图仅 P1/J1/R1/R2/C2

## 模拟电路

### 接收输出偏置

接收输出节点由 R1 10KΩ 接 VCC、R2 20KΩ 接 GND；忽略 P1/J1 外部负载时，电阻分压的节点电压为 VCC×20K/(10K+20K)，即约 2/3 VCC。

- 参数与网络：`upper_resistor=R1 10KΩ to VCC`；`lower_resistor=R2 20KΩ to GND`；`unloaded_ratio=2/3 VCC`；`node=P1.2/J1.1 MISO`
- 证据：图 35fefbbab46a / 第 1 页 / 第 1 页中央 R1/R2 与 P1.2/J1.1 公共节点

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Laser RX 系统结构 | `sensor_connector=P1 Header 3`；`host_connector=J1 GROVE_IO`；`signal=P1.2 -> J1.1 MISO/DOUT`；`bias=R1 10KΩ to VCC,R2 20KΩ to GND`；`active_signal_ic_shown=false` |
| 接口 | P1 Header 3 | `pin_1=GND`；`pin_2=receiver signal / J1 pin1`；`pin_3=VCC` |
| 接口 | J1 GROVE_IO | `pin_1=MISO / DOUT / unit-to-host`；`pin_2=MOSI / no visible connection`；`pin_3=VCC / power input`；`pin_4=GND` |
| 模拟电路 | 接收输出偏置 | `upper_resistor=R1 10KΩ to VCC`；`lower_resistor=R2 20KΩ to GND`；`unloaded_ratio=2/3 VCC`；`node=P1.2/J1.1 MISO` |
| GPIO 与控制信号 | DOUT/MISO 输出 | `source=P1 pin2`；`destination=J1 pin1 MISO/DOUT`；`buffer_shown=false`；`level_shifter_shown=false`；`input_pin_used=false`；`unused_pin=J1 pin2 MOSI` |
| 电源 | VCC 电源轨 | `source=J1 pin3`；`vcc_nodes=P1.3,R1,C2`；`ground_nodes=J1.4,P1.1,R2,C2`；`decoupling=C2 100nF`；`regulator_shown=false`；`enable_shown=false`；`power_switch_shown=false` |
| 电源 | J1 VCC 输入电压 | `documented_input=5V`；`schematic_net=VCC`；`voltage_printed_on_schematic=false`；`regulator_shown=false` |
| 传感器 | 激光接收元件 | `documented_element=laser transistor`；`schematic_representation=P1 Header 3`；`part_number_printed=false`；`polarity_printed=false`；`wavelength_printed=false` |
| 传感器 | 激光接收频率范围 | `documented_min_frequency=140KHz`；`documented_max_frequency=205KHz`；`frequency_network_shown=false`；`bandwidth_printed=false` |
| 关键网络 | 接收输出关键路径 | `signal_path=P1.2->R1/R2 node->J1.1`；`power_path=J1.3 VCC->P1.3,C2,R1`；`ground_path=P1.1,J1.4,R2,C2` |
| 保护电路 | Grove 与接收输入保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`series_limiter_shown=false`；`overvoltage_clamp_shown=false` |
| 总线地址 | 通信总线与地址 | `i2c_shown=false`；`spi_complete_bus_shown=false`；`uart_shown=false`；`can_shown=false`；`rs485_shown=false`；`usb_shown=false`；`device_address=null` |
| 时钟 | 时钟、复位与调试 | `clock_shown=false`；`crystal_shown=false`；`reset_shown=false`；`boot_shown=false`；`debug_connector_shown=false`；`testpoint_shown=false` |
| 内存与 Flash | 主控与存储器 | `mcu_shown=false`；`coprocessor_shown=false`；`flash_shown=false`；`eeprom_shown=false`；`ram_shown=false`；`sd_card_shown=false` |

## 待确认事项

- `power.documented-5v-input`：产品正文 Grove 映射将 VCC 标为 5V，但原理图只标 VCC，没有打印标称值或允许范围。（证据：图 35fefbbab46a / 第 1 页 / 第 1 页 J1 pin3 VCC 与 P1/R1/C2，页面无电压数值）
- `sensor.documented-laser-transistor`：产品正文描述内部主要由激光晶体管构成，但原理图仅以 P1 Header 3 表示三针接收元件连接，没有给出光敏晶体管位号、型号、极性或响应波长。（证据：图 35fefbbab46a / 第 1 页 / 第 1 页 P1 Header 3，无光敏器件型号或符号）
- `sensor.documented-frequency`：产品正文列出 140KHz~205KHz 接收频率，原理图未显示频率选择网络、时钟、滤波器或带宽标注，无法由本页确认该范围。（证据：图 35fefbbab46a / 第 1 页 / 第 1 页完整图仅有电阻分压和连接器，无频率标注）
- `review.vcc-input`：请依据整板电气规格或实物确认 J1 VCC 的标称输入为 5V。；原因：5V 来自产品正文 Grove 映射，原理图仅标 VCC。
- `review.receiver-element`：请依据 BOM、PCB 网表或实物确认 P1 所接激光/光敏晶体管的型号、极性和光谱响应。；原因：原理图只画三针 Header，没有展开实际光敏器件。
- `review.receive-frequency`：请依据接收元件数据手册或频率扫描实测确认 140KHz~205KHz 接收范围。；原因：原理图未显示任何频率选择或带宽参数。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `35fefbbab46ae4201891214daa527d56e3fdbacbaa6d567e9b13bbd2215d48d9` | `https://static-cdn.m5stack.com/resource/docs/products/unit/laser-rx/laser-rx_sch_01.webp` |

---

源文档：`zh_CN/unit/laser-rx.md`

源文档 SHA-256：`69d207c71155ba973d043614360681f067464974e9f676e106edb18d83a3498f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
