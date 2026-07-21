# StamPLC AC

<span class="product-sku">SKU:A160</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160_StamPLC-AC-main-pictures_12.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160-weight.jpg">
</PictureViewer>

## 描述

StamPLC AC 是一款适配 StamPLC 主机的交流继电器拓展模块。模块集成交流负载控制与整机供电功能，有效简化应用供电布线。采用触点式继电器（单刀单掷 - 常开型）, 最大支持 AC 240V@10A 线路通断。内置 AC-DC 隔离转换电路，支持 AC 100~240V 输入，可在为继电器负载供电的同时，降压输出 DC 12V 为整机供电。板载可编程三色 LED 灯，用于工作状态指示。StamPLC 主控通过 I2C 协议的 IO 拓展芯片对继电器、RGB LED 进行编程控制，有效节省 IO 资源。适用于交流负载设备开关、电磁阀控制等工业级应用场景。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/projects/stamplc/stamplc_ac) | 本教程介绍如何通过 Arduino IDE 编程控制 StamPLC AC。|

## 产品特性

- 集成供电与控制一体，简化布线
- 触点式继电器
- 内置 AC-DC 隔离转换电路，支持 AC 100 ~ 240V 宽电压输入
- 可编程三色 LED 状态指示
- I2C 协议控制
- DIN 导轨安装 / 挂孔安装
- 开发平台
  - Arduino
  - UiFlow2

## 包装内容

- 1 x StamPLC AC
- 2 x 固定连接件

## 应用场景

- 交流或直流负载开 / 关控制
- 电磁阀控制
- 工业设备远程通断

## 规格参数

| 规格           | 参数                                                                         |
| -------------- | ---------------------------------------------------------------------------- |
| AC-DC 转换模块 | 内置 AC-DC 隔离转换电路（WCAL12-S12CA）<br>输出功率：DC 12V@1A（12W）        |
| 继电器         | HF3FF/005-1HTF，1 路交流继电器                                               |
| 绝缘电阻       | 100MΩ（DC 500V）                                                             |
| 触点规格       | 容量：AC 240V@10A<br>寿命：≥100,000 次（AC 阻性负载）<br>耐压：AC 1500V 1min |
| 动作时间       | ≤ 10ms                                                                       |
| 释放时间       | ≤ 5ms                                                                        |
| 接口类型       | 2 × 8P 2.54mm 排针 / 排母，KF128-2P 5.0mm                                    |
| 输入电压       | AC 100 ~ 240V                                                                |
| IO 扩展芯片    | PI4IOE5V6408 I2C@0x44                                                        |
| RGB LED        | 1 × NH-B2020RGBA-HF                                                          |
| 安装方式       | DIN 导轨安装 / 挂孔                                                          |
| 产品尺寸       | 80.5 x 50.5 x 27.1mm                                                         |
| 产品重量       | 73.6g                                                                        |
| 包装尺寸       | 82.0 x 60.0 x 28.0mm                                                         |
| 毛重           | 80.9g                                                                        |

## 操作说明

!> 供电说明 | 使用 StamPLC AC 的输入电源为整机供电时，AD-DC 电路将固定降压至 DC 12V 为整机供电，此时在 StamPLC 侧请勿连接除 DC 12V 以外的电源同时供电，否则可能导致设备损坏。

### StamPLC 与 StamPLC AC 连接示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/stamplc_ac_connect.png" width="70%">

## 原理图

- [StamPLC AC 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/SCH_StamPLC_AC_SCH_Main_B0.5_2025_10_24_19_41_42.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/SCH_StamPLC_AC_SCH_Main_B0.5_2025_10_24_19_41_42_page_01.png">
</SchViewer>

## 管脚映射

### IO 扩展芯片

| PI4IOE5V6408 (0x44) | P2     | P5       | P6       | P7       | SCL | SDA |
| ------------------- | ------ | -------- | -------- | -------- | --- | --- |
| StamPLC AC          | REL_EN | SYS_LEDR | SYS_LEDG | SYS_LEDB |     |     |
| StamPLC             |        |          |          |          | G15 | G13 |

### StamPLC-Bus

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN    |
| ------- | ---- | ----- | ------ |
| VIN     | 1    | 2     | GND    |
| GND     | 3    | 4     | GND    |
| GND     | 5    | 6     | EXT_5V |
| SCL     | 7    | 8     | SDA    |
| PHY_RST | 9    | 10    |        |
|         | 11   | 12    |        |
|         | 13   | 14    |        |
|         | 15   | 16    |        |
::

## 尺寸图

- [StamPLC AC 尺寸图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/stamplc-ac.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/stamplc-ac_page_01.png">

## 结构文件

- [StamPLC AC 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/A160_StamPLC_AC/Structures)

## 数据手册

- [PI4IOE5V6408](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1129/PI4IOE5V6408.pdf)

## 软件开发

### Arduino

- [StamPLC AC Arduino 快速上手](/zh_CN/arduino/projects/stamplc/stamplc_ac)
- [StamPLC AC Arduino 案例程序](https://github.com/m5stack/M5StamPLC/tree/main/examples/Modules/StamPLC_AC)

### UiFlow2

- [StamPLC AC UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/stamplc/ac.html)

### Home Assistant

- [StampPLC AC Home Assistant 集成](/zh_CN/homeassistant/kit/stamplc#stamplc%20ac)

## 相关视频

- StamPLC AC 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1187/A160-StamPLC-AC-video-ZH.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115705848531370&bvid=BV1dbmEBwE33&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/4Jei3vaaSh8?si=kFDpiXaKSUkDG8pP" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
