# Capsule IR NEC 红外

M5Capsule IR驱动案例程序。本案例使用到了[Arduino-IRremote - Lib](https://github.com/Arduino-IRremote/Arduino-IRremote)来实现NEC编码。

## 案例程序

```cpp line-num
#define DISABLE_CODE_FOR_RECEIVER  // Disables restarting receiver after each
                                   // send. Saves 450 bytes program memory and
                                   // 269 bytes RAM if receiving functions are
                                   // not used.
#define SEND_PWM_BY_TIMER
#define IR_TX_PIN 4

#include "M5Capsule.h"
#include <IRremote.hpp>  // include the library IRremote: https://github.com/Arduino-IRremote/Arduino-IRremote

uint8_t sCommand = 0x34;
uint8_t sRepeats = 0;

void setup() {
    auto cfg = M5.config();
    M5Capsule.begin(cfg);

    IrSender.begin(DISABLE_LED_FEEDBACK);  // Start with IR_SEND_PIN as send pin
    IrSender.setSendPin(IR_TX_PIN);
}

void loop() {
    Serial.println();
    Serial.print(F("Send now: address=0x1111, command=0x"));
    Serial.print(sCommand, HEX);
    Serial.print(F(", repeats="));
    Serial.print(sRepeats);
    Serial.println();
    Serial.println("IR NEC SEND");
    Serial.println("ADDR:0x1111");
    Serial.println("CMD:0x" + String(sCommand, HEX));
    Serial.println(F("Send standard NEC with 16 bit address"));
    IrSender.sendNEC(0x1111, sCommand, sRepeats);
    // IrSender.sendOnkyo(0x1111, 0x2223, sRepeats);
    /*
     * Increment send values
     */
    sCommand += 1;
    delay(1000);
}
```

