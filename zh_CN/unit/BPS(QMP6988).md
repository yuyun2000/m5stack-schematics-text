# Unit Mini BPS v1.1

<span class="product-sku">SKU:U090-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/BPS(QMP6988)/img-61abcaeb-6126-4445-ba9c-10599ee0411c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/BPS(QMP6988)/img-da0dfb96-fca7-4f3f-b665-9ed9c10b3598.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/740/U090-B-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/BPS(QMP6988)/img-ad69b9ae-bcd5-430b-a1ad-3d7dee6de926.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/BPS(QMP6988)/img-d13305dc-f06c-485d-8c67-b4aa4ada24d9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/BPS(QMP6988)/img-b6196263-bfef-48b8-b6bc-89213882d8e8.webp">
</PictureViewer>

## 描述

**Unit Mini BPS v1.1** 是一款数字气压传感器单元，采用 QMP6988 气压传感器，单元采用 I2C 通信接口。本产品主要用于测量气压强度，相对精度可达到 ±0.039 hPa （±0.12 hPa，相当于 ±1 m 的高度差），测量范围广。此外，在芯片内部还集成了温度传感器，绝对精度 2°C。

## 产品特性

- 自带温度和压力传感器
- 高精度 (压力精度：±0.039hPa，绝对温度精度：2°C)
- 低电流损耗：21.4uA
- 开发平台: Arduino，UiFlow (Blockly，Python)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit Mini BPS v1.1
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 室内导航 (楼层检测)
- 测高仪，高度计
- 天气预测

## 规格参数

| 规格         | 参数                 |
| ------------ | -------------------- |
| 传感器       | QMP6988              |
| LDO          | HT7533               |
| 气压测量范围 | 30kPa to 110kPa      |
| 相对压力精度 | ±3.9                 |
| 压力分辨率   | 0.06Pa               |
| 温度分辨率   | 0.0002°C             |
| 温度测量范围 | -40 ~ 80°C           |
| 通信接口     | I2C 通信 @ 0x56      |
| 供电电压     | 5v                   |
| 产品尺寸     | 24.0 x 24.0 x 8.0mm  |
| 产品重量     | 3.3g                 |
| 包装尺寸     | 138.0 x 93.0 x 9.0mm |
| 毛重         | 7.0g                 |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/BPS(QMP6988)/img-4e77d8e1-09d6-43d6-a0da-d7e15d171c79.png" width="100%" />

## 管脚映射

### Unit Mini BPS v1.1

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/BPS(QMP6988)/img-b2c73882-6358-4799-bec0-c5ca736dfc20.png" width="100%" />

## 数据手册

- [QMP6988](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/enviii/QMP6988%20Datasheet.pdf)

## 软件开发

### Arduino

- [Unit Mini BPS v1.1 Example with M5Core](https://github.com/m5stack/M5Unit-ENV/tree/master/examples/Unit_BPS1.1_M5Core)
- [Unit Mini BPS v1.1 Example with M5Atom](https://github.com/m5stack/M5Unit-ENV/tree/master/examples/Unit_BPS1.1_M5Atom)
- [Unit Mini BPS v1.1 Example with M5AtomS3](https://github.com/m5stack/M5Unit-ENV/tree/master/examples/Unit_BPS1.1_M5AtomS3)
- [Unit Mini BPS v1.1 Example with M5AtomS3Lite](https://github.com/m5stack/M5Unit-ENV/tree/master/examples/Unit_BPS1.1_M5AtomS3Lite)
- [Unit Mini BPS v1.1 Example with M5Core2](https://github.com/m5stack/M5Unit-ENV/tree/master/examples/Unit_BPS1.1_M5Core2)
- [Unit Mini BPS v1.1 Example with M5StickC](https://github.com/m5stack/M5Unit-ENV/tree/master/examples/Unit_BPS1.1_M5StickC)
- [Unit Mini BPS v1.1 Example with M5StickCPlus](https://github.com/m5stack/M5Unit-ENV/tree/master/examples/Unit_BPS1.1_M5StickCPlus)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/BPS(QMP6988)/arduinoCase-1668071767199image.png" width="100%"/>

### UiFlow1

- [Unit Mini BPS v1.1 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/bps_v1.1)

### UiFlow2

learn>|![UiFlow2](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/uiflow2/uiflow2.0_banner_01.png)|[UiFlow2 Unit bps Docs](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/bps.html)|How to use Unit bps and related API instructions in the UiFlow2|

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113185944243017&bvid=BV13gsSe2EUZ&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/jyh07uxdIRI?si=lI9SNwmglk9qKsiW" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
