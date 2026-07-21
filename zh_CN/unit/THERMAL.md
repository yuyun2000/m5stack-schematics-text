# Unit Thermal

<span class="product-sku">SKU:U016</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/THERMAL/img-92fc4d7d-3b52-4ee6-b483-80d7209289e3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/THERMAL/img-55d31a15-2d3f-4f36-9b98-ad457a8be664.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/708/U016-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/THERMAL/img-5cbd4577-b064-4e15-ba52-95063770d133.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/THERMAL/img-0ee52714-e57d-4ca9-86bf-d560f65ff9df.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/THERMAL/img-7d138fbd-75c5-4e70-b7cb-235a36bded19.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/THERMAL/img-a121057a-6406-48a3-b0c6-d0928714f79c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/THERMAL/img-4f95711d-53a0-41c4-99e0-be4db4023c2e.webp">
</PictureViewer>

## 描述

**Unit Thermal** 是一款高性能红外热成像单元。它内置 MLX90640 热电堆传感器阵列，能够通过检测物体表面的红外辐射，生成分辨率达 32×24 像素的热成像图片，直观呈现温度分布。该单元通过 I2C 协议 (地址 0x33) 通信，具备 110°×75° 的广角视野、-40°C ~ 300°C 的宽温测温范围以及高达 64Hz 的可编程刷新率，并采用 LEGO 兼容孔设计，可灵活对接 LEGO 结构或进行螺丝固定。适用于非接触式测温、安防监控、工业设备诊断及智能家居感知等多种热视觉应用场景。

## 产品特性

- 成像分辨率：32 × 24 像素（768 个测温点）
- 视场角：110° × 75°
- 测温范围：-40°C ~ 300°C
- 测温精度：±1.5°C
- 刷新频率：0.5Hz ~ 64Hz（可编程）
- 通信接口：I2C (0x33)
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit Thermal
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 高精度的非接触性测温器
- 生物移动检测
- 可视化红外成像

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 通信接口 | I2C 通信 @ 0x33      |
| 工作电流 | 23mA                 |
| 视场角   | 110°×75°             |
| 测温范围 | ﹣40°C ~ 300°C       |
| 精度     | ±1.5°C               |
| 刷新频率 | 0.5Hz ~ 64Hz         |
| 工作温度 | ﹣40°C ~ 85°C        |
| 产品尺寸 | 32.0 x 24.0 x 8.6mm  |
| 产品重量 | 5.1g                 |
| 包装尺寸 | 138.0 x 93.0 x 9.6mm |
| 毛重     | 10.1g                |

## 原理图

- [Unit Thermal 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/708/U016-UNIT_THERMAL-SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/708/U016-UNIT_THERMAL-SCHE_page_01.png">
</SchViewer>

## 管脚映射

### Unit Thermal

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="size" width="100%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/thermal/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg">

## 结构文件

- [Unit Thermal 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U016_Unit_Thermal/Structures)

## 数据手册

- [MLX90640 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/MLX90640-Datasheet-Melexis_en.pdf)

## 软件开发

### Arduino

- [Unit Thermal Test Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/THERMAL_MLX90640)
- [Unit Thermal Test Example with M5Core2](https://github.com/m5stack/M5Core2/tree/master/examples/Unit/THERMAL_MLX90640)

### UiFlow2

- [Unit Thermal UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/thermal.html)

### EasyLoader

| Easyloader                   | 下载链接                                                                                                                         | 备注 |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Thermal Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/THERMAL/ezLoader-779bfbf3-0155-4277-ab85-8a07c024a190.exe) | /    |

## 相关视频

-Unit Thermal 的演示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201811/Infrared%20Thermal%20Imaging.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113157204938646&bvid=BV18atGemEWi&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/50X_uDQMNQU?si=BgUVHv6CPZZsHtRI" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
