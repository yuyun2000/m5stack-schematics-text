# Unit ByteButton

<span class="product-sku">SKU:U192</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/16.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/13.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/14.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/15.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/819/U192-weight.jpg">
</PictureViewer>

## 描述

**Unit ByteButton** 是一款 8 路轻触开关输入单元，配备 8 路 按键输入和 9 颗 WS2812C RGB 灯珠，采用 STM32 作为主控，支持 I2C 通讯，板载两个 **Port A** 接口，支持多个 Unit ByteButton 模块 **级联** 使用，满足复杂系统的需求。它能够实现按键输入检测与动态灯光状态反馈，适用于智能家居控制、游戏娱乐设备、教育开发平台、工业状态显示以及互动展览等领域。

## 产品特性

- 8 路按键输入
- 9 颗 WS2812C RGB 灯珠
- STM32 主控
- I2C 通讯接口
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit ByteButton
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 按键标识贴纸

## 应用场景

- 智能家居控制面板
- 游戏或娱乐设备控制器
- 教育与实验室开发平台
- 状态控制与反馈装置
- 便携式设备调试工具
- 互动展览或场景控制
- 小型仪器的用户界面

## 规格参数

| 规格       | 参数                                                  |
| ---------- | ----------------------------------------------------- |
| MCU        | STM32G031G8U6，32 位 ARM Cortex-M0+ 内核，主频 64 MHz |
| 按键数量   | 8 路独立按键输入                                      |
| 按键类型   | 轻触式按键                                            |
| RGB 灯珠   | WS2812C-2020 (9 颗)                                   |
| 通信接口   | I2C 通讯 @0x47                                        |
| Grove 接口 | 2 个 (I2C 总线扩展)                                   |
| 待机功耗   | DC 5V@8.94mA                                          |
| 工作温度   | 0 ~ 40°C                                              |
| 产品尺寸   | 88.0 x 24.0 x 12.0mm                                  |
| 产品重量   | 15.2g                                                 |
| 包装尺寸   | 170.0 x 120.0 x 15.0mm                                |
| 毛重       | 21.8g                                                 |

## 原理图

- [Unit ByteButton 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/819/U192_SCH_Unit-ByteButton_V1.0_2024_11_20_16_18_15.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/819/U192_SCH_Unit-ByteButton_V1.0_2024_11_20_16_18_15_page_01.png">
</SchViewer>

## 管脚映射

### Unit ByteButton

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### STM32

| STM32 | PA0   | PA1   | PA5   | PA6   | PA7   | PA15  | PB3   | PA8   | PB5 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | --- |
| KEY   | SW_K0 | SW_K1 | SW_K2 | SW_K3 | SW_K4 | SW_K5 | SW_K6 | SW_K7 | RGB |

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 软件开发

### Arduino

- [Unit ByteButton Arduino 驱动库](https://github.com/m5stack/M5Unit-ByteButton)

### UiFlow2

- [Unit ByteButton UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/bytebutton.html)

### 内置固件

- [Unit ByteButton 内置固件](https://github.com/m5stack/M5Unit-ByteButton-Internal-FW)

### 通信协议

- [Unit ByteButton I2C Protocol](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/Byte_Button%20Protocol.pdf)

<img alt="protocol" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/protocol.png" width="100%" />

## 相关视频

- Unit ByteButton 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteButton/unit%20bytebutton%20video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113660420688501&bvid=BV1C8BPYpEHP&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/lkEenKprM7U?si=6UeWqOVrwawwTGEe" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
