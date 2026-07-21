# 屏幕电源管理

- [电源状态管理](#电源状态管理)
  - [powerSave](#powersave)
  - [powerSaveOff](#powersaveoff)
  - [powerSaveOn](#powersaveon)
- [休眠与唤醒](#休眠与唤醒)
  - [sleep](#sleep)
  - [wakeup](#wakeup)

## 电源状态管理

#>说明：|仅为电源状态记录函数，不涉及实际情况的电源开启和关闭。

### powerSave

**函数原型：**

```cpp
void powerSave(bool flg)
```

**功能说明：**

- 设置电源保存状态

**传入参数:**

- flg：电源保存标志
  - true：开启电源保存
  - false：关闭电源保存

**返回值：**

- null

### powerSaveOff

**函数原型：**

```cpp
void powerSaveOff(void)
```

**功能说明：**

- 设置电源保存状态为关闭

**传入参数:**

- null

**返回值：**

- null

### powerSaveOn

**函数原型：**

```cpp
void powerSaveOn(void)
```

**功能说明：**

- 设置电源保存状态为开启

**传入参数:**

- null

**返回值：**

- null

## 休眠与唤醒

### sleep

**函数原型：**

```cpp
void sleep(void)
```

**功能说明：**

- 休眠面板，使用 [wakeup](#wakeup) 唤醒面板

**传入参数:**

- null

**返回值：**

- null

### wakeup

**函数原型：**

```cpp
void wakeup(void)
```

**功能说明：**

- 唤醒面板，使用 [sleep](#sleep) 休眠面板

**传入参数:**

- null

**返回值：**

- null

**案例程序：**

```cpp line-num
#include <Arduino.h>
#include <M5GFX.h>

M5GFX display;

void setup() {
    display.begin();

    display.setRotation(3);
    if(display.isEPD())
    {
        display.setColorDepth(8);//The ink screen product supports a maximum bit depth of 8 bits.
        display.setEpdMode(epd_fastest);
    }
    else
    {
        display.setColorDepth(16);
    }
    
    display.clear(TFT_WHITE);
    display.setFont(&fonts::FreeMonoBoldOblique12pt7b);
    display.setTextColor(TFT_BLACK);
    display.setTextSize(1);
    display.setCursor(0, 0);

    display.println("\nFive seconds later, the rear panel enters sleep mode. After three seconds of sleep, it is awakened.");
    delay(5000);
    display.sleep();
    display.powerSave(false);
    delay(3000);
    display.wakeup();
    display.powerSaveOn();
    display.println("\nPanel awakended!");
}

void loop() {
}
```
