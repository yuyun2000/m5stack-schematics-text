# Cap LoRa868 / LoRa-1262 Arduino 使用教程

本教程适用于 Cap LoRa868 和 Cap LoRa-1262。

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [RadioLib](https://github.com/jgromes/RadioLib)
  - [TinyGPSPlus](https://github.com/m5stack/TinyGPSPlus)

\#> 注意 | TinyGPSPlus 库需要在 GitHub 上下载适配过 M5Stack 设备的库版本，库地址: [TinyGPSPlus - M5Stack GitHub](https://github.com/m5stack/TinyGPSPlus)，请勿在 Arduino Library 中下载。（如有疑问，请参考[此教程](/zh_CN/arduino/arduino_library#git%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85)）

- 使用到的硬件产品：
  - [Cardputer-Adv](https://shop.m5stack.com/products/m5stack-cardputer-adv-version-esp32-s3)
  - [Cap LoRa868](https://shop.m5stack.com/products/lora-gps-cap-for-cardputer-adv-sx1262-atgm336h) / [Cap LoRa-1262](https://shop.m5stack.com/products/cap-lora-1262-for-cardputer-adv-sx1262-atgm336h)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Cardputer-Adv_02.webp" width="20%"/> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1177/Cap_LoRa868_04.webp" width="20%"/>

## 2. 编译上传

- 将 Cardputer-Adv 侧面的开关键置于 `OFF` 状态，然后在开机前按住 `G0` 按键，在设备后通电后释放，之后设备将进入下载模式，等待烧录。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Cardputer-Adv_operation_01.jpg" width="50%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Cardputer-Adv_operation.gif" width="40%">

- 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1177/cap_lora868_arduino_example.png" width="70%">

## 3. 案例程序

- 本教程中使用的主控设备为 Cardputer-Adv ，搭配 Cap LoRa868。 Cap LoRa868 的 LoRa 部分采用 SPI 的方式通讯， GPS 部分采用串口的方式通讯，请根据实际的电路连接修改程序中的引脚定义，设备连接后对应的 LoRa SPI IO 为 `G5 (NSS)`、`G14 (MOSI)`、`G39 (MISO)`、`G40 (SCK)`，其他 IO 为 `G4 (TRQ)`、`G3 (RST)`、`G6 (BUSY)`；串口 IO 为 `G15 (RX)`、`G13 (TX)`。

实物连接组装如下图所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1177/cap_lora868_connect.jpg" width="70%">

### 3.1 LoRa 使用案例

\#> 说明 | 下方代码中只设置了 `NSS`、`TRQ`、`GD02`、`RST` 四个引脚，但实际上 RadioLib 库会根据所使用的主控设备，自动映射剩余的 SPI 引脚 (`MOSI`、`MISO`、`SCK`)，即使用 M5Unified 库初始化时根据不同设备默认定义的引脚，Cardputer-Adv 上分别为 `G14 (MOSI)`、`G39 (MISO)`、`G40 (SCK)`，因此无需手动指定。

#### 发送端

```cpp line-num
#include <M5Unified.h>
#include <RadioLib.h>
#include "utility/PI4IOE5V6408_Class.hpp"

#define LORA_BW           125.0f // SX1262 bandwidth (kHz) - 125kHz is common for long-range
#define LORA_SF           12     // Spreading factor (6-12) - higher = longer range, slower data rate
#define LORA_CR           5      // Coding rate (5-8, represents 4/5 to 4/8) - higher = more error correction
#define LORA_FREQ         868.0  // Carrier frequency (MHz) - 868MHz is EU ISM band for SX1262
#define LORA_SYNC_WORD    0x34   // Sync word for packet recognition - must match between transmitter/receiver
#define LORA_TX_POWER     22     // Transmission power (dBm) - 22dBm is maximum for many regions
#define LORA_PREAMBLE_LEN 20     // Preamble length (symbols) - ensures receiver can detect packet start

//         SX1262 PIN         NSS,       IRQ,         RST,        BUSY
SX1262 radio = new Module(GPIO_NUM_5, GPIO_NUM_4, GPIO_NUM_3, GPIO_NUM_6);

// Tracks the result of the last transmission attempt (error code from RadioLib)
int transmissionState = RADIOLIB_ERR_NONE;

// Special attribute for ESP8266/ESP32 to place ISR in RAM (faster interrupt response)
#if defined(ESP8266) || defined(ESP32)
ICACHE_RAM_ATTR
#endif
// Packet sent flag
volatile bool transmittedFlag = false;
// This function is called when a complete packet is transmitted by the module
// IMPORTANT: this function MUST be 'void' type and MUST NOT have any arguments!
void setFlag(void)
{
    // we sent a packet, set the flag
    transmittedFlag = true;
}

String LoRaName;
m5::PI4IOE5V6408_Class ioe(0x43, 400000, &m5::In_I2C);

void setup()
{
    M5.begin();
    Serial.begin(115200);
    // Cap LoRa-1262 Detection
    if (!m5::In_I2C.begin()) {
        Serial.println("I2C init failed");
        while (true) delay(1000);
    }

    if (ioe.begin()) {
        Serial.printf("Using Cap LoRa-1262\n");
        LoRaName = "LoRa-1262";
        ioe.setDirection(0, true);      // Output
        ioe.setHighImpedance(0, false); // Disable high-impedance so pin can actually drive
        ioe.digitalWrite(0, true);      // High Level
    } else {
        Serial.printf("Using Cap LoRa868\n");
        LoRaName = "LoRa868";
    }

    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);

    // Init SX1262
    Serial.printf("[%s] Initializing ...", LoRaName);
    int state =
        radio.begin(LORA_FREQ, LORA_BW, LORA_SF, LORA_CR, LORA_SYNC_WORD, LORA_TX_POWER, LORA_PREAMBLE_LEN, 3.0, true);
    if (state == RADIOLIB_ERR_NONE) {
        Serial.println(F("Init success!"));
    } else {
        Serial.print(F("Init failed, code: "));
        Serial.println(state);
        while (true) { delay(10); }
    }
    radio.setCurrentLimit(140);// Current range: 0-140mA , step 2.5mA

    // Register callback function after sending packet successfully
    radio.setPacketSentAction(setFlag);

    // Send first packet to enable flag
    Serial.printf("[%s] Sending first packet...", LoRaName);
    transmissionState = radio.startTransmit("Hello World!");
    M5.Display.setCursor(5,0);
    M5.Display.printf("Hello World!\n");
}

// Counter to keep track of transmitted packets
int count = 0;

void loop()
{
    if (transmittedFlag) {
        // reset flag
        transmittedFlag = false;

        if (transmissionState == RADIOLIB_ERR_NONE) {
            // packet was successfully sent
            Serial.println(F("Transmission finished!"));
            M5.Display.println("Send sucessfully!");

            // NOTE: when using interrupt-driven transmit method,
            //       it is not possible to automatically measure
            //       transmission data rate using getDataRate()

        } else {
            Serial.print(F("Send failed, code: "));
            Serial.println(transmissionState);
            M5.Display.print("\nSend failed\ncode:");
            M5.Display.println(transmissionState);
        }

        // Clean up after transmission is finished
        // This will ensure transmitter is disabled,
        // RF switch is powered down etc.
        radio.finishTransmit();

        // Wait a second before transmitting again
        delay(1000);

        Serial.printf("[%s] Sending #%d packet ... ", LoRaName, count);
        // You can transmit C-string or Arduino string up to 256 characters long
        String str        = "Cap " + LoRaName + "#" + String(count++);
        transmissionState = radio.startTransmit(str);
        M5.Display.clear();
        M5.Display.setCursor(0,5);
        M5.Display.printf("[%s]\nSending #%d packet\n......\n", LoRaName, count);

        // You can also transmit byte array up to 256 bytes long
        /*
          byte byteArr[] = {0x01, 0x23, 0x45, 0x67,
                            0x89, 0xAB, 0xCD, 0xEF};
          transmissionState = radio.startTransmit(byteArr, 8);
        */
    }
}
```

#### 接收端

```cpp line-num
#include <M5Unified.h>
#include <RadioLib.h>
#include "utility/PI4IOE5V6408_Class.hpp"

#define LORA_BW           125.0f // LoRa bandwidth (kHz) - 125kHz is common for long-range
#define LORA_SF           12     // Spreading factor (6-12) - higher = longer range, slower data rate
#define LORA_CR           5      // Coding rate (5-8, represents 4/5 to 4/8) - higher = more error correction
#define LORA_FREQ         868.0  // Carrier frequency (MHz) - 868MHz is EU ISM band for LoRa
#define LORA_SYNC_WORD    0x34   // Sync word for packet recognition - must match between transmitter/receiver
#define LORA_TX_POWER     22     // Transmission power (dBm) - 22dBm is maximum for many regions
#define LORA_PREAMBLE_LEN 20     // Preamble length (symbols) - ensures receiver can detect packet start

//         SX1262 PIN         NSS,       IRQ,         RST,        BUSY
SX1262 radio = new Module(GPIO_NUM_5, GPIO_NUM_4, GPIO_NUM_3, GPIO_NUM_6);

#if defined(ESP8266) || defined(ESP32)
ICACHE_RAM_ATTR
#endif
// Packet received flag
volatile bool receivedFlag = false;
// This function is called when a complete packet is received by the module
// IMPORTANT: This function MUST be 'void' type and MUST NOT have any arguments!
void setFlag(void)
{
    receivedFlag = true;
}

String LoRaName;
m5::PI4IOE5V6408_Class ioe(0x43, 400000, &m5::In_I2C);

void setup()
{
    M5.begin();
    Serial.begin(115200);
    // Cap LoRa-1262 Detection

    if (!m5::In_I2C.begin(I2C_NUM_0, 8, 9)) {
        Serial.println("I2C init failed");
        while (true) delay(1000);
    }

    if (ioe.begin()) {
        Serial.printf("Using Cap LoRa-1262\n");
        LoRaName = "LoRa-1262";
        ioe.setDirection(0, true);      // output
        ioe.setHighImpedance(0, false); // disable high-impedance so pin can actually drive
        ioe.digitalWrite(0, true);     // default low
    } else {
        Serial.printf("Using Cap LoRa868\n");
        LoRaName = "LoRa868";
    }

    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);

    // Init SX1262
    Serial.printf("[%s] Initializing ... ", LoRaName);
    int state = radio.begin(LORA_FREQ, LORA_BW, LORA_SF, LORA_CR, LORA_SYNC_WORD, LORA_TX_POWER, LORA_PREAMBLE_LEN, 3.0, true);
    if (state == RADIOLIB_ERR_NONE) {
        Serial.println(F("Init success!"));
    } else {
        Serial.print(F("Init failed, code: "));
        Serial.println(state);
        while (true) { delay(10); }
    }
    radio.setCurrentLimit(140);// Current range: 0-140mA , step 2.5mA

    // Register callback function after receiving packet successfully
    radio.setPacketReceivedAction(setFlag);

    // Start listening for LoRa packets
    Serial.printf("[%s] Starting to listen ... ", LoRaName);
    state = radio.startReceive();
    if (state == RADIOLIB_ERR_NONE) {
        Serial.println(F("Listen successfully!"));
    } else {
        Serial.print(F("Listen failed, code: "));
        Serial.println(state);
        while (true) { delay(10); }
    }

    // If needed, 'listen' mode can be disabled by calling any of the following methods:
    // radio.standby()
    // radio.sleep()
    // radio.transmit();
    // radio.receive();
    // radio.scanChannel();
}

void loop()
{
    if (receivedFlag) {
        // reset flag
        receivedFlag = false;

        // Read received data as an Arduino String
        String str;
        int state = radio.readData(str);

        // Read received data as byte array
        /*
          byte byteArr[8];
          int numBytes = radio.getPacketLength();
          int state = radio.readData(byteArr, numBytes);
        */

        if (state == RADIOLIB_ERR_NONE) {
            // Packet was successfully received
            Serial.printf("[%s] Received packet:\n", LoRaName);
            M5.Display.clear();
            M5.Display.setCursor(0,5);
            M5.Display.printf("[%s]\nReceived packet:\n", LoRaName);

            // Data of the packet
            Serial.printf("[%s] Data:\t\t", LoRaName);
            Serial.println(str);
            M5.Display.printf("Data: %s\n", str.c_str());

            // RSSI (Received Signal Strength Indicator)
            Serial.printf("[%s] RSSI:\t\t", LoRaName);
            Serial.print(radio.getRSSI());
            Serial.println(F(" dBm"));
            M5.Display.printf("RSSI: %0.2f dBm\n", radio.getRSSI());

            // SNR (Signal-to-Noise Ratio)
            Serial.printf("[%s] SNR:\t\t", LoRaName);
            Serial.print(radio.getSNR());
            Serial.println(F(" dB"));
            M5.Display.printf("SNR:  %0.2f dB\n", radio.getSNR());

            // Frequency error
            Serial.printf("[%s] Frequency error:\t", LoRaName);
            Serial.print(radio.getFrequencyError());
            Serial.println(F(" Hz"));
            M5.Display.printf("Freq err: %0.2f Hz\n", radio.getFrequencyError());

        } else if (state == RADIOLIB_ERR_CRC_MISMATCH) {
            // Packet was received, but is malformed
            Serial.println(F("CRC error!"));

        } else {
            Serial.print(F("Receive failed, code: "));
            Serial.println(state);
        }
    }
}
```

上述例程效果为发送端会每秒发送一次包含计数的字符串，接收端会打印接收到的字符串，并显示 RSSI、SNR 和频率误差等信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1177/cap_lora868_arduino_lora.jpg" width="60%">

- 发送端串口返回信息：

```
[LoRa868] Sending #39 packet ... Transmission finished!
```

- 接收端串口返回信息：

```
[LoRa868] Received packet:
[LoRa868] Data:		    Cap LoRa868#38
[LoRa868] RSSI:		    -7.00 dBm
[LoRa868] SNR:		     4.50 dB
[LoRa868] Frequency error: -779.60 Hz
```

### 3.2 GPS 使用案例

- 本设备 GPS 模块支持多种卫星系统，包括 GPS、GLONASS、GALILEO、BDS 和 QZSS，例程提供了修改卫星系统的函数 `setSatelliteMode()` ，默认为 GLONASS 系统，当修改后屏幕上的前缀也会随之修改，方便确定卫星系统。

```cpp line-num
#include "M5Unified.h"
#include "M5GFX.h"
#include "MultipleSatellite.h"

static const int RXPin = 15, TXPin = 13;
static const uint32_t GPSBaud = 115200;
MultipleSatellite gps(Serial1, GPSBaud, SERIAL_8N1, RXPin, TXPin);

// Variable to track current satellite system mode (default: GLONASS)
satellite_mode_t currentMode = SATELLITE_MODE_GLONASS;

// Function prototype for displaying information
void displayInfo(void);

/**
 * Get the prefix string for different satellite systems
 * @param mode Current satellite system mode
 * @return Corresponding prefix string for the satellite system
 */
const char* getSatPrefix(satellite_mode_t mode) {
    switch (mode) {
        case SATELLITE_MODE_GPS:      return "GPS_Sat";   // GPS satellite prefix
        case SATELLITE_MODE_BDS:      return "BDS_Sat";   // BeiDou satellite prefix
        case SATELLITE_MODE_GLONASS:  return "GLN_Sat";   // GLONASS satellite prefix
        case SATELLITE_MODE_GALILEO:  return "GAL_Sat";   // Galileo satellite prefix
        case SATELLITE_MODE_QZSS:     return "QZS_Sat";   // QZSS satellite prefix
        default:                      return "Unknown";   // Default for unknown systems
    }
}

void setup() {
    M5.begin();
    Serial.begin(115200);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    gps.begin();              // Initialize GPS module
    // Set GPS to factory start mode
    gps.setSystemBootMode(BOOT_FACTORY_START);

    // Print initialization information to serial monitor
    Serial.println(F("<----------Cap LoRa868 Example---------->"));
    Serial.print(F("Testing TinyGPSPlus library v. "));
    Serial.println(TinyGPSPlus::libraryVersion());
    String version = gps.getGNSSVersion();
    Serial.printf("GNSS SW=%s\r\n", version.c_str());
    delay(1000);  // Short delay for initialization
    gps.setSatelliteMode(currentMode);

    displayInfo();  // Initial display of information
}

void loop() {
    gps.updateGPS();  // Update GPS data
    displayInfo();    // Update display with new data
    delay(100);
}

void displayInfo(void) {
    Serial.println("=========================================");
    Serial.print(F("Location: "));

    Serial.printf("satellites:%d\n", gps.satellites.value());
    String gps_mode = gps.getSatelliteMode();
    Serial.printf("GNSS Mode:%s\r\n", gps_mode.c_str());

    // Get appropriate satellite prefix based on current mode
    const char* satPrefix = getSatPrefix(currentMode);

    // Check if location data has been updated
    if (gps.location.isUpdated()) {
        auto latitude = gps.location.lat();
        auto longitude = gps.location.lng();
        // Print latitude and longitude to serial with 6 decimal places
        Serial.print(latitude, 6); Serial.print(F(","));
        Serial.print(longitude, 6);Serial.print(F("\n"));

        M5.Display.fillRect(0, 0, 240, 135, TFT_BLACK);
        M5.Display.setCursor(0, 0);
        M5.Display.printf("%s: \nSat: %d\nLat: %.6f\nlng: %.6f\n", satPrefix,
                          (uint8_t)gps.satellites.value(),
                          latitude,
                          longitude);
    } else {
        // If no valid location data, display placeholders
        M5.Display.fillRect(0, 0, 240, 135, TFT_BLACK);
        M5.Display.setCursor(0, 0);
        M5.Display.printf("%s\n", satPrefix);
        M5.Display.print("Sat: ----\nLat: ----\nLng: ----\n");
        Serial.print(F("LOCATION INVALID\n"));  // Indicate invalid data on serial
    }

    Serial.print(F("Date/Time: "));
    // Check if date data has been updated
    if (gps.date.isUpdated()) {
        auto month = gps.date.month();
        auto day = gps.date.day();
        auto year = gps.date.year();
        // Print date to serial (month/day/year)
        Serial.printf("%d/%d/%d ", month, day, year);

        M5.Display.fillRect(0, 80, 128, 128, TFT_BLACK);
        M5.Display.setCursor(0, 80);
        M5.Display.printf("Date: %d/%d/%d\n", month, day, year);
    } else {
        Serial.print(F("DATE INVALID"));  // Indicate invalid date
    }

    // Check if time data has been updated
    if (gps.time.isUpdated()) {
        auto hour = gps.time.hour();
        auto minute = gps.time.minute();
        auto sec = gps.time.second();
        auto centisec = gps.time.centisecond();
        // Print time to serial with leading zeros where necessary (HH:MM:SS.CS)
        if (hour < 10) Serial.print(F("0"));
        Serial.print(hour);Serial.print(F(":"));
        if (minute < 10) Serial.print(F("0"));
        Serial.print(minute);Serial.print(F(":"));
        if (sec < 10) Serial.print(F("0"));
        Serial.print(sec);Serial.print(F("."));
        if (centisec < 10) Serial.print(F("0"));
        Serial.print(centisec);

        M5.Display.fillRect(0, 128, 128, 60, TFT_BLACK);
        M5.Display.setCursor(0, 96);
        M5.Display.printf("Time: %02d:%02d:%02d.%02d\n", hour, minute, sec, centisec);
    } else {
        Serial.print(F("TIME INVALID"));  // Indicate invalid time
    }
    Serial.println();
    delay(1000);  // Delay to stabilize display updates
}
```

由于该产品 GPS 采用内置天线，无外置天线，请尽量在户外空旷区域使用，如操场、天台等，且定位等待时间较长，约为几分钟，请耐心等待设备成功搜索卫星与获取坐标。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1177/cap_lora868_arduino_gps.jpg" width="40%">

- 串口返回信息：

```
=========================================
Location: satellites:22
GNSS Mode:GLN_Sat
22.687541,113.772193
Date/Time: 9/5/2025 03:00:24.00
```

### 3.3 使用 LoRa 通信传递 GPS 信息

?> 注意 | LoRa 和 GPS 同时使用时，LoRa 信号会对 GPS 定位造成一定的干扰，导致 GPS 定位信号接收不稳定，建议在实际使用中限制 LoRa 的发送功率过高，以达到 GPS 定位和 LoRa 通信的平衡。

#### 发送端

```cpp line-num
#include <M5Unified.h>
#include <RadioLib.h>
#include "utility/PI4IOE5V6408_Class.hpp"
#include "MultipleSatellite.h"

// LoRa configuration parameters
#define LORA_BW           125.0f // Bandwidth (kHz)
#define LORA_SF           12     // Spreading factor (6-12)
#define LORA_CR           5      // Coding rate (5-8)
#define LORA_FREQ         868.0  // Frequency (MHz)
#define LORA_SYNC_WORD    0x34   // Sync word
#define LORA_TX_POWER     16     // Transmission power (dBm)
#define LORA_PREAMBLE_LEN 20     // Preamble length

// LoRa pin definition
SX1262 radio = new Module(GPIO_NUM_5, GPIO_NUM_4, GPIO_NUM_3, GPIO_NUM_6);

// GPS configuration parameters
static const int RXPin = 15, TXPin = 13;
static const uint32_t GPSBaud = 115200;
MultipleSatellite gps(Serial1, GPSBaud, SERIAL_8N1, RXPin, TXPin);

// Global variables
int transmissionState = RADIOLIB_ERR_NONE;
volatile bool transmittedFlag = false;
int count = 0;
satellite_mode_t currentMode = SATELLITE_MODE_GLONASS;
float lastLat = 0.0f, lastLng = 0.0f;
int lastSatellites = 0;
String lastDate = "", lastTime = "";

// LoRa transmission completion callback function
#if defined(ESP8266) || defined(ESP32)
ICACHE_RAM_ATTR
#endif
void setFlag(void) {
    transmittedFlag = true;
}

// Function to get satellite system prefix
const char* getSatPrefix(satellite_mode_t mode) {
    switch (mode) {
        case SATELLITE_MODE_GPS:      return "GPS_Sat";
        case SATELLITE_MODE_BDS:      return "BDS_Sat";
        case SATELLITE_MODE_GLONASS:  return "GLN_Sat";
        case SATELLITE_MODE_GALILEO:  return "GAL_Sat";
        case SATELLITE_MODE_QZSS:     return "QZS_Sat";
        default:                      return "Unknown";
    }
}

// Function to update display information
String displayInfo(void) {
    M5.Display.setTextColor(TFT_WHITE);
    Serial.println("\n=========================================");
    Serial.print(F("Location: "));
    // Update satellite count
    lastSatellites = gps.satellites.value();
    Serial.printf("satellites:%d\n", lastSatellites);
    String gps_mode = gps.getSatelliteMode();
    Serial.printf("GNSS Mode:%s\r\n", gps_mode.c_str());

    const char* satPrefix = getSatPrefix(currentMode);

    // Update location information
    if (gps.location.isUpdated()) {
        lastLat = gps.location.lat();
        lastLng = gps.location.lng();
        Serial.print(lastLat, 6); Serial.print(F(","));
        Serial.print(lastLng, 6);Serial.print(F("\n"));

        // Display GPS information
        M5.Display.fillRect(0, 0, 240, 135, TFT_BLACK);
        M5.Display.setCursor(0, 0);
        M5.Display.printf("%s: \nSat: %d\nLat: %.6f\nLng: %.6f\n",
                          satPrefix, lastSatellites, lastLat, lastLng);
    } else {
        M5.Display.fillRect(0, 0, 240, 135, TFT_BLACK);
        M5.Display.setCursor(0, 0);
        M5.Display.printf("%s\nSat: ----\nLat: ----\nLng: ----\n", satPrefix);
        Serial.print(F("LOCATION INVALID\n"));
    }

    // Update date information
    Serial.print(F("Date/Time: "));
    if (gps.date.isUpdated()) {
        lastDate = String(gps.date.month()) + "/" +
                  String(gps.date.day()) + "/" +
                  String(gps.date.year());
        Serial.print(lastDate);
        Serial.print(F(" "));

        M5.Display.setCursor(0, 75);
        M5.Display.printf("Date: %s\n", lastDate.c_str());
    } else {
        lastDate = "DATE INVALID";
        Serial.print(F("DATE INVALID "));
    }

    // Update time information
    if (gps.time.isUpdated()) {
        lastTime = (gps.time.hour() < 10 ? "0" : "") + String(gps.time.hour()) + ":" +
           (gps.time.minute() < 10 ? "0" : "") + String(gps.time.minute()) + ":" +
           (gps.time.second() < 10 ? "0" : "") + String(gps.time.second()) + "." +
           (gps.time.centisecond() < 10 ? "0" : "") + String(gps.time.centisecond());
        Serial.print(lastTime);

        M5.Display.printf("Time: %s\n", lastTime.c_str());
    } else {
        lastTime = "TIME INVALID";
        Serial.print(F("TIME INVALID"));
    }
    Serial.println();

    return String("Type:") + satPrefix +
           " Count:" + String(count) +
           " Sat:" + String(lastSatellites) +
           " Lat:" + String(lastLat, 6) +
           " Lng:" + String(lastLng, 6) +
           " Date:" + lastDate +
           " Time:" + lastTime;
}

String LoRaName;
m5::PI4IOE5V6408_Class ioe(0x43, 400000, &m5::In_I2C);

void setup() {
    // Initialize M5 device
    M5.begin();
    Serial.begin(115200);
    // Cap LoRa-1262 Detection
    if (!m5::In_I2C.begin()) {
        Serial.println("I2C init failed");
        while (true) delay(1000);
    }

    if (ioe.begin()) {
        Serial.printf("Using Cap LoRa-1262\n");
        LoRaName = "LoRa-1262";
        ioe.setDirection(0, true);      // Output
        ioe.setHighImpedance(0, false); // Disable high-impedance so pin can actually drive
        ioe.digitalWrite(0, true);      // High Level
    } else {
        Serial.printf("Using Cap LoRa868\n");
        LoRaName = "LoRa868";
    }

    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);

    // Initialize LoRa module
    Serial.printf("[%s] Initializing ...", LoRaName);
    int state = radio.begin(LORA_FREQ, LORA_BW, LORA_SF, LORA_CR,
                           LORA_SYNC_WORD, LORA_TX_POWER, LORA_PREAMBLE_LEN, 3.0, true);
    if (state == RADIOLIB_ERR_NONE) {
        Serial.println(F("Init success!"));
    } else {
        Serial.print(F("Init failed, code: "));
        Serial.println(state);
        while (true) { delay(10); }
    }
    radio.setCurrentLimit(140);
    radio.setPacketSentAction(setFlag);
    // Send first data packet
    Serial.printf("[%s] Sending first packet...", LoRaName);
    transmissionState = radio.startTransmit("GPS Initializing...");

    M5.Display.setCursor(5,0);
    M5.Display.printf("GPS Initializing...\n");
    // Initialize GPS module
    gps.begin();
    gps.setSystemBootMode(BOOT_FACTORY_START);
    gps.setSatelliteMode(currentMode);
    Serial.println(F("<----------Cap LoRa868/1262 Example---------->"));
    Serial.print(F("Testing TinyGPSPlus library v. "));
    Serial.println(TinyGPSPlus::libraryVersion());
    String version = gps.getGNSSVersion();
    Serial.printf("GNSS SW=%s\r\n", version.c_str());
    delay(1000);
}

void loop() {
    // Handle LoRa transmission completion event
    if (transmittedFlag) {
        transmittedFlag = false;

        if (transmissionState == RADIOLIB_ERR_NONE) {
            // Update GPS data and display
            Serial.println(F("      Transmission finished!"));
            M5.Display.setTextColor(TFT_GREEN);
            M5.Display.println("  OK!");
        } else {
            Serial.print(F("Send failed, code: "));
            Serial.println(transmissionState);
            M5.Display.print("\nSend failed\ncode:");
            M5.Display.println(transmissionState);
        }

        radio.finishTransmit();
        // delay(500);
        gps.updateGPS();
        String gpsData = displayInfo();
        // Send GPS data
        Serial.printf("[%s] Sending GPS data:\n %s\n", LoRaName, gpsData.c_str());
        transmissionState = radio.startTransmit(gpsData);

        // Update display
        M5.Display.fillRect(0, 115, 240, 20, TFT_BLACK);
        M5.Display.setCursor(0,115);
        M5.Display.setTextColor(TFT_YELLOW);
        M5.Display.printf("Sending #%d... ", count++);
    }
}
```

#### 接收端

```cpp line-num
#include <M5Unified.h>
#include <RadioLib.h>
#include "utility/PI4IOE5V6408_Class.hpp"

#define LORA_BW           125.0f // LoRa bandwidth (kHz) - 125kHz is common for long-range
#define LORA_SF           12     // Spreading factor (6-12) - higher = longer range, slower data rate
#define LORA_CR           5      // Coding rate (5-8, represents 4/5 to 4/8) - higher = more error correction
#define LORA_FREQ         868.0  // Carrier frequency (MHz) - 868MHz is EU ISM band for LoRa
#define LORA_SYNC_WORD    0x34   // Sync word for packet recognition - must match between transmitter/receiver
#define LORA_TX_POWER     16     // Transmission power (dBm) - 22dBm is maximum
#define LORA_PREAMBLE_LEN 20     // Preamble length (symbols) - ensures receiver can detect packet start

//         SX1262 PIN         NSS,       IRQ,         RST,        BUSY 
SX1262 radio = new Module(GPIO_NUM_5, GPIO_NUM_4, GPIO_NUM_3, GPIO_NUM_6);

// Packet received flag
volatile bool receivedFlag = false;
#if defined(ESP8266) || defined(ESP32)
ICACHE_RAM_ATTR
#endif
// This function is called when a complete packet is received by the module
// IMPORTANT: This function MUST be 'void' type and MUST NOT have any arguments!
void setFlag(void)
{
    receivedFlag = true;
}

String Type = "Unknown";
String Count = "--";
String Sat = "--";
String Lat = "--";
String Lng = "--";
String Date = "Invalid";
String Time = "Invalid";

void gpsInfoParse(String str) {
   
    int pos = 0;
    while (pos < str.length()) {
        int newlinePos = str.indexOf(' ', pos);
        if (newlinePos == -1) newlinePos = str.length();
        
        String line = str.substring(pos, newlinePos);
        pos = newlinePos + 1;
        
        int fieldType = -1;
        if (line.startsWith("Type:")) fieldType = 0;
        else if (line.startsWith("Count:")) fieldType = 1;
        else if (line.startsWith("Sat:")) fieldType = 2;
        else if (line.startsWith("Lat:")) fieldType = 3;
        else if (line.startsWith("Lng:")) fieldType = 4;
        else if (line.startsWith("Date:")) fieldType = 5;
        else if (line.startsWith("Time:")) fieldType = 6;
        
        switch (fieldType) {
            case 0: Type = line.substring(5); break;// Type
            case 1: Count = line.substring(6); break; // Count
            case 2: Sat = line.substring(4); break; // Sat
            case 3: Lat = line.substring(4); break; // Lat
            case 4: Lng = line.substring(4); break; // Lng
            case 5: Date = line.substring(5); break; // Date
            case 6: Time = line.substring(5); break; // Time
            default: break;
        }
    }
}

String LoRaName;
m5::PI4IOE5V6408_Class ioe(0x43, 400000, &m5::In_I2C);

void setup()
{
    M5.begin();
    Serial.begin(115200);
    // Cap LoRa-1262 Detection
    if (!m5::In_I2C.begin()) {
        Serial.println("I2C init failed");
        while (true) delay(1000);
    }

    if (ioe.begin()) {
        Serial.printf("Using Cap LoRa-1262\n");
        LoRaName = "LoRa-1262";
        ioe.setDirection(0, true);      // Output
        ioe.setHighImpedance(0, false); // Disable high-impedance so pin can actually drive
        ioe.digitalWrite(0, true);      // High Level
    } else {
        Serial.printf("Using Cap LoRa868\n");
        LoRaName = "LoRa868";
    }

    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);

    // Init SX1262
    Serial.printf("[%s] Initializing ...", LoRaName);
    int state = radio.begin(LORA_FREQ, LORA_BW, LORA_SF, LORA_CR, LORA_SYNC_WORD, LORA_TX_POWER, LORA_PREAMBLE_LEN, 3.0, true);
    if (state == RADIOLIB_ERR_NONE) {
        Serial.println(F("Init success!"));
    } else {
        Serial.print(F("Init failed, code: "));
        Serial.println(state);
        while (true) { delay(10); }
    }
    radio.setCurrentLimit(140);// Current range: 0-140mA , step 2.5mA

    // Register callback function after receiving packet successfully
    radio.setPacketReceivedAction(setFlag);

    // Start listening for LoRa packets
    Serial.printf("[%s] Starting to listen ... ", LoRaName);
    state = radio.startReceive();
    if (state == RADIOLIB_ERR_NONE) {
        Serial.println(F("Listen successfully!"));
    } else {
        Serial.print(F("Listen failed, code: "));
        Serial.println(state);
        while (true) { delay(10); }
    }

    // If needed, 'listen' mode can be disabled by calling any of the following methods:
    // radio.standby()
    // radio.sleep()
    // radio.transmit();
    // radio.receive();
    // radio.scanChannel();
}

void loop()
{
    if (receivedFlag) {
        // reset flag
        receivedFlag = false;

        // Read received data as an Arduino String
        String gpsDataStr;
        int state = radio.readData(gpsDataStr);

        if (state == RADIOLIB_ERR_NONE) {
            gpsInfoParse(gpsDataStr);
            // Packet was successfully received
            Serial.printf("[%s] Received packet:\n", LoRaName);
            M5.Display.clear();

            // Data of the packet
            Serial.printf("[%s] Data:\t\t", LoRaName);
            Serial.println(gpsDataStr);

            // RSSI (Received Signal Strength Indicator)
            Serial.printf("[%s] RSSI:\t\t", LoRaName);
            Serial.print(radio.getRSSI());
            Serial.println(F(" dBm"));

            // SNR (Signal-to-Noise Ratio)
            Serial.printf("[%s] SNR:\t\t", LoRaName);
            Serial.print(radio.getSNR());
            Serial.println(F(" dB"));

            // Frequency error
            Serial.printf("[%s] Frequency error:\t", LoRaName);
            Serial.print(radio.getFrequencyError());
            Serial.println(F(" Hz"));

            // Display GPS Information
            M5.Display.setCursor(0,5);
            M5.Display.setTextColor(TFT_BLUE);
            M5.Display.printf("Received packet: ");
            M5.Display.setTextColor(TFT_WHITE);
            M5.Display.printf("#%s\n", Count);
            M5.Display.setTextColor(TFT_YELLOW);
            M5.Display.printf("Type: %s\n", Type);
            M5.Display.printf("Sat: %s\n", Sat);
            M5.Display.printf("Lat: %s\n", Lat);
            M5.Display.printf("Lng: %s\n", Lng);
            M5.Display.printf("Date: %s\n", Date);
            M5.Display.printf("Time: %s\n", Time);
        } else if (state == RADIOLIB_ERR_CRC_MISMATCH) {
            // Packet was received, but is malformed
            Serial.println(F("CRC error!"));

        } else {
            Serial.print(F("Receive failed, code: "));
            Serial.println(state);
        }
        // radio.startReceive();
    }
}
```

由于该产品 GPS 采用内置天线，无外置天线，请尽量在户外空旷区域使用发送设备，如操场、天台等，且初次使用等待时间较长，约为几分钟，请耐心等待设备成功搜索卫星与获取坐标。

上述例程成功运行结果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1177/cap_lora868_arduino_gps_lora.jpg" width="70%">

- 发送端串口返回信息：

```
=========================================
Location: satellites:17
GNSS Mode:GLN_Sat
22.687502,113.772232
Date/Time: 9/5/2025 01:31:06.00
[LoRa868] Sending GPS data:
 Type:GLN_Sat Count:120 Sat:17 Lat:22.687502 Lng:113.772232 Date:9/5/2025 Time:01:31:06.00
      Transmission finished!

```

- 接收端串口返回信息：

```
[LoRa868] Received packet:
[LoRa868] Data:		    Type:GLN_Sat Count:120 Sat:17 Lat:22.687502 Lng:113.772232 Date:9/5/2025 Time:01:31:06.00
[LoRa868] RSSI:		    -2.00 dBm
[LoRa868] SNR:		     6.50 dB
[LoRa868] Frequency error: -789.77 Hz
```
