# Paper SHT30 温湿度传感器

Paper SHT30 温湿度传感器相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 2.1.4
- 开发板选项 = M5Paper
- M5Unified 库版本 >= 0.2.5
- M5GFX 库版本 >= 0.2.7
- M5Unit-ENV 库版本 >= 1.2.1

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>
#include <M5UnitENV.h>
// #include <M5UnitUnifiedENV.h>

float temp, humi;
SHT3X sht3x;

void setup() {
  M5.begin();
  M5.Display.setRotation(0);
  M5.Display.setFont(&fonts::FreeMonoBold24pt7b);
  M5.Display.setEpdMode(epd_fast);  // epd_quality, epd_text, epd_fast, epd_fastest

  Serial.begin(115200);
  Serial.println("SHT30 Sensor");

  M5.Display.clear();
  M5.Display.setCursor(80, 100);
  M5.Display.print("SHT30 Sensor");

  if (!sht3x.begin(&Wire, SHT3X_I2C_ADDR, 21, 22, 400000U)) {
    Serial.println("SHT30 not found");
    M5.Display.setCursor(60, 300);
    M5.Display.print("SHT30 not found");
    while (1) delay(1);
  }
}

void loop() {
  M5.update();
  sht3x.update();

  temp = sht3x.cTemp;
  humi = sht3x.humidity;

  Serial.printf("Temp:%6.2f C", temp);
  Serial.println();
  Serial.printf("Humi:%6.2f %%", humi);
  Serial.println("\n");

  M5.Display.setCursor(60, 300);
  M5.Display.printf("Temp:%6.2f C", temp);
  M5.Display.setCursor(60, 360);
  M5.Display.printf("Humi:%6.2f %%", humi);

  delay(800);

  // refresh the whole display every 60 seconds
  int refreshTimer = millis() % 60000;
  if (refreshTimer >= 58200 && refreshTimer < 60000) {
    M5.Display.clear();
    M5.Display.setCursor(80, 100);
    M5.Display.print("SHT30 Sensor");
    Serial.println("\nscreen refreshed\n");
  }
}
```

该程序将会在屏幕上显示传感器实时检测的温度（摄氏度 ℃）和相对湿度（%）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/689/Paper_Arduino_SHT30.jpeg" width="50%">

## API

Paper SHT30 温湿度传感器部分使用了 `M5Unit-ENV` 库中的 `SHT3X` 类，更多相关的API可以参考 GitHub 中的库文件：

- [M5Unit-ENV - SHT3X](https://github.com/m5stack/M5Unit-ENV/blob/master/src/SHT3X.cpp)