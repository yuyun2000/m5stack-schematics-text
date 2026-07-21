# Unit Fingerprint2 Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [M5Unit-Fingerprint2](https://github.com/m5stack/M5Unit-Fingerprint2)

- 使用到的硬件产品：
  - [CoreS3](https://shop.m5stack.com/products/m5stack-cores3-esp32s3-lotdevelopment-kit)
  - [Unit Fingerprint2](https://shop.m5stack.com/products/fingerprint-2-unit-a-k323cp)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/CoreS3/img-2f6b5728-af80-4934-854f-4771a7fe859e.webp" width="20%"/> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/U203-mainpictures_02.webp" width="20%"/>

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/unit/Unit_Fingerprint2)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U203" type="UNIT"></ProductCompatible> 

## 3. 案例程序

- 本教程中使用的主控设备为 CoreS3 ，搭配 Unit Fingerprint2。本指纹识别模块采用串口的方式通讯，根据实际的电路连接修改程序中的引脚定义，设备连接后对应的串口 IO 为 `G17 (RX)`，`G18 (TX)`。

### 3.1 灯光设置

本指纹传感器内置 RGB 灯，可以通过使用 `PS_ControlBLN` 函数设置灯光的颜色与模式，可根据需要选用下方定义。

#### PS_ControlBLN

**函数原型：**

```cpp
fingerprint_status_t PS_ControlBLN(
    fingerprint_led_control_mode_t mode,  
    fingerprint_led_color_t startColor,  
    fingerprint_led_color_t endColor,  
    uint8_t loopCount = 0             
) const;
```

**传入参数：**

- `mode`：灯光模式，见下方 `fingerprint_led_control_mode_t`。
- `startColor`：起始颜色，见下方 `fingerprint_led_color_t`，**仅在普通呼吸灯模式下有效**。
- `endColor`：结束颜色，见下方 `fingerprint_led_color_t`。
- `loopCount`：循环次数，0 表示无限循环，N 表示循环 N 次，**仅呼吸、闪烁模式下有效**。

**返回值：**

- `FINGERPRINT_OK`：设置成功
- 其他值表示失败，具体定义请见库文件 `fingerprint_status_t`。

**相关定义：**

- `fingerprint_led_control_mode_t`

```cpp
typedef enum {
  FINGERPRINT_LED_BREATHING = 1,  // 普通呼吸灯 / Normal breathing light
  FINGERPRINT_LED_FLASHING  = 2,  // 闪烁灯 / Flashing light
  FINGERPRINT_LED_ON        = 3,  // 常开灯 / Always on
  FINGERPRINT_LED_OFF       = 4,  // 常闭灯 / Always off
  FINGERPRINT_LED_FADE_IN   = 5,  // 渐开灯 / Fade in
  FINGERPRINT_LED_FADE_OUT  = 6   // 渐闭灯 / Fade out
} fingerprint_led_control_mode_t;
```

- `fingerprint_led_color_t`

```cpp
typedef enum {
  FINGERPRINT_LED_COLOR_OFF    = 0x00,  // 全灭 / All off
  FINGERPRINT_LED_COLOR_BLUE   = 0x01,  // 蓝灯 / Blue
  FINGERPRINT_LED_COLOR_GREEN  = 0x02,  // 绿灯 / Green
  FINGERPRINT_LED_COLOR_CYAN   = 0x03,  // 青色灯 (蓝+绿) / Cyan (Blue + Green)
  FINGERPRINT_LED_COLOR_RED    = 0x04,  // 红灯 / Red
  FINGERPRINT_LED_COLOR_PURPLE = 0x05,  // 紫色灯 (蓝+红) / Purple (Blue + Red)
  FINGERPRINT_LED_COLOR_YELLOW = 0x06,  // 黄色灯 (绿+红) / Yellow (Green + Red)
  FINGERPRINT_LED_COLOR_WHITE  = 0x07   // 白色灯 (蓝+绿+红) / White (Blue + Green + Red)
} fingerprint_led_color_t;
```

#>说明 | 模块上电后默认灯光为无限循环蓝色呼吸灯，调用 PS_ControlBLN 函数设置后`掉电不保存该设置`。

```cpp line-num
#include <Arduino.h>
#include <M5UnitFingerprint2.hpp>    
#include <M5Unified.hpp>          

M5Canvas canvas(&M5.Lcd);   
M5UnitFingerprint2 fp2(&Serial1, 17, 18);  // Initialize fingerprint sensor

void setup() {
    Serial.begin(115200);             
    M5.begin();                      
    fp2.begin();// Hardware Interface Init                  
    canvas.createSprite(320, 240); 
    canvas.fillScreen(TFT_BLACK); 
    canvas.setTextColor(TFT_WHITE); 
    canvas.setFont(&fonts::FreeMonoBold9pt7b);

    // Activate the fingerprint module (prepares it to accept commands; must required)
    if (fp2.PS_ActivateFingerprintModule() == FINGERPRINT_OK) { // Software-based activation, ready to receive commands
      canvas.drawString("Fingerprint2 Ready", 2, 45);  
      Serial.printf("Fingerprint2 Ready\n");          
    } else {
      canvas.drawString("Fingerprint2 Init Failed", 2, 45); 
      Serial.printf("Fingerprint2 Init Failed\n");    
    }
    canvas.pushSprite(0, 0);
}

void loop() {
    fp2.PS_ControlBLN(FINGERPRINT_LED_BREATHING, FINGERPRINT_LED_COLOR_GREEN, FINGERPRINT_LED_COLOR_BLUE, 0); /// 0-endless loop, N-loop N times
    delay(2000);
    fp2.PS_ControlBLN(FINGERPRINT_LED_FLASHING, FINGERPRINT_LED_COLOR_RED, FINGERPRINT_LED_COLOR_RED, 0); /// 0-endless loop, N-loop N times
    delay(2000);
    fp2.PS_ControlBLN(FINGERPRINT_LED_FADE_IN, FINGERPRINT_LED_COLOR_CYAN, FINGERPRINT_LED_COLOR_CYAN, 0); 
    delay(2000);
    fp2.PS_ControlBLN(FINGERPRINT_LED_FADE_OUT, FINGERPRINT_LED_COLOR_YELLOW, FINGERPRINT_LED_COLOR_YELLOW, 0); 
    delay(2000);
    fp2.PS_ControlBLN(FINGERPRINT_LED_ON, FINGERPRINT_LED_COLOR_PURPLE, FINGERPRINT_LED_COLOR_PURPLE, 0); 
    delay(2000);
}  
```

### 3.2 指纹图像获取显示

```cpp line-num
#include <Arduino.h>
#include <M5UnitFingerprint2.hpp>
#include <M5Unified.hpp>

M5Canvas canvas(&M5.Lcd);
int fingerPresentCount = 0;              // Counter for consecutive finger detection

M5UnitFingerprint2 fp2(&Serial1, 17, 18);  // Fingerprint sensor

bool displayFingerprintImage(M5UnitFingerprint2& fp2, uint32_t maxBufferSize, M5Canvas& canvas,
                             int displayX, int displayY, uint8_t rotation);

void setup() {
    Serial.begin(115200);
    M5.begin();
    fp2.begin();

    canvas.createSprite(320, 240);
    canvas.fillScreen(TFT_BLACK);
    canvas.setTextColor(TFT_WHITE, TFT_BLACK);
    canvas.setFont(&fonts::FreeMonoBold9pt7b);
    canvas.drawString("Unit Fingerprint2 Image", 2, 0);
    Serial.println("<-------Unit Fingerprint2 Image------->");
    canvas.drawLine(0, 20, 320, 20, TFT_WHITE);

    // Activate fingerprint sensor module
    if (fp2.PS_ActivateFingerprintModule() == FINGERPRINT_OK) {
      canvas.drawString("Fingerprint2 Ready", 2, 45);
      canvas.drawString("Please place finger......", 2, 75);
      Serial.printf("Fingerprint2 Ready\n");
    } else {
      canvas.drawString("Fingerprint2 Init Failed", 2, 45);
      Serial.printf("Fingerprint2 Init Failed\n");
    }

    canvas.pushSprite(0, 0);
}

void loop() {
    M5.update();  
    delay(200);    // Light delay to reduce CPU usage
    fingerprint_status_t result = fp2.PS_GetImage();
    // PS_GetImage can be replaced by PS_GetImageInfo to further verify the quality of the fingerprint image. 
    if (result == FINGERPRINT_OK) {
      fingerPresentCount++;
      Serial.printf("Finger detected! Count: %d/3\n", fingerPresentCount);
      canvas.fillRect(0, 41, 320, 240, TFT_BLACK);
      canvas.setCursor(2, 60);
      canvas.printf("Finger detected! Count: %d/3\n", fingerPresentCount);
      canvas.pushSprite(0, 0);
      // Show fingerprint image after 3 consecutive detections
      if (fingerPresentCount >= 3) {
        Serial.println("Entering displayFingerprintImage.");
        if (displayFingerprintImage(fp2, 1024 * 16, canvas, 56, 100, 1)) {
          Serial.println("Fingerprint image displayed successfully.");
          delay(1000);
        } else {
          Serial.println("Failed to display fingerprint image.");
        }
        canvas.pushSprite(0, 0);
        fingerPresentCount = 0;   // Reset count
      }
    } else {
      // No finger detected, reset count
      if (fingerPresentCount > 0) {
        Serial.println("Finger removed, resetting count.");
        fingerPresentCount = 0;
      }
    }
}

bool displayFingerprintImage(M5UnitFingerprint2& fp2, uint32_t maxBufferSize, M5Canvas& canvas,
                             int displayX, int displayY, uint8_t rotation) {
    // Allocate buffer for image
    uint8_t* imageBuffer = (uint8_t*)malloc(maxBufferSize);
    if (imageBuffer == nullptr) {
      Serial.println("Failed to allocate memory for image buffer.");
      canvas.setCursor(2, 60);
      canvas.printf("Memory allocation failed");
      return false;
    }
    // Upload image data from sensor
    uint32_t actualImageSize = 0;
    fingerprint_status_t result = fp2.PS_UpImage(imageBuffer, maxBufferSize, actualImageSize);
    if (result == FINGERPRINT_OK) {
      Serial.printf("Image uploaded successfully, size: %d bytes\r\n", actualImageSize);
      // Display image info on canvas
      canvas.fillRect(0, 41, 320, 240, TFT_BLACK);
      canvas.setCursor(2, 60);
      canvas.printf("Image size: %d bytes", actualImageSize);

      if (actualImageSize > 0) {
        const int imageWidth = 80;
        const int imageHeight = 208;
        for (int y = 0; y < imageHeight && y < 220; y++) {   // Limit height
          for (int x = 0; x < imageWidth && x < 200; x++) {  // Limit width
            int byteIndex = (y * imageWidth + x) / 2;
            if (byteIndex < actualImageSize) {
              // Extract 4-bit pixel value
              uint8_t pixelValue;
              if ((y * imageWidth + x) % 2 == 0) {
                pixelValue = imageBuffer[byteIndex] & 0x0F;
              } else {
                pixelValue = (imageBuffer[byteIndex] & 0xF0) >> 4;
              }
              // Map 4-bit to grayscale RGB565
              uint8_t grayValue = pixelValue * 17;  // Scale to 0-255
              uint16_t rgb565 = ((grayValue >> 3) << 11) | ((grayValue >> 2) << 5) | (grayValue >> 3);
              // Compute rotated pixel position
              int drawX, drawY;
              switch (rotation) {
                case 0:  // No rotation
                  drawX = displayX + x; drawY = displayY + y; break;
                case 1:  // 90 degrees clockwise
                  drawX = displayX + imageHeight - 1 - y; drawY = displayY + x; break;
                case 2:  // 180 degrees
                  drawX = displayX + imageWidth - 1 - x; drawY = displayY + imageHeight - 1 - y; break;
                case 3:  // 270 degrees (counterclockwise)
                  drawX = displayX + y; drawY = displayY + imageWidth - 1 - x; break;
                default:  // Default: 90 degrees clockwise
                  drawX = displayX + imageHeight - 1 - y; drawY = displayY + x; break;
              }
              canvas.drawPixel(drawX, drawY, rgb565);
            }
          }
        }
      }
      free(imageBuffer);
      return true;
    } else {
      Serial.println("Failed to upload image.");
      canvas.setCursor(2, 60);
      canvas.printf("Failed to upload image");
      free(imageBuffer);
      return false;
    }
}
```

### 3.3 指纹录入

本例程采用自动录入方式（使用 `PS_AutoEnroll` 函数），用户只需将手指放在传感器上，系统会自动完成图像采集、特征提取与模板合成等步骤，最终生成指纹模板并存储在模块内的数据库中。若想按步骤发送相应指令进行指纹录入，可参考 [Fingerprint2 串口通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/Unit-Fingerprint-Protocol-CN-V1.0.pdf)使用 `PS_GetImage`、`PS_GenChar`、`PS_RegModel`、`PS_StoreChar` 等函数。

#### PS_AutoEnroll

**函数原型：**

```cpp
fingerprint_status_t PS_AutoEnroll(
    uint16_t ID,
    uint8_t enrollCount,
    fingerprint_auto_enroll_flags_t flags,
    uint8_t* param1 = nullptr,
    uint8_t* param2= nullptr,
    PS_AutoEnrollCallback_t callback = nullptr
) const; 
```

**传入参数：**

- `ID`：指纹的唯一编号，范围为 0~99。
- `enrollCount`：录入时需要采集的指纹样本数量，有效值 1-6，数值越大生成的模板越可靠，但录入时间也会相应增加。
- `flags`：录入选项，可按位组合使用，具体定义见 `fingerprint_auto_enroll_flags_t`。
- `param1`、`param2`：可选输出参数，param1 -- 阶段码，param2 -- 状态/错误码，具体定义请见下方 `ps_auto_enroll_param1_t`/`fingerprint_auto_enroll_stage_t`、`ps_auto_enroll_param2_t`。
- `callback`：回调函数（可选），回调函数会在**每个阶段完成后被调用（即使用 `PS_AutoEnroll` 后会被多次调用）**，详细内容请见库文件中 `PS_AutoEnroll` 定义。

**返回值：**

- `FINGERPRINT_OK`：成功
- 其他值表示失败，具体定义请见库文件 `fingerprint_status_t`。

#### PS_AutoEnroll_callback

**函数原型：**

```cpp
bool PS_AutoEnroll_callback(
    uint16_t ID,
    fingerprint_status_t confirmationCode,
    uint8_t param1,
    uint8_t param2,
    int packetCount
) const;
```
**传入参数：**

- `ID`：当前录入的指纹 ID。
- `confirmationCode`：当前阶段的状态码，`FINGERPRINT_OK` 表示成功，具体定义请见库文件 `fingerprint_status_t`。
- `param1`：当前阶段码，具体定义请见 `ps_auto_enroll_param1_t`。
- `param2`：当前状态/错误码，具体定义请见 `ps_auto_enroll_param2_t`。
- `packetCount`：当前回调函数调用次数（当前已处理的数据包数量），从 0 开始计数。

**相关定义：**

- `fingerprint_auto_enroll_flags_t`
```cpp
typedef enum {
    FINGERPRINT_AUTO_ENROLL_DEFAULT              = 0x0000, // 默认设置 / Default setting
    FINGERPRINT_AUTO_ENROLL_NO_STATUS_RETURN     = (1 << 2), // 注册过程中不返回当前状态 / Don't return current status during enrollment
    FINGERPRINT_AUTO_ENROLL_ALLOW_OVERWRITE_ID   = (1 << 3), // 允许覆盖已存在的ID号 / Allow overwriting existing ID
    FINGERPRINT_AUTO_ENROLL_FORBID_DUPLICATES    = (1 << 4), // 禁止指纹重复注册 / Forbid duplicate fingerprint enrollment
    FINGERPRINT_AUTO_ENROLL_NO_LIFT_REQUIRED     = (1 << 5), // 采集间不要求手指离开 / No finger lift required between captures
} fingerprint_auto_enroll_flags_t;
```

- `ps_auto_enroll_param1_t`
```cpp
typedef enum : uint8_t {
    PS_AUTO_ENROLL_PARAM1_LEGAL_CHECK   = 0x00, // 指纹合法性检测 / Fingerprint legality check
    PS_AUTO_ENROLL_PARAM1_GET_IMAGE     = 0x01, // 获取图像 / Get image
    PS_AUTO_ENROLL_PARAM1_GEN_CHAR      = 0x02, // 生成特征 / Generate characteristics
    PS_AUTO_ENROLL_PARAM1_LIFT_FINGER   = 0x03, // 判断手指离开 / Check finger lift
    PS_AUTO_ENROLL_PARAM1_MERGE_TEMPLATE= 0x04, // 合并模板 / Merge template
    PS_AUTO_ENROLL_PARAM1_VERIFY        = 0x05, // 注册验证 / Enrollment verification
    PS_AUTO_ENROLL_PARAM1_STORE         = 0x06  // 存储模板 / Store template
} ps_auto_enroll_param1_t;
```

- `ps_auto_enroll_param2_t`

```cpp
typedef enum : uint8_t {
    PS_AUTO_ENROLL_PARAM2_OK                = 0x00, // 指纹合法性检测 / Fingerprint legality check
    PS_AUTO_ENROLL_PARAM2_MERGE_TEMPLATE    = 0xF0, // 合并模板 / Merge template
    PS_AUTO_ENROLL_PARAM2_FINGER_DUPLICATED = 0xF1, // 检验该手指是否已注册 / Check if finger is already registered
    PS_AUTO_ENROLL_PARAM2_STORE_TEMPLATE    = 0xF2, // 存储模板 / Store template
} ps_auto_enroll_param2_t;
```

下方例程中使用回调函数获取当前录入过程状态并反馈相关信息。

```cpp line-num
#include <Arduino.h>
#include <M5UnitFingerprint2.hpp>    
#include <M5Unified.hpp>          

M5Canvas canvas(&M5.Lcd);   
M5UnitFingerprint2 fp2(&Serial1, 17, 18);  // Initialize fingerprint sensor

uint16_t enrollID = 0;                // Unique ID for the fingerprint being enrolled (range: 0~99, cycles after 99)
const uint8_t enrollCount = 3;        // Number of fingerprint samples needed to create a reliable template (3 = standard)
bool waitingForTouch = true;          // Flag to track if the system is waiting for a screen touch to start enrollment

void setup() {
    Serial.begin(115200);             
    M5.begin();                      
    fp2.begin();                  
    canvas.createSprite(320, 240); 
    canvas.fillScreen(TFT_BLACK); 
    canvas.setTextColor(TFT_WHITE); 
    canvas.setFont(&fonts::FreeMonoBold9pt7b);
    canvas.drawString("Unit Fingerprint2 Enroll", 2, 0);
    Serial.println("<-------Unit Fingerprint2 Enroll------->"); 
    canvas.drawLine(0, 20, 320, 20, TFT_WHITE);

    // Activate the fingerprint module (prepares it to accept commands; required before enrollment/verification)
    if (fp2.PS_ActivateFingerprintModule() == FINGERPRINT_OK) { // Software-based activation
      canvas.drawString("Fingerprint2 Ready", 2, 45);  
      Serial.printf("Fingerprint2 Ready\n");          
    } else {
      canvas.drawString("Fingerprint2 Init Failed", 2, 45); 
      Serial.printf("Fingerprint2 Init Failed\n");    
    }

    // Set sensor work mode: 1 = Always-on (sensor stays active), 0 = Timed sleep (auto-sleeps to save power)
    fp2.PS_SetWorkMode(1);
    fp2.PS_Empty();// Clear all fingerprint database

    // Prompt user to touch the screen to start fingerprint enrollment
    canvas.drawString("Touch screen to enroll", 2, 70);
    canvas.pushSprite(0, 0);  // Update LCD with all canvas content (renders drawn elements)
    Serial.println("Waiting for touch to start enrollment...");  // Debug message for user action
}

void loop() {
    M5.update(); 
    if (waitingForTouch) {
        if (M5.Touch.getCount() && M5.Touch.getDetail().wasPressed()) {
            waitingForTouch = false; 
            canvas.fillRect(0, 70, 320, 170, TFT_BLACK);  
            canvas.setCursor(2, 70);
            canvas.printf("Enrolling Fingerprint ID: %d", enrollID); 
            canvas.drawString("Place finger to enroll...", 10, 90); 
            canvas.pushSprite(0, 0);  
            Serial.printf("Start enrolling fingerprint, ID=%d. Please place your finger...\n", enrollID); 

            uint8_t param1 = 0, param2 = 0; 
            // Start automatic enrollment:
            // Parameters: ID, sample count, flags (overwrite existing ID + no finger lift needed), output params, callback
            fingerprint_status_t result = fp2.PS_AutoEnroll(
                enrollID, enrollCount, 
                (fingerprint_auto_enroll_flags_t)(FINGERPRINT_AUTO_ENROLL_ALLOW_OVERWRITE_ID |
                                                  FINGERPRINT_AUTO_ENROLL_NO_LIFT_REQUIRED),
                &param1, &param2, PS_AutoEnroll_callback);

            canvas.fillRect(0, 90, 320, 150, TFT_BLACK); 
            if (result == FINGERPRINT_OK) {
                canvas.setCursor(2, 100);
                canvas.printf("ID:%d Enroll Success!", enrollID);
                Serial.printf("Fingerprint enrolled successfully! ID=%d\n", enrollID);
                enrollID = (enrollID + 1) % 100; 
            } else {
                canvas.drawString("Enroll Failed!", 2, 100);
                Serial.println("Fingerprint enrollment failed!"); 
            }
            canvas.drawString("Touch screen to enroll next", 10, 130);
            canvas.pushSprite(0, 0); 
            waitingForTouch = true; 
            delay(200); 
        }
    }
    delay(20); 
}

// Callback function for PS_AutoEnroll: updates status during each enrollment stage (runs automatically)
// Returns true to continue enrollment, false to abort (based on success of current stage)
bool PS_AutoEnroll_callback(uint16_t ID, fingerprint_status_t confirmationCode, uint8_t param1, uint8_t param2, int packetCount) {
    static int enrollStep = 0;  // Static variable: tracks current sample step (persists between callback calls)
    switch (param1) {
        // Stage 1: Capture fingerprint image from sensor
        case FINGERPRINT_AUTO_ENROLL_GET_IMAGE:
            if (confirmationCode == FINGERPRINT_OK) {
                enrollStep++;  // Increment step after successful image capture
                canvas.setCursor(10, 90);
                canvas.fillRect(0, 90, 320, 150, TFT_BLACK);  // Clear previous status
                canvas.printf("#%d:Image acquired success", enrollStep);  // Show step success
                Serial.printf("#%d:Image acquired success\n", enrollStep);  // Debug step success
            }
            break;
        
        // Stage 2: Extract fingerprint features (converts image to digital template data)
        case FINGERPRINT_AUTO_ENROLL_GEN_CHAR:
            if (confirmationCode == FINGERPRINT_OK) {
                canvas.setCursor(10, 110);
                canvas.printf("#%d:Feature generated success", enrollStep);  // Show feature success
                Serial.printf("#%d:Feature generated success\n", enrollStep);  // Debug feature success
            }
            break;
        
        // Stage 3: Merge multiple feature samples into a single, reliable template
        case FINGERPRINT_AUTO_ENROLL_MERGE_TEMPLATE:
            if (confirmationCode == FINGERPRINT_OK) {
                canvas.setCursor(10, 130);
                canvas.printf("Template merged success");  // Show merge success
                Serial.println("Template merged success");  // Debug merge success
            }
            break;
        
        // Stage 4: Verify merged template (ensures template is valid for future recognition)
        case FINGERPRINT_AUTO_ENROLL_VERIFY:
            if (confirmationCode == FINGERPRINT_OK) {
                canvas.setCursor(10, 150);
                canvas.printf("Template verified success");  // Show verification success
                Serial.println("Template verified success");  // Debug verification success
            }
            break;
        
        // Stage 5: Save verified template to sensor memory (links to enrollment ID)
        case FINGERPRINT_AUTO_ENROLL_STORE_TEMPLATE:
            if (confirmationCode == FINGERPRINT_OK) {
                canvas.setCursor(10, 170);
                canvas.printf("Template stored success,ID=%d", ID);  // Show storage success + ID
                Serial.printf("Template stored success,ID=%d\n", ID);  // Debug storage success
                enrollStep = 0;  // Reset step counter for next enrollment
            }
            break;
        
        default:
            break;  // Ignore unrecognized stages
    }
    canvas.pushSprite(0, 0); 
    return (confirmationCode == FINGERPRINT_OK);  // Continue enrollment only if current stage succeeded
} 
```

### 3.4 指纹识别

本例程采用自动识别方式（使用 `PS_AutoIdentify` 函数），用户只需将手指放在传感器上，系统会自动完成图像采集、特征提取与模板比对等步骤，最终返回匹配结果。若想按步骤发送相应指令进行指纹识别，可参考 [Fingerprint2 串口通信协议](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/Unit-Fingerprint-Protocol-CN-V1.0.pdf)使用 `PS_GetImage`、`PS_GenChar`、`PS_Search` 等函数。

#### PS_AutoIdentify

**函数原型：**

```cpp
fingerprint_status_t PS_AutoIdentify(
    uint8_t securityLevel,               
    uint16_t ID,                       
    fingerprint_auto_verify_flags_t flags,
    uint16_t& matchedID,       
    PS_AutoIdentifyCallback_t callback = nullptr
) const;
```

**传入参数：**

- `securityLevel`：安全等级，0 或 1，数值越大匹配越严格。
- `ID`：指定识别的指纹 ID 范围，0xFFFF 表示识别所有已录入的指纹，其他值只与指定 ID 对比。
- `flags`：识别选项，可按位组合使用，具体定义见下方 `fingerprint_auto_verify_flags_t`。
- `matchedID`：输出参数，返回匹配成功的指纹 ID。
- `callback`：回调函数（可选），回调函数会在**每个阶段完成后被多次调用**，可用于实时反馈识别进度。

**返回值：**

- `FINGERPRINT_OK`：识别成功
- 其他值表示失败，具体定义请见库文件 `fingerprint_status_t`。

#### PS_AutoIdentify_callback

```cpp
bool PS_AutoIdentify_callback(
    uint8_t securityLevel,                 
    fingerprint_status_t confirmationCode, 
    uint8_t param,                         
    uint16_t matchedID,                 
    uint16_t matchScore,                 
    int packetCount                    
);
```

**传入参数：**

- `securityLevel`：与 `PS_AutoIdentify` 中传入的参数相同。
- `confirmationCode`：当前阶段的状态码，`FINGERPRINT_OK` 表示成功，具体定义请见库文件 `fingerprint_status_t`。
- `param`：当前阶段码，具体定义请见下方 `ps_auto_identify_param_t`。
- `matchedID`：输出参数，返回匹配成功的指纹 ID。
- `matchScore`：输出参数，返回匹配分数，数值越大表示匹配度越高。
- `packetCount`：当前回调函数调用次数（当前已处理的数据包数量），从 0 开始计数。

**相关定义：**

- `fingerprint_auto_verify_flags_t`

```cpp
typedef enum {
    FINGERPRINT_AUTO_VERIFY_DEFAULT          = 0x0000, // 默认设置 / Default setting
    FINGERPRINT_AUTO_VERIFY_NO_STATUS_RETURN = (1 << 2), // 验证过程中不返回当前状态 / Don't return current status during verification
} fingerprint_auto_verify_flags_t;
```

- `ps_auto_identify_param_t`

```cpp
typedef enum {
    PS_AUTO_IDENTIFY_PARAM_LEGAL_CHECK   = 0x00, // 指纹合法性检测 / Fingerprint legality check
    PS_AUTO_IDENTIFY_PARAM_GET_IMAGE     = 0x01, // 获取图像 / Get image
    PS_AUTO_IDENTIFY_PARAM_VERIFY        = 0x05, // 已注册指纹比对 / Registered fingerprint matching
} ps_auto_identify_param_t;
```

下方例程中使用回调函数获取当前识别状态并反馈相关信息。

```cpp line-num
#include <Arduino.h>
#include <M5UnitFingerprint2.hpp>
#include <M5Unified.hpp>

M5Canvas canvas(&M5.Lcd);
M5UnitFingerprint2 fp2(&Serial1, 17, 18);  // Initialize fingerprint sensor

void setup() {
    Serial.begin(115200);
    M5.begin();
    fp2.begin();
    canvas.createSprite(320, 240);
    canvas.fillScreen(TFT_BLACK);
    canvas.setTextColor(TFT_WHITE);
    canvas.setFont(&fonts::FreeMonoBold9pt7b);
    canvas.drawString("Unit Fingerprint2 Identify", 2, 0);
    Serial.println("<-------Unit Fingerprint2 Identify------->");
    canvas.drawLine(0, 20, 320, 20, TFT_WHITE);

    if (fp2.PS_ActivateFingerprintModule() == FINGERPRINT_OK) {
        canvas.drawString("Fingerprint2 Ready", 2, 45);
        Serial.printf("Fingerprint2 Ready\n");
    } else {
        canvas.drawString("Fingerprint2 Init Failed", 2, 45);
        Serial.printf("Fingerprint2 Init Failed\n");
    }

    fp2.PS_SetWorkMode(1);
    canvas.pushSprite(0, 0);
}

void loop() {
    M5.update();

    canvas.fillRect(0, 70, 320, 170, TFT_BLACK);
    canvas.setCursor(2, 70);
    canvas.drawString("Place finger to identify...", 10, 90);
    canvas.pushSprite(0, 0);
    Serial.println("Start identifying fingerprint. Please place your finger...");

    uint16_t matchedID = 0;
    // Start automatic identification:
    // Parameters: security level(0 or 1), ID, flags, output matchedID, callback
    fingerprint_status_t result = fp2.PS_AutoIdentify(
        0, 0xFFFF, FINGERPRINT_AUTO_VERIFY_DEFAULT,
        matchedID, PS_AutoIdentify_callback);

    canvas.fillRect(0, 90, 320, 150, TFT_BLACK);
    if (result == FINGERPRINT_OK) {
        canvas.setCursor(2, 100);
        canvas.printf("Identify Success! ID:%d", matchedID);
        Serial.printf("Fingerprint identified! ID=%d\n", matchedID);
        delay(1000);
    } else {
        canvas.drawString("Identify Failed!", 2, 100);
        Serial.println("Fingerprint identification failed!");
    }
    canvas.pushSprite(0, 0);
    delay(20);
}

// Callback function for PS_AutoIdentify: updates status during each identification stage
bool PS_AutoIdentify_callback(uint8_t securityLevel, fingerprint_status_t confirmationCode, uint8_t param, uint16_t matchedID, uint16_t matchScore, int packetCount) {
    switch (param) {
        // Stage 1: Capture fingerprint image
        case PS_AUTO_IDENTIFY_PARAM_GET_IMAGE:
        if (confirmationCode == FINGERPRINT_OK) {
            canvas.setCursor(10, 90);
            canvas.fillRect(0, 90, 320, 150, TFT_BLACK);
            canvas.printf("Image acquired success");
            Serial.println("Image acquired success");
        }
        break;
        // Stage 2: Matching fingerprint
        case PS_AUTO_IDENTIFY_PARAM_VERIFY:
        if (confirmationCode == FINGERPRINT_OK) {
            canvas.setCursor(10, 110);
            canvas.printf("Match ID:%d Score:%d", matchedID, matchScore);
            Serial.printf("Match ID:%d Score:%d\n", matchedID, matchScore);
        } else {
            canvas.setCursor(10, 110);
            canvas.printf("No Fingerprint Matched");
            Serial.println("No Fingerprint Matched");
        }
        break;
        default:
        break;
    }
    canvas.pushSprite(0, 0);
    delay(500);
    return (confirmationCode == FINGERPRINT_OK);
} 
```

### 3.5 删除某已录入指纹

本指纹模组仅支持通过 ID 号删除指定指纹模板，故需要先识别获取 ID 号后再删除，若想清空所有指纹模板，请使用 `PS_Empty` 函数。

```cpp line-num
#include <Arduino.h>
#include <M5UnitFingerprint2.hpp>
#include <M5Unified.hpp>

M5Canvas canvas(&M5.Lcd);
M5UnitFingerprint2 fp2(&Serial1, 17, 18);  // Initialize fingerprint sensor

void setup() {
    Serial.begin(115200);
    M5.begin();
    fp2.begin();
    canvas.createSprite(320, 240);
    canvas.fillScreen(TFT_BLACK);
    canvas.setTextColor(TFT_WHITE);
    canvas.setFont(&fonts::FreeMonoBold9pt7b);
    canvas.drawString("Unit Fingerprint2 Delete", 2, 0);
    Serial.println("<-------Unit Fingerprint2 Delete------->");
    canvas.drawLine(0, 20, 320, 20, TFT_WHITE);

    if (fp2.PS_ActivateFingerprintModule() == FINGERPRINT_OK) {
        canvas.drawString("Fingerprint2 Ready", 2, 45);
        Serial.printf("Fingerprint2 Ready\n");
    } else {
        canvas.drawString("Fingerprint2 Init Failed", 2, 45);
        Serial.printf("Fingerprint2 Init Failed\n");
    }

    fp2.PS_SetWorkMode(1);
    fp2.PS_ControlBLN(FINGERPRINT_LED_BREATHING, FINGERPRINT_LED_COLOR_BLUE, FINGERPRINT_LED_COLOR_PURPLE, 0); /// 0-endless loop, N-loop N times
    canvas.pushSprite(0, 0);
}

void loop() {
    M5.update();

    canvas.fillRect(0, 70, 320, 170, TFT_BLACK);
    canvas.setCursor(2, 70);
    canvas.drawString("Place finger to delete...", 10, 90);
    canvas.pushSprite(0, 0);
    Serial.println("Please place your finger...");

    uint16_t matchedID = 0;
    // Start automatic identification:
    // Parameters: security level(0 or 1), ID, flags, output matchedID
    fingerprint_status_t result = fp2.PS_AutoIdentify(
        0, 0xFFFF, FINGERPRINT_AUTO_VERIFY_DEFAULT,
        matchedID);

    canvas.fillRect(0, 90, 320, 150, TFT_BLACK);
    if (result == FINGERPRINT_OK) {
        canvas.setCursor(2, 100);
        canvas.printf("Identified ID:%d", matchedID);
        Serial.printf("Identified ID:%d", matchedID);
        // Delete the matched fingerprint
        fingerprint_status_t delResult = fp2.PS_DeletChar(matchedID, 1);
        if (delResult == FINGERPRINT_OK) {
            canvas.setCursor(2, 120);
            canvas.printf("Deleted ID:%d Success!", matchedID);
            Serial.printf("Deleted fingerprint ID=%d Success!\n", matchedID);
        } else {
            canvas.setCursor(2, 120);
            canvas.printf("Delete ID:%d Failed!", matchedID);
            Serial.printf("Delete fingerprint ID=%d Failed!\n", matchedID);
        }
    } else {
        canvas.drawString("Identify Failed!", 2, 100);
        Serial.println("Fingerprint identification failed!");
    }
    canvas.pushSprite(0, 0);
    delay(2000);
} 
```

## 4. 编译上传

- 下载模式：不同设备进行程序烧录前需要进入下载模式，不同的主控设备该步骤可能有所不同。详情可参考[Arduino IDE上手教程](/zh_CN/arduino/arduino_ide)页面底部的设备程序下载教程列表，查看具体的操作方式。

- CoreS3 长按复位按键 (大约 2 秒) 直到内部绿色 LED 灯亮起，便可松开，此时设备已进入下载模式，等待烧录。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/M5CORES3%20SE/cores3%20(2).gif" width="30%">

- 选中设备端口，点击 Arduino IDE 左上角编译上传按钮，等待程序完成编译并上传至设备。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/Unit_Fingerprint2_Example.png" width="70%">

## 5. 例程效果展示

- 灯光设置：灯光效果为绿蓝色呼吸灯、红色闪烁灯、青色渐亮灯、黄色渐灭灯、紫色常亮灯，循环切换。

<video style="width:40vw;max-width:30%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/Unit_Fingerprint2_LED.mp4" type="video/mp4"></video>

- 指纹图像获取显示：将手指放在指纹传感器上，等待 3 次采集成功后会显示指纹图像。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/Unit_Fingerprint2_Image1.jpg" width="30%"> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/Unit_Fingerprint2_Image2.jpg" width="30%"> <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/Unit_Fingerprint2_Image3.jpg" width="30%">

- 指纹录入：点击屏幕，按照提示将手指放在指纹传感器上进行录入，录入成功后灯光变为绿色，屏幕显示 `Enroll Success` 等字样。

<video style="width:40vw;max-width:30%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/Unit_Fingerprint2_Enroll.mp4" type="video/mp4"></video>

- 指纹识别：按照提示将手指放在指纹传感器上进行识别，识别成功后灯光变为绿色，屏幕显示 `Identify Success` 等字样。

<video style="width:40vw;max-width:30%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/Unit_Fingerprint2_Indetify.mp4" type="video/mp4"></video>

- 删除某已录入指纹：按照提示将手指放在指纹传感器上进行删除，屏幕显示 `Deleted ID:X Success` 等字样。

<video style="width:40vw;max-width:30%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1186/Unit_Fingerprint2_Delete.mp4" type="video/mp4"></video>
