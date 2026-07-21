# Unit ID 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Unit ID |
| SKU | U124 |
| 产品 ID | `unit-id-14401b5e5d23` |
| 源文档 | `zh_CN/unit/id.md` |

## 概述

Unit ID 以 U2 ATECC608B-TNGTLSU-G 安全元件为唯一功能 IC，通过 J1 的 I2C_SCL/I2C_SDA 与外部主机通信。J1 pin3 的 +5V 经 U1 HT7533 稳压为 +3.3V，供 U2 VCC 使用；SCL/SDA 分别由 R1/R2 4.7KΩ 上拉到 +3.3V并直接连接 U2，没有电平转换器。原理图明确显示 U2 pin1-pin3/pin7 为 NC、pin4 GND、pin5 SDA、pin6 SCL、pin8 VCC，板上没有主控、外部存储、时钟、复位或调试接口。正文给出的地址 0x35、内部存储/序列号以及算法与 Trust&GO 预配置能力未直接印在原理图上，需结合对应安全元件资料或实际器件配置确认。

## 检索关键词

`Unit ID`、`U124`、`ATECC608B-TNGTLSU-G`、`ATECC608B`、`Trust&GO`、`TNGTLS`、`HT7533`、`I2C`、`0x35`、`I2C_SCL`、`I2C_SDA`、`J1 HY-2.0_IIC`、`+5V`、`+3.3V`、`R1 4.7KΩ`、`R2 4.7KΩ`、`C1 10uF`、`C2 10uF`、`C3 100nF`、`secure element`、`crypto coprocessor`、`10Kb EEPROM`、`16 key slots`、`72-bit serial number`、`ECC-P256`、`ECDH`、`ECDSA`、`SHA256`、`AES128-GCM`、`pre-provisioned certificate`、`AWS IoT`、`Azure`、`Google Cloud`、`hardware key storage`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | ATECC608B-TNGTLSU-G | I2C 安全元件/加密协处理器，使用 +3.3V 供电 | 图 1fc41dd9fea0 / 第 1 页 / 第 1 页左下 U2 ATECC608B-TNGTLSU-G pin1-pin8 |
| U1 | HT7533 | 将 J1 输入的 +5V 稳压为 +3.3V | 图 1fc41dd9fea0 / 第 1 页 / 第 1 页左上 U1 HT7533，VIN/VOUT/GND |
| J1 | HY-2.0_IIC | 外部 I2C、+5V 和 GND Grove 接口 | 图 1fc41dd9fea0 / 第 1 页 / 第 1 页右侧 J1 HY-2.0_IIC pin1-pin4 |
| R1/R2 | 4.7KΩ | 分别将 I2C_SCL 和 I2C_SDA 上拉到 +3.3V | 图 1fc41dd9fea0 / 第 1 页 / 第 1 页中央 R1/R2 4.7KΩ 与 I2C_SCL/I2C_SDA |
| C1/C2 | 10uF | HT7533 输入 +5V 与输出 +3.3V 的滤波电容 | 图 1fc41dd9fea0 / 第 1 页 / 第 1 页左上 C1/C2 10uF 与 U1 |
| C3 | 100nF | ATECC608B +3.3V 电源去耦电容 | 图 1fc41dd9fea0 / 第 1 页 / 第 1 页左下 C3 100nF，+3.3V 到 GND |

## 系统结构

### Unit ID 系统结构

J1 提供 I2C 和 +5V，U1 生成 +3.3V，U2 ATECC608B-TNGTLSU-G 直接连接 I2C_SCL/I2C_SDA；板上没有额外主控或电平转换器。

- 参数与网络：`secure_element=U2 ATECC608B-TNGTLSU-G`；`regulator=U1 HT7533`；`connector=J1 HY-2.0_IIC`；`bus=I2C`；`onboard_mcu_shown=false`；`level_shifter_shown=false`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页完整原理图全部功能区

## 核心器件

### U2 ATECC608B-TNGTLSU-G

U2 pin1/pin2/pin3 标 NC，pin4=GND，pin5=SDA/I2C_SDA，pin6=SCL/I2C_SCL，pin7=NC，pin8=VCC/+3.3V。

- 参数与网络：`pin_1=NC`；`pin_2=NC`；`pin_3=NC`；`pin_4=GND`；`pin_5=SDA / I2C_SDA`；`pin_6=SCL / I2C_SCL`；`pin_7=NC`；`pin_8=VCC / +3.3V`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页左下 U2 pin1-pin8 编号与网络

## 电源

### U1 HT7533

U1 VIN pin2 接 +5V，VOUT pin3 输出 +3.3V，GND pin1 接地；C1/C2 各 10uF 分别跨接输入/输出到 GND。

- 参数与网络：`input=+5V at U1 pin2`；`output=+3.3V at U1 pin3`；`ground=U1 pin1 GND`；`input_cap=C1 10uF`；`output_cap=C2 10uF`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页左上 U1/C1/C2 与 +5V/+3.3V

### U2 电源

U2 VCC pin8 接 +3.3V、GND pin4 接地，C3 100nF 跨接 +3.3V 与 GND；图中无使能、负载开关、电源监测、充电或电池路径。

- 参数与网络：`vcc=U2 pin8 +3.3V`；`ground=U2 pin4 GND`；`decoupling=C3 100nF`；`enable_shown=false`；`load_switch_shown=false`；`power_monitor_shown=false`；`battery_shown=false`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页左下 U2 pin4/pin8 与 C3

## 接口

### J1 HY-2.0_IIC

J1 pin1=IIC_SCL/I2C_SCL、pin2=IIC_SDA/I2C_SDA、pin3=VCC/+5V、pin4=GND；+5V 是板上电源输入，SCL/SDA 与外部主机双向通信。

- 参数与网络：`pin_1=I2C_SCL`；`pin_2=I2C_SDA`；`pin_3=+5V / power input`；`pin_4=GND`；`scl_direction=host-to-device clock`；`sda_direction=bidirectional`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页右侧 J1 pin1-pin4 网络标注

## 总线

### ATECC608B I2C 总线

J1 I2C_SCL/I2C_SDA 分别直接连接 U2 SCL pin6/SDA pin5，R1/R2 各 4.7KΩ 将两线拉到 +3.3V；图中没有 MOSFET 或专用电平转换 IC。

- 参数与网络：`controller=external host via J1`；`device=U2 ATECC608B-TNGTLSU-G`；`scl=J1.1 I2C_SCL -> U2.6, R1 4.7KΩ to +3.3V`；`sda=J1.2 I2C_SDA -> U2.5, R2 4.7KΩ to +3.3V`；`logic_pullup_rail=+3.3V`；`level_shifter_shown=false`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页 U2 SCL/SDA、R1/R2 与 J1 同名 I2C 网络

## GPIO 与控制信号

### 中断、唤醒与通用 GPIO

U2 仅连接 VCC、GND、SCL、SDA，pin1-pin3/pin7 均标 NC；原理图未引出中断、唤醒、复位或通用 GPIO。

- 参数与网络：`interrupt_shown=false`；`wake_shown=false`；`reset_shown=false`；`general_gpio_shown=false`；`connected_signals=VCC,GND,SCL,SDA`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页 U2 pin1-pin8 与 J1

## 时钟

### 时钟电路

完整原理图未显示晶振、振荡器或外部时钟网络。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页完整图无时钟器件或网络

## 复位

### 复位、BOOT 与调试

完整原理图未显示 RESET、BOOT、调试、下载或测试点连接。

- 参数与网络：`reset_shown=false`；`boot_shown=false`；`debug_connector_shown=false`；`download_connector_shown=false`；`testpoint_shown=false`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页完整图无复位、BOOT、调试或测试接口

## 保护电路

### J1 I2C 与 +5V 保护

完整原理图未在 J1 SCL、SDA、+5V 或 GND 路径画出 TVS、ESD 阵列、保险丝、反接保护或串联信号保护器件。

- 参数与网络：`tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`series_signal_protection_shown=false`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页 J1 至 U1/U2 的全部路径

## 关键网络

### 主机到安全元件路径

关键路径为 J1.1 I2C_SCL→U2.6 SCL、J1.2 I2C_SDA→U2.5 SDA、J1.3 +5V→U1→+3.3V→U2.8 VCC，所有地连接 J1.4/U1.1/U2.4。

- 参数与网络：`scl_path=J1.1->U2.6`；`sda_path=J1.2->U2.5`；`power_path=J1.3 +5V->U1->+3.3V->U2.8`；`ground_path=J1.4,U1.1,U2.4`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页完整 J1/U1/U2 信号与电源路径

## 内存与 Flash

### 外部存储与主控

完整原理图未显示 MCU、协处理器之外的控制器、外部 Flash、EEPROM、RAM、SD 卡或其他外部存储器。

- 参数与网络：`mcu_shown=false`；`additional_coprocessor_shown=false`；`external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false`
- 证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页完整图仅有 U2 安全元件、U1 稳压器和无源器件

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Unit ID 系统结构 | `secure_element=U2 ATECC608B-TNGTLSU-G`；`regulator=U1 HT7533`；`connector=J1 HY-2.0_IIC`；`bus=I2C`；`onboard_mcu_shown=false`；`level_shifter_shown=false` |
| 核心器件 | U2 ATECC608B-TNGTLSU-G | `pin_1=NC`；`pin_2=NC`；`pin_3=NC`；`pin_4=GND`；`pin_5=SDA / I2C_SDA`；`pin_6=SCL / I2C_SCL`；`pin_7=NC`；`pin_8=VCC / +3.3V` |
| 接口 | J1 HY-2.0_IIC | `pin_1=I2C_SCL`；`pin_2=I2C_SDA`；`pin_3=+5V / power input`；`pin_4=GND`；`scl_direction=host-to-device clock`；`sda_direction=bidirectional` |
| 总线 | ATECC608B I2C 总线 | `controller=external host via J1`；`device=U2 ATECC608B-TNGTLSU-G`；`scl=J1.1 I2C_SCL -> U2.6, R1 4.7KΩ to +3.3V`；`sda=J1.2 I2C_SDA -> U2.5, R2 4.7KΩ to +3.3V`；`logic_pullup_rail=+3.3V`；`level_shifter_shown=false` |
| 电源 | U1 HT7533 | `input=+5V at U1 pin2`；`output=+3.3V at U1 pin3`；`ground=U1 pin1 GND`；`input_cap=C1 10uF`；`output_cap=C2 10uF` |
| 电源 | U2 电源 | `vcc=U2 pin8 +3.3V`；`ground=U2 pin4 GND`；`decoupling=C3 100nF`；`enable_shown=false`；`load_switch_shown=false`；`power_monitor_shown=false`；`battery_shown=false` |
| 总线地址 | ATECC608B I2C 地址 | `documented_address=0x35`；`address_width=7-bit`；`device=U2 ATECC608B-TNGTLSU-G`；`address_printed_on_schematic=false`；`address_strap_shown=false` |
| 存储 | ATECC608B 内部安全存储 | `documented_eeprom=10Kb`；`documented_slots=16`；`documented_serial_number=72-bit`；`external_storage_shown=false`；`parameters_printed_on_schematic=false` |
| 其他事实 | 密码学算法与 Trust&GO 配置 | `documented_algorithms=ECC-P256,ECDH,ECDSA,SHA256,AES128-GCM`；`documented_rng=true`；`documented_provisioning=Trust&GO pre-provisioned certificate and key`；`configuration_visible_on_schematic=false` |
| 关键网络 | 主机到安全元件路径 | `scl_path=J1.1->U2.6`；`sda_path=J1.2->U2.5`；`power_path=J1.3 +5V->U1->+3.3V->U2.8`；`ground_path=J1.4,U1.1,U2.4` |
| 保护电路 | J1 I2C 与 +5V 保护 | `tvs_shown=false`；`esd_array_shown=false`；`fuse_shown=false`；`reverse_polarity_protection_shown=false`；`series_signal_protection_shown=false` |
| GPIO 与控制信号 | 中断、唤醒与通用 GPIO | `interrupt_shown=false`；`wake_shown=false`；`reset_shown=false`；`general_gpio_shown=false`；`connected_signals=VCC,GND,SCL,SDA` |
| 时钟 | 时钟电路 | `crystal_shown=false`；`oscillator_shown=false`；`clock_net_shown=false` |
| 复位 | 复位、BOOT 与调试 | `reset_shown=false`；`boot_shown=false`；`debug_connector_shown=false`；`download_connector_shown=false`；`testpoint_shown=false` |
| 内存与 Flash | 外部存储与主控 | `mcu_shown=false`；`additional_coprocessor_shown=false`；`external_flash_shown=false`；`external_eeprom_shown=false`；`external_ram_shown=false`；`sd_card_shown=false` |

## 待确认事项

- `address.documented-0x35`：产品正文列出 7 位 I2C 地址 0x35；原理图确认 U2 为总线设备，但未打印地址或地址绑带，因此需结合 TNGTLSU-G 配置资料或 I2C 扫描确认。（证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页 U2 SCL/SDA 与 J1 I2C，页面无地址数值）
- `storage.documented-secure-memory`：产品正文描述 10Kb EEPROM、最多 16 个密钥/证书/数据槽和 72 位唯一序列号；原理图仅标器件完整料号，未打印容量、槽位或序列号字段。（证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页 U2 ATECC608B-TNGTLSU-G，无存储容量/槽位/序列号标注）
- `other.documented-security-capabilities`：产品正文列出 ECC-P256/ECDH/ECDSA、SHA256、AES128-GCM、随机数和预置证书/密钥；原理图只确认 TNGTLSU-G 料号，无法显示实际配置区、证书内容或已启用算法。（证据：图 1fc41dd9fea0 / 第 1 页 / 第 1 页 U2 ATECC608B-TNGTLSU-G，页面无算法或证书配置）
- `review.i2c-address`：请依据 ATECC608B-TNGTLSU-G 配置资料或 I2C 扫描确认 7 位地址 0x35。；原因：原理图确认器件和 I2C 连接，但未打印地址值。
- `review.secure-memory`：请依据 ATECC608B-TNGTLSU-G 数据手册与实际配置确认 10Kb EEPROM、16 个槽位和 72 位序列号。；原因：这些参数来自产品正文，原理图只打印完整料号。
- `review.security-capabilities`：请依据 TNGTLSU-G 数据手册、配置区和证书读取结果确认算法、随机数及 Trust&GO 预配置能力。；原因：原理图无法展示芯片内部启用算法、锁定位或预置证书内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `1fc41dd9fea0f94a05a3af1d5d08e9acb6b20544b311f08d8c4c5b238d7e7459` | `https://static-cdn.m5stack.com/resource/docs/products/unit/id/id_sch_01.webp` |

---

源文档：`zh_CN/unit/id.md`

源文档 SHA-256：`db037f3b6b922f5ebd13839763a2fc2f94c9d900ae357613e523981986117a92`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
