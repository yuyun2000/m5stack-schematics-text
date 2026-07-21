# Unit MQ

<span class="product-sku">SKU:U199</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_weight.jpg">
</PictureViewer>

## 描述

**Unit MQ** 是一款基于半导体气体传感器（MQ-5）设计的可燃气体检测单元，内部集成了 MCU (STM32G030F6P6)，主要用于环境中可燃气体（如丙烷、甲烷等）的检测。该单元可通过 I2C 通信接口与各种主控设备进行通信，可获取内部参考电压、传感器电压、12 位和 8 位 ADC 原始值、固件版本、热敏电阻温度等信息。支持两种加热模式使传感器达到合适的工作温度：连续加热模式和间歇加热模式。连续加热模式下传感器可更快达到工作温度，数据响应更快；间歇加热模式下可灵活配置加热周期，优化设备功耗。本产品适用于智能家居、空气质量检测、工业安全等多种安全与监测需求应用场景。

## 产品特性

- 内置 STM32 核心主控
- I2C 通信接口
- 支持多种可燃气体（如液化气、甲烷等）检测
- 支持连续加热和可设定周期的间歇加热两种模式
- 集成热敏电阻，支持设备温度监控
- 可读取内部参考电压和传感器电压
- 标准 MQ 传感器接口，兼容多种传感器（如 MQ-2、MQ-3、MQ-7、MQ-135 等）
- 开发平台：
  - Arduino
  - UiFlow2

## 包装内容

- 1 x Unit MQ
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 智能家居
- 空气质量检测
- 工业安全

## 规格参数

| 规格                       | 参数                                                         |
| -------------------------- | ------------------------------------------------------------ |
| MCU                        | STM32G030F6P6@32 位 ARM Cortex-M0 + 处理器                   |
| 传感器                     | MQ-5 可燃气体传感器                                          |
| 通信接口                   | I2C 通信 @0x11，地址可设置                                   |
| 工作电流                   | 关闭模式：DC 5.02V@6.88mA<br>连续加热模式：DC 5.05V@188.89mA |
| 检测气体                   | 液化气、甲烷                                                 |
| 检测浓度                   | 300 ~ 10000ppm (甲烷，丙烷)                                  |
| 连续加热模式下推荐预热时间 | 20s                                                          |
| 产品尺寸                   | 64.0 x 24.0 x 25.0mm                                         |
| 产品重量                   | 19.3g                                                        |
| 包装尺寸                   | 138.0 x 93.0 x 25.0mm                                        |
| 毛重                       | 24.7g                                                        |

## 原理图

- [Unit MQ 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/UnitMQ_SCH_MAIN_V1.0_20250716_2025_07_16_11_13_24.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/UnitMQ_SCH_MAIN_V1.0_20250716_2025_07_16_11_13_24_page_01.png">
</SchViewer>

## 管脚映射

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

- [Unit MQ 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/UNIT-MQ.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/UNIT-MQ_page_01.png" width="100%">

## 结构文件

- [Unit MQ 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U199_Unit_MQ/Structures)

## 数据手册

- [MQ-5 数据手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/Gas_Sensor_MQ-5_datasheet.pdf)

## 软件开发

### Arduino

- [Unit MQ Arduino 使用教程](/zh_CN/arduino/projects/unit/unit_mq)
- [Unit MQ Arduino 驱动库](https://github.com/m5stack/M5Unit-MQ)

### UiFlow2

- [Unit MQ UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/mq.html)

### Home Assistant

- [Unit MQ Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_mq_sensor)

### 内置固件

- [Unit MQ 内置固件](https://github.com/m5stack/M5Unit-MQ-Internal-FW)

### 通讯协议

- [Unit MQ I2C 通信协议 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/MQ_I2C_Protocol_CN.pdf)

<!-- 英文版链接为：https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/MQ_I2C_Protocol_CN.pdf -->

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/MQ_I2C_Protocol_CN_page_01.png" width="100%">

<!-- 英文版链接为: https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/MQ_I2C_Protocol_EN_page_01.png -->

### 数据有效标志与各模式下控制引脚电平状态关系图示

- **关闭模式**:

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/Unit_MQ_I2C_1.png" width="70%">

- **持续加热模式**：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/Unit_MQ_I2C_2.png" width="70%">

- **间歇加热模式**（下方图 1、图 2 控制引脚高低电平时间不同，但数据有效标志均在高电平持续 20s 后生效，一旦切换为低电平就失效）：

图 1 ：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/Unit_MQ_I2C_3.png" width="70%">

图 2 ：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/Unit_MQ_I2C_4.png" width="70%">

## 相关视频

- Unit MQ 功能介绍

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1168/U199_Unit_MQ_video_zh.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115171712306621&bvid=BV1zFYPzyEys&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/wwDgjRw75_A?si=pWVVdE92jBqQpozC" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
