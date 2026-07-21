# Unit DLight

<span class="product-sku">SKU:U136</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DLight Unit/img-0f153f02-a61e-4071-85a9-b6af7795684f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DLight Unit/img-dbcf35a7-cc4e-4376-92c9-5a4fe5ad75aa.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/710/U136-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DLight Unit/img-532176d9-4697-40a6-ad33-1315800859b8.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DLight Unit/img-d10b78e0-ab82-459d-973a-a55410331462.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DLight Unit/img-9a2ab6a9-46e1-4236-ac22-09cb2485b086.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/710/U136_Unit_DLight_weight.jpg">
</PictureViewer>

## 描述

**Unit DLight** 是一款 **数字环境光检测传感器**，硬件采用 **BH1750FVI** 照度传感器 IC （ I2C 接口 ），内置 16bit AD 转换支持 (1 ~ 65535 lx) 照度值检测。具有体积小，功耗低等特点。适用于各种照度检测，光控调节场景。

## 产品特性

- I2C 通信接口 (addr: 0x23)
- 照度数字转换
- 光源依赖性小 (检测光源：白炽灯，荧光灯，卤素灯，白光 LED，太阳光均可)
- 检测范围 (1 ~ 65535 lx)
- HY2.0-4P 接口

## 包装内容

- 1 x Unit DLight
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 光照度检测

## 规格参数

| 规格                 | 参数                      |
| -------------------- | ------------------------- |
| 传感器型号           | BH1750FVI                 |
| 照度检测范围         | 1 ~ 65535 lx              |
| 通信接口             | I2C 通信接口 (addr: 0x23) |
| 峰值灵敏度波长典型值 | 560nm                     |
| 工作电流             | < 5V@143uA                |
| AD 转换深度          | 16bit                     |
| 产品尺寸             | 32.0 x 24.0 x 8.0mm       |
| 产品重量             | 4.8g                      |
| 包装尺寸             | 138.0 x 93.0 x 9.0mm      |
| 毛重                 | 10.0g                     |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/DLight Unit/img-36ddf1b9-94ea-41d7-9162-0e31ee8f8130.webp" width="100%" />

## 管脚映射

### Unit DLight

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="image" width="100%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/DLight%20Unit/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg">

## 结构文件

- [Unit DLight 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U136_Unit_DLight/Structures)

## 数据手册

- [BH1750FVI datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BH1750FVI.pdf)

## 软件开发

### Arduino

- [Unit DLight Arduino 驱动库](https://github.com/m5stack/M5-DLight)
- [Unit DLight Example with M5Atom](https://github.com/m5stack/M5-DLight/blob/master/examples/Unit_DLight_M5Atom/Unit_DLight_M5Atom.ino)
- [Unit DLight Example with M5Core](https://github.com/m5stack/M5-DLight/blob/master/examples/Unit_DLight_M5Core/Unit_DLight_M5Core.ino)
- [Unit DLight Example with M5Core2](https://github.com/m5stack/M5-DLight/blob/master/examples/Unit_DLight_M5Core2/Unit_DLight_M5Core2.ino)
- [Unit DLight Example with M5StickC](https://github.com/m5stack/M5-DLight/blob/master/examples/Unit_DLight_M5StickC/Unit_DLight_M5StickC.ino)
- [Unit DLight Example with M5StickCPlus](https://github.com/m5stack/M5-DLight/blob/master/examples/Unit_DLight_M5StickCPlus/Unit_DLight_M5StickCPlus.ino)

### UiFlow1

- [Unit DLight UiFlow1 文档](/zh_CN/uiflow/blockly/unit/dlight)

### UiFlow2

- [Unit DLight UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/dlight.html)

### Home Assistant

- [Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_dlight_sensor)

## 相关视频

- 照度数值检测

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UNIT_DLIGHT_VIDEO.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113382355109349&bvid=BV1Gx1GYCEMh&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/csQPUZuenoY?si=ryEKcaGtfv4MjTqq" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
