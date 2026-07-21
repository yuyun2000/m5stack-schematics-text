# StickC-Plus2 IMU 姿态传感器

M5StickCPlus2 IMU 姿态传感器输入相关 API 与案例程序。

## 案例程序

```cpp line-num
#include "M5StickCPlus2.h"

void setup() {
    auto cfg = M5.config();
    StickCP2.begin(cfg);
    StickCP2.Display.setRotation(1);
    StickCP2.Display.setTextColor(GREEN);
    StickCP2.Display.setTextDatum(middle_center);
    StickCP2.Display.setFont(&fonts::FreeSansBold9pt7b);
    StickCP2.Display.setTextSize(1);
}

void loop(void) {
    auto imu_update = StickCP2.Imu.update();
    if (imu_update) {
        StickCP2.Display.setCursor(0, 40);
        StickCP2.Display.clear();  // Delay 100ms 延迟100ms

        auto data = StickCP2.Imu.getImuData();

        // The data obtained by getImuData can be used as follows.
        // data.accel.x;      // accel x-axis value.
        // data.accel.y;      // accel y-axis value.
        // data.accel.z;      // accel z-axis value.
        // data.accel.value;  // accel 3values array [0]=x / [1]=y / [2]=z.

        // data.gyro.x;      // gyro x-axis value.
        // data.gyro.y;      // gyro y-axis value.
        // data.gyro.z;      // gyro z-axis value.
        // data.gyro.value;  // gyro 3values array [0]=x / [1]=y / [2]=z.

        // data.value;  // all sensor 9values array [0~2]=accel / [3~5]=gyro /
        //              // [6~8]=mag

        Serial.printf("ax:%f  ay:%f  az:%f\r\n", data.accel.x, data.accel.y,
                      data.accel.z);
        Serial.printf("gx:%f  gy:%f  gz:%f\r\n", data.gyro.x, data.gyro.y,
                      data.gyro.z);

        StickCP2.Display.printf("IMU:\r\n");
        StickCP2.Display.printf("%0.2f %0.2f %0.2f\r\n", data.accel.x,
                                data.accel.y, data.accel.z);
        StickCP2.Display.printf("%0.2f %0.2f %0.2f\r\n", data.gyro.x,
                                data.gyro.y, data.gyro.z);
    }
    delay(100);
}
```

## API

M5StickCPlus2 库基于 M5Unified 库实现, IMU 部分使用了 M5Unified 库中的`IMU_Class`, 更多按键相关的 API 可以参考下方文档:

- [M5Unified - IMU Class](/zh_CN/arduino/m5unified/imu_class)

## IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/512/IMU-StickC-Plus2.jpg" width="70%">