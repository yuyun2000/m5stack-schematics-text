# StackChan 触摸传感器

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.3.7
- 开发板选项 = M5CoreS3
- M5StackChan 库版本 >= 1.0.0

```cpp line-num
#include <M5StackChan.h>

void setup()
{
    /* Init StackChan */
    M5StackChan.begin();

    /* Setup display */
    M5StackChan.Display().setTextSize(2);
    M5StackChan.Display().setTextScroll(true);
    M5StackChan.Display().setTextColor(TFT_ORANGE);
    M5StackChan.Display().printf("> Touch or swipe the top\n");
    M5StackChan.Display().setTextColor(TFT_GREEN);
}

void loop()
{
    /* Update touch sensor */
    M5StackChan.update();

    auto& ts = M5StackChan.TouchSensor;

    if (ts.wasClicked()) {
        M5StackChan.Display().printf("> Was clicked\n");
    }

    if (ts.wasSwipedForward()) {
        M5StackChan.Display().printf("> Was swiped forward\n");
    }

    if (ts.wasSwipedBackward()) {
        M5StackChan.Display().printf("> Was swiped backward\n");
    }

    delay(50);
}
```

烧录成功后，可以通过触摸 StackChan 顶部的触摸传感器来与设备进行交互。当点击传感器时，屏幕上将显示 "Was clicked"；当向前触摸滑动传感器时，屏幕上将显示 "Was swiped forward"；当向后触摸滑动传感器时，屏幕上将显示 "Was swiped backward"。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/StackChan_TouchSensor.jpg" width="40%">
