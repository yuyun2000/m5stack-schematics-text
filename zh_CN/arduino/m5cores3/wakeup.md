# CoreS3 Wakeup 休眠唤醒

CoreS3 休眠唤醒相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5CoreS3
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include <M5Unified.h>

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);

    M5.Display.setTextColor(GREEN);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setFont(&fonts::FreeSerifItalic18pt7b);
    M5.Display.setTextSize(1);

    M5.Display.drawString("Touch", M5.Display.width() / 2,
                              M5.Display.height() / 2 - 60);
    M5.Display.drawString("to sleep", M5.Display.width() / 2,
                              M5.Display.height() / 2 - 20);
    M5.Display.drawString("After 5s", M5.Display.width() / 2,
                              M5.Display.height() / 2 + 20);
    M5.Display.drawString("Wakeup", M5.Display.width() / 2,
                              M5.Display.height() / 2 + 60);
}

void loop(void) {
    M5.update();

    if (M5.Touch.getCount() && M5.Touch.getDetail(0).wasClicked()) {
        M5.Power.timerSleep(5);
        // M5.Power.timerSleep(const rtc_time_t& time);
        // M5.Power.timerSleep(const rtc_date_t& date, const rtc_time_t&
        // time);
        // M5.Power.powerOff(); shutdown
    }
}
```

烧录成功后，您可以通过触摸 CoreS3 的屏幕来触发休眠。当您点击屏幕时，设备将进入休眠状态，并在5秒后自动唤醒。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/490/CoreS3_Wakeup.jpg" width="40%">

## API

CoreS3 电源部分使用了 M5Unified 库中的 `Power_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)

