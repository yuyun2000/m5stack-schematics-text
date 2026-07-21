# AWS IoT Core - Arduino

## 1.概述

本教程将使用M5Core2举例说明如何通过Arduino编程，使设备接入AWS IoT Core平台，实现订阅和发布数据。

## 2.创建设备

接入前,需要先通过AWS Management Console注册新设备。[点击此处访问AWS Management Console](https://console.aws.amazon.com/), 完成账号创建后进行登录。 

参考下方流程进行设备创建, 详情操作可参考[AWS官网文档](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html)。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_cloud/aws_iot_core/aws_iot_core_01.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_cloud/aws_iot_core/aws_iot_core_02.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_cloud/aws_iot_core/aws_iot_core_03.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_cloud/aws_iot_core/aws_iot_core_04.jpg" width="70%" />


在完成设备创建后将会弹出`密钥`与`证书`的下载页面, 请根据提示将所有证书下载至本地保存。其中`设备证书(Device certificate)`+`设备私钥(Private Key File)`+`CA根证书(Amazon Root CA 1)`，在后续的操作中将会用于验证使用。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_cloud/aws_iot_core/aws_iot_core_05.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_cloud/aws_iot_core/aws_iot_core_06.jpg" width="70%" />

## 3.安装依赖与案例库

该教程中，我们将使用M5Core2触摸按键控制发布数据至AWS-IoT-Core。 开始编程前，我们需要从`Github`下载`AWS-IoT`相关依赖库与案例程序, 你可以通过下面`git`指令直接下载(或是点击下方链接访问对应的项目地址下载zip压缩包, 下载后需进行解压)。并将依赖库放置到Arduino库管理路径(通常为`C:/Users/YourUserName/Documents/Arduino/libraries`)

- Libraries:
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [aws-iot-esp32-arduino-examples](https://github.com/aws-samples/aws-iot-esp32-arduino-examples)
  - [ArduinoJson](https://github.com/bblanchon/ArduinoJson)
  - [arduino-mqtt](https://github.com/256dpi/arduino-mqtt)

```bash
git clone https://github.com/m5stack/M5Unified.git
git clone https://github.com/m5stack/M5GFX.git
git clone https://github.com/aws-samples/aws-iot-esp32-arduino-examples.git
git clone https://github.com/bblanchon/ArduinoJson.git
git clone https://github.com/256dpi/arduino-mqtt.git
```

#>使用不同的设备| 除了以上的依赖库之外，你还可以根据你所使用的M5设备类型，引入不同的驱动库。其他有关M5Stack产品的库，你可以在M5Stack官方[Github](https://github.com/m5stack)中找到。

## 4.创建项目

我们可以从`aws-iot-esp32-arduino-examples`文件夹中，复制`basic-pubsub`案例程序, 作为程序的一个基础模板。项目中的`secrets.h`文件用于存放`密钥与证书`、`WIFI`信息。

#>**提示:**|1. 宏定义`THINGNAME`为我们的创建的设备名称,需要与`AWS Management Console`中的名称保持一致.<br/>2. 将我们之前在`AWS IoT Core`中创建设备获取的密钥与证书用编辑器打开，并复制粘贴内容到代码中的对应位置。<br/>3. 复制`AWS Management Console`->`Settings`中的`Endpoint`字段

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_cloud/aws_iot_core/aws_iot_core_07.jpg" width="70%" />


```cpp
#include <pgmspace.h>

#define SECRET
#define THINGNAME "THINGNAME"

const char WIFI_SSID[] = "WIFI_SSID";
const char WIFI_PASSWORD[] = "WIFI_PASSWORD";
const char AWS_IOT_ENDPOINT[] = "xxxxx.amazonaws.com";

// Amazon Root CA 1
static const char AWS_CERT_CA[] PROGMEM = R"EOF(
-----BEGIN CERTIFICATE-----
MIIDQTCCAimgAwIBAgIT........................
-----END CERTIFICATE-----
)EOF";

// Device Certificate
static const char AWS_CERT_CRT[] PROGMEM = R"KEY(
-----BEGIN CERTIFICATE-----
MIIDWjCCAkKgAwIBAgIVA........................
-----END CERTIFICATE-----
)KEY";

// Device Private Key
static const char AWS_CERT_PRIVATE[] PROGMEM = R"KEY(
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAq........................
-----END RSA PRIVATE KEY-----
)KEY";

```

## 5.编辑程序

参考下方程序, 并使用Arduino IDE将其编译上传至设备。完成上传后, 点击触摸设备按键A即可向AWS IoT Core发布数据, 当有收到新的下行数据时也将进行显示。

```cpp

#include <M5Unified.h>

#include "secrets.h"
#include <WiFiClientSecure.h>
#include <MQTTClient.h>
#include <ArduinoJson.h>
#include "WiFi.h"

// The MQTT topics that this device should publish/subscribe
#define AWS_IOT_PUBLISH_TOPIC   "esp32/pub"
#define AWS_IOT_SUBSCRIBE_TOPIC "esp32/sub"

WiFiClientSecure net = WiFiClientSecure();
MQTTClient client    = MQTTClient(256);

void messageHandler(String &topic, String &payload) {
    Serial.println("incoming: " + topic + " - " + payload);

    StaticJsonDocument<200> doc;
    deserializeJson(doc, payload);
    const char *message = doc["message"];
    M5.Lcd.clear();
    M5.Lcd.setCursor(0, 0, 2);
    M5.Lcd.setTextColor(TFT_BLUE);
    M5.Lcd.setTextFont(2);
    M5.Lcd.println(payload);
}

void connectAWS() {
    WiFi.mode(WIFI_STA);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    Serial.println("Connecting to Wi-Fi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    // Configure WiFiClientSecure to use the AWS IoT device credentials
    net.setCACert(AWS_CERT_CA);
    net.setCertificate(AWS_CERT_CRT);
    net.setPrivateKey(AWS_CERT_PRIVATE);
    // Connect to the MQTT broker on the AWS endpoint we defined earlier
    client.begin(AWS_IOT_ENDPOINT, 8883, net);
    // Create a message handler
    client.onMessage(messageHandler);
    Serial.print("Connecting to AWS IOT");
    while (!client.connect(THINGNAME)) {
        Serial.print(".");
        delay(100);
    }
    if (!client.connected()) {
        Serial.println("AWS IoT Timeout!");
        return;
    }
    // Subscribe to a topic
    client.subscribe(AWS_IOT_SUBSCRIBE_TOPIC);
    Serial.println("AWS IoT Connected!");
    M5.Lcd.println("AWS IoT Connected!");
}

void publishMessage() {
    StaticJsonDocument<200> doc;
    doc["time"]    = millis();
    doc["message"] = "Hello World";
    char jsonBuffer[512];
    serializeJson(doc, jsonBuffer);  // print to client

    client.publish(AWS_IOT_PUBLISH_TOPIC, jsonBuffer);
}

void setup() {
    M5.begin();
}

void loop() {
    M5.update();
    if (M5.BtnA.wasClicked()) {
        Serial.println("Button pressed");
        publishMessage();
        Serial.println("Publishing");
    }
    client.loop();
}

```


## 6.在线调试

点击AWS Management Console->Test进入在线测试页面。该功能用于测试AWS账户中设备的MQTT消息, 点击Additional configuration可调整QoS等级。

- 发布主题:填写Topic和Message payload,点击Publish发布。
- 订阅主题:填写Topic,点击Subcribe订阅。点击Additional configuration,可设置显示消息的类型，接收到的消息将在页面下方的控制台显示。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_cloud/aws_iot_core/aws_iot_core_08.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_cloud/aws_iot_core/aws_iot_core_09.jpg" width="70%" />
<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/iot_cloud/aws_iot_core/aws_iot_core_10.jpg" width="70%" />
