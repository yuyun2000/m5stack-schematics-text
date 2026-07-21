# Unit NeoFlash

<span class="product-sku">SKU:A042</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neoflash/neoflash_01.webp">
</PictureViewer>

## 描述

**Unit NeoFlash** 是一款 RGB LED 灯板。集成 192 个 RGB LED (24 x 8)，与 PIR 人体感应 Unit，且提供 3 个 I2C 拓展接口。灯板通过 PORT B 接口与 M5Core 进行连接。（ RGB LED 连接 G26 、PIR 人体感应连接至 G36。）灯板背部安装磁铁，可以将其放置在金属物体表面吸附固定。

人体红外感应 PIR 传感器接 M5Core 的 G36。

## 产品特性

- 人体感应
- 开发平台: Arduino，UiFlow (Blockly，Python)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit NeoFlash
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 规格参数

| 规格       | 参数            |
| ---------- | --------------- |
| RGB LED    | x 192           |
| PORTA 接口 | x 3             |
| 孔数量     | 40              |
| 产品重量   | 119g            |
| 毛重       | 131g            |
| 产品尺寸   | 220 x 53 x 10mm |
| 包装尺寸   | 220 x 59 x 10mm |

## 操作说明

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neoflash/neoflash_02.webp">

## 管脚映射

### Unit NeoFlash

::grove-table
| HY2.0-4P | Black | Red | Yellow     | White     |
| -------- | ----- | --- | ---------- | --------- |
| PORT.B   | GND   | 5V  | LED Signal | PIR Input |
::

## 软件开发

### Arduino

- [FastLED Arduino 驱动库](https://github.com/FastLED/FastLED)

该案例将展示基于网络的 PIR 人体感应时钟。当检测到人体靠近时，灯板点亮显示实时时间，当检测信号消失，则熄灭灯板.

- [Unit NeoFlash PIR Example](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/NEOFLASH_SK6812_PIR)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neoflash/neoflash_03.webp">

### UiFlow1

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/neoflash/neoflash_uiflow_01.webp" width="65%">

### EasyLoader

| Easyloader                    | 下载链接                                                                                         | 备注 |
| ----------------------------- | ------------------------------------------------------------------------------------------------ | ---- |
| Unit NeoFlash Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_NEOFLASH.exe) | /    |

## 相关视频

**Neoflash 在 UiFlow 上的使用**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/%E6%95%99%E7%A8%8B/NeoFlash/E1%20-%20Neoflash%20%E4%BE%8B%E7%A8%8B%EF%BC%88UIFlow%20Tutorials%202%EF%BC%89.mp4" type="video/mp4">
</video>
