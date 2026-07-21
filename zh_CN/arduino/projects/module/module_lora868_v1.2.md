# Module LoRa868 v1.2 Arduino 使用教程


## 1.准备工作

- 1.环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成IDE安装, 并根据实际使用的开发板安装对应的板管理, 与需要的驱动库。

- 2.使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [RadioLib](https://github.com/jgromes/RadioLib)

- 3.使用到的硬件产品:
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Module LoRa868 v1.2](https://shop.m5stack.com/products/lora-module-868mhz-v1-2)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/639/M029-V12_04.webp" width="20%">



## 2.案例程序

#>案例说明| 本案例采用 2 个 Module LoRa868 v1.2 模块与 2 个 CoreS3 主控，分别烧录相同的 LoRa 收发测试程序，用于实现点对点的数据通信。在与其他主控板配合使用时，请根据具体硬件连接情况，在程序中配置相应的 IO 引脚信息。此外，Module LoRa868 v1.2 支持通过底部的 DIP 拨码开关灵活切换引脚映射，可根据实际应用需求进行调整以兼容不同的主控设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/639/arduino_module_lora868_v1.2_dip_switch_01.jpg" width="60%">

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>
#include <M5Unified.h>
#include <RadioLib.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define LORA_BW 500.0
#define LORA_SF 7
#define LORA_CR 8

#define LORA_FREQ         868.0
#define LORA_SYNC_WORD    0x34
#define LORA_TX_POWER     22
#define LORA_PREAMBLE_LEN 20

#define CONFIG_MISO_GPIO GPIO_NUM_35
#define CONFIG_MOSI_GPIO GPIO_NUM_37
#define CONFIG_SCLK_GPIO GPIO_NUM_36

#define CONFIG_LORA_NSS  GPIO_NUM_1
#define CONFIG_LORA_BUSY GPIO_NUM_2
#define CONFIG_LORA_RST  GPIO_NUM_7
#define CONFIG_LORA_IRQ  GPIO_NUM_10

SX1262 *radio = NULL;

// save transmission states between loops
int transmissionState = RADIOLIB_ERR_NONE;

// flag to indicate transmission or reception state
bool transmitFlag = false;

volatile bool operationDone = false;

ICACHE_RAM_ATTR void setFlag(void)
{
    // we sent or received a packet, set the flag
    operationDone = true;
}

void lora_init()
{
    radio = new SX1262(new Module(CONFIG_LORA_NSS,     // NSS
                                  CONFIG_LORA_IRQ,     // DIO1
                                  CONFIG_LORA_RST,     // RST
                                  CONFIG_LORA_BUSY));  // BUSY

    M5.Display.println("LoRa init...");

    //   RADIOLIB_ERR_NONE
    int state = radio->begin(LORA_FREQ, LORA_BW, LORA_SF, LORA_CR, LORA_SYNC_WORD, LORA_TX_POWER, LORA_PREAMBLE_LEN,
                             3.0, false);

    radio->setDio1Action(setFlag);

    // radio->setPacketReceivedAction(lora_set_rx_flag);
    // radio->setPacketSentAction(lora_set_tx_flag);

    Serial.print(F("Starting to listen ... "));
    state = radio->startReceive();
    if (state == RADIOLIB_ERR_NONE) {
        Serial.println(F("success!"));
        M5.Display.println("LoRa int success");
        M5.Display.println("Touch to send packet");
    } else {
        Serial.print(F("failed, code "));
        M5.Display.println("LoRa init failed");
        Serial.println(state);
        while (true) {
            delay(10);
        }
    }
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    M5.Display.setTextColor(YELLOW);
    M5.Display.setFont(&fonts::FreeSansBold9pt7b);
    M5.Display.setTextScroll(true);
    lora_init();
}

int msg_count = 0;
String tx_payload;
String rx_payload;
void loop()
{
    M5.update();
    auto t = M5.Touch.getDetail();

    if (t.wasClicked() || M5.BtnA.wasClicked()) {
        // send another one
        msg_count++;
        Serial.print(F("Sending another packet ... "));

        tx_payload = "Hello LoRa Count: " + String(msg_count);
        // transmissionState = radio->startTransmit(Payload);
        transmissionState = radio->transmit(tx_payload);
        M5.Display.println("Sending packet!");
        M5.Display.println(tx_payload);
        transmitFlag = true;
    }
    // check if the previous operation finished
    if (operationDone) {
        // reset flag
        operationDone = false;
        if (transmitFlag) {
            transmitFlag = false;
            int state    = radio->startReceive();
        } else {
            int state = radio->readData(rx_payload);
            Serial.println("lora_rx_flag");
            Serial.println(state);
            if (state == RADIOLIB_ERR_NONE) {
                // packet was successfully received
                Serial.println(F("Received packet!"));

                // print data of the packet
                Serial.print(F("Data:\t\t"));
                Serial.println(rx_payload);

                // print RSSI (Received Signal Strength Indicator)
                Serial.print(F("RSSI:\t\t"));
                Serial.print(radio->getRSSI());
                Serial.println(F(" dBm"));

                // print RSSI (Received Signal Strength Indicator)
                Serial.print(F("Length:\t\t"));
                Serial.print(radio->getPacketLength());

                // print SNR (Signal-to-Noise Ratio)
                Serial.print(F("SNR:\t\t"));
                Serial.print(radio->getSNR());
                Serial.println(F(" dB"));

                // packet was successfully received
                M5.Display.println("Received packet!");

                // print data of the packet
                M5.Display.println("Data:");
                M5.Display.println(rx_payload);

                // print RSSI (Received Signal Strength Indicator)
                M5.Display.print("RSSI:");
                M5.Display.print(radio->getRSSI());
                M5.Display.println(" dBm");

                // print SNR (Signal-to-Noise Ratio)
                M5.Display.print("SNR:");
                M5.Display.print(radio->getSNR());
                M5.Display.println(" dB");
            }
        }
    }
}
```

## 3.编译上传

- 1.下载模式: 不同设备进行程序烧录前需要下载模式, 不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表, 查看具体的操作方式。

- CoreS3长按复位按键(大约2秒)直到内部绿色LED灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="50%">


- 2.选中设备端口, 点击Arduino IDE左上角编译上传按钮, 等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/639/arduino_module_lora868_v1.2_example_01.jpg" width="70%">

## 4.LoRa收发测试

2 组 CoreS3 + Module LoRa868 v1.2 设备分别烧录相同的 LoRa 收发测试程序后，触摸屏幕进行数据发送测试。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/639/arduino_module_lora868_v1.2_example_02.jpg" width="70%">

