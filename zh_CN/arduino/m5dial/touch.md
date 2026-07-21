# Dial Touch 触摸屏

Dial Touch 屏幕触摸相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Dial
- M5Dial 库版本 >= 1.0.3

```cpp line-num
#include <M5Dial.h>

m5::touch_detail_t touchDetail;

void setup() {
  auto cfg = M5.config();
  M5Dial.begin(cfg, false, false);  // encoder, RFID

  M5Dial.Display.setTextColor(GREEN);
  M5Dial.Display.setTextDatum(middle_center);
  M5Dial.Display.setTextFont(&fonts::FreeMono12pt7b);
  M5Dial.Display.setTextSize(1);

  M5Dial.Display.drawString("Touch Test", M5Dial.Display.width() / 2, M5Dial.Display.height() / 2);
}

void loop() {
  M5Dial.update();
  touchDetail = M5Dial.Touch.getDetail();

  if (touchDetail.isPressed()) {
    M5.Display.fillCircle(touchDetail.x, touchDetail.y, 2, SKYBLUE);
  }
}
```

运行效果如下：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/Arduino_touch.gif" width="30%">

## API

M5Dial 库基于 M5Unified 库实现，屏幕触摸部分使用了 M5Unified 库中的`Touch_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Touch Class](/zh_CN/arduino/m5unified/touch_class)
