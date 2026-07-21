# Unit OP90

<span class="product-sku">SKU:U057</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/OP.90/img-103a3854-fbc1-43a3-9ebe-88cf6051e273.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/OP.90/img-2c594846-92c5-4f3b-b8d0-30e3133beb5f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/OP.90/img-8dbd5909-296e-4a7a-86ce-28b1de7e2358.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/OP.90/img-48d60ccd-42f8-4cf5-a590-e32dcd8054f3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/OP.90/img-85cbfb24-3eab-49c6-a107-596e8573c359.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/702/U057-weight.jpg">
</PictureViewer>

## 描述

**Unit OP90** 是一款 90° 的非接触式光电限位开关。该 Unit 上两侧分别为红外、发射接收器，正常工作时，发射侧会不断发射红外信号至接收侧，当有物体从中间经过并遮挡到红外信号时，输出端将产生动作信号，判断物体经过。常用于机械控制系统中，作为安全联锁或是光电计数装置。

## 产品特性

- 角度：90°
- 红外限位开关

## 包装内容

- 1 x Unit OP90
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 自动门
- 自动化机械控制

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 工作温度 | 0 ~ 40°C              |
| 产品尺寸 | 32.0 x 24.0 x 12.8mm  |
| 产品重量 | 4.2g                  |
| 包装尺寸 | 138.0 x 93.0 x 12.8mm |
| 毛重     | 9.6g                  |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/OP.90/img-2e3ce6f3-673a-4a87-9d0f-e355656ec33f.webp" width="100%" />

## 管脚映射

### Unit OP90

::grove-table
| HY2.0-4P | Black | Red | Yellow | White          |
| -------- | ----- | --- | ------ | -------------- |
| PORT.B   | GND   | 5V  | NC     | Digital Output |
::

## 尺寸图

<img alt="Model Size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/OP.90/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit OP90 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U057_Unit_OP90/Structures)

## 软件开发

### Arduino

- [Unit OP90 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/OP90.180_ITR9606)

### UiFlow2

- [Unit OP90 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/op90.html)

### EasyLoader

| Easyloader                | 下载链接                                                                                                                       | 备注 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---- |
| Unit OP90 Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/OP.90/ezLoader-2b8d81b2-4cf7-42eb-8a4e-02e35283edf1.exe) | /    |

## 相关视频

- Unit OP.90 案例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/OP90_UNIT.MP4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
		<iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113461812006275&bvid=BV1Q6myYgEyQ&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
		<iframe width="560" height="315" src="https://www.youtube.com/embed/OGxn7rOou_8?si=4BCM_fbwNdHB2upT" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
