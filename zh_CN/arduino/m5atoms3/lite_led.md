# AtomS3 LED

AtomS3 RGB LED控制

```cpp line-num
#include <M5AtomS3.h>

void setup() {
    AtomS3.begin(true);  // Init M5AtomS3Lite.
    AtomS3.dis.setBrightness(100);
}

void loop() {
    AtomS3.dis.drawpix(0xff0000);
    AtomS3.update();
    delay(500);
    AtomS3.dis.drawpix(0x00ff00);
    AtomS3.update();
    delay(500);
    AtomS3.dis.drawpix(0x0000ff);
    AtomS3.update();
    delay(500);
}
```