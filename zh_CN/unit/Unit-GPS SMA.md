# Unit GPS SMA

<span class="product-sku">SKU:U190</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20SMA/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20SMA/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20SMA/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20SMA/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20SMA/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20SMA/10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/850/U190-weight.jpg">
</PictureViewer>

## 描述

**Unit GPS SMA** 是一款 GNSS 全球定位导航单元，集成了高性能中科微导航模组 ATGM336H，采用 AT6668 芯片方案，搭配有源外置天线，提供更加精确和可靠的卫星定位服务。相比之前的产品，AT6668 支持多频多模 GNSS 信号接收，可接收多个卫星导航系统 (包括 GPS、BD2、BD3、GLONASS、GALILEO 和 QZSS 等) 的信号，支持多系统联合定位和单系统独立定位，具备更强的抗干扰能力和更高的定位精度。在信号较弱的区域，能快速获取更高精度的位置信息。此模块适用于车载定位与导航、物联网定位设备等高精度定位的应用场景。

## 产品特性

- 支持多种卫星导航系统 (GPS/QZSS/BD2/BD3/GAL/GLO)
- 多频点多系统接收
- 多通道
- 外置有源天线
- 2 x LEGO 兼容孔
- 编程平台：Arduino，UiFlow，ESP-IDF 等

## 包装内容

- 1 x Unit GPS SMA
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 有源外置天线

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
| SoC              | AT6668                                                                                                       |
| 支持卫星导航系统 | GPS/QZSS/BD2/BD3/GAL/GLO<br/>频点:<br/>BDS：B1I+B1C <br/>GPS/QZSS/SBAS：L1 <br/>GALILEO：E1 <br/>GLONASS：R1 |
| 通道             | 50 通道                                                                                                      |
| 通讯             | 串口 (UART) 通讯，默认 115200bps@8N1                                                                         |
| 定位精度         | <1.5m (CEP50)                                                                                                |
| 定位更新率       | 最大 10Hz                                                                                                    |
| 协议             | NMEA0183 4.1                                                                                                 |
| 灵敏度           | 跟踪: -162dBm，捕捉: -160dBm，冷启动: -148dBm                                                                |
| 启动时间         | 冷启动: 23 seconds，热启动: 1 second                                                                         |
| 天线             | SMA 有源外置天线 (内螺内针)，增益：30DBI 频段：1555MHz~1580MHz 长度：1m 尺寸：38 x 36 x 13mm                 |
| 功耗             | 待机功耗：DC 5V/31.64mA <br/> 工作功耗：DC 5V/40.90mA                                                        |
| 产品尺寸         | 71.4 x 24.0 x 8.0mm                                                                                          |
| 产品重量         | 11.4g                                                                                                        |
| 包装尺寸         | 170.0 x 120.0 x 9.0mm                                                                                        |
| 毛重             | 55.1g                                                                                                        |

## 原理图

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20SMA/schematic.png" width="100%" />

## 管脚映射

### Unit GPS SMA

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20SMA/MODULE_SIZE.jpg" width="100%" />

## 数据手册

- [ATGM336H-6N](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/ATGM336H-6N.pdf)
- [MAX2659](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/MAX2659_en.pdf)
- [CASIC 多模卫星导航接收机协议规范](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/CASIC_Multi-mode_Satellite_Navigation_Receiver_Protocol_Specification.pdf)

## 软件开发

### Arduino

- [Unit GPS v1.1 Arduino 驱动库](https://github.com/m5stack/TinyGPSPlus)

## 相关视频

- Unit GPS SMA 产品示例介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20SMA/Unit_GPS_SMA_Video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113546755048134&bvid=BV1bozMY5Ep7&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <iframe width="560" height="315" src="https://www.youtube.com/embed/BsrkLs_3S5w?si=9lXgNGy6SyMCInhb" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </template>
</TabPanel>

## 产品对比

::compare-table
| Product Compare                   | [Unit-GPS SMA](/zh_CN/unit/Unit-GPS%20SMA) ![Unit-GPS SMA](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20SMA/8.webp) | [Unit-GPS v1.1](/zh_CN/unit/Unit-GPS%20v1.1) ![Unit-GPS v1.1](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/8.webp) | [Unit-GPS](/zh_CN/unit/gps) ![Unit-GPS](https://static-cdn.m5stack.com/resource/docs/products/unit/gps/gps_02.webp) |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| SoC                               | AT6668                                                                                                                                                     | AT6668                                                                                                                                                         | AT6558                                                                                                              |
| 支持卫星                          | BD2/BD3/GPS/GLONASS/GALILEO/QZSS                                                                                                                           | BD2/BD3/GPS/GLONASS/GALILEO/QZSS                                                                                                                               | BDS/GPS                                                                                                             |
| 定位精度                          | 1.5m                                                                                                                                                       | 1.5m                                                                                                                                                           | 2.5m                                                                                                                |
| 通道                              | 50 通道 (CEP50)                                                                                                                                            | 50 通道 (CEP50)                                                                                                                                                | 32 通道 (CEP50)                                                                                                     |
| 灵敏度                            | 跟踪: -162dBm，捕捉: -160dBm，冷启动: -148dBm                                                                                                              | 跟踪: -162dBm，捕捉: -160dBm，冷启动: -148dBm                                                                                                                  | 跟踪: -162dBm，捕捉: -148dBm，冷启动: -146dBm                                                                       |
| 冷启动                            | 冷启动: 23 seconds，热启动: 1 second                                                                                                                       | 冷启动: 23 seconds，热启动: 1 second                                                                                                                           | 冷启动: 35 seconds，热启动: 1 second                                                                                |
| 天线                              | 外置有源天线                                                                                                                                               | 板载陶瓷天线                                                                                                                                                   | 板载陶瓷天线                                                                                                        |
| 信号强度 (同等条件下测得卫星数量) | 北斗卫星：18                                                                                                                                               | 北斗卫星：8                                                                                                                                                    | 北斗卫星: 5                                                                                                         |
::
