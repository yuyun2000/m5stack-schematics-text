# TimerCAM Wakeup 休眠唤醒

## 案例程序

```cpp line-num
#include "M5TimerCAM.h"

void led_breathe(int ms) {
    for (int16_t i = 0; i < 255; i++) {
        TimerCAM.Power.setLed(i);
        vTaskDelay(pdMS_TO_TICKS(ms));
    }

    for (int16_t i = 255; i >= 0; i--) {
        TimerCAM.Power.setLed(i);
        vTaskDelay(pdMS_TO_TICKS(ms));
    }
}

void setup() {
    TimerCAM.begin(true);
    Serial.println("Wake up!!!");
    led_breathe(10);
    // sleep after 5s wakeup!
    TimerCAM.Power.timerSleep(5);
}

void loop() {
}
```