# Module NB-IoT Plus

<span class="product-sku">SKU:M030</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot_plus/nb-iot_plus_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot_plus/nb-iot_plus_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot_plus/nb-iot_plus_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot_plus/nb-iot_plus_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot_plus/nb-iot_plus_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/nb-iot_plus/nb-iot_plus_06.webp">
</PictureViewer>

## 描述

**Module NB-IoT Plus** 是 M5Stack 堆叠模块系列中的一款 NB-IoT 物联网通信模块，内部集成高性能 NB-IoT 全网通无线通信模组 **M5311 - GB (国际版)**，相较 M5311-LV 增加了更多频段，可支持 B1/B3/B5/B8/B20/B28 多个频段。内置铜制螺旋天线，并预留了 ipex 连接座，方便用户使用外置天线以获得更好的信号强度。模块支持休眠功能，低功耗设计可以帮助客户获得更长的终端使用寿命。M5311-GB 提供丰富的外部接口和协议栈，支持外接传感器设备，为用户的产品开发提供了极大的便利。该模块特别适用于以超低功耗、超小尺寸为核心需求的智能抄表、智能穿戴、智能停车、市政管理等行业。

## 产品特性

- SIM 卡类型: Nano
- 状态信号：两路 LED 指示灯
- 单路开关机按钮
- 板载天线可选：内置铜制螺旋天线 (或通过跳线切换至 IPEX 座)
- 串行通信：Uart2 16/17
- 工作温度范围:-40°C 至 + 85°C
- NB-IoT: 支持 LTE Cat NB2\*
- 频段:
  B1/B3/B5/B8/B20/B28
- 数据传输:
  LTE Cat NB1 速率 (kbps):
  - Single Tone 15.625(UL)/21.25(DL)
  - Multi Tone 62.5(UL)/21.25(DL)
  - SMS 支持 PDU/TEXT 模式
  - 网络协议 IPv4/IPv6/UDP/TCP/CoAP/LwM2M/HTTP/MQTT/TLS
- 电气特性:
  - 电压: 3.3V
  - 耗流:
    3uA@PSM
    0.4mA@ldle mode (DRx=1.28S)
    167mA@Tx (23dBm/15kHzST)
    54mA@Rx
  - 输出功率: 23dBm±2dB
  - 灵敏度:
    -114dBm (无重传)
    -130dBm ( 开启重传 )

## 包装内容

- 1 x Module NB-IoT Plus

## 应用场景

- 智能表计
- 智能停车
- 市政管理

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 产品重量 | 13g                  |
| 毛重     | 24g                  |
| 产品尺寸 | 54.2 x 54.2 x 12.8mm |
| 包装尺寸 | 60 x 57 x 17mm       |

## 操作说明

### 部分国家运营商频段

以下内容非实时信息，仅供参考。

| 北美             | B4 (1700), B12 (700), B66 (1700), B71 (600), B26 (850)                              |
| ---------------- | ----------------------------------------------------------------------------------- |
| 亚太             | B1 (2100), B3 (1800), B5 (850), B8 (900), B18 (850), B20 (800), B26 (850),B28 (700) |
| 欧洲             | B3 (1800), B8 (900) , B20 (800)                                                     |
| 拉丁美洲         | B2 (1900), B3 (1800), B5 (850), B28 (700)                                           |
| 俄罗斯及周边国家 | B3 (1800), B8 (900), B20 (800)                                                      |
| 南非             | B3 (1800), B8 (900)                                                                 |
| 中东及北非       | B8 (900), B20 (800)                                                                 |

补充说明:

- GPIO2 维持高电平 2s 开机
- GPIO2 维持高电平 8s 关机
- 电源按钮长按 2s 开机
- 电源按钮长按 8s 关机
- GPIO26 高电平模块复位

## 原理图

- [Module NB-IoT Plus 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Modules/module_nb_iot_sch.pdf)

## 管脚映射

| M5Core             | G16 | G17 | 3.3V | GND |
| ------------------ | --- | --- | ---- | --- |
| Module NB-IoT Plus | RX  | TX  | 3.3V | GND |

## 数据手册

- [M5311](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M5311_cn.pdf)

## 软件开发

### Arduino

- [Module NB-IoT Plus Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/NB-IoT-PLUS_M5311GB)

### 通信协议

- [M5311 AT指令表](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/M5311_AT_Command_Interface_Specification_en.pdf)

### Easyloader

| Easyloader                                        | 下载链接                                                                                                             | 备注 |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---- |
| Module NB-IoT Plus Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_NB-IoT-Plus_MODULE.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/NB-IoT-Plus.mp4" type="video/mp4">
</video>
