# Tab5 IMU 六轴姿态传感器

Tab5 六轴姿态传感器相关 API 与案例程序。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.0
- 开发板选项 = M5Tab5
- M5Unified 库版本 >= 0.2.17
- M5GFX 库版本 >= 0.2.22

```cpp line-num
#include <M5Unified.h>
#include <M5GFX.h>

m5::imu_data_t imuData;

void setup() {
  M5.begin();
  M5.Display.setRotation(3);
  M5.Display.setTextDatum(top_center);
  M5.Display.setFont(&fonts::FreeMonoBold24pt7b);
  M5.Display.clear(WHITE);
  M5.Display.drawString("IMU Realtime Data", M5.Lcd.width() / 2, 0);
}

void loop() {
  M5.Imu.update();
  imuData = M5.Imu.getImuData();

  M5.Display.setCursor(0, 100);
  M5.Display.printf(" Acc X = %6.2f  \n", imuData.accel.x);
  M5.Display.printf(" Acc Y = %6.2f  \n", imuData.accel.y);
  M5.Display.printf(" Acc Z = %6.2f  \n\n", imuData.accel.z);

  M5.Display.printf(" Gyr X = %6.2f  \n", imuData.gyro.x);
  M5.Display.printf(" Gyr Y = %6.2f  \n", imuData.gyro.y);
  M5.Display.printf(" Gyr Z = %6.2f  \n", imuData.gyro.z);

  delay(1000);
}
```

该程序会显示实时的加速度计、陀螺仪读数，每秒钟刷新一次。

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/Tab5_Arduino_IMU.jpg" width="50%">

## API

Tab5 姿态传感器部分使用了 `M5Unified` 库中的 `Imu_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - IMU Class](/zh_CN/arduino/m5unified/imu_class)

## IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1132/IMU-Tab5.jpg" width="70%">
