# Unit PoE-P4 RGB LED

Unit PoE-P4 RGB LED 案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.6
- 开发板选项 = M5UnitPoEP4
- M5Unified 库版本 >= 0.2.13

```cpp line-num
#include "M5Unified.h"

void setRGB(uint8_t r, uint8_t g, uint8_t b){
    uint8_t red = ~r;
    uint8_t green = ~g;
    uint8_t blue = ~b;
    analogWrite(17, red);
    analogWrite(15, green);
    analogWrite(16, blue);
}

void setup() {
    M5.begin();
    pinMode(15, OUTPUT);
    analogWriteResolution(15, 8);
    pinMode(16, OUTPUT);
    analogWriteResolution(16, 8);
    pinMode(17, OUTPUT);
    analogWriteResolution(17, 8);
}

void loop() {
    setRGB(255, 0, 0);// red
    delay(2000);
    setRGB(0, 255, 0);// green
    delay(2000);
    setRGB(0, 0, 255);// blue
    delay(2000);
}
```

Unit PoE-P4 上的 RGB LED 连接在 GPIO 15、16、17 引脚，且为共阳极设计，因此在程序中需要对 RGB 数值取反后进行输出，上方程序将依次显示红、绿、蓝三种颜色，每种颜色持续两秒。
