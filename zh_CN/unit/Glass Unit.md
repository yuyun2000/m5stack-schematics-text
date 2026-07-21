# Unit Glass

<span class="product-sku">SKU:U158</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass Unit/img-4384183e-b663-4dfc-bc3f-5070166c6e2b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass Unit/img-b4a18f37-d10d-49ef-b047-ba0e7fccd96c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass Unit/img-46712c1f-837b-458b-b748-705fc2c257d4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass Unit/img-52548b3e-3459-49a3-a436-e2bb61a90f3c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass Unit/img-284d30f4-69be-4188-a9e7-d29cf3d3d08e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass Unit/img-b550040d-4a7e-4771-a83a-d096daf1251c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass Unit/img-fc5ff9fe-829a-4cda-9548-360f2425125b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass Unit/img-467f2a5f-e95c-4e39-b99a-baf0f1505c72.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass Unit/img-3e65950c-839c-4853-aa32-77064fdbba65.webp">
</PictureViewer>

## 描述

**Unit Glass** 是一款 **1.51 英寸** 的 **透明 OLED** 拓展屏幕单元。采用 **STM32 + SSD1309** 驱动方案，**分辨率为 128 x 64**，单色显示，**透明区域为 128 x 56**。MCU 采用 **STM32F030F4P6**，内部集成 **两路输入按键** 和 **一路蜂鸣器**，方便用户与屏幕互动，支持通过 I2C（**0x3D**）通信接口进行控制与固件升级。该透明 OLED 屏幕拓展适合嵌入到各种家居产品或者各种控制设备中作为显示面板。

## 产品特性

- 128×56 透明像素（128×64 总像素）
- 显示区域 35.05×18mm
- 玻璃面积 42.04×27.22mm
- 1 位颜色深度
- I2C 通信（地址 0x3D）
- 支持编程平台：Arduino、UiFlow

## 包装内容

- 1 x Unit Glass
- 1 x HY2.0-4P Grove 连接线（20cm）

## 应用场景

- 家居产品
- 控制设备
- 显示面板

## 规格参数

| 规格     | 参数                    |
| -------- | ----------------------- |
| MCU      | STM32F030F4P6           |
| 屏幕     | 1.51 英寸透明 OLED 屏幕 |
| 分辨率   | 128 x 64                |
| 显示颜色 | 蓝色                    |
| 显示区域 | 35.05 x 18mm            |
| 面板尺寸 | 42.04 x 27.22 x 1.25mm  |
| 视角方向 | 全视角                  |
| 工作温度 | 0 ~ 40°C                |
| 逻辑电压 | 3.3V                    |
| 通信接口 | I2C 通信 @ 0x3D         |
| 产品尺寸 | 53.0 x 42.0 x 6.0mm     |
| 产品重量 | 10.1g                   |
| 包装尺寸 | 138.0 x 93.0 x 7.0mm    |
| 毛重     | 16.4g                   |

## 原理图

- [Unit Glass 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/612/Sch_UNIT-GLASS.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/612/Sch_UNIT-GLASS_sch_01.png">
</SchViewer>

## 管脚映射

### Unit Glass

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass Unit/img-81ef47d6-593a-4f70-96c8-1cedd6038c53.png" width="100%">

## 数据手册

- [STM32F030F4P6](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/STM32F030F4P6.PDF)
- [SSD1309](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/U158%20unit%20glass/SSD1309.pdf)
- [128\*64 Transparent OLED](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/U158%20unit%20glass/ZJY-2856KLBAG01.pdf)

## 软件开发

### Arduino

- [Unit Glass Arduino 教程](/zh_CN/arduino/projects/unit/unit_glass)

### UiFlow1

- [Unit Glass UiFlow1 文档](/zh_CN/uiflow/blockly/unit/glass)

### UiFlow2

- [Unit Glass UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/glass.html)

### 内置固件

- [Unit Glass 内置固件](https://github.com/m5stack/M5Unit-GLASS-Internal-FW)

### 通信协议

- [Unit Glass I2C Protocol PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/612/UnitGlass_I2C_Protocol.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/612/UnitGlass_I2C_Protocol.png" width="100%">

## 相关视频

- UiFlow2 Glass Unit

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112970726115255&bvid=BV1jTe3eqEew&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/qERIEFdp5iM?si=nqrHja0lQEZz29ev" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
