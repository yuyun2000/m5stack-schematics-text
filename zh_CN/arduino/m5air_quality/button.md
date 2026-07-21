# Air Quality 按键

Air Quality按键输入相关API与案例程序。

## 案例程序

```cpp line-num
#include <M5Unified.h>

void setup() {
  
  auto cfg = M5.config(); 
  cfg.serial_baudrate = 115200;
  M5.begin(cfg);

  M5.Lcd.clear();
  M5.Lcd.setTextSize(2);
  M5.Lcd.setCursor(0, 0);
  M5.Lcd.println("M5AirQ Button Test");
}

void loop() {
  M5.update();           

  // 检测 BtnA（GPIO0）点击
  if (M5.BtnA.wasClicked()) {
    Serial.println("AirQ BtnA clicked");
    M5.Lcd.println("BtnA clicked");
  }

  // 检测 BtnB（GPIO8）点击
  if (M5.BtnB.wasClicked()) {
    Serial.println("AirQ BtnB clicked");
    M5.Lcd.println("BtnB clicked");
  }
  delay(10);
}
```

上传完成按下按键就可以看到下面的效果了

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/467/m5air_quality_arduino_quickstart_button.jpg" width="30%">


## API

按键部分使用了M5Unified库中的`Button_Class`， 更多按键相关的API可以参考下方文档：

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)

