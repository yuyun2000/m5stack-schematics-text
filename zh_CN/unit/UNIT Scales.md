# Unit Scales

<span class="product-sku">SKU:U108</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT Scales/img-94426368-7f2e-43ae-a514-9d38ee161b46.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT Scales/img-22f5b336-4142-40f9-90ad-a99eaefeea09.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT Scales/img-de642cd3-5584-4489-8f12-7ebaa35bec9a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT Scales/img-04fe2bea-5437-453c-bce9-06ec5e719062.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT Scales/img-dabbf3ee-2751-4110-baf5-f5be99f4cb39.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/705/U108-weight.jpg">
</PictureViewer>

## 描述

**Unit Scales** 是一款提供 I2C 接口的 20 kG 一体化称重传感器单元，内部集成 **STM32F030** 主控、采集电路及 20 kG 称重传感器，内部采用 **HX711** 专用称重采集芯片，自带清零去皮功能按钮以及可编程 **RGB** 状态指示灯。用户通过 I2C 接口读取称重数据。该单元能为用户提供一体化高集成度的称重检测方案，可用于质量检测、计件、物件挪动检测等场景。

## 产品特性

- HX711:
  - 高精度 24bit ADC
  - 可编程增益放大 32，64 and 128
  - 10SPS 输出数据速率
- I2C 接口
- 开发平台: Arduino，UiFlow (Blockly，Python)

## 包装内容

- 1 x Unit Scales
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 智能秤
- 厨房秤
- 物品计数装置
- 人体感应检测

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| MCU      | STM32F030F4P6        |
| ADC      | HX711                |
| 通信接口 | I2C 通信 @ 0x26      |
| LED      | SK6812 (PA7 接口)    |
| 按键     | PA2 接口             |
| 外壳材料 | 塑料                 |
| 产品尺寸 | 56.0 x 40.0 x 41.0mm |
| 产品重量 | 83.5g                |
| 包装尺寸 | 57.0 x 42.0 x 41.0mm |
| 毛重     | 92.3g                |

## 操作说明

### Unit Scales 称重误差说明

| 重量 (g)     | 50   | 100  | 250  | 500  | 1000 |
| ------------ | ---- | ---- | ---- | ---- | ---- |
| 绝对误差 (g) | 0.45 | 0.25 | 0.20 | 0.25 | 4.15 |
| 相对误差     | 0.9% | 0.3% | 0.1% | 0.1% | 0.4% |

## 原理图

- [Unit Scales 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/592/Sch_UNIT-Scales.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/592/Sch_UNIT-Scales_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Scales

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT Scales/img-18e45241-a9b7-4d70-ab63-ba93b7473f18.png" width="100%" />

## 结构文件

- [Unit Scales 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U108_Unit_Scales/Structures)

## 数据手册

- [HX711](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/HX711_en.pdf)

## 软件开发

### Arduino

- [Unit Scales Config I2C Address Example](https://github.com/m5stack/M5Unit-Scales/blob/main/examples/ADDR_CONFIG/ADDR_CONFIG.ino)
- [Unit Scales Test Example with M5Core](https://github.com/m5stack/M5Unit-Scales/blob/main/examples/SCALES_TEST/SCALES_TEST.ino)
- [Unit Scales Test Example with M5Atom](https://github.com/m5stack/M5Unit-Scales/blob/main/examples/SCALES_TEST/SCALES_TEST.ino)

### UiFlow1

- [Unit Scales UiFlow1 文档](/zh_CN/uiflow/blockly/unit/scales)

### UiFlow2

- [Unit Scales UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/scales.html)

### 内置固件

- [Unit Scales 内置固件](https://github.com/m5stack/M5Unit-Scales-Internal-FW)

### 通讯协议

- [Unit Scales I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/705/Unit-Scales_Protocol.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/705/Unit-Scales_Protocol_page_01.png" width="70%">

### EasyLoader

| Easyloader                  | 下载链接                                                                                                                               | 备注 |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Scales Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT%20Scales/ezLoader-4b167a0c-093b-492d-b344-88ffc7526632.exe) | /    |

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113270333638816&bvid=BV1wU2nY9EBc&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/ptLs4c7NXIE?si=6oLAL3ngBoNjkeWg" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
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
