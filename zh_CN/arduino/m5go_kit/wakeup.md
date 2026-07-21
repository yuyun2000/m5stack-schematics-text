# M5GO Wakeup 休眠唤醒

M5GO 休眠唤醒相关API与案例程序。

## 案例程序

```cpp line-num
#include <M5Unified.h>

void setup(void) {
  auto cfg = M5.config();
  M5.begin(cfg);

  M5.Display.setTextDatum(middle_center);
  M5.Display.setTextFont(&fonts::FreeSerifBold9pt7b);
  M5.Display.setTextSize(1);

  M5.Display.drawString("Press BtnA", M5.Display.width() / 2, M5.Display.height() / 2 - 20);
  M5.Display.drawString("to Sleep 5s", M5.Display.width() / 2, M5.Display.height() / 2 + 20);
}

void loop(void) {
  M5.update();

  if (M5.BtnA.wasPressed()) {
    M5.Display.clear();
    M5.Display.drawString("Sleep 5s", M5.Display.width() / 2, M5.Display.height() / 2 + 20);
    M5.Power.timerSleep(5);//sec
  }
}
```

由于没有独立的RTC芯片，M5GO无法使用RTC相关功能，只能调用例程中sec级定时唤醒。

例程效果如下：

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/659/Core_Arduino_wakeup.mp4" type="video/mp4"></video>

## API

M5GO 电源部分使用了M5Unified库中的`Power_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)

