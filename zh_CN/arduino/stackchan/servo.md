# StackChan Servo 舵机

StackChan 舵机控制案例程序。

## 原点校准

```cpp line-num
#include <M5StackChan.h>

namespace {

constexpr uint16_t kBackgroundColor          = TFT_BLACK;
constexpr uint16_t kBorderColor              = TFT_WHITE;
constexpr uint16_t kTopButtonColor           = 0x39C7;
constexpr uint16_t kTopButtonPressedColor    = 0x2204;
constexpr uint16_t kBottomButtonColor        = 0x03EF;
constexpr uint16_t kBottomButtonPressedColor = 0x01E8;
constexpr uint16_t kTextColor                = TFT_WHITE;

enum class ButtonZone {
    None,
    SetHome,
    GoHome,
};

ButtonZone pressed_zone = ButtonZone::None;

ButtonZone getButtonZone(const int16_t y, const int16_t height)
{
    return y < (height / 2) ? ButtonZone::SetHome : ButtonZone::GoHome;
}

void drawButton(const int16_t x, const int16_t y, const int16_t w, const int16_t h, const uint16_t color,
                const char* line_1, const char* line_2)
{
    auto& display = M5StackChan.Display();

    display.fillRect(x, y, w, h, color);
    display.drawRect(x, y, w, h, kBorderColor);

    display.setTextDatum(middle_center);
    display.setTextColor(kTextColor, color);
    display.setTextSize(2);
    display.drawString(line_1, x + w / 2, y + h / 2 - 12);
    display.drawString(line_2, x + w / 2, y + h / 2 + 12);
}

void drawUi(ButtonZone active_zone)
{
    auto& display          = M5StackChan.Display();
    const int16_t width    = display.width();
    const int16_t height   = display.height();
    const int16_t gap      = 8;
    const int16_t button_x = 8;
    const int16_t button_w = width - button_x * 2;
    const int16_t half_h   = (height - gap) / 2;

    display.startWrite();
    display.fillScreen(kBackgroundColor);
    display.fillRect(0, half_h, width, gap, kBackgroundColor);

    drawButton(button_x, 8, button_w, half_h - 12,
               active_zone == ButtonZone::SetHome ? kTopButtonPressedColor : kTopButtonColor, "set current postion",
               "as home");

    drawButton(button_x, half_h + gap + 4, button_w, height - (half_h + gap + 12),
               active_zone == ButtonZone::GoHome ? kBottomButtonPressedColor : kBottomButtonColor, "move to", "home");

    display.endWrite();
}

}  // namespace

void setup()
{
    /* Init StackChan */
    M5StackChan.begin();

    /* Setup display */
    M5StackChan.Display().setTextScroll(false);
    drawUi(ButtonZone::None);
}

void loop()
{
    M5StackChan.update();
    auto& display               = M5StackChan.Display();
    const int16_t screen_height = display.height();
    int16_t touch_x             = 0;
    int16_t touch_y             = 0;
    const bool touching         = display.getTouch(&touch_x, &touch_y);

    if (touching) {
        const ButtonZone current_zone = getButtonZone(touch_y, screen_height);
        if (current_zone != pressed_zone) {
            pressed_zone = current_zone;
            drawUi(pressed_zone);
        }
    } else if (pressed_zone != ButtonZone::None) {
        const ButtonZone released_zone = pressed_zone;
        pressed_zone                   = ButtonZone::None;
        drawUi(ButtonZone::None);

        if (released_zone == ButtonZone::SetHome) {
            M5StackChan.Motion.setCurrentPostionAsHome();
        } else if (released_zone == ButtonZone::GoHome) {
            M5StackChan.Motion.goHome();
        }
    }

    delay(20);
}
```

该程序在屏幕上显示两个按钮，分别用于设置当前舵机位置为原点和回到原点。可以通过触摸屏幕上的按钮来进行操作。当按下并释放“set current position as home”按钮时，当前舵机位置将被设置为原点；当按下并释放“move to home”按钮时，舵机会回到原点位置。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/StackChan_Servo_Calibration.jpg" width="40%">

## 舵机控制

!> 注意 | StackChan 的 Y 轴舵机（垂直方向）的动作角度建议控制在 5 ~ 85°，极限角度下容易出现舵机堵转导致损坏。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/K143-stackchan-note_01.png" width="30%">

```cpp line-num
#include <M5StackChan.h>

int state = 1; 
const int MAX_STATE = 8;

void setup()
{
    /* Init StackChan */
    M5StackChan.begin();
    M5StackChan.Motion.goHome();

    /* Setup display */
    M5StackChan.Display().setTextSize(2);
    M5StackChan.Display().setTextScroll(true);
    M5StackChan.Display().setTextColor(TFT_ORANGE);
    M5StackChan.Display().printf("> Touch the top to start\n");
    M5StackChan.Display().setTextColor(TFT_GREEN);

    // Set to false if high-frequency updates are needed
    // M5StackChan.Motion.setAutoAngleSyncEnabled(false);
}

void loop()
{
    M5StackChan.update();
    if (M5StackChan.TouchSensor.wasPressed()) {
        switch(state){
            /* Angle unit: 10 = 1 degrees, Speed range: 0~1000 */
            /* Range X: -1280 ~ 1280 (-128° ~ 128°), Range Y: 0 ~ 900 (0° ~ 90°) */
            case 1: 
                /* Move X servo to 0°, Y servo to 45° */
                M5StackChan.Motion.move(0, 450);
                M5StackChan.Display().printf("> Turn Y to 45\n");
                break;
            case 2: 
                /* Move X servo to 90° */
                M5StackChan.Motion.moveX(900, 500);
                M5StackChan.Display().printf("> Turn Left\n");
                break;
            case 3:
                /* Move X servo to -90° */
                M5StackChan.Motion.moveX(-900, 500);
                M5StackChan.Display().printf("> Turn Right\n");
                break;
            case 4:
                /* Move Y servo to 90° */
                M5StackChan.Motion.moveY(900, 300);
                M5StackChan.Display().printf("> Look Up\n");
                break;
            case 5:
                /* Move Y servo to 0° */
                M5StackChan.Motion.moveY(0, 300);
                M5StackChan.Display().printf("> Look Down\n");
                break;
            /* Only X axis supports continuous 360° rotation. Y axis does not. */
            /* Velocity range: -1000 ~ 1000 (Negative: CW, Positive: CCW) */
            case 6:
                /* Rotate clockwise */
                M5StackChan.Motion.rotateX(-800);
                M5StackChan.Display().printf("> Rotate clockwise\n");
                delay(2000);
                M5StackChan.Motion.stop();
                break;
            case 7:
                /* Rotate counter-clockwise */
                M5StackChan.Motion.rotateX(800);
                M5StackChan.Display().printf("> Rotate counter-clockwise\n");
                delay(2000);
                M5StackChan.Motion.stop();
                break;
            default:
                M5StackChan.Motion.goHome();
                M5StackChan.Display().printf("> Go home\n");
                break;
        }        

        state++;
        if (state > MAX_STATE) {
            state = 1;
            M5StackChan.Display().setTextColor(TFT_ORANGE);
            M5StackChan.Display().printf("> Touch the top to start\n");
            M5StackChan.Display().setTextColor(TFT_GREEN);
        }
    }
    delay(10);
}
```

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1205/StackChan_Servo_Move.jpg" width="40%">

该程序通过触摸屏幕来控制舵机的运动状态。每次触摸屏幕时，程序会依次执行以下动作：  
1\. 将 X 轴舵机移动到 0°，Y轴舵机移动到45°;  
2\. 将 X 轴舵机移动到 90°（向左转）;  
3\. 将 X 轴舵机移动到 -90°（向右转）;  
4\. 将 Y 轴舵机移动到 90°（向上看）;  
5\. 将 Y 轴舵机移动到 0°（向下看）;  
6\. 以 800 的速度顺时针旋转 X 轴舵机，持续 2 秒后停止;  
7\. 以 800 的速度逆时针旋转 X 轴舵机，持续 2 秒后停止;  
8\. 回到原点位置。