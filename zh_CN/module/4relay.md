# Module13.2 4Relay

<span class="product-sku">SKU:M121</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4relay/4relay_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4relay/4relay_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4relay/4relay_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4relay/4relay_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4relay/4relay_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4relay/4relay_06.webp">
</PictureViewer>

## 描述

**Module13.2 4Relay** 是一款适配 M5Core/Core2 型主控的继电器模块，板载**4 路机械式继电器**控制通道 (NO, COM)。模块采用**I2C 通信**协议控制，有效节省 IO 资源。跳线帽设计可用于切换继电器**有源 / 无源工作模式**，满足不同的电路需求。该继电器模块仅支持**直流线路通断**，4 通道最大负载能力为**24W(DC 24V@1A)**，适用于小型负载线路的通断控制。

## 产品特性

- 内嵌 STM32F030F4 主控方案:
  - I2C 通信接口 (addr: 0x26)
- 继电器:
  - 4 x 继电器控制 (COM, NO 接口)
  - 最大负载能力 24W (DC 24V@1A)
- 支持两种工作模式 (通过跳线帽控制模式)：
  - 有源控制：
    - 电源输入连接继电器 NO 接口，直接供电负载。
  - 无源控制：
    - 电源输入不连接继电器接口，用户线路需包含电源。
- 电源输入 (仅支持直流输入)：
  - DC 5-24V INPUT -> M5 BUS HPWR 总线 (通过跳线帽控制是否接入，当堆叠多个不同 M5 模块时，HPWR 总线可为其他需要 24V 供电的模块供电，如 SERVO2 模块等)
- 开发方式：
  - 开发平台: UiFlow，Arduino

## 包装内容

- 1 x 4Relay Module
- 5 x 接线端子 2.54mm-2P (绿色)
- 10 x 跳线帽
- 1 x 接线说明书

## 应用场景

- 电磁阀控制
- 直流线路通断

## 规格参数

| 规格               | 参数                                     |
| ------------------ | ---------------------------------------- |
| 通信接口           | I2C 通信 @ 0x26                          |
| 支持工作模式       | 有源控制 / 无源控制                      |
| 继电器通道数       | 4x (COM, NO 接口)                        |
| 电源输入接口       | DC5521 母头 5.5 x 2.1mm@5-24V (内正外负) |
| 负载能力           | 4 通道最大负载能力 24W (DC 24V@1A)       |
| 继电器接线端子规格 | 2.54-2P                                  |
| 单路继电器功耗     | 5V@40mA                                  |
| 线圈动作时间       | 6ms                                      |
| 线圈释放时间       | 4ms                                      |
| 产品重量           | 37.2g                                    |
| 毛重               | 37.6g                                    |
| 产品尺寸           | 54.2 x 54.2 x 13.2mm                     |
| 包装尺寸           | 95 x 65 x 25mm                           |

## 操作说明

跳线帽使用说明

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4relay/4relay_07.webp" width="30%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4relay/4relay_08.webp" width="35%">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4relay/4relay_09.webp" width="35%">

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/4relay/4relay_sch_01.webp" width="100%">

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

## 数据手册

- [继电器规格书](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/4relay/Datasheet-Realy-HK4100F-DC5V-SHG(1).pdf>)

## 软件开发

### Arduino

- [Module13.2 4Relay Arduino 驱动库](https://github.com/m5stack/M5Module-4Relay)
- [Module13.2 4Relay with M5Core](https://github.com/m5stack/M5Module-4Relay/blob/main/examples/Module_4RELAY_M5Core/Module_4RELAY_M5Core.ino)
- [Module13.2 4Relay with M5Core2](https://github.com/m5stack/M5Module-4Relay/blob/main/examples/Module_4RELAY_M5Core2/Module_4RELAY_M5Core2.ino)

### UiFlow1

- [Module13.2 4Relay UiFlow1 文档](/zh_CN/uiflow/blockly/module/4relay)

### 内置固件

- [Module13.2 4Relay 内置固件](https://github.com/m5stack/M5Module-4Relay-Internal-FW)

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
