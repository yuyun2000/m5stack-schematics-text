# Stamp PWR485 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp PWR485 |
| SKU | S001 |
| 产品 ID | `stamp-pwr485-f925b02d2ef4` |
| 源文档 | `zh_CN/stamp/stamp_pwr485.md` |

## 概述

Stamp PWR485 以 U2 SP485EEN-L/TR 将 TTL UART 接口转换为 RS485_A/RS485_B，Q1 SS8050 Y1 由 TX 驱动并控制 /RE 与 DE，RO 经 R6 输出 RX。+VIN 经 F1 1.5A/24V 和 U1 ME3116AM6G 降压为 +5V，为收发器和外部主机供电。J1 StampPWR485_Pin 提供两组并联的 GND/VIN/A/B PWR485 端口及单独的 GND/5V/TX/RX 接口，RS-485 线配置偏置和三颗 SP4021-01FTG-C 保护器件。

## 检索关键词

`Stamp PWR485`、`S001`、`SP485EEN-L/TR`、`ME3116AM6G`、`SS8050 Y1`、`RS485`、`RS485_A`、`RS485_B`、`RX`、`TX`、`RO`、`RE`、`DE`、`DI`、`+VIN`、`+5V`、`F1 1.5A/24V`、`SP4021-01FTG-C`、`LESD3Z5.0CMT1G`、`SS34`、`B5819W SL`、`StampPWR485_Pin`、`PWR485`、`9600bps`、`115200bps`、`128000bps`、`9-24V`、`3.3V TTL`、`Modbus`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | SP485EEN-L/TR | TTL/UART 至半双工 RS-485 A/B 收发器 | 图 5a406f6a3742 / 第 1 页 / 页面 C1-C2 U2 SP485EEN-L/TR，RO,/RE,DE,DI,A,B,VCC,GND 引脚 |
| U1 | ME3116AM6G | +VIN 至 +5V 的降压转换器 | 图 5a406f6a3742 / 第 1 页 / 页面 A1-B2 U1 ME3116AM6G，VIN/EN/BST/LX/FB/GND 与 L1/R2/R3 |
| Q1 | SS8050 Y1 | 由 TX 驱动的 /RE 与 DE 自动方向控制晶体管 | 图 5a406f6a3742 / 第 1 页 / 页面 C1 Q1 SS8050 Y1，基极经 R9 1KΩ 接 TX，集电极接 /RE+DE，发射极接 GND |
| F1 | 1.5A/24V | +VIN 输入串联保险丝 | 图 5a406f6a3742 / 第 1 页 / 页面 A1 +VIN 与 U1 输入之间 F1 1.5A/24V |
| D2 | SS34 | F1 后输入节点到 GND 的肖特基保护器件 | 图 5a406f6a3742 / 第 1 页 / 页面 A1 F1 后 D2 SS34 对 GND |
| L1,D1 | 10uH; B5819W SL | ME3116 +5V 降压输出电感与自举/开关节点二极管 | 图 5a406f6a3742 / 第 1 页 / 页面 A2 U1 右侧 D1 B5819W SL 与 L1 10uH 至 +5V |
| D3,D4,D5 | SP4021-01FTG-C x3 | RS485_B 对地、B-A 线间、RS485_A 对地的三级浪涌/ESD 保护 | 图 5a406f6a3742 / 第 1 页 / 页面 C2-C3 D3/D4/D5 SP4021-01FTG-C，跨接 GND-RS485_B-RS485_A-GND |
| D6 | LESD3Z5.0CMT1G | +5V 电源对地 ESD/TVS 保护 | 图 5a406f6a3742 / 第 1 页 / 页面 A4-B4 D6 LESD3Z5.0CMT1G 跨接 +5V 与 GND |
| D7,R4 | 红灯 0603; 4.7KΩ | +5V 电源指示灯 | 图 5a406f6a3742 / 第 1 页 / 页面 A3-B3 +5V 经 D7 红灯 0603 与 R4 4.7KΩ 串联到 GND |
| J1 | StampPWR485_Pin | 12 针 Stamp/PWR485 主接口，提供两组并联 A/B/VIN/GND 与 TTL RX/TX/5V/GND | 图 5a406f6a3742 / 第 1 页 / 页面 C3-C4 J1 StampPWR485_Pin，pin 1-12 与底部 pin 5-8 网络 |

## 系统结构

### Stamp PWR485 系统架构

ME3116AM6G 将 PWR485 的 +VIN 转换为 +5V，SP485EEN-L/TR 完成 TTL/RS-485 物理层转换，SS8050 控制收发方向，J1 提供双路并联 PWR485 与主机 TTL/5V 接口。

- 参数与网络：`buck=U1 ME3116AM6G`；`transceiver=U2 SP485EEN-L/TR`；`direction=Q1 SS8050 Y1`；`connector=J1 StampPWR485_Pin`；`protection=D3,D4,D5 SP4021-01FTG-C`
- 证据：图 5a406f6a3742 / 第 1 页 / 完整单页 A1-C4 电源、RS485、保护与接口分区

## 电源

### +VIN 输入保护与滤波

+VIN 经 F1 1.5A/24V 进入 U1 输入节点，D2 SS34 从该节点接 GND，C2 10uF 滤波，R1 100KΩ 将 U1 EN 上拉至输入。

- 参数与网络：`input=+VIN`；`fuse=F1 1.5A/24V`；`diode=D2 SS34 to GND`；`filter=C2 10uF`；`enable_pullup=R1 100KΩ`
- 证据：图 5a406f6a3742 / 第 1 页 / 页面 A1 +VIN/F1/D2/C2/R1/U1

### U1 +5V 降压

U1 ME3116AM6G 的 LX 经 L1 10uH 输出 +5V，R2 52.3KΩ（5232）与 R3 10KΩ构成 FB 分压，C6/C3/C4 各 22uF 滤波输出，C1 100nF 与 D1 B5819W SL 位于自举/开关节点。

- 参数与网络：`converter=U1 ME3116AM6G`；`input=+VIN after F1`；`inductor=L1 10uH`；`output=+5V`；`feedback=R2 52.3KΩ,R3 10KΩ`；`output_caps=C6 22uF,C3 22uF,C4 22uF`；`bootstrap=C1 100nF,D1 B5819W SL`
- 证据：图 5a406f6a3742 / 第 1 页 / 页面 A2-B2 U1/L1/R2/R3/C1/C3/C4/C6/D1/+5V

## 接口

### J1 StampPWR485_Pin 针脚

J1 pin 1 GND、2 VIN、3 A、4 B；pin 5 GND、6 VIN、7 A、8 B；pin 9 GND、10 5V、11 TX、12 RX。两组 GND/VIN/A/B 使用同名网络并联。

- 参数与网络：`pwr485_port1=1:GND,2:VIN,3:A,4:B`；`pwr485_port2=5:GND,6:VIN,7:A,8:B`；`ttl_port=9:GND,10:5V,11:TX,12:RX`；`parallel=true`
- 证据：图 5a406f6a3742 / 第 1 页 / 页面 C3-C4 J1 StampPWR485_Pin pin 1-12 与底部 pin 5-8

## 总线

### RS-485 接收路径

U2 pin 6/A 与 pin 7/B 连接 RS485_A/RS485_B；pin 1/RO 经 R6 1KΩ 输出 RX。R5 4.7KΩ 将 B 下拉至 GND，R10 4.7KΩ 将 A 上拉至 +5V。

- 参数与网络：`a=U2 pin 6 -> RS485_A`；`b=U2 pin 7 -> RS485_B`；`receiver=U2 pin 1/RO -> R6 1KΩ -> RX`；`b_bias=R5 4.7KΩ to GND`；`a_bias=R10 4.7KΩ to +5V`
- 证据：图 5a406f6a3742 / 第 1 页 / 页面 C1-C3 U2 RO/A/B、R6/R5/R10 与 RX/RS485_A/RS485_B

## 总线地址

### 总线地址可见性

Stamp PWR485 是 UART/RS-485 物理层转换器，原理图没有 Modbus 节点地址、I2C/SPI 地址或其他数值设备地址。

- 参数与网络：`modbus_address_visible=false`；`i2c_visible=false`；`spi_visible=false`；`numeric_address_visible=false`
- 证据：图 5a406f6a3742 / 第 1 页 / 完整单页所有接口，无设备地址

## GPIO 与控制信号

### RS-485 /RE 与 DE 自动方向

U2 pin 2 /RE 与 pin 3 DE 共接方向节点，R7 4.7KΩ 将其上拉到 +5V，Q1 SS8050 Y1 可拉低该节点；Q1 基极由 TX 经 R9 1KΩ 驱动。

- 参数与网络：`control=U2 pins 2 /RE and 3 DE`；`pullup=R7 4.7KΩ to +5V`；`transistor=Q1 SS8050 Y1`；`base=TX -> R9 1KΩ`；`emitter=GND`
- 证据：图 5a406f6a3742 / 第 1 页 / 页面 C1 TX/R9/Q1/R7 与 U2 /RE/DE

### +5V 红色指示灯

+5V 经 D7 红灯 0603 与 R4 4.7KΩ 串联到 GND，形成电源状态指示。

- 参数与网络：`path=+5V -> D7 red 0603 -> R4 4.7KΩ -> GND`
- 证据：图 5a406f6a3742 / 第 1 页 / 页面 A3-B3 D7/R4/+5V/GND

## 时钟

### 时钟、复位与调试可见性

原理图没有 MCU、晶体、振荡器、复位、BOOT、SWD/JTAG 或专用调试接口。

- 参数与网络：`mcu_visible=false`；`crystal_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false`
- 证据：图 5a406f6a3742 / 第 1 页 / 完整单页器件与接口

## 保护电路

### RS485_A/B 三级保护

D3 SP4021-01FTG-C 跨接 GND 与 RS485_B，D4 同型号跨接 RS485_B 与 RS485_A，D5 同型号跨接 RS485_A 与 GND，形成对地及线间保护。

- 参数与网络：`b_to_ground=D3 SP4021-01FTG-C`；`line_to_line=D4 SP4021-01FTG-C`；`a_to_ground=D5 SP4021-01FTG-C`
- 证据：图 5a406f6a3742 / 第 1 页 / 页面 C2-C3 D3/D4/D5 与 RS485_B/RS485_A/GND

### +5V 输出保护

D6 LESD3Z5.0CMT1G 跨接 +5V 与 GND，为 5V 输出域提供 ESD/TVS 保护。

- 参数与网络：`protector=D6 LESD3Z5.0CMT1G`；`rail=+5V`；`return=GND`
- 证据：图 5a406f6a3742 / 第 1 页 / 页面 A4-B4 D6 +5V-GND

### RS-485 终端与隔离可见性

原理图没有 120Ω A-B 终端电阻、共模电感或隔离器；两路 PWR485 端口直接并联到同一 A/B/VIN/GND 网络。

- 参数与网络：`termination_visible=false`；`common_mode_choke_visible=false`；`galvanic_isolation_visible=false`；`ports_parallel=true`
- 证据：图 5a406f6a3742 / 第 1 页 / 完整 RS485_A/B 电路与 J1 两组端口

## 内存与 Flash

### 存储器与内存可见性

原理图没有 Flash、EEPROM、RAM、SD 卡或其他存储器件。

- 参数与网络：`flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false`
- 证据：图 5a406f6a3742 / 第 1 页 / 完整单页全部器件，无存储位号

## 其他事实

### 其他功能分区可见性

原理图未绘出 I2C、SPI、CAN、USB、SDIO、MIPI、I2S、射频、音频、传感器或模拟采样链；核心功能为 DC-DC 与 RS-485 物理层。

- 参数与网络：`i2c_visible=false`；`spi_visible=false`；`can_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false`
- 证据：图 5a406f6a3742 / 第 1 页 / 完整单页功能分区

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp PWR485 系统架构 | `buck=U1 ME3116AM6G`；`transceiver=U2 SP485EEN-L/TR`；`direction=Q1 SS8050 Y1`；`connector=J1 StampPWR485_Pin`；`protection=D3,D4,D5 SP4021-01FTG-C` |
| 电源 | +VIN 输入保护与滤波 | `input=+VIN`；`fuse=F1 1.5A/24V`；`diode=D2 SS34 to GND`；`filter=C2 10uF`；`enable_pullup=R1 100KΩ` |
| 电源 | U1 +5V 降压 | `converter=U1 ME3116AM6G`；`input=+VIN after F1`；`inductor=L1 10uH`；`output=+5V`；`feedback=R2 52.3KΩ,R3 10KΩ`；`output_caps=C6 22uF,C3 22uF,C4 22uF`；`bootstrap=C1 100nF,D1 B5819W SL` |
| 电源 | PWR485 输入电压范围 | `documented_range=9-24V`；`schematic_range_visible=false`；`fuse_marking=1.5A/24V` |
| 总线 | RS-485 接收路径 | `a=U2 pin 6 -> RS485_A`；`b=U2 pin 7 -> RS485_B`；`receiver=U2 pin 1/RO -> R6 1KΩ -> RX`；`b_bias=R5 4.7KΩ to GND`；`a_bias=R10 4.7KΩ to +5V` |
| GPIO 与控制信号 | RS-485 /RE 与 DE 自动方向 | `control=U2 pins 2 /RE and 3 DE`；`pullup=R7 4.7KΩ to +5V`；`transistor=Q1 SS8050 Y1`；`base=TX -> R9 1KΩ`；`emitter=GND` |
| 总线 | RS-485 发送数据路径 | `visible_tx=TX -> R9 -> Q1 direction`；`visible_di=U2 pin 4/DI -> GND`；`tx_to_di_visible=false` |
| 保护电路 | RS485_A/B 三级保护 | `b_to_ground=D3 SP4021-01FTG-C`；`line_to_line=D4 SP4021-01FTG-C`；`a_to_ground=D5 SP4021-01FTG-C` |
| 保护电路 | +5V 输出保护 | `protector=D6 LESD3Z5.0CMT1G`；`rail=+5V`；`return=GND` |
| 接口 | J1 StampPWR485_Pin 针脚 | `pwr485_port1=1:GND,2:VIN,3:A,4:B`；`pwr485_port2=5:GND,6:VIN,7:A,8:B`；`ttl_port=9:GND,10:5V,11:TX,12:RX`；`parallel=true` |
| 总线 | RS-485 波特率测试值 | `documented_stable=9600bps,115200bps`；`documented_test_max=128000bps`；`schematic_baud_visible=false` |
| 总线 | TTL 输入逻辑电平 | `documented_logic_level=3.3V`；`transceiver_supply=+5V`；`logic_threshold_visible=false` |
| GPIO 与控制信号 | +5V 红色指示灯 | `path=+5V -> D7 red 0603 -> R4 4.7KΩ -> GND` |
| 保护电路 | RS-485 终端与隔离可见性 | `termination_visible=false`；`common_mode_choke_visible=false`；`galvanic_isolation_visible=false`；`ports_parallel=true` |
| 总线地址 | 总线地址可见性 | `modbus_address_visible=false`；`i2c_visible=false`；`spi_visible=false`；`numeric_address_visible=false` |
| 时钟 | 时钟、复位与调试可见性 | `mcu_visible=false`；`crystal_visible=false`；`reset_visible=false`；`boot_visible=false`；`swd_visible=false`；`jtag_visible=false` |
| 内存与 Flash | 存储器与内存可见性 | `flash_visible=false`；`eeprom_visible=false`；`ram_visible=false`；`sd_visible=false` |
| 其他事实 | 其他功能分区可见性 | `i2c_visible=false`；`spi_visible=false`；`can_visible=false`；`usb_visible=false`；`sdio_visible=false`；`mipi_visible=false`；`i2s_visible=false`；`rf_visible=false`；`audio_visible=false`；`sensor_visible=false`；`analog_sampling_visible=false` |

## 待确认事项

- `power.documented-range`：产品正文记载 PWR485 输入为 9-24V；原理图只显示 +VIN、F1 1.5A/24V 与 ME3116 电源链，没有打印 9V 下限或完整工作范围。（证据：图 5a406f6a3742 / 第 1 页 / 页面 +VIN/F1/U1 电源链，无输入范围文字）
- `bus.rs485-transmit`：产品功能要求 TX 数据进入 U2 DI，但原理图中 TX 只清晰连接 Q1 方向控制，U2 pin 4/DI 显示直接接 GND，未见 TX 到 DI 的数据连线。（证据：图 5a406f6a3742 / 第 1 页 / 页面 C1-C2 TX/R9/Q1 与 U2 pin 4/DI 区域）
- `bus.documented-baud`：产品正文记载稳定通信 9600/115200bps、最大测试 128000bps；原理图没有打印波特率或 UART 帧格式。（证据：图 5a406f6a3742 / 第 1 页 / 页面 U2/RX/TX/J1 通信路径，无速率文字）
- `bus.documented-logic-level`：产品正文记载 TTL 侧输入逻辑为 3.3V；原理图显示收发器由 +5V 供电，但未打印 RX/TX 输入门限或 3.3V 兼容说明。（证据：图 5a406f6a3742 / 第 1 页 / 页面 U2 VCC/+5V 与 RX/TX 接口，无逻辑门限文字）
- `review.input-range`：Stamp PWR485 的正式 +VIN 输入范围是否确认为 9-24V？；原因：原理图未打印输入范围，F1 的 24V 标记不能单独确认上下限。
- `review.tx-path`：TX 数据如何连接 U2 pin 4/DI，当前图中 DI 对地连接是否为原理图版本错误？；原因：TX 只清晰驱动 Q1 方向控制，发送数据路径无法从本页闭合。
- `review.baud`：稳定 9600/115200bps 与最大测试 128000bps 是否为当前硬件版本的正式通讯指标？；原因：波特率来自产品正文，原理图没有速率或帧格式。
- `review.logic-level`：U2 在 +5V 供电时的 TTL 输入是否正式保证兼容 3.3V 逻辑？；原因：产品正文写 3.3V，原理图未打印输入门限或电平转换器。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `5a406f6a3742855c299234d4cabac6124569492ba192e34ecc26f3a25ba31685` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/567/Sch_StampPWR485_sch_01.png` |

---

源文档：`zh_CN/stamp/stamp_pwr485.md`

源文档 SHA-256：`6d819d07a281888c047fb5ddf52acd3c4580397aa294f63cc1e0199c13fee663`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
