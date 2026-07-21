# M5Camera-F New 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | M5Camera-F New |
| SKU | U037 |
| 产品 ID | `m5camera-f-new-1006d5674b34` |
| 源文档 | `zh_CN/unit/m5camera_f_new.md` |

## 概述

M5Camera-F New 的三张原理图页面覆盖电源、ESP32-Wrover 与摄像头 FPC 外围，以及 USB 转串口和自动下载电路。VIN_USB/VBAT 经肖特基二极管汇入 VBUS，SY8089 生成 VCC_3V3，RT9182-G 再生成 VDD_2V5/VDD_1V8，TP4057 管理 VBAT 充电。ESP32-Wrover 连接 24-pin Camera FPC、GPIO14 红蓝 LED、SPM1423 数字麦克风电路和标注可选未装的 MPU60X0/BME280 电路，CP2104 则连接 USB 数据线与 TXD0/RXD0。图面未给出 OV2640、存储容量、HY2.0 和机械信息，而且 USB_Micro 图符、USB_CC1/USB_CC2 电阻与源文档 Type-C 线材之间仍需核对当前硬件版本。

## 检索关键词

`M5Camera-F New`、`M5CameraF`、`U037`、`ESP32-Wrover`、`OV2640`、`SY8089`、`RT9182-G`、`TP4057`、`CP2104`、`SPM1423HM4H-B`、`MPU60X0`、`BME280`、`FPC0.5-SMT-24P-B`、`USB_Micro`、`USB Type-C`、`VBUS`、`VIN_USB`、`VBAT`、`VCC_3V3`、`VDD_2V5`、`VDD_1V8`、`GPIO14`、`GPIO0`、`EN`、`DTR`、`RTS`、`TXD0`、`RXD0`、`DVP`、`SCCB`、`HY2.0-4P`、`WiFi AP`、`192.168.4.1`、`150 degree`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | ESP32-Wrover | ESP32 无线主控模组，连接 Camera FPC、USB UART、LED、数字麦克风和可选传感器电路 | 图 794cbb7a3c54 / 第 1 页 / 上左 U4 ESP32-Wrover pins1-39 |
| U1 | SY8089 | VBUS 到 VCC_3V3 的同步降压转换器 | 图 46c05cd332c8 / 第 1 页 / 上方 5V -> 3.3V DCDC Buck，U1 SY8089 |
| U2 | RT9182-G | VCC_3V3 到 VDD_2V5 与 VDD_1V8 的双路 LDO | 图 46c05cd332c8 / 第 1 页 / 中左 3.3V -> 2V5 & 1V8 LDO，U2 RT9182-G |
| U3 | TP4057 | VIN_USB 到 VBAT 的单节锂电池充电管理 | 图 46c05cd332c8 / 第 1 页 / 左下 U3 TP4057、LED1/R3/R4 与 VBAT |
| D1,D2 | 1N5819 | 将 VIN_USB 与 VBAT 分别接入系统 VBUS 的肖特基二极管 | 图 46c05cd332c8 / 第 1 页 / 下中 D1/D2 1N5819 与 VIN_USB/VBUS/VBAT |
| J1 | FPC0.5-SMT-24P-B | 摄像头数据、时钟、控制和三路电源的 24-pin FPC 接口 | 图 794cbb7a3c54 / 第 1 页 / 上中 J1 FPC0.5-SMT-24P-B pins1-24 |
| U5 | SPM1423HM4H-B | VCC_3V3 供电、GPIO2 数据和 GPIO4 时钟的数字麦克风电路位置 | 图 794cbb7a3c54 / 第 1 页 / 中右 U5 SPM1423HM4H-B，DAT/CLK/SEL |
| U6 | MPU60X0 | 标注为 Not Installed Optional 的惯性传感器电路位置 | 图 794cbb7a3c54 / 第 1 页 / 下左 U6 MPU60X0 与红色 Not Installed Optional 标注 |
| U7 | BME280 | 标注为 Not Installed Optional 的环境传感器电路位置 | 图 794cbb7a3c54 / 第 1 页 / 下右 U7 BME280 与红色 Not Installed Optional 标注 |
| U8 | CP2104 | USB 差分信号到 ESP32 TXD0/RXD0 的 USB 转串口桥 | 图 e5ccaeec1a54 / 第 1 页 / 中上 U8 CP2104 pins1-25 |
| U9 | USB_Micro | 原理图标注的 USB 供电与数据连接器 | 图 e5ccaeec1a54 / 第 1 页 / 下中 U9 USB_Micro pins1-7 |
| VT1,VT2 | NPN-S8050 | 由 CP2104 DTR/RTS 控制 ESP32 EN/GPIO0 的自动下载晶体管 | 图 e5ccaeec1a54 / 第 1 页 / 左上 VT1/VT2 NPN-S8050、DTR/RTS、EN/GPIO0 |

## 系统结构

### ESP32-Wrover 主控模组

U4 明确标为 ESP32-Wrover，由 VCC_3V3 供电并引出 GPIO0-39、TXD0/RXD0 和 EN；模块的 SD0-SD3、CMD、CLK 外部引脚在本页标为未连接。

- 参数与网络：`module=ESP32-Wrover`；`supply=VCC_3V3`；`uart=TXD0,RXD0`
- 证据：图 794cbb7a3c54 / 第 1 页 / U4 ESP32-Wrover pins1-39

## 电源

### VBUS 到 VCC_3V3 同步降压

U1 SY8089 的 IN/EN 接 VBUS，LX 经 L1 2.2uH 输出 VCC_3V3；反馈网络为 R1 267K、R2 59K，输入 C4/C5 与输出 C2/C3 均标为 22uF/6.3V。

- 参数与网络：`converter=SY8089`；`input=VBUS`；`output=VCC_3V3`；`inductor=2.2uH`；`feedback=R1=267K,R2=59K`
- 证据：图 46c05cd332c8 / 第 1 页 / 上方 U1/L1/R1/R2/C2-C5

### VCC_3V3 到 VDD_2V5 与 VDD_1V8

U2 RT9182-G 的 VIN、EN1、EN2 接 VCC_3V3，VOUT1 输出 VDD_2V5，VOUT2 输出 VDD_1V8；C6/C7 为两路输出去耦，C8 为输入去耦。

- 参数与网络：`regulator=RT9182-G`；`input=VCC_3V3`；`output1=VDD_2V5`；`output2=VDD_1V8`
- 证据：图 46c05cd332c8 / 第 1 页 / 中左 U2 RT9182-G、C6/C7/C8

### VIN_USB 到 VBAT 充电

U3 TP4057 以 VIN_USB 为输入并在 BAT 引脚输出 VBAT；CHRG 通过 LED1 与 R3 3K 指示状态，PROG 通过 R4 3K 接地，VBAT 端使用 C10 2.2uF/6.3V。

- 参数与网络：`charger=TP4057`；`input=VIN_USB`；`battery_net=VBAT`；`program_resistor=3K`
- 证据：图 46c05cd332c8 / 第 1 页 / 左下 U3/LED1/R3/R4/C9/C10

### VIN_USB 与 VBAT 汇入 VBUS

D1 与 D2 均标为 1N5819，分别位于 VIN_USB 到 VBUS 和 VBAT 到 VBUS 的路径上，使 USB 输入与电池输入在 VBUS 节点汇合。

- 参数与网络：`usb_path=VIN_USB-D1-VBUS`；`battery_path=VBAT-D2-VBUS`；`diodes=1N5819`
- 证据：图 46c05cd332c8 / 第 1 页 / 下中 D1/D2 与 VIN_USB/VBUS/VBAT

## 接口

### J1 24-pin Camera FPC 引脚

J1 的已标网络为 pin22 GPIO34、pin21 GPIO35、pin20 GPIO5、pin19 GPIO32、pin18 GPIO39、pin17 GPIO21、pin16 GPIO18、pin15 GND、pin14 GPIO36、pin13 GPIO27、pin12 GPIO19、pin11 VCC_3V3、pin10 VCC_1V8、pin9 GPIO26、pin8 GPIO22、pin7 GPIO15、pin6 GPIO23、pin4 VCC_2V5、pin3 GPIO25、pin1 GND；pins24/23/5/2 标为未连接。

- 参数与网络：`connector=FPC0.5-SMT-24P-B`；`gpio_pins=22=G34,21=G35,20=G5,19=G32,18=G39,17=G21,16=G18,14=G36,13=G27,12=G19,9=G26,8=G22,7=G15,6=G23,3=G25`；`power_pins=11=VCC_3V3,10=VCC_1V8,4=VCC_2V5`；`ground_pins=15,1`；`nc_pins=24,23,5,2`
- 证据：图 794cbb7a3c54 / 第 1 页 / J1 FPC0.5-SMT-24P-B pins1-24 网络标签与未连接标记

### GPIO14 红蓝 LED

GPIO14 连接 LED2 BLUE 与 LED3 RED 的公共驱动节点，LED2 另一端接 GND，LED3 另一端接 VCC_3V3。

- 参数与网络：`gpio=14`；`blue_return=GND`；`red_return=VCC_3V3`
- 证据：图 794cbb7a3c54 / 第 1 页 / 右上 GPIO14、LED2 BLUE、LED3 RED

### CP2104 USB 转串口

U8 CP2104 的 DP/DM 分别接 USB_DP/USB_DN，TXD 经 R10 470ohm 接 RXD0，RXD 直接接 TXD0；REGIN/VBUS 接 VIN_USB，VIO/VDD 使用 VDD_3V45。

- 参数与网络：`bridge=CP2104`；`usb_data=USB_DP,USB_DN`；`uart_cross=TXD-R10-RXD0,RXD-TXD0`；`usb_supply=VIN_USB`；`logic_supply=VDD_3V45`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 中上 U8 CP2104、R10、USB_DP/USB_DN、TXD0/RXD0

## 总线

### 可选传感器 GPIO22/GPIO23 连接与模式绑带

U6 的 SCL/SCLK 接 GPIO23、SDA/SDI 接 GPIO22，FSYNC 与 AD0/SDO 接 GND；U7 的 SCK 接 GPIO23、SDI 接 GPIO22，CSB 接 VCC_3V3、SDO 接 GND。

- 参数与网络：`clock_net=GPIO23`；`data_net=GPIO22`；`mpu_straps=FSYNC=GND,AD0/SDO=GND`；`bme_straps=CSB=VCC_3V3,SDO=GND`
- 证据：图 794cbb7a3c54 / 第 1 页 / U6 MPU60X0 与 U7 BME280 GPIO22/GPIO23 网络及绑带

## 保护电路

### USB 数据串阻、ESD 与 CC 下拉

U9 的 D-/D+ 分别经 R16/R17 22ohm 接 USB_DN/USB_DP，并由 D3/D4 ESD 器件对地保护；独立的 USB_CC1 与 USB_CC2 网络分别经 R7/R11 5.1K 下拉到 GND。

- 参数与网络：`data_resistors=R16=22ohm,R17=22ohm`；`esd=D3,D4`；`cc_pulldowns=R7=5.1K,R11=5.1K`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 右上 R7/R11 USB_CC1/USB_CC2 与下中 R16/R17/D3/D4/U9

## 关键网络

### J1 GPIO26 下拉

J1 pin9 的 GPIO26 网络通过 R6 10K 下拉到 GND。

- 参数与网络：`connector_pin=9`；`net=GPIO26`；`pulldown=10K`
- 证据：图 794cbb7a3c54 / 第 1 页 / J1 pin9 GPIO26 与 R6 10K 到 GND

## 音频

### SPM1423 数字麦克风电路

U5 SPM1423HM4H-B 的 VDD 接 VCC_3V3，DAT 接 GPIO2，CLK 接 GPIO4，SEL 与两个 GND 引脚接地，C13 2.2uF/6.3V 跨接电源与地。

- 参数与网络：`microphone=SPM1423HM4H-B`；`supply=VCC_3V3`；`data_gpio=2`；`clock_gpio=4`；`select=GND`
- 证据：图 794cbb7a3c54 / 第 1 页 / 中右 U5 SPM1423HM4H-B 与 C13

## 传感器

### MPU60X0 与 BME280 可选未装电路

U6 MPU60X0 与 U7 BME280 所在区域被红色 Not Installed Optional 标注指向，表示这两组传感器电路为可选未装位置。

- 参数与网络：`devices=U6 MPU60X0,U7 BME280`；`schematic_note=Not Installed Optional`
- 证据：图 794cbb7a3c54 / 第 1 页 / 下方 U6/U7 与红色 Not Installed Optional 标注

## 调试与烧录

### DTR/RTS 自动下载与手动复位

CP2104 的 DTR/RTS 通过 R9/R12 10K 与 VT1/VT2 两颗 NPN-S8050 交叉控制 ESP32 EN/GPIO0；S1 将 EN 手动拉低，R18 10K 将 EN 上拉到 VCC_3V3，C1 2.2uF/6.3V 接地。

- 参数与网络：`control_signals=DTR,RTS`；`esp32_targets=EN,GPIO0`；`transistors=VT1,VT2 NPN-S8050`；`reset_button=S1`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 左上 VT1/VT2/R9/R12 与左下 S1/R18/C1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | ESP32-Wrover 主控模组 | `module=ESP32-Wrover`；`supply=VCC_3V3`；`uart=TXD0,RXD0` |
| 电源 | VBUS 到 VCC_3V3 同步降压 | `converter=SY8089`；`input=VBUS`；`output=VCC_3V3`；`inductor=2.2uH`；`feedback=R1=267K,R2=59K` |
| 电源 | VCC_3V3 到 VDD_2V5 与 VDD_1V8 | `regulator=RT9182-G`；`input=VCC_3V3`；`output1=VDD_2V5`；`output2=VDD_1V8` |
| 电源 | VIN_USB 到 VBAT 充电 | `charger=TP4057`；`input=VIN_USB`；`battery_net=VBAT`；`program_resistor=3K` |
| 电源 | VIN_USB 与 VBAT 汇入 VBUS | `usb_path=VIN_USB-D1-VBUS`；`battery_path=VBAT-D2-VBUS`；`diodes=1N5819` |
| 接口 | J1 24-pin Camera FPC 引脚 | `connector=FPC0.5-SMT-24P-B`；`gpio_pins=22=G34,21=G35,20=G5,19=G32,18=G39,17=G21,16=G18,14=G36,13=G27,12=G19,9=G26,8=G22,7=G15,6=G23,3=G25`；`power_pins=11=VCC_3V3,10=VCC_1V8,4=VCC_2V5`；`ground_pins=15,1`；`nc_pins=24,23,5,2` |
| 关键网络 | J1 GPIO26 下拉 | `connector_pin=9`；`net=GPIO26`；`pulldown=10K` |
| 音频 | SPM1423 数字麦克风电路 | `microphone=SPM1423HM4H-B`；`supply=VCC_3V3`；`data_gpio=2`；`clock_gpio=4`；`select=GND` |
| 传感器 | MPU60X0 与 BME280 可选未装电路 | `devices=U6 MPU60X0,U7 BME280`；`schematic_note=Not Installed Optional` |
| 总线 | 可选传感器 GPIO22/GPIO23 连接与模式绑带 | `clock_net=GPIO23`；`data_net=GPIO22`；`mpu_straps=FSYNC=GND,AD0/SDO=GND`；`bme_straps=CSB=VCC_3V3,SDO=GND` |
| 接口 | GPIO14 红蓝 LED | `gpio=14`；`blue_return=GND`；`red_return=VCC_3V3` |
| 接口 | CP2104 USB 转串口 | `bridge=CP2104`；`usb_data=USB_DP,USB_DN`；`uart_cross=TXD-R10-RXD0,RXD-TXD0`；`usb_supply=VIN_USB`；`logic_supply=VDD_3V45` |
| 调试与烧录 | DTR/RTS 自动下载与手动复位 | `control_signals=DTR,RTS`；`esp32_targets=EN,GPIO0`；`transistors=VT1,VT2 NPN-S8050`；`reset_button=S1` |
| 保护电路 | USB 数据串阻、ESD 与 CC 下拉 | `data_resistors=R16=22ohm,R17=22ohm`；`esd=D3,D4`；`cc_pulldowns=R7=5.1K,R11=5.1K` |
| 内存与 Flash | Flash、内部 RAM 与 PSRAM 容量 | `description_flash=4M`；`description_ram=520K`；`description_psram=4M`；`table_flash=4M`；`table_ram=4MB` |
| 传感器 | OV2640 与鱼眼成像参数 | `documented_sensor=OV2640`；`documented_megapixels=2`；`documented_optical_format=1/4 inch`；`documented_fov_deg=150`；`documented_formats=YUV422/420,YCbCr422,RGB565/555,8-/10-bit Raw RGB` |
| 接口 | Camera DVP/SCCB/RESET/PWDN 语义映射 | `documented_control=SIOC=IO23,SIOD=IO22,XCLK=IO27,VSYNC=IO25,HREF=IO26,PCLK=IO21,RESET=IO15`；`documented_data=D2=IO32,D3=IO35,D4=IO34,D5=IO5,D6=IO39,D7=IO18,D8=IO36,D9=IO19`；`documented_pwdn_pulldown=12K` |
| 接口 | HY2.0-4P 接口与有线图像链路 | `documented_scl=G4`；`documented_sda=G13`；`documented_power=5V,GND`；`documented_use=wired camera image` |
| 系统结构 | 预装 Wi-Fi AP 摄像头固件 | `documented_ssid_prefix=m5stack-`；`documented_ip=192.168.4.1`；`documented_resolution=600x800`；`documented_fps=5-6` |
| 系统结构 | 产品与包装机械参数 | `documented_product_size_mm=24x48x19`；`documented_product_weight_g=17`；`documented_gross_weight_g=41`；`documented_package_size_mm=75x45x30` |
| 接口 | USB_Micro 图符与 Type-C 版本线索 | `schematic_connector=USB_Micro`；`schematic_cc=USB_CC1/R7=5.1K,USB_CC2/R11=5.1K`；`documented_cable=USB Type-C 20cm` |

## 待确认事项

- `memory.documented-capacities`：源文档描述写为 4M Flash、520K RAM、4M PSRAM，而规格表写为 Flash 4M、RAM 4MB 且未单列 PSRAM；原理图仅标 ESP32-Wrover，没有模组子型号、存储颗粒或容量。（证据：图 794cbb7a3c54 / 第 1 页 / U4 仅标 ESP32-Wrover，无容量和子型号）
- `sensor.documented-ov2640-imaging`：源文档称采用 OV2640 2MP、1/4 inch、150-degree 鱼眼镜头，并列出 YUV/YCbCr、RGB565/555 与 Raw RGB 输出；三页原理图没有 OV2640 器件、镜头、像素阵列或输出格式标注。（证据：图 794cbb7a3c54 / 第 1 页 / 页面仅有 J1 Camera FPC，无 OV2640 或镜头图符）
- `interface.documented-camera-signal-map`：源文档将 SIOC/SIOD/XCLK/VSYNC/HREF/PCLK 映射到 IO23/IO22/IO27/IO25/IO26/IO21，将 D2-D9 映射到 IO32/IO35/IO34/IO5/IO39/IO18/IO36/IO19，并称 RESET 接 IO15、PWDN 由 12K 下拉；原理图能确认这些 GPIO 出现在 J1，但没有 DVP/SCCB 信号名或 12K PWDN 电阻。（证据：图 794cbb7a3c54 / 第 1 页 / J1 pins1-24 仅标 GPIO/电源，未标 Camera 信号语义或 PWDN）
- `interface.documented-hy2-port`：源文档称 HY2.0-4P 引出 SCL=G4、SDA=G13、5V 与 GND，并可用于有线获取摄像头图片；当前三页原理图没有 HY2.0-4P 连接器或对应有线图像协议路径。（证据：图 794cbb7a3c54 / 第 1 页 / 页面无 HY2.0-4P 连接器）
- `system.documented-wifi-camera-firmware`：源文档称预装 ESP-IDF Wi-Fi 相机程序，创建 m5stack- 前缀 AP，在 192.168.4.1 提供 600x800、约 5-6fps 视频；原理图不包含固件版本、SSID、IP、分辨率或帧率配置。（证据：图 794cbb7a3c54 / 第 1 页 / U4 ESP32-Wrover 硬件图无固件或网络配置）
- `system.documented-mechanical`：源文档规格表称产品尺寸 24x48x19mm、重量 17g、毛重 41g、包装尺寸 75x45x30mm；当前三页电气原理图没有板框、镜头高度、机械公差或质量信息。（证据：图 46c05cd332c8 / 第 1 页 / 电气原理图无板框与机械尺寸）
- `interface.usb-connector-version`：原理图把 U9 明确标为 USB_Micro，但同页另有 USB_CC1/USB_CC2 各经 5.1K 下拉，源文档包装内容又列出 USB Type-C 连接线；仅凭这些资料无法确认 M5Camera-F New 当前装配的连接器版本。（证据：图 e5ccaeec1a54 / 第 1 页 / U9 USB_Micro 与右上 USB_CC1/USB_CC2、R7/R11）
- `review.memory-capacities`：确认 ESP32-Wrover 子型号、Flash/内部 RAM/PSRAM 的实际容量及规格表 RAM 4MB 的含义；原因：源文档描述与规格表字段不一致，原理图没有容量或模组子型号。
- `review.ov2640-imaging`：确认当前配套摄像头是否为 OV2640 2MP 1/4 inch 150-degree 鱼眼镜头及其输出格式；原因：当前原理图只有 Camera FPC，没有传感器和镜头电路。
- `review.camera-signal-map`：确认 OV2640 的 DVP、SCCB、RESET、PWDN 在当前硬件版本的完整连接和 PWDN 下拉阻值；原因：J1 图面只有 GPIO 标签，没有 Camera 语义与 12K PWDN 器件。
- `review.hy2-port`：确认 HY2.0-4P 是否实际装配，以及 G4/G13 的有线图像协议和方向；原因：当前三页原理图没有 HY2.0-4P 连接器。
- `review.wifi-camera-firmware`：确认量产预装固件版本、SSID、IP、默认分辨率和实际帧率；原因：这些行为由软件镜像和运行环境决定，电气原理图不能确认。
- `review.mechanical`：确认 24x48x19mm 外形、17g 产品重量与当前量产配置；原因：当前电气原理图没有机械尺寸和质量信息。
- `review.usb-connector-version`：确认 M5Camera-F New 当前量产板使用 USB-Micro 还是 USB Type-C 连接器；原因：U9 图符、USB CC 下拉网络和源文档随附线材给出不同版本线索。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `46c05cd332c8c7e51b5650844de2a7bceb43307c6e40f703f728119ac8562180` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_01.webp` |
| 2 | 1 | `794cbb7a3c5418d5d9ff7d5d33747368cd8abb6d109ea2d2c1f15f8c4992c8da` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_02.webp` |
| 3 | 1 | `e5ccaeec1a54e3359ebda4eef57a310709c03edeca5872b60e1ed6128bc12b6e` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_03.webp` |

---

源文档：`zh_CN/unit/m5camera_f_new.md`

源文档 SHA-256：`091edc0299117d9badefc11289a092a522e405bddb0dce8fe7a9dadb252ebdb7`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
