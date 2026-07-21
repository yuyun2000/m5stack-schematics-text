# Unit ZigBee

<span class="product-sku">SKU:U110</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/zigbee/zigbee_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/zigbee/zigbee_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/zigbee/zigbee_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/zigbee/zigbee_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/zigbee/zigbee_06.webp">
</PictureViewer>

## 描述

**Unit ZigBee** 是 M5Stack 推出的一款 Zigbee 自组网通讯模块。模块采用 CC2630F128 方案，内部集成 Zigbee 协议栈，开放串口通信接口。集成外部天线，单节点稳定通信距离可达 1 km，200 级 router 深度，通过 MESH 组网方式能够将你的物联网应用进行广范围的延展，兼具超低功耗与高灵敏度特性。Zigbee 网络可以支持数以百计的节点，并具有增强的安全特性。可为家庭和楼宇自动化提供完整且可互操作的物联网解决方案。

## 产品特性

- CC2630F128 (双 ARM 核 - 32 位)
- 串口通信
- 低功耗 (模组工作电流：25mA，休眠 5uA)
- 动态路由维护，支持 200 级路由深度
- 传输速度 250Kbps
- 节点通信距离 1km
- UART 透明传输 / 广播 / P2P

## 包装内容

- 1 x Unit ZigBee
- 1 x SMA 天线
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 智能家居
- 物联网采集节点
- 楼宇自动化

## 规格参数

| 规格       | 参数                                  |
| ---------- | ------------------------------------- |
| CC2630F128 | ARM Cortex-M3 32bit                   |
| 通讯方式   | UART 38400bps 8N1 (default)           |
| 通信距离   | 1km (空旷地区)                        |
| 工作频率   | 2.4GHZ (2405MHz-2480MHz，步长为 5MHz) |
| 产品重量   | 24g                                   |
| 毛重       | 50g                                   |
| 产品尺寸   | 71.5 x 24 x 8mm                       |
| 包装尺寸   | 136 x 92 x 10mm                       |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/zigbee/zigbee_sch_01.webp" width="80%">

## 管脚映射

### Unit ZigBee

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 数据手册

- [CC2630 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/Zigbee_CC2630/cc2630_datasheet.pdf)

## 软件开发

### Arduino

- [Unit ZigBee P2P Chat Room Example](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/Zigbee_CC2630/P2P_TEST)
- [Unit ZigBee P2P Rssi 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/Zigbee_CC2630/RSSI_TEST)

### UiFlow2

- [Unit ZigBee UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/zigbee.html)

### 通信协议

- [模块使用手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/Zigbee_CC2630/Zigbee_Module_Guide.pdf)
- [上位机使用说明](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/Zigbee_CC2630/Zigbee_PCTool_Guide.pdf)
- [上位机调试工具](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/Zigbee_CC2630/Zigbee%20PCTool.msi)

### EasyLoader

| Easyloader                                    | 下载链接                                                                                                                  | 备注 |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit ZigBee P2P Chat Room Example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_Zigbee_P2P_CHATROOM.exe)     | /    |
| Unit ZigBee Coordinator Example with M5Core   | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_Zigbee_RSSI_Coordinator.exe) | /    |
| Unit ZigBee End Device Example with M5Core    | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_Zigbee_RSSI_EndDevice.exe)   | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/Zigbee_CC2630.mp4" type="video/mp4">
</video>
