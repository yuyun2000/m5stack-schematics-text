# Module13.2 ECG

<span class="product-sku">SKU:M034</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/ecg/ecg_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/ecg/ecg_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/ecg/ecg_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/ecg/ecg_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/ecg/ecg_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/ecg/ecg_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/ecg/ecg_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/ecg/ecg_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/ecg/ecg_09.webp">
</PictureViewer>

## 描述

**Module13.2 ECG**是一款心率测量模块，能够用于人体的心率统计与心电图曲线的生成。心电图 (ECG) 是利用心电图机从体表记录心脏每一心动周期所产生的电活动变化图形的技术。在信号采集端，这款 Module13.2 ECG 模块集成 AD8232 单导联心率监护前端，采集的心电信号经过 AD8603 低通滤波器信号处理，由 10bit-ADC (AD7476) 进行模拟 / 数字信号输入 STM32 (内置心率统计算法) 进行信号分析。最后将处理结果以串口通信形式对外输出，方便主控设备的获取与显示。在信号输出方面采用前端 / 数字全隔离设计，加强设备稳定性与安全性。

## 注意事项

!> 电源注意事项 | 该产品仅允许使用 **5V** 电源输入，在使用该产品时请严格遵守该电源输入标准，避免损坏设备或是造成人体伤害。

## 产品特性

- ADI 集成前端 (高信号增益 G=100, 带 DC 阻塞能力)
- 串口数据输出
- 内置心率统计算法
- 前端 / 数字全隔离设计
- 超精密运放

## 包装内容

- 1 x Module13.2 ECG
- 3 x 心电导联线
- 6 x 导联贴

## 应用场景

- 生物电信号采集
- 便携式 ECG
- 健身及运动心率监护仪

## 规格参数

| 规格     | 参数                   |
| -------- | ---------------------- |
| MCU      | STM32F031G4U6          |
| 通讯方式 | UART 115200bps         |
| AD8232   | 高信号增益 G=100       |
| AD7476   | 10bit-ADC              |
| 产品尺寸 | 54.0 x 54.0 x 13.2 mm  |
| 产品重量 | 18.0 g                 |
| 包装尺寸 | 105.0 x 65.0 x 40.0 mm |
| 毛重     | 101.0 g                |

## 原理图

<img src = "https://static-cdn.m5stack.com/resource/docs/products/module/ecg/ecg_sch_01.webp" width="80%">

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN  | LEFT | RIGHT | PIN |
| ---- | ---- | ----- | --- |
| GND  | 1    | 2     |     |
| GND  | 3    | 4     |     |
| GND  | 5    | 6     |     |
|      | 7    | 8     |     |
|      | 9    | 10    |     |
|      | 11   | 12    | 3V3 |
|      | 13   | 14    |     |
|      | 15   | 16    |     |
|      | 17   | 18    |     |
|      | 19   | 20    | RXD |
|      | 21   | 22    | TXD |
|      | 23   | 24    |     |
| HPWR | 25   | 26    |     |
| HPWR | 27   | 28    | 5V  |
| HPWR | 29   | 30    | BAT |
::

## 尺寸图

- [Module13.2 ECG 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1027/M034-ECG.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1027/M034-ECG_page_01.png" width="100%">

## 数据手册

- [AD8232](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/AD8232_datasheet_cn.pdf)
- [AD8603](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/AD8603_datasheet_cn.pdf)
- [AD7476](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/AD7476_datasheet_en.pdf)
- [ECG 数据包格式](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1027/Module13.2-ECG-Protocol-CN.pdf)

## 软件开发

### Arduino

- [Module13.2 ECG Example with M5Core](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Module/ECG)

### UiFlow2

- [Module13.2 ECG UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/ecg.html)

### Easyloader

| Easyloader                                    | 下载链接                                                                                              | 备注 |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---- |
| Module13.2 ECG Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_ECG.exe) | /    |

### 其他

\#> 上位机使用说明 | 使用 PC 端心率读取工具时候，设备需烧录串口透传固件 (上传前，请更改串口初始化引脚为实际连接的引脚), 将数据转发至 PC。

- [RawDisplay-PC 上位机](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/RawDisplay.zip)
- [M5Core UART 透传程序](https://github.com/m5stack/M5Stack/blob/master/examples/Advanced/MultSerial/MultSerial.ino)

## 相关视频

- 统计心率，显示心电图曲线

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/ECG.mp4">
</video>
