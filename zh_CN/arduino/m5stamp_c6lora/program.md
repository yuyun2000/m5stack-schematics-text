# Stamp C6LoRa Arduino 示例程序编译与烧录 

## 1.准备工作

- 1.Arduino IDE安装： 参考[Arduino IDE安装教程](/zh_CN/arduino/arduino_ide)，完成IDE安装。
- 2.板管理安装: 参考[基本环境搭建教程](/zh_CN/arduino/arduino_board)，完成M5Stack板管理安装并选择开发板`M5StampC6LoRa`。
- 3.依赖库安装：参考[库管理安装教程](/zh_CN/arduino/arduino_library)，完成最新版 `M5Unified`、`M5GFX`、`RadioLib` 驱动库安装，并根据提示安装全部依赖库。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/arduino_stamp_c6lora_select_board.png" width="70%" />

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/arduino_stamp_c6lora_lib_01.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/arduino_stamp_c6lora_lib_02.png" width="70%" />
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/arduino_stamp_c6lora_lib_03.png" width="70%" />

## 2.烧录方式

Stamp C6LoRa 支持通过 UART 或 USB 接口下载程序，下载前需要控制 Boot 引脚 (GPIO9) 保持低电平，然后复位模组使其进入下载模式。

- 通过 UART 方式下载需搭配 USB-TTL 转接板，下方接线示意图以 [ESP32 Downloader](https://shop.m5stack.com/products/esp32-downloader-kit) 转接板为例连接 Stamp C6LoRa 的 UART 程序下载接口。 
- ESP32 Downloader 带自动下载电路，烧录程序运行时将自动控制模组进入下载模式。
- 通过 USB 方式下载，需控制 Boot 引脚保持低电平的状态，通过 RST 引脚复位模组 (低电平->高电平)，进入下载模式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/stamp_c6lora_download.png" width="90%" />


进入下载模式后，可在Arduino IDE中可选中对应设备的端口进行烧录。

## 3.程序编译&烧录

在 Arduino IDE 工作区粘贴下方代码, 点击上传按钮，将自动进行程序编译与烧录。

#> 日志输出 | `Tools`->`USB CDC On Boot` 选项默认为 `Enabled`，模组默认日志将输出至 USB 接口，若需要将日志切换输出至 UART0，可将该选项设置为 `Disabled`

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/arduino_stamp_c6lora_select_cdc_onboot.png" width="70%" />

### Hello World

```cpp line-num
#include "Arduino.h"

void setup()
{
    Serial.begin(115200);
}

void loop()
{
    delay(1000);
    Serial.println("Hello, world!");
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/arduino_stamp_c6lora_example_01.png" width="70%">

### LoRa Ping Pong 

以下为 LoRa Ping Pong 测试程序，需使用**两组 Stamp C6LoRa 模组**, 模组**先后间隔上电**后，将自动互相进行收发测试:

- 示例程序中 **LORA_IRQ 使用 GPIO7 作为中断信号接收引脚**，测试时请将模组的 **LORA_IRQ 引脚连接至 GPIO7**。
- 使用前需连接好 LoRa 天线，避免损坏射频电路。


```cpp line-num
#include <Arduino.h>
#include <SPI.h>
#include <RadioLib.h>
#include <M5Unified.h>
#include "utility/PI4IOE5V6408_Class.hpp"

// Stamp C6LoRa board mapping
#define I2C_SDA_PIN 10
#define I2C_SCL_PIN 8

// SX1262 base pins on Stamp C6LoRa
#define SX1262_MOSI_PIN 21
#define SX1262_MISO_PIN 22
#define SX1262_SCK_PIN  20
#define SX1262_CS_PIN   23
#define SX1262_IRQ_PIN  7
#define SX1262_BUSY_PIN 19

// PI4IOE5V6408 -> SX1262 control lines
#define SX_LNA_EN_PIN 5
#define SX_ANT_SW_PIN 6
#define SX_NRST_PIN   7

// SX1262: CS, IRQ(DIO1), NRST, BUSY
SX1262 radio = new Module(SX1262_CS_PIN, SX1262_IRQ_PIN, RADIOLIB_NC, SX1262_BUSY_PIN);

m5::I2C_Class i2c_bus_0;
// Stamp C6LoRa uses PI4IOE5V6408 at 0x43 to control SX1262 power path
m5::PI4IOE5V6408_Class ioe(0x43, 400000, &i2c_bus_0);

// save transmission state between loops
int transmissionState = RADIOLIB_ERR_NONE;

// flag to indicate transmission/reception state
bool transmitFlag = false;

// flag to indicate that a packet was sent/received
volatile bool operationDone = false;

void setFlag(void)
{
    operationDone = true;
}

static bool initIoExpanderAndRfPath()
{
    if (!i2c_bus_0.begin(I2C_NUM_0, I2C_SDA_PIN, I2C_SCL_PIN)) {
        Serial.println("[I2C] begin failed");
        return false;
    }

    if (!ioe.begin()) {
        Serial.println("[IOE] PI4IOE5V6408 begin failed");
        return false;
    }

    ioe.setHighImpedance(SX_NRST_PIN, false);
    ioe.setHighImpedance(SX_ANT_SW_PIN, false);
    ioe.setHighImpedance(SX_LNA_EN_PIN, false);
    ioe.setDirection(SX_NRST_PIN, true);
    ioe.setDirection(SX_ANT_SW_PIN, true);
    ioe.setDirection(SX_LNA_EN_PIN, true);
    delay(100);

    // SX1262 reset and RF path enable sequence.
    ioe.digitalWrite(SX_NRST_PIN, false);
    delay(100);
    ioe.digitalWrite(SX_NRST_PIN, true);
    ioe.digitalWrite(SX_ANT_SW_PIN, true);
    ioe.digitalWrite(SX_LNA_EN_PIN, true);
    delay(10);

    return true;
}

void setup()
{
    Serial.begin(115200);
    delay(300);
    Serial.println("\n[Stamp C6LoRa] RadioLib ping-pong start");

    SPI.begin(SX1262_SCK_PIN, SX1262_MISO_PIN, SX1262_MOSI_PIN, SX1262_CS_PIN);

    if (!initIoExpanderAndRfPath()) {
        while (true) {
            delay(1000);
        }
    }

    Serial.print("[SX1262] Initializing... ");
    int state = radio.begin(868.0, 125.0, 12, 5, 0x34, 22, 20, 3.0, true);
    if (state != RADIOLIB_ERR_NONE) {
        Serial.print("failed, code: ");
        Serial.println(state);
        while (true) {
            delay(1000);
        }
    }
    Serial.println("ok");

    // One callback handles both TX done and RX done on SX1262 DIO1.
    radio.setDio1Action(setFlag);

    // Send first PING packet.
    Serial.print("[SX1262] Sending first packet... ");
    transmissionState = radio.startTransmit("PING");
    if (transmissionState == RADIOLIB_ERR_NONE) {
        Serial.println("ok");
        transmitFlag = true;
    }
}

void loop()
{
    // check if the previous operation finished
    if (operationDone) {
        // reset flag
        operationDone = false;

        if (transmitFlag) {
            // the previous operation was transmission, listen for response
            // print the result
            if (transmissionState == RADIOLIB_ERR_NONE) {
                // packet was successfully sent
                Serial.println(F("transmission finished!"));

            } else {
                Serial.print(F("failed, code "));
                Serial.println(transmissionState);
            }

            // listen for response
            radio.startReceive();
            transmitFlag = false;

        } else {
            // the previous operation was reception
            // print data and send another packet
            String str;
            int state = radio.readData(str);

            if (state == RADIOLIB_ERR_NONE) {
                // packet was successfully received
                Serial.println(F("[SX1262] Received packet!"));

                // print data of the packet
                Serial.print(F("[SX1262] Data:\t\t"));
                Serial.println(str);

                // print RSSI (Received Signal Strength Indicator)
                Serial.print(F("[SX1262] RSSI:\t\t"));
                Serial.print(radio.getRSSI());
                Serial.println(F(" dBm"));

                // print SNR (Signal-to-Noise Ratio)
                Serial.print(F("[SX1262] SNR:\t\t"));
                Serial.print(radio.getSNR());
                Serial.println(F(" dB"));
            }

            // wait a second before transmitting again
            delay(1000);

            // send another one
            Serial.print(F("[SX1262] Sending another packet ... "));
            transmissionState = radio.startTransmit("Hello World!");
            transmitFlag      = true;
        }
    }
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1223/arduino_stamp_c6lora_example_02.png" width="70%">


## 4. API

Stamp C6LoRa 使用了`RadioLib`库作为 LoRa 驱动，更多相关的 API 可以参考下方文档：

- [RadioLib Library - GitHub](https://github.com/jgromes/RadioLib)
- [RadioLib Wiki - GitHub](https://github.com/jgromes/RadioLib/wiki/Basics)
- [RadioLib Docs](https://jgromes.github.io/RadioLib/index.html)
- [RadioLib SX1262 Docs](https://jgromes.github.io/RadioLib/class_s_x126x.html)

