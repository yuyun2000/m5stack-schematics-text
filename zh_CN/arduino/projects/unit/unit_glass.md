# Unit Glass Arduino 使用教程

## 1.准备工作

- 环境配置：参考 [Arduino IDE 上手教程](/zh_CN/arduino/arduino_ide) 完成 IDE 安装，并根据实际使用的开发板安装对应的板管理与需要的驱动库。
- 使用到的驱动库：
  - [M5Unified](https://github.com/m5stack/M5Unified)
  - [M5GFX](https://github.com/m5stack/M5GFX)
- 使用到的硬件产品：
  - [Atom Lite](https://shop.m5stack.com/products/atom-lite-esp32-development-kit)
  - [Unit Glass](https://shop.m5stack.com/products/glass-unit-w-1-51inch-transparent-oled)

<img src="https://static-cdn.m5stack.com/resource/docs/products/core/ATOM%20Lite/img-d066cf3f-63a8-4866-bed2-2c2a6d9c034e.webp" width="20%"><img src="https://static-cdn.m5stack.com/resource/docs/products/unit/Glass%20Unit/img-467f2a5f-e95c-4e39-b99a-baf0f1505c72.webp" width="20%">

## 2.案例程序

#> 编译要求 | M5Stack 板管理版本 >= 3.2.2<br>M5Unified 库版本 >= 0.2.7<br>M5GFX 库版本 >= 0.2.9

```cpp line-num
#include <Wire.h>
#include <M5UnitGLASS.h>
#include <M5Unified.h>

#define GLASS_BUZZ_PARAM_REG 0xC0
#define GLASS_BUZZ_ONOFF_REG 0xC3
#define GLASS_KEY_A_REG 0xD0
#define GLASS_KEY_B_REG 0xD1

int index_unit_glass;

void setup() {
  Wire.setClock(400000);

  auto cfg = M5.config();
  cfg.external_display.unit_glass = true;
  M5.begin(cfg);

  index_unit_glass = M5.getDisplayIndex(m5::board_t::board_M5UnitGLASS);
  M5.Displays(index_unit_glass).setTextSize(2);
  M5.Displays(index_unit_glass).clear();

  M5.Displays(index_unit_glass).setCursor(0, 0);
  M5.Displays(index_unit_glass).print("This is \nUnit Glass");
  delay(1000);
  M5.Displays(index_unit_glass).clear();

  M5.Displays(index_unit_glass).drawRect(0, 0, 128, 64, 0xFFFF);  // x, y, w, h, color
  delay(500);
  M5.Displays(index_unit_glass).drawCircle(20, 20, 15, 0xFFFF);  // x, y, r, color
  delay(500);
  M5.Displays(index_unit_glass).fillArc(50, 45, 17, 20, 100, 330, 0xFFFF);  // x, y, r0, r1, angle0, angle1, color
  delay(500);
  M5.Displays(index_unit_glass).fillRect(45, 10, 25, 10, 0xFFFF);  // x, y, w, h, color
  delay(500);
  M5.Displays(index_unit_glass).fillTriangle(90, 10, 80, 40, 110, 55, 0xFFFF);  // x0, y0, x1, y1, x2, y2, color
  delay(500);
  M5.Displays(index_unit_glass).drawLine(110, 0, 128, 64, 0xFFFF);  // x0, y0, x1, y1, color
  delay(1000);

  M5.Displays(index_unit_glass).clear();
}

void loop() {
  bool keyA = get_keyA_state();
  bool keyB = get_keyB_state();

  if (keyA || keyB) {
    M5.Displays(index_unit_glass).clear();

    if (keyA) {
      M5.Displays(index_unit_glass).setCursor(0, 0);
      M5.Displays(index_unit_glass).print("Key A \npressed");
      set_buzz_param(2000, 128);  // freq, duty
    }
    if (keyB) {
      M5.Displays(index_unit_glass).setCursor(0, 0);
      M5.Displays(index_unit_glass).print("Key B \npressed");
      set_buzz_param(5000, 128);  // freq, duty
    }

    set_buzz_onoff(true);
  } else {
    M5.Displays(index_unit_glass).setCursor(0, 0);
    M5.Displays(index_unit_glass).print("No key \npressed");
    set_buzz_onoff(false);
  }

  delay(10);
}

// Set buzzer frequency (Hz) and duty (0-255)
void set_buzz_param(int freq, int duty) {
  Wire.beginTransmission(M5UNITGLASS_ADDR);
  Wire.write(GLASS_BUZZ_PARAM_REG);
  Wire.write(freq & 0xFF);         // frequency low bit
  Wire.write((freq >> 8) & 0xFF);  // frequency high bit
  Wire.write(duty);
  Wire.endTransmission();
}

// Toggle buzzer on / off
void set_buzz_onoff(bool on) {
  Wire.beginTransmission(M5UNITGLASS_ADDR);
  Wire.write(GLASS_BUZZ_ONOFF_REG);
  Wire.write(on ? 0x01 : 0x00);
  Wire.endTransmission();
}

// Read key A state
bool get_keyA_state() {
  Wire.beginTransmission(M5UNITGLASS_ADDR);
  Wire.write(GLASS_KEY_A_REG);
  Wire.endTransmission(false);
  Wire.requestFrom(M5UNITGLASS_ADDR, 1);
  bool keyAState = !Wire.read();
  return keyAState;
}

// Read key B state
bool get_keyB_state() {
  Wire.beginTransmission(M5UNITGLASS_ADDR);
  Wire.write(GLASS_KEY_B_REG);
  Wire.endTransmission(false);
  Wire.requestFrom(M5UNITGLASS_ADDR, 1);
  bool keyBState = !Wire.read();
  return keyBState;
}
```

运行效果：

<video class="video-container" controls><source src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/612/UnifiedLib_1.mp4" type="video/mp4"></video>

## 3.API

- [M5GFX API](/zh_CN/arduino/m5gfx/m5gfx_functions)
- [Unit Glass I2C Protocol PDF](https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/612/UnitGlass_I2C_Protocol.pdf)
- [M5Unit-GLASS - GitHub](https://github.com/m5stack/M5Unit-GLASS)<br>该库已停止更新，推荐使用上述的 M5Unified 与 M5GFX 库。旧库中的示例程序可参考 [迁移至 M5Unified](/zh_CN/arduino/m5unified/migration) 做相应的更改。
