# Unit Roller485/RollerCAN 电机位置校准

#>编码器校准:|Unit Roller485/RollerCAN内部的磁编码器在出厂前经过了校准, 若用户在一些特殊情况对电机进行了拆解, 电机可能会出现无法正常起转的情况。出现该情况后, 可参考以下教程对电机编码器重新校准。

## 准备工作

1.长按底部按键A, 然后连接Grove线为设备供电

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/roller485/roller485_i2c_port_01.jpg" width="50%">

2.进入配置菜单, 通过旋转电机切换选项, 将设备配置为I2C工作模式。

<img src="https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/static/assets/img/guide/motor_ctl/roller485/roller485_i2c_mode_01.jpg" width="50%">

3.连接Unit Roller485/RollerCAN至M5主控, 并参考下方指引烧录校准程序。

## 操作校准

- 烧录校准程序[M5Unit-Roller - encoder_calibration](https://github.com/m5stack/M5Unit-Roller/blob/main/examples/i2c/encoder_calibration/encoder_calibration.ino)至你的主控设备, 若是使用其他的控制器设备可根据实际使用的`GPIO`进行调整`RollerI2C.begin(&Wire, 0x64, SDA, SCL, 400000)`

```cpp line-num
/*
 *SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
 *
 *SPDX-License-Identifier: MIT
 */
#include "unit_rolleri2c.hpp"
#include <M5Unified.h>

#define ROLLER_CALIBRATION_DELAY 10000

UnitRollerI2C RollerI2C;  // Create a UNIT_ROLLERI2C object

uint8_t is_roller_valid             = 0;
uint8_t is_roller_calibrated        = 0;
uint32_t roller_start_delay_counter = 0;

void setup()
{
    M5.begin();
    if (RollerI2C.begin(&Wire, 0x64, 21, 22, 400000)) {
        is_roller_valid            = 1;
        roller_start_delay_counter = millis();
    }
}

void loop()
{
    if (is_roller_valid) {
        if (millis() - roller_start_delay_counter < ROLLER_CALIBRATION_DELAY) {
            printf("Calibration will start after %dS\n",
                   (roller_start_delay_counter - (millis() - roller_start_delay_counter)) / 1000);
        } else {
            if (!is_roller_calibrated) {
                printf("Start encoder calibration\n");
                RollerI2C.setOutput(0);
                delay(100);
                RollerI2C.startAngleCal();
                delay(100);
                printf("Calibrationing...\n");
                while (RollerI2C.getCalBusyStatus()) {
                    printf("Calibrationing...\n");
                }
                RollerI2C.updateAngleCal();
                printf("Encoder calibration done\n");
                delay(500);
                RollerI2C.setOutput(0);
                RollerI2C.setMode(ROLLER_MODE_SPEED);
                RollerI2C.setSpeed(240000);
                RollerI2C.setSpeedMaxCurrent(100000);
                RollerI2C.setOutput(1);
                is_roller_calibrated = 1;
            }
        }
    } else {
        printf("No roller485 dectected\n");
    }
}
```
