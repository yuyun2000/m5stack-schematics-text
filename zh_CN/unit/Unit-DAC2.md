# Unit DAC2

<span class="product-sku">SKU:U012-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-DAC2/img-d3d02dea-e7ad-4543-ae7c-84957de8329e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-DAC2/img-fc97ab1d-c25d-43ca-9388-f1e91700defd.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/818/U012-B-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-DAC2/img-a240497e-ac81-4480-aaca-a0e537bbd909.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-DAC2/img-4eb2dc14-e3b6-415a-b139-c3c022d25a0b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-DAC2/img-3b2ba18c-bd96-443a-9acc-10d6b19e811d.webp">
</PictureViewer>

## 描述

**Unit DAC2** 是一款 I2C 数字信号转模拟信号转换单元。采用 GP8413 的方案，在精度方面，此芯片可以将 15Bit 数字量线性转换成两路独立的 0-5V/0-10V 模拟电压，输出电压误差为 0.2%，线性度可达 0.01%。在扩展性方面，电路设计通过三位硬件地址 A2/A1/A0 进行选择，支持同时并联 8 个设备同时运行，多达 16 通道同时输出。在安全性能方面，设备具有短路保护功能，输出引脚与地短路时自动进入保护模式停止输出。适用于通用信号转换、马达调速、LED 调光、逆变器、电源和工业模拟信号隔离等领域。

## 产品特性

- I2C 通讯 (默认地址 0x59)
- 支持多路并联使用
- 短路保护
- 高精度，误差小

## 包装内容

- 1 x Unit DAC2
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96-4P

## 应用场景

- 通用信号转换
- 马达调速、LED 调光
- 逆变器、电源
- 工业模拟信号隔离

## 规格参数

| 规格               | 参数                                |
| ------------------ | ----------------------------------- |
| DAC 芯片           | GP8413                              |
| 分辨率             | 15 位                               |
| 通信接口           | I2C 通信 @ 0x58 ~ 0X65，默认为 0x59 |
| 最大输出电压       | 10V                                 |
| 输出电压误差       | <0.2%                               |
| 输出电压线性度误差 | 0.01%                               |
| 工作温度           | 0 ~ 40°C                            |
| 产品尺寸           | 32.0 x 24.0 x 10.2mm                |
| 产品重量           | 8.0g                                |
| 包装尺寸           | 138.0 x 93.0 x 12.0mm               |
| 毛重               | 13.4g                               |

## 原理图

- [Unit DAC2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/575/SCH_UNIT_DAC2_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/575/SCH_UNIT_DAC2_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### Unit DAC2

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-DAC2/img-3a3d2a51-bc94-41e5-81ce-1adc772c837c.jpg" width="100%" />

## 数据手册

- [GP8413 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DAC2/GP8413.pdf)

## 软件开发

### Arduino

- [Unit DAC2 Test Example with M5StickC-Plus](https://github.com/m5stack/M5StickC-Plus/tree/master/examples/Unit/DAC2_GP8413)
- [Unit DAC2 Test Example with M5StickC-Plus2](https://github.com/m5stack/M5StickCPlus2/tree/master/examples/Unit/DAC2_GP8413)
- [Unit DAC2 Test Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/DAC2_GP8413)
- [Unit DAC2 Test Example with M5Core2](https://github.com/m5stack/M5Core2/tree/master/examples/Unit/DAC2_GP8413)
- [Unit DAC2 Test Example with M5CoreS3](https://github.com/m5stack/M5CoreS3/tree/main/examples/Unit/DAC2_GP8413)

## UiFlow2

- [Unit DAC2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/dac2.html)
