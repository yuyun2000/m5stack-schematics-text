# Air Quality 获取电池电量相关数据

Air Quality 电池电量相关API与案例程序。


## 案例程序


```cpp line-num
#include <M5Unified.h>

static constexpr int BAT_PIN        = 14;     
static constexpr float VREF        = 3.3f;   // ADC 参考电压
static constexpr int ADC_RESOLUTION = 4095;  // 12 位分辨率 (0～4095)
static constexpr float DIVIDER      = 2.0f;   // 分压系数

void setup() {
  // 初始化 M5Unified
  M5.begin();
  analogSetPinAttenuation(BAT_PIN, ADC_11db);

 
  M5.Display.clear(TFT_BLACK);
  M5.Display.setTextColor(TFT_WHITE, TFT_BLACK);
  M5.Display.setTextSize(3);
}

void loop() {
  // 读一次 ADC
  int raw = analogRead(BAT_PIN);
  // 计算电压：raw/4095*3.3 * 2
  float vb = (raw / float(ADC_RESOLUTION)) * VREF * DIVIDER;

  // 把结果显示到屏幕
  M5.Display.fillScreen(TFT_BLACK);
  M5.Display.setCursor( 10,  20);
  M5.Display.printf("Battery:\n%.2f V", vb);

  // 每秒更新一次
  delay(5000);
  M5.update();
}
```

上传完成就可以看到下面的效果了

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/m5air_quality_arduino_quickstart_battery.jpg" width="30%">

