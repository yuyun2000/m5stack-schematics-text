# FLIR

<span class="product-sku">SKU:K021</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/flir/flir_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/flir/flir_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/app/flir/flir_03.webp">
</PictureViewer>

## 描述

**FLIR** 是一款微型红外热成像仪。采用最新的 FLIR Lepton 3.0 长波红外 (LWIR) 摄像头内核，相对于 2.x 版本增强了 2 倍分辨率，4 倍像素。使用 3D 打印定制的底座外壳，完美兼容 M5Core 堆叠体系。模块通过 I2C 协议进行控制，默认生成分辨率为 160×120 的有效图像，你可以通过修改程序进行图像处理，使其显示不同的分辨率。功能强大的 FLIR 是非接触式温度测量的完美解决方案.

## 注意事项

\#> 注意事项 | 长时间工作的热成像仪 Lepton 存在发热现象，但并不会影响输出的图像。

## 产品特性

- 160×120 有效像素
- Lepton 低功耗工作  — 150 mW (典型工作), 650 mW (快门拍摄), 5 mW (待机)
- Field of view: 56°, with shutter
- Lepton 输入电源电压: 1.2V,2.8V,2.5V - 3.1V IO
- 快速成像 (0.5 second)

## 包装内容

- 1 x FLIR

## 应用场景

- 车辆发动机故障检测
- 建筑除湿保温密封性检测
- 工业炉内壁耐火材料裂痕检测
- 夜晚户外观测动物

## 规格参数

| _技术指标_   | _参数值_                                           |
| :----------: | :------------------------------------------------: |
| 有效帧频     | 8.7Hz                                              |
| 输入时钟     | 25-MHz                                             |
| 像素尺寸     | 12µm                                               |
| 场景动态范围 | 低增益模式: -10 to 400°C; 高增益模式: -10 to 140°C |
| 波长范围     | 8 µm to 14 µm                                      |
| 热灵敏度     | ＜ 50 mK (0.050℃)                                  |
| 输入电压     | 2.8 V, 1.2 V, 2.5 V - 3.1 V IO                     |
| 最佳温度范围 | -10 °C to +80 °C                                   |
| 产品重量     | 17.0g                                              |
| 毛重         | 34.0g                                              |
| 产品尺寸     | 54 x 54 x 13mm                                     |
| 包装尺寸     | 125 x 67 x 23mm                                    |

## 数据手册

- [Lepton 3&3.5](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/lepton-3-3.5-datasheet_en.pdf)
- [Lepton Engineering Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/flir-lepton-engineering-datasheet_en.pdf)
- [Lepton Software Interface Description](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/application/flir-lepton-software-interface-description-document_en.pdf)

## 软件开发

### Arduino

- [FLIR 测试程序](https://github.com/m5stack/Applications-Lepton3.0/tree/master/lepton3/Src/Lepton_Bot)

### Easyloader

| Easyloader           | 下载链接                                                                                                                | 备注 |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---- |
| FLIR Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Application/FLIR/EasyLoader_APP_FLIR_Lepton_Bot.exe) | /    |
