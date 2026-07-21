# M5Unified Touch Class

- [Touch Class](#touch-class)
  - [begin](#begin)
  - [update](#update)
  - [isEnabled](#isenabled)
  - [end](#end)
  - [getCount](#getcount)
  - [getDetail](#getdetail)
  - [getTouchPointRaw](#gettouchpointraw)
  - [setHoldThresh](#setholdthresh)
  - [setFlickThresh](#setflickthresh)
- [Touch Detail](#touch-detail)
  - [deltaX](#deltax)
  - [deltaY](#deltay)
  - [distanceX](#distancex)
  - [distanceY](#distancey)
  - [isPressed](#ispressed)
  - [wasPressed](#waspressed)
  - [wasClicked](#wasclicked)
  - [isReleased](#isreleased)
  - [wasReleased](#wasreleased)
  - [isHolding](#isholding)
  - [wasHold](#washold)
  - [wasFlickStart](#wasflickstart)
  - [isFlicking](#isflicking)
  - [wasFlicked](#wasflicked)
  - [wasDragStart](#wasdragstart)
  - [isDragging](#isdragging)
  - [wasDragged](#wasdragged)
  - [getClickCount](#getclickcount)

## Touch Class

## begin

**函数原型:**

```cpp
void begin(m5gfx::LGFX_Device* gfx);
```

**功能说明:**

- 初始化 Touch 实例

**传入参数:**

- m5gfx::LGFX_Device* gfx:
  - 屏幕设备实例指针

**返回值:**

- bool:
  - true: 初始化成功
  - false: 初始化失败

## update

**函数原型:**

```cpp
void update(std::uint32_t msec);
```

**功能说明:**

- 更新 Touch 状态

**传入参数:**

- uint32_t msec:
  - 更新时间

**返回值:**

- null

## isEnabled

**函数原型:**

```cpp
bool isEnabled(void);
```

**功能说明:**

- 判断 Touch 是否初始化

**传入参数:**

- null

**返回值:**

- bool:
  - true: Touch 已经初始化
  - false: Touch 未初始化

## end

**函数原型:**

```cpp
void end(void);
```

**功能说明:**

- Touch 屏幕设备实例指针至为空, 逆初始化。

**传入参数:**

- null

**返回值:**

- null

## getCount

**函数原型:**

```cpp
std::uint8_t getCount(void);
```

**功能说明:**

- 获取当前屏幕触点的数量

**传入参数:**

- null

**返回值:**

- uint8_t points:
  - 屏幕触点的数量

## getDetail

**函数原型:**

```cpp
const touch_detail_t& getDetail(std::size_t index = 0);
```

**功能说明:**

- 获取触摸点详细信息

**传入参数:**

- size_t index:
  - 获取触摸点的索引值

**返回值:**

- touch_detail_t detail:
  - 屏幕触摸点详细信息, 包含坐标, 偏移, 触摸点事件等。详细参考[Touch Detail](#touch-detail)部分说明。

## getTouchPointRaw

**函数原型:**

```cpp
inline const m5gfx::touch_point_t& getTouchPointRaw(std::size_t index = 0) const { return _touch_raw[index < _detail_count ? index : 0]; }
```

**功能说明:**

- 获取触摸点原始信息

**传入参数:**

- size_t index:
  - 获取触摸点的索引值

**返回值:**

- touch_point_t point:
  - 屏幕触摸点原始信息, 包含坐标, id。

## setHoldThresh

**函数原型:**

```cpp
void setHoldThresh(std::uint16_t msec) { _msecHold = msec; }
```

**功能说明:**

- 设置触摸保持触发时间阈值

**传入参数:**

- uint16_t msec:
  - Hold 触发阈值 ms

**返回值:**

- null

## setFlickThresh

**函数原型:**

```cpp
void setFlickThresh(std::uint16_t distance) { _flickThresh = distance; }
```

**功能说明:**

- 设置触摸消抖阈值

**传入参数:**

- uint16_t distance:
  - 触摸偏移消抖阈值

**返回值:**

- null

## Touch Detail

**函数原型:**

```cpp line-num
    struct touch_detail_t : public m5gfx::touch_point_t
    {
      union
      { /// Previous point
        point_t prev;
        struct
        {
          std::int16_t prev_x;
          std::int16_t prev_y;
        };
      };
      union
      { /// Flick start point
        point_t base;
        struct
        {
          std::int16_t base_x;
          std::int16_t base_y;
        };
      };

      std::uint32_t base_msec;
      touch_state_t state = touch_state_t::none;
      std::uint8_t click_count = 0;

      inline int deltaX(void) const { return x - prev_x; }
      inline int deltaY(void) const { return y - prev_y; }
      inline int distanceX(void) const { return x - base_x; }
      inline int distanceY(void) const { return y - base_y; }
      inline bool isPressed(void) const { return state & touch_state_t::mask_touch; };
      inline bool wasPressed(void) const { return state == touch_state_t::touch_begin; };
      inline bool wasClicked(void) const { return state == touch_state_t::touch_end; };
      inline bool isReleased(void) const { return !(state & touch_state_t::mask_touch); };
      inline bool wasReleased(void) const { return (state & (touch_state_t::mask_touch | touch_state_t::mask_change)) == touch_state_t::mask_change; };
      inline bool isHolding(void) const { return (state & (touch_state_t::mask_touch | touch_state_t::mask_holding)) == (touch_state_t::mask_touch | touch_state_t::mask_holding); }
      inline bool wasHold(void) const { return state == touch_state_t::hold_begin; }
      inline bool wasFlickStart(void) const { return state == touch_state_t::flick_begin; }
      inline bool isFlicking(void) const { return (state & touch_state_t::drag) == touch_state_t::flick; }
      inline bool wasFlicked(void) const { return state == touch_state_t::flick_end; }
      inline bool wasDragStart(void) const { return state == touch_state_t::drag_begin; }
      inline bool isDragging(void) const { return (state & touch_state_t::drag) == touch_state_t::drag; }
      inline bool wasDragged(void) const { return state == touch_state_t::drag_end; }
      inline std::uint8_t getClickCount(void) const { return click_count; }
    };
```

## deltaX

**函数原型:**

```cpp
inline int deltaX(void) const { return x - prev_x; }
```

**功能说明:**

- 获取触摸点 X 坐标相对于上一次采样的偏移

**传入参数:**

- null

**返回值:**

- int deltaX:
  - 触摸点 X 坐标相对于上一次采样的偏移

## deltaY

**函数原型:**

```cpp
inline int deltaY(void) const { return y - prev_y; }
```

**功能说明:**

- 获取触摸点 Y 坐标相对于上一次采样的偏移

**传入参数:**

- null

**返回值:**

- int deltaY:
  - 触摸点 Y 坐标相对于上一次采样的偏移

## distanceX

**函数原型:**

```cpp
inline int distanceX(void) const { return x - base_x; }
```

**功能说明:**

- 获取触摸点 X 坐标相对于触摸起点采样的偏移

**传入参数:**

- null

**返回值:**

- int distanceX:
  - 触摸点 X 坐标相对于上一次采样的偏移

## distanceY

**函数原型:**

```cpp
inline int distanceY(void) const { return y - base_y; }
```

**功能说明:**

- 获取触摸点 Y 坐标相对于触摸起点采样的偏移

**传入参数:**

- null

**返回值:**

- int distanceY:
  - 触摸点 X 坐标相对于上一次采样的偏移

## isPressed

**函数原型:**

```cpp
inline bool isPressed(void) const { return state & touch_state_t::mask_touch; };
```

**功能说明:**

- 判断触摸点是否按下

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触摸点处于按下状态
  - false: 触摸点不处于按下状态

## wasPressed

**函数原型:**

```cpp
inline bool wasPressed(void) const { return state == touch_state_t::touch_begin; };
```

**功能说明:**

- 判断触摸点由释放状态, 变化为按下状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发触摸点由释放状态变化为按下状态
  - false: 未触发触摸点由释放状态变化为按下状态

## wasClicked

**函数原型:**

```cpp
inline bool wasClicked(void) const { return state == touch_state_t::touch_end; };
```

**功能说明:**

- 判断触摸点是否点击

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发触摸点点击
  - false: 未触发触摸点点击

## isReleased

**函数原型:**

```cpp
inline bool isReleased(void) const { return !(state & touch_state_t::mask_touch); };
```

**功能说明:**

- 判断触摸点是否处于释放状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触摸点处于释放状态
  - false: 触摸点不处于释放状态

## wasReleased

**函数原型:**

```cpp
inline bool wasReleased(void) const { return (state & (touch_state_t::mask_touch | touch_state_t::mask_change)) == touch_state_t::mask_change; };
```

**功能说明:**

- 判断触摸点由按下状态, 变化为释放状态

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发触摸点由按下状态变化为释放状态
  - false: 未触发触摸点由按下状态变化为释放状态

## isHolding

**函数原型:**

```cpp
inline bool isHolding(void) const { return (state & (touch_state_t::mask_touch | touch_state_t::mask_holding)) == (touch_state_t::mask_touch | touch_state_t::mask_holding); }
```

**功能说明:**

- 判断触摸点当前是否按下保持

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触摸点当前处于按下保持状态
  - false: 触摸点当前不处于按下保持状态

## wasHold

**函数原型:**

```cpp
inline bool wasHold(void) const { return state == touch_state_t::hold_begin; }
```

**功能说明:**

- 判断触摸点是否保持按下, 默认判断阈值时间为 500ms

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发触摸点保持
  - false: 未触发触摸点保持

## wasFlickStart

**函数原型:**

```cpp
inline bool wasFlickStart(void) const { return state == touch_state_t::flick_begin; }
```

**功能说明:**

- 判断触摸滑动动作开始

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发触摸滑动动作开始
  - false: 未触发

## isFlicking

**函数原型:**

```cpp
inline bool isFlicking(void) const { return (state & touch_state_t::drag) == touch_state_t::flick; }
```

**功能说明:**

- 判断触摸滑动动作进行中

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发触摸滑动动作进行中
  - false: 未触发

## wasFlicked

**函数原型:**

```cpp
inline bool wasFlicked(void) const { return state == touch_state_t::flick_end; }
```

**功能说明:**

- 判断触摸滑动动作结束

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发触摸滑动动作结束
  - false: 未触发

## wasDragStart

**函数原型:**

```cpp
inline bool wasDragStart(void) const { return state == touch_state_t::drag_begin; }
```

**功能说明:**

- 判断触摸拖拽动作开始, 触发 hold 后移动触发该事件。

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发拖拽动作开始
  - false: 未触发

## isDragging

**函数原型:**

```cpp
inline bool isDragging(void) const { return (state & touch_state_t::drag) == touch_state_t::drag; }
```

- 判断触摸拖拽进行中

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发拖拽动作进行中
  - false: 未触发

## wasDragged

**函数原型:**

```cpp
inline bool wasDragged(void) const { return state == touch_state_t::drag_end; }
```

**功能说明:**

- 判断触摸拖拽动作结束

**传入参数:**

- null

**返回值:**

- bool:
  - true: 触发拖拽动作结束
  - false: 未触发

## getClickCount

**函数原型:**

```cpp
inline std::uint8_t getClickCount(void) const { return click_count; }
```

**功能说明:**

- 获取连续触摸点击次数

**传入参数:**

- null

**返回值:**

- uint8_t count:
  - 连续触摸点击次数
