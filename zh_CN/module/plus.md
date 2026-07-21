# Module Plus

<span class="product-sku">SKU:M019</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/plus/plus_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/plus/plus_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/plus/plus_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/plus/plus_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/plus/plus_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/plus/plus_06.webp">
</PictureViewer>

## 描述

**Module Plus** 是 M5Stack 堆叠模块系列中的一款功能增强型模块。模块配备了锂电池（500mAh）、齿轮电位器、红外发射器。集成 MEGA328 ，提供麦克风接口焊盘，并且对 M5Core 的端口 PORT.B (GPIO)、PORT.C (UART) 进行了拓展。Module Plus 能够升级你的硬件资源，为你带来更好的开发体验。

## 产品特性

- 400mAh 锂电池
- 可编程齿轮电位器
- 红外发射器
- PORT B & PORT C

## 包装内容

- 1 x Module Plus

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 通信接口 | I2C 通信 @ 0x62      |
| 产品尺寸 | 64.3 x 24.0 x 8.0mm  |
| 产品重量 | 20.0g                |
| 包装尺寸 | 62.0 x 58.0 x 17.0mm |
| 毛重     | 30.0g                |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/plus/plus_sch_01.webp" width="80%">

## 管脚映射

### Mega328 ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

### M5-Bus

::m5-bus-table
| PIN    | LEFT | RIGHT | PIN    |
| ------ | ---- | ----- | ------ |
| GND    | 1    | 2     |        |
| GND    | 3    | 4     | PORT.B |
| GND    | 5    | 6     |        |
|        | 7    | 8     |        |
|        | 9    | 10    | PORT.B |
|        | 11   | 12    |        |
|        | 13   | 14    |        |
| PORT.C | 15   | 16    | PORT.C |
| SCL    | 17   | 18    | SDA    |
|        | 19   | 20    |        |
|        | 21   | 22    | IR_TX  |
|        | 23   | 24    |        |
|        | 25   | 26    |        |
|        | 27   | 28    | 5V     |
|        | 29   | 30    |        |
::

## 软件开发

### Arduino

- [Module Plus Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/PLUS)

### UiFlow1

- [Module Plus UiFlow1 文档](/zh_CN/uiflow/blockly/module/plus)

### UiFlow2

- [Module Plus UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/plus.html)

### 内置固件

- [Module Plus 内置固件](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Module/PLUS/firmware_328p)

### Easyloader

| Easyloader                                 | 下载链接                                                                                       | 备注 |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------- | ---- |
| Module Plus Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_PLUS.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201812/M5Stack%20Encoder.mp4" type="video/mp4">
</video>
