# Unit 8Servos

<span class="product-sku">SKU:U165</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Servos Unit/img-353a21be-5d6e-4323-912c-5b9df887b513.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Servos Unit/img-26c85ded-7753-46e5-9e68-5fe9eec7565c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Servos Unit/img-5b0a720e-2518-42d4-84a7-08ab14aed759.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Servos Unit/img-609b7c35-e340-46c3-9eb8-3d2f3e4d3cb7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Servos Unit/img-8ababac7-87dd-4141-bff9-7846e1e4a754.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Servos Unit/img-b6355b6b-fb6b-4e69-80e2-a77ea7396ca9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Servos Unit/img-bec39611-f510-4f83-b347-a4b2734c07fe.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Servos Unit/img-884ad9cd-e07b-4cbd-8f36-eb00b6ae5898.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Servos Unit/img-d8a37910-b392-470e-a43a-48cbb401a9f9.webp">
</PictureViewer>

## 描述

**Unit 8Servos** 是一款 8 通道舵机驱动单元，采用 **STM32F030F4** 主控产生多路 PWM 信号用于舵机驱动，通过 I2C (addr: 0x25) 与 M5 主机进行通信。内置总电源 MOS 管开关电路，支持编程动态控制电机释放 / 锁定；内置总电流采集电路，可获知总电路参数。支持两组电源输入 (9 ~ 24V / 5V)。本产品适用于舵机控制、机器人控制、智能玩具等。

## 产品特性

- 8 通道舵机驱动
- 可编程电机供电控制
- I2C 协议控制 (0x25)
- 电源反接保护
- 总电流采集功能

## 包装内容

- 1 × Unit 8Servos
- 1 × HT3.96-4P
- 1 × HY2.0-4P Grove 线 (20cm)

## 应用场景

- 舵机控制器
- 机器人控制
- 智能玩具

## 规格参数

| 规格               | 参数                         |
| ------------------ | ---------------------------- |
| MCU                | STM32F030F4P6                |
| 电流采集芯片       | INA199A1DCKR                 |
| 驱动器舵机驱动通道 | 8 通道                       |
| 驱动器最大负载能力 | 8 通道最大负载能力: DC 5V@3A |
| 通信接口           | I2C 通信 @ 0x25              |
| 产品尺寸           | 55.0 x 24.0 x 10.5mm         |
| 产品重量           | 10.0g                        |
| 包装尺寸           | 138.0 x 93.0 x 11.5mm        |
| 毛重               | 17.9g                        |

## 原理图

- [Unit 8Servos 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/620/SCH_UNIT_8Servos_V1.01.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/620/SCH_UNIT_8Servos_V1.01_sch_01.png">
</SchViewer>

## 管脚映射

### Unit 8Servos

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Servos Unit/img-2eae2b86-5d70-4245-9511-36a8efa3098f.jpg" width="100%" />

## 数据手册

- [INA199A1DCKR](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/8Servos%20Unit/INA199A1DCKR.pdf)

## 软件开发

### Arduino

- [Unit 8Servos Arduino 驱动库](https://github.com/m5stack/M5Unit-8Servo)

### UiFlow1

- [Unit 8Servos UiFlow1 文档](/zh_CN/uiflow/blockly/unit/8servo)
- [Unit 8Servos UiFlow1 Example](https://flow.m5stack.com/?examples=unit_8servos_demo)

### UiFlow2

- [Unit 8Servos UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/servos8.html)

### 内置固件

- [Unit 8Servos 内置固件](https://github.com/m5stack/Unit8Servo-Internal-FW)

### 通信协议

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/8Servos Unit/arduinoCase-1691131676758ptotocol.png" width="100%"/>

## 相关视频

- 舵机控制案例

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/8Servos%20Unit/U165.mp4" type="video/mp4"></video>

- UiFlow2

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113382388731166&bvid=BV1ij1GYSEHW&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/TlXNiie_GAU?si=UcInNRaDQlR3oIeh" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
