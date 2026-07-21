# Hat DLight

<span class="product-sku">SKU:U134</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_dlight/hat_dlight_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_dlight/hat_dlight_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_dlight/hat_dlight_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_dlight/hat_dlight_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_dlight/hat_dlight_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_dlight/hat_dlight_06.webp">
</PictureViewer>

## 描述

**Hat DLight** 是一款适配 M5StickC/C Plus 系列的**数字环境光检测传感器**，硬件采用 **BH1750FVI** 照度传感器 IC（I2C 接口），内置 16bit AD 转换，支持 **1 ~ 65535 lx** 照度值检测。具有体积小、功耗低等特点，适用于各种照度检测与光控调节场景。

## 产品特性

- 适配 M5StickC/C Plus 系列
- I2C 通信接口 (addr: 0x23)
- 照度数字转换
- 光源依赖性小。(检测光源：白炽灯，荧光灯，卤素灯，白光 LED，太阳光均可)
- 检测范围 (1 - 65535 lx)

## 包装内容

- 1 x Hat DLight
- 1 x 双面胶

## 应用场景

- 光照度检测

## 规格参数

| 规格                 | 参数                  |
| -------------------- | --------------------- |
| 传感器型号           | BH1750FVI             |
| 照度检测范围         | 1 - 65535 lx          |
| 通信接口             | I2C 通信 @ 0x23       |
| 峰值灵敏度波长典型值 | 560nm                 |
| 工作电流             | < 3.3V@0.3mA          |
| AD 转换深度          | 16bit                 |
| 产品尺寸             | 24.0 x 24.9 x 13.7mm  |
| 产品重量             | 5.3g                  |
| 包装尺寸             | 138.0 x 93.0 x 15.0mm |
| 毛重                 | 7.4g                  |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_dlight/hat_dlight_sch_01.webp" width="80%">

## 管脚映射

- HAT DLight

| M5StickC   | G0  | G26 | 3.3V | GND |
| ---------- | --- | --- | ---- | --- |
| HAT DLight | SDA | SCL | VCC  | GND |

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/852/U118_model_size_page_01.png" width="50%" height="50%">

## 数据手册

- [BH1750FVI datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BH1750FVI.pdf)

## 软件开发

### Arduino

- [Hat DLight Arduino 驱动库](https://github.com/m5stack/M5-DLight)
- [Hat DLight Example - with M5StickC](https://github.com/m5stack/M5-DLight/blob/master/examples/Hat_DLight_M5StickC/Hat_DLight_M5StickC.ino)
- [Hat DLight Example - with M5StickC-Plus](https://github.com/m5stack/M5-DLight/blob/master/examples/Hat_DLight_M5StickCPlus/Hat_DLight_M5StickCPlus.ino)

### UiFlow1

- [Hat DLight UiFlow1 文档](/zh_CN/uiflow/blockly/hat/dlight)

### UiFlow2

- [Hat DLight UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/dlight.html)

## 相关视频

- 照度数值检测

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/HAT_DLIGHT_VIDEO.mp4" type="video/mp4">
</video>
