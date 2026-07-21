# Unit QRCode

<span class="product-sku">SKU:U173</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-QRCode/img-aa3b7064-8e0c-43c7-807e-40cea135ffa7.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-QRCode/img-202a32b2-2826-4989-8e7b-b864cbc8afc9.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/770/U173-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-QRCode/img-49bd82e0-0ccc-40a2-b9a3-74dfba8a09c4.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-QRCode/img-7be358eb-fa74-4370-954c-1779896889e9.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-QRCode/img-932bfc18-c3a5-4c2f-91e2-d689778c18e0.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-QRCode/img-1b47187f-e3d7-47df-84f2-8f46f145918b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-QRCode/img-0e90ee2d-75b0-467d-a4c7-f104c284a74c.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-QRCode/img-53aeac81-c8d7-4146-a9be-930c9985ddb5.webp">
</PictureViewer>

## 描述

**Unit QRCode** 是一款一体化一维 / 二维码扫描单元，内部集成了 640x480 分辨率的 CMOS 二维码采集引擎和总线转化 MCU (STM32F030)。通过设备侧拨动开关，能实现 I2C 和 UART 通讯接口的切换。采集引擎支持市场上主流的 3 类二维码和 14 类一维码，并预留可升级固件接口。该单元带有扫描触发按钮，内置蜂鸣器以及补光 LED，在不同状态下提供音效提示，红色 LED 用于辅助对焦与瞄准功能。可通过程序设置，调整为自动连续触发或手动触发模式。适用于物流、零售、制造等领域。

## 产品特性

- STM32F030F4P6@32 位 ARM Cortex-M0 处理器
- 支持 3 类二维码和 14 类一维码
- 可升级固件
- 内置 I2C 和 UART 通讯接口切换开关
- 内置蜂鸣器音效提示
- 内置照明 LED
- 高分辨率成像
- 对焦与瞄准功能

## 包装内容

- 1 x Unit QRCode
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 物流
- 零售
- 制造

## 规格参数

| 规格           | 参数                                                                                                                                      |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| MCU            | STM32F030F4P6@32 位 ARM Cortex-M0 处理器                                                                                                  |
| 传感器         | 640x480 CMOS@M14 模组                                                                                                                     |
| 照明           | 白光 LED                                                                                                                                  |
| 对焦瞄准       | 红光 LED                                                                                                                                  |
| 识读二维码类型 | PDF417，QR Code，Data Matrix                                                                                                              |
| 识读一维码类型 | Code11, Code39, Code93, Code128, EAN-13, EAN-8, UPC-A, UPC-E, <br>Codabar, Interleaved 2 of 5, Matrix 2 of 5, Industrial 2 of 5, MSI, GS1 |
| 识别读取精度   | ≥5mil                                                                                                                                     |
| 打印对比度     | ≥ 20%                                                                                                                                     |
| 扫描角度       | 仰角 ±55°，偏角 ±55° (加上折射镜头，可改变扫描角度)                                                                                       |
| 通信接口       | I2C 通信 @ 0x21                                                                                                                           |
| 外壳材质       | Plastic (PC)                                                                                                                              |
| 产品尺寸       | 65.8 x 27.2 x 18.4mm                                                                                                                      |
| 产品重量       | 14.0g                                                                                                                                     |
| 包装尺寸       | 138.0 x 93.0 x 19.4mm                                                                                                                     |
| 毛重           | 19.4g                                                                                                                                     |

## 操作说明

<img alt="schematics" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-QRCode/7fe612c4547c8c90bc1dac6afb17cc6.png" width="50%" />

> 安装折射头扫描头可以改变扫描的角度，如上图

## 原理图

- [Unit QRCode 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/627/SCH_UNIT_QRCODE_V1.0.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/627/SCH_UNIT_QRCODE_V1.0_sch_01.png">
</SchViewer>

## 管脚映射

### Unit QRCode I2C Mode

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### Unit QRCode UART Mode

::grove-table
| HY2.0-4P | Black | Red | Yellow  | White   |
| -------- | ----- | --- | ------- | ------- |
| PORT.C   | GND   | 5V  | UART_RX | UART_TX |
::

### STM32 Trig Button

| STM32  | PB1  |
| ------ | ---- |
| BUTTON | TRIG |

## 尺寸图

<img alt="module size" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Unit-QRCode/img-3bc3b2bd-e524-40fa-93e9-e82489c050c3.jpg" width="100%" />

## 数据手册

- [QRCode 模块数据手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1163/M14-Pro_CN_2025_07_21_15_21_26.pdf)

## 软件开发

### Arduino

- [Unit QRCode I2C Mode 测试程序](https://github.com/m5stack/M5Unit-QRCode/tree/main/example/i2c_mode)
- [Unit QRCode UART Mode 测试程序](https://github.com/m5stack/M5Unit-QRCode/tree/main/example/uart_mode)

### UiFlow1

- [Unit QRCode UiFlow1 文档](/zh_CN/uiflow/blockly/unit/qrcode)

### UiFlow2

- [Unit QRCode UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/qrcode.html)

### 内置固件

- [Unit QRCode 内置固件](https://github.com/m5stack/M5Unit-QRCode-Internal-FW)

### 通信协议

- [Unit QRCode 控制指令](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/770/Unit-QRCode-Protocol-CN.pdf)
- [Unit QRCode 识读模块用户手册](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1163/ZBarcode_Scanner_User_Guide-2.5.3-CN.pdf)
- [Unit QRCode I2C 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/770/UnitQrcode.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/770/UnitQrcode_page_01.png">

## 相关视频

- Unit QRCode 功能介绍

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/Unit-QRCode/U173%20Unit-QRCode%20%E8%A7%86%E9%A2%91.mp4" type="video/mp4"></video>

- UiFlow2 Unit QRCode

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112947573690211&bvid=BV1wveFeSESS&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/nbZlpORTPmE?si=qjte735j_XtpvQdW" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
