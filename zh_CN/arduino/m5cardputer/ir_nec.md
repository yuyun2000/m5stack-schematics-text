# Cardputer IR 红外发射

Cardputer IR 红外发射相关 API 与案例程序，适用于 Cardputer 和 Cardputer-Adv。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Cardputer
- M5Cardputer 库版本 >= 1.1.0
- M5Unified 库版本 >= 0.2.8
- M5GFX 库版本 >= 0.2.10

```cpp line-num
// Disable restarting receiver after each send.
// Save 450 bytes program memory and 269 bytes RAM if receiving functions are not used.
#define DISABLE_CODE_FOR_RECEIVER
#define SEND_PWM_BY_TIMER
#define IR_TX_PIN 44

#include "M5Cardputer.h"
// Third-party library: https://github.com/Arduino-IRremote/Arduino-IRremote
#include <IRremote.hpp>

uint8_t sCommand = 0x34;
uint8_t sRepeats = 0;

void setup() {
  auto cfg = M5.config();
  M5Cardputer.begin(cfg, true);  // enableKeyboard
  Serial.begin();

  M5Cardputer.Display.setRotation(1);
  M5Cardputer.Display.setTextColor(GREEN);
  M5Cardputer.Display.setTextDatum(middle_center);
  M5Cardputer.Display.setTextFont(&fonts::Orbitron_Light_24);
  M5Cardputer.Display.setTextSize(1);

  IrSender.begin(DISABLE_LED_FEEDBACK);
  IrSender.setSendPin(IR_TX_PIN);
}

void loop() {
  Serial.println();
  Serial.print(F("Send now: address=0x1111, command=0x"));
  Serial.print(sCommand, HEX);
  Serial.print(F(", repeats="));
  Serial.print(sRepeats);
  Serial.println();
  Serial.println(F("Send standard NEC with 16 bit address"));

  M5Cardputer.Display.clear();
  M5Cardputer.Display.drawString("IR NEC SEND", M5Cardputer.Display.width() / 2, M5Cardputer.Display.height() / 2 - 40);
  M5Cardputer.Display.drawString("ADDR:0x1111", M5Cardputer.Display.width() / 2, M5Cardputer.Display.height() / 2);
  M5Cardputer.Display.drawString("CMD:0x" + String(sCommand, HEX), M5Cardputer.Display.width() / 2, M5Cardputer.Display.height() / 2 + 40);

  M5Cardputer.Display.fillCircle(32, 105, 8, GREEN);
  IrSender.sendNEC(0x1111, sCommand, sRepeats);
  // IrSender.sendOnkyo(0x1111, 0x2223, sRepeats);

  sCommand += 1;
  delay(500);

  M5Cardputer.Display.fillCircle(32, 105, 8, YELLOW);
  delay(500);
}
```

这段程序将会通过红外线以 NEC 编码向 0x1111 地址发送编号递增的命令。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Arduino_IR.jpg" width="70%">

## API

Cardputer IR 红外发射部分使用了驱动库 `Arduino-IRremote`，更多相关的 API 可以参考下方文档：

- [Arduino-IRremote - GitHub](https://github.com/Arduino-IRremote/Arduino-IRremote)