# Unit LoRaWAN915

<span class="product-sku">SKU:U115</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan915/lorawan915_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan915/lorawan915_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan915/lorawan915_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan915/lorawan915_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan915/lorawan915_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan915/lorawan915_06.webp">
</PictureViewer>

## 教程 & 快速上手

learn>| ![TTN (The Things Network) ](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lorawan/ttn_01.jpg) | [TTN (The Things Network) ](/zh_CN/guide/lora/lorawan/ttn) | 本教程将向你说明如何在 TTN 中创建应用与节点设备并实现设备到云端的数据发送与接收。|

## 描述

**Unit LoRaWAN915**是 M5Stack 推出的适用于 915MHz 频率的 LoRaWAN 通讯模块。模块采用 ASR6501 方案，支持远距离通信的同时兼具超低功耗与高灵敏度特性。模组集成 LoRaWAN 协议栈，采用串口通信接口 (使用 AT 指令集进行控制)，使用时可作为采集节点大量接入网关进行数据收集管理。该模块适合应用于长距离的低功耗物联网通信应用，如环境监测节点部署等。

\#>**注意:**<br/>该产品默认频段支持**US915**，不支持**AU915**

## 产品特性

- ASR6501
- 支持 US915
- SMA 天线
- 通信接口: UART
- 指令协议：AT 命令

## 包装内容

- 1 x Unit LoRaWAN915
- 1 x SMA 天线
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 自动远程抄表
- 智能交通智能停车场
- 远程灌溉及环境监测

## 规格参数

| 规格           | 参数                      |
| -------------- | ------------------------- |
| 通信芯片       | ASR6501                   |
| 工作频率       | 915MHz                    |
| LoRaWAN 版本   | v1.0.1                    |
| 最小接收灵敏度 | -137dBm (SF=12/BW=125KHz) |
| 最大发射功率   | +21dBm                    |
| 通讯方式       | UART 115200bps            |
| 产品重量       | 12.8g                     |
| 毛重           | 45g                       |
| 产品尺寸       | 71.5 x 24 x 8mm           |
| 包装尺寸       | 95 x 65 x 25mm            |

## 操作说明

### US915 支持的主要国家及地区

?>**阿根廷**/**加拿大**/**智利**/**哥伦比亚**/**厄瓜多尔**/**希腊危地马拉**/**牙买加**/**墨西哥**/**尼加拉瓜**/**巴拿马**/**美国**/**乌拉圭**

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan915/lorawan915_support_area.webp">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan915/lorawan915_sch_01.webp" width="80%">

## 管脚映射

### Unit LoRaWAN915

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 数据手册

- [LoRaWAN 区域参数](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/lorawantm_regional_parameters_v1.1rb_-_final.pdf)

## 软件开发

### Arduino

- [Unit LoRaWAN915 Arduino 驱动库](https://github.com/m5stack/UNIT_LoRaWAN)
- [Unit LoRaWAN915 ABP Example](https://github.com/m5stack/UNIT_LoRaWAN/tree/master/examples/LoRaWAN_ABP)
- [Unit LoRaWAN915 OTAA Example](https://github.com/m5stack/UNIT_LoRaWAN/tree/master/examples/LoRaWAN_OTAA)

### 通信协议

- [Unit LoRaWAN915 AT指令集](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/COM.LoRaWAN.Ra-07.asr6501-asr6502-at-commands-introduction-v4.3.pdf)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/LoRaWAN_470_868_915.mp4" type="video/mp4">
</video>
