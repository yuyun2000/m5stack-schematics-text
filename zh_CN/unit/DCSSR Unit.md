# Unit DCSSR

<span class="product-sku">SKU:U140</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR Unit/img-5e00db88-b5c7-4dd9-9061-b4700dc60c6e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR Unit/img-67321bb8-624a-419c-83f0-d43210d86914.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR Unit/img-384ea9c6-9bd0-4f33-a6ca-08dd90de1bf2.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR Unit/img-95afa67a-03b9-417a-8f4f-69e6016791fe.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR Unit/img-2695703c-0ba4-4b53-8798-09fe0b0fb8a5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR Unit/img-302ddfdb-8315-41a7-b26d-51d5c46aab4a.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR Unit/img-7e125e3f-e1f6-444f-961f-4ab32dfa04d7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR Unit/img-cbc38a33-3ef5-4f3d-a09c-00b1c771d4b9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR Unit/img-24d0cf2a-24c0-4930-8c51-c20df8575e19.webp">
</PictureViewer>

## 描述

**Unit DCSSR** 是一款 **直流控直流** 的 **单相固态继电器** 控制器套件，套装内含单相固态继电器 + ESP32C3 核心控制板。支持 **按键控制**，**I2C 从机**，**Modbus 组网** 三种工作模式。集成的可编程全彩 RGB LED 可用于各种状态的指示。与传统机械式继电器相比，该继电器是采用半导体元件组装固化而成的一种无触点开关。具有开关速度快、工作频率高、使用寿命长、噪声低和动作可靠，无火花等一系列优点。适用于数字程控装置、电机控制装置、调温装置、数据处理系统及计算机终端接口电路，尤其适用于动作频繁、防爆、耐潮和耐蚀的特殊场合。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/projects/unit/unit_acssr) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Unit DCSSR 设备。 |

## 产品特性

- 单相固态继电器
- 三种工作模式:
  - 按键控制
  - I2C 从机 (支持设备 I2C 地址配置)
  - Modbus 组网 (支持设备 ID 配置)
- 可编程全彩 RGB LED
- RS485PWR 接口 (支持 9-24V 设备供电)

## 包装内容

- 1x Unit DCSSR
- 1x 单相固态继电器
- 2 x 3.96-4P 接线端子
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 通信协议说明书

## 应用场景

- 直流线路通断
- 电机设备控制
- 调温设备控制

## 规格参数

| 规格             | 参数                               |
| ---------------- | ---------------------------------- |
| 控制器主控       | ESP32C3                            |
| 通信接口         | I2C 通信 @ 0x50                    |
| 可编程 RGB LED   | SK6812                             |
| 负载电流         | 10A                                |
| 输入控制电压     | DC 3 ~ 32V                         |
| 负载电压         | DC 24 ~ 220V                       |
| 输入控制电流     | 5 ~ 20mA                           |
| 断态漏电流       | ≤5mA                               |
| 通态降压         | ≤1.6V                              |
| 工作电流安全系列 | 阻性负载：50% 感性负载：50%        |
| 电寿命           | ≥100 万次                          |
| 指示灯           | 红色 (点亮：闭合状态 / 熄灭：断开) |
| 产品尺寸         | 45.0 x 30.7 x 11.5mm               |
| 包装尺寸         | 147 x 90 x 40mm                    |
| 产品重量         | 112.6g                             |
| 毛重             | 137.8g                             |

## 操作说明

### 工作模式配置

使用前请参考以下流程配置工作模式:

1. 设备断电状态下，保持长按中间按键。
2. 设备供电，当设备 RGB LED 灯快速闪烁时，表示进入模式配置状态。
3. 单击按键进行模式切换：

- 绿灯：按键手动模式，工作时通过中间按键，控制开关。
- 红灯：I2C 通信模式，工作时通过设备 HY2.0-4P Grove 接口接入 I2C 总线进行控制。
- 黄灯: Modbus 通信模式，工作时通过设备两端 HT3.96-4P 接口接入 Modbus 总线进行控制。

4. 长按按键，选中当前模式进行保存。

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/814/unit_dcssr_mode_change_guide_01.mp4"></video>

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/814/AC-AND-DCSSR-UNIT-note.png" width="70%">

- 负载接线示例图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/acssr/connect_example.png" width="70%">

## 管脚映射

### Unit DCSSR

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR Unit/img-b2a53bb8-4cbb-49bd-9daa-b5ed0f490271.png" width="100%" />

## 软件开发

### Arduino

- [Unit DCSSR Arduino 驱动库](https://github.com/m5stack/M5Unit-ACSSR)
- [Arduino485 Library](https://github.com/m5stack/ArduinoRS485)
- [ArduinoModbus Library](https://github.com/m5stack/ArduinoModbus)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/DCSSR Unit/arduinoCase-1681444659018微信图片_20230414112925.png" width="100%"/>

### UiFlow1

- [Unit DCSSR UiFlow1 文档](/zh_CN/uiflow/blockly/unit/dcssr)

### UiFlow2

- [Unit DCSSR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/dcssr.html)

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113342760878900&bvid=BV117yqYwEuH&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/zkQ43Tn500I?si=rEWawqz9v3bYZvc6" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
