# Unit MQTT

<span class="product-sku">SKU:U129</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt/mqtt_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt/mqtt_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt/mqtt_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt/mqtt_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt/mqtt_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt/mqtt_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt/mqtt_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/mqtt/mqtt_08.webp">
</PictureViewer>

## 描述

**Unit MQTT** 是一款以太网 MQTT 通信模块，内嵌 W5500 以太网芯片，采用 UART 通信接口 (AT 指令控制)，集成 RJ45 自适应 10 / 100M 网口。支持 4x Topic 订阅。具备极低的网络延迟与高稳定性，适合应用于各种工业自动化、安防监控系统、自动测控系统、设备数据上云应用。

## 产品特性

- 内嵌 W5500 以太网芯片
- RJ45 网口 10/100Mbps
- 以太网 MQTT 通信
- 支持 4x Topic 订阅
- 低延迟
- 开发方式:
  - AT 指令，UART: 9600bps 默认
  - 开发平台: UiFlow，Arduino

## 包装内容

- 1 x Unit MQTT
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 远程数据采集 / 上云

## 规格参数

| 规格         | 参数                             |
| ------------ | -------------------------------- |
| 模组处理器   | ARM  Cortex-M3                   |
| 通信接口     | UART: baud 9600bps 8N1 默认      |
| MQTT         | 支持 4x Topic 订阅，不支持 MQTTS |
| 网口         | RJ45 自适应 10/100M 网口         |
| 延时         | 延迟 \`10ms                      |
| 待机工作电流 | 40.4mA                           |
| 产品重量     | 22.4g                            |
| 毛重         | 27.2g                            |
| 产品尺寸     | 72 x 26 x 19mm                   |
| 包装尺寸     | 73 x 35 x 20mm                   |

## 管脚映射

### Unit MQTT

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/829/U129_Model_Size_page_01.png" width="70%">

## 软件开发

### Arduino

- [Unit MQTT Arduino 驱动库](https://github.com/m5stack/M5Unit-MQTT)

### UiFlow2

- [Unit MQTT UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/mqtt.html)

### 通信协议

\#> 注意：发送每一条命令的结尾需添加回车换行`\r\n`，否则模块无法识别命令

- [Unit MQTT AT 指令](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/829/Unit-MQTT-Protocol-CN.pdf)

## 相关视频

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UNIT_MQTT.mp4" type="video/mp4">
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
