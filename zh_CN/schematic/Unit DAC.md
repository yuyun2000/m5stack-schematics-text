# Unit DAC 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit DAC |
| SKU | U012 |
| 产品 ID | `unit-dac-fadb28ec7087` |
| 源文档 | `zh_CN/unit/dac.md` |

## 概述

Unit DAC 以 MCP4725_DAC（U2）为 I2C 数模转换器，U2 Vout 经 LM321MFX（U1）电压跟随器缓冲后输出到 P1 pin 1，P1 pin 2 接 GND。J1 四针接口引出 IIC_SCL、IIC_SDA、VCC 和 GND，SCL/SDA 各由 4.7KΩ 上拉到 VCC，U2 A0 接地。U1 与 U2 均直接使用 J1 的 VCC 供电，C1/C2/C3 分别提供接口、DAC 和运放去耦；原理图未打印 VCC 数值、数字地址、分辨率、EEPROM 或绝对输出范围。

## 检索关键词

`Unit DAC`、`U012`、`MCP4725_DAC`、`MCP4725`、`LM321MFX`、`IIC_Socket_4P`、`Header 2`、`I2C`、`0x60`、`IIC_SCL`、`IIC_SDA`、`A0`、`Vout`、`OUTPUT`、`VCC`、`VSS`、`R1 4.7KΩ`、`R2 4.7KΩ`、`C1 100nF`、`C2 100nF`、`C3 100nF`、`12-bit DAC`、`EEPROM`、`voltage follower`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | MCP4725_DAC | 接收 I2C 数据并在 Vout pin 1 生成模拟电压 | 图 bbe5ea067bbf / 第 1 页 / 页 1 中央 U2 MCP4725_DAC：A0 pin 6、SCL pin 5、SDA pin 4、Vout pin 1、Vss pin 2、Vdd pin 3 |
| U1 | LM321MFX | 将 U2 Vout 缓冲到 P1 输出的电压跟随器 | 图 bbe5ea067bbf / 第 1 页 / 页 1 右中 U1 LM321MFX：+IN pin 1 接 U2 Vout，OUTPUT pin 4 回接 -IN pin 3 并连接 P1 |
| J1 | IIC_Socket_4P | 外部 I2C、VCC 和 GND 接口 | 图 bbe5ea067bbf / 第 1 页 / 页 1 左侧 J1 IIC_Socket_4P：pin 1 IIC_SCL、pin 2 IIC_SDA、pin 3 VCC、pin 4 GND |
| P1 | Header 2 | 缓冲模拟电压输出与地连接器 | 图 bbe5ea067bbf / 第 1 页 / 页 1 右侧 P1 Header 2：pin 1 接 U1 OUTPUT，pin 2 接 GND |
| R1/R2 | 4.7KΩ | IIC_SCL 与 IIC_SDA 到 VCC 的上拉电阻 | 图 bbe5ea067bbf / 第 1 页 / 页 1 左中：R1/R2 均 4.7KΩ，上端接 VCC，下端分别接 IIC_SCL/IIC_SDA |
| C1/C2/C3 | 100nF | J1/U2/U1 的 VCC 电源去耦电容 | 图 bbe5ea067bbf / 第 1 页 / 页 1：C1、C2、C3 均标 100nF，分别位于 J1、U2 Vdd、U1 VCC 附近并接 GND |

## 系统结构

### Unit DAC

J1 的 IIC_SCL/IIC_SDA 连接 U2 MCP4725_DAC，U2 Vout 进入 U1 LM321MFX 电压跟随器，U1 OUTPUT 直接送到 P1 pin 1；J1、U2 和 U1 共用 VCC/GND。

- 参数与网络：`digital_interface=J1 IIC_SCL,IIC_SDA`；`dac=U2 MCP4725_DAC`；`buffer=U1 LM321MFX`；`analog_output=P1 pin 1`；`power=VCC,GND`
- 证据：图 bbe5ea067bbf / 第 1 页 / 整页：J1/R1/R2/U2/U1/P1 与 VCC/GND 直接连线

## 电源

### IIC_SCL/IIC_SDA 上拉

R1 和 R2 均为 4.7KΩ，分别将 IIC_SCL 与 IIC_SDA 上拉到 VCC。

- 参数与网络：`scl_pullup=R1 4.7KΩ`；`sda_pullup=R2 4.7KΩ`；`rail=VCC`
- 证据：图 bbe5ea067bbf / 第 1 页 / 页 1 左中：VCC-R1-IIC_SCL 与 VCC-R2-IIC_SDA 支路

### U1/U2 VCC 供电

U2 Vdd pin 3 与 U1 VCC pin 5 均接 VCC，U2 Vss pin 2 与 U1 VSS pin 2 均接 GND。

- 参数与网络：`dac_supply=U2 Vdd pin 3 VCC`；`dac_ground=U2 Vss pin 2 GND`；`opamp_supply=U1 VCC pin 5`；`opamp_ground=U1 VSS pin 2`
- 证据：图 bbe5ea067bbf / 第 1 页 / 页 1 中右 U2 pins 2/3 与 U1 pins 2/5 的 VCC/GND 网络

### VCC 去耦

C1、C2、C3 均为 100nF 并连接 VCC 与 GND，分别位于 J1、U2 和 U1 电源附近。

- 参数与网络：`interface_capacitor=C1 100nF`；`dac_capacitor=C2 100nF`；`opamp_capacitor=C3 100nF`；`rail=VCC`；`return=GND`
- 证据：图 bbe5ea067bbf / 第 1 页 / 页 1 C1/C2/C3 三个 VCC-GND 100nF 支路

## 接口

### J1 IIC_Socket_4P

J1 pin 1 接 IIC_SCL，pin 2 接 IIC_SDA，pin 3 接 VCC，pin 4 接 GND。

- 参数与网络：`pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC`；`pin_4=GND`
- 证据：图 bbe5ea067bbf / 第 1 页 / 页 1 左侧 J1 pins 1~4、IIC_SCL/IIC_SDA/VCC/GND 标签

### P1 Header 2

P1 pin 1 接 U1 OUTPUT pin 4，作为缓冲模拟电压输出；P1 pin 2 接 GND。

- 参数与网络：`pin_1=buffered analog output from U1 pin 4`；`pin_2=GND`；`direction=Unit to external load`
- 证据：图 bbe5ea067bbf / 第 1 页 / 页 1 右侧 P1 pins 1/2 与 U1 OUTPUT/GND 连线

## 总线

### U2 I2C

J1 pin 1 的 IIC_SCL 连接 U2 SCL pin 5，J1 pin 2 的 IIC_SDA 连接 U2 SDA pin 4；两条总线均上拉到 VCC。

- 参数与网络：`device=U2 MCP4725_DAC`；`scl=J1 pin 1 to U2 pin 5`；`sda=J1 pin 2 to U2 pin 4`；`pullup_rail=VCC`；`controller=external I2C host`
- 证据：图 bbe5ea067bbf / 第 1 页 / 页 1 左中 J1/U2 的 IIC_SCL/IIC_SDA 同名网络

## GPIO 与控制信号

### U2 A0

U2 A0 pin 6 在原理图中连接 GND，没有绘出跳线、焊盘或外部地址选择器。

- 参数与网络：`device=U2 MCP4725_DAC`；`pin=A0 pin 6`；`strap=GND`；`configurable_selector=null`
- 证据：图 bbe5ea067bbf / 第 1 页 / 页 1 中央 U2 左侧 A0 pin 6 的对地连线和 GND 符号

## 时钟

### 外部时钟

本页未绘出晶振、振荡器或时钟网络，U2 对外仅显示 A0、SCL、SDA、Vout、Vss 和 Vdd。

- 参数与网络：`external_crystal=null`；`external_oscillator=null`；`clock_net=null`
- 证据：图 bbe5ea067bbf / 第 1 页 / 整页无晶振/振荡器位号；U2 六引脚符号无时钟脚

## 保护电路

### I2C 与模拟输出保护

本页没有绘出 TVS、ESD 阵列、保险丝、反接保护或模拟输出限流器件。

- 参数与网络：`i2c_esd=null`；`output_esd=null`；`fuse=null`；`reverse_polarity=null`；`output_series_resistor=null`
- 证据：图 bbe5ea067bbf / 第 1 页 / 整页可见器件仅 J1/R1/R2/C1/U2/C2/U1/C3/P1，无保护位号

## 关键网络

### Unit DAC 关键网络索引

关键路径为 J1 pin 1/2→IIC_SCL/IIC_SDA→U2 pins 5/4，U2 Vout pin 1→U1 +IN pin 1→U1 OUTPUT pin 4→P1 pin 1，以及 J1 pin 3 VCC→U2/U1/R1/R2。

- 参数与网络：`i2c_path=J1.1/2-U2.5/4`；`analog_path=U2.1-U1.1-U1.4-P1.1`；`feedback=U1.4-U1.3`；`power_path=J1.3 VCC-U2.3/U1.5/R1/R2`；`ground=J1.4,U2.2,U1.2,P1.2`
- 证据：图 bbe5ea067bbf / 第 1 页 / 整页 IIC_SCL/IIC_SDA/VCC/GND 与 U2 Vout/U1 OUTPUT 直接连线

## 模拟电路

### U2 Vout

U2 Vout pin 1 直接连接 U1 +IN pin 1，未在 DAC 与运放之间绘出串联电阻或 RC 滤波器。

- 参数与网络：`source=U2 Vout pin 1`；`destination=U1 +IN pin 1`；`series_resistor=null`；`filter=null`
- 证据：图 bbe5ea067bbf / 第 1 页 / 页 1 中右 U2 Vout 到 U1 +IN 的直接水平连线

### U1 LM321MFX

U1 OUTPUT pin 4 回接 -IN pin 3，+IN pin 1 接 U2 Vout，形成电压跟随连接；OUTPUT pin 4 同时直接连接 P1 pin 1。

- 参数与网络：`non_inverting_input=pin 1 from U2 Vout`；`inverting_input=pin 3 tied to output`；`output=pin 4 to P1 pin 1`；`configuration=voltage follower`
- 证据：图 bbe5ea067bbf / 第 1 页 / 页 1 右中 U1 +IN/-IN/OUTPUT 及上方反馈线

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit DAC | `digital_interface=J1 IIC_SCL,IIC_SDA`；`dac=U2 MCP4725_DAC`；`buffer=U1 LM321MFX`；`analog_output=P1 pin 1`；`power=VCC,GND` |
| 接口 | J1 IIC_Socket_4P | `pin_1=IIC_SCL`；`pin_2=IIC_SDA`；`pin_3=VCC`；`pin_4=GND` |
| 总线 | U2 I2C | `device=U2 MCP4725_DAC`；`scl=J1 pin 1 to U2 pin 5`；`sda=J1 pin 2 to U2 pin 4`；`pullup_rail=VCC`；`controller=external I2C host` |
| 电源 | IIC_SCL/IIC_SDA 上拉 | `scl_pullup=R1 4.7KΩ`；`sda_pullup=R2 4.7KΩ`；`rail=VCC` |
| GPIO 与控制信号 | U2 A0 | `device=U2 MCP4725_DAC`；`pin=A0 pin 6`；`strap=GND`；`configurable_selector=null` |
| 总线地址 | Unit DAC I2C 地址 | `device=U2 MCP4725_DAC`；`a0=GND`；`schematic_address=null`；`address_rule_source_needed=MCP4725 datasheet and ordering code` |
| 模拟电路 | U2 Vout | `source=U2 Vout pin 1`；`destination=U1 +IN pin 1`；`series_resistor=null`；`filter=null` |
| 模拟电路 | U1 LM321MFX | `non_inverting_input=pin 1 from U2 Vout`；`inverting_input=pin 3 tied to output`；`output=pin 4 to P1 pin 1`；`configuration=voltage follower` |
| 接口 | P1 Header 2 | `pin_1=buffered analog output from U1 pin 4`；`pin_2=GND`；`direction=Unit to external load` |
| 电源 | U1/U2 VCC 供电 | `dac_supply=U2 Vdd pin 3 VCC`；`dac_ground=U2 Vss pin 2 GND`；`opamp_supply=U1 VCC pin 5`；`opamp_ground=U1 VSS pin 2` |
| 电源 | VCC 去耦 | `interface_capacitor=C1 100nF`；`dac_capacitor=C2 100nF`；`opamp_capacitor=C3 100nF`；`rail=VCC`；`return=GND` |
| 电源 | J1 VCC 额定值 | `connector_pin=J1 pin 3`；`net=VCC`；`loads=U2 Vdd,U1 VCC,R1,R2`；`schematic_voltage=null` |
| 模拟电路 | DAC 输出规格 | `dac=U2 MCP4725_DAC`；`buffer=U1 LM321MFX`；`schematic_resolution=null`；`schematic_output_range=null`；`schematic_output_current=null`；`schematic_linearity=null` |
| 内存与 Flash | MCP4725 非易失存储能力 | `device=U2 MCP4725_DAC`；`external_eeprom=null`；`schematic_internal_eeprom=null`；`schematic_write_cycle=null`；`capability_source_needed=MCP4725 datasheet` |
| 时钟 | 外部时钟 | `external_crystal=null`；`external_oscillator=null`；`clock_net=null` |
| 保护电路 | I2C 与模拟输出保护 | `i2c_esd=null`；`output_esd=null`；`fuse=null`；`reverse_polarity=null`；`output_series_resistor=null` |
| 关键网络 | Unit DAC 关键网络索引 | `i2c_path=J1.1/2-U2.5/4`；`analog_path=U2.1-U1.1-U1.4-P1.1`；`feedback=U1.4-U1.3`；`power_path=J1.3 VCC-U2.3/U1.5/R1/R2`；`ground=J1.4,U2.2,U1.2,P1.2` |

## 待确认事项

- `address.i2c-not-printed`：原理图明确显示 A0 pin 6 接 GND，但没有打印十六进制 I2C 地址；数字地址仍需结合 MCP4725 的器件地址规则确认。（证据：图 bbe5ea067bbf / 第 1 页 / 页 1 U2 A0/SCL/SDA 区域，页面无 0x 地址文字）
- `power.vcc-rating-not-shown`：J1 pin 3、U2 Vdd 和 U1 VCC 共用名为 VCC 的电源，但原理图没有打印 VCC 数值，无法仅凭该页确认接口供电电压。（证据：图 bbe5ea067bbf / 第 1 页 / 整页 VCC 网络，未见 3.3V/5V 数字标注）
- `analog.output-specs-not-shown`：原理图显示 MCP4725_DAC 与 LM321MFX 的连接，但没有打印 DAC 分辨率、输出电压范围、输出电流、线性度或建立时间。（证据：图 bbe5ea067bbf / 第 1 页 / 页 1 U2/U1/P1 模拟链，仅有型号和引脚，无性能参数）
- `memory.eeprom-not-shown`：原理图只标注器件型号 MCP4725_DAC，没有绘出或文字说明 EEPROM 容量、写入路径、上电恢复行为或写周期。（证据：图 bbe5ea067bbf / 第 1 页 / 页 1 U2 器件符号与整页，未见 EEPROM 文字或外部存储器）
- `review.i2c-address`：A0 接 GND 时，本产品所装 MCP4725 变体的 I2C 地址是否为 0x60？；原因：原理图未打印数字地址，MCP4725 地址还取决于器件固定地址位和订货后缀，需要数据手册/BOM 确认。
- `review.vcc-rating`：J1 pin 3 的 VCC 额定供电电压是多少？；原因：原理图只使用 VCC 网络名，没有打印电压数值；该值同时影响 I2C 电平、DAC 和运放供电。
- `review.output-specs`：当前硬件的 DAC 分辨率、P1 输出范围、带载能力和误差指标分别是什么？；原因：原理图只确认 MCP4725_DAC 和 LM321MFX 跟随器拓扑，没有打印性能参数，且输出范围受 VCC 与器件规格限制。
- `review.eeprom-capability`：本产品 MCP4725 的 EEPROM 写入与上电恢复行为、写入次数和限制是什么？；原因：内部 EEPROM 能力不在原理图中表达，需要器件数据手册和软件实现确认。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `bbe5ea067bbf4836c1d296bc29f435407e26701a5e22f20e0b20723afd8d5bf9` | `https://static-cdn.m5stack.com/resource/docs/products/unit/dac/dac_sch_01.webp` |

---

源文档：`zh_CN/unit/dac.md`

源文档 SHA-256：`1609713c4ca03c37faf61f5531b2c23d61a2d176b0723ec56078e8eb796e67c9`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
