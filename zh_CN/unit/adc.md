# Unit ADC

<span class="product-sku">SKU:U013</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/adc/adc_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/adc/adc_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/adc/adc_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/adc/adc_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/adc/adc_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/adc/adc_06.webp">
</PictureViewer>

## 描述

**Unit ADC**是一款 A/D 转换器，其内置 16 位自校准模数转换器 **ADS1100**。通过 I2C 通信协议，ADS1100 可每秒采样 8、16、32 或 128 次进行转换。片内可编程的增益放大器 (PGA) 提供高达 8 倍的增益。对于需要高分辨率 A/D 转换采集的应用场景，**Unit ADC**是完美解决方案，其 I2C 地址是 0x48。

## 产品特性

- 完整的数据采集系统
- 封装：TINY SOT23-6
- 16 位无漏失码
- 连续自校准
- 单循环转换
- 内部系统时钟
- I2C 接口
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit ADC
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96 Male Socket (2 pins)

## 应用场景

- 心电信号采集
- 血压测量
- 测力计

## 规格参数

| 规格     | 参数                            |
| -------- | ------------------------------- |
| INL      | 满标度是量程的 0.0125% (最大值) |
| 增益倍数 | 1，2，4，8                      |
| 编程速率 | 8SPS 至 128SPS                  |
| 电流     | 90µA                            |
| 噪声     | 4μVp-p                          |
| 通信接口 | I2C 通信 @ 0x48                 |
| 产品尺寸 | 32.0 x 24.0 x 10.2mm            |
| 产品重量 | 4.2g                            |
| 包装尺寸 | 138.0 x 93.0 x 11.3mm           |
| 毛重     | 14.7g                           |

## 原理图

- [Unit ADC 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/736/U013_UNIT_ADC_SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/736/U013_UNIT_ADC_SCHE_page_01.png">
</SchViewer>

## 管脚映射

### Unit ADC

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/adc/module_size.jpg" width="80%">

## 数据手册

- [ADS1100](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/ADS1100_en.pdf)

## 软件开发

### Arduino

- [Unit ADC with M5Core](https://github.com/m5stack/M5-ADS1100/blob/master/examples/Unit_ADC_M5Core/Unit_ADC_M5Core.ino)
- [Unit ADC with M5Core2](https://github.com/m5stack/M5-ADS1100/blob/master/examples/Unit_ADC_M5Core2/Unit_ADC_M5Core2.ino)
- [Unit ADC with M5Atom](https://github.com/m5stack/M5-ADS1100/blob/master/examples/Unit_ADC_M5Atom/Unit_ADC_M5Atom.ino)
- [Unit ADC with M5StickC](https://github.com/m5stack/M5-ADS1100/blob/master/examples/ADC_M5StickC/ADC_M5StickC.ino)
- [Unit ADC with M5StickCPlus](https://github.com/m5stack/M5-ADS1100/blob/master/examples/ADC_M5StickCPlus/ADC_M5StickCPlus.ino)

### UiFlow1

- [Unit ADC UiFlow1 文档](/zh_CN/uiflow/blockly/unit/adc)

### UiFlow2

- [Unit ADC UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/adc.html)

### EasyLoader

| Easyloader                   | 下载链接                                                                                    | 备注 |
| ---------------------------- | ------------------------------------------------------------------------------------------- | ---- |
| Unit ADC example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_ADC.exe) | /    |

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113461828783810&bvid=BV1damyY1EWt&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/9O_fZiP4DxQ?si=-v1uJ3fXrRrA32wu" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
