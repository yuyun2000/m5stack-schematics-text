# Module HMI

<span class="product-sku">SKU:M129</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/HMI Module/img-4c227abf-0a4c-4e3a-b711-b81a35899aaf.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/HMI Module/img-e65de291-c881-4367-8043-5c14904758a3.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/HMI Module/img-096f61e8-f01c-4c2e-baa8-655c7ee85bc9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/HMI Module/img-959c9664-8025-48af-9c23-873a49e326c0.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/HMI Module/img-6d9d1949-300d-48cf-a273-03cd231d733e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/HMI Module/img-6681bb67-363b-4c6e-a815-47ff23656c30.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/HMI Module/img-e4ab2d6d-b58d-4f3f-91ab-96e656b0b835.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/HMI Module/img-35aec29d-b7f5-43ab-b9c4-7a2d6ada1d09.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/HMI Module/img-efb6a714-d1e6-4278-bac5-e17a3d52d87c.webp">
</PictureViewer>

## 描述

**Module HMI** 是一款人机交互操作的模块，提供了**拨轮旋转编码器**、**两个输入按键**和**两个 LED 指示灯**，采用 STM32F030 作为采集及通信 MCU ，与 M5 主机通过 I2C 进行通讯。此外，模块上留有 **PORT.B** 和 **PORT.C** 接口，并内置一个 **500mAh** 的锂电池。该模块适用于各种需要手持操作交互的应用领域。

## 产品特性

- STM32F030F4P6，ARM Cortex-M0 @ 16 KB 闪存和 4 KB SRAM
- 人机交互方式 (拨轮旋转编码器 Encoder、两路输入按键和两路指示灯)
- PORT B 和 PORT C 接口
- 编程平台：Arduino、UiFlow

## 包装内容

- 1× Module HMI

## 应用场景

- 工业控制
- 嵌入式系统
- 智能家居

## 规格参数

| 规格     | 参数                                             |
| -------- | ------------------------------------------------ |
| MCU      | STM32F030F4P6                                    |
| 通信接口 | I2C 通信 @ 0x41                                  |
| 互动外设 | 拨轮旋转编码器 Encoder、两路输入按键和两路指示灯 |
| 电池     | 500mAh 的聚合物电池                              |
| 输入电压 | 5V                                               |
| 工作温度 | 0°C ~ 40°C                                       |
| 产品尺寸 | 54.0 x 55.8 x 13.0mm                             |
| 产品重量 | 22.8g                                            |
| 包装尺寸 | 95.0 x 77.0 x 14.0mm                             |
| 毛重     | 30.0g                                            |

## 原理图

- [Module HMI 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/556/SCH_Module_HMI_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/556/SCH_Module_HMI_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN      |
| -------- | ---- | ----- | -------- |
| GND      | 1    | 2     |          |
| GND      | 3    | 4     | PORT.B   |
| GND      | 5    | 6     |          |
|          | 7    | 8     | PORT.B   |
|          | 9    | 10    |          |
|          | 11   | 12    |          |
|          | 13   | 14    |          |
| TXD      | 15   | 16    | RXD      |
| SDA      | 17   | 18    | SCL      |
|          | 19   | 20    |          |
|          | 21   | 22    |          |
|          | 23   | 24    |          |
| HPWR     | 25   | 26    |          |
| HPWR     | 27   | 28    | 5V       |
| HPWR     | 29   | 30    |          |
::

## 尺寸图

[Module HMI模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/989/hmi.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/989/hmi_page_01.png" width="100%">

## 数据手册

- [STM32F030F4P6 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/STM32F030F4P6.PDF)

## 软件开发

### Arduino

- [Module HMI Arduino 驱动库](https://github.com/m5stack/M5Module-HMI)

### UiFlow1

- [Module HMI UiFlow1 文档](/zh_CN/uiflow/blockly/module/hmi)

### UiFlow2

- [Module HMI UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/hmi.html)

### 内置固件

- [Module HMI 内置固件](https://github.com/m5stack/M5Module-HMI-Internal-FW)

### 通信协议

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/module/HMI%20Module/c774678ce7cb21e4de63f7442df7b3d.png" width="100%" />

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113678288422342&bvid=BV1jUkgYuESB&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/qOm6c--WZRA?si=mttbsIQ6Bo7K-_0a" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
