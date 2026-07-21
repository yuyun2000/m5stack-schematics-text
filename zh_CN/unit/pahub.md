# Unit PaHub

<span class="product-sku">SKU:U040</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_03.webp">
</PictureViewer>

## 描述

**Unit PaHub**，是一款 I2C 设备分线器，能够将单路 I2C HY2.0-4P 接口拓展至六路，并且允许挂载相同 I2C 地址的从设备 (通过控制轮询不同的通道实现同地址设备共存)。内嵌 TCA9548A-I2C 多路通道开关 IC，支持 6 组 I2C 设备拓展。

## 产品特性

- I2C HY2.0-4P PORTA 拓展
- 2 x LEGO 兼容孔
- 允许多个嵌套
- 1-6 拓展

## 包装内容

- 1 x Unit PaHub
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- I2C 扩展

## 规格参数

| 规格     | 参数                                         |
| -------- | -------------------------------------------- |
| 通信接口 | I2C 通信 @ 0x70 (可通过电阻 A0，A1，A2 修改) |
| 产品尺寸 | 48.0 x 24.0 x 10.8mm                         |
| 产品重量 | 6.7g                                         |
| 包装尺寸 | 138.0 x 93.0 x 11.8mm                        |
| 毛重     | 12.0g                                        |

## 操作说明

\#> 注意：工作时，分线器通过控制轮询不同的通道实现同地址设备共存，编程时请注意通道顺序

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_08.webp">

参考原理图及 TCA9548A 数据手册可知，该 Unit 能够通过控制 A0~A2 引脚的电平组合，修改设备的 I2C 地址。(默认地址为 0x70)

在 Unit 的 PCB 板上预留了三个贴片电阻焊接位，分别为 A0-A2，如下图所示。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_09.webp">

焊接 0 欧电阻后，相应的引脚将由低电平变为高电平，引脚电平组合与其对应的 I2C 地址如下表所示。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_10.webp">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_sch_01.webp" width="50%">

## 管脚映射

### Unit PaHub

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 数据手册

- [TCA9548A](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/TCA9548A_en.pdf)

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/793/U040-B_Module_Size_sch_01.png" width="100%">

## 软件开发

### Arduino

- [Unit PaHub 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/PaHUB_TCA9548A)

### UiFlow1

- [UiFlow1 文档](/zh_CN/uiflow/blockly/unit/pahub)

### EasyLoader

| Easyloader                 | 下载链接                                                                                      | 备注 |
| -------------------------- | --------------------------------------------------------------------------------------------- | ---- |
| Unit PaHub Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_PaHUB.exe) | /    |
