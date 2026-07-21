# Dial v1.1

<span class="product-sku">SKU:K130-V11</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_V11_Weight.jpg">
</PictureViewer>

## 描述

**Dial v1.1** 是一款高性能、多功能的嵌入式开发板，在原有产品 Dial 的基础上实现了全面升级。新版产品采用全新的 **Stamp-S3A** 主控，进一步提升系统处理能力和稳定性；同时，对核心模组天线和按键进行了优化，有效增强了无线通信性能和用户操作体验。产品配置 **1.28 寸** 圆形 TFT 触摸屏与高精度旋转编码器，并内置 **RFID** 检测模块，RTC 电路，板载**蜂鸣器**以及**屏下按键**，实现设备互动和提醒唤醒功能。供电方案支持 **DC 6 ～ 36V** 宽电压直流输入，并预留锂电池接口及**充电**电路，以满足多样化应用需求。此外，预留的 PORT.A 和 PORT.B 接口便于扩展 I2C 和 GPIO 设备。该产品适用于智能家居控制、物联网应用、智能穿戴、门禁系统、工业控制及教育创客等领域。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5dial/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Dial v1.1 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5dial/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Dial v1.1 设备。 |

## 产品特性

- 圆形 TFT 触摸屏
- Stamp-S3A 作为主控
- 旋转编码器
- RFID 检测模块
- 宽电压输入
- 接口扩展：预留的 PORT.A 和 PORT.B 接口
- 开发平台
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Dial V1.1
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)
- 1 x 2.54-2P 端子

## 应用场景

- 智能家居控制
- 物联网项目
- 门禁系统
- 工业控制

## 规格参数

| 规格           | 参数                                                               |
| -------------- | ------------------------------------------------------------------ |
| SoC            | ESP32-S3FN8@Xtensa LX7 双核，主频 240MHz                           |
| USB            | USB OTG, USB Serial/JTAG                                           |
| Flash          | 8MB                                                                |
| Wi-Fi          | 2.4 GHz Wi-Fi                                                      |
| 宽电压输入范围 | DC 6~36V                                                           |
| 屏幕驱动       | GC9A01<br/>1.28 Inch 240 x 240px                                   |
| 触摸驱动       | FT3267                                                             |
| RFID           | WS1850S @标签工作频率: 13.56 MHz ,ISO/IEC 14443 Type A/Type B 协议 |
| 编码器         | 分辨率：16 定位，64 脉冲 / 圈                                      |
| 蜂鸣器         | 80dB                                                               |
| 电池座子规格   | 1.25mm-2P                                                          |
| 休眠电流       | USB 供电：DC 5V@6.84mA (LDO 占用功耗)<br/>仅电池供电：DC 4V@6uA    |
| 工作电流       | USB 供电：DC 5V@88.19mA<br/>仅电池供电：DC 4V@100mA                |
| 电源接口规格   | 型号 KF2EDGV-2.54-2P，直针设计，2.54mm 间距（2Pin），绿色          |
| 工作温度       | 0 ~ 40°C                                                           |
| 产品尺寸       | 51.0 x 51.0 x 32.3mm                                               |
| 产品重量       | 46.2g                                                              |
| 包装尺寸       | 71.9 x 71.9 x 57.4mm                                               |
| 毛重           | 61.0g                                                              |

## 操作说明

### 开关机操作

- 开机：在无 USB 外部供电（仅电池供电）时，可通过按 “WAKE” 按钮或由 RTC 定时触发的 IRQ 信号进行唤醒启动，完成唤醒后需在程序初始化中将 HOLD (GPIO46) 引脚设为高电平 (1) 以维持电源，否则设备将重新进入休眠状态。
- 关机：同样在无 USB 外部供电（仅电池供电）时，可按下 RST 按键直接关机，或在程序中将 HOLD (GPIO46) 引脚设为低电平 (0) 实现断电关机。

### 进入下载模式

如果要进入下载模式，请在开机前按住 Stamp-S3A 上的 G0 按键，通电之后再松开。<br/><img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/dial%20(2).gif" width="30%" />

### Dial v1.1 锂电池拓展接口

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/M5PPT.png" width="100%" />

### RFID 卡片

如果 RFID 标签的尺寸小于 Dial 的外轮廓，很可能无法识别或通信异常，建议使用标准银行卡大小的 RFID 卡片。

## 原理图

- [Dial v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/499/Sch_M5Dial.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/499/Sch_M5Dial_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/499/Sch_M5Dial_sch_02.png">
</SchViewer>

## 管脚映射

### I2C Sensor (RTC8563 & WS1850S)

| ESP32-S3      | G12 | G11 | G8  | G10 | G3   |
| ------------- | --- | --- | --- | --- | ---- |
| RTC8563       | SCL | SDA |     |     |      |
| WS1850S(RFID) | SCL | SDA | RST | IRQ |      |
| Buzzer        |     |     |     |     | beep |

### ENCODER

| ESP32-S3 | G40 | G41 | VCC | GND |
| -------- | --- | --- | --- | --- |
| ENCODER  | B   | A   | 5V  | GND |

### Screen Driver (GC9A01-SPI) & Touch Driver

| ESP32-S3 | G4     | G5       | G6      | G7     | G8        | G9     | G11    | G12    | G14    |
| -------- | ------ | -------- | ------- | ------ | --------- | ------ | ------ | ------ | ------ |
| GC9A01   | LCD_RS | LCD_MOSI | LCD_SCK | LCD_CS | LCD_RESET | LCD_BL |        |        |        |
| FT3267   |        |          |         |        |           |        | TP_SDA | TP_SCL | TP_INT |

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | G13    | G15   |
| PORT.B   | GND   | 5V  | G2     | G1    |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Dial/img-4739e0cc-227a-4f6b-9956-48915212e9c8.png" width="100%" />

## 结构文件

- [Dial v1.1 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K130_Dial/Structures)

## 数据手册

- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [WS1850S](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/WS1850S.PDF)
- [DC 电源端子规格](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/DB2EK-2.54-2P-GN-S%202.54mm%202Pin%20Green.pdf)
- [锂电池座子](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/1.25WT-2P.pdf)

## 软件开发

### Arduino

- [Dial v1.1 Arduino 快速上手](/zh_CN/arduino/m5dial/program)
- [Dial v1.1 Arduino 驱动库](https://github.com/m5stack/M5Dial)

### UiFlow2

- [Dial v1.1 UiFlow2 快速上手](/zh_CN/uiflow2/m5dial/program)

### Easyloader

| Easyloader                           | 下载链接                                                                                                                    | 备注 |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- | ---- |
| Dial v1.1 User Demo Easyloader       | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/M5dial%20Factory%20Demo.exe)     | /    |
| Dial v1.1 Knob Panel Demo Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/M5dial%20Smart%20Home%20GUI.exe) | /    |

### ESP-IDF

- [Dial v1.1 出厂固件](https://github.com/m5stack/M5Dial-UserDemo)
- [Espressif's Board Support Packages - M5Dial](https://github.com/espressif/esp-bsp/tree/master/bsp/m5dial)
- [Dial v1.1 Knob Panel Demo](https://github.com/Gitshaoxiang/M5Dial-Gui-Demo)

## 相关视频

- Dial v1.1 产品展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/0906%20M5%E4%BA%A7%E5%93%81%E4%BB%8B%E7%BB%8D%E7%89%87.m4v" type="video/mp4"></video>

- Dial v1.1 产品介绍与案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/M5%20DIAL%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113009179558517&bvid=BV129WUeeEJP&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/UlVJe4v8cd4?si=q9zUgyJB4k5K_LXg" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比项             | [Dial v1.1](/zh_CN/core/M5Dial%20V1.1)<br/>![Dial v1.1](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/K130_v11_01.webp) | [Dial](/zh_CN/core/M5Dial)<br/>![Dial](https://static-cdn.m5stack.com/resource/docs/products/core/M5Dial/img-2afd549e-8af8-47b4-823a-e90e063a0139.webp) |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 核心模组               | Stamp-S3A                                                                                                                       | StampS3                                                                                                                                                 |
| 天线设计               | 优化设计，信号更强                                                                                                              | 常规设计                                                                                                                                                |
| StampS3 模组 Boot 按键 | 优化按键手感，按键采用 4.0 x 3.0 x 2.0mm 规格                                                                                   | 按键规格 2.6 x 1.6 x 0.55mm                                                                                                                             |
| 功耗表现               | 经过优化，实现更低功耗                                                                                                          | 常规设计                                                                                                                                                |
::
