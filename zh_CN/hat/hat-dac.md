# Hat DAC

<span class="product-sku">SKU:U068</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-dac/hat-dac_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-dac/hat-dac_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-dac/hat-dac_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-dac/hat-dac_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-dac/hat-dac_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-dac/hat-dac_06.webp">
</PictureViewer>

## 描述

**Hat DAC**是一款兼容 M5SticKC 的 DA 转换模块，内部集成 DAC 转换芯片 MCP4725，具备低功耗、高精度、单通道、12 位缓冲电压输出数模转换器（DAC）以及非易失性存储器（EEPROM）。其片上精密输出放大器使其能够达到轨到轨模拟输出摆幅。用户可以使用 I2C 接口命令将 DAC 输入和配置烧写到非易失性存储器（EEPROM）中，使得 DAC 在断电期间仍能保持代码，上电后即可直接使用，I2C 地址为 0x60。

## 产品特性

- 输出电压: 0-3.3V
- 开发平台: Arduino, UiFlow (Blockly, MicroPython)
- MCP4725:
  - 12 位分辨率
  - 外部 A0 地址引脚
  - 正常或关断模式
  - 快速稳定时间为 6μs (典型值)
  - 外部电压参考 (VDD)
  - 轨到轨输出
  - 低功耗
  - 单电源工作：2.7V 至 5.5V
  - 外部电压参考 (VDD)
  - I2C 接口
  - 扩展级温度范围:-40°C 至 + 125°C

## 包装内容

- 1 x Hat DAC

## 应用场景

- 设定点或失调微调
- 传感器校准
- 闭环伺服控制
- 低功耗便携式仪表
- PC 外设
- 数据采集系统

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 通信接口 | I2C 通信 @ 0x60      |
| 产品尺寸 | 24.0 x 25.0 x 13.0mm |
| 产品重量 | 6.0g                 |
| 包装尺寸 | 67.0 x 53.0 x 12.0mm |
| 毛重     | 19.0g                |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-dac/hat-dac_sch_01.webp" width="80%" height="80%">

## 软件开发

### Arduino

- [Hat DAC Example](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/DAC)

### UiFlow1

- [Hat DAC UiFlow1 文档](/zh_CN/uiflow/blockly/hat/dac)

### UiFlow2

- [Hat DAC UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/dac.html)

### Easyloader

| Easyloader         | 下载链接                                                                                                  | 备注 |
| ------------------ | --------------------------------------------------------------------------------------------------------- | ---- |
| Hat DAC Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/HAT/ENV/EasyLoader_StickC_HAT_ENV.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/ADC-DAC-HAT.mp4" type="video/mp4" >
</video>
