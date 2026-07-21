# Module13.2 PwrCAN

<span class="product-sku">SKU:M139</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module13.2-PwrCAN/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module13.2-PwrCAN/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module13.2-PwrCAN/13.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module13.2-PwrCAN/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module13.2-PwrCAN/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module13.2-PwrCAN/11.webp">
</PictureViewer>

## 描述

**Module13.2 PwrCAN** 是一款专为 PwrCAN 总线而设的多功能模块，PwrCAN 总线集成了带隔离的 CAN 通信和 DC 9 ~ 24V 的供电总线，同时模块内附带了 Pwr485 (带隔离) 总线功能，本模块能为 M5 主机提供隔离的 5V 电源供电。
CAN 通信部分采用 CA - IS3050G 隔离收发器，RS485 部分采用 CA-IS3082W 隔离收发器，其中 CAN 及 RS485 通信关联的 GPIO 均可通过拨位开关进行选择，CAN 及 RS485 出口处均可通过拨位开关选择并联 120 欧姆 终端电阻。
本模块供电总线支持 DC 9 ~ 24V 宽电压输入，其中 DC 插座与 HT3.96 和 XT30 的电源部分直接相连，通过内置隔离电源模块 F0505S-2WR3 向 M5 主机提供供电。
本模块适用于机器人控制、协议转换、工业自动化、车载通信系统、智能交通、楼宇自动化等领域。

## 注意事项

?>注意|XT30 与 HT3.96 接口的电源部分与 DC 输入直接相连，无降压，输出电压 = 输入电压。接入前请核对设备支持的工作电压，防止因过压导致设备损坏。

## 产品特性

- 隔离 CAN 总线 (双通道)
- 隔离 RS485 总线
- 信号隔离
- 电源隔离供电
- 多供电接口
- 宽电压输入范围 (9-24V)
- CAN/RS485 通信引脚切换拨码开关

## 包装内容

- 1 x Module13.2 PwrCAN
- 1 x HT3.96-4P
- 1 x XT30 (2+2) PW-M 线缆

## 应用场景

- 机器人控制
- 协议转换
- 工业自动化
- 车载通信系统
- 智能交通
- 楼宇自动化

## 规格参数

| 规格             | 参数                                                                              |
| ---------------- | --------------------------------------------------------------------------------- |
| 支持协议         | CAN & RS485 总线通信协议                                                          |
| CAN 通信         | CA-IS3050G@双通道                                                                 |
| RS485 通信       | CA-IS3082W@单通道                                                                 |
| CAN 接口         | XT30 (2+2) PW-M 卧式焊板公头                                                      |
| RS485 接口       | HT3.96-4P                                                                         |
| CAN 总线速率     | 最大 1Mbps                                                                        |
| RS485 总线速率   | 最大 500Kbps                                                                      |
| CAN 支持节点数   | 110 个                                                                            |
| RS485 支持节点数 | 256 个                                                                            |
| 电压输入范围     | 9-24V                                                                             |
| 电源供电方式     | DC 电源座子 (5.5/2.1mm，内正外负极)、485 接口 (HT3.96) 供电、CAN 接口 (XT30) 供电 |
| 工作温度         | 0-40°C                                                                            |
| 产品尺寸         | 54.0 x 54.0 x 19.7mm                                                              |
| 产品重量         | 27.8g                                                                             |
| 包装尺寸         | 132.0 x 95.0 x 21.0mm                                                             |
| 毛重             | 51.2g                                                                             |

### RS485 通讯测试

| 通讯距离 | 数据速率                                                 |
| -------- | -------------------------------------------------------- |
| 30 米    | 最大数据速率 512Kbps，接收发送正常，丢包率 0%，错误率 0% |
| 50 米    | 最大数据速率 512Kbps，接收发送正常，丢包率 0%，错误率 0% |
| 100 米   | 最大数据速率 512Kbps，接收发送正常，丢包率 0%，错误率 0% |

### CAN 通讯测试

| 通讯距离 | 数据速率                                              |
| -------- | ----------------------------------------------------- |
| 10 米    | 数据速率 1000Kbps，接收发送正常，丢包率 0%，错误率 0% |
| 30 米    | 数据速率 500Kbps，接收发送正常，丢包率 0%，错误率 0%  |
| 50 米    | 数据速率 500Kbps，接收发送正常，丢包率 0%，错误率 0%  |
| 100 米   | 数据速率 250Kbps，接收发送正常，丢包率 0%，错误率 0%  |

### 带载能力测试

| 参数类别     | 规格参数                                                                     |
| ------------ | ---------------------------------------------------------------------------- |
| 输出带载能力 | 隔离后输出最大电流：DC: 4.70V@218mA <br/> 隔离前输出最大电流：DC: 4.70V@1.1A |

### 功耗测试

| 参数类别          | 规格参数                                             |
| ----------------- | ---------------------------------------------------- |
| 待机电流          | DC 9V@30.94mA <br/> DC 12V@23.57mA <br/> DC 24V@10mA |
| 工作电流 (带主机) | DC 9V@78.60mA <br/> DC 12V@65.54mA <br/> DC 24V@31mA |

## 原理图

- [Module13.2 PwrCAN 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/565/SCH_Module_PwrCan_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/565/SCH_Module_PwrCan_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

\#> DIP Switch | 下方 M5-Bus 中标记 `SW` 的引脚，可通过拨码开关进行切换，用于适配不同的主控设备。

::m5-bus-table
| PIN                | LEFT | RIGHT | PIN                |
| ------------------ | ---- | ----- | ------------------ |
| GND                | 1    | 2     | CAN_RX/485_RX (SW) |
| GND                | 3    | 4     |                    |
| GND                | 5    | 6     |                    |
|                    | 7    | 8     |                    |
|                    | 9    | 10    |                    |
|                    | 11   | 12    | 3V3                |
|                    | 13   | 14    |                    |
| CAN_RX/485_RX (SW) | 15   | 16    | CAN_TX/485_TX (SW) |
|                    | 17   | 18    |                    |
|                    | 19   | 20    |                    |
| CAN_TX/485_TX (SW) | 21   | 22    | CAN_RX/485_RX (SW) |
| CAN_TX/485_TX (SW) | 23   | 24    | CAN_TX/485_TX (SW) |
|                    | 25   | 26    | CAN_RX/485_RX (SW) |
|                    | 27   | 28    | 5V                 |
|                    | 29   | 30    | BAT                |
::

?> 注意 | 板载的拨码开关可用于更改 CAN/R485 总线所使用的 I/O，切换至 ON 侧表示线路连接。<br>使用拨码开关切换 I/O 时请注意， CAN 总线与 RS485 总线的所使用的 I/O 引脚不能重复，否则将会引起冲突，导致通信异常。

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module13.2-PwrCAN/38c324f157b3ec044fbe91acfb0571b.png" width="30%" />

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/module/Module13.2-PwrCAN/img-66ce1d4e-78ae-497f-bd11-ed33e4d5fdcb.jpg" width="100%" />

## 数据手册

- [CA-IS3050G(CAN)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module13.2-PwrCAN/CA-IS3050G.PDF)
- [CA-IS3082W(RS485)](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module13.2-PwrCAN/CA-IS3082W.PDF)

## 软件开发

### Arduino

- [Module13.2 PwrCAN Transceiver Test](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/CAN)
- [Module13.2 PwrCAN RS485 Example](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/ISO485)
- [Module13.2 PwrCAN 控制小米电机案例](https://github.com/project-sternbergia/cybergear_m5)

### UiFlow2

- [Module13.2 PwrCAN UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/pwrcan.html)

## 相关视频

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/Module13.2-PwrCAN/pwrcan%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115602349885276&bvid=BV1hoUGBkE3f&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/ChFfdFWFIvs?si=EayvAfS4_Yp4Vim9" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
