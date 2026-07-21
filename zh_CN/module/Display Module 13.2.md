# Module13.2 Display

<span class="product-sku">SKU:M126</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Display Module 13.2/img-cec9dc43-a087-44da-a219-831f70b19314.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Display Module 13.2/img-56cbbfc5-dc17-4bc6-a4c9-4c2f8f0f2c5c.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/986/M126-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Display Module 13.2/img-8710dbe2-77bf-4e67-9c7a-be20d7000ccc.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Display Module 13.2/img-dac8bbbb-0efe-4fba-9e21-2ffa9280654f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Display Module 13.2/img-a31c77f5-39b0-4e2d-8a7c-18f2dc1c94fe.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Display Module 13.2/img-68e38dc3-4064-425d-a993-dc72ba0e8c38.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Display Module 13.2/img-3e3554b5-c23c-4b45-b6c5-a20a5588d8dd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Display Module 13.2/img-c8ed4176-2ca2-40e4-9b6d-e20331f1dfc8.webp">
</PictureViewer>

## 描述

**Module13.2 Display** 是一款用于**高清视音频**的扩展模块，采用**高云 GW1NR 系列 FPGA 芯片**输出**Display 信号**，并用**LT8618S 芯片**作为信号输出调理，能实现 **24 位颜色深度 Display 信号**以及**高达 8 通道音频信号**的输出，分辨率可达 **1080P** 。其中 FPGA 内部实现了**I2S 音频生成功能**，模块内含有 **DC 电源输入插座** 以及相应的 **DC-DC 电路**，能实现整机供电。本产品适用于**各种可编程的高清视音频输出**等场合。

## 产品特性

- 支持 24 位 RGB 输入
- 分辨率高达 1080P
- 支持高达 8 通道音频输入
- 内含 9-24V 转 5V、3.3V 和 1.2V 的 DC-DC 电路和 5V 转 1.8V 的 LDO 电路
- 高清音视频接口、JTAG 下载接口
- 9-24V 直流电源接口
- 电源开关

## 包装内容

- 1 x Module13.2 Display

## 应用场景

- 输出高清音视频信号
- 人机互动

## 规格参数

| 规格                             | 参数                    |
| -------------------------------- | ----------------------- |
| 音视频信号采集芯片               | GW1NR-LV9QN88C6-I5 FPGA |
| 音视频信号处理芯片               | LT8616SXB @ 0x39        |
| 9-24V 转 5V DCDC 降压芯片        | SY8303                  |
| 5V 转 3.3V 和 1.2V DCDC 降压芯片 | SY8089                  |
| 5V 转 1.8V LDO 降压芯片          | LP5907                  |
| 分辨率                           | 最大 1080P (1920x1080)  |
| 输入电源                         | 9 ~ 24V                 |
| 产品尺寸                         | 54.0 × 54.0 × 19.8mm    |
| 产品重量                         | 21.6g                   |
| 包装尺寸                         | 134.0 × 95.0 × 20.2mm   |
| 毛重                             | 41.2g                   |

## 原理图

- [Module13.2 Display 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/553/Display_Module_13.2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/553/Display_Module_13.2_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/553/Display_Module_13.2_sch_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/553/Display_Module_13.2_sch_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/553/Display_Module_13.2_sch_04.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN     |
| -------- | ---- | ----- | ------- |
| GND      | 1    | 2     |         |
| GND      | 3    | 4     |         |
| GND      | 5    | 6     |         |
| SPI_MOSI | 7    | 8     |         |
| SPI_MISO | 9    | 10    |         |
| SPI_CLK  | 11   | 12    | 3V3     |
|          | 13   | 14    |         |
|          | 15   | 16    |         |
| I2C_SDA  | 17   | 18    | I2C_SCL |
|          | 19   | 20    |         |
|          | 21   | 22    |         |
|          | 23   | 24    |         |
|          | 25   | 26    |         |
|          | 27   | 28    | 5V      |
|          | 29   | 30    |         |
::

## 尺寸图

- [Module13.2 Display 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/986/M126-displaymoudle.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/986/M126-displaymoudle_page_01.png" width="100%">

## 数据手册

- [GW1NR-LV9 FPGA](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M126%20Display%20Module%2013.2/GW1N(R)FPGA.pdf>)
- [LT8616SXB](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M126%20Display%20Module%2013.2/Lontium-LT8618SXB.pdf)
- [SY8089](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/ATOMS3/sy8089.pdf)
- [SY8303](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M126%20Display%20Module%2013.2/SY8303.pdf)
- [LP5907](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M126%20Display%20Module%2013.2/LP5907.pdf)

## 软件开发

### Arduino

- [Module13.2 Display Arduino Example](https://github.com/m5stack/M5Module-Display-13.2)

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/Display Module 13.2/arduinoCase-1673421428810微信图片_20230111151551.png" width="100%"/>

### UiFlow1

- [Module13.2 Display UiFlow1 文档](/zh_CN/uiflow/blockly/module/display)

### UiFlow2

- [Module13.2 Display UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/display.html)

### Easyloader

| Easyloader                            | 下载链接                                                                                                          | 备注 |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---- |
| Module13.2 Display Example Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/EasyLoader_Display%20Module%2013.2.exe) | /    |
