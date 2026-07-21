# Stamp-S3Bat Camera

Stamp-S3Bat Camera 相关案例程序。

## 案例程序

#> 说明 | Camera 功能需要与 [Stamp-AddOn Cam0308](/zh_CN/stamp/Stamp-AddOn_Cam0308) 摄像头模组配合使用，请确保摄像头排线方向、供电以及接口连接正确后方可运行以下示例程序。

### 编译要求

- M5Stack 板管理版本 >= 3.3.8
- 开发板选项 = M5StampS3Bat
- M5Unified 库版本 >= 0.2.11

#>说明 | 实际应用时，请将下方代码中的 `ssid` 改为实际的 Wi-Fi 名称，`password` 改为实际的 Wi-Fi 密码。  

```cpp line-num
#include <M5Unified.h>
#include <WiFi.h>
#include <WebServer.h>
#include "esp_camera.h"
#include "img_converters.h"

const char *ssid     = "ssid";
const char *password = "password";

WebServer server(80);

static camera_config_t camera_config = {
    .pin_pwdn     = 39,
    .pin_reset    = 41,
    .pin_xclk     = 46,
    .pin_sscb_sda = 48,
    .pin_sscb_scl = 47,
    .pin_d7       = 40,
    .pin_d6       = 38,
    .pin_d5       = 12,
    .pin_d4       = 14,
    .pin_d3       = 15,
    .pin_d2       = 16,
    .pin_d1       = 18,
    .pin_d0       = 21,

    .pin_vsync = 42,
    .pin_href  = 17,
    .pin_pclk  = 13,

    .xclk_freq_hz = 20000000,
    .ledc_timer   = LEDC_TIMER_0,
    .ledc_channel = LEDC_CHANNEL_0,

    .pixel_format  = PIXFORMAT_RGB565,
    .frame_size    = FRAMESIZE_QVGA,
    .jpeg_quality  = 0,
    .fb_count      = 2,
    .fb_location   = CAMERA_FB_IN_PSRAM,
    .grab_mode     = CAMERA_GRAB_WHEN_EMPTY,
    .sccb_i2c_port = -1,
};

const char index_html[] PROGMEM = R"rawliteral(
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Stamp-S3Bat GC0308 Camera</title>
  <style>
    body {
      margin: 0;
      background: #111;
      color: #eee;
      font-family: Arial, sans-serif;
      text-align: center;
    }
    h2 {
      font-size: 20px;
      font-weight: 600;
      margin: 18px 0 8px;
    }
    img {
      width: 100vw;
      max-width: 640px;
      height: auto;
      display: block;
      margin: 0 auto;
    }
  </style>
</head>
<body>
  <h2>Stamp-AddOn Cam0308 Live Stream</h2>
  <img src="/stream" alt="GC0308 live camera stream">
</body>
</html>
)rawliteral";

static bool cameraBegin()
{
    // Release the internal I2C bus before the camera driver configures the SCCB bus.
    M5.In_I2C.release();

    // PWDN is active high on the GC0308 module, so drive it low to keep the sensor awake.
    pinMode(39, OUTPUT);
    digitalWrite(39, LOW);

    // RESETB is active low. Toggle it once to make sure the sensor starts from a known state.
    pinMode(41, OUTPUT);
    digitalWrite(41, LOW);
    delay(20);
    digitalWrite(41, HIGH);
    delay(100);

    // Initialize the ESP camera driver with the Stamp-AddOn Cam0308 DVP pin mapping.
    esp_err_t err = esp_camera_init(&camera_config);
    if (err != ESP_OK) {
        Serial.printf("Camera Init Fail: 0x%x\r\n", err);
        return false;
    }

    // Fetch the detected sensor handle so the frame size can be adjusted after probing.
    sensor_t *sensor = esp_camera_sensor_get();
    if (!sensor) {
        Serial.println("Camera sensor get failed");
        return false;
    }

    sensor->set_framesize(sensor, FRAMESIZE_QVGA);
    Serial.println("Camera Init Success");
    return true;
}

static void handleRoot()
{
    // Serve a compact HTML page that displays the MJPEG stream in a browser image element.
    server.send_P(200, "text/html", index_html);
}

static void handleStream()
{
    WiFiClient client = server.client();

    // Tell the browser that this response is a continuous multipart JPEG stream.
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: multipart/x-mixed-replace; boundary=frame");
    client.println("Access-Control-Allow-Origin: *");
    client.println();

    while (client.connected()) {
        camera_fb_t *fb = esp_camera_fb_get();
        if (!fb) {
            Serial.println("Camera capture failed");
            delay(30);
            continue;
        }

        uint8_t *jpg_buf = nullptr;
        size_t jpg_len   = 0;

        // GC0308 frames are captured as RGB565, so convert each frame to JPEG for the browser.
        bool ok = frame2jpg(fb, 80, &jpg_buf, &jpg_len);
        esp_camera_fb_return(fb);

        if (!ok || !jpg_buf) {
            Serial.println("JPEG convert failed");
            delay(30);
            continue;
        }

        // Send one JPEG frame as a multipart section, then keep the connection open.
        client.printf("--frame\r\n");
        client.printf("Content-Type: image/jpeg\r\n");
        client.printf("Content-Length: %u\r\n\r\n", (unsigned int)jpg_len);
        client.write(jpg_buf, jpg_len);
        client.printf("\r\n");

        free(jpg_buf);

        // A short delay limits CPU usage and leaves time for Wi-Fi background tasks.
        delay(30);
        yield();
    }
}

static void connectWiFi()
{
    WiFi.mode(WIFI_STA);
    WiFi.setSleep(false);
    WiFi.begin(ssid, password);

    Serial.print("Connecting to WiFi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println();
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}

void setup()
{
    Serial.begin(115200);
    delay(1000);

    auto cfg = M5.config();
    M5.begin(cfg);

    if (!cameraBegin()) {
        while (true) {
            delay(1000);
        }
    }

    connectWiFi();

    server.on("/", handleRoot);
    server.on("/stream", handleStream);
    server.begin();

    Serial.println("Web server started");
    Serial.print("Open: http://");
    Serial.println(WiFi.localIP());
}

void loop()
{
    server.handleClient();
    delay(2);
}
```

串口反馈信息示例：

```
Camera Init Success
Connecting to WiFi....
IP address: 192.168.51.95
Web server started
Open: http://192.168.51.95
```

浏览器访问示例：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1256/arduino_stamp_s3bat_camera_stream_example.png" width="100%" />

