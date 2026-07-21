# Dial Encoder 旋转编码器

Dial Encoder 旋转编码器相关API与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Dial
- M5Dial 库版本 >= 1.0.3

```cpp line-num
#include "M5Dial.h"

long oldPosition = -999;

void setup() {
  auto cfg = M5.config();
  M5Dial.begin(cfg, true, false);  // encoder, RFID

  M5Dial.Display.setTextColor(GREEN);
  M5Dial.Display.setTextDatum(middle_center);
  M5Dial.Display.setTextFont(&fonts::Orbitron_Light_32);
  M5Dial.Display.setTextSize(2);
}

void loop() {
  M5Dial.update();

  long newPosition = M5Dial.Encoder.read();
  if (newPosition != oldPosition) {
    M5Dial.Speaker.tone(8000, 20);
    M5Dial.Display.clear();
    M5Dial.Display.drawString(String(newPosition),
                              M5Dial.Display.width() / 2,
                              M5Dial.Display.height() / 2);
    oldPosition = newPosition;
  }

  if (M5Dial.BtnA.wasPressed()) {
    M5Dial.Encoder.readAndReset();
  }
  if (M5Dial.BtnA.pressedFor(5000)) {
    M5Dial.Encoder.write(100);
  }
}
```

编译上传后，屏幕上将显示一个跟随旋转编码器变化的数字。短按按钮将数字复位为 0，长按按钮 5s 将数字复位为 100。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1126/Arduino_encoder.gif" width="30%">

## begin

**函数原型:**

```cpp
void begin();
```

**功能说明:**

- 初始化编码器 IO

可在调用`M5Dial.begin()`时将参数`enableEncoder`设置为`true`一同初始化。

```cpp
M5Dial.begin(m5::M5Unified::config_t cfg, bool enableEncoder, bool enableRFID);
```

**传入参数:**

- null

**返回值:**

- null

## read

**函数原型:**

```cpp
int32_t read();
```

**功能说明:**

- 读取当前编码器数值

**传入参数:**

- null

**返回值:**

- int32_t: 当前编码器数值

## write

**函数原型:**

```cpp
void write(int32_t p);
```

**功能说明:**

- 写入更新编码器数值

**传入参数:**

- int32_t p: 更新的编码器数值

**返回值:**

- null

## readAndReset

**函数原型:**

```cpp
int32_t readAndReset();
```

**功能说明:**

- 重置当前编码器数值

**传入参数:**

- null

**返回值:**

- int32_t: 重置前的编码器数值
