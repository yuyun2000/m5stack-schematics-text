# Unit AMeter

<span class="product-sku">SKU:U086</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ameter Unit/img-c6537146-ee26-435c-96e7-4726cc9cfb7c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ameter Unit/img-deb01365-ce11-48d3-a572-d7efefe804c6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ameter Unit/img-fadd1196-34ca-4efc-883c-91dc7291a793.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ameter Unit/img-939ef304-a995-4fc9-9bfc-6cde1034d198.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Ameter Unit/img-3cbee12f-6812-4276-8c4c-7d77f24af99a.webp">
</PictureViewer>

## 描述

**Unit AMeter**是一款电流计，可以对电流进行实时监测。内部采用 16 位 ADC 数模转换器 ADS1115，通过 I2C (0X48) 进行通讯。为了保证测量精度，内置 DC-DC 隔离电源，同时 I2C 接口通过低功耗隔离器 CA-IS3020S 进行电气隔离，防止数据总线或其他电路上的噪声和浪涌进入本地接地端而干扰或损坏敏感电路。每个 Unit 在出厂时都单独进行校准，精度为满量程 %1，±1 位读数，分辨率为 0.3mA，最大测量电流为 ±4A，内部集成 4A 熔断器，防止测量电流过大烧毁电路。

## 注意事项

\#> 校准参数 | EEPROM (0x51) 在出厂时内置了校准参数，请勿对 EEPROM 进行写操作，否则校准数据将被覆盖导致测量结果不准确。

## 产品特性

- ±4A 量程
- 16 位 ADC 转换
- 4A 熔断器
- 精度为满量程 %1，±1 位读数
- 分辨率 0.3mA
- LED 电源指示灯
- 过流保护
- 免重新校准 (EEPROM 出厂写入)
- 内置 CA-IS3020S 隔离芯片，抗干扰
- 隔离 DC-DC
- 开发平台: Arduino，UiFlow (Blockly，Pyhton)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit AMeter
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96-4P 端子

## 应用场景

- 电流计

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 测量范围 | ±4A                  |
| 通信接口 | I2C 通信 @ 0x48      |
| 产品尺寸 | 56.0 x 24.0 x 8.0mm  |
| 产品重量 | 8.4g                 |
| 包装尺寸 | 138.0 x 93.0 x 9.0mm |
| 毛重     | 16.7g                |

## 管脚映射

### Unit AMeter

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Ameter%20Unit/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit AMeter 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U086_Unit_AMeter/Structures)

## 数据手册

- [CA-IS3020S](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/CA-IS3020S.pdf)
- [ADS1115](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/ADS1115.PDF)

## 软件开发

### Arduino

- [M5Unit-Ameter with M5Core](https://github.com/m5stack/M5-ADS1115/blob/master/examples/Unit_AMeter_M5Core/Unit_AMeter_M5Core.ino)
- [M5Unit-Ameter with M5Core2](https://github.com/m5stack/M5-ADS1115/blob/master/examples/Unit_AMeter_M5Core2/Unit_AMeter_M5Core2.ino)
- [M5Unit-Ameter with M5Atom](https://github.com/m5stack/M5-ADS1115/blob/master/examples/Unit_AMeter_M5Atom/Unit_AMeter_M5Atom.ino)
- [M5Unit-Ameter with M5StickC](https://github.com/m5stack/M5-ADS1115/blob/master/examples/Unit_AMeter_M5StickC/Unit_AMeter_M5StickC.ino)
- [M5Unit-Ameter with M5StickCPlus](https://github.com/m5stack/M5-ADS1115/blob/master/examples/Unit_AMeter_M5StickCPlus/Unit_AMeter_M5StickCPlus.ino)

### UiFlow1

- [Unit AMeter UiFlow1 文档](/zh_CN/uiflow/blockly/unit/ameter)
- [Unit AMeter UiFlow1 Example](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/A_Meter_Unit/UIFlow)

### UiFlow2

- coming soon...

### Home Assistant

- [Unit AMeter Home Assistant 集成](/zh_CN/homeassistant/sensor/unit_ameter_sensor)

### EasyLoader

| Easyloader                      | 下载链接                                                                                                                               | 备注 |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit AMeter example with M5Core | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/Ameter%20Unit/ezLoader-51db0670-77bd-42e4-b8a1-006632e4518a.exe) | /    |

## 相关视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/AMeter.mp4" type="video/mp4"></video>
