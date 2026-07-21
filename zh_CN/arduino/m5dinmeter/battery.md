# DinMeter 获取电池电量相关数据

DinMeter 电池电量相关API与案例程序。


## 案例程序


```cpp line-num
#include <M5Unified.h>

static constexpr int BAT_PIN         = G10;      // DinMeter 电池检测引脚
static constexpr float VREF         = 3.3f;     // ADC 参考电压
static constexpr int ADC_RESOLUTION = 4095;     // 12 位分辨率 (0～4095)
static constexpr float DIVIDER      = 2.0f;     // 分压系数

void setup() {
  // 初始化 M5Unified（包含 Display、按键、RTC、电源管理等）
  auto cfg = M5.config();
  M5.begin(cfg);

  // 配置电池引脚的 ADC 衰减，以获得满量程读取
  analogSetPinAttenuation(BAT_PIN, ADC_11db);

  // Display 初始化
  M5.Display.fillScreen(TFT_BLACK);
  M5.Display.setTextColor(TFT_WHITE, TFT_BLACK);
  M5.Display.setTextSize(2);
}

void loop() {
  // 读取原始 ADC 值
  int raw = analogRead(BAT_PIN);
  // 计算实际电压： (raw/4095) * 3.3V * 2
  float vb = (raw / float(ADC_RESOLUTION)) * VREF * DIVIDER;

  // 显示电压
  M5.Display.fillScreen(TFT_BLACK);
  M5.Display.setCursor(10, 20);
  M5.Display.printf("Battery:\n%.2f V", vb);

  // 每 5 秒更新一次
  delay(5000);
  M5.update();
}

```

上传完成就可以看到下面的效果了

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/K134_battery.jpg" width="30%">

