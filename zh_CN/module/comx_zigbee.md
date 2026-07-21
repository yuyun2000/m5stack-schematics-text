# Module COMX Zigbee

<span class="product-sku">SKU:M031-Z</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_09.webp">
</PictureViewer>

## 描述

**Module COMX Zigbee** 是 M5Stack 推出的一款 Zigbee 自组网通讯模块。模块采用 CC2630F128 方案，内部集成 Zigbee 协议栈，开放串口通信接口。集成外部天线，单节点稳定通信距离可达 1km ，200 级 router 深度，通过 MESH 组网方式能够将你的物联网应用进行广范围的延展，兼具超低功耗与高灵敏度特性。Zigbee 网络可以支持数以百计的节点，并具有增强的安全特性。可为家庭和楼宇自动化提供完整且可互操作的物联网解决方案。

## 注意事项

?> 兼容性 | 搭配 Fire 主控使用时候，由于 PSRAM 引脚（G16/G17）冲突，使用时候请将模块底座拨码开关引脚切换至 TX (G0/G13),RX (G5/G15)。

## 产品特性

- CC2630F128
- 免设置快速入网
  - 初始化 coordinator 并配置 router 预设，可实现连按三次按键自动入网
- 串口通信
- 低功耗 (模组工作电流：25mA, 休眠 5uA)
- 动态路由维护，支持 200 级路由深度
- 传输速度 250Kbps
- 节点通信距离 1km
- UART 透明传输 / 广播 / P2P

## 包装内容

- 1 x Module COMX Zigbee
- 1 x SMA 天线

## 应用场景

- 智能家居
- 物联网采集节点
- 楼宇自动化

## 规格参数

| 规格               | 参数                                  |
| ------------------ | ------------------------------------- |
| CC2630F128         | ARM Cortex-M3 32bit                   |
| 通讯方式           | UART 38400bps 8N1 (default)           |
| 通信距离           | 1km (空旷地区)                        |
| 工作频率           | 2.4GHZ (2405MHz-2480MHz, 步长为 5MHz) |
| DC 接口规格        | 5.5mm                                 |
| 产品尺寸           | 54.0 x 54.0 x 13.2mm                  |
| 产品重量（含天线） | 37.0g                                 |
| 包装尺寸           | 165.0 x 60.0 x 36.0mm                 |
| 毛重               | 70.0g                                 |

## 操作说明

\#> 供电切换 | 模块底座带有 DC 电源输入接口，使用该接口接入电源请严格按照输入范围 (5-12V) 防止模块损坏。内部电源拨码开关可调节内部的端子 VIN 的电压水平，用于适配不同模块。

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte/comx_lte_dc_power.webp" width="70%">

## 原理图

<SchViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_sch_01.webp" width="80%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_zigbee/comx_zigbee_sch_02.webp" width="80%">
</SchViewer>

## 管脚映射

### M5-Bus

\#> Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     |          |
| GND      | 3    | 4     |          |
| GND      | 5    | 6     |          |
|          | 7    | 8     |          |
|          | 9    | 10    |          |
|          | 11   | 12    | 3V3      |
|          | 13   | 14    |          |
| TXD (SW) | 15   | 16    | RXD (SW) |
|          | 17   | 18    |          |
|          | 19   | 20    | TXD (SW) |
|          | 21   | 22    | RXD (SW) |
| TXD (SW) | 23   | 24    | RXD (SW) |
|          | 25   | 26    |          |
|          | 27   | 28    | 5V       |
|          | 29   | 30    |          |
::

## 尺寸图

- [Module COMX Zigbee 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/935/MODLUE-COMX_page_01.png" width="100%">

## 数据手册

- [CC2630 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/Zigbee_CC2630/cc2630_datasheet.pdf)
- [上位机使用说明](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/Zigbee_CC2630/Zigbee_PCTool_Guide.pdf)
- [上位机调试工具](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/Zigbee_CC2630/Zigbee%20PCTool.msi)

## 软件开发

### Arduino

- [Zigbee P2P CHAT ROOM](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/COM_Zigbee_CC2630/P2P_TEST)
- [Zigbee RSSI TEST](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/COM_Zigbee_CC2630/RSSI_TEST)

### UiFlow1

- [Module COMX Zigbee UiFlow1 文档](/zh_CN/uiflow/blockly/module/comx_zigbee)

### UiFlow2

- [Module COMX Zigbee UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/zigbee.html)

### 通信协议

- [模块使用手册](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/Zigbee_CC2630/Zigbee_Module_Guide.pdf)

### Easyloader

| Easyloader                                                      | 下载链接                                                                                                                  | 备注 |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---- |
| Module COMX Zigbee P2P Chat Room Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_Zigbee_P2P_CHATROOM.exe)     | /    |
| Module COMX Zigbee Coordinator Example Easyloader with M5Core   | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_Zigbee_RSSI_Coordinator.exe) | /    |
| Module COMX Zigbee End Device Example Easyloader with M5Core    | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_Zigbee_RSSI_EndDevice.exe)   | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/Zigbee_CC2630.mp4" type="video/mp4">
</video>
