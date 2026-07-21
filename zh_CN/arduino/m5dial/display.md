# Dial Display 屏幕显示

Dial Display 屏幕显示相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Dial
- M5Dial 库版本 >= 1.0.3

```cpp line-num
#include "M5Dial.h"

void setup() {
  auto cfg = M5.config();
  M5Dial.begin(cfg, false, false);  // encoder, RFID

  int textsize = M5Dial.Display.height() / 60;
  if (textsize == 0) {
    textsize = 1;
  }
  M5Dial.Display.setTextSize(textsize);
}

void loop() {
  int x = rand() % M5Dial.Display.width();
  int y = rand() % M5Dial.Display.height();
  int r = (M5Dial.Display.width() >> 4) + 2;
  uint16_t c = rand();
  M5Dial.Display.fillCircle(x, y, r, c);

  draw_function(&M5Dial.Display);
}

void draw_function(LovyanGFX* gfx) {
  int x = rand() % gfx->width();
  int y = rand() % gfx->height();
  int r = (gfx->width() >> 4) + 2;
  uint16_t c = rand();
  gfx->fillRect(x - r, y - r, r * 2, r * 2, c);
}
```

运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/Arduino_display.gif" width="30%">

## API

Dial 屏幕显示部分使用 `M5GFX` 库作为驱动，更多相关的 API 可以参考下方文档：

- [M5GFX Setup](/zh_CN/arduino/m5gfx/m5gfx)
- [M5GFX API](/zh_CN/arduino/m5gfx/m5gfx_functions)
- [M5GFX - GitHub](https://github.com/m5stack/M5GFX)