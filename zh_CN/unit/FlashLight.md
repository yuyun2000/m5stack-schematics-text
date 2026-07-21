# Unit FlashLight

<span class="product-sku">SKU:U152</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/FlashLight/img-ded1dc49-1697-43d2-857e-551bbb664eda.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/FlashLight/img-86a7b1f1-e930-458b-ac81-a6964553e566.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/765/U152-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/FlashLight/img-1867e836-67eb-4b62-96f3-360b48ff73eb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/FlashLight/img-23652565-5c7f-48f0-a9e4-d81eea3b868f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/FlashLight/img-8cd03d10-7725-44b0-b204-81694d606488.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/FlashLight/img-00d4d62e-af70-4fe3-aa91-213f06f44bed.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/FlashLight/img-eaf5f95d-4f6d-4f3a-bfb8-0fa5ce61bed5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/FlashLight/img-25533591-c9ad-457f-a6d9-6c2391829285.webp">
</PictureViewer>

## 描述

**Unit FlashLight**是一款自带闪光灯的输出单元，内含 AW3641 驱动以及 1 颗 5000 ~ 5700K 色温的白光灯珠。内部 PCB 上有模式选择开关，可选择闪光模式以及常亮模式，采用 GPIO 输入接口。可用作闪光源或照明等应用。

## 产品特性

- PWM 亮度调节方式
- 过温报警
- 过电压和短路保护
- 两种工作模式

## 包装内容

- 1 x Unit FlashLight
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 光源
- DIY
- 警报

## 规格参数

| 规格                    | 参数                 |
| ----------------------- | -------------------- |
| 驱动芯片                | AW3641EDNR           |
| 调节方式                | PWM                  |
| AW3641EDNR 使用环境温度 | -40℃ ~ +85℃          |
| Unit 工作温度           | 0 ~ 40℃              |
| Color Temperature       | 6000K~6500K (Kevin)  |
| 产品尺寸                | 32.0 x 24.0 x 8.0mm  |
| 产品重量                | 4.6g                 |
| 包装尺寸                | 138.0 x 93.0 x 9.0mm |
| 毛重                    | 10.0g                |

## 操作说明

### 工作模式说明

Unit Flashlight 提供两种工作模式，拆开设备外壳后，可根据内部拨码开关的丝印标识切换：
- Flash（闪光灯）模式：脉冲闪光控制，瞬间高亮，支持通过单线协议设置 8 档闪光强度（100%~30%）与闪光超时时间，专为拍照补光设计。
- Torch（手电筒）模式：持续常亮照明，支持 PWM 调光，亮度可无级调节，适合录像或日常照明场景。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/765/U152-mode-note.png" width="50%">

?>注意|闪光灯模式下亮度较高，单次闪光会产生热量，为避免设备过热损坏，建议两次闪光间隔 8～15 秒。

## 原理图

- [Unit FlashLight 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/606/UNIT-FlashLight.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/606/UNIT-FlashLight_sch_01.png">
</SchViewer>

## 管脚映射

### Unit FlashLight

::grove-table
| HY2.0-4P | Black | Red | Yellow        | White |
| -------- | ----- | --- | ------------- | ----- |
| PORT.C   | GND   | 5V  | Light Control | NC    |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/FlashLight/img-f88ae770-4c7a-402a-b238-9b5fdc85d992.png" width="100%" />

## 数据手册

- [AW3641EDNR Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/FlashLight/FLASHLEDDRIVER_2019-07-01.PDF)

## 软件开发

### Arduino

- [Unit FlashLight 测试程序](https://github.com/m5stack/M5Unit-FlashLight)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/FlashLight/arduinoCase-1666167871368微信图片_20221019161414.png" width="100%"/>

### UiFlow1

- [Unit FlashLight UiFlow1 文档](/zh_CN/uiflow/blockly/unit/flash_light)

### UiFlow2

- [Unit FlashLight UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/flash_light.html)

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113089005490138&bvid=BV1TdHSeNEpe&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/InLXjITC9aA?si=fQBmNsPPn6PZDAmb" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
