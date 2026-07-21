# Unit ToF4M

<span class="product-sku">SKU:U172</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ToF4M/img-b393dca4-9143-4409-8753-0a776b8fe2a2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ToF4M/img-bb6247a0-82d1-4060-8725-b230c2affcae.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/746/U172-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ToF4M/img-71b71b77-67c9-4627-bc97-49017d1f4542.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ToF4M/img-06538272-4432-4bff-8a33-d06e7c7cbb6b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ToF4M/img-a19a8345-fd99-44d1-8fb5-3af26261688a.webp">
</PictureViewer>

## 描述

**Unit ToF4M** 是一款高精度距离传感器单元，采用 VL53L1CXV0FY/1 传感器，借助 Time-of-Flight（ToF）技术，能够在 4 米范围内精准测量距离。该传感器通过 I2C 输出（通讯地址：0x29），并可通过 Grove 口实现通信。

此传感器应用场景广泛，适用于机器人、自动驾驶汽车、无人机以及安防等领域。在具体应用中，它不仅能够测量物体的高度，还可用于检测物体是否存在以及监测物体的移动情况等。

## 产品特性

- 测量距离可达 4 米
- 快速响应时间
- 长寿命
- 编程平台
  - Arduino
  - UiFlow

## 包装内容

- 1 x Unit ToF4M
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 机器人
- 自动驾驶
- 无人机
- 安防

## 规格参数

| 规格         | 参数                 |
| ------------ | -------------------- |
| 传感器       | VL53L1CXV0FY/1       |
| 测量范围     | 4 ~ 400cm            |
| 分辨率       | 毫米级别             |
| 测量速度     | 毫秒级别             |
| 视角 (FoV)   | 15 ~ 27°             |
| 光源类型     | 激光 (ToF)           |
| 通信接口     | I2C 通信 @ 0x29      |
| 工作温度范围 | 0 ~ 40°C             |
| 产品尺寸     | 32.0 x 24.0 x 8.0mm  |
| 产品重量     | 4.3g                 |
| 包装尺寸     | 138.0 x 93.0 x 9.0mm |
| 毛重         | 10.0g                |

## 原理图

- [Unit ToF4M 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/626/UNIT-ToF4M.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/626/UNIT-ToF4M_sch_01.png">
</SchViewer>

## 管脚映射

### Unit ToF4M

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ToF4M/img-0c360975-630d-412d-a109-8f9f7e672f85.jpg" width="100%" />

## 数据手册

- [VL53L1CXV0FY/1](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-ToF4M/VL53L1CXV0FY.PDF)

## 软件开发

### Arduino

- [Unit ToF4M Arduino 驱动库](https://github.com/m5stack/M5Unit-ToF4M)

### UiFlow1

- [Unit ToF4M UiFlow1 文档](/zh_CN/uiflow/blockly/unit/tof4m)

### UiFlow2

- [Unit ToF4M UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/tof4m.html)

## 相关视频

- Unit ToF4M 应用例子

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-ToF4M/U172%20ToF4M%20Unit%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112868267656178&bvid=BV1vTvPe7EAt&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/586xK9gFycA?si=uwtI6-SALXrsd8YY" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| Product Compare          | [Unit-ToF4M](/zh_CN/unit/Unit-ToF4M) ![Unit-ToF4M](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-ToF4M/img-bb6247a0-82d1-4060-8725-b230c2affcae.webp) | [Unit-TOF](/zh_CN/unit/TOF) ![Unit-TOF](https://static-cdn.m5stack.com/resource/docs/products/unit/TOF/img-b7d05799-9772-4e4b-a8ef-8398360f57f1.webp) |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chip                     | VL53L1X                                                                                                                                                                 | VL53L0X                                                                                                                                               |
| Maximum Range            | 4 meters                                                                                                                                                                | 2 meters                                                                                                                                              |
| Typical Accuracy         | ±1-2%                                                                                                                                                                   | ±3%                                                                                                                                                   |
| Field of View (FoV)      | 27° (adjustable)                                                                                                                                                        | 25°                                                                                                                                                   |
| Adjustable Field of View | YES                                                                                                                                                                     | NO                                                                                                                                                    |
::
