# StickC-Plus2 Display 屏幕显示

#>M5StickC Plus2使用M5GFX库作为屏幕驱动, 参考下方API & 案例即可实现简单的显示, 获取更多API内容可以参考[M5GFX](https://github.com/m5stack/M5GFX)源码。

## 案例程序


```cpp line-num
#include "M5StickCPlus2.h"

void draw_function(LovyanGFX* gfx) {
    int x      = rand() % gfx->width();
    int y      = rand() % gfx->height();
    int r      = (gfx->width() >> 4) + 2;
    uint16_t c = rand();
    gfx->fillRect(x - r, y - r, r * 2, r * 2, c);
}

void setup() {
    auto cfg = M5.config();
    StickCP2.begin(cfg);
    int textsize = StickCP2.Display.height() / 60;
    if (textsize == 0) {
        textsize = 1;
    }
    StickCP2.Display.setTextSize(textsize);
}

void loop() {
    int x      = rand() % StickCP2.Display.width();
    int y      = rand() % StickCP2.Display.height();
    int r      = (StickCP2.Display.width() >> 4) + 2;
    uint16_t c = rand();
    StickCP2.Display.fillCircle(x, y, r, c);
    draw_function(&StickCP2.Display);
}
```