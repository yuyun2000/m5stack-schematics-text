# UnitV/StickV Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [Arduino_JSON](https://github.com/arduino-libraries/Arduino_JSON)

- 使用到的硬件产品：
  - [Core2 v1.1](https://shop.m5stack.com/products/m5stack-core2-esp32-iot-development-kit)
  - [StickV](https://shop.m5stack.com/products/stickv?variant=40115186729132)
  - [UnitV-OV7740](https://shop.m5stack.com/products/unitv-k210-edge-computing-ai-camera-ov7740)
  - [UnitV-M12](https://shop.m5stack.com/products/unitv-k210-ai-camera-m12-version-ov7740)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/Core2%20v1.1/img-9eb726ec-5729-42c3-9cce-e06140856095.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/core/m5stickv/m5stickv_cover_01.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/unitv_ov7740/unitv_ov7740_cover_01.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/UNIT-V%20M12/img-2149e60a-2402-4e1e-8f96-97e46b6a1aff.webp" width="20%">

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，为了让用户更方便地使用，M5Stack 官方提供了引脚兼容性表，请根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="K027" type="Stick"></ProductCompatible>

## 3. 编译上传

- 请根据需要复制粘贴下方例程代码到项目代码区，然后选中设备端口（详情请参考 [程序编译与烧录](/zh_CN/arduino/m5core2/program)），点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_Arduino.png" width="70%">

## 4. 案例程序

?> 说明 | 1.UnitV/StickV 的设置和返回数据格式均为 JSON，各功能的 JSON 数据格式请见例程前提示。  
2.UnitV/StickV 需要通过 **USB Type-C** 接口供电才能工作，USB Type-C 接口拔插后本单元会重启。  
3.M5Burner 中的固件**并非所有功能下都有默认参数设置**，且本单元设置的参数**掉电会丢失**，故本单元断电重启后需要再配置一次设置参数。

下方所有例程功能为主机**配置和解析 UnitV/StickV 的 JSON 数据**，不能达到切换 UnitV/StickV 的功能，切换功能请在 M5Burner 中 `STICKV & UNITV` 界面中选择烧录对应功能固件到 UnitV/StickV。  

### 4.1 运动目标检测

该功能固件如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_M5Burner_MotionTracker.png" width="70%">

运动目标检测功能可配置两种检测模式：静态检测模式（`COMPUTE_MODE_STATIC`）和动态检测模式（`COMPUTE_MODE_DYNAMIC`），M5Burner 中的固件默认为动态检测模式。

运动目标检测功能 JSON 数据格式详见[此处](/zh_CN/guide/ai_camera/unitv/v_function#运动目标检测)。

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <Arduino_JSON.h>

M5GFX display;
int motion_cnt = 0;

void setup() {

    display.begin();
    display.setRotation(1);
    display.clear(TFT_WHITE);
    display.setFont(&fonts::FreeMonoBold9pt7b);
    display.setTextColor(TFT_BLACK);
    delay(100);
    display.drawString("UnitV Json Example", 5, 5);
    display.drawLine(0, 25, 320, 25, TFT_BLACK);

    Serial.begin(115200);
    Serial2.begin(115200, SERIAL_8N1, 13, 14);//PORT.C

    //Setting JSON
    JSONVar obj;
    obj["MOTION DETECT"] = 1.0;                     // Not optional                     
    obj["mode"] = "COMPUTE_MODE_DYNAMIC";           // "COMPUTE_MODE_STATIC" or "COMPUTE_MODE_DYNAMIC"
    obj["thr_w"] = 20;                              // optional
    obj["thr_h"] = 20;                              // optional
    obj["stepx"] = 1;                               // optional
    obj["stepy"] = 2;                               // optional
    obj["delta"] = 20;                              // optional
    obj["merge"] = 10;                              // optional
    String jsonString = JSON.stringify(obj);
    Serial2.println(jsonString);
    Serial2.flush();
}

void loop() {

    if (Serial2.available() > 0) {
      String line = Serial2.readStringUntil('\r');
      while (line.length() && line[0] != '{') {// clear '\0'
          line.remove(0, 1);
      }
      Serial2.flush();

      JSONVar motion_detect_obj = JSON.parse(line);

      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (!(JSON.typeof(motion_detect_obj) == "undefined")){
        display.fillRect(0, 35, 320, 205, TFT_WHITE);
        Serial.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
        Serial.println("M5Stack Motion Detect V-Func example");
        if (motion_detect_obj.hasOwnProperty("FUNC")) {
          Serial.print("V-Function = ");
          Serial.println((const char*) motion_detect_obj["FUNC"]);
          display.setCursor(0, 35);
          display.printf(" V-Fun: %s\n", (const char*) motion_detect_obj["FUNC"]);
        }
        if (motion_detect_obj.hasOwnProperty("DIFF TOTAL")) {
          Serial.print("Diff TOTAL = ");
          Serial.println((int)motion_detect_obj["DIFF TOTAL"]);
          display.printf(" Diff TOTAL: %d\n", (int)motion_detect_obj["DIFF TOTAL"]);
        }
        if (motion_detect_obj.hasOwnProperty("DIFF MAX")) {
          Serial.print("Diff MAX = ");
          Serial.println((int)motion_detect_obj["DIFF MAX"]);
          display.printf(" Diff MAX: %d\n", (int)motion_detect_obj["DIFF MAX"]);
        }

        if (motion_detect_obj.hasOwnProperty("TOTAL")) {
          motion_cnt = (int)motion_detect_obj["TOTAL"];
          Serial.printf("Motion number = %d\n", motion_cnt);
          display.printf(" Motion number: %d\n", motion_cnt);
        }
        for (int i = 0; i < motion_cnt; i++) {
          display.setCursor(0, 120);
          display.fillRect(0, 120, 320, 130, TFT_WHITE);
          Serial.print("Motion ");
          Serial.print(i);
          display.printf("Motion %d:", i);
          Serial.print(":\r\n\tX:");
          Serial.println((int) motion_detect_obj[String(i)]["x"]);
          display.printf("\r\n\t X: %d", (int) motion_detect_obj[String(i)]["x"]);
          Serial.print("\tY:");
          Serial.println((int) motion_detect_obj[String(i)]["y"]);
          display.printf("\r\n\t Y: %d", (int) motion_detect_obj[String(i)]["y"]);
          Serial.print("\tWidth:");
          Serial.println((int) motion_detect_obj[String(i)]["w"]);
          display.printf("\r\n\t Width: %d", (int) motion_detect_obj[String(i)]["w"]);
          Serial.print("\tHeight:");
          Serial.println((int) motion_detect_obj[String(i)]["h"]);
          display.printf("\r\n\t Height: %d", (int) motion_detect_obj[String(i)]["h"]);
          Serial.print("\tArea:");
          Serial.println((int) motion_detect_obj[String(i)]["area"]);
          display.printf("\r\n\t Area: %d", (int) motion_detect_obj[String(i)]["area"]);
          delay(500);
        }
        Serial.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
      } else {
        return;
      }
    }
}
```

上方例程使用动态检测模式，当 StickV/UnitV 检测到物体运动时，会实时反馈物体所处位置等数据，检测结果如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_motion_detect_example.jpg" width="40%">

### 4.2 目标追踪

该功能固件如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_M5Burner_ObjectTracker.png" width="70%">

目标追踪功能需要在 UnitV/StickV 上电后抓取目前摄像头画面中目标物体的信息后才能正常使用，抓取起点及长宽参数设置代码如下所示，想要自定义抓取位置请修改此处。

```cpp
    obj["x"] = 80;  //start point x-coordinate           
    obj["y"] = 0;   //start point y-coordinate                             
    obj["w"] = 100; //width                            
    obj["h"] = 100; //heigth
```

目标追踪功能 JSON 数据格式详见[此处](/zh_CN/guide/ai_camera/unitv/v_function#目标追踪)。

下方例程会在主机上电后发送一次参数设置数据，此时 StickV 页面如下图所示，请确保追踪目标位于黄色抓取框中。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_object_track_example_1.jpg" width="40%">

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <Arduino_JSON.h>

M5GFX display;

void setup() {

    display.begin();
    display.setRotation(1);
    display.clear(TFT_WHITE);
    display.setFont(&fonts::FreeMonoBold9pt7b);
    display.setTextColor(TFT_BLACK);
    delay(100);
    display.drawString("UnitV Json Example", 5, 5);
    display.drawLine(0, 25, 320, 25, TFT_BLACK);

    Serial.begin(115200);
    Serial2.begin(115200, SERIAL_8N1, 13, 14);//PORT.C

    //Setting JSON
    JSONVar obj;
    obj["TARGET TRACKER"] = " V1.0";                     
    obj["x"] = 80;            
    obj["y"] = 0;                              
    obj["w"] = 100;                              
    obj["h"] = 100;                               
    String jsonString = JSON.stringify(obj);
    Serial2.println(jsonString);
    Serial2.flush();
}

void loop() {

    if (Serial2.available() > 0) {
      String line = Serial2.readStringUntil('\r');
      while (line.length() && line[0] != '{') {  // clear '\0'
        line.remove(0, 1);
      }
      Serial2.flush();

      JSONVar object = JSON.parse(line);

      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (!(JSON.typeof(object) == "undefined")){
        display.fillRect(0, 35, 320, 205, TFT_WHITE);
        Serial.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
        Serial.println("M5Stack Target Tracker V-Func example");
        if (object.hasOwnProperty("FUNC")) {
          Serial.print("V-Function = ");
          Serial.println((const char*) object["FUNC"]);
          display.setCursor(0, 35);
          display.printf(" V-Fun: %s\n", (const char*) object["FUNC"]);
        }
        if (object.hasOwnProperty("x")) {
          Serial.print("X: ");
          Serial.println((int) object["x"]);
          display.printf(" X: %d\n", (int) object["x"]);
        }
        if (object.hasOwnProperty("y")) {
          Serial.print("Y: ");
          Serial.println((int) object["y"]);
          display.printf(" Y: %d\n", (int) object["y"]);
        }
        if (object.hasOwnProperty("w")) {
          Serial.print("Width: ");
          Serial.println((int) object["w"]);
          display.printf(" Width: %d\n", (int) object["w"]);
        }
        if (object.hasOwnProperty("h")) {
          Serial.print("Height: ");
          Serial.println((int) object["h"]);
          display.printf(" Height: %d\n", (int) object["h"]);
        }
        display.waitDisplay();
        Serial.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
      } else {
        return;
      }
    }
}
```

成功抓取目标物体数据后，主机会实时显示打印目标物体所处位置等数据，检测结果如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_object_track_example_2.jpg" width="40%">

### 4.3 颜色追踪

该功能固件如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_M5Burner_ColorTracker.png" width="70%">

颜色追踪功能需要在 UnitV/StickV 上电后设置所追踪颜色参数才能正常使用，颜色参数获取需要使用[LAB 取色工具](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/LAB-Color-Tool.exe)。  
获取颜色参数获取及配置步骤如下：
- 打开工具后点击下方所示工具页面的 `open` 处打开采样图片（本例程[示例图片](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_color_track_Sample_pic.jpg)），然后点击图片中需要采样的具体位置，根据下方白色区域（即采样具体位置）确定最终的颜色参数。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/LAB_tool.png" width="60%">

- 将上图中的 `LAB color` 按照**从左到右**的顺序填入下方代码处（从上到下）即可。

```cpp
    obj["Lmin"] = 0;               
    obj["Lmax"] = 100;              
    obj["Amin"] = 51;               
    obj["Amax"] = 61;               
    obj["Bmin"] = 34;               
    obj["Bmax"] = 44;
```

颜色追踪功能 JSON 数据格式详见[此处](/zh_CN/guide/ai_camera/unitv/v_function#43-颜色追踪)。

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <Arduino_JSON.h>

M5GFX display;

void setup() {

    display.begin();
    display.setRotation(1);
    display.clear(TFT_WHITE);
    display.setFont(&fonts::FreeMonoBold9pt7b);
    display.setTextColor(TFT_BLACK);
    delay(100);
    display.drawString("UnitV Json Example", 2, 2);
    display.drawLine(0, 20, 320, 20, TFT_BLACK);

    Serial.begin(115200);
    Serial2.begin(115200, SERIAL_8N1, 13, 14);//PORT.C

    //Setting JSON
    JSONVar obj;
    obj["COLOR TRACKER"] = 1.0;    
    obj["thr_w"] = 20;             
    obj["thr_h"] = 20;             
    obj["stepx"] = 2;              
    obj["stepy"] = 2;              
    obj["merge"] = 10;             
    //Please fill in the below six parameters with the values extracted from the LAB color selection tool.
    obj["Lmin"] = 0;               
    obj["Lmax"] = 100;              
    obj["Amin"] = 51;               
    obj["Amax"] = 61;               
    obj["Bmin"] = 34;               
    obj["Bmax"] = 44;               
    String jsonString = JSON.stringify(obj);
    Serial2.println(jsonString);
    Serial2.flush();
}

void loop() {

    if (Serial2.available() > 0) {
      String line = Serial2.readStringUntil('\r');
      while (line.length() && line[0] != '{') {  // clear '\0'
        line.remove(0, 1);
      }
      Serial2.flush();

      JSONVar color_obj = JSON.parse(line);

      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (!(JSON.typeof(color_obj) == "undefined")) {
        display.fillRect(0, 35, 320, 205, TFT_WHITE);
        Serial.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
        Serial.println("M5Stack Color Tracker V-Func example");
        if (color_obj.hasOwnProperty("FUNC")) {
          Serial.print("V-Function = ");
          Serial.println((const char*) color_obj["FUNC"]);
          display.setCursor(0, 35);
          display.printf(" V-Fun: %s\n", (const char*) color_obj["FUNC"]);
        }
        int box_cnt = 0;
        if (color_obj.hasOwnProperty("TOTAL")) {
          box_cnt = (int)color_obj["TOTAL"];
          Serial.printf("Box number = %d\n", box_cnt);
          display.printf(" Box number: %d\n", box_cnt);
        }
        for (int i = 0; i < box_cnt; i++) {
          Serial.print("Box ");
          Serial.print(i);
          display.printf("Box %d:", i);
          Serial.print(":\r\n\tX:");
          Serial.println((int) color_obj[String(i)]["x"]);
          display.printf("\r\n\t X: %d", (int) color_obj[String(i)]["x"]);
          Serial.print("\tY:");
          Serial.println((int) color_obj[String(i)]["y"]);
          display.printf("\r\n\t Y: %d", (int) color_obj[String(i)]["y"]);
          Serial.print("\tWidth:");
          Serial.println((int) color_obj[String(i)]["w"]);
          display.printf("\r\n\t Width: %d", (int) color_obj[String(i)]["w"]);
          Serial.print("\tHeight:");
          Serial.println((int) color_obj[String(i)]["h"]);
          display.printf("\r\n\t Height: %d", (int) color_obj[String(i)]["h"]);
          Serial.print("\tArea:");
          Serial.println((int) color_obj[String(i)]["area"]);
          display.printf("\r\n\t Area: %d\r\n\t", (int) color_obj[String(i)]["area"]);
        }
        Serial.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
      }
      delay(50);
    }
} 
```

例程成功运行时，主机会实时显示打印追踪颜色块所处位置、大小、数量等数据，检测结果如下图所示。（多个追踪颜色块情况下建议使用串口查看反馈数据）

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_color_track_example.jpg" width="40%">

### 4.4 人脸检测

该功能固件如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_M5Burner_FaceDetect.png" width="70%">

人脸检测功能 JSON 数据格式详见[此处](/zh_CN/guide/ai_camera/unitv/v_function#人脸识别)。

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <Arduino_JSON.h>

M5GFX display;
int face_cnt;

void setup() {

  display.begin();
  display.setRotation(1);
  display.clear(TFT_WHITE);
  display.setFont(&fonts::FreeMonoBold9pt7b);
  display.setTextColor(TFT_BLACK);
  delay(100);
  display.drawString("UnitV Json Example", 5, 5);
  display.drawLine(0, 25, 320, 25, TFT_BLACK);

  Serial.begin(115200);
  Serial2.begin(115200, SERIAL_8N1, 13, 14);//PORT.C
}

void loop() {

  if (Serial2.available() > 0) {
    String line = Serial2.readStringUntil('\r');
    while (line.length() && line[0] != '{') {  // clear '\0'
      line.remove(0, 1);
    }
    Serial2.flush();

    JSONVar face_detect_obj = JSON.parse(line);

    // JSON.typeof(jsonVar) can be used to get the type of the var
    if (!(JSON.typeof(face_detect_obj) == "undefined")) {
      display.fillRect(0, 35, 320, 205, TFT_WHITE);
      // display.drawString("Parsing Json succeed!", 5, 30);
      Serial.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
      Serial.println("M5Stack Face Detect V-Func example");
      if (face_detect_obj.hasOwnProperty("FUNC")) {
        Serial.print("V-Function = ");
        Serial.println((const char*)face_detect_obj["FUNC"]);
        display.setCursor(0, 35);
        display.printf(" V-Fun: %s\n", (const char*)face_detect_obj["FUNC"]);
      }

      if (face_detect_obj.hasOwnProperty("count")) {
        face_cnt = (int)face_detect_obj["count"];
        Serial.printf("Face number = %d\n", face_cnt);
        display.printf(" Face number: %d\n", face_cnt);
      }

      for (int i = 0; i < face_cnt; i++) {
        Serial.print("Face ");
        Serial.print(i + 1);
        display.printf("Face %d:", i);
        Serial.print(":\r\n\tX:");
        Serial.println((int)face_detect_obj[String(i)]["x"]);
        display.printf("\r\n\t X: %d", (int)face_detect_obj[String(i)]["x"]);
        Serial.print("\tY:");
        Serial.println((int)face_detect_obj[String(i)]["y"]);
        display.printf("\r\n\t Y: %d", (int)face_detect_obj[String(i)]["y"]);
        Serial.print("\tWidth:");
        Serial.println((int)face_detect_obj[String(i)]["w"]);
        display.printf("\r\n\t Width: %d", (int)face_detect_obj[String(i)]["w"]);
        Serial.print("\tHeight:");
        Serial.println((int)face_detect_obj[String(i)]["h"]);
        display.printf("\r\n\t Height: %d", (int)face_detect_obj[String(i)]["h"]);
        Serial.print("\tConfidence:");
        Serial.println(face_detect_obj[String(i)]["value"]);
        display.printf("\r\n\t Confidence:");
        display.println(face_detect_obj[String(i)]["value"]);
      }
      Serial.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
    } else {
      return;
    }
  }
} 
```

扫描下方左边人脸，检测结果如下方右图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/detect_face.jpg" width="35%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_face_detect_example.jpg" width="35%">

### 4.5 二维码识别

扫码功能固件如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_M5Burner_FindCode.png" width="70%">

二维码识别功能 JSON 数据格式详见[此处](/zh_CN/guide/ai_camera/unitv/v_function#二维码识别)。

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <Arduino_JSON.h>

M5GFX display;

void setup() {

    display.begin();
    display.setRotation(1);
    display.clear(TFT_WHITE);
    display.setFont(&fonts::FreeMonoBold9pt7b);
    display.setTextColor(TFT_BLACK);
    delay(100);
    display.drawString("UnitV Json Example", 5, 5);
    display.drawLine(0, 25, 320, 25, TFT_BLACK);

    Serial.begin(115200);
    Serial2.begin(115200, SERIAL_8N1, 13, 14);//PORT.C

    //Setting JSON
    JSONVar obj;
    obj["FIND CODE"] = 1.0;                    
    obj["mode"] = "QRCODE";      // Recognition mode, optional: QRCODE, APRILTAG, DATAMATRIX, BARCODE
    String jsonString = JSON.stringify(obj);
    Serial2.println(jsonString);
    Serial2.flush();
}

void loop() {

    if (Serial2.available() > 0) {
      String line = Serial2.readStringUntil('\r');
      while (line.length() && line[0] != '{') {  // clear '\0'
        line.remove(0, 1);
      }
      Serial2.flush();

      JSONVar code_obj = JSON.parse(line);

      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (!(JSON.typeof(code_obj) == "undefined")){
        display.fillRect(0, 35, 320, 205, TFT_WHITE);
        Serial.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
        Serial.println("M5Stack QRCode Detect V-Func example");
        if (code_obj.hasOwnProperty("FUNC")) {
          Serial.print("V-Function = ");
          Serial.println((const char*) code_obj["FUNC"]);
          display.setCursor(0, 35);
          display.printf(" V-Fun: %s\n", (const char*) code_obj["FUNC"]);
        }
        int qrcode_cnt = 0;
        if (code_obj.hasOwnProperty("count")) {
          qrcode_cnt = (int)code_obj["count"];
          Serial.printf("QR Code number = %d\n", qrcode_cnt);
          display.printf(" QR Code number: %d\n", qrcode_cnt);
        }
        for (int i = 0; i < qrcode_cnt; i++) {
          Serial.print("QRCode ");
          Serial.print(i);
          display.printf("QRCode %d:", i);
          Serial.print(":\r\n\tX:");
          Serial.println((int) code_obj[String(i)]["x"]);
          display.printf("\r\n\t X: %d", (int) code_obj[String(i)]["x"]);
          Serial.print("\tY:");
          Serial.println((int) code_obj[String(i)]["y"]);
          display.printf("        Y: %d", (int) code_obj[String(i)]["y"]);
          Serial.print("\tWidth:");
          Serial.println((int) code_obj[String(i)]["w"]);
          display.printf("\r\n\t Width: %d", (int) code_obj[String(i)]["w"]);
          Serial.print("\tHeight:");
          Serial.println((int) code_obj[String(i)]["h"]);
          display.printf("    Height: %d", (int) code_obj[String(i)]["h"]);
          Serial.print("\tPayload:");
          Serial.println((const char*) code_obj[String(i)]["payload"]);
          display.printf("\r\n\t Payload: %s", (const char*) code_obj[String(i)]["payload"]);
          Serial.print("\tVersion:");
          Serial.println((int) code_obj[String(i)]["version"]);
          display.printf("\r\n\t Version: %d", (int) code_obj[String(i)]["version"]);
          Serial.print("\tECC Level:");
          Serial.println((int) code_obj[String(i)]["ecc_level"]);
          display.printf("\r\n\t ECC Level: %d", (int) code_obj[String(i)]["ecc_level"]);
          Serial.print("\tMask:");
          Serial.println((int) code_obj[String(i)]["mask"]);
          display.printf("\r\n\t Mask: %d", (int) code_obj[String(i)]["mask"]);
          Serial.print("\tData Type:");
          Serial.println((int) code_obj[String(i)]["data_type"]);
          display.printf("\r\n\t Data Type: %d", (int) code_obj[String(i)]["data_type"]);
          Serial.print("\tECI:");
          Serial.println((int) code_obj[String(i)]["eci"]);
          display.printf("\r\n\t ECI: %d", (int) code_obj[String(i)]["eci"]);
        }
        Serial.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
      }
      delay(50);
    }
}
```

扫描下方左边二维码，检测结果如下方右图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/M5Stack_QRCode.png" width="33%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_QRCode_example.jpg" width="35%">

### 4.6 条形码识别

条形码识别功能 JSON 数据格式详见[此处](/zh_CN/guide/ai_camera/unitv/v_function#条形码识别)。

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <Arduino_JSON.h>

M5GFX display;

void setup() {

    display.begin();
    display.setRotation(1);
    display.clear(TFT_WHITE);
    display.setFont(&fonts::FreeMonoBold9pt7b);
    display.setTextColor(TFT_BLACK);
    delay(100);
    display.drawString("UnitV Json Example", 5, 5);
    display.drawLine(0, 25, 320, 25, TFT_BLACK);

    Serial.begin(115200);
    Serial2.begin(115200, SERIAL_8N1, 13, 14);//PORT.C

    JSONVar obj;
    obj["FIND CODE"] = 1.0;        
    obj["mode"] = "BARCODE";       // Recognition mode, optional: QRCODE, APRILTAG, DATAMATRIX, BARCODE
    String jsonString = JSON.stringify(obj);
    Serial2.println(jsonString);
    Serial2.flush();
}

void loop() {

    if (Serial2.available() > 0) {
      String line = Serial2.readStringUntil('\r');
      while (line.length() && line[0] != '{') {  // clear '\0'
        line.remove(0, 1);
      }
      Serial2.flush();

      JSONVar code_obj = JSON.parse(line);

      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (!(JSON.typeof(code_obj) == "undefined")){
        display.fillRect(0, 35, 320, 205, TFT_WHITE);
        Serial.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
        Serial.println("M5Stack Barcode Detect V-Func example");
        if (code_obj.hasOwnProperty("FUNC")) {
          Serial.print("V-Function = ");
          Serial.println((const char*) code_obj["FUNC"]);
          display.setCursor(0, 35);
          display.printf(" V-Fun: %s\n", (const char*) code_obj["FUNC"]);
        }
        int barcode_cnt = 0;
        if (code_obj.hasOwnProperty("count")) {
          barcode_cnt = (int)code_obj["count"];
          Serial.printf("Barcode number = %d\n", barcode_cnt);
          display.printf(" Barcode number: %d\n", barcode_cnt);
        }
        for (int i = 0; i < barcode_cnt; i++) {
          Serial.print("Barcode ");
          Serial.print(i);
          display.printf("Barcode %d:", i);
          Serial.print(":\r\n\tX:");
          Serial.println((int) code_obj[String(i)]["x"]);
          display.printf("\r\n\t X: %d", (int) code_obj[String(i)]["x"]);
          Serial.print("\tY:");
          Serial.println((int) code_obj[String(i)]["y"]);
          display.printf("\r\n\t Y: %d", (int) code_obj[String(i)]["y"]);
          Serial.print("\tWidth:");
          Serial.println((int) code_obj[String(i)]["w"]);
          display.printf("\r\n\t Width: %d", (int) code_obj[String(i)]["w"]);
          Serial.print("\tHeight:");
          Serial.println((int) code_obj[String(i)]["h"]);
          display.printf("\r\n\t Height: %d", (int) code_obj[String(i)]["h"]);
          Serial.print("\tPayload:");
          Serial.println((const char*) code_obj[String(i)]["payload"]);
          display.printf("\r\n\t Payload: %s", (const char*) code_obj[String(i)]["payload"]);
          Serial.print("\tType:");
          Serial.println((int) code_obj[String(i)]["type"]);
          display.printf("\r\n\t Type: %d", (int) code_obj[String(i)]["type"]);
          Serial.print("\tRotation:");
          Serial.println((double) code_obj[String(i)]["rotation"]);
          display.printf("\r\n\t Rotation: %f", (double) code_obj[String(i)]["rotation"]);
          Serial.print("\tQuality:");
          Serial.println((int) code_obj[String(i)]["quality"]);
          display.printf("\r\n\t Quality: %d", (int) code_obj[String(i)]["quality"]);
        }
        Serial.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
      }
      delay(50);
    }
}
```

扫描下方条形码，检测结果如下图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/M5Stack_BarCode.png" width="35%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_BarCode_example.jpg" width="35%">

### 4.7 Datamatrix 码识别

Datamatrix 码识别功能 JSON 数据格式详见[此处](/zh_CN/guide/ai_camera/unitv/v_function#datamatrix码识别)。

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <Arduino_JSON.h>

M5GFX display;

void setup() {

    display.begin();
    display.setRotation(1);
    display.clear(TFT_WHITE);
    display.setFont(&fonts::FreeMonoBold9pt7b);
    display.setTextColor(TFT_BLACK);
    delay(100);
    display.drawString("UnitV Json Example", 5, 5);
    display.drawLine(0, 25, 320, 25, TFT_BLACK);

    Serial.begin(115200);
    Serial2.begin(115200, SERIAL_8N1, 13, 14);//PORT.C

    JSONVar obj;
    obj["FIND CODE"] = 1.0;                   
    obj["mode"] = "DATAMATRIX";      // Recognition mode, optional: QRCODE, APRILTAG, DATAMATRIX, BARCODE
    String jsonString = JSON.stringify(obj);
    Serial2.println(jsonString);
    Serial2.flush();
}

void loop() {

    if (Serial2.available() > 0) {
      String line = Serial2.readStringUntil('\r');
      while (line.length() && line[0] != '{') {  // clear '\0'
        line.remove(0, 1);
      }
      Serial2.flush();

      JSONVar code_obj = JSON.parse(line);

      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (!(JSON.typeof(code_obj) == "undefined")){
        display.fillRect(0, 40, 320, 200, TFT_WHITE);
        Serial.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
        Serial.println("M5Stack DataMatrix Detect V-Func example");
        if (code_obj.hasOwnProperty("FUNC")) {
          Serial.print("V-Function = ");
          Serial.println((const char*) code_obj["FUNC"]);
          display.setCursor(0, 35);
          display.printf(" V-Fun: %s\n", (const char*) code_obj["FUNC"]);
        }
        int dm_cnt = 0;
        if (code_obj.hasOwnProperty("count")) {
          dm_cnt = (int)code_obj["count"];
          Serial.printf("DataMatrix number = %d\n", dm_cnt);
          display.printf(" DataMatrix number: %d\n", dm_cnt);
        }
        for (int i = 0; i < dm_cnt; i++) {
          Serial.print("DataMatrix ");
          Serial.print(i);
          display.printf("DataMatrix %d:", i);
          Serial.print(":\r\n\tX:");
          Serial.println((int) code_obj[String(i)]["x"]);
          display.printf("\r\n\t X: %d", (int) code_obj[String(i)]["x"]);
          Serial.print("\tY:");
          Serial.println((int) code_obj[String(i)]["y"]);
          display.printf("       Y: %d", (int) code_obj[String(i)]["y"]);
          Serial.print("\tWidth:");
          Serial.println((int) code_obj[String(i)]["w"]);
          display.printf("\r\n\t Width: %d", (int) code_obj[String(i)]["w"]);
          Serial.print("\tHeight:");
          Serial.println((int) code_obj[String(i)]["h"]);
          display.printf("    Height: %d", (int) code_obj[String(i)]["h"]);
          Serial.print("\tPayload:");
          Serial.println((const char*) code_obj[String(i)]["payload"]);
          display.printf("\r\n\t Payload: %s", (const char*) code_obj[String(i)]["payload"]);
          Serial.print("\tRotation:");
          Serial.println((double) code_obj[String(i)]["rotation"]);
          display.printf("\r\n\t Rotation: %f", (double) code_obj[String(i)]["rotation"]);
          Serial.print("\tRows:");
          Serial.println((int) code_obj[String(i)]["rows"]);
          display.printf("\r\n\t Rows: %d", (int) code_obj[String(i)]["rows"]);
          Serial.print("\tColumns:");
          Serial.println((int) code_obj[String(i)]["columns"]);
          display.printf("     Columns: %d", (int) code_obj[String(i)]["columns"]);
          Serial.print("\tCapacity:");
          Serial.println((int) code_obj[String(i)]["capacity"]);
          display.printf("\r\n\t Capacity: %d", (int) code_obj[String(i)]["capacity"]);
          Serial.print("\tPadding:");
          Serial.println((int) code_obj[String(i)]["padding"]);
          display.printf("\r\n\t Padding: %d", (int) code_obj[String(i)]["padding"]);
        }
        Serial.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
      }
      delay(50);
    }
}
```

扫描下方左边 Datamatrix 码，检测结果如下方右图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/M5Stack_DataMatrix.png" width="28%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_DataMatrix_example.jpg" width="35%">

### 4.8 Apriltag 码识别

Apriltag 码识别功能 JSON 数据格式详见[此处](/zh_CN/guide/ai_camera/unitv/v_function#apriltag码识别)。

?>说明 | UnitV/StickV 仅支持识别 TAG36H11 家族的 Apriltag 码。

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <Arduino_JSON.h>

M5GFX display;

void setup() {

    display.begin();
    display.setRotation(1);
    display.clear(TFT_WHITE);
    display.setFont(&fonts::Font2);
    display.setTextColor(TFT_BLACK);
    delay(100);
    display.drawString("UnitV Json Example", 2, 2);
    display.drawLine(0, 20, 320, 20, TFT_BLACK);

    Serial.begin(115200);
    Serial2.begin(115200, SERIAL_8N1, 13, 14);//PORT.C

    JSONVar obj;
    obj["FIND CODE"] = 1.0;                    
    obj["mode"] = "APRILTAG";      // Recognition mode, optional: QRCODE, APRILTAG, DATAMATRIX, BARCODE
    String jsonString = JSON.stringify(obj);
    Serial2.println(jsonString);
    Serial2.flush();
}

void loop() {

    if (Serial2.available() > 0) {
      String line = Serial2.readStringUntil('\r');
      while (line.length() && line[0] != '{') {  // clear '\0'
        line.remove(0, 1);
      }
      Serial2.flush();

      JSONVar code_obj = JSON.parse(line);

      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (!(JSON.typeof(code_obj) == "undefined")){
        display.fillRect(0, 25, 320, 215, TFT_WHITE);
        Serial.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
        Serial.println("M5Stack AprilTag Detect V-Func example");
        if (code_obj.hasOwnProperty("FUNC")) {
          Serial.print("V-Function = ");
          Serial.println((const char*) code_obj["FUNC"]);
          display.setCursor(0, 25);
          display.printf(" V-Fun: %s\n", (const char*) code_obj["FUNC"]);
        }
        int april_cnt = 0;
        if (code_obj.hasOwnProperty("count")) {
          april_cnt = (int)code_obj["count"];
          Serial.printf("AprilTag number = %d\n", april_cnt);
          display.printf(" AprilTag number: %d\n", april_cnt);
        }
        for (int i = 0; i < april_cnt; i++) {
          Serial.print("AprilTag ");
          Serial.print(i);
          display.printf("AprilTag %d:", i);
          Serial.print(":\r\n\tX:");
          Serial.println((int) code_obj[String(i)]["x"]);
          display.printf("  X: %d", (int) code_obj[String(i)]["x"]);
          Serial.print("\tY:");
          Serial.println((int) code_obj[String(i)]["y"]);
          display.printf("  Y: %d", (int) code_obj[String(i)]["y"]);
          Serial.print("\tWidth:");
          Serial.println((int) code_obj[String(i)]["w"]);
          display.printf("  Width: %d", (int) code_obj[String(i)]["w"]);
          Serial.print("\tHeight:");
          Serial.println((int) code_obj[String(i)]["h"]);
          display.printf("  Height: %d", (int) code_obj[String(i)]["h"]);
          Serial.print("\tID:");
          Serial.println((int) code_obj[String(i)]["id"]);
          display.printf("\r\n\t ID: %d", (int) code_obj[String(i)]["id"]);
          Serial.print("\tFamily:");
          Serial.println((int) code_obj[String(i)]["family"]);
          display.printf("    Family: %d", (int) code_obj[String(i)]["family"]);
          Serial.print("\tCX:");
          Serial.println((int) code_obj[String(i)]["cx"]);
          display.printf("    CX: %d", (int) code_obj[String(i)]["cx"]);
          Serial.print("\tCY:");
          Serial.println((int) code_obj[String(i)]["cy"]);
          display.printf("    CY: %d", (int) code_obj[String(i)]["cy"]);
          Serial.print("\tRotation:");
          Serial.println((double) code_obj[String(i)]["rotation"]);
          display.printf("\r\n\t Rotation: %f", (double) code_obj[String(i)]["rotation"]);
          Serial.print("\tDecision margin:");
          Serial.println((double) code_obj[String(i)]["decision_margin"]);
          display.printf("\r\n\t Decision margin: %f", (double) code_obj[String(i)]["decision_margin"]);
          Serial.print("\tHamming:");
          Serial.println((int) code_obj[String(i)]["hamming"]);
          display.printf("    Hamming: %d", (int) code_obj[String(i)]["hamming"]);
          Serial.print("\tGoodness:");
          Serial.println((double) code_obj[String(i)]["goodness"]);
          display.printf("\r\n\t Goodness: %f", (double) code_obj[String(i)]["goodness"]);
          Serial.print("\tX translation:");
          Serial.println((double) code_obj[String(i)]["x_translation"]);
          display.printf("\r\n\t X translation: %f", (double) code_obj[String(i)]["x_translation"]);
          Serial.print("\tY translation:");
          Serial.println((double) code_obj[String(i)]["y_translation"]);
          display.printf("\r\n\t Y translation: %f", (double) code_obj[String(i)]["y_translation"]);
          Serial.print("\tZ translation:");
          Serial.println((double) code_obj[String(i)]["z_translation"]);
          display.printf("\r\n\t Z translation: %f", (double) code_obj[String(i)]["z_translation"]);
          Serial.print("\tX rotation:");
          Serial.println((double) code_obj[String(i)]["x_rotation"]);
          display.printf("\r\n\t X rotation: %f", (double) code_obj[String(i)]["x_rotation"]);
          Serial.print("\tY rotation:");
          Serial.println((double) code_obj[String(i)]["y_rotation"]);
          display.printf("\r\n\t Y rotation: %f", (double) code_obj[String(i)]["y_rotation"]);
          Serial.print("\tZ rotation:");
          Serial.println((double) code_obj[String(i)]["z_rotation"]);
          display.printf("\r\n\t Z rotation: %f", (double) code_obj[String(i)]["z_rotation"]);
        }
        Serial.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
      }
      delay(50);
    }
}
```

扫描下方左边 Apriltag 码，检测结果如下方右图所示。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/M5Stack_Apriltag.png" width="35%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_Aprialtag_example.jpg" width="35%">

<!-- ### 自定义标签识别

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <Arduino_JSON.h>

M5GFX display;

void setup() {

    display.begin();
    display.setRotation(1);
    display.clear(TFT_WHITE);
    display.setFont(&fonts::FreeMonoBold9pt7b);
    display.setTextColor(TFT_BLACK);
    delay(100);
    display.drawString("UnitV Json Example", 5, 5);
    display.drawLine(0, 25, 320, 25, TFT_BLACK);

    // Print the result.
    Serial.begin(115200);

    // Serial2.begin(unsigned long baud, uint32_t config, int8_t rxPin, int8_t txPin, bool invert)
    Serial2.begin(115200, SERIAL_8N1, 13, 14);//PORT.C

    //Setting JSON
    JSONVar obj;
    obj["FIND CODE"] = 1.0;                    
    obj["mode"] = "QRCODE";      // Recognition mode, optional: QRCODE, APRILTAG, DATAMATRIX, BARCODE
    String jsonString = JSON.stringify(obj);
    Serial2.println(jsonString);
    Serial2.flush();
}

void loop() {

    if (Serial2.available() > 0) {
      String line = Serial2.readStringUntil('\r');
      while (line.length() && line[0] != '{') {  // clear '\0'
        line.remove(0, 1);
      }
      Serial2.flush();

      JSONVar code_obj = JSON.parse(line);

      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (!(JSON.typeof(code_obj) == "undefined")){
        display.fillRect(0, 35, 320, 205, TFT_WHITE);
        Serial.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
        Serial.println("M5Stack QRCode Detect V-Func example");
        if (code_obj.hasOwnProperty("FUNC")) {
          Serial.print("V-Function = ");
          Serial.println((const char*) code_obj["FUNC"]);
          display.setCursor(0, 35);
          display.printf(" V-Fun: %s\n", (const char*) code_obj["FUNC"]);
        }
        int qrcode_cnt = 0;
        if (code_obj.hasOwnProperty("count")) {
          qrcode_cnt = (int)code_obj["count"];
          Serial.printf("QR Code number = %d\n", qrcode_cnt);
          display.printf(" QR Code number: %d\n", qrcode_cnt);
        }
        for (int i = 0; i < qrcode_cnt; i++) {
          Serial.print("QRCode ");
          Serial.print(i);
          display.printf("QRCode %d:", i);
          Serial.print(":\r\n\tX:");
          Serial.println((int) code_obj[String(i)]["x"]);
          display.printf("\r\n\t X: %d", (int) code_obj[String(i)]["x"]);
          Serial.print("\tY:");
          Serial.println((int) code_obj[String(i)]["y"]);
          display.printf("        Y: %d", (int) code_obj[String(i)]["y"]);
          Serial.print("\tWidth:");
          Serial.println((int) code_obj[String(i)]["w"]);
          display.printf("\r\n\t Width: %d", (int) code_obj[String(i)]["w"]);
          Serial.print("\tHeight:");
          Serial.println((int) code_obj[String(i)]["h"]);
          display.printf("    Height: %d", (int) code_obj[String(i)]["h"]);
          Serial.print("\tPayload:");
          Serial.println((const char*) code_obj[String(i)]["payload"]);
          display.printf("\r\n\t Payload: %s", (const char*) code_obj[String(i)]["payload"]);
          Serial.print("\tVersion:");
          Serial.println((int) code_obj[String(i)]["version"]);
          display.printf("\r\n\t Version: %d", (int) code_obj[String(i)]["version"]);
          Serial.print("\tECC Level:");
          Serial.println((int) code_obj[String(i)]["ecc_level"]);
          display.printf("\r\n\t ECC Level: %d", (int) code_obj[String(i)]["ecc_level"]);
          Serial.print("\tMask:");
          Serial.println((int) code_obj[String(i)]["mask"]);
          display.printf("\r\n\t Mask: %d", (int) code_obj[String(i)]["mask"]);
          Serial.print("\tData Type:");
          Serial.println((int) code_obj[String(i)]["data_type"]);
          display.printf("\r\n\t Data Type: %d", (int) code_obj[String(i)]["data_type"]);
          Serial.print("\tECI:");
          Serial.println((int) code_obj[String(i)]["eci"]);
          display.printf("\r\n\t ECI: %d", (int) code_obj[String(i)]["eci"]);
        }
        Serial.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
      }
      delay(50);
    }
}
``` -->

### 4.9 巡线

该功能固件如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_M5Burner_LineTracker.png" width="70%">

巡线功能需要在 UnitV/StickV 上电后设置追踪线条颜色参数才能正常使用，颜色参数获取需要使用[LAB 取色工具](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/software/LAB-Color-Tool.exe)。  
获取及配置颜色参数与[颜色追踪](#43-颜色追踪)相同，权重（weight）取样区域示例图如下，请根据自身需要自行设置比例值。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_Weight_Sample_region.png" width="35%">

巡线功能 JSON 数据格式详见[此处](/zh_CN/guide/ai_camera/unitv/v_function#巡线)。

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <Arduino_JSON.h>

M5GFX display;

void setup() {

    display.begin();
    display.setRotation(1);
    display.clear(TFT_WHITE);
    display.setFont(&fonts::FreeMonoBold9pt7b);
    display.setTextColor(TFT_BLACK);
    delay(100);
    display.drawString("UnitV Json Example", 5, 5);
    display.drawLine(0, 25, 320, 25, TFT_BLACK);

    Serial.begin(115200);
    Serial2.begin(115200, SERIAL_8N1, 13, 14);//PORT.C

    //Setting JSON
    JSONVar obj;
    obj["LINE  TRACKER"] = 1.0;    
    obj["thr_w"] = 20;             
    obj["thr_h"] = 20;             
    obj["stepx"] = 2;              
    obj["stepy"] = 2;              
    obj["merge"] = 10;             
    //Please fill in the below six parameters with the values extracted from the LAB color selection tool.
    obj["Lmin"] = 0;               
    obj["Lmax"] = 100;              
    obj["Amin"] = 51;               
    obj["Amax"] = 61;               
    obj["Bmin"] = 34;               
    obj["Bmax"] = 44;                
    obj["weight_0"] = 0.1;          
    obj["weight_1"] = 0.3;          
    obj["weight_2"] = 0.6;          
    String jsonString = JSON.stringify(obj);
    Serial2.println(jsonString);
    Serial2.flush();
}

void loop() {

    if (Serial2.available() > 0) {
      String line = Serial2.readStringUntil('\r');
      while (line.length() && line[0] != '{') {  // clear '\0'
        line.remove(0, 1);
      }
      Serial2.flush();

      JSONVar line_obj = JSON.parse(line);

      // JSON.typeof(jsonVar) can be used to get the type of the var
      if (!(JSON.typeof(line_obj) == "undefined")){
        display.fillRect(0, 40, 320, 200, TFT_WHITE);
        Serial.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
        Serial.println("M5Stack Line Tracker V-Func example");
        if (line_obj.hasOwnProperty("FUNC")) {
          Serial.print("V-Function = ");
          Serial.println((const char*) line_obj["FUNC"]);
          display.setCursor(0, 35);
          display.printf(" V-Fun: %s\n", (const char*) line_obj["FUNC"]);
        }
        if (line_obj.hasOwnProperty("angle")) {
          Serial.print("Angle: ");
          Serial.println((double) line_obj["angle"]);
          display.printf(" Angle: %f\n", (double) line_obj["angle"]);
        }
        Serial.println("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<");
      } else {
        return;
      }
    }
}  
```

例程成功运行时，主机会实时显示打印转弯角度。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1056/UnitV_line_track_example.jpg" width="35%">
