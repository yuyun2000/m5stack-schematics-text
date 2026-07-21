# Unit Light

<span class="product-sku">SKU:U021</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LIGHT/img-0b6d72e0-3533-4245-9c84-bfe6c24a50a6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LIGHT/img-d4a40e15-134b-465f-9c31-d5f8388b0e2a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LIGHT/img-1c3e73dd-9ccf-489d-9be1-948aad68fb54.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LIGHT/img-7f73b96e-4887-4506-b0e1-ca8f250071a8.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/LIGHT/img-884c70cd-7472-465e-b3f2-1e80c3470a8a.webp">
</PictureViewer>

## 描述

**Unit Light** 是一款光强度检测传感器。集成光敏电阻与 10K 可调电阻，能够对光照强度进行检测并设定光强门槛值。光敏电阻的阻值会随着入射光强度的增加而降低，依此检测其电压的变化，通过 AD 转换得到光强数据信息。为获得更精准的光强度检测数据，该 Unit 还采用 **LM393** 双差分比较器，用作比较光敏电阻和压敏电阻之间的差分电压。

## 产品特性

- 差分电压设计
- 模拟数字输出
- 开发平台: Arduino，UiFlow
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit Light
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 光控开关
- 太阳能庭院灯
- 红外监控摄像头

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 可调电阻 | 10K                  |
| 产品尺寸 | 32.0 x 24.0 x 8.0mm  |
| 产品重量 | 4.6g                 |
| 包装尺寸 | 138.0 x 93.0 x 9.0mm |
| 毛重     | 10.0g                |

## 原理图

- [Unit Light 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/709/U201-UNIT_LIGHT_SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/709/U201-UNIT_LIGHT_SCHE_page_01.png">
</SchViewer>

## 管脚映射

### Unit Light

::grove-table
| HY2.0-4P | Black | Red | Yellow         | White         |
| -------- | ----- | --- | -------------  | ------------  |
| PORT.B   | GND   | 5V  | Digital Output | Analog Output |
::

## 尺寸图

<img alt="image" width="100%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/LIGHT/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg">

## 结构文件

- [Unit Light 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U021_Unit_Light/Structures)

## 软件开发

### Arduino

- [Unit Light 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/LIGHT)

### UiFlow2

- [Unit Light UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/light.html)

## EasyLoader

| Easyloader                         | 下载链接                                                                                                                       | 备注 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---- |
| Unit Light Test Example Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/LIGHT/ezLoader-50479bee-bdc1-43eb-981b-1bf503710806.exe) | /    |

## 相关视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/Light_UNIT.mp4" type="video/mp4"></video>

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/LukeVideo/m5stack%20iot%20lighting%20part%202%20-%20light%20sensor%20control.mp4" type="video/mp4"></video>
