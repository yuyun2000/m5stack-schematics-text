# Hat PIR

<span class="product-sku">SKU:U054</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-pir/hat-pir_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-pir/hat-pir_02.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/hat/hat-pir/U054.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-pir/hat-pir_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-pir/hat-pir_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/853/U054-weight.jpg">
</PictureViewer>

## 描述

**Hat PIR**是一款兼容 M5SticKC 的人体红外传感器，它属于 “被动式热释电红外探测器”，通过检测由人体或物体发射、反射的红外辐射进行判断工作。当检测到红外时，输出高电平，并进行一段时间的延时（期间保持高电平且允许重复触发），直至触发信号消失（恢复低电平）。

## 产品特性

- 检测距离: 500cm
- 延时时间: 2s
- 感应范围: < 100°
- 静态电流: < 60uA
- 工作温度: -20 - 80 °C

## 包装内容

- 1 x Hat PIR
- 1 x 双面胶

## 应用场景

- 人体感应灯具
- 安防产品
- 自动感应电器设置

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 产品尺寸 | 24.0 x 25.0 x 20.0mm  |
| 产品重量 | 5.4g                  |
| 包装尺寸 | 136.0 x 92.0 x 21.0mm |
| 毛重     | 7.6g                  |

## 操作说明

\#> 注意事项:| 检测触发后存在 2 秒延时。

## 原理图

- [Hat PIR原理图PDF](https://github.com/m5stack/M5-Schematic/blob/master/Hat/StickHat_PIR.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/853/StickHat_PIR_page_01.png">

## 管脚映射

| StickC  | G36 | 3.3V | GND |
| ------- | --- | ---- | --- |
| HAT PIR | OUT | 3.3V | GND |

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/853/U054_model_size_page_01.png">

## 软件开发

### Arduino

- [Hat PIR 测试程序](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/PIR)

### UiFlow1

- [Hat PIR UiFlow1 文档](/zh_CN/uiflow/blockly/hat/pir)

### UiFlow2

- [Hat PIR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/pir.html)

### EasyLoader

| Easyloader         | 下载链接                                                                                               | 备注 |
| ------------------ | ------------------------------------------------------------------------------------------------------ | ---- |
| Hat PIR Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/HAT/EasyLoader_PIR_HAT.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/PIR_HAT.mp4" type="video/mp4">
</video>
