# M5Camera-F 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | M5Camera-F |
| SKU | U037 |
| 产品 ID | `m5camera-f-00c809bf2b2e` |
| 源文档 | `zh_CN/unit/m5camera_f.md` |

## 概述

M5Camera-F 产品页提供三张通用 m5camera_sch 图面，分别覆盖电源、ESP32-Wrover 外围和 USB-UART。图面中 VIN_USB/VBAT 经 TP4057 与 1N5819 汇入 VBUS，SY8089 生成 VCC_3V3，RT9182-G 再生成 VDD_2V5/VDD_1V8；U4 ESP32-Wrover 连接 24-pin FPC、GPIO14 红蓝 LED、SPM1423 数字麦克风以及标为 Not Installed Optional 的 MPU60X0/BME280；U8 CP2104 与 U9 USB_Micro 提供串口、自动下载和 EN 复位。三张图没有打印 M5Camera-F、U037、OV2640、镜头或内存容量，且 U9 标 USB_Micro 与正文 Type-C 描述不同，因此产品版本归属、OV2640/160°、内存、完整相机映射、HY2.0、USB 形态、固件和机械参数均保留为待确认。

## 检索关键词

`M5Camera-F`、`M5CameraF`、`U037`、`ESP32-Wrover`、`OV2640`、`fish-eye`、`160 degree`、`2MP`、`SY8089`、`RT9182-G`、`TP4057`、`CP2104`、`SPM1423HM4H-B`、`MPU60X0`、`MPU6050`、`BME280`、`FPC0.5-SMT-24P-B`、`USB_Micro`、`USB Type-C`、`VBUS`、`VBAT`、`VIN_USB`、`VCC_3V3`、`VDD_2V5`、`VDD_1V8`、`GPIO14`、`GPIO0`、`EN`、`DTR`、`RTS`、`TXD0`、`RXD0`、`DVP`、`SCCB`、`HY2.0-4P`、`4M Flash`、`4M PSRAM`、`520K RAM`、`WiFi AP`、`192.168.4.1`、`600 x 800`、`5-6 fps`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | ESP32-Wrover | 3.3V 无线主控模组，连接摄像头 FPC、USB-UART、LED、数字麦克风与可选传感器 | 图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页左上 U4 ESP32-Wrover pins1-39 |
| U1 | SY8089 | VBUS 到 VCC_3V3 的同步降压转换器 | 图 46c05cd332c8 / 第 1 页 / 资源 1 第 1 页上方 U1 SY8089、L1 与 VBUS/VCC_3V3 |
| U2 | RT9182-G | VCC_3V3 到 VDD_2V5/VDD_1V8 的双路 LDO | 图 46c05cd332c8 / 第 1 页 / 资源 1 第 1 页中左 U2 RT9182-G |
| U3 | TP4057 | VIN_USB 到 VBAT 的单节锂电池充电管理器 | 图 46c05cd332c8 / 第 1 页 / 资源 1 第 1 页左下 U3 TP4057、LED1/R3/R4 与 VBAT |
| J1 | FPC0.5-SMT-24P-B | 摄像头 GPIO、电源和地的 24-pin FPC 接口 | 图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页上中 J1 FPC0.5-SMT-24P-B pins1-24 |
| U5 | SPM1423HM4H-B | GPIO2 数据、GPIO4 时钟的 3.3V PDM 数字麦克风 | 图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页中右 U5 SPM1423HM4H-B |
| U6/U7 | MPU60X0 / BME280 | 图面标为 Not Installed Optional 的惯性与环境传感器位置 | 图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页下方 U6/U7 与红色 Not Installed Optional 标注 |
| U8 | CP2104 | USB_DN/USB_DP 到 ESP32 TXD0/RXD0 的 USB-UART 桥 | 图 e5ccaeec1a54 / 第 1 页 / 资源 3 第 1 页中上 U8 CP2104 |
| U9 | USB_Micro | VIN_USB 和 USB D-/D+ 的图面 USB 连接器 | 图 e5ccaeec1a54 / 第 1 页 / 资源 3 第 1 页下中 U9 USB_Micro |
| VT1/VT2 | NPN-S8050 | 将 CP2104 DTR/RTS 转换为 ESP32 EN/GPIO0 自动下载控制 | 图 e5ccaeec1a54 / 第 1 页 / 资源 3 第 1 页左上 VT1/VT2 NPN-S8050 与 DTR/RTS/EN/GPIO0 |

## 系统结构

### M5Camera-F 页面所提供的三张图面

三张资源分别绘制 VBUS/VBAT 电源树、U4 ESP32-Wrover 与摄像头/麦克风/可选传感器外围，以及 U8 CP2104、U9 USB_Micro、自动下载和 EN 复位电路。

- 参数与网络：`power_sheet=resource 1`；`controller_sheet=resource 2`；`usb_uart_sheet=resource 3`；`controller=U4 ESP32-Wrover`
- 证据：图 46c05cd332c8 / 第 1 页 / 资源 1 第 1 页完整电源图; 图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页完整 ESP32/FPC/外设图; 图 e5ccaeec1a54 / 第 1 页 / 资源 3 第 1 页完整 USB-UART/下载图

## 核心器件

### U4 ESP32-Wrover

U4 明确标为 ESP32-Wrover，由 VCC_3V3 供电，展开 GPIO0-39、TXD0/RXD0、EN 与模块地；SD0-SD3/CMD/CLK 外部引脚在本页标为未连接。

- 参数与网络：`reference=U4`；`part_number=ESP32-Wrover`；`supply=VCC_3V3`；`unused_external_flash_pins=SD0,SD1,SD2,SD3,CMD,CLK`
- 证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页左上 U4 ESP32-Wrover

## 电源

### VBUS 到 3.3V、2.5V 与 1.8V

U1 SY8089 以 VBUS 为输入，经 L1 2.2uH 生成 VCC_3V3；U2 RT9182-G 以 VCC_3V3 为输入，分别输出 VDD_2V5 与 VDD_1V8。

- 参数与网络：`input=VBUS`；`buck=U1 SY8089 + L1 2.2uH`；`main_rail=VCC_3V3`；`dual_ldo=U2 RT9182-G`；`camera_rails=VDD_2V5,VDD_1V8`
- 证据：图 46c05cd332c8 / 第 1 页 / 资源 1 第 1 页 U1 SY8089 与 U2 RT9182-G

### SY8089 电源外围与图面额定标注

VBUS 侧 C4/C5 各为 22uF/6.3V，VCC_3V3 侧 C2/C3 各为 22uF/6.3V，C1 标 22pF/DNW；图区文字把 SY8089 描述为 5.5V、2A 同步降压器。

- 参数与网络：`input_caps=C4,C5 22uF/6.3V`；`output_caps=C2,C3 22uF/6.3V`；`optional_cap=C1 22pF/DNW`；`schematic_rating_text=5.5V,2A Synchronous Buck Regulator`
- 证据：图 46c05cd332c8 / 第 1 页 / 资源 1 第 1 页 5V -> 3.3V DCDC Buck 分区

### RT9182-G 双路 LDO

U2 RT9182-G 的 VIN、EN1、EN2 接 VCC_3V3，VOUT1=VDD_2V5、VOUT2=VDD_1V8；C8、C6、C7 均标 2.2uF/6.3V，图区文字标 Dual Low-Noise 200mA LDO Regulator。

- 参数与网络：`input=VCC_3V3`；`outputs=VDD_2V5,VDD_1V8`；`capacitors=C8,C6,C7 2.2uF/6.3V`；`schematic_rating_text=Dual Low-Noise,200mA LDO Regulator`
- 证据：图 46c05cd332c8 / 第 1 页 / 资源 1 第 1 页 3.3V -> 2V5 & 1V8 LDO 分区

### USB 充电与 VIN_USB/VBAT 汇流

U3 TP4057 以 VIN_USB 为输入并输出 VBAT，LED1/R3 连接 CHRG/STDBY 状态，R4 3K 接 PROG；D1/D2 两颗 1N5819 将 VIN_USB 与 VBAT 分别接入 VBUS。

- 参数与网络：`charger=U3 TP4057`；`usb_input=VIN_USB`；`battery_net=VBAT`；`program_resistor=R4 3K`；`oring_diodes=D1,D2 1N5819`；`system_bus=VBUS`
- 证据：图 46c05cd332c8 / 第 1 页 / 资源 1 第 1 页左下 U3/LED1/R3/R4/D1/D2

## 接口

### J1 24-pin 摄像头 FPC

J1 FPC0.5-SMT-24P-B 引出 GPIO34、GPIO35、GPIO5、GPIO32、GPIO39、GPIO21、GPIO18、GPIO36、GPIO27、GPIO19、GPIO26、GPIO22、GPIO15、GPIO23、GPIO25，以及 VCC_3V3、VCC_2V5 和 GND。

- 参数与网络：`connector=FPC0.5-SMT-24P-B`；`connector_pins=24`；`gpio_bundle=34,35,5,32,39,21,18,36,27,19,26,22,15,23,25`；`power=VCC_3V3,VCC_2V5,GND`
- 证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页上中 J1 pins1-24 网络标签

### GPIO14 红蓝指示灯

GPIO14 连接 LED2 BLUE 与 LED3 RED 的公共驱动节点，LED2 另一端接 GND，LED3 另一端接 VCC_3V3。

- 参数与网络：`gpio=14`；`blue_branch=GPIO14 -> LED2 BLUE -> GND`；`red_branch=VCC_3V3 -> LED3 RED -> GPIO14`
- 证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页右上 GPIO14、LED2 BLUE、LED3 RED

### CP2104 USB 转串口

U8 CP2104 的 TXD pin21 经 R10 470R 连接 RXD0，RXD pin20 连接 TXD0；USB_DN/USB_DP 接 U8 DM/DP，VIN_USB 接 VREGIN/VBUS。

- 参数与网络：`bridge=U8 CP2104`；`uart_tx=U8.TXD -> R10 470R -> RXD0`；`uart_rx=U8.RXD -> TXD0`；`usb_data=USB_DN/USB_DP`；`usb_supply=VIN_USB`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 资源 3 第 1 页中上 U8 CP2104、R10 与 TXD0/RXD0

## 时钟

### 外部时钟源

三张资源未显示 ESP32-Wrover 外部晶振、振荡器或时钟输入网络，模组内部时钟实现未在图面展开。

- 参数与网络：`external_crystal_shown=false`；`external_oscillator_shown=false`；`module_internal_clock_expanded=false`
- 证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页 U4 ESP32-Wrover 外围无时钟器件

## 复位

### ESP32 EN 手动复位

S1 SMT_SW_TS_015 将 EN 拉到 GND；R18 10K 把 EN 上拉到 VCC_3V3，C1 2.2uF/6.3V 对地，D5 并联在 EN RC 网络。

- 参数与网络：`switch=S1 SMT_SW_TS_015`；`net=EN`；`pullup=R18 10K`；`capacitor=C1 2.2uF/6.3V`；`diode=D5`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 资源 3 第 1 页左下 EN、S1、R18、C1、D5

## 保护电路

### USB 数据与电源保护

U9 的 D-/D+ 经 R16/R17 各 22R 连接 USB_DN/USB_DP，并分别配置 D3/D4 RLSD52A031V 对地保护；VIN_USB 另配置 D6 RLSD52A031V 对地。

- 参数与网络：`dm_series=R16 22R`；`dp_series=R17 22R`；`dm_esd=D3 RLSD52A031V`；`dp_esd=D4 RLSD52A031V`；`vbus_esd=D6 RLSD52A031V`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 资源 3 第 1 页下中 U9/R16/R17/D3/D4/D6

## 内存与 Flash

### 外部存储器

三张资源未展示 ESP32-Wrover 之外的独立 Flash、PSRAM、EEPROM、RAM 或存储卡器件；U4 的 SD0-SD3/CMD/CLK 外部引脚标未连接。

- 参数与网络：`external_flash_shown=false`；`external_psram_shown=false`；`external_eeprom_shown=false`；`memory_card_shown=false`
- 证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页 U4 与完整外围，无独立存储器

## 音频

### SPM1423 数字麦克风

U5 SPM1423HM4H-B 由 VCC_3V3 供电，DAT pin5 连接 GPIO2，CLK pin4 连接 GPIO4，SEL pin2 与 GND pins1/3 接地，C13 2.2uF/6.3V 对地去耦。

- 参数与网络：`microphone=U5 SPM1423HM4H-B`；`data=GPIO2`；`clock=GPIO4`；`select=GND`；`supply=VCC_3V3`；`decoupling=C13 2.2uF/6.3V`
- 证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页中右 U5 SPM1423HM4H-B

## 传感器

### 可选未装 MPU60X0 与 BME280

U6 MPU60X0 与 U7 BME280 电路被红色箭头标为 Not Installed Optional；两者使用 VCC_3V3，并连接 GPIO23/GPIO22 总线网络。

- 参数与网络：`unpopulated=U6 MPU60X0,U7 BME280`；`annotation=Not Installed Optional`；`bus_gpio=GPIO23,GPIO22`；`supply=VCC_3V3`
- 证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页下方 U6/U7 与 Not Installed Optional

## 调试与烧录

### DTR/RTS 自动下载控制

CP2104 DTR/RTS 通过 R9/R12 各 10K 和 VT1/VT2 两颗 NPN-S8050 交叉控制 ESP32 EN 与 GPIO0。

- 参数与网络：`control_signals=DTR,RTS`；`base_resistors=R9,R12 10K`；`transistors=VT1,VT2 NPN-S8050`；`esp32_targets=EN,GPIO0`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 资源 3 第 1 页左上 DTR/RTS、R9/R12 与 VT1/VT2

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | M5Camera-F 页面所提供的三张图面 | `power_sheet=resource 1`；`controller_sheet=resource 2`；`usb_uart_sheet=resource 3`；`controller=U4 ESP32-Wrover` |
| 核心器件 | U4 ESP32-Wrover | `reference=U4`；`part_number=ESP32-Wrover`；`supply=VCC_3V3`；`unused_external_flash_pins=SD0,SD1,SD2,SD3,CMD,CLK` |
| 电源 | VBUS 到 3.3V、2.5V 与 1.8V | `input=VBUS`；`buck=U1 SY8089 + L1 2.2uH`；`main_rail=VCC_3V3`；`dual_ldo=U2 RT9182-G`；`camera_rails=VDD_2V5,VDD_1V8` |
| 电源 | SY8089 电源外围与图面额定标注 | `input_caps=C4,C5 22uF/6.3V`；`output_caps=C2,C3 22uF/6.3V`；`optional_cap=C1 22pF/DNW`；`schematic_rating_text=5.5V,2A Synchronous Buck Regulator` |
| 电源 | RT9182-G 双路 LDO | `input=VCC_3V3`；`outputs=VDD_2V5,VDD_1V8`；`capacitors=C8,C6,C7 2.2uF/6.3V`；`schematic_rating_text=Dual Low-Noise,200mA LDO Regulator` |
| 电源 | USB 充电与 VIN_USB/VBAT 汇流 | `charger=U3 TP4057`；`usb_input=VIN_USB`；`battery_net=VBAT`；`program_resistor=R4 3K`；`oring_diodes=D1,D2 1N5819`；`system_bus=VBUS` |
| 接口 | J1 24-pin 摄像头 FPC | `connector=FPC0.5-SMT-24P-B`；`connector_pins=24`；`gpio_bundle=34,35,5,32,39,21,18,36,27,19,26,22,15,23,25`；`power=VCC_3V3,VCC_2V5,GND` |
| 音频 | SPM1423 数字麦克风 | `microphone=U5 SPM1423HM4H-B`；`data=GPIO2`；`clock=GPIO4`；`select=GND`；`supply=VCC_3V3`；`decoupling=C13 2.2uF/6.3V` |
| 传感器 | 可选未装 MPU60X0 与 BME280 | `unpopulated=U6 MPU60X0,U7 BME280`；`annotation=Not Installed Optional`；`bus_gpio=GPIO23,GPIO22`；`supply=VCC_3V3` |
| 接口 | GPIO14 红蓝指示灯 | `gpio=14`；`blue_branch=GPIO14 -> LED2 BLUE -> GND`；`red_branch=VCC_3V3 -> LED3 RED -> GPIO14` |
| 接口 | CP2104 USB 转串口 | `bridge=U8 CP2104`；`uart_tx=U8.TXD -> R10 470R -> RXD0`；`uart_rx=U8.RXD -> TXD0`；`usb_data=USB_DN/USB_DP`；`usb_supply=VIN_USB` |
| 保护电路 | USB 数据与电源保护 | `dm_series=R16 22R`；`dp_series=R17 22R`；`dm_esd=D3 RLSD52A031V`；`dp_esd=D4 RLSD52A031V`；`vbus_esd=D6 RLSD52A031V` |
| 调试与烧录 | DTR/RTS 自动下载控制 | `control_signals=DTR,RTS`；`base_resistors=R9,R12 10K`；`transistors=VT1,VT2 NPN-S8050`；`esp32_targets=EN,GPIO0` |
| 复位 | ESP32 EN 手动复位 | `switch=S1 SMT_SW_TS_015`；`net=EN`；`pullup=R18 10K`；`capacitor=C1 2.2uF/6.3V`；`diode=D5` |
| 时钟 | 外部时钟源 | `external_crystal_shown=false`；`external_oscillator_shown=false`；`module_internal_clock_expanded=false` |
| 内存与 Flash | 外部存储器 | `external_flash_shown=false`；`external_psram_shown=false`；`external_eeprom_shown=false`；`memory_card_shown=false` |
| 其他事实 | 三张共享图面与 U037 的版本归属 | `source_product=M5Camera-F`；`sku=U037`；`asset_names=m5camera_sch_01,m5camera_sch_02,m5camera_sch_03`；`product_marking_on_sheets=false`；`revision_marking_on_sheets=false` |
| 内存与 Flash | Flash、RAM 与 PSRAM 容量 | `description_flash=4M`；`description_internal_ram=520K`；`description_psram=4M`；`table_flash=4M`；`table_ram=4MB`；`schematic_capacity_text=false` |
| 传感器 | OV2640、2MP 与 160° 鱼眼成像 | `documented_sensor=OV2640`；`documented_megapixels=2`；`documented_optical_format=1/4 inch`；`documented_fov_deg=160`；`documented_formats=YUV422/420,YCbCr422,RGB565/555,8-/10-bit Raw RGB` |
| 接口 | OV2640 DVP/SCCB 映射与 PWDN | `documented_control=SIOC=G23,SIOD=G22,XCLK=G27,VSYNC=G25,HREF=G26,PCLK=G21,RESET=G15`；`documented_data=D2=G32,D3=G35,D4=G34,D5=G5,D6=G39,D7=G18,D8=G36,D9=G19`；`documented_pwdn=OV2640 pin8 via 12K to GND` |
| 接口 | HY2.0-4P G13/G4 接口 | `documented_scl=GPIO13`；`documented_sda=GPIO4`；`documented_power=5V,GND`；`documented_use=wired camera image`；`connector_shown=false` |
| 接口 | USB Type-C 与图面 USB_Micro 差异 | `documented_cable=USB Type-C`；`schematic_connector=U9 USB_Micro`；`cc_pulldowns=R7,R11 5.1K to GND`；`type_c_connector_shown=false` |
| 传感器 | 可选 BME280/MPU6050 地址 | `documented_bme280_address=0x76`；`documented_mpu6050_address=0x68`；`schematic_devices=U6 MPU60X0,U7 BME280`；`population=Not Installed Optional`；`address_text_shown=false` |
| 系统结构 | Wi-Fi AP 摄像头预装固件 | `documented_ssid_prefix=m5stack-`；`documented_ip=192.168.4.1`；`documented_resolution=600x800`；`documented_fps=5-6`；`schematic_confirms_firmware=false` |
| 其他事实 | M5Camera-F 尺寸与重量 | `documented_product_size=24 x 48 x 19mm`；`documented_product_weight=17g`；`documented_package_size=75 x 45 x 30mm`；`documented_gross_weight=41g` |

## 待确认事项

- `other.schematic-version-attribution`：源文档把三张 m5camera_sch_01/02/03 图用于 M5Camera-F，但图面标题栏没有产品名、SKU、版本号或 U037 标记，且相同资源也可能被系列其他页面引用；无法仅凭图面确认其与 U037 量产版本完全一致。（证据：图 46c05cd332c8 / 第 1 页 / 资源 1 第 1 页标题栏无产品名/SKU/版本; 图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页标题栏无产品名/SKU/版本; 图 e5ccaeec1a54 / 第 1 页 / 资源 3 第 1 页标题栏无产品名/SKU/版本）
- `memory.documented-capacities`：正文描述称 4M Flash、520K RAM、4M PSRAM，规格表则列 Flash=4M、RAM=4MB；原理图只标 ESP32-Wrover，没有模组子型号、存储颗粒或容量文字。（证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页 U4 仅标 ESP32-Wrover，无容量信息）
- `sensor.documented-ov2640-imaging`：正文称 M5Camera-F 配套 OV2640、2MP、1/4 inch、160° 鱼眼广角镜头，并列 YUV422/420、YCbCr422、RGB565/555 和 8-/10-bit Raw RGB 输出；三张图只有 J1 摄像头 FPC，没有 OV2640 器件、镜头或成像参数。（证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页仅 J1 摄像头 FPC，无 OV2640/镜头图符）
- `interface.documented-camera-map-pwdn`：正文把 SIOC/SIOD/XCLK/VSYNC/HREF/PCLK 映射到 G23/G22/G27/G25/G26/G21，把 D2-D9 映射到 G32/G35/G34/G5/G39/G18/G36/G19，并称 RESET=G15、PWDN pin8 由 12K 下拉；图面只在 J1 标 GPIO 与电源，没有 OV2640 信号语义或 12K PWDN 电阻。（证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页 J1 pins1-24 仅标 GPIO/电源，无 OV2640 语义）
- `interface.documented-hy2-port`：正文称 HY2.0-4P 引出 SCL=G13、SDA=G4、5V 与 GND，并可有线获取摄像头图片；当前三张图没有 HY2.0-4P 连接器或有线图像协议路径。（证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页无 HY2.0-4P 连接器）
- `interface.documented-usb-connector-type`：正文包装内容称附带 USB Type-C 连接线并描述 USB 端口调试，图面连接器 U9 明确标为 USB_Micro；另有 USB_CC1/USB_CC2 的 5.1K 下拉电阻支路，但未画出对应 Type-C 连接器。（证据：图 e5ccaeec1a54 / 第 1 页 / 资源 3 第 1 页 U9 USB_Micro 与右上 USB_CC1/USB_CC2、R7/R11）
- `sensor.documented-optional-addresses`：正文把保留 BME280 和 MPU6050 的 I2C 地址分别写为 0x76 与 0x68；图面将 U6/U7 标为 Not Installed Optional，并只显示 GPIO23/GPIO22、地址选择引脚和电源连接，没有打印地址数值。（证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页 U6/U7 与 Not Installed Optional，无地址文字）
- `system.documented-wifi-camera-firmware`：正文称预装 ESP-IDF Wi-Fi 相机固件，创建 m5stack- 前缀 AP，在 192.168.4.1 提供默认 600x800、约 5-6fps 视频；原理图不包含固件镜像、SSID、IP、图像尺寸或帧率配置。（证据：图 794cbb7a3c54 / 第 1 页 / 资源 2 第 1 页 ESP32-Wrover 硬件图无固件或网络配置）
- `other.documented-mechanical`：正文列出产品尺寸 24 x 48 x 19mm、产品重量 17g、包装尺寸 75 x 45 x 30mm 和毛重 41g；三张电气图没有板框、镜头高度、机械公差或质量信息。（证据：图 46c05cd332c8 / 第 1 页 / 资源 1 第 1 页电气图无机械尺寸或重量）
- `review.schematic-version-attribution`：请依据 U037 正式原理图、PCB 版本或 BOM 确认这三张共享 m5camera_sch 图与 M5Camera-F 量产硬件的对应版本。；原因：图面没有 M5Camera-F、U037 或版本标记，不能用系列共享图名替代版本确认。
- `review.memory-capacities`：请依据 U037 BOM、ESP32-Wrover 子型号和固件构建配置确认 Flash、内部 RAM、PSRAM 容量，并解释规格表 RAM=4MB 与描述 520K RAM+4M PSRAM 的关系。；原因：源文档字段语义存在冲突，图面没有模组子型号或容量。
- `review.ov2640-imaging`：请用 U037 摄像头 BOM、模组丝印和镜头规格确认 OV2640、2MP、1/4 inch、160° 鱼眼视角及支持的输出格式。；原因：当前图面只有通用 FPC，没有传感器与镜头器件。
- `review.camera-map-pwdn`：请依据 U037 正式摄像头页或 PCB 网表确认 OV2640 全部 DVP/SCCB/RESET/PWDN 逐针映射和 PWDN 12K 下拉。；原因：图面 J1 只标 GPIO，未写 OV2640 语义或 12K PWDN 网络。
- `review.hy2-port`：请确认 U037 是否实际装配 HY2.0-4P，并提供 G13/G4 有线图像协议、方向与带宽。；原因：当前三张原理图没有 HY2.0-4P 连接器或协议路径。
- `review.usb-connector-type`：请依据 U037 PCB/BOM 和产品照片确认量产 USB 连接器是 Type-C 还是 Micro-USB，并解释图面的 CC 下拉支路。；原因：正文与 U9 器件标注不一致，图面没有 Type-C 连接器。
- `review.optional-sensor-addresses`：请依据 U037 装配状态、U6/U7 具体料号和固件确认 MPU6050/BME280 是否装配及其 0x68/0x76 地址。；原因：图面把两个位置标为 Not Installed Optional，且未打印地址数值。
- `review.wifi-camera-firmware`：请确认 U037 量产预装固件版本、SSID、IP、默认图像尺寸和实测帧率。；原因：这些行为由固件镜像、摄像头配置和运行环境决定。
- `review.mechanical`：请用 U037 正式结构图、量产配置和称重记录复核 24 x 48 x 19mm、17g 及包装参数。；原因：电气图不包含板框、镜头机械尺寸或质量信息。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `46c05cd332c8c7e51b5650844de2a7bceb43307c6e40f703f728119ac8562180` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_01.webp` |
| 2 | 1 | `794cbb7a3c5418d5d9ff7d5d33747368cd8abb6d109ea2d2c1f15f8c4992c8da` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_02.webp` |
| 3 | 1 | `e5ccaeec1a54e3359ebda4eef57a310709c03edeca5872b60e1ed6128bc12b6e` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_03.webp` |

---

源文档：`zh_CN/unit/m5camera_f.md`

源文档 SHA-256：`4b9f44e95cc0df33528e73b04cd2239d64bac67ec993271251f71ed8a4beb92f`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
