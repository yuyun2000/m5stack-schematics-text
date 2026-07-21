# StickS3 Display 屏幕显示

#>说明 | StickS3 使用 M5GFX 库作为屏幕驱动, 参考下方 API & 案例即可实现简单的显示, 获取更多API内容可以参考 [M5GFX](https://github.com/m5stack/M5GFX) 源码。

## 案例程序

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5StickS3
- M5Unified 库版本 >= 0.2.12
- M5GFX 库版本 >= 0.2.18

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

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_display.jpg" width="40%">
