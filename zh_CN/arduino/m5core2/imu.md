# Core2 IMU 六轴姿态传感器

Core2 IMU 姿态传感器输入相关 API 与案例程序。

## 案例程序

```cpp line-num
#include <M5Unified.h>

void setup(void) {
    auto cfg = M5.config();
    M5.begin(cfg);
    M5.Display.setTextFont(&fonts::Font4);
    M5.Display.setTextSize(1);
}

void loop(void) {
    auto imu_update = M5.Imu.update();
    if (imu_update) {
        M5.Display.setCursor(0, 24);
        M5.Display.clear(TFT_WHITE);

        auto ImuData = M5.Imu.getImuData();

        // The ImuData obtained by getImuData can be used as follows.
        ImuData.accel.x;      // accel x-axis value.
        ImuData.accel.y;      // accel y-axis value.
        ImuData.accel.z;      // accel z-axis value.
        ImuData.accel.value;  // accel 3values array [0]=x / [1]=y / [2]=z.

        ImuData.gyro.x;      // gyro x-axis value.
        ImuData.gyro.y;      // gyro y-axis value.
        ImuData.gyro.z;      // gyro z-axis value.
        ImuData.gyro.value;  // gyro 3values array [0]=x / [1]=y / [2]=z.

        M5.Display.setTextColor(TFT_BLACK);
        M5.Display.printf("IMU:\r\n");
        M5.Display.printf("ax:%6.2f  ay:%6.2f  az:%6.2f\r\n", ImuData.accel.x, ImuData.accel.y, ImuData.accel.z);
        M5.Display.printf("gx:%6.2f  gy:%6.2f  gz:%6.2f\r\n", ImuData.gyro.x, ImuData.gyro.y, ImuData.gyro.z);
    }
    delay(500);
}           
```

该程序将在屏幕上显示姿态传感器各轴信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/core2_arduino_imu.jpg" width="50%">

## API

Core2 IMU 部分使用了 M5Unified 库中的`IMU_Class`, 更多按键相关的 API 可以参考下方文档:

- [M5Unified - IMU Class](/zh_CN/arduino/m5unified/imu_class)

## IMU 三轴方向示意图

- Core2
  <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/644/IMU-Core2.jpg" width="50%">

- Core2 v1.3
  <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1231/IMU-Core2-v1.3.jpg" width="50%">

- Core2 For AWS
  <img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/646/IMU-Core2-For-AWS.jpg" width="50%">
