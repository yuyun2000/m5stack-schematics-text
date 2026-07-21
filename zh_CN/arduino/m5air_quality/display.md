# Air Quality Display 屏幕显示

#>Air Quality使用M5GFX库作为屏幕驱动, 参考下方API & 案例即可实现简单的显示, 获取更多API内容可以参考[M5GFX](https://github.com/m5stack/M5GFX)源码。

## 案例程序

```cpp line-num
#include <M5Unified.h>

// 随机绘制方块的函数
void draw_function(LovyanGFX* gfx) {
    int x      = rand() % gfx->width();
    int y      = rand() % gfx->height();
    int r      = (gfx->width() >> 4) + 2;
    uint16_t c = rand();
    gfx->fillRect(x - r, y - r, r * 2, r * 2, c);
}

void setup() {
    // 初始化 M5Unified
    auto cfg = M5.config();
    M5.begin(cfg);  

    // 根据屏幕高度设置文字大小
    int textsize = M5.Display.height() / 60;
    if (textsize == 0) {
        textsize = 1;
    }
    M5.Display.setTextSize(textsize);
}

void loop() {
    // 随机绘制一个填充圆
    int x      = rand() % M5.Display.width();
    int y      = rand() % M5.Display.height();
    int r      = (M5.Display.width() >> 4) + 2;
    uint16_t c = rand();
    M5.Display.fillCircle(x, y, r, c);

    // 调用 draw_function 绘制一个随机方块
    draw_function(&M5.Display);

    delay(50);
}
```

上传完成就可以看到下面的效果了

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/m5air_quality_arduino_quickstart_display01.jpg" width="30%">