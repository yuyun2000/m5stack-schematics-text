# Hat Finger

<span class="product-sku">SKU:U074</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-finger/hat-finger_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-finger/hat-finger_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-finger/hat-finger_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-finger/hat-finger_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-finger/hat-finger_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-finger/hat-finger_06.webp">
</PictureViewer>

## 描述

**Hat Finger**是一款指纹识别传感器。 内部集成 FPC1020SC 电容式指纹识别模组，具备多指纹录入、图像处理、特征值提取、指纹比对、搜索等功能。
采用 UART 通信协议、紧凑的外观设计、与低功耗能带给项目可靠的安全级别的同时，提供最佳的用户便利性。如果你想要为你的项目添加生物指纹识别功能，并希望其具备稳定可靠的添加、验证、管理机制那么**Hat Finger** 是一个不错的解决方案。

UART 参数设置:

- 波特率 (默认: 19200bps)
- 起始位 (1 bit)
- 停止位 (1 bit)
- 校验位 (无)

## 产品特性

- 指纹容量: 150
- 采用电容式面阵式半导体指纹传感器
- 传感器每个像素拥有 256 灰度级的像素质量
- 最小存储条件下实现指纹数据的登记及比对：指纹模板为 193 字节
- 1:N 识别 及 1:1 验证功能
- 支持手指 360 旋转识别
- 可适当调节的安全等级 0-9, 默认等级 5
- 输出格式：用户名、图像、特征值
- 特征值大小: 193Byte
- 通讯接口: UART
- 通讯波特率: 9600-115200 (默认为 19200)
- 工作温度: -10° - 60°
- 相对湿度: 20% - 80%

## 包装内容

- 1 x Hat Finger

## 应用场景

- 指纹考勤
- 替代密码认证
- 身份识别

## 规格参数

| 规格     | 参数           |
| -------- | -------------- |
| 产品重量 | 14g            |
| 毛重     | 26g            |
| 产品尺寸 | 24 x 65 x 20mm |
| 包装尺寸 | 75 x 46 x 29mm |

## 原理图

- Hat Finger Schematics

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-finger/hat-finger_sch_01.webp" width="50%" height="50%">

- [Hat Finger 总体设计框图](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/869/hatfinger.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/869/hatfinger_page_01.webp">s
</SchViewer>

## 数据手册

- [FPC1020A](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/hat/1020A_datasheet_cn.pdf)

## 软件开发

### Arduino

- [Hat Finger - with M5StickC](https://github.com/m5stack/M5-FPC1020A/blob/master/examples/Hat_Finger_M5StickC/Hat_Finger_M5StickC.ino)
- [Hat Finger - with M5StickC-Plus](https://github.com/m5stack/M5-FPC1020A/blob/master/examples/Hat_Finger_M5StickCPlus/Hat_Finger_M5StickCPlus.ino)

### UiFlow1

- [Hat Finger UiFlow1 文档](/zh_CN/uiflow/blockly/hat/finger)

### UiFlow2

- [Hat Finger UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/hats/finger.html)

### 通信协议

- [FINGER 串口通信协议](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/biovo_fingerprint_Protocol.pdf)

### Easyloader

| Easyloader            | 下载链接                                                                                                  | 备注 |
| --------------------- | --------------------------------------------------------------------------------------------------------- | ---- |
| Hat Finger Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/HAT/EasyLoader_Finger_HAT.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/HAT/FINGER-HAT.mp4" type="video/mp4" >
</video>
