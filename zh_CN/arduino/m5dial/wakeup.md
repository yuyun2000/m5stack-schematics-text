# Dial Wakeup 休眠唤醒

Dial Wakeup 休眠唤醒相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Dial
- M5Dial 库版本 >= 1.0.3

```cpp line-num
#include <M5Dial.h>

void setup() {
  auto cfg = M5.config();
  M5Dial.begin(cfg, false, false);  // encoder, RFID

  M5Dial.Display.setTextColor(GREEN);
  M5Dial.Display.setTextDatum(middle_center);
  M5Dial.Display.setTextFont(&fonts::FreeSerifItalic18pt7b);
  M5Dial.Display.setTextSize(1);

  M5Dial.Display.drawString("Press Btn", M5Dial.Display.width() / 2, M5Dial.Display.height() / 2 - 60);
  M5Dial.Display.drawString("to sleep",  M5Dial.Display.width() / 2, M5Dial.Display.height() / 2 - 20);
  M5Dial.Display.drawString("After 5s",  M5Dial.Display.width() / 2, M5Dial.Display.height() / 2 + 20);
  M5Dial.Display.drawString("Wakeup",    M5Dial.Display.width() / 2, M5Dial.Display.height() / 2 + 60);
}

void loop() {
  M5Dial.update();

  if (M5Dial.BtnA.wasPressed()) {
    M5Dial.Power.timerSleep(5);
    // M5Dial.Power.timerSleep(const rtc_time_t& time);
    // M5Dial.Power.timerSleep(const rtc_date_t& date, const rtc_time_t& time);
    // M5Dial.Power.powerOff();  // shutdown
  }
}
```

将以上程序编译上传，按下按钮，设备将休眠 5 秒钟然后自动唤醒。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/Arduino_wakeup.gif" width="30%">

## API

M5Dial 库基于 M5Unified 库实现，电源部分使用了 M5Unified 库中的`Power_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)
