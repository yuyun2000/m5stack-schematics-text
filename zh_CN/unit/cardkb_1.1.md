# Unit CardKB v1.1

<span class="product-sku">SKU:U035-B</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/cardkb_1.1/cardkb_1.1_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/cardkb_1.1/cardkb_1.1_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/806/U035-B-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/cardkb_1.1/cardkb_1.1_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/cardkb_1.1/cardkb_1.1_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/cardkb_1.1/cardkb_1.1_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/cardkb_1.1/cardkb_1.1_06.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/806/U035-B-weight.jpg">
</PictureViewer>

## 描述

**Unit CardKB v1.1**是一款卡片尺寸的 QWERTY **50 键** PCB 矩阵键盘，使用 **ATMega8A** 作为编码 MCU，输出接口为 **I2C**。板载 1 颗 **RGB-LED** 以显示键盘状态。

## 产品特性

- 全键盘输入，多种按键组合.
- HY2.0-4P 接口，支持 [UiFlow](http://flow.m5stack.com) 、 [Arduino](http://www.arduino.cc)

## 包装内容

- 1 x Unit CardKB v1.1
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- M5Stack Core 的键盘外设

## 规格参数

| 规格     | 参数                  |
| -------- | --------------------- |
| MCU      | ATMega8A              |
| 键位数量 | 50                    |
| RGB LED  | 1 颗                  |
| 通信接口 | I2C 通信 @ 0x5F       |
| 产品尺寸 | 88.0 x 54.0 x 5.0mm   |
| 产品重量 | 14.3g                 |
| 包装尺寸 | 170.0 x 120.0 x 7.0mm |
| 毛重     | 18.0g                 |

## 操作说明

- **按下单个按键**，键盘将输出第一键值 (字母键值则输出小写形式) . 例如，按下 "Q"，键盘将输出 "q" (小写形式) .

- **Sym+key**，键盘将输出第二键值。例如，单击 "Sym" 后，按下 "Q"，键盘将输出 "{". 双击 "Sym" 锁定功能，之后按下的任意按键都将输出第二键值。再次双击 "Sym" 进行解锁.

- **Shift+key**，键盘将输出字母的大写形式。例如，单击 "Shift" 后，按下 "Q"，键盘将输出 "Q" (大写形式) . 双击 "Shift" 锁定功能，之后按下的任意按键都将输出大写形式，再次双击 "Shift" 进行解锁.

- **Fn+key (自定义功能键组合)** ，键盘将输出第三键值。你可以自定义按下的按键其对应的功能.

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/cardkb/cardkb_02.webp" width="80%">

## 管脚映射

### Unit CardKB v1.1

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

### ATMega8A ISP 下载接口 Pin 脚定义

<img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat-cardkb/mega328_isp_sch_01.webp" width="30%" height="30%">

## 尺寸图

[Unit CardKB v1.1模型尺寸 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/806/cardkeyboard_v1_1.pdf)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/806/cardkeyboard_v1_1_page_01.png" width="100%">

## 软件开发

### Arduino

- [Unit CardKB v1.1 Example with M5Core](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/CardKB)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/cardkb/cardkb_arduino_01.webp">

### UiFlow1

- [Unit CardKB v1.1 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/cardkb)

### UiFlow2

- [Unit CardKB v1.1 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/cardkb.html)

### 内置固件

- [Unit CardKB v1.1 内置固件](https://github.com/m5stack/M5-ProductExampleCodes/tree/master/Unit/CARDKB/firmware_328p/CardKeyBoard)

### 通信协议

- [Unit CardKB v1.1 通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/806/Unit_CardKB_v1_1_User_Manual_CN.pdf)

### EasyLoader

| Easyloader                      | 下载链接                                                                                       | 备注 |
| ------------------------------- | ---------------------------------------------------------------------------------------------- | ---- |
| Unit CardKB example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_CardKB.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Blog/Twitch201901/M5stack%20Cardkb.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112907912220450&bvid=BV1yZaoeGE4u&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/m1xtyyHLKOk?si=ORcji8GuwF3VAril" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>