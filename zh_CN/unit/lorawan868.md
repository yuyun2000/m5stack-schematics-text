# Unit LoRaWAN868

<span class="product-sku">SKU:U117</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan868/lorawan868_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan868/lorawan868_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan868/lorawan868_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan868/lorawan868_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan868/lorawan868_06.webp">
</PictureViewer>

## 教程 & 快速上手

learn>| ![TTN (The Things Network) ](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/lora/lorawan/ttn_01.jpg) | [TTN (The Things Network) ](/zh_CN/guide/lora/lorawan/ttn) | 本教程将向你说明如何在 TTN 中创建应用与节点设备并实现设备到云端的数据发送与接收。|

## 描述

**Unit LoRaWAN868** 是 M5Stack 推出的适用于 868MHz 频率的 LoRaWAN 通讯模块。模块采用 ASR6501 方案，支持远距离通信的同时兼具超低功耗与高灵敏度特性。模组集成 LoRaWAN 协议栈，采用串口通信接口 (使用 AT 指令集进行控制)，使用时可作为采集节点大量接入网关进行数据收集管理。该模块适合应用于长距离的低功耗物联网通信应用，如环境监测节点部署等。

## 产品特性

- ASR6501
- 工作频率：868MHz
- SMA 天线
- 通信接口: UART
- 指令协议：AT 命令

## 包装内容

- 1 x Unit LoRaWAN868
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
| 工作频率       | 868MHz                    |
| LoRaWAN 版本   | v1.0.1                    |
| 最小接收灵敏度 | -137dBm (SF=12/BW=125KHz) |
| 最大发射功率   | +21dBm                    |
| 通讯方式       | UART 115200bps            |
| 产品重量       | 12.8g                     |
| 毛重           | 45g                       |
| 产品尺寸       | 71.5 x 24 x 8mm           |
| 包装尺寸       | 136 x 92 x 13mm           |

## 操作说明

### 868Mhz 支持的主要国家及地区

**阿尔巴尼亚 / 安道尔 / 亚美尼亚 / 奥地利 / 巴林 / 孟加拉国 / 白俄罗斯 / 比利时 / 缅甸 / 波斯尼亚和黑塞哥维那 / 文莱达鲁萨兰国 / 保加利亚 / 柬埔寨 / 柬埔寨 / 克罗地亚 / 塞浦路斯 / 丹麦 / 埃及 / 爱沙尼亚 / 芬兰 / 法国 / 德国 / 德国危地马拉 / 匈牙利 / 冰岛 / 伊朗 / 爱尔兰 / 意大利 / 老挝 / 拉脱维亚 / 黎巴嫩 / 列支敦斯登 / 立陶宛 / 卢森堡 / 马其顿，前南斯拉夫联盟共和国 / 马耳他 / 摩尔多瓦 / 黑山 / 摩洛哥 / 荷兰 / 荷兰 / 纽西兰 尼日利亚 / 挪威 / 阿曼 / 巴基斯坦 / 波兰 / 葡萄牙 / 卡塔尔 / 罗马尼亚 / 沙特阿拉伯 / 塞尔维亚 / 新加坡 / 斯洛文尼亚 / 南非 / 西班牙 / 瑞典 / 瑞士 / 突尼斯 / 土耳其 / 乌克兰 / 阿联酋 / 英国 / 越南**

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan868/lorawan868_support_area.webp">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/lorawan868/lorawan868_sch_01.webp" width="80%">

## 管脚映射

### Unit LoRaWAN868

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 数据手册

- [LoRaWAN 区域参数](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/lorawantm_regional_parameters_v1.1rb_-_final.pdf)

## 软件开发

### Arduino

- [Unit LoRaWAN868 Arduino 驱动库](https://github.com/m5stack/UNIT_LoRaWAN)
- [Unit LoRaWAN868 ABP Example](https://github.com/m5stack/UNIT_LoRaWAN/tree/master/examples/LoRaWAN_ABP)
- [Unit LoRaWAN868 OTAA Example](https://github.com/m5stack/UNIT_LoRaWAN/tree/master/examples/LoRaWAN_OTAA)

### 通信协议

- [Unit LoRaWAN868 AT指令集](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/COM.LoRaWAN.Ra-07.asr6501-asr6502-at-commands-introduction-v4.3.pdf)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/LoRaWAN_470_868_915.mp4" type="video/mp4">
</video>
