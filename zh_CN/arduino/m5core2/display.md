# Core2 Display 屏幕显示

#>说明|Core2 使用M5GFX库作为屏幕驱动, 参考下方API & 案例即可实现简单的显示, 获取更多API内容可以参考[M5GFX](https://github.com/m5stack/M5GFX)源码。

## 案例程序


```cpp line-num
#include "M5Unified.h"

void draw_function(LovyanGFX* gfx)
{
    int x      = rand() % gfx->width();
    int y      = rand() % gfx->height();
    int r      = (gfx->width() >> 4) + 2;
    uint16_t c = rand();
    gfx->fillRect(x - r, y - r, r * 2, r * 2, c);
}

void setup()
{
    auto cfg = M5.config();
    M5.begin(cfg);
    int textsize = M5.Display.height() / 60;
    if (textsize == 0) {
        textsize = 1;
    }
    M5.Display.setTextSize(textsize);
    M5.Display.clear(TFT_WHITE);
}

void loop()
{
    int x      = rand() % M5.Display.width();
    int y      = rand() % M5.Display.height();
    int r      = (M5.Display.width() >> 4) + 2;
    uint16_t c = rand();
    M5.Display.fillCircle(x, y, r, c);
    draw_function(&M5.Display);
    delay(1000);
}  
```

例程效果如下：

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/Core2_Arduino_display.mp4" type="video/mp4"></video>
