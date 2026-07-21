# NanoH2 IR NEC 发射器

NanoH2 IR NEC 发射器相关 API 与案例程序。本案例使用到了 [Arduino-IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote) - Lib 来实现 NEC 编码。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5NanoH2
- IRremote 库版本 >= 4.5.0

```cpp line-num
#include <IRremote.hpp>
#define IR_TX_PIN 3  // IR transmitter pin for NanoH2

uint8_t sCommand = 0x34;
uint8_t sRepeats = 0;

void setup() {
  Serial.begin(115200);

  // Initialize IR transmitter
  IrSender.begin(IR_TX_PIN, DISABLE_LED_FEEDBACK);

  Serial.println("NanoH2 IR NEC Transmitter");
  Serial.println("Sending incremental NEC codes...");
}

void loop() {
  Serial.println();
  Serial.print("Send now: address=0x1111, command=0x");
  Serial.print(sCommand, HEX);
  Serial.print(", repeats=");
  Serial.print(sRepeats);
  Serial.println();

  // Display on Serial
  Serial.println("--- IR NEC SEND ---");
  Serial.println("ADDR: 0x1111");
  Serial.print("CMD: 0x");
  Serial.println(sCommand, HEX);
  Serial.println("-------------------");

  // Send NEC IR signal
  Serial.println("Sending standard NEC with 16 bit address");

  IrSender.sendNEC(0x1111, sCommand, sRepeats);

  // Increment command for next transmission
  sCommand += 1;

  delay(1000);  // Wait 1 second between transmissions
}
```

该程序将通过设备上的红外发射器发送 NEC 协议信号，并在串口监视器打印消息：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/arduino_nanoh2_ir_nec_example_01.jpg" width="70%" >
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1204/arduino_nanoh2_ir_nec_example_serial_02.png" width="70%" >

## API

NanoH2 IR NEC 发射器部分驱动使用了 `IRremote` 库中的 `IrSender_Class`，更多相关的 API 可以参考下方文档：

- [Arduino-IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote)
- [Arduino-IRremote API 文档](https://github.com/Arduino-IRremote/Arduino-IRremote#api-documentation)
