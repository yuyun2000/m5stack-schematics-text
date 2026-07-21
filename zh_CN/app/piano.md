# Piano

<span class="product-sku">SKU:A047</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/piano/piano_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/piano/piano_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/piano/piano_03.webp">
</PictureViewer>

## 描述

**Piano** 是一款触摸板钢琴。配备两颗 **TS20** 触摸传感器，通过 I2C 协议与 M5Core 进行通信，I2C 地址分别为 0x6A 和 0x7A。通过触摸控制钢琴的发声，适合应用在 STEM 教育与音乐表演场景。

## 包装内容

- 1 x Piano

## 规格参数

| 规格     | 参数            |
| -------- | --------------- |
| 产品重量 | 114.0g          |
| 毛重     | 115.0g          |
| 产品尺寸 | 240 x 53 x 8mm  |
| 包装尺寸 | 250 x 55 x 6mm |

## 管脚映射

### 触摸芯片 TS20 & LED 灯

| ESP32 Chip | G7    | G6  | G5  | G26 | G2         |
| ---------- | ----- | --- | --- | --- | ---------- |
| TS20       | RESET | EN  | SCL | SDA | /          |
| RGB LED    | /     | /   | /   | /   | Signal Pin |

## 软件开发

### Arduino

- [Piano 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/blob/master/App/PIANO/Arduino/M5PIANO/M5PIANO.ino)

### Easyloader

| Easyloader            | 下载链接                                                                                                                 | 备注 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---- |
| Piano Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/APPLICATION/EasyLoader_PIANO_APPLICATION.exe) | /    |

## 相关视频

- 触摸钢琴键盘，驱动扬声器发出不同的音调。

<video id="example_video" controls>
   <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/App/PIANO.mp4" type="video/mp4">
</video>
