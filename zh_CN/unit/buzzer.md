# Unit Buzzer

<span class="product-sku">SKU:U132</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/buzzer/buzzer_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/buzzer/buzzer_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/buzzer/buzzer_03.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/735/U132-package.jpg">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/buzzer/buzzer_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/buzzer/buzzer_06.webp">
</PictureViewer>

## 描述

**Unit Buzzer** 是一款基于无源蜂鸣器的高效声音反馈单元。它通过外部 PWM 方波信号驱动振膜振动发声，可实现蜂鸣报警与自定义提示音播放。该单元采用 Grove HY2.0-4P 接口通信，内置带保护电路的 NPN 三极管驱动，支持 4KHz 推荐驱动频率与 72dB 清晰声压，并采用 LEGO 兼容孔设计，便于灵活对接 LEGO 结构或使用螺丝固定。适用于报警系统、用户交互提示、智能设备反馈等应用场景。

## 产品特性

- 蜂鸣器类型：无源蜂鸣器（需外部 PWM 驱动）
- 声压等级：72dB（10cm 距离，5V 供电）
- 驱动方式： PWM 方波信号（严禁直流高电平）
- 推荐频率：4KHz
- 响应速度：快速启动 / 停止
- 通信接口：Grove HY2.0-4P
- 2 x LEGO 兼容孔
- 开发平台
  - UiFlow1
  - UiFlow2
  - Arduino IDE

## 包装内容

- 1 x Unit Buzzer
- 1 x HY2.0-4P Grove 连接线 (5cm)

## 应用场景

- 蜂鸣报警 / 提示

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 驱动频率 | 4KHz 1/2duty 方波    |
| 功耗     | 5V@86mA              |
| 产品尺寸 | 24.0 x 24.0 x 8.0mm  |
| 产品重量 | 3.3g                 |
| 包装尺寸 | 138.0 x 93.0 x 9.0mm |
| 毛重     | 6.8g                 |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/buzzer/buzzer_sch_01.webp" width="80%">

## 管脚映射

### Unit Buzzer

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | Signal | /     |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/buzzer/moudle_zize.jpg" width="80%">

## 软件开发

### Arduino

```cpp

#include <Arduino.h>

#define buzzer_pin 26
int freq = 4000;
int ledChannel = 0;
int resolution = 10;

void setup() {
  ledcSetup(ledChannel, freq, resolution);  //Sets the frequency and number of counts corresponding to the channel.  设置通道对应的频率和计数位数
  ledcAttachPin(buzzer_pin, ledChannel); //Binds the specified channel to the specified I/O port for output.  将指定通道绑定到指定 IO 口上以实现输出
  ledcWrite(ledChannel, 512);  //Output PWM.  输出PWM
}

void loop() {
    ledcWrite(ledChannel, 512);  //Output PWM.  输出PWM
    delay(3000);
    ledcWrite(ledChannel, 0);  //Output PWM.  输出PWM
    delay(3000);
}

```

### UiFlow1

- [Unit Buzzer UiFlow1 文档](/zh_CN/uiflow/blockly/unit/buzzer)

### UiFlow2

- [Unit Buzzer UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/buzzer.html)

## 相关视频

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113423174075111&bvid=BV1wADnYFEip&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/L_josLPafDI?si=MiAHO6by_7G_4IRH" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
