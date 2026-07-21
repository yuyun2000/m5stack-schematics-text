# PowerHub Wakeup 休眠唤醒

PowerHub Wakeup 休眠唤醒相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.3
- 开发板选项 = M5PowerHub
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include <M5Unified.h>

int myIndex = 0;

void setup() {
  M5.begin();
  M5.Led.setBrightness(255);

  Serial.begin(115200);
  Serial.println("\n\nPowerHub Sleep & Wakeup Test");
  delay(1000);
}

void loop() {
  myIndex++;
  Serial.printf("%d ", myIndex);
  M5.Led.setAllColor(TFT_WHITE);
  M5.Led.display();
  delay(200);

  if (myIndex % 20 == 0) {
    M5.Led.setAllColor(TFT_BLACK);
    M5.Led.display();

    M5.Power.timerSleep(5);  // in seconds
    // M5.Power.deepSleep(5000000, false);  // in microseconds
    // M5.Power.lightSleep(5000000, false);  // in microseconds
  }

  if (myIndex >= 1000) {
    myIndex = 0;
  }
}
```

该程序将会点亮 LED 灯并在串口打印一个从 0 开始自增 1 的计数器，每次增长到 20 的倍数时让设备进入计时休眠 5 秒（LED 灯熄灭）然后唤醒，程序重新开始（LED 灯点亮）。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1183/Arduino_wakeup.png" width="90%">

## API

PowerHub Wakeup 休眠唤醒部分驱动使用了`M5Unified`库中的`Power_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Power Class](/zh_CN/arduino/m5unified/power_class)

?>注意|由于 PowerHub 的电源、LED 灯由协处理器 STM32 控制，所以主控 ESP32-S3 进入休眠时不会自动改变电源和 LED 灯的状态。如果需要通过休眠模式省电，请在进入休眠前关闭电源及 LED 灯，可参考 [Power](/zh_CN/arduino/powerhub/power) 及 [RGB LED](/zh_CN/arduino/powerhub/rgb) 页面。