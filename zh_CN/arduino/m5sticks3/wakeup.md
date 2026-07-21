# StickS3 Wakeup 休眠唤醒

StickS3 休眠唤醒相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5StickS3
- M5Unified 库版本 >= 0.2.12
- M5GFX 库版本 >= 0.2.18

```cpp line-num
#include "M5Unified.h"

void setup(void) {
  M5.begin();

  M5.Display.setTextDatum(middle_center);
  M5.Display.setTextFont(&fonts::FreeMonoBoldOblique9pt7b);
  M5.Display.setRotation(1);

  M5.Display.drawString("BtnA to Sleep 5s", M5.Display.width() / 2, M5.Display.height() / 2);
}

void loop(void) {
  M5.update();

  if (M5.BtnA.wasPressed()) {
    M5.Display.clear();
    M5.Power.timerSleep(5);//sec
  }
}
```

例程效果如下：

<video style="width:40vw;max-width:40%;height:auto;" controls>
  <source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_wakeup.mp4" type="video/mp4"></video>

## API

StickS3 电源部分使用了 `M5Unified` 库中的 `Power_Class` , 更多相关的 API 可以参考下方文档：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)

## M5PM1 Timer 定时器唤醒

StickS3 可使用 [M5PM1 Arduino Library](https://github.com/m5stack/M5PM1) 驱动库，通过 M5PM1 实现设备的定时唤醒，该模式下可关断 ESP32-S3 等外设的供电，功耗更低。

更多 StickS3 M5PM1 使用教程可参考 [StickS3 M5PM1 低功耗配置](/zh_CN/arduino/m5sticks3/m5pm1)。

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5StickS3
- M5Unified 库版本 >= 0.2.12
- M5GFX 库版本 >= 0.2.18
- M5PM1 库版本 >= 1.0.1

案例说明：设备开机后，单击按键 A 配置 10s 定时器触发唤醒。

```cpp line-num
#include <M5Unified.h>
#include <M5PM1.h>
#include <Wire.h>

M5PM1 pm1;

void setup(void)
{
    M5.begin();
    M5.Display.setRotation(1);
    Serial.begin(115200);
    auto pin_num_sda = M5.getPin(m5::pin_name_t::in_i2c_sda);
    auto pin_num_scl = M5.getPin(m5::pin_name_t::in_i2c_scl);
    M5_LOGI("getPin: SDA:%u SCL:%u", pin_num_sda, pin_num_scl);
    Wire.end();
    Wire.begin(pin_num_sda, pin_num_scl, 100000U);

    // Initialize PM1
    m5pm1_err_t err = pm1.begin(&Wire, M5PM1_DEFAULT_ADDR, pin_num_sda, pin_num_scl, M5PM1_I2C_FREQ_100K);

    if (err == M5PM1_OK) {
        Serial.println("PM1 initialization successful");
    } else {
        Serial.printf("PM1 initialization failed, error code: %d\n", err);
    }
    M5.Display.fillScreen(BLACK);
    M5.Display.setTextSize(2);
    M5.Display.setTextColor(WHITE);
    M5.Display.setCursor(0, 10);
    M5.Display.println("Timer Power Test");
    M5.Display.println("BtnA: After 10s Wakeup");
}

void loop(void)
{
    M5.update();
    if (M5.BtnA.wasPressed()) {
        M5.Display.fillScreen(BLACK);
        M5.Display.setCursor(0, 10);
        M5.Display.println("Shutdown");
        M5.Display.println("After 10s");
        M5.Display.println("Wakeup");
        delay(1000);
        pm1.timerSet(10, M5PM1_TIM_ACTION_POWERON);
        pm1.shutdown();
    }
}
```
