# Unit Color

<span class="product-sku">SKU:U009</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/COLOR/img-5e8f77b1-0a2d-4810-8b8d-c2374bd738fb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/COLOR/img-99d06578-bff0-4d57-bb82-a5debaca515f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/COLOR/img-72160d6e-c47d-4d89-84a1-ba9a3bbb9239.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/COLOR/img-91e53454-e42d-4f33-87a2-2fa2f78c453a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/COLOR/img-8a6ebbb4-f768-466a-b7d4-53ae5318f8ed.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/707/U009-weight.jpg">
</PictureViewer>

## 描述

Unit Color 是一款高精度 RGB 颜色识别单元。它内置 TCS3472 彩色光数字转换器，支持 RGBC（红、绿、蓝、环境光）四通道测量，能精准将环境光转换为 RGB 数据。单元通过 I2C 接口通信 (0x29)，集成 LED 补光系统以确保在各种光照下准确识别颜色，并采用 LEGO 兼容孔设计，可灵活对接 LEGO 结构或进行螺丝固定。适用于产品颜色验证、颜色追踪机器人、环境光监测等多种需要进行色彩识别的应用场景。

## 产品特性

- 核心芯片：TCS3472
- 测量通道：RGBC 四通道
- 补光系统：集成白光 LED
- 通信接口：I2C (0x29)
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit Color
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 产品颜色验证
- 颜色追踪机器人

## 规格参数

| 规格         | 参数                 |
| ------------ | -------------------- |
| IC 型号      | TCS3472              |
| 通信接口     | I2C 通信 @ 0x29      |
| 工作温度范围 | -40 ~ 85°C           |
| 产品尺寸     | 32.0 x 24.0 x 8.0mm  |
| 产品重量     | 4.2g                 |
| 包装尺寸     | 138.0 x 93.0 x 9.0mm |
| 毛重         | 10.0g                |

## 数据手册

- [Datasheet-TCS3472](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/TCS3472_en.pdf)

## 原理图

- [Unit Color 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/707/U009-UNIT_COLOR-SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/707/U009-UNIT_COLOR-SCHE_page_01.png">
</SchViewer>

## 管脚映射

### Unit Color

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="image" width="100%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/COLOR/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg">

## 结构文件

- [Unit Color 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U009_Unit_Color/Structures)

## 软件开发

### Arduino

- [Unit Color 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/COLOR_TCS3472)

### UiFlow1

- [Unit Color UiFlow1 文档](/zh_CN/uiflow/blockly/unit/color)

### UiFlow2

- [Unit Color UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/color.html)

### EasyLoader

| Easyloader                 | 下载链接                                                                                                                       | 备注 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---- |
| Unit Color Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/COLOR/ezLoader-8b2c7c7b-0391-4f39-9ade-c27aae193a13.exe) | /    |

## 相关视频

- Unit Color 示例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/Color_UNIT.mp4" type="video/mp4"></video>

- Color Unit UiFlow2 Use

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113185977863818&bvid=BV18VsSeyEtW&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/pLu1sYrWeek?si=qXzJhVvZw6J_BWui" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
