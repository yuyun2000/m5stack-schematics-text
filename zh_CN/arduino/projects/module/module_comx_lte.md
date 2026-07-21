# Module COMX LTE Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)

- 使用到的硬件产品：
  - [CoreS3-SE](https://shop.m5stack.com/products/m5stack-cores3-se-iot-controller-w-o-battery-bottom?variant=45170957451521)
  - [Module COMX LTE](https://shop.m5stack.com/products/com-lte-modulesim7600g)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/M5CORES3%20SE/3.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/module/comx_lte/comx_lte_08.webp" width="20%"/>

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/module/comx_lte)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="M031-A" type="MODULE"></ProductCompatible>

## 3. 案例程序

- 本教程中使用的主控设备为 CoreS3-SE，搭配 Module COMX LTE 外接带麦耳机实现拨号通话。使用前请参考下图，将引脚拨码开关，切换到指定位置。

### 3.1 引脚拨码开关

Module COMX LTE 采用串口的方式通讯，请根据实际的电路连接修改程序中的引脚定义，设备连接后对应的串口IO 为 `G1 (RX)`、`G7 (TX)`，实物如下图所示：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/Module_COMX_LTE_PIN.png" width="40%">

#> 说明 | 1\. 若拨码开关 `COM RST` 位置设置为 **ON**，则模块会连接到主控的复位引脚，当主控复位时，模块也会被复位，此时模块初始化时间将会较长，请根据实际需求进行设置。  
2\. 若使用 Core 系列主控设备，可将拨码开关 `25 OUT` 位置设置为 **ON**，使用主控设备内部集成的扬声器作为通话音频输出（**仅适用于 Core 系列**）。

### 3.2 耳机选用

Module COMX LTE 集成了 3.5mm TRRS 耳机插孔，可外接带麦耳机作为通话音频的输入输出，此插孔适配 **17mm** 长度的插头。若使用 14mm 长度的插头，将不能正常使用耳机，请使用类似于下图所示的公对母转接头进行连接：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/Module_COMX_LTE_Headset_adapter.jpg" width="30%">

### 3.3 程序代码

```cpp line-num
#include <M5Unified.h>

// Call-related status variables (volatile for interrupt-safe access)
volatile bool call_connected = false;
volatile bool call_ended     = false;
volatile int  call_result    = 0;   // Call result code: 0=Unknown, 1=Connected, 2=Unanswered, 3=Busy

bool  network_ready = false;
bool  calling       = false;

// Read all available data from LTE module serial port and update call status
// Parses Unsolicited Result Codes (URC) from LTE module to detect call state changes
void readLTEURC()
{
    static String buf;

    while (Serial2.available() > 0) {
        char c = (char)Serial2.read();
        buf += c;
    }

    if (buf.length() == 0) return;

    // Determine call status by matching URC keywords
    if (buf.indexOf("VOICE CALL: BEGIN") != -1) {
        call_connected = true;
        call_result    = 1;
        Serial.println("[COMX LTE URC] CALL CONNECTED (VOICE CALL: BEGIN)");
    }
    if (buf.indexOf("VOICE CALL: END") != -1) {
        call_ended = true;
        Serial.println("[COMX LTE URC] CALL ENDED (VOICE CALL: END)");
    }
    if (buf.indexOf("NO CARRIER") != -1) {
        call_ended = true;
        if (!call_connected) {
            call_result = 2;
        }
        Serial.println("[COMX LTE URC] CALL ENDED (NO CARRIER)");
    }
    if (buf.indexOf("BUSY") != -1) {
        call_ended  = true;
        call_result = 3;
        Serial.println("[COMX LTE URC] CALL BUSY");
    }

    // Print raw OK/ERROR responses (dialing uses sendATandWait's timeout handling)
    if (buf.indexOf("OK") != -1 || buf.indexOf("ERROR") != -1) {
        Serial.print("[COMX LTE RSP RAW] ");
        Serial.println(buf);
    }

    // Clear after processing to prevent overflow
    buf = "";
}

// Send AT command to LTE module and wait for OK/ERROR response with timeout
// @param cmd: AT command string (must include \r\n for line ending)
// @param resp: Reference to store full response from module
// @param timeout_ms: Maximum wait time in milliseconds
// @return: true = "OK" received, false = "ERROR" received or timeout
bool sendATandWait(const String& cmd, String& resp, uint32_t timeout_ms)
{
    resp = "";
    Serial.print("[COMX LTE TX] ");
    Serial.print(cmd);

    Serial2.print(cmd);// Transmit AT command to LTE module

    uint32_t start = millis();
    // Wait for response until timeout expires
    while (millis() - start < timeout_ms) {
        while (Serial2.available() > 0) {
            char c = (char)Serial2.read();
            resp += c;

            // Check for termination conditions (OK/ERROR)
            if (resp.indexOf("OK") != -1) {
                Serial.print("[COMX LTE RSP] ");
                Serial.println(resp);
                return true;
            }
            if (resp.indexOf("ERROR") != -1) {
                Serial.print("[COMX LTE RSP] ");
                Serial.println(resp);
                return false;
            }
        }
        delay(10);
    }

    Serial.print("[COMX LTE RSP TIMEOUT] ");
    Serial.println(resp);
    return false;
}

// Wait for LTE module initialization completion
// Verifies basic AT command responsiveness (OK response to "AT" command)
// @param timeout_ms: Maximum wait time for module to respond
// @return: true = module ready (AT port responsive), false = timeout
bool waitForModuleReady(uint32_t timeout_ms)
{
    uint32_t start = millis();
    Serial.println("[COMX LTE] Waiting for module ready...");
    while (millis() - start < timeout_ms) {
        readLTEURC();                 // 吃掉启动URC/残留输出
        String resp;
        if (sendATandWait("AT\r\n", resp, 1000)) {
            Serial.println("[COMX LTE] Module ready.");
            return true;              // 回复OK，说明AT口已就绪
        }
        delay(200);
    }
    Serial.println("[COMX LTE] Module not ready (timeout).");
    return false;
}

// Wait for SIM7600G network readiness (GPRS attach + LTE network registration)
// Verifies both CGATT (attach) and CEREG (registration) statuses
// @param timeout_ms: Maximum wait time for network registration
// @return: true = network registered, false = timeout
bool waitForNetworkReady(uint32_t timeout_ms)
{
    uint32_t start = millis();
    Serial.println("[COMX LTE] Waiting for network...");

    while (millis() - start < timeout_ms) {
        String resp;

        // 1) Query GPRS attach status: AT+CGATT?
        // Expected response: +CGATT: 1 (attached) / +CGATT: 0 (detached)
        if (sendATandWait("AT+CGATT?\r\n", resp, 2000)) {
            if (resp.indexOf("+CGATT: 1") == -1) {
                Serial.println("[COMX LTE] Not attached, retry...");
                delay(1000);
                continue;
            }
        } else {
            Serial.println("[COMX LTE] CGATT? error, retry...");
            delay(1000);
            continue;
        }

        // 2) Query LTE network registration status: AT+CEREG?
        // Expected responses: 
        // +CEREG: 0,1 = Registered (home network)
        // +CEREG: 0,5 = Registered (roaming network)
        resp = "";
        if (sendATandWait("AT+CEREG?\r\n", resp, 2000)) {
            if (resp.indexOf("+CEREG:") != -1 &&
                (resp.indexOf(",1") != -1 || resp.indexOf(",5") != -1)) {
                Serial.println("[COMX LTE] Network registered.");
                return true;
            } else {
                Serial.println("[COMX LTE] Not registered, retry...");
            }
        } else {
            Serial.println("[COMX LTE] CEREG? error, retry...");
        }

        delay(100);
    }

    Serial.println("[COMX LTE] Network not ready (timeout).");
    return false;
}

void setup()
{
    M5.begin();
    Serial.begin(115200);
    Serial.println("\r\n[COMX LTE] Start");
    Serial2.begin(115200, SERIAL_8N1, 1, 7); // Initialize LTE module serial port RX=1,TX=7

    M5.Display.setFont(&fonts::FreeMonoBold9pt7b);
    M5.Display.setTextDatum(middle_center);
    M5.Display.clear();
    M5.Display.drawString("Module Initializing...", 160, 120);

    delay(500);

    // Initialize LTE module first, then check network status
    if (!waitForModuleReady(25000)) {// Module initialization typically takes up to 20s
        network_ready = false;
    } else {
        network_ready = waitForNetworkReady(30000);
    }

    M5.Display.clear();
    if (network_ready) {
        Serial.println("[COMX LTE] Touch screen to dial/stop");
        M5.Display.drawString("Touch screen to dial", 160, 80);
    } else {
        Serial.println("[COMX LTE] Network NOT ready, please reset.");
        M5.Display.drawString("Network not ready", 160, 120);
    }
}

void loop()
{
    M5.update();
    auto touchDetail = M5.Touch.getDetail();

    // Continuously read URC messages from LTE module
    readLTEURC();

    // Block dialing if network is not fully registered
    if (!network_ready) {
        delay(50);
        return;
    }

    // Handle touch input for dial/hangup control
    if (!calling && touchDetail.wasPressed()) {
        calling          = true;
        call_connected = false;
        call_ended     = false;
        call_result    = 0;

        Serial.println("[COMX LTE] Dialing...");
        M5.Display.clear();
        M5.Display.drawString("Calling......", 160, 120);
        M5.Display.drawString("Touch screen to hang up", 160, 80);

        String resp;
        // ATD command format: ATD<phone_number>
        bool ok = sendATandWait("ATDXXXXXXXXXXX;\r\n", resp, 10000);

        Serial.print("[DIAL RESULT] ");
        Serial.println(ok ? "OK" : "ERROR/TIMEOUT");
    }
    else if (calling && touchDetail.wasPressed()) {
        Serial.println("[COMX LTE] Hangup");
        String resp;
        sendATandWait("AT+CHUP\r\n", resp, 5000);

        calling     = false;
        call_ended  = true; 
        M5.Display.clear();
        M5.Display.drawString("Call ended", 160, 120);
        M5.Display.drawString("Touch screen to dial", 160, 80);
    }

    // Update display based on real-time call status
    if (calling) {
        if (call_connected) {
            M5.Display.clear();
            M5.Display.drawString("Speaking......", 160, 120);
            M5.Display.drawString("Touch screen to hang up", 160, 80);
        }
        if (call_ended) {
            calling = false;
            M5.Display.clear();
            M5.Display.drawString("Call ended", 160, 120);
            M5.Display.drawString("Touch screen to dial", 160, 80);
        }
    }

    delay(20);
}
```

## 4. 编译上传

- 1\. 进入下载模式：CoreS3-SE 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

#> 说明| 不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/498/K128_SE_Download_Mode.gif" width="30%">

- 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/Module_COMX_LTE_example.png" width="70%">

## 5. 拨号通话

- 上电后，Module COMX LTE 模块会自动初始化，并尝试连接网络，连接成功后触摸主控屏幕即可拨号，通话过程中再次触摸主控屏幕即可挂断，并且在屏幕上会显示当前的通话状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/Module_COMX_LTE_Arduino_example_1.jpg" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/Module_COMX_LTE_Arduino_example_2.jpg" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/Module_COMX_LTE_Arduino_example_3.jpg" width="20%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/942/Module_COMX_LTE_Arduino_example_4.jpg" width="20%">

- 以下为串口监视器的输出示例：

```
[COMX LTE] Start
[COMX LTE] Waiting for module ready...
[COMX LTE TX] AT
[COMX LTE RSP] AT

OK
[COMX LTE] Module ready.
[COMX LTE] Waiting for network...
[COMX LTE TX] AT+CGATT?
[COMX LTE RSP] 
AT+CGATT?

+CGATT: 1

OK
[COMX LTE TX] AT+CEREG?
[COMX LTE RSP] 
AT+CEREG?

+CEREG: 0,1

OK
[COMX LTE] Network registered.
[COMX LTE] Touch screen to dial/stop
[COMX LTE] Dialing...
[COMX LTE TX] ATDXXXXXXXXXX;
[COMX LTE RSP] ATDXXXXXXXXXX;

OK
[DIAL RESULT] OK
[COMX LTE URC] CALL CONNECTED (VOICE CALL: BEGIN)
[COMX LTE] Hangup
[COMX LTE TX] AT+CHUP
[COMX LTE RSP] AT+CHUP

VOICE CALL: END: 000008

OK
```
