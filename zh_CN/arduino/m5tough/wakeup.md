# Tough Wakeup 休眠唤醒

Tough 休眠唤醒相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 2.1.4
- 开发板选项 = M5Tough
- M5Unified 库版本 >= 0.2.5
- M5GFX 库版本 >= 0.2.7

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

int myIndex = 0;

void setup() {
  M5.begin();
  M5.Display.setRotation(1);
  M5.Display.setFont(&fonts::FreeMonoBold12pt7b);

  M5.Display.clear();
  M5.Display.print("Sleep & Wakeup Test\n");
}

void loop() {
  myIndex++;

  M5.Display.setCursor(0, 50);
  M5.Display.printf("   %4d", myIndex);
  delay(50);

  if (myIndex % 20 == 0) {
    // M5.Power.timerSleep(5);              // in seconds
    // M5.Power.deepSleep(5000000, false);  // in microseconds
    M5.Power.lightSleep(5000000, false);    // in microseconds

    M5.Display.setCursor(0, 0);
    M5.Display.print("Sleep & Wakeup Test\n");
  }
  if (myIndex >= 1000) {
    myIndex = 0;
  }
}
```

该程序将会显示一个从 0 开始自增 1 的计数器，每次增长到 20 的倍数时让设备进入浅度休眠 5 秒然后唤醒，程序继续。如果将程序改为计时休眠或者深度休眠（注释掉的两行），则唤醒后整个程序会从头开始。

## API

Tough 休眠唤醒部分使用了 `M5Unified` 库中的 `Power_Class`，更多相关的API可以参考下方文档：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)