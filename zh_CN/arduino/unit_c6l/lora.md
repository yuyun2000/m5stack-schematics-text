# Unit C6L LoRa 通信

Unit C6L LoRa 通信相关 API 与案例程序。

#> 注意 | Unit C6L 使用 SX1262 LoRa 通信芯片，开发时请注意选择相应的类。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.3
- 开发板选项 = M5UnitC6L
- RadioLib 库版本 >= 7.3.0

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/RadioLib.png" width="70%">

### 发送端

```cpp line-num
#include <RadioLib.h>
#include <M5Unified.h>

// SX1262: CS, IRQ, NRST, BUSY
SX1262 radio = new Module(23, 7, RADIOLIB_NC, 19);

int transmitState = RADIOLIB_ERR_NONE;  // save transmission state between loops
bool transmitFlag = false;              // flag to indicate that a packet was sent
int count = 0;                          // counter of transmitted packets

// function to be called when a complete packet is transmitted
void setFlag(void) {
  transmitFlag = true;
}

void setup() {
  Serial.begin(115200);
  M5.begin();
  delay(1000);

  auto& ioe = M5.getIOExpander(0);
  ioe.digitalWrite(7, false);
  delay(100);
  ioe.digitalWrite(7, true);  // re-enable SX_NRST
  ioe.digitalWrite(6, true);  // enable SX_ANT_SW
  ioe.digitalWrite(5, true);  // enable SX_LNA_EN

  // initialize SX1262
  Serial.print("\n[SX1262] Initializing... ");
  // frequency MHz, bandwidth kHz, spreading factor, coding rate denominator, sync word,
  // output power dBm, preamble length, TCXO reference voltage, useRegulatorLDO
  int beginState = radio.begin(868.0, 125.0, 12, 5, 0x34, 22, 20, 3.0, true);
  if (beginState == RADIOLIB_ERR_NONE) {
    Serial.println("Succeeded!");
  } else {
    Serial.print("Failed, code: ");
    Serial.println(beginState);
    while (true) { delay(100); }
  }

  // set the function to be called when packet transmission is finished
  radio.setPacketSentAction(setFlag);

  // start transmitting the first packet
  Serial.print("[SX1262] Sending the first packet... ");

  // you can transmit C-string or Arduino string up to 256 characters long
  transmitState = radio.startTransmit("Hello world from M5Stack! #0");
}

void loop() {
  if (transmitFlag) {      // check if the previous transmission is finished
    transmitFlag = false;  // reset the flag

    if (transmitState == RADIOLIB_ERR_NONE) {  // packet was sent successfully
      Serial.println("Succeeded!");
    } else {
      Serial.print("Failed, code: ");
      Serial.println(transmitState);
    }

    // clean up after transmission is finished. This will ensure transmitter is disabled, RF switch is powered down, etc.
    radio.finishTransmit();

    delay(1000);

    // send another packet
    count++;
    Serial.printf("[SX1262] Sending packet #%d... ", count);
    String str = "Hello world from M5Stack! #" + String(count);
    transmitState = radio.startTransmit(str);
  }
}
```

### 接收端

```cpp line-num
#include <RadioLib.h>
#include <M5Unified.h>

// SX1262: CS, IRQ, NRST, BUSY
SX1262 radio = new Module(23, 7, RADIOLIB_NC, 19);

bool receiveFlag = false;  // flag to indicate that a packet was received

// function to be called when a complete packet is received
void setFlag(void) {
  receiveFlag = true;
}

void setup() {
  Serial.begin(115200);
  M5.begin();
  delay(1000);

  auto& ioe = M5.getIOExpander(0);
  ioe.digitalWrite(7, false);
  delay(100);
  ioe.digitalWrite(7, true);  // re-enable SX_NRST
  ioe.digitalWrite(6, true);  // enable SX_ANT_SW
  ioe.digitalWrite(5, true);  // enable SX_LNA_EN

  // initialize SX1262
  Serial.print("\n[SX1262] Initializing... ");
  // frequency MHz, bandwidth kHz, spreading factor, coding rate denominator, sync word,
  // output power dBm, preamble length, TCXO reference voltage, useRegulatorLDO
  int beginState = radio.begin(868.0, 125.0, 12, 5, 0x34, 22, 20, 3.0, true);
  if (beginState == RADIOLIB_ERR_NONE) {
    Serial.println("Succeeded!");
  } else {
    Serial.print("Failed, code: ");
    Serial.println(beginState);
    while (true) { delay(100); }
  }

  // set the function to be called when a new packet is received
  radio.setPacketReceivedAction(setFlag);

  // start listening for LoRa packets
  Serial.print("[SX1262] Starting to listen... ");
  int receiveState = radio.startReceive();
  if (receiveState == RADIOLIB_ERR_NONE) {
    Serial.println("Succeeded!");
  } else {
    Serial.print("Failed, code: ");
    Serial.println(receiveState);
    while (true) { delay(100); }
  }
}

void loop() {
  if (receiveFlag) {      // check if a new packet is received
    receiveFlag = false;  // reset the flag

    String str;  // read the received data as an Arduino String
    int readState = radio.readData(str);

    if (readState == RADIOLIB_ERR_NONE) {  // packet was received successfully
      Serial.println("\n[SX1262] Received packet!");
      Serial.print("[SX1262] Data: ");
      Serial.println(str);

      Serial.print("[SX1262] RSSI: ");
      Serial.print(radio.getRSSI());  // Received Signal Strength Indicator
      Serial.println(" dBm");

      Serial.print("[SX1262]  SNR: ");
      Serial.print(radio.getSNR());  // Signal-to-Noise Ratio
      Serial.println(" dB");

      Serial.print("[SX1262] Frequency error: ");
      Serial.print(radio.getFrequencyError());
      Serial.println(" Hz");

    } else if (readState == RADIOLIB_ERR_CRC_MISMATCH) {  // packet was received but malformed
      Serial.println("CRC error!");

    } else {  // some other error occurred
      Serial.print("Failed, code: ");
      Serial.println(readState);
    }
  }
}
```

### 运行结果

将以上两段代码分别编译上传至两个 Unit C6L，发送端将会发射 LoRa 信号，接收端收取此信号。各自的串口输出如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/LoRa_Transmit.png" width="90%">

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/LoRa_Receive.png" width="90%">

## API

Unit C6L LoRa 通信部分使用了`RadioLib`库作为驱动，更多相关的 API 可以参考下方文档：

- [RadioLib Library - GitHub](https://github.com/jgromes/RadioLib)
- [RadioLib Wiki - GitHub](https://github.com/jgromes/RadioLib/wiki/Basics)
- [RadioLib Docs](https://jgromes.github.io/RadioLib/index.html)
- [RadioLib SX1262 Docs](https://jgromes.github.io/RadioLib/class_s_x126x.html)