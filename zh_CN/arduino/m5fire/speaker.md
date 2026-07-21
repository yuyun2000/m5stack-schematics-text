# Fire Speaker 扬声器

Fire 扬声器相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Fire
- M5Unified 库版本 >= 0.2.8

```cpp line-num
#include "M5Unified.h"

void setup() {
  M5.begin();
}

void loop() {
  M5.Speaker.tone(7000, 100);  // frequency, duration
  delay(1000);
  M5.Speaker.tone(4000, 20);  // frequency, duration
  delay(1000);
}
```

## API

Fire 扬声器部分驱动使用了`M5Unified`库中的`Speaker_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Speaker Class](/zh_CN/arduino/m5unified/speaker_class)