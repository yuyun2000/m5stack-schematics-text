# Unit Key

<span class="product-sku">SKU:U144</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/key/key_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/key/key_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/key/key_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/803/U144-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/key/key_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/key/key_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/key/key_07.webp">
</PictureViewer>

## 描述

**Unit Key** 是一款 **内置 RGB 灯** 的 **单按键输入** 单元，按键轴体采用段落感极强的 **青轴**，键帽可替换，具备出色的机械触感与回弹效果。内嵌一颗 **SK6812 可编程全彩 RGB LED**，支持 **256 级亮度显示**。单元引出两个数字 IO 接口，用于按键状态获取与灯光控制。适于 DIY 各种需要按键输入交互的应用。

## 产品特性

- 青轴 (段落感强)
- SK6812 可编程全彩 RGB LED

## 包装内容

- 1 x Unit Key
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 人机交互设计

## 规格参数

| 规格             | 参数                  |
| ---------------- | --------------------- |
| 供电电压         | DC 5V                 |
| 按键输出逻辑信号 | DC 3.3V               |
| 待机电流         | DC 5V@2mA             |
| 工作电流         | DC 5V@13mA            |
| 产品尺寸         | 40.0 x 24.0 x 22.6mm  |
| 产品重量         | 7.6g                  |
| 包装尺寸         | 138.0 x 93.0 x 18.0mm |
| 毛重             | 13.1g                 |

## 原理图

- [Unit Key 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/599/SCH_unitKey_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/599/SCH_unitKey_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Key

::grove-table
| HY2.0-4P | Black | Red | Yellow     | White |
| -------- | ----- | --- | ---------- | ----- |
| PORT.B   | GND   | 5V  | LED Signal | DIN   |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/803/U144_Model_Size_page_01.png" width="100%">

## 软件开发

### Arduino

- [Unit Key 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/KEY)
- [FastLED Arduino 驱动库](https://github.com/FastLED/FastLED/wiki/Overview)

### UiFlow1

- [Unit Key UiFlow1 文档](/zh_CN/uiflow/blockly/unit/key)

### UiFlow2

- [Unit Key UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/key.html)
