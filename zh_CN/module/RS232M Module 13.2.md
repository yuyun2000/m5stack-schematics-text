# Module13.2 RS232M

<span class="product-sku">SKU:M131</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RS232M Module 13.2/img-6071f525-97b7-4acc-a283-d66a7a5b53cd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RS232M Module 13.2/img-e977533e-4ef7-44e6-9e9c-da11c00a5dc6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RS232M Module 13.2/img-706215e9-dac0-4aa8-83e5-68a4bcae4868.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RS232M Module 13.2/img-c5eb0664-004f-44d3-9da0-e84a672a27b9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RS232M Module 13.2/img-c60f0186-526b-4182-96ec-034f94146448.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RS232M Module 13.2/img-8920b008-a78e-4627-86b9-dc0218ced79b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RS232M Module 13.2/img-f4048b93-1b81-4da4-b6d1-209979cfc8d2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RS232M Module 13.2/img-76b36f1e-f718-4acd-8ec4-efdde9c7d499.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/RS232M Module 13.2/img-f432e069-6a2d-4f26-baaa-6ab82df55e4a.webp">
</PictureViewer>

## 描述

**Module13.2 RS232M** 是一款 **带隔离的 RS232 串行通信** 的扩展模块，采用 **TD301D232H 串口转换芯片 + 公头 DB9 接口** 的方案实现 RS232 和 TTL/CMOS 逻辑电平信号之间的接口转换，并用 **F0505S - 2WR3** DC/DC 电源模块实现电气和噪声的隔离功能， **拨动开关** 以及**编码开关**可实现 DB9 信号线的直通或交叉的切换和串行接口的切换，满足不同连接需求。模块内置 **DC 电源输入插座** 和相应的 **DC-DC 电路** ，可为整个设备提供电源。该产品适用于工业自动化、仪器仪表、医疗设备和通信设备等领域。

## 产品特性

- TD301D232H 串口芯片，支持全双工，快速可靠
- F0505S-2WR3 电气与噪声隔离
- 拨动开关和编码开关切换线序和 GPIO
- 编程平台：Arduino、UiFlow

## 包装内容

- 1 × Module13.2 RS232M
- 1 x HT3.96-4P 端子

## 应用场景

- 工业自动化
- 仪器仪表
- 医疗设备
- 通信设备

## 规格参数

| 规格                | 参数                                                                            |
| ------------------- | ------------------------------------------------------------------------------- |
| RS232               | TD301D232H                                                                      |
| DC-DC 隔离          | F0505S-2WR3                                                                     |
| 通讯速率            | 高达 115200bps                                                                  |
| 通讯方式            | DB9 公头接口，支持全双工通信，支持 RS232 和 TTL/CMOS 逻辑电平信号之间的接口转换 |
| 工作温度            | 0-40°                                                                           |
| DC 电源接口输入电压 | 9-24V                                                                           |
| 产品尺寸            | 63.0 x 54.0 x 19.7mm                                                            |
| 产品重量            | 31.4g                                                                           |
| 包装尺寸            | 95.0 x 66.0 x 26.0mm                                                            |
| 毛重                | 54.2g                                                                           |

## 原理图

- [Module13.2 RS232M 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/558/Sch_Module_13.2_RS232M_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/558/Sch_Module_13.2_RS232M_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN       | LEFT | RIGHT | PIN       |
| --------- | ---- | ----- | --------- |
| GND       | 1    | 2     | RS232_TX  |
| GND       | 3    | 4     |           |
| GND       | 5    | 6     |           |
|           | 7    | 8     |           |
|           | 9    | 10    |           |
|           | 11   | 12    |           |
| RS232_TX  | 13   | 14    | RS232_RX  |
| RS232_TX  | 15   | 16    | RS232_RX  |
|           | 17   | 18    |           |
|           | 19   | 20    |           |
| RS232_RX  | 21   | 22    | RS232_TX  |
| RS232_RX  | 23   | 24    | RS232_RX  |
| HPWR      | 25   | 26    | RS232_TX  |
| HPWR      | 27   | 28    | 5V        |
| HPWR      | 29   | 30    |           |
::

## 尺寸图

- [Module13.2 RS232M 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/987/M130-M131-232moudle.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/987/M130-M131-232moudle_page_01.png" width="100%">

## 数据手册

- [F0505S-2WR3](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M130%20RS232%20Module%2013.2/F0505S-2WR3.pdf)
- [TD301D232H](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/M130%20RS232%20Module%2013.2/TD301D232H.PDF)

## 软件开发

### Arduino

- [Module13.2 RS232M Example with M5Core](https://github.com/m5stack/M5Stack/blob/master/examples/Modules/RS232/RS232.ino)

### UiFlow1

- [Module13.2 RS232M UiFlow1 文档](/zh_CN/uiflow/blockly/module/rs232)

### UiFlow2

- [Module13.2 RS232M UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/rs232.html)

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114097802775678&bvid=BV1ix9iYgEZu&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/jljrzLPykEg?si=1X_7vZVKenevAVYX" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
