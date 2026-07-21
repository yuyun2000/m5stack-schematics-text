# Unit Joystick v1.1

<span class="product-sku">SKU:U024-C</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick_1.1/joystick_1.1_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick_1.1/joystick_1.1_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/799/U024-C-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick_1.1/joystick_1.1_05.webp">
</PictureViewer>

## 描述

**Unit Joystick v1.1** 是一款摇杆控制输入单元，采用 I2C 通信接口，支持三轴控制信号输入 (X / Y 轴偏移模拟量输入，Z 轴按键数字量输入)。适用于游戏 / 机器人控制等应用场景。

## 产品特性

- 三轴输入:
  - X/Y 轴偏移模拟量输入
  - Z 轴按键数字量输入
- 2 x LEGO 兼容孔
- 开发平台: Arduino，UiFlow (Blockly，Python)

## 包装内容

- 1 x Unit Joystick v1.1
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 游戏控制器
- 机器人远程控制

## 规格参数

| 规格              | 参数                  |
| ----------------- | --------------------- |
| 主控 MCU          | MEGA8A                |
| 通信接口          | I2C 通信 @ 0x52       |
| X、Y 轴偏移输出值 | 0-255                 |
| Z 轴按键输出值    | 0/1                   |
| 产品尺寸          | 48.0 x 24.0 x 32.0mm  |
| 产品重量          | 11.0g                 |
| 包装尺寸          | 138.0 x 93.0 x 25.0mm |
| 毛重              | 27.0g                 |

## 原理图

- [Unit Joystick v1.1 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/799/U024-C_UNIT_JOYSTICK_SCHE.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/799/U024-C_UNIT_JOYSTICK_SCHE_page_01.png">
</SchViewer>

## 管脚映射

### Unit Joystick v1.1

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/799/U024-C_Model_Size.png" width="100%">

## 软件开发

### Arduino

- [Unit Joystick v1.1 Get Value Example](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/JOYSTICK)

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/joystick_1.1/joystick_1.1_07.webp">

### UiFlow1

- [Unit Joystick v1.1 UiFlow1 文档](/zh_CN/uiflow/blockly/unit/joystick)

### UiFlow2

- [Unit Joystick v1.1 UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/joystick.html)

### 通讯协议

- 协议类型 I2C
- I2C Address: **0x52**

> JOYSTICK REG 0x52

| REG  | len | description  | return values                                     |
| :--: | :-: | :----------- | :-----------------------------------------------: |
| 0x52 | 3   | 读取摇杆状态 | \[0] X VALUE<br/>\[1] Y VALUE<br/>\[2] BTN STATUS |

### EasyLoader

| Easyloader                         | 下载链接                                                                                                                               | 备注 |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Joystick v1.1 Test Easyloader | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Windows/UNIT/For%20M5Core/EasyLoader_Joystick_UNIT_With_M5Core.exe) | /    |

### 相关视频

- 显示摇杆 XY 数据及按钮状态.

<video id="example_video" controls>
  <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/Joystick_UNIT.mp4" type="video/mp4">
</video>

- UiFlow2 Joystick Unit

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113026929787677&bvid=BV1MEsLeVEwC&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/F2jBH8hb-kI?si=AeWqTQ71scoCQB25" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
