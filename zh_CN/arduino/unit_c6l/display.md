# Unit C6L Display 屏幕显示

Unit C6L 屏幕显示相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.3
- 开发板选项 = M5UnitC6L
- M5Unified 库版本 >= 0.2.10
- M5GFX 库版本 >= 0.2.15

```cpp line-num
#include <M5Unified.h>

void setup() {
  M5.begin();

  M5.Display.setTextSize(1);
  M5.Display.clear();
}

void loop() {
  M5.Display.setCursor(0, 0);
  M5.Display.print("This is \nUnit C6L");
  delay(1000);
  M5.Display.clear();

  M5.Display.drawRect(0, 0, 64, 48, 0xFFFF);  // x, y, w, h, color
  delay(500);
  M5.Display.drawCircle(10, 10, 8, 0xFFFF);  // x, y, r, color
  delay(500);
  M5.Display.fillArc(26, 32, 8, 12, 100, 330, 0xFFFF);  // x, y, r0, r1, angle0, angle1, color
  delay(500);
  M5.Display.fillRect(24, 7, 15, 7, 0xFFFF);  // x, y, w, h, color
  delay(500);
  M5.Display.fillTriangle(45, 7, 40, 30, 55, 42, 0xFFFF);  // x0, y0, x1, y1, x2, y2, color
  delay(500);
  M5.Display.drawLine(55, 0, 64, 48, 0xFFFF);  // x0, y0, x1, y1, color
  delay(1000);

  M5.Display.clear();
}
```

运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1185/display.gif" width="50%">

## API

Unit C6L 屏幕显示部分使用 `M5GFX` 库作为驱动，更多相关的 API 可以参考下方文档：

- [M5GFX Setup](/zh_CN/arduino/m5gfx/m5gfx)
- [M5GFX API](/zh_CN/arduino/m5gfx/m5gfx_functions)
- [M5GFX - GitHub](https://github.com/m5stack/M5GFX)