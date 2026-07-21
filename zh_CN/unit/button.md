# Unit Button

<span class="product-sku">SKU:U027</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/button/button_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/button/button_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/button/button_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/button/button_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/button/button_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/button/button_07.webp">
</PictureViewer>

## 描述

**Unit Button** 是一个单按键 Unit，通过检测输入引脚高 / 低电平变化，进而判断按键状态。

## 产品特性

- HY2.0-4P 接口，支持 [UiFlow](http://flow.m5stack.com) 、 [Arduino](http://www.arduino.cc).
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit Button
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 灯座开关
- 远程控制开关

## 规格参数

| 规格     | 参数           |
| -------- | -------------- |
| 产品重量 | 4g             |
| 毛重     | 16g            |
| 产品尺寸 | 32 x 24 x 8mm  |
| 包装尺寸 | 136 x 92 x 9mm |

## 操作说明

**输出状态:**

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/button/button_08.webp" width="60%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/button/button_09.webp" width="60%">

## 原理图

- [Unit Button 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/804/U027_UNIT_BUTTON_SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/804/U027_UNIT_BUTTON_SCHE_page_01.png">
</SchViewer>

## 管脚映射

### Unit Button

::grove-table
| HY2.0-4P | Black | Red | Yellow | White          |
| -------- | ----- | --- | ------ | -------------  |
| PORT.B   | GND   | 5V  | NC     | Digital Output |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/804/U027_Model_Size_page_01.png" width="100%">

## 软件开发

### Arduino

- [Unit Button Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/BUTTON)

### UiFlow1

- [Unit Button UiFlow1 文档](/zh_CN/uiflow/blockly/unit/button)

### UiFlow2

- [Unit Button UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/button.html)

### EasyLoader

| Easyloader                      | 下载链接                                                                                                                             | 备注 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| Unit Button example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_Button_UNIT_With_M5Core.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/Button_UNIT.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113157087429768&bvid=BV1MqtGe5EMX&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/nkrWA4XPmjc?si=uXkLNGQG1Tz9vRJQ" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
