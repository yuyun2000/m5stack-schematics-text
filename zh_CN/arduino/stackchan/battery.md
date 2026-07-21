# StackChan Battery 电池

StackChan 电池状态读取案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.3.7
- 开发板选项 = M5CoreS3
- M5StackChan 库版本 >= 1.0.0

```cpp line-num
#include <M5StackChan.h>

void setup() {
    M5StackChan.begin();
    M5StackChan.Display().setFont(&fonts::FreeMonoBold12pt7b);

    M5StackChan.Display().clear();
    M5StackChan.Display().setCursor(0, 0);
    M5StackChan.Display().print("StackChan Battery");
}

void loop() {
    M5StackChan.update();
    float voltage = M5StackChan.getBatteryVoltage();
    float current = M5StackChan.getBatteryCurrent() * 1000;

    M5StackChan.Display().setCursor(0, 50);
    M5StackChan.Display().printf("Voltage: %0.2fV", voltage);

    M5StackChan.Display().setCursor(0, 100);
    M5StackChan.Display().printf("Current: %0.2fmA", current);

    delay(1000);
}
```

该程序将在屏幕上显示电池电压、电流信息，每秒刷新一次。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/StackChan_Battery.jpg" width="40%">

