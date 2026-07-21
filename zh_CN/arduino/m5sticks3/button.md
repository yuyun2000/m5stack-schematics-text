# StickS3 Button 按键

StickS3 按键输入相关 API 与案例程序。

#>注意事项: | 使用时需要在主循环中包含`M5.update()`函数用于读取状态更新且尽可能减少阻塞情况, 否则可能无法及时获取的按键变化状态。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5StickS3
- M5Unified 库版本 >= 0.2.12
- M5GFX 库版本 >= 0.2.18

```cpp line-num
#include "M5Unified.h"
#include "M5GFX.h"

static int32_t w;
static int32_t h;
static bool drawed = false;

void setup()
{
    auto cfg = M5.config();
    M5.begin(cfg);
    
    M5.Lcd.setRotation(1);
    w = M5.Lcd.width();
    h = M5.Lcd.height();
    M5.Lcd.setFont(&fonts::FreeMonoBold12pt7b);
    M5.Lcd.drawString("Button Released", 0, 0);
}

void loop()
{
    M5.update();
    if(M5.BtnA.isPressed() || M5.BtnB.isPressed())
    {
        if (!drawed){
            M5.Lcd.clear();
        }
        M5.Lcd.drawString("Button  Detail:", 0, 0);
        if (M5.BtnA.isPressed()) {
            M5.Lcd.drawString("ButtonA Pressed", 0, 30);
        }
        else if (M5.BtnB.isPressed()) {
            M5.Lcd.drawString("ButtonB Pressed", 0, 60);
        }
        drawed = true;
    }
    else if (drawed){
        drawed = false;
        M5.Lcd.clear();
        M5.Lcd.drawString("Button Released", 0, 0);
    } 
    vTaskDelay(1);
} 
```

该程序效果为按动按键，屏幕上会显示具体按键状态。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_button_release.jpg" width="30%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_buttonA.jpg" width="30%"><img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_buttonB.jpg" width="30%">

## API

StickS3 按键部分使用了M5Unified库中的`Button_Class`, 更多按键相关的API可以参考下方文档:

- [M5Unified - Button Class](/zh_CN/arduino/m5unified/button_class)

