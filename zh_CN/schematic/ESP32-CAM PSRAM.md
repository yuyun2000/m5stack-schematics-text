# ESP32-CAM PSRAM 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | ESP32-CAM PSRAM |
| SKU | U017-PCBA |
| 产品 ID | `esp32-cam-psram-4bf1cbd7fd68` |
| 源文档 | `zh_CN/unit/ESP32CAM-PSRAM.md` |

## 概述

三张原理图页面覆盖 ESP32-CAM PSRAM 的电源、ESP32-Wrover 外围和 USB 串口。5V VBUS 经 SY8089 生成 3.3V，RT9182-G 再生成 2.5V/1.8V；TP4057 负责 VIN_USB 到 VBAT 充电，D1/D2 将 VIN_USB/VBAT 汇入 VBUS。ESP32-Wrover 连接 24-pin FPC、GPIO14 双向 LED、SPM1423 数字麦克风和可选未装的 MPU60X0/BME280；CP2104 通过 Micro-USB 提供串口及 DTR/RTS 自动下载。图面没有 OV2640 器件、存储容量、镜头/成像性能、完整 DVP 语义、HY2.0 接口或 Wi-Fi 应用配置。

## 检索关键词

`ESP32-CAM PSRAM`、`ESP32CAM-PSRAM`、`U017-PCBA`、`ESP32-Wrover`、`OV2640`、`PSRAM`、`SY8089`、`RT9182-G`、`TP4057`、`CP2104`、`SPM1423HM4H-B`、`MPU60X0`、`BME280`、`FPC0.5-SMT-24P-B`、`USB_Micro`、`VBUS`、`VBAT`、`VCC_3V3`、`VDD_2V5`、`VDD_1V8`、`GPIO14`、`GPIO0`、`EN`、`DTR`、`RTS`、`TXD0`、`RXD0`、`DVP`、`SCCB`、`HY2.0-4P`、`4MB Flash`、`4MB PSRAM`、`150 degree`、`WiFi AP`、`192.168.4.1`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U4 | ESP32-Wrover | ESP32 无线主控模组，连接摄像头 FPC、USB UART、LED、数字麦克风与可选传感器 | 图 794cbb7a3c54 / 第 1 页 / 上左 U4 ESP32-Wrover pins1-39 |
| U1 | SY8089 | VBUS 到 VCC_3V3 的同步降压转换器 | 图 46c05cd332c8 / 第 1 页 / 上方 U1 SY8089、L1 2.2uH 与 VBUS/VCC_3V3 |
| U2 | RT9182-G | VCC_3V3 到 VDD_2V5/VDD_1V8 的双路 LDO | 图 46c05cd332c8 / 第 1 页 / 中左 U2 RT9182-G 与 2V5/1V8 输出 |
| U3 | TP4057 | VIN_USB 到 VBAT 的单节锂电池充电管理 | 图 46c05cd332c8 / 第 1 页 / 左下 U3 TP4057、LED1/R3/R4 与 VBAT |
| J1 | FPC0.5-SMT-24P-B | 摄像头数据、时钟、控制与电源的 24-pin FPC 接口 | 图 794cbb7a3c54 / 第 1 页 / 上中 J1 FPC0.5-SMT-24P-B pins1-24 |
| U5 | SPM1423HM4H-B | GPIO2 数据、GPIO4 时钟的数字麦克风 | 图 794cbb7a3c54 / 第 1 页 / 中右 U5 SPM1423HM4H-B、DAT GPIO2、CLK GPIO4 |
| U6,U7 | MPU60X0 / BME280 | 标注为 Not Installed Optional 的惯性与环境传感器位置 | 图 794cbb7a3c54 / 第 1 页 / 下方 U6 MPU60X0、U7 BME280 与红色 Not Installed Optional 标注 |
| U8,U9 | CP2104 / USB_Micro | Micro-USB 到 ESP32 UART 的 USB 转串口与下载接口 | 图 e5ccaeec1a54 / 第 1 页 / 中上 U8 CP2104 与下中 U9 USB_Micro |

## 系统结构

### ESP32-Wrover 主控模组

U4 明确标为 ESP32-Wrover，VCC_3V3 供电，展开 GPIO0-39、TXD0/RXD0、EN 与模块地；SD0-SD3/CMD/CLK 外部引脚在本页标为未连接。

- 参数与网络：`module=ESP32-Wrover`；`supply=VCC_3V3`
- 证据：图 794cbb7a3c54 / 第 1 页 / U4 ESP32-Wrover

## 电源

### VBUS 到 3.3V、2.5V 与 1.8V 电源树

U1 SY8089 以 VBUS 为输入，经 L1 2.2uH 生成 VCC_3V3；U2 RT9182-G 以 VCC_3V3 为输入，分别输出 VDD_2V5 与 VDD_1V8。

- 参数与网络：`input=VBUS`；`rails=VCC_3V3,VDD_2V5,VDD_1V8`
- 证据：图 46c05cd332c8 / 第 1 页 / U1 SY8089 与 U2 RT9182-G

### USB 充电与 VIN_USB/VBAT 电源汇流

U3 TP4057 以 VIN_USB 为输入并输出 VBAT，LED1/R3 显示充电状态，R4 3K 设置 PROG；D1/D2 两颗 1N5819 将 VIN_USB 与 VBAT 分别连接到 VBUS。

- 参数与网络：`charger=TP4057`；`usb_input=VIN_USB`；`battery_net=VBAT`；`system_bus=VBUS`
- 证据：图 46c05cd332c8 / 第 1 页 / 下方 U3/LED1/R3/R4/D1/D2

## 接口

### 24-pin 摄像头 FPC 的 ESP32 GPIO 与电源

J1 FPC0.5-SMT-24P-B 引出 GPIO34、GPIO35、GPIO5、GPIO32、GPIO39、GPIO21、GPIO18、GPIO36、GPIO27、GPIO19、GPIO26、GPIO22、GPIO23、GPIO25，以及 VCC_3V3、VCC_2V5 和 GND。

- 参数与网络：`connector_pins=24`；`connector=FPC0.5-SMT-24P-B`；`gpio_bundle=34,35,5,32,39,21,18,36,27,19,26,22,23,25`
- 证据：图 794cbb7a3c54 / 第 1 页 / J1 pins1-24 net labels

### GPIO14 红蓝指示灯

GPIO14 连接 LED2 BLUE 与 LED3 RED 的公共驱动节点，LED2 另一端接 GND，LED3 另一端接 VCC_3V3。

- 参数与网络：`gpio=14`；`colors=blue,red`
- 证据：图 794cbb7a3c54 / 第 1 页 / 右上 GPIO14、LED2 BLUE、LED3 RED

### CP2104 USB 转串口

U8 CP2104 的 TXD 经 R10 470ohm 连接 RXD0，RXD 连接 TXD0；U9 USB_Micro 的 D-/D+ 经 R16/R17 22ohm 和 D3/D4 ESD 器件连接 USB_DN/USB_DP。

- 参数与网络：`bridge=CP2104`；`usb_connector=USB_Micro`；`uart=TXD0,RXD0`
- 证据：图 e5ccaeec1a54 / 第 1 页 / U8 CP2104、U9 USB_Micro、R10/R16/R17/D3/D4

## 音频

### SPM1423 数字麦克风

U5 SPM1423HM4H-B 由 VCC_3V3 供电，DAT 连接 GPIO2，CLK 连接 GPIO4，SEL 与 GND 接地。

- 参数与网络：`microphone=SPM1423HM4H-B`；`data_gpio=2`；`clock_gpio=4`
- 证据：图 794cbb7a3c54 / 第 1 页 / U5 SPM1423HM4H-B

## 传感器

### 可选未装 MPU60X0 与 BME280

U6 MPU60X0 与 U7 BME280 电路被红色箭头标为 Not Installed Optional；两者连接 VCC_3V3，并使用 GPIO23/GPIO22 总线网络。

- 参数与网络：`unpopulated=MPU60X0,BME280`；`bus_gpio=GPIO23,GPIO22`
- 证据：图 794cbb7a3c54 / 第 1 页 / U6/U7 与 Not Installed Optional 标注

## 调试与烧录

### DTR/RTS 自动下载与复位

CP2104 DTR/RTS 通过 R9/R12 10K 和 VT1/VT2 两颗 NPN-S8050 分别控制 ESP32 EN 与 GPIO0；S1 将 EN 手动拉低，R18 10K 上拉并配 C1 2.2uF。

- 参数与网络：`auto_program_signals=DTR,RTS`；`esp32_controls=EN,GPIO0`；`manual_reset=S1`
- 证据：图 e5ccaeec1a54 / 第 1 页 / 左上 VT1/VT2/DTR/RTS 与左下 S1/R18/C1

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | ESP32-Wrover 主控模组 | `module=ESP32-Wrover`；`supply=VCC_3V3` |
| 电源 | VBUS 到 3.3V、2.5V 与 1.8V 电源树 | `input=VBUS`；`rails=VCC_3V3,VDD_2V5,VDD_1V8` |
| 电源 | USB 充电与 VIN_USB/VBAT 电源汇流 | `charger=TP4057`；`usb_input=VIN_USB`；`battery_net=VBAT`；`system_bus=VBUS` |
| 接口 | 24-pin 摄像头 FPC 的 ESP32 GPIO 与电源 | `connector_pins=24`；`connector=FPC0.5-SMT-24P-B`；`gpio_bundle=34,35,5,32,39,21,18,36,27,19,26,22,23,25` |
| 音频 | SPM1423 数字麦克风 | `microphone=SPM1423HM4H-B`；`data_gpio=2`；`clock_gpio=4` |
| 传感器 | 可选未装 MPU60X0 与 BME280 | `unpopulated=MPU60X0,BME280`；`bus_gpio=GPIO23,GPIO22` |
| 接口 | GPIO14 红蓝指示灯 | `gpio=14`；`colors=blue,red` |
| 接口 | CP2104 USB 转串口 | `bridge=CP2104`；`usb_connector=USB_Micro`；`uart=TXD0,RXD0` |
| 调试与烧录 | DTR/RTS 自动下载与复位 | `auto_program_signals=DTR,RTS`；`esp32_controls=EN,GPIO0`；`manual_reset=S1` |
| 内存与 Flash | Flash、RAM 与 PSRAM 容量 | `documented_flash_mb=4`；`documented_psram_mb=4`；`description_ram_kb=520`；`table_ram_kb=500` |
| 传感器 | OV2640、2MP 与镜头成像参数 | `documented_sensor=OV2640`；`documented_megapixels=2`；`documented_optical_format=1/4 inch`；`documented_fov_deg=150`；`documented_formats=YUV422/420,YCbCr422,RGB565/555,Raw RGB` |
| 接口 | OV2640 DVP/SCCB 映射与 PWDN | `documented_control=SIOC=G23,SIOD=G22,XCLK=G27,VSYNC=G25,HREF=G26,PCLK=G21,RESET=G15`；`documented_data=D2=G32,D3=G35,D4=G34,D5=G5,D6=G39,D7=G18,D8=G36,D9=G19`；`documented_pwdn_pulldown_kohm=12` |
| 接口 | HY2.0-4P G13/G4 接口 | `documented_scl=G13`；`documented_sda=G4`；`documented_power=5V,GND` |
| 系统结构 | Wi-Fi AP 摄像头预装固件 | `documented_ssid_prefix=m5stack-`；`documented_ip=192.168.4.1`；`documented_resolution=600x800`；`documented_fps=5-6` |
| 系统结构 | 板体尺寸与重量 | `documented_size_mm=47x20x10`；`documented_weight_g=9.4` |

## 待确认事项

- `memory.documented-capacities`：正文描述称 4MB Flash、520KB RAM、4MB PSRAM，规格表却写 4MB Flash、500KB RAM、4MB PSRAM；原理图只标 ESP32-Wrover，没有模组子型号、Flash/PSRAM 颗粒或容量标注。（证据：图 794cbb7a3c54 / 第 1 页 / U4 仅标 ESP32-Wrover，无容量信息）
- `sensor.documented-ov2640-imaging`：正文称配套 OV2640 2MP、1/4 inch、150-degree 广角镜头，并支持 YUV/YCbCr、RGB565/555 和 Raw RGB 输出；三页原理图没有 OV2640 器件、镜头、像素阵列或输出格式标注。（证据：图 794cbb7a3c54 / 第 1 页 / 仅有 J1 摄像头 FPC，无 OV2640 图符）
- `interface.documented-camera-map-pwdn`：正文把 SIOC/SIOD/XCLK/VSYNC/HREF/PCLK 映射到 G23/G22/G27/G25/G26/G21，把 D2-D9 映射到 G32/G35/G34/G5/G39/G18/G36/G19，并称 RESET 接 G15、PWDN 由 12K 下拉；当前图只确认多数 GPIO 出现在 J1，未显示 OV2640 信号名、G15 连接或 12K PWDN 电阻。（证据：图 794cbb7a3c54 / 第 1 页 / J1 仅标 GPIO 和电源，未标 OV2640 语义或 PWDN 电阻）
- `interface.documented-hy2-port`：正文称 HY2.0-4P 引出 SCL=G13、SDA=G4、5V 与 GND，并可有线获取摄像头图片；当前三页图没有 HY2.0-4P 连接器或该有线图像协议路径。（证据：图 794cbb7a3c54 / 第 1 页 / 页面无 HY2.0-4P 连接器）
- `system.documented-wifi-camera-firmware`：正文称预装 ESP-IDF Wi-Fi 相机固件，创建 m5stack- 前缀 AP，在 192.168.4.1 提供 600x800、约 5-6fps 视频；原理图不包含固件镜像、SSID、IP、图像尺寸或帧率配置。（证据：图 794cbb7a3c54 / 第 1 页 / ESP32-Wrover 硬件图无固件或网络配置）
- `system.documented-mechanical`：正文称产品尺寸 47x20x10mm、重量 9.4g；当前三页电气原理图没有板框、摄像头高度、机械公差或质量信息。（证据：图 46c05cd332c8 / 第 1 页 / 电气原理图无机械尺寸）
- `review.memory-capacities`：ESP32-Wrover 的具体子型号、Flash/PSRAM 容量和 RAM 应为 500KB 还是 520KB；原因：源文档内部 RAM 数值冲突，图面没有容量或模组子型号。
- `review.ov2640-imaging`：配套摄像头是否为 OV2640 2MP 1/4 inch 150-degree 镜头及支持哪些输出格式；原因：当前原理图只有摄像头 FPC，无传感器和镜头电路。
- `review.camera-map-pwdn`：OV2640 全部 DVP/SCCB/RESET/PWDN 引脚在当前硬件版本的实际连接是什么；原因：图面只标 J1 GPIO，未显示 OV2640 语义、G15 或 12K PWDN。
- `review.hy2-port`：HY2.0-4P 是否实际装配，G13/G4 的有线图像协议和带宽是什么；原因：当前三页原理图没有 HY2.0 连接器。
- `review.wifi-camera-firmware`：量产预装固件的版本、SSID、IP、默认分辨率和实际帧率是什么；原因：这些行为由软件镜像和运行环境决定。
- `review.mechanical`：47x20x10mm 外形与 9.4g 重量由哪份机械图和量产配置确认；原因：电气原理图没有机械与质量信息。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `46c05cd332c8c7e51b5650844de2a7bceb43307c6e40f703f728119ac8562180` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_01.webp` |
| 2 | 1 | `794cbb7a3c5418d5d9ff7d5d33747368cd8abb6d109ea2d2c1f15f8c4992c8da` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_02.webp` |
| 3 | 1 | `e5ccaeec1a54e3359ebda4eef57a310709c03edeca5872b60e1ed6128bc12b6e` | `https://m5stack.oss-cn-shenzhen.aliyuncs.com/image/m5-docs_schematic/unit/m5camera_sch_03.webp` |

---

源文档：`zh_CN/unit/ESP32CAM-PSRAM.md`

源文档 SHA-256：`5f0bcf0ff2d4099a30cbb8df3ed0cf7b8884c1c0eb0f631e2db397d5beab182d`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
