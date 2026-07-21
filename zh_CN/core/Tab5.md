# Tab5

<span class="product-sku">SKU:C145/K145</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/K145_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/K145_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_13.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_K145_Weight.jpg">
</PictureViewer>

## 描述

**Tab5** 是一款面向开发者的高度可扩展便携式智能物联网终端开发设备，集成了双芯片架构和丰富的硬件资源。其主控采用基于 RISC‑V 架构的 **ESP32‑P4** SoC，并配备 16MB Flash 与 32MB PSRAM。无线模块则选用 ESP32-C6-MINI-1U，支持 Wi-Fi 6，其天线系统可在内置 3D 天线与外部 MMCX 天线接口之间自由切换，灵活适应不同部署环境，确保数据吞吐与低时延控制。

在视觉与交互方面，Tab5 配备 MIPI‑DSI 接口的 5″ 1280×720 IPS 触控屏幕，带来流畅灵敏的触控体验。搭载 MIPI‑CSI 接口的 SC2356 2MP **摄像头**（1600×1200），可实现高清视频录制，图像处理及边缘 AI 应用（如人脸识别、目标追踪）等。

外设接口方面，Tab5 同时具备 **USB Type‑A**（Host）和 **USB Type-C**（USB 2.0 OTG）端口，可连接鼠标、键盘等传统外设。工业场景可通过 **RS‑485**（SIT3088 + 拨码开关 120Ω 终端电阻）总线通信。HY2.0-4P，M5-Bus，GPIO_EXT 排母和 **microSD** 卡槽，以及预留 STAMP 焊盘（支持 Cat.M，NB‑IoT，LoRaWAN 等模块），可灵活扩展多种传感器和通信方案。另外还配备了 Reset/Boot 按键，用于快速复位和进入烧录模式。

音视频方面，Tab5 采用 ES8388 **音频编解码器**，配合 ES7210 AEC 回声消除前端，**双麦克风**阵列，3.5mm 耳机孔与扬声器，实现高保真录放和精准语音识别。内置 BMI270 **六轴传感器**（加速度计 + 陀螺仪，支持中断唤醒）可在运动追踪与姿态检测中主动唤醒主控，提升低功耗场景下的响应效率。

时间与电源管理方面，Tab5 集成 RX8130CE **实时时钟**（支持定时中断唤醒），底部兼容 NP‑F550 可拆卸**锂电池**，并集成 MP4560 升降压管理，IP2326 充放电与 INA226 实时**监测**电路，保证在无外部电源条件下持续稳定运行。

结构方面，Tab5 侧面预留标准 1/4″-20 三脚架安装螺母孔，可直接固定到三脚架或其他支架，便于拍摄与部署。

Tab5 可用于智能家居控制，远程监控，工业自动化，物联网原型开发及教育科研等场景，为开发者和企业提供了一个功能全面，易于扩展的高性能开发平台。

## 教程 & 快速上手

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/Tab5/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Tab5 设备。 |

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5tab5/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Tab5 设备。 |

<!--
learn>| ![Home Assistant](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1145/hhome_assistant_cover_02.jpg) | [Home Assistant](/zh_CN/homeassistant/application/tab5_ha_hmi) | 本教程提供了一个 Home Assistant 人机交互面板的范例 |-->

## 产品特性

- ESP32‑P4 双核主控
- ESP32‑C6 无线模组
- 2.4 GHz Wi-Fi 6
- 内置 3D 天线 & MMCX 外置天线端口
- 5 英寸 IPS TFT 显示屏，分辨率 1280×720（720P）
- SC2356 2MP 摄像头
- USB Type‑A Host + USB Type‑C OTG
- RS485 工业接口
- HY2.0-4P & M5-Bus 扩展
- microSD 卡槽
- Stamp 扩展
- ES8388 音频编解码
- ES7210 AEC 双麦克风
- 1W 扬声器 + 3.5mm 耳机
- BMI270 六轴传感器
- RX8130CE 实时时钟
- Reset/Boot & Power 键
- NP‑F550 可拆卸电池
- 标准 1/4″-20 三脚架安装螺母孔
- 开发平台
- - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

\#> 产品提示 | Tab5 Kit 为内置可拆卸 NP-F550 锂电池的整机套件版，而标准版 Tab5 不含电池，需要外接电源或另行购置电池使用。

### Tab5 (SKU:C145)

- 1 x Tab5
- 1 x 1.25-6P 单头端子线

### Tab5 Kit (SKU:K145)

- 1 x Tab5 Kit
- 1 x 1.25-6P 单头端子线
- 1 x NP‑F550 2000mAh 可拆卸电池

## 应用场景

- 智能家居控制
- 远程监控系统
- 物联网设备开发
- 工业自动化

## 规格参数

| 规格            | 参数                                                                                                                                          |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 主控制器 SoC    | ESP32-P4NRW32@RISC-V 32 位双核 360MHz + LP 单核 40MHz                                                                                         |
| 无线模块 SoC    | ESP32-C6-MINI-1U                                                                                                                              |
| Flash           | 16MB                                                                                                                                          |
| PSRAM           | 32MB Octal                                                                                                                                    |
| Wi-Fi           | 2.4 GHz Wi-Fi 6, Thread, Zigbee                                                                                                               |
| 天线            | 内置 3D 天线 & 2 x MMCX 外置天线端口                                                                                                          |
| 显示            | 采用 5 英寸 IPS TFT 显示屏，分辨率 1280×720（720P），搭载显示触控一体化驱动 IC：ST7123 / ST7121                                               |
| 摄像头          | SC2356 @ 2MP（1600×1200），通过 MIPI‑CSI 接口                                                                                                 |
| 音频芯片        | ES8388 编解码，ES7210 AEC 前端                                                                                                                |
| 麦克风          | 双麦克风系统（AEC 回声消除）                                                                                                                  |
| 扬声器          | 1W@8Ω NS4150B                                                                                                                                 |
| 耳机孔          | 3.5mm                                                                                                                                         |
| USB 端口        | USB Type-A（Host），USB Type-C（USB 2.0 OTG）                                                                                                 |
| RS485 端口      | SIT3088（120Ω 可切换终端电阻）<br/>供电范围: 6 ~ 24V                                                                                          |
| 扩展接口        | 1× HY2.0-4P，1× M5-Bus，GPIO_EXT 拓展总线                                                                                                     |
| 存储扩展        | microSD 卡槽                                                                                                                                  |
| 可扩展贴片接口  | Stamp 焊盘（支持 Cat.M/ NB‑IoT / LoRaWAN 等模块）                                                                                             |
| 运动传感器      | BMI270 六轴（加速度计 + 陀螺仪，支持中断唤醒）                                                                                                |
| RTC             | RTC 芯片：RX8130CE（支持定时中断唤醒），RTC 超级电容规格: 70000μF/3.3V，尺寸 Φ4.8×1.4mm                                                       |
| Reset/Boot 按键 | 1x Button，开关机及进入烧录模式                                                                                                               |
| 充电管理        | IP2326 充电管理芯片                                                                                                                           |
| 实时电源监测    | INA226（总线电流 / 电压监测）                                                                                                                 |
| 电池            | NP-F550 可拆卸锂电池，7.4V@2000mAh（14.8 Wh）                                                                                                 |
| 续航            | 在标准使用环境（屏幕亮度 50%、Wi‑Fi 常连、后台任务运行等）下，Tab5 内置电池电压从满电（8.23 V）放电至关机阈值（6.0 V），可持续运行约 6 小时。 |
| 工作温度        | 0 ~ 40°C                                                                                                                                      |
| 产品尺寸        | Tab5: 128.0 x 80.0 x 12.0mm <br/> Tab5 Kit: 128.0 x 80.0 x 26.7mm                                                                             |
| 产品重量        | Tab5: 118.4g <br/>Tab5 Kit: 217.3g<br/>电池: 98.9g                                                                                            |
| 包装尺寸        | Tab5: 148.0 x 103.0 x 21.0mm<br/>Tab5 Kit: 191.0 x 103.0 x 25.0mm                                                                             |
| 毛重            | Tab5: 161.5g<br/>Tab5 Kit: 280.5g                                                                                                             |

## 操作说明

### Tab5 供电

?>Tab5 供电注意事项 | Tab5 断开电源或更换电池前，需先执行关机操作。如直接断开电源，需间隔 5 秒后才能重新上电使用，否则可能因为电压异常原因导致 IMU 传感器无法正常初始化。

### Tab5 充电

?>Tab5 充电注意事项 | 1.Tab5 需要在设备开机初始化后才能进行充电，关机状态下无法充电。<br>2.当电池过度放电，电压低于 6V 时，电池将进入保护状态。再次充电时前，需拆下电池，并复位设备，重新安装，然后通过设备 USB Type-C 接口充电。<br>充电前期，由于电池还处于保护状态，充电芯片将以小电流的方式涓流充电，该状态下将持续数分钟，具体时长与当前电池电压水平有关。<br>待电池升压超过 6V 后，充电芯片将自动切换至正常充电模式进行充电。

### 开关机

\#> 开关机 | 在设备通过 USB 数据线或电池供电的情况下，处于关机状态时单击电源按键一次即可开机。处于开机状态时双击电源按键即可关机。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Power_On.gif" width="30%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/ShutDown.gif" width="30%">

### 下载模式

\#> 下载模式 | 在已接入 USB 数据线或电池供电的情况下，长按复位按键（约 2 秒），直至内部绿色 LED 指示灯开始快速闪烁，松开按键后，设备即进入下载模式，等待固件烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/download_mode2.gif" width="30%">

### 安装电池注意事项

\#> 安装电池 | 在设备断电状态下，先按住主板侧边的红色锁定按钮，随后将电池模块背面的金属弹片对准主板上的 “BATTERY” 卡槽，从上方向下沿导轨轻推，直到电池模块与主板完全贴合，再松开红色按钮，完成安装并开始供电。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/K145_install_battery.gif" width="30%">

### M5-Bus 总线拓展

\#> M5-Bus 总线拓展 | 如下图所示，Tab5 背部集成了 M5-Bus 总线接口，可用于拓展 Module 系列产品。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/tab5_m5_bus_extension_01.jpg" width="70%">

### IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/IMU-Tab5.jpg" width="70%">

## 原理图

- [Tab5 总体设计框图](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Tab5_Overall_Design_Block_Diagram.pdf)
- [Tab5 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Tab5_Schematics_PDF.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Tab5_Overall_Design_Block_Diagram.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/sch_tab5_b08_page_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/sch_tab5_b08_page_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/sch_tab5_b08_page_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/sch_tab5_b08_page_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/sch_tab5_b08_page_05.webp">
</SchViewer>

## 管脚映射

### CAM

| ESP32‑P4          | CAM         |
| ----------------- | ----------- |
| G32               | CAM_SCL     |
| G31               | CAM_SDA     |
| G36               | CAM_MCLK    |
| CSI_DATAP1 (专用) | CAM_D1P     |
| CSI_DATAN1 (专用) | CAM_D1N     |
| CSI_CLKP (专用)   | CAM_CSI_CKP |
| CSI_CLKN (专用)   | CAM_CSI_CKN |
| CSI_DATAP0 (专用) | CSI_DOP     |
| CSI_DATAN0 (专用) | CSI_DON     |

### ES8388

| ESP32-P4      | G30  | G27  | G26   | G29  | G32 | G31 |
| ------------- | ---- | ---- | ----- | ---- | --- | --- |
| ES8388 (0x10) | MCLK | SCLK | DSDIN | LRCK | SCL | SDA |

### ES7210

| ESP32-P4      | G30  | G27  | G28    | G29  | G32 | G31 |
| ------------- | ---- | ---- | ------ | ---- | --- | --- |
| ES7210 (0x40) | MCLK | SCLK | ASDOUT | LRCK | SCL | SDA |

### LCD

| ESP32‑P4          | ILI9881C / ST7123 / ST7121 |
| ----------------- | -------------------------- |
| G22               | LEDA                       |
| DSI_CLKN (专用)   | DSI_CK_N                   |
| DSI_CLKP (专用)   | DSI_CK_P                   |
| DSI_DATAN1 (专用) | DSI_D1_N                   |
| DSI_DATAP1 (专用) | DSI_D1_P                   |
| DSI_DATAN0 (专用) | DSI_D0_N                   |
| DSI_DATAP0 (专用) | DSI_D0_P                   |

### Touch

| ESP32‑P4                                     | G31 | G32 | G23    |
| -------------------------------------------- | --- | --- | ------ |
| GT911 (0x14) / ST7123 (0x55) / ST7121 (0x55) | SDA | SCL | TP_INT |

### BMI270 & RTC(RX8130CE) & INA226

| ESP32-P4        | G32 | G31 |
| --------------- | --- | --- |
| BMI270 (0x68)   | SCL | SDA |
| RX8130CE (0x32) | SCL | SDA |
| INA226 (0x41)   | SCL | SDA |

- 中断唤醒 (PMS150G-U06)

| PMS150G-U06   | PA6/CIN-   |
| ------------- | ---------- |
| BMI270 (0x68) | INT(E_TRG) |
| RX8130CE      | INT(E_TRG) |

### ESP32-C6

| ESP32-P4 | G11      | G10      | G9       | G8       | G13       | G12      | G15   | G14 |
| -------- | -------- | -------- | -------- | -------- | --------- | -------- | ----- | --- |
| ESP32-C6 | SDIO2_D0 | SDIO2_D1 | SDIO2_D2 | SDIO2_D3 | SDIO2_CMD | SDIO2_CK | RESET | IO2 |

### microSD

| ESP32-P4          | G39  | G40  | G41  | G42  | G43 | G44  |
| ----------------- | ---- | ---- | ---- | ---- | --- | ---- |
| microSD SPI Mode  | MISO |      |      | CS   | SCK | MOSI |
| microSD SDIO Mode | DAT0 | DAT1 | DAT2 | DAT3 | CLK | CMD  |

### RS485

| ESP32-P4 | G21 | G20 | G34 |
| -------- | --- | --- | --- |
| SIT3088  | RX  | TX  | DIR |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G53    | G54   |
::

### PI4IOE5V6408

| ESP32-P4              | G32 | G31 | CHIP_PU |
| --------------------- | --- | --- | ------- |
| PI4IOE5V6408-1 (0x43) | SCL | SDA | RST     |
| PI4IOE5V6408-2 (0x44) | SCL | SDA | RST     |

| PI4IOE5V6408-1 (0x43) | E1.P0             | E1.P1  | E1.P2    | E1.P4   | E1.P5  | E1.P6   | E1.P7  |
| --------------------- | ----------------- | ------ | -------- | ------- | ------ | ------- | ------ |
| RF_PTH_L_INT_H_EXT    | RF_INT_EXT_SWITCH |        |          |         |        |         |        |
| NS4150B               |                   | SPK_EN |          |         |        |         |        |
| EXT_5V_BUS            |                   |        | EXT5V_EN |         |        |         |        |
| LCD                   |                   |        |          | LCD_RST |        |         |        |
| TP                    |                   |        |          |         | TP_RST |         |        |
| CAM                   |                   |        |          |         |        | CAM_RST |        |
| HEADPHONE             |                   |        |          |         |        |         | HP_DET |

- RF_PTH_L_INT_H_EXT: 用于切换 Wi-Fi 使用内置天线或 SMA 外置天线。低电平时使用内置天线，高电平时使用外置天线。
- EXT_5V_BUS: 包含了 Tab5 背部 M5-Bus 总线和机身侧边 2.54-10P 拓展，以及 HY2.0-4P 接口的 5V 供电。通过 EXT5V_EN 可控制上述拓展接口电源输出。

| PI4IOE5V6408-2 (0x44) | E2.P0       | E2.P3    | E2.P4        | E2.P5      | E2.P6        | E2.P7  |
| --------------------- | ----------- | -------- | ------------ | ---------- | ------------ | ------ |
| ESP32-C6              | WLAN_PWR_EN |          |              |            |              |        |
| USB-A                 |             | USB5V_EN |              |            |              |        |
| DEVICE PWR            |             |          | PWROFF_PLUSE |            |              |        |
| IP2326 (CHARGE IC)    |             |          |              | nCHG_QC_EN | CHG_STAT_LED | CHG_EN |

- WLAN_PWR_EN: 用于开启内部 ESP32-C6 (Wi-Fi SoC) 的供电。

### M5-Bus

::m5-bus-table
| FUNC    | PIN  | LEFT | RIGHT | PIN | FUNC    |
| ------- | ---- | ---- | ----- | --- | ------- |
|         | GND  | 1    | 2     | G16 | GPIO    |
|         | GND  | 3    | 4     | G17 | PB_IN   |
|         | GND  | 5    | 6     | RST | EN      |
| MOSI    | G18  | 7    | 8     | G45 | GPIO    |
| MISO    | G19  | 9    | 10    | G52 | PB_OUT  |
| SCK     | G5   | 11   | 12    | 3V3 |         |
| RXD0    | G38  | 13   | 14    | G37 | TXD0    |
| PC_RX   | G7   | 15   | 16    | G6  | PC_TX   |
| Int SDA | G31  | 17   | 18    | G32 | Int SCL |
| GPIO    | G3   | 19   | 20    | G4  | GPIO    |
| GPIO    | G2   | 21   | 22    | G48 | GPIO    |
| GPIO    | G47  | 23   | 24    | G35 | GPIO    |
|         | HVIN | 25   | 26    | G51 | GPIO    |
|         | HVIN | 27   | 28    | 5V  |         |
|         | HVIN | 29   | 30    | BAT |         |
::

### Tab5 Board PinMap Overview

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_Pinmap_Overview.png" width="40%">

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_Model_Size_page_01.png" width="100%">

## 结构文件

- [Tab5 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/C145_Tab5/Structures)

## 数据手册

- [ESP32-P4](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/esp32-p4_datasheet_cn.pdf)
- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/app/Stamp%20Fly/BMI270.PDF)
- [ESP32-C6](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/505/esp32-c6_datasheet_cn.pdf)
- [NS4150B](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/atom/Atomic%20Echo%20Base/NS4150B.pdf)
- [ES7210](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/ES7210.PDF)
- [ES8388](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1141/ES8388.pdf)
- [INA226](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/INA226.pdf)
- [IP2326](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/IP2326.pdf)
- [NP‑F550 Battery Report](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/K145_Battery_Product_Report.zip)
- [ST7123 型号触控 IC 的接口协议文档](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/ST7123-TDDI-Interface-Protocol-V01.11.pdf.pdf)
- [ST7123 型号屏幕手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/ST7123_SPEC_Preliminary_V0.5.pdf)
- [RX8130CE 技术手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/RX8130CE_cn.pdf)
- [RX8130CE 寄存器手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/RX8130CE_cn-Register-Datasheet.pdf)

## 软件开发

<!--
### 快速上手

- [Tab5 Home Assistant HMI 案例](/zh_CN/homeassistant/application/tab5_ha_hmi)-->

### Arduino

- [Tab5 Arduino 快速上手](/zh_CN/arduino/m5tab5/program)
- [Tab5 Arduino M5Unified 驱动库](https://github.com/m5stack/M5Unified)
- [Tab5 Arduino M5GFX 驱动库](https://github.com/m5stack/M5GFX)

?> 屏幕驱动变更 | 2025 年 10 月 14 日起，Tab5 的原独立显示驱动 ILI9881C 及触控驱动 GT911，变更为 ST7123 显示触控一体式驱动，部分早期编译的固件程序将无法正常运行。 目前最新版本的 M5Unified 与 M5GFX 已对该屏幕驱动进行了兼容适配，旧程序可以使用最新版本的 M5Unified 与 M5GFX 重新编译实现兼容。<br>通过查看 Tab5 产品背部贴纸，可确认设备的驱动型号。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/K145_Note_01.png" width="40%">

### UiFlow2

- [Tab5 UiFlow2 快速上手](/zh_CN/uiflow2/Tab5/program)

### PlatformIO

```bash
[env:esp32p4_pioarduino]
platform = https://github.com/pioarduino/platform-espressif32.git#54.03.21
upload_speed = 1500000
monitor_speed = 115200
build_type = debug
framework = arduino
board = esp32-p4-evboard
board_build.mcu = esp32p4
board_build.flash_mode = qio

build_flags =
    -DBOARD_HAS_PSRAM
    -DCORE_DEBUG_LEVEL=5
    -DARDUINO_USB_CDC_ON_BOOT=1
    -DARDUINO_USB_MODE=1
lib_deps =
    https://github.com/M5Stack/M5Unified.git
    https://github.com/M5Stack/M5GFX.git
```

### ESP-IDF

- [Tab5 出厂固件源码](https://github.com/m5stack/M5Tab5-UserDemo)
- [Tab5 出厂固件编译教程](/zh_CN/esp_idf/m5tab5/userdemo)
- [Tab5 ESP-IDF BSP](https://components.espressif.com/components/espressif/m5stack_tab5/versions/1.0.0/readme)

### Easyloader

| Easyloader    | 下载链接                                                                                  | 备注 |
| ------------- | ----------------------------------------------------------------------------------------- | ---- |
| Tab5 出厂固件 | [download](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/C145_Tab5_User_Demo.exe) | /    |

### 其他

- [Tab5 恢复出厂固件教程](/zh_CN/guide/restore_factory/m5tab5)
- [Tab5 内部Wi-Fi模组恢复出厂固件](/zh_CN/guide/restore_factory/m5tab5_c6_wifi)

## 相关视频

- Tab5 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/Tab5/C145_K145_Video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114730958064676&bvid=BV1UbKtzZE3N&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/HHG4Y3nnW-o?si=ex3SUlbrge7Nev8M" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 版本变更

| 发布日期            | 产品变更                                                                                            |
|--------------------------------------------------------------------------------------------------- |--|
| 2026.4.28  | 屏幕驱动 IC 型号由 ST7123 变更为**ST7121**                                                          | 
| 2025.10.14 | Tab5 屏幕驱动方案优化：原独立显示驱动 ILI9881C 及触控驱动 GT911，变更为 ST7123 显示触控一体式驱动。 |
| 2025.5.9   | 产品首次发布                                                                                        | 
