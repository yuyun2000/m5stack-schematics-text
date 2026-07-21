# TimerCAM Power 电源状态

## 案例程序


```cpp line-num
#include "M5TimerCAM.h"

void setup() {
    TimerCAM.begin(true);
}

void loop() {
    Serial.printf("Bat Voltage: %dmv\r\n", TimerCAM.Power.getBatteryVoltage());
    Serial.printf("Bat Level: %d%%\r\n", TimerCAM.Power.getBatteryLevel());
    delay(1000);
}
```