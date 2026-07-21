# Unit PaHub v2.0

<span class="product-sku">SKU:U040-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub2/pahub2_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub2/pahub2_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub2/pahub2_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub2/pahub2_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub2/pahub2_06.webp">
</PictureViewer>

## 描述

**Unit PaHub v2.0**，是一款 I2C 设备分线器，能够将单路 I2C HY2.0-4P 接口拓展至六路，并且允许挂载相同 I2C 地址的从设备 (通过控制轮询不同的通道实现同地址设备共存)。内嵌 PCA9548AP-I2C 多路通道开关 IC，支持 6 组 I2C 设备拓展。

## 产品特性

- I2C HY2.0-4P PORTA 拓展
- 2 x LEGO 兼容孔
- 允许多个嵌套
- 1-6 拓展

## 包装内容

- 1 x Unit PaHub v2.0
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- I2C 扩展

## 规格参数

| 规格        | 参数                                         |
| ----------- | -------------------------------------------- |
| 通道控制 IC | PCA9548AP                                    |
| 通信接口    | I2C 通信 @ 0x70 (可通过电阻 A0，A1，A2 修改) |
| 产品尺寸    | 48.0 x 24.0 x 10.8mm                         |
| 产品重量    | 7.5g                                         |
| 包装尺寸    | 138.0 x 93.0 x 11.8mm                        |
| 毛重        | 13.0g                                        |

## 操作说明

\#> 注意：工作时，分线器通过控制轮询不同的通道实现同地址设备共存，编程时请注意通道顺序。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_08.webp" width="50%">

参考原理图及 PCA9548AP 数据手册可知，该 Unit 能够通过控制 A0~A2 引脚的电平组合，修改设备的 I2C 地址。(默认地址为 0x70)

在 Unit 的 PCB 板上预留了三个贴片电阻焊接位，分别为 A0-A2，如下图所示。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_09.webp" width="50%">

焊接 0 欧电阻后，相应的引脚将由低电平变为高电平，引脚电平组合与其对应的 I2C 地址如下表所示。

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_10.webp" width="50%">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_sch_01.webp">

## 管脚映射

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 数据手册

- [PCA9548AP](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/pahub2/pca9548a.pdf)

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/793/U040-B_Module_Size_sch_01.png" width="100%">

## 软件开发

### Arduino

- [Unit PaHub v2.0 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/PaHUB_TCA9548A)

### UiFlow1

- [Unit PaHub v2.0 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/pahub)

### EasyLoader

| Easyloader                      | 下载链接                                                                                      | 备注 |
| ------------------------------- | --------------------------------------------------------------------------------------------- | ---- |
| Unit PaHub v2.0 Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_PaHUB.exe) | /    |
