# Unit CAN

<span class="product-sku">SKU:U085</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/can/can_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/can/can_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/839/U085-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/can/can_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/can/can_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/can/can_06.webp">
</PictureViewer>

## 描述

**Unit CAN**是一款独立的控制器区域网络 (CAN) 收发器单元，可用于构建复杂的 CAN 通信网络。内置的 DC-DC 隔离电源芯片可以隔离噪音和干扰，防止损坏敏感电路。隔离的 CAN 收发器的型号是 CA-IS3050G，它可以提供差分接收和差分传输能力。该总线可支持多达 110 个节点，信号传输速率可达 1 Mbps。具有限流、过压、接地损耗保护 (-40V～40V) 和热关断功能，能防止输出短路，符合 ISO11898-2 标准的技术规范。CAN 是 ISO 国际标准串行通信协议。CAN 属于现场总线类别。它是一种能够有效支持分布式控制或实时控制的串行通信网络。
基于 CAN 总线的分布式控制系统采用多主机竞争仲裁方式通讯，具有多主机操作、分散仲裁和广播通信的特点。它在以下几个方面具有明显的优势：网络中节点间的数据通信速度快、故障率低。同一优先级的同一线路，同一优先级的多个节点通信时，同一优先级的多个节点间的通信将避免发生拥塞。通信距离可达 10 km (速率小于 5 Kbps)，速率可达 1 Mbps (通信距离小于 40 m)。

## 产品特性

- 内置隔离 DC-DC
- 电源指示灯
- 信号速率高达 1Mbps
- 保护功能：信号隔离、限流、过压保护、热关断
- 2 个乐高兼容孔
- HY2.0-4P 接口

## 包装内容

- 1 x Unit CAN
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96-4P
- 1 x 120R 电阻

## 应用场景

- CAN 总线通信
- 工业现场控制
- 安全系统

## 规格参数

| 规格       | 参数                           |
| ---------- | ------------------------------ |
| 隔离耐压值 | 1000V                          |
| 最高速率   | 1Mbps                          |
| 支持节点数 | 110                            |
| 低环路延迟 | -150ns                         |
| 共模电压   | -12V ~ 12V                     |
| 外壳材料   | PC                             |
| 保护功能   | 限流，过压，主动态超时，热关断 |
| 产品尺寸   | 56.0 x 24.0 x 10.2mm           |
| 产品重量   | 9.1g                           |
| 包装尺寸   | 138.0 x 93.0 x 11.2mm          |
| 毛重       | 17.1g                          |

## 原理图

- [Unit CAN 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/586/SCH_UNIT_ISOCAN_v1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/586/SCH_UNIT_ISOCAN_v1.1_sch_01.png">
</SchViewer>

## 管脚映射

### HY2.0-4P

::grove-table
| HY2.0-4P | Black | Red | Yellow | White  |
| -------- | ----- | --- | ------ | ------ |
| PORT.C   | GND   | 5V  | CAN_TX | CAN_RX |
::

## 尺寸图

- [Unit CAN 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/839/U085_MODEL_SIZE.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/839/U085_Model_Size.jpg" width="100%">

## 数据手册

- [CA-IS3050G](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/CA-IS3050G.pdf)

## 软件开发

### Arduino

- [CAN-Transceiver TEST](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/CAN)

### UiFlow1

- [Unit CAN UiFlow1 文档](/zh_CN/uiflow/blockly/unit/can)

### UiFlow2

- [Unit CAN UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/can.html)

### EasyLoader

| Easyloader                   | 下载链接                                                                                                                             | 备注 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| Unit CAN example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_CAN_Unit_SEND%26RECEIVE.zip) | /    |

## 产品对比

::compare-table
| 产品对比表   | [Unit Mini CAN](/zh_CN/unit/Unit-Mini%20CAN) ![Unit Mini CAN](https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-Mini%20CAN/img-fde85c7a-655d-497c-8ece-3f3e81e2dfc4.webp) | [Unit CAN](/zh_CN/unit/can) ![Unit CAN](https://static-cdn.m5stack.com/resource/docs/products/unit/can/can_cover_01.webp) |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| CAN 收发器   | TJA1051T/3                                                                                                                                                                              | CA-IS3050G                                                                                                                |
| 是否电源隔离 | 不带隔离                                                                                                                                                                                | 带隔离                                                                                                                    |
| 速率         | 1Mbps                                                                                                                                                                                   | 1Mbps                                                                                                                     |
| 输入电源     | HY2.0-4P 接口 DC 5V 供电 <br/> HT3.96-4P 接口 DC 9 ~ 24V 供电                                                                                                                           | HY2.0-4P 接口 DC 5V 供电                                                                                                  |
::

## 相关视频

<video id="example_video" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/CAN%20UNIT.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113157087432460&bvid=BV1TqtGe5EUN&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/_3YKMTSZpzA?si=-mUanDvaO1saX87v" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
