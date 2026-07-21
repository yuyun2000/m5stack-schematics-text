# Unit RFID2

<span class="product-sku">SKU:U031-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid2/rfid2_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid2/rfid2_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/841/U031-B-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid2/rfid2_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid2/rfid2_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid2/rfid2_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/841/U031-B-weight.jpg">
</PictureViewer>

## 描述

Unit RFID2 是一款基于 13.56MHz 频率的射频识别读写单元。它内置 WS1850S 芯片，遵循 ISO/IEC 14443 Type A/B 标准，可支持 MIFARE、NTAG 等系列 RFID 卡的数据读写。单元通过 I2C 接口通信，读写距离小于 20mm，并采用 LEGO 兼容孔设计，便于集成到创意结构或使用螺丝固定。适用于门禁系统、身份识别、数据记录等多种需要进行信息验证的应用场景。

?>Unit RFID2 相对前代 Unit RFID 仅做出读写 IC 替换 (RC522->WS1850S)，功能上无区别。

## 产品特性

- 核心芯片：WS1850S
- 工作频率：13.56 MHz
- 兼容标准：ISO/IEC 14443 Type A/B
- 通信接口：I2C
- 读写距离：< 20mm
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit RFID2
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 智能家居门禁系统
- 车辆管理
- 智能交通
- 智能书架

## 规格参数

| 规格     | 参数                             |
| -------- | -------------------------------- |
| 读写 IC  | WS1850S                          |
| 工作频率 | 13.56MHz                         |
| 通信接口 | I2C 通信 @ 0x28                  |
| 支持协议 | ISO/IEC 14443 Type A/Type B 协议 |
| 产品尺寸 | 48.0 x 24.0 x 8.0mm              |
| 产品重量 | 5.9g                             |
| 包装尺寸 | 138.0 x 93.0 x 16.0mm            |
| 毛重     | 11.3g                            |

## 原理图

- [Unit RFID2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/841/U031-B-Sch_Unit-RFID_v1.3.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/841/U031-B-Sch_Unit-RFID_v1.3_page_01.png">
</SchViewer>

## 管脚映射

### Unit RFID2

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/rfid2/%E5%8E%9F%E7%90%86%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit RFID2 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U031-B_Unit_RFID2/Structures)

## 数据手册

- [WS1850S](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/rfid2/WS1850S%20QFN-32.PDF)
- [MFRC522](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/MFRC522_en.pdf)

## 软件开发

### Arduino

- [Unit RFID2 Arduino 使用教程](/zh_CN/arduino/projects/unit/unit_rfid)

### UiFlow1

- [Unit RFID UiFlow1 文档](/zh_CN/uiflow/blockly/unit/rfid)

### UiFlow2

- [Unit RFID UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/rfid.html)

### EasyLoader

| Easyloader                | 下载链接                                                                                     | 备注 |
| ------------------------- | -------------------------------------------------------------------------------------------- | ---- |
| Unit RFID Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_RFID.exe) | /    |

## 相关视频

- Unit RFID2 产品介绍以及功能展示

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/841/U031-B-Unit-RFID2-video-ZH.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112868284435128&bvid=BV1a3vPeyEV2&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/T10ITxWbxy4?si=DZgZF5q1MXbigko1" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
