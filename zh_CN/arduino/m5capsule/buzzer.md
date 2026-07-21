# Capsule Buzzer 蜂鸣器

M5Capsule Buzzer蜂鸣器相关API与案例程序。


## 案例程序


```cpp line-num
#include "M5Capsule.h"

void setup() {
    auto cfg = M5.config();
    M5Capsule.begin(cfg);
}

void loop() {
    M5Capsule.Speaker.tone(10000, 100);
    delay(1000);
    M5Capsule.Speaker.tone(4000, 20);
    delay(1000);
}
```

## API

M5Capsule库基于M5Unified库实现, Buzzer部分驱动使用了M5Unified库中的`Speaker_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)

