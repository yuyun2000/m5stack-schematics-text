# Unit Vibrator

<span class="product-sku">SKU:U059</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/vibrator/vibrator_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/vibrator/vibrator_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/758/U059-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/vibrator/vibrator_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/vibrator/vibrator_06.webp">
</PictureViewer>

## 描述

**Unit Vibrator** 是一款基于 N20 电机与金属偏心轮的高性能震动反馈模块。它采用高速旋转的偏心轮产生物理震动，实现精准的触觉反馈功能。该单元通过 Grove HY2.0-4P 接口通信，支持 GPIO 数字控制和 PWM 脉宽调制，可通过调节 PWM 占空比实现震动强度的无级调节。模块内置 N-Channel MOSFET 低侧开关驱动电路，具有 8800 RPM 转速和 10KHz 推荐 PWM 频率，并采用 LEGO 兼容孔设计，可灵活集成到各种结构中进行安装。适用于电子产品信息提示、触摸反馈系统、用户交互反馈等多种需要触觉反馈的应用场景。

## 产品特性

- 电机类型：N20 直流电机 + 金属偏心轮
- 旋转方向：单向旋转（不支持反向制动）
- 电机转速：8800 RPM（无负载）
- 控制方式：GPIO 数字控制 / PWM 脉宽调制
- 响应速度：快速启动 / 停止（依赖机械惯性）
- 通信接口：Grove HY2.0-4P
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit Vibrator
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 触摸反馈
- 震动信息提示

## 规格参数

| 规格     | 参数                                    |
| -------- | --------------------------------------- |
| 功耗     | PWM Freq: 10KHz，Duty: 50%，5V@424.35mA |
| 产品尺寸 | 32.0 x 24.0 x 8.0mm                     |
| 产品重量 | 10.0g                                   |
| 包装尺寸 | 138.0 x 93.0 x 14.0mm                   |
| 毛重     | 15.8g                                   |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unit_fan/unit_fan_sch_01.webp" width="50%" height="50%">

## 管脚映射

### Unit Vibrator

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | DIN    | NC    |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/vibrator/model%20size.png" width="100%">

## 软件开发

### Arduino

- [Unit Vibrator 测试程序](https://github.com/m5stack/M5Stack/tree/master/examples/Unit/VIBRATOR)

### UiFlow1

- [Unit Vibrator UiFlow1 文档](/zh_CN/uiflow/blockly/unit/vibrator)

### UiFlow2

- [Unit Vibrator UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/vibrator.html)

### EasyLoader

| Easyloader                        | 下载链接                                                                                         | 备注 |
| --------------------------------- | ------------------------------------------------------------------------------------------------ | ---- |
| Unit Vibrator Example with M5Core | [download](https://m5stack.oss-cn-shenzhen.aliyuncs.com/EasyLoader/Unit/EasyLoader_VIBRATOR.exe) | /    |

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Vibrator.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113269813675113&bvid=BV1Rn2EYNEvw&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/EjJqyg11tVA?si=FI84gAKhALleaIJw" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
