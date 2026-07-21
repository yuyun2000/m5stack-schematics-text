# Unit ACSSR

<span class="product-sku">SKU:U139</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/acssr/acssr_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/acssr/acssr_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/acssr/acssr_09.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/acssr/acssr_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/acssr/acssr_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/acssr/acssr_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/acssr/acssr_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/acssr/acssr_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/acssr/acssr_08.webp">
</PictureViewer>

## 描述

**Unit ACSSR** 是一款单相交流固态继电器控制套件，内含单相固态继电器与 ESP32C3 核心控制板。支持 **按键控制、I2C 从机、Modbus 组网** 三种工作模式，并集成可编程全彩 RGB LED，用于多种状态指示。相比传统机械继电器，固态继电器采用半导体器件构成，无触点设计，具备 **开关速度快、频率高、寿命长、噪声低、动作可靠、无电弧火花** 等优势。该产品适用于工业自动化、电机控制、温控系统等应用场景。

## 教程 & 快速上手

learn>| ![Arduino IDE](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/arduino/arduino_banner_01.png) | [Arduino IDE](/zh_CN/arduino/projects/unit/unit_acssr) | 本教程将向你介绍，如何通过 Arduino IDE 编程控制 Unit ACSSR 设备。 |

## 产品特性

- 单相固态继电器
- 支持通断负载线路电压: AC 24 ~ 480V
- 三种工作模式：
  - 按键控制
  - I2C 模式 (支持配置 I2C 地址)
  - Modbus 模式 (支持配置设备 ID)
- 可编程全彩 RGB LED
- RS485PWR 控制接口
  - 用于 Modbus 控制
  - 支持 DC 9 ~ 24V 供电输入
  - 通信速率配置: 115200bps 8N1
  - 默认 ID: 0x0004
- HY2.0-4P Grove 控制接口
  - 用于 I2C 通信控制
  - 支持 DC 5V 供电输入
  - 3.3V 逻辑电平通信

## 包装内容

- 1 x Unit ACSSR
- 1 x 单相固态继电器
- 2 x 3.96-4P 接线端子
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 通信协议说明书

## 应用场景

- 交流线路通断
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
| 负载电压         | AC 24 ~ 480V                       |
| 输入控制电流     | 5 ~ 20mA                           |
| 断态漏电流       | ≤5mA                               |
| 通态降压         | ≤1.6V                              |
| 工作电流安全系列 | 阻性负载：50% 感性负载：50%        |
| 电寿命           | ≥100 万次                          |
| 指示灯           | 红色 (点亮：闭合状态 / 熄灭：断开) |
| 产品重量         | 112.6g                             |
| 毛重             | 137.8g                             |
| 产品尺寸         | 80 x 45 x 31mm                     |
| 包装尺寸         | 147 x 90 x 40mm                    |

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

## 原理图

- [Unit ACSSR 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/598/Sch_UNIT_ACSSR.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/598/Sch_UNIT_ACSSR_sch_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/598/Sch_UNIT_ACSSR_sch_02.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/598/Sch_UNIT_ACSSR_sch_03.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/598/Sch_UNIT_ACSSR_sch_04.png">
</SchViewer>

## 管脚映射

### Unit ACSSR

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### ESP32-C3

| ESP32-C3   | G0  | G1  | G2      | G3  | G4        | G5       | G6       |
| ---------- | --- | --- | ------- | --- | --------- | -------- | -------- |
| Unit ACSSR | SCL | SDA | RGB LED | BTN | RELAY CTL | RS485-TX | RS485-RX |

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/786/U139_Model_Size.png" width="100%">

## 软件开发

### Arduino

- [Unit ACSSR Arduino 使用教程](/zh_CN/arduino/projects/unit/unit_acssr)
- [Unit ACSSR Arduino 驱动库](https://github.com/m5stack/M5Unit-ACSSR)
- [ArduinoModbus 驱动库](https://github.com/m5stack/ArduinoModbus)
- [Arduino485 驱动库](https://github.com/m5stack/ArduinoRS485)
- [Unit ACSSR I2C Relay Control Example](https://github.com/m5stack/M5Unit-ACSSR/tree/main/examples/ACSSR_I2C/I2C_RELAY_CTL)
- [Unit ACSSR I2C Addr Config Example](https://github.com/m5stack/M5Unit-ACSSR/tree/main/examples/ACSSR_I2C/I2C_ADDR_CONFIG)
- [Unit ACSSR Modbus Relay Control Example](https://github.com/m5stack/M5Unit-ACSSR/tree/main/examples/ACSSR_MODBUS/MODBUS_RELAY_CTL)
- [Unit ACSSR Modbus Slave ID Config Example](https://github.com/m5stack/M5Unit-ACSSR/tree/main/examples/ACSSR_MODBUS/SLAVE_ID_CONFIG)

### UiFlow1

- [Unit ACSSR UiFlow1 文档](/zh_CN/uiflow/blockly/unit/acssr)

### UiFlow2

- [Unit ACSSR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/acssr.html)

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113342760878900&bvid=BV117yqYwEuH&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" autoplay="0" ></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/zkQ43Tn500I?si=rEWawqz9v3bYZvc6" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
