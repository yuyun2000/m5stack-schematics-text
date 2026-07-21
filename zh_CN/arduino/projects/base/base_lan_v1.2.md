# Base LAN v1.2 Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5-Ethernet](https://github.com/m5stack/M5-Ethernet)

\#> 注意 | 需要在 GitHub 上下载最新的库版本，库地址: [M5-Ethernet - M5Stack GitHub](https://github.com/m5stack/M5-Ethernet)，请勿在 Arduino Library 中下载。（如有疑问，请参考[此教程](/zh_CN/arduino/arduino_library#git%E6%89%8B%E5%8A%A8%E5%AE%89%E8%A3%85)）

- 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Base LAN v1.2](https://shop.m5stack.com/products/lan-module-with-w5500-v12)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"/> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/999/Base_LAN_v1.2_3.jpg" width="20%"/>

## 2. 注意事项

\#> 通信拓展板 | LAN BASE V12 标配了 TTL-RS485 + TTL-RS232 两款转接板，用于适配不同通信接口。焊接位置如下，实际链接 GPIO 请参考管脚映射表格。

- RS232 转接板焊接位或 RS485 转接板焊接位

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_07.webp" width="40%"/>

<img src="https://static-cdn.m5stack.com/resource/docs/products/base/lan_v12/lan_v12_08.webp" width="40%"/>

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/base/lan_v12#兼容性)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="K012-B-V12" type="BASE"></ProductCompatible>

## 3. 案例程序

- 本教程中使用的主控设备为 CoreS3 ，搭配 Base LAN v1.2 。本以太网控制器底座具有多种通信接口，根据实际的电路连接修改程序中的引脚定义。

### 3.1 串口数据接收

```cpp line-num
#include <M5Unified.h>

void setup()
{
    M5.begin();
    M5.Display.fillScreen(WHITE);
    M5.Display.setTextFont(&fonts::FreeMono12pt7b);
    M5.Display.setTextColor(BLACK);
    M5.Display.setCursor(0, 0);
    Serial.begin(115200);
    Serial2.begin(115200, SERIAL_8N1, 1, 13);
}

void loop()
{
    M5.Display.setCursor(0, 0);
    M5.Display.printf("M5Stack LAN PoE\n");
    if (Serial.available()) {     // If the serial port receives a
                                  // message. 如果串口收到信息
        int ch = Serial.read();   // Read the message. 读取信息
        Serial2.write(ch);
        M5.Display.fillCircle(100, 65, 15, GREEN);  // Set the light to Green. 设置灯为绿色
    }
    else  M5.Display.fillCircle(100, 65, 15, WHITE);

    Serial2.write('a');
    delay(50);

    if (Serial2.available()) {    // If the serial port receives a
                                  // message. 如果串口收到信息
        int ch = Serial2.read();  // Read the message. 读取信息
        Serial.write(ch);
        M5.Display.fillCircle(100, 65, 15, GREEN);
        delay(50);
    } else  M5.Display.fillCircle(100, 65, 15, WHITE);
}
```

### 3.2 WebServer 使用

- 本 demo 中 PC 和 M5Stack 使用以太网进行数据通信。

```cpp line-num
#include <M5Unified.h>
#include <SPI.h>
#include <M5_Ethernet.h>

#define SCK  36
#define MISO 35
#define MOSI 37
#define CS   9

//  01 05 00 01 02 00 9d 6a
char uart_buffer[8]    = {0x01, 0x05, 0x00, 0x01, 0x02, 0x00, 0x9d, 0x6a};
char uart_rx_buffer[8] = {0};

char Num                   = 0;
char stringnum             = 0;
unsigned long W5500DataNum = 0;
unsigned long Send_Num_Ok  = 0;
unsigned long Rec_Num      = 0;
unsigned long Rec_Num_Ok   = 0;

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
IPAddress ip(192, 168, 1, 177);

// Initialize the Ethernet server library
// with the IP address and port you want to use
// (port 80 is default for HTTP):
EthernetServer server(80);

void setup()
{
    // Open serial communications and wait for port to open:
    M5.begin();
    Serial.begin(115200);
    SPI.begin(SCK, MISO, MOSI, -1);
    Ethernet.init(CS);
    // start the Ethernet connection and the server:
    Ethernet.begin(mac, ip);
    server.begin();
    Serial.print("server is at ");
    Serial.println(Ethernet.localIP());

    M5.Display.fillScreen(WHITE);
    M5.Display.setTextFont(&fonts::FreeMonoBold12pt7b);
    M5.Display.setTextColor(BLACK);
    M5.Display.setCursor(0, 0);
    M5.Display.println("M5Stack W5500 Test");
    M5.Display.print(Ethernet.localIP());
}

void loop()
{
    // listen for incoming clients
    EthernetClient client = server.available();
    if (client) {
        Serial.println("new client");
        // an http request ends with a blank line
        boolean currentLineIsBlank = true;
        while (client.connected()) {
            if (client.available()) {
                char c = client.read();
                Serial.write(c);
                // if you've gotten to the end of the line (received a newline
                // character) and the line is blank, the http request has ended,
                // so you can send a reply
                if (c == '\n' && currentLineIsBlank) {
                    // send a standard http response header
                    client.println("HTTP/1.1 200 OK");
                    client.println("Content-Type: text/html");
                    client.println("Connection: close");  // the connection will be closed
                                                          // after completion of the
                                                          // response
                    client.println("Refresh: 5");         // refresh the page
                                                          // automatically every 5 sec
                    client.println();
                    client.println("<!DOCTYPE HTML>");
                    client.println("<html>");

                    client.println("<body>");
                    client.println("<h1>M5Stack W5500 Test</h1>");
                    client.println("<br />");
                    client.println("<p>Please click here</p>");
                    client.println("<a href=\"http://www.M5Stack.com\">M5Stack</a>");
                    client.println("<br />");
                    client.println("<br />");
                    client.println("<br />");

                    client.print("W5500 Counter Num :");
                    client.print(W5500DataNum);
                    client.println("<br />");
                    client.println("<br />");
                    W5500DataNum++;

                    client.print("Rec_Num_Ok Counter :");
                    client.print(Rec_Num_Ok);
                    client.println("<br />");
                    client.println("<br />");

                    client.print("Rec_Num Counter :");
                    client.print(Rec_Num);
                    client.println("<br />");
                    client.println("<br />");

                    client.println("</body>");

                    client.println("</html>");
                    break;
                }
                if (c == '\n') {
                    // you're starting a new line
                    currentLineIsBlank = true;
                } else if (c != '\r') {
                    // you've gotten a character on the current line
                    currentLineIsBlank = false;
                }
            }
        }
        // give the web browser time to receive the data
        delay(1);
        // close the connection:
        client.stop();
        Serial.println("client disconnected");
    }
}
```

## 4. 编译上传

- 下载模式：不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- CoreS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="30%">

- 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1125/module_fan_v1.1_arduino_example_01.jpg" width="70%">

## 5. 通讯效果

- 串口发送实验：本模块有 RS485 和 RS232 两种通讯方式，在软件的引脚上都是通过 Serial2 进行通讯的。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/999/Base_LAN_v1.2_1.jpg" width="50%">

- WebServer 测试：

1. 使用网线将 PC 与 Base LAN PoE v1.2 模块直连。
2. 在模块端（固件中）将 IP 地址静态配置为 `192.168.1.177`，子网掩码设为 `255.255.255.0`。
3. 在 PC 端的有线网卡属性中，将 IP 地址手动设置为 `192.168.1.x`（ `x` 为 2~254 且不等于 177），子网掩码为 `255.255.255.0`，默认网关可留空。
4. 确认双方处于同一网段，可以通过 `ping 192.168.1.177` 测试连通性。
5. 在 PC 浏览器地址栏输入 `http://192.168.1.177`，即可访问模块内置的网页服务器。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/999/Base_LAN_v1.2_2.jpg" width="40%">
