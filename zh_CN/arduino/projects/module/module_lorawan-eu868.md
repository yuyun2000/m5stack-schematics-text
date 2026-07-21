# Module LoRaWAN-EU868 Arduino 使用教程

## 1. 准备工作

- 1\. 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 2\. 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5-LoRaWAN-RAK](https://github.com/m5stack/M5-LoRaWAN-RAK)

- 3\. 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Module LoRaWAN-EU868](https://shop.m5stack.com/products/m5stack-lorawan-eu868-module-stm32wle5)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"/> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/M148-Module-LoRaWAN-EU868-main-pictures_02.webp" width="20%"/>

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/module/Module_LoRaWAN-EU868)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="M148" type="MODULE"></ProductCompatible>

## 3. 引脚拨码开关

- 本教程中使用的主控设备为 CoreS3，搭配 Module LoRaWAN-EU868 实现无线通信，通信方式为串口通信，使用引脚为`G18 (RX)`、`G43 (TX)`、`G5 (RST)`。使用前请参考下图，将引脚拨码开关，切换到指定位置。

#> 说明 | 原理图及实物标注的引脚编号为 M5Core 系列主控适配引脚编号，实际使用时请根据主控设备的引脚定义进行确认。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_DIP.png" width="40%">

## 4. LoRa P2P

#> 说明 | 下方例程用于两套 Module LoRaWAN-EU868 设备之间的点对点通信测试，发送端和接收端的程序相同，均包含发送和接收功能。

```cpp line-num
#include <M5Unified.h>
#include "rak3172_p2p.hpp"

#define LORA_CONFIG_PRLEN 8
#define LORA_CONFIG_PWR   22
#define LORA_FREQ         868E6  // 868E6 equals to 868*10^6, which is the frequency 868M(Hz)
#define LORA_CR           0      // (4/5=0, 4/6=1, 4/7=2, 4/8=3)
#define LORA_SF           7      // (6, 7, 8, 9, 10, 11, 12)
#define LORA_BW           500    // (125, 250, 500)

#define LORA_RX 18
#define LORA_TX 43

RAK3172P2P lora;

void LoRaLoopTask(void* arg) {
    while (1) {
        lora.update();
        vTaskDelay(5);
    }
}

void setup() {
    M5.begin();
    pinMode(LORA_RST, OUTPUT);
    digitalWrite(LORA_RST, LOW);
    delay(100);
    digitalWrite(LORA_RST, HIGH);
    Serial.begin(115200);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    Serial.println("LoRa Init...");
    M5.Display.setCursor(5,0);
    M5.Display.printf("LoRa Init...\n");
    while (!lora.init(&Serial2, LORA_RX, LORA_TX, RAK3172_BPS_115200)) {
        delay(1000);
    }

    lora.setMode(P2P_RX_MODE, 0);
    if (lora.config(LORA_FREQ, LORA_SF, LORA_BW, LORA_CR, LORA_CONFIG_PRLEN, LORA_CONFIG_PWR)) {
        Serial.println("LoRa config success");
        M5.Display.printf("LoRa config success\n");
    } else {
        Serial.println("LoRa config failed");
        M5.Display.printf("LoRa config failed\n");
    }
    lora.setMode(P2P_TX_RX_MODE);
    xTaskCreate(LoRaLoopTask, "LoRaLoopTask", 1024 * 10, NULL, 2, NULL);
    M5.Display.setCursor(0, 40);
    M5.Display.printf("Touch screen to send \"Hello!\"\n");
}

void loop() {
    M5.update();
    if (M5.Touch.getCount() && M5.Touch.getDetail(0).wasClicked()) {
        M5.Display.fillRect(0, 0, 320, 70, TFT_BLACK);
        if (lora.print("Hello!")) {
        Serial.println("Send Hello! success");
        M5.Display.setCursor(0,0);
        M5.Display.printf("Send Hello! success\n");
        }
        M5.Display.setCursor(0, 40);
        M5.Display.printf("Touch screen to send \"Hello!\"\n");
    }

    if (lora.available()) {
        std::vector<p2p_frame_t> frames = lora.read();
        M5.Display.fillRect(0, 100, 320, 140, TFT_BLACK);
        M5.Display.setCursor(0, 100);
        M5.Display.printf("Received:\n");
        for (int i = 0; i < frames.size(); i++) {
        Serial.print(" RSSI: ");
        Serial.print(frames[i].rssi);
        M5.Display.printf("RSSI: %d\n", frames[i].rssi);
        Serial.print(" SNR: ");
        Serial.print(frames[i].snr);
        M5.Display.printf("SNR: %d\n", frames[i].snr);
        Serial.print(" LEN: ");
        Serial.print(frames[i].len);
        M5.Display.printf("LEN: %d\n", frames[i].len);
        Serial.print(" Payload: ");
        M5.Display.printf("Payload: ");
        for (uint8_t j = 0; j < frames[i].len; j++) {
            Serial.printf("%02X", frames[i].payload[j]);
            M5.Display.printf("%c", frames[i].payload[j]);
        }
        Serial.println();
        M5.Display.println();
        }
        lora.flush();
    }
} 
```

烧录案例程序后，可通过串口监视器查看输出日志，点击 CoreS3 屏幕发送数据，设备将会收到数据并显示在屏幕上。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_P2P.jpg" width="50%">

## 5. LoRaWAN

LoRaWAN 通信模式下，`设备需要连接到 LoRaWAN 网关才能实现数据交互`。得益于跳频技术的优势，这种接入方式能够同时管理更多的 LoRa 设备节点，并且可以提供一定的数据安全性保障。`在使用前，请您确认当前区域内存在公共 LoRaWAN 网关，若没有公共网关，用户也可自行搭建网关以实现连接。`

### 5.1 通信密钥

- 1\. 参考[TTN - 设备创建教程](/zh_CN/guide/lora/lorawan/ttn)，依据当前使用的设备频段创建节点，并获取对应的密钥信息。这些密钥信息包含 DevEUI、AppEUI（JoinEUI） 和 AppKey 等，不同的入网模式（OTAA / ABP）所使用的密钥内容也存在差异。这些密钥是设备接入 LoRaWAN 网络的`必要信息`。 

- 2\. 设置过程中可根据下方相关信息配置相应设置与设备类型（ClassA ~ C）。有关 LoRaWAN 介绍与设备配置信息介绍可参考[TTN - LoRaWAN Docs](https://www.thethingsnetwork.org/docs/lorawan/what-is-lorawan/)。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_TTN_cluster.png" width="70%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_setting.png" width="35%">

- 3\. 将在 TTN 或其他 LoRaWAN 服务器中获取的设备密钥信息填入案例程序中，然后编译案例并烧录至设备。

### 5.2 OTAA

```cpp line-num
#include <M5Unified.h>
#include "rak3172_lorawan.hpp"

#define APPEUI "****************"  // Application EUI (JoinEUI)
#define DEVEUI "****************"  // Device EUI
#define APPKEY "********************************"  // Application Key

#define LORA_RX 18
#define LORA_TX 43
#define LORA_RST 5

RAK3172LoRaWAN lorawan;
bool isJoin = false;

void joinCallback(bool status)
{
    isJoin = status;
    if (status) {
        Serial.println("[LoRaWAN] Join network successful!");
        M5.Display.printf("Join network successful!\nTouch screen to send\n");
        Serial.println("Device EUI: " + String(DEVEUI));
        lorawan.send("Device connected");
    } else {
        Serial.println("[LoRaWAN] Join network failed!");
    }
}

void sendCallback()
{
    Serial.println("[LoRaWAN] Uplink confirmed by server");
}

void errorCallback(char* error)
{
    Serial.print("[LoRaWAN] Error: ");
    Serial.println(error);
}

void LoRaWANLoopTask(void* arg)
{
    while (1) {
        lorawan.update();
        vTaskDelay(5);
    }
}

void setup()
{
    M5.begin();
    pinMode(LORA_RST, OUTPUT);
    digitalWrite(LORA_RST, LOW);
    delay(100);
    digitalWrite(LORA_RST, HIGH);
    Serial.begin(115200);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    Serial.println("[Init] Initialize LoRaWAN module...");
    M5.Display.setCursor(0,0);
    M5.Display.printf("Initialize LoRaWAN module...\n");
    while (!lorawan.init(&Serial2, LORA_RX, LORA_TX, RAK3172_BPS_115200)) {
        Serial.println("[Init] Failed to initialize module, retrying...");
        delay(1000);
    }
    Serial.println("Device Init OK");
    Serial.println("[Config] Set band to EU868...");
    M5.Display.printf("Device Init OK\nSet band to EU868...\n");
    // get or set the channel mask to close or open the channel (only for US915, AU915, CN470)
    while (!lorawan.setBAND(EU868)) {
        Serial.println(" failed, retrying...");
        delay(1000);
    }
    Serial.println("[Config] Set OTAA parameters...");
    M5.Display.printf("Set OTAA parameters...\n");
    while (!lorawan.setOTAA(DEVEUI, APPEUI, APPKEY)) {
        Serial.println(" failed, retrying...");
        delay(1000);
    }
    Serial.println("[Config] Set device mode to CLASS_C...");
    M5.Display.printf("Set device mode to CLASS_C...\n");
    while (!lorawan.setMode(CLASS_C)) {
        Serial.println(" failed, retrying...");
        delay(1000);
    }
    Serial.println("[Config] Set data rate to DR4...");
    M5.Display.printf("Set data rate to DR4...\n");
    while (!lorawan.setDR(4)) {
        Serial.println(" failed, retrying...");
        delay(1000);
    }
    Serial.println("[Config] Set Link check...");
    M5.Display.printf("Set Link check...\n");
    while (!lorawan.setLinkCheck(ALLWAYS_LINKCHECK)) {
        delay(1000);
    }

    lorawan.onSend(sendCallback);
    lorawan.onJoin(joinCallback);
    lorawan.onError(errorCallback);
    lorawan.flush();
    xTaskCreate(LoRaWANLoopTask, "LoRaWANLoopTask", 1024 * 10, NULL, 5, NULL);

    Serial.println("[Info] Attempting to join the network...");
    if (lorawan.join(true, false, 10, 10)) {
        Serial.println("Start Join...");
    } else {
        Serial.println("Join Fail");
    }
}

void loop()
{
    M5.update();
    if (M5.Touch.getCount() && M5.Touch.getDetail(0).wasClicked()) {
        if (isJoin) {
            String data = "UPlink LoRaWAN Frame: " + String(millis());
            if (lorawan.send(data)) {
                Serial.println("Send Successful");
                M5.Display.printf("Send Successful\n");
            } else {
                Serial.println("Send fail");
            }
        } else {
            Serial.println("LoRaWAN not joined");
        }
    }
    if (lorawan.available()) {
        std::vector<lorawan_frame_t> frames = lorawan.read();
        M5.Display.clear();
        M5.Display.setCursor(0, 0);
        M5.Display.printf("Received:\n");
        for (int i = 0; i < frames.size(); i++) {
            Serial.print("RSSI: ");
            Serial.println(frames[i].rssi);
            M5.Display.printf("RSSI: %d\n", frames[i].rssi);
            Serial.print("SNR: ");
            Serial.println(frames[i].snr);
            M5.Display.printf("SNR: %d\n", frames[i].snr);
            Serial.print("LEN: ");
            Serial.println(frames[i].len);
            M5.Display.printf("LEN: %d\n", frames[i].len);
            Serial.print("PORT: ");
            Serial.println(frames[i].port);
            M5.Display.printf("PORT: %d\n", frames[i].port);
            Serial.print("UNITCAST: ");
            Serial.println(frames[i].unicast);
            M5.Display.printf("UNITCAST: %d\n", frames[i].unicast);
            Serial.print("Payload: ");
            M5.Display.printf("Payload: ");
            for (uint8_t j = 0; j < frames[i].len; j++) {
                Serial.printf("%02X", frames[i].payload[j]);
                M5.Display.printf("%c", frames[i].payload[j]);
            }
            Serial.println();
            M5.Display.println();
        }
        lorawan.flush();
    }
    if (Serial.available()) {             // If the serial port reads data.
        String ch = Serial.readString();  // Copy the data read from the serial port
        lorawan.sendCommand(ch);
    }
}
```

烧录上述例程成功过后，点击 CoreS3 屏幕发送数据，设备将会连接 LoRaWAN 网络并发送数据；在 TTN 控制台 `Messaging` 中 `Playload` 处输入 `48 65 6C 6C 6F 21`（十六进制字符串，代表 ASCII 字符串 "Hello!"），点击 `Schedule downlink` 按钮后，设备将会收到数据并显示在屏幕上。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_TTN_messaging.png" width="70%">

- 串口监视器输出日志如下所示：

```
[Init] Initializing LoRaWAN module...
Device Init OK
[Config] Setting band to EU868...
[Config] Setting OTAA parameters...
[Config] Setting device mode to CLASS_C...
[Config] Setting data rate to DR4...
[Config] Setting Link check...
[Info] Attempting to join the network...
Start Join...
[LoRaWAN] Join network successful!
Device EUI: XXXXXXXXXXXXXXXX
Send Successful
RSSI: -57
SNR: 11
LEN: 6
PORT: 1
UNITCAST: 1
Payload: 48656C6C6F21
```

- CoreS3 屏幕显示如下所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_OTAA_1.jpg" width="35%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_OTAA_2.jpg" width="35%">

- TTN 控制台日志显示如下所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_OTAA_live_data.png" width="70%">

### 5.3 ABP

?> 注意事项 | ABP 模式下，TTN 服务器 LoRaWAN 协议为了防重放攻击，使用了两个帧计数器：FCntUp：上行帧计数器（设备→网关）、
FCntDown：下行帧计数器（网关→设备），TTN 服务器会严格检查新收到的 FCntUp 是否大于上一次记录的 FCntUp，否则会被当作重放攻击而直接丢弃，导致设备在重启后（设备端 FCntUp 归零）无法正常与 TTN 通信。请在 TTN Console 对应设备的 `Settings` 中，在 `Network layer` 中找到 `Custom MAC settings`，勾选 `Resets frame counters`（Frame counter resets） 选项（如下图所示），以允许 TTN 在设备重启后重置帧计数器，从而避免上述问题。  
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_ABP_counter.png" width="40%">

```cpp line-num
#include <M5Unified.h>
#include "rak3172_lorawan.hpp"

#define DEVADDR "260B8AF9"             // Device Address
#define NWKSKEY "E87AA07838189048FF31AD51BB9843D1"  // Network Session Key
#define APPSKEY "7D887F47B374962E0A83C4BD2E11D2E8"  // Application Session Key

#define LORA_RX 18
#define LORA_TX 43
#define LORA_RST 5

RAK3172LoRaWAN lorawan;

void errorCallback(char* error)
{
    Serial.print("[LoRaWAN] Error: ");
    Serial.println(error);
}

void LoRaWANLoopTask(void* arg)
{
    while (1) {
        lorawan.update();
        vTaskDelay(5);
    }
}

void setup()
{
    M5.begin();
    pinMode(LORA_RST, OUTPUT);
    digitalWrite(LORA_RST, LOW);
    delay(100);
    digitalWrite(LORA_RST, HIGH);
    Serial.begin(115200);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    Serial.println("[Init] Initialize LoRaWAN module...");
    M5.Display.printf("Initialize LoRaWAN module...\n");
    while (!lorawan.init(&Serial2, LORA_RX, LORA_TX, RAK3172_BPS_115200)) {
        Serial.println("[Init] Failed to initialize module, retrying...");
        delay(1000);
    }
    Serial.println("Device Init OK");
    Serial.println("[Config] Set band to EU868...");
    M5.Display.printf("Device Init OK\nSet band to EU868...\n");
    // get or set the channel mask to close or open the channel (only for US915, AU915, CN470)
    while (!lorawan.setBAND(EU868)) {
        Serial.println(" failed, retrying...");
        delay(1000);
    }
    Serial.println("[Config] Set ABP parameters...");
    M5.Display.printf("Set ABP parameters...\n");
    while (!lorawan.setABP(DEVADDR, NWKSKEY, APPSKEY)) {
        Serial.println(" failed, retrying...");
        delay(1000);
    }
    Serial.println("[Config] Set device mode to CLASS_C...");
    M5.Display.printf("Set device mode to CLASS_C...\n");
    while (!lorawan.setMode(CLASS_C)) {
        Serial.println(" failed, retrying...");
        delay(1000);
    }
    Serial.println("[Config] Set data rate to DR4...");
    M5.Display.printf("Set data rate to DR4...\n");
    while (!lorawan.setDR(4)) {
        Serial.println(" failed, retrying...");
        delay(1000);
    }
    Serial.println("[Config] Set Link check...");
    M5.Display.printf("Set Link check...\n");
    while (!lorawan.setLinkCheck(ALLWAYS_LINKCHECK)) {
        delay(1000);
    }
    delay(2000);
    Serial.println("[Config] Link successful!");
    M5.Display.printf("Link successful!\nTouch screen to send\n");
    lorawan.send("Device connected");

    lorawan.onError(errorCallback);
    lorawan.flush();
    xTaskCreate(LoRaWANLoopTask, "LoRaWANLoopTask", 1024 * 10, NULL, 5, NULL);
}

void loop()
{
    M5.update();
    if (M5.Touch.getCount() && M5.Touch.getDetail(0).wasClicked()) {
        String data = "UPlink LoRaWAN Frame: " + String(millis());
        if (lorawan.send(data)) {
            Serial.println("Send Successful");
            M5.Display.printf("Send Successful\n");
        } else {
            Serial.println("Send fail");
        }
    }

    if (lorawan.available()) {
        std::vector<lorawan_frame_t> frames = lorawan.read();
        M5.Display.clear();
        M5.Display.setCursor(0, 0);
        M5.Display.printf("Received:\n");
        for (int i = 0; i < frames.size(); i++) {
            Serial.print("RSSI: ");
            Serial.println(frames[i].rssi);
            M5.Display.printf("RSSI: %d\n", frames[i].rssi);
            Serial.print("SNR: ");
            Serial.println(frames[i].snr);
            M5.Display.printf("SNR: %d\n", frames[i].snr);
            Serial.print("LEN: ");
            Serial.println(frames[i].len);
            M5.Display.printf("LEN: %d\n", frames[i].len);
            Serial.print("PORT: ");
            Serial.println(frames[i].port);
            M5.Display.printf("PORT: %d\n", frames[i].port);
            Serial.print("UNITCAST: ");
            Serial.println(frames[i].unicast);
            M5.Display.printf("UNITCAST: %d\n", frames[i].unicast);
            Serial.print("Payload: ");
            M5.Display.printf("Payload: ");
            for (uint8_t j = 0; j < frames[i].len; j++) {
                Serial.printf("%02X", frames[i].payload[j]);
                M5.Display.printf("%c", frames[i].payload[j]);
            }
            Serial.println();
            M5.Display.println();
        }
        lorawan.flush();
    }
    if (Serial.available()) {             // If the serial port reads data.
        String ch = Serial.readString();  // Copy the data read from the serial port
        lorawan.sendCommand(ch);
    }
}
```

烧录上述例程成功过后，同理 OTAA，点击 CoreS3 屏幕发送数据，设备将会连接 LoRaWAN 网络并发送数据；在 TTN 控制台 `Messaging` 中 `Playload` 处输入 `48 65 6C 6C 6F 21`（十六进制字符串，代表 ASCII 字符串 "Hello!"），点击 `Schedule downlink` 按钮后，设备将会收到数据并显示在屏幕上。

- 串口监视器输出日志如下所示：

```
[Init] Initialize LoRaWAN module...
Device Init OK
[Config] Set band to EU868...
[Config] Set ABP parameters...
[Config] Set device mode to CLASS_C...
[Config] Set data rate to DR4...
[Config] Set Link check...
[Config] Link successful!
Send Successful
RSSI: -44
SNR: 5
LEN: 6
PORT: 1
UNITCAST: 1
Payload: 48656C6C6F21
```

- CoreS3 屏幕显示如下所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_ABP_1.jpg" width="35%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_ABP_2.jpg" width="35%">

- TTN 控制台日志显示如下所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1235/module_lorawan-eu868_ABP_live_data.png" width="70%">
