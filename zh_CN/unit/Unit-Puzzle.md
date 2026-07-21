# Unit Puzzle

<span class="product-sku">SKU:U193</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/3.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/781/U193-weight.jpg">
</PictureViewer>

## 描述

**Unit Puzzle** 是一款多彩灯光控制单元，由 8x8 共 64 颗多彩 WS2812E RGB 灯珠组成 RGB 阵列。每个灯珠间特设 **栅格** 结构，避免相邻灯光互相干扰，确保光效更加清晰和纯净。产品板载两个 Grove 接口，其中一个为 **输入** 信号接口，另一个为 **输出** 接口，并附带一个连接件，用于连接多个 **Unit Puzzle** 单元，扩展更多灯光显示区域。该输出 Grove 接口还预留了一个 **IO** 口，支持外接其他 M5 设备，例如 Unit Angle 等包含 **Port B** 接口的传感器，实现更多的交互控制功能。**Unit Puzzle** 设计紧凑，安装便捷，底部配有一个 M2 孔，方便固定。产品大小只有 24 x 24 x 15mm。该产品适用于智能照明、装饰显示和互动装置等应用场景。

?> 灯珠亮度 | 长时间高亮度驱动可能导致损坏，推荐使用 10% 亮度，减少发热和功耗。

## 产品特性

- 8 x 8 WS2812 RGB 灯珠矩阵
- 栅格隔离设计
- 双 Grove 接口 (级联扩展)
- 2 x LEGO 兼容孔
- 编程平台：Arduino，UiFlow，ESP-IDF 等

## 包装内容

- 1 x Unit Puzzle
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 连接扩展件
- 1 x 亮度参数说明贴纸

## 应用场景

- 智能照明
- 装饰显示
- 互动装置

## 规格参数

| 规格         | 参数                                  |
| ------------ | ------------------------------------- |
| RGB 灯珠类型 | WS2812E-1313@8 x 8 阵列               |
| 灯珠数量     | 64 颗 (8x8 矩阵)                      |
| 单灯功耗     | 约 6mW (亮度 8%，白灯)                |
| 待机电流     | DC 5V@14.27mA                         |
| 工作电流     | DC 5V@93.99mA (亮度 8%，白灯)         |
| 供电电压     | DC 5V                                 |
| 接口类型     | 2 个 Grove 接口 (输入和输出 Grove 口) |
| 支持色彩     | 1677 万色                             |
| 控制方式     | 支持串行数据控制 (单线控制)           |
| 工作温度     | 0 ~ 40°C                              |
| 产品尺寸     | 24.0 x 24.0 x 15.0mm                  |
| 产品重量     | 6.4g                                  |
| 包装尺寸     | 138.0 x 93.0 x 16.0mm                 |
| 毛重         | 12.8g                                 |

## 操作说明

### 亮度和电流的关系

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/brightness%20and%20current.png" width="60%" />

- 灯珠排列顺序

<img alt="module_size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/pixel%20serial.png" width="30%" />

## 原理图

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/schematic.png" width="100%" />

## 管脚映射

### Unit Puzzle

::grove-table
| HY2.0-4P | Black | Red | Yellow     | White |
| -------- | ----- | --- | ---------- | ----- |
| PORT.B   | GND   | 5V  | LED Signal | NC    |
::

## 尺寸图

<img alt="module_size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/module_size.jpg" width="100%" />

## 数据手册

- [WS2812E](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/ws2812e.pdf)

## 软件开发

### Arduino

- [Adafruit Neopiexl Arduino 驱动库](https://github.com/adafruit/Adafruit_NeoPixel)
- [FastLED Arduino 驱动库](https://github.com/FastLED/FastLED)

### UiFlow1

- [Unit Puzzle UiFlow1 文档](/zh_CN/uiflow/blockly/unit/puzzle)

### UiFlow2

- [Unit Puzzle UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/puzzle.html)

## 视频

- Unit Puzzle 功能演示以及介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-Puzzle/puzzle_video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113501641115349&bvid=BV1ugUnYqEDS&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/_mkXOlexcBk?si=RNuR4I46NpGYSWPR" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
