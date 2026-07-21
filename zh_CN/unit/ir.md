# Unit IR

<span class="product-sku">SKU:U002</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ir/ir_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ir/ir_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/833/U002-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ir/ir_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ir/ir_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/833/U002-weight.jpg">
</PictureViewer>

## 描述

Unit IR 是一款集成红外发射与接收功能的短距离光电对管单元。它采用 940nm 红外发射二极管与 38kHz 硬件解调接收头，支持 NEC 等标准红外协议的调制发射与自动识别解调接收。该单元通过 Grove HY2.0-4P 接口通信，有效通信距离小于 5 米，并采用 LEGO 兼容孔设计，便于灵活对接 LEGO 结构或使用螺丝固定。适用于智能家居控制、红外遥控学习、设备间短距离通信等应用场景。

## 产品特性

- 发射波长：940nm (不可见光)
- 接收频率：38kHz (硬件解调)
- 有效距离：≤ 5m
- 通信接口：Grove HY2.0-4P
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit IR
- 1 x HY2.0-4P 线缆

## 应用场景

- 智能家居
- 红外遥控

## 规格参数

| 规格           | 参数                 |
| -------------- | -------------------- |
| 红外发射器波长 | 940nm                |
| 产品尺寸       | 32.0 x 24.0 x 8.0mm  |
| 产品重量       | 4.6g                 |
| 包装尺寸       | 67.0 x 53.0 x 12.0mm |
| 毛重           | 17.0g                |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ir/ir_sch_01.webp" width="80%">

## 管脚映射

### Unit IR

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | IR_TX  | IR_RX |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/833/U002_Model_Size_sch_01.png" width="100%">

## 结构文件

- [Unit IR 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U002_Unit_IR/Structures)

## 软件开发

### Arduino

- [Unit IR Example - with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/IR)

### UiFlow1

- [Unit IR UiFlow1 文档](/zh_CN/uiflow/blockly/unit/ir)

### UiFlow2

- [Unit IR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/ir.html)

### Home Assistant

- [Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_ir)

### EasyLoader

| Easyloader              | 下载链接                                                                                   | 备注 |
| ----------------------- | ------------------------------------------------------------------------------------------ | ---- |
| Unit IR Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_IR.exe) | /    |

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113983868633934&bvid=BV138NieoEpN&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" autoplay="0" ></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/mYbJGz976sA?si=c_2pVaOjly39AbO1" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
