# Dial

<span class="product-sku">SKU:K130</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Dial/img-2afd549e-8af8-47b4-823a-e90e063a0139.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Dial/img-d99f4115-0a49-4a2e-8637-2c2214830959.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Dial/img-0166bf2f-d338-4041-8141-b92579cd11d9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Dial/img-25a09e85-7d7b-4f34-abab-c8fa97f55b8f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Dial/img-1091d85e-5192-4202-8033-349ec6d99b15.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Dial/img-cca1e0fc-a495-491b-b546-af72f218938c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Dial/img-c54d138e-1d49-4e20-8aa0-ed0998301a99.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Dial/img-6615b008-a565-44c8-b639-f4ee903f7cd2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5Dial/img-375c0fa8-b1ab-4e7f-89f5-f67dacc77a65.webp">
</PictureViewer>

## 描述

**Dial** 是一款多功能的嵌入式开发板，配备 **1.28 寸**圆形 TFT 触摸屏，以 **StampS3** 为主控，内置旋转编码器，可精确记录旋钮位置。此外，板载 RFID 检测模块，RTC 电路，板载蜂鸣器以及屏下按键用于设备互动和提醒唤醒等功能。供电方面，产品设计支持宽电压 6 ~ 36V 直流电输入，并预留了锂电池接口和充电电路，以提供不同需求。此外，预留的 PORT.A 和 PORT.B 接口可方便扩展 I2C 和 GPIO 设备。该产品适用于智能家居控制、物联网项目、智能穿戴、门禁、工业控制和教育创客项目等领域。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/m5dial/program) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Dial 设备。 |

learn>| ![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png) | [UiFlow2](/zh_CN/uiflow2/m5dial/program) | 本教程将向你介绍，如何通过 UiFlow2 图形化编程平台控制 Dial 设备。 |

## 产品特性

- 圆形 TFT 触摸屏
- Stamp-S3 作为主控
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

- 1 x Dial
- 1 x M2 内六角扳手
- 1 x 2.54-2P 端子

## 应用场景

- 智能家居控制
- 物联网项目
- 门禁系统
- 工业控制

## 规格参数

| 规格                          | 参数                                                                                    |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| SoC                           | ESP32-S3FN8@Xtensa LX7 双核，主频 240MHz, 支持 OTG/CDC 功能                             |
| Flash                         | 8MB                                                                                     |
| Wi-Fi                         | 2.4 GHz Wi-Fi                                                                           |
| 设备供电                      | USB Type-C DC 5V <br> 背部供电端子 DC 6 ~ 36V <br> 电池供电 DC 3.7V                     |
| 屏幕驱动                      | GC9A01<br/>1.28 Inch 240x240px                                                          |
| 触摸驱动                      | FT3267                                                                                  |
| RFID                          | WS1850S @标签工作频率: 13.56 MHz ,ISO/IEC 14443 Type A/Type B 协议                      |
| 编码器                        | 分辨率：16 定位，64 脉冲 / 圈                                                           |
| 蜂鸣器                        | 80dB                                                                                    |
| 电池座子规格                  | 1.25mm-2P                                                                               |
| 休眠电流 (电池供电的休眠电流) | DC 4.2V@1.9uA                                                                           |
| 工作电流（背部供电端子）      | DC 6V 供电 :DC 6V@140.6mA<br/>DC 12V 供电：DC 12V@82.5mA<br/>DC 36V 供电：DC 36V@28.1mA |
| 工作温度                      | 0-40°C                                                                                  |
| 电源接口规格                  | 型号 KF2EDGV-2.54-2P，直针设计，2.54mm 间距（2Pin），绿色                               |
| 产品尺寸                      | 51.0 x 51.0 x 32.3mm                                                                    |
| 产品重量                      | 46.3g                                                                                   |
| 包装尺寸                      | 71.9 x 71.9 x 57.4mm                                                                    |
| 毛重                          | 61.4g                                                                                   |

## 操作说明

### 开关机操作

- 开机：可通过按 "WAKE" 按钮，以及 RTC 定时触发的 IRQ 信号进行唤醒启动，在完成触发唤醒信号后，在程序初始化中需要设置 hold (G46) 引脚为高电平 (1) 对电源进行维持，否则设备将重新进入休眠状态。
- 关机：在无 USB 外部供电时，按 RST 按键实现，或者无 USB 外部供电时，在程序运行中设置 HOLD (GPIO46)=0，即实现断电关机。

### 进入下载模式

如果要进入下载模式，请在开机前按住 StampS3 上的 G0 按键，通电之后再松开。<br/><img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/dial%20(2).gif" width="30%" />

### Dial 锂电池拓展接口

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/M5PPT.png" width="100%" />

### RFID 卡片

如果 RFID 标签的尺寸小于 Dial 的外轮廓，很可能无法识别或通信异常，建议使用标准银行卡大小的 RFID 卡片。

## 原理图

- [Dial 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/499/Sch_M5Dial.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/499/Sch_M5Dial_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/499/Sch_M5Dial_sch_02.png">
</SchViewer>

## 管脚映射

### I2C Sensor (RTC8563 & WS1850S)

| ESP32-S3             | G12 | G11 | G8  | G10 | G3   |
| -------------------- | --- | --- | --- | --- | ---- |
| RTC8563 (0x51)       | SCL | SDA |     |     |      |
| WS1850S(RFID) (0x28) | SCL | SDA | RST | IRQ |      |
| Buzzer               |     |     |     |     | beep |

### ENCODER

| ESP32-S3 | G40 | G41 | VCC | GND |
| -------- | --- | --- | --- | --- |
| ENCODER  | B   | A   | 5V  | GND |

### Screen Driver (GC9A01-SPI) & Touch Driver

| ESP32-S3      | G4     | G5       | G6      | G7     | G8        | G9     | G11    | G12    | G14    |
| ------------- | ------ | -------- | ------- | ------ | --------- | ------ | ------ | ------ | ------ |
| GC9A01        | LCD_RS | LCD_MOSI | LCD_SCK | LCD_CS | LCD_RESET | LCD_BL |        |        |        |
| FT3267 (0x38) |        |          |         |        |           |        | TP_SDA | TP_SCL | TP_INT |

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

- [Dial 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/K130_Dial/Structures)

## 数据手册

- [BM8563](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/BM8563_V1.1_cn.pdf)
- [WS1850S](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/WS1850S.PDF)
- [DC 电源端子规格](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/DB2EK-2.54-2P-GN-S%202.54mm%202Pin%20Green.pdf)
- [锂电池座子](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/1.25WT-2P.pdf)

## 软件开发

### Arduino

- [Dial Arduino 快速上手](/zh_CN/arduino/m5dial/program)
- [Dial Arduino 驱动库](https://github.com/m5stack/M5Dial)

### UiFlow2

- [Dial UiFlow2 快速上手](/zh_CN/uiflow2/m5dial/program)

### Easyloader

| Easyloader                      | 下载链接                                                                                                                    | 备注 |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---- |
| Dial User Demo Easyloader       | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/M5dial%20Factory%20Demo.exe)     | /    |
| Dial Knob Panel Demo Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/M5dial%20Smart%20Home%20GUI.exe) | /    |

### ESP-IDF

- [Espressif's Board Support Packages - M5Dial](https://github.com/espressif/esp-bsp/tree/master/bsp/m5dial)
- [Dial 出厂固件](https://github.com/m5stack/M5Dial-UserDemo)
- [Dial Knob Panel Demo](https://github.com/Gitshaoxiang/M5Dial-Gui-Demo)

## 相关视频

- Dial 相关介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5Dial/0906%20M5%E4%BA%A7%E5%93%81%E4%BB%8B%E7%BB%8D%E7%89%87.m4v" type="video/mp4"></video>

- Dial Demo

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
