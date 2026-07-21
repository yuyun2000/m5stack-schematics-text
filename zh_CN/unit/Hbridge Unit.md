# Unit HBridge

<span class="product-sku">SKU:U160</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/img-3f610a3a-12be-4bd9-83b7-32f24b16b982.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/img-d13af54d-b8fc-4731-a8e5-b22935be78b3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/img-2c632802-aebd-468e-a364-3ac030a16234.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/img-e97aacd0-3218-407d-89f2-58c7a6d734c9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/img-4877fe4a-c9f2-42ac-a437-134a02b6f642.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/img-7d6f90c1-2a1d-4b5e-bcbf-167b1568007c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/img-6009ced7-8cd6-4dec-a159-3b61b0330fd1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/img-08e15ee0-02f7-4a5f-a73e-de5498e3bf79.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/img-b286be3e-fc45-4462-ab05-6849076bf46c.webp">
</PictureViewer>

## 描述

**Unit HBridge**是一款直流电机驱动模块，**采用 “STM32F030 + RZ7899” 方案实现电机驱动功能**，与 M5 主机采用 I2C 通讯方式实现 **PWM** 控制转速，**前进，后退和制动**等功能。模块具有可靠的 **过流、过压、过热**保护功能，可以保证电机的安全运行，同时电路内还具有 6 ~ 12V 和 5V 切换电路，以适应不同电机的输入电源需求。该产品适用于 **机器人、电机驱动、工业自动化、智能家居**等领域。

## 产品特性

- 过流、过压、过热保护
- 电源切换
- i2c 地址：默认 0x20
- 编程平台：Arduino、UiFlow

## 包装内容

- 1 × Unit HBridge
- 1 × HT3.96-4P
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)

## 应用场景

- 机器人
- 电机驱动
- 工业自动化
- 智能家居

## 规格参数

| 规格                | 参数                                       |
| ------------------- | ------------------------------------------ |
| MCU                 | STM32F030F4P6                              |
| DC 双向马达驱动芯片 | RZ7899                                     |
| 外部接入直流电压    | MAX 12V                                    |
| 通信接口            | I2C 通信 @ 0x20 (可以通过编码开关拨动修改) |
| 最大允许电流        | 3A                                         |
| 使用温度            | 0 ~ 40°C                                   |
| 产品尺寸            | 56.0 x 24.0 x 10.2mm                       |
| 产品重量            | 8.9g                                       |
| 包装尺寸            | 138.0 x 93.0 x 11.2mm                      |
| 毛重                | 18.1g                                      |

## 操作说明

?>470uF 铝电解电容 | 配套铝电解电容接入电源输入正负极，可对电路起到缓冲与保护作用，安装时请注意正负极方向，切勿接反。

<img alt="module size" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/769/U160_v1.1_connect_cap.png" width="30%" />

### 电机电源选择

?> 电机电源选择 | Unit HBridge 内部集成 DC/DC 降压电路，可以将外部 3.96 端子输入的 6 ~ 12V 降低至 5V 用于适配不同电机的电源需求。同时提供了一个电源切换开关，可用于选择电机电源使用外部输入的 6 ~ 12V 或 DC/DC 降压后的 5V。实际使用时，请根据电机的规格选择适合的驱动电压。

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/img-f4f40b0f-e9ef-47f0-9b5d-6378e00d3c0f.png" width="100%" />

## 管脚映射

### Unit HBridge

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/839/U085_Model_Size.jpg" width="100%">

## 数据手册

- [STM32F030F4P6](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/STM32F030F4P6.PDF)
- [RZ7899](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U160%20Hbridge%20Unit/RZ7899.PDF)

## 软件开发

### Arduino

- [Unit HBridge Arduino 驱动库](https://github.com/m5stack/M5Unit-Hbridge)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/arduinoCase-1680848177975M5PPT.png" width="100%"/>

### UiFlow1

- [Unit HBridge UiFlow1 文档](/zh_CN/uiflow/blockly/unit/hbridge)

### UiFlow2

- [Unit Hbridge UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/hbridge.html)

### 内置固件

- [Unit HBridge 内置固件](https://github.com/m5stack/M5Unit-Hbridge-Internal-FW)

### 通信协议

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Hbridge Unit/arduinoCase-168057629657611.png" width="100%"/>

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113269897430233&bvid=BV1Yk27YcEhh&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/PtXUO9MpqM4?si=KKCD0mwybw_cm6p-" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
