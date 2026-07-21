# Unit Glass2 Arduino 使用教程

## 1.准备工作

- 环境配置：参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide) 完成 IDE 安装，并根据实际使用的开发板安装对应的板管理与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
- 使用到的硬件产品：
  - [Atom Lite](https://shop.m5stack.com/products/atom-lite-esp32-development-kit)
  - [Unit Glass2](https://shop.m5stack.com/products/glass-2-unit-w-1-51inch-transparent-oled)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM%20Lite/img-d066cf3f-63a8-4866-bed2-2c2a6d9c034e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass2%20Unit/img-b54af17c-414a-41d1-92ea-cbf59d9f9955.webp" width="20%">

## 2.案例程序

#> 编译要求 | M5Stack 板管理版本 >= 3.2.2<br>M5Unified 库版本 >= 0.2.7<br>M5GFX 库版本 >= 0.2.9

```cpp line-num
#include <M5UnitGLASS2.h>
#include <M5Unified.h>

#define M5UNITGLASS2_ADDR 0x3C  // For Unit Glass2, 0x3C is default, and 0x3D is modified.

int index_unit_glass2;

void setup() {
  auto cfg = M5.config();
  cfg.external_display.unit_glass2 = true;
  M5.begin(cfg);

  index_unit_glass2 = M5.getDisplayIndex(m5::board_t::board_M5UnitGLASS2);
  M5.Displays(index_unit_glass2).setTextSize(2);
  M5.Displays(index_unit_glass2).clear();
}

void loop() {
  M5.Displays(index_unit_glass2).setCursor(0, 0);
  M5.Displays(index_unit_glass2).print("This is \nUnit \nGlass2");
  delay(1000);
  M5.Displays(index_unit_glass2).clear();

  M5.Displays(index_unit_glass2).drawRect(0, 0, 128, 64, 0xFFFF);  // x, y, w, h, color
  delay(500);
  M5.Displays(index_unit_glass2).drawCircle(20, 20, 15, 0xFFFF);  // x, y, r, color
  delay(500);
  M5.Displays(index_unit_glass2).fillArc(50, 45, 17, 20, 100, 330, 0xFFFF);  // x, y, r0, r1, angle0, angle1, color
  delay(500);
  M5.Displays(index_unit_glass2).fillRect(45, 10, 25, 10, 0xFFFF);  // x, y, w, h, color
  delay(500);
  M5.Displays(index_unit_glass2).fillTriangle(90, 10, 80, 40, 110, 55, 0xFFFF);  // x0, y0, x1, y1, x2, y2, color
  delay(500);
  M5.Displays(index_unit_glass2).drawLine(110, 0, 128, 64, 0xFFFF);  // x0, y0, x1, y1, color
  delay(1000);

  M5.Displays(index_unit_glass2).clear();
}
```

运行效果：

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/757/UnifiedLib_2.mp4" type="video/mp4"></video>

## 3.I2C地址修改

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/757/Unit_Glass_2_I2C.png" width="70%">

如上图所示，用六角扳手取下两颗螺丝，向上取下盖板，推开屏幕排线，露出圆圈里的两个半圆形焊盘。在圆圈内点锡使两个焊盘导通，即可将 I2C 地址修改为 `0x3D`；移除点锡即可恢复为 `0x3C`。

I2C 地址若修改为 `0x3D`，需要在程序中添加宏定义 `#define M5UNITGLASS2_ADDR 0x3D`。两个 HY2.0-4P Grove 接口是连通的，可互换使用，用于连接其他 I2C 设备。

## 4.API

- [M5GFX API](/zh_CN/arduino/m5gfx/m5gfx_functions)
