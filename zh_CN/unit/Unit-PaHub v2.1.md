# Unit PaHub v2.1

<span class="product-sku">SKU:U040-B-V21</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-PaHub2.1/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-PaHub2.1/8.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/794/U040-B-V21-package.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-PaHub2.1/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-PaHub2.1/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-PaHub2.1/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-PaHub2.1/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-PaHub2.1/10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/794/U040-B-V21_weight.jpg">
</PictureViewer>

## 描述

**Unit PaHub v2.1** 是一款 I2C 多路复用单元，采用 **PCA9548AP** 芯片方案，可将单路 I2C 接口扩展为六路。通过选择不同通道，它允许在同一 I2C 总线上连接多个具有相同或不同 I2C 地址的设备，实现设备共存 (通过轮询通道进行切换)。模块配备板载 **拨码开关**，可轻松调整 **Unit PaHub v2.1** 的 I2C 地址，支持多单元级联以连接更多 I2C 设备。相比前代产品，它在多路 I2C 设备并行使用场景中提供了更强的灵活性和扩展性。该产品适用于多路 I2C 设备同时使用的场景。

## 产品特性

- I2C HY2.0-4P PORTA 拓展
- 允许多个嵌套
- 6 个扩展 Grove 口
- 拨码切换 I2C 地址
- LEGO 兼容孔

## 包装内容

- 1 x Unit PaHub v2.1
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- I2C 扩展

## 规格参数

| 规格            | 参数                                               |
| --------------- | -------------------------------------------------- |
| I2C 多路扩展 IC | PCA9548AP                                          |
| 通讯协议        | I2C:0x70~0x77 (默认：0x70，可通过拨码开关进行修改) |
| 工作温度        | 0 ~ 40°C                                           |
| 产品尺寸        | 48.0 x 24.0 x 10.8mm                               |
| 产品重量        | 7.3g                                               |
| 包装尺寸        | 138.0 x 93.0 x 13.0mm                              |
| 毛重            | 12.3g                                              |

## 操作说明

<img alt="status" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-PaHub2.1/status.jpg" width="100%" />

> 支持通过拨码开关修改设备地址，用户可通过配置相应的真值表设置来调整 I2C 地址。

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-PaHub2.1/img-103440a9-d7e4-4aab-b784-825aa9b35614.png" width="100%" />

## 管脚映射

### Unit PaHub v2.1

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="Model Size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-PaHub2.1/module%20size.jpg" width="100%" />

## 结构文件

- [Unit PaHub v2.1 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U040-B-V21_Unit_PaHub_v2.1/Structures)

## 数据手册

- [PCA9548AP](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/pahub2/pca9548a.pdf)

## 软件开发

### Arduino

- [Unit PaHub v2.1 Arduino 驱动库](https://github.com/m5stack/M5Unit-HUB)

## 相关视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-PaHub2.1/U040-B-V21%20PaHub%20V2.1%20video.mp4" type="video/mp4"></video>

## 产品对比

::compare-table
| Product Compare   | [Unit PaHub v2.1](/zh_CN/unit/Unit-PaHub%20v2.1) ![Unit PaHub v2.1](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-PaHub2.1/9.webp) | [Unit PaHub2](/zh_CN/unit/pahub2) ![Unit PaHub2](https://static-cdn.m5stack.com/resource/docs/products/unit/pahub2/pahub2_02.webp) | [Unit PaHub](/zh_CN/unit/pahub) ![Unit PaHub](https://static-cdn.m5stack.com/resource/docs/products/unit/pahub/pahub_02.webp) |
| ---------------   | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| 芯片方案          | PCA9548A                                                                                                                                                           | PCA9548A                                                                                                                           | TCA9548A                                                                                                                      |
| 更换 I2C 地址方式 | 拨码开关切换                                                                                                                                                       | 板载电阻焊接切换                                                                                                                   | 板载电阻焊接切换                                                                                                              |
| 地址              | 0x70~0x77 (默认：0x70)                                                                                                                                             | 默认 0x70                                                                                                                          | 默认 0x70                                                                                                                     |
::
