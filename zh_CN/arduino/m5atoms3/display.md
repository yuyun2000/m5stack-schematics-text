# AtomS3 Display 屏幕显示

#>M5AtomS3使用M5GFX库作为屏幕驱动, 参考下方API & 案例即可实现简单的显示, 获取更多API内容可以参考[M5GFX](https://github.com/m5stack/M5GFX)源码。


```cpp line-num
#include "M5AtomS3.h"

void setup() {
    AtomS3.begin();
    AtomS3.Display.setTextDatum(middle_center);
    AtomS3.Display.fillScreen(WHITE);
    AtomS3.Display.fillCircle(AtomS3.Display.width() / 2,
                              AtomS3.Display.height() / 2, 30, ORANGE);
    AtomS3.Display.drawString("Hello", AtomS3.Display.width() / 2,
                              AtomS3.Display.height() / 2);
}

void loop() {
}
```
