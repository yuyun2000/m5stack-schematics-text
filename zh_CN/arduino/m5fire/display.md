# Fire Display 屏幕显示

Fire 屏幕显示相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Fire
- M5Unified 库版本 >= 0.2.8
- M5GFX 库版本 >= 0.2.11

```cpp line-num
#include "M5Unified.h"

void setup() {
  M5.begin();

  int textsize = M5.Display.height() / 60;
  if (textsize == 0) {
    textsize = 1;
  }
  M5.Display.setTextSize(textsize);
}

void loop() {
  int x = rand() % M5.Display.width();
  int y = rand() % M5.Display.height();
  int r = (M5.Display.width() >> 4) + 2;
  uint16_t c = rand();
  M5.Display.fillCircle(x, y, r, c);

  draw_function(&M5.Display);
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

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/658/Arduino_display.gif" width="50%">

## API

Fire 屏幕显示部分使用 `M5GFX` 库作为驱动，更多相关的 API 可以参考下方文档：

- [M5GFX Setup](/zh_CN/arduino/m5gfx/m5gfx)
- [M5GFX API](/zh_CN/arduino/m5gfx/m5gfx_functions)
- [M5GFX - GitHub](https://github.com/m5stack/M5GFX)