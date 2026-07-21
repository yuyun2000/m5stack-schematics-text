# Stamp-C5 Wi-Fi

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.3.8
- 开发板选项 = M5StampC5
#>说明 | 实际应用时，请将下方代码中的 `ssid` 改为实际的 Wi-Fi 名称，`password` 改为实际的 Wi-Fi 密码。

### Wi-Fi STA / AP

```cpp line-num
#include <WiFi.h>

const char *ssid     = "ssid";
const char *password = "password";

void setup()
{
    Serial.begin(115200);
    delay(1000);

    Serial.println();
    Serial.println("Stamp-C5 Wi-Fi demo");

    // STA MODE
    WiFi.mode(WIFI_STA);
    Serial.println("WiFi mode set to STA");
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println();
    Serial.print("Connected to ");
    Serial.println(ssid);
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
    Serial.print("RSSI: ");
    Serial.print(WiFi.RSSI());
    Serial.println(" dBm");

    // AP MODE
    // WiFi.mode(WIFI_AP);
    // Serial.println("WiFi mode set to AP");
    // WiFi.softAP(ssid, password);
    // Serial.println("AP started");
    // Serial.print("IP address: ");
    // Serial.println(WiFi.softAPIP());
}

void loop()
{
}
```

串口反馈信息示例：

```
Stamp-C5 Wi-Fi demo
WiFi mode set to STA
Connecting to M5Stack
....
Connected to M5Stack
IP address: 192.168.51.135
RSSI: -59 dBm
```

### Wi-Fi Scan

```cpp line-num
#include <WiFi.h>

void setup()
{
    Serial.begin(115200);
    delay(1000);

    WiFi.mode(WIFI_STA);
    WiFi.disconnect();
    delay(100);
}

void loop()
{
    Serial.println("Scan start");

    // WiFi.scanNetworks will return the number of networks found.
    int n = WiFi.scanNetworks();
    Serial.println("Scan done");

    if (n == 0) {
        Serial.println("no networks found");
    } else {
        Serial.print(n);
        Serial.println(" networks found");
        Serial.println("Nr | SSID                             | RSSI | CH | Encryption");

        for (int i = 0; i < n; ++i) {
            Serial.printf("%2d", i + 1);
            Serial.print(" | ");
            Serial.printf("%-32.32s", WiFi.SSID(i).c_str());
            Serial.print(" | ");
            Serial.printf("%4ld", static_cast<long>(WiFi.RSSI(i)));
            Serial.print(" | ");
            Serial.printf("%2ld", static_cast<long>(WiFi.channel(i)));
            Serial.print(" | ");

            switch (WiFi.encryptionType(i)) {
                case WIFI_AUTH_OPEN:
                    Serial.print("open");
                    break;
                case WIFI_AUTH_WEP:
                    Serial.print("WEP");
                    break;
                case WIFI_AUTH_WPA_PSK:
                    Serial.print("WPA");
                    break;
                case WIFI_AUTH_WPA2_PSK:
                    Serial.print("WPA2");
                    break;
                case WIFI_AUTH_WPA_WPA2_PSK:
                    Serial.print("WPA+WPA2");
                    break;
                case WIFI_AUTH_WPA2_ENTERPRISE:
                    Serial.print("WPA2-EAP");
                    break;
                case WIFI_AUTH_WPA3_PSK:
                    Serial.print("WPA3");
                    break;
                case WIFI_AUTH_WPA2_WPA3_PSK:
                    Serial.print("WPA2+WPA3");
                    break;
                case WIFI_AUTH_WAPI_PSK:
                    Serial.print("WAPI");
                    break;
                default:
                    Serial.print("unknown");
                    break;
            }
            Serial.println();
            delay(10);
        }
    }

    Serial.println();
    // Delete the scan result to free memory for code below.
    WiFi.scanDelete();

    // Wait a bit before scanning again.
    delay(5000);
}
```

串口反馈信息示例：

```
Scan start
Scan done
5 networks found
Nr | SSID                             | RSSI | CH | Encryption
 1 | M5Stack                          |  -45 |  6 | WPA2+WPA3
 2 | M5Stack-Guest                    |  -58 |  6 | WPA2
 3 | Office-WiFi                      |  -63 | 11 | WPA+WPA2
 4 | IoT-Test                         |  -72 |  1 | WPA2
 5 | Open-Network                     |  -80 |  1 | open
```
