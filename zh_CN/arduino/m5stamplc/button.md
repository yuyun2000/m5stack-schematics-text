# StamPLC Button 按键

StamPLC按键输入相关API与案例程序。

#>注意事项: | 使用时需要在主循环中包含`M5.update()`函数用于读取状态更新且尽可能减少阻塞情况, 否则可能无法及时获取的按键变化状态。

## 案例程序

```cpp line-num
#include <Arduino.h>
#include <M5Unified.h>

void setup()
{
    /* Init M5 */
    M5.begin();

    M5.Display.setTextScroll(true);
    M5.Display.setTextColor(TFT_GREENYELLOW);
    M5.Display.println("Button example");
    M5.Display.setTextColor(TFT_YELLOW);
}

void loop()
{
    /* Update button states */
    M5.update();

    /* Check if button was clicked */
    if (M5.BtnA.wasClicked()) {
        M5.Display.println("Button A was clicked");
    } else if (M5.BtnB.wasClicked()) {
        M5.Display.println("Button B was clicked");
    } else if (M5.BtnC.wasClicked()) {
        M5.Display.println("Button C was clicked");
    }

    delay(100);
}
```


## API

M5StamPLC库基于M5Unified库实现, 按键部分使用了M5Unified库中的`Button_Class`, 更多按键相关的API可以参考下方文档:

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)

