# StickC Button 按键

<a id="stickc-button"></a>

- [Button](#stickc-button)
  - [read](#read)
  - [lastChange](#lastchange)
  - [isPressed](#ispressed)
  - [wasPressed](#waspressed)
  - [pressedFor](#pressedfor)
  - [isReleased](#isreleased)
  - [releasedFor](#releasedfor)
  - [wasReleased](#wasreleased)
  - [wasReleasefor](#wasreleasefor)

## read

**函数原型:**

```cpp
uint8_t read();
```

**功能说明:**

- 读取按键状态

**传入参数:**

- null

**返回值:**

- uint8_t:
  - 1:按下
  - 0:释放

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.println("Please pressed Button A.");
}

void loop() {
  M5.Lcd.setCursor(0, 0);
  M5.Lcd.printf("Button A Status: %d ",M5.BtnA.read());
}
```

## lastChange

**函数原型:**

```cpp
uint32_t lastChange();
```

**功能说明:**

- 获取上一次状态更新的时间

**传入参数:**

- null

**返回值:**

- uint32_t: 上一次状态更新的时间 ms

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.println("Please pressed Button A.");
}

void loop() {
  M5.update();
  M5.Lcd.setCursor(0, 0);
  M5.Lcd.printf("The last change at %d ms /n",M5.BtnA.lastChange());
}
```

## isPressed

**函数原型:**

```cpp
uint8_t isPressed();
```

**功能说明:**

- 判断按键是否按下

**传入参数:**

- null

**返回值:**

- uint8_t:
  - 1: 按键处于按下状态
  - 0: 按键不处于按下状态

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.println("Please pressed Button A.");
}

void loop() {
  M5.update();
  M5.Lcd.setCursor(0, 0);
  if (M5.BtnA.isPressed()) {
    M5.Lcd.println("Button is Pressed.");
  }else{
    M5.Lcd.println("Button is Released.");
  }
  delay(20);
}
```

## wasPressed

**函数原型:**

```cpp
uint8_t wasPressed();
```

**功能说明:**

- 判断按键由释放状态, 变化为按下状态

**传入参数:**

- null

**返回值:**

- uint8_t:
  - 1: 触发按键由释放状态变化为按下状态
  - 0: 未触发按键由释放状态变化为按下状态

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.println("Please pressed Button A.");
}

void loop() {
  M5.update();
  if (M5.BtnA.wasPressed()) {	
    M5.Lcd.println("Button is pressed.");
  } 
  delay(20);
}
```

## pressedFor

**函数原型:**

```cpp
uint8_t pressedFor(uint32_t ms);
```

**功能说明:**

- 判断按键是否按下超过指定超时时间

**传入参数:**

- uint32_t ms：
  - 按键按下超时时间 ms

**返回值:**

- uint8_t:
  - 1: 触发按键释放超过超时时间
  - 0: 未触发

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.println("Please pressed Button A.");
}

void loop() {
  M5.update();
  if (M5.BtnA.pressedFor(2000)) {
    M5.Lcd.println("Button A was pressed for more than 2 seconds.");
    delay(1000);
  }
}
```

## isReleased

**函数原型:**

```cpp
uint8_t isPressed();
```

**功能说明:**

- 判断按键是否处于释放状态

**传入参数:**

- null

**返回值:**

- uint8_t:
  - 1: 按键处于释放状态
  - 0: 按键不处于释放状态

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
}

void loop() {
  M5.update();
  if (M5.BtnA.isReleased()) {
    M5.Lcd.println("Button is released.");
  }else{
    M5.Lcd.println("Button is Pressed .");
  }
  delay(20);
}
```

## releasedFor

**函数原型:**

```cpp
uint8_t releasedFor(uint32_t ms);
```

**功能说明:**

- 判断按键释放超时时间

**传入参数:**

- uint32_t ms：
  - 按键释放超时时间 ms

**返回值:**

- uint8_t:
  - 1: 触发按键释放超过超时时间
  - 0: 未触发

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
}

void loop() {
  M5.update();
  M5.Lcd.setCursor(0, 0);
  if (M5.BtnA.releasedFor(2000)) {
    M5.Lcd.println("Button A was released for more than 2 seconds.");
    delay(1000);
  }else{
    M5.Lcd.println("Button A is pressed                           ");
  }
}
```

## wasReleased

**函数原型:**

```cpp
uint8_t wasReleased();
```

**功能说明:**

- 判断按键由按下状态, 变化为释放状态

**传入参数:**

- null

**返回值:**

- uint8_t:
  - 1: 触发按键由按下状态变化为释放状态
  - 0: 未触发按键由按下状态变化为释放状态

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.println("Please pressed Button A.");
}

void loop() {
  M5.update();
  if(M5.BtnA.wasReleased()) {
    M5.Lcd.println("Button is Released.");
  }
  delay(20);
}
```

## wasReleasefor

**函数原型:**

```cpp
uint8_t wasReleasefor(uint32_t ms);
```

**功能说明:**

- 判断按键是否按下超过指定超时时间, 释放后触发

**传入参数:**

- uint32_t ms：
  - 按键释放超时时间 ms

**返回值:**

- uint8_t:
  - 1: 触发按键释放超过超时时间
  - 0: 未触发

**案例程序:**

```cpp line-num
#include <M5StickC.h>

void setup() {
  M5.begin();
  M5.Lcd.println("Please pressed Button A.");
}

void loop() {
  M5.update();
  if (M5.BtnA.wasReleasefor(3000)) {
      M5.Lcd.println("OK");
  }
}
```
