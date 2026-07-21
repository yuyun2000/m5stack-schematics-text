# Unit Hall

<span class="product-sku">SKU:U084</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hall/hall_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hall/hall_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hall/hall_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hall/hall_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/hall/hall_06.webp">
</PictureViewer>

## 描述

**Unit Hall**是一款霍尔传感器。内部集成 3 个 A3144E 霍尔感应开关，通过 74 系列门集成电路进行逻辑处理，当有 S 磁极物体靠近 hall 正面或 N 磁极靠近 hall 背面时，可以产生低电平信号，同时内部的 LED 指示灯会点亮。霍尔传感器适用于门磁报警、接近感应、转速测量等场景。

## 产品特性

- 单极霍尔开关量感应
- 响应速度快，灵敏度高
- 带状态指示灯
- 低电平输出
- 可与积木搭配使用

## 包装内容

- 1 x Unit Hall
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 磁铁

## 应用场景

- 门磁报警
- 磁场接近感应
- 转速测量

## 规格参数

| 规格        | 参数                 |
| ----------- | -------------------- |
| 霍尔传感器  | A3144E \* 3          |
| 逻辑处理 IC | 74HC08D              |
| 状态指示    | 红色 LED             |
| 输出电平    | 低电平有效           |
| 产品尺寸    | 32.0 x 24.0 x 8.0mm  |
| 产品重量    | 4.2g                 |
| 包装尺寸    | 138.0 x 93.0 x 9.0mm |
| 毛重        | 10.0g                |

## 原理图

<img src= "https://static-cdn.m5stack.com/resource/docs/products/unit/hall/hall_sch_01.webp" width="80%">

## 管脚映射

### Unit Hall

::grove-table
| HY2.0-4P | Black | Red | Yellow | White          |
| -------- | ----- | --- | ------ | -------------  |
| PORT.B   | GND   | 5V  | NC     | Digital Output |
::

## 尺寸图

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/hall/module_size.jpg" width="100%" />

## 数据手册

- [A3144E](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/3141Thru3144E_HALL.PDF)

## 软件开发

### Arduino

- [Unit Hall 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/HALL).

### UiFlow2

- [Unit Hall UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/hall_effect.html)

### EasyLoader

| Easyloader                | 下载链接                                                                                                                           | 备注 |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Hall Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_HALL_UNIT_With_M5Core.exe) | /    |

## 相关视频

- 屏幕显示磁感状态，低电平有效

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/HALL_Unit.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113463791782704&bvid=BV1H8mUYeEFa&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/LJVO2HJA4TU?si=vPe7hsfpyD3Iip83" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
