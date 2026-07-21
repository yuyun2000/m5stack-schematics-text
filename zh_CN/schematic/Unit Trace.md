# Unit Trace 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit Trace |
| SKU | A048 |
| 产品 ID | `unit-trace-b883f0a704ce` |
| 源文档 | `zh_CN/unit/trace.md` |

## 概述

Unit Trace 的本地资源是一张高层信号映射图：四个 SensorArray[0-3] 的 ADIN0-3 分别进入 ATMEGA328 PC0-PC3，四个 LED1-4 分别连接 PD2-PD5。右侧 ESP32 图块表示主机接口，标出 G22/IIC_SCL、G21/IIC_SDA、VCC 与 GND。图中同时把 I2C 连到 ATMEGA328 PD4/PD5，与 LED3/LED4 的 PD4/PD5 重复，实际引脚、0x5A 地址和器件级电路需要复核。

## 检索关键词

`Unit Trace`、`A048`、`ATMEGA328`、`MEGA328`、`SensorArray[0]`、`SensorArray[1]`、`SensorArray[2]`、`SensorArray[3]`、`ADIN0`、`ADIN1`、`ADIN2`、`ADIN3`、`PC0`、`PC1`、`PC2`、`PC3`、`PD2`、`PD3`、`PD4`、`PD5`、`LED1`、`LED2`、`LED3`、`LED4`、`IIC_SCL`、`IIC_SDA`、`G22`、`G21`、`0x5A`、`PORT.A`、`VCC`、`GND`、`line tracking`、`infrared sensor array`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| MCU block | ATMEGA328 | 采集四路 ADIN 信号、驱动四路 LED，并与外部主机交换 I2C 信号的板载控制器 | 图 02d7a98e11c9 / 第 1 页 / 页面中央 ATMEGA328 方框，左侧 PC0-PC3，右侧 PD2-PD5 与上方 I2C 连线 |
| SensorArray[0-3] | 未标注 | 四路地面反射传感阵列块，输出 ADIN0-ADIN3 | 图 02d7a98e11c9 / 第 1 页 / 页面左侧四个 SensorArray[0]/[1]/[2]/[3] 方框与 ADIN0-ADIN3 |
| LED1-LED4 | 未标注 | 由 ATMEGA328 PD2-PD5 分别驱动的四个 LED 图块 | 图 02d7a98e11c9 / 第 1 页 / 页面右下 LED1/LED2/LED3/LED4 图标与 ATMEGA328 PD2/PD3/PD4/PD5 连线 |
| Host block | ESP32 | 外部主机端接口表示，接收 IIC_SCL/IIC_SDA 并提供 VCC/GND | 图 02d7a98e11c9 / 第 1 页 / 页面右上红色 ESP32 图块，G22/IIC_SCL、G21/IIC_SDA、VCC、GND |

## 系统结构

### Unit Trace

图示系统由四个 SensorArray 输入、一个 ATMEGA328 控制块、四个 LED 输出和一个 ESP32 主机接口块组成；页面未展开电阻、电容、传感器型号、电源转换、晶振、复位或保护器件。

- 参数与网络：`controller=ATMEGA328`；`sensor_channels=4`；`sensor_blocks=SensorArray[0-3]`；`led_channels=4`；`host_block=ESP32`；`schematic_level=block/net mapping`；`passives_shown=false`；`clock_shown=false`；`reset_shown=false`；`protection_shown=false`
- 证据：图 02d7a98e11c9 / 第 1 页 / 整页仅含 SensorArray、ATMEGA328、ESP32 和 LED 图块及网络线

## 接口

### ESP32 主机接口块

主机接口块明确标注 G22/IIC_SCL、G21/IIC_SDA、VCC 和 GND，VCC/GND 作为该图唯一可见电源端。

- 参数与网络：`signal_1=G22 IIC_SCL`；`signal_2=G21 IIC_SDA`；`power=VCC`；`ground=GND`；`connector_reference=null`
- 证据：图 02d7a98e11c9 / 第 1 页 / 页面右上 ESP32 图块左侧四条 G22/G21/VCC/GND 连接

## 总线

### ATMEGA328 到 ESP32 I2C

页面把 ATMEGA328 上方 PD4 连到 ESP32 G22/IIC_SCL，把上方 PD5 连到 ESP32 G21/IIC_SDA；两线构成图示主机通信路径。

- 参数与网络：`controller=ATMEGA328 block`；`host=ESP32 block`；`SCL=ATMEGA328 PD4 -> ESP32 G22 IIC_SCL`；`SDA=ATMEGA328 PD5 -> ESP32 G21 IIC_SDA`；`direction=bidirectional bus as drawn`
- 证据：图 02d7a98e11c9 / 第 1 页 / 页面中央上方 PD4/PD5 到右上 G22/IIC_SCL、G21/IIC_SDA 连线

## GPIO 与控制信号

### LED1-LED4

图中 ATMEGA328 PD2 连接 LED1，PD3 连接 LED2，PD4 连接 LED3，PD5 连接 LED4。

- 参数与网络：`PD2=LED1`；`PD3=LED2`；`PD4=LED3`；`PD5=LED4`；`direction=MCU to LED blocks`
- 证据：图 02d7a98e11c9 / 第 1 页 / 页面中央右侧 PD2-PD5 四条线分别到右下 LED1-LED4

## 模拟电路

### SensorArray[0]/[1]

SensorArray[0] 输出 ADIN0 并连接 ATMEGA328 PC0；SensorArray[1] 输出 ADIN1 并连接 PC1。

- 参数与网络：`channel_0=SensorArray[0] ADIN0 -> ATMEGA328 PC0`；`channel_1=SensorArray[1] ADIN1 -> ATMEGA328 PC1`；`direction=sensor to MCU analog input`
- 证据：图 02d7a98e11c9 / 第 1 页 / 页面左上 SensorArray[0]/[1] 的 ADIN0/ADIN1 到中央 PC0/PC1 连线

### SensorArray[2]/[3]

SensorArray[2] 输出 ADIN2 并连接 ATMEGA328 PC2；SensorArray[3] 输出 ADIN3 并连接 PC3。

- 参数与网络：`channel_2=SensorArray[2] ADIN2 -> ATMEGA328 PC2`；`channel_3=SensorArray[3] ADIN3 -> ATMEGA328 PC3`；`direction=sensor to MCU analog input`
- 证据：图 02d7a98e11c9 / 第 1 页 / 页面左下 SensorArray[2]/[3] 的 ADIN2/ADIN3 到中央 PC2/PC3 连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit Trace | `controller=ATMEGA328`；`sensor_channels=4`；`sensor_blocks=SensorArray[0-3]`；`led_channels=4`；`host_block=ESP32`；`schematic_level=block/net mapping`；`passives_shown=false`；`clock_shown=false`；`reset_shown=false`；`protection_shown=false` |
| 模拟电路 | SensorArray[0]/[1] | `channel_0=SensorArray[0] ADIN0 -> ATMEGA328 PC0`；`channel_1=SensorArray[1] ADIN1 -> ATMEGA328 PC1`；`direction=sensor to MCU analog input` |
| 模拟电路 | SensorArray[2]/[3] | `channel_2=SensorArray[2] ADIN2 -> ATMEGA328 PC2`；`channel_3=SensorArray[3] ADIN3 -> ATMEGA328 PC3`；`direction=sensor to MCU analog input` |
| GPIO 与控制信号 | LED1-LED4 | `PD2=LED1`；`PD3=LED2`；`PD4=LED3`；`PD5=LED4`；`direction=MCU to LED blocks` |
| 总线 | ATMEGA328 到 ESP32 I2C | `controller=ATMEGA328 block`；`host=ESP32 block`；`SCL=ATMEGA328 PD4 -> ESP32 G22 IIC_SCL`；`SDA=ATMEGA328 PD5 -> ESP32 G21 IIC_SDA`；`direction=bidirectional bus as drawn` |
| 接口 | ESP32 主机接口块 | `signal_1=G22 IIC_SCL`；`signal_2=G21 IIC_SDA`；`power=VCC`；`ground=GND`；`connector_reference=null` |
| GPIO 与控制信号 | PD4/PD5 重复占用 | `PD4_use_1=IIC_SCL to ESP32 G22`；`PD4_use_2=LED3`；`PD5_use_1=IIC_SDA to ESP32 G21`；`PD5_use_2=LED4`；`confirmed_actual_map=null` |
| 总线地址 | Unit Trace I2C 地址 | `documented_address=0x5A`；`schematic_address_label=null`；`address_select=null`；`firmware_defined=true` |
| 传感器 | 四路红外传感器与 11mm 范围 | `documented_channels=4`；`documented_emitter=infrared LED`；`documented_receiver=phototransistor`；`documented_range=less than 11mm`；`schematic_part_numbers=null`；`thresholds=null`；`optical_geometry=null` |
| 核心器件 | LED1-LED4 物理器件角色 | `references=LED1-LED4`；`schematic_color=yellow graphic`；`part_number=null`；`wavelength=null`；`current_limit=null`；`confirmed_role=null` |
| 调试与烧录 | Mega328 ISP 下载接口 | `documented_interface=Mega328 ISP`；`connector_reference=null`；`MOSI=null`；`MISO=null`；`SCK=null`；`RESET=null`；`pinout_on_schematic=false` |
| 电源 | VCC 电压与 Grove 线色 | `schematic_power=VCC`；`schematic_voltage=null`；`documented_voltage=5V`；`schematic_signals=G22 IIC_SCL,G21 IIC_SDA`；`color_labels=null`；`documented_colors=Black,Red,Yellow,White` |

## 待确认事项

- `gpio.pd4-pd5-duplicate-map`：同一页面将 PD4/PD5 同时画为 IIC_SCL/IIC_SDA 主机通信线和 LED3/LED4 输出，映射存在自相冲突，无法确定实际 ATMEGA328 固件/PCB 使用的 I2C 与 LED 引脚。（证据：图 02d7a98e11c9 / 第 1 页 / 页面中央 ATMEGA328 右侧，上方 PD4/PD5 接 I2C、下方 PD4/PD5 接 LED3/LED4）
- `address.documented-i2c-address`：正文给出 I2C 地址 0x5A，但本地映射图没有地址值、地址选择电阻或固件常量，因此 0x5A 不能作为原理图确认事实。（证据：图 02d7a98e11c9 / 第 1 页 / 整页 IIC_SCL/IIC_SDA 连线，无 0x5A 或地址绑带）
- `sensor.sensor-array-implementation`：正文称有四组红外发光 LED/光电晶体管且反射面距离小于 11mm；页面只以 SensorArray[0-3] 方框表示，没有发射/接收器型号、阻值、光学布局、阈值或距离参数。（证据：图 02d7a98e11c9 / 第 1 页 / 页面左侧 SensorArray[0-3] 仅为方框，无内部器件或距离标注）
- `component.led-physical-role`：图中 LED1-LED4 用黄色通用 LED 图标表示并连接 PD2-PD5，但没有型号、波长、颜色、限流电阻或说明其是红外发射灯还是状态灯，物理角色需复核。（证据：图 02d7a98e11c9 / 第 1 页 / 页面右下 LED1-LED4 通用图标，无器件参数）
- `debug.documented-isp`：正文另行提到 Mega328 ISP 下载接口，但当前资源页面没有 ISP 连接器、MOSI/MISO/SCK/RESET/VCC/GND 网络或针脚定义，无法由本地图复核。（证据：图 02d7a98e11c9 / 第 1 页 / 整页仅有 SensorArray/ATMEGA328/ESP32/LED 映射，无 ISP 图块）
- `power.vcc-voltage-and-colors`：正文 Grove 表写 5V 及 Black/Red/Yellow/White 线色，但页面只标 VCC/GND/G22/G21，没有电压数值、连接器针号或线色，无法仅凭本地图确认 5V 与线缆对应。（证据：图 02d7a98e11c9 / 第 1 页 / 页面右上主机块仅标 G22/G21/VCC/GND）
- `review.pd4-pd5-conflict`：请用 PCB 网表、ATMEGA328 固件或正式电路图确认 I2C 与 LED1-4 的实际引脚，特别是 PD4/PD5 重复占用。；原因：当前页面同一引脚被画到两个不同功能。
- `review.i2c-address`：请用 MEGA328 内置固件确认 Unit Trace 的 I2C 地址是否固定为 0x5A。；原因：地址由固件定义且未打印在图中。
- `review.sensor-array`：请提供器件级原理图/BOM/光学设计，确认四路红外发射接收器、阈值、阻值与小于 11mm 工作范围。；原因：当前页面只显示 SensorArray 方框。
- `review.led-role`：请用 BOM 或实板确认 LED1-LED4 的型号、波长、限流与其是否为红外发射灯。；原因：图中只有通用 LED 图标。
- `review.isp`：请提供当前硬件版本的 ISP 连接器位号与完整 pinout。；原因：本地资源页没有 ISP 电路。
- `review.vcc-colors`：请用连接器/线缆规范确认 VCC 是否为 5V，以及 Black/Red/Yellow/White 与 GND/VCC/SDA/SCL 的对应。；原因：页面无电压数值、针号和线色。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `02d7a98e11c9d0aa86d64aa0b78458e406866569927f7fbe7d653b1dc0bb3535` | `https://static-cdn.m5stack.com/resource/docs/products/unit/trace/trace_sch_01.webp` |

---

源文档：`zh_CN/unit/trace.md`

源文档 SHA-256：`dcdde54703c0c02f9a6874e8595cb9655e3cf7436f4151511b767acd4dcad015`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
