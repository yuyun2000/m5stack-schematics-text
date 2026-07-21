# Unit Watering

<span class="product-sku">SKU:U101</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/watering/watering_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/watering/watering_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/729/U101-package.png">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/watering/watering_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/watering/watering_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/watering/watering_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/watering/watering_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/watering/watering_07.webp">
</PictureViewer>

## 描述

**Unit Watering** 是一款电容式土壤湿度检测调节 Unit，产品集成水泵与测量极板，用于土壤湿度检测与水泵抽水控制，应用在植物智能养殖场景中，能够非常便捷的实现湿度检测与灌溉控制。测量极板采用电容式设计，与电阻式极板相比，该设计能够有效避免实际使用时极板的腐蚀问题。

## 产品特性

- 电容式测量极板 / 更耐腐蚀
- 集成 5W 功率水泵
- LEGO 兼容孔

## 包装内容

- 1 x Unit Watering
- 2 x 抽水导管
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 植物培养
- 土壤湿度检测
- 智能灌溉

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 水泵功率 | 5W                    |
| 产品尺寸 | 192.8 x 26.5 x 33.0mm |
| 产品重量 | 94.6g                 |
| 包装尺寸 | 200.0 x 45.0 x 35.0mm |
| 毛重     | 114.2g                |

## 原理图

- [Unit Watering 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/729/U101_Unit-Watering_SCH.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/729/U101_Unit-Watering_SCH_page_01.png" width="80%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/729/U101_Unit-Watering_SCH_page_02.png" width="80%">
</SchViewer>

## 管脚映射

### Unit Watering

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White         |
| -------- | ----- | --- | ------- | ------------- |
| PORT.B   | GND   | 5V  | PUMP_EN | Analog Output |
::

## 尺寸图

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/watering/module_size.jpg" width="100%" />

## 结构文件

- [Unit Watering 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U101_Unit_Watering/Structures)

## 软件开发

### Arduino

- [Unit Watering 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/WATERING)

### UiFlow1

- [Unit Watering UiFlow1 文档](/zh_CN/uiflow/blockly/unit/watering)

### UiFlow2

- [Unit Watering UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/watering.html)

### Home Assistant

- [Unit Watering Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_watering_sensor)

### EasyLoader

| Easyloader                        | 下载链接                                                                                                                               | 备注 |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Watering Example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_WATERING_UNIT_With_M5Core.exe) | /    |

## 相关视频

- Unit Watering 示例展示

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/WATERING.mp4" type="video/mp4">
</video>

- Unit Watering UiFlow2 图形化编程

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113208291626800&bvid=BV11zsZefEP3&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
    <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/uDJ87WKIHqo?si=zg6k9o7XxwOeOOGh" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
