# Unit GPS v1.1

<span class="product-sku">SKU:U032-V11</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/7.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/849/U032-V11-package.jpg">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/9.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/849/U032-V11_Weight.jpg">
</PictureViewer>

## 描述

**Unit GPS v1.1** 是一款 GNSS 全球定位导航单元，采用 **AT6668** 方案，内置陶瓷天线，提供更加精确和可靠的卫星定位服务。相比之前的产品，AT6668 支持多频多模 GNSS 信号接收，可接收多个卫星导航系统 (包括 GPS、BD2、BD3、GLONASS、GALILEO 和 QZSS 等) 的信号，支持多系统联合定位和单系统独立定位，具备更强的抗干扰能力和更高的定位精度。在信号较弱的区域，能快速获取更高精度的位置信息。此模块适用于车载定位与导航、物联网定位设备等高精度定位的应用场景。

## 产品特性

- 支持多种卫星导航系统 (GPS/QZSS/BD2/BD3/GAL/GLO)
- 多频点多系统接收
- 多通道
- 2 x LEGO 兼容孔
- 编程平台：Arduino、UiFlow 等

## 包装内容

- 1 x Unit GPS v1.1
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 车载定位与导航
- 可穿戴设备
- 物联网定位设备
- 无人机
- 便携式设备
- 公交报站

## 规格参数

| 规格             | 参数                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------ |
| SoC              | ATGM336H-6N 模组 @AT6668                                                                                     |
| 支持卫星导航系统 | GPS/QZSS/BD2/BD3/GAL/GLO<br/>频点:<br/>BDS：B1I+B1C <br/>GPS/QZSS/SBAS：L1 <br/>GALILEO：E1 <br/>GLONASS：R1 |
| 通道             | 50 通道                                                                                                      |
| 通讯             | 串口 (UART) 通讯，默认 115200bps@8N1                                                                         |
| 定位精度         | <1.5m (CEP50)                                                                                                |
| 定位更新率       | 最大 10Hz                                                                                                    |
| 协议             | NMEA0183 4.1                                                                                                 |
| 灵敏度           | 跟踪: -162dBm，捕捉: -160dBm，冷启动: -148dBm                                                                |
| 启动时间         | 冷启动: 23 seconds，热启动: 1 second                                                                         |
| 功耗             | DC 5V/31.64mA                                                                                                |
| 产品尺寸         | 48.0 x 24.0 x 8.0mm                                                                                          |
| 产品重量         | 12.3g                                                                                                        |
| 包装尺寸         | 138.0 x 93.0 x 9.0mm                                                                                         |
| 毛重             | 17.6g                                                                                                        |

## 原理图

- [Unit GPS v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/849/U032-V11-UNIT_GPS_SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/849/U032-V11-UNIT_GPS_SCHE_page_01.png">
</SchViewer>

## 管脚映射

### Unit GPS v1.1

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/module_size.jpg" width="100%" />

## 数据手册

- [ATGM336H-6N](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/ATGM336H-6N.pdf)
- [MAX2659](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/MAX2659_en.pdf)
- [CASIC 多模卫星导航接收机协议规范](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/CASIC_Multi-mode_Satellite_Navigation_Receiver_Protocol_Specification.pdf)

## 软件开发

### Arduino

- [Unit-GPS v1.1 Arduino 驱动库](https://github.com/m5stack/TinyGPSPlus)

### UiFlow2

- [Unit GPS v1.1 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/gps_v11.html)

## 相关视频

- Unit GPS v1.1 产品示例介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/unit%20gps%20v1.1%20video.mp4" type="video/mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113546755114304&bvid=BV1UozMY5EhJ&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <iframe width="560" height="315" src="https://www.youtube.com/embed/Ht9ZVqukhrg?si=VdEtylNINcTWUu_5" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </template>
</TabPanel>

## 产品对比

::compare-table
| Product Compare | [Unit-GPS v1.1](/zh_CN/unit/Unit-GPS%20v1.1) ![Unit-GPS v1.1](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/8.webp) | [Unit-GPS](/zh_CN/unit/gps) ![Unit-GPS](https://static-cdn.m5stack.com/resource/docs/products/unit/gps/gps_02.webp) |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| SoC             | AT6668                                                                                                                                                         | AT6558                                                                                                              |
| 支持卫星        | BD2/BD3/GPS/GLONASS/GALILEO/QZSS                                                                                                                               | BDS/GPS                                                                                                             |
| 定位精度        | 1.5m                                                                                                                                                           | 2.5m                                                                                                                |
| 通道            | 50 通道 (CEP50)                                                                                                                                                | 32 通道 (CEP50)                                                                                                     |
| 灵敏度          | 跟踪: -162dBm，捕捉: -160dBm，冷启动: -148dBm                                                                                                                  | 跟踪: -162dBm，捕捉: -148dBm，冷启动: -146dBm                                                                       |
| 冷启动          | 冷启动: 23 seconds，热启动: 1 second                                                                                                                           | 冷启动: 35 seconds，热启动: 1 second                                                                                |
::
