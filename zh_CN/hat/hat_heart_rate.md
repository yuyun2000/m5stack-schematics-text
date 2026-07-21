# Hat Heart

<span class="product-sku">SKU:U118</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_heart_rate/hat_heart_rate_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_heart_rate/hat_heart_rate_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_heart_rate/hat_heart_rate_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_heart_rate/hat_heart_rate_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_heart_rate/hat_heart_rate_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_heart_rate/hat_heart_rate_06.webp">
</PictureViewer>

## 描述

**Hat Heart** 是一款血氧心率传感器。集成 **MAX30102**，提供完整的脉搏血氧仪和心率传感器系统解决方案。这是一款非插入式的血氧心率传感器， 其检测原理是通过红外 led 灯照射，检测携带氧气和非携带氧气的红血球数量比例，从而得到血氧含量。该传感器采用 I2C 通信接口，内部集成红外发光二极管，光电探测器，光学元件和低噪声电子设备，具备一定的环境光抑制功能使得测量结果更加准确。

**使用方法：程序运行后，将手指稳定保持固定压力的放置在检测区域。**

## 产品特性

- 心率监测器和脉搏血氧仪传感器
- LED 反光解决方案
- 集成式防护玻璃，坚固耐用表现
- 可编程的采样率和 LED 电流
- 快速的数据输出能力
- 高采样率
- 强大的运动伪影弹性
- 高信噪比

## 包装内容

- 1 x Hat Heart
- 1 x 双面胶贴纸

## 应用场景

- 可穿戴设备
- 心率血氧采集器
- 智慧医疗

## 规格参数

| 规格       | 参数                  |
| ---------- | --------------------- |
| 传感器型号 | MAX30102              |
| 通信接口   | I2C 通信 @ 0x57       |
| 产品尺寸   | 24.9 x 24.0 x 13.7mm  |
| 产品重量   | 5.1g                  |
| 包装尺寸   | 136.0 x 92.0 x 14.0mm |
| 毛重       | 8.0g                  |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_heart_rate/hat_heart_rate_sch_01.webp" width="80%">

## 管脚映射

| M5StickC       | G26 | G0  | 3.3V | GND |
| -------------- | --- | --- | ---- | --- |
| HEART RATE HAT | SCL | SDA | 3.3V | GND |

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/852/U118_model_size_page_01.png" width="50%" height="50%">

## 数据手册

- [MAX30102](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/heart_rate/MAX30102_Datasheet.pdf)

## 软件开发

### Arduino

- [Hat Heart Example - with M5StickC-Plus](https://github.com/m5stack/M5StickC-Plus/blob/master/examples/Hat/HEART_RATE_MAX30102/HEART_RATE_MAX30102.ino)

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_heart_rate/hat_heart_rate_uiflow_01.webp" width="65%">

- [Hat Heart Arduino 快速上手](/zh_CN/arduino/projects/hat/hat_heart)

### UiFlow1

- [Hat Heart UiFlow1 文档](/zh_CN/uiflow/blockly/hat/heart_rate)

### UiFlow2

- [Hat Heart UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/heart.html)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/HEART_RATE_HAT.mp4" type="video/mp4">
</video>
