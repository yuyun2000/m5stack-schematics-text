# Unit HBridge v1.1

<span class="product-sku">SKU:U160-V11</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/HBridge v1.1 Unit/img-8b503691-1b66-49d7-b05d-5838eb4a6c36.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/HBridge v1.1 Unit/img-2ff69023-7888-4cbc-be2e-e0017d49cbdd.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/HBridge v1.1 Unit/img-a0001536-d6ad-4e8c-aa3a-1ea87d0464ed.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/HBridge v1.1 Unit/img-9ac9a03f-0dd6-4458-8b1f-af435cae9b96.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/HBridge v1.1 Unit/img-8906fc21-abd8-43ee-ba20-b523f5e879a1.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/HBridge v1.1 Unit/img-8f2dd08e-2857-4613-9d53-5e2c8f395984.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/HBridge v1.1 Unit/img-5c8fbb96-801a-4743-b2d1-9ba28fc4c814.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/HBridge v1.1 Unit/img-573b5981-03f7-40ac-8365-04c212e91b02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/HBridge v1.1 Unit/img-1ffb9b4e-83f3-42e6-9abb-1a47029514df.webp">
</PictureViewer>

## 描述

**Unit HBridge v1.1**是一款直流电机驱动模块，采用 **STM32F030** 为主控，**RZ7899** 为驱动的方案实现电机驱动功能，与 M5 主机采用 **I2C** 通讯，用 (最高 16 位数据的) **PWM** 信号控制 **转速，前进，后退和制动**等功能。模块具有可靠的 **过流、过压、过热**保护功能，内置总电源 MOS 管开关电路，支持编程动态控制电机释放 / 锁定。内置总电流采集电路，可获知总电路参数，可以保证电机的安全运行，同时电路内还具有 6-12V 和 5V 切换电路，以适应不同电机的输入电源需求。该产品适用于 **机器人、电机驱动、工业自动化、智能家居**等领域。

## 产品特性

- 过流、过压、过热保护
- 电源切换
- i2c 地址：默认 0x20
- 电流检测
- PWM 控制
- 编程平台：Arduino、UiFlow

## 包装内容

- 1 × Unit HBridge v1.1
- 1 × HT3.96-4P
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x 内六角扳手 L 形 1.5mm (适配 M2 螺丝)
- 1 x 470uF 铝电解电容

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
| 电流采集芯片        | INA199A1DCKR                               |
| 外部接入直流电压    | MAX 12V                                    |
| 通信接口            | I2C 通信 @ 0x20 (可以通过编码开关拨动修改) |
| 最大负载电流        | 3A                                         |
| 使用温度            | 0 ~ 40°C                                   |
| 产品尺寸            | 56.0 x 24.0 x 10.2mm                       |
| 产品重量            | 8.9g                                       |
| 包装尺寸            | 138.0 x 93.0 x 11.2mm                      |
| 毛重                | 20.0g                                      |

## 操作说明

?>470uF 铝电解电容 | 配套的铝电解电容接到电源输入的正负极，可以对电路起到缓冲保护的左右，注意别接反！

<img alt="module size" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/769/U160_v1.1_connect_cap.png" width="30%" />

### 电机电源选择

?> 电机电源选择 | Unit HBridge v1.1 内部集成 DC/DC 降压电路，可以将外部 3.96 端子输入的 6 ~ 12V 降低至 5V 用于适配不同电机的电源需求。同时提供了一个电源切换开关，可用于选择电机电源使用外部输入的 6 ~ 12V 或 DC/DC 降压后的 5V。实际使用时，请根据电机的规格选择适合的驱动电压。

## 数据手册

- [STM32F030F4P6](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/STM32F030F4P6.PDF)
- [RZ7899](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/U160%20Hbridge%20Unit/RZ7899.PDF)
- [INA199A1DCKR](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/8Servos%20Unit/INA199A1DCKR.pdf)

## 原理图

- [Unit HBridge v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/615/SCH_UNIT_HBridge_V1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/615/SCH_UNIT_HBridge_V1.1_sch_01.png">
</SchViewer>

## 管脚映射

### Unit HBridge v1.1

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/839/U085_Model_Size.jpg" width="100%">

## 软件开发

### Arduino

- [Unit HBridge v1.1 测试程序](https://github.com/m5stack/M5Unit-Hbridge)

### UiFlow1

- [Unit HBridge v1.1 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/hbridge)

### 内置固件

- [Unit HBridge v1.1 内置固件](https://github.com/m5stack/M5Unit-Hbridge-Internal-FW)

### 通信协议

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/HBridge%20v1.1%20Unit/1c0f2f06b03b7b55265dfb4d4902827.png">

## 相关视频

- Unit HBridge V1.1 控制舵机

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/HBridge%20v1.1%20Unit/U160-V11%20HBridge%20v1.1%20Unit.mp4" type="video/mp4"></video>

## 版本变更

| SKU      | 版本              | 变更细节                       | 发布时间 |
| -------- | ----------------- | ------------------------------ | -------- |
| U160-V11 | Unit HBridge v1.1 | 优化电路以及添加了电流检测功能 | 2023.8   |
| U160     | Unit HBridge      | 首次发布                       | /        |