# Module13.2 ECG 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 ECG |
| SKU | M034 |
| 产品 ID | `module13-2-ecg-7962c838495e` |
| 源文档 | `zh_CN/module/ecg.md` |

## 概述

Module13.2 ECG 的现有资源是一页功能框图，不是带位号、网络名和针脚号的器件级原理图。框图确认 ECG 模拟输入依次经过标注 G=100 的放大级、滤波/模拟调理级和 ADC，再以数字串行数据进入 MCU；MCU 输出经数字隔离块形成 Digital serial output。产品正文列出的 AD8232、AD8603、AD7476、STM32F031G4U6、10-bit ADC、UART 115200bps 和 M5-Bus 映射均无法由该页独立确认，电源转换、保护、时钟、复位和具体隔离边界也未展示。

## 检索关键词

`Module13.2 ECG`、`M034`、`ECG`、`G=100`、`Analog signal output`、`ADC`、`MCU`、`Digital serial data`、`Digital Isolator`、`Digital serial output`、`AD8232`、`AD8603`、`AD7476`、`STM32F031G4U6`、`10bit-ADC`、`UART`、`115200bps`、`M5-Bus Pin 20 RXD`、`M5-Bus Pin 22 TXD`、`M5-Bus Pin 28 5V`、`心电信号`、`模拟前端`、`低通滤波`、`数字隔离`、`串行输出`、`心率测量`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| ECG input block (unreferenced) | 未标注 | 框图左上 ECG 模拟信号源，送入后续增益级 | 图 d1106ad5d0f8 / 第 1 页 / 第 1 页左上圆形波形图标与下方 ECG 标签，箭头指向 G=100 三角块 |
| G=100 amplifier block (unreferenced) | 未标注 | 对 ECG 输入执行框图明确标注为 G=100 的模拟放大 | 图 d1106ad5d0f8 / 第 1 页 / 第 1 页上部左侧第一个三角放大器块，内部标注 G=100 |
| First filter block (unreferenced) | 未标注 | 位于 G=100 放大级之后的第一模拟滤波功能块 | 图 d1106ad5d0f8 / 第 1 页 / 第 1 页上部中左，G=100 三角块右侧的方形双波形滤波图标 |
| Second amplifier block (unreferenced) | 未标注 | 第一滤波块之后、第二滤波块之前的模拟放大/缓冲功能块 | 图 d1106ad5d0f8 / 第 1 页 / 第 1 页上部中央，两个方形滤波图标之间的第二个三角块 |
| Second filter block (unreferenced) | 未标注 | 在 ADC 之前对模拟信号进行进一步滤波 | 图 d1106ad5d0f8 / 第 1 页 / 第 1 页上部中右，第二个三角块右侧的方形波形滤波图标 |
| ADC block (unreferenced) | 未标注 | 接收上部 Analog signal output，并向 MCU 方向输出数字数据 | 图 d1106ad5d0f8 / 第 1 页 / 第 1 页右下标注 ADC 的竖直芯片块，上部模拟线向下连接，左向箭头指向 MCU |
| MCU block (unreferenced) | 未标注 | 接收 ADC 数据并向数字隔离方向输出 Digital serial data | 图 d1106ad5d0f8 / 第 1 页 / 第 1 页下部中央带芯片图案的 MCU 方块，右接 ADC、左接 Digital serial data 箭头 |
| Digital Isolator block (unreferenced) | 未标注 | 位于 MCU 数字串行数据与外部数字串行输出之间的隔离功能块 | 图 d1106ad5d0f8 / 第 1 页 / 第 1 页左下线圈隔离图标及 Digital Isolator 标签，两侧为 Digital serial data/output 箭头 |

## 系统结构

### Module13.2 ECG 功能框图

框图展示 ECG 输入沿上部模拟链向右经过 G=100 放大、第一滤波、第二放大和第二滤波，随后进入 ADC；ADC 数据沿下部链向左进入 MCU，再经 Digital Isolator 输出 Digital serial output。

- 参数与网络：`diagram_type=functional block diagram`；`analog_path=ECG -> G=100 amplifier -> filter -> amplifier -> filter -> ADC`；`digital_path=ADC -> MCU -> Digital Isolator -> Digital serial output`
- 证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页完整框图，上部由左向右模拟箭头、右侧向下连接、下部由右向左数字箭头

## 总线

### ADC 到 MCU 数据路径

ADC 左侧的粗箭头指向 MCU，确认转换结果由 ADC 送往 MCU；框图没有给出总线名称、信号名、位宽、时钟、片选或引脚号。

- 参数与网络：`source=ADC block`；`destination=MCU block`；`direction=ADC to MCU`；`protocol_shown=false`；`signals_shown=null`；`pin_numbers_shown=false`
- 证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页下部右侧 ADC 与 MCU 之间的左向白色箭头

### MCU 数字串行链

MCU 左侧通过标为 Digital serial data 的左向箭头连接 Digital Isolator，隔离器左侧再以 Digital serial output 箭头输出。

- 参数与网络：`source=MCU block`；`internal_label=Digital serial data`；`isolation_block=Digital Isolator`；`external_label=Digital serial output`；`direction=MCU toward external output`
- 证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页下部 MCU、Digital serial data 箭头、Digital Isolator 与 Digital serial output 箭头

## 保护电路

### 数字串行隔离

框图在 MCU 与 Digital serial output 之间明确画出 Digital Isolator 功能块，但没有器件位号、料号、隔离耐压、通道数或隔离电源连接。

- 参数与网络：`isolation_present_in_block_diagram=true`；`reference=null`；`part_number=null`；`isolation_rating=null`；`channel_count=null`；`isolated_power_shown=false`
- 证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页左下 Digital Isolator 线圈图标及相邻串行箭头

## 传感器

### ECG 输入

左上 ECG 波形图标是框图的模拟输入起点，其输出箭头直接进入 G=100 放大块。

- 参数与网络：`input_label=ECG`；`next_stage=G=100 amplifier block`；`signal_domain=analog`
- 证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页左上 ECG 图标、ECG 标签及右向箭头

## 模拟电路

### ECG 前级增益

ECG 输入后的第一个三角放大块内部明确标注 G=100。

- 参数与网络：`gain_label=G=100`；`position=first stage after ECG input`；`component_reference=null`；`part_number=null`
- 证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页上部左侧第一个三角形内部 G=100 标注

### ADC 前模拟调理链

G=100 放大块之后依次画有一个方形滤波块、一个三角放大/缓冲块和第二个方形滤波块，信号随后进入标为 Analog signal output 的水平节点。

- 参数与网络：`stage_1=first filter block`；`stage_2=second amplifier block`；`stage_3=second filter block`；`output_label=Analog signal output`
- 证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页上部从 G=100 块右侧至 Analog signal output 的连续功能块和箭头

### Analog signal output 到 ADC

第二滤波块后的 Analog signal output 水平线在右侧向下转接至 ADC 功能块。

- 参数与网络：`source=Analog signal output`；`destination=ADC block`；`signal_domain=analog`；`adc_input_pin=null`
- 证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页右侧上部模拟输出线及其向下至右下 ADC 的连线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Module13.2 ECG 功能框图 | `diagram_type=functional block diagram`；`analog_path=ECG -> G=100 amplifier -> filter -> amplifier -> filter -> ADC`；`digital_path=ADC -> MCU -> Digital Isolator -> Digital serial output` |
| 传感器 | ECG 输入 | `input_label=ECG`；`next_stage=G=100 amplifier block`；`signal_domain=analog` |
| 模拟电路 | ECG 前级增益 | `gain_label=G=100`；`position=first stage after ECG input`；`component_reference=null`；`part_number=null` |
| 模拟电路 | ADC 前模拟调理链 | `stage_1=first filter block`；`stage_2=second amplifier block`；`stage_3=second filter block`；`output_label=Analog signal output` |
| 模拟电路 | Analog signal output 到 ADC | `source=Analog signal output`；`destination=ADC block`；`signal_domain=analog`；`adc_input_pin=null` |
| 总线 | ADC 到 MCU 数据路径 | `source=ADC block`；`destination=MCU block`；`direction=ADC to MCU`；`protocol_shown=false`；`signals_shown=null`；`pin_numbers_shown=false` |
| 总线 | MCU 数字串行链 | `source=MCU block`；`internal_label=Digital serial data`；`isolation_block=Digital Isolator`；`external_label=Digital serial output`；`direction=MCU toward external output` |
| 保护电路 | 数字串行隔离 | `isolation_present_in_block_diagram=true`；`reference=null`；`part_number=null`；`isolation_rating=null`；`channel_count=null`；`isolated_power_shown=false` |
| 核心器件 | 正文列出的主要芯片 | `documented_afe=AD8232`；`documented_op_amp=AD8603`；`documented_adc=AD7476`；`documented_mcu=STM32F031G4U6`；`reference_designators_shown=false`；`part_numbers_on_diagram=null` |
| 模拟电路 | 正文中的 ADC 分辨率 | `documented_adc=AD7476`；`documented_resolution=10bit`；`diagram_label=ADC`；`resolution_on_diagram=null` |
| 总线 | ADC 与 MCU 的具体数字接口 | `controller=MCU block`；`device=ADC block`；`protocol=null`；`sclk=null`；`chip_select=null`；`data_signal=null`；`address=null` |
| 接口 | 正文中的 UART 与 M5-Bus 映射 | `documented_protocol=UART`；`documented_baud=115200bps`；`documented_pin_20=RXD`；`documented_pin_22=TXD`；`diagram_output_label=Digital serial output`；`connector_shown=false` |
| 电源 | 正文中的 5V 电源要求 | `documented_input=5V`；`documented_m5bus_pin=28`；`power_input_on_diagram=null`；`converter_shown=false`；`ldo_shown=false`；`isolated_power_shown=false`；`charger_shown=false`；`battery_path_shown=false` |
| 保护电路 | 隔离器与隔离边界细节 | `digital_isolator_block=true`；`isolator_part_number=null`；`isolated_supply=null`；`primary_ground=null`；`secondary_ground=null`；`isolation_voltage=null`；`input_protection=null` |
| 调试与烧录 | MCU 时钟、复位、启动与调试 | `clock=null`；`crystal=null`；`reset=null`；`boot=null`；`swd=null`；`debug_connector=null`；`interrupts=null`；`gpio_map=null` |
| 内存与 Flash | 存储器与外部存储接口 | `flash_shown=false`；`eeprom_shown=false`；`external_ram_shown=false`；`sd_shown=false`；`storage_bus=null` |

## 待确认事项

- `component.documented-chip-models`：产品正文列出 AD8232、AD8603、AD7476 和 STM32F031G4U6，但当前框图只展示无位号的放大、滤波、ADC 与 MCU 功能块，无法将这些料号逐一绑定到图中器件。（证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页全图仅有功能块标签，未显示 AD8232/AD8603/AD7476/STM32F031G4U6 字样或位号）
- `analog.documented-adc-resolution`：产品正文称 ADC 为 AD7476、分辨率 10bit；当前 ADC 功能块未显示料号或分辨率，因此该参数不能由本页确认。（证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页右下 ADC 功能块，无 AD7476 或 10bit 标注）
- `bus.documented-adc-interface`：框图只确认 ADC 到 MCU 的数据方向，没有 SCLK、CS、SDATA、SPI 或其他协议标注，因此具体控制器、信号网络和时序无法确认。（证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页下部 ADC 与 MCU 之间仅有一枚抽象左向箭头）
- `interface.documented-uart-output`：产品正文给出 UART 115200bps，并在 M5-Bus 表中标出 Pin 20=RXD、Pin 22=TXD；当前框图只写 Digital serial output，没有 UART、波特率、连接器、针脚或网络名，需由正式原理图确认。（证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页左下仅标 Digital serial output，无 M5-Bus、UART、115200bps、Pin 20 或 Pin 22）
- `power.documented-5v-input`：产品正文要求仅使用 5V，并在 M5-Bus 表中标出 Pin 28=5V；当前框图未画电源输入、转换器、LDO、负载开关、隔离电源、充电器、电池或监测路径，无法确认板内供电拓扑。（证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页全框图未显示任何电源轨、电源引脚、稳压器或 M5-Bus）
- `protection.isolation-details-unknown`：框图确认串行数据路径存在 Digital Isolator，但没有显示隔离器件型号、隔离电源、两侧地网络、爬电距离、隔离耐压或输入端保护，因此不能据本页声明具体安全等级或完整前端/数字域隔离拓扑。（证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页左下只有 Digital Isolator 功能图标；全图无电源、地、保护器件或隔离参数）
- `clock-reset-debug.not-visible`：MCU 仅以抽象功能块出现，框图没有晶振、时钟频率、RESET、BOOT、SWD、调试连接器、中断或 GPIO 映射，因此这些实现均无法确认。（证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页下部中央 MCU 抽象方块，无外围引脚或最小系统电路）
- `storage-memory.not-visible`：框图未展示独立 Flash、EEPROM、RAM、SD 卡或其他存储器及其总线，无法判断是否存在 MCU 之外的存储器。（证据：图 d1106ad5d0f8 / 第 1 页 / 第 1 页完整框图仅含模拟链、ADC、MCU、数字隔离与串行输出，无存储功能块）
- `review.chip-models`：请用 M034 当前版本正式原理图与 BOM 确认 AD8232、AD8603、AD7476、STM32F031G4U6 的位号、封装和实际装配型号。；原因：当前资源是无位号功能框图，无法把产品正文中的料号绑定到具体电路块。
- `review.adc-resolution`：M034 当前量产 ADC 是否为 AD7476、有效分辨率是否为 10 bit？；原因：框图 ADC 块没有型号和分辨率标注。
- `review.adc-interface`：请确认 ADC 与 MCU 之间的协议、SCLK/CS/数据网络、主从关系和采样时序。；原因：当前框图只有 ADC 指向 MCU 的抽象箭头，没有任何总线信号名。
- `review.uart-m5bus`：请用正式原理图确认隔离后 UART 的 TXD/RXD 方向、M5-Bus Pin 20/22 映射、电平和 115200bps 要求。；原因：框图只标 Digital serial output，无法验证 UART 物理接口和波特率。
- `review.power-topology`：请确认 M5-Bus Pin 28 的 5V 输入路径、隔离 DC/DC/LDO 型号、各电源轨、电流能力、使能和两侧地网络。；原因：当前框图完全省略供电和接地电路，不能验证正文中的 5V 要求之外的板内拓扑。
- `review.isolation-details`：请确认数字隔离器型号、通道方向、隔离耐压、隔离电源、两侧地和 ECG 输入保护器件。；原因：框图仅以 Digital Isolator 图标表示功能，未给出器件级隔离与保护信息。
- `review.mcu-minimum-system`：请提供 MCU 最小系统页以确认时钟源、RESET、BOOT、SWD、调试连接器、中断和 GPIO 映射。；原因：MCU 在当前资源中只是无引脚功能块。
- `review.external-memory`：请确认 M034 是否包含 MCU 之外的 Flash、EEPROM 或其他存储器及其连接。；原因：当前框图没有存储器功能块，但框图省略不等于量产电路中不存在。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `d1106ad5d0f8b4dc162aba25450ed37d6b4f050922db4b91d0759b98d4583684` | `https://static-cdn.m5stack.com/resource/docs/products/module/ecg/ecg_sch_01.webp` |

---

源文档：`zh_CN/module/ecg.md`

源文档 SHA-256：`d0bfe0dff8c9b9461457cc14fcb9abfd2f3bea6a9431552d4c448505b58156c0`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
