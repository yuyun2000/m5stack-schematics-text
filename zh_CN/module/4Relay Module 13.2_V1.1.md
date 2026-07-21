# Module13.2 4Relay v1.1

<span class="product-sku">SKU:M121-V11</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4Relay Module 13.2_V1.1/img-dff44f86-211d-47b2-ba41-78dd61850cd3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4Relay Module 13.2_V1.1/img-e438015d-9ad4-4ec6-bedd-d9fa0a26562c.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/973/M121-V11-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4Relay Module 13.2_V1.1/img-d95d9183-cec8-4e2c-97e2-af5bf12e1c4a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4Relay Module 13.2_V1.1/img-3e51c927-c042-48c8-bb8d-3ee3204a288b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4Relay Module 13.2_V1.1/img-96b4fcde-f942-4381-8a24-acdb5259d71a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4Relay Module 13.2_V1.1/img-4bae1d8a-043c-4d23-8449-e6deea317d64.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4Relay Module 13.2_V1.1/img-8ac3687c-b3fc-43cd-b04d-c15c6e3d1a1b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4Relay Module 13.2_V1.1/img-2cfd356b-fff5-4028-a566-231b76eb910d.webp">
</PictureViewer>

## 描述

**Module13.2 4Relay v1.1** 是一款继电器模块，板载 4 路机械式继电器控制通道 (NO, COM) 。模块采用 I2C 通信协议控制，有效节省 IO 资源。跳线帽设计可用于切换继电器有源 / 无源工作模式，满足不同的电路需求。该继电器模块仅支持直流线路通断，4 通道最大负载能力为 24W (DC 24V @ 1A) ，内置外部电源电压检测以及 DC-DC 电路给主机供电。适用于小型负载线路的通断控制。

## 产品特性

- STM32G030F6
- I2C 通讯 (addr: 0x26)
- 4 路继电器控制，最大负载能力 24W (DC 24V@1A)
- 支持两种工作模式 (有源和无源)
- 电压检测
- 支持 Arduino、UiFlow 等编程平台

## 包装内容

- 1 x Module13.2 4Relay v1.1
- 5 x KF2EDGK-2.54-2P 接线端子（绿色）
- 10 x 跳线帽
- 1 x 接线说明书

## 应用场景

- 电磁阀控制
- 直流线路通断

## 规格参数

| 规格               | 参数                                     |
| ------------------ | ---------------------------------------- |
| MCU                | STM32F030F4P6                            |
| 通信接口           | I2C 通信 @ 0x26                          |
| 支持工作模式       | 有源控制 / 无源控制                      |
| 继电器通道数       | 4x (COM, NO 接口)                        |
| 电源输入接口       | DC5521 母头 5.5 x 2.1mm@5-24V (内正外负) |
| 负载能力           | 4 通道最大负载能力 24W (DC 24V@1A)       |
| 继电器接线端子规格 | KF2EDGR-2.54-2P                          |
| 单路继电器功耗     | 5V@40mA                                  |
| 线圈动作时间       | 6ms                                      |
| 线圈释放时间       | 4ms                                      |
| 产品尺寸           | 54.0 x 54.0 x 19.7mm                     |
| 产品重量           | 38.0g                                    |
| 包装尺寸           | 134.0 x 95.0 x 20.0mm                    |
| 毛重               | 58.1g                                    |

## 数据手册

- [继电器规格书](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/4relay/Datasheet-Realy-HK4100F-DC5V-SHG(1).pdf>)

## 原理图

- [Module13.2 4Relay v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/548/Sch_4Relay_13.2_Module_V1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/548/Sch_4Relay_13.2_Module_V1.1_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN  | LEFT | RIGHT | PIN |
| ---- | ---- | ----- | --- |
| GND  | 1    | 2     |     |
| GND  | 3    | 4     |     |
| GND  | 5    | 6     |     |
|      | 7    | 8     |     |
|      | 9    | 10    |     |
|      | 11   | 12    | 3V3 |
|      | 13   | 14    |     |
|      | 15   | 16    |     |
| SDA  | 17   | 18    | SCL |
|      | 19   | 20    |     |
|      | 21   | 22    |     |
|      | 23   | 24    |     |
| HPWR | 25   | 26    |     |
| HPWR | 27   | 28    | 5V  |
| HPWR | 29   | 30    |     |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/module/4Relay Module 13.2_V1.1/img-d370e126-9eef-432f-a08b-de8ae6a6222a.jpg" width="100%" />

## 软件开发

### Arduino

- [Module13.2 4Relay v1.1 Arduino 驱动库](https://github.com/m5stack/M5Module-4Relay)
- [Module13.2 4Relay v1.1 Example with M5Core](https://github.com/m5stack/M5Module-4Relay/blob/main/examples/Module_4RELAY_M5Core/Module_4RELAY_M5Core.ino)
- [Module13.2 4Relay v1.1 Example with M5Core2](https://github.com/m5stack/M5Module-4Relay/blob/main/examples/Module_4RELAY_M5Core2/Module_4RELAY_M5Core2.ino)

### 内置固件

- [Module13.2 4Relay v1.1 内置固件](https://github.com/m5stack/M5Module-4Relay-V1.1-Internal-FW)

### 通信协议

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/4Relay%20Module%2013.2_V1.1/47a504d92f6932dd0206cf2cdb6a350.png"  width="100%" />

<!--
## 产品对比

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/2relay/对比.png" width="100%"/>

-->

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113580561204429&bvid=BV1Nw6PY8EkS&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/ayLKLAJKVLs?si=3S_DiUgFIG8Sw-7o" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
