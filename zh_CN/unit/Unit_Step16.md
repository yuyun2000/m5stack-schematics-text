# Unit Step16

<span class="product-sku">SKU:U198</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit_Step16_11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/U198-weight.jpg">
</PictureViewer>

## 描述

**Unit Step16** 是一款基于 STM32G031G8U6 微控制器的 16 定位旋转编码器控制单元。其核心功能在于实时采集旋转编码器的 BCD 编码值，并通过集成数码管实现 0-F hex 编码数值可视化。设备采用 I2C 通信接口，支持配置编码器旋转递增方向、数码管工作模式、RGB 灯珠颜色等功能，同时支持 I2C 地址配置，方便同时挂载的多个编码器单元。

该单元以简洁高效的设计提供有效的物理交互控制与实时视觉反馈，适用于智能交互设备（如智能家居中控面板）、设备控制接口（如音量调节、RGB 灯光控制、电机调速）以及 STEAM 教育领域的硬件原型开发与教学等场景。

## 产品特性

- 16 定位 BCD 旋转编码器
- 集成数码管编码显示
- 可控制数码管亮度与工作模式
- 可设置顺时针、逆时针方向控制
- 支持配置 RGB LED 颜色 / 亮度
- 支持 I2C 通信，地址可设置
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit Step16
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 智能交互设备（如智能家居中控面板）
- 设备控制接口（如音量调节、RGB LED 灯光控制、电机调速）
- STEAM 教育

## 规格参数

| 规格           | 参数                                                                                                                                      |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| MCU            | STM32G031G8U6, 32 位 ARM Cortex-M0+ 内核， 主频 64 MHz                                                                                    |
| 步进编码       | 16 定位，8421 BCD 编码                                                                                                                    |
| 编码显示       | 7 段数码管                                                                                                                                |
| 可编程 RGB     | 1 x WS2812                                                                                                                                |
| 编码值更新周期 | 100ms                                                                                                                                     |
| 通信接口       | I2C 通信 @ 0x48，地址范围：0x08 ~ 0x77，掉电不丢失                                                                                        |
| 待机功耗       | DC 5V@5.85mA                                                                                                                              |
| 工作功耗       | 显示 LED 灯 60%：DC 5V@14.76mA<br /> 显示 LED 灯 100%：DC 5V@24.13mA<br />RGB 灯 100%：DC 5V@18.9mA<br />显示 LED/RGB 全开：DC 5V@29.91mA |
| 产品尺寸       | 32.0 x 24.0 x 16.9mm                                                                                                                      |
| 产品重量       | 5.5g                                                                                                                                      |
| 包装尺寸       | 138.0 x 93.0 x 13.0mm                                                                                                                     |
| 毛重           | 10.9g                                                                                                                                     |

## 操作说明

\#> 旋钮编码器的使用 | 为了延长编码器使用寿命，旋转时请保持适度力度，请勿暴力反复旋转。

## 原理图

- [Unit Step16 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/SCH_Unit_Step16_V1_0_2025_06_27_19_17_43.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/SCH_Unit_Step16.png">
</SchViewer>

## 管脚映射

### HY2.0-4P

::grove-table
| HY2.0-4P   | Black   | Red   | Yellow   | White   |
| ---------- | ------- | ----- | -------- | ------- |
| PORT.A     | GND     | 5V    | SDA      | SCL     |
::

## 数据手册

- [GSMR-16 数据手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/GSMR-16_datasheet_2025_07_10_10_57_18.pdf)

## 尺寸图

- [Unit Step16 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/UNIT16STEP.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/UNIT16STEP_page_01.png" width="100%">

## 软件开发

### Arduino

- [Unit Step16 Arduino 快速上手](/zh_CN/arduino/projects/unit/unit_step16)
- [Unit Step16 Arduino 驱动库](https://github.com/m5stack/M5Unit-Step16)

### UiFlow2

- [Unit Step16 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/step16.html)

### Home Assistant

- [Home Assistant 集成](/zh_CN/homeassistant/input_device/unit_step16)

### 内置固件

- [Unit Step16 内置固件](https://github.com/m5stack/M5Unit-Step16-Internal-FW)

### 通讯协议

- [Unit Step16 I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit-Step16_Protocol.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/Unit-Step16_Protocol.png" width="70%">

## 相关视频

Unit Step16 产品介绍以及案例展示

<video class="video-container" controls><source src="
https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1160/U198-Unit_Step16_video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114952987740688&bvid=BV14HhHziEza&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/BsgMSQKtIvY?si=M0-03cU8nhkh_Dhl" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
