# Tough Touch 触摸屏

Tough 触摸屏相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 2.1.4
- 开发板选项 = M5Tough
- M5Unified 库版本 >= 0.2.5
- M5GFX 库版本 >= 0.2.7

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

m5::touch_detail_t touchDetail;

int width, height;

void setup() {
  M5.begin();
  M5.Display.setRotation(1);
  M5.Display.setFont(&fonts::DejaVu40);

  width = M5.Display.width();
  height = M5.Display.height();

  Serial.begin(115200);
  Serial.println("Start touching!");
  M5.Display.print("Start touching!");
}

void loop() {
  M5.update();
  touchDetail = M5.Touch.getDetail();

  if (touchDetail.isPressed()) {
    Serial.printf("x:%d, y:%d\r\n", touchDetail.x, touchDetail.y);

    for (int i = 0; i < width; i += 10) {
      for (int j = 0; j < height; j += 10) {
        uint8_t cr = map((touchDetail.x - i) % width, 0, width, 0, 256);
        uint8_t cg = map((touchDetail.y - j) % height, 0, height, 0, 256);
        uint16_t color = M5.Display.color565(cr, cg, 255 - (cr + cg) / 2);
        M5.Display.fillRect(i, j, 10, 10, color);
      }
    }
  }
}
```

该程序的主要功能是，当手指触摸屏幕时，通过串口向电脑输出触摸点的坐标，屏幕上的彩色阵列跟随触摸点移动。程序中只读取了一个触摸点，你也可以通过下述API开发使用 Tough 的两点触控功能。

<!--
<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/Tough_Arduino_touch.gif" width="30%">
-->

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/647/Tough_Arduino_touch.mp4" type="video/mp4"></video>

## API

Tough 触摸屏部分使用了 `M5Unified` 库中的 `Touch_Class`，更多相关的API可以参考下方文档：

- [M5Unified - Touch Class](/zh_CN/arduino/m5unified/touch_class)