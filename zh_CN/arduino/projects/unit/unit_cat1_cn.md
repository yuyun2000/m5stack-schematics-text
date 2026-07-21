# Unit Cat1-CN Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [TinyGSM](https://github.com/m5stack/TinyGSM)
  - [StreamDebugger](https://github.com/vshymanskyy/StreamDebugger)
  - [PubSubClient](https://github.com/knolleary/pubsubclient)
  - [ArduinoHttpClient](https://github.com/arduino-libraries/ArduinoHttpClient)

\#> 注意 | 需要在 GitHub 上下载最新的库版本，库地址: [TinyGSM - M5Stack GitHub](https://github.com/m5stack/TinyGSM)，请勿在 Arduino Library 中下载。（如有疑问，请参考[此教程](/zh_CN/arduino/arduino_library#git%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85)）

- 使用到的硬件产品：
  - [CoreS3-SE](https://shop.m5stack.com/products/m5stack-cores3-se-iot-controller-w-o-battery-bottom?variant=45170957451521)
  - [Unit Cat1-CN](https://item.taobao.com/item.htm?ft=t&id=997753094852)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5CORES3%20SE/3.webp" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1189/U204_CAT1-CN_main_pictures_04.webp" width="20%">

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/unit/Unit_Fingerprint2)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U204" type="UNIT"></ProductCompatible>

Unit Cat1-CN 使用前请确保已插入支持 LTE Cat1 网络的 SIM 卡（中国移动、中国联通、中国电信的常规的 SIM 卡都支持），并开通数据业务。SIM 卡槽位于模块内部，请使用六角螺丝刀卸下 Unit Cat1-CN 底部的三颗螺丝，**然后翻转**，取下底盖，卡槽具体位置如下图红框处所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1189/Unit_Cat1-CN_SIM_card_slot_location.jpg" width="40%">

## 3. 案例程序

- 本教程中使用的主控设备为 CoreS3 ，搭配 Unit Cat1-CN。本通信模块采用串口的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的串口 IO 为 `G17 (RX)`，`G18 (TX)`。

Unit Cat1-CN 支持多种通信协议，以下提供 MQTT 和 HTTP 两种协议的示例程序。

### 3.1 MQTT

```cpp line-num
#include <M5Unified.h>
#define TINY_GSM_MODEM_ML307  // Specify to use ML307 module; TinyGsm library adapts instruction set based on this macro, must be placed here
#include <TinyGsmClient.h>
#include <StreamDebugger.h>
#include <PubSubClient.h>

#define SerialMon        Serial             // MCU -> PC for log output
#define MONITOR_BAUDRATE 115200
#define SerialAT         Serial1            // MCU <-> ML307 module communication
#define ML307_BAUDRATE   115200
#define ML307_RESET      -1
#define MCU_TX           17
#define MCU_RX           18
#define MQTT_BROKER      "XXXXXXXX"         // MQTT broker address
#define MQTT_PORT        1883               // MQTT service port
#define mqtt_devid       "XXXXXXXX"         // MQTT client ID
#define mqtt_pubid       "XXXXXXXX"         // MQTT username
#define mqtt_password    "XXXXXXXX"         // MQTT authentication key
#define UPLOAD_INTERVAL  10000              // Data upload interval, 10s

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
void nbConnect(void);   // Function to initialize ML307 and connect to NB-IoT network

const char* topicSub = "Unit Cat1-CN Receive"; // MQTT topic for receiving messages (replace with your actual subscribe topic)
const char* topicPub = "Unit Cat1-CN Send";    // MQTT topic for sending messages (replace with your actual publish topic)
int         num               = 0; // Counter for published messages
uint32_t lastReconnectAttempt = 0; // Timestamp for last MQTT reconnection attempt (avoid frequent retries)
bool lastMqttState = false; // Track MQTT connection status
const char apn[] = "cmnet";

void log(String info)
{
    SerialMon.println(info);
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println(">>ML307 MQTT TEST");
    SerialAT.begin(ML307_BAUDRATE, SERIAL_8N1, MCU_RX, MCU_TX);
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setCursor(5,0);
    M5.Display.printf("Unit Cat1-CN Example");
    M5.Display.setCursor(0, 120);
    M5.Display.printf("[MQTT RECEIVE] (latest)\n NULL");
    nbConnect(); // Initialize ML307 module and connect to network
    mqttClient.setServer(MQTT_BROKER, MQTT_PORT);  // Set MQTT broker address and port
    mqttClient.setKeepAlive(120);                  // MQTT keep-alive interval (120 seconds)
    mqttClient.setSocketTimeout(15000);            // TCP connection timeout (15 seconds)
    mqttClient.setCallback(mqttCallback);          // Register MQTT message receive callback
}

void loop()
{
    static unsigned long timer = 0;

    // Check for MQTT connection status change (connected <-> disconnected)
    if (mqttClient.connected() != lastMqttState) {
        if (mqttClient.connected()) {
            log("=== MQTT CONNECTED ===");
            M5.Display.fillRect(0, 25, 320, 25, TFT_BLACK);
            M5.Display.setTextColor(TFT_GREEN);
            M5.Display.setCursor(5, 25);
            M5.Display.printf("MQTT CONNECTED");
        } else {
            log("=== MQTT DISCONNECTED ===");
            M5.Display.fillRect(0, 25, 320, 25, TFT_BLACK);
            M5.Display.setCursor(5, 25);
            M5.Display.setTextColor(TFT_RED);
            M5.Display.printf("MQTT DISCONNECTED");
        }
        lastMqttState = mqttClient.connected();
    }

    // MQTT reconnection logic (retry every 3 seconds if disconnected)
    if (!mqttClient.connected()) {
        log(">> MQTT NOT CONNECTED");
        log("MQTT state code: " + String(mqttClient.state()));
        M5.Display.fillRect(0, 25, 320, 25, TFT_BLACK);
        M5.Display.setCursor(5, 25);
        M5.Display.setTextColor(TFT_RED);
        M5.Display.printf("MQTT NOT CONNECTED");
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
            snprintf(jsonBuf, sizeof(jsonBuf), "ML307 MQTT! #%d", num++);
            log(">> [MQTT SEND] Topic: " + String(topicPub));
            log("Info: " + String(jsonBuf));
            mqttClient.publish(topicPub, jsonBuf);
            M5.Display.fillRect(0, 50, 320, 70, TFT_BLACK);
            M5.Display.setCursor(0, 50);
            M5.Display.setTextColor(TFT_WHITE);
            M5.Display.printf("[MQTT SEND]\n Topic: ");
            M5.Display.print(String(topicPub));
            M5.Display.setCursor(0, 85);
            M5.Display.printf(" Info: ");
            M5.Display.print(String(jsonBuf));
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
    M5.Display.fillRect(0, 120, 320, 70, TFT_BLACK);
    M5.Display.setCursor(0, 120);
    M5.Display.setTextColor(TFT_WHITE);
    M5.Display.printf("[MQTT RECEIVE] (latest)\n Topic: ");
    M5.Display.print(String(topic));
    M5.Display.setCursor(0, 155);
    M5.Display.printf(" Info: ");
    M5.Display.print(String(payloadStr));
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
    // Get card number
    String ccid = modem.getSimCCID();
    Serial.println("CCID: " + ccid);
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
#include <M5Unified.h>
#define TINY_GSM_MODEM_ML307  // Specify to use ML307 module; TinyGsm library adapts instruction set based on this macro, must be placed here
#include <TinyGsmClient.h>
#include <StreamDebugger.h>
#include <ArduinoHttpClient.h>

#define SerialMon        Serial             // MCU -> PC for log output
#define MONITOR_BAUDRATE 115200
#define SerialAT         Serial1            // MCU <-> ML307 module communication
#define ML307_BAUDRATE   115200
#define ML307_RESET      -1
#define MCU_TX           17
#define MCU_RX           18

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
const char server[]   = "api.m5stack.com";
const char resource[] = "/v1"; // API endpoint path
const int port        = 80;    // HTTP port
TinyGsmClient client(modem); // Create TCP client based on TinyGsm (HTTP relies on TCP connection)
HttpClient http(client, server, port); // Create HTTP client instance (specify TCP client, server and port)

void modemConnect(void);// Initialize ML307 module and establish network connection

const char apn[] = "cmnet"; // APN (Access Point Name) configuration: "cmnet" for China Mobile, "3GNET" for China Unicom, "CTNET" for China Telecom 

void log(String info)
{
    SerialMon.println(info);
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    log(">>ML307 HTTP TEST");
    SerialAT.begin(ML307_BAUDRATE, SERIAL_8N1, MCU_RX, MCU_TX);
    M5.Display.clear();
    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setCursor(5,0);
    M5.Display.printf("Unit Cat1-CN Example");
    modemConnect(); // Initialize ML307 module and connect to network
}

void loop()
{
    SerialMon.print(F("Performing HTTP GET request... "));
    M5.Display.fillRect(0, 25, 320, 215, TFT_BLACK);
    M5.Display.setTextColor(TFT_YELLOW);
    M5.Display.setCursor(5,25);
    M5.Display.printf("HTTP GET request...");
    // Send HTTP GET request to the specified resource (server + resource = http://api.m5stack.com/v1)
    int err = http.get(resource);
    if (err != 0) {
        log(F("failed to connect"));
        delay(10000);
        return;
    }
    else {
        M5.Display.fillRect(0, 25, 320, 25, TFT_BLACK);
        M5.Display.setTextColor(TFT_GREEN);
        M5.Display.setCursor(5,25);
        M5.Display.printf(server);
        M5.Display.printf(resource);
    }
    // Get HTTP response status code (e.g., 200=Success, 404=Not Found, 500=Server Error)
    int status = http.responseStatusCode();
    SerialMon.print(F("Response status code: "));
    log(String(status));
    M5.Display.setTextColor(TFT_WHITE);
    M5.Display.printf("\n\n Response status code: ");
    M5.Display.print(String(status));M5.Display.println();
    if (!status) {
        delay(10000);
        return;
    }
    // Log all HTTP response headers (metadata about the response)
    log(F("Response Headers:"));
    // Loop through all available response headers (header name + value pairs)
    while (http.headerAvailable()) {
        String headerName  = http.readHeaderName(); // Read header name (e.g., "Content-Type")
        String headerValue = http.readHeaderValue();// Read header value (e.g., "text/plain")
        log("    " + headerName + " : " + headerValue); // Log header in "Name : Value" format
    }

    int length = http.contentLength();
    if (length >= 0) {
        SerialMon.print(F("Content length is: "));
        log(String(length));        
        M5.Display.printf("\n Content length is: %d\n", length);
    }
    // Check if the response uses chunked transfer encoding (common for dynamic content)
    if (http.isResponseChunked()) {
        log(F("The response is chunked"));
    }
    // Read the full HTTP response body (the actual data returned by the server)
    String body = http.responseBody();
    log(F("Response:"));
    log("    " + body);
    M5.Display.printf("\n Response: ");
    M5.Display.print(body);M5.Display.println();

    SerialMon.print(F("Body length is: "));
    log(String(body.length()));
    M5.Display.printf("\n Body length is: ");
    M5.Display.print(String(body.length()));M5.Display.println();

    http.stop(); // Close the HTTP connection to release resources
    log(F("Server disconnected"));
    delay(5000); // Wait 5 seconds before sending the next HTTP request 
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
    // Get card number
    String ccid = modem.getSimCCID();
    log("CCID: " + ccid);
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

- 1\. 进入下载模式：CoreS3-SE 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

#> 说明| 不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128_SE_Download_Mode.gif" width="30%">

- 2\. 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1189/Unit_Cat1-CN_Arduino_example.jpg" width="70%">

## 5. 例程效果展示

- MQTT 通信

设备上电后，串口监视器会输出连接网络及 MQTT 服务器的信息，连接成功后每隔 10 秒会向服务器发布一条消息，同时订阅的主题有消息时会打印接收到的消息内容。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1189/Unit_Cat1-CN_Arduino_MQTT.jpg" width="40%">

串口监视器反馈如下所示：

```
>>ML307 MQTT TEST
Initializing modem...
Waiting for network...
success
Waiting for GPRS connect...
success
CCID: 898600B11925F0192677
Signal quality: 31
Device IP address: 10.42.155.4
success
>> Connecting to MQTT broker: mqtt.m5stack.com
>> MQTT CONNECTED, subscribing: Unit Cat1-CN Receive
=== MQTT CONNECTED ===
>> [MQTT SEND] Topic: Unit Cat1-CN Send
Info: ML307 MQTT! #0
......
>> [MQTT RECEIVE] Topic: Unit Cat1-CN Receive
Info: Hello from MQTT Broker
```

- HTTP 通信
  
设备上电后，串口监视器会输出连接网络的信息，连接成功后会向指定服务器发送 HTTP GET 请求，并打印返回的状态码、响应头及响应体内容。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1189/Unit_Cat1-CN_Arduino_HTTP.jpg" width="40%">

串口监视器反馈如下所示：

```
Performing HTTP GET request... Response status code: 200
Response Headers:
    Server : nginx/1.14.0 (Ubuntu)
    Date : Tue, 25 Nov 2025 07:27:26 GMT
    Content-Type : text/plain;charset=UTF-8
    Content-Length : 13
    Connection : close
    Vary : Origin
    Vary : Access-Control-Request-Method
    Vary : Access-Control-Request-Headers
    X-Content-Type-Options : nosniff
    X-XSS-Protection : 1; mode=block
    Cache-Control : no-cache, no-store, max-age=0, must-revalidate
    Pragma : no-cache
    Expires : 0
    X-Frame-Options : DENY
Content length is: 13
Response:
    Hello M5 User
Body length is: 13
Server disconnected
```
