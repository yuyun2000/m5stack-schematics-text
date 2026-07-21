# Unit Heart Arduino 使用教程

## 1. 准备工作

- 环境配置： 参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide)完成 IDE 安装，并根据实际使用的开发板安装对应的板管理，与需要的驱动库。

- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
  - [MAX30100lib](https://github.com/oxullo/Arduino-MAX30100)

- 使用到的硬件产品：
  - [StickS3](https://shop.m5stack.com/products/m5stickc-plus-esp32-pico-mini-iot-development-kit)
  - [Unit Heart](https://shop.m5stack.com/products/mini-heart-unit)

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/K150-stickS3_main-products_02.webp" width="20%"/> <img src="https://static-cdn.m5stack.com/resource/docs/products/unit/heart/heart_cover_01.webp" width="20%"/>

## 2. 注意事项

\#> 引脚兼容性 | 由于每款主机的引脚配置不同，使用前请参考产品文档中的[引脚兼容表](/zh_CN/unit/heart)，并根据实际引脚连接情况修改案例程序。

<ProductCompatible sku="U029" type="UNIT"></ProductCompatible> 

## 3. 案例程序

- 本教程中使用的主控设备为 StickS3，搭配 Unit Heart 模块。本心率模块采用 I2C 方式通讯，根据实际的电路连接修改程序中的引脚定义，设备堆叠后对应的 I2C IO 为 `G9 (SCL)`，`G10 (SDA)`。

```cpp line-num
#include "M5Unified.h"
#include "MAX30100.h"

#define SAMPLING_RATE   MAX30100_SAMPRATE_100HZ
#define IR_LED_CURRENT  MAX30100_LED_CURR_24MA
#define RED_LED_CURRENT MAX30100_LED_CURR_27_1MA
#define PULSE_WIDTH     MAX30100_SPC_PW_1600US_16BITS
#define HIGHRES_MODE    true

MAX30100 sensor;  // Instantiate a MAX30100 sensor class

void setup()
{
    M5.begin();        
    M5.Power.begin();  // Init power
    Serial.print("Initializing MAX30100..");

    while (!sensor.begin()) {  // Initialize the sensor
        M5.Lcd.setCursor(50, 100);
        M5.Lcd.println("Sensor not found");
        delay(1000);
    }
    M5.Lcd.setRotation(3);
    M5.Lcd.fillScreen(BLACK);
    M5.Lcd.setFont(&fonts::FreeMonoBold12pt7b);
    M5.Lcd.setTextSize(1.5);
    // Set up the wanted parameters
    sensor.setMode(MAX30100_MODE_SPO2_HR);
    sensor.setLedsCurrent(IR_LED_CURRENT, RED_LED_CURRENT);
    sensor.setLedsPulseWidth(PULSE_WIDTH);
    sensor.setSamplingRate(SAMPLING_RATE);
    sensor.setHighresModeEnabled(HIGHRES_MODE);
}

void loop()
{
    uint16_t ir, red;
    sensor.update();                       // Update sensor data
    if (sensor.getRawValues(&ir, &red)) {  // if get data
        M5.Lcd.setCursor(5, 20);
        M5.Lcd.printf("IR: %d", ir);
        M5.Lcd.setCursor(5, 70);
        M5.Lcd.printf("RED: %d", red);
    }
    delay(100); // Appropriate delay
    M5.Lcd.fillScreen(BLACK);
}
```

## 4. 心率原始数据检测

- 设备上电后，屏幕上会显示从 MAX30100 传感器获取的原始红外和红光数据。将手指放在心率模块的传感器区域，观察屏幕上显示的数值变化，数值会根据血液流动的变化而波动。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/716/Unit_Heart_Arduino_1.jpg" width="40%">
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/716/Unit_Heart_Arduino_2.jpg" width="40%">