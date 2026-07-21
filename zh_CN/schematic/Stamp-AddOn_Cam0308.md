# Stamp-AddOn_Cam0308 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Stamp-AddOn_Cam0308 |
| SKU | A178 |
| 产品 ID | `stamp-addon-cam0308-be641eb7056e` |
| 源文档 | `zh_CN/stamp/Stamp-AddOn_Cam0308.md` |

## 概述

单页原理图标题为 Stamp S3 BAT CAM、Revision V0.3，核心器件 U3 为 GC0308。传感器通过 D0-D7 八位 DVP 数据、PCLK、VSYNC、HSYNC、MCLK 与主机连接，使用 G47_SCL/G48_SDA 作为 SBCL/SBDA 配置总线；G39_PWDN 由 100K 下拉，G41_CAM_RST 由 100K 上拉到 3V3_L2。JP1 为 X0400WVS-24-LPV01 24-pin 接口。图面未标 I2C/SCCB 地址、分辨率、帧率、MCLK 数值、功耗、电压范围、连接器间距或机械尺寸。

## 检索关键词

`Stamp-AddOn_Cam0308`、`Stamp-AddOn Cam0308`、`A178`、`Stamp S3 BAT CAM`、`V0.3`、`GC0308`、`CMOS camera`、`DVP`、`D0-D7`、`PCLK`、`VSYNC`、`HSYNC`、`MCLK`、`SCCB`、`I2C`、`SBCL`、`SBDA`、`G47_SCL`、`G48_SDA`、`G39_PWDN`、`G41_CAM_RST`、`3V3_L2`、`X0400WVS-24-LPV01`、`24Pin FPC`、`VGA`、`QVGA`、`0x21`、`20MHz XCLK`、`PWDN`、`RESETB`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U3 | GC0308 | 八位 DVP CMOS 图像传感器 | 图 7f6350f20f99 / 第 1 页 / B3-C3 U3 GC0308 |
| JP1 | X0400WVS-24-LPV01 | 连接 Stamp 主机与摄像头信号的 24-pin FPC 接口 | 图 7f6350f20f99 / 第 1 页 / A1-B1 JP1 pins1-24 |
| R5,R6,C5-C7 | 100K control pulls / 100nF decoupling | PWDN 与 RESETB 默认状态及传感器电源/参考去耦 | 图 7f6350f20f99 / 第 1 页 / A2-B3 R5/R6/C5/C6/C7 |

## 系统结构

### GC0308 摄像头核心

U3 明确标为 GC0308，页面展开 DVDD28、VREF、AVDD25、SBCL/SBDA、PWDN、RESETB、INCLK、D0-D7、PCLK、VSYNC、HSYNC 与 GND 引脚。

- 参数与网络：`sensor=GC0308`；`parallel_data_bits=8`
- 证据：图 7f6350f20f99 / 第 1 页 / B3-C3 U3 GC0308 全部引脚

### 图纸标题与硬件修订

原理图标题栏写为 Stamp S3 BAT CAM，Revision V0.3，Date 5/06/2026，Number 1/1。

- 参数与网络：`schematic_title=Stamp S3 BAT CAM`；`revision=V0.3`；`date=5/06/2026`；`sheets=1/1`
- 证据：图 7f6350f20f99 / 第 1 页 / D3-D4 title block

## 电源

### PWDN 默认正常工作状态

G39_PWDN 连接 GC0308 PWDN，并由 R5 100K 下拉到 GND；图面注释定义 PWDN=0 为 normal work、PWDN=1 为 standby，因此默认状态为正常工作。

- 参数与网络：`control_net=G39_PWDN`；`pull=100K to GND`；`active_standby_level=1`
- 证据：图 7f6350f20f99 / 第 1 页 / A2-B3 R5、PWDN 注释与 U3 PWDN

### GC0308 电源与参考去耦

3V3_L2 连接 GC0308 DVDD28 并配置 C5 100nF；VREF 与 AVDD25 各配置 C6/C7 100nF 对地电容，传感器 GND 直接接地。

- 参数与网络：`external_rail=3V3_L2`；`decoupling=C5,C6,C7 100nF`
- 证据：图 7f6350f20f99 / 第 1 页 / B3-C3 U3 DVDD28/VREF/AVDD25/GND 与 C5-C7

## 接口

### 八位 DVP 数据映射

GC0308 D0-D7 分别连接 G21_D0、G18_D1、G16_D2、G15_D3、G14_D4、G12_D5、G38_D6、G40_D7，并全部引到 JP1。

- 参数与网络：`d0=G21`；`d1=G18`；`d2=G16`；`d3=G15`；`d4=G14`；`d5=G12`；`d6=G38`；`d7=G40`
- 证据：图 7f6350f20f99 / 第 1 页 / U3 D0-D7 与 JP1 left pins2-18

## 总线

### SCCB 配置总线

GC0308 SBCL 连接 G47_SCL，SBDA 连接 G48_SDA；两条网络分别引到 JP1 pin17 与 pin23。

- 参数与网络：`clock_net=G47_SCL`；`data_net=G48_SDA`；`sensor_pins=SBCL,SBDA`
- 证据：图 7f6350f20f99 / 第 1 页 / B3 U3 SBCL/SBDA 与 A1-B1 JP1 pins17/23

## 时钟

### 摄像头输入、像素与帧同步信号

GC0308 INCLK 连接 G46_MCLK，PCLK 连接 G13_PCLK，VSYNC 连接 G42_VS，HSYNC 连接 G17_HS；四路均引到 JP1。

- 参数与网络：`input_clock=G46_MCLK`；`pixel_clock=G13_PCLK`；`vsync=G42_VS`；`hsync=G17_HS`
- 证据：图 7f6350f20f99 / 第 1 页 / U3 INCLK/PCLK/VSYNC/HSYNC 与 JP1 pins1/8/9/13

## 复位

### RESETB 默认正常工作状态

G41_CAM_RST 连接 GC0308 RESETB，并由 R6 100K 上拉到 3V3_L2；图面注释定义 RESETB=0 为 chip reset、RESETB=1 为 normal work。

- 参数与网络：`reset_net=G41_CAM_RST`；`pull=100K to 3V3_L2`；`active_reset_level=0`
- 证据：图 7f6350f20f99 / 第 1 页 / A3-B3 R6、RESETB 注释与 U3 RESETB

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | GC0308 摄像头核心 | `sensor=GC0308`；`parallel_data_bits=8` |
| 接口 | 八位 DVP 数据映射 | `d0=G21`；`d1=G18`；`d2=G16`；`d3=G15`；`d4=G14`；`d5=G12`；`d6=G38`；`d7=G40` |
| 总线 | SCCB 配置总线 | `clock_net=G47_SCL`；`data_net=G48_SDA`；`sensor_pins=SBCL,SBDA` |
| 时钟 | 摄像头输入、像素与帧同步信号 | `input_clock=G46_MCLK`；`pixel_clock=G13_PCLK`；`vsync=G42_VS`；`hsync=G17_HS` |
| 电源 | PWDN 默认正常工作状态 | `control_net=G39_PWDN`；`pull=100K to GND`；`active_standby_level=1` |
| 复位 | RESETB 默认正常工作状态 | `reset_net=G41_CAM_RST`；`pull=100K to 3V3_L2`；`active_reset_level=0` |
| 电源 | GC0308 电源与参考去耦 | `external_rail=3V3_L2`；`decoupling=C5,C6,C7 100nF` |
| 系统结构 | 图纸标题与硬件修订 | `schematic_title=Stamp S3 BAT CAM`；`revision=V0.3`；`date=5/06/2026`；`sheets=1/1` |
| 总线地址 | SCCB/I2C 设备地址 0x21 | `documented_address=0x21` |
| 传感器 | GC0308 分辨率、光学与帧率参数 | `documented_megapixels=0.3`；`documented_optical_format=1/6.5 inch`；`documented_pixel_um=3.4x3.4`；`documented_resolutions=640x480,320x240`；`documented_fps=30`；`documented_xclk_mhz=20` |
| 电源 | 供电范围与待机/工作电流 | `documented_supply_v=2.7-3.3`；`documented_sleep_ua=10`；`documented_active_ma=25` |
| 接口 | 24Pin 0.5mm FPC 接口 | `documented_pins=24`；`documented_pitch_mm=0.5`；`schematic_part=X0400WVS-24-LPV01` |
| 系统结构 | L 型 FPC、M2 固定孔与工作温度 | `documented_structure=L-shaped flexible FPC`；`documented_mount=M2`；`documented_temperature_c=-20 to 60` |

## 待确认事项

- `address.documented-sccb-address`：正文称 GC0308 的 I2C/SCCB 设备地址为 0x21；原理图只显示 SBCL/SBDA 网络，没有地址标注、地址选择引脚或 7-bit/8-bit 表示说明。（证据：图 7f6350f20f99 / 第 1 页 / U3 SBCL/SBDA 无地址信息）
- `sensor.documented-imaging-specs`：正文称 GC0308 为 0.3MP、1/6.5 英寸、3.4um 像素，支持 VGA 640x480 与 QVGA 320x240，并在 20MHz XCLK 下输出 VGA 30fps；原理图没有像素阵列、分辨率、光学尺寸、帧率或时钟频率标注。（证据：图 7f6350f20f99 / 第 1 页 / U3 仅标 GC0308 与信号名，无成像参数）
- `power.documented-operating-range`：正文称供电范围为 2.7-3.3V，PWDN 高电平休眠约 10uA，VGA 工作约 25mA；图面只显示 3V3_L2、PWDN 控制与去耦，没有电流检测、输入容差或测试条件。（证据：图 7f6350f20f99 / 第 1 页 / 3V3_L2 与 PWDN 网络，无电流测量或电压范围）
- `interface.documented-fpc-pitch`：正文称接口为 24Pin、0.5mm 间距；原理图确认 JP1 有 24 pins 且料号为 X0400WVS-24-LPV01，但没有机械尺寸或明确的 0.5mm 间距标注。（证据：图 7f6350f20f99 / 第 1 页 / JP1 pins1-24 与料号，无机械尺寸）
- `system.documented-mechanical-environment`：正文称模组采用 L 型柔性 FPC、侧边 M2 固定孔并在 -20C 至 60C 无凝露环境工作；当前电气原理图没有板框、层叠、孔位、柔性区或温度额定信息。（证据：图 7f6350f20f99 / 第 1 页 / 电气原理图无板框、孔位或环境额定）
- `review.sccb-address`：GC0308 的 0x21 是 7-bit 地址还是其他表示形式；原因：原理图没有地址标注或地址选择硬件。
- `review.imaging-specs`：VGA/QVGA、30fps、20MHz XCLK、光学尺寸与像素参数适用哪些寄存器配置；原因：原理图只确认传感器型号和接口。
- `review.operating-power`：2.7-3.3V 范围、10uA 休眠与 25mA 工作电流的供电边界和测试条件是什么；原因：图面只显示 3V3_L2 和 PWDN，没有输入范围与电流测量。
- `review.fpc-pitch`：JP1 X0400WVS-24-LPV01 的实际触点间距是否为 0.5mm；原因：图纸没有连接器机械尺寸，需查料号规格或 PCB 封装。
- `review.mechanical-environment`：L 型柔性区、M2 固定孔和 -20C 至 60C 环境额定由哪份机械图与材料规格确认；原因：当前资源仅为电气原理图。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `7f6350f20f999b52cf1c21ac4e176d606d671628f520de8095ac8ffa5e5d33a2` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1256/SCH_A178_Stamp-AddOn_Cam0308_CAM_SCH_PDF_20260506_2026_06_09_09_31_04_page_01.png` |

---

源文档：`zh_CN/stamp/Stamp-AddOn_Cam0308.md`

源文档 SHA-256：`490a453425830b34f613db63428a18db58cf930f2ad3d0adfbe5f5a911a66d7e`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
