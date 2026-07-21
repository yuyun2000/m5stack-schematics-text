# Unit PIR

<span class="product-sku">SKU:U004</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PIR/img-4647c010-1e57-4cc9-85e3-cbd450882074.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PIR/img-625b76c4-caf0-42c9-bc2d-8081d7a77e5e.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/701/U004_main_pictures_01.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PIR/img-958951eb-482b-443b-9e98-fb752819607b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/PIR/img-d3d367ff-4aa0-43f5-bff0-c32d9fe9e45c.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/701/U004_Weight.jpg">
</PictureViewer>

## 描述

Unit PIR 是一款高性能被动式热释电红外探测器，采用热释电红外传感技术，通过检测人体或物体所辐射的红外线变化来判定运动。该单元通过 Grove HY2.0-4P 接口通信，当检测到红外信号时输出高电平，并具备 2 秒延时和可重复触发机制（触发后持续检测将延长高电平时间）。它具有 500cm 的检测距离、< 100° 的广角感应范围，并采用 LEGO 兼容孔设计，可灵活对接 LEGO 结构或进行螺丝固定。适用于人体感应照明、安防报警、智能家居自动控制等多种需要进行运动检测的应用场景。

## 产品特性

- 检测距离：500cm
- 感应范围：< 100°（广角覆盖）
- 延时时间：2 秒（固定）
- 触发模式：可重复触发
- 通信接口：Grove HY2.0-4P
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit PIR
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 人体感应灯具
- 安防产品
- 自动感应电器设置

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 静态电流 | < 60uA                |
| 工作温度 | -20℃ ~ 80℃            |
| 产品尺寸 | 32.0 x 24.0 x 12.5mm  |
| 产品重量 | 5.1g                  |
| 包装尺寸 | 138.0 x 93.0 x 13.5mm |
| 毛重     | 10.0g                 |

## 原理图

- [Unit PIR 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/701/UNIT_PIR.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/701/UNIT_PIR_page_01.png">
</SchViewer>

## 管脚映射

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White          |
| -------- | ----- | --- | ------ | -------------- |
| PORT.B   | GND   | 5V  | NC     | Digital Output |
::

## 尺寸图

<img alt="Model Size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/PIR/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit PIR 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U004_Unit_PIR/Structures)

## 软件开发

### Arduino

- [Unit PIR Arduino 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/PIR)

### UiFlow1

- [Unit PIR UiFlow1 文档](/zh_CN/uiflow/blockly/unit/pir)

### UiFlow2

- [Unit PIR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/pir.html)

### EasyLoader

| Easyloader               | 下载链接                                                                                                                     | 备注 |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit PIR Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/PIR/ezLoader-a38c38d2-c621-4dc0-8401-48b53d12f16a.exe) | /    |

## 相关视频

- Unit PIR 案例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/PIR_UNIT.mp4" type="video/mp4"></video>
