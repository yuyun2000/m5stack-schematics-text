# Unit Angle

<span class="product-sku">SKU:U005</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/angle/angle_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/angle/angle_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/800/U005-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/angle/angle_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/angle/angle_06.webp">
</PictureViewer>

## 描述

**Unit Angle** 是一款旋钮开关输入 Unit，其内置了一个 **10K** 的电位器，通过旋转旋钮能够改变其内部的电阻值。

电位器是具有三个引出端、阻值可按某种变化规律调节的电阻元件。根据此原理，ESP32 通过端口 B 获取电位器输出电压的大小，再经过 AD 转换得到对应的映射数据。在 “音量 、亮度调节，或是电机调速” 等需要连续信号控制的应用场景中，**Unit Angle** 会是一个不错的选择。

## 产品特性

- HY2.0-4P 接口，支持 [UiFlow](http://flow.m5stack.com) 、 [Arduino](http://www.arduino.cc) .
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit Angle
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 输出电压 | 0 ~ 2500mV            |
| 产品尺寸 | 32.0 x 24.0 x 22.0mm  |
| 产品重量 | 6.0g                  |
| 包装尺寸 | 138.0 x 93.0 x 21.0mm |
| 毛重     | 23.0g                 |

## 原理图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/800/U005_Sche.jpg" width="80%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/angle/angle_sch_02.webp" width="80%">

## 管脚映射

### Unit Angle

::grove-table
| HY2.0-4P | Black | Red | Yellow | White         |
| -------- | ----- | --- | ------ | ------------  |
| PORT.B   | GND   | 5V  | NC     | Analog Output |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/800/U005_Model_Size_page_01.png" width="100%">

## 结构文件

- [Unit Angle 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U005_Unit_Angle/Structures)

## 软件开发

### Arduino

- [Unit Angle Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/ANGLE)

### UiFlow1

- [Unit Angle UiFlow1 文档](/zh_CN/uiflow/blockly/unit/angle)

### UiFlow2

- [Unit Angle UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/angle.html)

### EasyLoader

| Easyloader                     | 下载链接                                                                                                                            | 备注 |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Angle example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_Angle_UNIT_With_M5Core.exe) | /    |

## 相关视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/Angle_UNIT.mp4" type="video/mp4"></video>
