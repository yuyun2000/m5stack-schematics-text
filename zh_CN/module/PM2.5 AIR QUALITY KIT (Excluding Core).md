# Module Air Quality

<span class="product-sku">SKU:M134</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PM2.5 AIR QUALITY KIT (Excluding Core)/img-3fdafe0e-bb11-4ad5-b6d6-061919cc735b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PM2.5 AIR QUALITY KIT (Excluding Core)/img-865d4d36-439c-4f27-874c-e319052d91fb.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PM2.5 AIR QUALITY KIT (Excluding Core)/img-8bfbaac4-1127-43f9-b5ae-da5ef8c02650.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PM2.5 AIR QUALITY KIT (Excluding Core)/img-619b0053-f93a-472d-acee-dbbc2ed85618.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PM2.5 AIR QUALITY KIT (Excluding Core)/img-09fe6653-aa56-486a-b0c2-d6b06bc13ae7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PM2.5 AIR QUALITY KIT (Excluding Core)/img-e87513b1-6bf7-4ba4-ba56-0e0257ce9e46.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PM2.5 AIR QUALITY KIT (Excluding Core)/img-b9a61c81-e57f-40bb-ad3b-064de8649e56.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PM2.5 AIR QUALITY KIT (Excluding Core)/img-76cba9d0-c425-4a6d-a76d-acb03ca1ad98.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/module/PM2.5 AIR QUALITY KIT (Excluding Core)/img-50f14bb6-030f-4d1a-8f66-3be477e8c7bf.webp">
</PictureViewer>

## 描述

**Module Air Quality** 是一款环境空气质量检测产品套件。该产品采用 **PMSA003** 数字式通用颗粒物浓度传感器，能够快速检测当前环境的温湿度数据，并采集计算单位体积内空气中不同粒径的悬浮颗粒物个数。简洁可靠的设计使其能够快速地部署节点，并应用在生活或是工业等场景中，用作环境数据采集，或为空气中悬浮颗粒物浓度相关的仪器仪表或环境改善设备，提供实时准确的浓度数据。

## 产品特性

- 直流 5V 电源
- 兼容 M5Stack 拓展堆叠体系
- Core 底座 (Pin out SPI/I2C/Power)

## 包装内容

- 1 x Module Air Quality
- 1 x 内六角扳手 L 形 2.5mm (适配 M3 螺丝)
- 2 x M3x14 螺丝

## 应用场景

- 环境 PM2.5 测量

## 规格参数

| 规格                 | 参数                          |
| -------------------- | ----------------------------- |
| PM2.5 传感器         | PMSA003                       |
| 最小分辨粒径         | 0.3μm                         |
| 颗粒物质量浓度分辨率 | 1μg/m³                        |
| 颗粒物测量范围       | 0.3-1.0、1.0-2.5、2.5-10 微米 |
| 供电电压             | 5V                            |
| 工作温度             | 0~+40°C                       |
| 工作湿度范围         | 0~99%                         |
| 产品尺寸             | 54.0 × 54.0 × 18.7mm          |
| 产品重量             | 33.8g                         |
| 包装尺寸             | 95.0 × 66.0 × 26.0mm          |
| 毛重                 | 58.2g                         |

## 原理图

[Module Air Quality 原理图PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1030/Module-Air-Quality.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1030/M134_01.png">
</SchViewer>

## 管脚映射

### Ext Port-2.54 6P

| M5-Bus Pin Num   | 28  | 12  | 1-3 | 17  | 18  | 7    | 9    | 11  |
| ---------------- | --- | --- | --- | --- | --- | ---- | ---- | --- |
| Ext Port 2.54-6P | 5V  | 3V3 | GND | SDA | SCL | MOSI | MISO | SCK |

### M5-Bus

::m5-bus-table
| PIN      | LEFT | RIGHT | PIN     |
| -------- | ---- | ----- | ------- |
| GND      | 1    | 2     | NC      |
| GND      | 3    | 4     | NC      |
| GND      | 5    | 6     | NC      |
| SPI_MOSI | 7    | 8     | NC      |
| SPI_MISO | 9    | 10    | NC      |
| SPI_CLK  | 11   | 12    | 3V3     |
| NC       | 13   | 14    | NC      |
| UART_TX  | 15   | 16    | UART_RX |
| I2C_SDA  | 17   | 18    | I2C_SCL |
| NC       | 19   | 20    | NC      |
| NC       | 21   | 22    | NC      |
| NC       | 23   | 24    | NC      |
| NC       | 25   | 26    | NC      |
| NC       | 27   | 28    | 5V      |
| NC       | 29   | 30    | BAT     |
::

## 尺寸图

- [Module Air Quality模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1030/M134-module-airquality.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1030/M134-module-airquality_page_01.png" width="100%">

## 数据手册

- [PMSA003](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/base/PMSA003_cn.pdf)

## 软件开发

### Arduino

- [Module Air Quality Example with Basic](https://github.com/m5stack/M5Stack/tree/master/examples/KIT/PM25)

### Easyloader

| Easyloader                                        | 下载链接                                                                                                               | 备注 |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---- |
| Module Air Quality Example Easyloader with M5Core | [download](<https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Module/PM2.5%20Air%20Quality%20Kit%20(SHT30).exe>) | /    |

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113580544427294&bvid=BV1NA6PYfETi&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/j3Pws5dBzWs?si=zzzRXcMBCwZV7-uR" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
