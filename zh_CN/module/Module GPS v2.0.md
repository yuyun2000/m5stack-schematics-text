# Module GPS v2.0

<span class="product-sku">SKU:M003-V2</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/11.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/950/M003-V2-weight.jpg">
</PictureViewer>

## 描述

**Module GPS v2.0** 是一款高性能的 GNSS 全球定位模块，集成高性能 AT6668 芯片，提供精确和可靠的卫星定位服务。该模块支持多频多模 GNSS 信号接收，兼容多个卫星导航系统，包括 GPS、BD2、BD3、GLONASS、GALILEO 和 QZSS 等，能够实现高精度、多系统联合定位或单系统独立定位，并具备优秀的抗干扰能力。在信号较弱的区域，能够快速获取更高精度的位置信息。
该模块默认搭载外置 **SMA 天线**，此外，模块上还预留了**拨码开关**，用户可以灵活切换 TX/RX 通讯引脚，并通过 **PPS** 信号输出进行精准时序设置。模块支持多个**堆叠**使用，提供更多的自定义可能性和灵活性，适用于车载定位与导航、物联网定位设备、远程监控、智能城市、家庭和工业自动化等高精度定位应用场景。

## 产品特性

- 支持多种卫星导航系统 (GPS/QZSS/BD2/BD3/GAL/GLO)
- 多频点多系统接收
- 多通道
- 低功耗
- 精确时序支持
- 模块堆叠支持
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Module GPS v2.0
- 1 x 外置有源 GPS/BD 天线 (长度: 1 m)

## 应用场景

- 车载定位与导航
- 物联网定位设备 (IoT)
- 工业自动化与机器人定位
- 高精度测绘与地理信息系统

## 规格参数

| 规格             | 参数                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------ |
| SoC              | AT6668                                                                                                       |
| 支持卫星导航系统 | GPS/QZSS/BD2/BD3/GAL/GLO<br/>频点:<br/>BDS：B1I+B1C <br/>GPS/QZSS/SBAS：L1 <br/>GALILEO：E1 <br/>GLONASS：R1 |
| 通道             | 50 通道                                                                                                      |
| 定位精度         | <1.5m (CEP50)                                                                                                |
| 定位更新率       | 最大 10Hz                                                                                                    |
| 协议             | NMEA0183 4.1                                                                                                 |
| 通信方式         | UART 115200bps @ 8N1                                                                                         |
| 灵敏度           | 跟踪: -162dBm，捕捉: -160dBm，冷启动: -148dBm，热启动：-156dBm                                               |
| 启动时间         | 冷启动: 23 seconds，热启动: 1 second                                                                         |
| 功耗             | 待机电流：DC 5V/42.78uA 工作电流：DC 5V/41.96mA                                                              |
| 产品尺寸         | 54.0 x 54.0 x 13.1mm                                                                                         |
| 产品重量         | 15.3g                                                                                                        |
| 包装尺寸         | 126.0 x 68.0 x 22.0mm                                                                                        |
| 毛重             | 78.0g                                                                                                        |

## 原理图

- [Module GPS v2.0 原理图 PDF](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/SCH_Module%20GPS%20V2.pdf)

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/schematic.png" width="100%">

## 管脚映射

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/module%20gps%20v2.0%20pinmap%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%954.png" width="80%"> <!--注意这个图中英日三个的链接不同的-->

?> 拨码开关引脚注意事项 | 搭配`Basic`主机使用时，开机时，`G12`引脚作为 Strapping 管脚，开机必须置低，不能拨至 ON 端，否则不能正常开机，待开机正常之后才可和其他引脚正常配置使用，才可拨至 ON 端。`G25`引脚作为 PPS 引脚输出功能，而扬声器的为输入功能，导致功能冲突，只能二选一使用。<br/>搭配`Core2`使用时，`G2`引脚和扬声器引脚复用，只能二选一使用。

### M5-Bus

\#> Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN         | LEFT | RIGHT | PIN             |
| ----------- | ---- | ----- | --------------- |
| GND         | 1    | 2     | GNSS_TX/PPS(SW) |
| GND         | 3    | 4     | PPS(SW)         |
| GND         | 5    | 6     |                 |
|             | 7    | 8     | PPS(SW)         |
|             | 9    | 10    |                 |
|             | 11   | 12    |                 |
|             | 13   | 14    |                 |
| GNSS_TX(SW) | 15   | 16    | GNSS_RX(SW)     |
|             | 17   | 18    |                 |
|             | 19   | 20    |                 |
| GNSS_RX(SW) | 21   | 22    | GNSS_TX(SW)     |
| GNSS_RX(SW) | 23   | 24    | GNSS_RX(SW)     |
| HPWR        | 25   | 26    | GNSS_TX(SW)     |
| HPWR        | 27   | 28    | 5V              |
| HPWR        | 29   | 30    | BAT             |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/model%20size.jpg" width="100%">

## 数据手册

- [ATGM336H-6N](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-GPS%20v1.1/ATGM336H-6N.pdf)
- [VRH3301NLX](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/950/LDO_VRH3301NLX_datasheet.pdf)
- [CASIC 多模卫星导航接收机协议规范](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1173/CASIC_Multi-mode_Satellite_Navigation_Receiver_Protocol_Specification.pdf)

## 软件开发

### 快速上手

- [Module GPS v2.0 Arduino Guide](/zh_CN/arduino/projects/module/module_gps_v2.0)

### Arduino

- [Module GPS v2.0 Arduino 驱动库](https://github.com/m5stack/TinyGPSPlus)

### UiFlow1

coming soon

<!--
- Product Name UiFlow1 文档
-->

### UiFlow2

- [Module GPS v2.0 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/gpsv2.html)

## 相关视频

- Module GPS v2.0 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/M003-V2%20%20GPS%20v2.0%20Module%20video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113858022739553&bvid=BV1Fkw1efEv5&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/bOyBogq4DpU?si=N7AE3IrTnZ6ZGTiC" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

## 产品对比

::compare-table
| 产品对比表       | [Module GPS v2.0](/zh_CN/module/Module%20GPS%20v2.0) ![Module GPS v2.0](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module%20GPS%20v2.0/9.webp)                         | [Module GPS](/zh_CN/module/gps) ![Module GPS](https://static-cdn.m5stack.com/resource/docs/products/module/gps/gps_03.webp) |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| GPS 模组         | AT6668                                                                                                                                                                                                 | NEO-M8N                                                                                                                     |
| 支持卫星         | BD2/BD3/GPS/GLONASS/GALILEO/QZSS                                                                                                                                                                       | GPS, Galileo, GLONASS, BeiDou                                                                                               |
| 定位精度         | 1.5m                                                                                                                                                                                                   | 2.5m                                                                                                                        |
| 灵敏度           | 跟踪: -162dBm，捕捉: -160dBm，冷启动: -148dBm                                                                                                                                                          | 跟踪: -167dBm，捕捉: -160dBm，冷启动: -148dBm                                                                               |
| 拨码开关切换引脚 | 包含拨码开关切换引脚，增加兼容性                                                                                                                                                                       | 固定引脚，不包含拨码开关切换                                                                                                |
::
