# Unit Weight

<span class="product-sku">SKU:U030</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/WEIGHT/img-a0113c8c-ed62-43b9-ad38-5cb934811d9e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/WEIGHT/img-1ab21298-f9e9-4de9-9f1e-806cdf9d3baf.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/WEIGHT/img-fe55170a-8b54-4f11-8993-27f5839d729c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/WEIGHT/img-1d8b985f-2c03-476e-8c26-d63496137652.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/WEIGHT/img-d34002f1-5687-4a48-a4cf-5662135b35e3.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/704/U030-weight.jpg">
</PictureViewer>

## 描述

**Unit Weight** 是一款计重 Unit。集成了专为高精度电子秤设计的 24 位 A/D 转换器芯片 **HX711**。本设计仅采用其 **通道 A**，通过内置低噪声可编程放大器 (PGA) 对采集的信号进行放大。通道 A 的可编程增益可设为 128 或 64，对应的满额度差分输入信号幅值分别为 ±20mV 或 ±40mV。所有控制信号由管脚驱动，无需对芯片内部寄存器编程。该产品适用于高精度计重系统、工业自动化控制、物流和仓储管理、食品加工、药品计量等领域

## 产品特性

- HX711:
  - 高精度 24bit ADC
  - 可编程增益放大 32，64 and 128
  - 10SPS 输出数据速率
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 包装内容

- 1 x Unit Weight
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96-4P 端子

## 应用场景

- 微型重量计
- 厨房秤

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 产品尺寸 | 32.0 x 24.0 x 10.2mm  |
| 产品重量 | 5.1g                  |
| 包装尺寸 | 138.0 x 93.0 x 11.2mm |
| 毛重     | 13.0g                 |

## 原理图

- [Unit Weight 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/704/U030-UNIT_WEIGHT-weight.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/704/U030-UNIT_WEIGHT-weight_page_01.png">
</SchViewer>

## 管脚映射

### Unit Weight

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | CLK    | DAT   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/WEIGHT/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit Weight 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U030_Unit_Weight/Structures)

## 数据手册

- [HX711](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/HX711_en.pdf)

## 软件开发

### Arduino

- [Unit Weight Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/WEIGHT_HX711)

### UiFlow1

- [Unit Weight UiFlow1 文档](/zh_CN/uiflow/blockly/unit/weight)

### UiFlow2

- [Unit Weight UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/weight.html)

### EasyLoader

| Easyloader                      | 下载链接                                                                                                                        | 备注 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Weight Example with M5Core | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/WEIGHT/ezLoader-d80f5842-7fed-4614-b7bb-d6d12f99d6c3.exe) | /    |

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
		   <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113661192504884&bvid=BV1mKBTYiE9o&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/8HQovUGDxgs?si=iB28tri1fDLGYLV4" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比表   | [Unit Scales](/zh_CN/unit/UNIT%20Scales) ![Unit Scales](https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT%20Scales/img-d095bc9f-0f3f-4243-abde-82f8d6b67949.webp) | [Scales Kit](/zh_CN/app/scales_kit) ![Scales Kit](https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_cover_01.webp) | [Unit Mini Scales](/zh_CN/unit/Unit-Mini%20Scales) ![Unit Mini Scales](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini%20Scales/img-c370a473-d300-42c0-bf4c-cdf6d7963a6a.webp) | [Unit Weight](/zh_CN/unit/WEIGHT) ![Unit Weight](https://static-cdn.m5stack.com/resource/docs/products/unit/WEIGHT/img-e051022a-5e26-4ca5-9080-71eeb98fdf5e.webp) | [Unit Weight-I2C](/zh_CN/unit/Unit-Weight%20I2C) ![Unit Weight-I2C](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight%20I2C/img-998f3dae-bddd-4eea-8361-0c24821f367e.webp) |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 通信协议     | I2C                                                                                                                                                                             | ADC                                                                                                                                              | I2C                                                                                                                                                                                                 | ADC                                                                                                                                                               | I2C                                                                                                                                                                                             |
| 芯片方案     | STM32+HX711                                                                                                                                                                     | HX711                                                                                                                                            | STM32+HX711                                                                                                                                                                                         | HX711                                                                                                                                                             | STM32+HX711                                                                                                                                                                                     |
| 传感器量程   | 0~20kg                                                                                                                                                                          | 0~200kg                                                                                                                                          | 0~5kg                                                                                                                                                                                               | 取决应变片与控制芯片                                                                                                                                              | 取决应变片与控制芯片                                                                                                                                                                            |
::
