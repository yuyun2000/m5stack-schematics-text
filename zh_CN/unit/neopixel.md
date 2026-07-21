# Unit RGB LED

<span class="product-sku">SKU:A035/A035-B/A035-C/A035-D/A035-E</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neopixel/neopixel_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/762/A035-package.jpg">
</PictureViewer>

## 描述

**Unit RGB LED** 是一款可编程灯条，采用灯珠 SK6812。该灯条支持数字寻址，这意味着你可以单独控制灯条上的每一个单独的 LED 灯显示的颜色、亮度。使用单总线编程，可进行灯条拓展。需要注意的是，随着灯条连接数量的逐渐增加，伴随的功耗也会增加，因此在使用 LED 个数较多的 **Unit RGB LED** 灯条时，需要额外为其提供电源。

## 产品特性

- 可选长度: 10cm (15 LED) /20cm (29 LED) /0.5m (72 LED) /1m (144 LED) /2m (288 LED)
- 开发平台: Arduino，UiFlow (Blockly，Python)
- 可拓展长度

## 包装内容

- 1 x Unit RGB LED

## 规格参数

| 规格         | 参数                                                                 |
| ------------ | -------------------------------------------------------------------- |
| 灯珠型号     | SK6812 (3535)                                                        |
| 功率         | 18W/m                                                                |
| 数据传输速率 | 800K/s                                                               |
| 工作温度     | -40~80°C                                                             |
| 防水等级     | 裸板 - 不防水                                                        |
| 产品尺寸     | 10.0 x 100.0/10.0 x 200.0/10.0 x 500.0/10.0 x 1000.0/10.0 x 2000.0mm |
| 产品重量     | 4.0g/6.0g/10.0g/12.0g/34.0g                                          |
| 包装尺寸     | 138.0 x 93.0 x 8mm                                                   |
| 毛重         | 5.0g/7.0g/11.0g/13.0g/35.0g                                          |

## 操作说明

\#> 信号输入输出 | 灯条端部**白色**PCB 板处为灯条信号输入 (连接主控)，**黑色**PCB 板处用于延长拓展灯条。

## 管脚映射

### Unit RGB LED

::grove-table
| HY2.0-4P | Black | Red | Yellow     | White |
| -------- | ----- | --- | ---------- | ----- |
| PORT.B   | GND   | 5V  | LED Signal | NC    |
::

## 软件开发

### Arduino

- [FastLED Arduino 驱动库](https://github.com/FastLED/FastLED)
- [Unit RGB LED Display Rainbow Example](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/RGB_LED_SK6812/display_rainbow)

### UiFlow1

- [Unit RGB LED 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/NEOPIXEL/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neopixel/neopixel_uiflow_02.webp" width="60%">

### EasyLoader

| Easyloader                   | 下载链接                                                                                         | 备注 |
| ---------------------------- | ------------------------------------------------------------------------------------------------ | ---- |
| Unit RGB LED Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_NEOPIXEL.exe) | /    |

## 相关视频

**Unit RGB LED 的演示 - 01**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/LukeVideo/M5stack%20Neopixel%20Cosplay%20costume%20lights%20-%20super%20simple.mp4" type="video/mp4">
</video>
