# Atomic Display Base 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Atomic Display Base |
| SKU | A115 |
| 产品 ID | `atomic-display-base-d9f0339de757` |
| 源文档 | `zh_CN/atom/Atomic Display Base.md` |

## 概述

当前唯一的本地原理图页显示 ESP32-V3-02 控制器、板载与预留外部天线、Atom 4/5 Pin、Grove 接口、用户按键和手动复位。该页未显示 Atomic Display Base 产品正文所述 GW1NR-9C FPGA、LT8618SX、RGB 视频总线、电源转换或显示输出连接器，因此只能记录页面中可见的控制器事实，无法确认产品核心显示桥接子系统。

## 检索关键词

`Atomic Display Base`、`A115`、`ESP32-V3-02`、`PROANT_440`、`IPEX`、`ANT_LNA`、`VCC_3V3`、`BUTTON_G39`、`ESP32_EN`、`GPIO0`、`GROVE_G32`、`GROVE_G26`、`CONN_GP21`、`CONN_GP25`、`CONN_GP22`、`CONN_GP19`、`CONN_GP5`、`CONN_GP33`、`U0RXD`、`U0TXD`、`GW1NR-9C`、`LT8618SX`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-V3-02 | 页面中的 ESP32 控制器，连接 UART、按键、天线与扩展接口 | 图 f1897d180c6b / 第 1 页 / 左上 U1 ESP32-V3-02：LNA_IN/EN、GPIO、U0RXD/U0TXD、VCC_3V3 与 GND |
| ANT1 | PROANT_440 | ESP32 板载天线 | 图 f1897d180c6b / 第 1 页 / 上部中央 ANT1 PROANT_440，连接 ANT_LNA 匹配网络 |
| J5 | IPEX | 预留外部天线连接器，信号路径中的 C25 标为 NC | 图 f1897d180c6b / 第 1 页 / 上部 J5 IPEX：外壳 pins 2/3 接 GND，pin 1 经 C25 NC 到 ANT_LNA |
| J2 | 5P-2.54 | Atom 5 Pin 的 3.3V 与 GPIO22/19/5/33 接口 | 图 f1897d180c6b / 第 1 页 / 右上 J2 5P-2.54，pins 1~5 为 VCC_3V3/CONN_GP22/CONN_GP19/CONN_GP5/CONN_GP33 |
| J1 | 4PIN-2.54 | Atom 4 Pin 的 GPIO21/GPIO25/5V/GND 接口 | 图 f1897d180c6b / 第 1 页 / 右侧 J1 4PIN-2.54，pins 1~4 为 CONN_GP21/CONN_GP25/VUSB_5V/GND |
| J3 | PH2.0_4P_SMT | Grove GPIO32/GPIO26 与 5V/GND 接口 | 图 f1897d180c6b / 第 1 页 / 右侧 J3 PH2.0_4P_SMT，pins 1~4 为 GROVE_G32/GROVE_G26/VUSB_5V/GND |
| S2 | SMT_SW_PTS_820 | GPIO39 用户按键，按下接地 | 图 f1897d180c6b / 第 1 页 / 左下 BUTTON_G39-R1 5.1KΩ-S2 SMT_SW_PTS_820-GND |
| S1 | SMT_SW_TS_015 | ESP32_EN 复位按键，按下接地 | 图 f1897d180c6b / 第 1 页 / 下部 ESP32_EN-R2 5.1KΩ-C14 470nF-S1 SMT_SW_TS_015-GND，C13 NC |
| C25/C26/L1/C1/C2 | Antenna matching network | 板载天线与 IPEX 之间的可配置射频匹配网络 | 图 f1897d180c6b / 第 1 页 / 上部 ANT_LNA-C25 NC-C26 0R-L1 TBD/NC-C1 TBD/0R-C2 TBD/NC-ANT1 |

## 系统结构

### Atomic Display Base 当前本地原理图范围

唯一资源页包含 ESP32-V3-02、天线、Atom/Grove 接口、用户按键、手动复位与 VCC_3V3 去耦，没有显示 FPGA 或视频输出电路。

- 参数与网络：`local_assets=1`；`page_1=ESP32-V3-02,antenna,Atom connectors,Grove,button,reset,3V3 decoupling`
- 证据：图 f1897d180c6b / 第 1 页 / source_001 全页：U1、ANT1/J5、J1/J2/J3、S1/S2 与 C3~C12

## 电源

### ESP32 VCC_3V3 电源域

VCC_3V3 连接 U1 的 VDDA pins 1/43/46、VDDA3P3 pins 3/4、VDD3P3_CPU pin 37 与 VDD3P3_RTC pin 19；C3/C4 各 4.7uF，C5~C12 各 470nF 接在 VCC_3V3 与 GND 之间。

- 参数与网络：`analog_supply=U1 pins 1,43,46`；`analog_3v3=U1 pins 3,4`；`cpu_supply=U1 pin 37`；`rtc_supply=U1 pin 19`；`bulk_decoupling=C3/C4 4.7uF/6.3V`；`local_decoupling=C5-C12 470nF/10V`
- 证据：图 f1897d180c6b / 第 1 页 / 左侧 U1 VCC_3V3 电源引脚与中下部 C3~C12 去耦阵列

## 接口

### J2 Atom 5 Pin

J2 pins 1~5 依次连接 VCC_3V3、CONN_GP22、CONN_GP19、CONN_GP5、CONN_GP33；R6 标为 NC，预留在 CONN_GP23 与 CONN_GP5 之间。

- 参数与网络：`pin_1=VCC_3V3`；`pin_2=CONN_GP22`；`pin_3=CONN_GP19`；`pin_4=CONN_GP5`；`pin_5=CONN_GP33`；`optional_link=R6 NC between CONN_GP23 and CONN_GP5`
- 证据：图 f1897d180c6b / 第 1 页 / 右上 J2 5P-2.54 与 R6 NC、CONN_GP23/GP5

### J1 Atom 4 Pin

J1 pins 1~4 依次连接 CONN_GP21、CONN_GP25、VUSB_5V 与 GND。

- 参数与网络：`pin_1=CONN_GP21`；`pin_2=CONN_GP25`；`pin_3=VUSB_5V`；`pin_4=GND`
- 证据：图 f1897d180c6b / 第 1 页 / 右侧 J1 4PIN-2.54 pins 1~4 与左侧网络

### J3 Grove 接口

J3 pins 1~4 依次连接 GROVE_G32、GROVE_G26、VUSB_5V 与 GND，对应 U1 GPIO32、GPIO26、5V 和地。

- 参数与网络：`pin_1=GROVE_G32 U1 IO32`；`pin_2=GROVE_G26 U1 IO26`；`pin_3=VUSB_5V`；`pin_4=GND`
- 证据：图 f1897d180c6b / 第 1 页 / 右侧 J3 PH2.0_4P_SMT 与左上 U1 IO32/IO26 的 GROVE_G32/GROVE_G26 网络

## GPIO 与控制信号

### U1 ESP32-V3-02 已连接 GPIO

U1 的 IO39 接 BUTTON_G39，IO32/IO26 接 GROVE_G32/GROVE_G26，IO33/IO25/IO5/IO19/IO22/IO21 接 CONN_GP33/25/5/19/22/21，IO27 接 SK_DIN，IO0 接 GPIO0，U0RXD/U0TXD 接同名 UART 网络。

- 参数与网络：`GPIO39=BUTTON_G39`；`GPIO32=GROVE_G32`；`GPIO26=GROVE_G26`；`GPIO33=CONN_GP33`；`GPIO25=CONN_GP25`；`GPIO5=CONN_GP5`；`GPIO19=CONN_GP19`；`GPIO22=CONN_GP22`；`GPIO21=CONN_GP21`；`GPIO27=SK_DIN`；`GPIO0=GPIO0`；`UART=U0RXD,U0TXD`
- 证据：图 f1897d180c6b / 第 1 页 / 左上 U1 pins 8/12~16/23/34/38~42 的网络标签

### BUTTON_G39

U1 IO39 连接 BUTTON_G39，R1 5.1KΩ 将该网络上拉到 VCC_3V3，S2 SMT_SW_PTS_820 按键将该网络接到 GND。

- 参数与网络：`mcu_pin=U1 IO39`；`network=BUTTON_G39`；`pullup=R1 5.1KΩ to VCC_3V3`；`switch=S2 SMT_SW_PTS_820 to GND`
- 证据：图 f1897d180c6b / 第 1 页 / U1 pin 8 SENSOR_VN/IO39 与左下 BUTTON_G39-R1-S2-GND

## 复位

### ESP32_EN 手动复位

U1 EN pin 9 连接 ESP32_EN，R2 5.1KΩ 上拉到 VCC_3V3，C14 470nF 接 GND，S1 SMT_SW_TS_015 按下时接 GND；跨按键的 C13 标为 NC。

- 参数与网络：`mcu_pin=U1 pin 9 EN`；`network=ESP32_EN`；`pullup=R2 5.1KΩ`；`capacitor=C14 470nF/10V`；`switch=S1 SMT_SW_TS_015`；`optional_capacitor=C13 NC`
- 证据：图 f1897d180c6b / 第 1 页 / U1 pin 9 EN 与下部 ESP32_EN-R2-C14-S1-C13-GND

## 射频

### ESP32 板载天线路径

U1 LNA_IN pin 2 的 ANT_LNA 网络经 C26 0R、C1 TBD/0R 到 ANT1 PROANT_440；L1 与 C2 为到 GND 的 TBD/NC 匹配位。

- 参数与网络：`radio_pin=U1 pin 2 LNA_IN`；`net=ANT_LNA`；`series_1=C26 0R`；`series_2=C1 TBD/0R`；`shunt_1=L1 TBD/NC to GND`；`shunt_2=C2 TBD/NC to GND`；`antenna=ANT1 PROANT_440`
- 证据：图 f1897d180c6b / 第 1 页 / 上部 U1 LNA_IN-ANT_LNA-C26-L1-C1-C2-ANT1 PROANT_440

### J5 IPEX 预留路径

J5 IPEX 的信号 pin 1 通过 C25 连接 ANT_LNA，C25 标为 NC；J5 外壳 pins 2/3 接 GND。

- 参数与网络：`connector=J5 IPEX`；`signal_pin=pin 1`；`link=C25 NC to ANT_LNA`；`ground_pins=2,3`
- 证据：图 f1897d180c6b / 第 1 页 / 上部 J5 IPEX-C25 NC-ANT_LNA 与两侧 GND

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | Atomic Display Base 当前本地原理图范围 | `local_assets=1`；`page_1=ESP32-V3-02,antenna,Atom connectors,Grove,button,reset,3V3 decoupling` |
| GPIO 与控制信号 | U1 ESP32-V3-02 已连接 GPIO | `GPIO39=BUTTON_G39`；`GPIO32=GROVE_G32`；`GPIO26=GROVE_G26`；`GPIO33=CONN_GP33`；`GPIO25=CONN_GP25`；`GPIO5=CONN_GP5`；`GPIO19=CONN_GP19`；`GPIO22=CONN_GP22`；`GPIO21=CONN_GP21`；`GPIO27=SK_DIN`；`GPIO0=GPIO0`；`UART=U0RXD,U0TXD` |
| 电源 | ESP32 VCC_3V3 电源域 | `analog_supply=U1 pins 1,43,46`；`analog_3v3=U1 pins 3,4`；`cpu_supply=U1 pin 37`；`rtc_supply=U1 pin 19`；`bulk_decoupling=C3/C4 4.7uF/6.3V`；`local_decoupling=C5-C12 470nF/10V` |
| 接口 | J2 Atom 5 Pin | `pin_1=VCC_3V3`；`pin_2=CONN_GP22`；`pin_3=CONN_GP19`；`pin_4=CONN_GP5`；`pin_5=CONN_GP33`；`optional_link=R6 NC between CONN_GP23 and CONN_GP5` |
| 接口 | J1 Atom 4 Pin | `pin_1=CONN_GP21`；`pin_2=CONN_GP25`；`pin_3=VUSB_5V`；`pin_4=GND` |
| 接口 | J3 Grove 接口 | `pin_1=GROVE_G32 U1 IO32`；`pin_2=GROVE_G26 U1 IO26`；`pin_3=VUSB_5V`；`pin_4=GND` |
| GPIO 与控制信号 | BUTTON_G39 | `mcu_pin=U1 IO39`；`network=BUTTON_G39`；`pullup=R1 5.1KΩ to VCC_3V3`；`switch=S2 SMT_SW_PTS_820 to GND` |
| 复位 | ESP32_EN 手动复位 | `mcu_pin=U1 pin 9 EN`；`network=ESP32_EN`；`pullup=R2 5.1KΩ`；`capacitor=C14 470nF/10V`；`switch=S1 SMT_SW_TS_015`；`optional_capacitor=C13 NC` |
| 射频 | ESP32 板载天线路径 | `radio_pin=U1 pin 2 LNA_IN`；`net=ANT_LNA`；`series_1=C26 0R`；`series_2=C1 TBD/0R`；`shunt_1=L1 TBD/NC to GND`；`shunt_2=C2 TBD/NC to GND`；`antenna=ANT1 PROANT_440` |
| 射频 | J5 IPEX 预留路径 | `connector=J5 IPEX`；`signal_pin=pin 1`；`link=C25 NC to ANT_LNA`；`ground_pins=2,3` |
| 其他事实 | Atomic Display Base 原理图资源覆盖范围 | `local_assets=1`；`gw1nr_9c_visible=false`；`lt8618sx_visible=false`；`rgb_bus_visible=false`；`display_connector_visible=false`；`highest_level_component=ESP32-V3-02`；`resource_association_requires_review=true` |

## 待确认事项

- `other.resource-product-mismatch`：当前资源页未显示产品正文中的 GW1NR-9C、LT8618SX、RGB 视频总线、电源转换或显示输出连接器，且页面最高层器件为 ESP32-V3-02；无法由此资源确认 Atomic Display Base 的核心硬件。（证据：图 f1897d180c6b / 第 1 页 / source_001 全页：U1 为 ESP32-V3-02，外围为天线、Atom/Grove 接口、按键和复位；未见 GW1NR-9C、LT8618SX、RGB 或显示输出连接器）
- `review.atomic-display-base-resource`：请核对 Atomic Display Base 的原理图图片 URL，或补充 Sch_AtomDisplay.pdf 中包含 GW1NR-9C、LT8618SX、RGB 总线、电源和显示输出连接器的页面。；原因：当前唯一图片看起来属于 ESP32 Atom 控制器页面，不能支持产品核心显示桥接、电源与输出接口描述；旧发布文档中的相关内容因此不能继续作为已确认事实。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `f1897d180c6bb2fe8600104f62c7814079568a7c58ac70d75712aacb97780eb9` | `https://static-cdn.m5stack.com/resource/docs/products/atom/Atomic Display Base/img-3f5ac8bb-5276-4d1d-9edb-2921f8aab2f2.jpg` |

---

源文档：`zh_CN/atom/Atomic Display Base.md`

源文档 SHA-256：`c5449fcb431532e38512fc4208912ab60fadf2443401ff1c09f59146360f1a41`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
