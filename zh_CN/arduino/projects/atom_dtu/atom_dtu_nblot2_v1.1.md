# Atom DTU NBIoT2 v1.1 Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5IOE1](https://github.com/m5stack/M5IOE1)
  - [TinyGSM](https://github.com/m5stack/TinyGSM)
  - [PubSubClient](https://github.com/knolleary/pubsubclient)
  - [ArduinoHttpClient](https://github.com/arduino-libraries/ArduinoHttpClient)
  - [StreamDebugger](https://github.com/vshymanskyy/StreamDebugger)

\#> 注意 | 需要在 GitHub 上下载最新的库版本，库地址: [TinyGSM - M5Stack GitHub](https://github.com/m5stack/TinyGSM)，请勿在 Arduino Library 中下载。（如有疑问，请参考[此教程](/zh_CN/arduino/arduino_library#git%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85)）

- 3\. 使用到的硬件产品:
  - [AtomS3R](https://shop.m5stack.com/products/atoms3r-dev-kit)
  - [Atom DTU NBIoT2 v1.1](https://shop.m5stack.com/products/atomic-dtu-nb-iot2-global-version-v1-1-sim7028?variant=47382416130305)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/AtomS3R/3.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/A106-V21-main_pictures_02.jpg" width="20%">

## 2. 注意事项

\#> SIM 卡兼容性 | 本模块需使用 Micro SIM 规格的**物联网卡**，请确保卡片支持 Cat-M1 或 NB-IoT 网络，并建议优先选用经过以下运营商认证的卡片：Deutsche Telekom、Vodafone、Telefonica 以及中国电信、中国移动、中国联通。

!> 注意 | 请勿在未断开电源的情况下对物联网卡进行插拔，或者把同一张 SIM 卡在不同的设备中使用，否则可能会触发物联网卡自动锁卡而联网失败，锁卡后需要联系运营商解除。

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/atom/Atom_DTU_NBIoT2_v1.1)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="A106-V21" type="ATOMIC"></ProductCompatible>

## 3. 案例程序

- 本教程中使用的主控设备为 AtomS3，搭配 Atom DTU NBIoT v1.1。本模块采用串口的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的串口 IO 为 `G5 (TX)`、`G6 (RX)`，RS485 IO 为 `G7 (TX)`，`G8 (RX)`（下方例程中定义后未实际使用）。

\#> 说明 | 下方例程默认使用 SIM 卡的 CAT 模式，若需要切换至 NB-Iot 模式，请把 `TinyGSM` 库中 `TinyGsmClientSIM7028.h` 文件 **line 32** 的 `MODE_NB_IOT` 的宏定义注释去掉；如果需要 debug ，同理可将 `TINY_GSM_DEBUG` 及下方代码中的 `DUMP_AT_COMMANDS` 宏定义取消注释。

### 3.1 MQTT

```cpp line-num
#include "M5Unified.h"
#define TINY_GSM_MODEM_SIM7028  // Specify to use SIM7028 module; TinyGsm library adapts instruction set based on this macro, must be placed here
#include "PubSubClient.h"
#include "TinyGsmClient.h"
#include "StreamDebugger.h"
#include "M5IOE1.h"

#define SerialMon        Serial             // MCU -> PC for log output
#define MONITOR_BAUDRATE 115200
#define SerialAT         Serial1            // MCU <-> SIM7028 module communication
#define SIM7028_BAUDRATE 115200
#define SIM7028_RESET    -1
#define MCU_TX           5
#define MCU_RX           6
#define RS485_TX         7
#define RS485_RX         8
#define IO_SCL           39
#define IO_SDA           38
#define MQTT_BROKER      "mqtt.m5stack.com" // MQTT broker address
#define MQTT_PORT        1883               // MQTT service port
#define mqtt_devid       "XXXXXXXX"         // MQTT client ID
#define mqtt_pubid       "XXXXXXXX"         // MQTT username
#define mqtt_password    "XXXXXXXX"         // MQTT authentication key
#define UPLOAD_INTERVAL  10000              // Data upload interval, 10s

// M5IOE1 device instance
M5IOE1 ioe1;

// M5IOE1 I2C address (default 0x6F)
#define I2C_ADDR M5IOE1_DEFAULT_ADDR

// Pin definitions for M5IOE1 GPIOs
#define SIM_PWR_EN M5IOE1_PIN_9
#define SIM_RST M5IOE1_PIN_11
#define VIN_ADC M5IOE1_PIN_2

// If you need to see log detail, you can open the following macro definition
// #define DUMP_AT_COMMANDS
// If you need to debug, you can open the following macro definition in TinyGsmClientSIM7028.h line 13
// #define TINY_GSM_DEBUG Serial
#ifdef DUMP_AT_COMMANDS
StreamDebugger debugger(SerialAT, SerialMon);
TinyGsm modem(debugger);
#else
TinyGsm modem(SerialAT);
#endif

TinyGsmClient tcpClient(modem); // Create TCP client based on TinyGsm (MQTT relies on TCP connection)
PubSubClient mqttClient(MQTT_BROKER, MQTT_PORT, tcpClient); // Create MQTT client instance (specify broker, port and TCP client)

void mqttCallback(char *topic, byte *payload, unsigned int len); // Callback function for receiving MQTT messages
bool mqttConnect(void); // Function to establish MQTT connection
void nbConnect(void);   // Function to initialize SIM7028 and connect to NB-IoT network

const char* topicSub = "Atom DTU NBIoT v1.1 Receive"; // MQTT topic for receiving messages (replace with your actual subscribe topic)
const char* topicPub = "Atom DTU NBIoT v1.1 Send";    // MQTT topic for sending messages (replace with your actual publish topic)
int         num               = 0; // Counter for published messages
uint32_t lastReconnectAttempt = 0; // Timestamp for last MQTT reconnection attempt (avoid frequent retries)
bool lastMqttState = false; // Track MQTT connection status
const char apn[] = "cmnbiot";

void log(String info)
{
    SerialMon.println(info);
}

void SIM7028_EN()
{
    if (ioe1.begin(&Wire, I2C_ADDR, IO_SDA, IO_SCL, M5IOE1_I2C_FREQ_100K, M5IOE1_INT_MODE_POLLING) == M5IOE1_OK){
        ioe1.pinMode(SIM_PWR_EN, OUTPUT);
        ioe1.digitalWrite(SIM_PWR_EN, HIGH); // Enable SIM power
        delay(100);
        ioe1.pinMode(SIM_RST, OUTPUT);
        ioe1.digitalWrite(SIM_RST, LOW); // SIM reset
        delay(100);
        ioe1.digitalWrite(SIM_RST, HIGH);
        log("SIM power enabled");
    }
    else{
        log("Failed to enable SIM power");
    }
}

void setup()
{
    M5.begin();
    SerialMon.begin(115200);
    SerialMon.println(">>SIM7028 MQTT TEST");
    SerialAT.begin(SIM7028_BAUDRATE, SERIAL_8N1, MCU_RX, MCU_TX);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setTextDatum(middle_center);
    M5.Display.drawString("NBIoT MQTT", M5.Display.width() / 2, 10);
    M5.Display.drawString("Init...", M5.Display.width() / 2, 60);
    delay(500);
    SIM7028_EN();
    nbConnect(); // Initialize SIM7028 module and connect to network
    mqttClient.setServer(MQTT_BROKER, MQTT_PORT);  // Set MQTT broker address and port
    mqttClient.setKeepAlive(120);                  // MQTT keep-alive interval (120 seconds)
    mqttClient.setSocketTimeout(15000);            // TCP connection timeout (15 seconds)
    mqttClient.setCallback(mqttCallback);          // Register MQTT message receive callback
}

void loop()
{
    static unsigned long timer = 0;
    M5.update();

    // Check for MQTT connection status change (connected <-> disconnected)
    if (mqttClient.connected() != lastMqttState) {
        if (mqttClient.connected()) {
            log("=== MQTT CONNECTED ===");
            M5.Display.fillRect(0, 20, 128, 20, TFT_BLACK);
            M5.Display.setTextColor(TFT_GREEN);
            M5.Display.drawString("CONNECTED", M5.Display.width() / 2, 30);
        } else {
            log("=== MQTT DISCONNECTED ===");
            M5.Display.fillRect(0, 20, 128, 20, TFT_BLACK);
            M5.Display.setTextColor(TFT_RED);
            M5.Display.drawString("DISCONNECTED", M5.Display.width() / 2, 30);
        }
        lastMqttState = mqttClient.connected();
    }

    // MQTT reconnection logic (retry every 3 seconds if disconnected)
    if (!mqttClient.connected()) {
        log(">> MQTT NOT CONNECTED");
        log("MQTT state code: " + String(mqttClient.state()));
        M5.Display.fillRect(0, 20, 128, 20, TFT_BLACK);
        M5.Display.setTextColor(TFT_RED);
        M5.Display.drawString("DISCONNECTED", M5.Display.width() / 2, 30);
        uint32_t t = millis();
        if (t - lastReconnectAttempt > 3000L) {
            lastReconnectAttempt = t;
            if (mqttConnect()) {
                lastReconnectAttempt = 0;
            }
        }
        delay(100);
    }

    // Periodic data publishing (triggered when timer expires)
    if (millis() >= timer) {
        timer = millis() + UPLOAD_INTERVAL;
        if (mqttClient.connected()) {
            char jsonBuf[256];
            snprintf(jsonBuf, sizeof(jsonBuf), "SIM7028 MQTT #%d", num);
            log(">> [MQTT SEND] Topic: " + String(topicPub));
            log("Info: " + String(jsonBuf));
            mqttClient.publish(topicPub, jsonBuf);
            M5.Display.fillRect(0, 40, 128, 40, TFT_BLACK);
            M5.Display.setTextColor(TFT_WHITE);
            M5.Display.drawString("Send:", M5.Display.width() / 2, 50);
            M5.Display.drawString("#" + String(num++), M5.Display.width() / 2, 70);
        }
    }

    mqttClient.loop();// Process MQTT incoming messages, maintain connection and handle keep-alive
    delay(10);
}

void mqttCallback(char *topic, byte *payload, unsigned int len)
{
    String payloadStr;
    for (unsigned int i = 0; i < len; i++) {
        payloadStr += (char)payload[i];
    }
    log(">> [MQTT RECEIVE] Topic: " + String(topic) + "\nInfo: " + payloadStr);
    M5.Display.fillRect(0, 90, 128, 38, TFT_BLACK);
    M5.Display.setTextColor(TFT_WHITE);
    M5.Display.drawString("Rece:", M5.Display.width() / 2, 90);
    M5.Display.drawString(String(payloadStr), M5.Display.width() / 2, 110);
}

bool mqttConnect(void)
{
    log(">> Connecting to MQTT broker: " + String(MQTT_BROKER));
    bool status = mqttClient.connect(mqtt_devid, mqtt_pubid, mqtt_password);
    if (!status) {
        log("!! MQTT Connection FAILED, code: " + String(mqttClient.state()));
        return false;
    }
    log(">> MQTT CONNECTED, subscribing: " + String(topicSub));
    mqttClient.subscribe(topicSub);
    return true;
}

void nbConnect(void)
{
    unsigned long start = millis();
    log("Initializing modem...");
    while (!modem.init()) {
        log("waiting...." + String((millis() - start) / 1000) + "s");
    };

    start = millis();
    log("Waiting for network...");
    while (!modem.waitForNetwork()) {
        log("waiting...." + String((millis() - start) / 1000) + "s");
    }
    log("success");

    log("Waiting for GPRS connect...");
    if (!modem.gprsConnect(apn)) {
        log("waiting...." + String((millis() - start) / 1000) + "s");
    }
    log("success");

    // Get CCID for IoT SIM card
    SerialAT.println("AT+CICCID");
    delay(100);  // Short delay for response
    String resp = "";
    while (SerialAT.available()) {
        resp += (char)SerialAT.read();
    }
    int pos = resp.indexOf("+CICCID:");
    if (pos != -1) {
        String ccid = resp.substring(pos + 9, resp.indexOf("\r", pos));
        ccid.trim();
        Serial.println("CCID: " + ccid);
    } else {
        Serial.println("CCID: Not found");
    }

    // Acquire signal strength
    int csq = modem.getSignalQuality();
    Serial.println("Signal quality: " + String(csq));
    // Example Query the IP address of a device
    String ip = modem.getLocalIP();
    log("Device IP address: " + ip);
    log("success");
}
```

### 3.2 HTTP

```cpp line-num
#include "M5Unified.h"
#define TINY_GSM_MODEM_SIM7028  // Specify to use SIM7028 module; TinyGsm library adapts instruction set based on this macro, must be placed here
#include "ArduinoHttpClient.h"
#include "TinyGsmClient.h"
#include "StreamDebugger.h"
#include "M5IOE1.h"

#define SerialMon        Serial             // MCU -> PC for log output
#define MONITOR_BAUDRATE 115200
#define SerialAT         Serial1            // MCU <-> SIM7028 module communication
#define SIM7028_BAUDRATE 115200
#define SIM7028_RESET    -1
#define MCU_TX           5
#define MCU_RX           6
#define RS485_TX         7
#define RS485_RX         8
#define IO_SCL           39
#define IO_SDA           38

// M5IOE1 device instance
M5IOE1 ioe1;

// M5IOE1 I2C address (default 0x6F)
#define I2C_ADDR M5IOE1_DEFAULT_ADDR

// Pin definitions for M5IOE1 GPIOs
#define SIM_PWR_EN M5IOE1_PIN_9
#define SIM_RST M5IOE1_PIN_11
#define VIN_ADC M5IOE1_PIN_2

// If you need to see log detail, you can open the following macro definition
// #define DUMP_AT_COMMANDS
// If you need to debug, you can open the following macro definition in TinyGsmClientSIM7028.h line 13
// #define TINY_GSM_DEBUG Serial
#ifdef DUMP_AT_COMMANDS
StreamDebugger debugger(SerialAT, SerialMon);
TinyGsm modem(debugger);
#else
TinyGsm modem(SerialAT);
#endif

// Server details
const char server[]   = "httpbin.org";
const char resource[] = ""; // API endpoint path
const int port        = 80;    // HTTP port
TinyGsmClient client(modem); // Create TCP client based on TinyGsm (HTTP relies on TCP connection)
HttpClient http(client, server, port); // Create HTTP client instance (specify TCP client, server and port)

void modemConnect(void);// Initialize ML307 module and establish network connection
const char apn[] = "cmnbiot";

void log(String info)
{
    SerialMon.println(info);
}

void SIM7028_EN()
{
    if (ioe1.begin(&Wire, I2C_ADDR, IO_SDA, IO_SCL, M5IOE1_I2C_FREQ_100K, M5IOE1_INT_MODE_POLLING) == M5IOE1_OK){
        ioe1.pinMode(SIM_PWR_EN, OUTPUT);
        ioe1.digitalWrite(SIM_PWR_EN, HIGH); // Enable SIM power
        delay(100);
        ioe1.pinMode(SIM_RST, OUTPUT);
        ioe1.digitalWrite(SIM_RST, LOW); // SIM reset
        delay(100);
        ioe1.digitalWrite(SIM_RST, HIGH);
        log("SIM power enabled");
    }
    else{
        log("Failed to enable SIM power");
    }
}

void setup()
{
    M5.begin();
    SerialMon.begin(115200);
    SerialMon.println(">>SIM7028 HTTP TEST");
    SerialAT.begin(SIM7028_BAUDRATE, SERIAL_8N1, MCU_RX, MCU_TX);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setTextDatum(middle_center);
    M5.Display.drawString("NBIoT HTTP", M5.Display.width() / 2, 10);
    M5.Display.drawString("Init...", M5.Display.width() / 2, 60);
    delay(500);
    SIM7028_EN();
    modemConnect();
}

void loop()
{
    // --- GET request ---
    M5.Display.fillRect(0, 30, 128, 98, TFT_BLACK);
    M5.Display.drawString("GET", M5.Display.width() / 2, 40);
    Serial.println("making GET request");

    http.get("/get");
    // read the status code and body of the response
    int statusCode  = http.responseStatusCode();
    String response = http.responseBody();

    Serial.print("Status code: ");
    Serial.println(statusCode);
    Serial.print("Response: ");
    Serial.println(response);
    Serial.println("Wait five seconds");

    M5.Display.drawString("STATUS:", M5.Display.width() / 2, 70);
    M5.Display.drawString(String(statusCode), M5.Display.width() / 2, 100);

    delay(5000);

    // --- POST request ---
    M5.Display.fillRect(0, 30, 128, 98, TFT_BLACK);
    M5.Display.drawString("POST", M5.Display.width() / 2, 40);
    Serial.println("making POST request");

    String contentType = "application/x-www-form-urlencoded";
    String postData    = "name=Alice&age=12";

    http.post("/post", contentType, postData);

    // read the status code and body of the response
    statusCode = http.responseStatusCode();
    response   = http.responseBody();

    Serial.print("Status code: ");
    Serial.println(statusCode);
    Serial.print("Response: ");
    Serial.println(response);
    Serial.println("Wait five seconds");

    M5.Display.drawString("STATUS:", M5.Display.width() / 2, 70);
    M5.Display.drawString(String(statusCode), M5.Display.width() / 2, 100);

    delay(5000);
}

void modemConnect(void)
{
    unsigned long start = millis();
    log("Initializing modem...");
    while (!modem.init()) {
        log("waiting...." + String((millis() - start) / 1000) + "s");
    };

    start = millis();
    log("Waiting for network...");
    while (!modem.waitForNetwork()) {
        log("waiting...." + String((millis() - start) / 1000) + "s");
    }
    log("success");

    log("Waiting for GPRS connect...");
    if (!modem.gprsConnect(apn)) {
        log("waiting...." + String((millis() - start) / 1000) + "s");
    }
    log("success");
    // Get CCID for SIM card
    SerialAT.println("AT+CICCID");
    delay(100);  // Short delay for response
    String resp = "";
    while (SerialAT.available()) {
        resp += (char)SerialAT.read();
    }
    int pos = resp.indexOf("+CICCID:");
    if (pos != -1) {
        String ccid = resp.substring(pos + 9, resp.indexOf("\r", pos));
        ccid.trim();
        Serial.println("CCID: " + ccid);
    } else {
        Serial.println("CCID: Not found");
    }
    // Acquire signal strength
    int csq = modem.getSignalQuality();
    log("Signal quality: " + String(csq));
    // Example Query the IP address of a device
    String ip = modem.getLocalIP();
    log("Device IP address: " + ip);
    log("success");
}
```

## 4. 编译上传

- 1\. AtomS3R 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

\#> 说明 | 不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/AtomS3R/download%20mode.gif" width="30%">

- 2\. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/Atom_DTU_NBIoT2_Arduino_example.jpg" width="70%">

## 5. 通信效果

- MQTT 通信

设备上电后，串口监视器会输出通信模块及 MQTT 服务器相关信息，连接成功后每隔 10 秒会向服务器发布一条消息，同时订阅的主题有消息时会打印接收到的消息内容。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/Atom_DTU_NBIoT2_v1.1_Arduino_MQTT.jpg" width="40%">

串口监视器反馈如下所示：

```
>>SIM7028 MQTT TEST
Initializing modem...
Waiting for network...
success
Waiting for GPRS connect...
success
CCID: 898607B01022C0006068
Signal quality: 18
Device IP address: 100.50.14.152

OK
success
>> MQTT NOT CONNECTED
MQTT state code: -1
>> Connecting to MQTT broker: mqtt.m5stack.com
>> MQTT CONNECTED, subscribing: Atom DTU NBIoT v1.1 Receive
>> [MQTT SEND] Topic: Atom DTU NBIoT v1.1 Send
Info: SIM7028 MQTT! #0
=== MQTT CONNECTED ===
>> [MQTT RECEIVE] Topic: Atom DTU NBIoT v1.1 Receive
Info: Hello NBIoT
```

- HTTP 通信

设备上电后，串口监视器会输出通信模块相关信息，连接成功后会向指定服务器循环发送 GET 和 POST 请求，主控屏幕会显示请求状态，串口可查看详细信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/Atom_DTU_NBIoT2_v1.1_Arduino_HTTP_GET.jpg" width="40%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1210/Atom_DTU_NBIoT2_v1.1_Arduino_HTTP_POST.jpg" width="40%">

串口监视器反馈如下所示：

```
>>SIM7028 HTTP TEST
[M5IOE1] Initializing M5IOE1 with 100KHz (device default)
[M5IOE1] Device UID: 0xDF0E, FW Version: 41
[M5IOE1] Current I2C speed matches user request (100K)
[M5IOE1] I2C config set and verified: sleep=0, speed=100K, wake=falling, pull=on
[M5IOE1] M5IOE1 initialized at address 0x6F (I2C: 100000 Hz)
[M5IOE1] Interrupt mode -> POLLING (pause if I2C sleep on; resume when off)
[M5IOE1] Pin 1 interrupt detached and verified
[M5IOE1] Pin 8 mode set and verified: 0x03
[M5IOE1] Pin 10 mode set and verified: 0x03
SIM power enabled
Initializing modem...
Waiting for network...
success
Waiting for GPRS connect...
success
CCID: 898607B01022C0006068
Signal quality: 16
Device IP address: 100.65.16.242

OK
success
making GET request
Status code: 200
Response: {
  "args": {},
  "headers": {
    "Host": "httpbin.org",
    "User-Agent": "Arduino/2.2.0",
    "X-Amzn-Trace-Id": "Root=1-6961fd12-1549e2280f15840b34db2c4e"
  },
  "origin": "111.55.204.81",
  "url": "http://httpbin.org/get"
}

Wait five seconds
making POST request
Status code: 200
Response: {
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "age": "12",
    "name": "Alice"
  },
  "headers": {
    "Content-Length": "17",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "Arduino/2.2.0",
    "X-Amzn-Trace-Id": "Root=1-6961fd1a-4d5c07665fbd6ae37525cd8d"
  },
  "json": null,
  "origin": "111.55.204.81",
  "url": "http://httpbin.org/post"
}

Wait five seconds
```
