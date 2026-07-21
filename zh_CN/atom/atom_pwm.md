# Atom PWM

<span class="product-sku">SKU:K065</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_pwm/atom_pwm_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_pwm/atom_pwm_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_pwm/atom_pwm_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_pwm/atom_pwm_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_pwm/atom_pwm_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_pwm/atom_pwm_06.webp">
</PictureViewer>

## 描述

**Atom PWM** 是一款单通道 PWM 可调直流驱动器，内置的 MOSFET 负载能力可达 12V@100W ，适用于大功率直流电机 PWM 调速以及工业发热丝控制等应用。使用 Atom-Lite 作为核心控制器 (内置 ESP32) ，有着较广的 PWM 动态调节范围 (例：频率为 5 kHz 的情况下，占空比调节范围 0-100%，分辨率可达 13bit) ，结合内置的 WIFI 功能，还能够轻松实现远程控制。支持 UiFlow 图形化编程，可轻松配置信号输出与功能拓展。

## 产品特性

- 单通道低延时 PWM 信号输出
- 大功率 MOSFET，输出能力 12V@100W
- 内置 DC-DC (12V->5V) 转换电路
- 安装方便，操作简单
- 一体化设计，自带保护外壳
- 开发平台：Arduino、UiFlow

## 包装内容

- 1 x Atom-Lite
- 1 x Atomic PWM Base
- 1 x M2 内六角扳手
- 1 x M2\*8 杯头机械牙螺丝
- 1 x HT3.96-4P 端子
- 1 x TYPE-C USB 数据线 (20cm)

## 应用场景

- 直流电机控制
- 灯光控制
- 发热丝控制
- 直流负载

## 规格参数

| 规格         | 参数           |
| ------------ | -------------- |
| 驱动芯片     | EG27324        |
| MOSFET       | FDD8447L       |
| 最大输出功率 | 100W           |
| 输入电压范围 | DC 12V-24V     |
| 驱动通道数   | 1              |
| 电源指示灯   | 红色           |
| 产品尺寸     | 24 x 48 x 18mm |
| 产品重量     | 28.9g          |
| 包装尺寸     | 54 x 54 x 20mm |
| 毛重         | 37.3g          |

## 操作说明

### 常用频率与分辨率

| LEDC 时钟源       | LEDC 输出 (PWM) 频率 | 分辨率           |
| ----------------- | -------------------- | ---------------- |
| APB_CLK (80 MHz)  | 1 kHz                | 1/65536 (16 bit) |
| APB_CLK (80 MHz)  | 5 kHz                | 1/8192 (13 bit)  |
| APB_CLK (80 MHz)  | 10 kHz               | 1/4096 (12 bit)  |
| RTC8M_CLK (8 MHz) | 1 kHz                | 1/4096 (12 bit)  |
| RTC8M_CLK (8 MHz) | 8 kHz                | 1/512 (9 bit)    |
| REF_TICK (1 MHz)  | 1 kHz                | 1/512 (9 bit)    |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_pwm/atom_pwm_sch_01.webp" width="80%">

## 管脚映射

| Atom    | G22 |
| ------- | --- |
| EG27324 | INA |

## 数据手册

- [FDD8447L](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_pwm/C247783_FDD8447L_2018-10-11.PDF)
- [EG27324](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_pwm/C189546_EG27324_2018-03-27.PDF)
- [ME3116AM6G](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/atombase/atom_pwm/C97643_ME3116AM6G_2017-03-22.PDF)

## 软件开发

### Arduino

```cpp
#include <Arduino.h>

#define SIGNAL 22

int freq = 10000;
int ledChannel1 = 0;
int resolution = 10;

void setup() {
  ledcSetup(ledChannel1, freq, resolution);
  ledcAttachPin(SIGNAL, ledChannel1);
}

void loop() {

    for(int i=0; i < 500; i++){
      ledcWrite(ledChannel1, i);
      delay(2);
    }

    for(int i=500; i > 0; i--){
      ledcWrite(ledChannel1, i);
      delay(2);
    }
}
```

### UiFlow1

- [Atom PWM UiFlow1 文档](/zh_CN/uiflow/blockly/hardwares/pwm)

<img src="https://static-cdn.m5stack.com/resource/docs/products/atom/atom_pwm/atom_pwm_uiflow_01.webp" width="65%">

## 相关视频

<video width="500" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/AtomBase/ATOM_PWM_VIDEO.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=114318876085795&bvid=BV1xKdUYbEj9&p=1&autoplay=0" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/yeqbq9yGDOM?si=8pxFkJ1D-3Br1aJ-" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
