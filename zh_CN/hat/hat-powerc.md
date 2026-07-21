# Hat PowerC

<span class="product-sku">SKU:U081</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-powerc/hat-powerc_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-powerc/hat-powerc_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-powerc/hat-powerc_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-powerc/hat-powerc_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-powerc/hat-powerc_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-powerc/hat-powerc_06.webp">
</PictureViewer>

## 描述

**Hat PowerC** 是一款专为 M5StickC 设计的充电模块，内置 IP3005 高精度锂电池保护 IC 与 IP5209 电源管理 IC，采用 I2C 通信协议与主机 M5StickC 进行数据传输，通过编程可查看电压、电流等信息。模块背面电池座可安装 2 节 16340 电池，通过充电模块对电池进行充电，也可作为充电宝通过电池对外供电。此外提供了 XH1.25 插头锂电池充电接口。模块提供一个 I2C 接口用于连接 I2C 外设，Type-C 接口用于电源输入，USB-A 母座用于电源输出，电压输出为 5V/1.5A，输入电压为 5V。模块配有一个独立开关，按一次开启，连按两次关闭。

## 产品特性

- 同步开关充放电
  - 2.4A 同步升压转换，2.1A 同步开关充电
  - 升压效率最高达 96%
  - 充电效率最高达 97%
  - 内置电源路径管理，支持边充边放
- 充电
  - 自适应充电电流调节，匹配所有适配器
  - 充电电压精度：±0.5%,
  - 支持 4.20V、4.30V 和 4.35V 电池
  - 支持电池温度 NTC 比较
- 电量显示
  - 内置 14bit ADC 和电量计
  - 支持 5 / 4/ 3 颗 LED 电量显示
  - 电池电量曲线可设置，显示灯更均匀
- 功能丰富
  - 自动检测手机插入和拔出
  - 集成手机充电电流智能识别 DCP
- 低功耗
  - 智能识别负载，自动进待机
  - 待机功耗小于 100 µA
- I2C 接口 (地址 0x75)

## 包装内容

- 1 x Hat PowerC

## 应用场景

- 充电宝
- 电池充电器

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| 通信接口 | I2C 通信 @ 0x75       |
| 产品尺寸 | 55.0 x 35.0 x 25.0mm  |
| 产品重量 | 55.0g                 |
| 包装尺寸 | 100.0 x 96.0 x 70.0mm |
| 毛重     | 68.0g                 |

## 原理图

- [Hat PowerC Schematic PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Hat/POWERC_HAT_SCH.pdf)

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-powerc/hat-powerc_sch_01.webp" width="60%">

## 管脚映射

| M5StickC | G0    | G26   | 5V  | GND   |
| -------- | ----- | ----- | --- | ----- |
| PowerC   | SDA   | SCL   | 5V  | GND   |
| PortA    | YELLO | WHITE | RED | BLACK |

## 数据手册

- [IP5209 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/IP5209.pdf)
- [IP3005 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/IP3005-INJOINIC.pdf)

## 软件开发

### Arduino

- [Hat PowerC Example - with M5StickC](https://github.com/m5stack/M5Hat-PowerC/blob/master/examples/Hat_PowerC_M5StickC/Hat_PowerC_M5StickC.ino)
- [Hat PowerC Example - with M5StickC-Plus](https://github.com/m5stack/M5Hat-PowerC/blob/master/examples/Hat_PowerC_M5StickCPlus/Hat_PowerC_M5StickCPlus.ino)

### UiFlow1

- [Hat PowerC UiFlow1 文档](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Hat/PowerC/UIFlow)

- [Hat PowerC 测试程序](/zh_CN/uiflow/blockly/hat/roverc)

### EasyLoader

| Easyloader            | 下载链接                                                                                                  | 备注 |
| --------------------- | --------------------------------------------------------------------------------------------------------- | ---- |
| Hat PowerC Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/HAT/EasyLoader_PowerC_HAT.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/PowerC_HAT.mp4" type="video/mp4">
</video>
