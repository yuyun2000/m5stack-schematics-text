# Cap CC1101

?> Work in progress | 本产品包装及软件研发尚未完成，最终功能及资料可能有变，敬请理解。

<span class="product-sku">SKU:U219</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1250/U219_Cap_CC1101_main_pictures_01.jpg">
</PictureViewer>

## 描述

**Cap CC1101** 是一款集成 Sub-1 GHz 射频与 NFC 功能的扩展模块。射频部分基于 TI CC1101 收发器，通过内置单刀三掷（SP3T）射频开关和多频段射频匹配电路，将 315MHz、433MHz、868MHz、915MHz 四个频段汇聚到一个 RP-SMA 天线接口，支持 2-FSK、4-FSK、GFSK、MSK、ASK、OOK 等调制方式。

NFC 部分采用 ST25R3916 芯片，支持 ISO14443A/B、FeliCa™、ISO15693 协议，可工作在读卡器、卡模拟模式，读卡距离最远可达 45mm。模块通过 SPI 通信，板载 DC-DC 降压电路，引出标准 Grove 接口方便扩展传感器。适用于遥控信号抓包与重放、门禁卡/公交卡的读取与模拟、智能家居 DIY 等场景。

## 产品特性

- SPI 串行通信协议
- CC1101 低功耗 Sub-1 GHz 射频收发器
- 独立的 64 字节射频 RX FIFO 和 TX FIFO
- 内置双单刀三掷（SP3T）射频开关与多频段射频匹配网络，支持频段动态切换
- 工作频率 315/433/868/915 MHz
- 支持 2-FSK、4-FSK、GFSK、MSK、ASK、OOK 调制方式
- 外置 RP-SMA 天线接口
- NFC 支持读卡器、卡模拟模式
- 兼容标准：NFC-A、NFC-B、NFC-F、NFC-V
- NFC 读写距离最大可至 45mm
- 512 字节 NFC FIFO
- Grove 接口支持扩展传感器
<!-- - 开发平台:
  - Arduino
  - UiFlow2 -->

## 包装内容

- 1 x Cap CC1101
- 1 x 315 MHz RP-SMA 胶棒天线
- 1 x 433 MHz RP-SMA 胶棒天线
- 1 x 868 MHz RP-SMA 胶棒天线

## 应用场景

- 遥控信号抓包与重放（如汽车钥匙、遥控门铃）
- 门禁卡/公交卡的读取与模拟
- 智能家居 DIY

## 规格参数

| 规格       | 参数                                                                                                               |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| 射频芯片   | CC1101                                                                                                             |
| 工作频段   | 315/433/868/915 MHz                                                                                                |
| 通讯距离   | 315MHz: 435m<br>433/868/975MHz: 441m                                                                               |
| 发射功率   | +10 dBm                                                                                                            |
| 接收灵敏度 | 最高 -99.5 dBm                                                                                                     |
| NFC 芯片   | ST25R3916                                                                                                          |
| NFC 协议   | **读写器模式**：NFC-A/B（兼容 ISO14443A/B）、NFC-F（FeliCa™）、NFC-V（ISO15693 ）<br>**卡模拟模式**：NFC-A / NFC-F |
| 通讯接口   | SPI                                                                                                                |
| 休眠功耗   | DC 5V@140.87uA（CC1101、NFC 均休眠）                                                                               |
| 工作功耗   | DC 5V@96mA（CC1101 最大功率连续发送数据，NFC 连续读卡）                                                            |

<!-- | 产品尺寸     | XX x XX x XXmm                                                                                                                                                                                        |
| 包装尺寸     | XX x XX x XXmm                                                                                                                                                                                        |
| 产品重量     | XXg                                                                                                                                                                                                   |
| 毛重         | XXg                                                                                                                                                                                                   | -->

## 原理图

- [Cap CC1101 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1250/SCH_Cap_CC1101_SCH_V0.3_20260528.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1250/SCH_Cap_CC1101_SCH_V0.3_20260528_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1250/SCH_Cap_CC1101_SCH_V0.3_20260528_page_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1250/SCH_Cap_CC1101_SCH_V0.3_20260528_page_03.png">
</SchViewer>

## 管脚映射

### Cap-Bus

::m5-bus-table
| PIN           | LEFT | RIGHT | PIN       |
| ------------- | ---- | ----- | --------- |
| CC1101_G0     | 1    | 14    | CC1101_CS |
| CC1101_RF_SW0 | 2    | 13    | SPI_MISO  |
|               | 3    | 12    | SPI_MOSI  |
|               | 4    | 11    | SPI_SCLK  |
| 5V_OUT        | 5    | 10    | NFC_CS    |
| GND           | 6    | 9     | NFC_IRQ   |
|               | 7    | 8     | POWER_EN  |
::

| Cardputer-Adv       | G5        | G13           | G15       | G40      | G14      | G39      |
| ------------------- | --------- | ------------- | --------- | -------- | -------- | -------- |
| Cap CC1101 (CC1101) | CC1101_CS | CC1101_RF_SW0 | CC1101_G0 | SPI_SCLK | SPI_MOSI | SPI_MISO |

| Cardputer-Adv          | G4      | G6     | G40      | G14      | G39      |
| ---------------------- | ------- | ------ | -------- | -------- | -------- |
| Cap CC1101 (ST25R3916) | NFC_IRQ | NFC_CS | SPI_SCLK | SPI_MOSI | SPI_MISO |

### 射频开关控制真值表

| RF_SW0 | RF_SW1 | 频段          |
| ------ | ------ | ------------- |
| 0      | 0      | 315MHz        |
| 0      | 1      | 433MHz        |
| 1      | 1      | 868MHz/915MHz |

<!-- ## 尺寸图

- [Cap CC1101 模型尺寸 PDF]()

<img src="" width="100%"> -->

## 数据手册

- [CC1101](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/CC1101_Datasheet.pdf)
- [ST25R3916](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1229/st25r3916_datasheet.pdf)

## 软件开发

### Arduino

<!-- - [Cap CC1101 Arduino 快速上手](/zh_CN/arduino/projects/cap/cap_cc1101) -->
- [Cap CC1101 Arduino CC1101 驱动库](https://github.com/jgromes/RadioLib)
- [Cap CC1101 Arduino NFC 驱动库](https://github.com/m5stack/M5Unit-NFC)

<!-- ### UiFlow2

- [Cap CC1101 UiFlow2 文档]()

## 相关视频

- Cap CC1101 产品介绍 -->
