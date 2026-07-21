# Unit Earth

<span class="product-sku">SKU:U019</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/earth/earth_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/earth/earth_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/728/U019-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/earth/earth_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/earth/earth_06.webp">
</PictureViewer>

## 描述

**Unit Earth** 是一款土壤湿度传感器，用于采集土壤或是类似材料中的水分。传感器上有两个测量探头，将其插入待测量土壤中，由于水分含量越高，则拥有更好的导电性，通过测量两探头之间的电势差，并进行 ADC 转换，将检测结果发送给 M5Core。Unit 上还集成了一个 10K 可调电阻，用于调节检测门槛值。

## 产品特性

- 集成 10K 可调电阻，用于调节阈值.
- 模拟 & 数字 输出
- HY2.0-4P 接口，支持 [UiFlow](http://flow.m5stack.com) 、 [Arduino](http://www.arduino.cc)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit Earth
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 盆栽土壤湿度监控

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 产品尺寸 | 64.3 x 24.0 x 8.0mm  |
| 产品重量 | 5.0g                 |
| 包装尺寸 | 138.0 x 93.0 x 9.0mm |
| 毛重     | 10.0g                |

## 操作说明

?> 注意事项 | 该模块的电极并不防腐或防水，仅用于概念验证。请不要将其长时间放置在潮湿的环境中。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/earth/earth_08.webp">

## 原理图

- [Unit Earth 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/728/U019_UNIT_EARTH_SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/728/U019_UNIT_EARTH_SCHE_page_01.png">
</SchViewer>

## 管脚映射

### Unit Earth

::grove-table
| HY2.0-4P | Black | Red | Yellow         | White         |
| -------- | ----- | --- | -------------  | ------------  |
| PORT.B   | GND   | 5V  | Digital Output | Analog Output |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/earth/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%">

## 结构文件

- [Unit Earth 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U019_Unit_Earth/Structures)

## 软件开发

### Arduino

- [Unit Earth 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/EARTH)

### UiFlow1

- [Unit Earth UiFlow1 文档](/zh_CN/uiflow/blockly/unit/earth)

### UiFlow2

- [Unit Earth UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/earth.html)

### EasyLoader

| Easyloader                 | 下载链接                                                                                      | 备注 |
| -------------------------- | --------------------------------------------------------------------------------------------- | ---- |
| Unit Earth Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_Earth.exe) | /    |

## 相关视频

**EARTH 的教程 - 监控花瓶土壤含水量**

<video width="500" height="315" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/LukeVideo/(M5stack%20x%20Arduino)%20Do%20plants%20have%20feelings.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113342777658103&bvid=BV1UuyqYqEFY&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/dgxSJn-oQr4?si=VTIY0YaXY1cSHdhd" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
