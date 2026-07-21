# Arduino Nesso N1 IR NEC 红外

Arduino Nesso N1 IR驱动案例程序。本案例使用到了[Arduino-IRremote - Lib](https://github.com/Arduino-IRremote/Arduino-IRremote)来实现NEC编码。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = ArduinoNessoN1
- M5GFX 库版本 >= 0.2.17
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#define DISABLE_CODE_FOR_RECEIVER  // Disables restarting receiver after each
                                   // send. Saves 450 bytes program memory and
                                   // 269 bytes RAM if receiving functions are
                                   // not used.
#define SEND_PWM_BY_TIMER
#define IR_TX_PIN 9

#include "M5Unified.h"
#include <IRremote.hpp>  // include the library
// IRremote: https://github.com/Arduino-IRremote/Arduino-IRremote

uint8_t sCommand = 0x34;
uint8_t sRepeats = 0;

void setup() {
    auto cfg = M5.config();
    M5.begin(cfg);
    M5.Display.setRotation(1);
    M5.Display.setTextColor(GREEN);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setTextFont(&fonts::Orbitron_Light_24);
    M5.Display.setTextSize(1);

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

    M5.Display.clear();
    M5.Display.drawString("IR NEC SEND", M5.Display.width() / 2,
                                M5.Display.height() / 2 - 40);

    M5.Display.drawString("ADDR:0x1111", M5.Display.width() / 2,
                                M5.Display.height() / 2);

    M5.Display.drawString("CMD:0x" + String(sCommand, HEX),
                                M5.Display.width() / 2,
                                M5.Display.height() / 2 + 40);

    Serial.println(F("Send standard NEC with 16 bit address"));

    M5.Display.fillCircle(32, 105, 8, GREEN);
    IrSender.sendNEC(0x1111, sCommand, sRepeats);
    // IrSender.sendOnkyo(0x1111, 0x2223, sRepeats);
    /*
     * Increment send values
     */
    sCommand += 1;
    delay(500);
    M5.Display.fillCircle(32, 105, 8, YELLOW);
    delay(500);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1198/arduino_nesso_n1_ir_nec_example_01.jpg" width="50%" />
