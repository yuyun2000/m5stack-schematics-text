# M5Unified Button Class

- [Button Class](#m5unified-button-class)
  - [wasClicked](#wasclicked)
  - [wasHold](#washold)
  - [wasSingleClicked](#wassingleclicked)
  - [wasDoubleClicked](#wasdoubleclicked)
  - [wasDecideClickCount](#wasdecideclickcount)
  - [getClickCount](#getclickcount)
  - [isHolding](#isholding)
  - [wasChangePressed](#waschangepressed)
  - [isPressed](#ispressed)
  - [isReleased](#isreleased)
  - [wasPressed](#waspressed)
  - [wasReleased](#wasreleased)
  - [wasReleasedAfterHold](#wasreleasedafterhold)
  - [wasReleaseFor](#wasreleasefor)
  - [setDebounceThresh](#setdebouncethresh)
  - [setHoldThresh](#setholdthresh)
  - [setRawState](#setrawstate)
  - [setState](#setstate)
  - [getState](#getstate)
  - [lastChange](#lastchange)
  - [getDebounceThresh](#getdebouncethresh)
  - [getHoldThresh](#getholdthresh)
  - [getUpdateMsec](#getupdatemsec)

## wasClicked

**函数原型:**

```cpp
bool wasClicked(void)
```

**功能说明:**

- 判断按键是否点击

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发按键点击
  - false: 未触发按键点击

## wasHold

**函数原型:**

```cpp
bool wasHold(void)
```

**功能说明:**

- 判断按键是否保持按下, 默认判断阈值时间为 500ms

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发按键保持
  - false: 未触发按键保持

## wasSingleClicked

**函数原型:**

```cpp
bool wasSingleClicked(void)
```

**功能说明:**

- 判断按键单击事件

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发按键单击
  - false: 未触发按键单击

## wasDoubleClicked

**函数原型:**

```cpp
bool wasDoubleClicked(void)
```

**功能说明:**

- 判断按键双击事件

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发按键双击
  - false: 未触发按键双击

## wasDecideClickCount

**函数原型:**

```cpp
bool wasDecideClickCount(void)
```

**功能说明:**

- 触发按键点击计数, 可通过 getClickCount API 获取点击次数

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发点击计数
  - false: 为触发点击计数

## getClickCount

**函数原型:**

```cpp
uint8_t getClickCount(void)
```

**功能说明:**

- 获取按键点击次数

**传入参数:**

- null

**返回值:**

- uint8_t: 点击次数

## isHolding

**函数原型:**

```cpp
bool isHolding(void)
```

**功能说明:**

- 判断按键当前是否按下保持

**传入参数:**

- null

**返回值:**

- bool:
  - true: 按键当前处于按下保持状态
  - false: 按键当前不处于按下保持状态

## wasChangePressed

**函数原型:**

```cpp
bool wasChangePressed(void)
```

**功能说明:**

- 判断按键状态是否变化

**传入参数:**

- null

**返回值:**

- bool:
  - true: 按键状态变化
  - false: 无按键状态变化

## isPressed

**函数原型:**

```cpp
bool isPressed(void)
```

**功能说明:**

- 判断按键是否按下

**传入参数:**

- null

**返回值:**

- bool:
  - true: 按键处于按下状态
  - false: 按键不处于按下状态

## isReleased

**函数原型:**

```cpp
bool isReleased(void)
```

**功能说明:**

- 判断按键是否处于释放状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 按键处于释放状态
  - false: 按键不处于释放状态

## wasPressed

**函数原型:**

```cpp
bool wasPressed(void)
```

**功能说明:**

- 判断按键由释放状态, 变化为按下状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发按键由释放状态变化为按下状态
  - false: 未触发按键由释放状态变化为按下状态

## wasReleased

**函数原型:**

```cpp
bool wasReleased(void)
```

**功能说明:**

- 判断按键由按下状态, 变化为释放状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发按键由按下状态变化为释放状态
  - false: 未触发按键由按下状态变化为释放状态

## wasReleasedAfterHold

**函数原型:**

```cpp
bool wasReleasedAfterHold(void)
```

**功能说明:**

- 判断按键按下后, 保持一段时间, 然后变化为释放状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发按键按下保持, 然后变化为释放状态
  - false: 未触发按键按下保持, 然后变化为释放状态。

## wasReleaseFor

**函数原型:**

```cpp
bool wasReleaseFor(std::uint32_t ms)
```

**功能说明:**

- 判断按键是否按下超过指定超时时间, 释放后触发

**传入参数:**

- uint32_t ms：
  - 按键释放超时时间 ms

**返回值:**

- bool:
  - true: 触发按键释放超过超时时间
  - false: 未触发

## setDebounceThresh

**函数原型:**

```cpp
void setDebounceThresh(std::uint32_t msec)
```

**功能说明:**

- 设置按键消抖阈值

**传入参数:**

- uint32_t msec:
  - 按键消抖时间 ms

**返回值:**

- null

**函数原型:**

## setHoldThresh

**函数原型:**

```cpp
void setHoldThresh(std::uint32_t msec)
```

**功能说明:**

- 设置 Hold 按键保持触发时间阈值

**传入参数:**

- uint32_t msec:
  - Hold 触发阈值 ms

**返回值:**

- null

## setRawState

**函数原型:**

```cpp
void setRawState(std::uint32_t msec, bool press);
```

**功能说明:**

- 向对象中传入当前时间与按键电平, 用于更新判断按键的事件。

**传入参数:**

- uint32_t msec：
  - 当前时间 ms

- bool press:
  - 按键引脚电平

**返回值:**

- null

## setState

**函数原型:**

```cpp
void setState(std::uint32_t msec, button_state_t state);
```

**功能说明:**

- 向对象中传入按键状态, 用于更新判断按键的事件。

**传入参数:**

- uint32_t msec：
  - 当前时间 ms

- button_state_t state
  - 按键状态

**返回值:**

- null

## getState

**函数原型:**

```cpp
button_state_t getState(void)
```

**功能说明:**

- 获取当前按键状态

**传入参数:**

- null

**返回值:**

- button_state_t:
  - state_nochange: 状态无更新
  - state_clicked: 按键单击
  - state_hold: 按键保持
  - state_decide_click_count: 按键计数

## lastChange

**函数原型:**

```cpp
std::uint32_t lastChange(void) 
```

**功能说明:**

- 获取上一次状态更新的时间

**传入参数:**

- null

**返回值:**

- uint32_t: 上一次状态更新的时间 ms

## getDebounceThresh

**函数原型:**

```cpp
std::uint32_t getDebounceThresh(void)
```

**功能说明:**

- 获取消除抖动时间阈值

**传入参数:**

- null

**返回值:**

- uint32_t: 消除抖动时间阈值 ms

## getHoldThresh

**函数原型:**

```cpp
std::uint32_t getHoldThresh(void)
```

**功能说明:**

- 获取当前 Hold 触发阈值

**传入参数:**

- null

**返回值:**

- uint32_t: 触发阈值 ms

## getUpdateMsec

**函数原型:**

```cpp
std::uint32_t getUpdateMsec(void)
```

**功能说明:**

- 获取上一次执行状态检测的时间

**传入参数:**

- null

**返回值:**

- uint32_t: 上一次执行状态检测的时间 ms
