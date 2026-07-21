# StackChan IR 红外通信

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5CoreS3
- M5StackChan 库版本 >= 1.0.0
- IRremote 库版本 >= 4.5.0

```cpp line-num
#include <IRremote.hpp>
#include <M5StackChan.h>

#define IR_SEND_PIN    5      // GPIO pin for IR transmitter
#define IR_RECEIVE_PIN 10      // GPIO pin for IR receiver

// Demo parameters for NEC protocol
uint16_t address = 0x0000;     // Starting device address
uint8_t  command = 0x55;       // Starting command value
uint8_t  repeats = 0;          // Number of repeat transmissions

void setup() {
    M5StackChan.begin();                // Initialize M5Stack device
    Serial.begin(115200);      // Start serial communication at 115200 baud
    delay(200);                // Wait for serial port to stabilize
    
    // Configure Display() settings
    M5StackChan.Display().setTextFont(&fonts::FreeMonoBold9pt7b);
    M5StackChan.Display().clear();
    M5StackChan.Display().setCursor(0,0);
    M5StackChan.Display().printf("IRremote example");
    Serial.println("IRremote example");

    // Initialize IR communication
    IrReceiver.begin(IR_RECEIVE_PIN);     // Start IR receiver
    IrSender.begin(DISABLE_LED_FEEDBACK);  // Initialize IR sender without LED feedback
    IrSender.setSendPin(IR_SEND_PIN);      // Assign transmitter pin

    Serial.printf("IR Send Pin: %d, IR Recv Pin: %d\n", IR_SEND_PIN, IR_RECEIVE_PIN);
    delay(500); // Wait for hardware components to stabilize
}

void loop() {
    // 1. Send infrared signal using NEC protocol
    Serial.printf("Send NEC: addr=0x%04x, cmd=0x%02x\n", address, command);
    IrSender.sendNEC(address, command, repeats);
    
    // Update Display with transmission info
    M5StackChan.Display().fillRect(0, 20, 320, 90, TFT_BLACK);  // Clear previous content
    M5StackChan.Display().setCursor(0, 40);
    M5StackChan.Display().printf("Send NEC:\n addr=0x%04x\n cmd=0x%02x\n", address, command);

    IrReceiver.restartAfterSend();  // Re-enable receiver after transmission

    // 2. Wait for possible reflection (short-range testing)
    delay(20);  // Brief pause to allow signal reception

    // Attempt to decode received IR signal
    if (IrReceiver.decode()) {
        // Print received data to serial monitor
        Serial.printf("Received: protocol=%s, addr=0x%04x, cmd=0x%02x, raw=0x%08lx\n",
                      getProtocolString(IrReceiver.decodedIRData.protocol),
                      IrReceiver.decodedIRData.address,
                      IrReceiver.decodedIRData.command,
                      (unsigned long)IrReceiver.decodedIRData.decodedRawData);
        
        // Display received data on screen
        M5StackChan.Display().fillRect(0, 110, 320, 130, TFT_BLACK);  // Clear previous content
        M5StackChan.Display().setCursor(0, 110);
        M5StackChan.Display().printf("Received:\n protocol=%s\n addr=0x%04x\n cmd=0x%02x\n raw=0x%08lx\n",
                        getProtocolString(IrReceiver.decodedIRData.protocol),
                        IrReceiver.decodedIRData.address,
                        IrReceiver.decodedIRData.command,
                        (unsigned long)IrReceiver.decodedIRData.decodedRawData);
        
        IrReceiver.resume();  // Enable reception of next signal
    } else {
        // Handle case where no signal was received
        Serial.println("No IR received.");
        M5StackChan.Display().fillRect(0, 110, 320, 130, TFT_BLACK);  // Clear previous content
        M5StackChan.Display().setCursor(0, 110);
        M5StackChan.Display().println("No IR received.");
    }

    // Update transmission parameters for next cycle
    address += 0x0001;  // Increment device address
    command += 0x01;     // Increment command code
    repeats  = 0;        // Disable repeat frames (set >0 to test repeats)

    delay(2000);  // Main loop delay (2 seconds)
}
```

该程序将控制 StackChan 发收红外 NEC 编码并在屏幕上显示 NEC 编码相关信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/StackChan_IR.jpg" width="40%">

## 驱动库

- [IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote)