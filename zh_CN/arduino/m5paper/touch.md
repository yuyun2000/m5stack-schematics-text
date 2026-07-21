# Paper Touch 触摸屏

Paper 触摸屏相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 2.1.4
- 开发板选项 = M5Paper
- M5Unified 库版本 >= 0.2.5
- M5GFX 库版本 >= 0.2.7

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

m5::touch_detail_t touchDetail;
uint16_t color;

void setup() {
  M5.begin();
  M5.Display.setRotation(0);
  M5.Display.setFont(&fonts::DejaVu40);
  M5.Display.setEpdMode(epd_fastest);  // epd_quality, epd_text, epd_fast, epd_fastest

  color = random(65535);

  Serial.begin(115200);
  Serial.println("Start drawing!");
  M5.Display.print(" Start drawing! ");
}

void loop() {
  M5.update();
  touchDetail = M5.Touch.getDetail();

  if (touchDetail.isPressed()) {
    Serial.printf("x:%d, y:%d\r\n", touchDetail.x, touchDetail.y);
    color = (color + 5) % 65536;
    M5.Display.fillCircle(touchDetail.x, touchDetail.y, 15, color);
  }
}
```

该程序的主要功能是，当手指触摸屏幕时，通过串口向电脑输出触摸点的坐标，并在触摸点画出不同颜色（灰度）的圆圈。程序中只读取了一个触摸点，您也可以通过下述API开发使用 Paper 的两点触控功能。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/689/Paper_Arduino_touch.jpeg" width="50%">

## API

Paper 触摸屏部分使用了 `M5Unified` 库中的 `Touch_Class`，更多相关的API可以参考下方文档：

- [M5Unified - Touch Class](/zh_CN/arduino/m5unified/touch_class)