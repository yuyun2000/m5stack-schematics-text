# Unit Finger

<span class="product-sku">SKU:U008</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/finger/finger_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/finger/finger_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/finger/finger_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/finger/finger_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/finger/finger_06.webp">
</PictureViewer>

## 描述

**Unit Finger**是一款指纹识别传感器。内部集成 FPC1020A 电容式指纹识别模组，具备多指纹录入、图像处理、特征值提取、指纹比对、搜索等功能。

采用 UART 通信协议、紧凑的外观设计、与低功耗能带给项目可靠的安全级别的同时，提供最佳的用户便利性。如果你想要为你的项目添加生物指纹识别功能，并希望其具备稳定可靠的添加、验证、管理机制，**Unit Finger**是一个不错的解决方案。

**使用时，请将该 Unit 连接到 PORT C，它将通过 UART 协议与 M5Core 进行通信**

UART 参数设置:

- 波特率 (**默认: 19200bps**)
- 起始位 (1 bit)
- 停止位 (1 bit)
- 校验位 (无)

## 产品特性

- 采用电容式面阵式半导体指纹传感器
- 传感器每个像素拥有 256 灰度级的像素质量
- 1:N 识别 及 1:1 验证功能
- 支持手指 360 旋转识别
- 指纹比对、搜索功能

## 包装内容

- 1 x Unit Finger
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 指纹考勤机
- 指纹储物柜

## 规格参数

| 规格       | 参数                 |
| ---------- | -------------------- |
| 指纹容量   | 150                  |
| 安全等级   | 0-9，默认 5          |
| 输出格式   | 用户名、图像、特征值 |
| 特征值大小 | 193Byte              |
| 通讯方式   | UART (9600-115200)   |
| 工作温度   | -10°C ~ 60°C         |
| 相对湿度   | 20%-80%              |
| 产品尺寸   | 48.0 x 24.0 x 8.0mm  |
| 产品重量   | 7.7g                 |
| 包装尺寸   | 138.0 x 93.0 x 9.0mm |
| 毛重       | 12.9g                |

## 原理图

- [Unit Finger 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/717/U008_UNIT_FINGER_SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/717/U008_sche.png">
</SchViewer>

## 管脚映射

### Unit Finger

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

## 尺寸图

<img alt="module size" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/finger/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="100%" />

## 结构文件

- [Unit Finger 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U008_Unit_Finger/Structures)

## 数据手册

- 通信协议 **[FINGER 串口通信协议](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/biovo_fingerprint_Protocol.pdf)**

- 数据手册 **[FPC1020A](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/1020A_datasheet_cn.pdf)**

## 软件开发

### Arduino

- [Unit Finger Example with M5Atom](https://github.com/m5stack/M5-FPC1020A/blob/master/examples/Unit_Finger_M5Atom/Unit_Finger_M5Atom.ino)
- [Unit Finger Example with M5Core](https://github.com/m5stack/M5-FPC1020A/blob/master/examples/Unit_Finger_M5Core/Unit_Finger_M5Core.ino)
- [Unit Finger Example with M5Core2](https://github.com/m5stack/M5-FPC1020A/blob/master/examples/Unit_Finger_M5Core2/Unit_Finger_M5Core2.ino)
- [Unit Finger Example with M5StickC](https://github.com/m5stack/M5-FPC1020A/blob/master/examples/Unit_Finger_M5StickC/Unit_Finger_M5StickC.ino)
- [Unit Finger Example with M5StickCPlus](https://github.com/m5stack/M5-FPC1020A/blob/master/examples/Unit_Finger_M5StickCPlus/Unit_Finger_M5StickCPlus.ino)

### UiFlow1

- [Unit Finger UiFlow1 文档](/zh_CN/uiflow/blockly/unit/finger)

### UiFlow2

- [Unit Finger UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/finger.html)

### EasyLoader

| Easyloader                  | 下载链接                                                                                                                             | 备注 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| Unit Finger Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_Finger_UNIT_With_M5Core.exe) | /    |

## 相关视频

- FINGER UNIT 使用案例：按下左侧按键进入录入指纹模式。按下中间按键进入指纹识别模式.

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/Finger_UNIT.mp4" type="video/mp4">
</video>

- **FINGER 的演示**

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201901/Fingerprint%20Unit.mp4" type="video/mp4">
</video>

- **UIflow Use**

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113123163964438&bvid=BV1Ep4HeQE92&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/UVnhipDAD3k?si=W-TPg5fI2-17S3_i" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
