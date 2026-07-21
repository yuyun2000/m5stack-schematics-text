# TimerCAM LED

## 案例程序


```cpp line-num
#include "M5TimerCAM.h"

void setup() {
    TimerCAM.begin();
}

void loop() {
    for (int16_t i = 0; i < 255; i++) {
        TimerCAM.Power.setLed(i);
        vTaskDelay(pdMS_TO_TICKS(10));
    }

    for (int16_t i = 255; i >= 0; i--) {
        TimerCAM.Power.setLed(i);
        vTaskDelay(pdMS_TO_TICKS(10));
    }
}
```