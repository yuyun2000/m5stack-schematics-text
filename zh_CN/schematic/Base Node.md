# Base Node 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Base Node |
| SKU | M017 |
| 产品 ID | `base-node-2f0fc735961b` |
| 源文档 | `zh_CN/base/node_base.md` |

## 概述

Base Node 以 U1 WM8978 为音频编解码核心，通过 M5Stack_BUS 的 GPIO0/GPIO13/GPIO5/GPIO2/GPIO34 构成 I2S，并以 GPIO21/GPIO22 作为 I2C 控制总线；板上 U2/U3 两路麦克风接 WM8978 差分输入，模拟输出连接 3.5mm 插座、功放层次端口和 GPIO25。另一页包含 12 颗级联 SK6812、U1 IP5306、BAT+ 电池接口及 +5V/SK6812 板间接口。GPIO12/GPIO35、I2C_SDA/I2C_SCL 和 R_OUT2/L_OUT2/PA_SD 只引到 IR/传感器及功放层次端口，具体 DHT12、红外、功放器件与地址未在两页中展示。

## 检索关键词

`Base Node`、`M017`、`WM8978`、`IP5306`、`SK6812`、`LED1-LED12`、`I2S`、`I2C`、`I2S_CLK_24M`、`I2S_WS`、`I2S_BCK`、`I2S_IN`、`I2S_OUT`、`I2C_SDA`、`I2C_SCL`、`GPIO0`、`GPIO13`、`GPIO5`、`GPIO2`、`GPIO34`、`GPIO21`、`GPIO22`、`GPIO25`、`GPIO12`、`GPIO35`、`MIC1_IN`、`MIC1_P`、`MIC2_N`、`MIC2_P`、`MICBIAS`、`L_OUT1`、`L_OUT2`、`R_OUT2`、`DAC_L`、`BAT+`、`+5V`、`+3.3V`、`IR_Send`、`IR_Receive`、`M5Stack_BUS`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| LED1-LED12 | SK6812 | 十二颗 +5V 供电的可寻址 RGB LED，数据从 SK6812IN 依次级联 | 图 58f435221064 / 第 1 页 / 第 1 张第 1 页左侧 LED1-LED12，每颗标 SK6812，VDD +5V、VSS GND、DIN/DOUT 级联 |
| U1 (电源页) | IP5306 | VIN 与 BAT+ 之间的电池电源管理器件，外接 L1 和输入/电池侧电容 | 图 58f435221064 / 第 1 页 / 第 1 张第 1 页右上 U1 IP5306，VIN/VOUT/SW/BAT/GND/KEY 引脚 |
| L1 | 1uH ±10% | IP5306 SW 节点与 BAT+ 之间的电感 | 图 58f435221064 / 第 1 页 / 第 1 张第 1 页 U1 右侧 L1 1uH ±10%，连接 SW 与 BAT+ |
| J1 (电源页) | Socket_4p | 引出 +5V、BAT+、SK6812 数据和 GND 的板间接口 | 图 58f435221064 / 第 1 页 / 第 1 张第 1 页右下 J1 Socket_4p，pin1 +5V、pin2 BAT+、pin3 SK6812、pin4 GND |
| J2 (电源页) | SOCKET-2P | BAT+ 与 GND 的两针电池接口 | 图 58f435221064 / 第 1 页 / 第 1 张第 1 页右侧 J2 SOCKET-2P，pin1 BAT+、pin2 GND |
| U1 (音频页) | WM8978 | 连接 I2S、I2C、双麦克风、模拟输出与音频电源域的音频编解码器 | 图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页中央 U1 WM8978，LRC/BCLK/ADCDAT/DACDAT/MCLK、SCLK/SDIN、模拟输入输出和电源引脚 |
| U2,U3 | MIC | 两路板载麦克风，经耦合和 MICBIAS 网络接 WM8978 MIC1/MIC2 差分输入 | 图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页左侧 U2/U3 MIC 与 C2/C5、C10/C11、R5/R10、MICBIAS、MIC1/MIC2 网络 |
| J1 (音频页) | 3.5mm_jack_1 | 连接 MIC_IN2 与 L_OUT1 的 3.5mm 音频插座 | 图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页右上 J1 3.5mm_jack_1，左侧网络 MIC_IN2 与 L_OUT1 |
| J2 | M5Stack_BUS | 30 针主控堆叠总线，承载 I2S、I2C、IR、SK6812、DAC_L 与电源网络 | 图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页右侧 J2 M5Stack_BUS，pin1-pin30 与外部网络 |
| J3 | Socket_4p | 与电源/LED 页 J1 对应的 +5V、BAT+、SK6812 和 GND 板间接口 | 图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页左下 J3 Socket_4p，pin1 +5V、pin2 BAT+、pin3 SK6812、pin4 GND |
| Sensor_M | 未标注 | 引出 DHT I2C_SDA/I2C_SCL 与 IR_Send/IR_Receive 的层次端口 | 图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页左上 Sensor_M 层次端口，I2C_SDA、I2C_SCL、IR_Send、IR_Receive |
| PA_CS8305E_M | 未标注 | 引出 R_OUT2、L_OUT2 与 PA_SD 到 Audio_R/Audio_L/Audio_SD 的功放层次端口 | 图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页左上 PA_CS8305E_M 层次端口，R_OUT2/L_OUT2/PA_SD 与 Audio_R/Audio_L/Audio_SD |

## 系统结构

### Base Node 系统架构

J2 M5Stack_BUS 连接 U1 WM8978 的 I2S/I2C、双麦克风、模拟音频输出、Sensor_M 的 IR/I2C 网络以及 SK6812 数据；J3/J1 板间接口再连接 12 颗 SK6812 和 IP5306/BAT+ 电源页。

- 参数与网络：`codec=U1 WM8978`；`host=J2 M5Stack_BUS`；`microphones=U2,U3`；`rgb=LED1-LED12 SK6812`；`battery_power=IP5306 and BAT+`；`sheet_link=+5V,BAT+,SK6812,GND via J3/J1 Socket_4p`
- 证据：图 58f435221064 / 第 1 页 / 第 1 张第 1 页 SK6812、IP5306、J1/J2; 图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页 WM8978、双 MIC、M5Stack_BUS、Sensor_M、PA_CS8305E_M 与 J3

## 电源

### SK6812 阵列供电

LED1-LED12 每颗 VDD pin4 接 +5V、VSS pin2 接 GND；+5V 与 GND 通过 J1/J3 Socket_4p 的 pin1/pin4 在两页间连接。

- 参数与网络：`leds=LED1-LED12`；`supply=+5V`；`ground=GND`；`connector=J1/J3 pin1 +5V, pin4 GND`
- 证据：图 58f435221064 / 第 1 页 / 第 1 张第 1 页 LED1-LED12 VDD/VSS 与 J1 +5V/GND

### IP5306 与 BAT+ 路径

VIN 经 R1 2Ω 到 U1 IP5306 VIN，C1/C2 各 10uF 对地；U1 SW 经 L1 1uH 连接 BAT+，U1 BAT pin6 也接 BAT+，BAT+ 侧有 R2 1Ω 与 C3/C4 各 22uF。VOUT pin8 与 KEY pin5 在本页标为未连接。

- 参数与网络：`input=VIN -> R1 2Ω -> U1 VIN`；`input_caps=C1/C2 10uF`；`switch_path=U1 SW -> L1 1uH -> BAT+`；`battery_pin=U1 BAT pin6 -> BAT+`；`battery_network=R2 1Ω, C3/C4 22uF`；`unconnected=VOUT pin8, KEY pin5`
- 证据：图 58f435221064 / 第 1 页 / 第 1 张第 1 页右上 VIN/R1/C1/C2/U1 IP5306/L1/R2/C3/C4/BAT+

### WM8978 电源与参考网络

WM8978 使用 +3.3V、+5V、WM_GND 和 GND 网络；DCVDD/DBVDD/AVDD 侧连接 +3.3V，SPKVDD 侧连接 +5V，MICBIAS 与 VMID 各由 C7/C8 4.7uF 接 WM_GND，页底给出 C12-C22 的本地去耦与 0Ω 接地桥。

- 参数与网络：`digital_analog_supply=+3.3V`；`speaker_supply=+5V`；`grounds=GND,WM_GND`；`micbias_cap=C7 4.7uF`；`vmid_cap=C8 4.7uF`；`decoupling=C12-C22`；`ground_bridges=R13/R15 0Ω`
- 证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页 U1 电源/地、MICBIAS/VMID C7/C8 与底部 C12-C22/R13/R15

## 接口

### BAT+ 外部与板间接口

J2 SOCKET-2P 的 pin1 接 BAT+、pin2 接 GND；J1/J3 Socket_4p 的 pin2 也连接 BAT+，将电池网络送到音频/M5Stack_BUS 页。

- 参数与网络：`battery_socket=J2 pin1 BAT+, pin2 GND`；`sheet_connector=J1/J3 pin2 BAT+`；`direction=bidirectional battery power path`
- 证据：图 58f435221064 / 第 1 页 / 第 1 张第 1 页 J2 SOCKET-2P 与 J1 Socket_4p BAT+; 图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页 J3 pin2 BAT+ 与 M5Stack_BUS pin30 BAT+

### J2 M5Stack_BUS 功能网络

J2 的 pin2 GPIO35 接 IR_Receive，pin8 GPIO25 接 DAC_L，pin17 GPIO21 接 I2C_SDA，pin18 GPIO22 接 I2C_SCL，pin19 GPIO2 接 I2S_IN，pin20 GPIO5 接 I2S_BCK，pin21 GPIO12 接 IR_Send，pin22 GPIO13 接 I2S_WS，pin23 GPIO15 接 SK6812，pin24 GPIO0 接 I2S_CLK_24M，pin26 GPIO34 接 I2S_OUT，pin28 接 +5V，pin30 接 BAT+。

- 参数与网络：`ir=pin2 GPIO35 IR_Receive; pin21 GPIO12 IR_Send`；`analog=pin8 GPIO25 DAC_L`；`i2c=pin17 GPIO21 SDA; pin18 GPIO22 SCL`；`i2s=pin19 GPIO2 IN; pin20 GPIO5 BCK; pin22 GPIO13 WS; pin24 GPIO0 CLK; pin26 GPIO34 OUT`；`rgb=pin23 GPIO15 SK6812`；`power=pin28 +5V; pin30 BAT+`
- 证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页右侧 J2 M5Stack_BUS pin1-pin30 与外部功能网络

## 总线

### WM8978 I2S 映射

WM8978 的 MCLK 接 I2S_CLK_24M/GPIO0，LRC 接 I2S_WS/GPIO13，BCLK 接 I2S_BCK/GPIO5，DACDAT 接 I2S_IN/GPIO2，ADCDAT 接 I2S_OUT/GPIO34；这些网络均进入 J2 M5Stack_BUS。

- 参数与网络：`controller=M5Stack host`；`device=U1 WM8978`；`mclk=I2S_CLK_24M -> GPIO0`；`word_select=I2S_WS -> GPIO13`；`bit_clock=I2S_BCK -> GPIO5`；`dac_data=I2S_IN -> GPIO2 -> WM8978 DACDAT`；`adc_data=WM8978 ADCDAT -> I2S_OUT -> GPIO34`
- 证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页 U1 左上 LRC/BCLK/ADCDAT/DACDAT/MCLK 与右侧 J2 I2S 网络

### WM8978 I2C 控制总线

WM8978 SCLK 与 SDIN 分别连接 I2C_SCL 和 I2C_SDA；I2C_SCL 进入 J2 GPIO22，I2C_SDA 进入 J2 GPIO21，并同时引到 Sensor_M 的 DHT_I2C_SCL/DHT_I2C_SDA。

- 参数与网络：`controller=M5Stack host`；`codec=U1 WM8978`；`scl=WM8978 SCLK -> I2C_SCL -> GPIO22`；`sda=WM8978 SDIN -> I2C_SDA -> GPIO21`；`other_endpoint=Sensor_M DHT_I2C_SCL/DHT_I2C_SDA`
- 证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页 U1 SCLK/SDIN、左上 Sensor_M 与右侧 J2 I2C_SCL/I2C_SDA

## GPIO 与控制信号

### 十二颗 SK6812 数据链

M5Stack_BUS 的 SK6812 网络连接 J3 pin3，并通过同名板间网络到 J1 pin3 和 SK6812IN；SK6812IN 经 R3 4.7KΩ 上拉到 +5V 后进入 LED12 DIN，LED12 至 LED1 通过 DOUT/DIN 依次级联，LED1 DOUT 端未继续连接。

- 参数与网络：`host_gpio=GPIO15 via M5Stack_BUS pin23`；`sheet_connector=J3 pin3 <-> J1 pin3 SK6812`；`input_net=SK6812IN`；`pullup=R3 4.7KΩ to +5V`；`chain=LED12 -> LED11 -> ... -> LED1`；`last_output=LED1 DOUT NC`
- 证据：图 58f435221064 / 第 1 页 / 第 1 张第 1 页 J1 pin3、R3、SK6812IN 与 LED12-LED1 数据链; 图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页 J2 pin23 GPIO15 的 SK6812 网络与 J3 pin3

### 红外收发控制网络

IR_Send 从 J2 M5Stack_BUS 的 GPIO12 引到 Sensor_M，IR_Receive 从 Sensor_M 引到 J2 GPIO35；本页只展示同名网络和层次端口。

- 参数与网络：`transmit=GPIO12 -> IR_Send -> Sensor_M`；`receive=Sensor_M -> IR_Receive -> GPIO35`；`external_circuit_shown=false`
- 证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页左上 Sensor_M IR_Send/IR_Receive 与右侧 J2 GPIO12/GPIO35

## 时钟

### WM8978 主时钟

WM8978 MCLK 引脚接网络 I2S_CLK_24M，该网络连接 J2 M5Stack_BUS 的 GPIO0；图中未画独立晶振或振荡器。

- 参数与网络：`clock_net=I2S_CLK_24M`；`host_gpio=GPIO0`；`source=external M5Stack host`；`local_crystal_shown=false`
- 证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页 U1 MCLK 与 J2 GPIO0 上的 I2S_CLK_24M

## 音频

### 双麦克风到 WM8978

U2 经 C2/C5 各 1.0uF 连接 MIC1_IN/MIC1_P，再接 WM8978 RIP/RIN；U3 经 C10/C11 各 1.0uF 连接 MIC2_N/MIC2_P，再接 WM8978 LIP/LIN。

- 参数与网络：`mic1=U2 -> C2/C5 1.0uF -> MIC1_IN/MIC1_P -> WM8978 RIP/RIN`；`mic2=U3 -> C10/C11 1.0uF -> MIC2_N/MIC2_P -> WM8978 LIP/LIN`；`channels=2`
- 证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页左侧 U2/U3、C2/C5/C10/C11 与 U1 RIP/RIN/LIP/LIN

### WM8978 模拟输出路径

WM8978 ROUT2/LOUT2 输出 R_OUT2/L_OUT2 到 PA_CS8305E_M 的 Audio_R/Audio_L；ROUT1/LOUT1 经 R2/R3 0Ω、C3/C4 220uF/6.3V 形成 L_OUT1 并接 J1 3.5mm 插座，L_OUT1 还经 R8 0Ω 接 DAC_L/GPIO25。

- 参数与网络：`amplifier_port=ROUT2 R_OUT2 -> Audio_R; LOUT2 L_OUT2 -> Audio_L`；`jack_path=ROUT1/LOUT1 -> R2/R3 0Ω -> C3/C4 220uF/6.3V -> L_OUT1 -> J1`；`host_analog=L_OUT1 -> R8 0Ω -> DAC_L -> GPIO25`
- 证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页 U1 ROUT2/LOUT2、ROUT1/LOUT1、C3/C4、J1、R8/DAC_L 与 PA_CS8305E_M

## 模拟电路

### 麦克风偏置与滤波

WM8978 MICBIAS 网络通过 R5/R10 各 680Ω 向 U2/U3 麦克风支路供偏置；两路还包含 R6/R11 10KΩ、R7/R12 47KΩ 和 C9/C16 220pF 到 WM_GND 的网络。

- 参数与网络：`bias_source=WM8978 MICBIAS`；`series_resistors=R5/R10 680Ω`；`ground_resistors=R6/R11 10KΩ; R7/R12 47KΩ`；`filter_capacitors=C9/C16 220pF`；`ground=WM_GND`
- 证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页 U2/U3 周围 R5-R7/R10-R12/C9/C16 与 MICBIAS

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Base Node 系统架构 | `codec=U1 WM8978`；`host=J2 M5Stack_BUS`；`microphones=U2,U3`；`rgb=LED1-LED12 SK6812`；`battery_power=IP5306 and BAT+`；`sheet_link=+5V,BAT+,SK6812,GND via J3/J1 Socket_4p` |
| GPIO 与控制信号 | 十二颗 SK6812 数据链 | `host_gpio=GPIO15 via M5Stack_BUS pin23`；`sheet_connector=J3 pin3 <-> J1 pin3 SK6812`；`input_net=SK6812IN`；`pullup=R3 4.7KΩ to +5V`；`chain=LED12 -> LED11 -> ... -> LED1`；`last_output=LED1 DOUT NC` |
| 电源 | SK6812 阵列供电 | `leds=LED1-LED12`；`supply=+5V`；`ground=GND`；`connector=J1/J3 pin1 +5V, pin4 GND` |
| 电源 | IP5306 与 BAT+ 路径 | `input=VIN -> R1 2Ω -> U1 VIN`；`input_caps=C1/C2 10uF`；`switch_path=U1 SW -> L1 1uH -> BAT+`；`battery_pin=U1 BAT pin6 -> BAT+`；`battery_network=R2 1Ω, C3/C4 22uF`；`unconnected=VOUT pin8, KEY pin5` |
| 接口 | BAT+ 外部与板间接口 | `battery_socket=J2 pin1 BAT+, pin2 GND`；`sheet_connector=J1/J3 pin2 BAT+`；`direction=bidirectional battery power path` |
| 总线 | WM8978 I2S 映射 | `controller=M5Stack host`；`device=U1 WM8978`；`mclk=I2S_CLK_24M -> GPIO0`；`word_select=I2S_WS -> GPIO13`；`bit_clock=I2S_BCK -> GPIO5`；`dac_data=I2S_IN -> GPIO2 -> WM8978 DACDAT`；`adc_data=WM8978 ADCDAT -> I2S_OUT -> GPIO34` |
| 时钟 | WM8978 主时钟 | `clock_net=I2S_CLK_24M`；`host_gpio=GPIO0`；`source=external M5Stack host`；`local_crystal_shown=false` |
| 总线 | WM8978 I2C 控制总线 | `controller=M5Stack host`；`codec=U1 WM8978`；`scl=WM8978 SCLK -> I2C_SCL -> GPIO22`；`sda=WM8978 SDIN -> I2C_SDA -> GPIO21`；`other_endpoint=Sensor_M DHT_I2C_SCL/DHT_I2C_SDA` |
| 接口 | J2 M5Stack_BUS 功能网络 | `ir=pin2 GPIO35 IR_Receive; pin21 GPIO12 IR_Send`；`analog=pin8 GPIO25 DAC_L`；`i2c=pin17 GPIO21 SDA; pin18 GPIO22 SCL`；`i2s=pin19 GPIO2 IN; pin20 GPIO5 BCK; pin22 GPIO13 WS; pin24 GPIO0 CLK; pin26 GPIO34 OUT`；`rgb=pin23 GPIO15 SK6812`；`power=pin28 +5V; pin30 BAT+` |
| 音频 | 双麦克风到 WM8978 | `mic1=U2 -> C2/C5 1.0uF -> MIC1_IN/MIC1_P -> WM8978 RIP/RIN`；`mic2=U3 -> C10/C11 1.0uF -> MIC2_N/MIC2_P -> WM8978 LIP/LIN`；`channels=2` |
| 模拟电路 | 麦克风偏置与滤波 | `bias_source=WM8978 MICBIAS`；`series_resistors=R5/R10 680Ω`；`ground_resistors=R6/R11 10KΩ; R7/R12 47KΩ`；`filter_capacitors=C9/C16 220pF`；`ground=WM_GND` |
| 音频 | WM8978 模拟输出路径 | `amplifier_port=ROUT2 R_OUT2 -> Audio_R; LOUT2 L_OUT2 -> Audio_L`；`jack_path=ROUT1/LOUT1 -> R2/R3 0Ω -> C3/C4 220uF/6.3V -> L_OUT1 -> J1`；`host_analog=L_OUT1 -> R8 0Ω -> DAC_L -> GPIO25` |
| 电源 | WM8978 电源与参考网络 | `digital_analog_supply=+3.3V`；`speaker_supply=+5V`；`grounds=GND,WM_GND`；`micbias_cap=C7 4.7uF`；`vmid_cap=C8 4.7uF`；`decoupling=C12-C22`；`ground_bridges=R13/R15 0Ω` |
| GPIO 与控制信号 | 红外收发控制网络 | `transmit=GPIO12 -> IR_Send -> Sensor_M`；`receive=Sensor_M -> IR_Receive -> GPIO35`；`external_circuit_shown=false` |
| 总线地址 | WM8978 I2C 地址 | `device=U1 WM8978`；`bus=I2C_SCL/I2C_SDA`；`address=null`；`address_strap=null` |
| 传感器 | DHT 与红外器件实现 | `documented_sensor=DHT12`；`visible_nets=DHT_I2C_SDA,DHT_I2C_SCL,IR_Send,IR_Receive`；`sensor_reference=null`；`sensor_address=null`；`ir_tx_devices=null`；`ir_rx_device=null` |
| 音频 | 外部功放实现 | `hierarchical_port=PA_CS8305E_M`；`signals=R_OUT2,L_OUT2,PA_SD`；`port_names=Audio_R,Audio_L,Audio_SD`；`amplifier_reference=null`；`part_number=null`；`output_power=null` |
| 电源 | 电池容量与充电边界 | `documented_capacity=500mAh`；`controller=U1 IP5306`；`battery_net=BAT+`；`connector=J2 SOCKET-2P`；`chemistry=null`；`voltage=null`；`charge_current=null`；`termination_voltage=null`；`temperature_monitoring=null` |

## 待确认事项

- `address.wm8978-i2c`：原理图确认 WM8978 使用 I2C_SCL/I2C_SDA，但没有标出从地址、地址选择脚状态或总线扫描结果。（证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页 U1 SCLK/SDIN 与 I2C 网络，图中无地址文字）
- `sensor.dht-ir-implementation`：Sensor_M 只显示 DHT_I2C_SDA、DHT_I2C_SCL、IR_Send 和 IR_Receive 层次端口；两页均未展示 DHT12 位号/电源/地址、红外发射器数量/型号/驱动器或红外接收器型号与保护。（证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页左上 Sensor_M 层次端口，页面无 DHT/IR 器件符号）
- `audio.power-amplifier-implementation`：PA_CS8305E_M 只显示 R_OUT2/L_OUT2/PA_SD 到 Audio_R/Audio_L/Audio_SD 的层次端口；两页未展示功放 IC 位号、完整料号、供电、扬声器连接或输出功率。（证据：图 68679daa7b47 / 第 1 页 / 第 2 张第 1 页左上 PA_CS8305E_M 层次端口，页面无功放 IC 或扬声器）
- `power.documented-battery-capability`：正文称内置 500mAh 锂电池；原理图只确认 IP5306、BAT+、J2 电池接口和被动器件，未标注电池化学体系、额定电压、容量、充电电流、终止电压、温度监测或保护指标。（证据：图 58f435221064 / 第 1 页 / 第 1 张第 1 页 U1 IP5306、BAT+ 与 J2，图中无电池规格或充电参数）
- `review.wm8978-address`：M017 的 WM8978 实际 I2C 从地址和地址选择配置是什么？；原因：原理图只显示 SCLK/SDIN 总线连接，没有地址标注或扫描结果。
- `review.dht-ir-circuit`：请提供 Sensor_M 子页或 BOM，确认 DHT12 位号/地址/供电、四路红外发射驱动和红外接收器型号与保护。；原因：当前资源仅有层次端口，无法验证器件级实现。
- `review.power-amplifier`：请提供 PA_CS8305E_M 子页或 BOM，确认功放型号、供电、关断极性、扬声器连接与输出功率。；原因：当前资源只展示 Audio_R/Audio_L/Audio_SD 层次端口。
- `review.battery-safety`：M017 量产电池的化学体系、额定电压/容量、极性及 IP5306 的充电电流、终止电压和保护配置是什么？；原因：原理图未给出电池和充电安全参数，正文容量不能替代 BOM 与电气规格。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `58f435221064d664320045352649180a9ab616fa31a48e4fc72b0ac5d5313a62` | `https://static-cdn.m5stack.com/resource/docs/products/base/node_base/node_base_sch_01.webp` |
| 2 | 1 | `68679daa7b47b04d7bf706a126cec9d53cfc45251fbd5f1d1ea59228463f787b` | `https://static-cdn.m5stack.com/resource/docs/products/base/node_base/node_base_sch_02.webp` |

---

源文档：`zh_CN/base/node_base.md`

源文档 SHA-256：`9ed6fd2d8631d0fb7e6e08e4ccfa3d6384f7f8601061a7f721e04e922acfebd4`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
