# 16-Key Capacitive Touch

<span class="product-sku">SKU:U026</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/makey/makey_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/makey/makey_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/makey/makey_03.webp">
</PictureViewer>

## 描述

**16-Key Capacitive Touch** 是一款创意键盘 Unit。该 Unit 的灵感来自一个名为 Makey Makey 的发明套件，它带给用户全新的交互使用概念。将日常物品连接至该 Unit，利用物体的导电性构建一个电路回路，从而模拟键盘输入或是鼠标点击的信号。例如将水果接入回路，当我们触碰水果时，将产生电信号用作控制，基于这样的交互方式能够制作水果钢琴，或是游戏控制器等应用。

该 Unit 通过 PORT A 接口与 M5Core 进行通信，I2C 地址为 0x51.

**使用方法:**

- 1\. 驱动 Unit 上的蜂鸣器发出声音：使用杜邦线 (公对公)，将其一端插入 "GND"，当另一端短接至 Unit 上的键值的时候，蜂鸣器将发出相应的音调.

- 2\. 驱动 M5Core 的扬声器：将 MAKEY Unit 连接至 M5Core 的 PORT A. 并烧录该[案例程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/Makey_NewVersion/Arduino/Makey_new_version).

- 3\. 在 MAKEY Unit 上使用同样的方式进行 "GND" 短接，将驱动 M5Core 发出对应的音调.

## 产品特性

- Arduino Mega328p 控制器
- 内置蜂鸣器
- 内置 16 个音调
- 开发平台: Arduino，UiFlow (Blockly，Python)
- 2 x LEGO 兼容孔

## 包装内容

- 1 x 16-Key Capacitive Touch
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 水果键盘
- 触摸传感器

## 规格参数

| 规格     | 参数           |
| -------- | -------------- |
| 通讯协议 | I2C:0x51       |
| 产品重量 | 7g             |
| 毛重     | 19g            |
| 产品尺寸 | 32 x 24 x 8mm  |
| 包装尺寸 | 67 x 53 x 12mm |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/makey/makey_sch_01.webp" width="80%">

## 管脚映射

### 16-Key Capacitive Touch

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 软件开发

### Arduino

- [Unit Makey 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/MAKEY)

### UiFlow1

- [Unit Makey 测试程序](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/Makey_NewVersion/UIFlow)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/makey/makey_uiflow_01.webp" width="65%">

### 内置固件

- [Unit Makey 内置固件](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/Makey_NewVersion/firmware_328p)

### 通信协议

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/makey/makey_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/makey/makey_03.webp" width="30%" height="30%">

### EasyLoader

| Easyloader                 | 下载链接                                                                                      | 备注 |
| -------------------------- | --------------------------------------------------------------------------------------------- | ---- |
| Unit Makey Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_Makey.exe) | /    |
