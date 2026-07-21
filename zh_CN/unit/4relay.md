# Unit 4Relay

<span class="product-sku">SKU:U097</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/4relay/4relay_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/4relay/4relay_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/4relay/4relay_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/4relay/4relay_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/4relay/4relay_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/4relay/4relay_06.webp">
</PictureViewer>

## 描述

Unit 4Relay 是一款集成 4 路继电器控制的高压驱动单元。它基于 STM32F030F4P6 微控制器，通过 I2C 总线实现对 4 路机械继电器的独立控制，支持 AC 250V / DC 28V 高压切换。该单元通过 Grove HY2.0-4P 接口通信，具备物理隔离、可编程状态指示灯和过载能力，并采用 LEGO 兼容孔设计，便于灵活对接 LEGO 结构或使用螺丝固定。适用于智能家居、工业控制及大功率设备电源管理等高压负载切换场景。

## 产品特性

- 通道数量：4 路继电器独立控制
- 负载能力：AC 250V@10A 或 DC 28V@10A
- 状态指示：每路独立可编程 LED 指示灯
- 隔离特性：高低压侧物理隔离
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit 4Relay
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 4 x HT3.96-4P 端子

## 应用场景

- 直流信号切换
- 数字设备电源通断

## 规格参数

| 规格         | 参数                   |
| ------------ | ---------------------- |
| MCU          | STM32F030F4P6          |
| 最大输入电压 | AC 250V / DC 28V       |
| 额定电流     | 10A                    |
| 最大瞬时电流 | 16A                    |
| 通信接口     | I2C 通信 @ 0x26        |
| 产品尺寸     | 112.0 x 23.0 x 18.0mm  |
| 产品重量     | 40.0g                  |
| 包装尺寸     | 163.0 x 100.0 x 20.0mm |
| 毛重         | 84.0g                  |

## 原理图

- [Unit 4Relay 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/589/Sch_UNIT-4RELAY.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/589/Sch_UNIT-4RELAY_sch_01.png">
</SchViewer>

## 管脚映射

### Unit 4Relay

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/4relay/model%20size.png" width="100%">

## 结构文件

- [Unit 4Relay 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U097_Unit_4Relay/Structures)

## 软件开发

### Arduino

- [Unit 4Relay Example with M5Atom](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_4RELAY_M5Atom/Unit_4RELAY_M5Atom.ino)
- [Unit 4Relay Example with M5Core](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_4RELAY_M5Core/Unit_4RELAY_M5Core.ino)
- [Unit 4Relay Example with M5Core2](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_4RELAY_M5Core2/Unit_4RELAY_M5Core2.ino)
- [Unit 4Relay Example with M5StickC](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_4RELAY_M5StickC/Unit_4RELAY_M5StickC.ino)
- [Unit 4Relay Example with M5StickC-Plus](https://github.com/m5stack/M5Unit-RELAY/blob/master/examples/Unit_4RELAY_M5StickCPlus/Unit_4RELAY_M5StickCPlus.ino)

### UiFlow1

- [Unit 4Relay UiFlow1 文档](/zh_CN/uiflow/blockly/unit/4relay)

### UiFlow2

- [Unit 4Relay UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/relay4.html)

### Home Assistant

- [Unit 4Relay Home Assistant 集成](/zh_CN/homeassistant/switch/unit_4relay)

### 通讯协议

- 协议类型: I2C
- I2C Address: 0x26

#### Mode control Reg 0x10

| Bit | Desc                          | R/W |
| --- | ----------------------------- | --- |
| 7   | R                             | R/W |
| 6   | R                             | R/W |
| 5   | R                             | R/W |
| 4   | R                             | R/W |
| 3   | R                             | R/W |
| 2   | R                             | R/W |
| 1   | R                             | R/W |
| 0   | LED Sync Mode 0:Manual 1:Auto | R/W |

\#> 工作模式说明 | Manual:LED 灯支持独立控制<br/>Auto:LED 跟随 Relay 状态变化，Relay ON 则点亮，OFF 则熄灭。

#### RELAY control Reg 0x11

| Bit | Desc                 | R/W |
| --- | -------------------- | --- |
| 7   | LED1 / 1: ON 0:OFF   | R/W |
| 6   | LED2 / 1: ON 0:OFF   | R/W |
| 5   | LED3 / 1: ON 0:OFF   | R/W |
| 4   | LED4 / 1: ON 0:OFF   | R/W |
| 3   | RELAY1 / 1: ON 0:OFF | R/W |
| 2   | RELAY2 / 1: ON 0:OFF | R/W |
| 1   | RELAY3 / 1: ON 0:OFF | R/W |
| 0   | RELAY4 / 1: ON 0:OFF | R/W |

### EasyLoader

| Easyloader                      | 下载链接                                                                                                                  | 备注                                                             |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Unit 4Relay Example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_4_Relay_Unit.exe) | A 键切换继电器序号，B 键切换 LED 同步 / 异步，C 键控制所有继电器 |

## 相关视频

- Unit 4Relay Test with M5Core

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/4-RELAY_UNIT.mp4" type="video/mp4"></video>

- UiFlow2 Unit 4Relay

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113066473686215&bvid=BV1KCHre3EEs&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/Y-wzaE-_U7I?si=Dc9Z2q29sFq7tMHt" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
