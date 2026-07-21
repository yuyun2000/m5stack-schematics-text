# Unit MIC

<span class="product-sku">SKU:U096</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mic/mic_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mic/mic_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/733/U096-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mic/mic_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mic/mic_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mic/mic_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mic/mic_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mic/mic_09.webp">
</PictureViewer>

## 描述

**Unit MIC** 是一款声音传感器，内置全指向型驻极体麦克风，通过麦克风前置放大器 MAX4466 对信号进行放大输出。该放大器能有效抑制电源噪声与共模噪声，输出信号声音还原度高，可在嘈杂环境中使用。该 Unit 不仅可以输出模拟信号，也可以输出数字电平信号，内置 LM393 双电压比较器，可通过调节 10K 可调电阻，设定比较电压阈值。该传感器非常适用于声电转换、声控开关等项目。

## 产品特性

- 声音采样 / 音频录制
- 内置麦克风前置放大器 MAX4466
- 全指向，52dB 灵敏度
- 模拟与数字信号输出
- 内置电压比较器与可调电阻，阈值可调
- 开发平台: Arduino，UiFlow (Blockly，Python)
- HY2.0-4P 接口
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit MIC
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 声电转换
- 声控开关

## 规格参数

| 规格                  | 参数                 |
| --------------------- | -------------------- |
| 麦克风灵敏度 / 信噪比 | 52dB/40dB            |
| 输出信号              | 模拟 / 数字          |
| 输入电压              | 5V                   |
| 产品尺寸              | 32.0 x 24.0 x 8.0mm  |
| 产品重量              | 4.6g                 |
| 包装尺寸              | 138.0 x 93.0 x 9.0mm |
| 毛重                  | 10.0g                |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mic/mic_sch_01.webp" width="100%">

## 管脚映射

### Unit MIC

::grove-table
| HY2.0-4P | Black | Red | Yellow         | White         |
| -------- | ----- | --- | -------------  | ------------  |
| PORT.B   | GND   | 5V  | Digital Output | Analog Output |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/mic/Module%20Size.jpg" width="80%">

## 数据手册

- [MAX4466](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/MAX4466_V2.PDF)
- [LM393](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/LM393.PDF)

## 软件开发

### Arduino

- [Unit MIC 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/MIC_Unit)

### EasyLoader

| Easyloader               | 下载链接                                                                                                                          | 备注 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit MIC Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_MIC_Unit_With_M5Core.exe) | /    |

## 相关视频

- 显示麦克风采集 AD 值

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/MIC.mp4">
</video>
