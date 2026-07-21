# Unit Fader

<span class="product-sku">SKU:U123</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/fader/fader_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/fader/fader_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/fader/fader_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/fader/fader_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/fader/fader_06.webp">
</PictureViewer>

## 描述

**Unit Fader**是一款集成指示灯的 **滑动电位器 / 推子**，采用 **35mm 行程的滑动电位器** + **14x SK6812 可编程 RGB 灯**组合设计。推子自带 **中心定位**，出色的滑动阻尼感能够实现更加平稳、顺畅、精准的控制。集成的灯珠支持数字寻址，这意味着你可以单独控制每一个 LED 灯显示的颜色、亮度，实现各种灯光效果。该产品适用于灯光、音乐控制等应用场景。

## 产品特性

- 带中心定位
- 舒适的滑动阻尼感
- 单联 10kΩ 可调电阻
- 可编程 RGB 灯
- GROVE 接口
- 开发平台:
  - Arduino、UiFlow

## 包装内容

- 1 x Unit Fader
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 人机交互
- 灯光、音乐控制
- 调节开关
- 电位器电平信号输入

## 规格参数

| 规格     | 参数                                     |
| -------- | ---------------------------------------- |
| 推子行程 | 35mm                                     |
| 推子柄长 | 10mm                                     |
| 单联电阻 | 1OkΩ                                     |
| 输出电压 | 0-3.3V (5V 供电情况下)                   |
| RGB LED  | 14x SK6812 可编程 RGB 灯                 |
| 工作电流 | 90.04mA (灯光亮度配置 50%，推子最大输出) |
| 产品重量 | 32g                                      |
| 毛重     | 40g                                      |
| 产品尺寸 | 64.0 x 24.0 x 22.8mm                     |
| 包装尺寸 | 136 x 92 x 24mm                          |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/fader/fader_sch_01.webp" width="80%">

## 管脚映射

### Unit Fader

::grove-table
| HY2.0-4P | Black | Red | Yellow | White        |
| -------- | ----- | --- | ------ | ------------ |
| PORT.B   | GND   | 5V  | RGB    | Analog Input |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/802/U123_Model_Size_page_01.png" width="100%">

## 软件开发

### Arduino

- [Unit Fader Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/FADER)
- [FastLED Arduino 驱动库](https://github.com/FastLED/FastLED)

### UiFlow1

- [Unit Fader UiFlow1 文档](/zh_CN/uiflow/blockly/unit/fader)

### UiFlow2

- [Unit Fader UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/fader.html)

### Home Assistant

- [Home Assistant 集成](/zh_CN/homeassistant/input_device/unit_fader)

## 相关视频

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/FADER_UNIT_VIDEO.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112868284436317&bvid=BV1a3vPeyEcM&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/ybEGVHWRxfQ?si=lfAE4ME_Hnt2yyIQ" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
