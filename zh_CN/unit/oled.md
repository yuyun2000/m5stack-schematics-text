# Unit OLED

<span class="product-sku">SKU:U119</span>

<PictureViewer>
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/oled/oled_01.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/oled/oled_02.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/oled/oled_03.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/oled/oled_04.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/oled/oled_05.webp">
<img src="https://static-cdn.m5stack.com/resource/docs/products/unit/oled/oled_06.webp">
</PictureViewer>

## 描述

**Unit OLED** 是一款 1.3 英寸的 OLED 拓展屏幕单元。采用 SH1107 驱动方案，支持黑 / 白显示，分辨率为 128 x 64。驱动芯片选用 I2C 通信接口，使用时用户能够将其挂载到现有设备的 I2C 总线中，起到节省 IO 的作用。屏幕背部集成了磁吸设计，能够轻松吸附金属表面进行固定。该 OLED 屏幕拓展适合嵌入到各种需要显示简单内容的仪器仪表或是控制设备中作为显示面板。

## 产品特性

- OLED 显示面板
- SH1107 驱动方案
- 显示颜色：黑 / 白
- I2C 通信接口
- 128 x 64 分辨率
- 可视角：全视角
- 背部磁吸设计

## 包装内容

- 1 x Unit OLED
- 1 x HY2.0-4P Grove 连接线 (20cm)

## 应用场景

- 信息显示屏

## 规格参数

| 规格     | 参数                 |
| -------- | -------------------- |
| 工作电流 | 58mA                 |
| 通信接口 | I2C 通信 @ 0x3C      |
| 显示尺寸 | 14.7 × 29.42mm       |
| 像素间距 | 0.17×0.17mm          |
| 像素尺寸 | 0.15×0.15mm          |
| 可视角   | 全视角               |
| 工作温度 | 0 ~ 60°C             |
| 外壳材质 | Plastic (PC)         |
| 产品尺寸 | 56.0 x 24.0 x 8.0mm  |
| 产品重量 | 9.2g                 |
| 包装尺寸 | 68.0 x 57.0 x 17.0mm |
| 毛重     | 21.3g                |

## 原理图

- [Unit OLED 原理图 PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/594/Sch_UNIT_OLED_v1.1.pdf)

<SchViewer>
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/594/Sch_UNIT_OLED_v1.1_sch_01.png">
</SchViewer>

## 管脚映射

### Unit OLED

::grove-table
| HY2.0-4P | Black | Red | Yellow | White |
| -------- | ----- | --- | ------ | ----- |
| PORT.A   | GND   | 5V  | SDA    | SCL   |
::

## 尺寸图

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/unit/oled/%E5%B0%BA%E5%AF%B8%E5%9B%BE.jpg" width="80%">

## 数据手册

- [SH1107](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/oled/SH1107Datasheet.pdf)

## 软件开发

- [M5GFX Arduino 驱动库](https://github.com/m5stack/M5GFX)

- Arduino

```cpp

#include <M5UnitOLED.h>

//M5UnitOLED display ( 21, 22, 400000 ); // SDA, SCL, FREQ
M5UnitOLED display; // default setting

M5Canvas canvas(&display);

static constexpr char text[] = "Hello world ! こんにちは世界！ this is long long string sample. 寿限無、寿限無、五劫の擦り切れ、海砂利水魚の、水行末・雲来末・風来末、喰う寝る処に住む処、藪ら柑子の藪柑子、パイポ・パイポ・パイポのシューリンガン、シューリンガンのグーリンダイ、グーリンダイのポンポコピーのポンポコナの、長久命の長助";
static constexpr size_t textlen = sizeof(text) / sizeof(text[0]);
int textpos = 0;
int scrollstep = 2;

void setup(void)
{
  display.init();
  display.setRotation(2);
  canvas.setColorDepth(1); // mono color
  canvas.setFont(&fonts::lgfxJapanMinchoP_32);
  canvas.setTextWrap(false);
  canvas.setTextSize(2);
  canvas.createSprite(display.width() + 64, 72);
}

void loop(void)
{
  int32_t cursor_x = canvas.getCursorX()-scrollstep;
  if (cursor_x <= 0)
  {
    textpos = 0;
    cursor_x = display.width();
  }

  canvas.setCursor(cursor_x, 0);
  canvas.scroll(-scrollstep, 0);
  while (textpos < textlen && cursor_x <= display.width())
  {
    canvas.print(text[textpos++]);
    cursor_x = canvas.getCursorX();
  }
  display.waitDisplay();
  canvas.pushSprite(&display, 0, (display.height()-canvas.height()) >> 1);
}

```

## UiFlow1

- [Unit OLED UiFlow1 文档](/zh_CN/uiflow/blockly/unit/oled)

## UiFlow2

- [Unit OLED UiFlow2 文档](https://uiflow-micropython.readthedocs.io/zh-cn/latest/unit/oled.html)

## 相关视频

<video class="video-container" controls>
    <source src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/video/Product_example_video/Unit/UNIT_OLED.mp4" type="video/mp4">
</video>

- UiFlow2 Unit OLED

<TabPanel>
  <template #tab-Bilibili>
      <div class="video-iframe">
        <iframe src="//player.bilibili.com/player.html?isOutside=true&aid=113026946565358&bvid=BV1MjsLeyEgf&p=1&autoplay=0" loading="lazy" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"></iframe>
      </div>
  </template>
  <template #tab-Youtube>
      <div class="video-iframe">
      <iframe width="560" height="315" src="https://www.youtube.com/embed/m72_Tk-LEJI?si=5lHVCyQmSBNjZGL4" title="YouTube video player" frameborder="0" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
      </div>
  </template>
</TabPanel>
