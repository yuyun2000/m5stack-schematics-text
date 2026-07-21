# Unit GPS

<span class="product-sku">SKU:U032</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/gps/gps_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/gps/gps_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/gps/gps_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/gps/gps_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/gps/gps_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/gps/gps_07.webp">
</PictureViewer>

## 描述

**Unit GPS**是一款卫星定位 Unit。内部集成科微北斗导航芯片 AT6558 和信号放大芯片 MAX2659，能够提供优质的卫星定位服务。

**AT6558**是一款高性能的导航芯片，支持多种卫星导航系统，以 56 通道接收卫星信号，同时接收 6 个卫星导航系统的 GNSS 信号，并且实现联合定位、导航和授时，获得准确的全球位置信息。AT6558 能够在城市、峡谷、高架下面等弱信号的地方，以及汽车内部任何位置可以快速、准确地定位。此模块可用于车载监控、公交车报站、车载导航、船载导航、笔记本导航等产品上。

**使用时，请将该 Unit 连接到 PORT C，它将通过 UART 协议与 M5Core 进行通信**

UART 参数设置:

- 波特率 (**默认: 9600bps**)
- 起始位 (1 bit)
- 停止位 (1 bit)
- 校验位 (无)

## 产品特性

- 支持 BDS / GPS 卫星导航系统的单系统定位，或任意组合的多系统联合定位
- 低功耗设计
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit GPS
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 车载、船载定位与导航
- 智能执法定位

## 规格参数

| 规格               | 参数                                                     |
| ------------------ | -------------------------------------------------------- |
| 定位精度           | 2.5 米                                                   |
| 通道数             | 56                                                       |
| 更新频率           | 1-10Hz                                                   |
| 最大速度           | 515 米 / 秒                                              |
| 工作最大加速度温度 | <= 4g                                                    |
| 灵敏度             | 跟踪: -162dBm，捕捉: -148dBm，冷启动: -146dBm            |
| 启动时间           | 冷启动: 35 seconds，温启动: 32 seconds，热启动: 1 second |
| 工作温度           | -40 ~ 85°C                                               |
| 产品重量           | 13g                                                      |
| 毛重               | 26g                                                      |
| 产品尺寸           | 48 x 24 x 8mm                                            |
| 包装尺寸           | 136 x 92 x 13mm                                          |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/gps/gps_sch_01.webp" width="80%">

## 管脚映射

### Unit GPS

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/gps/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 数据手册

- [AT6558](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/AT6558_en.pdf)
- [MAX2659](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/MAX2659_en.pdf)
- [TinyGPS++ library](http://arduiniana.org/libraries/tinygpsplus/)
- [CASIC 多模卫星导航接收机协议规范](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/950/Multimode_satellite_navigation_receiver_cn.pdf)
- [上位机软件 GnssToolKit3 (Windows Version) ](http://www.icofchina.com/d/file/xiazai/2018-05-23/2b29a8da746eec0ef1dcd9deae895298.zip)

## 软件开发

### Arduino

- [Unit GPS 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/GPS_AT6558)

### UiFlow1

- [Unit GPS UiFlow1 文档](/zh_CN/uiflow/blockly/unit/gps)

### EasyLoader

| Easyloader               | 下载链接                                                                                       | 备注 |
| ------------------------ | ---------------------------------------------------------------------------------------------- | ---- |
| Unit GPS Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_GPSRaw.exe) | /    |

## 相关视频

- UiFlow2 GPS Unit

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113066490463376&bvid=BV1ZFHkebExc&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/r6kZPjTDq7c?si=d3pzkk2hJl573lvA" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
