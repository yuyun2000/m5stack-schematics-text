# Unit Mini PDM

<span class="product-sku">SKU:U089</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pdm/pdm_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pdm/pdm_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/734/U089-package.jpg">
=<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pdm/pdm_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pdm/pdm_06.webp">
</PictureViewer>

## 描述

**Unit Mini PDM** 是一款基于 PDM (脉冲密度调制) 信号的数字式 MEMS 硅基麦克风，该麦克风具有高信噪比、高灵敏度、功耗低、抗射频干扰、频率响应平滑等特性，根据时钟频率自动切换麦克风状态 (断电 / 激活 / 休眠)，可用于可穿戴设备、智能数码设备的音频数据采集。

## 产品特性

- PDM 信号输出 (CLK/DAT)
- 高灵敏度、高信噪比
- 功耗低
- 抗射频干扰
- 兼容 LEGO

## 包装内容

- 1 x Unit Mini PDM
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 频谱仪
- 录音
- 响度计

## 规格参数

| 规格       | 参数                                 |
| ---------- | ------------------------------------ |
| 数字麦克风 | SPM1423                              |
| 灵敏度     | 94dB SPL@1KHz 典型值:-22dBFS         |
| 信噪比     | 94dB SPL@1KHz，A 加权 典型值：61.4dB |
| 总谐波失真 | 100dB SPL@1KHz 典型值：1%            |
| 工作电流   | 600µA                                |
| 外壳材质   | Plastic (PC)                         |
| 产品尺寸   | 24.0 x 24.0 x 13.0mm                 |
| 产品重量   | 4.0g                                 |
| 包装尺寸   | 138.0 x 93.0 x 7.0mm                 |
| 毛重       | 8.0g                                 |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pdm/pdm_sch_01.webp" width="80%">

## 管脚映射

### Unit Mini PDM

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | Data   | Clock |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/pdm/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="80%">

## 数据手册

- [SPM1423](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/SPM1423HM4H-B_datasheet_en.pdf)

## 软件开发

### Arduino

- [Unit Mini PDM Arduino 使用教程](/zh_CN/arduino/projects/unit/unit_mini_pdm)
- [Unit Mini PDM 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/PDM_SPM1423)

### UiFlow2

- [Unit Mini PDM UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/pdm.html)

### EasyLoader

| Easyloader               | 下载链接                                                                                                              | 备注 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit PDM Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_PDM_Unit.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/PDM.mp4">
</video>
