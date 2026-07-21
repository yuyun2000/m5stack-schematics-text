# Hat Heart Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [SparkFun_MAX3010x_Sensor](https://github.com/adafruit/Adafruit_MLX90640)

- 使用到的硬件产品：
  - [StickS3](https://shop.m5stack.com/products/m5stickc-plus-esp32-pico-mini-iot-development-kit)
  - [Hat Heart](https://shop.m5stack.com/products/m5stickc-heart-rate-hat-max30102)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_02.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/hat/hat_heart_rate/hat_heart_rate_cover_01.webp" width="20%"/>

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/hat/hat_heart_rate)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U118" type="HAT"></ProductCompatible> 

## 3. 案例程序

- 本教程中使用的主控设备为 StickS3，搭配 Hat Heart 模块。本热成像模块采用 I2C 方式通讯，根据实际的电路连接修改程序中的引脚定义，设备堆叠后对应的 I2C IO 为 `G0 (SCL)`，`G8 (SDA)`。

?> 注意事项 | 1\. 手指放上传感器后，请保持手指稳定并等待几十秒，以获得正确的 SpO2 和 BPM（心率）数值。  
2\. 若使用 StickS3 作为主控设备，由于硬件限制，按下复位按键后不能复位心率模块，需断电重启设备以重新初始化心率模块，否则主控设备会显示初始化失败的提示信息。

```cpp line-num
#include <M5Unified.h>    
#include <Wire.h>      
#include "MAX30105.h"   
#include "heartRate.h"    // Heart rate detection algorithm
#include "spo2_algorithm.h" // SpO2 calculation algorithm

M5Canvas canvas = M5Canvas(&M5.Lcd);

MAX30105 Sensor;

#define Heart_SDA 8
#define Heart_SCL 0

// Length of sample buffer for SpO2 calculation
#define bufferLength   100

// Button A pin definition
const byte Button_A = 11;

// Buffers to store infrared (IR) and red light sensor data
uint32_t irBuffer[bufferLength];
uint32_t redBuffer[bufferLength];

// Button state and reset flag
int8_t ButtonState, flag_Reset;

// SpO2 and heart rate calculation results
int32_t spo2, heartRate, old_spo2;
int8_t validSPO2, validHeartRate;

// Heart rate averaging parameters
const byte RATE_SIZE = 5;     // Number of beats used for averaging
uint16_t rate_begin  = 0;     // Counter for initial averaging
uint16_t rates[RATE_SIZE];   // Circular buffer for BPM values
byte rateSpot = 0;            // Index for BPM buffer
float beatsPerMinute;         // Instantaneous BPM
int beatAvg;                  // Averaged BPM

// Failure counter (e.g., finger removed)
byte num_fail;

// Display waveform buffers (red & IR), width 320 samples
uint16_t line[2][320] = {0};

// Current write positions for waveform buffers
uint32_t red_pos = 0, ir_pos = 0;

// Max/min values for waveform scaling
uint16_t ir_max = 0, red_max = 0, ir_min = 0, red_min = 0;
uint16_t ir_last = 0, red_last = 0;

// Raw filtered values from last sample
uint16_t ir_last_raw = 0, red_last_raw = 0;

// Display-mapped waveform values
uint16_t ir_disdata, red_disdata;

// Low-pass filter coefficient (scaled by 256)
uint16_t Alpha = 0.3 * 256;

// Timing variables for beat detection
uint32_t t1, t2, last_beat, Program_freq;

/**
 * @brief Interrupt callback for Button A
 *        Sets reset flag when button is pressed
 */
void callBack(void) {
    ButtonState = digitalRead(Button_A); // Read button state
    if (ButtonState == 0) flag_Reset = 1; // Set reset flag if button pressed
    delay(10);                         // Simple debounce delay
}

void setup() {
    M5.begin();
    Serial.begin(115200);
    pinMode(Button_A, INPUT);
    Wire.begin(Heart_SDA, Heart_SCL);

    M5.Lcd.setRotation(3);
    M5.Lcd.setSwapBytes(false);
    canvas.createSprite(240, 135);
    canvas.setSwapBytes(true);
    canvas.createSprite(240, 135);

    // Initialize MAX30102/MAX30105 sensor
    if (!Sensor.begin(Wire, I2C_SPEED_FAST)) {
        M5.Lcd.print("Init Failed");
        Serial.println(F("MAX30102 was not found. Please check wiring/power."));
        while (1); // Halt program
    }

    // Prompt user to place finger on sensor
    Serial.println("Place your index finger on the Sensor with steady pressure");

    // Attach interrupt to Button A (falling edge)
    attachInterrupt(Button_A, callBack, FALLING);

    // Configure MAX30102 sensor with default settings
    Sensor.setup();
    Sensor.clearFIFO(); // Optional FIFO clear (commented out)
}

void loop() {
    uint16_t ir, red;

    // If reset flag is set, clear sensor FIFO
    if (flag_Reset) {
        Sensor.clearFIFO();
        delay(5);
        flag_Reset = 0;
    }

    // Main acquisition loop (runs until reset)
    while (flag_Reset == 0) {
        // Wait until sensor data is available
        while (Sensor.available() == false) {
            delay(10);
            Sensor.check();
        }

        // Continuous data reading loop
        while (1) {
            red = Sensor.getRed(); // Read red light value
            ir  = Sensor.getIR();  // Read infrared value

            // Check if finger is properly placed
            if ((ir > 1000) && (red > 1000)) {
                num_fail = 0;       // Reset failure counter
                t1 = millis();      // Timestamp before processing

                // Store samples into circular buffers
                redBuffer[(red_pos + 100) % 100] = red;
                irBuffer[(ir_pos + 100) % 100]   = ir;

                // Measure processing frequency
                t2 = millis();
                Program_freq++;

                // Heartbeat detection using IR signal
                if (checkForBeat(ir) == true) {
                    long delta =
                        millis() - last_beat - (t2 - t1) * (Program_freq - 1);
                    last_beat = millis();
                    Program_freq = 0;

                    // Calculate BPM
                    beatsPerMinute = 60 / (delta / 1000.0);

                    if (beatsPerMinute > 40 && beatsPerMinute < 180) {

                        if (rate_begin == 0) {
                            beatAvg = (int)beatsPerMinute;
                        }

                        rates[rateSpot++] = (uint16_t)beatsPerMinute;
                        rateSpot %= RATE_SIZE;

                        if (rate_begin < RATE_SIZE) rate_begin++;

                        int sum = 0;
                        for (byte i = 0; i < rate_begin; i++) {
                            sum += rates[i];
                        }
                        beatAvg = sum / rate_begin;
                    }
                }
            } else {
                num_fail++; // Increase failure count if finger not detected
            }

            // Apply low-pass filtering to waveform data
            line[0][(red_pos + 240) % 320] =
                (red_last_raw * (256 - Alpha) + red * Alpha) / 256;
            line[1][(ir_pos + 240) % 320] =
                (ir_last_raw * (256 - Alpha) + ir * Alpha) / 256;

            red_last_raw = line[0][(red_pos + 240) % 320];
            ir_last_raw  = line[1][(ir_pos + 240) % 320];

            // Advance waveform positions
            red_pos++;
            ir_pos++;

            // Exit loop if no more data or reset requested
            if ((Sensor.check() == false) || flag_Reset) break;
        }

        // Clear FIFO after processing batch
        Sensor.clearFIFO();

        // Find max and min values for waveform scaling
        for (int i = 0; i < 240; i++) {
            if (i == 0) {
                red_max = red_min = line[0][(red_pos + i) % 320];
                ir_max = ir_min = line[1][(ir_pos + i) % 320];
            } else {
                red_max = (line[0][(red_pos + i) % 320] > red_max)
                              ? line[0][(red_pos + i) % 320]
                              : red_max;
                red_min = (line[0][(red_pos + i) % 320] < red_min)
                              ? line[0][(red_pos + i) % 320]
                              : red_min;
                ir_max = (line[1][(ir_pos + i) % 320] > ir_max)
                             ? line[1][(ir_pos + i) % 320]
                             : ir_max;
                ir_min = (line[1][(ir_pos + i) % 320] < ir_min)
                             ? line[1][(ir_pos + i) % 320]
                             : ir_min;
            }
            if (flag_Reset) break;
        }

        // Clear display canvas
        canvas.fillRect(0, 0, 240, 135, BLACK);

        // Draw waveform lines
        for (int i = 0; i < 240; i++) {
            red_disdata =
                map(line[0][(red_pos + i) % 320], red_max, red_min, 0, 135);
            ir_disdata =
                map(line[1][(ir_pos + i) % 320], ir_max, ir_min, 0, 135);

            canvas.drawLine(i, red_last, i + 1, red_disdata, RED);
            canvas.drawLine(i, ir_last, i + 1, ir_disdata, BLUE);

            ir_last  = ir_disdata;
            red_last = red_disdata;

            if (flag_Reset) break;
        }

        // Save previous SpO2 value
        old_spo2 = spo2;

        // Calculate heart rate and SpO2 when enough samples are collected
        if (red_pos > 100)
            maxim_heart_rate_and_oxygen_saturation(
                irBuffer, bufferLength, redBuffer,
                &spo2, &validSPO2,
                &heartRate, &validHeartRate);

        // Keep old SpO2 if new value is invalid
        if (!validSPO2) spo2 = old_spo2;

        // Display text information
        canvas.setTextSize(1);

        canvas.setTextColor(RED);
        canvas.setCursor(5, 5);
        canvas.printf("red:%d,%d,%d", red_max, red_min, red_max - red_min);
        Serial.printf("red:%d,%d,%d, ", red_max, red_min, red_max - red_min);

        canvas.setTextColor(BLUE);
        canvas.setCursor(5, 15);
        canvas.printf("ir:%d,%d,%d", ir_max, ir_min, ir_max - ir_min);
        Serial.printf("ir:%d,%d,%d ", ir_max, ir_min, ir_max - ir_min);

        canvas.setCursor(5, 25);
        if (num_fail < 10) {
            canvas.setTextColor(GREEN);
            canvas.printf("spo2:%d,", spo2);
            canvas.setCursor(60, 25);
            canvas.printf(" BPM:%d", beatAvg);
            Serial.printf(" spo2:%d, BPM:%d\n", spo2, beatAvg);
        } else {
            canvas.setTextColor(RED);
            canvas.printf("No Finger!!");
            Serial.printf("No Finger!!\n");
        }

        // Push canvas to LCD
        canvas.pushSprite(0, 0);
    }
}
```

## 4. 心率检测

- 设备上电后，屏幕上会显示从 MAX30102 传感器获取的原始红外和红光数据。将手指放在心率模块的传感器区域，可观察到屏幕上 SpO2 和 BPM（心率）数值及曲线的变化，请根据实际情况调整手指位置和压力，以获得稳定的读数。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/852/Hat_Heart_Arduino.jpg" width="40%">
