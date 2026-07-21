# Core2 Touch 触摸屏

Core2 触摸屏相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.0
- 开发板选项 = M5Core2
- M5Unified 库版本 >= 0.2.7
- M5GFX 库版本 >= 0.2.8

### 1.触屏按键检测

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

m5::touch_detail_t touchDetail;
static int32_t w;
static int32_t h;

LGFX_Button button;

void setup() {
  M5.begin();

  w = M5.Lcd.width();
  h = M5.Lcd.height();
  
  M5.Lcd.fillScreen(WHITE);
  M5.Display.setRotation(0);
  M5.Display.setTextDatum(top_center);
  M5.Display.drawString("Button Released", w / 2, 0, &fonts::FreeMonoBold24pt7b);

  button.initButton(&M5.Lcd, w / 2, h / 2, 200, 200, TFT_BLUE, TFT_YELLOW, TFT_BLACK, "BTN", 4, 4);
  button.drawButton();
}

void loop() {
  M5.update();
  touchDetail = M5.Touch.getDetail();

  if (touchDetail.isPressed()) {
    if(button.contains(touchDetail.x, touchDetail.y)){
        M5.Display.drawString("Button  Pressed", w / 2, 0, &fonts::FreeMonoBold24pt7b);
    }
  }
  else {
    M5.Display.drawString("Button Released", w / 2, 0, &fonts::FreeMonoBold24pt7b);
  }
}
```

该程序的功能是，当手指触摸屏幕时，若触摸点在按钮区域内，则显示“Button Pressed”，否则显示“Button Released”。

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/Core2_Arduino_touch.mp4" type="video/mp4"></video>

### 2.多点触摸检测

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

m5::touch_point_t touchPoint[2];//Core2 supports up to 2-point touch
static bool drawed = false;
static int32_t w;
static int32_t h;

void setup() {
  M5.begin();

  w = M5.Lcd.width();
  h = M5.Lcd.height();
  
  M5.Lcd.fillScreen(WHITE);
  M5.Display.setRotation(1);
  M5.Display.setTextDatum(top_center);
  M5.Display.drawString("Touch not found", w / 2, 0, &fonts::FreeMonoBold12pt7b);
  M5.Display.setFont(&fonts::FreeMonoBold12pt7b);
}

void loop() {
  M5.update();
  int nums = M5.Lcd.getTouchRaw(touchPoint, 2);  

  if (nums)
  {
    M5.Display.drawString(" Touch detail: ", w / 2, 0, &fonts::FreeMonoBold12pt7b);
    for (int i = 0; i < nums; i++)
    {
      M5.Display.setCursor(0, 40 + i * 25);
      M5.Display.printf("Point %d X:%04d  Y:%04d", i+1, touchPoint[i].x, touchPoint[i].y);
    }
    drawed = true;
  }
  else if (drawed){
    drawed = false;
    M5.Display.clear(WHITE);
    M5.Display.drawString("Touch not found", w / 2, 0, &fonts::FreeMonoBold12pt7b);
  }
  vTaskDelay(1);
}  
```

该程序的功能是，当手指触摸屏幕时，显示触摸点的坐标信息。Core2 支持最多 2 点触摸。

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/Core2_Arduino_multouch.mp4" type="video/mp4"></video>

## API

Core2 触摸屏部分使用了 `M5Unified` 库中的 `Touch_Class`，更多相关的API可以参考下方文档：

- [M5Unified - Touch Class](/zh_CN/arduino/m5unified/touch_class)