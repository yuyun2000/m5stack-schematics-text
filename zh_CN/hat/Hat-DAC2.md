# Hat DAC2

<span class="product-sku">SKU:U068-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/Hat-DAC2/img-26204d9b-195c-4c62-afbb-5b3232c09381.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/Hat-DAC2/img-62ee689a-6de2-497f-8e0d-82e70df42e1e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/Hat-DAC2/img-9af8822c-a3cb-471e-b29c-0e2469f58a22.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/Hat-DAC2/img-289dfe58-0972-4f00-9bb7-908eff81fbf6.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/Hat-DAC2/img-2513a25e-2e38-41cb-a630-8715f3a8a56f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/Hat-DAC2/img-c66a4a27-da26-406f-82d7-461da413d14a.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/885/U068-B-weight.jpg">
</PictureViewer>

## 描述

**Hat DAC2**是一款适配 StickC 系列主机的 I2C 数字信号转模拟信号转换单元。采用 GP8413 的方案，在精度方面，此芯片可以将 15Bit 数字量线性转换成两路独立的 0 - 5V/0 - 10V 模拟电压，输出电压误差为 0.2%，线性度可达 0.01%。扩展性方面，电路设计通过三位硬件地址 A2/A1/A0 进行选择。在安全性能方面，设备支持输出短路保护，输出引脚与地短路时自动进入保护模式停止输出。适用于通用信号转换，马达调速，LED 调光，逆变器、电源和工业模拟信号隔离等领域。

## 产品特性

- 适配 StickC/StickC PLUS/StickC PLUS2
- I2C 通讯 (默认地址 0x59)
- 支持多路并联使用
- 短路保护
- 高精度，误差小

## 包装内容

- 1 x Hat DAC2
- 1 x HT3.96-4P 端子
- 1 x 贴纸

## 应用场景

- 通用信号转换
- 马达调速、LED 调光
- 逆变器、电源
- 工业模拟信号隔离

## 规格参数

| 规格               | 参数                                |
| ------------------ | ----------------------------------- |
| DAC 芯片           | GP8413                              |
| 分辨率             | 15 位                               |
| 通信接口           | I2C 通信 @ 0x58 ~ 0x65，默认为 0x59 |
| 最大输出电压       | 10V                                 |
| 输出电压误差       | <0.2%                               |
| 输出电压线性度误差 | 0.01%                               |
| 工作温度           | 0-40°C                              |
| 产品尺寸           | 35.0 x 24.0 x 13.7mm                |
| 产品重量           | 6.8g                                |
| 包装尺寸           | 138.0 x 93.0 x 14.7mm               |
| 毛重               | 11.9g                               |

## 操作说明

<img alt="Address Select" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/hat/Hat-DAC2/98d93ea4c395cf6f97bce53fb1448d8.png" width="30%" />

| A2  | A1  | A0  | I2C 地址 (7 位) |
| :-: | :-: | :-: | :-------------: |
| 0   | 0   | 0   | 0x58            |
| 0   | 0   | 1   | 0x59 (默认)     |
| 0   | 1   | 0   | 0x5A            |
| 0   | 1   | 1   | 0x5B            |
| 1   | 0   | 0   | 0x5C            |
| 1   | 0   | 1   | 0x5D            |
| 1   | 1   | 0   | 0x5E            |
| 1   | 1   | 1   | 0x5F            |

\#> 地址选择 | 通过设置 A0、A1、A2 引脚为高电平 (1) 或低电平 (0)，可以获得从 0x58 到 0x5F 的 8 个不同 I2C 地址。连接了电阻即视为高电平 (1)，未连接电阻的则为低电平 (0)。

## 原理图

- [Hat DAC2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/581/SCH_StickHat_DAC2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/581/SCH_StickHat_DAC2_sch_01.png">
</SchViewer>

## 管脚映射

| StickC   | SDA | SCL | VCC | GND |
| -------- | --- | --- | --- | --- |
| DAC2 Hat | G0  | G26 | 5V  | GND |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/hat/Hat-DAC2/img-6af530a5-400b-41b9-8ade-f3d275fdc03a.jpg" width="100%" />

## 数据手册

- [GP8413 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-DAC2/GP8413.pdf)

## 软件开发

### Arduino

- [Hat DAC2 - with M5StickC](https://github.com/m5stack/M5StickC/tree/master/examples/Hat/DAC2_GP8413)
- [Hat DAC2 - with M5StickC-Plus](https://github.com/m5stack/M5StickC-Plus/tree/master/examples/Hat/DAC2_GP8413)
- [Hat DAC2 - with M5StickC-Plus2](https://github.com/m5stack/M5StickCPlus2/tree/master/examples/Hat/DAC2_GP8413)

### UiFlow1

- [Hat DAC2 UiFlow1 文档](/zh_CN/uiflow/blockly/hat/dac2)

### UiFlow2

- [Unit DAC2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/dac2.html)

## 常见问题

### Question: Hat-DAC2 与 Hat-DAC 的区别？

| 产品     | 通信协议 | 芯片方案 | EEPROM | 分辨率 | 输出电压     | I2C 地址                                 | 通道   |
| -------- | -------- | -------- | ------ | ------ | ------------ | ---------------------------------------- | ------ |
| DAC2 Hat | I2C      | GP8413   | /      | 15Bit  | 0-10V        | 可调 A0/A1/A2 (8 个 I2C 地址)(默认 0x59) | 双通道 |
| DAC Hat  | I2C      | MCP4725  | 配备   | 12Bit  | VDD (0-3.3V) | 默认 0x60，不可调                        | 单通道 |
