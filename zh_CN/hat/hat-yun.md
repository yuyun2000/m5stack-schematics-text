# Hat Yun

<span class="product-sku">SKU:U070</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-yun/hat-yun_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-yun/hat-yun_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-yun/hat-yun_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-yun/hat-yun_04.webp">
</PictureViewer>

## 描述

**Hat Yun**是一款云朵形状的多功能环境信息采集底座。内置温湿度传感器**SHT20**、气压传感器**BMP280**、光敏电阻，以及 14 颗 RGB LED。内嵌**STM32F030F4**控制芯片，提供简洁高效的程序调用接口。精致的设计外观，在实现精准环境信息数据采集的同时具备一定的装饰效果。

底座针对 M5StickC 设计，预留相同数目的排针与空间，能够与 M5StickC 顶部的拓展端口完美插接。整体结构采用三层设计，上下两层 PCB 板，分别充当固定结构与主体电路。为利于电路的长时间工作，板上还提供了独立外部电源接口。中层为导光亚克力件，为获得更好的灯光显示效果，亚克力外轮廓切割面部分采用了打磨工艺，目的在于编程控制灯光时，能够有效减少光的散射，使其呈现更均匀饱和的灯光效果。板上嵌入 2 个 6 x 4.0mm 磁铁并预留 1 个挂钩孔，用户能够便捷地将它安装在生活中的任意角落。

## 产品特性

- 控制芯片**STM32F030F4**
- 温湿度传感器**SHT20**
- 气压传感器**BMP280**
- 光敏电阻
- 14 x SK6812 4020 RGB LED
- 三层结构设计:
  - 1 x 挂钩孔
  - 2 x 6 x 4mm 磁铁嵌入
  - 1 x 亚克力外轮廓切割面加工打磨
- 开发平台: Arduino, UiFlow (Blockly, Python)

## 包装内容

- 1 x Hat Yun
- 2 x 杜邦线

## 应用场景

- 环境信息采集
- 智能家居装饰

## 规格参数

| 规格     | 参数                                         |
| -------- | -------------------------------------------- |
| MCU      | STM32F030F4P6                                |
| 通信协议 | I2C:SHT20（0x40）,BMM280（0x76）,YUN（0x38） |
| 产品重量 | 7g                                           |
| 毛重     | 15g                                          |
| 产品尺寸 | 75 x 55 x 5mm                                |
| 包装尺寸 | 100 x 85 x 20mm                              |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-yun/hat-yun_sch_01.webp" width="70%">

## 管脚映射

| M5StickC | GND | 5V OUT | G26 | G0  | G36 | BAT | 3V3   | 5V IN  |
| -------- | --- | ------ | --- | --- | --- | --- | ----- | ------ |
| YUN HAT  | GND | +5V    | SCL | SDA | /   | BAT | +3.3V | +5V IN |

## 数据手册

- [SHT20](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/SHT20_Datasheet_en.pdf)
- [BMP280](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/BMP280-DS001-11_en.pdf)

## 软件开发

### Arduino

- [Hat Yun Example](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/YUN)

### UiFlow1

- [Hat Yun UiFlow1 文档](/zh_CN/uiflow/blockly/hat/yun)

### Easyloader

| Easyloader         | 下载链接                                                                                           | 备注 |
| ------------------ | -------------------------------------------------------------------------------------------------- | ---- |
| Hat Yun Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/YUN/EasyLoader_YUN_HAT.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/YUN-HAT.mp4" type="video/mp4" >
</video>
