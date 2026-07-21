# Cardputer-Adv IMU 六轴姿态传感器

Cardputer-Adv IMU 六轴姿态传感器相关 API 与案例程序，仅适用于 Cardputer-Adv，不适用于 Cardputer。

## 案例程序

### 编译要求

- M5Stack 板管理版本 >= 3.2.2
- 开发板选项 = M5Cardputer
- M5Cardputer 库版本 >= 1.1.0
- M5Unified 库版本 >= 0.2.8
- M5GFX 库版本 >= 0.2.10

```cpp line-num
#include <M5Cardputer.h>

m5::imu_data_t imuData;

void setup() {
  auto cfg = M5.config();
  M5Cardputer.begin(cfg, true);  // enableKeyboard
  M5Cardputer.Display.setFont(&fonts::FreeMonoBold9pt7b);

  M5Cardputer.Display.clear();
  M5Cardputer.Display.setCursor(0, 0);
  M5Cardputer.Display.print("    IMU Live Data");
}

void loop() {
  // Use M5 for Imu class, not M5Cardputer
  M5.Imu.update();
  imuData = M5.Imu.getImuData();

  M5Cardputer.Display.setCursor(0, 30);
  M5Cardputer.Display.println("      Acc    Gyr");

  M5Cardputer.Display.printf("  x  % 4.2f  % 4.2f\n", imuData.accel.x, imuData.gyro.x);
  M5Cardputer.Display.printf("  y  % 4.2f  % 4.2f\n", imuData.accel.y, imuData.gyro.y);
  M5Cardputer.Display.printf("  z  % 4.2f  % 4.2f\n", imuData.accel.z, imuData.gyro.z);

  delay(100);
}
```

运行效果：

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/Arduino_IMU.jpg" width="70%">

## API

Cardputer-Adv IMU 六轴姿态传感器部分驱动使用了`M5Unified`库中的`Imu_Class`，更多相关的 API 可以参考下方文档：

- [M5Unified - Imu Class](/zh_CN/arduino/m5unified/imu_class)

## IMU 三轴方向示意图

<img src="https://m5stack-doc.oss-cn-shenzhen.aliyuncs.com/1178/IMU-Cardputer-Adv.jpg" width="70%">