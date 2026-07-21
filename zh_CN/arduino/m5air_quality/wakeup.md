# Air Quality Wakeup 休眠唤醒

Air Quality 休眠唤醒相关API与案例程序。

## 案例程序

```cpp line-num
#include <M5Unified.h>
#include <esp_sleep.h>

void setup() {
  auto cfg = M5.config();
  M5.begin(cfg);                         // 初始化显示、按键、RTC 等 

  M5.Display.fillScreen(TFT_WHITE);
  M5.Display.setTextSize(2);
  M5.Display.setTextColor(TFT_BLACK);
  M5.Display.setTextDatum(middle_center);


  esp_sleep_wakeup_cause_t cause = esp_sleep_get_wakeup_cause();
  int cx = M5.Display.width()  / 2;
  int cy = M5.Display.height() / 2;
  if (cause == ESP_SLEEP_WAKEUP_TIMER) {
    M5.Display.drawString("Woken up!", cx, cy - 20);
    M5.Display.drawString("Press BtnA", cx, cy + 20);
  } else {
    M5.Display.drawString("Press BtnA", cx, cy - 20);
    M5.Display.drawString("to sleep 5s", cx, cy + 20);
  }
}

void loop() {
  M5.update();                           // 刷新按键状态 

  // 按下 A 键后进入 5 秒定时睡眠
  if (M5.BtnA.wasPressed()) {
    int cx = M5.Display.width()  / 2;
    int cy = M5.Display.height() / 2;
    M5.Display.fillScreen(TFT_WHITE);
    M5.Display.setTextDatum(middle_center);
    M5.Display.drawString("Sleeping...", cx, cy);
    delay(500);
    M5.Power.timerSleep(5);              // 5 秒后唤醒
  }
}
```

上传完成按下按键就可以看到下面的效果了

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/m5air_quality_arduino_quickstart_wakeup01.jpg" width="30%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/m5air_quality_arduino_quickstart_wakeup02.jpg" width="30%">

## API

电源部分使用了M5Unified库中的`Power_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)

