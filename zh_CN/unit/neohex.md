# Unit NeoHEX

<span class="product-sku">SKU:A045-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neohex/neohex_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neohex/neohex_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/532/A045-B-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neohex/neohex_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neohex/neohex_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neohex/neohex_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neohex/neohex_06.webp">
</PictureViewer>

## 描述

**Unit NeoHEX** 是一款六边形 RGB LED 灯板，内嵌 37 颗 RGB LED 全彩灯珠。使用单总线控制，支持多个灯板级联。提供两组不同座子角度输入接口，可用于独立电源供电 + 信号控制，在级联多个灯板的情况下确保供电充足。外部结构带固定耳，方便嵌入与固定。自带乳白色均光片，发光效果更加柔和，适用于各种灯光 DIY 展品制作。

## 产品特性

- WS2812C-2020-V1
- NeoHEX 灯珠个数: 37
- 支持多个灯板，灯条级联
- 6 x 固定耳 (易拆设计)
- 自带乳白色均光片
- 单个像素支持 256 级亮度显示，可实现组合实现 16777216 种颜色的全真色彩显示

## 包装内容

- 1 x Unit NeoHEX
- 1 x 乳白色均光片
- 1 x 功耗情况参考卡
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 灯光装饰

## 规格参数

| 规格            | 参数                                                                                                                       |
| --------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 灯珠型号        | WS2812C-2020-V1                                                                                                            |
| 灯珠个数        | 37                                                                                                                         |
| 供电电压        | 3.7 ~ 5.3V                                                                                                                 |
| 逻辑输入电平    | -0.3V ~ VDD+0.7                                                                                                            |
| 输出 / 输出接口 | HY2.0-4P 接口：2x 输入 (信号，电源)，1x 输出 (延展)                                                                        |
| 刷新速率        | 30 帧 (级联数 1024)。                                                                                                      |
| 颜色 / 功耗参考 | 实测功耗情况 (37 灯全亮，白色灯) ：<br/>10%：DC 5V@207mA<br/>绿灯：DC 5V@109mA<br/>蓝灯：DC 5V@208mA<br/>白灯：DC 5V@568mA |
| 可调亮度        | 256 级                                                                                                                     |
| 支持颜色        | 16777216 种颜色                                                                                                            |
| 固定孔直径      | 2mm                                                                                                                        |
| 产品尺寸        | 36.0 x 36.0 x 9.6mm                                                                                                        |
| 产品重量        | 3.9g                                                                                                                       |
| 包装尺寸        | 138.0 x 93.0 x 8.0mm                                                                                                       |
| 毛重            | 9.7g                                                                                                                       |

## 操作说明

### 亮度 / 功耗参考

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neohex/neohex_07.webp" width="100%">

### 驱动情况

\#> 不同的 M5 主控在 USB 供电条件下该灯板驱动情况参考：

- 实测驱动情况：
  - ATOM: 白灯亮度为 82% 正常驱动 (>86% 时无法点亮)
  - CORE: 白灯亮度为 100% 正常驱动
  - CORE2: 白灯亮度为 100% 正常驱动
  - M5StickC: 白灯亮度为 86% 正常驱动 (>90% 时无法点亮)
  - M5StickCPlus: 白灯亮度 78% 正常驱动 (>86% 时无法点亮)

## 原理图

- [Unit NeoHEX 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/532/Sch_NeoHex_V1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/532/Sch_NeoHex_V1.1_sch_01.png">
</SchViewer>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/532/Sch_NeoHex_V1.1_sch_02.jpg" width="50%">

## 管脚映射

### Unit NeoHEX

::grove-table
| HY2.0-4P | Black | Red | Yellow     | White |
| -------- | ----- | --- | ---------- | ----- |
| PORT.B   | GND   | 5V  | LED Signal | NC    |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/532/A045_B_Model_Size_sch_01.png" width="100%">

## 软件开发

### Arduino

- [FastLED Arduino 驱动库](https://github.com/FastLED/FastLED)
- [Unit NeoHEX 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/HEX_SK6812)

### UiFlow1

- [Unit NeoHEX 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/HEX/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_uiflow_01.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_uiflow_02.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_uiflow_03.webp" width="70%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hex/hex_uiflow_04.webp" width="70%">


### Home Assistant

- [Unit NeoHEX Home Assistant 集成](/zh_CN/homeassistant/light/unit_neo_hex)