# StickS3 IMU 六轴姿态传感器

StickS3 IMU 姿态传感器输入相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.5
- 开发板选项 = M5StickS3
- M5Unified 库版本 >= 0.2.12
- M5GFX 库版本 >= 0.2.18

```cpp line-num
#include <M5Unified.h>

void setup(void)
{
    M5.begin();
    M5.Lcd.setTextFont(&fonts::FreeMonoBold9pt7b);
}

void loop(void)
{
    auto imu_update = M5.Imu.update();
    if (imu_update) {
        M5.Lcd.setCursor(0, 5);
        M5.Lcd.clear();

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

        M5.Lcd.printf("IMU:\n\n");
        M5.Lcd.printf(" ax:%6.2f\n ay:%6.2f\n az:%6.2f\r\n", ImuData.accel.x, ImuData.accel.y, ImuData.accel.z);
        M5.Lcd.println();
        M5.Lcd.printf(" gx:%6.2f\n gy:%6.2f\n gz:%6.2f\r\n", ImuData.gyro.x, ImuData.gyro.y, ImuData.gyro.z);
    }
    delay(500);
}
```

该程序将在屏幕上显示姿态传感器各轴信息。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/StickS3_Arduino_imu.jpg" width="40%">

## API

StickS3 IMU 部分使用了 `M5Unified` 库中的 `IMU_Class` ,  更多按键相关的 API 可以参考下方文档:

- [M5Unified - IMU Class](/zh_CN/arduino/m5unified/imu_class)

## IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1207/IMU-StickS3.jpg" width="70%">