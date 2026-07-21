# Unit HEX

<span class="product-sku">SKU:A045</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/764/A045-package.jpg">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/764/A045-PCB_main-pictures_01.jpg">
</PictureViewer>

## 描述

**Unit HEX** 是一款六边形 RGB LED 灯板，板载 37 颗 RGB LED 灯珠，配置专用输入 / 输出端口，支持多块灯板串联扩展，可灵活组建多样化灯光阵列。

## 产品特性

- LED 颜色数量：16.7 万色
- 开发平台: Arduino，UiFlow (Blockly & python)

## 包装内容

- 1 x Unit HEX
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| RGB LED  | SK6812 x 37           |
| 产品尺寸 | 31.2 x 36.0 x 7.0mm   |
| 产品重量 | 4.6g                  |
| 包装尺寸 | 138.0 x 93.0 x 12.0mm |
| 毛重     | 10.0g                 |

## 操作说明

以下为 HEX 灯板中的 LED 布局排序方式

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_05.webp" width="50%">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_04.webp" width="50%">

## 管脚映射

### Unit HEX

::grove-table
| HY2.0-4P | Black | Red | Yellow     | White |
| -------- | ----- | --- | ---------- | ----- |
| PORT.B   | GND   | 5V  | LED Signal | /     |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/764/A045_Model_Size_sch_01.png" width="50%">

## 软件开发

### Arduino

- [FastLED Arduino 驱动库](https://github.com/FastLED/FastLED/wiki/Overview)
- [Unit HEX 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/HEX_SK6812)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_06.webp">

### UiFlow1

- [Unit HEX 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/HEX/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_uiflow_01.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_uiflow_02.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_uiflow_03.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_uiflow_04.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_uiflow_05.webp" width="70%">

### EasyLoader

| Easyloader               | 下载链接                                                                                                                          | 备注 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit HEX Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_HEX_UNIT_With_M5Core.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/HEX_UNIT.mp4" type="video/mp4">
</video>
