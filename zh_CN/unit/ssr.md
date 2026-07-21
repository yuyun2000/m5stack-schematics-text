# Unit SSR

<span class="product-sku">SKU:U122</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ssr/ssr_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ssr/ssr_02.webp">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/785/U122-01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ssr/ssr_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ssr/ssr_06.webp">
</PictureViewer>

## 描述

**Unit SSR** 是一款固态继电器，集成 MOC3043M 光耦隔离，自带过零检测。支持输入 3.3-5V DC 控制信号，控制输出单相 220-250V AC 电源。结合 M5 控制器接入 UiFlow 编程平台，能够轻松实现远程控制。相对普通机械继电器，该固态继电器使用功率半导体器件控制，具备微秒级通断速度，内置过流保护。无物理触点、寿命长、可靠性高，能够适应剧烈震动等复杂作业环境。适用于灯光控制，数控机床等需要频繁通断线路、快速响应的场景。

\#>1. 使用高压交流负载时请小心，请勿带电操作。<br/> 2. 此继电器仅适用于交流负载

## 产品特性

- 过零型 SSR
- 内置过流保护
- 内置光耦隔离，自带过零检测
- 速度快，低噪声，高寿命，高可靠，灵敏度高
- 采用 GROVE 接口，接入更加方便
- 支持 UiFlow 图形化编程，结合 M5 控制器 3 分钟可实现继电器远程控制

\#>**固态继电器与机械继电器相比的优势:**<br/>1. 更快的通断速度，且无物理触点磨损。<br/>2 . 完全静音操作。<br/>3 . 无电火花，可用于复杂环境。<br/>4. 更长的使用寿命。<br/>5 . 更小的体积

## 包装内容

- 1 x Unit SSR
- 1 x HY2.0-4P Grove 连接线 (20cm)
- 1 x HT3.96-4P 端子

## 应用场景

- 电机控制
- 工业和家用照明
- 加热和静态开关
- 舞台灯光
- 医疗设备、交通信号灯

## 规格参数

| 规格         | 参数                  |
| ------------ | --------------------- |
| 可控硅型号   | BT136S                |
| 光耦隔离型号 | MOC3043               |
| 控制信号     | 3.3-5V DC             |
| 通断电压     | 单相 AC: 220-250V     |
| 最大负载电流 | 2A                    |
| 控制通道数   | 1                     |
| 过流保护     | 熔断器：2A            |
| 工作温度     | -10 ~ 80°C            |
| 产品尺寸     | 56.0 x 24.0 x 10.2mm  |
| 产品重量     | 8.3g                  |
| 包装尺寸     | 138.0 x 93.0 x 11.2mm |
| 毛重         | 16.5g                 |

## 原理图

<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/ssr/ssr_sch_01.webp" width="80%">

## 管脚映射

### Unit SSR

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.B   | GND   | 5V  | DIN    | NC    |
::

## 数据手册

- [BT136S](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/ssr/C23427_BT136S.PDF)
- [MOC3043M](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/ssr/C41809_MOC3043SR2M_2015-01-24.PDF)

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/ssr/model%20size.png" width="100%">

## 软件开发

### Arduino

```cpp
#include <M5Stack.h>

void setup() {
  M5.begin();
  M5.Power.begin();
  M5.Lcd.clear(BLACK);
  M5.Lcd.setTextFont(4);
  M5.Lcd.setTextColor(YELLOW, BLACK);
  M5.Lcd.setCursor(50, 0, 4);
  M5.Lcd.println(("SSR Example"));
  //disable the speak noise
  dacWrite(25, 0);
  pinMode(26, OUTPUT);
}

void loop(void) {
  digitalWrite(26, HIGH);
  delay(500);
  digitalWrite(26, LOW);
  delay(500);
}

```

### UiFlow2

- [Unit SSR UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/ssr.html)

## 相关视频

<video controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/SSR_UNIT_VIDEO.mp4" type="video/mp4">
</video>

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113501624403830&bvid=BV1bGUnYKEyL&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/2pMBdyNAPcA?si=aZBv5QwR4EYAxDLW" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
