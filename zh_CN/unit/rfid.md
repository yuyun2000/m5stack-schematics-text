# Unit RFID

<span class="product-sku">SKU:U031</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid/rfid_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid/rfid_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid/rfid_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid/rfid_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid/rfid_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid/rfid_06.webp">
</PictureViewer>

## 描述

**Unit RFID** 是一款射频识别 Unit。内置 **MFRC522** 芯片，工作频率为 13.56MHz。支持读卡、写卡、识别、记录、对 RF 卡进行编码和授权等多个功能。利用磁场感应技术，实现进行非接触式双向信息交互，读取感应卡的信息并验证。能够运用在门禁系统、打卡系统、仓库货物进存和小区车辆出入登记等需要进行信息验证的应用场景。

## 产品特性

- 工作频率: 13.56 MHz
- I2C 数据速率：快速模式：最高 400 Kbit/s; 高速模式：最高 3400 Kbit/s
- RC522 收发器缓冲器: 64 bytes
- 支持的协议: ISO14443A，MIFARE and NTAG
- 工作温度: -20-85℃
- 数据保存: > 10 年
- 读写距离: < 20mm
- 开发平台: Arduino，UiFlow (Blockly，Python)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x Unit RFID
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 智能家居门禁系统
- 车辆管理
- 智能交通
- 智能书架

## 规格参数

| 规格     | 参数            |
| -------- | --------------- |
| 通信接口 | I2C 通信 @ 0x28 |
| 产品尺寸 | 48.0 x 24.0 x 8.0mm |
| 产品重量 | 6.0g            |
| 包装尺寸 | 67.0 x 53.0 x 12.0mm |
| 毛重     | 21.0g           |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/rfid/rfid_sch_01.webp" width="80%">

## 管脚映射

### Unit RFID

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 数据手册

- [MFRC522](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/module/MFRC522_en.pdf)
- [WS1850S](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/rfid2/WS1850S%20QFN-32.PDF)

## 软件开发

### Arduino

- [Unit RFID Arduino 使用教程](/zh_CN/arduino/projects/unit/unit_rfid)

### UiFlow1

- [Unit RFID UiFlow1 文档](/zh_CN/uiflow/blockly/unit/rfid)

### EasyLoader

| Easyloader                | 下载链接                                                                                     | 备注 |
| ------------------------- | -------------------------------------------------------------------------------------------- | ---- |
| Unit RFID Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_RFID.exe) | /    |

## 相关视频

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
