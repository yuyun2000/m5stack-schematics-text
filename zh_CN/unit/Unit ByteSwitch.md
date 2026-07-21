# Unit ByteSwitch

<span class="product-sku">SKU:U191</span>

<PictureViewer>
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/4.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/6.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/15.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/5.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/7.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/8.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/9.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/10.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/11.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/12.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/13.webp">
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/14.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/820/U191-weight.jpg">
</PictureViewer>

## 描述

**Unit ByteSwitch** 是一款 8 路钮子开关输入单元，配备 8 路 钮子开关和 9 颗 WS2812C RGB 灯珠，采用 STM32 作为主控，支持 I2C 通讯，板载两个 **Port A** I2C 接口，支持多个 Unit ByteSwitch 单元 **级联** 使用，满足复杂系统的需求。它能够实现拨动钮子开关输入检测与动态灯光状态反馈，适用于智能家居控制、游戏娱乐设备、教育开发平台、工业状态显示以及互动展览等领域。

## 产品特性

- 8 路钮子开关输入
- 9 颗 WS2812C RGB 灯珠
- STM32 主控
- I2C 通讯接口
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit ByteSwitch
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x DIY 贴纸

## 应用场景

- 智能家居控制面板
- 游戏或娱乐设备控制器
- 教育与实验室开发平台
- 状态控制与反馈装置
- 便携式设备调试工具
- 互动展览或场景控制
- 小型仪器的用户界面

## 规格参数

| 规格       | 参数                                                  |
| ---------- | ----------------------------------------------------- |
| MCU        | STM32G031G8U6，32 位 ARM Cortex-M0+ 内核，主频 64 MHz |
| 钮子开关   | 8 路独立钮子开关 (双刀双掷)                           |
| RGB 灯珠   | WS2812C-2020 (9 颗)                                   |
| 通信接口   | I2C 通讯 @0x46                                        |
| Grove 接口 | 2 个 (I2C 总线级联扩展)                               |
| 待机功耗   | DC 5V@9.03mA                                          |
| 工作温度   | 0 ~ 40°C                                              |
| 产品尺寸   | 88.0 x 24.0 x 19.6mm                                  |
| 产品重量   | 12.2g                                                 |
| 包装尺寸   | 170.0 x 120.0 x 20.6mm                                |
| 毛重       | 29.3g                                                 |

## 原理图

- [Unit ByteSwtich 原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/820/SCH_Unit-ByteSwitch_V1.0.pdf)

<img alt="schematics" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/820/SCH_Unit-ByteSwitch_V1.0_page_01.png" width="100%" />

## 管脚映射

### Unit ByteSwitch

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### STM32

| STM32 | PA0   | PA1   | PA5   | PA6   | PA7   | PA15  | PB3   | PA8   | PB5 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | --- |
| KEY   | SW_K0 | SW_K1 | SW_K2 | SW_K3 | SW_K4 | SW_K5 | SW_K6 | SW_K7 | RGB |

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/model%20size.png" width="100%" />

## 软件开发

### Arduino

- [Unit ByteSwitch 测试程序](https://github.com/m5stack/M5Unit-ByteButton/tree/main/examples/unit-byteSwitch)

### UiFlow2

- [Unit ByteSwitch UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/byteswitch.html)

### 内置固件

- [Unit ByteSwitch 内置固件](https://github.com/m5stack/M5Unit-ByteSwitch-Internal-FW)

### 通信协议

- [Unit ByteSwtich I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/820/Byte_Switch_protocol.pdf)

<img alt="protocol" src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/820/Byte_Switch_protocol_page_01.png" width="100%" />

## 相关视频

- Unit ByteSwtich 产品介绍以及案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit%20ByteSwitch/U191%20BYTESWITCH%20UNIT%20Video.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113802104275442&bvid=BV1Z3cEe3Exo&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/g7iKdCUl0U4?si=zIwdeURCyIb-6j4o" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
