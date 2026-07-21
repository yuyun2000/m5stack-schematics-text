# StackChan Touch 触摸屏

StackChan 屏幕触摸相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5CoreS3
- M5Unified 库版本 >= 0.2.11

```cpp line-num
#include <M5Unified.h>

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);

    M5.Display.setTextColor(GREEN);
    M5.Display.setTextDatum(middle_center);
    M5.Display.setFont(&fonts::Orbitron_Light_24);
    M5.Display.setTextSize(1);

    M5.Display.drawString("Touch Test", M5.Display.width() / 2,
                              M5.Display.height() / 2);
}

int prev_x = -1;
int prev_y = -1;

static m5::touch_state_t prev_state;

void loop(void) {
    M5.update();

    auto t = M5.Touch.getDetail();
    if (prev_state != t.state) {
        prev_state                                  = t.state;
        static constexpr const char* state_name[16] = {
            "none", "touch", "touch_end", "touch_begin",
            "___",  "hold",  "hold_end",  "hold_begin",
            "___",  "flick", "flick_end", "flick_begin",
            "___",  "drag",  "drag_end",  "drag_begin"};
        M5_LOGI("%s", state_name[t.state]);
        M5.Display.fillRect(0, 0, M5.Display.width(), 140, BLACK);

        M5.Display.drawString(state_name[t.state],
                                  M5.Display.width() / 2,
                                  M5.Display.height() / 2 - 30);
    }
    if (prev_x != t.x || prev_y != t.y) {
        M5.Display.fillRect(0, 140, M5.Display.width(), 100, BLACK);
        M5.Display.drawString(
            "X:" + String(t.x) + " / " + "Y:" + String(t.y),
            M5.Display.width() / 2, 200);
        prev_x = t.x;
        prev_y = t.y;
        M5.Display.fillCircle(prev_x, prev_y, 4, GREEN);
    }
}
```

烧录成功后，您可以通过触摸 StackChan 的屏幕来与设备进行交互。当您触摸屏幕时，屏幕上会显示当前的触摸状态（如 touch、hold、flick、drag 等）以及触摸点的坐标信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/StackChan_Touch.jpg" width="40%">

## API

StackChan 屏幕触摸部分使用了M5Unified库中的`Touch_Class`, 更多相关的API可以参考下方文档:

- [M5Unified - Touch Class](/zh_CN/arduino/m5unified/touch_class)

