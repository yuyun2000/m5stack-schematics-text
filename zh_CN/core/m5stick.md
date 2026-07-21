# M5Stick

<span class="product-sku">SKU:K016</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/static/assets/img/product_pics/core/minicore/m5stick/m5stick_04.webp">
</PictureViewer>

## 描述

**M5Stick** 是一款迷你的 IoT 开发板。它集成了 ESP32 芯片，具备 Wi-Fi 功能以及 IMU 姿态传感器，无论是用于编程学习，还是进行项目开发，M5Stick 都能提供可靠的硬件支持。

它能做些什么呢？这个小巧的开发工具，可以激发无限的创作可能性。 M5Stick 能够助力快速搭建物联网产品原型，简化整个开发流程。即使是刚接触编程开发的初学者，也能够利用它搭建出一些有趣的应用，并将其应用到实际生活当中。

M5Stick 是 M5Stack 产品系列中的核心设备之一，该产品系列构建于不断发展的硬件和软件生态系统之上。它拥有众多兼容的拓展功能模块、丰富的开源代码以及活跃的论坛社区，这些资源能够在开发过程中为使用者提供强大的支持。

## 产品特性

- 基于 ESP32 开发
- 9 自由度姿态传感器 (只有灰色款配备)
- 内置 LED
- 集成蜂鸣器
- 集成红外发射管
- 自定义按键，OLED (1.3 寸)，电源 / 复位按键 x1
- 内置锂电池
- Grove 接口
- 可穿戴 & 可固定
- 开发平台
  - PlatformIO

## 包装内容

- 1 x M5Stick
- 1 x USB Type-C(20cm)

## 应用场景

- 物联网控制器
- STEM 教育
- DIY 作品
- 智能家居设备
- 开发平台
  - Arduino IDE
  - ESP-IDF
  - PlatformIO

## 规格参数

| 主控资源  | 参数                                     |
| --------- | ---------------------------------------- |
| SoC       | ESP32-WROOM32@双核处理器，主频 240MHz    |
| Flash     | 4MB                                      |
| Wi-Fi     | 2.4 GHz Wi-Fi                            |
| DMIPS     | 600                                      |
| SRAM      | 520KB                                    |
| 输入电压  | 5V@500mA                                 |
| 接口      | USB Type-C x 1，GROVE (I2C+I/O+UART) x 1 |
| OLED 屏幕 | 1.3 inch，64 x 128，SH1107               |
| 蜂鸣器    | 有源蜂鸣器 x 1                           |
| 按键      | 自定义按键 x 1                           |
| LED       | Blue LED x 1                             |
| IR        | Infrared transmission x 1                |
| MEMS      | MPU9250 (灰色版)                         |
| 电池      | 80mAh@3.7V，inside vb                    |
| 天线      | 2.4G 3D 天线                             |
| 工作温度  | 0 ~ 60°C                                 |
| 外壳材质  | Plastic ( PC )                           |
| 产品尺寸  | 48.2 x 25.5 x 13.7mm                     |
| 产品重量  | 14.0g                                    |
| 包装尺寸  | 85.0 x 55.0 x 31.0mm                     |
| 毛重      | 65.0g                                    |

## 操作说明

**开关机操作：**

- 开机：按复位按键，单击

- 关机：按复位按键，双击

## 原理图

- [EspCore-schematic](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/m5stick/EspCore.pdf).
- [Power-schematic](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/m5stick/Power.pdf).
- [UsbUART-schematic](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/schematic/Core/m5stick/UsbUART%20(revised%20edition).pdf>).

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/511/EspCore_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/511/Power_page_01.png">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/511/UsbUART_page_01.png">
</SchViewer>

## 管脚映射

### LED & BUTTON & BUZZER & IR

| ESP32-WROOM32 | G17        | G19      | G26        | G35      |
| ------------- | ---------- | -------- | ---------- | -------- |
| 红外发射管 IR | 发射管引脚 |          |            |          |
| 蓝色 LED      |            | LED 管脚 |            |          |
| 蜂鸣器 BUZZER |            |          | 蜂鸣器管脚 |          |
| 按键 BUTTON   |            |          |            | 按键管脚 |

### OLED 屏幕

| ESP32-WROOM32 | G14 | G27 | G33 | G18 | G23 |
| ------------- | --- | --- | --- | --- | --- |
| OLED 屏幕     | CS  | DC  | RST | D0  | D1  |

### IP5306 充 / 放电，电压参数

| 充电                | 放电                 |
| ------------------- | -------------------- |
| 0.00 ~ 3.40V -> 0%  | 4.20 ~ 4.07V -> 100% |
| 3.40 ~ 3.61V -> 25% | 4.07 ~ 3.81V -> 75%  |
| 3.61 ~ 3.88V -> 50% | 3.81 ~ 3.55V -> 50%  |
| 3.88 ~ 4.12V -> 75% | 3.55 ~ 3.33V -> 25%  |
| 4.12 ~ /-> 100%     | 3.33 ~ 0.00V -> 0%   |

### 灰色版本：

| ESP32-WROOM32          | G22 | G21 |
| ---------------------- | --- | --- |
| 九轴姿态传感器 MPU9250 | SCL | SDA |

### HY2.0-4P

::grove-table
| HY2.0-4P    | Black | Red | Yellow | White |
| ----------- | ----- | --- | ------ | ----- |
| PORT.CUSTOM | GND   | 5V  | G32    | G33   |
::

## 数据手册

- [ESP32](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/esp32_datasheet_cn.pdf)

- [MPU9250](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/PS-MPU-9250A-01-v1.1_en.pdf)

- [IP5306](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/IIC_IP5306_REG_V1.4_cn.pdf)

## 软件开发

### Arduino

- [M5Stick 出厂测试例程](https://github.com/m5stack/M5Stack/tree/master/examples/Stick/FactoryTest)

- [M5Stick 手表](https://github.com/m5stack/StickWatch)

### Easyloader

> EasyLoader 是一个简洁快速的程序烧录器，其内置了一个产品相关的案例程序，通过简单步骤将其烧录至主控，即可进行一系列的功能验证。

| Easyloader              | 下载链接                                                                                                            | 备注 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- | ---- |
| FactoryTest for Windows | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/CORE/EasyLoader_M5Stick_FactoryTest.exe) | /    |
| FactoryTest for MacOS   | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/MacOS/CORE/EasyLoader_M5Stick_FactoryTest.dmg)   |

## 相关视频

- M5Stick 出厂例子

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Core/M5Stick.mp4" type="video/mp4">
</video>

\#>**案例描述：**<br/>屏幕 LED IR 蜂鸣器 按键测试，单击按键 A 屏幕将打印显示 helloworld。

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1055479573&bvid=BV17n4y197jg&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" autoplay="0"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/CmgF4-5rKgA?si=AR0UgPb_Xe-mh3Fu" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=1005334471&bvid=BV16x4y1E7Mj&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" autoplay="0"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/giUopfku__o?si=pXtELBMXt9HC8ZqJ" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
