# Unit PbHub

<span class="product-sku">SKU:U041</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub/pbhub_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub/pbhub_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub/pbhub_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub/pbhub_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub/pbhub_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub/pbhub_06.webp">
</PictureViewer>

## 描述

**Unit PbHub**，是一款 GPIO HY2.0-4P PORTB 扩展器，能够将单路 GPIO Grove 接口拓展至六路。内部集成 MEGA328，且搭载驱动程序。不支持多 Unit 嵌套，这意味着无法像 **PaHUB** 一样挂载多个相同协议、地址的设备。

## 产品特性

- GPIO HY2.0-4P PORTB 拓展
- 2 x LEGO 兼容孔
- 1-6 拓展

## 包装内容

- 1 x Unit PbHub
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 规格参数

| 规格     | 参数                                         |
| -------- | -------------------------------------------- |
| MCU      | STM32F030F4P6                                |
| 通信接口 | I2C 通信 @ 0x61 (可通过电阻 A0，A1，A2 修改) |
| 产品尺寸 | 48.0 x 24.0 x 10.8mm                         |
| 产品重量 | 7.1g                                         |
| 包装尺寸 | 138.0 x 93.0 x 11.8mm                        |
| 毛重     | 12.4g                                        |

## 操作说明

\#>**注意**<br/>1. 内置 MCU 的 ADC 输入电压默认范围为**0-5V**，对应的 ADC 分辨率为**10bit** (1024)，因此在使用输入范围小于 5V 的模拟信号输入时候，会无法达到最大值 1024。<br/>2. 并非所有带有黑色接口 (PortB) 的 Unit 都支持通过 PbHUB 扩展.PbHUB 只能应用于基本的单总线通信，通过 I2C 协议 (内置 MEGA328) 能够实现基本的数字读写，模拟读写。但对于像 Weight (内置 HX711) 这种通信不仅需要进行 anglog 读取，还需要依赖于时序的 Unit 来说，PbHUB 无法进行拓展.<br/>3.Port B 中的两条数据总线与 ESP32 的**G36**和**G26**连接，可根据需求编程配置多个端口的输入 (支持模拟输入) 、输出.

<div class="product_pic"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub/pbhub_note_01.webp"></div>

### 修改 I2C 地址

该 Unit 的 I2C 地址为 0x61 (可通过焊接电阻 A0 ~ A2 进行更改，地址范围为 0x61 ~ 0x68) .

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub/pbhub_note_02.webp" width="25%">

| A0       | A1       | A2       | I2C Address |
| -------- | -------- | -------- | ----------- |
| /        | /        | /        | 0x61        |
| 焊接电阻 | /        | /        | 0x62        |
| /        | 焊接电阻 | /        | 0x63        |
| 焊接电阻 | 焊接电阻 | /        | 0x64        |
| /        | /        | 焊接电阻 | 0x65        |
| 焊接电阻 | /        | 焊接电阻 | 0x66        |
| /        | 焊接电阻 | 焊接电阻 | 0x67        |
| 焊接电阻 | 焊接电阻 | 焊接电阻 | 0x68        |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub/pbhub_sch_01.webp" width="80%">

## 管脚映射

### Unit PbHub

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### Mega328 ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

## 软件开发

### Arduino

- [Unit PbHub 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/PbHUB)

### UiFlow1

- [Unit PbHub UiFlow1 文档](/zh_CN/uiflow/blockly/unit/pbhub)
- [Unit PbHub 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/PbHUB/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/pbhub/pbhub_uiflow_01.webp" width="65%">

### 通信协议

| state              | IO0 Digital Write | IO1 Digital Write | IO0 Analog Write | IO1 Analog Write | IO0 Digital Read | IO1 Digital Read | IO0 Analog Read | reserve | Set RGB LED Num | Set oneLED Color\* | Set moreLED Color\* | Set Brightness |
| ------------------ | ----------------- | ----------------- | ---------------- | ---------------- | ---------------- | ---------------- | --------------- | ------- | --------------- | ------------------ | ------------------- | -------------- |
| r/w                | w                 | w                 | w                | w                | r                | r                | r               | r       | w               | w                  | w                   | w              |
| data length (Byte) | 1                 | 1                 | 1                | 1                | 1                | 1                | 2               | /       | 2               | 5                  | 7                   | 1              |
| ch0 cmd            | 40                | 41                | 42               | 43               | 44               | 45               | 46              | 47      | 48              | 49                 | 4A                  | 4B             |
| ch1 cmd            | 50                | 51                | 52               | 53               | 54               | 55               | 56              | 57      | 58              | 59                 | 5A                  | 5B             |
| ch2 cmd            | 60                | 61                | 62               | 63               | 64               | 65               | 66              | 67      | 68              | 69                 | 6A                  | 6B             |
| ch3 cmd            | 70                | 71                | 72               | 73               | 74               | 75               | 76              | 77      | 78              | 79                 | 7A                  | 7B             |
| ch4 cmd            | 80                | 81                | 82               | 83               | 84               | 85               | 86              | 87      | 88              | 89                 | 8A                  | 8B             |
| ch5 cmd            | A0                | A1                | A2               | A3               | A4               | A5               | A6              | A7      | A8              | A9                 | AA                  | AB             |

### EasyLoader

| Easyloader                 | 下载链接                                                                                      | 备注 |
| -------------------------- | --------------------------------------------------------------------------------------------- | ---- |
| Unit PbHub Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_PbHUB.exe) | /    |

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112907928996428&bvid=BV11daoeCEHH&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/yE_FMxObeUk?si=svANLqUs94r86esD" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
