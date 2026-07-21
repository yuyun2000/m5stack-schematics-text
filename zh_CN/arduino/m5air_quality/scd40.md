# Air Quality 获取SCD40传感器相关数据

Air Quality SCD40传感器相关API与案例程序。

## 案例程序


```cpp line-num
#include <M5Unified.h>
#include <Wire.h>
#include <SensirionI2CScd4x.h>

SensirionI2CScd4x scd4x;

void setup() {
  Serial.begin(115200);

  // 初始化屏幕
  M5.begin();
  M5.Display.clear(TFT_BLACK);
  M5.Display.setTextSize(1);
  M5.Display.setTextColor(TFT_WHITE, TFT_BLACK);

  // 初始化 I2C 总线（SDA=11, SCL=12）
  Wire.begin(11, 12);
  scd4x.begin(Wire);


  uint16_t err;
  char errMsg[128];
  err = scd4x.stopPeriodicMeasurement();
  if (err) {
    Serial.print("stopPeriodicMeasurement 错: ");
    errorToString(err, errMsg, sizeof(errMsg));
    Serial.println(errMsg);
  }

  // 启动周期测量（默认间隔 2s）
  err = scd4x.startPeriodicMeasurement();
  if (err) {
    Serial.print("startPeriodicMeasurement 错: ");
    errorToString(err, errMsg, sizeof(errMsg));
    Serial.println(errMsg);
  }

  // 等待第一次数据稳定
  delay(5000);
}

void loop() {
  // 每两秒刷新一次
  delay(2000);

  uint16_t err;
  bool ready = false;
  char errMsg[128];

  // 先检查数据准备好了没有
  err = scd4x.getDataReadyFlag(ready);
  if (err) {
    Serial.print("getDataReadyFlag 错: ");
    errorToString(err, errMsg, sizeof(errMsg));
    Serial.println(errMsg);
    return;
  }
  if (!ready) {
    // 还没准备好就跳过
    return;
  }

  // 读取 CO2 / 温度 / 湿度
  uint16_t co2;
  float temp, hum;
  err = scd4x.readMeasurement(co2, temp, hum);
  if (err) {
    Serial.print("readMeasurement 错: ");
    errorToString(err, errMsg, sizeof(errMsg));
    Serial.println(errMsg);
  }

  // 把结果打印到串口
  if (!err && co2) {
    Serial.printf("CO2=%uppm  Temp=%.1f°C  Hum=%.1f%%\n", co2, temp, hum);
  }

  // 把结果显示到 AirQ 屏幕上
  M5.Display.fillScreen(TFT_BLACK);
  M5.Display.setCursor(10,  10);
  if (err || co2 == 0) {
    M5.Display.setTextColor(TFT_RED, TFT_BLACK);
    M5.Display.println("读取失败");
  } else {
    M5.Display.setTextColor(TFT_WHITE, TFT_BLACK);
    M5.Display.printf("CO2   : %4uppm\n", co2);
    M5.Display.printf("Temp  : %5.1f°C\n", temp);
    M5.Display.printf("Hum   : %5.1f%%\n", hum);
  }

  M5.update();
}
```

上传完成就可以看到下面的效果了

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/m5air_quality_arduino_quickstart_scd40.jpg" width="30%">

