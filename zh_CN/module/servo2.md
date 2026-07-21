# Module13.2 Servo2

<span class="product-sku">SKU:M014-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/965/M014-B-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_06.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_07.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_08.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_09.webp">
</PictureViewer>

## 描述

**Module13.2 Servo2** 是 M5Stack 堆叠模块系列中的一款舵机驱动模块 ，内部采用 PCA9685 16 通道 PWM 控制器，可以同时控制 16 路舵机。采用直流电源输入（6 ~ 12V） 设计，通过两片 SY8368AQQC 进行降压，双通道输出最大总功率 35W （5V/3.5A x 2） ，单通道输出最大功率 25W（5V / 5A） ，当使用电池底座供电时最高支持 5V/2A 输出。模块与主机直接通过 I2C 进行通讯 （默认 0x40） ，通过拨码开关可改变 I2C 地址 （0x40 ~ 0x47） ，这也意味着多个 Module13.2 Servo2 可以堆叠使用，板上有一个电源切换开关，可控制 Module13.2 Servo2 电源通断。

## 注意事项

\#> 模块供电 | 该模块驱动舵机时必须使用 DC 接口外部供电。使用电源管理芯片的主控 (如 Core2/CoreS3), 在程序初始化时需要将 M5-Bus 电源模式配置为输入。

## 产品特性

- 16 x 舵机驱动通道
- 2 x 电源指示灯
- I2C 地址可调
- 独立开关电源控制
- 外部 DC 电源输入: 6-12V
- DC 连接器类型: XT60

## 包装内容

- 1 x Module13.2 Servo2
- 1 x XT60 电源连接线 (11.5cm)

## 应用场景

- 人形机器人
- 仿生多关节机器人
- 3 轴舵机云台

## 规格参数

| 规格     | 参数                   |
| -------- | ---------------------- |
| 通信接口 | I2C 通信 @ 0x40 ~ 0x47 |
| 产品尺寸 | 54.2 x 54.2 x 19.7mm   |
| 产品重量 | 28.0g                  |
| 包装尺寸 | 135.0 x 95.0 x 20.5mm  |
| 毛重     | 60.0g                  |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/module/servo2/servo2_sch_01.webp" width="80%">

## 管脚映射

### M5-Bus

::m5-bus-table
| PIN | LEFT | RIGHT | PIN |
| --- | ---- | ----- | --- |
| GND | 1    | 2     |     |
| GND | 3    | 4     |     |
| GND | 5    | 6     |     |
|     | 7    | 8     |     |
|     | 9    | 10    |     |
|     | 11   | 12    | 3V3 |
|     | 13   | 14    |     |
|     | 15   | 16    |     |
| SDA | 17   | 18    | SCL |
|     | 19   | 20    |     |
|     | 21   | 22    |     |
|     | 23   | 24    |     |
|     | 25   | 26    |     |
|     | 27   | 28    | 5V  |
|     | 29   | 30    |     |
::

## 尺寸图

- [Module13.2 Servo2 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/965/servo2.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/965/servo2_page_01.png" width="100%">

## 数据手册

- [PCA9685 - datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/PCA9685.pdf)

## 软件开发

### Arduino

- [Module13.2 Servo2 Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Modules/SERVO2_PCA9685)

### UiFlow1

- [Module13.2 Servo2 UiFlow1 文档](/zh_CN/uiflow/blockly/module/servo2)

### UiFlow2

- [Module13.2 Servo2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/module/servo2.html)

### Easyloader

| Easyloader                                       | 下载链接                                                                                                 | 备注 |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | ---- |
| Module13.2 Servo2 Example Easyloader with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/MODULE/EasyLoader_Servo2.exe) | /    |

## 相关视频

<video id="example_video" controls> <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Module/Servo2.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114057386394083&bvid=BV1vYPsewEXE&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/tgN8T9_Nju0?si=feyFbVjPnrIp0XPX" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
