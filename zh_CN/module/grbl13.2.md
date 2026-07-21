# Module13.2 GRBL

<span class="product-sku">SKU:M035</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/grbl13.2/grbl13.2_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/grbl13.2/grbl13.2_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/grbl13.2/grbl13.2_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/grbl13.2/grbl13.2_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/grbl13.2/grbl13.2_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/grbl13.2/grbl13.2_09.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/grbl13.2/grbl13.2_06.webp">
</PictureViewer>

## 描述

**Module13.2 GRBL** 是 M5Stack 堆叠模块系列中的一款三轴步进电机驱动模块，采用 ATmega328P-AU 控制器搭配三组 DRV8825PWPR 步进电机驱动芯片控制方案，能够同时驱动三台双极步进电机联动。提供 I2C 通信接口 (addr:0x70) 并集成拨码开关用于调节电机步进细分 (最大支持 1/32 步进细分) 与 I2C 地址调节 (支持双地址调节 0x70 , 0x71 )，这意味着你可以通过堆叠两块 **Module13.2 GRBL** 模块实现六轴控制。电源输入接口为 DC 9 ~ 24V ，电机驱动电流可达 1.5A ，开放三组限位开关信号接口，能够用于外接限位开关实现电机制动功能 (低电平有效) 。适用于多种步进电机运动控制场景，如打印机，机械臂等。

## 产品特性

- ATmega328P-AU 控制器
- 三轴 DRV8825PWPR 步进电机驱动器
- 驱动电流可达 1.5A
- 适用于双极步进电机
- 最大 1/32 模式 STEP 细分
- 限位开关接口 (低电平有效)

## 包装内容

- 1 x Module13.2 GRBL

## 应用场景

- 打印机
- 扫描仪
- 办公自动化机器
- 工厂自动化
- 机器人技术

## 规格参数

| 规格               | 参数                  |
| ------------------ | --------------------- |
| 电机驱动芯片       | DRV8825PWPR           |
| 控制器芯片         | ATmega328P-AU         |
| 通信接口           | I2C 通信 @ 0x70, 0x71 |
| 单通道最大驱动电流 | 1.5A                  |
| 支持最大步进细分   | 1/32                  |
| 接口类型           | XT2.54-4P             |
| 产品尺寸           | 54.2 x 54.2 x 13.2mm  |
| 产品重量           | 22.5g                 |
| 包装尺寸           | 95.0 x 65.0 x 25.0mm  |
| 毛重               | 42.3g                 |

## 操作说明

### 步进细分调节

| MODE2 | MODE1 | MODE0 | STEP MODE                                       |
| ----- | ----- | ----- | ----------------------------------------------- |
| 0     | 0     | 0     | Full step (2-phase excitation) with 71% current |
| 0     | 0     | 1     | 1/2 step (1-2 phase excitation)                 |
| 0     | 1     | 0     | 1/4 step (W1-2 phase excitation)                |
| 0     | 1     | 1     | 1/8 step                                        |
| 1     | 0     | 0     | 1/16 step                                       |
| 1     | 0     | 1     | 1/32 step                                       |
| 1     | 1     | 0     | 1/32 step                                       |
| 1     | 1     | 1     | 1/32 step                                       |

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/grbl13.2/grbl13.2_11.webp">

### I2C 地址调节

| Switch | Address |
| ------ | ------- |
| 0      | 0x70    |
| 1      | 0x71    |

## 原理图

- [Module13.2 GRBL 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/546/Sch_M5GRBL_V1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/546/Sch_M5GRBL_V1.1_sch_01.png">
</SchViewer>

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN | LEFT | RIGHT | PIN |
| --- | ---- | ----- | --- |
| GND | 1    | 2     | TXD |
| GND | 3    | 4     |     |
| GND | 5    | 6     | RST |
|     | 7    | 8     |     |
|     | 9    | 10    |     |
|     | 11   | 12    | 3V3 |
|     | 13   | 14    |     |
|     | 15   | 16    |     |
| SDA | 17   | 18    | SCL |
|     | 19   | 20    |     |
|     | 21   | 22    | RXD |
|     | 23   | 24    |     |
|     | 25   | 26    |     |
|     | 27   | 28    | 5V  |
|     | 29   | 30    |     |
::

## 尺寸图

- [Module13.2 GRBL 模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/546/Module-GRBL.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/546/Module-GRBL_page_01.png" width="100%">

## 数据手册

- [DRV8825 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/DRV8825_en.pdf)
- [GRBL-Firmware](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/GRBL13.2-Module-Arduino-Library.zip)
- [GRBL v0.8-Configuration reference document](https://github.com/grbl/grbl/wiki/Configuring-Grbl-v0.8)

## 软件开发

### Arduino

- [Module13.2 GRBL Arduino 驱动库](https://github.com/m5stack/M5Module-GRBL-13.2/tree/master)

### UiFlow1

- [Module13.2 GRBL UiFlow1 文档](/zh_CN/uiflow/blockly/module/grbl)

### UiFlow2

- [Module13.2 GRBL UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/grbl.html)

### Easyloader

| Easyloader                                     | 下载链接                                                                                                   | 备注 |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---- |
| Module13.2 GRBL Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_GRBL13.2.exe) | /    |

## 相关视频

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/GRBL13.2.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115705898927514&bvid=BV1YXm7BoEbc&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/TXTcbJrklcg?si=ksIyLgbXwCa8ttXM" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
