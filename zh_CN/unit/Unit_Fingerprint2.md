# Unit Fingerprint2

<span class="product-sku">SKU:U203</span>

<PictureViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-mainpictures_01.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-mainpictures_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-mainpictures_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-mainpictures_04.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-mainpictures_05.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-mainpictures_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-mainpictures_07.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-mainpictures_08.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-mainpictures_09.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-mainpictures_10.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-weight.jpg">
</PictureViewer>

## 描述

Unit Fingerprint2 是一款高性能指纹识别传感器单元，内部集成 STM32 核心主控与 A - K323CP 一体化指纹识别模组，采用半导体电容式传感器，具备指纹采集、特征提取、注册、比对、存储、检索等多项功能。模块内置指纹识别算法，能适配干湿手指等不同状况。用户指纹数据管理灵活，数据安全性高，且具备快速搜索和定位功能。该单元采用 UART 通讯接口，便于与各类主控平台集成，集成七彩 RGB LED 灯环和电源指示灯用于交互状态提示。适用于智能门锁、门禁考勤、身份认证、金融支付及小型安防等多种场景的快速开发与集成。

## 产品特性

- 集成 STM32 核心主控
- 高分辨率的电容式指纹传感器，具有高精度识别能力
- 指纹容量 100 枚
- 自适应对干、湿手指进行处理
- 指纹管理、精确比对、搜索功能
- 自带七彩灯圈，支持七种灯光（工作状态）指示
- 开发平台
  - UiFlow2
  - Arduino IDE
  - PlatformIO

## 包装内容

- 1 x Unit Fingerprint2
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 智能门锁
- 门禁考勤
- 身份认证
- 金融支付
- 小型安防

## 规格参数

| 规格             | 参数                                                           |
| ---------------- | -------------------------------------------------------------- |
| MCU              | STM32G031G8U6                                                  |
| 指纹传感器模组   | A-K323CP                                                       |
| 指纹传感器分辨率 | 508 dpi                                                        |
| 图像像素         | 80 \* 208                                                      |
| 获取图像大小     | 8230 Bytes （80 \* 208 / 2 = 8320，每像素 4 bit）              |
| 指纹容量         | 100 枚                                                         |
| 指纹数据大小     | 7262 Bytes / 枚                                                |
| 通讯方式         | UART 115200bps @ 8N1                                           |
| 功耗             | 工作模式：呼吸灯开 40mA；呼吸灯关 37.25mA<br>休眠模式：14.11mA |
| 产品尺寸         | 40.0 x 24.0 x 8.0mm                                            |
| 产品重量         | 6.1g                                                           |
| 包装尺寸         | 138.0 x 93.0 x 11.0mm                                          |
| 毛重             | 11.6g                                                          |

## 原理图

- [Unit Fingerprint2 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/SCH_Unit_Fingerprint2_SCH_MAIN_V1.0_20250822_2025_09_22_14_45_23.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/SCH_Unit_Fingerprint2_SCH_MAIN_V1.0_20250822_2025_09_22_14_45_23_page_01.png">
</SchViewer>

## 管脚映射

### Unit Fingerprint2

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

- [Unit Fingerprint2 模型尺寸PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203_Model_size_UNIT-Fingerprint2.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-MODEL-SIZE-unit-2sma_page_01.png" width="100%">

## 结构文件

- [Unit Fingerprint2 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U203_Unit_Fingerprint2/Structures)

## 软件开发

### Arduino

- [Unit Fingerprint2 Arduino 驱动库](https://github.com/m5stack/M5Unit-Fingerprint2)
- [Unit Fingerprint2 Arduino 快速上手](/zh_CN/arduino/projects/unit/unit_fingerprint2)

### UiFlow2

- [Unit Fingerprint2 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/fingerprint2.html)

### 内置固件

- [Unit Fingerprint2 内置固件](https://github.com/m5stack/M5Unit-Fingerprint2-Internal-FW)

### 通信协议

- [Unit Fingerprint2 串口通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/Unit-Fingerprint-Protocol-CN-V1.0.pdf)

## 相关视频

- Unit Fingerprint2 产品介绍以及功能展示

<video class="video-container" controls poster="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/zh-U203-video-cover.jpg"><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/zh-U203-Unit-Fingerprint2-video.mp4" type="video/mp4"> </video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=115388608218204&bvid=BV16XWEzAEkx&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/89Uv8vQ9HSY?si=sm8hZkMxsjCvqkc1" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
