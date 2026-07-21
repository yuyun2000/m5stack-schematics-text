# Unit RGB

<span class="product-sku">SKU:U003</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rgb/rgb_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rgb/rgb_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rgb/rgb_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rgb/rgb_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rgb/rgb_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/760/U003-weight.jpg">
</PictureViewer>

## 描述

Unit RGB 是一款集成了 3 颗 SK6812 可编程 RGB LED 的智能灯带单元。用户可通过程序独立控制每颗 LED 的颜色与 256 级精细亮度，实现丰富的灯光效果。其独特的可串接设计，允许将多个单元轻松扩展，形成更长的灯带或复杂的光阵。单元配备 LEGO 兼容孔，便于安装在各种结构或项目中，是 STEM 教育、灯光艺术、氛围营造及交互装置创作的理想组件。

## 产品特性

- 3 × SK6812 可编程的 RGB LED
- 256 级亮度调节
- 支持串接多个 Unit RGB 进行拓展
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit RGB
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- STEM 教育
- 灯光艺术
- 交互装置创作

## 规格参数

| 规格             | 参数                 |
| ---------------- | -------------------- |
| 灯珠型号         | SK6812 (3535)        |
| 工作电压         | DC 5V                |
| LED 灯珠灰度调节 | 256 级               |
| 产品尺寸         | 32.0 x 24.0 x 8.0mm  |
| 产品重量         | 4.7g                 |
| 包装尺寸         | 138.0 x 93.0 x 9.0mm |
| 毛重             | 10.0g                |

## 原理图

- [Unit RGB 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/760/U003-UNIT_RGB-SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/760/U003-UNIT_RGB-SCHE_page_01.png">
</SchViewer>

## 管脚映射

### Unit RGB

::grove-table
| HY2.0-4P | Black | Red | Yellow     | White |
| -------- | ----- | --- | ---------- | ----- |
| PORT.B   | GND   | 5V  | LED Signal | NC    |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/760/U003_Model_Size_sch_01.png" width="80%">

## 结构文件

- [Unit RGB 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U003_Unit_RGB/Structures)

## 软件开发

### Arduino

- [Unit RGB Test Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/RGB_SK6812)
- [Unit RGB Test Example with M5CoreS3](https://github.com/m5stack/M5CoreS3/blob/49580074f79832a9929b6b58c28aa7db1b01f7d3/examples/Unit/Unit_RGB_U003/Unit_RGB_U003.ino)

### UiFlow2

- [Unit RGB UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/rgb.html)

### EasyLoader

| Easyloader               | 下载链接                                                                                                                          | 备注 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit RGB Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_RGB_UNIT_With_M5Core.exe) | /    |

## 相关视频

- Unit RGB 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/760/U003-Unit-RGB-video-ZH.mp4" type="video/mp4"></video>

- 驱动 RGB LED 点亮不同颜色.

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/RGB_UNIT.mp4" type="video/mp4">
</video>
