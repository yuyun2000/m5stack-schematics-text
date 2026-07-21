# Unit Laser RX

<span class="product-sku">SKU:U065</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/laser-rx/laser-rx_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/laser-rx/laser-rx_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/843/U065-01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/laser-rx/laser-rx_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/laser-rx/laser-rx_06.webp">
</PictureViewer>

## 描述

**Unit Laser RX** 是一款激光接收器 Unit，内部主要由激光晶体管构成。激光通信设备通过大气的无线连接。除了光束通过自由空间传输外，它们的工作方式类似于光纤链路。虽然发射器和接收器必须要求视距条件，但它们的好处是不需要广播权和埋地电缆。因其小巧，低功率并且不需要任何无线电干扰研究的特点，激光通信系统可以很容易地部署到各个位置。

## 产品特性

- 激光接收
- 配对 LASER.TX
- 2 x LEGO 兼容孔
- 开发平台: Arduino，UiFlow (Blockly，Python)

## 包装内容

- 1 x Unit Laser RX
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 空间激光通信系统.

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 接收频率 | 140KHz ~205KHz       |
| 产品尺寸 | 32.0 x 24.0 x 8.0mm  |
| 产品重量 | 3.7g                 |
| 包装尺寸 | 138.0 x 93.0 x 9.0mm |
| 毛重     | 9.3g                 |

## 原理图

- [Unit Laser RX 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/843/U065-UNIT_LASER_RX-SCHE.pdf)

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/laser-rx/laser-rx_sch_01.webp">
</SchViewer>

## 管脚映射

### Unit Laser RX

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | NC     | DOUT  |
::

## 尺寸图

- [Unit Laser RX 尺寸图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/843/U065_Model_Size.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/843/U065_Model_Size_sch_01.png" width="100%">

## 软件开发

### Arduino

- [Unit Laser RX 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/LASER)

### UiFlow1

- [Unit Laser RX UiFlow1 文档](/zh_CN/uiflow/blockly/unit/laser_rx)

### UiFlow2

- [Unit Laser RX UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/laser_rx.html)

### EasyLoader

| Easyloader                            | 下载链接                                                                                               | 备注 |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---- |
| Unit Laser RX Test Example Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/LASER/EasyLoader_LASER_RX.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/LASER-TX-RX.mp4" type="video/mp4" >
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113342744104784&bvid=BV1CEyqYhE8c&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/OwWc-fiTAm8?si=p9UX3TPLsronFQYW" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
