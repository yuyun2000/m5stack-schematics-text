# Atom VoiceS3R IR 红外发射

Atom VoiceS3R IR 红外发射相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5AtomS3R
- M5Unified 库版本 >= 0.2.8
- Arduino-IRremote 库版本 >= 4.5.0

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/Arduino_ir_lib.png" width="70%">

```cpp line-num
// Disable receiver functions will save program memory and RAM.
#define DISABLE_CODE_FOR_RECEIVER
#define NO_LED_SEND_FEEDBACK_CODE
#define NO_LED_FEEDBACK_CODE
#define SEND_PWM_BY_TIMER
#define IR_TX_PIN 47

#include "M5Unified.h"
// Third-party library: https://github.com/Arduino-IRremote/Arduino-IRremote
#include <IRremote.hpp>

uint16_t sAddress = 0x1234;
uint8_t sCommand  = 0x56;
uint8_t sRepeats  = 0;

void setup() {
  M5.begin();
  Serial.begin(115200);

  IrSender.begin(IR_TX_PIN);
}

void loop() {
  Serial.println("Sending standard NEC signal with 16 bit address: ");
  Serial.printf("address=0x%x, command=0x%x, repeats=%d\n\n", sAddress, sCommand, sRepeats);

  IrSender.sendNEC(sAddress, sCommand, sRepeats);

  sCommand += 1;
  delay(1000);
}
```

这段程序将会通过红外线以 NEC 编码向程序中指定的地址发送编号递增的命令。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1182/Arduino_ir.png" width="90%">

## API

Atom VoiceS3R IR 红外发射部分使用了驱动库 `Arduino-IRremote`，更多相关的 API 可以参考下方文档：

- [Arduino-IRremote - GitHub](https://github.com/Arduino-IRremote/Arduino-IRremote)
- [Arduino-IRremote Docs](https://arduino-irremote.github.io/Arduino-IRremote/index.html)
