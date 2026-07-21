# Unit Neco

<span class="product-sku">SKU:U163</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Neco Unit/img-bb90b98e-1718-4a9d-8e36-afebfa1ee7d3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Neco Unit/img-0829fc9e-df08-42df-9b0e-7bc4fe3f32d4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Neco Unit/img-a3b8f61c-75b9-4d06-9794-fec1967311e4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Neco Unit/img-f441c430-5ab7-44e4-b5be-b1b878a0096c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Neco Unit/img-84e18cd8-11d4-44c9-9b22-f99ff8500699.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Neco Unit/img-faaede42-e434-423c-9382-fb4ee440cd56.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Neco Unit/img-5fd72387-a3a4-4aeb-a973-11d5dd6aadd6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Neco Unit/img-94522859-d857-491f-baee-2746db819d48.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Neco Unit/img-029f06c7-bc7d-4fc7-af8b-ba732082420b.webp">
</PictureViewer>

## 描述

**Unit Neco** 是一款具有 “猫耳朵造型” 的 RGB 灯板单元，采用 35 个 **WS2812C-2020** RGB 灯珠。它配备两个 4pin 的 grove 口，用于连接 M5 主机和扩展更多单元。此外，还有一个 **轻触按钮**，可与主机互动并切换不同灯光效果。适用于家居装饰、派对氛围、舞台表演等场景。

\#> 最好不要长时间处于全亮状态，容易烧坏灯珠，建议设置亮度 20 左右。

## 产品特性

- WS2812C-2020 RGB
- HY2.0-4P
- 轻触开关
- 兼容多平台开发:
  - UiFlow
  - Arduino

## 包装内容

- 2 × Unit Neco
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HY2.0-4P Grove 连接线 (1m)
- 2 × 塑料涂层铁丝

## 应用场景

- 家居装饰
- 派对氛围
- 舞台表演

## 规格参数

| 规格                 | 参数                 |
| -------------------- | -------------------- |
| 灯珠                 | WS2812C-2020         |
| 每个灯珠消耗电流大小 | 5mA                  |
| 亮度级别             | 256 级亮度显示       |
| 连接方式             | 串行级联接口         |
| 工作温度             | 0-85°C               |
| 颜色数量             | 16777216 种颜色      |
| 产品尺寸             | 44.6 x 43.0 x 10.1mm |
| 产品重量             | 9.6g                 |
| 包装尺寸             | 99.0 x 66.0 x 27.0mm |
| 毛重                 | 52.8g                |

## 原理图

- [Unit Neco 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/618/Sch_neco-unit.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/618/Sch_neco-unit_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Neco

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | DATA   | BTN   |
::

## 尺寸图

<img alt="module size" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/767/U163_Model_Size_sch_01.png" width="100%" />

## 结构文件

- [Unit Neco 3D Stp](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Neco%20Unit/NECO.stp)

## 数据手册

- [WS2812C-2020 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Neco%20Unit/WS2812C-2020.PDF)

## 软件开发

### Arduino

```cpp
#include <Adafruit_NeoPixel.h>
#define PIN        2 // M5AtomS3
#define NUMPIXELS 70
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
#define DELAYVAL 100

void setup() {
pixels.setBrightness(20);
  pixels.begin();
}

void loop() {
  pixels.clear();
  for (int i=0; i<NUMPIXELS; i++) {
    pixels.setPixelColor (i, pixels.Color(244, 24, 208) );
  }
  pixels.show();
}
```

### UiFlow

- [Unit Neco 测试程序](https://flow.m5stack.com/?examples=unit_neco_demo)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Neco Unit/uiflowCase-1687247453354image.png" width="100%"/>

### UiFlow2

- [Unit Neco UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/neco.html)
