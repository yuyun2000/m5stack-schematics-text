# Unit Mini Scales

<span class="product-sku">SKU:U177</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini Scales/img-b9cc6e44-bd3c-4256-bd72-5fb45423483c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini Scales/img-e124306a-177f-4385-996d-18f10f928040.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/748/U177-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini Scales/img-7130217a-1753-42b3-adac-426f4390876c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini Scales/img-d8315796-ac9f-413f-98ee-b9f7ea74eaf3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini Scales/img-7291873c-48bf-413f-a218-156c069e2141.webp">
</PictureViewer>

## 描述

**Unit Mini Scales** 是一款一体化迷你称重单元，内部整合了量程为 5 Kg 的称重传感器和 ADC 采集芯片 HX711，以及协议转换 MCU，可直接输出称重结果。该产品搭载了 STM32F030F4P6 微控制器，采用 I2C 通信协议与外部通信，支持多个模块同时协同工作。此外，它配备了 SK6812 RGB 可编程 LED 指示灯和一个功能按键，使用户能够轻松进行零点校准和去皮调整。产品顶部预留了 M3 螺母固定孔，提供更多安装选项。**Unit Mini Scales** 适用于科学实验、工业生产等领域。

## 产品特性

- STM32F030F4P6@32 位 ARM Cortex-M0 处理器
- I2C 通讯，可多个同时并联使用
- SK6812 RGB
- 按键清零去皮
- 称重最大 5KG
- 编程平台：Arduino、UiFlow、python 等

## 包装内容

- 1 x Unit Mini Scales
- 4 x 螺母 M3 (六边形 6 x 2.25mm)
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 科学实验
- 工业生产

## 规格参数

| 规格                | 参数                                     |
| ------------------- | ---------------------------------------- |
| 传感器 ADC 检测芯片 | HX711                                    |
| 微控制器            | STM32F030F4P6@32 位 ARM Cortex-M0 处理器 |
| 通信接口            | I2C 通信 @ 0x26                          |
| LED 指示灯          | SK6812 RGB 可编程                        |
| 专用按键            | 用于零点校准和去皮调整                   |
| 称重能力            | 5KG                                      |
| 底部固定螺母规格    | M3                                       |
| 产品尺寸            | 40 x 24 x 18mm                           |
| 包装尺寸            | 136 x 92 x 24mm                          |
| 产品重量            | 15.3g                                    |
| 毛重                | 22g                                      |

## 操作说明

> 安装称重板到 Mini Scales Unit 上进行称重。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MiniScales/f9eb499abd882df1e17c9027400793c.png" width="50%" />

## 原理图

- [Unit Mini Scales 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/629/SCH_UNIT_MiniScales_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/629/SCH_UNIT_MiniScales_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Mini Scales

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### SK6812，Button

| STM32  | PB1 | PA7 |
| ------ | --- | --- |
| SK6812 | RGB |     |
| BUTTON |     | KEY |

## 尺寸图

- [Unit Mini Scales模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/748/U177_miniscale_asm_v1.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/748/U177_miniscale_asm_v1_page_01.png" width="100%">

## 数据手册

- [模块数据手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MiniScales/CZL928MC-Model.pdf)

## 软件开发

### Arduino

- [Unit Mini Scales Arduino 驱动库](https://github.com/m5stack/M5Unit-Miniscale)

### UiFlow1

- [Unit Mini Scales UiFlow1 文档](/zh_CN/uiflow/blockly/unit/mini_scales)

### UiFlow2

- [Unit Mini Scales UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/miniscale.html)

### 内置固件

- [Unit Mini Scales 内置固件](https://github.com/m5stack/M5Unit-Miniscale-Internal-FW)

| 固件版本 | 修改记录                                                      | 通信协议                                                                                                                       |
| -------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| v3       | 首次发布时版本                                                | [Unit Mini Scales I2C Protocol v3](https://github.com/m5stack/M5Unit-Miniscale/blob/main/docs/Unit_MiniScale_I2C_Protocol.pdf) |
| v4       | 取消了对 ADC 变化值的绝对值限制，以便能够显示负的重量测量值。 | 通信协议无变更，使用 v3 版本                                                                                                   |

\#> M5 DAPLink | 若您没有 STM32 下载器工具，可参考[M5 DAPLink](/zh_CN/guide/develop_tools/daplink)教程，使用 Core2 或 CoreS3 作为烧录器，为设备完成固件更新。

### 通信协议

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/748/Unit_MiniScale_I2C_Protocol_page_01.png" width="100%"/>

## 相关视频

- Unit Mini Scales 功能演示以及介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-MiniScales/U177%20Unit-MiniScales%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113270367193097&bvid=BV1EL2nYjE4d&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/B76Uw2weIg4?si=TghLoUeKK9KZiqlz" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比表   | [Unit Scales](/zh_CN/unit/UNIT%20Scales) ![Unit Scales](https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT%20Scales/img-d095bc9f-0f3f-4243-abde-82f8d6b67949.webp) | [Scales Kit](/zh_CN/app/scales_kit) ![Scales Kit](https://static-cdn.m5stack.com/resource/docs/products/app/scales_kit/scales_kit_cover_01.webp) | [Unit Mini Scales](/zh_CN/unit/Unit-Mini%20Scales) ![Unit Mini Scales](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini%20Scales/img-c370a473-d300-42c0-bf4c-cdf6d7963a6a.webp) | [Unit Weight](/zh_CN/unit/WEIGHT) ![Unit Weight](https://static-cdn.m5stack.com/resource/docs/products/unit/WEIGHT/img-e051022a-5e26-4ca5-9080-71eeb98fdf5e.webp) | [Unit Weight-I2C](/zh_CN/unit/Unit-Weight%20I2C) ![Unit Weight-I2C](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Weight%20I2C/img-998f3dae-bddd-4eea-8361-0c24821f367e.webp) |
| ------------ | ---------------------                                                                                                                                                           | --------------------                                                                                                                             | --------------------------                                                                                                                                                                          | ---------------------                                                                                                                                             | -------------------------                                                                                                                                                                       |
| 通信协议     | I2C                                                                                                                                                                             | ADC                                                                                                                                              | I2C                                                                                                                                                                                                 | ADC                                                                                                                                                               | I2C                                                                                                                                                                                             |
| 芯片方案     | STM32+HX711                                                                                                                                                                     | HX711                                                                                                                                            | STM32+HX711                                                                                                                                                                                         | HX711                                                                                                                                                             | STM32+HX711                                                                                                                                                                                     |
| 传感器量程   | 0~20kg                                                                                                                                                                          | 0~200kg                                                                                                                                          | 0~5kg                                                                                                                                                                                               | 取决应变片与控制芯片                                                                                                                                              | 取决应变片与控制芯片                                                                                                                                                                            |
::
