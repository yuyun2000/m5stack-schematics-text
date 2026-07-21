# IIoT Dual-Switch

<span class="product-sku">SKU:A072</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/iiot_dual_switch_kit_with_core/iiot_dual_switch_kit_with_core_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/iiot_dual_switch_kit_with_core/iiot_dual_switch_kit_with_core_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/base/iiot_dual_switch_kit_with_core/iiot_dual_switch_kit_with_core_03.webp">
</PictureViewer>

## 描述

**IIoT Dual-Switch** 是 M5 体系中一款面向工业物联网领域的双继电器控制底座。基于 M5 工业控制产品的 BASE26 设计，在原有的可定制化结构基础上，添加了双继电器控制模块，硬件拓展性上兼容了 M5Stack 独有的模块堆叠体系，使功能拓展变得更加简易。套件提供多种通信模块搭配选择（如 LoRa、GSM、LTE 等），能够构建稳定可靠的工业 IoT 控制节点。

## 产品特性

- 双继电器控制模块
- 继电器允许通断电流 / 电压:
  - AC：10A@250V
  - DC：10A@24V
- DC 电源输入：9 ~ 24V
- BASE26 可定制化底座
- 4 pin HT3.96 端子
- G15 - 继电器 A/G12 - 继电器 B

## 包装内容

- 1 x IIoT Dual-Switch
- 1 x HT3.96-4P 端子

## 应用场景

- IIoT 节点
- 工业继电器开关

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 毛重     | 25.0g                |
| 包装尺寸 | 55.0 x 55.0 x 30.0mm |

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN     | LEFT | RIGHT | PIN     |
| ------- | ---- | ----- | ------- |
| GND     | 1    | 2     | NC      |
| GND     | 3    | 4     | NC      |
| GND     | 5    | 6     | NC      |
| NC      | 7    | 8     | NC      |
| NC      | 9    | 10    | NC      |
| NC      | 11   | 12    | 3V3     |
| NC      | 13   | 14    | NC      |
| NC      | 15   | 16    | NC      |
| NC      | 17   | 18    | NC      |
| NC      | 19   | 20    | NC      |
| RELAY.B | 21   | 22    | NC      |
| RELAY.A | 23   | 24    | NC      |
| NC      | 25   | 26    | NC      |
| NC      | 27   | 28    | 5V      |
| NC      | 29   | 30    | BAT     |
::

## 软件开发

### Arduino

- [IIoT Dual-Switch 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/App/IIoT%20Dual)

### UiFlow1

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/iiot_dual_switch_kit_with_core/iiot_dual_switch_kit_with_core_uiflow_01.webp" width="50%" height="50%">

### EasyLoader

| Easyloader                       | Download                                                                                                                                              | Note |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| IIoT Dual-Switch Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Base/IIoT_Dual_Switch_Kit_with_core/EasyLoader_IIoT_Dual_Switch_Kit_with_core.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Base/iiot_dual_switch%20kit_with_core.mp4" type="video/mp4" >
</video>
