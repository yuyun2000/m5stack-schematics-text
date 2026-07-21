# Cardputer Keyboard 键盘

Cardputer 键盘输入相关 API 与案例程序，适用于 Cardputer 和 Cardputer-Adv。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Cardputer
- M5Cardputer 库版本 >= 1.1.0
- M5Unified 库版本 >= 0.2.8
- M5GFX 库版本 >= 0.2.10

#> 注意事项 | 使用时需要在主循环中包含`M5Cardputer.update()`函数用于读取状态更新，且尽可能减少阻塞情况，否则可能无法及时获取键盘变化。

```cpp line-num
#include "M5Cardputer.h"

M5Canvas canvas(&M5Cardputer.Display);
String data = "> ";

void setup() {
  auto cfg = M5.config();
  M5Cardputer.begin(cfg, true);  // enableKeyboard
  M5Cardputer.Display.setRotation(1);
  M5Cardputer.Display.setTextSize(0.5);
  M5Cardputer.Display.setTextFont(&fonts::FreeSerifBoldItalic18pt7b);

  M5Cardputer.Display.drawRect(0, 0, M5Cardputer.Display.width(), M5Cardputer.Display.height() - 28, GREEN);
  M5Cardputer.Display.fillRect(0, M5Cardputer.Display.height() - 4, M5Cardputer.Display.width(), 4, GREEN);

  canvas.setTextSize(0.5);
  canvas.setTextFont(&fonts::FreeSerifBoldItalic18pt7b);
  canvas.setTextScroll(true);

  canvas.createSprite(M5Cardputer.Display.width() - 8, M5Cardputer.Display.height() - 36);
  canvas.println("Press Key and Enter to Input Text");
  canvas.pushSprite(4, 4);

  M5Cardputer.Display.drawString(data, 4, M5Cardputer.Display.height() - 24);
}

void loop() {
  M5Cardputer.update();

  if (M5Cardputer.Keyboard.isChange()) {
    if (M5Cardputer.Keyboard.isPressed()) {
      Keyboard_Class::KeysState status = M5Cardputer.Keyboard.keysState();

      for (auto i : status.word) {
        data += i;
      }

      if (status.del) {
        data.remove(data.length() - 1);
      }

      if (status.enter) {
        data.remove(0, 2);
        canvas.println(data);
        canvas.pushSprite(4, 4);
        data = "> ";
      }

      M5Cardputer.Display.fillRect(0, M5Cardputer.Display.height() - 28, M5Cardputer.Display.width(), 25, BLACK);
      M5Cardputer.Display.drawString(data, 4, M5Cardputer.Display.height() - 24);
    }
  }
}
```

运行效果如图：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Arduino_keyboard.gif" width="70%">

## Keyboard_Class API

### begin

**函数原型：**

```cpp
void begin();
```

**功能说明：**

- 初始化键盘

可在调用`M5Cardputer.begin()`时将参数`enableKeyboard`设置为`true`一同初始化。

```cpp
M5Cardputer.begin(m5::M5Unified::config_t cfg, bool enableKeyboard);
```

**传入参数：**

- null

**返回值：**

- null

### isChange

**函数原型：**

```cpp
bool isChange();
```

**功能说明：**

- 检测键盘状态有无变化，键盘上任何按键被按下或松开时都会触发。

**传入参数：**

- null

**返回值：**

- bool
  - true: 键盘状态有变化
  - false: 键盘状态无变化

### isPressed

**函数原型：**

```cpp
uint8_t isPressed();
```

**功能说明：**

- 读取被按下的按键数量

**传入参数：**

- null

**返回值：**

- uint8_t
  - 被按下的按键数量

### isKeyPressed

**函数原型：**

```cpp
bool isKeyPressed(char c);
```

**功能说明：**

- 检测当前指定按键是否被按下

**传入参数：**

- char c
  - 按键名称，比如 `'A'`、`'a'`、`'1'`、`','`、`' '`（空格）、`KEY_LEFT_SHIFT`、`KEY_BACKSPACE`、`KEY_ENTER`、`KEY_FN` 等。

**返回值：**

- bool
  - true: 指定按键被按下
  - false: 指定按键未被按下

### getKey

**函数原型：**

```cpp
uint8_t getKey(Point2D_t keyCoor);
```

**功能说明：**

- 返回指定坐标的按键对应的十进制 ASCII 编码

**传入参数：**

- Point2D_t keyCoor
  - keyCoor.x: 按键的横坐标，取值范围为 [0, 13]，最左列为 0
  - keyCoor.y: 按键的纵坐标，取值范围为 [0, 3]，最上行为 0

**返回值：**

- uint8_t
  - 按键对应的十进制 ASCII 编码

## 相关链接

- [GitHub](https://github.com/m5stack/M5Cardputer/tree/master/src/utility) M5Cardputer 库中的键盘部分源码