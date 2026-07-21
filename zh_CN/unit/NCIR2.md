# Unit NCIR2

<span class="product-sku">SKU:U150</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/NCIR2/img-2eb52d27-8e6d-4673-94fd-055628c26a53.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/NCIR2/img-7182d3fa-862e-47e6-abbe-d1bb3c88c73d.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/NCIR2/img-7cc7cd6a-3efd-42a5-8ef4-471d9cf519fa.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/NCIR2/img-77bc1f8d-bedb-4081-b74a-000d5d6e36d5.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/NCIR2/img-a8932041-3ca1-45eb-89a4-0c3a2763f339.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/NCIR2/img-53c5aa20-4ecd-411d-af33-57af9896c06f.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/NCIR2/img-fd84b907-a693-4934-8135-08b21885b8d7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/NCIR2/img-bd85f23f-8075-447c-85b0-27dffaf35dfc.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/NCIR2/img-162ae4fb-2013-42e2-8321-0c136d29c71f.webp">
</PictureViewer>

## 描述

**Unit NCIR2** 是一款搭载数据处理 MCU 的 MLX90614 非接触式红外单点测温单元，测温范围 -70℃ ~ 380℃，MCU 采用 STM32，通过数据处理能实现高、低温告警功能。板上集成了蜂鸣器、RGB 指示灯、一个功能按键和一个复位按键，采用 I2C 与上位机通信。该产品可与上位机一并使用，也能单独使用，适合用于温度测量及异常告警等场合。

## 产品特性

- STM32F030F4P6
- MLX90614 红外 (IR) 传感器
- GROVE I2C/HY2.0-4P 接口
- 编程平台：Arduino、UiFlow
- 两个乐高兼容孔

## 包装内容

- 1 x Unit NCIR2
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 高精度非接触式温度测量
- 移动检测
- 智能家居

## 规格参数

| 规格               | 参数                 |
| ------------------ | -------------------- |
| MCU                | STM32F030F4P6        |
| 传感器             | MLX90614ESF-BAA      |
| 通信接口           | I2C 通信 @ 0x5A      |
| 被测量对象温度范围 | -70°C ~ 380°C        |
| 传感器工作温度     | -40°C ~ 125˚C        |
| Unit 工作温度      | 0°C ~ 40°C           |
| 测量精度           | ±0.5°C               |
| 编程平台           | Arduino，UiFlow      |
| 产品尺寸           | 48.0 x 24.0 x 8.0mm  |
| 产品重量           | 7.3g                 |
| 包装尺寸           | 138.0 x 93.0 x 9.0mm |
| 毛重               | 12.8g                |

## 原理图

- [Unit NCIR2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/604/Sch_UNIT-NCIR2.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/604/Sch_UNIT-NCIR2_sch_01.png">
</SchViewer>

## 管脚映射

### Unit NCIR2

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/NCIR2/img-2917ac6d-78f5-414a-a3a5-dc3e10b4068a.png" width="100%" />

## 数据手册

- [STM32F030F4P6 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/STM32F030F4P6.PDF)
- [MLX90614 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/MLX90614-Datasheet-Melexis_en.pdf)

## 软件开发

### Arduino

- [Unit NCIR2 Arduino 驱动库](https://github.com/m5stack/M5Unit-NCIR2)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/NCIR2/arduinoCase-1665570359798微信图片_20221012180333.png" width="100%"/>

### UiFlow1

- [Unit NCIR2 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/ncir2)

### UiFlow2

- [Unit NCIR2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/ncir2.html)

### 内置固件

- [Unit NCIR2 内置固件](https://github.com/m5stack/M5Unit-NCIR2-Internal-FW)

### 通信协议

- [Unit NCIR2 I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/739/NCIR-STM32.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/739/NCIR-STM32_page_01.png" width="100%"/>

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113123163964283&bvid=BV1Jp4HeQEs9&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/bqafQFzpd_M?si=E8m_RGyNtrMCjhDf" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
