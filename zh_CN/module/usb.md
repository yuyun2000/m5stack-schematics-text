# Module USB

<span class="product-sku">SKU:M020</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/usb/usb_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/usb/usb_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/usb/usb_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/usb/usb_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/usb/usb_06.webp">
</PictureViewer>

## 描述

**Module USB** 是 M5Stack 堆叠模块系列中的 USB 扩展模块，基于 **MAX3421E** 方案，提供标准 USB 2.0 接口并支持 USB 主机/外设功能。模块通过 SPI 与主控通信，可为具备 SPI 接口的嵌入式系统快速补充 USB 能力；同时提供 GPIO 扩展能力（5 路输入、5 路输出），并引出 3V3、5V、GND 供电接口，便于外设连接与功能扩展。板载锂电池座，进一步提升移动部署与供电灵活性。该模块适用于 USB 外设接入、功能验证、原型开发与教学实验等场景。

## 注意事项

?> 兼容性说明 | Core2、CoreS3 主控不兼容此产品；受 3.3V 上电时序影响，USB 芯片将拉低 EN，由于其 EN 与 MCU EN 引脚相连，可能导致设备无法正常启动；如遇该问题，可将 M5-Bus 的 EN 引脚剪断以断开与 USB 芯片 EN 的连接。

## 产品特性

- MAX3421E USB 控制芯片方案
- 标准 USB 2.0 接口，支持 USB 主机/外设模式
- SPI 通信接口，便于与 M5 主控快速对接
- GPIO 扩展能力（5 路输入、5 路输出）
- 引出 3V3、5V、GND 电源接口
- 板载锂电池座，提升移动部署与供电灵活性

## 包装内容

- 1 x Module USB

## 应用场景

- USB 主机/外设功能扩展
- USB 键盘、鼠标等 HID 设备接入
- USB 存储设备读写与数据交互
- 嵌入式系统 USB 协议学习与教学实验
- 工业设备 USB 通讯接口扩展

## 规格参数

| 规格      | 参数                   |
| --------- | ---------------------- |
| 芯片型号  | MAX3421E               |
| USB 标准  | USB 2.0                |
| 通信接口  | SPI                    |
| GPIO 扩展 | 5 路输入、5 路输出     |
| 电源引脚  | 3V3、5V、GND           |
| 电池接口  | 板载锂电池座           |
| 产品重量  | 13 g                   |
| 毛重      | 25 g                   |
| 产品尺寸  | 54.2 x 54.2 x 12.8 mm  |
| 包装尺寸  | 60 x 57 x 17 mm        |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/usb/usb_sch_01.webp" width="80%">

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN    |
| -------- | ---- | ----- | ------ |
| GND      | 1    | 2     | INT    |
| GND      | 3    | 4     |        |
| GND      | 5    | 6     | EN     |
| SPI_MOSI | 7    | 8     |        |
| SPI_MISO | 9    | 10    |        |
| SPI_SCLK | 11   | 12    | 3V3    |
|          | 13   | 14    |        |
|          | 15   | 16    |        |
|          | 17   | 18    |        |
|          | 19   | 20    | SPI_CS |
|          | 21   | 22    |        |
|          | 23   | 24    |        |
|          | 25   | 26    |        |
|          | 27   | 28    | 5V     |
|          | 29   | 30    | BAT    |
::

## 数据手册

- [MAX3421E](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/MAX3421E_en.pdf)

## 软件开发

### Arduino

- [Module USB Mouse Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/USB_MAX3421E)

\#> 依赖库 | 在编译该程序前，你需要[点击此处下载相应的USB库](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Module/USB/Arduino/Library)并将其解压缩到 Arduino 库路径中.(`C:/Users/<user_name>/Documents/Arduino/libraries`)。

### UiFlow2

- [Module USB UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/usb.html)

### Easyloader

| Easyloader                                | 下载链接                                                                                      | 备注 |
| ----------------------------------------- | --------------------------------------------------------------------------------------------- | ---- |
| Module USB Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_USB.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201902/USB%20Interface.mp4" type="video/mp4">
</video>

## 版本变更

| 上市日期 | 产品变动                                       |
| -------- | ---------------------------------------------- |
| 2023.1   | 驱动芯片型号由 MAX3421EEHJ + 改为 MAX3421EETJ+ |
| -        | 首次发售                                       |