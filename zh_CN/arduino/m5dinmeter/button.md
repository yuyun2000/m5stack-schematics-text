# DinMeter 按键

DinMeter 按键相关案例程序。

- 打开示例程序`button`,上传代码

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/quickstart_arduino_dinmeter_install_library_button.png" width="70%">


## 案例程序

```cpp line-num
/**
 * @file button.ino
 * @author SeanKwok (shaoxiang@m5stack.com)
 * @brief M5DinMeter Button Test
 * @version 0.1
 * @date 2024-03-07
 *
 *
 * @Hardwares: M5DinMeter
 * @Platform Version: Arduino M5Stack Board Manager v2.1.1
 * @Dependent Library:
 * M5GFX: https://github.com/m5stack/M5GFX
 * M5Unified: https://github.com/m5stack/M5Unified
 */

#include "M5DinMeter.h"

void setup() {
    auto cfg = M5.config();
    DinMeter.begin(cfg, true);
    DinMeter.Display.setRotation(1);
    DinMeter.Display.setTextColor(GREEN);
    DinMeter.Display.setTextDatum(middle_center);
    DinMeter.Display.setTextFont(&fonts::Orbitron_Light_32);
    DinMeter.Display.setTextSize(1);
    DinMeter.Display.drawString("Button Test", DinMeter.Display.width() / 2,
                                DinMeter.Display.height() / 2);
}

void loop() {
    DinMeter.update();
    if (DinMeter.BtnA.wasPressed()) {
        DinMeter.Speaker.tone(8000, 20);
        DinMeter.Display.clear();
        DinMeter.Display.drawString("Pressed", DinMeter.Display.width() / 2,
                                    DinMeter.Display.height() / 2);
    }
    if (DinMeter.BtnA.wasReleased()) {
        DinMeter.Speaker.tone(8000, 20);
        DinMeter.Display.clear();
        DinMeter.Display.drawString("Released", DinMeter.Display.width() / 2,
                                    DinMeter.Display.height() / 2);
    }
}

```

上传完成就可以看到下面的效果了

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/500/K134_button.jpg" width="30%">
