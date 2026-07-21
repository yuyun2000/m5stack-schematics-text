# Tab5 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Tab5 |
| SKU | C145 |
| 产品 ID | `tab5-2e8b5b5de1fb` |
| 源文档 | `zh_CN/core/Tab5.md` |

## 概述

Tab5 以 ESP32-P4 为主控并通过 SDIO2 连接 ESP32-C6-MINI-1U 无线模块，集成 MIPI-DSI 显示、MIPI-CSI 摄像头、microSD、双芯片音频、RS-485、USB、可切换射频天线以及电池充放电与多路电源管理电路。

## 检索关键词

`Tab5`、`C145`、`ESP32-P4`、`ESP32-C6-MINI-1U`、`MIPI-DSI`、`MIPI-CSI`、`SDIO1`、`SDIO2`、`BMI270`、`ES7210`、`ES8388`、`SIT3088EEUA`、`RS-485`、`INA226`、`RX8130CE`、`IP2326`、`M5-Bus`、`SOC_3.3V`、`SYS_INT5V`、`SYS_USB5V`、`xG31_SYS_SDA`、`xG32_SYS_SCL`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | ESP32-P4 | 系统主控 SoC | 图 0073d2eba37a / 第 1 页 / 网格 2B-D，U1 ESP32-P4 主控符号及全部 GPIO、MIPI、USB 和 SDIO 网络 |
| U2 | ESP32-C6-MINI-1U | 无线通信模块 | 图 0073d2eba37a / 第 1 页 / 网格 4B-D，U2 ESP32-C6-MINI-1U 及 SDIO2、UART、复位和射频网络 |
| U3 | XM25QH128CHIQ | ESP32-P4 外部串行 Flash | 图 0073d2eba37a / 第 1 页 / 网格 3B-C，U3 与 FLASH_CS、FLASH_DO、FLASH_SCK、FLASH_DI、FLASH_HOLD、FLASH_WP 网络 |
| U6 | PI4IOE5V6408 | 显示、触控、摄像头、扬声器和扩展电源控制 I/O 扩展器 | 图 0073d2eba37a / 第 1 页 / 网格 4A-B，U6 及 RF_PTH_L_INT_H_EXT、SPK_EN、EXT5V_EN、LCD_RST、TP_RST、CAM_RST、HP_DET |
| U7 | PI4IOE5V6408 | 无线、电源、USB 和充电控制 I/O 扩展器 | 图 0073d2eba37a / 第 1 页 / 网格 4B-C，U7 及 WLAN_PWR_EN、USB5V_EN、PWROFF_PLUSE、nCHG_QC_EN、CHG_STAT、CHG_EN |
| U19 | BMI270 | 惯性测量单元 | 图 6595fcde2331 / 第 1 页 / 网格 1B-C，U19 BMI270、I2C 电平转换和 E_TRIG 中断电路 |
| U13 | ES7210 | 双麦克风音频 ADC | 图 5df9e83529fc / 第 1 页 / 网格 2A-C，U13 ES7210、I2C、I2S 和 MIC1/MIC2 差分输入 |
| U14 | ES8388 | 音频编解码器和耳机输出驱动 | 图 5df9e83529fc / 第 1 页 / 网格 2C-D，U14 ES8388、I2C、I2S、HPOUT_L 和 HPOUT_R 网络 |
| U15 | NS4150B | 扬声器功率放大器 | 图 5df9e83529fc / 第 1 页 / 网格 4C-D，U15 NS4150B、SPK_EN、SYS_INT5V 和差分扬声器输出 |
| U18 | SIT3088EEUA | RS-485 收发器 | 图 8417c78e9731 / 第 1 页 / 网格 2C-D，U18 SIT3088EEUA、A/B 总线及 GPIO20、GPIO21、GPIO34 控制网络 |
| U20 | IP2326 | 双节电池充电管理芯片 | 图 d2a3a730220a / 第 1 页 / 网格 1B-C，U20 IP2326 及 SYS_5VCHG、SYS_BAT_2S、CHG_EN、CHG_STAT 网络 |
| U21 | MP4560DN | SYS_VIN 至 PRE_5V 降压转换器 | 图 d2a3a730220a / 第 1 页 / 网格 1A，U21 MP4560DN、SYS_VIN 输入和 PRE_5V 输出 |
| U31 | INA226 | 电池电流和总线电压监测器 | 图 d2a3a730220a / 第 1 页 / 网格 1D，U31 INA226 与 R39 电流采样电阻、SYS_BAT_PRE 和 SYS_BAT_2S |
| U30 | RX8130CE | 实时时钟 | 图 d2a3a730220a / 第 1 页 / 网格 3D，U30 RX8130CE、VDD_STBY、I2C 和 E_TRIG 网络 |
| U28 | PMS150G-U06 | 开关机、启动和中断状态管理微控制器 | 图 d2a3a730220a / 第 1 页 / 网格 4A，U28 PMS150G-U06 及 MPWR_EN、SW_PWR、BOOT_GPIO35、nINT_STAT_TRIG |
| U29 | TPG619C6 | ESP32-C6 内置与外置天线路径射频开关 | 图 8417c78e9731 / 第 1 页 / 网格 3A-B，U29 TPG619C6、J13 射频输入、ANT1 内置天线和 J15 外置天线接口 |

## 系统结构

### ESP32-P4 与 ESP32-C6-MINI-1U

ESP32-P4 通过 SDIO2_D0、SDIO2_D1、SDIO2_D2、SDIO2_D3、SDIO2_CLK 和 SDIO2_CMD 连接 ESP32-C6-MINI-1U，并以 SOC_EXTRF_RST 控制其 EN。

- 参数与网络：`host=U1 ESP32-P4`；`wireless_module=U2 ESP32-C6-MINI-1U`；`reset_net=SOC_EXTRF_RST`
- 证据：图 0073d2eba37a / 第 1 页 / 网格 2B-D 的 U1 SDIO2 引脚与网格 4C-D 的 U2 IO19-IO23、EN 对应网络

### PMS150G-U06 管理控制

U28 PMS150G-U06 连接 MPWR_EN、SW_PWR、BOOT_GPIO35 和 nINT_STAT_TRIG，工作电源为 VDD_STBY。

- 参数与网络：`reference=U28`；`supply=VDD_STBY`；`signals=MPWR_EN, SW_PWR, BOOT_GPIO35, nINT_STAT_TRIG`
- 证据：图 d2a3a730220a / 第 1 页 / 网格 4A，U28 PMS150G-U06 的 PA3、PA4、PA5、PA6 与 VDD

## 核心器件

### ESP32-P4 外部 Flash

U3 XM25QH128CHIQ 通过 FLASH_CS、FLASH_DO、FLASH_SCK、FLASH_DI、FLASH_HOLD 和 FLASH_WP 网络连接 ESP32-P4 的专用 Flash 引脚。

- 参数与网络：`reference=U3`；`part_number=XM25QH128CHIQ`；`supply=ESP_LDO1`
- 证据：图 0073d2eba37a / 第 1 页 / 网格 2B-D 的 U1 FLASH 引脚和网格 3B-C 的 U3

## 电源

### LCD 背光

U8 ME2212 从 SYS_INT5V 驱动 LCD_LEDA，EN 由 LCD_BL_GPIO22 控制，LCD_LEDK 作为反馈回路返回。

- 参数与网络：`controller=U8 ME2212`；`input=SYS_INT5V`；`enable=LCD_BL_GPIO22`；`output=LCD_LEDA`
- 证据：图 6595fcde2331 / 第 1 页 / 网格 3A，U8 ME2212、L3、D3、LCD_LEDA 和 LCD_LEDK

### 主输入降压

U21 MP4560DN 从 SYS_VIN 取电，经 L5 输出 PRE_5V。

- 参数与网络：`converter=U21 MP4560DN`；`input=SYS_VIN`；`output=PRE_5V`；`inductor=L5 10uH`
- 证据：图 d2a3a730220a / 第 1 页 / 网格 1A，U21、L5、SYS_VIN 和 PRE_5V

### 电池充电路径

U20 IP2326 以 SYS_5VCHG 为输入，VOUT 接 SYS_BAT_2S，充电使能和状态分别通过 CHG_EN 与 CHG_STAT 网络控制和读取。

- 参数与网络：`charger=U20 IP2326`；`input=SYS_5VCHG`；`battery_net=SYS_BAT_2S`；`enable=CHG_EN`；`status=CHG_STAT`
- 证据：图 d2a3a730220a / 第 1 页 / 网格 1B-C，U20 及 SYS_5VCHG、SYS_BAT_2S、CHG_EN、CHG_STAT

### 电池电流监测

U31 INA226 跨接 R39 0.005 Ω 分流电阻监测 SYS_BAT_PRE 到 SYS_BAT_2S 的电流，并接入 xG32_SYS_SCL、xG31_SYS_SDA。

- 参数与网络：`monitor=U31 INA226`；`shunt=R39`；`shunt_ohm=0.005`；`scl=xG32_SYS_SCL`；`sda=xG31_SYS_SDA`
- 证据：图 d2a3a730220a / 第 1 页 / 网格 1D，U31、R39、SYS_BAT_PRE 和 SYS_BAT_2S

### 系统派生电源

SOC_3.3V 由 U4 SY8089AAAC 从 SYS_INT5V 生成；SYS_EXT5V0 由 U26 LPW5209AB5F 受 EXT5V_EN 控制生成；SYS_USB5V 由 U27 MT9700 受 USB5V_EN 控制生成。

- 参数与网络：`soc_3v3_converter=U4 SY8089AAAC`；`external_5v_switch=U26 LPW5209AB5F`；`usb_5v_switch=U27 MT9700`
- 证据：图 d2a3a730220a / 第 1 页 / 网格 3B-C，U4 SOC_3.3V 电源与网格 4B-C 的 U26、U27 输出开关

## 接口

### 显示与触控 FPC J3

J3 使用两数据通道 MIPI-DSI，包含 LCD_DSI_CK_P/N、LCD_DSI_D0_P/N 和 LCD_DSI_D1_P/N；同一连接器还引出 I2C、TP_INT、TP_RST、LCD_RST 及背光 LEDA/LEDK。

- 参数与网络：`connector=J3`；`connector_type=FPC 24P`；`backlight_enable=LCD_BL_GPIO22`；`touch_interrupt=TP_INT_GPIO23`
- 证据：图 6595fcde2331 / 第 1 页 / 网格 4A-B，J3 FPC 24P 的全部显示、触控和背光网络; 图 0073d2eba37a / 第 1 页 / 网格 2C-D，U1 的 DSI 差分引脚、LCD_BL_GPIO22 和 TP_INT_GPIO23

### 摄像头 FPC J4

J4 引出两数据通道 MIPI-CSI 差分信号、CAM_MCLK_1V8、CAM_RST_1V8、CAM_SCL_1V8、CAM_SDA_1V8 以及 CAM_VDD1、CAM_VDD2、CAM_VDD3 三路电源。

- 参数与网络：`connector=J4`；`connector_type=FPC 24P`；`mipi_lanes=2`；`clock_source=X2 PXT_24M`
- 证据：图 6595fcde2331 / 第 1 页 / 网格 4B-D，J4 FPC 24P 的 CAM_CSI、控制和电源网络; 图 6595fcde2331 / 第 1 页 / 网格 3B-D，X2 24MHz 振荡器、U9-U11 摄像头电源及 U35/U36 电平转换

### 双模拟麦克风

U17 和 U16 两只麦克风分别输出 AMIC1P/N 和 AMIC2P/N 差分信号，并经交流耦合连接 ES7210 的 MIC1P/N 与 MIC2P/N。

- 参数与网络：`microphone_1=U17`；`microphone_2=U16`；`adc=U13 ES7210`
- 证据：图 5df9e83529fc / 第 1 页 / 网格 4A-B 的 U17/U16 与网格 2A-C 的 U13 MIC1/MIC2 输入

### 扬声器输出

ES8388 的 HPOUT_L 经交流耦合和输入电阻驱动 NS4150B，NS4150B 由 SYS_INT5V 供电、SPK_EN 控制并输出差分扬声器信号。

- 参数与网络：`codec=U14 ES8388`；`amplifier=U15 NS4150B`；`enable=SPK_EN`；`supply=SYS_INT5V`
- 证据：图 5df9e83529fc / 第 1 页 / 网格 4C-D，C88、C89、R43、R44、U15 与 TP1/TP13 扬声器输出

### RS-485 接口

U18 SIT3088EEUA 的 RO 连接 RS485_RX_GPIO21，DI 连接 RS485_TX_GPIO20，nRE 与 DE 并接 RS485_DIR_GPIO34；A/B 连接外部 RS-485 接口。

- 参数与网络：`transceiver=U18 SIT3088EEUA`；`rx_gpio=21`；`tx_gpio=20`；`direction_gpio=34`
- 证据：图 8417c78e9731 / 第 1 页 / 网格 1C-2D，RS-485 连接器、U18 及 RS485_RX/TX/DIR 网络

### RS-485 终端电阻

RS-485 A/B 之间配置 120 Ω 电阻 R55，并由开关 S2 控制其接入。

- 参数与网络：`resistor=R55`；`resistance_ohm=120`；`switch=S2`
- 证据：图 8417c78e9731 / 第 1 页 / 网格 2C-D，S2 C01LHP 与 R55 120R/5% 跨接 RS-485 A/B

### USB Type-C 设备接口

J8 的 USBIN_DP/DM 经 ESD0524P D5、共模扼流圈 FT1 和 33 Ω 串联电阻连接 USB_DEVICE_DP/DM，VBUS 经 2 A/6 V 自恢复保险丝 FU1 接入 USB_5VIN。

- 参数与网络：`connector=J8`；`data_nets=USB_DEVICE_DP/DM`；`esd=D5 ESD0524P`；`fuse=FU1 2A/6V`
- 证据：图 8417c78e9731 / 第 1 页 / 网格 1A，J8、FU1、D5、FT1、R111、R112

### USB Type-A Host 接口

J10 由 SYS_USB5V 供电，USB_HOST_DP/DM 经 33 Ω 串联电阻、共模扼流圈 FT2 和 ESD0524P D21 连接接口数据脚。

- 参数与网络：`connector=J10`；`supply=SYS_USB5V`；`data_nets=USB_HOST_DP/DM`；`esd=D21 ESD0524P`
- 证据：图 8417c78e9731 / 第 1 页 / 网格 4B-C，J10、D21、FT2、R113、R114

### ESP32-C6 天线路径

ESP32-C6 射频信号经 U29 TPG619C6 在 ANT1 内置天线与 J15 外置天线接口之间切换，控制网络为 RF_PTH_L_INT_H_EXT 和 RF_PTH_EXT_EN。

- 参数与网络：`rf_switch=U29 TPG619C6`；`internal_antenna=ANT1`；`external_connector=J15`；`control_nets=RF_PTH_L_INT_H_EXT, RF_PTH_EXT_EN`
- 证据：图 8417c78e9731 / 第 1 页 / 网格 3A-4B，J13、U29、Q6、ANT1 和 J15

### M5-Bus

BUS1 M5_BUS 提供 SYS_VIN、SYS_EXT5V0、VBAT_OUT、SOC_3.3V、SOC_RST，以及 SPI、UART、I2C 和多路 GPIO 信号。

- 参数与网络：`connector=BUS1`；`pins=30`；`i2c=xG31_SYS_SDA, xG32_SYS_SCL`；`spi=xSPI_MOSI_G18, xSPI_MISO_G19, xSPI_SCK_GPIO5`
- 证据：图 8417c78e9731 / 第 1 页 / 网格 1B-2C，BUS1 M5_BUS 30 针连接器及各引脚网络

## 总线

### PI4IOE5V6408 I/O 扩展器

U6 和 U7 共用 xG32_SYS_SCL、xG31_SYS_SDA I2C 总线和 SOC_RST 复位；U6 的 ADDR 接地，U7 的 ADDR 接 SOC_3.3V。

- 参数与网络：`scl=xG32_SYS_SCL`；`sda=xG31_SYS_SDA`；`reset=SOC_RST`；`u6_addr_strap=GND`；`u7_addr_strap=SOC_3.3V`
- 证据：图 0073d2eba37a / 第 1 页 / 网格 4A-C，U6、U7 的 SCL、SDA、nRESET 和 ADDR 引脚

### microSD 卡槽 J2

J2 以 SDIO1_D0、SDIO1_D1、SDIO1_D2、SDIO1_D3、SDIO1_CMD 和 SDIO1_SCK 连接 ESP32-P4，并由 SOC_3.3V 供电。

- 参数与网络：`connector=J2`；`supply=SOC_3.3V`；`protection=D1 and D2 ESD0524P`
- 证据：图 6595fcde2331 / 第 1 页 / 网格 1C-2D，J2 TF_CARD_SOCKET、D1、D2 及 SDIO1 网络

### BMI270

BMI270 的 SCx、SDx 通过 Q13A/Q13B 双向电平转换连接 xG32_SYS_SCL 和 xG31_SYS_SDA；INT1 经 Q8 接入 E_TRIG。

- 参数与网络：`reference=U19`；`scl=xG32_SYS_SCL`；`sda=xG31_SYS_SDA`；`interrupt=E_TRIG`
- 证据：图 6595fcde2331 / 第 1 页 / 网格 1B-C，U19、Q8、Q13A、Q13B 和相关网络

### ES7210 与 ES8388 音频总线

ES7210 和 ES8388 共用 xG31_SYS_SDA、xG32_SYS_SCL 控制总线以及 GPIO30 MCLK、GPIO27 SCLK、GPIO29 LRCK；ES7210 的 SDOUT1 连接 GPIO28，ES8388 的 DSDIN 连接 GPIO26。

- 参数与网络：`mclk=GPIO30`；`sclk=GPIO27`；`lrck=GPIO29`；`adc_data=GPIO28`；`codec_data=GPIO26`
- 证据：图 5df9e83529fc / 第 1 页 / 网格 2A-C，U13 ES7210 的 CDATA/CCLK 和 I2S 网络; 图 5df9e83529fc / 第 1 页 / 网格 2C-D，U14 ES8388 的 CCLK/CDATA 和 I2S 网络

## 时钟

### ESP32-P4 主时钟

ESP32-P4 的 XTAL_P 和 XTAL_N 连接 40 MHz 晶体 X1，晶体两端各配置 15 pF 负载电容。

- 参数与网络：`reference=X1`；`frequency=40MHz`；`load_capacitors=C33=15pF, C34=15pF`
- 证据：图 0073d2eba37a / 第 1 页 / 网格 3A-B，X1 40MHz、C33、C34 及 XTAN、XTAP 网络

### RX8130CE 实时时钟

U30 RX8130CE 由 VDD_STBY 供电，SCL/SDA 连接系统 I2C，总线中断 nIRQ 通过 Q11 接入 E_TRIG，并配置后备电源器件 BT1。

- 参数与网络：`reference=U30`；`supply=VDD_STBY`；`interrupt=E_TRIG`；`backup=BT1`
- 证据：图 d2a3a730220a / 第 1 页 / 网格 3D，U30、Q11、BT1、VDD_STBY 和 E_TRIG

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | ESP32-P4 与 ESP32-C6-MINI-1U | `host=U1 ESP32-P4`；`wireless_module=U2 ESP32-C6-MINI-1U`；`reset_net=SOC_EXTRF_RST` |
| 时钟 | ESP32-P4 主时钟 | `reference=X1`；`frequency=40MHz`；`load_capacitors=C33=15pF, C34=15pF` |
| 核心器件 | ESP32-P4 外部 Flash | `reference=U3`；`part_number=XM25QH128CHIQ`；`supply=ESP_LDO1` |
| 总线 | PI4IOE5V6408 I/O 扩展器 | `scl=xG32_SYS_SCL`；`sda=xG31_SYS_SDA`；`reset=SOC_RST`；`u6_addr_strap=GND`；`u7_addr_strap=SOC_3.3V` |
| 接口 | 显示与触控 FPC J3 | `connector=J3`；`connector_type=FPC 24P`；`backlight_enable=LCD_BL_GPIO22`；`touch_interrupt=TP_INT_GPIO23` |
| 电源 | LCD 背光 | `controller=U8 ME2212`；`input=SYS_INT5V`；`enable=LCD_BL_GPIO22`；`output=LCD_LEDA` |
| 接口 | 摄像头 FPC J4 | `connector=J4`；`connector_type=FPC 24P`；`mipi_lanes=2`；`clock_source=X2 PXT_24M` |
| 总线 | microSD 卡槽 J2 | `connector=J2`；`supply=SOC_3.3V`；`protection=D1 and D2 ESD0524P` |
| 总线 | BMI270 | `reference=U19`；`scl=xG32_SYS_SCL`；`sda=xG31_SYS_SDA`；`interrupt=E_TRIG` |
| 总线 | ES7210 与 ES8388 音频总线 | `mclk=GPIO30`；`sclk=GPIO27`；`lrck=GPIO29`；`adc_data=GPIO28`；`codec_data=GPIO26` |
| 接口 | 双模拟麦克风 | `microphone_1=U17`；`microphone_2=U16`；`adc=U13 ES7210` |
| 接口 | 扬声器输出 | `codec=U14 ES8388`；`amplifier=U15 NS4150B`；`enable=SPK_EN`；`supply=SYS_INT5V` |
| 接口 | RS-485 接口 | `transceiver=U18 SIT3088EEUA`；`rx_gpio=21`；`tx_gpio=20`；`direction_gpio=34` |
| 接口 | RS-485 终端电阻 | `resistor=R55`；`resistance_ohm=120`；`switch=S2` |
| 接口 | USB Type-C 设备接口 | `connector=J8`；`data_nets=USB_DEVICE_DP/DM`；`esd=D5 ESD0524P`；`fuse=FU1 2A/6V` |
| 接口 | USB Type-A Host 接口 | `connector=J10`；`supply=SYS_USB5V`；`data_nets=USB_HOST_DP/DM`；`esd=D21 ESD0524P` |
| 接口 | ESP32-C6 天线路径 | `rf_switch=U29 TPG619C6`；`internal_antenna=ANT1`；`external_connector=J15`；`control_nets=RF_PTH_L_INT_H_EXT, RF_PTH_EXT_EN` |
| 接口 | M5-Bus | `connector=BUS1`；`pins=30`；`i2c=xG31_SYS_SDA, xG32_SYS_SCL`；`spi=xSPI_MOSI_G18, xSPI_MISO_G19, xSPI_SCK_GPIO5` |
| 电源 | 主输入降压 | `converter=U21 MP4560DN`；`input=SYS_VIN`；`output=PRE_5V`；`inductor=L5 10uH` |
| 电源 | 电池充电路径 | `charger=U20 IP2326`；`input=SYS_5VCHG`；`battery_net=SYS_BAT_2S`；`enable=CHG_EN`；`status=CHG_STAT` |
| 电源 | 电池电流监测 | `monitor=U31 INA226`；`shunt=R39`；`shunt_ohm=0.005`；`scl=xG32_SYS_SCL`；`sda=xG31_SYS_SDA` |
| 电源 | 系统派生电源 | `soc_3v3_converter=U4 SY8089AAAC`；`external_5v_switch=U26 LPW5209AB5F`；`usb_5v_switch=U27 MT9700` |
| 时钟 | RX8130CE 实时时钟 | `reference=U30`；`supply=VDD_STBY`；`interrupt=E_TRIG`；`backup=BT1` |
| 系统结构 | PMS150G-U06 管理控制 | `reference=U28`；`supply=VDD_STBY`；`signals=MPWR_EN, SW_PWR, BOOT_GPIO35, nINT_STAT_TRIG` |

## 待确认事项

- 无：当前结构化事实中没有标记为 `uncertain` 的内容。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `6c6c2afb71ccf33d85f0bea40878fa8bdf1751d036115ca577c6cb1283ba978a` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Tab5_Overall_Design_Block_Diagram.webp` |
| 2 | 1 | `0073d2eba37ad21668c3f6b06883f05ea77cc4018fdc42af023c92818f3d805e` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/sch_tab5_b08_page_01.webp` |
| 3 | 1 | `6595fcde23317d6070a71647ab65e765e04802ce22f0c62a3b0d5e422838ba7b` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/sch_tab5_b08_page_02.webp` |
| 4 | 1 | `5df9e83529fcfc566a0f426e0bfa19c351d6070f53e1a2695c59b01276e3bae7` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/sch_tab5_b08_page_03.webp` |
| 5 | 1 | `8417c78e97315268e61f6823101981144f20f1ef1bdfa14a74a15f6016d88e62` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/sch_tab5_b08_page_04.webp` |
| 6 | 1 | `d2a3a730220a661a14f2f95713176d9ef16dd8d223d24ad0260910f5d26aa1b2` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/sch_tab5_b08_page_05.webp` |

---

源文档：`zh_CN/core/Tab5.md`

源文档 SHA-256：`6c272963b453ca2eea49f0dbf65d1065e74422a1e0cba17252a0a7334acc459b`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
