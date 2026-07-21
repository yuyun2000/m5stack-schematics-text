# Unit MQTT-PoE

<span class="product-sku">SKU:U129-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt_poe/mqtt_poe_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt_poe/mqtt_poe_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt_poe/mqtt_poe_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt_poe/mqtt_poe_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt_poe/mqtt_poe_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt_poe/mqtt_poe_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt_poe/mqtt_poe_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt_poe/mqtt_poe_08.webp">
</PictureViewer>

## 描述

**Unit MQTT-PoE** 是一款以太网 MQTT 通信模块，硬件采用 PoE 供电 + W5500 以太网控制器组合，采用 UART 通信接口 (AT 指令控制)，集成 RJ45 自适应 10 / 100M 网口。支持 4x Topic 订阅。具备极低的网络延迟与高稳定性，适合应用于各种工业自动化 、 安防监控系统 、 自动测控系统 、 设备数据上云应用。

\#> Unit MQTT 版本比较 | 相对于 [Unit MQTT](/zh_CN/unit/mqtt)，该 PoE 版本集成 PoE 供电功能，具备 1.2A@5V (6W) 负载能力。

## 产品特性

- 内嵌 W5500 以太网芯片
- RJ45 网口 10/100Mbps
- PoE 供电能力：1.2A@5V (6W)
- 以太网 MQTT 通信
- 支持 4x Topic 订阅
- 低延迟
- 开发方式:
  - AT 指令，UART: 9600bps 默认
  - 开发平台: UiFlow，Arduino

## 包装内容

- 1 x Unit MQTT-PoE
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 远程数据采集 / 上云

## 规格参数

| 规格         | 参数                              |
| ------------ | --------------------------------- |
| 模组处理器   | ARM  Cortex-M3                    |
| 通信接口     | UART: baud 9600bps 8N1 默认       |
| MQTT         | 支持 4x Topic 订阅，不支持 MQTTS  |
| 网口         | RJ45 自适应 10/100M 网口          |
| 延时         | 延迟 \`10ms                       |
| PoE 供电能力 | 1.2A@5V (6W) / 供电电压 DC 37-57V |
| 工作电流     | 190mA                             |
| 待机电流     | 130mA                             |
| 产品重量     | 27.0g                             |
| 毛重         | 34.2g                             |
| 产品尺寸     | 72 x 26 x 19mm                    |
| 包装尺寸     | 73 x 35 x 20mm                    |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt_poe/mqtt_poe_sch_01.webp" width="70%">

## 管脚映射

### Unit MQTT-PoE

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/829/U129_Model_Size_page_01.png" width="70%">

## 软件开发

### Arduino

- [Unit MQTT-PoE Arduino 驱动库](https://github.com/m5stack/UNIT_MQTT)

### UiFlow2

- [Unit MQTT-PoE UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/mqttpoe.html)

### 通信协议

\#> 注意：发送每一条命令的结尾需添加回车换行`\r\n`，否则模块无法识别命令

- [Unit MQTT AT 指令](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/829/Unit-MQTT-Protocol-CN.pdf)

## 相关视频

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/mqtt_poe_video.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114097785930721&bvid=BV1j49iYzEQd&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/nxp0Veib3EE?si=7SRyKqigceWo3MZn" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
