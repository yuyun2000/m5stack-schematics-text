# Module13.2 LAN

<span class="product-sku">SKU:M136</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/LAN Module 13.2/img-bb8b9bf1-a7ca-46ae-8e5c-bcc4ae7a6184.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/LAN Module 13.2/img-d6bb4ea2-2786-42ff-882c-62c72738a864.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/LAN Module 13.2/img-4f54f059-6697-4f6d-9e57-c1b772b92287.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/LAN Module 13.2/img-b384fc76-b8f4-413f-b12e-5ddb69182a16.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/LAN Module 13.2/img-30d7882f-d8ec-4bfd-a3ce-5840d24d65d6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/LAN Module 13.2/img-507f44ee-f670-4515-8c2e-3e3246e65e6f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/LAN Module 13.2/img-6d4519bf-fc94-45c1-94e3-262a123490ab.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/LAN Module 13.2/img-f9248228-436c-435c-8f2f-97e9a772831b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/LAN Module 13.2/img-3f838da4-12ce-41bc-a28a-4972bbf0e636.webp">
</PictureViewer>

## 描述

**Module13.2 LAN** 是一款以太网控制器模块，内置 W5500 全硬件 TCP/IP 嵌入式以太网控制器 (SPI 通信接口)，支持多种通信协议 (TCP，UDP，IPv4，ICMP，ARP，IGMP 和 PPPoE 等) 并集成储存缓存区便于以太网数据包处理。安全性方面：内置信号隔离百兆变压器，将 RJ45 接口输入端的信号转换为适合输出端的信号，提供电气隔离和防止电磁的干扰。供电方面：DC-JACK 接口以及相应的 DC/DC 降压电路，可为整个设备提供电源。板载片选**跳线插针**，可实现多个 Module13.2 LAN 堆叠使用，预留 HT3.96 接口，用户可以添加扩展器件。兼具性能与拓展灵活性的 Module13.2 LAN 能够为你提供更加简洁的嵌入式以太网连接方式。适用于工业自动化、物联网 (IoT)、数据采集与远程监控等领域。

## 产品特性

- 信号隔离：内置百兆变压器，实现信号隔离，防止电磁干扰，提高系统稳定性和可靠性。
- 电源供应：提供 9-24V DC-JACK 接口和 DC-DC 降压电路，为整个设备提供电源，简化电源管理。
- 扩展性：预留 HT3.96 接口，允许用户添加扩展器件，以满足特定应用的需求，提供更大的灵活性。
- 支持多种协议：内置 W5500 全硬件 TCP/IP 嵌入式以太网控制器，协议支持，包括 TCP、UDP、IPv4 等。

## 包装内容

- 1 x Module13.2 LAN
- 2 x HT3.96-4P 端子
- 2 x HT3.96-4P 座子

## 应用场景

- 工业自动化
- 物联网 (IoT)
- 网络通信设备
- 数据采集与远程监控

## 规格参数

| 规格         | 参数                     |
| ------------ | ------------------------ |
| 以太网控制器 | W5500                    |
| 网口         | RJ45 自适应 10/100M 网口 |
| 外接供电电压 | 9-24V                    |
| 工作温度     | 0-40°C                   |
| 通讯方式     | SPI                      |
| 产品尺寸     | 54 x 54 x 13.2mm         |
| 包装尺寸     | 132 x 95 x 21mm          |
| 产品重量     | 29.6g                    |
| 毛重         | 40.7g                    |

## 原理图

- [Module13.2 LAN 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/562/Sch_Module13.2_LAN.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/562/Sch_Module13.2_LAN_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     | INTN(JC) |
| GND      | 3    | 4     |          |
| GND      | 5    | 6     |          |
| SPI_MOSI | 7    | 8     |          |
| SPI_MISO | 9    | 10    |          |
| SPI_SCLK | 11   | 12    |          |
|          | 13   | 14    |          |
|          | 15   | 16    |          |
| SDA      | 17   | 18    | SCL      |
|          | 19   | 20    | CSN(JC)  |
|          | 21   | 22    | RSTN(JC) |
| CSN(JC)  | 23   | 24    | RSTN(JC) |
| HPWR     | 25   | 26    | INTN(JC) |
| HPWR     | 27   | 28    | 5V       |
| HPWR     | 29   | 30    |          |
::

\#> 引脚切换说明 | Module13.2 LAN 的 M5-Bus 总线侧提供了 3 组跳线帽（上表中带有`JC`字样的引脚），可用于切换不同的 IO 连接。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/957/M136_pins_change_01.png" width="60%" >

## 尺寸图

- [Module13.2 LAN 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/957/lan-module.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/957/lan-module_page_01.png" width="100%">

## 数据手册

- [Datasheet - W5500](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/W5500_datasheet_v1.0.2_1_en.pdf)

## 软件开发

### Arduino

- [Module13.2 LAN Arduino 驱动库](https://github.com/m5stack/M5Module-LAN-13.2/tree/main)
- [Module13.2 LAN HTTP Example](https://github.com/m5stack/M5Module-LAN-13.2/tree/main/examples/HTTP)
- [Module13.2 LAN MQTT Example](https://github.com/m5stack/M5Module-LAN-13.2/tree/main/examples/MQTT)
- [Module13.2 LAN WebServer Example](https://github.com/m5stack/M5Module-LAN-13.2/tree/main/examples/WebServer)

### UiFlow1

- [Module13.2 LAN UiFlow1 文档](/zh_CN/uiflow/blockly/module/lan)

### UiFlow2

- [Module13.2 LAN UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/lan.html)

## 相关视频

- Module13.2 LAN 案例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/LAN%20Module%2013.2/M136%20Module13.2-LAN%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115705915771415&bvid=BV1DZm7BWEqM&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/4i8huB7WizI?si=uM5BvmtCsZ8gtnEE" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
