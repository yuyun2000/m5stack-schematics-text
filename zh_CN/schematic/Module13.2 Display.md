# Module13.2 Display 原理图描述

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 产品 | Module13.2 Display |
| SKU | M126 |
| 产品 ID | `module13-2-display-b5f636da83c6` |
| 源文档 | `zh_CN/module/Display Module 13.2.md` |

## 概述

Module13.2 Display 以 U1 GW1NR-9/SDRAM FPGA 接收 M5-Bus 的 SPI/I2C/I2S 类信号，产生 24-bit RGB、同步信号和 I2S 音频送入 U6 LT8618SXB。LT8618SXB 将 RGB/音频转换为四对 TMDS 并输出到 HDMI1，CI2CA 接地配置地址 0x72。外部 VCC_EXT 经 SY8303A 生成 5.2 V/5 V，总线再由两颗 SY8089A 生成 1.2 V 与 3.3 V，并由 LP5907MFX-1.8 生成 1.8 V。模块提供 74.25 MHz 与 50 MHz 时钟、JTAG/SPI 配置、HDMI DDC/HPD、ESD 和 0.5 A HDMI 5 V 保护。

## 检索关键词

`Module13.2 Display`、`M126`、`GW1NR-9/SDRAM`、`GW1NR-LV9QN88C6-I5`、`LT8618SXB`、`LT8616SXB`、`0x72`、`0x39`、`SY8303A`、`SY8089A`、`LP5907MFX-1.8`、`HDMI`、`TMDS`、`RGB D0-D23`、`RGB_HSYNC`、`RGB_VSYNC`、`RGB_DE`、`RGB_IDCK`、`I2S_I_SCK`、`I2S_I_WS`、`I2S_I_SDO`、`I2S_I_MCLK`、`FPGA SPI`、`JTAG`、`74.250MHz`、`50MHz`、`VCC_1V2`、`VCC_1V8`、`VCC_3V3`、`VCC_5V`、`VBUS_5V`、`Ext_VIN_5-24V`、`HDMI_DCLK`、`HDMI_DSDA`、`HDMI_HPD`、`M5_BUS`、`1080P`、`24-bit RGB`

## 主要器件

| 位号 | 型号 | 作用 | 证据 |
| --- | --- | --- | --- |
| U1 | GW1NR-9/SDRAM | 视频/音频 FPGA，生成 24-bit RGB、I2S、配置与 JTAG 信号 | 图 c8856f121743 / 第 1 页 / A1-C4，U1A/U1B/U1C GW1NR-9/SDRAM banks1-3; 图 8f1bf8a1ccc6 / 第 1 页 / A2-B3，U1D GW1NR-9/SDRAM FPGA power |
| U6 | LT8618SXB(QFN64) | 24-bit RGB/I2S 到 HDMI TMDS 的音视频转换器 | 图 ec61131032b6 / 第 1 页 / A1-C2，U6 LT8618SXB(QFN64) RGB/I2S/I2C/TMDS |
| U7 | SY8303A | VCC_EXT 至 5.2 V/5 V 的主降压转换器 | 图 8f1bf8a1ccc6 / 第 1 页 / A1-A2，U7 SY8303A、L2 6.8uH、Vset=5.27V |
| U2/U8 | SY8089A | VCC_5V 至 VCC_1V2 与 VCC_3V3 的两路降压转换器 | 图 8f1bf8a1ccc6 / 第 1 页 / B1-B2，U2 1.2v DC-DC 与 U8 3.3v DC-DC |
| U3 | LP5907MFX-1.8 | VCC_5V 至 VCC_1V8 的 LDO | 图 8f1bf8a1ccc6 / 第 1 页 / C1-C2，U3 LP5907MFX-1.8 |
| X1/X2 | YSO690PR/74.250MHz/3225/3.3V; YSO690PR/50MHz/3225/3.3V | TMDS_CLK_IN 与 FPGA_CLK_IN 有源时钟源 | 图 c8856f121743 / 第 1 页 / C1-C2，X1 74.250MHz/R3 22R 与 X2 50MHz/R4 22R |
| HDMI1 | HDMI connector | TMDS、DDC、HPD 与 5 V 高清音视频输出连接器 | 图 43cbb9ce0587 / 第 1 页 / A3-C4，HDMI1 pins0-19 |
| BUS1 | M5BUS | M5Stack 主机 SPI/I2C/I2S/GPIO 与电源接口 | 图 43cbb9ce0587 / 第 1 页 / B1-B2，BUS1 M5BUS pins1-30 |
| J2 | IDC2X5 | FPGA JTAG 调试/下载接口 | 图 43cbb9ce0587 / 第 1 页 / C1-C2，J2 IDC2X5 BUS_SCK/TCK、MISO/TDO、CS/TMS、MOSI/TDI |
| J1 | DC_050 | 外部 VCC_EXT/GND 直流电源插座 | 图 43cbb9ce0587 / 第 1 页 / B2，J1 DC_050，Ext_VIN_5-24V |
| U4/U5 | PESDALC10N5VU | HDMI 四对 TMDS 的低电容 ESD 保护阵列 | 图 43cbb9ce0587 / 第 1 页 / A2-B3，U4/U5 PESDALC10N5VU 于 HDMI_TXC/TX0/TX1/TX2 |
| D22/D23/D25 | ESD5Z3.3C | HDMI DDC 与 HPD 的 3.3 V ESD 保护 | 图 43cbb9ce0587 / 第 1 页 / B2-C3，HDMI_DCLK/HDMI_DSDA/HDMI_HPD 至 ESD5Z3.3C |

## 系统结构

### 高清音视频输出架构

BUS1 的主机信号进入 U1 GW1NR-9/SDRAM FPGA，FPGA 生成 24-bit RGB、同步和 I2S 音频送给 U6 LT8618SXB，U6 输出 TMDS/DDC/HPD 到 HDMI1。

- 参数与网络：`host=BUS1 M5BUS`；`fpga=U1 GW1NR-9/SDRAM`；`bridge=U6 LT8618SXB`；`video=RGB D0-D23/DE/IDCK/HSYNC/VSYNC`；`audio=I2S SCK/WS/SDO/MCLK`；`output=HDMI1`
- 证据：图 c8856f121743 / 第 1 页 / U1 FPGA RGB/I2S outputs; 图 ec61131032b6 / 第 1 页 / U6 LT8618SXB RGB/I2S/TMDS; 图 43cbb9ce0587 / 第 1 页 / HDMI1 connector

## 核心器件

### FPGA 信号分区

U1 的 BANK2/BANK3 承载 RGB D0-D23、HSYNC、VSYNC、DE、IDCK 与 FPGA SPI 配置；BANK1 承载 I2S、主机 GPIO 和 HDMI LED 控制。

- 参数与网络：`reference=U1`；`marking=GW1NR-9/SDRAM`；`rgb=D0-D23 plus HSYNC/VSYNC/DE/IDCK`；`audio=I2S_I_SCK/WS/SDO/MCLK`；`configuration=FPGA_SPI_MOSI/MISO/CS/SCK`；`jtag=TMS/TCK/TDI/TDO`
- 证据：图 c8856f121743 / 第 1 页 / U1A/U1B/U1C banks1-3

## 电源

### 外部输入与 5 V 主电源

J1 DC_050 提供 VCC_EXT/GND；S1 与 Pwr_EN 控制 U7 SY8303A，U7 设定 Vset=5.27V、Freq=666kHz，输出 VCC_5V2 后经 D1 SS34 形成 VBUS_5V。

- 参数与网络：`connector=J1 DC_050`；`input=VCC_EXT`；`switch=S1 SS-12F23/Pwr_EN`；`converter=U7 SY8303A`；`inductor=L2 6.8uH`；`setpoint=5.27V`；`frequency=666kHz`；`diode=D1 SS34`；`output=VBUS_5V`
- 证据：图 43cbb9ce0587 / 第 1 页 / B2 J1 Ext_VIN_5-24V; 图 8f1bf8a1ccc6 / 第 1 页 / A1-A2 5V DC-DC 与 C1-D1/L2/U7

### FPGA/LT8618 次级电源

U2 SY8089A 从 VCC_5V 生成 VCC_1V2，U8 SY8089A 生成 VCC_3V3，U3 LP5907MFX-1.8 从 VCC_5V 生成 VCC_1V8；三路均有独立去耦和测试点。

- 参数与网络：`1v2=U2 SY8089A / TP2`；`3v3=U8 SY8089A / TP4`；`1v8=U3 LP5907MFX-1.8 / TP3`；`input=VCC_5V`
- 证据：图 8f1bf8a1ccc6 / 第 1 页 / B1-C2 1.2V/3.3V DC-DC 与 1.8V LDO

## 接口

### M5-Bus 使用引脚

BUS1 使用 pin3 VBUS_5V、pin7 BUS_G0、pin9 BUS_CS/TMS、pin11 BUS_G5、pin13 BUS_CSCL、pin15 BUS_G17、pin19 VHost_3V3、pins21/23 BUS_G26/BUS_G25，以及右侧 BUS_G15/G12/G2/BUS_CSDA/BUS_G16/BUS_SCK/TCK/BUS_MISO/TDO/BUS_MOSI/TDI 和多路 GND。

- 参数与网络：`power=pin3 VBUS_5V; pin19 VHost_3V3`；`i2c=pin13 BUS_CSCL; pin14 BUS_CSDA`；`jtag_spi=BUS_CS/TMS; BUS_SCK/TCK; BUS_MISO/TDO; BUS_MOSI/TDI`；`i2s_gpio=BUS_G0/G5/G12/G15/G16/G17/G25/G26`；`ground=pins26/28/30 plus lower ground`
- 证据：图 43cbb9ce0587 / 第 1 页 / B1-B2 BUS1 M5BUS pins1-30

### HDMI 输出连接

HDMI1 接收 HDMI_TX2/TX1/TX0/TXC 四对差分 TMDS、HDMI_DCLK/HDMI_DSDA、HDMI_HPD 与 VCC_5V；CEC pin13 与 NC pin14 未连接。

- 参数与网络：`tmps_pairs=TX2 pins1/3; TX1 pins4/6; TX0 pins7/9; TXC pins10/12`；`ddc=pin15 SCL HDMI_DCLK; pin16 SDA HDMI_DSDA`；`hpd=pin19 HDMI_HPD`；`5v=pin18 VCC_5V`；`cec=pin13 NC`；`shield=GND`
- 证据：图 43cbb9ce0587 / 第 1 页 / A3-C4 HDMI1

## 总线

### 24-bit RGB 视频总线

FPGA RGB_D0 至 RGB_D23 一一连接 U6 D0-D23，并同时连接 RGB_DE、RGB_IDCK、RGB_HSYNC、RGB_VSYNC。

- 参数与网络：`data_width=24`；`data=RGB_D0-RGB_D23`；`pixel_clock=RGB_IDCK`；`data_enable=RGB_DE`；`sync=RGB_HSYNC/RGB_VSYNC`；`source=U1 FPGA`；`destination=U6 LT8618SXB`
- 证据：图 c8856f121743 / 第 1 页 / FPGA RGB nets; 图 ec61131032b6 / 第 1 页 / U6 pins D0-D23/DE/IDCK/HSYNC/VSYNC

### LT8618 控制 I2C

BUS_CSCL/BUS_CSDA 经 R19/R21 1 kΩ 串联成为 LT_CSCL/LT_CSDA，并由 4.7 kΩ 电阻上拉到 VCC_3V3 后连接 U6 CSCK/CSDA。

- 参数与网络：`controller=external M5Stack host`；`device=U6 LT8618SXB`；`scl=BUS_CSCL -> R19 1KΩ -> LT_CSCL -> U6 pin34`；`sda=BUS_CSDA -> R21 1KΩ -> LT_CSDA -> U6 pin35`；`pullups=4.7KΩ to VCC_3V3`；`level=3.3V`
- 证据：图 43cbb9ce0587 / 第 1 页 / A1，LT_CSCL/LT_CSDA to BUS_CSCL/BUS_CSDA; 图 ec61131032b6 / 第 1 页 / U6 CSCK/CSDA pullups

## 总线地址

### LT8618SXB I2C 地址

U6 CI2CA pin32 由 R35 0 Ω 下拉到 GND，R34 上拉位 DNP；页面地址表规定 0-400 mV 对应 0x72，因此本板地址为 0x72。

- 参数与网络：`device=U6 LT8618SXB`；`address=0x72`；`strap_pin=CI2CA pin32`；`pulldown=R35 0Ω`；`pullup=R34 DNP`；`strap_voltage=GND/0V`
- 证据：图 ec61131032b6 / 第 1 页 / 右上 LT_CI2CA R34/R35 与 CI2CA I2C address 表

## GPIO 与控制信号

### FPGA 启动模式

GW_MODE1 与 GW_MODE0 分别由 R7/R8 4.7 kΩ 下拉到 GND，页面标注 BOOT[1:0]=00 AUTO BOOT；GW_JTRSEL 的 R1 为 DNP。

- 参数与网络：`mode1=R7 4.7KΩ to GND`；`mode0=R8 4.7KΩ to GND`；`boot=BOOT[1:0]=00 AUTO BOOT`；`jtrsel=R1 DNP`
- 证据：图 c8856f121743 / 第 1 页 / C2 FPGA_CFG block

## 时钟

### FPGA 与 TMDS 时钟

X1 为 74.250 MHz 有源振荡器，经 R3 22 Ω 输出 TMDS_CLK_IN；X2 为 50 MHz 有源振荡器，经 R4 22 Ω 输出 FPGA_CLK_IN。

- 参数与网络：`x1=YSO690PR 74.250MHz 3225 3.3V`；`x1_net=TMDS_CLK_IN`；`x1_series=R3 22Ω`；`x2=YSO690PR 50MHz 3225 3.3V`；`x2_net=FPGA_CLK_IN`；`x2_series=R4 22Ω`
- 证据：图 c8856f121743 / 第 1 页 / C1-C2 FPGA_CLK block

## 保护电路

### HDMI 保护与供电

U4/U5 PESDALC10N5VU 保护四对 TMDS；D22/D23/D25 ESD5Z3.3C 保护 DDC/HPD；HDMI pin18 的 5 V 经 FUSE1 0.5A/6V Poly，DDC 由 R25/R26 2.2 kΩ 上拉到 VCC_3V3。

- 参数与网络：`tmds_esd=U4/U5 PESDALC10N5VU`；`ddc_hpd_esd=D22/D23/D25 ESD5Z3.3C`；`5v_fuse=FUSE1 0.5A/6V Poly`；`ddc_pullups=R25/R26 2.2KΩ to VCC_3V3`；`hpd_filter=R29 1KΩ; C34 100nF; C35 4.7uF; R30 DNP`
- 证据：图 43cbb9ce0587 / 第 1 页 / A2-C4 HDMI_ESD/HDMI_CON blocks

## 音频

### FPGA 至 LT8618SXB I2S

I2S_I_SCK、I2S_I_WS、I2S_I_SDO、I2S_I_MCLK 从 FPGA BANK1 连接 U6 SCLK、WS、SD0、MCLK；U6 SPDIF pin5 未连接。

- 参数与网络：`source=U1 FPGA`；`destination=U6`；`bit_clock=I2S_I_SCK`；`word_select=I2S_I_WS`；`data=I2S_I_SDO`；`master_clock=I2S_I_MCLK`；`spdif=U6 pin5 NC`
- 证据：图 c8856f121743 / 第 1 页 / U1A I2S nets pins74-77; 图 ec61131032b6 / 第 1 页 / U6 SCLK/WS/SD0/MCLK/SPDIF

## 调试与烧录

### FPGA JTAG/配置

BUS_CS/TMS、BUS_SCK/TCK、BUS_MOSI/TDI、BUS_MISO/TDO 经 22 Ω 电阻连接 FPGA JTAG TMS/TCK/TDI/TDO，并引到 J2 IDC2X5；FPGA SPI MOSI/MISO/CS/SCK 另有预留 JP1，JP1 标为不装。

- 参数与网络：`tms=BUS_CS/TMS`；`tck=BUS_SCK/TCK`；`tdi=BUS_MOSI/TDI`；`tdo=BUS_MISO/TDO`；`connector=J2 IDC2X5`；`series=22Ω`；`spi_header=JP1 DNP`
- 证据：图 43cbb9ce0587 / 第 1 页 / A1 JTAG resistors/JP1 与 C1-C2 J2; 图 c8856f121743 / 第 1 页 / U1C JTAG/FPGA SPI pins

## 参数与信号索引

| 分类 | 对象 | 参数 |
| --- | --- | --- |
| 系统结构 | 高清音视频输出架构 | `host=BUS1 M5BUS`；`fpga=U1 GW1NR-9/SDRAM`；`bridge=U6 LT8618SXB`；`video=RGB D0-D23/DE/IDCK/HSYNC/VSYNC`；`audio=I2S SCK/WS/SDO/MCLK`；`output=HDMI1` |
| 核心器件 | FPGA 信号分区 | `reference=U1`；`marking=GW1NR-9/SDRAM`；`rgb=D0-D23 plus HSYNC/VSYNC/DE/IDCK`；`audio=I2S_I_SCK/WS/SDO/MCLK`；`configuration=FPGA_SPI_MOSI/MISO/CS/SCK`；`jtag=TMS/TCK/TDI/TDO` |
| 总线 | 24-bit RGB 视频总线 | `data_width=24`；`data=RGB_D0-RGB_D23`；`pixel_clock=RGB_IDCK`；`data_enable=RGB_DE`；`sync=RGB_HSYNC/RGB_VSYNC`；`source=U1 FPGA`；`destination=U6 LT8618SXB` |
| 音频 | FPGA 至 LT8618SXB I2S | `source=U1 FPGA`；`destination=U6`；`bit_clock=I2S_I_SCK`；`word_select=I2S_I_WS`；`data=I2S_I_SDO`；`master_clock=I2S_I_MCLK`；`spdif=U6 pin5 NC` |
| 总线地址 | LT8618SXB I2C 地址 | `device=U6 LT8618SXB`；`address=0x72`；`strap_pin=CI2CA pin32`；`pulldown=R35 0Ω`；`pullup=R34 DNP`；`strap_voltage=GND/0V` |
| 总线 | LT8618 控制 I2C | `controller=external M5Stack host`；`device=U6 LT8618SXB`；`scl=BUS_CSCL -> R19 1KΩ -> LT_CSCL -> U6 pin34`；`sda=BUS_CSDA -> R21 1KΩ -> LT_CSDA -> U6 pin35`；`pullups=4.7KΩ to VCC_3V3`；`level=3.3V` |
| 时钟 | FPGA 与 TMDS 时钟 | `x1=YSO690PR 74.250MHz 3225 3.3V`；`x1_net=TMDS_CLK_IN`；`x1_series=R3 22Ω`；`x2=YSO690PR 50MHz 3225 3.3V`；`x2_net=FPGA_CLK_IN`；`x2_series=R4 22Ω` |
| 调试与烧录 | FPGA JTAG/配置 | `tms=BUS_CS/TMS`；`tck=BUS_SCK/TCK`；`tdi=BUS_MOSI/TDI`；`tdo=BUS_MISO/TDO`；`connector=J2 IDC2X5`；`series=22Ω`；`spi_header=JP1 DNP` |
| GPIO 与控制信号 | FPGA 启动模式 | `mode1=R7 4.7KΩ to GND`；`mode0=R8 4.7KΩ to GND`；`boot=BOOT[1:0]=00 AUTO BOOT`；`jtrsel=R1 DNP` |
| 电源 | 外部输入与 5 V 主电源 | `connector=J1 DC_050`；`input=VCC_EXT`；`switch=S1 SS-12F23/Pwr_EN`；`converter=U7 SY8303A`；`inductor=L2 6.8uH`；`setpoint=5.27V`；`frequency=666kHz`；`diode=D1 SS34`；`output=VBUS_5V` |
| 电源 | FPGA/LT8618 次级电源 | `1v2=U2 SY8089A / TP2`；`3v3=U8 SY8089A / TP4`；`1v8=U3 LP5907MFX-1.8 / TP3`；`input=VCC_5V` |
| 接口 | M5-Bus 使用引脚 | `power=pin3 VBUS_5V; pin19 VHost_3V3`；`i2c=pin13 BUS_CSCL; pin14 BUS_CSDA`；`jtag_spi=BUS_CS/TMS; BUS_SCK/TCK; BUS_MISO/TDO; BUS_MOSI/TDI`；`i2s_gpio=BUS_G0/G5/G12/G15/G16/G17/G25/G26`；`ground=pins26/28/30 plus lower ground` |
| 接口 | HDMI 输出连接 | `tmps_pairs=TX2 pins1/3; TX1 pins4/6; TX0 pins7/9; TXC pins10/12`；`ddc=pin15 SCL HDMI_DCLK; pin16 SDA HDMI_DSDA`；`hpd=pin19 HDMI_HPD`；`5v=pin18 VCC_5V`；`cec=pin13 NC`；`shield=GND` |
| 保护电路 | HDMI 保护与供电 | `tmds_esd=U4/U5 PESDALC10N5VU`；`ddc_hpd_esd=D22/D23/D25 ESD5Z3.3C`；`5v_fuse=FUSE1 0.5A/6V Poly`；`ddc_pullups=R25/R26 2.2KΩ to VCC_3V3`；`hpd_filter=R29 1KΩ; C34 100nF; C35 4.7uF; R30 DNP` |
| 核心器件 | LT8616SXB/LT8618SXB 型号与地址差异 | `document_model=LT8616SXB`；`document_address=0x39`；`schematic_model=LT8618SXB`；`schematic_address=0x72` |
| 核心器件 | FPGA 完整订货型号 | `document_model=GW1NR-LV9QN88C6-I5`；`schematic_marking=GW1NR-9/SDRAM`；`full_order_code=not printed` |
| 电源 | 外部输入范围冲突 | `document_range=9-24V`；`schematic_range=5-24V`；`connector=J1 DC_050` |
| 其他事实 | 1080P 与八通道音频能力 | `confirmed_wiring=24-bit RGB; I2S SCK/WS/SDO/MCLK`；`claimed_resolution=1920x1080`；`claimed_audio_channels=8`；`timing_table=not printed` |

## 待确认事项

- `component.bridge-discrepancy`：产品正文写 LT8616SXB @ 0x39，但正式原理图明确标 U6 LT8618SXB，并以 CI2CA=GND 配置为 0x72；需确认量产 BOM 与软件目标。（证据：图 ec61131032b6 / 第 1 页 / U6 LT8618SXB 与 CI2CA 地址表）
- `component.fpga-variant`：产品正文给出 GW1NR-LV9QN88C6-I5，原理图器件标记仅为 GW1NR-9/SDRAM，无法从页面确认封装、速度等级和温度等级后缀。（证据：图 c8856f121743 / 第 1 页 / U1A/U1B/U1C GW1NR-9/SDRAM）
- `power.input-range`：产品正文给出 9-24 V 输入，而原理图在 J1 旁标 Ext_VIN_5-24V；实际允许的最低输入电压需要确认。（证据：图 43cbb9ce0587 / 第 1 页 / J1 DC_050 下方 Ext_VIN_5-24V）
- `other.performance`：原理图确认 24-bit RGB 和一组 I2S 数据链路，但未直接标注最大 1920x1080 分辨率或最多 8 通道音频的时序/采样条件。（证据：图 c8856f121743 / 第 1 页 / FPGA RGB/I2S nets; 图 ec61131032b6 / 第 1 页 / U6 RGB/I2S inputs）
- `review.bridge-discrepancy`：请用 M126 量产 BOM、丝印和驱动代码确认实际桥接芯片及 I2C 地址是 LT8618SXB/0x72 还是正文所列 LT8616SXB/0x39。；原因：正式原理图与产品正文直接冲突。
- `review.fpga-variant`：请用 FPGA 顶部标记或 BOM 确认 GW1NR-LV9QN88C6-I5 完整订货型号。；原因：原理图只写 GW1NR-9/SDRAM。
- `review.input-range`：请用 SY8303A 设计计算和模块测试规范确认最低输入为 5 V 还是 9 V。；原因：正文与原理图输入范围不一致。
- `review.performance`：请用 FPGA bitstream、LT8618SXB 配置和实测确认 1080P 最大时序及 8 通道音频支持条件。；原因：这些能力未在原理图中直接量化。

## 原理图来源

| 资源 | 页码 | SHA-256 | 原始地址 |
| --- | --- | --- | --- |
| 1 | 1 | `8f1bf8a1ccc6905c9dc664c556ad0cf8ee2014b9b467f211923a3557bdf7eb93` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/553/Display_Module_13.2_sch_01.png` |
| 2 | 1 | `c8856f12174390c2c105c0ec922a97802b369f407a43531eb6a8371ecc05df30` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/553/Display_Module_13.2_sch_02.png` |
| 3 | 1 | `ec61131032b6c5f1488ceb49c29ef338a46a559ce924ccfdceaea67f32b204b5` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/553/Display_Module_13.2_sch_03.png` |
| 4 | 1 | `43cbb9ce0587243bcf0a085f6514e0f436d05873594905dc5e5eef1ec4bd79a1` | `https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/553/Display_Module_13.2_sch_04.png` |

---

源文档：`zh_CN/module/Display Module 13.2.md`

源文档 SHA-256：`2cb69b1f1173e63d7d809d1f5d08b932a448aec5a390175a823c6b7fed0db3ea`

*该文档由专用原理图子智能体基于原理图证据自动生成；无法确认的内容集中列在“待确认事项”章节。*
