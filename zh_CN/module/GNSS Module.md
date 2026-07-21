# Module GNSS

<span class="product-sku">SKU:M135</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/GNSS Module/img-87c65bc6-1d16-4078-b0dd-4011cbf04d97.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/GNSS Module/img-824d0251-e9ac-4d4d-ae16-7aaea58827eb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/GNSS Module/img-00db1283-6546-467b-b460-b42a811302fb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/GNSS Module/img-53c0dd2a-0643-4e99-b3fa-17d303010c73.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/GNSS Module/img-df220a2d-21c3-43f0-93ca-e2688a159910.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/GNSS Module/img-2bfb3252-cad6-44e7-aa23-d6fb01c459a3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/GNSS Module/img-129dc7fb-5f50-4ae6-add2-be5f69e9523d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/GNSS Module/img-d060bc72-272f-48f4-9a64-0f5e9f965831.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/GNSS Module/img-b0cdbc6c-d5d5-42bb-bdf6-69016e003b14.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/956/M135-weight.jpg">
</PictureViewer>

## 描述

**Module GNSS** 是一款多功能全球定位通信模块，内置 **NEO-M9N-OOB** 高精度 GNSS 定位模组，支持多种卫星信号接收。同时集成六轴姿态传感器 BMI270、三轴地磁计 BMM150 和气压传感器，实现全面测量位置、角度、高度等地理信息。模块内部预留 M5Stamp 系列拓展位，可拓展更多物联网通信功能。适用于定位与导航、农业、物流、地理测绘、环境检测等领域。

## 产品特性

- 多种卫星定位：支持多种卫星系统 (GPS、GLONASS、伽利略和北斗)，精确定位。
- 高精度：定位精度约 1.5 米。
- 多信号接收：同时接收四个 GNSS 信号，定位更准确。
- 外置天线：可选配置，适应不同需求。
- 数据保护：备用电池与 EEPROM 芯片，保证断电时数据安全。
- 多传感器：集成六轴姿态传感器、地磁计和气压传感器。
- 灵活配置：可自定义串口引脚、PPS 同步信号引脚等设置。
- 多领域应用：适用于定位、农业、物流、环境监测等。
- 物联网支持：可加入 M5Stamp 无线通信模块，实现远程通讯。

## 包装内容

- 1 x Module GNSS
- 1 x 外置有源 GPS/BD 天线 (长度: 1 m)
- 1 x 天线馈线
- 2 x M2\*4 螺丝
- 1 x 六角钥匙 1.5mm

## 应用场景

- 定位与导航
- 农业
- 物流
- 地理测绘
- 环境检测

## 规格参数

| 规格             | 参数                                                                                                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GNSS 芯片        | NEO-M9N-00B<br/> 精度：1.5 米、<br/> 运行限制：最大海拔高度：80000m、最大重力加速度：4G、最大运动速度：500m/s <br/> 支持通道个数：92 个 <br/> 动态航向精度：0.3 度 <br/> 最大导航更新速率 ：25Hz |
| 六轴姿态传感器   | BMI270<br/> 加速度计量程范围：±2g/±4g/±8g/±16g <br/> 陀螺仪流程范围：±125dps/±250dps/±500dps/±1000dps/±2000dps                                                                                   |
| 三轴地磁计       | BMM150 (磁场分辨率：0.3uT)                                                                                                                                                                       |
| 气压传感器       | BMP280 (测量范围：300 ~ 1100 hPa)                                                                                                                                                                |
| 支持导航卫星类型 | GPS / QZSS 、GLONASS、Galileo、BeiDou                                                                                                                                                            |
| 波特率           | 默认 38400bps 8N1                                                                                                                                                                                |
| 产品尺寸         | 54.0 x 54.0 x 13.1mm                                                                                                                                                                             |
| 产品重量         | 14.3g                                                                                                                                                                                            |
| 包装尺寸         | 126.0 x 67.0 x 23.0mm                                                                                                                                                                            |
| 毛重             | 80.0g                                                                                                                                                                                            |

## 操作说明

?> BMM150 磁场干扰 | 带有磁铁的产品可能对 BMM150 磁场传感器造成干扰，导致读数异常。当搭配含有磁铁的 M5 主控设备时，需拆除磁铁，同时避免 BMM150 传感器放置在强磁场附近。

\#> 信号质量 | 为了使 GPS 模块获得良好信号，请在使用时将模块放置在室外。

\#> 预留的拨码开关和拨动开关，可以调整串口引脚、时间戳 PPS 引脚和姿态传感器通讯地址。

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/GNSS%20Module/2.png" width="50%" />

\#> 传感器 I2C 地址 | BMM150 的 I2C 总线是连接到了 BMI270 上的，注意主机扫描不到 BMM150 的 I2C 地址

| Chip        | ADDRESS |
| ----------- | ------- |
| BMI270 ADDR | 0x69    |
| BMM150 ADDR | 0x10    |
| BMM280 ADDR | 0x76    |

## 原理图

- [Module GNSS 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/561/SCH_Module_GNSS_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/561/SCH_Module_GNSS_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

\#> Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN          | LEFT | RIGHT | PIN              |
| ------------ | ---- | ----- | ---------------- |
| GND          | 1    | 2     | NEO_TXD/PPS (SW) |
| GND          | 3    | 4     |                  |
| GND          | 5    | 6     |                  |
|              | 7    | 8     |                  |
|              | 9    | 10    |                  |
|              | 11   | 12    | 3V3              |
|              | 13   | 14    |                  |
| NEO_TXD (SW) | 15   | 16    | NEO_RXD (SW)     |
| I2C_SDA      | 17   | 18    | I2C_SCL          |
|              | 19   | 20    |                  |
| NEO_RXD (SW) | 21   | 22    | NEO_TXD (SW)     |
| NEO_RXD (SW) | 23   | 24    | NEO_RXD/PPS (SW) |
| HPWR         | 25   | 26    | NEO_TXD/PPS (SW) |
| HPWR         | 27   | 28    | 5V               |
| HPWR         | 29   | 30    | BAT              |
::

## 尺寸图

- [Module GNSS 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M135-and-M146-model-size-GNSS-1.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1188/M135-and-M146-model-size-GNSS-1_page_01.png" width="100%">

## 数据手册

- [BMI270](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMI270.PDF)
- [BMM150](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/K128%20CoreS3/BMM150.PDF)
- [NEO-M9N-00B](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/4Relay%20Module%2013.2_V1.1/NEO-M9N-00B.pdf)
- [u-blox 协议规范](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/GNSS%20Module/u-blox8-M8_ReceiverDescrProtSpec__UBX-13003221__Public.pdf)

## 软件开发

### Arduino

- [Module GNSS 获取地理位置](https://github.com/m5stack/M5Module-GNSS/tree/main/examples/getPosition)
- [Module GNSS 获取姿态传感器、地磁计、大气压力传感器数值](https://github.com/m5stack/M5Module-GNSS/tree/main/examples/getSensorData)

### UiFlow1

- [Module GNSS UiFlow1 文档](/zh_CN/uiflow/blockly/module/gnss)

### UiFlow2

- [Module GNSS UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/gnss.html)

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115807786894352&bvid=BV1nWvYBUEri&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/rIazK7yoS7U?si=szIHlBqZQy6ATFmJ" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
