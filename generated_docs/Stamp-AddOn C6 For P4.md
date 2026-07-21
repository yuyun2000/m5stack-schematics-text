# Stamp-AddOn C6 For P4 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-AddOn C6 For P4 |
| SKU | A172 |
| 产品 ID | `stamp-addon-c6-for-p4-e374038cd38a` |
| 源文档 | `zh_CN/stamp/Stamp-AddOn_C6_For_P4.md` |

## 概述

Stamp-AddOn C6 For P4 通过 J1 的六线 SDIO2 总线与主机连接，U1 SY8089AAAC 在 RST 控制下把 SYS_5V 转换为 WLAN_3.3V，为 U2 无线模组符号供电。U2 的 IO18-IO23 通过 22Ω 串阻连接 SDIO2_CMD/CLK/D0-D3，并配置 4.7KΩ 上拉；IO12/IO13 引出原生 USB 测试点，RXD0/TXD0、IO8、IO9、复位、电源和地也设有测试点。J1 还引出 RF_C6_IO2、RF_C6_IO9、RST 和 SYS_5V。原理图没有打印 U2 完整料号，也没有展开模组内部 Flash、时钟或射频实现，因此正文所列 ESP32-C6-MINI-1-N4、ESP32-C6FH4、4MB Flash、2.4GHz Wi-Fi 6、Stamp-P4 适配与工作温度需结合 BOM、模组资料和实机确认。

## 检索关键词

`Stamp-AddOn C6 For P4`、`A172`、`ESP32-C6`、`ESP32-C6-MINI-1-N4`、`ESP32-C6FH4`、`Stamp-P4`、`SY8089AAAC`、`FTC201610S2R2MBCA`、`HC-PBB40C-20DP-0.4`、`HC-PBB40C-20DP-0.4V-02`、`SDIO`、`SDIO2_CMD`、`SDIO2_CLK`、`SDIO2_D0`、`SDIO2_D1`、`SDIO2_D2`、`SDIO2_D3`、`RF_C6_USB_N`、`RF_C6_USB_P`、`RF_C6_TXD`、`RF_C6_RXD`、`RF_C6_RST`、`RF_C6_IO2`、`RF_C6_IO8`、`RF_C6_IO9`、`SYS_5V`、`WLAN_3.3V`、`4MB Flash`、`2.4GHz Wi-Fi 6`、`TP1`、`TP9`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U2 | 未标注 | 3.3V 无线模组符号，连接 SDIO2、原生 USB、UART、复位和 GPIO；图面未打印完整料号 | 图 cade20681dc0 / 第 1 页 / 第 1 页网格 2B-4C，U2 3V3/EN/IO/RXD0/TXD0 与多脚 GND/NC |
| U1 | SY8089AAAC | 受 RST 控制、把 SYS_5V 降压为 WLAN_3.3V 的开关稳压器 | 图 cade20681dc0 / 第 1 页 / 第 1 页网格 1C-2C，U1 SY8089AAAC |
| L4 | FTC201610S2R2MBCA | U1 LX 至 WLAN_3.3V 的降压电感 | 图 cade20681dc0 / 第 1 页 / 第 1 页网格 1C-2C，L4 FTC201610S2R2MBCA |
| J1 | HC-PBB40C-20DP-0.4 | 20 针 SDIO/电源/控制连接器，引出六线 SDIO2、SYS_5V、RST、IO2、IO9 和 GND | 图 cade20681dc0 / 第 1 页 / 第 1 页网格 1A-1B，J1 HC-PBB40C-20DP-0.4 |
| R2/R3 | 22R/1% | U2 IO12/IO13 到 RF_C6_USB_N/RF_C6_USB_P 的 USB 数据串联电阻 | 图 cade20681dc0 / 第 1 页 / 第 1 页网格 3B-4B，U2 IO12/IO13 与 R2/R3 |
| R4/R6/R5/R17/R18/R19 | 22R/1% | U2 IO18-IO23 到 SDIO2_CMD/CLK/D0-D3 的六路串联电阻 | 图 cade20681dc0 / 第 1 页 / 第 1 页网格 3B-4C，U2 IO18-IO23 的六只 22R/1% 电阻 |
| TP1-TP9 | Test Point | 引出 WLAN_3.3V、UART、复位、IO9、GND、USB N/P 与 IO8 的调试测试点 | 图 cade20681dc0 / 第 1 页 / 第 1 页网格 1B-2B，Debug Interface TP1-TP9 |
| R11/R16/C1 | 10K/1%, 0R/1%, 1uF/10V | RF_C6_RST 的上拉、主机 RST 串联连接和 RC 延时网络 | 图 cade20681dc0 / 第 1 页 / 第 1 页网格 4B，RST-R16-RF_C6_RST 与 R11/C1 |

## 系统结构

### Stamp-AddOn C6 For P4 系统结构

J1 接收 SYS_5V、RST 和主机 SDIO2 信号；U1 SY8089AAAC 生成 WLAN_3.3V，为 U2 供电；U2 连接六线 SDIO2、原生 USB、UART、GPIO 和调试测试点。

- 参数与网络：`host_connector=J1`；`converter=U1 SY8089AAAC`；`wireless_symbol=U2`；`host_bus=SDIO2`；`debug=TP1-TP9`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页完整 SDIO Interface、Debug Interface、DCDC 与 U2 分区

## 电源

### SYS_5V 至 WLAN_3.3V 降压

SYS_5V 接 U1 SY8089AAAC IN pin4，RST 接 EN pin1，LX pin3 经 L4 FTC201610S2R2MBCA 输出 WLAN_3.3V；图面分别标注 SYS_5V Imax=500mA、WLAN_3.3V Imax=600mA。

- 参数与网络：`input=SYS_5V`；`input_annotation=Imax=500mA`；`converter=U1 SY8089AAAC`；`enable=RST`；`inductor=L4 FTC201610S2R2MBCA`；`output=WLAN_3.3V`；`output_annotation=Imax=600mA`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 1C-2C，DCDC:3.3V_600mA

### U1 反馈与滤波网络

U1 FB pin5 使用 R1 100K/1% 与 R13 22K/1% 分压，C19 标 NC 并联在 R1 两端；SYS_5V 侧配置 C21 10uF/10V、C20 100nF/10V，WLAN_3.3V 侧配置 C22 10uF/10V、C23 100nF/10V。

- 参数与网络：`feedback=R1 100K/1%,R13 22K/1%`；`feedforward_cap=C19 NC`；`input_caps=C21 10uF/10V,C20 100nF/10V`；`output_caps=C22 10uF/10V,C23 100nF/10V`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 1C-2C，U1/L4/R1/R13/C19-C23

### U2 3.3V 供电

WLAN_3.3V 接 U2 3V3 pin3，并由 C6 0.1uF/16V 和 C2-C5 电容组对地去耦；U2 的多只 GND 引脚统一接地。

- 参数与网络：`rail=WLAN_3.3V`；`u2_pin=3V3 pin3`；`known_decoupling=C6 0.1uF/16V`；`additional_caps=C2,C3,C4,C5`；`ground_pins=U2 pins1,2,11,14,36-53`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 2B-4B，U2 3V3/GND 与 C2-C6

## 接口

### J1 20 针连接器

J1 pins1/3/5/7/9/11/13/15 分别为 RF_C6_IO2、SDIO2_D3、SDIO2_D2、SDIO2_D0、SDIO2_D1、SDIO2_CMD、SDIO2_CLK、RST；pin10 经 R14 0R 接 RF_C6_IO9，pins16/18 接 SYS_5V，pins2/4/17/19/20 与 SH 接 GND，pins12/14 未连接。

- 参数与网络：`odd_signals=1 IO2,3 D3,5 D2,7 D0,9 D1,11 CMD,13 CLK,15 RST`；`io9=pin10 via R14 0R`；`power=pins16,18 SYS_5V`；`ground=pins2,4,17,19,20,SH`；`not_connected=pins12,14`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 1A-1B，J1 pins1-20 与 SH

## 总线

### U2 六线 SDIO2 映射

U2 IO18 pin24、IO19 pin25、IO20 pin26、IO21 pin27、IO22 pin28、IO23 pin29 分别连接 SDIO2_CMD、SDIO2_CLK、SDIO2_D0、SDIO2_D1、SDIO2_D2、SDIO2_D3。

- 参数与网络：`cmd=U2.IO18 pin24`；`clk=U2.IO19 pin25`；`d0=U2.IO20 pin26`；`d1=U2.IO21 pin27`；`d2=U2.IO22 pin28`；`d3=U2.IO23 pin29`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 3B-4C，U2 IO18-IO23 与 SDIO2_CMD/CLK/D0-D3

### SDIO2 串阻与上拉

SDIO2_CMD/CLK/D0/D1/D2/D3 分别串联 R4/R6/R5/R17/R18/R19，均为 22R/1%；对应网络分别由 R10/R12/R20/R21/R22/R23 以 4.7K/1% 上拉到 WLAN_3.3V。

- 参数与网络：`series=CMD R4,CLK R6,D0 R5,D1 R17,D2 R18,D3 R19; all 22R/1%`；`pullups=CMD R10,CLK R12,D0 R20,D1 R21,D2 R22,D3 R23; all 4.7K/1%`；`rail=WLAN_3.3V`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 3B-4C，六线 SDIO 电阻阵列

### U2 原生 USB 信号

U2 IO12 pin17 经 R2 22R/1% 形成 RF_C6_USB_N 并接 TP7，IO13 pin18 经 R3 22R/1% 形成 RF_C6_USB_P 并接 TP8；本页没有画出 USB 连接器。

- 参数与网络：`usb_n=U2.IO12 pin17 -> R2 22R/1% -> RF_C6_USB_N -> TP7`；`usb_p=U2.IO13 pin18 -> R3 22R/1% -> RF_C6_USB_P -> TP8`；`connector_shown=false`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 2B-4B，U2 IO12/IO13、R2/R3 与 TP7/TP8

## GPIO 与控制信号

### RF_C6_IO2/IO8/IO9

U2 IO2 pin5 直接接 J1 pin1；U2 IO8 pin22 形成 RF_C6_IO8 并接 TP9，由 R7 4.7K/1% 上拉；U2 IO9 pin23 形成 RF_C6_IO9，接 TP5 并经 R14 0R 接 J1 pin10，由 R9 4.7K/1% 上拉。

- 参数与网络：`io2=U2.IO2 pin5 -> J1.1`；`io8=U2.IO8 pin22 -> TP9; R7 4.7K/1% pull-up`；`io9=U2.IO9 pin23 -> TP5 -> R14 0R -> J1.10; R9 4.7K/1% pull-up`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 1A-4C，U2 IO2/IO8/IO9、J1、TP5/TP9 与上拉

### U2 未连接 GPIO

U2 IO3、IO4、IO5、IO0、IO1、IO6、IO7、IO14、IO15 均在器件引脚处标记未连接；U2 另有 pins4/7/21/32/33/34/35 标 NC。

- 参数与网络：`unused_gpio=IO3,IO4,IO5,IO0,IO1,IO6,IO7,IO14,IO15`；`module_nc_pins=4,7,21,32,33,34,35`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 2B-3C，U2 红色未连接叉号与 NC 引脚

## 时钟

### 外部时钟

完整原理图页未显示晶振、振荡器或外部时钟网络，U2 内部时钟实现未在本页展开。

- 参数与网络：`crystal_shown=false`；`oscillator_shown=false`；`external_clock_net_shown=false`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页完整图无 Y/X 晶振或 CLK 源器件

## 复位

### RST 与 RF_C6_RST

J1 pin15 的 RST 同时连接 U1 EN，并由 R15 100K/1% 下拉；RST 经 R16 0R/1% 形成 RF_C6_RST，连接 U2 EN pin8 和 TP4，R11 10K/1% 将 RF_C6_RST 上拉到 WLAN_3.3V，C1 1uF/10V 对地。

- 参数与网络：`host_reset=J1.15 RST`；`dcdc_enable=U1.EN pin1`；`rst_pulldown=R15 100K/1%`；`series=R16 0R/1%`；`module_reset=RF_C6_RST -> U2.EN pin8,TP4`；`pullup=R11 10K/1%`；`capacitor=C1 1uF/10V`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 1A-4C，J1 RST、U1 EN、R15/R16/R11/C1 与 U2 EN

## 内存与 Flash

### 外部存储器

完整原理图页未展示独立 Flash、PSRAM、EEPROM、SD 卡或其他存储器器件；U2 内部存储配置未在本页展开。

- 参数与网络：`flash_shown=false`；`psram_shown=false`；`eeprom_shown=false`；`sd_card_shown=false`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页完整图无独立存储器

## 射频

### 无线射频实现

完整原理图页没有画出射频引脚、匹配网络、天线或天线连接器，U2 内部或板上其他层级的射频实现不在本页展开。

- 参数与网络：`rf_pin_shown=false`；`matching_network_shown=false`；`antenna_shown=false`；`antenna_connector_shown=false`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页完整图无 RF/ANT 电路分区

## 调试与烧录

### U2 UART0 调试信号

U2 RXD0 pin30 直接连接 RF_C6_RXD 和 TP3；U2 TXD0 pin31 经 R8 499R/1% 连接 RF_C6_TXD 和 TP2；R24/R25 标为 NC 的可选上拉位置。

- 参数与网络：`rx=U2.RXD0 pin30 -> RF_C6_RXD -> TP3`；`tx=U2.TXD0 pin31 -> R8 499R/1% -> RF_C6_TXD -> TP2`；`optional_pullups=R24/R25 NC`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 2B-4C，U2 RXD0/TXD0、R8、R24/R25 与 TP2/TP3

### TP1-TP9 调试测试点

TP1=WLAN_3.3V、TP2=RF_C6_TXD、TP3=RF_C6_RXD、TP4=RF_C6_RST、TP5=RF_C6_IO9、TP6=GND、TP7=RF_C6_USB_N、TP8=RF_C6_USB_P、TP9=RF_C6_IO8。

- 参数与网络：`TP1=WLAN_3.3V`；`TP2=RF_C6_TXD`；`TP3=RF_C6_RXD`；`TP4=RF_C6_RST`；`TP5=RF_C6_IO9`；`TP6=GND`；`TP7=RF_C6_USB_N`；`TP8=RF_C6_USB_P`；`TP9=RF_C6_IO8`
- 证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 1B-2B，Debug Interface

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Stamp-AddOn C6 For P4 系统结构 | `host_connector=J1`；`converter=U1 SY8089AAAC`；`wireless_symbol=U2`；`host_bus=SDIO2`；`debug=TP1-TP9` |
| 电源 | SYS_5V 至 WLAN_3.3V 降压 | `input=SYS_5V`；`input_annotation=Imax=500mA`；`converter=U1 SY8089AAAC`；`enable=RST`；`inductor=L4 FTC201610S2R2MBCA`；`output=WLAN_3.3V`；`output_annotation=Imax=600mA` |
| 电源 | U1 反馈与滤波网络 | `feedback=R1 100K/1%,R13 22K/1%`；`feedforward_cap=C19 NC`；`input_caps=C21 10uF/10V,C20 100nF/10V`；`output_caps=C22 10uF/10V,C23 100nF/10V` |
| 电源 | U2 3.3V 供电 | `rail=WLAN_3.3V`；`u2_pin=3V3 pin3`；`known_decoupling=C6 0.1uF/16V`；`additional_caps=C2,C3,C4,C5`；`ground_pins=U2 pins1,2,11,14,36-53` |
| 接口 | J1 20 针连接器 | `odd_signals=1 IO2,3 D3,5 D2,7 D0,9 D1,11 CMD,13 CLK,15 RST`；`io9=pin10 via R14 0R`；`power=pins16,18 SYS_5V`；`ground=pins2,4,17,19,20,SH`；`not_connected=pins12,14` |
| 总线 | U2 六线 SDIO2 映射 | `cmd=U2.IO18 pin24`；`clk=U2.IO19 pin25`；`d0=U2.IO20 pin26`；`d1=U2.IO21 pin27`；`d2=U2.IO22 pin28`；`d3=U2.IO23 pin29` |
| 总线 | SDIO2 串阻与上拉 | `series=CMD R4,CLK R6,D0 R5,D1 R17,D2 R18,D3 R19; all 22R/1%`；`pullups=CMD R10,CLK R12,D0 R20,D1 R21,D2 R22,D3 R23; all 4.7K/1%`；`rail=WLAN_3.3V` |
| 总线 | U2 原生 USB 信号 | `usb_n=U2.IO12 pin17 -> R2 22R/1% -> RF_C6_USB_N -> TP7`；`usb_p=U2.IO13 pin18 -> R3 22R/1% -> RF_C6_USB_P -> TP8`；`connector_shown=false` |
| 调试与烧录 | U2 UART0 调试信号 | `rx=U2.RXD0 pin30 -> RF_C6_RXD -> TP3`；`tx=U2.TXD0 pin31 -> R8 499R/1% -> RF_C6_TXD -> TP2`；`optional_pullups=R24/R25 NC` |
| GPIO 与控制信号 | RF_C6_IO2/IO8/IO9 | `io2=U2.IO2 pin5 -> J1.1`；`io8=U2.IO8 pin22 -> TP9; R7 4.7K/1% pull-up`；`io9=U2.IO9 pin23 -> TP5 -> R14 0R -> J1.10; R9 4.7K/1% pull-up` |
| 调试与烧录 | TP1-TP9 调试测试点 | `TP1=WLAN_3.3V`；`TP2=RF_C6_TXD`；`TP3=RF_C6_RXD`；`TP4=RF_C6_RST`；`TP5=RF_C6_IO9`；`TP6=GND`；`TP7=RF_C6_USB_N`；`TP8=RF_C6_USB_P`；`TP9=RF_C6_IO8` |
| 复位 | RST 与 RF_C6_RST | `host_reset=J1.15 RST`；`dcdc_enable=U1.EN pin1`；`rst_pulldown=R15 100K/1%`；`series=R16 0R/1%`；`module_reset=RF_C6_RST -> U2.EN pin8,TP4`；`pullup=R11 10K/1%`；`capacitor=C1 1uF/10V` |
| GPIO 与控制信号 | U2 未连接 GPIO | `unused_gpio=IO3,IO4,IO5,IO0,IO1,IO6,IO7,IO14,IO15`；`module_nc_pins=4,7,21,32,33,34,35` |
| 时钟 | 外部时钟 | `crystal_shown=false`；`oscillator_shown=false`；`external_clock_net_shown=false` |
| 内存与 Flash | 外部存储器 | `flash_shown=false`；`psram_shown=false`；`eeprom_shown=false`；`sd_card_shown=false` |
| 射频 | 无线射频实现 | `rf_pin_shown=false`；`matching_network_shown=false`；`antenna_shown=false`；`antenna_connector_shown=false` |
| 其他事实 | U2 无线模组具体型号 | `documented_module=ESP32-C6-MINI-1-N4`；`documented_soc=ESP32-C6FH4`；`schematic_reference=U2`；`schematic_part_number=null` |
| 其他事实 | 正文无线与存储规格 | `documented_flash=4MB`；`documented_wireless=2.4GHz Wi-Fi 6`；`documented_main_core=RISC-V 32-bit single-core 160MHz`；`documented_low_power_core=RISC-V 32-bit single-core 20MHz`；`schematic_confirms_specs=false` |
| 核心器件 | J1 连接器完整型号 | `schematic_label=HC-PBB40C-20DP-0.4`；`documented_model=HC-PBB40C-20DP-0.4V-02`；`pin_count=20`；`full_part_number_confirmed=false` |
| 其他事实 | Stamp-P4 适配与 SDIO 性能 | `documented_host=Stamp-P4`；`documented_interface=0.4mm 20P SDIO`；`documented_performance=high-speed`；`schematic_pin_count=20`；`bus_frequency=null`；`throughput=null` |
| 其他事实 | 工作温度范围 | `documented_operating_temperature=0 to 40°C`；`schematic_temperature_marking=false` |

## 待确认事项

- `other.documented-module-identity`：正文称核心模组为 ESP32-C6-MINI-1-N4，规格表称 SoC 为 ESP32-C6FH4；原理图 U2 只显示管脚名称与位号，没有打印模组或 SoC 完整料号。（证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 2B-3C，U2 无料号字段）
- `other.documented-wireless-memory-specs`：正文列出 4MB Flash、2.4GHz Wi-Fi 6、160MHz RISC-V 主核和 20MHz RISC-V 低功耗协处理器；原理图未标这些容量、协议、频率或内核信息。（证据：图 cade20681dc0 / 第 1 页 / 第 1 页 U2 与完整图均无容量、无线协议或处理器频率标注）
- `component.connector-full-model`：原理图 J1 标注 HC-PBB40C-20DP-0.4，正文规格表写 HC-PBB40C-20DP-0.4V-02；两者后缀不同，无法仅凭该页确认量产连接器完整料号。（证据：图 cade20681dc0 / 第 1 页 / 第 1 页网格 1A-1B，J1 下方型号 HC-PBB40C-20DP-0.4）
- `other.documented-host-compatibility`：正文称 J1 为适配 Stamp-P4 的 0.4mm 20P SDIO 接口并描述为高速通信；原理图确认 20 针连接器、0.4 型号标记和六线 SDIO2 连接，但未给出配对连接器、总线频率或吞吐率。（证据：图 cade20681dc0 / 第 1 页 / 第 1 页 J1 20P 连接器与 SDIO2_CMD/CLK/D0-D3，无主机料号或速率标注）
- `other.documented-operating-temperature`：正文规格表给出工作温度 0~40°C，原理图没有温度等级、器件选型后缀或热设计条件。（证据：图 cade20681dc0 / 第 1 页 / 第 1 页完整图无温度规格）
- `review.module-identity`：请依据 A172 量产 BOM、U2 丝印或贴片资料确认 U2 为 ESP32-C6-MINI-1-N4，并确认内部 SoC 为 ESP32-C6FH4。；原因：正文给出模组和 SoC 型号，但原理图 U2 没有打印完整料号。
- `review.wireless-memory-specs`：请依据确认后的 U2 具体料号、datasheet 和固件验证 4MB Flash、2.4GHz Wi-Fi 6 及双 RISC-V 内核频率。；原因：这些参数来自产品正文，原理图未标容量、协议或处理器频率。
- `review.connector-full-model`：请依据 A172 BOM 或采购料号确认 J1 的完整型号及 `-0.4` 与 `-0.4V-02` 标记关系。；原因：原理图和正文规格表的 J1 型号后缀不同。
- `review.host-compatibility`：请以 Stamp-P4 对应版本的连接器/BOM 和联合测试确认机械配对、信号兼容、SDIO 时钟上限与实际吞吐率。；原因：原理图确认连接器和网络，但未标配对连接器、主机版本或性能参数。
- `review.operating-temperature`：请依据 A172 量产器件温度等级和整机环境测试确认 0~40°C 工作温度范围。；原因：原理图没有器件温度等级和整机热条件。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `cade20681dc035a8b83ca65b7a0621ae850969a4e7498f681f51279d1b70b061` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1220/SCH_C6_Add-on_Stamp-P4_2026_03_16_15_10_59_page_01.png` |

---

源文档：`zh_CN/stamp/Stamp-AddOn_C6_For_P4.md`

源文档 SHA-256：`c45939343d4f53b3ba6496be783e5c8b31c1ff67bc2cfd11b2ef0905a3f8c469`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
