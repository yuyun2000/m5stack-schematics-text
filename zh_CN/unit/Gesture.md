# Unit Gesture

<span class="product-sku">SKU:U127</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Gesture/img-9e68c6c6-41f6-4c6c-837b-78d15785399b.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Gesture/img-0a7e858d-ca7b-4ebe-bf00-d669d4aa4c27.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/706/U127-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Gesture/img-b7f9f0d1-68b3-470a-8072-f942cd6ce13e.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Gesture/img-441d6677-53f0-4a56-98a1-8c63fb988678.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Gesture/img-c330684a-d6ec-485e-b392-f8e22b14dfd0.webp">
</PictureViewer>

## 描述

**Unit Gesture**是一款使用 **I2C 通信**接口的 **3D 手势识别**传感器。采用 **PAJ7620U2** 传感器方案，程序默认支持 **9 种手势识别**，最大手势更新频率可达 **240Hz**，具备一定的 **抗环境光干扰**能力。支持自定义单位采样时间，还可根据需求，通过程序算法添加识别手势组合。传感器具备 **稳定性强**，**识别速度快**，**准确率高**，**功耗低** (工作电流仅 2.2mA) 等特点，适用于各种 **非接触式遥控器**，**机器人交互**，**人机互动游戏**，**手势灯光控制**等应用。

- **支持 9 种手势:**

  - **上**，**下**，**左**，**右**，**前**，**后**，**顺时针**，**逆时针**，**快速挥手**

## 产品特性

- PAJ7620U2 手势传感器 / I2C 接口
- 9 种可识别手势
- 识别速度快，准确率高，交互性强
- 支持自定义添加识别手势组合 (需要二次软件开发实现)
- 有效识别距离：5cm-15cm
- 内置红外 LED 和光学元件，具备环境光免疫力
- 开发平台: Arduino、UiFlow

## 包装内容

- 1 x Unit Gesture
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 非接触式遥控器
- 机器人交互
- 人机互动游戏
- 手势灯光控制

## 规格参数

| 规格           | 参数                        |
| -------------- | --------------------------- |
| 通信接口       | I2C 通信 @ 0x73             |
| 手势识别频率   | 典型值: 120Hz，最大 240Hz   |
| 支持手势       | 9 种内置 + 支持软件算法拓展 |
| 有效识别距离   | 5cm-15cm                    |
| R 环境光免疫力 | <100k Lux                   |
| 通信接口       | I2C，addr: 0x73             |
| 工作电流       | 2.2mA                       |
| 产品尺寸       | 32.0 x 24.0 x 8.0mm         |
| 产品重量       | 4.6g                        |
| 包装尺寸       | 138.0 x 93.0 x 9.0mm        |
| 毛重           | 10.0g                       |

## 原理图

<img alt="schematics" src="https://static-cdn.m5stack.com/resource/docs/products/unit/Gesture/img-023620e1-ce53-412b-a928-eb79681e0af6.webp" width="100%" />

## 管脚映射

### Unit Gesture

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img alt="image" width="100%" src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/gesture/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg">

## 结构文件

- [Unit Gesture 结构文件](https://github.com/m5stack/M5_Hardware/tree/master/Products/U127_Unit_Gesture/Structures)

## 数据手册

- [PAJ7620U2 Datasheet](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/gesture/paj7620u2_datasheet.pdf)

## 软件开发

### Arduino

- [Unit Gesture Test Example with M5Core](https://github.com/m5stack/M5Stack/blob/master/examples/Unit/GESTURE_PAJ7620U2/GESTURE_PAJ7620U2.ino)

### UiFlow1

- [Unit Gesture UiFlow1 文档](/zh_CN/uiflow/blockly/unit/gesture)

## EasyLoader

| Easyloader                   | 下载链接                                                                                                                         | 备注 |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---- |
| Unit Gesture Test Easyloader | [download](https://static-cdn.m5stack.com/resource/docs/products/unit/Gesture/ezLoader-b244c14c-9556-4e26-8a6f-f98f3324c02e.exe) | /    |

## 相关视频

- Unit Gesture 案例展示

<video class="video-container" controls><source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/GESTURE_UNIT_VIDEO.mp4" type="video/mp4"></video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=112907912217507&bvid=BV11ZaoeGEE9&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/zur5g9PbNkg?si=ubXvVz6q2B3dAwjg" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
