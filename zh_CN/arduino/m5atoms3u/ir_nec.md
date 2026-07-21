# AtomS3U IR 红外发送

AtomS3U IR 红外发送相关库与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.6
- 开发板选项 = M5AtomS3
- M5Unified 库版本 >= 0.2.13
- [IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote/tree/v4.5.0) 库版本 >= 4.5.0

```cpp line-num
#include "M5Unified.h"
#include <IRremote.hpp>

#define IR_SEND_PIN    12    

// Demo parameters for NEC protocol
uint16_t address = 0x0000;     // Starting device address
uint8_t  command = 0x55;       // Starting command value
uint8_t  repeats = 0;          // Number of repeat transmissions

void setup() {
    M5.begin();                // Initialize M5Stack device
    Serial.begin(115200);      // Start serial communication at 115200 baud
    delay(200);                // Wait for serial port to stabilize

    Serial.println("AtomS3U IRremote example");
    pinMode(IR_SEND_PIN, OUTPUT);// Essential! Otherwise can not transmit 

    // Initialize IR communication
    IrSender.begin(DISABLE_LED_FEEDBACK);  // Initialize IR sender without LED feedback
    IrSender.setSendPin(IR_SEND_PIN);      // Assign transmitter pin

    Serial.printf("IR Send Pin: %d\n", IR_SEND_PIN);
    delay(500); // Wait for hardware components to stabilize
}

void loop() {
    // Send infrared signal using NEC protocol
    Serial.printf("Send NEC: addr=0x%04x, cmd=0x%02x\n", address, command);
    IrSender.sendNEC(address, command, repeats);

    // Update transmission parameters for next cycle
    address += 0x0001;  // Increment device address
    command += 0x01;     // Increment command code
    repeats  = 0;        // Disable repeat frames (set >0 to test repeats)

    delay(2000);
}
```

AtomS3U 每两秒发送一次 NEC 红外信号，地址（Address）和命令（Command）分别从 0x0000 和 0x55 开始递增，可以使用支持 NEC 协议的红外接收设备进行接收验证。

## 驱动库

- [IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote)
