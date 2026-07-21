# Unit PoE-P4 Ethernet 网络通信

Unit PoE-P4 Ethernet 网络通信案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.6
- 开发板选项 = M5UnitPoEP4

```cpp line-num
#include <ETH.h>

#ifndef ETH_PHY_MDC
#define ETH_PHY_TYPE  ETH_PHY_IP101
#define ETH_PHY_ADDR  1
#define ETH_PHY_MDC   31
#define ETH_PHY_MDIO  52
#define ETH_PHY_POWER 51
#define ETH_CLK_MODE  EMAC_CLK_EXT_IN
#endif

static bool eth_connected = false;

// WARNING: onEvent is called from a separate FreeRTOS task (thread)!
void onEvent(arduino_event_id_t event) {
  switch (event) {
    case ARDUINO_EVENT_ETH_START:
      Serial.println("ETH Started");
      // The hostname must be set after the interface is started, but needs
      // to be set before DHCP, so set it from the event handler thread.
      ETH.setHostname("esp32-ethernet");
      break;
    case ARDUINO_EVENT_ETH_CONNECTED: Serial.println("ETH Connected"); break;
    case ARDUINO_EVENT_ETH_GOT_IP:
      Serial.println("ETH Got IP");
      Serial.println(ETH);
      eth_connected = true;
      break;
    case ARDUINO_EVENT_ETH_LOST_IP:
      Serial.println("ETH Lost IP");
      eth_connected = false;
      break;
    case ARDUINO_EVENT_ETH_DISCONNECTED:
      Serial.println("ETH Disconnected");
      eth_connected = false;
      break;
    case ARDUINO_EVENT_ETH_STOP:
      Serial.println("ETH Stopped");
      eth_connected = false;
      break;
    default: break;
  }
}

void testClient(const char *host, uint16_t port) {
  Serial.print("\nconnecting to ");
  Serial.println(host);

  NetworkClient client;
  if (!client.connect(host, port)) {
    Serial.println("connection failed");
    return;
  }
  client.printf("GET / HTTP/1.1\r\nHost: %s\r\n\r\n", host);
  while (client.connected() && !client.available());
  while (client.available()) {
    Serial.write(client.read());
  }

  Serial.println("closing connection\n");
  client.stop();
}

void setup() {
  Serial.begin(115200);
  Network.onEvent(onEvent);  // Will call onEvent() from another thread.
  ETH.begin(ETH_PHY_TYPE, ETH_PHY_ADDR, ETH_PHY_MDC, ETH_PHY_MDIO, ETH_PHY_POWER, ETH_CLK_MODE);
}

void loop() {
  if (eth_connected) {
    testClient("baidu.com", 80);
  }
  delay(10000);
}
```

Unit PoE-P4 上电后每 10 秒钟连接一次 baidu.com，成功连接后会输出 HTTP 响应信息，如果连接失败则输出连接失败的提示信息。

串口输出示例：

- 网络连接成功

```
ETH Started
ETH Connected
ETH Got IP
*eth0: <UP,100M,FULL_DUPLEX,AUTO,ADDR:0x1> (DHCPC,GARP,IP_MOD)
      ether 30:ED:A0:EA:92:D2
      inet 192.168.20.121 netmask 255.255.255.0 broadcast 192.168.20.255
      gateway 192.168.20.1 dns 223.5.5.5


connecting to baidu.com
HTTP/1.1 301 Moved Permanently
Location: https://www.baidu.com/
Date: Sat, 28 Feb 2026 04:29:55 GMT
Content-Length: 57
Content-Type: text/html; charset=utf-8

<a href="https://www.baidu.com/">Moved Permanently</a>.

closing connection
```

- 网络连接失败

```
ETH Disconnected
ETH Connected
ETH Got IP
*eth0: <UP,100M,FULL_DUPLEX,AUTO,ADDR:0x1> (DHCPC,GARP,IP_MOD)
      ether 30:ED:A0:EA:92:D2
      inet 192.168.20.121 netmask 255.255.255.0 broadcast 192.168.20.255
      gateway 192.168.20.1 dns 223.5.5.5


connecting to baidu.com
connection failed
```


